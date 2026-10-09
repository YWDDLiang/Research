# R3｜从物理后果学习晶体生成动作：过程条件化教师与独立生成器自蒸馏

**定位更新（2026-10-10）：本文件保留为前轮技术备选。当前研究以[六条挑战](../landscape/02-open-problems.md)和[四组科学问题](../programs/README.md)为主线，方法实现不预先限定论文问题。**

2026-10-09。中文论文提案；尚未运行本方案实验。已纳入同行讨论修订。目标为无机晶体独立生成的严格 SUN 提升、低能新颖结果覆盖和 U 保留。只有一个主基座 OMatG，不增加验证基座。物理模型用于训练数据获取与最终评价，普通学生生成时不查询物理模型。

## 提案摘要

晶体生成器可以通过物理精修得到更好的端点，但昂贵计算通常只以一个能量奖励或一组松弛后结构返回训练。我们研究：同样的已付费物理计算中，力、应力和松弛响应能否改善生成动作的学习，使下一次独立生成本身更可靠？方案固定 OMatG 的原生物种离散流与坐标随机动力学、分支采集和物理评价数据；训练一个读取实测物理后果的特权教师，输出原生动作分布，再蒸馏到只看当前状态的普通生成器。教师输入包括原始力/应力、六个松弛节点的相对响应和终点资格，输出坐标转移均值与物种概率。它不输出标量 value，也不把松弛端点当学生回归目标。关键比较是同候选、同奖励、同预算下，丰富物理教师与标量教师、终点模仿和奖励后训练的差异。预期贡献是说明哪种物理后果能形成可迁移的动作知识，并增加新独立采样中的严格 SUN；所有性能结论等待实验。

## 1. Introduction：物理优化能改变结果，却还没有教会生成器怎样改变

生成先验使晶体搜索进入合理区域，物理计算决定这些区域是否真的有用。两者已经可以有效结合：[GSS](https://arxiv.org/html/2604.27636v1) 在给定组成的周期结构搜索中结合生成 score 与物理力，扩大若干参考结构的覆盖；[OMatG-IRL](https://proceedings.mlr.press/v306/hollmer26a.html) 在 CSP 中把物理能量反馈用于速度场和退火策略。这些原文表明物理信息能够改变搜索结果，但它们处理的主要对象是采样引导、给定组成的优化和采样成本，尚未回答如何把过程中的知识摊销成普通无机 DNG 能力。

另一条路线直接修改生成器。[OMatGRPO](https://arxiv.org/html/2610.03880v1) 更新物种离散转移并在松弛后评分；其奖励交换结果提示，反馈能否被利用取决于生成表示与解码器。[CrystAF](https://arxiv.org/html/2609.36398v1) 在分子晶体中固定 UMA 信号比较注入位置，发现其普通松弛目标回归收益有限，物理后训练更有效。[PackFlow](https://arxiv.org/html/2602.20140v1) 已用能量/力优势进行分子晶体后训练。因此，R3 的动机不是“再引入力奖励”，而是**同样的物理反馈为什么在一种学习接口下能改变有用动作，在另一种接口下只改变自评分或重建概率**。

内部历史使问题更具体。固定成分的 JTF 同512源比较，known stable 为 plain/restored/detached 的76/85/86，每臂24未知；连续几何与晶胞演化能改变端点。F800在B0/Crys中把confirmed SUN分别从45→118/1500和77→95/1022提高，同时novelty下降。随后某个早段skip对比无strict gains/losses，极小坐标动作和自学习H的单调增长也没有稳定带来终点收益。成败共同指出：物理下降、状态可预测性、动作可改变终点是三个不同对象。R3保留前两类信息，却以第三类能力组织学习。[历史证据](../evidence/historical-evidence.md)、[PDE15–30](../evidence/historical-evidence.md)。这些旧实验不是本方案数据或新基座结果。

本文拟提出的中心主张是：**在固定原生动作族和实测采集池下，带原子与时间结构的物理后果条件，比终点标量条件更有效地学习可执行的动作投影，并提高普通独立生成的严格SUN。**它改善的是独立 generator 的参数学习；没有增加部署时的source修订核。

## 2. 近邻与真正的学习差别

| 近邻 | 实际对象及反馈 | R3的区别 |
|---|---|---|
| OMatG-IRL，ICML2026 | 主要CSP；相对能量、速度场/退火policy | 固定原生动作和采集池，比较过程后果如何指导动作分布学习；主结果为DNG独立采样 |
| OMatGRPO，2026-10预印本 | 无机DNG；species+continuous likelihood，终点reward | 同物理标签训练action-conditioned teacher；学习期有过程token，学生部署没有 |
| [OMatG-flash](https://arxiv.org/abs/2609.26402)，2026-09预印本 | 无机CSP/DNG flow map；RAM后训练只实验CSP，reward在50步松弛后计算 | R3保持原native generator/action，不以少步flow map或RAM为贡献，主张过程信息改善DNG动作学习 |
| GSS，2026-04预印本 | 固定组成/分子构象的物理搜索；每次score+force | 过程调用只在采集阶段，知识进入学生参数；不把局部驻点等同严格hull稳定 |
| CrystAF/NFT | 分子CSP；标量能量、力、应力优势；前向loss更新 | 力/应力以带原子与时间结构的后果条件进入教师，更新目标是native动作分布的蒸馏 |
| PackFlow | 分子CSP；heavy-atom energy/force优势 | 不将分子packing成功等同无机严格SUN，保持真实DNG评价 |
| Traj2Relax，JCIM2026 | 几何轨迹→松弛velocity；加速结构relax | R3输出独立生成器原生动作，最终仍共同物理评价，不替换松弛器 |
| ANCHOR，2026-09预印本 | 冻结CSP的组成搜索；发现结构回流likelihood训练 | 不新增composition search policy；保持原生联合动作，输入实际物理过程，训练后仍普通DNG |
| endpoint SFT | 以松弛终点作为新训练结构 | R3的监督对象是生成状态→下一原生动作，物理终点是后果条件而非坐标目标 |
| scalar value/PDE H | 状态→终点能量/成功概率；按其梯度或分数选动作 | R3教师输出各原子坐标转移与物种概率；不会部署或微分一个预测H来行动 |

ANCHOR的结构回流说明“将发现的结构再训练”本身已有直接近邻；本方案应在**相同终点池**上证明过程信息及动作学习的额外作用。[ANCHOR](https://arxiv.org/html/2609.33407v1)。CV中的[DRM](https://arxiv.org/html/2605.25661v1)支持噪声态反馈接口、[DTS](https://arxiv.org/html/2506.20701v1)支持用终点后果更新早期判断；特权条件教师的训练原则也与[SDPO](https://arxiv.org/html/2601.20802v2)有关。R3的科学对象是物理后果与无机生成动作的映射，不能仅以算法名迁移主张创新。

## 3. 一个基座，明确的状态、动作与输出

主基座选已发布的 **OMatG/MP-20-DNG，Trig-SDE-Gamma**。2026-10-09只读API核查：仓库revision为`6af2cc9a1fa569341fb7a08a542490868ab84867`，`Trig-SDE-Gamma/checkpoint.ckpt`与`train.yaml`均列在文件清单；没有下载权重。[发布入口](https://huggingface.co/OMatG/MP-20-DNG/tree/main/Trig-SDE-Gamma)、[原始配置](https://huggingface.co/OMatG/MP-20-DNG/raw/main/Trig-SDE-Gamma/train.yaml)。

该配置的真实接口是：坐标SDE、species masked DFM、cell ODE，760个原生积分时间节点。不能把它们都写成Gaussian action。

- **状态**：`s_t=(N,A_t,X_t,L_t,t)`，保留原子槽位身份、当前masked species、周期坐标、晶胞及原生hidden states。N仍按基座原分布产生；本版本不增加删原子的动作。
- **动作**：一个原生Euler子步的坐标未wrap增量，以及本步发生unmask时的物种选择；remask/unmask时钟和随机规则固定。连续坐标由原生SDE产生。cell仍按同一冻结基座的ODE规则随当前联合状态演化。
- **学生可学参数**：冻结原始OMatG，增添残差adapter，输出坐标drift修正与species-logit修正。保留原denoiser、扩散强度与cell函数。新坐标/物种会改变后续原生cell响应，因此并非固定晶胞。
- **续程**：冻结当前采集policy快照，在一段原生block之后继续原生生成到完整raw晶体；再调用共同MLIP变胞FIRE。来自同一parent的分支用相同后续噪声bank；部分动作追加第二个后续bank，测量晚期随机性的影响。
- **最终输出**：只输入新随机seed的普通OMatG学生生成raw晶体。教师和物理bundle均不在部署路径。主评价在共同最终松弛几何上计算S、N、U。

当前配置已核species采样代码：categorical head只在native unmask事件进入；continuous实现返回velocity与denoiser供SDE使用。[species代码](https://github.com/FERMat-ML/OMatG/blob/main/omg/si/discrete_flow_matching_mask.py)、[连续积分代码](https://github.com/FERMat-ML/OMatG/blob/main/omg/si/single_stochastic_interpolant.py)。采集时需保存实际Euler子步的未wrap增量，才能建立正确的坐标转移likelihood。teacher与student使用同一deterministic cell rule，所以动作KL不包含虚构的cell Gaussian项。

## 4. 实测物理信息与教师输入

每个已评估branch得到物理bundle `Y`：

1. raw完整晶体的每原子力、6分量应力、能量。
2. FIRE轨迹中0%、20%、40%、60%、80%、100%六个节点的力、应力及相对raw的能量变化；不足六节点的轨迹用节点mask。
3. 每原子松弛位移和晶胞相对应变；统一到raw的原子槽位、周期/胞基规范，移除平移自由度。
4. 最终E_hull、convergence状态、reference-novel标记、同parent各branch的最终结构匹配关系。无法取得hull/reference标签时，该字段是unknown，过程字段仍可用。

教师不读取生成动作的随机噪声、下一生成状态、完整native未来轨迹、future species序列或最终绝对坐标。第3项位移是**raw晶体到物理松弛终点的响应**，并非parent到native第一步的位移。它仍包含未来信息，正是需要摊销的特权知识；主机制比较同时提供不含位移的force/stress过程教师，以识别直接几何复制的贡献。反馈价值以新后续和新parent的物理收益建立，而非teacher重建旧动作的准确率。

教师采用基座副本加feedback adapter：原子过程token与当前槽位一一对应，全局stress/energy/terminal token通过cross-attention进入；力和位移向量使用等变投影或相对于当前周期位移的标量投影，避免把固定Cartesian分量当作旋转不变量。输出仍是基座的coordinate drift和species logits。学习期关闭一部分feedback token可训练missing-field处理；学生从来不接这些token。

主物理体系采用组合提案的[共同CHGNet/FIRE协议](../evidence/common-protocol.md)：以CHGNet0.3.0、变胞FIRE500和`fmax=0.05 eV/Å`为初始设置，候选与冻结参考快照使用一致能量约定。reference定义、matcher和严格`E_hull<=0`在主比较中固定。UMA/LeMat-Bulk是OMatGRPO近邻的真实评估路线，不作为本方案另一套主标签。旧结果仅用于motivation，新OMatG数据按共同流程取得。

## 5. 方法：后果条件化的原生动作教师

### 5.1 先建立同状态的原生反事实分支

从完整原生生成中抽取parent，分配在`t≈0.30/0.55/0.80`三个时段；每个parent只分配一个时段。复制状态，使用同一原生策略与不同Brownian/species随机数产生8个block动作；block包含约总生成时长的10%，不是0.003Å单点微扰。动作族、solver、评价数据在各学习方法之间相同；该分支采样是获得信息的方法，不作为新的物理编辑算法主张。

对每个branch执行共同续程并保存`(s_(b,j,i),a_(b,j,i),Y_(b,j))`，其中b是parent，j是branch，i是block内部子步。只有`i=0`的各branch共享同一个`s_b`；之后状态已经分叉。固定parent划分TRAIN/DEV，整条原生轨迹和所有物理后果始终跟随parent。内部子步提供动作监督，物理样本数按branch终点计，不能把时间节点当独立晶体结果。

### 5.2 教师学习后果条件化的受限native动作模型

令`T_psi(a|s,Y)`为物理后果条件化的受限原生动作模型。它拟合当前采集策略下的后果—动作关系，训练目标为：

`L_teacher = − E_(s,a,Y) log T_psi(a|s,Y)`。

坐标分布采用原生Euler的同一协方差`Sigma_t`，仅学习mean；species采用原native event rate和条件categorical概率。等价地，teacher loss包含协方差归一的坐标误差，以及实际unmask事件的species CE。cell没有独立随机action，不加入cell NLL。

该教师学的是“观测到这种物理过程后果时，哪些原生动作更可能产生它”。每原子响应使训练可以共享局部几何/化学兼容信息，global stress和terminal token使局部知识联系到共同后果；不是直接将末端force复制成当前force guidance。

### 5.3 将有用后果的动作分布蒸馏到普通学生

为同parent的实测后果定义utility：低E_hull的平滑资格函数乘reference novelty，训练中还保留strict success标记。采用`r(Y)=nu(Y)/(1+exp(E_hull(Y)/sigma))`，`sigma=0.05 eV/atom`为首版计划参数；**主成功阈值仍为0**。未知终点不获得虚构成功credit。rich/scalar教师比较使用相同utility；其它学习对象对照也报告这一评分，但其损失并不因此成为相同目标。

首版固定`tau=0.25`、uniform replay比例`rho=0.20`：对资格标签已知的branch按指数utility归一，再混入所有branch的uniform项，即`w_(b,j)=(1−rho) exp(r_j/tau) 1_known/Z_b + rho/K`。一个parent全未知时仅使用uniform回放。主比较不加入类平衡或occupancy权重。rich/scalar教师和直接action targets使用完全相同的权重、状态、容量、回放及原生动作族；两教师看到相同终点标量bundle（E_hull、novelty、状态及r），rich教师额外看到已付费过程信息。

学生只看各自实际状态，进行带后果条件的**轨迹加权蒸馏**：

`L_student = E_b sum_j w_(b,j) (1/m) sum_(i=0)^(m−1) KL[T_psi(.|s_(b,j,i),Y_(b,j)) || pi_theta(.|s_(b,j,i))] + lambda L_base`。

共同起点`i=0`可对实测`Y_(b,j)`混合教师；内部`i>0`只使用该branch自己的状态与后果，并继承parent的branch权重。另一branch的Y不是该内部状态的实测可达后果，不跨branch移植。各branch时间步数有差异时分别按实际m归一化。

这里`L_base`是原MP20 stochastic-interpolant训练回放与对原native action的anchor，两个目的分别是保留普通生成能力、限制单轮数据的剧烈偏移。教师stop-gradient。categorical KL只在unmask支持上计算，并按实际event概率加权。学生生成时不请求目标Y，不寻找source crystal。

**有限步投影的数学意义。** 在共享起点，教师坐标项为`sum_j w_j KL[N(mu_j,Sigma_t)||N(mu_student,Sigma_t)]`，其无其它约束的最优均值是`mu_student=sum_j w_j mu_j`。这把后果条件动作混合投影到现有Gaussian族，可能平均通往不同有用结果的方向。它与下面理想Bayes边际是不同层次；固定协方差、因子化species及base约束均限制可表达的分布，不宣称保留一般多峰后验。分叉状态的loss仍按本branch配对计算。

仅在同一共享状态s处，一个理想化解释是：参考联合分布`P0(a,Y|s)`按有用后果加权后，其动作边际可写成

`pi_target(a|s)=integral P0(a|s,Y) q_target(Y|s) dY`，

其中`q_target(Y|s) ∝ P0(Y|s) exp(r(Y)/tau)`。相应边际为`pi_target(a|s) ∝ pi0(a|s) E[exp(r(Y)/tau)|s,a]`，包含终点utility的条件指数矩；它不等于`exp(E[r|s,a]/tau)`，也不直接等同冻结续程下普通expected-reward问题的最优策略。该恒等式解释共享起点的后果混合，内部实际采用上述轨迹加权loss。在无限数据、精确posterior下，标量充分统计也能表示同一倾斜。R3的假设是：**有限物理数据中，带原子/过程结构的Y比单值reward更容易学习和迁移这个条件映射**。

因此主比较必须包括同一批futures直接产生的scalar-weighted action BC／soft action targets，使用相同指数权重、原生state分布和base回放。rich teacher需胜过这个直接动作监督，才能支持条件泛化或估计优势；并不能仅靠更多label或改变倾斜规则解释。

### 5.4 新后续区分特权教师、动作投影与学生

DEV parent仍有实际观察到的候选Y。在同parent和共同新后续噪声下比较四个执行策略：rich教师抽取一个Y后执行native block；rich教师仅在共享起点将第一步mean/categorical混合投影、后续沿同一选定Y的教师执行；终点scalar教师按同一个Y的标量bundle执行；普通student执行。第二项只隔离共同起点的投影效应，不把root的其它Y移植为内部状态的实测后果。结果比较terminal qualification，配合共享起点的均值/方向审计；teacher loglikelihood只作为学习诊断。

这区分“选Y教师能行动，但均值投影损失收益”和“投影有效，但普通student未学到”。新parent的普通独立生成仍是主结论，特权教师优势不能替代它。主机制比较为rich/scalar同池同容量同权重的学生；NFT、直接action targets及endpoint SFT分别检验其它更新接口，不声称全部优化目标相同。

## 6. 数据与预算方案：只为最小科学问题付费

拟采用以下初始预算，全部是规划而非已支出：

| 项目 | 结构终点数 | 获得的信息 |
|---|---:|---|
| 512个parent×8原生branch | 4,096 | 同状态替代动作、完整raw→physical后果；parent中384 TRAIN、64 DEV、64保留分析 |
| 128个TRAIN parent×4既有动作再追加一个后续 | 512 | 区分动作后果与后续随机性；同动作的第二次结果 |
| 64个DEV parent×3新后续×选Yrich/root投影rich/scalar/student四策略 | 768 | 特权教师、共享起点投影与学生的真实行动收益；不参与训练 |
| 独立主评价：每模型2,500生成×3训练seed | 每模型7,500 | strict SUN、U与distinct low-energy novel曲线 |

初始数据获取为4,608个已评终点，其中TRAIN为`384×8+128×4=3,584`，DEV及保留分析共1,024。教师新后续另768，合计获取与机制评价5,376个终点。六个物理节点主要是同一FIRE过程中已计算的量，不为每个节点再启动一次relaxation。参考缓存复用共同协议，但计算模型/energy convention须一致。记录generator NFE、MLIP E/F/stress calls、实际optimizer steps、墙钟、训练GPUh与reference缺失；本提案没有可保证的运行时间估计。

第一轮主比较共用冻结采集pool，以区分**更多信息**与**更多样本/更大搜索预算**。后续在线刷新可作为实际训练延伸，但首个机制结论不依赖各方法生成不同训练池。旧JTF/F800数据不能直接作为新OMatG action posterior监督；可用的原子过程规范与物理历史用于接口设计。

## 7. 关键结果图表与机制实验

### 主表：普通独立生成是否改善

同基座、同adapter部署容量、同训练pool、同物理/matcher条件比较：原始OMatG；同终点pool的relaxed endpoint SFT；同futures、同指数权重的直接action BC/soft targets；同raw候选及reward的离线NFT；scalar-conditioned teacher→student；rich teacher→student。明确离线固定池更新不等于原论文完整online训练。主列为strict SUN数量/率、S/N/U联合结果、未知数、low-E_hull分布和部署生成成本。新增熟悉框架化学组合与新框架都计入成功。

### 图1：物理信息是否真的改善动作，而非只解释旧动作

DEV的新后续中画选Yrich、共享起点投影rich、scalar和student的稳定新颖资格；再画普通student独立新seed结果。前半区分反馈可行动性与动作族投影，后半回答收益能否摊销。

### 图2：收益发生于哪些原生决定

分三个采集时间段，比较species改变、结构改变与terminal class变化。用同成分子集区分几何作用，用composition-matched conditional结果解释化学分配作用，但不将任何子集取代DNG主任务。展示成功与失败路径各一例：哪个native选择改变了后续物理响应；哪种force减少却未跨hull事件。

### 图3：已付过程信息的最小消融

同pool比较terminal-only、raw F/stress+terminal、六节点response+terminal，全部使用相同teacher容量和目标utility。一个feedback跨parent shuffle对照仅用于判断teacher是否使用来源相容物理信息；不增加新物理样本。结果联系到哪种反馈改善新后续及独立学生，避免只报告auxiliary误差。

### 图4：成功结果支持与总成本

画相同新生成预算下distinct strict-SUN/低能新颖结果类曲线、以及训练物理费用摊销后的累计发现数。可另画一次性screening/物理搜索的费用—发现曲线，让已付训练成本和部署优势都有解释。结果类在共同最终几何上定义，不能以raw形状差异替代物理不同。

## 8. 实施路径

1. 固定发布checkpoint与原配置；做原native solver日志接口，保存unwrapped Euler动作、species event和parent identity。相同随机流下日志版forward保持原样，复用项目相应replay惯例。
2. 实现统一CHGNet-FIRE结果bundle；先用少量已有/新计划branch确认槽位、周期坐标和相对应变表示能对齐。普通格式问题自主修复，不加冗长验收流程。
3. 构建teacher adapter：原子向量响应和global tokens→coordinate drift/species logits；先在同pool训练rich/scalar教师，再评价新后续动作收益。
4. 在同native生成网络上蒸馏student residual adapter；部署删除feedback adapter与teacher。保留相同原denoiser、noise schedule和cell函数。
5. 完成独立生成主比较、过程信息消融及发现曲线。只有这组结果支持中心主张后，再决定是否需要在线刷新或更多基座；本版本不计划第二基座。

## 9. 最重要未决点

**丰富后果能否形成新的行动收益并迁移到学生。** 物理反馈具有特权未来信息，teacher重建旧动作可能很好却无法改善新后续，或者teacher有效但学生丢失收益。上述teacher→新后续→独立student三个层次直接区分它们；这是本论文的核心未知，而不是以精确likelihood代替科学结果。

**当前原生支持和物理样本能否提供足够不同的成功后果。** 小幅动作或强refiner可能使8个branch几乎同结果；strict positives也可能稀少。完整block和实际remask支持给出更丰富替代，过程监督提供密集信息，但不会凭空增加基座没有的动作。本方案首先报告同parent真实结果差异，再由实验决定需要改变采集阶段或扩大预算。它不承诺结果，也不从局部负例提前断言整条物理学习路线失败。

预期论文贡献若成立，将是可复用的物理后果条件化动作学习：在同反馈成本下比scalar/endpoint接口更有效，且提升普通独立生成的严格SUN与有用覆盖。提案目前完成的是科学问题、机制和可执行方案，尚无该方法实验结果。

## 10. 同行意见与修订

已读[R2完整评议](../evidence/reviews/r2-reviews-r3.md)，并整合root数学意见。三项修订为：共同起点的后果混合与内部实际配对分开；将教师明确为受限native动作模型，把forward-KL平均mean投影与理想Bayes解释分开；固定rich/scalar主比较的终点信息、指数权重、uniform回放、容量与动作族，将NFT/SFT列为不同学习对象对照。复用768个DEV终点预算区分选Y教师、root投影、scalar教师及student，不增加模型或查新。中心主张现由过程信息的额外新后续收益和普通独立SUN收益支持，不由特权重建、posterior精确性或一般mode-preservation支持。
