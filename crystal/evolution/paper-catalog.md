# 逐篇问题、方法、结果与剩余缺口

[综述正文](README.md) · [年表](chronology.md) · [结构化引用](references.json) · [BibTeX](references.bib)

共57项去重工作。下列结果属于所列原文与协议；本文的六挑战归纳和四方向议程与原论文成果分开。

<a id="r01"></a>
## [R01] High-Pressure Phases of Silane

[原始来源](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504) · 首次已核公开：2006-04-19 · Physical Review Letters 97, 045504；2006-07-27正式发表

作者：Chris J. Pickard, R. J. Needs。

**任务：**高压硅烷的结构搜索。

**研究的问题：**难以事先知道有竞争力的晶体构型

**核心方法：**随机初始结构加第一性原理弛豫

**原文结果及适用范围：**

- 在最多至少10原子的原胞实例中找到低焓结构并研究高压相

**仍需研究：**每个新体系仍需付出物理搜索费用；没有学到跨体系生成分布

关联：C4, C5, C6；方向 C, D。

<a id="r02"></a>
## [R02] Crystal structure prediction using ab initio evolutionary techniques: Principles and applications

[原始来源](https://doi.org/10.1063/1.2210932) · 首次已核公开：2006-06-28 · Journal of Chemical Physics 124, 244704 (2006)

作者：Artem R. Oganov, Colin W. Glass。

**任务：**给定化合物的晶体结构搜索。

**研究的问题：**候选结构数量巨大，第一性原理评价昂贵，局部极小值众多

**核心方法：**进化搜索与第一性原理能量评价结合

**原文结果及适用范围：**

- 通过具体体系展示全局结构搜索的有效性；原文任务不包含现代DNG的SUN

**仍需研究：**跨化学空间的可复用生成分布与多解发现效率仍需学习

关联：C4, C5, C6；方向 C, D。

<a id="r03"></a>
## [R03] Ab initio Random Structure Searching

[原始来源](https://arxiv.org/abs/1101.3987) · 首次已核公开：2011-01-05 · Journal of Physics: Condensed Matter；2011；在线 2011-01-05；状态 published

作者：Chris J Pickard, R J Needs。

**研究的问题：**指定组成和外部条件后，怎样在极多局部极小值中找到低能结构？

**核心方法：**生成满足可选化学、距离及对称约束的随机结构，物理松弛到局部极小值，并从重复搜索积累低能结构。

**重要性：**结构搜索使晶体候选能经物理计算获得检验，亚稳结构也有实际意义。

**主要困难：**极小值数量迅速增长、盆地吸引域不等、每次第一性原理松弛昂贵。

**原文结果及适用范围：**

- 原文位置：§2 Potential energy surfaces；结构构造与约束章节；结果：明确区分随机初始态、吸引盆地和物理极小值，展示多类系统的低能结构搜索。；评价口径：固定组成/条件的物理搜索；具体势能、约束与采样预算决定结果。

**仍需研究：**计算主要针对当前体系，跨体系的快速候选分布与可复用决策知识仍需学习；相竞争稳定与局部极小值需分别判断。

关联：C2, C4, C5, C6；方向 A, C, D。

<a id="r04"></a>
## [R04] Commentary: The Materials Project: A materials genome approach to accelerating materials innovation

[原始来源](https://doi.org/10.1063/1.4812323) · 首次已核公开：2013-07-18 · APL Materials 1, 011002 (2013)

作者：Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter et al.。

**任务：**高通量材料数据与开放计算生态。

**研究的问题：**物理数据分散且逐材料计算成本高

**核心方法：**标准化高通量第一性原理计算、结构及性质数据库

**原文结果及适用范围：**

- 为结构、性质和竞争相信息提供可重复使用的数据资源

**仍需研究：**已观测数据分布不直接描述全部稳定材料空间或合成条件

关联：C1, C3, C5, C6；方向 A, B, C, D。

<a id="r05"></a>
## [R05] Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties

[原始来源](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301) · 首次已核公开：2017-10-27 · Physical Review Letters 120, 145301；2018-04-06

作者：Tian Xie, Jeffrey C. Grossman。

**任务：**给定晶体结构的性质预测。

**研究的问题：**手工描述符难以统一不同结构与化学环境

**核心方法：**从晶体图学习局部环境与整体性质映射

**原文结果及适用范围：**

- 原文研究八种性质，并用局部贡献解释材料设计规律

**仍需研究：**前向预测知识如何组织为可生成的周期结构仍是另一问题

关联：C1, C3, C6；方向 A, B, C, D。

<a id="r06"></a>
## [R06] Inverse Design of Solid-State Materials via a Continuous Representation

[原始来源](https://doi.org/10.1016/j.matt.2019.08.017) · 首次已核公开：2019 · Matter 1(5), 1370–1384；卷期 2019-11-06；状态 published journal article

作者：Juhwan Noh, Jaehoon Kim, Helge S. Stein, Benjamin Sanchez-Lengeling, John M. Gregoire, Alan Aspuru-Guzik, Yousung Jung。

**任务：**DNG within V–O；rediscovery；inverse design proof of concept。

**研究的问题：**性质预测描述符通常不可逆，模型不能把潜变量解码为化学组成、晶胞和原子位置。

**核心方法：**把晶胞和原子基底拆成三维图像，经VAE压缩到连续潜空间，再将解码图像转换为晶胞与坐标并进行物理筛选。

**原文结果及适用范围：**

- 任务：V–O候选生成与再发现；评价口径：在未包含若干已知实验结构的训练设置中再发现；生成约20,000个假想候选并开展DFT/亚稳性分析。；结果：获得新的V–O组成和多晶型候选，证明连续潜空间能够产生可交给物理计算的结构。；原文位置：原文摘要；Results and Discussion

**仍需研究：**实证集中于V–O，图像分辨率、元素扩展和几何等价表示增加学习成本；可解码性本身不保证候选稳定或可合成。

关联：C1, C3, C5；方向 A, B, D。

<a id="r07"></a>
## [R07] An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties

[原始来源](https://arxiv.org/pdf/2005.07609v3) · 首次已核公开：2020-05-15 · Matter 5, 314–335；2022；状态 published journal article; DOI与作者README年份含2021，卷期为2022

作者：Zekun Ren, Siyu Isaac Parker Tian, Juhwan Noh, Felipe Oviedo, Guangzong Xing, Jiali Li, Qiaohao Liang, Ruiming Zhu et al.。

**任务：**property conditional inverse design；joint composition/structure generation。

**研究的问题：**生成器常限定元素/原型；目标性质难对应可解码的通用晶体结构。

**核心方法：**实空间与倒空间FTCP可逆表示、带性质分支VAE组织潜空间，再按目标采样/解码。

**原文结果及适用范围：**

- 任务：三个性质设计案例；评价口径：作者以DFT弛豫和第一性原理性质验证目标是否满足；不同目标及候选分母分别计算。；结果：共报告142个新候选，目标成功率7.1%–38.9%；原文同时讨论晶体不变性的困难。；原文位置：原文三个设计案例、Results；arXiv最新稿
- 原文结果：142个设计候选经第一性原理验证，三类设计成功率7.1%–38.9%；带隙1.5eV且形成能<-1.5eV/atom任务7/19=36.8%。；评价阶段：DFT relaxation/property calculations；定义：首原理验证的目标满足数/设计数；形成能任务±0.06eV/atom；原文位置：three design cases; Table 1; Fig.5

**仍需研究：**潜空间候选能命中功能，但复杂混合意图、精确结构关系以及共同严格相稳定资格尚需更直接控制。

关联：C1, C2, C3；方向 A, B。

<a id="r08"></a>
## [R08] Crystal Diffusion Variational Autoencoder for Periodic Material Generation

[原始来源](https://arxiv.org/abs/2110.06197) · 首次已核公开：2021-10-12 · ICLR 2022；2022；状态 published main-conference paper

作者：Tian Xie, Xiang Fu, Octavian-Eugen Ganea, Regina Barzilay, Tommi Jaakkola。

**任务：**DNG；reconstruction；latent property optimization。

**研究的问题：**有效周期排列稀少，表示/解码缺少周期、对称和邻居成键归纳偏置。

**核心方法：**VAE组织全局组成/晶格信息，周期图score decoder生成原子坐标与类型；性质分支支持潜空间梯度优化。

**原文结果及适用范围：**

- 任务：MP-20原始DNG；评价口径：10,000样本，距离/体积及SMACT检验；该表未对生成结构做DFT弛豫。；结果：Table 2结构有效率100%、组成有效率86.70%；相比同期FTCP的1.55%结构有效率，几何执行能力显著改善。；原文位置：Table 2
- 原文结果：重构、有效多样生成及性质优化优于当时基线；§5.3相对FTCP显著改善。；评价阶段：生成结构与学习性质预测器评价；定义：不同数据集的代理性质优化/validity/coverage；该部分非独立DFT严格SUN；原文位置：§5.3/Table3; AppendixD

**仍需研究：**性质潜空间的良好目标值与实际弛豫后资格之间仍需物理连接；终态分布score与物理力不是同一已验证对象。

关联：C1, C2, C3, C4, C6；方向 A, B, C, D。

<a id="r09"></a>
## [R09] GFlowNet Foundations

[原始来源](https://jmlr.org/papers/v24/22-0364.html) · 首次已核公开：2021-11-17 · Journal of Machine Learning Research；2023；状态 published

作者：Bengio, Yoshua, Lahlou, Salem, Deleu, Tristan, Hu, Edward J., Tiwari, Mo, Bengio, Emmanuel。

**研究的问题：**怎样将多峰奖励函数变成可快速独立采样的生成器，而不是只求最高奖励？

**核心方法：**在构造状态图上学习守恒流与前/后向策略，以平衡目标产生近似按非负终端奖励比例的采样。

**重要性：**科学设计通常需要多个候选，昂贵MCMC及模式混合的工作有机会被训练摊销。

**主要困难：**一个对象有多条构造路径，奖励的归一化常未知，多峰探索与泛化都困难。

**原文结果及适用范围：**

- 原文位置：§1.1与flow matching/detailed balance理论；结果：建立奖励比例采样、条件边缘化与复合对象的理论基础。；评价口径：方法基础，非晶体strict SUN榜单。

**仍需研究：**奖励比例目标本身不指定未知合格结果的发现价值；物理后处理身份与资格需额外建模，有限训练不能继承理想分布保证。

关联：C4, C5, C6；方向 C, D。

<a id="r10"></a>
## [R10] A universal graph deep learning interatomic potential for the periodic table

[原始来源](https://www.nature.com/articles/s43588-022-00349-3) · 首次已核公开：2022-02 · Nature Computational Science 2, 718–728；2022-11-28

作者：Chi Chen, Shyue Ping Ong。

**任务：**跨化学机器学习原子间势与筛选。

**研究的问题：**广泛化学空间中的可负担物理评价与弛豫

**核心方法：**三体图神经网络与Materials Project弛豫轨迹训练

**原文结果及适用范围：**

- 作者对最低预测hull能的2000个候选进行DFT核验，其中1578个稳定；该选择性核验率不是独立生成SUN

**仍需研究：**势能近似、候选分布偏移与竞争相参照仍影响生成评价

关联：C3, C4, C5, C6；方向 B, C, D。

<a id="r11"></a>
## [R11] CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling

[原始来源](https://www.nature.com/articles/s42256-023-00716-3) · 首次已核公开：2023-02 · Nature Machine Intelligence 5, 1031–1041；2023-09-14

作者：Bowen Deng, Peichen Zhong, KyuJung Jun, Janosh Riebesell, Kevin Han, Christopher J. Bartel, Gerbrand Ceder。

**任务：**跨化学原子间势与带电信息的原子建模。

**研究的问题：**原子几何、电子状态相关性与计算代价

**核心方法：**以磁矩监督表示、学习能量/力/应力等物理量

**原文结果及适用范围：**

- 在MPtrj测试集报告能量30meV/atom、力77meV/Å等MAE，并研究异价体系；这是预测与模拟结果

**仍需研究：**准确近似势不自动确定生成选择、新颖性或可合成性

关联：C3, C4, C6；方向 B, C, D。

<a id="r12"></a>
## [R12] Crystal structure generation with autoregressive large language modeling

[原始来源](https://www.nature.com/articles/s41467-024-54639-7) · 首次已核公开：2023-07-10 · Nature Communications 15, 10570；2024；在线 2024-12-06；状态 published journal article

作者：Luis M. Antunes, Keith T. Butler, Ricardo Grau-Crespo。

**任务：**formula/space-group prompted structure generation；CSP；unseen-compound generation；MCTS-guided decoding。

**研究的问题：**给定组成后的候选生成需要晶体几何知识；CIF文字是否可以学习组成—空间群—坐标规律未知。

**核心方法：**从晶体语料训练自回归CIF语言模型，组成/空间群前缀生成；形成能预测器指导MCTS。

**原文结果及适用范围：**

- 任务：约10,000个留出CIF生成；评价口径：组成与空间群前缀；CIF语法、计数、键长合理性和StructureMatcher检验。；结果：小模型有空间群前缀时有效率94.0%，首次结构匹配78.4%；这是带已知组成/空间群的结构恢复指标。；原文位置：arXiv v3 Tables 1–2
- 原文结果：未见组成/空间群组合能生成有效结构；选定DFT例子支持几何合理性；MCTS改善困难组成的有效率和预测能量。；评价阶段：CIF/结构匹配，预测形成能MCTS，选定DFT；定义：提供空间群与否分别评价；100次挑战集尝试和标准CSP另设预算；原文位置：main results; challenge set; author v3 Tables3/4/6

**仍需研究：**CIF前缀和学得模板提供重要晶体知识，如何把这些知识作用于未指定关系、连续实现反馈及新物理目标还可扩展。

关联：C1, C2, C3, C4, C6；方向 A, B, C, D。

<a id="r13"></a>
## [R13] Crystal Structure Prediction by Joint Equivariant Diffusion

[原始来源](https://arxiv.org/abs/2309.04475) · 首次已核公开：2023-07-30 · NeurIPS 2023；2023；状态 published main-conference paper

作者：Rui Jiao, Wenbing Huang, Peijia Lin, Jiaqi Han, Pin Chen, Yutong Lu, Yang Liu。

**任务：**CSP given atom-type multiset；DNG extension。

**研究的问题：**给定原子类型后的晶格与坐标需联合搜索，同时处理旋转、平移、置换和周期性。

**核心方法：**分数坐标与晶格联合扩散，周期E(3)等变去噪；基本CSP任务固定组成。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：标准60/20/20拆分，未弛豫；k=1和k=20按StructureMatcher参考恢复。；结果：匹配率51.49%/77.93%；Table 3分阶段L→F为50.03%、F→L为36.73%，支持该实现中联合几何更新的收益。；原文位置：Tables 1, 3
- 原文结果：标准CSP基准改善结构匹配和计算效率；样本数增加可提高参考恢复。；评价阶段：StructureMatcher reference recovery；定义：MP-20等参考结构Match/RMSE；不直接测完整多晶型低能集合；原文位置：§5/Table1; generation extension

**仍需研究：**物理功能设计往往还要决定组成和保存多晶型；恢复一个数据库参考之后，低能多解覆盖仍有独立问题。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r14"></a>
## [R14] Reinforcement learning in crystal structure prediction

[原始来源](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j) · 首次已核公开：2023-09-26 · Digital Discovery；2023；在线 2023-09-26；状态 published

作者：Elena Zamaraeva, Christopher M. Collins, Dmytro Antypov, Vladimir V. Gusev, Rahul Savani, Matthew S. Dyer, George R. Darling, Igor Potapov et al.。

**研究的问题：**手工固定的basin-hopping动作概率怎样随当前结构与搜索经验而改变？

**核心方法：**在FUSE和MC-EMMA中用policy gradient在线学习依赖当前结构的动作策略。

**重要性：**同一相域内的不同组成未必适用同一手调动作策略，物理调用可用于改善下一步选择。

**主要困难：**状态相关动作效果依赖体系与当前结构，学习过程也要保持搜索成本低。

**原文结果及适用范围：**

- 原文位置：§4 Conclusion；结果：两个basin-hopping代码的组成研究显示在线策略收益随体系而变化。；评价口径：两个basin-hopping CSP代码、六种组成的物理搜索；未提取原表，不录摘要或结论段的时间/胜率量化。

**仍需研究：**证明在线自适应搜索价值；不同生成状态中的可靠反馈与可执行决定、跨新请求知识迁移仍需专门研究。

关联：C4, C6；方向 C, D。

<a id="r15"></a>
## [R15] Scalable Diffusion for Materials Generation

[原始来源](https://arxiv.org/abs/2311.09235) · 首次已核公开：2023-10-18 · ICLR 2024；2024；状态 published conference paper

作者：Yang, Sherry, Cho, KwangHwan, Merchant, Amil, Abbeel, Pieter, Schuurmans, Dale, Mordatch, Igor, Cubuk, Ekin Dogus。

**任务：**DNG；composition-conditioned structure proposal。

**研究的问题：**显式结构图可能限制大规模训练；代理生成指标与实际低能结构产出之间不一致。

**核心方法：**把原子坐标按周期表的周期/族排成张量，以空位置标识缺失原子；训练注意力/卷积扩散模型，用随机置换旋转等增强处理等价性。

**原文结果及适用范围：**

- 任务：MP-20生成的DFT评估；评价口径：比较两生成器重合组成的弛豫结构，并相对MP2021/GNoME凸包评价。；结果：重合组成中86.3% UniMat候选能量更低，平均形成能比CDVAE低0.216eV/atom；Table 3相对MP2021低于凸包候选数414对56。；原文位置：Tables 2–3

**仍需研究：**张量维度与最大原子数限制仍存在；不变性主要通过增强获得，规模收益和表示收益需结合训练分布理解；凸包参照变化影响稳定计数。

关联：C1, C3, C5；方向 A, B, D。

<a id="r16"></a>
## [R16] An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning

[原始来源](https://www.nature.com/articles/s41467-023-42870-7) · 首次已核公开：2023-11-02 · Nature Communications 14, 7027；在线 2023-11-02；状态 published journal article

作者：Hang Xiao, Rong Li, Xiaoyang Shi, Yan Chen, Liangliang Zhu, Xi Chen, Lei Wang。

**任务：**structure reconstruction；topology-sequence inverse design；direct narrow-gap semiconductor design。

**研究的问题：**CIF/坐标把同一个周期结构展开成大量不同序列；理想序列须保留周期连通关系并可实现回三维结构。

**核心方法：**以带周期平移标签的商图编码晶体为字符串；SLI2Cry先进行图论实现，再以修改的GFN-FF和M3GNet完成几何优化。

**原文结果及适用范围：**

- 任务：重构与半导体逆设计；评价口径：在40,330个经筛选的MP-20结构上评价重构；解码包含物理优化，另开展DFT半导体筛选。；结果：原文验证周期拓扑字符串可以恢复大批结构并提出满足目标的半导体候选；重构能力属于完整解码流程。；原文位置：Results; Table 1

**仍需研究：**拓扑不能唯一确定连续晶胞及坐标，几何实现依赖优化器与势；物理相兼容性不能由字符串语法保证。

关联：C1, C3, C6；方向 A, B, C, D。

<a id="r17"></a>
## [R17] Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials

[原始来源](https://www.nature.com/articles/s41586-025-09992-y) · 首次已核公开：2023-11-29 · Nature 650, E1 (2026)

作者：Nathan J. Szymanski, Bernardus Rendy, Yuxing Fei, Rishi E. Kumar, Tanjin He, David Milsted, Matthew J. McDermott, Max Gallant et al.。

**任务：**实验合成流程与闭环决策；实验身份与新颖性表述的更正。

**研究的问题：**新颖性参照和实验物相识别需要明确

**核心方法：**重新分析衍射结果并修订原文

**原文结果及适用范围：**

- 更正版报告17天353次实验、57个目标中36个成功；身份与新颖性按更正后解释
- 原新颖性措辞修订，36个成功、4个衍射不足以判断；另移除一项误入训练数据的目标

**仍需研究：**评价参照与不确定性是发现结论的组成部分

关联：C1, C4, C5, C6；方向 A, B, C, D。

<a id="r18"></a>
## [R18] Scaling deep learning for materials discovery

[原始来源](https://www.nature.com/articles/s41586-023-06735-9) · 首次已核公开：2023-11-29 · Nature；2023；在线 2023-11-29；状态 published

作者：Amil Merchant, Simon Batzner, Samuel S. Schoenholz, Muratahan Aykol, Gowoon Cheon, Ekin Dogus Cubuk。

**任务：**生成候选、模型筛选、DFT验证与预测器迭代学习。

**研究的问题：**怎样让一次次候选物理验证同时扩展材料库和后续预测/提出能力？

**核心方法：**结构替换与组成候选提出、图网络能量筛选、标准化DFT验证，以及将结果加入训练数据和未来候选来源的主动循环。

**重要性：**单次筛选成功之外，昂贵DFT结果还可能提升整个发现循环。

**主要困难：**候选空间巨大，数据与稳定性标签随新竞争相变化，泛化需按组成隔离。

**原文结果及适用范围：**

- 相对旧资料约220万稳定候选，经相互竞争更新hull后为38.1万新稳定条目；不是38.1万已合成材料
- 原文位置：Active learning；Methods Active learning；Composition-based hashing；结果：DFT结果同时用于验证、重新训练GNN及扩大可替换父结构，体现计算积累的已完成能力。；评价口径：不同候选管线与新hull；本分稿不取Fig.1量化结果，避免把新hull条目称为全部已合成。

**仍需研究：**这里主要增长PES预测器与候选数据库；生成干预关系的学习、未知合格结果分布及应用实现仍有不同问题。

关联：C3, C4, C5, C6；方向 B, C, D。

<a id="r19"></a>
## [R19] A generative model for inorganic materials design

[原始来源](https://www.nature.com/articles/s41586-025-08628-5) · 首次已核公开：2023-12-06 · Nature；2025；在线 2025-01-16；状态 published

作者：Claudio Zeni, Robert Pinsler, Daniel Zügner, Andrew Fowler, Matthew Horton, Xiang Fu, Zilong Wang, Aliaksandra Shysheya et al.。

**任务：**DNG；property/chemistry/symmetry conditional generation after adapter fine-tuning。

**研究的问题：**能否直接提出稳定、新颖且满足多种目标性质的完整周期结构，并进入物理验证？

**核心方法：**联合扩散生成元素、坐标和晶格，性质adapter微调，MLFF预筛与DFT/实验验证。

**重要性：**从仅检索已有候选发展为可扩展逆向设计，需要可靠结构提出与验证闭环。

**主要困难：**元素、坐标、晶格相互依赖；性质标注不均；稳定与新颖受数据/参照/筛选影响。

**原文结果及适用范围：**

- 任务：基模DNG；评价口径：1,024个生成结构做DFT，相对联合Alex-MP-ICSD凸包，能量阈值0.1eV/atom。；结果：75%低于0.1eV/atom、3%低于0；95%生成到DFT弛豫的RMSD低于0.076Å，说明学到接近终态的结构分布。；原文位置：Nature Figure 2 and main text
- 原文结果：广泛单性质及磁密度+HHI联合设计；180次DFT性质调用获得106个高模量SUN候选，筛选40个；TaCr2O6合成验证目标设计。；评价阶段：MLIP筛选→DFT/性质→选定合成；定义：论文SUN采用其近凸包/去重/ordered-disordered matcher；预算为性质调用，不是全部计算。目标200GPa，DFT222GPa；实验无序样品最高169GPa、四次158±11GPa。；原文位置：Property-guided design; Fig6; Experimental validation; supplement B/D
- 原文位置：Base model evaluation；Chemistry-/Property-guided design；Experimental validation；结果：展示多类性质/化学条件材料提出、DFT验证与一个实验验证案例。；评价口径：正式base评价1024生成样本；stable允许DFT-relaxed energy above Alex-MP-ICSD hull≤0.1 eV/atom；不能与on-hull SUN直接混比。

**仍需研究：**完整闭环已实现，但不同收益来自模型、训练规模、化学访问还是后处理，需要有针对性分解；机制泛化仍受分布限制。

关联：C1, C2, C4, C5, C6；方向 A, B, C, D。

<a id="r20"></a>
## [R20] Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation

[原始来源](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html) · 首次已核公开：2024 · NeurIPS 2024；2024；状态 published conference paper

作者：Yan, Keqiang, Li, Xiner, Ling, Hongyi, Ashen, Kenna, Edwards, Carl, Arróyave, Raymundo, Zitnik, Marinka, Ji, Heng et al.。

**任务：**CSP；DNG；band-gap conditional generation。

**研究的问题：**同一晶体的多种CIF序列使序列模型重复学习等价性，缺少可完整重建且规范化的结构序列。

**核心方法：**用Niggli晶格约化、原点选择及原子排序构造规范单位胞，将SO(3)等变晶胞转成SE(3)及周期不变序列，并训练AR模型。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：与此前结构生成器的标准参考匹配口径；one-shot。；结果：匹配率61.3%，高于表内DiffCSP51.5%；DFT DNG附表在温度1.35下SUN2.0%，说明表示收益与物理发现须分别评价。；原文位置：Table 2; Appendix Table 10

**仍需研究：**表示完整性与不变性的论证针对其归一化定义和数值编码；性质控制主要依赖代理预测，规范化不会自行保证几何或竞争相稳定。

关联：C1, C3, C5；方向 A, B, D。

<a id="r21"></a>
## [R21] Fine-Tuned Language Models Generate Stable Inorganic Materials as Text

[原始来源](https://arxiv.org/abs/2402.04379) · 首次已核公开：2024-02-06 · ICLR 2024；2024；状态 published main-conference paper

作者：Nate Gruver, Anuroop Sriram, Andrea Madotto, Andrew Gordon Wilson, C. Lawrence Zitnick, Zachary Ulissi。

**任务：**DNG as text；text/property conditioning；infilling。

**研究的问题：**多类型科学数据难共享生成接口；通用LLM能否学习晶体数字几何与对称未知。

**核心方法：**LoRA微调LLaMA-2，固定精度晶体文本，任务提示与平移增强支持生成、条件和infilling。

**原文结果及适用范围：**

- 任务：MP-20文本DNG；评价口径：M3GNet先弛豫/筛选，只有预测低于0.1eV/atom者送DFT；Table 1稳定率按原生成候选计算。；结果：可生成经DFT验证低于参考凸包的候选，并显示相对于从头训练文本模型的预训练收益；逐项数字见原Table 1。；原文位置：Table 1; Appendix A.5/B.2
- 原文结果：70B模型约49%预测亚稳率（CDVAE28%）；空间群提示约24%命中，并展示结构填补。；评价阶段：M3GNet relaxation与selected DFT；条件匹配；定义：49%为预测亚稳，不是全部DFT严格SUN；空间群判断symprec0.2Å；原文位置：§5/Figs4–7

**仍需研究：**语言编码已构成可用晶体接口；精确计量、数值性质和几何反馈下的决定修订仍可提升。

关联：C1, C2, C3；方向 A, B。

<a id="r22"></a>
## [R22] Space Group Constrained Crystal Generation

[原始来源](https://arxiv.org/abs/2402.03992) · 首次已核公开：2024-02-06 · ICLR 2024；2024；状态 published conference paper

作者：Jiao, Rui, Huang, Wenbing, Liu, Yu, Zhao, Deli, Liu, Yang。

**任务：**CSP；DNG with sampled templates；space-group-controlled generation。

**研究的问题：**周期平移和整体旋转处理正确，仍不足以生成目标空间群；空间群约束同时影响晶格与各原子轨道。

**核心方法：**在O(3)不变的晶格对数空间施加晶系基约束，将坐标噪声/去噪限制到给定Wyckoff轨道的自由参数，并由群操作展开等价原子。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：需区分空间群/模板的预测与真值输入，未弛豫的参考匹配。；结果：Table 1真值模板/空间群设置匹配率80.27%，CSPML预测条件设置70.58%；条件来源实质改变任务难度。；原文位置：Table 1

**仍需研究：**DNG使用已有结构模板，限制模板创新；高对称约束可能排除较低能的对称破缺，满足指定群不等于最终精确空间群或稳定性保证。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r23"></a>
## [R23] Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms

[原始来源](https://arxiv.org/html/2403.03511v1) · 首次已核公开：2024-03-06 · Digital Discovery；2024；在线 2024-06-19；状态 published

作者：Marta Wolinska, Aron Walsh, Antoine Cully。

**研究的问题：**怎样同时找出低能与电子/机械性质不同的多种晶体，而非只找单一最低点？

**核心方法：**MAP-Elites按预设性质特征组织archive，在各区域优化能量；ML代理提供能量与性质评价。

**重要性：**多种可行结构和性质图谱能支持选材与理解搜索空间。

**主要困难：**高维构形与昂贵性质评价限制多样探索，单一最优或Pareto前沿会丢弃其它有用结构。

**原文结果及适用范围：**

- 原文位置：§4 TiO2与扩展系统；结果：恢复TiO2参考结构并探索C、SiO2、SiC多个具有不同性质的局部极小值。；评价口径：固定组成CSP、指定property feature space；不是开放组成DNG strict SUN。

**仍需研究：**已有多样低能档案；未知资格与结果类别如何共同学习，以及档案怎样影响未见请求生成能力仍有空间。

关联：C4, C5；方向 C, D。

<a id="r24"></a>
## [R24] Con-CDVAE: A method for the conditional generation of crystal structures

[原始来源](https://arxiv.org/html/2403.12478v1) · 首次已核公开：2024-03-19 · Computational Materials Today 1, 100003；2024；状态 published journal article

作者：Cai-Yuan Ye, Hong-Ming Weng, Quan-Sheng Wu。

**研究的问题：**潜空间性质优化之外，按用户条件直接提出结构及缺项补全仍不充分。

**核心方法：**条件property embedding、VAE+性质joint loss、条件DDPM latent prior，两阶段训练与default/full/less策略。

**原文结果及适用范围：**

- 原文结果：形成能、带隙、晶系及形成能+带隙联合标签控制；135个形成能样本DFT验证，8个弛豫失败。；评价阶段：CGCNN property plus selected DFT；定义：每任务20,000 latent proposals筛选至200再解码；联合结果主要为代理评价；原文位置：§2.3; §3; Tables2–3; Fig6

**仍需研究：**多字段条件和缺项补全已展示作用；精确对称、困难数值对和统一终态联合资格还待扩大验证。

关联：C1, C2；方向 A, B。

<a id="r25"></a>
## [R25] Space group informed transformer for crystalline materials generation

[原始来源](https://arxiv.org/abs/2403.15734) · 首次已核公开：2024-03-23 · Science Bulletin 70, 3522–3533；2025；卷期 2025-11；状态 published journal article

作者：Zhendong Cao, Xiaoshan Luo, Jian Lv, Lei Wang。

**任务：**space-group-controlled DNG；symmetric initialization；element substitution；property-guided MCMC。

**研究的问题：**全原子坐标生成反复预测对称冗余，固定模板又难提出新轨道组合；离散Wyckoff选择应与连续自由坐标同样进入概率模型。

**核心方法：**空间群条件自回归预测Wyckoff位点、元素和自由分数坐标，以von-Mises混合处理周期坐标，并预测独立晶格参数；对数似然可用于MCMC。

**原文结果及适用范围：**

- 任务：七个空间群的结构初始化；评价口径：各群100个候选，与相同组成/空间群PyXtal初始化做DFT；阈值E_hull<0.1eV/atom。；结果：高对称群中生成结构更接近DFT终点；报告MP-20外候选34个对PyXtal12个。低对称群并非每项优于PyXtal。；原文位置：Table 2; Figure 7; Appendix C

**仍需研究：**自回归顺序在部分信息下固定离散决策；给定空间群的表达能力依赖训练数据，高对称优势不能外推到所有畸变或低对称未知晶体。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r26"></a>
## [R26] FlowMM: Generating Materials with Riemannian Flow Matching

[原始来源](https://proceedings.mlr.press/v235/miller24a.html) · 首次已核公开：2024-06-07 · ICML 2024, PMLR 235；2024；状态 published conference paper

作者：Miller, Benjamin Kurt, Chen, Ricky T. Q., Sriram, Anuroop, Wood, Brandon M。

**任务：**CSP；DNG。

**研究的问题：**正确周期空间中的扩散仍需大量采样步，固定简单先验与数据之间的路径未必利于学习和采样。

**核心方法：**在晶格、周期坐标及元素状态的乘积空间进行Riemannian flow matching，回归条件运输向量场，并设计晶格初始分布与采样速度调节。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：与DiffCSP使用相同底层网络；无DFT弛豫的参考匹配。；结果：top-1匹配61.39%，约50步达到高匹配性能，原DiffCSP使用1,000步。；原文位置：Table 1; Figure 2
- 任务：DNG；评价口径：250步、10,000样本，CHGNet预弛豫→DFT；MP2023凸包，E_hull<0且元素种数≥2。；结果：SUN为2.38%，属于严格阈值下的物理验证指标。；原文位置：Table 2; Appendix A

**仍需研究：**运输路径拟合数据分布而非真实力场；步数效率不包含所有训练/物理计算费用，局部score或速度改进未自动给出新低能模式。

关联：C1, C2, C4, C5；方向 A, B, C, D。

<a id="r27"></a>
## [R27] Structural constraint integration in a generative model for the discovery of quantum materials

[原始来源](https://www.nature.com/articles/s41563-025-02355-y) · 首次已核公开：2024-07-05 · Nature Materials 25, 223–230；2026；在线 2025-09-22；卷期 2026-02；状态 published journal article; online/issue years separately retained

作者：Ryotaro Okabe, Mouyang Cheng, Abhijatmedhi Chotrattanapituk, Manasi Mandal, Kiran Mak, Denisse Córdova Carrizales, Nguyen Tuan Hung, Xiang Fu et al.。

**研究的问题：**蜂窝、kagome等几何模式与量子材料机制相关，普通随机生成缺少明确几何约束接口。

**核心方法：**把前向加噪约束结构按掩码并入每步去噪，生成自由部分来完成共同结构；以DiffCSP作实例，可复用已有diffusion。

**原文结果及适用范围：**

- 原文结果：最终版Data声明10.06M生成/1.01M预筛；26,000 DFT尝试、24,743 DFT-relaxed。13,880个Fmax合格结构（53.38%），二例提案指导实验合成。；评价阶段：four-stage prescreen→DFT→residual force/distortion→novelty/dedup; selected synthesis；定义：>95%对应24,743/26,000=95.17%的DFT弛豫输出；53%对应Fmax<0.01eV/Å，不是凸包稳定。Table3另要求dlatt/dxyz按AL为(1.0Å,0.5Å)/(2.0Å,1.0Å)/(3.0Å,1.5Å)，小畸变合格5,931，最终新颖去重3,018。；合成结果：提案TiPdBi、TiPdSb指导获得TiPd0.22Bi0.88、Ti0.5Pd1.5Sb；实验计量和空间群均改变，分别顺磁/抗磁。；原文位置：final abstract/Data availability; supplement §12/Table3 and §10.1

**仍需研究：**几何引导和实验发现价值已经确立；多个共享motif的兼容、弛豫后机制保持及实验无序/占位仍是扩展目标。

关联：C1, C3, C5；方向 A, B, D。

<a id="r28"></a>
## [R28] Generative Hierarchical Materials Search

[原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf) · 首次已核公开：2024-09-10 · NeurIPS 2024；2024；状态 published main-conference paper

作者：Sherry Yang, Simon Batzner, Ruiqi Gao, Muratahan Aykol, Alexander L. Gaunt, Brendan McMorrow, Danilo J. Rezende, Dale Schuurmans et al.。

**研究的问题：**用户往往能说功能/材料家族，却难预先确定可行化学式；缺少语言到完整结构的配对数据。

**核心方法：**LLM把请求转为公式，composition-conditioned diffusion生成几何，GNN性质评价与请求符合共同驱动forward tree search。

**原文结果及适用范围：**

- 原文结果：三类主要家族请求符合率>80%，相比直接zero-shot LLM生成有显著改善；DFT支持选定低能结构。；评价阶段：request compliance+predicted energy search, selected DFT；定义：请求家族及低形成能任务；不是统一未见条件strictSUN交集；原文位置：§2/Algorithm1; §3 and Introduction results summary

**仍需研究：**跨公式/几何搜索已让自然语言参与发现；部分生成状态中的关系修订和新混合条件仍可进一步联合学习。

关联：C1, C2, C4；方向 A, B, C。

<a id="r29"></a>
## [R29] FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions

[原始来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html) · 首次已核公开：2024-10-30 · NeurIPS 2024；2024；状态 published main-conference paper; official proceedings verified

作者：Anuroop Sriram, Benjamin Kurt Miller, Ricky T. Q. Chen, Brandon M. Wood。

**任务：**DNG via LLM initialization and composition-conditioned continuous transport。

**研究的问题：**LLM提供较好化学提案但几何精度有限；随机基分布flow需要较长运输。

**核心方法：**微调LLM形成化学/粗几何基分布，以同组成LLM样本—终态配对训练Riemannian flow；精修期间类型固定。

**原文结果及适用范围：**

- 任务：MP-20 DNG；评价口径：70B LLM、250流步，10,000候选，CHGNet→DFT；MP2023凸包、E_hull<0、元素种数≥2。；结果：温度0.7/nucleus0.9时稳定17.82%、SUN4.92%；types-only版本稳定约8.8–9.0%，支持初始几何也贡献收益。；原文位置：Table 1
- 原文结果：10,000例：DFT stable17.82%、SUN4.92%；CHGNet后弛豫步数约37.97，FlowMM约191.98。；评价阶段：CHGNet pre-relax→DFT relaxation；定义：Ehull<0、arity≥2、MP2023 hull；主要证据DNG，性质自然语言接口在§3为hypothetical；原文位置：§4–5/Tables1–2; §3 Training

**仍需研究：**学习化学/几何先验已显著提高发现效率；连续修订期间如何反馈组成、对称和其它离散决定仍可研究。

关联：C1, C2, C3, C4；方向 A, B, C。

<a id="r30"></a>
## [R30] Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks

[原始来源](https://arxiv.org/html/2411.04323v1) · 首次已核公开：2024-11-06 · Digital Discovery；2026；在线 2025-10-02；状态 published

作者：Nguyen, Tri Minh, Tawfik, Sherif Abdulkader, Tran, Truyen, Gupta, Sunil, Rana, Santu, Venkatesh, Svetha。

**研究的问题：**如何在巨大化学与周期几何动作空间中既高效探索又保持多种候选？

**核心方法：**层级GFlowNet先选空间群，再在相应晶格/原子子空间探索；终端reward结合形成能、键长、密度与组成有效性。

**重要性：**材料发现需要多个符合要求的结构，空间群层级可组织搜索。

**主要困难：**单体策略需同时学习空间群、晶格、元素和坐标的耦合，昂贵hull反馈难直接逐步使用。

**原文结果及适用范围：**

- 原文位置：§5 Modes exploration；§10.7；结果：层级策略在作者设置中提高模式发现效率；mode需有效、满足最短距离、负形成能及组成与已有mode不同。；评价口径：v1 mode不是共同松弛后strict SUN；Table1–3还使用reward-ranked top-K，不能移植成无筛选独立DNG分母。

**仍需研究：**层级探索已有能力；开放合格终态身份、相竞争稳定及结果分布的持续形成需要更具体目标。

关联：C1, C2, C4, C5；方向 A, B, C, D。

<a id="r31"></a>
## [R31] Establishing baselines for generative discovery of inorganic crystals

[原始来源](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f) · 首次已核公开：2025-01-04 · Materials Horizons；2025；在线 2025-07-04；状态 published

作者：Nathan J. Szymanski, Christopher J. Bartel。

**研究的问题：**生成模型相对化学/原型方案究竟新增哪些发现能力？

**核心方法：**电荷平衡原型随机枚举与数据挖掘离子替换，比较四种生成器，并加入共同MLIP/性质预筛与DFT验证。

**重要性：**相同物理筛选也能改善简单方法，模型能力需要强竞争基线。

**主要困难：**数据来源、提出数、novelty过滤和筛选成本不同，简单合成排名会混入管线差异。

**原文结果及适用范围：**

- 原文位置：Table1/Results stability and novelty；结果：MP-20重训MatterGen之外，离子替换在作者的MP新颖候选集合稳定率更高；模型能提出部分AFLOW未映射原型。；定量结果：stable_percent：random_enumeration：1.4；ion_exchange：9.2；mattergen_mp20：3.0；denominator：每方法500个未匹配MP的候选进入DFT；获得这些候选的原始提出数因方法不同。；评价口径：DFT decomposition energy≤0，MP竞争相；MatterGen common-data主比较为MP-20重训，不是Nature大数据checkpoint。

**仍需研究：**特定共同管线的结果不提供所有模型/预算排名；需要解释化学访问、条件实现与筛选分别贡献了什么。

关联：C3, C4, C5；方向 B, C, D。

<a id="r32"></a>
## [R32] A generative material transformer using Wyckoff representation

[原始来源](https://www.nature.com/articles/s41524-025-01940-8) · 首次已核公开：2025-01-27 · npj Computational Materials 12, 60；2026；在线 2026-01-23；状态 published journal article

作者：Pierre-Paul De Breuck, Hashim A. Piracha, Gian-Marco Rignanese, Miguel A. L. Marques。

**任务：**DNG；E_hull-conditioned generation。

**研究的问题：**稳定、对称与生成效率难兼顾；仅离散模板还缺连续自由参数。

**核心方法：**invertible Wyckoff token序列、离散/连续双head；稳定LOW/HIGH标签阈值0.075eV/atom，条件包括元素、空间群和Wyckoff。

**原文结果及适用范围：**

- 任务：规模化DNG后筛选；评价口径：报告三百万独特结构，使用MLIP/代理筛选后选取候选做DFT，凸包参照为Alexandria。；结果：发布包含4,000个经DFT验证距凸包≤0.001eV/atom候选的数据；这是筛选后结果，不是四千/三百万作为原始SUN率。；原文位置：arXiv v2 large-scale generation; DFT section
- 原文结果：稳定富集约8倍charge-compensated PyXtal；300万unique候选发布，4,000结构DFT距离凸包<0.001eV/atom；Al–Ca–Cu指定化学空间2,000提案恢复11/15 WBM稳定结构。；评价阶段：model→geometry→MLIP and selected DFT；定义：3M是生成数据，4k为选择/验证流水线结果；训练标签0.075与DFT资格0.001分开；原文位置：final Conditioning; Training/Results; Fig3; Data availability

**仍需研究：**对称和稳定条件已能有效组织探索；任意功能目标及新的局部/全局关系组合还需独立实证。

关联：C1, C2, C3, C5, C6；方向 A, B, C, D。

<a id="r33"></a>
## [R33] A Periodic Bayesian Flow for Material Generation

[原始来源](https://arxiv.org/abs/2502.02016) · 首次已核公开：2025-02-04 · ICLR 2025；2025；状态 published conference paper

作者：Wu, Hanlin, Song, Yuxuan, Gong, Jingjing, Cao, Ziyao, Ouyang, Yawen, Zhang, Jianbing, Zhou, Hao, Ma, Wei-Ying et al.。

**任务：**CSP；DNG。

**研究的问题：**欧氏BFN的Gaussian精度累积不直接适用周期坐标；圆周后验可能出现非单调熵变化，统一时间条件不足以说明当前信息量。

**核心方法：**对周期坐标建立基于von-Mises分布的Bayesian flow，训练网络读取均值和熵状态，配合近似线性熵sender accuracy schedule及快速模拟。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：原基准参考匹配，未开展DFT发现评估。；结果：匹配64.35%；去除熵条件变52.16%、去除torus BFN变6.17%，直接支持信息状态与周期建模的重要性。；原文位置：Tables 2–3

**仍需研究：**圆周精度不可简单相加，日程仍依赖近似/数值设计；优越的参考匹配或少步采样未测真实物理反馈或新稳定终点覆盖。

关联：C1, C2, C4；方向 A, B, C。

<a id="r34"></a>
## [R34] Open Materials Generation with Stochastic Interpolants

[原始来源](https://proceedings.mlr.press/v267/hollmer25a.html) · 首次已核公开：2025-02-04 · ICML 2025, PMLR 267；2025；状态 published conference paper

作者：Hoellmer, Philipp, Egg, Thomas, Martirossyan, Maya M., Fuemmeler, Eric, Shui, Zeren, Gupta, Amit, Prakash, Pawan, Roitberg, Adrian et al.。

**任务：**CSP；DNG joint model；DNG formula-model plus CSP。

**研究的问题：**diffusion和flow各自使用固定噪声/路径，难分离路径、随机性、采样器与表示的贡献；元素与几何需要不同动态但彼此协调。

**核心方法：**将stochastic interpolants推广到周期坐标与多变量联合分布，配合元素离散CTMC、ODE/SDE采样和线性/三角/encoder-decoder路径；另训练CFP→CSP分阶段模型。

**原文结果及适用范围：**

- 任务：MP-20 DNG；评价口径：1,000弛豫结构，MatterSim→DFT，Alex-MP参照，E_hull≤0.1eV/atom。；结果：线性SDE+γ的SUN22.48%；encoder-decoder ODE+γ稳定60.04%、SUN18.77%；CFP+CSP SUN20.17%。最优路径随目标变化，分阶段路线仍有竞争力。；原文位置：Table 3

**仍需研究：**SI路径连接训练终态与先验，不是实际形成/弛豫轨迹；稳定、独特、新颖的权衡和在线物理反馈仍待学习，0.1阈值结果不能与严格SUN跨论文倍数比较。

关联：C1, C2, C4, C5, C6；方向 A, B, C, D。

<a id="r35"></a>
## [R35] SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models

[原始来源](https://arxiv.org/abs/2502.03638) · 首次已核公开：2025-02-05 · ICLR 2025；2025；状态 published conference paper

作者：Levy, Daniel, Panigrahi, Siba Smarak, Kaba, Sékou-Oumar, Zhu, Qiang, Lee, Kin Long Kelvin, Galkin, Mikhail, Miret, Santiago, Ravanbakhsh, Siamak。

**任务：**DNG over sampled space groups；symmetry-controlled generation。

**研究的问题：**固定已有Wyckoff模板可保持对称但限制新模板；直接Wyckoff字母在群之间不共享信息，稀有群数据碎片化。

**核心方法：**采样空间群G及轨道数M，联合扩散非等价原子的元素、坐标、晶格和位点对称二进制矩阵；投影到兼容位点并按群操作展开全晶体。

**原文结果及适用范围：**

- 任务：MP-20模板多样性；评价口径：各模型10,000原始候选，模板为群+占据Wyckoff多重集。；结果：新模板1,654个，DiffCSP++为110；CHGNet稳定/SUN总体与基线相当，主要收益为对称分布与模板能力。；原文位置：Tables 1–2
- 任务：DFT可优化性；评价口径：每模型100结构做CP2K晶格/坐标弛豫。；结果：报告较低优化后最大力；收敛率无显著差异，不能将此换成DFT SUN增益。；原文位置：Section 5.3; Appendix F.6

**仍需研究：**空间群先采样后固定；压缩空间难直接看到展开原子距离，结构无效率上升，位点组合新颖还需全局物理兼容。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r36"></a>
## [R36] WyckoffDiff – A Generative Diffusion Model for Crystal Symmetry

[原始来源](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html) · 首次已核公开：2025-02-10 · ICML 2025, PMLR 267；2025；状态 published conference paper

作者：Kelvinius, Filip Ekström, Andersson, Oskar B., Parackal, Abhijith S., Qian, Dong, Armiento, Rickard, Lindsten, Fredrik。

**任务：**DNG protostructure generation；geometry realization plus materials discovery proof of concept。

**研究的问题：**全原子生成在对称冗余中学习；需要在纯离散、带化学身份的原型层建模新组合。

**核心方法：**把空间群中固定及自由Wyckoff位置的占据/计数编码为离散状态，以D3PM/DiGress式扩散生成protostructure，采用全连接消息传递共享整体信息。

**原文结果及适用范围：**

- 任务：protostructure分布与发现；评价口径：10,000样本评FWD/新原型；20,000新protostructure经元素过滤后12,650个，反复PyXtal→MACE后挑200低形成能者做VASP。；结果：原文展示三类低于参考凸包新材料；证据属于选择后发现流程，FWD不是几何或DFT稳定率。；原文位置：Tables 1–2; Section 5; Appendix G

**仍需研究：**输出省略晶格与自由坐标，同一protostructure的几何实现需要独立搜索；局部位点占据合适仍可能无法形成整体低能晶体。

关联：C1, C3, C5, C6；方向 A, B, C, D。

<a id="r37"></a>
## [R37] Periodic Materials Generation using Text-Guided Joint Diffusion Model

[原始来源](https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html) · 首次已核公开：2025-03-01 · ICLR 2025；2025；状态 published main-conference paper

作者：Kishalay Das, Subhojyoti Khastagir, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, Niloy Ganguly。

**研究的问题：**生成时缺少用户所知的全局/局部晶体描述，端到端A/X/L联合建模仍需更强条件。

**核心方法：**Robocrystallographer长描述/较短模板经MatSciBERT嵌入，注入周期等变joint denoising。

**原文结果及适用范围：**

- 原文结果：长描述帮助CSP和DNG；MP-20单候选match55.15%；文本属性符合及更短prompt分别测试，信息减少时下降。；评价阶段：benchmark reference/validity/distribution and attribute matching；定义：长文本来自目标结构，含配位/键长/矿物/对称；极简请求是独立F.5设置；原文位置：§4.2; main results; F.4/F.5

**仍需研究：**文本结构知识有效；稀疏意图和新条件组合能否保持终态全部目标，需要按信息来源/实际请求另测。

关联：C1, C3；方向 A, B。

<a id="r38"></a>
## [R38] Wyckoff Transformer: Generation of Symmetric Crystals

[原始来源](https://arxiv.org/abs/2503.02407) · 首次已核公开：2025-03-04 · ICML 2025, PMLR 267, 29495–29526；2025；状态 published conference paper

作者：Kazeev, Nikita, Nong, Wei, Romanov, Ignat, Zhu, Ruiming, Ustyuzhanin, Andrey, Yamazaki, Shuya, Hippalgaonkar, Kedar。

**任务：**DNG discrete Wyckoff representation；property prediction from coordinate-free representation。

**研究的问题：**Wyckoff字母不便跨群共享，原子序列又有顺序冗余；能否把大部分结构资格压缩成无坐标离散知识是核心假设。

**核心方法：**空间群+元素+位点对称+enumeration token，Transformer无位置编码读取已知集合，以mask/cascade训练AR；用PyXtal/CHGNet或DiffCSP++实现几何。

**原文结果及适用范围：**

- 任务：MP-20 DNG；评价口径：1,000弛豫结构测模板；105新结构DFT阈值80meV/atom；另10,000样本DFT严格阈值。；结果：1,000样本产生180/186新独特模板（两解码器）；10,000样本DiffCSP++解码严格SUN3.83%，小105样本中若干方法稳定差异未显著。；原文位置：Table 1; Section 3.1.4

**仍需研究：**无位置编码保证输入集合的置换性质；原文明确AR过程及等价Wyckoff表示靠增强。数据库中98%表示唯一是经验观察，不能推出未知多晶型唯一或稳定性充分性。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r39"></a>
## [R39] Exploration of crystal chemical space using text-guided generative artificial intelligence

[原始来源](https://www.nature.com/articles/s41467-025-59636-y) · 首次已核公开：2025-05-12 · Nature Communications 16, 4379；2025；在线 2025-05-12；状态 published journal article

作者：Hyunsoo Park, Anthony Onwuli, Aron Walsh。

**研究的问题：**晶体文字与几何嵌入缺少对齐，语言难有效选择有意义化学空间。

**核心方法：**cross-modal Crystal CLIP contrastive alignment + classifier-free A/X/L diffusion；单独指定atom count。

**原文结果及适用范围：**

- 原文结果：Crystal CLIP相对BERT composition matching约3倍；Zn–Ti–O与Li–P–S–Cl空间探索及选定DFT/声子案例。；评价阶段：soft text compliance; raw energy diagnostics; selected DFT case studies；定义：Table1 metastability为同组成未弛豫MACE能量距参考0.1eV/atom内；Fig3计量遵循随原子数增加而下降；原文位置：Table1/Fig3; chemical-space Results; limitations

**仍需研究：**文本已经能导向有价值化学空间；精确计量和数值目标、多条件终态交集仍需更强物理落地。

关联：C1, C2；方向 A, B。

<a id="r40"></a>
## [R40] PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design

[原始来源](https://arxiv.org/html/2509.07150v4) · 首次已核公开：2025-09-08 · ICML；2026；状态 published

作者：Xu, Andy, Desai, Rohan, Wang, Larry, Ritz, Ethan, Hope, Gabriel。

**研究的问题：**科学生成需要多个满足物理约束的结果，偏好优化为何在坐标表示上集中到少数成功？

**核心方法：**Qwen2.5-7B的Wyckoff文本、SFT→迭代DPO，eqV2稳定/新颖/空间群偏好，以及逐轮温度调节；条件/无条件联合训练。

**重要性：**稳定率上升只有在更多不同成功出现时才改善发现。

**主要困难：**表示冗余、组级唯一性难写成单对偏好，稳定奖励易集中概率。

**原文结果及适用范围：**

- 原文结果：相对此前方法SUN提升约/超过50%；每1000例高模量SUN联合目标40vs单模量28；高gap SUN3vs基线0。；评价阶段：eqV2偏好/eSEN final与BM/MEGNet gap，另1000例unconditional DFT；定义：物性扩展主要MLIP/代理；unconditional DFT不能替代属性扩展DFT资格；原文位置：§4–5; Appendix7.2/Table4; unconditional DFT/results
- 原文位置：Table3；结果：坐标表示三轮偏好优化稳定提高而SUN下降。；定量结果：SUN_percent：2.93；2.23；1.69；stable_percent：10.35；13.47；15.94；denominator：§5.1每个无条件模型10000个可解析CIF；解析失败重采。；评价口径：eSEN最终松弛/评价、稳定hull≤0；eqV2构造偏好。Table1与Table3保留各自表值，未拼接成同一trajectory。
- 原文位置：§5.4 Figure3/4 discussion；结果：Wyckoff表示、动态温度与统一训练改善作者任务，且有未直接强化空间群的迁移观察。；评价口径：空间群任务用宽松亚稳SSUN；不混为unconditional strict SUN。

**仍需研究：**表示与探索的作用已有证据；物理可辨识关系、未见组合的实现机制和持久开放发现分布仍需区分。

关联：C1, C2, C4, C5, C6；方向 A, B, C, D。

<a id="r41"></a>
## [R41] OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure

[原始来源](https://arxiv.org/html/2509.10293v1) · 首次已核公开：2025-09-12 · arXiv；2025；状态 preprint; final venue not confirmed here

作者：Wang, Yinan, Wang, Xiaoyang, Wang, Zhenyu, Wu, Jing, Lv, Jian, Wang, Han。

**研究的问题：**近常压平衡数据训练的物理模型怎样在高压力CSP中获得可信stress与enthalpy？

**核心方法：**CALYPSO随机初态与压力约束松弛，pressure-aware DP-GEN并发学习，按force/enthalpy不确定性选择路径与极小值DFT标签。

**重要性：**压力改变配位和组成可行性，当前PES缺口会直接误导结构搜索。

**主要困难：**高压环境少、压力/体积共同影响焓排序，热扰动数据不能充分替代压缩数据。

**原文结果及适用范围：**

- 原文位置：Introduction、dataset and Methods concurrent learning；结果：有针对性物理数据采集改善作者压力CSP所需的energy/force/virial和排序能力。；评价口径：高压enthalpy与其DFT约定，非零压独立DNG strict SUN；不直接拼接不同PES或functional的能量标签。

**仍需研究：**已显示PES校准可跨以后的搜索复用；哪些观测揭示可迁移生成决策关系仍需进一步定义。

关联：C4, C6；方向 C, D。

<a id="r42"></a>
## [R42] All that structure matches does not glitter

[原始来源](https://arxiv.org/html/2509.12178v2) · 首次已核公开：2025-09-15 · NeurIPS Datasets and Benchmarks；2025；状态 published

作者：Martirossyan, Maya M., Egg, Thomas, Hoellmer, Philipp, Karypis, George, Transtrum, Mark, Roitberg, Adrian, Liu, Mingjie, Hennig, Richard G. et al.。

**研究的问题：**有多个可接受多晶型时，单参考匹配和随机划分是否仍能度量CSP能力？

**核心方法：**去重与polymorph-aware splits；METRe匹配生成集合与全部相关参考；cRMSE加入不匹配惩罚。

**重要性：**评价对象会决定哪种能力得到训练与被当作进步。

**主要困难：**重复晶胞表示、同组成多晶型跨split、匹配容差及任意一一配对均影响结果。

**原文结果及适用范围：**

- 原文位置：§3–6；Tables2–3；结果：展示去重与多晶型评价改变恢复结果，发布数据与新的集合匹配/误差工具。；评价口径：CSP参考集合恢复；METRe不是开放DNG新颖发现率，数据库未记载的物理结果不由该指标确认。

**仍需研究：**已知参考集合仍不完备；最终物理资格、终态身份及未观测结果需要额外证据。

关联：C2, C5；方向 A, D。

<a id="r43"></a>
## [R43] LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation

[原始来源](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html) · 首次已核公开：2025-10-27 · NeurIPS 2025；2025；状态 published main-conference paper; official proceedings verified

作者：Subhojyoti Khastagir, Kishalay Das, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, Niloy Ganguly。

**任务：**DNG hybrid initialization/refinement；text-conditional formula/space group generation。

**研究的问题：**语言模型化学组成较强、精确几何较弱；等变denoising连续几何较强，需要互补利用。

**核心方法：**独立训练LLaMA crystal text与DiffCSP扩展diffusion；LLM粗结构经中间噪声处理，固定原子类型精修晶格与坐标。

**原文结果及适用范围：**

- 任务：MP-20 DNG；评价口径：10,000候选，CHGNet弛豫/估能与MP凸包比较；没有Table 3生成候选DFT验证。；结果：MLIP估计稳定16.79%、SUN9.21%；结果支持其组成—几何分工的实证价值。；原文位置：Table 3; Section 5.2
- 原文结果：10000例CHGNet：stable16.79%、SUN9.21%（LLaMA SUN4.84%）；组成保持，空间群命中相对LLM改善42%。；评价阶段：CHGNet relaxation and hull; text composition/SG matching；定义：stable Ehull<0、metastable<0.1；SUN表为CHGNet能量，非FlowLLM的DFT；SG symprec0.2Å；原文位置：§5.2/Table3; §5.3/Fig2

**仍需研究：**组合化学先验与几何精修已成功；§7明确没有模块相互反馈，给出共同形成/修订的下一步空间。

关联：C1, C2, C3, C4；方向 A, B, C。

<a id="r44"></a>
## [R44] Accelerating inverse materials design using generative diffusion models with reinforcement learning

[原始来源](https://arxiv.org/html/2511.03112v1) · 首次已核公开：2025-11-05 · arXiv；2025；状态 preprint; final venue not confirmed here

作者：Chen, Junwu, Guo, Jeff, Fako, Edvin, Schwaller, Philippe。

**研究的问题：**性质条件微调依赖大标注集，怎样以少量目标评价适应单目标和冲突多目标？

**核心方法：**扩散MDP的policy optimization、reward-weighted KL、几何松弛与SUN预筛、经验重放和历史重复diversity filter。

**重要性：**昂贵性质验证的预算限制实际逆向设计，生成分布需要对最终目标适应。

**主要困难：**likelihood与目标错位，奖励集中可能降低多样性，代理性质精度随目标区域变化。

**原文结果及适用范围：**

- 原文位置：§2.1–2.3 and SupplementC；结果：在作者单/多性质任务中改变目标分布，提供物理/预测/经验oracle，并显示replay与多样过滤的作用。；评价口径：default MatterGen；SUN先筛要求hull<0.1 eV/atom；性质调用数量不包含全部候选产生、MLIP松弛/筛选成本。

**仍需研究：**已展示目标对齐与重放价值；能力增量的可迁移物理关系、同总费用的开放合格覆盖仍需独立研究。

关联：C4, C5, C6；方向 C, D。

<a id="r45"></a>
## [R45] Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning

[原始来源](https://www.nature.com/articles/s42256-026-01262-4) · 首次已核公开：2025-11-10 · Nature Machine Intelligence；2026；在线 2026-07-06；状态 published

作者：Hyunsoo Park, Aron Walsh。

**研究的问题：**似然分布偏向已知区域，怎样兼顾欠探索化学、新颖性与热力学可行性？

**核心方法：**latent denoising diffusion与GRPO；AMD连续creativity、MLFF hull资格、结构多样性及KL/熵regularization。

**重要性：**科学发现需要稳定又少见的材料，单一高密度区域的采样不能充分服务该目标。

**主要困难：**latent解码对罕见区域误差敏感；奖励容易推向熟悉原型或稀疏相图的复杂组成；批次多样性依赖评价规模。

**原文结果及适用范围：**

- 原文结果：3eV任务512例中82同时mSUN且2.7–3.3eV，raw mSUN45.3%；另DFT弛豫后mSUN60.8%、metastability85.5%，目标仍集中。；评价阶段：initial as-generated static DFT gap; separately DFT-relaxed；定义：mSUN采用Ehull<0.1eV/atom；82/512为raw目标交集，不能与60.8%拼成relaxed目标交集；原文位置：Fig6/property-guided Results; Methods; Supplementary19–20 references
- 原文位置：Main Benchmarking、novelty–stability dilemma与Methods；结果：在作者任务中RL提高metastable/unique/novel交集并支持性质目标，仍报告重复、原型迁移与相图稀疏奖励风险。；denominator：10000样本每模型无条件DNG；主要 as-generated，不进行geometry optimization。；评价口径：主指标mSUN，hull<0.1 eV/atom的MLFF代理；不能用该值作为共同松弛strict SUN。本文不取Fig.3主值作为原表定量。

**仍需研究：**多目标分布改变已有支持；最终物理结果上的未知类发现、原型创新与跨请求知识需进一步识别。

关联：C1, C3, C4, C5, C6；方向 A, B, C, D。

<a id="r46"></a>
## [R46] LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models

[原始来源](https://arxiv.org/html/2512.04562v2) · 首次已核公开：2025-12-04 · arXiv and public benchmark；2025；状态 preprint; formal main-conference venue not confirmed

作者：Betala, Siddharth, Gleason, Samuel P., Ramlaoui, Ali, Xu, Andy, Channing, Georgia, Levy, Daniel, Fourrier, Clémentine, Kazeev, Nikita et al.。

**研究的问题：**不同稳定、新颖、有效性与物理处理口径下，怎样判断生成进步？

**核心方法：**LeMat-Bulk参考；候选与各MLIP自己重算的hull配对；有效性→U/N/S序贯；分布/多样/效率及额外松弛附表。

**重要性：**统一标准能揭示综合交集与多个能力轴之间的变化，并使费用可核。

**主要困难：**候选/参考能量混用不同方法、各提交管线的松弛不同、novelty库与分母不同。

**原文结果及适用范围：**

- 原文位置：§3.1/3.2, §4.2, §5.2/5.3/5.4, AppendixC；结果：实现无条件模型的统一多轴比较，报告平均稳定—新颖/多样权衡，并分开自带松弛提交与其它模型。；denominator：2500提交结构，CrystalFormer例外1000；U/N/S百分比按全提交集并只计通过有效性者。；评价口径：主榜不再追加松弛，但部分提交pipeline已含松弛；统一额外松弛另报；SUN on-hull，亚稳交集另列。

**仍需研究：**统一评价降低口径差异；跨模型历史训练费用和物理外推仍不同，条件任务比较尚为后续工作。

关联：C4, C5, C6；方向 C, D。

<a id="r47"></a>
## [R47] Periodic Bayesian Flow Networks with Additive Accuracy

[原始来源](https://proceedings.mlr.press/v306/lin26ar.html) · 首次已核公开：2026 · ICML 2026, PMLR 306, 75161–75176；状态 published conference paper

作者：Peijia Lin, Zihan Zhang, Zhangrui Zhao, Shaohao Rui, Junyi An, Yun-Fei Shi, Fenglei Cao, Weijie Ma et al.。

**任务：**CSP；periodic phase synthesis adjacent task。

**研究的问题：**圆周von-Mises后验的集中度依赖观测相对角度，不存在独立于观测的标量精度可加律，导致训练与采样日程敏感。

**核心方法：**周期标量嵌入二维(cos,sin)平面，执行Gaussian Bayes更新以恢复严格可加精度；Rao–Blackwell化解析边缘化整体周期平移，降低监督噪声。

**原文结果及适用范围：**

- 任务：MP-20 CSP；评价口径：沿用CrysBFN等变网络、12.3M参数，并对齐网络前向次数；500 forwards。；结果：匹配率70.06%，CrysBFN主基准64.35%；采样步数变化时保持更稳定。此结果不是DNG发现率。；原文位置：Tables 1, 4, 7–8

**仍需研究：**形式保证针对嵌入后的信息精度与特定平移目标，未保证真实物理稳定；理论状态信息与化学/几何可执行选择的关系仍可拓展。

关联：C1, C2, C4, C6；方向 A, B, C, D。

<a id="r48"></a>
## [R48] Open Materials Generation with Inference-Time Reinforcement Learning

[原始来源](https://arxiv.org/html/2602.00424v2) · 首次已核公开：2026-01-31 · ICML；2026；状态 published

作者：Hoellmer, Philipp, Martiniani, Stefano。

**研究的问题：**只有速度场、没有显式score的生成器怎样利用物理reward学习有效策略？

**核心方法：**给ODE增加小随机扰动定义可估计policy ratios/KL的代理SDE，在速度场上GRPO；另学习时间退火。DNG hybrid保持物种通道训练不变，只强化坐标。

**重要性：**SI/flow已有高效候选先验，反馈接口应覆盖不同连续动态。

**主要困难：**确定性ODE缺少policy比率，探索噪声、离散积分与annealing共同影响原模型行为。

**原文结果及适用范围：**

- 原文位置：AppendixK.1/Table6；结果：在训练组成固定的CSP式坐标后训练后恢复全mask DNG，已有自主部署效应。；定量结果：baseline：stable_percent：10.6；SUN_percent：0.4；MSUN_percent：16.9；sampling_steps：840；CSP_style_RL：stable_percent：7.5；SUN_percent：0.7；MSUN_percent：18.1；sampling_steps：50；denominator：每模型1000独立DNG样本。；评价口径：共同MACE-MPA-0松弛，LeMat-Bulk self-consistent MACE hull；hull≤0为S；作者称SUN收益主要来自U/N；采样预算不同。
- 原文位置：§5.1–5.2, AppendixI；结果：CSP速度场能量强化与学到的退火有效，post-relaxation已知CSP表现接近但需要更少松弛步。；评价口径：CSP matching/relative energy与独立DNG发现分别保存。

**仍需研究：**已完成conditional physics→DNG能力影响；真正剩余是新条件实现关系的内容、有效行动窗口和未见组合上的物理成功增量。

关联：C4, C5, C6；方向 C, D。

<a id="r49"></a>
## [R49] Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling

[原始来源](https://proceedings.mlr.press/v306/seong26a.html) · 首次已核公开：2026-02-23 · ICML2026, PMLR306:109105–109131；2026；状态 published main-conference paper

作者：Kiyoung Seong, Sungsoo Ahn, Sehui Han, Changyoung Park。

**研究的问题：**CSP、DNG和结构条件元素生成通常使用任务专属模型，难共享条件表征。

**核心方法：**A与(X,L)独立flow时间轴；DiT内电负性/Wyckoff排序与分层排列增强，不用外部显式模板。

**原文结果及适用范围：**

- 原文结果：同一模型在MP-20/MPTS-52上支持CSP、DNG、geometry-conditioned atom type，及固定其它位点的元素替换。；评价阶段：reference recovery; LeMat-GenBench multi-MLIP DNG; composition generation；定义：any-to-any是原子类型与几何互条件，不是光谱/自然语言任意模态；DNG以三MLIP平均及LeMat-Bulk一致hull评价；原文位置：§3; Tables1–4; AppendixF

**仍需研究：**变量通道互条件已统一；新增混合功能约束和多个共享局部关系的兼容泛化仍是独立能力。

关联：C1, C2, C3；方向 A, B。

<a id="r50"></a>
## [R50] Generative structure search for efficient and diverse discovery of molecular and crystal structures

[原始来源](https://arxiv.org/html/2604.27636v2) · 首次已核公开：2026-04-30 · arXiv；2026；状态 preprint

作者：Qin, Yifang, Shi, Yu, Tan, Junfu, Liu, Chang, Zhang, Ming, Lu, Ziheng。

**研究的问题：**数据驱动生成访问少量训练模式，RSS覆盖多但低能效率低，怎样共同探索多个相关极小值？

**核心方法：**把generative score和physical force放入共同更新，用预设sigmoid从先验引导过渡到物理主导。

**重要性：**CSP需要多晶型和欠探索组成，生成先验与物理地形有互补作用。

**主要困难：**物理力在高噪声结构上难代表终点资格；数据先验对欠覆盖盆地有偏，昂贵调用限制探索。

**原文结果及适用范围：**

- 原文位置：§2 coverage/efficiency；§3 Discussion；结果：作者系统的参考低能极小值覆盖与能量效率同时改善，并明确将runtime diagnostics自适应schedule列为未来方向。；denominator：coverage分母为充分RSS得到的参考低能结构集合；budget cost为尝试数除以该系统参考集大小。；评价口径：给定组成CSP与另列分子构象；潜在参考不完备及PES模型边界保留，不转写为独立无机DNG strict SUN。

**仍需研究：**固定schedule尚不能按科学状态识别反馈行动窗口；当前搜索的物理经验也未明确学入后续生成器。

关联：C4, C5；方向 C, D。

<a id="r51"></a>
## [R51] Composable Crystals: Controllable Materials Discovery via Concept Learning

[原始来源](https://arxiv.org/html/2605.14769v2) · 首次已核公开：2026-05-14 · arXiv preprint；2026；状态 preprint; no formal venue inferred

作者：Nian Liu, Yuwei Zeng, Ryoji Kubo, Nikita Kazeev, Stephen Gregory Dale, Artem Maevskiy, Pengru Huang, Thomas Laurent et al.。

**研究的问题：**随机生成缺少可复用构件和主动组合接口，难控制训练外探索。

**核心方法：**局部邻域VQ-VAE提取10,000概念；concept-set DDPM与合格样本self-refinement，再条件化原子DDPM。

**原文结果及适用范围：**

- 原文结果：MP-20/Alex-MP-20分别最高53.2%/51.7% VSUN相对增益，主要来自novelty；concept组合可预测spacegroup/family。；评价阶段：surrogate and selected DFT; local/global interpretability；定义：AppendixC.3稳定定义Ehull≤epsilon，未在该段明确统一数字；组合训练使用training-reference资格，不能代为设置strict阈值。atom vector含3坐标+100元素+6整胞lattice。；原文位置：§2.1 Eq2; §3; §4; C.3/C.4

**仍需研究：**可复用概念已确立，需解释局部化学、全局晶格及模板统计的各自贡献，及新共享局部关系组合的整体可行性。

关联：C3, C5, C6；方向 B, C, D。

<a id="r52"></a>
## [R52] Substitution-Based Analysis of Structural Novelty for Generative Models of Materials

[原始来源](https://arxiv.org/html/2606.23166v1) · 首次已核公开：2026-06-22 · arXiv；2026；状态 preprint

作者：Negishi, Masahiro, Walsh, Aron。

**研究的问题：**普通数据库新颖性中的哪些结构可由已知结构元素替换加松弛实现？

**核心方法：**训练重复判定；按晶格/site与Wyckoff寻找候选，化学相似度排序，元素替换后一次MACE-MPA-0松弛，再比对。

**重要性：**新化学组合与新结构机制都可能有价值，但支持不同科学主张。

**主要困难：**元素身份、原型、畸变与松弛需要共同匹配，未匹配也可能由检索不完备造成。

**原文结果及适用范围：**

- 原文位置：Table2；结果：在作者所评合格子集，多数数据库新颖结构可被替换路径重现。；定量结果：mattergen_duplicate_percent：20.5；mattergen_substituted_percent：60.6；mattergen_unmatched_percent：18.9；denominator：10000独立生成后，SMACT化学有效性、MACE-MPA-0松弛及MP-hull≤0.1 eV/atom筛选留下的各模型集合；Table2只报比例未逐行列子集N。；评价口径：MP-20训练模型；k=3每种结构检索路径top-k，共top-2k候选；Substituted含一次松弛。

**仍需研究：**输出分类揭示可替换性，不直接识别训练的因果机制；新化学组合的价值也不能由原型复用否定。

关联：C3, C5；方向 B, D。

<a id="r53"></a>
## [R53] Text-guided flow matching enables sample-efficient crystal structure generation

[原始来源](https://arxiv.org/html/2609.01076v2) · 首次已核公开：2026-09-01 · arXiv preprint；2026；状态 preprint; no formal venue inferred

作者：Wentao Li。

**研究的问题：**组成/对称/原型/性质混合描述难共享为可检查的continuous flow条件。

**核心方法：**冻结MatSciBERT、mean pooling和投影条件化CrystalFlow；database-derived结构化metadata，无原子坐标/晶格矢量。

**原文结果及适用范围：**

- 原文结果：MP-20单候选match67.65→77.80%，20候选92.04%；DNG元素数/密度分布改善。组成筛选1994例形成能符号1913/1994=95.94%。；评价阶段：reference recovery; distribution metrics; CGCNN selected-subset diagnostic；定义：性质诊断不是全DNG人口；另1000例diagnostic run formula2.10%/SG2.30%/crystal-system0%，作者未取为主DNG结果。；原文位置：Results Tables1–2; property consistency; Discussion; Supplementary diagnostic paragraph

**仍需研究：**结构化语言能帮助选择参考盆地；新意图语义泛化、精确DNG多字段遵循与物理终态联合目标仍可深化。

关联：C1, C2；方向 A, B。

<a id="r54"></a>
## [R54] OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery

[原始来源](https://arxiv.org/html/2609.26402v1) · 首次已核公开：2026-09-22 · arXiv；2026；状态 preprint

作者：Egg, Thomas, Sullivan, Harry Winston, Tadmor, Ellad B., Martiniani, Stefano。

**研究的问题：**怎样在高候选吞吐量下保持结构质量，并把reward学习扩展到有限时间flow map？

**核心方法：**all-atom transformer flow map直接从数据self-distillation训练；RAM以奖励加权clean-state条件信息更新切向场并保留consistency。

**重要性：**候选生成速度影响同预算可探索材料数，后训练不能牺牲few-step优势。

**主要困难：**flow map无直接随机policy接口，有限时间运输需保持一致性，物种/周期几何的表示各不同。

**原文结果及适用范围：**

- 原文位置：§3.2, §4, §5.1; Tables1–2；结果：few-step base同时用于CSP/DNG，RAM在CSP改善matching/energy与精度。；评价口径：RAM只实施CSP；MACE-MPA-0 reward先50步松弛，结构MR/RMSE为raw；跨论文结果按作者文献值，不当共同预算试验。

**仍需研究：**高吞吐与CSP对齐已有能力；结果类别的保持、DNG新化学组合迁移和物理响应知识仍需独立证据。

关联：C4, C5, C6；方向 C, D。

<a id="r55"></a>
## [R55] Topology-Stratified Materials Discovery with A Flow-Based Generative Model

[原始来源](https://arxiv.org/html/2609.26547v1) · 首次已核公开：2026-09-22 · arXiv preprint；2026；状态 preprint; no formal venue inferred

作者：Jingyi Zhou, Oyshee Chowdhury, Noah Oyeniran, Chongze Hu。

**研究的问题：**复杂对称拓扑与化学占位使生成/外推困难；单一能量指标遗漏动力学和温度资格。

**核心方法：**StageI scaffold→StageII occupancy→StageIII continuous Wyckoff fiber flow；物性fine-tuning；MSE评估引入能量/声子/MD。

**原文结果及适用范围：**

- 原文结果：绕过StageI给未见scaffold，33,439条件实现中5,921 MSE合格，覆盖107个训练外SG；50k常规生成MSE依MLIP25.5/45.5/44.1%；selected DFT/phonon/AIMD支持物理可靠性。；评价阶段：CHGNet/MACE/MatterSim MSE; selected DFT; separately public SUN；定义：MSE: formation energy<0、负声子DOS积分<0.05 phonon mode、300K/10ps NVT形态保持。另SUN31.2%使用Ehull≤0.1，S5.1.2说明baseline由发表结果取值而非统一重算。；原文位置：§2.3–2.5; S4; S5.1.2 Eq40

**仍需研究：**条件拓扑外推及多类物理验证是明确进步；自主形成未见scaffold、多个局部关系兼容和共同严格凸包资格仍有独立研究空间。

关联：C1, C2, C3, C5；方向 A, B, D。

<a id="r56"></a>
## [R56] Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors

[原始来源](https://arxiv.org/html/2609.33407v2) · 首次已核公开：2026-09-27 · arXiv；2026；状态 preprint

作者：Hovmand, Emma Lei, Elsborg, Jonas, Kandemir, Melih, Bhowmik, Arghya。

**研究的问题：**发现reward主要该改变化学访问还是条件结构先验，搜索历史novelty怎样影响二者？

**核心方法：**GRPO组成策略查询冻结CSP；CAN同时参照固定库与搜索历史；组成/实现互换实验，访问组成重放语料用于likelihood学习。

**重要性：**一个晶体reward可同时改变组成与结构，分开两者能识别瓶颈与付费计算的学习价值。

**主要困难：**novelty随历史变化而物理结构不变；终点反馈很难给不同离散/连续决定正确credit。

**原文结果及适用范围：**

- 原文位置：AppendixF.6/Table23；结果：same-composition corpus的实现来源改变KLDM学习收益。；定量结果：KLDM_control_SUN_percent：17.1；KLDM_plus_anchor_SUN_percent：16.5；KLDM_crystalite_rendered_SUN_percent：18.9；KLDM_unrelaxed_SUN_percent：16.7；Crystalite_control_SUN_percent：14.4；Crystalite_plus_anchor_SUN_percent：24.5；denominator：同1000个held-out组成请求，seed0；百分比分母沿用MatterGen实际计分N，Table23未逐行列N；Table12 released KLDM N=993。；评价口径：MatterGen自带MatterSim/FIRE-cell松弛、Alex-MP reference_MP2020correction hull及matcher；同基座优化步数/曝光匹配，不跨基座费用等同。
- 原文位置：AppendixF.6 corpus definition；结果：训练语料不是搜索时保存的成功端点。；定量结果：corpus_structures：27136；denominator：从日志候选经validity/duplicate gate后抽样，组成重放生成结构。；评价口径：只保存composition和scores，不保存当时geometry；整个搜索时段均匀抽样，无稳定或新颖阈值；默认KLDM实现，诊断臂改Crystalite。
- 原文位置：§4 reciprocal controls；结果：其模型/评价下改变组成来源的收益显著大于在DNG组成下更换结构实现，反馈进结构的收益依更新方式与基座变化。；评价口径：不同potential/gate/reference管线分别报告；不形成全部CSP优于DNG或始终冻结最优的结论。

**仍需研究：**组成为主的访问缺口已可诊断；新化学关系下条件能力缺口、何时应更新结构及跨请求可复用内容仍需研究。

关联：C2, C4, C5, C6；方向 A, C, D。

<a id="r57"></a>
## [R57] Where Should Physics Enter a Molecular Crystal Generator?

[原始来源](https://arxiv.org/html/2609.36398v1) · 首次已核公开：2026-09-28 · arXiv；2026；状态 preprint

作者：Tang, Haocheng, Wang, Junmei, Jin, Wengong。

**研究的问题：**相同物理信号通过训练目标、后训练reward或部署修复进入分子晶体生成，分别改变什么？

**核心方法：**Clari蒸馏all-atom flow map；共同UMA下MeanFlowNFT后训练、relax-and-distill、force guidance/固定胞松弛与经典修复比较。

**重要性：**每次部署付费与一次性学入权重有不同价值，需要解释哪种约束可学、哪种由表示决定。

**主要困难：**packing、局部clash与stereochemistry依赖不同自由度，模型表示未必可表达全部约束。

**原文结果及适用范围：**

- 原文位置：Table1/§4.1；结果：post-training提高packing，固定胞松弛主要修局部clash；普通relaxed-target回归收益有限。；denominator：200 validation families×20 samples，matched arms同epoch4，32NFE，mean±SE；released epoch6另行展示。；评价口径：分子晶体PB/clash、volume/PDD/packing recovery，shared UMA；不能外推无机strict SUN。

**仍需研究：**不同反馈入口的作用已有控制证据；有限作用不否定全部distillation，跨新组成物理关系及开放无机多解仍是另一任务。

关联：C1, C4, C6；方向 A, B, C, D。
