# 任务—数据—输出—机制矩阵

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

这个矩阵用于强迫阅读者回答：一篇论文到底输入了什么信息、输出什么对象、从什么数据中学习、通过什么算子连接两者。  
长单元格不是为了快速排行榜，而是为了暴露论文故事中被省略的接口。

| 论文 / 报告 | 任务簇 | 数学任务 / 输出 | 数据与信息来源 | 核心算子 |
|---|---|---|---|---|
| [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/cdvae.md) | 生成基础 | 输入可为潜变量或性质条件，输出为原子种类、坐标和晶格；学习目标是稳定材料数据库分布的生成模型，而不是直接求解量子力学全局最优。 | 训练数据主要是数据库中的弛豫终态；它包含稳定结构统计规律，却几乎不包含从高能构型到势阱的真实搜索轨迹。 | 将全局结构编码到连续潜变量，预测组成与晶格，再用周期图网络估计坐标噪声分数并迭代去噪。 |
| [Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/diffcsp.md) | 条件 CSP | 输入为元素组成或原子种类集合，输出为晶格 L 与分数坐标 X；目标近似学习 p(X,L\|A)，标准评测则把样本与数据库参考结构匹配。 | 主要使用稳定结构终态数据；一个组成往往只保留一个或少量数据库参考，真实低能多晶型集合没有被完整观测。 | 分别对晶格和分数坐标构造噪声过程，使用周期 E(3) 等变网络联合去噪，使坐标表示天然适配周期边界。 |
| [Space Group Constrained Crystal Generation](../papers/diffcsppp.md) | 对称约束 | 输入为组成与可选空间群，输出满足相应晶格和 Wyckoff 约束的结构；优化仍是条件结构分布拟合。 | 依赖数据库给出的空间群/Wyckoff 标注和稳定终态，标注误差、标准化选择及低对称结构偏差会传入模型。 | 把群论约束转写成可实现的连续几何子空间，约束晶格与坐标的扩散轨迹。 |
| [FlowMM: Generating Materials with Riemannian Flow Matching](../papers/flowmm.md) | 生成基础 | 学习从 base distribution 到晶体数据分布的连续向量场；既支持 p(X,L\|A) 的 CSP，也支持联合生成 A,X,L。 | 仍以稳定数据库终态为主，训练目标是数据运输而非能量景观搜索。 | 在晶体乘积流形上构造条件概率路径和切空间向量场，用 ODE 积分生成；允许选择集中或数据启发的 base。 |
| [MatterGen: a generative model for inorganic materials design](../papers/mattergen.md) | 逆向设计 | 输入为空或性质/化学/对称条件，输出完整晶体；训练是条件生成，部署是生成—MLIP/DFT 筛选—实验验证链。 | 使用规模远大于经典 MP-20 的材料与非平衡数据；训练分布、筛选器和计算预算共同决定结果。 | 对元素类型、分数坐标和晶格设计联合扩散，使用性质 adapter 在标注较少时微调，并配套大规模验证。 |
| [Open Materials Generation with Stochastic Interpolants](../papers/omatg.md) | 生成基础 | 学习任意 base 到晶体目标分布的可调随机桥；输出条件或无条件晶体，目标仍是数据库分布生成。 | 主要来自常用材料数据库终态；插值路径由人工设定，而不是从真实弛豫/合成轨迹直接观测。 | 将 SI 的可调插值、速度场和随机性适配周期图表示，并用 discrete flow matching 处理元素。 |
| [A Periodic Bayesian Flow for Material Generation](../papers/crysbfn.md) | 生成基础 | 在参数分布空间中逐步聚合带噪观测，学习周期变量、晶格和元素的生成更新；支持 CSP 与 de novo。 | 使用常见稳定晶体 benchmark；并未直接观测物理轨迹，效率主要是网络前向次数。 | 构造周期 Bayesian flow，分析其非单调熵变化，并以熵而非单纯时间作为网络条件。 |
| [CrystalDiT: A Diffusion Transformer for Crystal Generation](../papers/crystaldit.md) | de novo 生成 | 联合建模完整晶体的扩散过程，主要面向 de novo；目标是提高稳定、唯一、新颖的联合成功率。 | 基于 MP-20 等数据库与代理稳定性评估；SUN 对去重、训练集版本和 MLIP 很敏感。 | 把所有晶体 token 放入统一 attention，利用元素周期表位置编码，并用平衡 checkpoint 选择避免只优化单一指标。 |
| [Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](../papers/sbcd.md) | 对称生成 | 联合状态含连续结构变量与离散空间群，跳扩散过程在群之间转移并生成完整晶体规格。 | 在 MP-20、MPTS-52 等数据库上训练；所谓“物理启发”来自对称破缺类比，并非真实温压相变轨迹。 | 以 Markov jump 处理离散群转移、连续扩散处理几何，形成混合离散—连续随机过程。 |
| [SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](../papers/symmcd.md) | 对称生成 | 输出不对称单元及其对称操作，再展开为完整晶体；目标是学习真实结构与对称信息的联合分布。 | 训练依赖结构标准化、空间群解析和 Materials Project 子集；对无序、缺陷或近似对称结构适用性有限。 | 以可解释的对称变换表示减少冗余原子，扩散生成 asymmetric unit 与群作用。 |
| [WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/wyckoffdiff.md) | 对称离散生成 | 输入噪声离散状态，输出元素—Wyckoff 占位等 protostructure，再经下游坐标实现/弛豫得到晶体。 | 训练依赖可靠的 Wyckoff 分解；连续自由参数和后续几何质量可能不在离散模型内充分解决。 | 设计适配集合/占位的离散扩散网络，硬编码对称合法性，并用新的嵌入距离评估生成分布。 |
| [Wyckoff Transformer: Generation of Symmetric Crystals](../papers/wyckoff-transformer.md) | 对称离散生成 | 输入空间群等条件，输出 Wyckoff/元素 token 集合；下游还需坐标实例化和弛豫。 | 数据库 Wyckoff 标注形成高度不均衡的离散词表；高对称结构可能被过度代表。 | 移除位置编码并随机 token 顺序逼近集合自回归，利用 Wyckoff 压缩减少序列长度。 |
| [Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist](../papers/haco-maskgxt.md) | AI co-scientist/CSP | 给定组成，离散化完整结构 token；训练随机 mask 恢复，推理从全 mask 并行预测并按置信度逐步固定。 | 基于 MP-20、MPTS-52 及 polymorph-aware split；坐标分箱和 sub-bin refinement 决定误差下限。 | 迁移 MaskGIT 的并行迭代解码，加入周期标签平滑、晶体对称 token、空间群分层采样与坐标细化。 |
| [Crystal Structure Generation with Autoregressive Large Language Modeling](../papers/crystallm.md) | LLM 生成 | 输入为组成/空间群提示，输出 CIF token 序列；最大似然学习 p(CIF\|condition)，MCTS 版本再用能量代理引导搜索。 | 训练来自数百万 CIF；同一物理结构可能有多种文本表示，数据库来源、标准化和去重决定模型看到的规律。 | 将数值字段离散为 token，使用自回归 Transformer 学习语法与结构统计，并用外部能量模型给树搜索评分。 |
| [Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/mat2seq.md) | LLM 表示 | 输入为晶体等价类，输出规范序列；核心目标先是定义近似单射/规范化映射，再用 LM 学习该序列分布。 | 仍使用数据库终态，但数据表示经过规范化；规范化失败、数值容差和边界退化会影响唯一性。 | 先寻找旋转等变、周期不变的规范晶胞，再确定原子排序与数值序列，使等价描述尽量折叠为一个表示。 |
| [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/crystal-text-llm.md) | LLM 生成 | 最大似然微调文本晶体分布；输入可为提示或部分结构，输出完整文本结构，再由 MLIP/DFT 判断亚稳性。 | 依赖文本化数据库与大模型预训练；训练集重复、元素替换和原型模式可能被语言模型记忆。 | 用 LLaMA 等预训练模型直接自回归生成结构文本，并比较模型规模与条件任务。 |
| [FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](../papers/flowllm.md) | LLM+Flow | LLM 学 p_base(A,X,L)，flow 学从 LLM base 到目标数据分布的条件运输；两阶段输出完整晶体。 | LLM 和 flow 都由相同或相近数据库训练，base 可能已经包含目标记忆；独立训练使贡献可拆但也可能重复建模。 | 把 LLM 明确放在 base distribution 接口，而非宣称其直接完成连续几何；flow 专注修正坐标与晶格。 |
| [LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](../papers/crysllmgen.md) | LLM+Diffusion | 两模型独立训练；采样时 LLM 提供 A,X,L，扩散从中间噪声层 refinement X,L，形成经验性的两阶段条件生成。 | 两阶段共享数据库规律；LLM 组成被直接保留，因此 de novo 的 compositional validity 可能主要由第一阶段决定。 | 把 LLM 样本映射到扩散时间步，固定离散元素并修复几何；核心接口是 warm start 与变量冻结。 |
| [Siamese Foundation Models for Crystal Structure Prediction](../papers/dao.md) | 条件 CSP/物理数据 | DAO-P 学能量/性质，DAO-G 学 p(X,L\|A)；预训练阶段借助预测器构造/弛豫数据，推理阶段可做能量引导。 | 引入大量稳定与不稳定构型及模型生成的弛豫数据；数据规模、质量、势模型偏差和预训练任务共同作用。 | 双模型互相提供表征与监督：预测器近似势能，生成器扩展候选分布；采用 pretrain-finetune 跨 benchmark。 |
| [Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models](../papers/omat24.md) | 数据/MLIP | 输入原子结构，监督能量、力、应力等；模型目标是学习 DFT 近似器，不直接生成晶体。 | DFT 结构由多种采样策略产生，包含大量非平衡和高力区域；但仍受泛函、元素覆盖和采样策略约束。 | 以规模化 DFT 数据和 EquiformerV2 训练建立通用 MLIP，并研究数据混合、模型规模与辅助去噪。 |
| [LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling](../papers/lemat-traj.md) | 数据/轨迹 | 输入结构，输出能量/力监督或轨迹序列；可用于 MLIP、局部修正器和生成路径建模。 | 聚合多个数据库和 PBE/PBEsol/SCAN/r2SCAN 等泛函；异质性既扩大覆盖，也引入不可直接比较的系统偏差。 | 标准化 schema、过滤质量、保留轨迹上下文，并提供可扩展抓取工具。 |
| [MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials](../papers/mp-aloe.md) | 数据/主动学习 | 主动学习选择 DFT 查询点，模型学习能量/力；目标是扩大物理势的可信域。 | 采样主要由主动学习策略决定，覆盖高能、高力和极端形变；r2SCAN 一致性较好但计算与元素分布仍不均。 | 通过模型不确定性/失败区域驱动查询，迭代扩充非平衡数据并进行多类鲁棒性 benchmark。 |
| [Accelerating Inverse Materials Design Using Generative Diffusion Models with Reinforcement Learning](../papers/matinvent.md) | RL 逆向设计 | 把扩散采样看作策略，黑盒性质预测器给终点 reward；优化期望奖励并维持生成可行性。 | 训练/奖励依赖性质代理模型；约千次性质评估的预算主张与 oracle 成本定义相关。 | 通用 RL wrapper 对不同 diffusion backbone 和目标函数进行在线更新，支持多目标权衡。 |
| [Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](../papers/chemeleon2.md) | RL de novo | 以 denoising trajectory 为策略，组内相对优势更新；reward 组合稳定、novelty、diversity 与性质。 | 奖励由结构匹配和 ML 代理构成；训练分布与 novelty reference 决定何为新颖。 | GRPO 在无需价值网络情况下对多目标终点奖励优化，并通过相对比较与多样性项抑制坍缩。 |
| [Open Materials Generation with Inference-Time Reinforcement Learning](../papers/omatg-irl.md) | RL/Flow | 把随机化连续生成动态视为策略，使用终点能量 reward 估计速度场参数梯度；也可优化采样日程。 | 以预训练 OMatG 和代理能量为基础；奖励仍是单点能量而非多晶型集合效用。 | 对 ODE 引入可控 SDE 扰动以保留探索和可微 log-prob/策略梯度，推理时或轻量更新速度场。 |
| [PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment](../papers/packflow.md) | 分子晶体 CSP | 输入分子图，输出晶体 packing 和晶格；flow proposal 经 RL 对齐后再弛豫、晶格能排序。 | 数据来自实验分子晶体和 MLIP 代理；盲测个例更接近真实 CSP，但体系数量有限。 | lattice-aware flow 负责候选，能量/力 reward 后训练把概率质量集中到物理有利区域。 |
| [CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](../papers/crystalgrpo.md) | RL/条件 CSP | 以联合坐标—晶格 SDE 为策略，reward 组合 MACE 能量、StructureMatcher recovery、轨迹正则与组内 coverage advantage。 | MP-20/MPTS-52 参考结构作为目标；coverage 指的是参考集合/样本覆盖，不等于未知真实低能盆地全集。 | CrystalGRPO-Q 优先单样本命中，CrystalGRPO-C 用全轨迹正则和 coverage-aware advantage 维持 Top-20。 |
| [Establishing Baselines for Generative Discovery of Inorganic Crystals](../papers/establishing-baselines.md) | evaluation | 在统一候选预算、稳定性评估器与后筛选设置下，比较简单化学/原型基线和深度生成模型的候选效用。 | 电荷平衡组成/原型、已知材料离子替换、VAE/LLM/扩散生成候选，以及统一机器学习势或稳定性筛选。 | 贡献不是新生成器，而是构造危险且廉价的反事实基线，并要求所有方法共享相同后处理，从而分离 proposal 质量与 evaluator 质量。 |
| [All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation](../papers/structure-matches-glitter.md) | evaluation | 重新设计晶体结构预测/生成的划分与指标，使评价更接近参考结构集合覆盖和连续结构误差，而非单个阈值命中。 | 多数据集的重复/多晶型统计、标准生成模型输出、polymorph-aware split，以及不同匹配容差下的评估结果。 | 通过数据去重、按组成/多晶型组织的划分、集合级匹配和连续误差指标，显式暴露 reference multiplicity 与阈值敏感性。 |
| [LeMat-GenBench: A Unified Benchmark for Generative Materials Models](../papers/lemat-genbench.md) | evaluation | 在统一数据、采样和 evaluator 下，对代表性生成模型进行多维度画像，而非只给单一排行榜。 | 多个公开晶体数据集、约十二类生成模型输出、统一结构处理和稳定性/新颖性/多样性计算工具。 | 标准化 evaluation harness，把模型质量拆成多条 Pareto 轴，并提供可复现代码以减少实现差异。 |
| [Are Crystal Generative Models Truly Discovering Novel Structures?](../papers/substitution-novelty.md) | evaluation | 将生成结构分成训练重复、元素替换可导出、已知原型复用和更强意义上的结构新颖类别。 | 代表性生成模型样本、训练数据库、结构匹配/原型归一化、元素映射或替换搜索，以及稳定性过滤结果。 | 把元素身份与几何/拓扑骨架分离，检查是否存在从训练结构经元素重标记即可获得的生成结构。 |
| [cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation](../papers/csun.md) | evaluation | 为稳定性、唯一性和新颖性定义连续分量，再组合成连续候选/集合质量指标。 | 晶体生成样本、稳定性代理、结构距离或相似度、训练/参考数据库及不同阈值下的 SUN 结果。 | 用平滑映射替代硬阈值，保留距离边界的信息，并使 reward 对小变化更连续。 |
| [PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability](../papers/phononbench.md) | evaluation | 在统一弛豫与声子计算协议下，对多个生成模型的大规模样本计算或近似动力学稳定率。 | 多个生成模型候选、统一 MLIP/弛豫设置、声子谱或最低频率标签，以及部分交叉验证。 | 增加二阶局部势能面信息：由能量/力的一阶筛选上升到振动模态与曲率审计。 |
| [PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals](../papers/phononscore.md) | evaluation | 学习或组合多层精度信号，对候选的动力学稳定性进行成本可控的评分与优先级排序。 | 生成晶体、不同精度的声子/曲率标签、结构与势能特征，以及高保真验证子集。 | 以 coarse-to-fine/multi-fidelity 方式融合廉价代理和昂贵声子标签，在固定预算下优先查询最有价值候选。 |
| [Flow Matching for Generative Modeling](../papers/flow-matching.md) | cross-domain | 给定数据分布与基分布，学习 ODE 向量场，使基分布沿选定概率路径运输到数据分布。 | 通用图像等生成数据；训练时从条件概率路径采样中间状态与解析条件向量场。 | 通过 conditional flow matching 将边缘向量场回归化为可采样条件目标；OT 路径可缩短运输并改善训练/采样。 |
| [Flow Matching on General Geometries](../papers/riemannian-flow-matching.md) | cross-domain | 在黎曼流形上定义条件概率路径、切向量场和测地/近似测地运输，学习流形内的生成流。 | 球面、环面、旋转群等合成/实际数据，以及可计算的流形操作。 | 将向量场限制在切空间并使用流形几何定义插值和 ODE，从表示层消除一部分无效状态。 |
| [Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](../papers/stochastic-interpolants.md) | cross-domain | 构造连接源分布和目标分布的随机过程，学习使其边缘分布成立的 drift、score 或相关场。 | 理论分布及图像等实验；训练样本来自端点和插值噪声，而非真实物理轨迹。 | 把 bridge、噪声调度与可逆/随机动力学置于统一公式中，使研究者可在 deterministic 与 stochastic 采样间连续选择。 |
| [GFlowNet Foundations](../papers/gflownet-foundations.md) | cross-domain | 在有向构造图上学习前向/后向流，使终止对象的边缘概率与正奖励成比例。 | 组合对象构造轨迹、终点奖励；可用 off-policy 采样与不同 flow consistency 目标训练。 | 把局部构造转移的流守恒与终点奖励连接，令多个生成路径的流量聚合到对象概率。 |
| [Diffusion Posterior Sampling for General Noisy Inverse Problems](../papers/diffusion-posterior-sampling.md) | cross-domain | 从后验 p(x\|y) 近似采样，其中 p(x) 由扩散模型表示，p(y\|x) 由已知前向测量模型给出。 | 图像先验数据、观测 y、已知线性/非线性噪声前向算子。 | 在反向扩散中叠加近似的 measurement consistency 梯度，以贝叶斯分解连接先验与观测。 |
| [MaskGIT: Masked Generative Image Transformer](../papers/maskgit.md) | cross-domain | 从全掩码 token 网格出发，多轮并行预测并固定高置信 token、重掩码低置信 token。 | 图像离散 tokenizer 产生的 token 网格与类别条件。 | 用迭代并行 refinement 替代左到右生成，把置信度调度变成生成顺序。 |
| [Training Diffusion Models with Reinforcement Learning](../papers/ddpo.md) | cross-domain | 将每个去噪转移视为策略动作，以终点 reward 估计策略梯度，并保持与预训练生成分布的约束。 | 预训练文生图扩散、图像 reward 模型或可计算目标，以及采样轨迹。 | 推导 denoising diffusion policy optimization，把终点黑盒 reward 反传为多步策略更新。 |
| [Stepwise Credit Assignment for GRPO on Flow-Matching Models](../papers/stepwise-flow-grpo.md) | cross-domain | 用中间预测或 reward gain 构造 stepwise advantage，再以 GRPO 式相对优势更新流模型。 | 图像 flow-matching 模型、终点/中间 reward 评估和多条组内采样轨迹。 | 把总奖励分解为时间局部增量，为每一步估计更有针对性的 advantage。 |
| [Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards](../papers/b2-diffurl.md) | cross-domain | 在扩散轨迹的不同位置分支采样多个后续结果，并渐进地把 reward 信号向更早时间传播。 | 预训练图像扩散、稀疏 reward 与分支采样轨迹。 | 用共享前缀的反事实分支估计中间状态价值，再按反向课程逐步扩展优化区间。 |

## 读表时必须检查

### 信息可得性

若方法推理时使用了：

- 数据库原型；
- reference space group；
- composition-specific 检索；
- 额外 MLIP 调用；
- 大规模预训练语料；

这些都是输入信息，不能被归为纯算法能力。

### 输出等价性

晶体输出需要对原子置换、周期平移、旋转和等价晶胞归一。  
序列、坐标、Wyckoff、图或 latent 都只是同一物理对象的表示。

### 数据—claim 对齐

- 稳定终点不能直接监督跨 basin 路径；
- 随机加噪不是物理弛豫轨迹；
- 能量/力数据不提供完整合成条件；
- 实验数据库不是无偏物理分布；
- self-generated reward 数据只反映 evaluator。

### 机制可替代性

每个复杂算子都应与最简单替代比较：

- 生成 ↔ 检索/替换/随机；
- LLM ↔ 小 Transformer；
- RL ↔ rejection/best-of-N；
- trajectory ↔ 等量 noise；
- symmetry model ↔ 频率/规则；
- flow/SI ↔ controlled diffusion。
