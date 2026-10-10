# 晶体生成研究：科学问题、方法与证据

目标是无条件生成更多不同的低能新颖晶体，提高严格 SUN，并保持独特性。熟悉框架中的新稳定化学组合同样属于有效发现。

## 四个独立研究方向

四个方向分别选择中心主张与技术范式，围绕共同的严格SUN目标研究不同能力。

| 方向 | 优先技术构思 | 独立中心问题 |
|---|---|---|
| A 共同形成 | LLM＋Diffusion/SI；混合SI竞争路线 | 化学知识与几何证据怎样共同形成正确选择？ |
| B 组合可行 | 显式周期关系的组合条件Diffusion | 局部规律怎样形成未见但整体可行的晶体？ |
| C 物理知识 | SI/flow分布与路径学习 | 物理经验怎样转化为可迁移生成知识？ |
| D 开放发现 | 层级LLM/AR＋Diffusion与开放探索 | 怎样持续发现并保持多种合格结果？ |

[四方向方法构思](./focus/README.md) · [技术范式与模型层级](./focus/technical-basis.md) · [现象与依据](./focus/evidence-and-alternatives.md)

## 研究问题

| 主题 | 核心问题 | 阅读入口 |
|---|---|---|
| 共同形成 | 化学选择与几何实现怎样在部分信息下形成相互兼容的组合？ | [A：化学与几何共同形成](./programs/a-coformation.md) |
| 组合可行 | 局部化学知识需要哪些共享条件，才能组成新的周期整体？ | [B：局部知识与整体可行](./programs/b-compositional-feasibility.md) |
| 物理反馈与知识 | 物理观测怎样改变仍有效的决定，并帮助后续生成？ | [C：物理反馈到可复用知识](./programs/c-physics-to-knowledge.md) |
| 开放多解发现 | 怎样让更多合格结果在有限计算下出现，并保留已学成功？ | [D：开放合格结果分布](./programs/d-open-successful-discovery.md) |

这些文档提出竞争解释、技术路线和关键科学比较，方法主张仍是研究假设。可以结合[研究议程](./programs/research-agenda.md)、[六条挑战](./landscape/02-open-problems.md)和[领域数学对象](./landscape/00-field-mathematical-abstraction.md)阅读。

## 方法与证据

- [相关候选方法](./ideas/README.md)：联合修订、对象执行接口、物理后果学习。
- [晶体原始文献支撑](./evidence/crystal-problem-support.md)与[来源索引](./evidence/README.md)：机制、证据范围和论文状态。
- [历史实验](./evidence/historical-evidence.md)：成功、负结果、评价阶段和未知标签。
- [共同评价](./evidence/common-protocol.md)：严格 SUN、最终结构身份与费用。
- [CV 方法目录](./literature/README.md)：生成、表示、条件控制、反馈与泛化。
- [文献—命题矩阵](./matrices/claim-evidence-matrix.md)与[能力矩阵](./matrices/contribution-matrix.md)：已有证据与待建立的科学认识。

## 43 篇论文分析

以下记录的资料核查日期为 2026-09-03。条目保留原论文的任务、方法、证据、适用范围和研究比较；六维贡献描述属于定性分析，不能作为跨任务性能排名。

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

[论文元数据](./bibliography/papers.json) · [CSV 索引](./bibliography/paper-index.csv) · [近期晶体来源](./bibliography/recent-crystal-sources.json)
