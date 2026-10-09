# 晶体发现研究：严格SUN与低能新结构

更新：2026-10-10。[返回仓库首页](../README.md)

当前目标是无条件生成更多不同的低能量新晶体，提高严格SUN，并保留独特性。熟悉框架上的新稳定化学组合继续计入发现；CSP、条件控制和框架分类用于理解能力。

研究以六条能力挑战和四组科学问题为主线，持续追问：即使一种方法实现成功，它回答了什么值得顶会讨论的重要问题？前轮 R1/R2/R3 保留为技术备选。

## 六条挑战与四组研究主线

[六条原始挑战](./landscape/02-open-problems.md) · [四组研究纲领](./programs/README.md)

| 研究组 | 中心问题 | 对应原始挑战 |
|---|---|---|
| [A 共同形成](./programs/a-coformation.md) | 化学选择与几何实现能否共同形成 | 1、2 |
| [B 组合可行](./programs/b-compositional-feasibility.md) | 局部化学知识怎样形成未见但整体可行的晶体 | 3，联系1 |
| [C 反馈与知识](./programs/c-physics-to-knowledge.md) | 物理反馈怎样成为有效决定与可积累知识 | 4、6 |
| [D 开放多解](./programs/d-open-successful-discovery.md) | 物理优化怎样扩大有效解空间并保持多种成功 | 5，联系6 |

[技术备选 R1/R2/R3](./ideas/README.md) · [本轮科学意义攻防](./programs/reviews/README.md) · [论文中心论题](./programs/research-agenda.md) · [共同评价](./evidence/common-protocol.md)

## 当前问题地图

| 文档 | 内容 |
|---|---|
| [学习对象与成功定义](./landscape/00-field-mathematical-abstraction.md) | 联合分布、周期兼容、物理干预与合格结果分布 |
| [已有能力与研究增量](./landscape/01-de-story-audit.md) | 近期晶体原文如何约束方法的新意 |
| [开放能力问题](./landscape/02-open-problems.md) | 六个开放challenge |
| [CV到晶体的对应](./landscape/03-cross-domain-transfer-map.md) | 从动机、任务和学习对象迁移 |
| [共同SUN评价](./landscape/04-evaluation-protocol.md) | 最终物理状态、请求分母和费用 |
| [当前研究主线](./landscape/05-current-research-thesis.md) | 六条挑战、四组问题与技术备选的关系 |
| [贡献矩阵](./matrices/contribution-matrix.md) | 当前学习对象与近邻 |
| [任务—数据—输出](./matrices/task-data-output-matrix.md) | 给定信息、训练单位和输出 |
| [证据矩阵](./matrices/claim-evidence-matrix.md) | 文献事实、历史观测和新假设 |

## 文献与研究依据

[CV前沿目录](./literature/README.md)保存69条记录、68项不同工作，覆盖基础生成、条件／推理、反馈／搜索与评价。真正文生图、类别条件基础生成和相邻任务分别记录。

[晶体原始论文支撑](./evidence/crystal-problem-support.md)与[四组与技术备选来源](./evidence/README.md)保存最近近邻、读取段落及具体基座发布入口。[项目历史摘要](./evidence/historical-evidence.md)同时保留精修成功、指定动作零增量、未知标签和旧评价阶段，作为新假设的依据。

## 43篇历史首轮记录

原核查日期保留2026-09-03。本轮依据既有[bibliography/papers.json](./bibliography/papers.json)精简各篇重复通用模板，保留具体问题、方法、论据和十二项标题，未重新核验全部旧论文。六维分数及首轮建议属于历史判断。

<details>
<summary>展开全部43篇历史论文及报告</summary>

| 年份／出处 | 论文及历史记录 | 角色 |
|---|---|---|
| 2021 · ICLR 2022 | [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](./papers/cdvae.md) | 开山/任务坐标系 |
| 2023 · NeurIPS 2023 | [Crystal Structure Prediction by Joint Equivariant Diffusion](./papers/diffcsp.md) | 任务形式化/机制 |
| 2024 · ICLR 2024 | [Space Group Constrained Crystal Generation](./papers/diffcsppp.md) | 形式化/机制 |
| 2024 · ICML 2024 | [FlowMM: Generating Materials with Riemannian Flow Matching](./papers/flowmm.md) | 几何机制 |
| 2023 · Nature 2025 | [MatterGen: a generative model for inorganic materials design](./papers/mattergen.md) | 系统/规模/验证 |
| 2025 · ICML 2025 | [Open Materials Generation with Stochastic Interpolants](./papers/omatg.md) | 统一机制 |
| 2025 · arXiv 2025 | [A Periodic Bayesian Flow for Material Generation](./papers/crysbfn.md) | 概率机制/效率 |
| 2025 · ICLR 2025 | [SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](./papers/symmcd.md) | 表示/机制 |
| 2025 · AAAI 2026 | [CrystalDiT: A Diffusion Transformer for Crystal Generation](./papers/crystaldit.md) | 架构/训练策略 |
| 2026 · arXiv 2026 | [Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](./papers/sbcd.md) | 新近机制预印本 |
| 2023 · Nature Communications 2024 | [Crystal Structure Generation with Autoregressive Large Language Modeling](./papers/crystallm.md) | 表示/系统先例 |
| 2025 · NeurIPS 2024 | [Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](./papers/mat2seq.md) | 表示/形式化 |
| 2024 · ICLR 2024 | [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](./papers/crystal-text-llm.md) | 规模/能力实证 |
| 2024 · NeurIPS 2024 | [FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](./papers/flowllm.md) | 结构化组合 |
| 2025 · NeurIPS 2025 | [LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](./papers/crysllmgen.md) | 故事整合/工程 |
| 2025 · ICML 2025 | [WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](./papers/wyckoffdiff.md) | 表示/离散机制 |
| 2025 · ICML 2025 | [Wyckoff Transformer: Generation of Symmetric Crystals](./papers/wyckoff-transformer.md) | 表示/高效自回归 |
| 2026 · arXiv 2026 | [Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist](./papers/haco-maskgxt.md) | 跨域机制迁移/系统 |
| 2025 · Nature Communications 2026 | [Siamese Foundation Models for Crystal Structure Prediction](./papers/dao.md) | 数据+双模型系统 |
| 2024 · arXiv 2024; updated 2026 | [Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models](./papers/omat24.md) | 数据基础设施 |
| 2025 · arXiv 2025 | [LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling](./papers/lemat-traj.md) | 数据标准化 |
| 2025 · arXiv 2025 | [MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials](./papers/mp-aloe.md) | 科学分层数据 |
| 2025 · arXiv 2025 | [Accelerating Inverse Materials Design Using Generative Diffusion Models with Reinforcement Learning](./papers/matinvent.md) | 目标对齐/系统 |
| 2025 · Nature Machine Intelligence 2026 | [Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](./papers/chemeleon2.md) | 多目标对齐 |
| 2026 · ICML 2026 | [Open Materials Generation with Inference-Time Reinforcement Learning](./papers/omatg-irl.md) | 连续时间策略优化 |
| 2026 · arXiv 2026 | [PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment](./papers/packflow.md) | 物理对齐/系统 |
| 2026 · arXiv 2026 | [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](./papers/crystalgrpo.md) | 目标重定义/直接先例 |
| 2025 · arXiv preprint | [Establishing Baselines for Generative Discovery of Inorganic Crystals](./papers/establishing-baselines.md) | 强基线 / 评价校准 |
| 2025 · NeurIPS 2025 Datasets and Benchmarks | [All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation](./papers/structure-matches-glitter.md) | Benchmark 纠偏 / 多晶型评价 |
| 2025 · arXiv preprint | [LeMat-GenBench: A Unified Benchmark for Generative Materials Models](./papers/lemat-genbench.md) | 统一生成 Benchmark |
| 2026 · arXiv preprint | [Are Crystal Generative Models Truly Discovering Novel Structures?](./papers/substitution-novelty.md) | 新颖性审计 / 替换派生 |
| 2025 · arXiv preprint (v3 updated 2026) | [cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation](./papers/csun.md) | 连续评价 / 可优化 Reward |
| 2025 · arXiv preprint | [PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability](./papers/phononbench.md) | 动力学稳定 Benchmark |
| 2026 · arXiv preprint | [PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals](./papers/phononscore.md) | 多保真动力学评分 |
| 2022 · ICLR 2023 | [Flow Matching for Generative Modeling](./papers/flow-matching.md) | 连续生成原语 |
| 2023 · ICLR 2024 | [Flow Matching on General Geometries](./papers/riemannian-flow-matching.md) | 流形生成原语 |
| 2023 · Foundational preprint / journal versions | [Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](./papers/stochastic-interpolants.md) | 随机桥与生成统一框架 |
| 2023 · Journal of Machine Learning Research | [GFlowNet Foundations](./papers/gflownet-foundations.md) | 多模态奖励比例采样 |
| 2022 · ICLR 2023 | [Diffusion Posterior Sampling for General Noisy Inverse Problems](./papers/diffusion-posterior-sampling.md) | 生成先验 + 测量似然 |
| 2022 · CVPR 2022 | [MaskGIT: Masked Generative Image Transformer](./papers/maskgit.md) | 并行迭代离散生成 |
| 2023 · ICLR 2024 | [Training Diffusion Models with Reinforcement Learning](./papers/ddpo.md) | 扩散策略优化 |
| 2026 · CVPR 2026 | [Stepwise Credit Assignment for GRPO on Flow-Matching Models](./papers/stepwise-flow-grpo.md) | 时间步信用分配 |
| 2025 · CVPR 2025 | [Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards](./papers/b2-diffurl.md) | 稀疏奖励 / 分支探索 |

</details>

[旧结构化索引](./bibliography/papers.json) · [原CSV索引](./bibliography/paper-index.csv) · [近期晶体来源索引](./bibliography/recent-crystal-sources.json) · [更新日志](./CHANGELOG.md)
