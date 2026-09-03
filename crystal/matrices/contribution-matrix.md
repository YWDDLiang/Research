# 论文贡献矩阵

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

## 评分定义

\[
\Delta =
(\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K)
\]

| 维度 | 说明 |
|---|---|
| \(\Delta P\) | 是否改变问题定义、任务或领域坐标系 |
| \(\Delta I\) | 是否引入新数据、信息、表示或观测 |
| \(\Delta O\) | 是否提出新的目标、算法原语或可复用机制 |
| \(\Delta C\) | 是否实质改变效率、规模或系统能力 |
| \(\Delta E\) | 是否改变评价标准与证据门槛 |
| \(\Delta K\) | 是否产生新的科学知识或规律 |

评分：

- 0：基本未改变；
- 1：明显推进；
- 2：实质改变。

**警告：** 总分不是论文质量、影响力或录用概率。一个单维度为 2 的工作可能比多个维度为 1 的工作更开创；评分是本库可被复现和讨论推翻的首轮判断。

## 全部论文

| 年份 | 论文 / 报告 | 角色 | ΔP | ΔI | ΔO | ΔC | ΔE | ΔK | 总计 |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2021 | [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/cdvae.md) | 开山/任务坐标系 | 2 | 2 | 2 | 1 | 2 | 0 | **9** |
| 2022 | [Diffusion Posterior Sampling for General Noisy Inverse Problems](../papers/diffusion-posterior-sampling.md) | 生成先验 + 测量似然 | 2 | 1 | 2 | 1 | 2 | 0 | **8** |
| 2022 | [Flow Matching for Generative Modeling](../papers/flow-matching.md) | 连续生成原语 | 2 | 1 | 2 | 2 | 1 | 0 | **8** |
| 2022 | [MaskGIT: Masked Generative Image Transformer](../papers/maskgit.md) | 并行迭代离散生成 | 2 | 1 | 2 | 2 | 1 | 0 | **8** |
| 2023 | [Crystal Structure Generation with Autoregressive Large Language Modeling](../papers/crystallm.md) | 表示/系统先例 | 1 | 1 | 1 | 1 | 1 | 0 | **5** |
| 2023 | [Training Diffusion Models with Reinforcement Learning](../papers/ddpo.md) | 扩散策略优化 | 2 | 1 | 2 | 1 | 1 | 0 | **7** |
| 2023 | [Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/diffcsp.md) | 任务形式化/机制 | 2 | 1 | 2 | 1 | 1 | 0 | **7** |
| 2023 | [GFlowNet Foundations](../papers/gflownet-foundations.md) | 多模态奖励比例采样 | 2 | 1 | 2 | 1 | 1 | 0 | **7** |
| 2023 | [MatterGen: a generative model for inorganic materials design](../papers/mattergen.md) | 系统/规模/验证 | 1 | 2 | 2 | 2 | 2 | 1 | **10** |
| 2023 | [Flow Matching on General Geometries](../papers/riemannian-flow-matching.md) | 流形生成原语 | 1 | 2 | 2 | 1 | 1 | 0 | **7** |
| 2023 | [Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](../papers/stochastic-interpolants.md) | 随机桥与生成统一框架 | 2 | 1 | 2 | 1 | 1 | 0 | **7** |
| 2024 | [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/crystal-text-llm.md) | 规模/能力实证 | 1 | 1 | 1 | 2 | 1 | 0 | **6** |
| 2024 | [Space Group Constrained Crystal Generation](../papers/diffcsppp.md) | 形式化/机制 | 1 | 2 | 2 | 1 | 1 | 0 | **7** |
| 2024 | [FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](../papers/flowllm.md) | 结构化组合 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2024 | [FlowMM: Generating Materials with Riemannian Flow Matching](../papers/flowmm.md) | 几何机制 | 1 | 2 | 2 | 2 | 1 | 0 | **8** |
| 2024 | [Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models](../papers/omat24.md) | 数据基础设施 | 1 | 2 | 1 | 2 | 2 | 0 | **8** |
| 2025 | [Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards](../papers/b2-diffurl.md) | 稀疏奖励 / 分支探索 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2025 | [Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](../papers/chemeleon2.md) | 多目标对齐 | 1 | 1 | 2 | 1 | 2 | 0 | **7** |
| 2025 | [A Periodic Bayesian Flow for Material Generation](../papers/crysbfn.md) | 概率机制/效率 | 1 | 2 | 2 | 2 | 1 | 0 | **8** |
| 2025 | [LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](../papers/crysllmgen.md) | 故事整合/工程 | 0 | 1 | 1 | 1 | 1 | 0 | **4** |
| 2025 | [CrystalDiT: A Diffusion Transformer for Crystal Generation](../papers/crystaldit.md) | 架构/训练策略 | 0 | 1 | 1 | 1 | 1 | 0 | **4** |
| 2025 | [cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation](../papers/csun.md) | 连续评价 / 可优化 Reward | 1 | 1 | 2 | 0 | 2 | 0 | **6** |
| 2025 | [Siamese Foundation Models for Crystal Structure Prediction](../papers/dao.md) | 数据+双模型系统 | 1 | 2 | 2 | 2 | 1 | 0 | **8** |
| 2025 | [Establishing Baselines for Generative Discovery of Inorganic Crystals](../papers/establishing-baselines.md) | 强基线 / 评价校准 | 2 | 1 | 1 | 1 | 2 | 0 | **7** |
| 2025 | [LeMat-GenBench: A Unified Benchmark for Generative Materials Models](../papers/lemat-genbench.md) | 统一生成 Benchmark | 1 | 2 | 1 | 1 | 2 | 0 | **7** |
| 2025 | [LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling](../papers/lemat-traj.md) | 数据标准化 | 1 | 2 | 1 | 1 | 1 | 0 | **6** |
| 2025 | [Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/mat2seq.md) | 表示/形式化 | 1 | 2 | 1 | 1 | 1 | 0 | **6** |
| 2025 | [Accelerating Inverse Materials Design Using Generative Diffusion Models with Reinforcement Learning](../papers/matinvent.md) | 目标对齐/系统 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2025 | [MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials](../papers/mp-aloe.md) | 科学分层数据 | 2 | 2 | 2 | 1 | 2 | 0 | **9** |
| 2025 | [Open Materials Generation with Stochastic Interpolants](../papers/omatg.md) | 统一机制 | 1 | 2 | 2 | 1 | 1 | 0 | **7** |
| 2025 | [PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability](../papers/phononbench.md) | 动力学稳定 Benchmark | 2 | 2 | 1 | 2 | 2 | 1 | **10** |
| 2025 | [All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation](../papers/structure-matches-glitter.md) | Benchmark 纠偏 / 多晶型评价 | 2 | 2 | 1 | 0 | 2 | 0 | **7** |
| 2025 | [SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](../papers/symmcd.md) | 表示/机制 | 1 | 2 | 2 | 1 | 1 | 0 | **7** |
| 2025 | [Wyckoff Transformer: Generation of Symmetric Crystals](../papers/wyckoff-transformer.md) | 表示/高效自回归 | 0 | 2 | 1 | 2 | 1 | 0 | **6** |
| 2025 | [WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/wyckoffdiff.md) | 表示/离散机制 | 1 | 2 | 2 | 2 | 1 | 0 | **8** |
| 2026 | [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](../papers/crystalgrpo.md) | 目标重定义/直接先例 | 2 | 1 | 2 | 1 | 2 | 0 | **8** |
| 2026 | [Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist](../papers/haco-maskgxt.md) | 跨域机制迁移/系统 | 1 | 2 | 2 | 1 | 2 | 0 | **8** |
| 2026 | [Open Materials Generation with Inference-Time Reinforcement Learning](../papers/omatg-irl.md) | 连续时间策略优化 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2026 | [PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment](../papers/packflow.md) | 物理对齐/系统 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2026 | [PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals](../papers/phononscore.md) | 多保真动力学评分 | 1 | 2 | 2 | 2 | 2 | 0 | **9** |
| 2026 | [Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](../papers/sbcd.md) | 新近机制预印本 | 1 | 2 | 2 | 0 | 0 | 0 | **5** |
| 2026 | [Stepwise Credit Assignment for GRPO on Flow-Matching Models](../papers/stepwise-flow-grpo.md) | 时间步信用分配 | 1 | 1 | 2 | 1 | 1 | 0 | **6** |
| 2026 | [Are Crystal Generative Models Truly Discovering Novel Structures?](../papers/substitution-novelty.md) | 新颖性审计 / 替换派生 | 2 | 2 | 1 | 0 | 2 | 1 | **8** |

## 使用方式

不要问“哪篇总分最高”，而要问：

- 我们的新工作准备改变哪一维？
- 这一维是否已有更强工作？
- 该变化能否用一个反事实实验直接证明？
- 其余维度是否只是故事性外推？
- 哪个维度最适合成为论文主贡献，哪些只应作为实现细节？

## 当前主线的目标贡献向量

若有限预算多势阱 CSP 路线完整成立，期望贡献是：

\[
\Delta_{\mathrm{target}}
=
(2,1,2,1,2,1)
\]

其中：

- \(\Delta P=2\)：单参考恢复转为有限预算集合发现；
- \(\Delta I=1\)：使用轨迹/非平衡/多保真数据；
- \(\Delta O=2\)：basin archive 与 set-level objective；
- \(\Delta C=1\)：amortized search efficiency；
- \(\Delta E=2\)：预算、polymorph、evaluator-robust 协议；
- \(\Delta K=1\)：若发现生成阶段与 basin commitment 的规律。

若最后仅实现 Diffusion + GRPO，预期更接近：

\[
(0,0,1,0,0,0)
\]

这正是为什么必须先改变问题和证据，而不是堆模块。
