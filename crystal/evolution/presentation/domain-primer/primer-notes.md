# 晶体生成：数据、模型与验证

2026年10月13日。面向AI研究者的30页补充汇报。第23–27页为MatterGen五页详解。

本文按原文区分训练数据、竞争相参考、新颖性参照、评价器与实际实验。教学图和算例为人为构造，原文结果保留其版本与口径。

## 1. 晶体生成：数据、模型与验证

本补充篇承接2026年10月12日的30页晶体研究演化PPT，面向熟悉AI而不熟悉材料科学的听众。主线为生成对象、训练数据、评价定义和实际物理验证，不重复六挑战与四路线。所有标为教学示例的数据均为人为构造。MatterGen在第23–27页单独展开五页。

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

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[IUCR How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists](https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html)。

## 3. 同一个晶体可以有多种编码

**周期边界。** f与f+m对应周期等价位置。0.99与0.01在胞边界两侧可以很近。

**几何等价。** 原子顺序、整体平移、旋转和晶胞选择都能改写输入。

**对称表示。** 空间群操作展开非等价原子。Wyckoff位置记录对称位点的重复数与自由坐标。

图中A、B仅为虚构原子类别，四个方格重复相同的两个分数位置，不代表真实材料。坐标逐项MSE或CIF字符串相等通常不足以判断晶体身份。NaCl原胞2原子而常规立方胞8原子，说明胞选择会影响原子数限制。

文献：[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R16 slices](https://www.nature.com/articles/s41467-023-42870-7)；[R35 symmcd](https://arxiv.org/abs/2502.03638)；[IUCR How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists](https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html)。

## 4. 先区分CSP、自主生成与条件设计

| 任务 | 给模型什么 | 模型需要输出 | 通常怎样评测 |
| --- | --- | --- | --- |
| 结构预测 CSP | 组成或化学式 | 晶胞与原子位置 | 参考命中、RMSD、多晶型 |
| 自主生成 DNG | 随机种子或噪声 | 组成与完整结构 | 有效率、S/U/N、SUN |
| 条件生成 | 性质、元素范围、空间群或图案 | 满足要求的完整结构 | 条件命中与物理资格交集 |
| 物理预测 | 完整原子构型 | 能量、力、应力或性质 | 误差、动力学与应用表现 |

化学系统条件如“Li–O”允许选择计量；给定“Li₂O”则固定了更具体的组成。

重构任务还可能编码整个输入晶体，不能自动视为仅给组成的CSP。MCFlow的互条件主要是元素A与几何(F,L)，不指所有自然语言、光谱和实验模态。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)。

## 5. 数据库、训练集与参考库各有用途

| 资源 | 主要内容 | 在生成研究中的作用 |
| --- | --- | --- |
| Materials Project | DFT结构、能量及性质 | 衍生训练集、竞争相和评价参考 |
| Alexandria / OQMD | 高通量DFT及假想结构 | 扩大化学覆盖，提供相能量 |
| ICSD | 整理后的无机结构，主要来自实验 | 已知材料与新颖性参考，含无序占位 |
| COD | 开放CIF，覆盖多类晶体 | 结构与文献来源，能量标签需另配 |

数据库会更新；模型实际使用的是某次下载、过滤和划分后的固定快照。

ICSD也收录部分理论结构，因此不能写成全部实验材料。COD涵盖有机、无机、金属有机和矿物，不自动带统一DFT能量或力。不同库的泛函、磁性、修正和结构标准化需要对齐。

文献：[R04 MaterialsProject2013](https://doi.org/10.1063/1.4812323)；[ALEX Alexandria official dataset releases](https://alexandria.icams.rub.de/datasets.html)；[OQMD OQMD official structure sources and API documentation](https://oqmd.org/documentation/structures)；[ICSD ICSD official data curation and theoretical data categories](https://icsd.products.fiz-karlsruhe.de/en/about/data-curation)；[COD Crystallography Open Database (COD): an open-access collection of crystal structures and platform for world-wide collaboration](https://academic.oup.com/nar/article/40/D1/D420/2903497)。

## 6. 常用生成基准各自检验什么

| 基准 | 固定规模 | 结构范围 | 用途与划分 |
| --- | --- | --- | --- |
| Perov-5 | 18,928 | ABX₃型，每胞5原子 | 组成变化为主；60/20/20 |
| Carbon-24 | 10,153 | 仅C，6–24原子，10 GPa | 结构与多晶型；60/20/20 |
| MP-20 | 45,231 | 89种元素，输入胞≤20原子 | 组成与结构；60/20/20 |
| MPTS-52 | 40,476 | 输入胞≤52原子 | 按时间划分<br>27,380 / 5,000 / 8,096 |

MP-20是特定基准文件和预处理流程，不等于现在查询所有“≤20原子”的MP结构。

前三个数据集为CDVAE固定快照，原随机划分60/20/20。Carbon-24来自10 GPa AIRSS候选低能10%及DFT弛豫，不能直接用来声称常压稳定发现。MP-20原过滤包括ICSD来源、Ehull<0.08eV/atom与formation energy<2eV/atom。MPTS-52按最早文献年份划分，缺失年份者排除。原胞/常规胞/超胞改变原子数，公开配置primitive=False，页面采用基准输入胞表述。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[CDVAE_CFG CDVAE official MP-20 configuration and build_crystal preprocessing](https://github.com/txie-93/cdvae/blob/main/conf/data/mp_20.yaml)。

## 7. 生成终态数据与势能轨迹数据不同

生成器学习哪些结构会出现，MLIP还要学习离开终态后能量怎样变化。

**生成训练集。** 一条记录通常是一种结构及可选性质。Alex-MP-20将生成训练扩展到数十万结构。

**MLIP轨迹集。** 同一材料的弛豫过程包含多帧，每帧带能量、力和应力。MPtrj约158万构型来自约14.6万材料。

**划分单位。** CHGNet按材料划分80/10/10，避免同一材料的相邻帧跨训练和测试。

**复现信息。** 记录数据版本、计算口径、过滤和划分。构型数、材料数、模型参数量分别报告。

CHGNet MPtrj含89种元素，原模型能量标签已做MP2020兼容性修正。MatterSim模型名1M/5M接近参数规模，当前模型卡的训练样本数是3M/6M，不能混为一项。不同模型/快照的标签和覆盖范围需分别描述。

文献：[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MATTERSIM_CARD MatterSim official model card: v1.0.0-1M and v1.0.0-5M](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md)。

## 8. 常见生成模型的技术分工

| 模型家族 | 代表工作 | 直接生成什么 |
| --- | --- | --- |
| 潜变量与周期去噪 | CDVAE | 先组织全局结构属性，再生成元素与坐标 |
| Diffusion | DiffCSP、MatterGen | 对晶格、周期坐标及可选元素联合去噪 |
| Flow / SI | FlowMM、OMatG | 学习连接初始分布与晶体分布的连续过程 |
| 语言与混合生成 | Crystal-LLM、FlowLLM<br>CrysLLMGen | 序列化结构；或用LLM提案接连续精修 |
| 对称与多模态 | SymmCD、MCFlow | 生成非等价位点，或完成元素与几何的互条件任务 |

DiffCSP主任务为固定组成的CSP，另有DNG扩展。FlowLLM针对LLM起始分布训练flow；CrysLLMGen加噪后用扩散精修，二者连续阶段固定元素。空间群和Wyckoff压缩几何自由度，但相稳定性仍需能量评价。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R21 crystal_llm](https://arxiv.org/abs/2402.04379)；[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 crysllmgen](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R35 symmcd](https://arxiv.org/abs/2502.03638)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)。

## 9. 代表论文怎样连接数据、模型和评测

| 工作 | 数据与任务 | 主要评测对象 |
| --- | --- | --- |
| CDVAE | Perov-5 / Carbon-24 / MP-20<br>重构与DNG | 有效率、指纹覆盖、性质分布 |
| DiffCSP / FlowMM | MP-20等，组成CSP与DNG | CSP匹配/RMSD；DNG另做物理评价 |
| FlowLLM / CrysLLMGen | MP-20为主，混合DNG | 前者报告DFT-SUN，后者主要CHGNet评测 |
| MatterGen | Alex-MP-20，DNG与条件设计 | 统一DFT弛豫、SUN、性质及实验案例 |
| Chemeleon2 | MP-20 / Alex-MP-20<br>DNG与性质后训练 | 代理势评价与选定DFT，含性质交集指标 |

CDVAE原文主要生成指标不是大规模DFT发现率。FlowLLM所引4.92%为DFT，CrysLLMGen所引9.21%为CHGNet。MatterGen正文对生成器与基线使用DFT，公开repo默认MatterSim评测另列。Chemeleon2细节在第28页及来源笔记。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 crysllmgen](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)。

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

文献：[R10 M3GNet2022](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[MACE A foundation model for atomistic materials chemistry](https://arxiv.org/html/2401.00096v3)；[MATTERSIM MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures](https://arxiv.org/html/2405.04967v2)；[MATTERSIM_CARD MatterSim official model card: v1.0.0-1M and v1.0.0-5M](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md)。

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

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R46 lemat](https://arxiv.org/html/2512.04562v2)；[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)。

## 12. Validity先判断候选能否继续计算

| 检查 | 具体对象 | 结果含义 |
| --- | --- | --- |
| 可读取与晶胞合法 | CIF、元素、占位、晶格体积 | 得到完整且可解析的结构 |
| 几何有效性 | 周期最小距离、密度、异常晶格 | 排除严重碰撞或畸形结构 |
| 组成有效性 | 允许氧化态与电荷平衡等规则 | 符合所采用的化学启发式 |
| 规则示例 | SMACT可寻找 Σₑ nₑqₑ = 0 的赋值 | NaCl可用Na⁺和Cl⁻解释电荷平衡 |

通过有效性检查后，再评价相稳定性和目标性质。

距离必须考虑周期镜像。SMACT可单独处理单质和金属合金，离子氧化态规则有适用范围。几何有效、组成有效及其交集分开报告。原论文公式和实际代码中的检查项应共同核对。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R46 lemat](https://arxiv.org/html/2512.04562v2)；[SMACT SMACT screening module](https://smact.readthedocs.io/en/latest/smact.screening.html)。

## 13. CSP评测：参考命中率与几何误差

MR@k = 命中至少一个参考结构的测试请求数 / 全部测试请求数

**匹配。** 处理原子重排、平移和晶胞等价后，按晶格、角度及位置容差比较。

**RMSD。** 匹配原子的位移均方根。文献可能报Å，也可能除以 (V/n)¹ᐟ³ 归一化。

**采样预算。** MR@20通常允许每个组成20个候选。best-of-k评测可用参考答案选最好者。

**多晶型。** 同一组成可能有多个低能结构，单个数据库参考不代表全部可行答案。

DiffCSP使用stol=0.5、ltol=0.3、angle_tol=10°；stol按自由长度归一化，不能解释为0.5Å。需要区分到参考结构的误差与生成结构到弛豫终态的位移。能量排序后的top-k还需计入排序成本。

文献：[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R42 glitter](https://arxiv.org/html/2509.12178v2)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)。

## 14. 分布指标衡量覆盖与偏移

| 指标 | 如何计算或理解 | 它描述什么 |
| --- | --- | --- |
| COV-Recall | 参考集合中被生成指纹邻域覆盖的比例 | 生成集合覆盖了多少参考变化 |
| COV-Precision | 生成集合中靠近参考指纹分布的比例 | 有多少输出处于参考邻域 |
| JSD | 两个类别分布的对称差异 | 元素、空间群等分布偏移 |
| Wasserstein-1 | 将一份标量分布搬成另一份的平均距离 | 密度、能量等性质分布差异 |

这些指标描述统计分布；稳定新材料还需要结构匹配及物理资格。

CDVAE使用CrystalNN结构指纹和归一化Magpie组成指纹。其Appendix G同一对同时近的公式，与公开源码分别取两类最近邻再AND存在差别，复现需声明版本。教学例：密度{3,3}与{4,4}g/cm³的W1=1g/cm³。空间群编号是类别，编号间数值距离不具有一般物理含义。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[SCIPY_JS scipy.spatial.distance.jensenshannon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html)；[SCIPY_W scipy.stats.wasserstein_distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)。

## 15. 形成能和凸包能比较不同的竞争对象

E_form = (E_cell − Σₑ nₑ μₑ) / n

**形成能。** 比较化合物与对应元素参考相。单位通常为eV/atom。

**相分解。** 即使形成能为负，也可能更愿意分解成若干更低能化合物。

**凸包。** 在组成守恒下，求参考相混合所能达到的最低能量。

**物理条件。** 常见电子能凸包近似0 K条件；压力下比较焓，有限温度平衡需要自由能。

教学算例：AB总能−10.6eV，A与B参考每原子能−4.0和−5.6eV，Eform=(−10.6+4.0+5.6)/2=−0.5eV/atom。凸包h_R(x)=min Σλ_r E_r，约束λ≥0、Σλ=1、Σλx_r=x。

文献：[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)。

## 16. 凸包能量差的两种口径

**固定参考包。** ΔE_ref = 候选形成能 − 参考包能量。它可为负，表示降低旧参考包。

**高于凸包的能量。** 把候选也加入相集合后，E_above hull ≥ 0；位于凸包上的结构为0。

**教学算例。** A₂B能量−0.450，旧包为−0.3667 eV/atom，ΔE_ref = −0.0833。

参考点A(0,0)、A3B(.25,−.30)、AB(.5,−.50)、AB3(.75,−.30)、B(1,0)。候选A2B=(1/3,−.45)位于参考线下方；另一A2B=(1/3,−.20)形成能虽负仍在参考包上方。多个新候选也会互相竞争。某些生成论文把带符号参考距离记为Ehull，读文献时需核准定义。

文献：[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[PYM_HULL pymatgen.analysis.phase_diagram.PhaseDiagram](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.phase_diagram.PhaseDiagram.get_decomp_and_e_above_hull)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)。

## 17. S、U、N与SUN分别回答什么

| 指标 | 计算对象 | 需要声明的条件 |
| --- | --- | --- |
| Stable，S | 达到稳定或近凸包阈值的结构 | 阈值、评价器、能量参考、弛豫阶段 |
| Unique，U | 一批结果中去重后的不同结构 | 匹配容差、聚类顺序、代表选择 |
| Novel，N | 与固定参考库不匹配的结构 | 参考库版本、化学和结构匹配规则 |
| SUN | 稳定且新颖的结果去重后的数量或比例 | 完整交集和分母，不假定各项独立 |

新化学可以沿用熟悉结构原型。参考库外、训练集外和项目首次发现是不同概念。

S/U/N应在同一物理终态重算。先筛稳定与新颖再去重，是一个可清楚解释的操作口径；其他论文顺序及分母可不同。引用其结果时保持原定义。标准hull=0与固定参考距离≤0按上页定义分别标明。

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R46 lemat](https://arxiv.org/html/2512.04562v2)；[R52 novelty](https://arxiv.org/html/2606.23166v1)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)。

## 18. SUN的分母与去重：一个算例

**全部请求。** 100个提案，90个通过有效性检查。

**稳定与去重。** 40个确认稳定，去重剩30个不同稳定结构。

**新颖交集。** 其中12个不在参考库，SUN = 12/100 = 12%。

条件比例相乘可还原漏斗；全体S、U、N的边缘比例不能直接相乘。

90/100 × 40/90 × 30/40 × 12/30 =12/100为条件计数恒等式。相同数据若全体U=60%、全体N=45%，乘.4×.6×.45=10.8%不等于SUN12%。如果只有80个完成评测，40/80是已评测比例，40/100是确认产出，剩余状态保留未知。

文献：[R46 lemat](https://arxiv.org/html/2512.04562v2)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)。

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

文献：[MP_DFT Materials Project: Parameters and Convergence](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details/gga+u-calculations/parameters-and-convergence)；[MP_ELECTRONIC Materials Project: Electronic Structure](https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)。

## 20. 弛豫是在寻找局部低能结构

| 方式或工具 | 优化什么 | 应报告什么 |
| --- | --- | --- |
| 固定晶胞 | 原子位置 | 原子最大力、步数、是否收敛 |
| 变胞弛豫 | 原子位置与晶胞形状/体积 | 力、应力、外压和约束 |
| FIRE / L-BFGS | 使用能量及梯度作局部优化 | 优化器、阈值、最大步数 |
| MD / AIMD | 按运动方程推进时间 | 温度、系综、步长与物理时长 |

FIRE的200步是优化工作量；MD的10,000步×1 fs才对应10 ps模拟时间。

小残余力说明接近驻点，曲率/声子提供进一步局部稳定性证据。FIRE使用伪动力学，优化时间步不是材料演化的物理时长。达到最大步数和达到力阈值分别报告。压力下目标包含适当PV项。

文献：[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)；[ASE_FILTER ASE: Filters](https://docs.ase-lib.org/ase/filters.html)；[ASE_MD ASE: Molecular dynamics](https://docs.ase-lib.org/ase/md.html)。

## 21. MLIP与DFT怎样配合评价

先用低成本势处理大量候选，再围绕论文主张选择DFT与性质复核。

**标签一致。** MLIP可能学习raw或已修正能量。候选、元素参考和竞争相必须处于相容尺度。

**具体例子。** CHGNet原MPtrj权重学习已做MP2020修正的能量，重复加同一修正会再次移动能量。

**自洽凸包。** 可用同一MLIP计算候选和竞争相，再构造参考包；模型外推误差仍需研究。

**DFT复核。** 记录选样规则、原始分母与失败。随机核验、阈值附近核验和高分筛选回答不同问题。

不同checkpoint可能使用PBE、r2SCAN、MatPES等训练数据，不能对所有MLIP统一说raw或corrected。自洽MLIP hull还需说明参考结构是固定几何单点，还是同一势弛豫后评价。项目既有MP校正约定不因这份教学PPT改变。

文献：[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[CHGNET_DOC CHGNet official project documentation](https://chgnet.lbl.gov/)；[R46 lemat](https://arxiv.org/html/2512.04562v2)；[MP_COMPAT Materials Project: Anion and GGA/GGA+U Mixing](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing)。

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

文献：[PHONOPY Phonopy: Formulations](https://phonopy.github.io/phonopy/formulation.html)；[MP_ELASTIC Materials Project: Elastic Constants](https://docs.materialsproject.org/methodology/materials-methodology/elasticity)；[ASE_MD ASE: Molecular dynamics](https://docs.ase-lib.org/ase/md.html)；[ASE_NEB ASE: Nudged elastic band](https://docs.ase-lib.org/ase/neb.html)；[MP_ELECTRONIC Materials Project: Electronic Structure](https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)。

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

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_DATA MatterGen official Alex-MP data release](https://github.com/microsoft/mattergen/blob/main/data-release/alex-mp/README.md)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)。

## 24. MatterGen 2/5：联合扩散与条件适配

**建模。** 元素用吸收mask噪声，位置用周期噪声，晶格用连续噪声；GemNet-dT联合预测去噪。

**训练与控制。** 条件经adapter注入，微调全部网络权重。采样用classifier-free guidance，保持周期结构表示。

原图：[Zeni et al., Nature 2025, Fig.1](https://www.nature.com/articles/s41586-025-08628-5/figures/1)，CC BY 4.0。

原图保持原始比例与标记，来源Nature Fig1。SI A/B：GemNet-dT 4 message-passing层，邻域7Å，node/edge hidden512；categorical D3PM与coordinate/lattice score-matching联合损失。基础模型1.74M训练步，8×A100，每GPU batch64/global512，Adam lr1e-4。4个zero-init adapters；SI B.1明确fine-tune更新所有权重，非只训adapter。fine-tune globalbatch128 lr6e-5。1000 ancestral predictor步，位置/晶格Langevin corrector，SNR0.4/0.2；条件CFG γ=2。

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)。

## 25. MatterGen 3/5：无条件生成怎样评测

相同Alex-MP训练范围下，用DFT弛豫后的结构评价SUN。

**评测链。** 1,024个样本经DFT弛豫、能量比较与结构匹配。

**结果。** 约75%在参考凸包0.1 eV/atom内，约3%低于固定参考包。

**解释。** Table D4的SUN为38.57%，生成到弛豫终态的RMSD为0.021 Å。

图表数据：{"categories":["DiffCSP","MatterGen"],"values":[33.27,38.57],"name":"论文SUN（%）","max":45,"decimals":2}

SI TableD4的同Alex-MP对比：MatterGen SUN38.57%、RMSD0.021Å；DiffCSP33.27%、0.104Å。标准初批1024；Nature约75%与3%为正文概括。RMSD是到DFT弛豫终态的变化，不是CSP到已知参考的误差。参考hull850384有序结构，novelty另含117652无序ICSD。当前公开repo默认MatterSim预测评价，且checkpoints为重训版本，不直接替代本文DFT数字。

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REPO Microsoft MatterGen official README and data-release descriptions](https://github.com/microsoft/mattergen)。

## 26. MatterGen 4/5：条件设计如何验证

性质条件的价值，用满足目标且物理合格的候选数量检验。

**条件与标签。** 磁性约60.5万、带隙约4.2万、体模量约5,000个标签，分别用于对应任务。

**计算对照。** 同一预测器辅助，180次DFT性质调用：MatterGen获得106个，筛选参照40个。

**代价范围。** 原文预算轴只统计性质调用。训练、筛选与DFT弛豫另计。

图表数据：{"categories":["筛选参照","MatterGen"],"values":[40,106],"name":"体模量 > 400 GPa的论文SUN数","max":120,"decimals":0}

Fig4a-c显示性质条件分布，Fig4h为bulk modulus>400GPa的合格数量。条件训练标签可由不同物理或ML预测器得到，例如bulk modulus adapter用ML预测标签，最终以DFT性质验证。需要同时检查条件命中及SUN交集，不把条件分布均值当材料发现。

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)。

## 27. MatterGen 5/5：计算怎样连接实际实验

**筛选过程。** 32,768个提案逐级筛到75个DFT候选，选四个尝试，原文报告一个产物。

**结构与成分。** 原文将产物拟合为约98%无序TaCr₂O₆，另有约2% Cr₂O₃。

**功能测量。** 目标200 GPa，DFT约222。实验换算体模量158±11 GPa，最高169 GPa。

原图：[Zeni et al., Nature 2025, Fig.6](https://www.nature.com/articles/s41586-025-08628-5/figures/6)，CC BY 4.0。

Fig6a为XRD/Rietveld及样品，b/c为有序目标及无序结构，d是95个ICSD再发现的DFT体模量，不是实验模量图。SI筛选：32768→7919含氧→2196(MatterSim Ehull≤.05)→551去重/新颖→119声子无负频→75(DFT≤.03)→4专家挑选→1报告合成，另外3个尝试失败。主文DFT222GPa，图6b标221GPa，页面用约222。纳米压痕测Young模量，K=Y/[3(1−2ν)]，ν取DFT0.30，四次推算均值158±11，最大169。原文“距目标20%内”采用最大值。2026-04-20 Juelsholt在Materials Horizons 13,5672–5679的再分析重新精修公开PXRD，报告Ta0.43Cr0.57O2，并指出已知TaCrO4型结构及三种有序近似存在训练资料，挑战该案例新化合物身份。这里分别归属2025原报告与2026再分析，未重做PXRD精修。

文献：[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REANALYSIS Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)。

## 28. NMI及相关期刊中的两类模型贡献

| 论文 | 模型与数据 | 主要评测与科学结果 |
| --- | --- | --- |
| Chemeleon2<br>NMI 2026 | latent Diffusion + GRPO<br>MP-20 / Alex-MP-20 | 10,000个原始样本做MACE评测；选择性DFT与带隙交集，无新合成 |
| CHGNet<br>NMI 2023 | 磁矩相关监督的通用势<br>MPtrj弛豫数据 | E/F/应力误差，MD及电荷相关应用；与DFT和已有实验比较 |
| M3GNet<br>Nature Computational Science | 三体图网络通用势<br>MP弛豫数据 | 约3,100万假想结构筛选，优先2,000个DFT核验，并开展声子等计算 |

前者研究怎样提出目标材料，后者研究怎样可靠计算结构响应。论文主张决定验证方式。

Chemeleon2基于latent DiT和GRPO，10,000个raw样本以MACE-MPA-0及Ehull<0.1评mSUN。原文同Alex-MP-20 RL前后mSUN15.9%到61.3%；novelty62.3%到97.5%；uniqueness99.4%到88.7%。1,000个样本DFT检验代理，条件3eV每批512，82个raw同时mSUN与2.7–3.3eV，另评DFT弛豫后保持。不能与MatterGen DFT弛豫SUN直接排名。CHGNet示例Li0.5MnO2 1100K、1.5ns MD，以及LixFePO4相图；本文无新合成，使用既有实验比较。M3GNet优先2,000个DFT得到1,578个低hull候选，328个无虚频为M3GNet声子，不是全DFT声子或合成。

文献：[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R10 M3GNet2022](https://www.nature.com/articles/s43588-022-00349-3)。

## 29. 相关子刊怎样增加材料层面的证据

| 工作与期刊 | 核心问题 | 在生成指标之外做什么 |
| --- | --- | --- |
| SCIGEN<br>Nature Materials | 把功能图案嵌入晶体 | DFT能带、合成探索、XRD及实际产物的磁性与电阻 |
| Chemeleon<br>Nature Communications | 文本条件探索化学空间 | MACE预筛、DFT相图，选定Li₂PS₃做声子；无新合成 |
| SLICES<br>Nature Communications | 周期结构的可逆图表示 | 重构、逆设计、最终14个计算直接带隙候选；无新合成 |
| CrystaLLM<br>Nature Communications | CIF自回归与引导搜索 | 语法及结构指标，选择新颖子集做DFT；无新合成 |

这些案例把算法改善连接到具体材料问题，并明确计算候选与实际产物分别是什么。

SCIGEN生成提案TiPdBi/TiPdSb，实际材料TiPd0.22Bi0.88/Ti0.5Pd1.5Sb，计量和对称均变化；作者说明实验探索不是理想结构的直接验证。其大规模53%主要为残余力/结构弛豫资格，不能当hull、SUN或phonon无虚频率。Chemeleon和SLICES的计算与实验范围按对应原文保留，不据期刊名补写合成。

文献：[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R39 Chemeleon](https://www.nature.com/articles/s41467-025-59636-y)；[R16 slices](https://www.nature.com/articles/s41467-023-42870-7)；[R12 crystallm](https://www.nature.com/articles/s41467-024-54639-7)。

## 30. 阅读与复现的关键来源

**任务与基准。** CDVAE、DiffCSP、FlowMM的原文与官方数据配置。

**数据与相稳定。** Materials Project方法文档、Alexandria发布页、pymatgen相图与结构匹配。

**物理计算。** CHGNet / MACE / MatterSim模型资料；ASE与Phonopy方法说明。

**MatterGen。** Nature正式论文、补充材料与官方代码。五页所引数据和原图各有来源位置。

本页备注附完整引用。教学图和算例为人为构造，其他数值均来自指定原始文献或官方方法资料。没有运行新生成、DFT或材料实验。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[MG_SI MatterGen Supplementary Information, Sections A–D](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf)；[MG_REPO Microsoft MatterGen official README and data-release descriptions](https://github.com/microsoft/mattergen)；[PHASE Materials Project: Phase diagrams and thermodynamic stability](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)；[MATCHER pymatgen StructureMatcher](https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher)；[ASE_OPT ASE: Structure optimization](https://docs.ase-lib.org/ase/optimize.html)；[PHONOPY Phonopy: Formulations](https://phonopy.github.io/phonopy/formulation.html)。

## 完整参考文献

- [R04] Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter, David Skinner, Gerbrand Ceder, Kristin A. Persson. Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. APL Materials 1, 011002 (2013). DOI: 10.1063/1.4812323. https://doi.org/10.1063/1.4812323

- [R08] Tian Xie, Xiang Fu, Octavian-Eugen Ganea, Regina Barzilay, Tommi Jaakkola. Crystal Diffusion Variational Autoencoder for Periodic Material Generation. ICLR 2022. https://arxiv.org/abs/2110.06197

- [R10] Chi Chen, Shyue Ping Ong. A universal graph deep learning interatomic potential for the periodic table. Nature Computational Science 2, 718–728. DOI: 10.1038/s43588-022-00349-3. https://www.nature.com/articles/s43588-022-00349-3

- [R11] Bowen Deng, Peichen Zhong, KyuJung Jun, Janosh Riebesell, Kevin Han, Christopher J. Bartel, Gerbrand Ceder. CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling. Nature Machine Intelligence 5, 1031–1041. DOI: 10.1038/s42256-023-00716-3. https://www.nature.com/articles/s42256-023-00716-3

- [R12] Luis M. Antunes, Keith T. Butler, Ricardo Grau-Crespo. Crystal structure generation with autoregressive large language modeling. Nature Communications 15, 10570 2024. DOI: 10.1038/s41467-024-54639-7. https://www.nature.com/articles/s41467-024-54639-7

- [R13] Rui Jiao, Wenbing Huang, Peijia Lin, Jiaqi Han, Pin Chen, Yutong Lu, Yang Liu. Crystal Structure Prediction by Joint Equivariant Diffusion. NeurIPS 2023. https://arxiv.org/abs/2309.04475

- [R16] Hang Xiao, Rong Li, Xiaoyang Shi, Yan Chen, Liangliang Zhu, Xi Chen, Lei Wang. An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning. Nature Communications 14, 7027 2023. DOI: 10.1038/s41467-023-42870-7. https://www.nature.com/articles/s41467-023-42870-7

- [R19] Claudio Zeni, Robert Pinsler, Daniel Zügner, Andrew Fowler, Matthew Horton, Xiang Fu, Zilong Wang, Aliaksandra Shysheya, Jonathan Crabbé, Shoko Ueda, Roberto Sordillo, Lixin Sun, Jake Smith, Bichlien Nguyen, Hannes Schulz, Sarah Lewis, Chin-Wei Huang, Ziheng Lu, Yichi Zhou, Han Yang, Hongxia Hao, Jielan Li, Chunlei Yang, Wenjie Li, Ryota Tomioka, Tian Xie. A generative model for inorganic materials design. Nature 2025. DOI: 10.1038/s41586-025-08628-5. https://www.nature.com/articles/s41586-025-08628-5

- [R21] Nate Gruver, Anuroop Sriram, Andrea Madotto, Andrew Gordon Wilson, C. Lawrence Zitnick, Zachary Ulissi. Fine-Tuned Language Models Generate Stable Inorganic Materials as Text. ICLR 2024. https://arxiv.org/abs/2402.04379

- [R26] Miller, Benjamin Kurt, Chen, Ricky T. Q., Sriram, Anuroop, Wood, Brandon M. FlowMM: Generating Materials with Riemannian Flow Matching. ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/miller24a.html

- [R27] Ryotaro Okabe, Mouyang Cheng, Abhijatmedhi Chotrattanapituk, Manasi Mandal, Kiran Mak, Denisse Córdova Carrizales, Nguyen Tuan Hung, Xiang Fu, Bowen Han, Yao Wang, Weiwei Xie, Robert J. Cava, Tommi S. Jaakkola, Yongqiang Cheng, Mingda Li. Structural constraint integration in a generative model for the discovery of quantum materials. Nature Materials 25, 223–230 2026. DOI: 10.1038/s41563-025-02355-y. https://www.nature.com/articles/s41563-025-02355-y

- [R29] Anuroop Sriram, Benjamin Kurt Miller, Ricky T. Q. Chen, Brandon M. Wood. FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions. NeurIPS 2024. DOI: 10.52202/079017-1464. https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html

- [R34] Hoellmer, Philipp, Egg, Thomas, Martirossyan, Maya M., Fuemmeler, Eric, Shui, Zeren, Gupta, Amit, Prakash, Pawan, Roitberg, Adrian, Liu, Mingjie, Karypis, George, Transtrum, Mark, Hennig, Richard G., Tadmor, Ellad B., Martiniani, Stefano. Open Materials Generation with Stochastic Interpolants. ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/hollmer25a.html

- [R35] Levy, Daniel, Panigrahi, Siba Smarak, Kaba, Sékou-Oumar, Zhu, Qiang, Lee, Kin Long Kelvin, Galkin, Mikhail, Miret, Santiago, Ravanbakhsh, Siamak. SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models. ICLR 2025. https://arxiv.org/abs/2502.03638

- [R39] Hyunsoo Park, Anthony Onwuli, Aron Walsh. Exploration of crystal chemical space using text-guided generative artificial intelligence. Nature Communications 16, 4379 2025. DOI: 10.1038/s41467-025-59636-y. https://www.nature.com/articles/s41467-025-59636-y

- [R42] Martirossyan, Maya M., Egg, Thomas, Hoellmer, Philipp, Karypis, George, Transtrum, Mark, Roitberg, Adrian, Liu, Mingjie, Hennig, Richard G., Tadmor, Ellad B., Martiniani, Stefano. All that structure matches does not glitter. NeurIPS Datasets and Benchmarks 2025. https://arxiv.org/html/2509.12178v2

- [R43] Subhojyoti Khastagir, Kishalay Das, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, Niloy Ganguly. LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation. NeurIPS 2025. DOI: 10.52202/085713-5635. https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html

- [R45] Hyunsoo Park, Aron Walsh. Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning. Nature Machine Intelligence 2026. DOI: 10.1038/s42256-026-01262-4. https://www.nature.com/articles/s42256-026-01262-4

- [R46] Betala, Siddharth, Gleason, Samuel P., Ramlaoui, Ali, Xu, Andy, Channing, Georgia, Levy, Daniel, Fourrier, Clémentine, Kazeev, Nikita, Joshi, Chaitanya K., Kaba, Sékou-Oumar, Therrien, Félix, Hernandez-Garcia, Alex, Mercado, Rocío, Krishnan, N. M. Anoop, Duval, Alexandre. LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models. arXiv 预印本 2025. https://arxiv.org/html/2512.04562v2

- [R49] Kiyoung Seong, Sungsoo Ahn, Sehui Han, Changyoung Park. Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling. ICML2026, PMLR306:109105–109131. https://proceedings.mlr.press/v306/seong26a.html

- [R52] Negishi, Masahiro, Walsh, Aron. Substitution-Based Analysis of Structural Novelty for Generative Models of Materials. arXiv 预印本 2026. https://arxiv.org/html/2606.23166v1

- [IUCR] How to read (and understand) Volume A of International Tables for Crystallography: an introduction for nonspecialists. 2010. https://journals.iucr.org/j/issues/2010/05/02/kk5061/index.html

- [ALEX] Alexandria official dataset releases. Official documentation. https://alexandria.icams.rub.de/datasets.html

- [OQMD] OQMD official structure sources and API documentation. Official documentation. https://oqmd.org/documentation/structures

- [ICSD] ICSD official data curation and theoretical data categories. Official documentation. https://icsd.products.fiz-karlsruhe.de/en/about/data-curation

- [COD] Crystallography Open Database (COD): an open-access collection of crystal structures and platform for world-wide collaboration. 2012. https://academic.oup.com/nar/article/40/D1/D420/2903497

- [CDVAE_CFG] CDVAE official MP-20 configuration and build_crystal preprocessing. Official documentation. https://github.com/txie-93/cdvae/blob/main/conf/data/mp_20.yaml

- [MACE] A foundation model for atomistic materials chemistry. 2025. https://arxiv.org/html/2401.00096v3

- [MATTERSIM] MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures. 2024. https://arxiv.org/html/2405.04967v2

- [MATTERSIM_CARD] MatterSim official model card: v1.0.0-1M and v1.0.0-5M. Official documentation. https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md

- [SMACT] SMACT screening module. Official documentation. https://smact.readthedocs.io/en/latest/smact.screening.html

- [SCIPY_JS] scipy.spatial.distance.jensenshannon. Official documentation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html

- [SCIPY_W] scipy.stats.wasserstein_distance. Official documentation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html

- [PYM_HULL] pymatgen.analysis.phase_diagram.PhaseDiagram. Official documentation. https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.phase_diagram.PhaseDiagram.get_decomp_and_e_above_hull

- [MP_COMPAT] Materials Project: Anion and GGA/GGA+U Mixing. Official documentation. https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability/anion-and-gga-gga+u-mixing

- [ASE_OPT] ASE: Structure optimization. Official documentation. https://docs.ase-lib.org/ase/optimize.html

- [ASE_FILTER] ASE: Filters. Official documentation. https://docs.ase-lib.org/ase/filters.html

- [ASE_MD] ASE: Molecular dynamics. Official documentation. https://docs.ase-lib.org/ase/md.html

- [ASE_NEB] ASE: Nudged elastic band. Official documentation. https://docs.ase-lib.org/ase/neb.html

- [PHONOPY] Phonopy: Formulations. Official documentation. https://phonopy.github.io/phonopy/formulation.html

- [MP_DFT] Materials Project: Parameters and Convergence. Official documentation. https://docs.materialsproject.org/methodology/materials-methodology/calculation-details/gga+u-calculations/parameters-and-convergence

- [MP_ELECTRONIC] Materials Project: Electronic Structure. Official documentation. https://docs.materialsproject.org/methodology/materials-methodology/electronic-structure

- [MP_ELASTIC] Materials Project: Elastic Constants. Official documentation. https://docs.materialsproject.org/methodology/materials-methodology/elasticity

- [CHGNET_DOC] CHGNet official project documentation. Official documentation. https://chgnet.lbl.gov/

- [MG_REPO] Microsoft MatterGen official README and data-release descriptions. Official documentation. https://github.com/microsoft/mattergen

- [MG_SI] Claudio Zeni et al.. MatterGen Supplementary Information, Sections A–D. Nature (2025). https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-08628-5/MediaObjects/41586_2025_8628_MOESM1_ESM.pdf

- [MG_DATA] MatterGen official Alex-MP data release. Official data documentation. https://github.com/microsoft/mattergen/blob/main/data-release/alex-mp/README.md

- [PHASE] Materials Project: Phase diagrams and thermodynamic stability. Official documentation. https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds

- [MATCHER] pymatgen StructureMatcher. Official API documentation. https://pymatgen.org/pymatgen.analysis.html#pymatgen.analysis.structure_matcher.StructureMatcher

- [MG_REANALYSIS] Mikkel Juelsholt. Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset. Materials Horizons 13, 5672–5679 (2026). https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d
