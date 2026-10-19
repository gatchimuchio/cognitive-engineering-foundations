#!/usr/bin/env python3
"""Finite Lean proof-assurance tests. No universal theorem is claimed."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audit-output"
CASEDIR = OUT / "cases"
LOGDIR = OUT / "logs"
TOOLCHAIN = "leanprover/lean4:v4.35.0"

CASES = [
    ("C01_valid", """
def increment (n : Nat) : Nat := n + 1
theorem increment_at_ten : increment 10 = 11 := by decide
#print axioms increment_at_ten
""", True, ["increment_at_ten"]),
    ("C02_spec_mismatch", """
def authenticated : Bool := false
def accessGranted : Bool := true
def claimedCorrectness : Prop := accessGranted = true
theorem acceptedWrongRequirement : claimedCorrectness := by decide
def actualRequirement : Prop :=
  authenticated = false → accessGranted = false
theorem actualRequirementViolated : ¬ actualRequirement := by decide
#print axioms acceptedWrongRequirement
#print axioms actualRequirementViolated
""", True, ["acceptedWrongRequirement", "actualRequirementViolated"]),
    ("C03_custom_axiom", """
axiom falsePremise : False
theorem arbitraryEquality : (1 : Nat) = 2 := False.elim falsePremise
#print axioms arbitraryEquality
""", True, ["falsePremise"]),
    ("C04_sorry", """
theorem unfinishedClaim : (1 : Nat) = 2 := by sorry
#print axioms unfinishedClaim
""", True, ["sorryAx"]),
    ("C05_transitive_sorry", """
theorem unprovedDependency : (1 : Nat) = 2 := by sorry
theorem apparentlyFinished : (1 : Nat) = 2 := unprovedDependency
#print axioms apparentlyFinished
""", True, ["sorryAx"]),
    ("C06_classical", """
theorem classicalExcludedMiddle (p : Prop) : p ∨ ¬p := Classical.em p
#print axioms classicalExcludedMiddle
""", True, ["classicalExcludedMiddle"]),
    ("C07_invalid_equality", """
theorem invalidEquality : (1 : Nat) = 2 := by rfl
""", False, ["error"]),
    ("C08_invalid_requirement", """
def authenticated : Bool := false
def accessGranted : Bool := true
theorem intendedRuleSatisfied :
  authenticated = false → accessGranted = false := by decide
""", False, ["error"]),
    ("C09_same_statement_supported", """
def Safety : Prop := (true = true)
theorem certified : Safety := by decide
#print axioms certified
""", True, ["certified"]),
    ("C10_same_statement_unsupported", """
def Safety : Prop := (true = false)
theorem certified : Safety := by decide
""", False, ["error"]),
    ("C11_lossy_encoding", """
def encode (_ : Bool) : Nat := 0
theorem collapse : encode true = encode false := by rfl
#print axioms collapse
""", True, ["collapse"]),
    ("C12_preserving_encoding", """
def encode (b : Bool) : Bool := b
theorem distinction : encode true ≠ encode false := by decide
#print axioms distinction
""", True, ["distinction"]),
    ("C13_unsupported_assumption", """
def Claim : Prop := (1 : Nat) = 2
axiom externallyCertified : Claim
theorem claimedProof : Claim := externallyCertified
#print axioms claimedProof
""", True, ["externallyCertified"]),
    ("C14_completeness_label", """
def allSymbolsComplete : Prop := True
theorem completeByName : allSymbolsComplete := by trivial
#print axioms completeByName
""", True, ["completeByName"]),
]

PROJECTS = {
    "strict": ("""
def authenticated : Bool := false
def accessGranted : Bool := true
def mistakenProperty : Prop := accessGranted = true
theorem proofOfMistakenProperty : mistakenProperty := by decide
theorem evidenceOfViolation :
  ¬ (authenticated = false → accessGranted = false) := by decide
""", 0),
    "lax": ("""
axiom falsePremise : False
theorem arbitraryEquality : (1 : Nat) = 2 := False.elim falsePremise
""", 1),
    "incomplete": ("""
theorem unprovedClaim : (1 : Nat) = 2 := by sorry
""", 1),
}

def execute(cmd: list[str], cwd: Path, label: str, timeout: int = 240) -> dict:
    record = {"command": cmd, "workdir": str(cwd.relative_to(ROOT)), "status": "NOT_EXECUTED"}
    try:
        cp = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        (LOGDIR / (label + ".stdout.txt")).write_text(cp.stdout, encoding="utf-8")
        (LOGDIR / (label + ".stderr.txt")).write_text(cp.stderr, encoding="utf-8")
        record.update(status="EXECUTED", exit_code=cp.returncode,
                      stdout_file="logs/" + label + ".stdout.txt",
                      stderr_file="logs/" + label + ".stderr.txt")
    except (OSError, subprocess.TimeoutExpired) as exc:
        record["reason"] = str(exc)
    return record

def verdict(run: dict, expected: int | str, tokens: list[str] | None = None) -> str:
    if run.get("status") != "EXECUTED":
        return "FAIL_ENVIRONMENT"
    rc = run["exit_code"]
    matches = rc == expected if isinstance(expected, int) else rc != 0
    if not matches:
        return "REVIEW_REQUIRED"
    if tokens:
        txt = ((OUT / run["stdout_file"]).read_text(encoding="utf-8") +
               (OUT / run["stderr_file"]).read_text(encoding="utf-8"))
        if not all(t.lower() in txt.lower() for t in tokens):
            return "REVIEW_REQUIRED"
    return "PASS_EXPECTED_OBSERVATION"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lake", action="store_true")
    args = parser.parse_args()
    CASEDIR.mkdir(parents=True, exist_ok=True)
    LOGDIR.mkdir(parents=True, exist_ok=True)
    report = {
        "audit": "Lean 4 language/formalization assurance boundary",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "expected_toolchain": TOOLCHAIN,
        "commit": os.environ.get("GITHUB_SHA"), "run_id": os.environ.get("GITHUB_RUN_ID"),
        "evidence": "Finite tests; no proof of universal completeness or incompleteness",
        "case_results": [], "lake_results": []
    }
    (OUT / "lean-toolchain").write_text(TOOLCHAIN + "\n", encoding="utf-8")
    lean = shutil.which("lean")
    lake = shutil.which("lake")
    if lean is None:
        report["overall"] = "FAIL_ENVIRONMENT_NO_LEAN"
        (OUT / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return 2
    v = execute([lean, "--version"], ROOT, "version", 60)
    report["version"] = v
    observed_version = ((OUT / v["stdout_file"]).read_text(encoding="utf-8")
                        if v["status"] == "EXECUTED" else "")
    report["version_verified"] = bool(re.search(r"\b4\.35\.0\b", observed_version))
    all_ok = report["version_verified"]
    for name, src, should_accept, tokens in CASES:
        source = CASEDIR / (name + ".lean")
        source.write_text(textwrap.dedent(src).strip() + "\n", encoding="utf-8")
        run = execute([lean, str(source)], ROOT, name)
        run["expected"] = "ACCEPT" if should_accept else "REJECT"
        run["verdict"] = verdict(run, 0 if should_accept else "nonzero", tokens)
        report["case_results"].append({"case": name, **run})
        all_ok &= run["verdict"] == "PASS_EXPECTED_OBSERVATION"
        print(name, run["verdict"], "exit_code", run.get("exit_code"), flush=True)
    if args.lake:
        if lake is None or sys.platform != "linux":
            report["lake_results"].append({"status": "FAIL_ENVIRONMENT_NO_LAKE_OR_LINUX"})
            all_ok = False
        else:
            for name, (src, expected) in PROJECTS.items():
                proj = OUT / "projects" / name
                proj.mkdir(parents=True, exist_ok=True)
                mod = name.capitalize()
                (proj / (mod + ".lean")).write_text(textwrap.dedent(src).strip() + "\n", encoding="utf-8")
                (proj / "lean-toolchain").write_text(TOOLCHAIN + "\n", encoding="utf-8")
                lakefile = ('name = "lean4_audit_' + name + '"\nversion = "0.1.0"\n'
                            'defaultTargets = ["' + mod + '"]\n\n[[lean_lib]]\nname = "' + mod + '"\n')
                (proj / "lakefile.toml").write_text(lakefile, encoding="utf-8")
                for step, command, expected_code in [
                    ("update", [lake, "update"], 0),
                    ("build", [lake, "build"], 0),
                    ("check", [lake, "check"], expected),
                    ("paranoid", [lake, "check", "--paranoid"], expected),
                ]:
                    run = execute(command, proj, name + "_" + step, 420)
                    run["project"] = name
                    run["step"] = step
                    run["expected_exit"] = expected_code
                    run["verdict"] = verdict(run, expected_code)
                    if run.get("exit_code") == 2 and step in ("check", "paranoid"):
                        run["verdict"] = "FAIL_ENVIRONMENT_OR_CONFIGURATION"
                    report["lake_results"].append(run)
                    all_ok &= run["verdict"] == "PASS_EXPECTED_OBSERVATION"
                    print(name, step, run["verdict"], "exit_code", run.get("exit_code"), flush=True)
                    if step in ("update", "build") and run["verdict"] != "PASS_EXPECTED_OBSERVATION":
                        break
    report["overall"] = "PASS_FINITE_CASE_EXPECTATIONS" if all_ok else "REVIEW_REQUIRED_OR_ENVIRONMENT_FAILURE"
    report["unresolved"] = [
        "Universal completeness of language, glyphs, concepts or symbolic representation not tested",
        "Original problem-to-formalization semantic validity not automatically certified",
        "Truth or legitimacy of axioms and rules not certified by checking a proof term",
        "Shared implementation defects and operational risks not universally eliminated",
    ]
    (OUT / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("SUMMARY", report["overall"])
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
