# 补充研究主题

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

这些主题补充生成模型、物理搜索、数据与评价的研究范围。具体文献的状态和证据以来源索引为准。

## A. 生成模型与条件信息

- SGEquiDiff：比较任务、正式标题、代码与对称机制；
- TGDMat：比较任务定义、条件信息和相对 DiffCSP 的增量；
- UniMat / 统一材料生成表示：比较是否真正覆盖 3D 周期结构；
- CrystalFlow / 相关 flow-based CSP：比较与 FlowMM 的差异；
- CrystalFormer 与 CrystalFormer-RL：比较生成目标、RL 奖励及正式版本；
- CRYSTAL: Coordinated Multi-Objective Reinforcement Learning for Crystal Generation：关注 S.U.N. 口径和集合覆盖；
- SG/space-group conditional generators：补齐空间群条件与硬约束路线；
- property-guided crystal diffusion：按性质类型、oracle 和 OOD 分层分析。

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
