# What Is a Principle? / Principle Discrimination Method
## A Cognitive-Engineering Specification for Preventing Observations, Patterns, Models, and Mechanisms from Being Mistakenly Promoted into Principles

**Source document**: `05A_原理とは何かと原理判別法_v0_2_ja_en.md`  
**Source version**: v0.2  
**Source revision date**: 2026-10-07  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Source authority**: Japanese Canonical Original (J0)  
**Translation class**: T1 / Aligned Full Translation  
**Translation status**: CURRENT  
**Target language**: English  
**Authority**: Non-authoritative. In any semantic conflict, ambiguity, omission, or translation residual, the Japanese J0 source prevails.  
**Policy**: `TRANSLATION_POLICY.md`

> **Position**: This paper specifies the current public definition of “principle” in Cognitive Engineering and the method for discriminating principles. It does not disclose internal HDS procedures for discovering principles, internal evaluators, or reproducible implementation recipes.

> **Theory-state rule**: “Principle,” “principle candidate,” necessity, minimality, isomorphism, causality, establishment, and collapse are themselves time-bounded Projections. This paper fixes their meaning inside the present version so discrimination can be performed, but does not promote them into final and immutable ontology.

---

# Part I. Full English Translation of the Japanese Canonical Original

## One-sentence definition

> **A principle is a structural core that, under a specified time, cognitive world, subject, target, relation, and condition, explains what acts, through which relation, under which conditions, what it establishes or changes, and what must be changed for it to collapse.**

A principle is not merely an observation result, a frequently recurring pattern, or a plausible explanation.

Under current Cognitive Engineering:

> **A principle is not discovered as absolute truth. It is adopted as a provisional principle with an explicit scope, time, refutation conditions, and reopening conditions.**

---

# 0. The principle question

The starting point of principle discrimination is:

> **What makes this possible? / What establishes this?**

“This” can include:

- a phenomenon,
- judgment,
- decision-making,
- capability,
- result,
- institution,
- theory,
- proof,
- safety,
- reproducibility,
- failure.

The first explanation obtained is not privileged.

One explanation is not yet a principle.

---

# 1. Separate a principle from lower-level descriptions

Principle discrimination does not mix at least the following:

| State | Current definition |
|---|---|
| Observation | What happened |
| Common feature | Multiple cases share a feature |
| Correlation | Multiple quantities or states covary |
| Pattern | A recurrent form or tendency |
| Model | A description or representation used to handle a target |
| Mechanism | A candidate account of how actions or transitions produce an outcome |
| Principle candidate | Candidate structural core that establishes multiple observations, mechanisms, or outcomes |
| Scope-bounded provisional principle | Structural core that passes the current discrimination gates and is adopted for local application |

Therefore:

```text
appears often
≠
principle

can explain something
≠
principle

is correlated
≠
principle

has a written mechanism
≠
principle
```

---

# 2. Minimum description required of a principle candidate

A candidate principle P must at least answer:

```text
1. What acts?
2. What stands in what relation to what?
3. Under what conditions does it hold?
4. What does it establish, maintain, or change?
5. What change causes it to collapse?
6. What observation would make it a refutation or revision target?
7. What is its scope?
```

If these cannot be separated, the candidate remains in a lower state such as:

```text
unformed
shadow of a principle
pattern
model
mechanism candidate
principle candidate
```

Lack of separation is not repaired by using a stronger-sounding word.

---

# 3. Core of the principle discrimination method

## 3.1 Core judgment

Apply a **complete mathematical proof** to candidate principle P.

“Complete mathematical proof” here does not mean merely:

> explain P in a convincing way.

Rather, expand the proposition P toward a complete proof from the adopted axioms, definitions, premises, and relations, then observe:

> **whether the proof structure ultimately recurses, reactivates, or returns to P itself or to a structure functionally isomorphic to P.**

The shortest form is:

```text
proposition P
↓
apply a complete mathematical proof
↓
fully expand the proof
↓
does it return to P itself or a functionally isomorphic structure?
↓
YES → principle candidate
NO  → reclassify as a derived proposition, theorem, rule, etc. derived from a higher structure
```

This **recursiveness** is the primary judgment of the principle discrimination method.

---

## 3.2 Distinguish recursion from circular argument

The recursion here is not the argumentative fallacy:

```text
P is correct
because P
```

It means structural return:

```text
prove P
↓
expand proof dependencies
↓
trace upward through conditions, relations, and structures
↓
attempt to close the proof
↓
P or a functionally isomorphic structure becomes necessary again
```

The audit therefore does not ask whether the same word reappears in the text.

It asks:

> **Does the same structure carrying the same responsibility for establishment reappear unavoidably in order to close the proof?**

---

## 3.3 Separate principle candidates from derived structures

When a complete mathematical proof is applied:

### A. The proof recurses to P itself

P remains strongly as a principle candidate.

### B. The proof recurses to a structure functionally isomorphic to P

Even if the name or expression differs, the structural core of P has recurred, so it is treated as a principle candidate.

### C. The proof does not return to P and instead closes through a distinct higher structure Q

P is reclassified as a proposition, theorem, rule, model-internal result, or another structure derived from Q.

### D. The return point is a still lower, local structure

P is not promoted into a universal principle. It is limited as a **derived principle / local principle candidate**.

### E. The proof conditions themselves do not close

SUSPEND.

---

# 4. Meaning of applying a complete mathematical proof

Mathematics is not used in the principle discrimination method because converting something into equations makes it prestigious.

The purpose is:

> **To avoid omitting premises, definitions, relations, derivations, dependencies, and completion conditions, and to trace where the proof returns.**

A complete mathematical proof may use:

- symbolization,
- formalization,
- axiomatization,
- definition expansion,
- dependency expansion,
- refutable completion conditions.

The goal is not formalization for its own sake.

What matters is:

```text
Where does the proof end?
What does the proof require again?
What does it recurse to?
```

---

# 5. Secondary audit: elimination and isomorphic reintroduction test

To reinforce the recursive judgment from the complete mathematical proof, candidate P and its functionally isomorphic structures `[P]~` may, when necessary, be temporarily excluded in an isolated validation world.

The same establishment goal G is then reconstructed.

```text
exclude P / [P]~
↓
reconstruct the same G
↓
is P or an isomorphic structure reintroduced?
```

This test is a **secondary audit that checks the recursion observed in complete proof from another angle**. It is not the primary principle-discrimination criterion itself.

The elimination test is not an operation that permanently deletes elements from the canonical source, production environment, or real system.

> **It is a counterfactual test conducted on an isolated validation copy.**

Even if removal produces no change, the record is limited to:

```text
contribution not detected under these conditions
```

---

# 6. Audits after recursion

Recursion alone does not automatically determine scope or granularity.

For a principle candidate in which recursion has been observed, at least the following are audited.

## G1 Minimality

Can further surplus elements be removed from the recurring structure without losing its establishment responsibility?

## G2 Isomorphism

Has the proof truly returned to a structure carrying the same establishment responsibility, rather than merely reusing a similar surface term?

## G3 Generativity

Can multiple downstream phenomena, rules, judgments, or mechanisms be derived from the structure?

## G4 Cross-case stability

Within the declared scope, is the same recursive structure preserved beyond one local case?

## G5 Failure detectability

Can conditions under which the principle fails, collapse points, and failure signatures be identified?

## G6 Scope

Can the system distinguish whether the result is a universal principle, derived principle, or local principle?

These are **post-recursion audits**. They do not replace the core discrimination:

```text
complete mathematical proof
→ does it recurse?
```

---

# 7. Additional audit: counter-models, counterfactuals, and perturbation

Do not examine only candidate principle P.

The audit may retain in parallel:

- baseline model,
- alternative model,
- contrary hypothesis,
- null model,
- no-change model,
- observation error,
- delayed effect,
- different objective,
- adversarial conditions,
- counterfactuals,
- mechanism candidates.

The fact that P was generated does not mean P has been verified or adopted.

---

# 8. Principle → operating principle

Do not reverse the order between principle and operating principle.

```text
principle
↓
operating principle
```

This paper distinguishes:

> **Principle = structural core that establishes the target, activity, or system.**

> **Operating principle = condition, boundary, or discipline that becomes operationally necessary or strongly required after adopting the principle.**

For example, if a principle implies that reversibility is required, then:

```text
preserve reversibility
```

may be an operating principle derived from it rather than the principle itself.

Do not place an operating principle first and later relabel it a principle.

---

# 9. Relation to axiom, theorem, law, and rule

Hierarchy is not decided by name alone.

### Axiom
A premise adopted as a starting point inside a formal system.

### Theorem
A proposition derived from axioms, definitions, and related premises.

### Law
A description of a relation or regularity that holds stably in a specified domain.

### Rule
A condition defining operation, judgment, or procedure.

### Operating principle
An operational condition, boundary, or discipline derived after adopting a principle.

### Principle
The structural core explaining what establishes a target, phenomenon, judgment, or system.

A so-called “law” may carry a principle-like structure, while something called a “principle” may actually be a rule, heuristic, or model-internal assumption.

> **Classification is based on establishment responsibility and discrimination, not on the label.**

---

# 10. A principle is not an absolute entity

Passing principle discrimination does not automatically promote a candidate into:

```text
final principle
universal principle
immutable principle
```

The current system retains it as:

> **a scope-bounded provisional principle.**

At minimum, record:

- time,
- cognitive world,
- subject,
- target,
- relation,
- scope,
- establishment conditions,
- boundaries,
- refutation conditions,
- return/reopening conditions.

If new observation changes subject, target, relation, condition, or the question itself, the principle is reopened.

---

# 11. Failure and reopening of principles

When an outcome does not match a prediction, do not jump directly to:

```text
the principle is false
```

First separate possibilities such as:

- target identity changed,
- the case was outside scope,
- a condition was missing,
- the mechanism was misunderstood,
- the observation method was wrong,
- an alternative model is stronger,
- the candidate principle is too coarse,
- the principle itself failed.

Then choose among:

```text
retain
revise
split
reject
reopen
```

---

# 12. Relation to the Trinity Principle

Principle discrimination itself requires a world, target, relations, and judgment conditions.

As a representative Projection:

```text
X = discrimination target, candidate P, establishment goal G
R = elimination, substitution, counterfactual, perturbation, generation, collapse relations
M = principle-judgment gates, scope, refutation, stopping conditions
```

can be used.

However, the principle discrimination method is not reduced to X / R / M itself.

---

# 13. Relation to 神の領域原理（仮）

Even after judging that a principle has been discovered, the principle description is not promoted into the pre-cognitive world-itself.

```text
appears indispensable under current conditions
≠
an eternally immutable principle is engraved in the world-itself
```

The principle discrimination method itself is not exempt from self-application or re-audit.

---

# 14. Relation to HDS

The publicly disclosable functional core of HDS / 人間意思決定理論（仮） includes:

> **finding principles.**

This paper gives a foundational public definition that prevents the term “principle” from becoming mixed in public discussion.

However, the following remain outside the public scope of this paper:

- internal principle-discovery circulation of HDS,
- internal states,
- ledgers,
- gate implementation,
- evaluation design,
- judgment mechanisms,
- reproducible operating recipes.

---

# 15. Shortest form of principle discrimination

```text
principle question
“What makes this possible?”
↓
proposition / candidate principle P
↓
apply a complete mathematical proof to P
↓
expand the proof to completion
↓
does it recursively circulate, reactivate, or return
to P itself or a functionally isomorphic structure?
↓
YES
→ principle candidate
→ classify return point and scope
→ secondary audit of minimality, isomorphism, generativity,
   cross-case stability, and failure detectability
→ scope-bounded provisional principle

NO
→ reclassify as theorem, rule,
  model-internal result, or other derived structure

undecidable
→ SUSPEND
```

---

# 16. Conclusion

A principle is not a profound-sounding word or a law named by authority.

> **It is the structural core that explains what acts, through which relation, under which conditions, what it establishes or changes, and what must change for it to collapse.**

And the core of principle discrimination is:

> **Apply a complete mathematical proof to the proposition and observe whether the proof structure recursively circulates, reactivates, or returns to the proposition itself or to a functionally isomorphic structure.**

A recursively returning candidate remains a principle candidate and is then audited for minimality, isomorphism, generativity, cross-case stability, failure detectability, and scope.

If the proof closes through a distinct higher structure without recursion, the candidate is reclassified as a theorem, rule, derived proposition, or related lower structure.

A principle itself remains provisional and is not exempt from reopening across time.
