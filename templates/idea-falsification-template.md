# Idea Falsification Sheet: <Idea>

> Date:  
> Related direction:  
> Decision deadline:

## 1. One-sentence hypothesis

\[
H:\quad
\text{intervention}
\Rightarrow
\text{mechanism}
\Rightarrow
\text{outcome}
\]

## 2. Variables

- Independent variable:
- Mediator/mechanism variable:
- Outcome:
- Confounders:
- Fixed budget:
- Evaluation oracle:

## 3. Why it should work

- Information newly introduced:
- Why the base problem becomes easier:
- Why existing method cannot use this information:
- Mathematical argument:
- Expected qualitative signature:

## 4. Strongest alternative explanations

| Alternative | Why plausible | Control experiment |
|---|---|---|
| More data |  |  |
| More parameters |  |  |
| More compute/samples |  |  |
| Retrieval/memorization |  |  |
| Post-processing |  |  |
| Evaluator bias |  |  |
| Simple regularization |  |  |

## 5. Dangerous baselines

1.  
2.  
3.  

## 6. Killer experiment

- Minimal implementation:
- Dataset/subset:
- Baselines:
- Primary endpoint:
- Secondary endpoint:
- Statistical unit:
- Exact falsification threshold:
- Maximum compute:
- Result that kills the idea:

## 7. Failure modes

- It improves only training reward:
- It improves local quality but not search:
- It fails OOD:
- It collapses diversity:
- It depends on a single evaluator:
- It is matched by a simple baseline:
- It is already covered by prior work:

## 8. Decision table

| Result | Interpretation | Action |
|---|---|---|
| Mechanism variable changes and endpoint improves | causal story survives | scale up |
| Endpoint improves but mechanism variable does not | wrong story | rename/reformulate |
| Training metric improves, audit metric does not | reward/evaluator exploitation | stop or fix evaluator |
| Simple baseline matches | complexity unjustified | simplify |
| No meaningful effect | hypothesis falsified | stop |

## 9. Allowed claim after the experiment

- Positive result:
- Negative result:
- Claims still forbidden:
