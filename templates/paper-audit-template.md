# <Paper Title>

> Paper: <URL>  
> Project/code: <URL or “not yet verified”>  
> Version/date audited: <YYYY-MM-DD>  
> Audit depth: quick screen / full text / code inspected / reproduced

## 0. Thirty-second verdict

**What it does:**  
<one paragraph>

**De-story verdict:**  
<what it truly changes; what it does not establish>

**Why it matters to our research:**  
<use / threat / baseline / transferable mechanism>

## 1. Scientific problem

- Real-world problem:
- Paper-stated problem:
- Gap between them:
- Unit of success:
- Budget and physical setting:
- Is it a real problem, or only a benchmark proxy?

## 2. Mathematical task

- Input \(X\):
- Output \(Y\):
- State space / equivalence:
- Learned object: distribution / score / vector field / function / policy / search process
- Training objective:
- Inference process:
- Scientific utility:
- Where training objective and utility diverge:

## 3. Data-generating process

- Data source:
- Experimental / DFT / endpoint / trajectory / synthetic / self-generated:
- Selection bias:
- Missing information:
- Train/test leakage risks:
- Composition/prototype/polymorph overlap:
- Does the data contain the information required by the claim?

## 4. Core mechanism

Remove all paper-specific names and write the core operator:

\[
\text{input/information}
\rightarrow
\text{new operator or constraint}
\rightarrow
\text{changed learning/search problem}
\rightarrow
\text{observable outcome}
\]

- New variable / information:
- Why it should help:
- Module responsibilities:
- Identifiability:
- Simplest alternative mechanism:

## 5. Claim–evidence alignment

| Claim | Evidence in paper | Direct or indirect? | Alternative explanation | Allowed conclusion |
|---|---|---|---|---|
| C1 |  |  |  |  |
| C2 |  |  |  |  |
| C3 |  |  |  |  |

- Strongest supported claim:
- Strongest unsupported/overstated claim:
- Evidence level: benchmark / mechanism / physics / DFT / experiment

## 6. Hidden assumptions

- A1:
- A2:
- A3:
- Which assumption is most fragile?
- How can it be tested?

## 7. Strongest alternative explanation

<Give the simplest explanation that can reproduce the result without the claimed mechanism.>

Possible sources:

- more data;
- model size/pretraining;
- extra sampling/oracle calls;
- retrieval/memorization;
- post-processing;
- leakage;
- evaluator bias;
- reward hacking.

## 8. Missing baseline

- Most dangerous baseline:
- Budget-matched baseline:
- Data-matched baseline:
- Simple non-neural baseline:
- Same model without claimed mechanism:

## 9. Killer experiment

- Intervention:
- Controlled variables:
- Primary endpoint:
- Result that supports the mechanism:
- Result that falsifies it:
- Early stop rule:

## 10. Contribution type

\[
\Delta =
(\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K)
\]

| Dimension | Score 0–2 | Evidence |
|---|---:|---|
| Problem |  |  |
| Information/data |  |  |
| Objective/mechanism |  |  |
| Compute/scale |  |  |
| Evaluation |  |  |
| Scientific knowledge |  |  |

Primary type:

- problem-opening;
- representation/mechanism;
- data/evaluation;
- scale/system;
- story integration;
- incremental/survival.

## 11. Transferable abstraction

- What transfers:
- What does not transfer:
- Interface variable \(Z\):
- Evidence that \(I(Z;Y\mid X)>0\):
- Evidence that \(H(Y\mid X,Z)<H(Y\mid X)\):
- Crystal-specific failure mode:

## 12. Final verdict

- What changed after reading:
- What remains uncertain:
- How this paper should be cited:
- How it should not be cited:
- Immediate next experiment:
- Priority: foundational / must reproduce / baseline / monitor / low priority

## Reproduction log

| Date | Paper/code version | Environment | Experiment | Result | Judgment update |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
