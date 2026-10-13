# 晶体生成：基础与研究演化

60页完整汇报，2026年10月13日。MatterGen为第23–27页；Chemeleon、SCIGEN、Chemeleon2为第28–30页。

## 1. 晶体生成：基础与研究演化

面向AI研究者：先介绍周期结构、数据、模型、指标和物理计算，再讲MatterGen与三篇近期子刊论文，随后讨论领域演化、六个挑战和四条研究路线。

## 2. 模型生成的是一个周期结构

一个晶体可以表示为 C = (A, F, L)，原子数 n 也可能需要生成。

| 变量 | 数学表示 | 物理含义 |
| --- | --- | --- |
| 元素 A | 每个位点的元素类别 | 组成相同，原子排布仍可以不同 |
| 分数坐标 F | fᵢ ∈ [0, 1)³ | 以晶格三条基矢表示原子位置 |
| 晶格 L | L = [a  b  c] | 决定晶胞大小、形状与角度 |
| 周期复制 | rᵢ,ₘ = L(fᵢ + m)，m ∈ ℤ³ | 有限胞内原子重复形成三维体材料 |

CIF保存结构及晶体学信息。生成CIF后，还需要计算能量、性质和结构身份。

A为每个位点元素，不仅是化学式。F为分数坐标，L列向量为三个晶格矢量，代码也可能使用行向量约定。占位无序、缺陷和磁性需要额外变量，当前多数DNG基准主要考虑有序周期结构。原胞为最小平移重复胞，常规胞强调对称，超胞通过重复扩大。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[IUCR How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists](https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html)

## 3. 同一个晶体可以有多种编码

**周期边界。** f与f+m对应周期等价位置。0.99与0.01在胞边界两侧可以很近。

**几何等价。** 原子顺序、整体平移、旋转和晶胞选择都能改写输入。

**对称表示。** 空间群操作展开非等价原子。Wyckoff位置记录对称位点的重复数与自由坐标。

图中A、B仅为虚构原子类别，四个方格重复相同的两个分数位置，不代表真实材料。坐标逐项MSE或CIF字符串相等通常不足以判断晶体身份。NaCl原胞2原子而常规立方胞8原子，说明胞选择会影响原子数限制。

来源：[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R16 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[IUCR How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists](https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html)

## 4. 先区分CSP、自主生成与条件设计

| 任务 | 给模型什么 | 模型需要输出 | 通常怎样评测 |
| --- | --- | --- | --- |
| 结构预测 CSP | 组成或化学式 | 晶胞与原子位置 | 参考命中、RMSD、多晶型 |
| 自主生成 DNG | 随机种子或噪声 | 组成与完整结构 | 有效率、S/U/N、SUN |
| 条件生成 | 性质、元素范围、空间群或图案 | 满足要求的完整结构 | 条件命中与物理资格交集 |
| 物理预测 | 完整原子构型 | 能量、力、应力或性质 | 误差、动力学与应用表现 |

化学系统条件如“Li–O”允许选择计量；给定“Li₂O”则固定了更具体的组成。

重构任务还可能编码整个输入晶体，不能自动视为仅给组成的CSP。MCFlow的互条件主要是元素A与几何(F,L)，不指所有自然语言、光谱和实验模态。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)

## 5. 数据库、训练集与参考库各有用途

| 资源 | 主要内容 | 在生成研究中的作用 |
| --- | --- | --- |
| Materials Project | DFT结构、能量及性质 | 衍生训练集、竞争相和评价参考 |
| Alexandria / OQMD | 高通量DFT及假想结构 | 扩大化学覆盖，提供相能量 |
| ICSD | 整理后的无机结构，主要来自实验 | 已知材料与新颖性参考，含无序占位 |
| COD | 开放CIF，覆盖多类晶体 | 结构与文献来源，能量标签需另配 |

数据库会更新；模型实际使用的是某次下载、过滤和划分后的固定快照。

ICSD也收录部分理论结构，因此不能写成全部实验材料。COD涵盖有机、无机、金属有机和矿物，不自动带统一DFT能量或力。不同库的泛函、磁性、修正和结构标准化需要对齐。

来源：[R04 Commentary: The Materials Project: A materials genome approach to accelerating materials innovation](https://doi.org/10.1063/1.4812323)；[ALEX Alexandria official dataset releases](https://alexandria.icams.rub.de/datasets.html)；[OQMD OQMD official structure sources and API documentation](https://oqmd.org/documentation/structures)；[ICSD ICSD official data curation and theoretical data categories](https://icsd.products.fiz-karlsruhe.de/en/about/data-curation)；[COD Crystallography Open Database (COD): an open-access collection of crystal structures and platform for world-wide collaboration](https://academic.oup.com/nar/article/40/D1/D420/2903497)

## 6. 常用生成基准各自检验什么

| 基准 | 固定规模 | 结构范围 | 用途与划分 |
| --- | --- | --- | --- |
| Perov-5 | 18,928 | ABX₃型，每胞5原子 | 组成变化为主；60/20/20 |
| Carbon-24 | 10,153 | 仅C，6–24原子，10 GPa | 结构与多晶型；60/20/20 |
| MP-20 | 45,231 | 89种元素，输入胞≤20原子 | 组成与结构；60/20/20 |
| MPTS-52 | 40,476 | 输入胞≤52原子 | 按时间划分<br>27,380 / 5,000 / 8,096 |

MP-20是特定基准文件和预处理流程，不等于现在查询所有“≤20原子”的MP结构。

前三个数据集为CDVAE固定快照，原随机划分60/20/20。Carbon-24来自10 GPa AIRSS候选低能10%及DFT弛豫，不能直接用来声称常压稳定发现。MP-20原过滤包括ICSD来源、Ehull<0.08eV/atom与formation energy<2eV/atom。MPTS-52按最早文献年份划分，缺失年份者排除。原胞/常规胞/超胞改变原子数，公开配置primitive=False，页面采用基准输入胞表述。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[CDVAE_CFG CDVAE official MP-20 configuration and build_crystal preprocessing](https://github.com/txie-93/cdvae/blob/main/conf/data/mp_20.yaml)

## 7. 生成终态数据与势能轨迹数据不同

生成器学习哪些结构会出现，MLIP还要学习离开终态后能量怎样变化。

**生成训练集。** 一条记录通常是一种结构及可选性质。Alex-MP-20将生成训练扩展到数十万结构。

**MLIP轨迹集。** 同一材料的弛豫过程包含多帧，每帧带能量、力和应力。MPtrj约158万构型来自约14.6万材料。

**划分单位。** CHGNet按材料划分80/10/10，避免同一材料的相邻帧跨训练和测试。

**复现信息。** 记录数据版本、计算口径、过滤和划分。构型数、材料数、模型参数量分别报告。

CHGNet MPtrj含89种元素，原模型能量标签已做MP2020兼容性修正。MatterSim模型名1M/5M接近参数规模，当前模型卡的训练样本数是3M/6M，不能混为一项。不同模型/快照的标签和覆盖范围需分别描述。

来源：[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MATTERSIM_CARD MatterSim official model card: v1.0.0-1M and v1.0.0-5M](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md)

## 8. 常见生成模型的技术分工

| 模型家族 | 代表工作 | 直接生成什么 |
| --- | --- | --- |
| 潜变量与周期去噪 | CDVAE | 先组织全局结构属性，再生成元素与坐标 |
| Diffusion | DiffCSP、MatterGen | 对晶格、周期坐标及可选元素联合去噪 |
| Flow / SI | FlowMM、OMatG | 学习连接初始分布与晶体分布的连续过程 |
| 语言与混合生成 | Crystal-LLM、FlowLLM<br>CrysLLMGen | 序列化结构；或用LLM提案接连续精修 |
| 对称与多模态 | SymmCD、MCFlow | 生成非等价位点，或完成元素与几何的互条件任务 |

DiffCSP主任务为固定组成的CSP，另有DNG扩展。FlowLLM针对LLM起始分布训练flow；CrysLLMGen加噪后用扩散精修，二者连续阶段固定元素。空间群和Wyckoff压缩几何自由度，但相稳定性仍需能量评价。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R21 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://arxiv.org/abs/2402.04379)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)

## 9. 代表论文怎样连接数据、模型和评测

| 工作 | 数据与任务 | 主要评测对象 |
| --- | --- | --- |
| CDVAE | Perov-5 / Carbon-24 / MP-20<br>重构与DNG | 有效率、指纹覆盖、性质分布 |
| DiffCSP / FlowMM | MP-20等，组成CSP与DNG | CSP匹配/RMSD；DNG另做物理评价 |
| FlowLLM / CrysLLMGen | MP-20为主，混合DNG | 前者报告DFT-SUN，后者主要CHGNet评测 |
| MatterGen | Alex-MP-20，DNG与条件设计 | 统一DFT弛豫、SUN、性质及实验案例 |
| Chemeleon2 | MP-20 / Alex-MP-20<br>DNG与性质后训练 | 代理势评价与选定DFT，含性质交集指标 |

CDVAE原文主要生成指标不是大规模DFT发现率。FlowLLM所引4.92%为DFT，CrysLLMGen所引9.21%为CHGNet。MatterGen正文对生成器与基线使用DFT，公开repo默认MatterSim评测另列。Chemeleon2细节在第28页及来源笔记。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)

## 10. 生成器与MLIP承担不同工作

MLIP学习势能面；优化器使用它给出的力与应力更新结构。

| 物理模型 | 主要训练信息 | 典型用途 |
| --- | --- | --- |
| M3GNet | MP弛豫中的能量、力、应力 | 结构弛豫、筛选与材料模拟 |
| CHGNet | MPtrj，加磁矩相关监督 | 电荷环境相关表示、弛豫与动力学 |
| MACE-MP-0 | 等变多体网络，MPtrj | 能量及导数、弛豫与MD |
| MatterSim-v1 | 离平衡与温压采样数据 | 更广物理状态下的预测与计算 |

物理输出包括 E、F = −∇ᵣE 和应力。记录实际checkpoint及标签口径。

力从总能量对位置的导数得到，不能把每原子能量不加转换地求导当总力。MACE是架构和模型系列，MP-0/MPA/OMat等权重不同。CHGNet磁矩作为训练监督并非精确原子电荷输入。模型覆盖元素集合，不表示它覆盖所有配位、温度和压力状态。

来源：[R10 A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[MACE A foundation model for atomistic materials chemistry](https://arxiv.org/html/2401.00096v3)；[MATTERSIM MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures](https://arxiv.org/html/2405.04967v2)；[MATTERSIM_CARD MatterSim official model card: v1.0.0-1M and v1.0.0-5M](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md)

## 11. 一次生成实验包含哪些计算

| 步骤 | 得到什么 | 应记录的费用或数量 |
| --- | --- | --- |
| 提出与有效性检查 | 原始结构、可计算候选 | 请求数、失败数、采样步数与硬件 |
| 结构弛豫 | 局部低能终态及收敛状态 | MLIP/DFT调用、优化步数、资源小时 |
| 能量与结构匹配 | 稳定资格、U/N/SUN | 竞争相参考、匹配规则、未知状态 |
| 性质与物理复核 | 功能性质、声子或迁移等 | 被选样本数、计算参数、筛选分母 |
| 实验材料 | 实际产物、结构与性质 | 尝试数、纯度、表征与测量条件 |

发现费用还包含数据、训练、失败重试和参考相计算；DFT性质调用只是其中一项。

不同GPU小时与CPU core-hours分别报告，只有有明确计费或换算才能相加。生成速度与完整发现成本不同。性质选样后的成功比例属于条件样本群体，应保留筛选过程。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)

## 12. Validity先判断候选能否继续计算

| 检查 | 具体对象 | 结果含义 |
| --- | --- | --- |
| 可读取与晶胞合法 | CIF、元素、占位、晶格体积 | 得到完整且可解析的结构 |
| 几何有效性 | 周期最小距离、密度、异常晶格 | 排除严重碰撞或畸形结构 |
| 组成有效性 | 允许氧化态与电荷平衡等规则 | 符合所采用的化学启发式 |
| 规则示例 | SMACT可寻找 Σₑ nₑqₑ = 0 的赋值 | NaCl可用Na⁺和Cl⁻解释电荷平衡 |

通过有效性检查后，再评价相稳定性和目标性质。

距离必须考虑周期镜像。SMACT可单独处理单质和金属合金，离子氧化态规则有适用范围。几何有效、组成有效及其交集分开报告。原论文公式和实际代码中的检查项应共同核对。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[SMACT SMACT screening module](https://smact.readthedocs.io/en/latest/smact.screening.html)

## 13. CSP评测：参考命中率与几何误差

MR@k = 命中至少一个参考结构的测试请求数 / 全部测试请求数

**匹配。** 处理原子重排、平移和晶胞等价后，按晶格、角度及位置容差比较。

**RMSD。** 匹配原子的位移均方根。文献可能报Å，也可能除以 (V/n)¹ᐟ³ 归一化。

**采样预算。** MR@20通常允许每个组成20个候选。best-of-k评测可用参考答案选最好者。

**多晶型。** 同一组成可能有多个低能结构，单个数据库参考不代表全部可行答案。

DiffCSP使用stol=0.5、ltol=0.3、angle_tol=10°；stol按自由长度归一化，不能解释为0.5Å。需要区分到参考结构的误差与生成结构到弛豫终态的位移。能量排序后的top-k还需计入排序成本。

来源：[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R42 All that structure matches does not glitter](https://arxiv.org/html/2509.12178v2)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)

## 14. 分布指标衡量覆盖与偏移

| 指标 | 如何计算或理解 | 它描述什么 |
| --- | --- | --- |
| COV-Recall | 参考集合中被生成指纹邻域覆盖的比例 | 生成集合覆盖了多少参考变化 |
| COV-Precision | 生成集合中靠近参考指纹分布的比例 | 有多少输出处于参考邻域 |
| JSD | 两个类别分布的对称差异 | 元素、空间群等分布偏移 |
| Wasserstein-1 | 将一份标量分布搬成另一份的平均距离 | 密度、能量等性质分布差异 |

这些指标描述统计分布；稳定新材料还需要结构匹配及物理资格。

CDVAE使用CrystalNN结构指纹和归一化Magpie组成指纹。其Appendix G同一对同时近的公式，与公开源码分别取两类最近邻再AND存在差别，复现需声明版本。教学例：密度{3,3}与{4,4}g/cm³的W1=1g/cm³。空间群编号是类别，编号间数值距离不具有一般物理含义。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[SCIPY_JS scipy.spatial.distance.jensenshannon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html)；[SCIPY_W scipy.stats.wasserstein_distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)

## 15. 形成能和凸包能比较不同的竞争对象

E_form = (E_cell − Σₑ nₑ μₑ) / n

**形成能。** 比较化合物与对应元素参考相。单位通常为eV/atom。

**相分解。** 即使形成能为负，也可能更愿意分解成若干更低能化合物。

**凸包。** 在组成守恒下，求参考相混合所能达到的最低能量。

**物理条件。** 常见电子能凸包近似0 K条件；压力下比较焓，有限温度平衡需要自由能。

教学算例：AB总能−10.6eV，A与B参考每原子能−4.0和−5.6eV，Eform=(−10.6+4.0+5.6)/2=−0.5eV/atom。凸包h_R(x)=min Σλ_r E_r，约束λ≥0、Σλ=1、Σλx_r=x。

来源：[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)

## 16. 凸包能量差的两种口径

**固定参考包。** ΔE_ref = 候选形成能 − 参考包能量。它可为负，表示降低旧参考包。

**高于凸包的能量。** 把候选也加入相集合后，E_above hull ≥ 0；位于凸包上的结构为0。

**教学算例。** A₂B能量−0.450，旧包为−0.3667 eV/atom，ΔE_ref = −0.0833。

参考点A(0,0)、A3B(.25,−.30)、AB(.5,−.50)、AB3(.75,−.30)、B(1,0)。候选A2B=(1/3,−.45)位于参考线下方；另一A2B=(1/3,−.20)形成能虽负仍在参考包上方。多个新候选也会互相竞争。某些生成论文把带符号参考距离记为Ehull，读文献时需核准定义。

来源：[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[PYM_HULL pymatgen.analysis.phase_diagram.PhaseDiagram](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.phase_diagram.PhaseDiagram.get_decomp_and_e_above_hull)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)

## 17. S、U、N与SUN分别回答什么

| 指标 | 计算对象 | 需要声明的条件 |
| --- | --- | --- |
| Stable，S | 达到稳定或近凸包阈值的结构 | 阈值、评价器、能量参考、弛豫阶段 |
| Unique，U | 一批结果中去重后的不同结构 | 匹配容差、聚类顺序、代表选择 |
| Novel，N | 与固定参考库不匹配的结构 | 参考库版本、化学和结构匹配规则 |
| SUN | 稳定且新颖的结果去重后的数量或比例 | 完整交集和分母，不假定各项独立 |

新化学可以沿用熟悉结构原型。参考库外、训练集外和项目首次发现是不同概念。

S/U/N应在同一物理终态重算。先筛稳定与新颖再去重，是一个可清楚解释的操作口径；其他论文顺序及分母可不同。引用其结果时保持原定义。标准hull=0与固定参考距离≤0按上页定义分别标明。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[R52 Substitution-Based Analysis of Structural Novelty for Generative Models of Materials](https://arxiv.org/html/2606.23166v1)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)

## 18. SUN的分母与去重：一个算例

**全部请求。** 100个提案，90个通过有效性检查。

**稳定与去重。** 40个确认稳定，去重剩30个不同稳定结构。

**新颖交集。** 其中12个不在参考库，SUN = 12/100 = 12%。

条件比例相乘可还原漏斗；全体S、U、N的边缘比例不能直接相乘。

90/100 × 40/90 × 30/40 × 12/30 =12/100为条件计数恒等式。相同数据若全体U=60%、全体N=45%，乘.4×.6×.45=10.8%不等于SUN12%。如果只有80个完成评测，40/80是已评测比例，40/100是确认产出，剩余状态保留未知。

来源：[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)

## 19. DFT在计算什么，为什么有不同结果

固定原子时求电子密度；得到能量、力和应力后，再决定是否更新结构。

| 计算设置 | 含义 | 影响 |
| --- | --- | --- |
| 泛函、Hubbard U | 电子交换关联及局域电子近似 | 相对能量、带隙与磁性 |
| 赝势 / PAW | 核电子与价电子表示 | 能量基准与数值精度 |
| k点与平面波截断 | 布里渊区积分与基组大小 | 能量、力和应力收敛 |
| 磁性、SOC与收敛标准 | 电子状态及计算精度 | 可能收敛到不同电子或磁性解 |

一次DFT弛豫含多次电子自洽计算。比较相稳定性时，候选和参照必须相容。

SCF在固定离子下迭代电子密度，外层离子/晶胞优化可多次调用SCF。PBE为常见近似泛函，并非精确真值。MP特定GGA(+U)设置用520eV截断及指定k点密度，但不能作为全部体系统一收敛保证。结构优化后可进行静态能量、能带或DOS计算。

来源：[MP_DFT Materials Project: Parameters and Convergence](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details/gga+u-calculations/parameters-and-convergence)；[MP_ELECTRONIC Materials Project: Electronic Structure](https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)

## 20. 弛豫是在寻找局部低能结构

| 方式或工具 | 优化什么 | 应报告什么 |
| --- | --- | --- |
| 固定晶胞 | 原子位置 | 原子最大力、步数、是否收敛 |
| 变胞弛豫 | 原子位置与晶胞形状/体积 | 力、应力、外压和约束 |
| FIRE / L-BFGS | 使用能量及梯度作局部优化 | 优化器、阈值、最大步数 |
| MD / AIMD | 按运动方程推进时间 | 温度、系综、步长与物理时长 |

FIRE的200步是优化工作量；MD的10,000步×1 fs才对应10 ps模拟时间。

小残余力说明接近驻点，曲率/声子提供进一步局部稳定性证据。FIRE使用伪动力学，优化时间步不是材料演化的物理时长。达到最大步数和达到力阈值分别报告。压力下目标包含适当PV项。

来源：[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)；[ASE_FILTER ASE: Filters](https://docs.ase-lib.org/ase/filters.html)；[ASE_MD ASE: Molecular dynamics](https://docs.ase-lib.org/ase/md.html)

## 21. MLIP与DFT怎样配合评价

先用低成本势处理大量候选，再围绕论文主张选择DFT与性质复核。

**标签一致。** MLIP可能学习raw或已修正能量。候选、元素参考和竞争相必须处于相容尺度。

**具体例子。** CHGNet原MPtrj权重学习已做MP2020修正的能量，重复加同一修正会再次移动能量。

**自洽凸包。** 可用同一MLIP计算候选和竞争相，再构造参考包；模型外推误差仍需研究。

**DFT复核。** 记录选样规则、原始分母与失败。随机核验、阈值附近核验和高分筛选回答不同问题。

不同checkpoint可能使用PBE、r2SCAN、MatPES等训练数据，不能对所有MLIP统一说raw或corrected。自洽MLIP hull还需说明参考结构是固定几何单点，还是同一势弛豫后评价。项目既有MP校正约定不因这份教学PPT改变。

来源：[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[CHGNET_DOC CHGNet official project documentation](https://chgnet.lbl.gov/)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)

## 22. 功能与物理稳定性怎样进一步计算

| 科学问题 | 计算或测量 | 得到的证据 |
| --- | --- | --- |
| 小扰动是否失稳 | 声子：二阶力常数与频率 | 集体微扰的动力学稳定性 |
| 刚度及机械响应 | 应变—应力，弹性张量 Cᵢⱼ | 体模量、剪切模量及机械稳定条件 |
| 有限温度下的行为 | MD / AIMD，给定温度与时间 | 该窗口内的结构保持或扩散 |
| 离子迁移或结构转变 | NEB / CI-NEB寻找路径与鞍点 | 指定端点之间的激活势垒 |
| 电子与实际材料性质 | 能带 / DOS；XRD、成分及物性测量 | 计算功能与实验产物的相应证据 |

每项计算回答一个具体问题。低凸包能、无虚频、短时MD保持与实际合成各有含义。

声子负ω²对应虚频，Γ点不能代表全部波矢，近零声学频率需检查数值收敛。弹性张量的小应变正定性支持相应机械稳定，高体模量主要表示刚度。Ea=Esaddle−Einitial，单条低势垒仍需连通性、载流子浓度和温度才能联系宏观输运。XRD/Rietveld识别相及结构，化学成分和功能测量检验实际产物。

来源：[PHONOPY Phonopy: Formulations](https://phonopy.github.io/phonopy/formulation.html)；[MP_ELASTIC Materials Project: Elastic Constants](https://docs.materialsproject.org/methodology/materials-methodology/elasticity)；[ASE_MD ASE: Molecular dynamics](https://docs.ase-lib.org/ase/md.html)；[ASE_NEB ASE: Nudged elastic band](https://docs.ase-lib.org/ase/neb.html)；[MP_ELECTRONIC Materials Project: Electronic Structure](https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)

## 23. MatterGen 1/5：问题、数据与训练对象

目标是在元素、位置与晶胞上联合生成，并用科学条件改变生成分布。

| 环节 | 正式论文采用什么 | 为什么这样做 |
| --- | --- | --- |
| 预训练数据 | 607,683个Alex-MP-20训练结构<br>输入胞≤20原子，近凸包过滤 | 联合学习化学与结构分布 |
| 能量对齐 | MP + Alexandria，非MP结构<br>按MP PBE(+U)流程重算 | 把不同来源放到可比较的能量尺度 |
| 稳定性参考 | 850,384个有序参考结构 | 计算相竞争的固定参考凸包 |
| 新颖性参考 | 上述结构再加117,652个<br>无序ICSD结构 | 考虑实际已知材料和占位无序 |

这是特定训练和参考快照。完整公开Alex-MP-20的675,204条与训练分区不同。

MP v2022.10.28、ICSD release2023.1、Alexandria官方资源2022.126。训练过滤Ehull<0.1eV/atom，移除well-explored系统和ICSD-only结构。OMatG报告完整675204及原90/10拆分，Nature正式训练607683。正式reference850384与公开repo845997不混用。来源计数为固定论文版本，不是当前数据库总量。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_DATA MatterGen official Alex-MP data release](https://github.com/microsoft/mattergen/blob/main/data-release/alex-mp/README.md)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)

## 24. MatterGen 2/5：联合扩散与条件适配

**建模。** 元素用吸收mask噪声，位置用周期噪声，晶格用连续噪声；GemNet-dT联合预测去噪。

**训练与控制。** 条件经adapter注入，微调全部网络权重。采样用classifier-free guidance，保持周期结构表示。

原图保持原始比例与标记，来源Nature Fig1。SI A/B：GemNet-dT 4 message-passing层，邻域7Å，node/edge hidden512；categorical D3PM与coordinate/lattice score-matching联合损失。基础模型1.74M训练步，8×A100，每GPU batch64/global512，Adam lr1e-4。4个zero-init adapters；SI B.1明确fine-tune更新所有权重，非只训adapter。fine-tune globalbatch128 lr6e-5。1000 ancestral predictor步，位置/晶格Langevin corrector，SNR0.4/0.2；条件CFG γ=2。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)

## 25. MatterGen 3/5：无条件生成怎样评测

相同Alex-MP训练范围下，用DFT弛豫后的结构评价SUN。

**评测链。** 1,024个样本经DFT弛豫、能量比较与结构匹配。

**结果。** 约75%在参考凸包0.1 eV/atom内，约3%低于固定参考包。

**解释。** Table D4的SUN为38.57%，生成到弛豫终态的RMSD为0.021 Å。

SI TableD4的同Alex-MP对比：MatterGen SUN38.57%、RMSD0.021Å；DiffCSP33.27%、0.104Å。标准初批1024；Nature约75%与3%为正文概括。RMSD是到DFT弛豫终态的变化，不是CSP到已知参考的误差。参考hull850384有序结构，novelty另含117652无序ICSD。当前公开repo默认MatterSim预测评价，且checkpoints为重训版本，不直接替代本文DFT数字。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REPO Microsoft MatterGen official README and data-release descriptions](https://github.com/microsoft/mattergen)

## 26. MatterGen 4/5：条件设计如何验证

性质条件的价值，用满足目标且物理合格的候选数量检验。

**条件与标签。** 磁性约60.5万、带隙约4.2万、体模量约5,000个标签，分别用于对应任务。

**计算对照。** 同一预测器辅助，180次DFT性质调用：MatterGen获得106个，筛选参照40个。

**代价范围。** 原文预算轴只统计性质调用。训练、筛选与DFT弛豫另计。

Fig4a-c显示性质条件分布，Fig4h为bulk modulus>400GPa的合格数量。条件训练标签可由不同物理或ML预测器得到，例如bulk modulus adapter用ML预测标签，最终以DFT性质验证。需要同时检查条件命中及SUN交集，不把条件分布均值当材料发现。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)

## 27. MatterGen 5/5：计算怎样连接实际实验

**筛选过程。** 32,768个提案逐级筛到75个DFT候选，选四个尝试，原文报告一个产物。

**结构与成分。** 原文将产物拟合为约98%无序TaCr₂O₆，另有约2% Cr₂O₃。

**功能测量。** 目标200 GPa，DFT约222。实验换算体模量158±11 GPa，最高169 GPa。

Fig6a为XRD/Rietveld及样品，b/c为有序目标及无序结构，d是95个ICSD再发现的DFT体模量，不是实验模量图。SI筛选：32768→7919含氧→2196(MatterSim Ehull≤.05)→551去重/新颖→119声子无负频→75(DFT≤.03)→4专家挑选→1报告合成，另外3个尝试失败。主文DFT222GPa，图6b标221GPa，页面用约222。纳米压痕测Young模量，K=Y/[3(1−2ν)]，ν取DFT0.30，四次推算均值158±11，最大169。原文“距目标20%内”采用最大值。2026-04-20 Juelsholt在Materials Horizons 13,5672–5679的再分析重新精修公开PXRD，报告Ta0.43Cr0.57O2，并指出已知TaCrO4型结构及三种有序近似存在训练资料，挑战该案例新化合物身份。这里分别归属2025原报告与2026再分析，未重做PXRD精修。

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REANALYSIS Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)

## 28. Chemeleon：文本引导化学空间探索

Nature Communications 16, 4379 · 2025

将组成与晶系的文字要求转成候选，再用物理计算判断材料资格

**数据。** MP-40：32,525个结构，≤40原子；按时间留出708个测试结构

**条件表示。** 组成与晶系生成文本；Crystal CLIP对齐文本与晶体图，FiLM/CFG将条件传入去噪器

**生成基座。** DiffCSP式周期等变扩散：联合生成元素、坐标与晶格；原子数另行给定

**AI评测。** 每题20次采样；一般文本下参考结构恢复率由6%升至20%（BERT与Crystal CLIP对照）

**物理案例。** Li–P–S–Cl：SMACT选组成，MACE预筛，DFT相图；四个选定四元结构声子无虚频

语言要求通过学习到的条件表示进入生成；相图和声子检验相竞争与局部稳定性。

文本接口把组成和结构偏好放在同一句描述里；本文实证主要是化学式与晶系。MP2023.11.01的32,525个结构来自实验记录：原胞≤40原子、E_hull<0.25 eV/atom、边长≤20 Å，剔除常温气体。2018年8月2日后的708条作为未来测试。GPT-3.5按组成与晶系为每结构生成五种改写。
模型先对齐材料BERT和晶体图嵌入，再以FiLM和CFG输入DiffCSP式去噪器。每题给文本和原子数、采20次；一般文本的参考恢复率为BERT 0.06、Crystal CLIP 0.20。计量为软条件。
应用先用SMACT挑781种Li–P–S–Cl组成，再采样、MACE预弛豫和预筛、VASP/PBE相图计算。原文报告相对原MP参考包17个更低能及435个E_hull<0.15 eV/atom候选，前者含二/三元相，部分含分子片段或空穴；并入新包后Fig.5a的250个四元亚稳结构是另一统计。四个选定四元结构用PBEsol/PhononMaker计算声子，无虚频。Table1中metastability是未弛豫MACE与同组成参考真值的能量差窗口，按原文单列。

[Park, H., Onwuli, A. & Walsh, A. Exploration of crystal chemical space using text-guided generative artificial intelligence. Nature Communications 16, 4379 (2025). DOI:10.1038/s41467-025-59636-y.](https://www.nature.com/articles/s41467-025-59636-y)

## 29. SCIGEN：把功能图案嵌入晶体

Nature Materials 25, 223–230 · 2025在线发表／2026卷期

把与电子行为相关的原子排列作为条件，生成与之兼容的完整材料

**基座与规模。** 复用MP-20训练的DiffCSP；约千万提案经预筛后，选26,000个做DFT

**约束方法。** 每步把带噪图案按mask并入去噪状态，约束目标子晶格，补全周围原子与晶胞

**结构筛选。** 残余力与小畸变筛选、MP-20外新颖性和批内去重后，保留3,018个结构

**电子功能。** Lieb图案候选的DFT能带出现费米能附近平带，建立几何与电子行为的联系

**实验验证。** Ti–Pd–Bi/Sb提案指导合成；实物计量与占位变化，磁性为顺磁／抗磁，输运为金属

功能图案提供生成条件；电子结构计算和合成测量检验材料层面的实现。

晶格几何影响电子跳跃和磁性挫折。SCIGEN以三角、蜂窝、kagome、Lieb层为外部结构条件：每步先给图案加入当前噪声，再与自由部分按mask合并，用既有DiffCSP继续去噪，无需为图案重新训练底座。
正式论文Data availability报告1,006万生成、101万预筛，从中选26,000个做DFT；24,743得到弛豫输出。SI §12/Table3按残余力、小畸变、MP-20外及去重进一步保留3,018。这个统计检验结构保持和新颖性，其物理定义与凸包SUN分开。
Lieb候选的DFT平带在费米能上方约0.1–0.2 eV；材料Ce3NaTb4、CeDy3NdYb见arXiv:2407.04557v1 Fig.4。实验选材结合化学判断：TiPdBi三角图案与TiPdSb方格图案提示Ti–Pd–Bi/Sb探索；衍射精修得到TiPd0.22Bi0.88与Ti0.5Pd1.5Sb，出现无序、计量及空间群变化。SQUID分别显示顺磁／抗磁，四探针电阻率显示金属，约2 K未见超导。来源为正式SI §10.1–10.7。
正式SI：https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41563-025-02355-y/MediaObjects/41563_2025_2355_MOESM1_ESM.pdf
Lieb原始能带：https://arxiv.org/html/2407.04557v1

[Okabe et al. Structural constraint integration in a generative model for the discovery of quantum materials. Nature Materials 25, 223–230 (2026); published online 22 September 2025. DOI:10.1038/s41563-025-02355-y.](https://www.nature.com/articles/s41563-025-02355-y)

## 30. Chemeleon2：用物理奖励改变生成分布

Nature Machine Intelligence 8, 1087–1099 · 2026

在连续潜空间中用GRPO优化近凸包资格、新颖性和多样性

**模型与物理反馈。** VAE编码晶体，DiT在潜空间生成。；GRPO用物理与多样性奖励；更新去噪策略。

**收益与结构覆盖。** N：62.3% → 97.5%；U：99.4% → 88.7%；生成收益伴随唯一性下降

**性质条件与物理检验。** 目标带隙3 eV，512个候选中82个同时满足mSUN和2.7–3.3 eV带隙（DFT）。

Chemeleon2先以VAE把元素、位置、晶格编码为连续潜变量，再训练latent DiT；GRPO将去噪步骤作为策略轨迹。奖励来自MACE-MPA-0估计的凸包能量差、AMD距离描述的新颖性/唯一性、以及组成和结构嵌入的批次多样性。
Fig.3在Alex-MP-20训练后每模型生成10,000个原始结构，不进行几何优化；mSUN要求E_hull<0.1 eV/atom。图中15.9→61.3是同一Chemeleon2基座加入RL前后的比较；metastability为51.2→72.1，N为62.3→97.5，U为99.4→88.7。
Fig.6使用43,295个带隙标签，目标3 eV，每模型512样本；RL样本中82个同时具有mSUN资格与2.7–3.3 eV的DFT带隙。原始样本mSUN为45.3%；附录另报告DFT弛豫后mSUN 60.8%、metastability 85.5%。1,000个结构的MLFF/DFT能量比较见Supplementary Fig.21。这里体现奖励改变生成能力和目标命中，原始势模型协议与MatterGen的弛豫DFT协议各自保留。

[Park, H. & Walsh, A. Guiding generative models to uncover diverse and novel crystals via reinforcement learning. Nature Machine Intelligence 8, 1087–1099 (2026). DOI:10.1038/s42256-026-01262-4.](https://www.nature.com/articles/s42256-026-01262-4)

## 31. 研究目标与科学价值

在相同计算投入下，获得更多稳定、独特且新颖的材料。

**稳定性 S。** 相对声明的竞争相集合计算能量，严格稳定阈值为 Eₕᵤₗₗ ≤ 0。

**独特与新颖。** U衡量集合内去重，N衡量相对参考库的新颖性。SUN同时满足S、U和N。

**条件生成。** 在稳定发现的基础上，控制组成、结构关系或目标性质。

**科学价值。** 材料空间远大于数据库。生成模型需要把已有知识用于尚未记录的材料。

项目主目标为严格SUN。S采用E_hull≤0，单位eV/atom。U为生成集合内去重，N相对于声明的参考结构集合。稳定性评价应明确能量理论水平和参考相集合。熟悉结构框架中的新稳定化学也可以构成发现。

来源：[R04 Commentary: The Materials Project: A materials genome approach to accelerating materials innovation](https://doi.org/10.1063/1.4812323)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R31 Establishing baselines for generative discovery of inorganic crystals](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)

## 32. 论文中的任务决定了证据的含义

| 原文任务 | 输入与输出 | 对应工作 |
| --- | --- | --- |
| 组成条件CSP | 已知组成，生成晶胞和原子位置 | DiffCSP、FlowMM |
| 自主生成DNG | 同时提出组成与完整晶体 | CDVAE、MatterGen、OMatG |
| 性质 / 文本条件生成 | 目标性质或描述，生成候选结构 | MatterGen、TGDMat、PLaID++ |
| 结构条件生成 | 对称配置或局部图案，补全晶体 | SymmCD、SCIGEN |
| 互条件生成 | 给定组成生成几何，或反向生成元素 | MCFlow |
| 物理搜索与模型更新 | 计算结构结果，改进行动或生成分布 | RL-CSP、GNoME、OMatG-IRL |

原文任务比方法名更能说明证据支持什么。CSP为给定组成结构预测，DNG为自主生成。物理搜索与模型更新一行包含不同下游对象，后续C4/C6及路线C分别展开。GNoME主要更新物性预测模型，不能作为生成器响应学习已经成功的证据。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R37 Periodic Materials Generation using Text-Guided Joint Diffusion Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R14 Reinforcement learning in crystal structure prediction](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)

## 33. 领域沿三条研究线并行发展

新方法不断扩展可表达的结构、可接受的条件和可利用的物理信息。

| 研究线 | 早期基础 | 2023—2024 | 2025—2026 |
| --- | --- | --- | --- |
| 结构表示与生成 | iMatGen、FTCP<br>CDVAE | DiffCSP、FlowMM<br>晶体语言模型 | OMatG、SymmCD<br>CrysLLMGen、MCFlow |
| 条件与科学知识 | 性质潜空间<br>给定组成 | 对称约束<br>语言条件与连续精修 | MatterGen、SCIGEN<br>PLaID++、组合条件 |
| 物理与多解发现 | AIRSS、USPEX<br>材料数据库 | 通用势、GNoME<br>RL搜索与晶体QD | 物理后训练<br>层级探索与数据回流 |

时间按代表工作首次公开或正式发表概括。三条线之间不断交换方法。

本页是能力演化的综合，不表示每一方法直接继承上一列。正式日期与首稿日期在完整文献年表中分别记录。SI、diffusion和flow存在数学联系，LLM可与连续生成模型结合。

来源：[R01 High-Pressure Phases of Silane](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504)；[R02 Crystal structure prediction using ab initio evolutionary techniques: Principles and applications](https://doi.org/10.1063/1.2210932)；[R06 Inverse Design of Solid-State Materials via a Continuous Representation](https://doi.org/10.1016/j.matt.2019.08.017)；[R07 An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties](https://arxiv.org/pdf/2005.07609v3)；[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 34. 周期生成开始直接建模晶体几何

| 工作 | 解决的主要困难 | 方法与已建立的能力 |
| --- | --- | --- |
| CDVAE<br>ICLR 2022 | 周期结构的可学习生成 | 潜变量组织结构属性，周期去噪生成坐标。 |
| DiffCSP<br>NeurIPS 2023 | 给定组成下晶胞与坐标耦合 | 联合等变扩散，提高参考结构预测能力。 |
| FlowMM<br>ICML 2024 | 周期变量的连续生成路径 | 在晶体流形上进行 flow matching。 |
| OMatG<br>ICML 2025 | 离散元素与连续几何联合生成 | 随机插值（SI）结合连续几何与离散元素过程。 |

这些方法提供了联合生成工具。新的问题是它们如何学到未见化学与几何的正确配对。

SI = stochastic interpolants，随机插值。SI为流与扩散提供统一的路径建模方式。这里保留方法差异，不将其描述成依次淘汰的模型序列。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)

## 35. 稳定率提高时，SUN仍可能下降

PLaID++的坐标表示对照说明，稳定性收益可能同时伴随发现数量损失。

**同一对照。** 稳定率由10.35%升至15.94%，SUN由2.93%降至1.69%。

**科学问题。** 怎样让稳定性优化增加不同的新结构？

**结果范围。** 该现象来自坐标表示消融。论文主方法研究表示与偏好学习。

偏好信号由eqV2提供。失败解析重新采样，因此分母是可解析CIF而非全部生成请求。该对照不代表PLaID++主方法整体下降。图按原文数值重绘，不推断未在该对照中分离的U/N损失机制。

来源：[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)

## 36. 稳定发现的评价需要共同口径

| 必须说明的条件 | 为什么影响结论 |
| --- | --- |
| 稳定阈值与参考相集合 | Eₕᵤₗₗ ≤ 0 与 ≤ 0.1 eV/atom对应不同的合格范围。 |
| 物理层级与弛豫流程 | DFT和MLIP提供不同证据。弛豫可能改变能量和结构身份。 |
| 分母与完整费用 | 全部请求、可解析结构和完成评价的样本数需要分别保留。 |
| 新颖性与独特性 | 参照集合和匹配阶段决定N与U，原型新颖性可作为额外分析。 |

本项目主结果采用严格SUN。熟悉原型中的新稳定化学仍属于有效发现。

严格SUN采用S≤0，另报M≤0.1。DFT校正口径、元素参考和竞争相集合固定。N/U与S应对应同一评价阶段。LeMat主比较各模型提交结构的流程不同，不能假设所有结构都是统一未弛豫输入。原型类别变化与参考结构新颖是互补指标。

来源：[R31 Establishing baselines for generative discovery of inorganic crystals](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)；[R42 All that structure matches does not glitter](https://arxiv.org/html/2509.12178v2)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)；[R52 Substitution-Based Analysis of Structural Novelty for Generative Models of Materials](https://arxiv.org/html/2606.23166v1)

## 37. C1：科学条件怎样得到正确结构

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2019–2022<br>iMatGen、FTCP、CDVAE | 性质逆设计、结构重构<br>目标性质或潜变量输入 | 建立可解码的周期表示。问题转向目标条件能否在完整结构中实现。 |
| 2024–2025<br>Crystal-LLM、TGDMat、Chemeleon | 文本 / 描述条件生成<br>描述输入，晶体输出 | 把化学及结构描述接入生成。条件中哪些关系得到落实成为新问题。 |
| 2025–2026<br>MatterGen、SCIGEN、PLaID++ | 性质或结构图案约束<br>生成并进行物理评价 | 获得条件候选及物理验证。多种要求的兼容与未见组合继续限制发现。 |

当前任务：同时检验条件命中与稳定新结构数量。主要导向A，并支持B。

任务演化为本综述综合，不把同一行方法视为直接继承。FTCP在具体性质目标中验证逆设计，CDVAE包括生成与性质优化。MatterGen将化学/性质条件接入联合扩散；SCIGEN将结构图案约束接入DiffCSP式生成。TGDMat与Chemeleon支持文本条件，PLaID++支持结构语言与偏好条件设计。MatterGen稳定阈值0.1与本项目严格阈值分别保留。

来源：[R06 Inverse Design of Solid-State Materials via a Continuous Representation](https://doi.org/10.1016/j.matt.2019.08.017)；[R07 An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties](https://arxiv.org/pdf/2005.07609v3)；[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R21 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://arxiv.org/abs/2402.04379)；[R37 Periodic Materials Generation using Text-Guided Joint Diffusion Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html)；[R39 Exploration of crystal chemical space using text-guided generative artificial intelligence](https://www.nature.com/articles/s41467-025-59636-y)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)

## 38. C2：耦合选择怎样形成和修订

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2022–2024<br>CDVAE、DiffCSP、FlowMM | 周期生成与组成CSP<br>联合生成晶胞和坐标 | 学习几何变量之间的依赖。进一步需要处理元素与几何的相互依赖。 |
| 2024–2025<br>FlowLLM、MatterGen、OMatG | DNG及分阶段生成<br>同时提出化学和结构 | 联合生成与组成先行都有效。问题转为两种组织何时各有优势。 |
| 2025–2026<br>CrysBFN、MCFlow、ANCHOR | 组成CSP、互条件完成<br>冻结CSP的组成探索 | 独立信息进度与组成策略均能改善任务。需要辨认哪类决定值得回改。 |

当前任务：在相同组成和数据条件下，判断几何信息是否改善化学选择。导向A。

FlowMM复用DiffCSP网络并改变生成过程。FlowLLM结合Crystal-LLM与FlowMM。MCFlow的独立模态时间处理多种条件推断；H.8匹配率45.58%与63.14%是CSP接口比较。ANCHOR冻结结构先验并改变组成分布，提供组成策略可能解释增益的强参照。概率分解本身可表示联合分布，当前问题在有限学习条件下的信息利用。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R33 A Periodic Bayesian Flow for Material Generation](https://arxiv.org/abs/2502.02016)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 39. C3：局部化学怎样组成周期整体

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2018–2023<br>CGCNN、M3GNet、CHGNet | 性质、能量、力的预测<br>完整结构输入 | 局部环境能支持物理预测。需要进一步研究如何用这些知识构造结构。 |
| 2023–2025<br>SLICES、SymmCD、Wyckoff | 周期图解码、对称DNG<br>关系或非等价位点输入 | 把周期连接和对称关系纳入生成。多个局部要求仍共享原子与晶胞。 |
| 2025–2026<br>SCIGEN、Composable、UFO-MGen | 图案约束、概念组合<br>给定配置的结构完成 | 已能组合概念并完成条件结构。下一步区分局部知识与模板信息，识别必要的全局条件。 |

当前任务：固定已学局部环境，改变化学或连接组合，检验整体稳定性。导向B。

CGCNN和MLIP是知识背景，不是组合生成结论。SymmCD和Wyckoff方法学习/构造对称配置。Composable Crystals的邻域concept含坐标及晶格信息，因此concept有效不能独自归因于纯局部化学。UFO-MGen的未见配置试验提供给定scaffold的条件完成证据。晶体局部环境共享原子、边和晶格，需要共同计量和几何实现。

来源：[R05 Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301)；[R10 A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[R16 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R36 WyckoffDiff – A Generative Diffusion Model for Crystal Symmetry](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html)；[R38 Wyckoff Transformer: Generation of Symmetric Crystals](https://arxiv.org/abs/2503.02407)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)；[R55 Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)

## 40. C4：物理反馈怎样改变有效的决定

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2006起<br>USPEX、AIRSS | 指定体系的结构搜索<br>提案后进行物理弛豫 | 能量评价帮助寻找低能结构。每个新体系仍需搜索，经验复用有限。 |
| 2023<br>RL-CSP | 组成条件的搜索决策<br>学习basin-hopping动作 | 根据结果改进动作分布。问题扩展到预训练生成器中的有效选择。 |
| 2025–2026<br>MatInvent、OMatG-IRL、GSS | 性质DNG、CSP后训练<br>生成先验结合物理力 | 奖励或力能改变生成过程。还需理解什么反馈在何种状态下改变终点。 |

当前任务：比较具体结构变化及其完整后果，建立反馈与终点增益的联系。导向C。

物理搜索、改变动作分布、后训练生成模型和推理时引导是不同反馈对象。MatInvent以MatterGen为默认基座，OMatG-IRL更新SI生成场，GSS将先验与物理力用于采样/搜索。当前研究从反馈存在推进到反馈何时能够支持有益的有限决定。项目PDE18零strict gain/loss为相关内部观察，不能外推为所有反馈无效。

来源：[R01 High-Pressure Phases of Silane](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504)；[R02 Crystal structure prediction using ab initio evolutionary techniques: Principles and applications](https://doi.org/10.1063/1.2210932)；[R14 Reinforcement learning in crystal structure prediction](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R50 Generative structure search for efficient and diverse discovery of molecular and crystal structures](https://arxiv.org/html/2604.27636v2)

## 41. C5：怎样发现并保留不同的合格结果

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2021–2023<br>GFlowNet Foundations | 通用多模态奖励采样<br>奖励定义的终态空间 | 学习按奖励比例采样多个结果。晶体中还需要定义物理资格和身份。 |
| 2024–2026<br>晶体QD、SHAFT | 固定组成的性质覆盖<br>层级对称材料生成 | 用档案或层级策略保留多解。开放化学空间的成功类别继续增加。 |
| 2025–2026<br>PLaID++、Chemeleon2、ANCHOR | 稳定 / 新颖后训练<br>依发现历史探索组成 | 开始联合改变资格与搜索分布。新增成功、重复及遗忘需要分别解释。 |

当前任务：按弛豫后的结构身份，统计首次发现、学会再生成和后续新发现。导向D。

GFlowNet Foundations首稿2021、JMLR2023。QD的性质档案针对选定组成；SHAFT以层级对称选择生成材料，其原文mode资格与严格SUN分开。PLaID++表征/后训练、Chemeleon2的latent RL与ANCHOR组成探索分别改变不同因素。稳定性、多样性和新颖性联合优化已有方法，研究需落在未知合格结果的持续获得与保持。

来源：[R09 GFlowNet Foundations](https://jmlr.org/papers/v24/22-0364.html)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[R30 Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 42. C6：物理计算怎样积累成生成能力

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |
| --- | --- | --- |
| 2013–2023<br>Materials Project、GNoME | 数据库积累、主动学习<br>新计算更新预测模型 | 计算结果跨材料复用。下一步是让信息直接帮助生成选择。 |
| 2025–2026<br>MatInvent、PLaID++、Chemeleon2 | 性质或物理资格后训练<br>终点评价更新生成器 | 计算开始进入模型权重。需要分辨端点记忆与可迁移的结构知识。 |
| 2026<br>OMatG-IRL、flash、ANCHOR | 条件训练后的DNG<br>少步生成、结构语料学习 | 能力可跨任务或采样阶段使用。仍需辨认哪些信息改善新的材料请求。 |

当前任务：控制终点数据与物理投入，检验额外关系信息的迁移价值。导向C和D。

GNoME是物理数据回流的先例，但不是扩散后训练。OMatG-IRL已有CSP式物理训练到DNG的证据。OMatG-flash直接采用RAM，关注少步生成映射。ANCHOR v2 F.6语料由访问组成重放形成，未按稳定/新颖阈值筛选。C关注学习的关系内容，D关注这些信息怎样扩大并保持成功分布。

来源：[R04 Commentary: The Materials Project: A materials genome approach to accelerating materials innovation](https://doi.org/10.1063/1.4812323)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R54 OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 43. 四条路线分别回答什么任务问题

| 路线与挑战 | 主要科学问题 | 直接研究任务 |
| --- | --- | --- |
| A 化学与几何<br>C1、C2 | 双向信息何时改善化学与结构的配对？ | 主任务：自主DNG<br>定位任务：CSP / 互条件完成 |
| B 局部知识组合<br>C3，联系C1 | 局部要求怎样在同一周期结构中成立？ | 主任务：自主DNG<br>定位任务：图案 / 新连接生成 |
| C 从物理反馈学习<br>C4、C6 | 哪些结构响应可以帮助新的材料？ | 物理数据学习后的独立生成<br>跨组成与条件迁移 |
| D 持续多解发现<br>C5、C6 | 新成功怎样学入模型并支持进一步发现？ | 多轮预算内DNG<br>新结果保持与继续发现 |

共同主目标是严格SUN。条件任务分别定位四条路线要学习的能力。

路线A侧重信息利用与联合推断；B侧重组合泛化；C侧重物理关系迁移；D侧重未知成功集合的获得与保持。任务输入输出不同，四方向各自可以构成独立论文。

## 44. A的演化：联合几何到化学与几何协作

| 时间与支持论文 | 原文任务 | 为路线A提供的能力 |
| --- | --- | --- |
| 2022–2024<br>CDVAE、DiffCSP、FlowMM | DNG、组成条件CSP | 联合建模晶胞与位置，支持周期连续生成。 |
| 2024<br>Crystal-LLM、GenMS | 晶体文本生成<br>语言条件的层级搜索 | 语言组织化学提案，连续模型实现几何。 |
| 2024–2025<br>FlowLLM、CrysLLMGen | LLM提案后的几何精修 | 连续模型改善语言提案。连续阶段固定元素，为双向修订提供明确参照。 |
| 2025–2026<br>MatterGen、OMatG、MCFlow | 联合DNG、互条件生成 | 建立化学与几何共同建模及多条件路径，支持比较不同信息组织。 |

演化留下的问题：何时只需更好提案，何时几何证据能帮助改变化学选择？

直接继承：FlowMM采用DiffCSP网络；FlowLLM结合Crystal-LLM式LLaMA先验与FlowMM；CrysLLMGen复用Crystal-LLM提示及DiffCSP式连续模型。GenMS将语言到公式和公式到结构分解。MatterGen、OMatG、MCFlow属于联合/多模态分支，不写成FlowLLM的单线后继。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R21 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://arxiv.org/abs/2402.04379)；[R28 Generative Hierarchical Materials Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)

## 45. A的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |
| --- | --- | --- |
| FlowLLM、CrysLLMGen<br>晶体混合模型 | 把语言提案接到连续几何生成 | LLM提出可修改的化学 / 占位选择，连续模型构造周期结构。 |
| OMatG、CrysBFN、MCFlow<br>混合变量生成 | 联合表示变量及其当前信息状态 | 让几何与元素更新读取共同状态，比较纯SI与LLM混合方案。 |
| NextStep-1 [T02]<br>文生图与编辑 | AR上下文预测连续token，flow输出细节 | 借鉴离散上下文与连续输出的分工，设计可交换的科学状态。 |
| SFD [T01]<br>ImageNet类别条件 | 分别推进语义与纹理的信息进度 | 借鉴相关变量的信息组织，研究化学和几何何时交换信息。 |

候选基座：LLM + Diffusion / SI。要新增的能力是内容相关的双向修订。

NextStep-1是连续token AR的图像方法，SFD主实验证据为ImageNet类别条件。迁移点是信息组织和方法接口。晶体需要保留元素、位置、晶胞及周期约束。双向信息的增量需与强分阶段和纯混合SI比较。

来源：[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R33 A Periodic Bayesian Flow for Material Generation](https://arxiv.org/abs/2502.02016)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[T02 NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale](https://arxiv.org/abs/2508.10711)；[T01 Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](https://arxiv.org/abs/2512.04926)

## 46. A的研究任务与可检验主张

中心问题：逐渐形成的几何，能否帮助模型选择更合适的化学？

**主任务DNG。** 模型自主提出组成与结构。用同一弛豫和新颖性规则比较不同生成组织的SUN。

**能力定位。** 给定部分组成或结构，补全另一部分。测试未见的化学与结构组合，观察修订是否改善配对。

**关键比较。** 强组成模型+CSP、纯联合Diffusion / SI、LLM与连续模型双向交互。保持数据与总费用可比。

**论文结果。** 建立信息交换何时有用的规律，并在独立新组合和DNG中保留收益。

研究主张待验证：几何内容应能解释有益修订，而非仅依赖更多采样。互条件完成源于MCFlow，混合模型参照源于FlowLLM/CrysLLMGen，组成搜索参照源于ANCHOR。最终主结果是全独立DNG严格SUN，条件任务用于解释能力。

来源：[R28 Generative Hierarchical Materials Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 47. B的演化：局部环境到新整体组合

| 时间与支持论文 | 原文任务 | 为路线B提供的能力 |
| --- | --- | --- |
| 2018–2023<br>CGCNN、M3GNet、CHGNet | 完整晶体的物理预测 | 说明局部环境包含可复用物理信息，提供知识来源与评价工具。 |
| 2022–2023<br>CDVAE、SLICES | 生成及可逆周期表示 | 支持整体结构生成和周期连接表达，使知识可以落实到结构。 |
| 2025<br>SymmCD、WyckoffDiff / Transformer | 对称配置生成与几何解码 | 用非等价位点组织共享约束，减少需要独立生成的自由度。 |
| 2025–2026<br>SCIGEN、Composable、UFO-MGen | 图案嵌入、概念组合<br>新配置条件完成 | 把指定关系嵌入晶体。进一步需要辨认组合成功所需的共同条件。 |

演化留下的问题：学到的局部规律，在改变连接、化学和晶胞后何时仍成立？

阶段表示问题推进，不声称所有工作直接继承。SLICES采用周期商图；Wyckoff Transformer的几何实现包括DiffCSP++解码；SCIGEN实际包装DiffCSP。Composable将邻域concept组合后交给条件DDPM。UFO-MGen采用离散配置与连续flow分工。预测知识的可生成性需要实验建立。

来源：[R05 Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301)；[R10 A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R16 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R36 WyckoffDiff – A Generative Diffusion Model for Crystal Symmetry](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html)；[R38 Wyckoff Transformer: Generation of Symmetric Crystals](https://arxiv.org/abs/2503.02407)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)；[R55 Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)

## 48. B的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |
| --- | --- | --- |
| SLICES、SymmCD<br>周期关系与对称表示 | 表示周期连接与非等价位点 | 让多个局部条件指向同一组原子和晶胞。 |
| SCIGEN、Composable Crystals<br>条件扩散生成 | 把图案或concept接入全结构生成 | 组成多个结构要求，并通过周期Diffusion实现。 |
| MCFlow、UFO-MGen<br>条件flow生成 | 互条件完成，或给定配置生成几何 | 提供flow替代基座与新配置完成的比较。 |
| DynFusion / Local Mechanisms<br>多条件融合 / 组合泛化 | 融合不同视觉条件，或干预局部条件依赖 | 按条件内容组织交互，在晶体中保留共享原子和晶格关系。 |

候选基座：显式周期关系的条件Diffusion。新增能力是跨连接方式的稳定组合。

DynFusion §3.2从当前噪声状态预测条件mask，§4.1比较多个空间、主体及混合视觉条件。Bradley的理论针对特定条件组合结构，原实验为CLEVR长度泛化及自然图像探索。晶体中邻域重叠、原子共享、周期晶格与相竞争需要新的条件。方法贡献需说明共享关系怎样改变组合泛化。

来源：[R16 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R55 Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)；[T03 Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)；[T07 DynFusion: Rethinking Condition Fusion for Adaptive Multi-Conditional Text-to-Image Generation](https://wrap.warwick.ac.uk/id/eprint/197869/8/WRAP-DynFusion-rethinking-condition-fusion-multi-conditional-text-to-image-generation-26.pdf)

## 49. B的研究任务与可检验主张

中心问题：熟悉的局部环境能否构成训练中未见的稳定整体？

**主任务DNG。** 模型自主提出组合方案并完成几何。评价严格稳定性和不同新结构数量。

**能力定位。** 给定多个配位或连接要求，生成同一周期结构。分别留出化学组合、连接方式或原胞复杂度。

**关键比较。** 离子替换 / 整结构检索、条件CSP、独立条件组合、共享周期关系建模。

**论文结果。** 说明共享条件怎样支持知识迁移，在未见组合与DNG中增加稳定新结构。

局部关系以统一邻接定义具体化。熟悉原型中的新稳定化学继续计入成功。复制超胞仅改变表示规模，不能当新整体结构。路线B主张待验证，不预设局部约束越多越好。各条件任务需在后处理后检查是否仍成立。

来源：[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R31 Establishing baselines for generative discovery of inorganic crystals](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)；[R51 Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)；[R52 Substitution-Based Analysis of Structural Novelty for Generative Models of Materials](https://arxiv.org/html/2606.23166v1)；[R55 Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)；[T03 Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)

## 50. C的演化：物理搜索到生成器学习

| 时间与支持论文 | 原文任务 | 物理反馈改变的对象 |
| --- | --- | --- |
| 2006–2023<br>AIRSS、USPEX、RL-CSP | 指定体系的低能结构搜索 | 先评价候选，再选择搜索动作。RL-CSP进一步学习动作分布。 |
| 2022–2025<br>CHGNet、GNoME、OpenCSP | 物理预测及压力CSP<br>新物理数据采集 | 计算扩展模型适用的结构和物理环境，主要改善预测与搜索基础。 |
| 2025–2026<br>MatInvent、PLaID++、Chemeleon2 | 性质DNG与物理资格优化 | 终点奖励或偏好开始更新生成器，而非仅筛选当前候选。 |
| 2026<br>OMatG-IRL、flash、GSS | CSP / DNG及少步生成<br>生成先验结合物理搜索 | IRL / flash更新生成场或映射，GSS在搜索中结合先验与物理力。 |

演化留下的问题：除了终点分数，哪些响应内容值得学入模型并迁移到新材料？

OpenCSP基于物理数据与并发学习研究压力CSP，截至原资料为2025预印本。MatInvent默认MatterGen，PLaID++是结构语言偏好训练，Chemeleon2是latent RL。OMatG-IRL基于SI，flash直接采用RAM。GSS主要是生成先验与物理势的混合搜索，不将其写作同一种生成器后训练。

来源：[R01 High-Pressure Phases of Silane](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504)；[R02 Crystal structure prediction using ab initio evolutionary techniques: Principles and applications](https://doi.org/10.1063/1.2210932)；[R14 Reinforcement learning in crystal structure prediction](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R11 CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R41 OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure](https://arxiv.org/html/2509.10293v1)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R54 OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)；[R50 Generative structure search for efficient and diverse discovery of molecular and crystal structures](https://arxiv.org/html/2604.27636v2)

## 51. C的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |
| --- | --- | --- |
| SI理论 [T08]、OMatG、FlowMM<br>连续分布与路径学习 | 学习连接分布的速度场，在周期空间生成结构 | 提供SI / flow基座，保留相同来源的多种可能终点。 |
| MatInvent、OMatG-IRL<br>晶体物理奖励后训练 | 用终点物理效用更新生成器 | 作为标量反馈的强参照，明确额外响应信息增加了什么。 |
| Flow-GRPO / RAM [T04–05]<br>图像生成后训练 | 用终点奖励训练flow / diffusion | 提供可实施的后训练目标。RAM已由OMatG-flash采用。 |
| GSS、CrystAF<br>物理引导 / 分子晶体packing | 比较生成先验、物理介入与修复 | 帮助区分当前样本修复与模型长期学习的作用。 |

候选基座：SI / flow。新增学习对象是结构变化、响应和终点之间的关系。

响应关系学习是当前路线的研究命题，而不是这些原工作已得出的共同结论。Flow-GRPO用在线策略梯度，RAM保持解析加噪回归形式并由终点奖励修正。CrystAF原对象是分子晶体，不用其packing结果充当无机SUN。

来源：[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[T08 Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](https://jmlr.org/papers/v26/23-1605.html)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[T04 Flow-GRPO: Training Flow Matching Models via Online RL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html)；[T05 Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2605.10759)；[R54 OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)；[R50 Generative structure search for efficient and diverse discovery of molecular and crystal structures](https://arxiv.org/html/2604.27636v2)；[R57 Where Should Physics Enter a Molecular Crystal Generator?](https://arxiv.org/html/2609.36398v1)

## 52. C的研究任务与可检验主张

中心问题：同样的物理投入，怎样帮助更多后续材料请求？

**主任务DNG。** 用物理数据训练后独立生成，检验新的材料请求能否受益。数据采集和训练成本同时计入。

**关系与迁移。** 学习同源结构改变的响应与后果，并在未见组成或条件上检验。

**关键比较。** 在线物理引导、成功端点训练、标量奖励后训练、保留变化与响应关系的训练。

**论文结果。** 辨认哪些物理信息可以迁移，并在计入数据采集和训练费用后提高SUN发现量。

对比保持终点池与物理投入可比，关系学习额外使用来源与实际变化的对应。模型需在新的请求中获益，不能仅重现训练终点。数值弛豫路径保留求解器依赖，生成模型可学习更一般的分布关系。

来源：[R14 Reinforcement learning in crystal structure prediction](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R18 Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)；[R41 OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure](https://arxiv.org/html/2509.10293v1)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R54 OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 53. D的演化：多解优化到持续发现

| 时间与支持论文 | 原文任务 | 为路线D提供的能力 |
| --- | --- | --- |
| 2021–2023<br>GFlowNet Foundations | 通用奖励比例采样 | 用生成分布表达多个高质量结果，提供多路径采样基础。 |
| 2024–2026<br>晶体QD、SHAFT | 固定组成的性质档案<br>层级对称材料生成 | 在不同性质或对称选择中探索多解，说明可以显式组织成功集合。 |
| 2025–2026<br>PLaID++、Chemeleon2、MatInvent | 物理或性质目标后训练 | 奖励与表示共同改变稳定性、新颖性和概率集中。 |
| 2025–2026<br>强基线研究、ANCHOR | 替换候选发现<br>冻结CSP下的组成探索 | 强替换和化学访问已能贡献发现，需要分开分配变化与新结构能力。 |

演化留下的问题：搜索遇到的新成功，怎样变成持续可用且能继续扩展的生成能力？

GFlowNet为通用基础，QD与SHAFT任务不同。强基线研究在分别选出的500个MP新颖候选上作DFT，上游提出成本不同。ANCHOR在冻结CSP条件下调节组成策略。其语料重放不必是成功结构，保持原数据定义。

来源：[R09 GFlowNet Foundations](https://jmlr.org/papers/v24/22-0364.html)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[R30 Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R44 Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)；[R31 Establishing baselines for generative discovery of inorganic crystals](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

## 54. D的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |
| --- | --- | --- |
| GFlowNet、SHAFT<br>层级多解生成 | 按奖励保留多个结果和科学选择 | AR / GFlowNet选择组成或对称配置，条件生成器给出多种几何实现。 |
| 晶体QD、ANCHOR<br>档案与历史相关探索 | 保存不同结果，改变下一轮探索分配 | 根据已发现结构选择新区域，并研究固定或更新低层生成器。 |
| Max@K [T06]<br>文生图的预定义模式覆盖 | 按样本对集合覆盖的贡献分配奖励 | 借鉴集合层面学习，晶体类别和资格由物理评价逐步确认。 |
| Structure Matches、LeMat<br>多晶型与生成评价 | 统一结果身份和资格的观察 | 在弛豫后统计不同合格结果，区分首次发现、再生成和进一步发现。 |

候选基座：层级LLM / AR + 条件Diffusion。新增能力是学会新成功并继续发现。

Max@K原任务的目标模式预定义，当前arXiv v2注记WACV2027接收。这里仅用其集合贡献分配机制作迁移参照。Structure Matches的多晶型目标与LeMat的统一框架帮助定义能力，但不替代生成方法。D可以固定低层先研究上层探索，也可研究联合更新。

来源：[R09 GFlowNet Foundations](https://jmlr.org/papers/v24/22-0364.html)；[R30 Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks](https://arxiv.org/html/2411.04323v1)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)；[T06 Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/abs/2607.14962)；[R42 All that structure matches does not glitter](https://arxiv.org/html/2509.12178v2)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)

## 55. D的研究任务与可检验主张

中心问题：多轮发现能否让模型持续获得不同的稳定新结构？

**多轮DNG。** 在开放化学空间连续生成、弛豫和更新模型。每轮保留完整费用与不同合格结构集合。

**保持与迁移。** 分别测量新成功的再生成、旧成功的保留，以及未用于更新的新发现。

**关键比较。** 固定采样、组成重分配、QD / GFlowNet探索、加入生成器持续学习。

**论文结果。** 解释何时只需改变探索分配，何时必须学习新结构关系，并改善同预算下累计SUN数量。

首次发现、新颖于固定参考库、新颖于本项目更新集分别记录。已经学入训练的自发现材料，在下一轮生成时可计入参考库外SUN与保持能力，但不能再次计为研究过程中的首次发现。熟悉框架的新稳定化学仍计有效结果。

来源：[R09 GFlowNet Foundations](https://jmlr.org/papers/v24/22-0364.html)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[R30 Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)；[R42 All that structure matches does not glitter](https://arxiv.org/html/2509.12178v2)；[R46 LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)

## 56. 项目历史现象怎样进入四条路线

| 历史观察 | 已完成结果 | 对应的研究问题 |
| --- | --- | --- |
| 几何反馈增加稳定终点 | 同512来源已知稳定数<br>plain / restored / detached为76 / 85 / 86 | A / C：什么信息和变化使化学与结构配对更有效？ |
| 指定动作缺少终点事件 | PDE18：128个DEV父来源<br>512配对严格稳定 gain / loss = 0 / 0 | C：反馈必须支持能够改变完整后果的决定。 |
| 稳定性到SUN仍有损失 | PDE22：86个稳定尝试<br>58个稳定新颖，53个独特SUN | D：资格、新颖性与重复分别影响最终发现集合。 |

B的依据主要来自局部环境与组合生成文献，其稳定组合能力需要新的直接证据。

证据来源：https://github.com/YWDDLiang/Research/blob/main/crystal/evidence/historical-evidence.md 。第一行每臂24个能量未知，组成固定，晶胞和位置仍演化。第二行是每个DEV父来源四个未来形成的512配对。第三行为同一项目队列的分解，不能当作通用领域损失比例。

## 57. 参考文献：任务与表示

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R21 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://arxiv.org/abs/2402.04379)；[R28 Generative Hierarchical Materials Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)；[R29 FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R34 Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)；[R49 Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)

## 58. 参考文献：条件与组合

来源：[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[R27 Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y)；[R35 SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)；[R38 Wyckoff Transformer: Generation of Symmetric Crystals](https://arxiv.org/abs/2503.02407)；[R16 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)；[R51 Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)；[R55 Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)；[T01 Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](https://arxiv.org/abs/2512.04926)；[T03 Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)

## 59. 参考文献：反馈与持续发现

来源：[R40 PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)；[R45 Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4)；[R48 Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)；[R54 OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)；[R56 Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)；[R23 Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1)；[T04 Flow-GRPO: Training Flow Matching Models via Online RL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html)；[T05 Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2605.10759)；[T06 Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/abs/2607.14962)

## 60. 阅读与复现的关键来源

**任务与基准。** CDVAE、DiffCSP、FlowMM的原文与官方数据配置。

**数据与相稳定。** Materials Project方法文档、Alexandria发布页、pymatgen相图与结构匹配。

**物理计算。** CHGNet / MACE / MatterSim模型资料；ASE与Phonopy方法说明。

**MatterGen。** Nature正式论文、补充材料与官方代码。五页所引数据和原图各有来源位置。

本页备注附完整引用。教学图和算例为人为构造，其他数值均来自指定原始文献或官方方法资料。没有运行新生成、DFT或材料实验。

来源：[R08 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)；[R13 Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)；[R26 FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)；[R19 A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REPO Microsoft MatterGen official README and data-release descriptions](https://github.com/microsoft/mattergen)；[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)；[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)；[PHONOPY Phonopy: Formulations](https://phonopy.github.io/phonopy/formulation.html)

## 完整来源

- [R01] [High-Pressure Phases of Silane](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504) DOI: 10.1103/PhysRevLett.97.045504

- [R02] [Crystal structure prediction using ab initio evolutionary techniques: Principles and applications](https://doi.org/10.1063/1.2210932) DOI: 10.1063/1.2210932

- [R03] [Ab initio Random Structure Searching](https://arxiv.org/abs/1101.3987) DOI: 10.1088/0953-8984/23/5/053201

- [R04] [Commentary: The Materials Project: A materials genome approach to accelerating materials innovation](https://doi.org/10.1063/1.4812323) DOI: 10.1063/1.4812323

- [R05] [Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301) DOI: 10.1103/PhysRevLett.120.145301

- [R06] [Inverse Design of Solid-State Materials via a Continuous Representation](https://doi.org/10.1016/j.matt.2019.08.017) DOI: 10.1016/j.matt.2019.08.017

- [R07] [An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties](https://arxiv.org/pdf/2005.07609v3) DOI: 10.1016/j.matt.2021.11.032

- [R08] [Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)

- [R09] [GFlowNet Foundations](https://jmlr.org/papers/v24/22-0364.html)

- [R10] [A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3) DOI: 10.1038/s43588-022-00349-3

- [R11] [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://www.nature.com/articles/s42256-023-00716-3) DOI: 10.1038/s42256-023-00716-3

- [R12] [Crystal structure generation with autoregressive large language modeling](https://www.nature.com/articles/s41467-024-54639-7) DOI: 10.1038/s41467-024-54639-7

- [R13] [Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)

- [R14] [Reinforcement learning in crystal structure prediction](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j) DOI: 10.1039/D3DD00063J

- [R15] [Scalable Diffusion for Materials Generation](https://arxiv.org/abs/2311.09235)

- [R16] [An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7) DOI: 10.1038/s41467-023-42870-7

- [R17] [Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials](https://www.nature.com/articles/s41586-025-09992-y) DOI: 10.1038/s41586-025-09992-y

- [R18] [Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9) DOI: 10.1038/s41586-023-06735-9

- [R19] [A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5) DOI: 10.1038/s41586-025-08628-5

- [R20] [Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html)

- [R21] [Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](https://arxiv.org/abs/2402.04379)

- [R22] [Space Group Constrained Crystal Generation](https://arxiv.org/abs/2402.03992)

- [R23] [Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms](https://arxiv.org/html/2403.03511v1) DOI: 10.1039/D4DD00054D

- [R24] [Con-CDVAE: A method for the conditional generation of crystal structures](https://arxiv.org/html/2403.12478v1) DOI: 10.1016/j.commt.2024.100003

- [R25] [Space group informed transformer for crystalline materials generation](https://arxiv.org/abs/2403.15734) DOI: 10.1016/j.scib.2025.09.035

- [R26] [FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)

- [R27] [Structural constraint integration in a generative model for the discovery of quantum materials](https://www.nature.com/articles/s41563-025-02355-y) DOI: 10.1038/s41563-025-02355-y

- [R28] [Generative Hierarchical Materials Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)

- [R29] [FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html) DOI: 10.52202/079017-1464

- [R30] [Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks](https://arxiv.org/html/2411.04323v1) DOI: 10.1039/D4DD00392F

- [R31] [Establishing baselines for generative discovery of inorganic crystals](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f) DOI: 10.1039/D5MH00010F

- [R32] [A generative material transformer using Wyckoff representation](https://www.nature.com/articles/s41524-025-01940-8) DOI: 10.1038/s41524-025-01940-8

- [R33] [A Periodic Bayesian Flow for Material Generation](https://arxiv.org/abs/2502.02016)

- [R34] [Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)

- [R35] [SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)

- [R36] [WyckoffDiff – A Generative Diffusion Model for Crystal Symmetry](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html)

- [R37] [Periodic Materials Generation using Text-Guided Joint Diffusion Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html)

- [R38] [Wyckoff Transformer: Generation of Symmetric Crystals](https://arxiv.org/abs/2503.02407)

- [R39] [Exploration of crystal chemical space using text-guided generative artificial intelligence](https://www.nature.com/articles/s41467-025-59636-y) DOI: 10.1038/s41467-025-59636-y

- [R40] [PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design](https://arxiv.org/html/2509.07150v4)

- [R41] [OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure](https://arxiv.org/html/2509.10293v1)

- [R42] [All that structure matches does not glitter](https://arxiv.org/html/2509.12178v2)

- [R43] [LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html) DOI: 10.52202/085713-5635

- [R44] [Accelerating inverse materials design using generative diffusion models with reinforcement learning](https://arxiv.org/html/2511.03112v1)

- [R45] [Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning](https://www.nature.com/articles/s42256-026-01262-4) DOI: 10.1038/s42256-026-01262-4

- [R46] [LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models](https://arxiv.org/html/2512.04562v2)

- [R47] [Periodic Bayesian Flow Networks with Additive Accuracy](https://proceedings.mlr.press/v306/lin26ar.html)

- [R48] [Open Materials Generation with Inference-Time Reinforcement Learning](https://arxiv.org/html/2602.00424v2)

- [R49] [Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling](https://proceedings.mlr.press/v306/seong26a.html)

- [R50] [Generative structure search for efficient and diverse discovery of molecular and crystal structures](https://arxiv.org/html/2604.27636v2)

- [R51] [Composable Crystals: Controllable Materials Discovery via Concept Learning](https://arxiv.org/html/2605.14769v2)

- [R52] [Substitution-Based Analysis of Structural Novelty for Generative Models of Materials](https://arxiv.org/html/2606.23166v1)

- [R53] [Text-guided flow matching enables sample-efficient crystal structure generation](https://arxiv.org/html/2609.01076v2)

- [R54] [OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery](https://arxiv.org/html/2609.26402v1)

- [R55] [Topology-Stratified Materials Discovery with A Flow-Based Generative Model](https://arxiv.org/html/2609.26547v1)

- [R56] [Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors](https://arxiv.org/html/2609.33407v2)

- [R57] [Where Should Physics Enter a Molecular Crystal Generator?](https://arxiv.org/html/2609.36398v1)

- [T01] [Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](https://arxiv.org/abs/2512.04926)

- [T02] [NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale](https://arxiv.org/abs/2508.10711)

- [T03] [Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)

- [T04] [Flow-GRPO: Training Flow Matching Models via Online RL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html)

- [T05] [Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2605.10759)

- [T06] [Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/abs/2607.14962)

- [T07] [DynFusion: Rethinking Condition Fusion for Adaptive Multi-Conditional Text-to-Image Generation](https://wrap.warwick.ac.uk/id/eprint/197869/8/WRAP-DynFusion-rethinking-condition-fusion-multi-conditional-text-to-image-generation-26.pdf)

- [T08] [Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](https://jmlr.org/papers/v26/23-1605.html)

- [IUCR] [How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists](https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html)

- [ALEX] [Alexandria official dataset releases](https://alexandria.icams.rub.de/datasets.html)

- [OQMD] [OQMD official structure sources and API documentation](https://oqmd.org/documentation/structures)

- [ICSD] [ICSD official data curation and theoretical data categories](https://icsd.products.fiz-karlsruhe.de/en/about/data-curation)

- [COD] [Crystallography Open Database (COD): an open-access collection of crystal structures and platform for world-wide collaboration](https://academic.oup.com/nar/article/40/D1/D420/2903497)

- [CDVAE_CFG] [CDVAE official MP-20 configuration and build_crystal preprocessing](https://github.com/txie-93/cdvae/blob/main/conf/data/mp_20.yaml)

- [MACE] [A foundation model for atomistic materials chemistry](https://arxiv.org/html/2401.00096v3)

- [MATTERSIM] [MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures](https://arxiv.org/html/2405.04967v2)

- [MATTERSIM_CARD] [MatterSim official model card: v1.0.0-1M and v1.0.0-5M](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md)

- [SMACT] [SMACT screening module](https://smact.readthedocs.io/en/latest/smact.screening.html)

- [SCIPY_JS] [scipy.spatial.distance.jensenshannon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html)

- [SCIPY_W] [scipy.stats.wasserstein_distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)

- [PYM_HULL] [pymatgen.analysis.phase_diagram.PhaseDiagram](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.phase_diagram.PhaseDiagram.get_decomp_and_e_above_hull)

- [MP_COMPAT] [Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)

- [ASE_OPT] [ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)

- [ASE_FILTER] [ASE: Filters](https://docs.ase-lib.org/ase/filters.html)

- [ASE_MD] [ASE: Molecular dynamics](https://docs.ase-lib.org/ase/md.html)

- [ASE_NEB] [ASE: Nudged elastic band](https://docs.ase-lib.org/ase/neb.html)

- [PHONOPY] [Phonopy: Formulations](https://phonopy.github.io/phonopy/formulation.html)

- [MP_DFT] [Materials Project: Parameters and Convergence](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details/gga+u-calculations/parameters-and-convergence)

- [MP_ELECTRONIC] [Materials Project: Electronic Structure](https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure)

- [MP_ELASTIC] [Materials Project: Elastic Constants](https://docs.materialsproject.org/methodology/materials-methodology/elasticity)

- [CHGNET_DOC] [CHGNet official project documentation](https://chgnet.lbl.gov/)

- [MG_REPO] [Microsoft MatterGen official README and data-release descriptions](https://github.com/microsoft/mattergen)

- [MG_SI] [MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)

- [MG_DATA] [MatterGen official Alex-MP data release](https://github.com/microsoft/mattergen/blob/main/data-release/alex-mp/README.md)

- [PHASE] [Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)

- [MATCHER] [pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)

- [MG_REANALYSIS] [Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)
