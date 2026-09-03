# Crystal Literature Watchlist

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

本页只记录后续需要核验和完成十二项报告的候选。  
**这些条目不属于主论文索引，也不能在未完成审计前作为本库的结论依据。**

## A. 需要补齐的生成模型

- SGEquiDiff：核验任务、正式标题、代码与对称机制；
- TGDMat：核验任务定义、条件信息和相对 DiffCSP 的增量；
- UniMat / 统一材料生成表示：核验是否真正覆盖 3D 周期结构；
- CrystalFlow / 相关 flow-based CSP：核验与 FlowMM 的差异；
- CrystalFormer 与 CrystalFormer-RL：核验生成目标、RL 奖励及正式版本；
- CRYSTAL: Coordinated Multi-Objective Reinforcement Learning for Crystal Generation：重点审计 S.U.N. 口径和集合覆盖；
- SG/space-group conditional generators：补齐空间群条件与硬约束路线；
- property-guided crystal diffusion：按性质类型、oracle 和 OOD 分层审计。

## B. 传统 CSP 与搜索基线

- AIRSS；
- USPEX；
- CALYPSO；
- basin hopping；
- evolutionary search；
- minima hopping；
- random/prototype/ionic substitution 系列；
- 分子晶体 packing/search 工具。

目标不是写历史综述，而是建立与神经生成模型相同预算口径的强基线。

## C. MLIP 与 evaluator

- M3GNet；
- CHGNet；
- MACE / MACE-MP；
- MatterSim；
- EquiformerV2/OMat 系列模型；
- ORB；
- SevenNet；
- phonon/elastic/finite-temperature surrogate。

每个 evaluator 报告应重点回答：训练域、OOD 校准、生成样本误差、ranking flip 和 reward-hacking 风险。

## D. 数据与 benchmark

- MP-20 的构建、泄漏和多晶型统计；
- Alexandria、Materials Project、OQMD、NOMAD 等数据差异；
- Matbench Discovery；
- dynamical stability / finite-temperature benchmark；
- experimental time-split 数据；
- synthesis-aware / metastability 数据；
- failed DFT、high-force 和 negative data。

## E. CV / AI 候选原语

- Schrödinger bridge；
- consistency/rectified flow；
- diffusion/flow distillation；
- quality-diversity；
- sequential Monte Carlo；
- active learning 与 optimal experimental design；
- world-model / model-based RL；
- process reward 与 verifier；
- self-correction 与 test-time search；
- distributional RL / risk-sensitive optimization。

## 进入主索引的条件

1. 核验论文与官方/作者项目；
2. 锁定版本；
3. 完成十二项报告；
4. 指出危险基线和杀手实验；
5. 说明与现有索引的直接重叠；
6. 更新 `papers.json`、CSV 和主索引；
7. 通过 `scripts/validate_repo.py`。
