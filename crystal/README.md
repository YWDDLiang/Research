# Crystal Research Knowledge Base

> 更新时间：**2026-09-03** · 首轮深度审计：**43 篇**  
> [返回仓库首页](../README.md)

这个子目录不是论文收藏夹，而是围绕晶体生成、晶体结构预测（CSP）和 AI for Materials 的**问题—数学—证据知识库**。每篇进入主索引的论文都有独立十二项报告；只有标题和链接、尚未完成审计的条目放在 [watchlist](./watchlist/README.md)，不计入主索引。

## 快速入口

| 文档 | 解决的问题 |
|---|---|
| [领域数学抽象](./landscape/00-field-mathematical-abstraction.md) | 晶体的状态空间、任务、数据、输出、目标和 oracle 到底是什么？ |
| [去故事化总审计](./landscape/01-de-story-audit.md) | 哪些论文改变了问题，哪些改变了表示/机制，哪些主要是系统或故事整合？ |
| [开放问题](./landscape/02-open-problems.md) | 当前真正有研究空间的问题是什么，如何证伪？ |
| [跨领域迁移图](./landscape/03-cross-domain-transfer-map.md) | CV、Flow、SI、GFlowNet、DPS、RL 应迁移哪个数学原语？ |
| [评价协议](./landscape/04-evaluation-protocol.md) | 怎样避免单参考匹配、弱基线、替换新颖性和单一 MLIP 的误导？ |
| [当前研究主线](./landscape/05-current-research-thesis.md) | 如何把 conditional generation 升格为有限预算多势阱搜索？ |
| [贡献矩阵](./matrices/contribution-matrix.md) | 逐篇比较 \(\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K\) |
| [任务—数据—输出矩阵](./matrices/task-data-output-matrix.md) | 论文究竟使用什么输入，输出什么，学习什么？ |
| [Claim–Evidence 矩阵](./matrices/claim-evidence-matrix.md) | 领域常见强 claim 需要哪些证据？ |

---

## 首先区分五种不同任务

| 任务 | 输入 | 输出 | 真正成功条件 |
|---|---|---|---|
| De novo generation | 无条件或性质 \(y\) | 组成 \(A\)、坐标 \(X\)、晶格 \(L\) | 新组成/结构、目标性质与多层稳定性 |
| 固定组成结构恢复 | 组成 \(A\) | 一个或多个 \((X,L)\) | 对数据库参考结构的匹配与误差 |
| 多晶型 / CSP 搜索 | \(A,P,T\) 与预算 \(B\) | 低能局部极小值集合 | 固定物理预算下的独立低能 basin 覆盖 |
| 逆向材料设计 | 性质 \(y\) 或约束集合 | \(A,X,L\) | 目标达成、稳定、新颖、可验证 |
| 实验结构后验 | 组成和 PXRD/PDF 等测量 \(y\) | \(p(s\mid A,y)\) 的候选 | 测量一致性、后验覆盖与校准 |

这些任务不能只用“晶体生成”一个词混在一起。一个模型在单参考恢复上更强，不自动说明它更会搜索多峰势能面；一个 de novo 模型 SUN 更高，也不自动说明它能解决给定组成 CSP。

---

## 论文报告如何阅读

每篇报告固定回答：

1. Scientific problem；
2. Mathematical task；
3. Data-generating process；
4. Core mechanism；
5. Claim–evidence alignment；
6. Hidden assumptions；
7. Strongest alternative explanation；
8. Missing baseline；
9. Killer experiment；
10. Contribution type；
11. Transferable abstraction；
12. Final verdict。

每篇报告中的“去故事化判断”和六维评分都是本库的**可证伪研究判断**，不是论文原文事实，也不是论文质量排行榜。

### 链接规则

- “论文”优先指向 arXiv 或正式论文一手页面；
- “项目”只列已核验到的官方/作者项目或代码；
- “—”表示当前未核验到官方项目地址，**不等于没有代码**；
- 2026 年新预印本的标题、数据规模和结果可能更新，使用时必须锁定版本。

---

## A. 生成基础、条件 CSP 与连续模型

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2021 | **Crystal Diffusion Variational Autoencoder for Periodic Material Generation** | 以 VAE 潜变量组织组成、晶格和原子数，用周期等变图网络通过退火 Langevin 动力学生成坐标，并建立后来广泛沿用的数据集与评价口径。 | 开山/任务坐标系 | [论文](https://arxiv.org/abs/2110.06197) | [代码/项目](https://github.com/txie-93/cdvae) | [审计](./papers/cdvae.md) | 正式发表 |
| 2023 | **Crystal Structure Prediction by Joint Equivariant Diffusion** | 把给定组成的 CSP 形式化为晶格与分数坐标的联合扩散，并通过周期 E(3) 等变网络处理晶体几何。 | 任务形式化/机制 | [论文](https://arxiv.org/abs/2309.04475) | [代码/项目](https://github.com/jiaor17/DiffCSP) | [审计](./papers/diffcsp.md) | 正式发表 |
| 2024 | **Space Group Constrained Crystal Generation** | 将空间群约束分解为晶格对数空间中的基约束与分数坐标的 Wyckoff 位置约束，在 DiffCSP 上实现可控对称生成。 | 形式化/机制 | [论文](https://arxiv.org/abs/2402.03992) | [代码/项目](https://github.com/jiaor17/DiffCSP-PP) | [审计](./papers/diffcsppp.md) | 正式发表 |
| 2024 | **FlowMM: Generating Materials with Riemannian Flow Matching** | 把 Riemannian Flow Matching 适配到晶格、周期坐标和元素变量组成的晶体流形，并强调 base distribution 的可设计性与采样效率。 | 几何机制 | [论文](https://arxiv.org/abs/2406.04713) | [代码/项目](https://github.com/facebookresearch/flowmm) | [审计](./papers/flowmm.md) | 正式发表 |
| 2023 | **MatterGen: a generative model for inorganic materials design** | 联合生成元素、坐标和晶格，并通过 adapter 支持多种性质条件；依靠大规模数据、计算筛选、DFT 与实验验证形成完整材料设计系统。 | 系统/规模/验证 | [论文](https://arxiv.org/abs/2312.03687) | [代码/项目](https://github.com/microsoft/mattergen) | [审计](./papers/mattergen.md) | 正式发表 |
| 2025 | **Open Materials Generation with Stochastic Interpolants** | 以 Stochastic Interpolants 统一 flow 与 diffusion，耦合连续坐标/晶格流和离散元素流，并同步改进 CSP 与 de novo 评测。 | 统一机制 | [论文](https://arxiv.org/abs/2502.02582) | [代码/项目](https://github.com/FERMat-ML/OMatG) | [审计](./papers/omatg.md) | 正式发表 |
| 2025 | **A Periodic Bayesian Flow for Material Generation** | 将 Bayesian Flow Network 扩展到周期变量，提出非单调熵动力学与 entropy conditioning，以很少网络前向完成晶体生成。 | 概率机制/效率 | [论文](https://arxiv.org/abs/2502.02016) | [代码/项目](https://github.com/wu-han-lin/CrysBFN) | [审计](./papers/crysbfn.md) | 预印本/持续更新 |
| 2025 | **CrystalDiT: A Diffusion Transformer for Crystal Generation** | 用统一 Transformer 同时处理晶格与原子变量，加入周期表二维元素编码、平衡训练/选点策略和概率元素解码。 | 架构/训练策略 | [论文](https://arxiv.org/abs/2508.16614) | [代码/项目](https://github.com/hanyi2021/CrystalDiT) | [审计](./papers/crystaldit.md) | 正式发表 |
| 2026 | **Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion** | 从最低对称先验出发，用 Markovian jump diffusion 显式建模空间群之间的离散跳转，把对称破缺/恢复纳入生成。 | 新近机制预印本 | [论文](https://arxiv.org/abs/2608.13457) | — | [审计](./papers/sbcd.md) | 预印本/持续更新 |
## B. 对称性、Wyckoff 与离散生成

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2025 | **SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models** | 把晶体拆成不对称单元和作用于其上的对称变换，联合生成两者，以显式表示真实空间群结构。 | 表示/机制 | [论文](https://arxiv.org/abs/2502.03638) | [代码/项目](https://github.com/sibasmarak/SymmCD) | [审计](./papers/symmcd.md) | 正式发表 |
| 2025 | **WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry** | 在 protostructure/Wyckoff 表示上进行离散扩散，使对称性按构造成立，并提出 Fréchet Wrenformer Distance 衡量对称分布。 | 表示/离散机制 | [论文](https://arxiv.org/abs/2502.06485) | [代码/项目](https://github.com/httk/wyckoffdiff) | [审计](./papers/wyckoffdiff.md) | 正式发表 |
| 2025 | **Wyckoff Transformer: Generation of Symmetric Crystals** | 以 Wyckoff 位置构造压缩离散序列，用无位置编码、置换不变的自回归 Transformer 按空间群条件快速生成。 | 表示/高效自回归 | [论文](https://arxiv.org/abs/2503.02407) | [代码/项目](https://github.com/SymmetryAdvantage/WyckoffTransformer) | [审计](./papers/wyckoff-transformer.md) | 正式发表 |
| 2026 | **Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist** | 通过 HACO 跨域检索将 CV 的 MaskGIT 迁移为 MaskGXT：离散化晶格、坐标、空间群与 Wyckoff token，并迭代置信度解码。 | 跨域机制迁移/系统 | [论文](https://arxiv.org/abs/2606.22866) | [代码/项目](https://github.com/kiyoung98/maskgxt) | [审计](./papers/haco-maskgxt.md) | 预印本/持续更新 |
## C. LLM、序列表示与混合生成

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2023 | **Crystal Structure Generation with Autoregressive Large Language Modeling** | 把 CIF 当作文本序列，用 GPT 类自回归模型按组成和可选空间群生成结构，并可结合能量预测器与 MCTS 改善候选。 | 表示/系统先例 | [论文](https://arxiv.org/abs/2307.04340) | [代码/项目](https://github.com/lantunes/CrystaLLM) | [审计](./papers/crystallm.md) | 正式发表 |
| 2025 | **Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation** | 通过 Niggli/primitive cell 等规范化步骤把等价的三维晶体映射为唯一、可重构、SE(3) 与周期不变的一维序列。 | 表示/形式化 | [论文](https://arxiv.org/abs/2503.00152) | — | [审计](./papers/mat2seq.md) | 正式发表 |
| 2024 | **Fine-Tuned Language Models Generate Stable Inorganic Materials as Text** | 系统比较不同规模预训练语言模型在文本化晶体生成上的能力，报告稳定性随模型规模提升，并支持 infilling 与文本条件。 | 规模/能力实证 | [论文](https://arxiv.org/abs/2402.04379) | [代码/项目](https://github.com/facebookresearch/crystal-text-llm) | [审计](./papers/crystal-text-llm.md) | 正式发表 |
| 2024 | **FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions** | 先由 LLM 产生非平凡的亚稳晶体 base distribution，再由 Riemannian flow 连续修正坐标与晶格。 | 结构化组合 | [论文](https://arxiv.org/abs/2410.23405) | [代码/项目](https://github.com/facebookresearch/flowmm) | [审计](./papers/flowllm.md) | 正式发表 |
| 2025 | **LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation** | LLM 先生成元素、坐标和晶格，保留元素类型，再把连续变量送入预训练等变扩散模型的中间时间步修正。 | 故事整合/工程 | [论文](https://arxiv.org/abs/2510.23040) | [代码/项目](https://github.com/kdmsit/crysllmgen) | [审计](./papers/crysllmgen.md) | 正式发表 |
## D. 物理数据、轨迹与能量引导

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2025 | **Siamese Foundation Models for Crystal Structure Prediction** | DAO-G 生成结构，DAO-P 预测能量并用于不稳定数据弛豫和采样引导，通过大规模稳定/不稳定结构预训练提升 CSP。 | 数据+双模型系统 | [论文](https://arxiv.org/abs/2503.10471) | [代码/项目](https://github.com/ManlioWu/DAO) | [审计](./papers/dao.md) | 正式发表 |
| 2024 | **Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models** | 发布超过 1.1 亿次 DFT 计算，重点覆盖结构与组成多样性，并训练 EquiformerV2 通用势模型。 | 数据基础设施 | [论文](https://arxiv.org/abs/2410.12771) | [代码/项目](https://github.com/FAIR-Chem/fairchem) | [审计](./papers/omat24.md) | 预印本/持续更新 |
| 2025 | **LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling** | 统一 Materials Project、Alexandria、OQMD 等来源的 1.2 亿余轨迹构型，协调多种 DFT 泛函和元数据。 | 数据标准化 | [论文](https://arxiv.org/abs/2508.20875) | [代码/项目](https://github.com/LeMaterial/lematerial-fetcher) | [审计](./papers/lemat-traj.md) | 预印本/持续更新 |
| 2025 | **MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials** | 以主动学习生成近百万 r2SCAN 非平衡结构，覆盖 89 种元素，并强调极端形变、高温高压和远离平衡力的鲁棒性。 | 科学分层数据 | [论文](https://arxiv.org/abs/2507.05559) | — | [审计](./papers/mp-aloe.md) | 预印本/持续更新 |
## E. RL、后训练与多目标生成

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2025 | **Accelerating Inverse Materials Design Using Generative Diffusion Models with Reinforcement Learning** | MatInvent 用 RL 直接优化晶体扩散模型，在较少性质评估下处理单目标和相互冲突的多目标条件设计。 | 目标对齐/系统 | [论文](https://arxiv.org/abs/2511.03112) | — | [审计](./papers/matinvent.md) | 预印本/持续更新 |
| 2025 | **Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning** | 在 latent diffusion 上使用 GRPO 与稳定、新颖、多样等可验证多目标奖励，缓解似然采样偏向已知高密度区域的问题。 | 多目标对齐 | [论文](https://arxiv.org/abs/2511.07158) | [代码/项目](https://github.com/hspark1212/chemeleon2) | [审计](./papers/chemeleon2.md) | 正式发表 |
| 2026 | **Open Materials Generation with Inference-Time Reinforcement Learning** | 直接在 flow 的速度场上构造随机扰动与策略梯度，无需显式 score，并可学习时间依赖 velocity annealing。 | 连续时间策略优化 | [论文](https://arxiv.org/abs/2602.00424) | [代码/项目](https://github.com/FERMat-ML/OMatG) | [审计](./papers/omatg-irl.md) | 正式发表 |
| 2026 | **PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment** | 联合生成分子重原子坐标与晶格，并用 MLIP 能量和力进行 RL physics alignment，接入标准 relax-and-rank 流程。 | 物理对齐/系统 | [论文](https://arxiv.org/abs/2602.20140) | — | [审计](./papers/packflow.md) | 预印本/持续更新 |
| 2026 | **CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction** | 指出能量不识别参考多晶型、奖励集中损害 Top-N 覆盖，提出联合坐标—晶格策略与 quality/coverage 两种模式。 | 目标重定义/直接先例 | [论文](https://arxiv.org/abs/2608.06582) | — | [审计](./papers/crystalgrpo.md) | 预印本/持续更新 |
## F. Benchmark、稳定性与新颖性审计

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2025 | **Establishing Baselines for Generative Discovery of Inorganic Crystals** | 把电荷平衡原型枚举、离子交换等传统方案与现代生成模型放到统一生成—筛选管线中比较，检验生成模型究竟超越了什么。 | 强基线 / 评价校准 | [论文](https://arxiv.org/abs/2501.02144) | — | [审计](./papers/establishing-baselines.md) | 预印本/持续更新 |
| 2025 | **All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation** | 系统揭示结构匹配、数据重复与随机划分对晶体生成评价的误导，提出多晶型感知划分及 METRe、cRMSE 等补充指标。 | Benchmark 纠偏 / 多晶型评价 | [论文](https://arxiv.org/abs/2509.12178) | [代码/项目](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter) | [审计](./papers/structure-matches-glitter.md) | 正式发表 |
| 2025 | **LeMat-GenBench: A Unified Benchmark for Generative Materials Models** | 以统一实现比较多种材料生成模型的有效性、分布一致性、多样性、新颖性与稳定性，突出维度间的系统权衡。 | 统一生成 Benchmark | [论文](https://arxiv.org/abs/2512.04562) | [代码/项目](https://github.com/LeMaterial/lemat-genbench) | [审计](./papers/lemat-genbench.md) | 预印本/持续更新 |
| 2026 | **Are Crystal Generative Models Truly Discovering Novel Structures?** | 指出常用数据库去重会把训练结构的元素替换体计为新结构，并以 substitution-aware 分析重新审计代表性模型的结构新颖性。 | 新颖性审计 / 替换派生 | [论文](https://arxiv.org/abs/2606.23166) | — | [审计](./papers/substitution-novelty.md) | 预印本/持续更新 |
| 2025 | **cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation** | 将离散阈值式 S.U.N. 扩展为连续可比较分数，减轻阈值跳变，并讨论其作为生成模型后训练信号的用途。 | 连续评价 / 可优化 Reward | [论文](https://arxiv.org/abs/2510.12405) | — | [审计](./papers/csun.md) | 预印本/持续更新 |
| 2025 | **PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability** | 以声子谱/虚频审计生成晶体的动力学稳定性，证明几何有效和热力学代理通过并不等于局部动力学稳定。 | 动力学稳定 Benchmark | [论文](https://arxiv.org/abs/2512.21227) | [代码/项目](https://github.com/xqh19970407/PhononBench) | [审计](./papers/phononbench.md) | 预印本/持续更新 |
| 2026 | **PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals** | 提出更低成本的多保真声子/动力学稳定评分和重排方案，使大规模生成候选的二阶稳定性筛选更可行。 | 多保真动力学评分 | [论文](https://arxiv.org/abs/2607.08518) | [代码/项目](http://phononbench.cn/phononscore/) | [审计](./papers/phononscore.md) | 预印本/持续更新 |
## G. 从 CV / 通用 AI 迁移的数学原语

| 年份 | 论文 | 一句话简介 | 首轮角色判断 | 论文 | 项目 | 报告 | 状态 |
|---:|---|---|---|---|---|---|---|
| 2022 | **Flow Matching for Generative Modeling** | 以条件概率路径构造可模拟的向量场回归目标，在无需显式模拟训练轨迹的情况下学习连续归一化流。 | 连续生成原语 | [论文](https://arxiv.org/abs/2210.02747) | [代码/项目](https://github.com/facebookresearch/flow_matching) | [审计](./papers/flow-matching.md) | 正式发表 |
| 2023 | **Flow Matching on General Geometries** | 将 Flow Matching 扩展到一般黎曼流形，为球面、环面和乘积流形上的几何一致生成提供统一工具。 | 流形生成原语 | [论文](https://arxiv.org/abs/2302.03660) | [代码/项目](https://github.com/facebookresearch/riemannian-fm) | [审计](./papers/riemannian-flow-matching.md) | 正式发表 |
| 2023 | **Stochastic Interpolants: A Unifying Framework for Flows and Diffusions** | 通过可设计的随机插值连接任意分布，统一确定性 flow 与随机 diffusion，并给出 drift/score 等可学习量。 | 随机桥与生成统一框架 | [论文](https://arxiv.org/abs/2303.08797) | — | [审计](./papers/stochastic-interpolants.md) | 预印本/持续更新 |
| 2023 | **GFlowNet Foundations** | 建立生成流网络的理论基础，使组合对象按未归一化奖励比例采样，而不是只寻找单一最优对象。 | 多模态奖励比例采样 | [论文](https://jmlr.org/papers/v24/22-0364.html) | — | [审计](./papers/gflownet-foundations.md) | 正式发表 |
| 2022 | **Diffusion Posterior Sampling for General Noisy Inverse Problems** | 将预训练扩散模型作为先验，通过近似似然梯度在采样时解决有噪声、非线性逆问题。 | 生成先验 + 测量似然 | [论文](https://arxiv.org/abs/2209.14687) | [代码/项目](https://github.com/DPS2022/diffusion-posterior-sampling) | [审计](./papers/diffusion-posterior-sampling.md) | 正式发表 |
| 2022 | **MaskGIT: Masked Generative Image Transformer** | 通过双向掩码预测与置信度驱动的迭代重掩码，实现比自回归更并行的离散 token 生成。 | 并行迭代离散生成 | [论文](https://arxiv.org/abs/2202.04200) | [代码/项目](https://github.com/google-research/maskgit) | [审计](./papers/maskgit.md) | 正式发表 |
| 2023 | **Training Diffusion Models with Reinforcement Learning** | 把扩散去噪过程视作多步决策过程，直接用下游奖励对生成策略进行策略梯度优化。 | 扩散策略优化 | [论文](https://arxiv.org/abs/2305.13301) | [代码/项目](https://github.com/jannerm/ddpo) | [审计](./papers/ddpo.md) | 正式发表 |
| 2026 | **Stepwise Credit Assignment for GRPO on Flow-Matching Models** | 根据中间状态带来的 reward 增量为 Flow/扩散不同时间步分配差异化信用，缓解终点稀疏奖励平均摊给所有步骤的问题。 | 时间步信用分配 | [论文](https://arxiv.org/abs/2603.28718) | — | [审计](./papers/stepwise-flow-grpo.md) | 正式发表 |
| 2025 | **Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards** | 通过反向渐进训练与分支采样改善扩散模型面对稀疏终点奖励时的探索和信用分配。 | 稀疏奖励 / 分支探索 | [论文](https://arxiv.org/abs/2503.11240) | — | [审计](./papers/b2-diffurl.md) | 正式发表 |

---

## 推荐阅读路径

### 路线 1：先建立领域坐标系

1. CDVAE；
2. DiffCSP；
3. FlowMM；
4. MatterGen；
5. OMatG；
6. `00-field-mathematical-abstraction.md`。

目标不是记网络，而是分清数据库分布、条件结构分布、物理低能分布和搜索策略分布。

### 路线 2：训练“不被 benchmark 忽悠”的能力

1. Establishing Baselines；
2. All That Structure Matches Does Not Glitter；
3. LeMat-GenBench；
4. substitution-aware novelty；
5. PhononBench / PhononScore；
6. `04-evaluation-protocol.md`。

这条路线应优先于设计新模型。

### 路线 3：理解 LLM 在晶体中到底可能贡献什么

1. CrystaLLM；
2. crystal-text-llm；
3. Mat2Seq；
4. FlowLLM；
5. CrysLLMGen；
6. HACO / MaskGXT。

每篇都要问：提升来自化学推理、序列表示、训练集先验、检索式 warm start，还是更好的 base distribution？

### 路线 4：理解物理数据与后训练

1. OMat24；
2. LeMat-Traj；
3. MP-ALOE；
4. DAO；
5. DDPO；
6. Chemeleon2 / OMatG-IRL / PackFlow / CrystalGRPO。

核心问题是：数据 score、真实 force、弛豫轨迹和终点 reward 分别是什么，是否被错误地解释成同一件事？

### 路线 5：从 CV / AI 迁移新方法

1. Flow Matching；
2. Flow Matching on General Geometries；
3. Stochastic Interpolants；
4. MaskGIT；
5. GFlowNet Foundations；
6. DPS；
7. DDPO 与步骤级信用分配。

只迁移数学原语，不迁移流行词和未经验证的图像叙事。

---

## 当前领域的首轮结论

### 已经拥挤的方向

- 只在 MP-20 上替换 Diffusion/Flow backbone；
- 仅增加空间群、Wyckoff 或对称条件而不研究其上限；
- “首次把 SI 用到晶体”；
- “Diffusion/Flow + GRPO + energy reward”；
- “LLM 生成初始 CIF，连续模型修复”；
- 用 StructureMatcher 未命中直接声称结构新颖。

### 更值得做的问题

- 固定物理预算下的多势阱发现，而不是平均单样本能量；
- 全局跨盆地探索与局部物理修正的可辨识分解；
- reward-proportional / coverage-preserving 的集合级目标；
- evaluator 不确定性与 reward hacking；
- 非平衡轨迹、力与应力如何进入生成，而非只做后筛选；
- 多晶型、substitution-aware novelty 和声子稳定的统一证据链；
- 实验测量条件下的晶体后验采样；
- 主动查询 DFT 的真正 self-improving scientific loop。

详细论证见 [开放问题](./landscape/02-open-problems.md)。

---

## 数据文件与自动检查

- [papers.json](./bibliography/papers.json)：机器可读论文元数据、报告地址与首轮审计字段；
- [paper-index.csv](./bibliography/paper-index.csv)：便于筛选和后续导入；
- `python scripts/validate_repo.py`：检查索引、报告、链接字段和重复 slug；
- `python scripts/new_paper.py --slug ... --title ...`：生成待填写的新报告骨架。

---

## 维护纪律

新增论文进入主索引前，必须完成：

- 一手论文地址和项目地址核验；
- 十二项报告；
- 至少一个危险基线；
- 至少一个杀手实验；
- 可支持 / 不可支持 claim；
- 与现有问题簇的关系；
- 最后核验日期。

只看摘要完成的内容必须标记为“快速初筛”，不能标成“已审计”。  
独立复现后，应在对应报告中追加：环境、commit、数据版本、结果偏差和判断变化。
