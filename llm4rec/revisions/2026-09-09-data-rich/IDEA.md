# Current paper idea

Canonical idea document:

`llm4rec/docs/ideas/11_budget_conditioned_behavioral_selection.md`

This revision (`2026-09-09-data-rich`) promotes the data-rich, fixed-training-budget formulation to the primary SFT direction.

Key decision:

> Do not claim “less data is better”. Test whether the **marginal value of additional supervision changes when candidate-pool richness exceeds available training exposure**, and whether learned behavioral update units improve the allocation of that exposure.

The revision keeps the original gradient-atom pipeline from the provided PDF (fixed projection → dictionary learning → sparse code → selection/refill), but makes full signed codes, magnitude preservation, production-template parity, rare-capability guards and strong raw-gradient/KMeans baselines mandatory.

See:
- `MATHEMATICS.md`
- `TASKS_AND_BASELINES.md`
- `EXPERIMENT_PROTOCOL.md`
- `AUDIT.md`
