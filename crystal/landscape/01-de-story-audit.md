# 晶体生成领域的去故事化总审计

> [返回晶体索引](../README.md) · 审计基准日：**2026-09-03**

## 1. 审计的目的

这里的“故事型”“系统型”“机制型”等标签不是对作者动机或论文价值的道德判断，而是回答：

> **把标题、模型名和宏大背景去掉后，这项工作究竟改变了问题、信息、目标、计算、评价还是科学知识？**

本库使用六维贡献向量：

\[
\Delta =
(\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K)
\]

- \(\Delta P\)：问题定义；
- \(\Delta I\)：信息、数据或表示；
- \(\Delta O\)：目标函数、算法原语或机制；
- \(\Delta C\)：计算效率、规模与系统能力；
- \(\Delta E\)：评价标准和证据门槛；
- \(\Delta K\)：新的科学知识。

高水平贡献不要求六项都高。关键是至少有一项发生**可验证且不可被简单基线解释的变化**。

---

## 2. 六类论文的判别

### 2.1 开山 / 问题定义型

判断标准：

- 后续工作即使更换网络，也必须在它提出的问题、表示或 benchmark 中讨论；
- 贡献不会随着一张 leaderboard 被刷新而消失；
- 它改变“什么值得优化”或“什么证据算成功”。

在当前索引中，CDVAE、DiffCSP、Flow Matching、GFlowNet Foundations，以及新的 benchmark 纠偏工作分别在不同层面接近这一类型。

### 2.2 机制 / 表示型

判断标准：

- 提出新的状态表示、概率路径、等变结构、离散生成算子或训练目标；
- 能被多个任务复用；
- 核心贡献可以脱离具体材料故事表达为数学命题。

FlowMM、Flow Matching on General Geometries、Mat2Seq、WyckoffDiff、MaskGIT 属于典型审计对象。

### 2.3 数据 / 评价型

判断标准：

- 暴露旧数据或旧指标无法支撑的 claim；
- 建立新的数据层或评测接口；
- 使此前不可区分的机制变得可区分。

OMat24、LeMat-Traj、MP-ALOE、Establishing Baselines、All That Structure Matches Does Not Glitter、LeMat-GenBench、PhononBench 与 substitution-aware novelty 都可能比“又一个模型”更能改变领域方向。

### 2.4 规模 / 系统 / 验证型

判断标准：

- 不是只增加参数，而是打通数据、模型、筛选、DFT、实验或部署；
- 把证据链推进到此前无法达到的层级；
- 清楚拆分规模增益、算法增益和 oracle 增益。

MatterGen 是代表性系统工作；它的价值不能只归因于某个扩散模块，也不能因为数学原语不是全新就被低估。

### 2.5 故事整合型

判断标准：

- 组合本身可以有价值；
- 但必须证明各模块承担不同且不可替代的职责；
- 需要排除检索、warm start、小模型、额外计算和后筛选解释。

LLM + Diffusion、LLM + Flow、AI co-scientist + generated algorithm 等路线都必须接受这一审计。

### 2.6 生存性增量型

常见特征：

- 相同任务、相同数据、相同证据标准；
- 替换 backbone、attention、loss 或 condition；
- 没有危险基线；
- 提升依赖特定 evaluator 或后处理；
- 机制解释没有直接干预证据。

这类工作可能是可靠工程，但不能靠宏大材料故事自动升格为科学贡献。

---

## 3. 各问题簇真正改变了什么

### 3.1 从 VAE / Diffusion 到 Flow / SI

#### 真正贡献

- 周期晶体的状态空间与等变性；
- 晶格、分数坐标与元素的联合生成；
- 条件 CSP 的概率建模；
- 在流形上设计生成路径；
- 通过 base distribution 和 bridge 改善运输问题。

#### 容易被故事化的部分

- 把生成向量场解释为物理力；
- 把“采样更稳定”解释为理解势能面；
- 仅更换 diffusion/flow/SI 名称就声称范式突破；
- 在不同网络、数据和采样步数下比较后归因于生成原理。

#### 必须做的区分实验

- 相同数据、backbone、参数、NFE 和 solver；
- 只改变概率路径/base distribution；
- 测量路径长度、数值误差、样本质量和 basin 覆盖；
- 将训练 score 与独立 force/DFT 分开。

### 3.2 对称性与 Wyckoff

#### 真正贡献

- 把晶体等价性和空间群先验放入状态空间；
- 通过低维 protostructure 降低无效搜索；
- 保证或提高对称合法性；
- 提供新的离散生成空间。

#### 核心风险

对称约束可能：

- 提高下限：减少无效结构；
- 同时降低上限：限制自发对称性破缺、低对称亚稳态和未知原型。

因此“对称性更强”不是单向正确。需要回答：

\[
\text{约束带来的样本效率收益}
\quad\text{vs.}\quad
\text{可达 basin 集合损失}
\]

### 3.3 LLM 与序列生成

#### 可能成立的贡献

- 学习离散结构模式；
- 提供非平凡 base distribution；
- 用统一序列接口联合组成、对称和几何；
- 借助预训练获得化学组合先验；
- 产生可搜索的粗结构假设。

#### 最危险的替代解释

- 训练结构记忆；
- CIF 语言模式学习；
- 检索或原型 warm start；
- 参数量与数据量；
- 一个小型普通 Transformer 即可完成；
- LLM 只生成更接近训练分布的初始化，连续模型承担全部物理质量。

#### LLM claim 的最低证据

1. 与检索、离子替换和小 Transformer 比较；
2. 控制参数、数据和采样预算；
3. 中间变量 \(z\) 对最终 basin 有新增信息：

\[
I(z;B_{\mathrm{final}}\mid A)>0
\]

4. 随机置换/打乱 reasoning 后性能下降；
5. 错误 reasoning 干预会因果改变预期结构；
6. OOD composition/prototype 下仍保持优势。

否则应把贡献写为序列建模或 base distribution，而不是“材料推理”。

### 3.4 物理数据、轨迹与能量引导

#### 真正机会

- 稳定终点之外的非平衡区域；
- 能量、力与应力的联合监督；
- 真实弛豫轨迹而非人工加噪；
- active learning 覆盖高力、高能和不确定区域；
- 多保真 oracle 选择。

#### 常见混淆

\[
\text{data score}
\neq
\text{physical force}
\neq
\text{optimizer trajectory}
\]

轨迹数据可以改善局部修正，但不自动赋予跨 basin 搜索能力。  
若加入 force 后只减少弛豫步数，却不增加独立低能 basin，方法是更好的 relaxer，而不是更好的 CSP searcher。

### 3.5 RL 与后训练

#### 已经被覆盖的基本叙事

截至 2026 年，以下组合均已有直接先例：

- 晶体生成 + 多目标 RL；
- Diffusion/Flow + energy/force reward；
- inference-time RL；
- 固定组成 CSP + GRPO；
- coverage-preserving reward；
- 分子晶体 Flow + RL alignment；
- 连续 SUN/cSUN reward。

因此，“使用 GRPO 让晶体更稳定”不再构成主贡献。

#### 更深的问题

单点 energy reward 可能导致：

\[
q_\theta(s\mid A)
\rightarrow
\delta_{s=s^*_{\mathrm{evaluator}}}
\]

但 CSP 需要多个低能 basin。真正问题是：

\[
\max_q
\quad
\text{quality}
+
\text{basin coverage}
-
\text{oracle cost}
\]

需要集合级目标、archive、reward-proportional sampling 或其他保持多模态的方法。

### 3.6 Benchmark、新颖性与动力学稳定

这一问题簇正在改变领域最基本的证据标准：

- StructureMatcher 命中不等于完整多晶型发现；
- 随机 split 可能包含同组成/同原型泄漏；
- 数据库未匹配不等于结构新颖；
- 元素替换体可能被宽松 novelty 计为新结构；
- 几何/热力学通过不等于无虚频；
- 单一 MLIP 排序可能被生成策略利用。

这些工作说明，评价论文不是“配套工作”，而是决定模型 claim 是否成立的核心研究。

---

## 4. 当前最拥挤的论文故事

### 故事 A：新的 backbone 在 MP-20 提分

缺陷：

- 数据规模小且任务已高度饱和；
- 单参考 Match Rate 可能奖励泄漏；
- 不能证明多势阱搜索；
- 微小增益容易由训练和容差解释。

只有当新方法改变表示、计算复杂度或 OOD 能力，且通过多晶型和预算审计，才可能升级。

### 故事 B：对称性约束提高有效性

缺陷：

- 有效性提升可能只是缩小答案空间；
- 对称破缺结构被排除；
- 需要报告可达 basin 上限，而不只是合法率。

### 故事 C：LLM 会化学推理，所以给 Diffusion 提供 proposal

缺陷：

- 没有可观察 reasoning 变量；
- 检索/小模型/warm start 未排除；
- 给定 composition 时 LLM 的组成优势消失；
- Diffusion 与 LLM 可能重复生成同一对象。

### 故事 D：去噪过程等价于沿势能面稳定化

缺陷：

- score 与 force 不相等；
- 随机加噪不是真实不稳定结构分布；
- 力下降不代表跨 basin 搜索；
- 需要轨迹、干预和独立物理 oracle。

### 故事 E：GRPO + energy reward 实现自提升

缺陷：

- 已有多项直接工作；
- reward hacking 和模式坍缩；
- 自生成样本回训不等于获得新科学信息；
- 若没有主动 DFT/实验反馈，只是在固定 evaluator 上自适应。

### 故事 F：未匹配数据库，因此发现新材料

缺陷：

- 可能是训练重复、同原型、元素替换或容差效应；
- 新颖性、稳定性、性质和可合成性是四个不同 claim；
- 必须拆分 novelty 层级。

---

## 5. 当前项目原叙事的严格审计

原始表达：

> “LLM + Diffusion + Stochastic Interpolants + GRPO，通过反馈和物理轨迹自提升，给定组成后生成更稳定晶体。”

### 5.1 What 不充分

“更稳定”可能指：

- 初始最大力更低；
- 弛豫后能量更低；
- \(E_{\mathrm{hull}}\) 更低；
- 无虚频；
- 更接近数据库 reference；
- 固定预算下找到更多低能多晶型。

这些目标互不等价。

### 5.2 Why 容易变成 benchmark 动机

若只是现有模型分数还不够高，缺少科学问题。  
更强 Why 是：

> 单参考恢复与样本级 energy optimization 都无法表达有限预算多势阱发现，而且可能主动损害候选覆盖。

### 5.3 How 目前模块重叠

- LLM 和 Diffusion 都在生成结构；
- SI 与 Diffusion 都是连续生成路径；
- GRPO 只提供优化器，不定义正确 reward；
- 轨迹数据主要支持局部修正，不自动支持全局搜索。

### 5.4 直接新颖性冲突

主索引中的 FlowLLM、CrysLLMGen、OMatG、Chemeleon2、OMatG-IRL、PackFlow 和 CrystalGRPO 已覆盖多个组件组合。  
因此方法名组合不能作为贡献。

### 5.5 升格后的问题

> 给定组成和有限物理评估预算，生成模型能否像 CSP 搜索算法一样发现多个不同低能势阱，同时保留 amortized efficiency？

形式化为：

\[
\max_\pi
\mathbb E
\left[
\sum_j
w_j
\mathbf 1\left(
\exists s_i\in\mathcal S_B:
R(s_i)\in\mathcal B_j
\right)
\right]
\]

其中 \(\mathcal S_B\) 是预算 \(B\) 下产生并评估的候选集合。

### 5.6 方法只应从职责推出

- 离散/LLM proposal：不同 basin family 之间的概率分配；
- 连续生成器：给定 family 的周期几何实现；
- 轨迹/force 模块：basin 内局部物理修正；
- archive/集合级目标：防止 energy reward 坍缩；
- 多保真 oracle：控制成本与 evaluator 风险。

### 5.7 四个核心假设

1. **轨迹数据改善局部修正，而不仅是增加数据量；**
2. **basin-aware set objective 优于 energy-only reward；**
3. **离散全局假设对最终 basin 有新增信息；**
4. **改进跨 MLIP/DFT 成立，不是 evaluator exploitation。**

任何一个失败，都应收窄主张或删除相应模块。

---

## 6. 逐篇压缩审计表

| 年份 | 论文 / 报告 | 角色 | 真正贡献 | 最危险的替代解释 |
|---:|---|---|---|---|
| 2021 | [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/cdvae.md) | 开山/任务坐标系 | 问题开拓、周期表示、基准基础设施三项贡献都较强；具体生成器会被替换，但它确立的任务坐标系长期存在。 | 增益可能主要来自更合适的周期等变表示、较强图网络和后处理，而非 VAE 潜变量或所谓物理去噪本身。 |
| 2023 | [Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/diffcsp.md) | 任务形式化/机制 | 对固定组成晶体生成的数学形式化与等变机制贡献强，是后续 conditional CSP 的核心基线。 | 提升可能主要来自分数坐标、联合训练和更强等变 backbone，而不是扩散范式本身。 |
| 2024 | [Space Group Constrained Crystal Generation](../papers/diffcsppp.md) | 形式化/机制 | 空间群约束的数学分解具有可复用性；模型增益属于强机制贡献而非新科学问题。 | 性能提升可能只是 oracle 条件显著降低了任务熵，并非模型更懂晶体。 |
| 2024 | [FlowMM: Generating Materials with Riemannian Flow Matching](../papers/flowmm.md) | 几何机制 | 将通用流形 flow matching 扎实迁移到晶体，属于机制与效率贡献。 | 增益可能主要来自更好的 base distribution、solver 或训练超参，而非 Riemannian flow matching 本身。 |
| 2023 | [MatterGen: a generative model for inorganic materials design](../papers/mattergen.md) | 系统/规模/验证 | 高价值系统、规模与验证贡献；不是纯算法开山，但把生成式材料设计推进到更完整证据链。 | 相当部分提升可能来自更大数据、更多算力、更强筛选和候选选择，而不是联合扩散架构。 |
| 2025 | [Open Materials Generation with Stochastic Interpolants](../papers/omatg.md) | 统一机制 | 生成机制与统一框架贡献明确；“SI 用于晶体”此后已不再构成新颖点。 | 收益可能来自更广超参空间、离散流实现和评测调优，而非 SI 统一性本身。 |
| 2025 | [A Periodic Bayesian Flow for Material Generation](../papers/crysbfn.md) | 概率机制/效率 | 周期 BFN 的数学适配与熵条件属于明确机制创新。 | 优势可能来自计算口径、checkpoint 选择或网络容量，非 BFN 概率机制。 |
| 2025 | [CrystalDiT: A Diffusion Transformer for Crystal Generation](../papers/crystaldit.md) | 架构/训练策略 | 清晰的简化架构与训练策略贡献，但没有重新定义晶体生成问题。 | 提升可能来自 checkpoint selection、解码策略和评测调参，而不是 DiT 架构本身。 |
| 2026 | [Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](../papers/sbcd.md) | 新近机制预印本 | 潜在强机制贡献，但当前仍是需要严格审计的新预印本。 | 增益可能来自更灵活的空间群搜索或额外容量，而非“对称破缺物理”。 |
| 2025 | [SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](../papers/symmcd.md) | 表示/机制 | 对称表示和生成机制贡献较强，科学问题仍是已有对称有效性问题。 | 结果改善可能主要来自降维与硬约束，而非对称变换表示的泛化。 |
| 2025 | [WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/wyckoffdiff.md) | 表示/离散机制 | 表示、离散生成和对称评价三项贡献较清楚。 | 结果可能来自压缩搜索空间与后处理，而非离散扩散；新指标可能偏好相同表示族。 |
| 2025 | [Wyckoff Transformer: Generation of Symmetric Crystals](../papers/wyckoff-transformer.md) | 表示/高效自回归 | 压缩表示和快速对称生成贡献明确，算法本身较工程化。 | 优势可能主要由输出空间更小和不计算连续坐标造成。 |
| 2026 | [Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist](../papers/haco-maskgxt.md) | 跨域机制迁移/系统 | MaskGXT 的离散并行机制有实质贡献；HACO 是系统/过程贡献，证据标准与模型贡献不同。 | 收益可能由人工加入的晶体先验、更多搜索实验和分层采样造成，而不是 MaskGIT 或 AI co-scientist。 |
| 2023 | [Crystal Structure Generation with Autoregressive Large Language Modeling](../papers/crystallm.md) | 表示/系统先例 | 证明 CIF 自回归生成可行，属于重要先例与系统整合；表示的非唯一性后来由 Mat2Seq 更直接处理。 | 模型可能主要记忆语法、元素替换和常见原型；MCTS 提升也可能完全来自外部 evaluator。 |
| 2025 | [Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/mat2seq.md) | 表示/形式化 | 强表示贡献：把 LLM 晶体生成中的数学不适定性显式提出并解决。 | 改进可能来自去重、标准化和降低序列熵，而不是 LM 生成能力。 |
| 2024 | [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/crystal-text-llm.md) | 规模/能力实证 | 规模实证和灵活文本接口贡献强，数学表示贡献弱于 Mat2Seq。 | 70B 优势可能纯粹来自容量和更低训练损失；稳定候选可能是数据库原型的近邻或替换。 |
| 2024 | [FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](../papers/flowllm.md) | 结构化组合 | A+B 接口较清楚：LLM 负责非平凡起点，flow 负责连续运输；属于较好的结构化组合。 | LLM 可能只是昂贵的原型采样器；简单 nearest-neighbor、元素替换或小 Transformer base 可能等效。 |
| 2025 | [LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](../papers/crysllmgen.md) | 故事整合/工程 | 有实用价值的混合工程，但相比 FlowLLM，数学分工与不可替代性证据较弱。 | 提升可能完全来自更好的组成先验与 diffusion 后处理；LLM 连续结构输出可能没有贡献。 |
| 2025 | [Siamese Foundation Models for Crystal Structure Prediction](../papers/dao.md) | 数据+双模型系统 | 数据扩展与生成—预测双模型系统贡献强，纯架构新颖性次之。 | 提升可能主要来自更多非平衡数据和更大模型，而不是 Siamese 架构；能量引导也可能只优化 evaluator。 |
| 2024 | [Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models](../papers/omat24.md) | 数据基础设施 | 数据规模和开放基础设施贡献极强，是生成后筛选与轨迹监督的重要底座。 | 模型成功可能主要来自巨大数据与计算，而非辅助目标；在特定体系上专用势可能更可靠。 |
| 2025 | [LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling](../papers/lemat-traj.md) | 数据标准化 | 大型轨迹数据整合贡献强；对生成方法的意义取决于是否利用顺序、力与盆地信息。 | 收益可能只是更多结构覆盖，而不是“轨迹顺序”信息；随机打乱轨迹也许同样有效。 |
| 2025 | [MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials](../papers/mp-aloe.md) | 科学分层数据 | 数据采样策略与科学鲁棒性贡献强，直接支持“Science 决定能力不能丢”的原则。 | 优势可能来自统一高质量泛函和数据清洗，而非主动学习策略。 |
| 2025 | [Accelerating Inverse Materials Design Using Generative Diffusion Models with Reinforcement Learning](../papers/matinvent.md) | 目标对齐/系统 | 目标对齐与低评估预算系统贡献明确，但“RL 用于晶体设计”已不是空白。 | 改进可能来自反复筛选和 best-of-N，而非策略学习；目标候选可能钻预测器漏洞。 |
| 2025 | [Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](../papers/chemeleon2.md) | 多目标对齐 | 多目标 RL 工程与目标错位讨论有价值；在 2026 已构成必须超越的直接先例。 | 提升可能由 novelty 计算口径、更多采样和 reward shaping 造成；生成物仍可能是 substitution-derived。 |
| 2026 | [Open Materials Generation with Inference-Time Reinforcement Learning](../papers/omatg-irl.md) | 连续时间策略优化 | 将 policy gradient 推到 velocity-only flow 的技术贡献清晰；科学目标仍较窄。 | 收益可能来自 annealing schedule、额外随机采样或局部搜索，而非 RL 更新。 |
| 2026 | [PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment](../papers/packflow.md) | 物理对齐/系统 | 端到端 CSP 流程和物理后训练证据较强，是无机晶体路线的重要邻域先例。 | RL 可能只是更强局部弛豫初始化，或过拟合特定 MLIP；低能集中可能降低其他多晶型覆盖。 |
| 2026 | [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](../papers/crystalgrpo.md) | 目标重定义/直接先例 | 问题意识非常重要：首次明确把 energy 与 coverage 冲突放到 flow-RL；但目标仍偏 benchmark-aligned。 | 改善可能来自直接使用测试式参考相似度 reward，使模型更会 benchmark matching，而非更会 CSP 搜索。 |
| 2025 | [Establishing Baselines for Generative Discovery of Inorganic Crystals](../papers/establishing-baselines.md) | 强基线 / 评价校准 | 它改变了基线与证据标准：高分不再足以，必须证明相对简单 proposal 的净增益，并把生成、筛选和数据库先验拆开。 | 观察到的差异可能主要来自方法访问的数据库先验不同、候选去重规则不同，或 MLIP 对某些生成分布更友好。 |
| 2025 | [All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation](../papers/structure-matches-glitter.md) | Benchmark 纠偏 / 多晶型评价 | 它重新定义了什么证据才算 CSP/生成进步，是问题与评价层贡献，而不是又一个模型增量。 | 排名变化也可能部分来自新划分更 OOD、训练分布发生变化，而不完全是旧指标错误；参考数据库本身仍是不完整观测。 |
| 2025 | [LeMat-GenBench: A Unified Benchmark for Generative Materials Models](../papers/lemat-genbench.md) | 统一生成 Benchmark | 它提供统一实验基础设施和多目标证据标准，价值在可复现比较而非提出新的科学模型。 | 一些 Pareto 权衡可能由模型训练预算、数据规模、采样温度和后处理不同造成，而非生成范式的内在限制。 |
| 2026 | [Are Crystal Generative Models Truly Discovering Novel Structures?](../papers/substitution-novelty.md) | 新颖性审计 / 替换派生 | 它改变了 novelty 的操作定义，并迫使论文把“新组成”“新结构原型”“新性质”和“新可合成材料”分开。 | 模型可能在已知拓扑上提出科学上有价值的新化学组成；因此 substitution-derived 不等于无价值，只是否定“新结构原型”的强声明。 |
| 2025 | [cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation](../papers/csun.md) | 连续评价 / 可优化 Reward | 它是评价和优化接口层贡献，解决了二元指标不连续，但没有解决每个分量是否与真实科学目标一致。 | 性能改善可能只是 reward shaping 更易优化，而非最终材料效用更高；连续相似度仍可能遗漏拓扑替换和 evaluator 偏差。 |
| 2025 | [PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability](../papers/phononbench.md) | 动力学稳定 Benchmark | 它把动力学稳定正式加入生成评价，是科学证据层的重要扩展，并暴露当前 SUN/热力学筛选的盲区。 | 虚频可能来自 MLIP、超胞、数值精度或未完全弛豫，而非结构真实不稳定；有限温度非谐效应也可能稳定软模。 |
| 2026 | [PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals](../papers/phononscore.md) | 多保真动力学评分 | 它主要改变计算效率和 evaluator 接口，使动力学信号有机会进入大规模生成循环。 | 排序提升可能来自与 benchmark 使用同源势模型或数据；模型会学习化学体系捷径而非真实曲率。 |
| 2022 | [Flow Matching for Generative Modeling](../papers/flow-matching.md) | 连续生成原语 | 它提出通用训练原语和路径设计坐标系，属于机制型开创工作，后续晶体 flow 多建立在此。 | 增益可能来自更好的路径/数值求解器，而非“flow”本身；与扩散比较易混入 backbone、步数和训练预算。 |
| 2023 | [Flow Matching on General Geometries](../papers/riemannian-flow-matching.md) | 流形生成原语 | 它改变表示和生成原语，使算法尊重状态空间；对晶体是方法基础而非完整科学答案。 | 收益可能来自更正确的周期表示，而非 flow matching；对于晶格商空间，简单流形近似仍可能遗漏等价晶胞。 |
| 2023 | [Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](../papers/stochastic-interpolants.md) | 随机桥与生成统一框架 | 它提供新的数学坐标系，属于开山式机制框架；应用论文的价值取决于是否提出任务特有 bridge。 | 实际收益可能来自特定 bridge/solver，而非统一理论本身；在应用中“用了 SI”常只是重新参数化已有路径。 |
| 2023 | [GFlowNet Foundations](../papers/gflownet-foundations.md) | 多模态奖励比例采样 | 它改变了优化目标：从 argmax 转为与 reward 成比例的多模态采样，是多解科学设计的重要抽象。 | 在连续高维晶体中，离散构造和终点归一困难；观察到的多样性也可能来自温度/熵正则，而非 flow matching。 |
| 2022 | [Diffusion Posterior Sampling for General Noisy Inverse Problems](../papers/diffusion-posterior-sampling.md) | 生成先验 + 测量似然 | 它建立了“生成模型是先验，不是答案”的重要逆问题接口。 | 重建提升可能来自强图像先验，后验近似未必校准；错误前向模型会把样本推向伪解。 |
| 2022 | [MaskGIT: Masked Generative Image Transformer](../papers/maskgit.md) | 并行迭代离散生成 | 它改变离散生成算子和采样并行性，属于可复用机制贡献。 | 速度/质量增益可能依赖 VQ tokenizer 和图像网格局部性；置信度未必等于晶体物理重要性。 |
| 2023 | [Training Diffusion Models with Reinforcement Learning](../papers/ddpo.md) | 扩散策略优化 | 它建立了 diffusion 后训练的通用策略优化接口，但没有解决 reward 是否正确。 | 提升可能是 evaluator hacking、prompt-specific 过拟合或多样性丧失；相同样本量的 rejection sampling 可能足够。 |
| 2026 | [Stepwise Credit Assignment for GRPO on Flow-Matching Models](../papers/stepwise-flow-grpo.md) | 时间步信用分配 | 它提供时间步 credit 原语，是 RL 优化几何贡献，不是领域科学贡献。 | 改进可能来自额外中间 evaluator 调用或更密集监督，而非 credit 公式；“早全局晚细节”可能只是特定模型现象。 |
| 2025 | [Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards](../papers/b2-diffurl.md) | 稀疏奖励 / 分支探索 | 它提供稀疏奖励下的反事实分支和反向课程思想，属于优化机制增量。 | 收益可能只是更多 best-of-N 样本或课程训练；分支数增加带来的计算优势需公平折算。 |

---

## 7. 哪些论文最值得反复读

### 为了学习问题定义

- CDVAE；
- DiffCSP；
- GFlowNet Foundations；
- All That Structure Matches Does Not Glitter。

### 为了学习表示与生成机制

- Mat2Seq；
- Flow Matching on General Geometries；
- FlowMM；
- Stochastic Interpolants；
- MaskGIT / MaskGXT。

### 为了学习系统与证据链

- MatterGen；
- OMat24 / LeMat-Traj；
- Establishing Baselines；
- LeMat-GenBench；
- PhononBench。

### 为了识别当前 idea 的直接竞争

- FlowLLM；
- CrysLLMGen；
- DAO；
- Chemeleon2；
- OMatG-IRL；
- PackFlow；
- CrystalGRPO。

---

## 8. 审计后的研究纪律

每提出一个新模块，必须同时回答：

1. 它修复哪个已形式化的失败模式？
2. 它输入了什么此前没有的信息？
3. 它改变了哪个随机变量、目标或搜索过程？
4. 最简单替代方案是什么？
5. 哪个实验能证明模块没有贡献？
6. 提升是否在独立 evaluator 与固定预算下存在？
7. 它会牺牲哪些模式、结构族或科学能力？
8. 结论最多能写到 benchmark、机制、物理还是实验哪一层？

只有这些问题回答清楚后，才进入大规模训练。
