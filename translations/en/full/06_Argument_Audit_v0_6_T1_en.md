# Trinity Principle Application: Argument Audit
## Auditing Natural-Language Claims Through Coordinates, Relations, Closure, and Stopping

**Source document**: `06_トリニティ原理適用_論証監査_v0_6_ja_en.md`  
**Source version**: v0.6  
**Source revision date**: 2026-10-07  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Source authority**: Japanese Canonical Original (J0)  
**Translation class**: T1 / Aligned Full Translation  
**Translation status**: CURRENT  
**Target language**: English  
**Authority**: Non-authoritative. In any semantic conflict, ambiguity, omission, or translation residual, the Japanese J0 source prevails.  
**Policy**: `TRANSLATION_POLICY.md`

> **Theory-state rule**: The audit structure, X / R / M mapping, PASS / SUSPEND / FAIL, rebuttal audit, evidential strength, and audit result in this paper are current Projections under a specified time, purpose, target, auditor, and context. Audit results are not fixed as permanent labels, and the audit instrument itself is not exempt from audit.

> **Projection responsibility**: If a claim in this version is refuted within the scope, conditions, and definitions declared by this version, that claim is recorded as a FAIL or revision target. The current description is not rescued by saying “the principle itself is different.” Updates are issued as new versions.

---

# Part I. Full English Translation of the Japanese Canonical Original

## One-sentence definition

> **This paper applies the Trinity Principle to the audit of natural-language arguments and provides a public application for checking not only the surface claim but whether target, relations, premises, judgments, and stopping conditions are sufficiently closed for the current purpose.**

This paper is not the Trinity Principle itself.

The layer separation and audit sequence shown here are not fixed as the only or final form of argument audit.

They are a **currently useful application Projection**.

---

# 0. Audit results are provisional too

An audit is not an act in which a permanently fixed external judge eternally rules on a permanently fixed claim.

At the time of audit, at least the following exist as current Projections:

- auditor,
- claimant,
- claim target,
- claim identity,
- context,
- time,
- definitions,
- premises,
- meaning of evidence,
- meaning of rebuttal,
- evaluation criteria,
- scope.

Therefore:

```text
PASS at t
≠ PASS forever
SUSPEND at t
≠ SUSPEND forever
FAIL at t
≠ FAIL forever
```

Provisionality does not mean weakening the present judgment. If the current conditions are sufficiently closed, PASS or FAIL may be issued strongly.

When a case is reopened, the older judgment is not erased. It is retained as an audit record under the coordinates and conditions of its time, and a new judgment is added under the new conditions.

---

# 1. Position of this paper

A natural-language claim may be grammatically complete while remaining unclosed as an auditable claim.

For example:

```text
AI will change the world.
```

can function as a meaningful utterance.

But as an audit target, at least the following remain unresolved:

- What is AI?
- What is the world?
- Who or what is the acting subject?
- What changes, and how?
- When and where does the claim hold?
- What counts as “changed”?

Natural-language argument audit therefore cannot be completed by inspecting surface inference form alone.

This paper applies to audit the representative operational Projection of the Trinity Principle’s triadic minimality:

```text
W_t := (X_t, R_t, M_t)
```

where:

- `X_t`: what is treated as the target at that time,
- `R_t`: how targets relate, change, and are compared,
- `M_t`: what counts as identical, where the boundary lies, what is judged, and where judgment stops.

X / R / M is not the Trinity Principle itself. It is the currently effective operational Projection that maps triadic minimality into argument audit. If another triadic Projection becomes available, that alone does not refute triadic minimality.

---

# 2. Purpose of the audit

The purpose of this paper is not to win arguments.

The purpose is:

> **To determine whether a claim is sufficiently closed, for the current purpose, to proceed to evaluation, adoption/rejection, or rebuttal.**

If it is unclosed, a conclusion is not forced.

A legitimate output is:

```text
SUSPEND
```

If the purpose of the audit changes, the closure conditions required of the same claim may also change.

---

# 3. Minimum audit structure

This paper provisionally divides argument audit into six viewpoints:

```text
0. Coordinates
1. Dynamics
2. Tacit conditions
3. Explicit argument
4. Integration
5. Reservation / SUSPEND
```

This is a decomposition for understanding and operation, not a fixed structure of the world.

It may be integrated, split, extended, or reduced when necessary.

## 3.1 Coordinates

Primarily checks X.

- Who is speaking?
- Who or what acts?
- What is the target?
- When?
- Where?
- For what purpose is the claim made?

If the coordinates are not fixed, the same sentence may be interpreted as referring to different targets.

If the coordinate categories themselves—“who,” “what,” “when,” and so on—are insufficient, the categories are added or re-separated.

## 3.2 Dynamics

Primarily checks R.

- initial state,
- input,
- change,
- intermediate state,
- branching,
- output,
- return,
- stopping.

If only the outcome is stated and the path of change is hidden, causal action cannot be audited.

## 3.3 Tacit conditions

Primarily checks M.

- definitions,
- premises,
- scope,
- judgment criteria,
- uncertainty,
- refutation conditions,
- stopping conditions.

Natural language often invites the reader to fill these in from common sense.

If the completion exists neither in the text nor in the log, it is treated as tacit injection for audit purposes.

## 3.4 Explicit argument

After the preceding layers close, audit the surface argument.

- Is there an inferential leap?
- Do definitions change midstream?
- Are the grounds sufficient for the strength of the conclusion?
- Are causation and correlation confused?
- Are comparison conditions isomorphic?

## 3.5 Integration

Cross the viewpoints and determine whether the claim remains stable as a whole.

A local step may be correct, yet the whole argument may no longer be the same argument if target, premise, or evaluation axis changes partway through.

## 3.6 Reservation / SUSPEND

What cannot be audited, has not been observed, or lies outside the current scope remains visible rather than being erased.

```text
unconfirmed
unobserved
unclosed
different context
awaiting additional observation
```

These are not filled by convenient assertion.

Reservation items are also not forgotten permanently. New observation returns them to the audit target.

---

# 4. Typed audit states

### PASS / ASSERT

Target, relation, judgment, and stopping are sufficiently closed for the current purpose.

PASS does not mean “truth of the world.”

### SUSPEND

Important targets, relations, conditions, or observations are missing, and the conclusion branches. This is epistemic reservation.

### REJECT

Definitions, target, premises, or form fail internally and the claim cannot be accepted as an audit target in its present form.

### OUT-OF-SCOPE

The case is not processed because it crosses a use boundary, disclosure boundary, or ethical boundary, separately from the audit result.

### FAIL

Operational failure such as Runtime failure, API failure, missing logs, or inability to execute.

```text
do not know = SUSPEND
argument/specification is broken = REJECT
will not handle / will not do = OUT-OF-SCOPE
execution system is broken = FAIL
```

These are time-, purpose-, and context-bounded states, not permanent properties of the target world.

---

# 5. Example 1: “AI will change the world”

```text
AI will change the world.
```

### X

- Does “AI” mean a model, an agent, or the entire industry?
- Does “world” mean the economy, technology, institutions, or everyday life?
- Is the acting subject AI itself, or humans and organizations using AI?

### R

- What input,
- through what mechanism,
- changes what,
- toward what state?

### M

- What amount or type of change counts as “changed”?
- What is the time horizon?
- What counts as a counterexample?
- What observation would cause the claim to be updated?

If these remain missing, the audit result is:

```text
SUSPEND
```

The sentence is not meaningless. It is **unclosed for the current audit purpose**.

If target, period, and action are fixed later, the same wording can be reopened as another audit case.

---

# 6. Example 2: a claim whose form alone is orderly

```text
This system increases efficiency.
Systems that increase efficiency are desirable.
Therefore, this system is desirable.
```

On the surface, this resembles a syllogistic structure.

But the argument is unclosed if the following are undefined:

- efficiency for whom,
- how efficiency is defined,
- the time axis,
- whether side effects are included,
- why efficiency connects to desirability.

Formal order is different from closure of target, premise, and evaluation.

If outcome observation later shows that “efficiency” itself is an inappropriate evaluation axis, the audit returns not merely to the value but to the evaluation axis itself.

---

# 7. Rebuttal audit

Rebuttal strength does not mean requiring the same quantity of evidence as the original claim.

First determine the claim type.

| Claim type | Primary refutation / audit conditions |
|---|---|
| Universal proposition | A single valid counterexample within scope may be sufficient |
| Existential proposition | Mere non-observation usually does not refute it; completeness of search, impossibility proof, or related evidence may be required |
| Statistical claim | Audit sample, population, measurement, effect size, uncertainty, reproducibility |
| Causal claim | Audit alternative causes, confounding, intervention, temporal order, counterfactuals |
| Definitional / formal claim | Audit definitional contradiction, circularity, type mismatch, derivation violation |
| Normative / decision claim | Audit purpose, value, risk, constraints, irreversibility, adoption rule |

Therefore:

> **This paper does not adopt the universal rule “a rebuttal is invalid unless it presents at least as much evidence as the original claim.”**

For example, a single valid counterexample can be decisive against a universal proposition.

On the other hand:

```text
An exception may exist.
```

as an unsupported possibility reservation does not automatically cancel a strongly observed claim.

A rebuttal is checked for claim type, counterexample or refutation route, which scope of the original claim it breaks, whether the same reservation survives when returned to the rebuttal side, and whether evidential strength fits the claim type.

The same type, scope, and evidence rules apply to the original claim and to the rebuttal.

---

## 7.1 Three rebuttal gates

To prevent weak reservations such as “there may be a possibility” or “not everyone” from being treated as successful rebuttals, three gates are applied.

## G-R1 Impossibility Gate

If the other side claims:

> **There may be an exception.**

then also pass:

> **Could that possibility itself be impossible?**

This is not an instruction to silence the other side by asserting impossibility.

Its purpose is:

> **Do not privilege one-sided unobserved possibility without grounds.**

Therefore:

```text
there may be an exception
```

by itself is not a rebuttal.

At least one of the following is required:

- a concrete candidate,
- observational grounds,
- conditions of establishment,
- identification of which scope of the existing claim would be broken.

Unsupported possibility reservation is not placed on the same footing as a strongly observed claim.

---

## G-R2 Rebuttal Symmetry Gate
### Also called: Isomorphic Rebuttal Robustness Test

Apply the rebuttal **in the same form back to the rebuttal itself** and see whether it still holds.

For example, if the rebuttal is:

```text
There may be an unobserved scientist who is not arrogant.
```

then, in the same form:

```text
There may also be no such scientist.
```

holds.

If only the first is privileged, require:

> **grounds for the asymmetry explaining why only the first should be adopted.**

Therefore:

> **Claims that cancel each other under the same rebuttal form cannot become decision conditions without additional grounds.**

This gate applies to the original claimant as well as the rebuttal side.

---

## G-R3 Rebuttal Strength Gate

Determine whether the rebuttal has **enough strength to actually break the type, scope, and observational strength of the original claim**.

“Strength” does not mean simple evidence quantity.

At minimum, it includes:

- fit to the claim type,
- concreteness,
- scope match,
- observational or logical grounds,
- consistency,
- an explicit refutation route,
- identification of which part of the original claim is broken.

Therefore:

```text
it is possible
not everyone
there may be exceptions
```

alone may be insufficient rebuttals to a strongly observed claim.

By contrast, a valid single counterexample to a universal proposition may have **decisive logical strength despite small evidence volume**.

Thus:

```text
rebuttal strength
≠ quantity of evidence
```

> **What is required is strength that actually breaks the original claim according to its claim type.**

---

## 7.2 Order of application of the three gates

For rebuttal candidate `R_b`:

```text
R_b
↓
Impossibility Gate
  Is one side's possibility being privileged without grounds?
↓
Rebuttal Symmetry Gate
  Does it still hold asymmetrically when the same form is returned?
↓
Rebuttal Strength Gate
  Does it actually break the original claim under the relevant type and scope?
↓
PASS / SUSPEND / REJECT
```

The three gates are not barriers designed to make rebuttal impossible.

> **They separate weak possibility reservations from strong refutations so the former are not mistakenly promoted into the same status as the latter.**

---

# 8. Time axis and reconstruction of audit results

New observation does not necessarily merely increase the quantity of evidence.

It may reveal that:

- the claim target was actually different,
- the claimant and acting subject had been confused,
- the meaning of the same word changed over time,
- what was treated as refutation belonged to another scope,
- the evaluation axis itself was inappropriate.

In that case, the old PASS / SUSPEND / FAIL is not overwritten.

> **The old judgment remains a record under its original coordinates, and the case is re-audited under the new coordinates.**

If the meaning of a past audit changes, that reinterpretation is also retained separately.

---

# 9. Connection to 神の領域原理（仮）

Even if an argument closes inside X / R / M, the closed description does not become the world-itself.

The final check in this application is therefore:

> **Has the conclusion forgotten that it is a cognition-after description and been misprojected into the world-itself?**

The upper boundary for this is provided by 神の領域原理（仮）.

神の領域原理（仮） itself also remains a provisional Projection rather than final truth.

---

# 10. Connection to Closure Phase Ψ

In repeated audit, stable signatures may remain in how a target preserves definitions, where it stops, and how it handles the unresolved.

Such patterns may become observation targets of Closure Phase Ψ.

However, Ψ must not be inferred from one answer, likability, tone, or personal-value judgment.

If target, time, or observation conditions change, an earlier stable signature is not unconditionally carried forward.

---

# 11. Self-application: audit the auditor

This paper does not audit only the claims of others while exempting itself.

It audits:

- whether the six-viewpoint decomposition is sufficient,
- whether PASS / SUSPEND / FAIL is enough for the purpose,
- whether the auditor’s value judgments are tacitly injected,
- whether the evidence criteria are biased,
- whether the rebuttal-strength standard is lenient only toward the original claim,
- whether the current X / R / M Projection is being fixed too strongly.

> **The moment an audit instrument makes itself unauditable, it becomes inconsistent as argument audit.**

---

# 12. Limitations and reopening conditions

This paper is not a universal instrument that uniquely evaluates every natural-language argument.

When audit target, purpose, or loss changes, the required decomposition may also change.

The paper is reopened at least if:

- the current six viewpoints repeatedly miss major failures,
- the current state set cannot preserve an important distinction,
- auditor dependence dominates results,
- a new argument form, medium, or AI breaks the current structure,
- a description other than X / R / M demonstrates higher audit performance.

---

# 13. Conclusion

Natural-language arguments cannot be fully audited by surface form alone.

If targets, relations, premises, judgment, stopping, or observation range remain tacit, even a formally orderly sentence may remain unclosed.

Applying the Trinity Principle to argument audit makes it possible to first check:

```text
X_t = what is being handled?
R_t = how does it relate?
M_t = what closes it, and where does it stop?
```

If it is not closed:

```text
SUSPEND
```

remains a legitimate output.

At the same time:

> **Audit result, audit coordinates, and the audit instrument itself remain time-bounded Projections. When conditions change, the system returns as far upstream as the question and re-audits.**

That is the state of v0.6.
