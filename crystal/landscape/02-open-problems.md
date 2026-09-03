# 晶体生成的开放问题：按 What–Why–How–Falsification 组织

> [返回晶体索引](../README.md) · 更新时间：2026-09-03  
> 优先级是本库对“科学价值 × 新颖性空间 × 可执行性 × 可证伪性”的首轮判断，不是客观排名。

## 总原则

一个值得做的问题必须同时满足：

1. 现有 benchmark 或方法确实遗漏了重要科学需求；
2. 缺口可被数学定义，而不只是语言描述；
3. 数据中存在或可主动获得解决它的信息；
4. 新方法有不可替代的职责；
5. 有便宜的早期杀手实验；
6. 失败后能明确停止或收窄。

---

# P0：有限预算下的多势阱晶体结构搜索

## What

给定组成 \(A\)、物理条件 \((P,T)\) 与最多 \(B\) 次物理评估，输出一组弛豫后落入不同低能 basin 的候选：

\[
\mathcal S_B(A)=\{s_1,\ldots,s_K\}
\]

目标：

\[
J_B =
\mathbb E
\left[
\sum_j
w_j
\mathbf 1
\left(
\exists s_i\in\mathcal S_B:
R(s_i)\in\mathcal B_j
\right)
\right]
\]

而不是只最小化平均能量或恢复单个数据库 reference。

## Why

- 真实 CSP 是多峰搜索；
- 多晶型可能在能量上接近；
- 单参考 Match Rate 会把另一个合理 basin 判错；
- energy-only RL 会把概率集中到少数 evaluator 最优模式；
- 神经生成模型的真正价值应体现在相对传统搜索的 amortized efficiency。

## How

### 任务层

- 建立 polymorph-aware split；
- 定义弛豫后 basin；
- 统一 MLIP/DFT 调用预算；
- 报告 discovery curve，而非单个终点分数。

### 方法层

- 全局 proposal 分配不同 basin family；
- 连续生成器实现几何；
- basin archive 去重；
- set-level / reward-proportional / coverage-preserving 更新；
- 多保真 oracle 选择 DFT 查询。

## 最危险替代解释

更好的结果只来自：

- 更多候选；
- 更强 MLIP；
- 更积极的后筛选；
- 数据库原型检索；
- 宽松 basin 聚类。

## Killer experiments

1. **同预算传统搜索**：离子替换、原型检索、AIRSS/遗传搜索。
2. **energy-only 对照**：观察平均能量提高是否伴随 coverage 下降。
3. **弛豫后去重**：初始 diversity 是否全部坍缩到同一 basin。
4. **双 evaluator**：第二 MLIP/DFT 是否保持结果。
5. **预算曲线**：优势是否只存在于某个任意候选数。

## 早期停止条件

若简单原型/离子替换在相同物理预算下达到相同低能 basin 覆盖，则不应继续堆复杂生成器；应转向 OOD 组成、未知原型或 evaluator efficiency。

---

# P0：全局跨 basin 探索与局部物理修正的可辨识分解

## What

判断生成轨迹中的不同阶段和模块究竟负责：

- 改变最终 basin；
- 还是只在已选 basin 内降低力、应力和能量。

定义中间状态 \(S_t\) 与弛豫后 basin \(B\)。研究：

\[
I(S_t;B\mid A)
\]

以及分支熵：

\[
H(B\mid S_t,A)
\]

如何随时间变化。

## Why

如果无法区分 global search 与 local repair：

- “物理引导”可能只是一个 relaxer；
- 步骤级 reward 没有正确 credit；
- LLM 和 Diffusion 可能重复承担相同功能；
- 轨迹数据不会自动产生 CSP 搜索能力。

## How

1. 保存完整生成轨迹；
2. 从相同中间状态分支采样；
3. 对每个分支统一弛豫；
4. 聚类最终 basin；
5. 分别干预 lattice、坐标、离散结构假设；
6. 估计 basin commitment time；
7. 根据实证结果设计阶段特定向量场或 reward。

候选模型：

\[
v_t
=
v_{\mathrm{explore},t}
+
\alpha_t(S_t)
v_{\mathrm{repair},t}
\]

## Killer experiments

- 随机时间权重是否与设计权重相同；
- 去掉物理轨迹后 basin coverage 是否不变；
- 只使用外部 relaxer 是否达到相同最终结果；
- 中间状态对 basin 的预测性是否只来自 composition。

## 早期停止条件

若生成早期到晚期均没有稳定的 basin commitment 结构，或阶段职责跨组成完全不一致，则不要构造“早全局、晚局部”的强叙事；转向显式层级模型或搜索树。

---

# P0：Evaluator-robust 的生成与后训练

## What

在多个 MLIP 与 DFT 之间保持质量提升，而不是优化单一 evaluator：

\[
\max_\pi
\mathbb E_{\phi\sim p(\phi)}
U_\phi(\mathcal S)
-
\lambda\,\mathrm{Var}_{\phi}[U_\phi(\mathcal S)]
\]

其中 \(\phi\) 表示不同势模型或计算设置。

## Why

生成策略会主动寻找 evaluator 的高分区域，这些区域可能正是模型最不可靠的 OOD 区域。  
单一 MLIP 上的 reward 优化越成功，reward hacking 风险越高。

## How

- MLIP ensemble 与不确定性；
- 训练/选择 oracle 与最终审计 oracle 分离；
- disagreement-aware reward；
- 多保真 active learning；
- 对高 reward、高不确定候选优先做 DFT；
- 报告 evaluator rank correlation 与翻转率。

## Killer experiments

1. 换第二 MLIP 后排名是否翻转；
2. DFT 后改进是否消失；
3. reward 优化后模型不确定性是否显著上升；
4. 随机 OOD 候选是否也能骗取高分；
5. 固定生成样本，只换 evaluator 是否改变论文结论。

## 早期停止条件

若方法优势仅在训练 evaluator 上存在，应将工作重新定义为 evaluator calibration/active learning，而不是物理生成提升。

---

# P1：从“稳定终点数据”到“势能面信息”的学习

## What

确定非平衡构型、能量、力、应力和弛豫轨迹分别为生成提供什么新增信息：

\[
D =
D_{\mathrm{endpoint}}
\cup
D_{\mathrm{offeq}}
\cup
D_{\mathrm{trajectory}}
\]

## Why

稳定数据库只覆盖局部极小值附近，无法告诉模型：

- 错误结构怎样失败；
- 哪些方向降低力；
- 哪些扰动跨越 basin；
- 高能/高力区域中 oracle 是否可靠。

OMat24、LeMat-Traj 与 MP-ALOE 等数据使这一问题具备可执行性，但“更多轨迹”并不自动等于“更会搜索”。

## How

### 数据因子实验

控制样本数和计算量，对比：

- 稳定终点；
- 终点 + 随机噪声；
- 独立非平衡结构；
- 真实弛豫轨迹；
- energy only；
- energy + force；
- energy + force + stress。

### 评价

- 初始最大力；
- 弛豫步数；
- relaxer 成功率；
- basin 保持/改变率；
- OOD evaluator error；
- 独立低能 basin coverage。

## Killer experiments

若真实轨迹与随机噪声在等样本量下相同，轨迹故事不成立；  
若只改善局部力而不改善 basin coverage，应明确定位为预弛豫/几何修正。

## 早期停止条件

不能获得可信 trajectory/force 标签，或数据域与生成域严重不匹配时，不应以“物理轨迹生成”作为主线。

---

# P1：正确的生成目标分布是什么？

## What

晶体生成模型应拟合：

- 数据库分布 \(p_{\mathrm{db}}\)；
- 物理平衡分布 \(p_{\mathrm{phys}}\)；
- 低能多晶型上的人为目标分布；
- 还是固定预算最优搜索策略 \(\pi^*\)？

## Why

不同分布对应不同成功标准：

\[
p_{\mathrm{db}}
\neq
p_{\mathrm{phys}}
\neq
\pi^*_{\mathrm{search}}
\]

如果不定义目标分布：

- likelihood 没有明确物理解释；
- energy RL 容易坍缩；
- diversity reward 的温度任意；
- “覆盖真实材料空间”无法验证。

## How

### 候选形式化

低能 basin 上的 reward-proportional 目标：

\[
q(m_j\mid A)
\propto
R(m_j)
\]

或带温度的 free-energy 权重：

\[
q(m_j\mid A,P,T)
\propto
g_j\exp[-\beta G_j(P,T)]
\]

或面向发现的 utility distribution：

\[
q(m_j)
\propto
\exp[
\alpha\,\text{quality}
+
\eta\,\text{novelty}
+
\kappa\,\text{uncertainty}
]
\]

### 方法候选

- GFlowNet；
- entropy-regularized RL；
- archive reweighting；
- SMC/MCMC；
- set prediction；
- optimal experimental design。

## Killer experiments

在小型、低能 landscape 已较充分枚举的体系上，检验生成 basin 频率与定义目标的 KL/coverage；若目标分布不可验证，只能把工作表述为搜索启发式。

## 早期停止条件

若状态测度、简并度、温度或 basin 定义无法稳定确定，不应声称学习了 Boltzmann 分布；可退回“发现效用分布”。

---

# P1：动力学与有限温度稳定进入生成闭环

## What

从零温热力学代理扩展到：

- 局部动力学稳定；
- 有限温度自由能；
- 软模与相变；
- 必要时的动力学可达性。

## Why

低能、低 \(E_{\mathrm{hull}}\) 或几何有效并不保证无虚频。  
PhononBench 类工作显示，生成结果在动力学稳定性上仍有明显 attrition。

## How

多保真漏斗：

\[
\text{geometry}
\rightarrow
\text{energy/force}
\rightarrow
\text{phonon proxy}
\rightarrow
\text{DFT phonon}
\rightarrow
\text{finite-}T
\]

研究问题不是简单增加一个 PhononScore reward，而是：

- 何时查询二阶信息最划算；
- 哪些软模可由局部修正消除；
- 哪些对应新的相或对称破缺；
- 动力学 reward 是否与热力学和 diversity 冲突。

## Killer experiments

- 独立 DFT phonon；
- 不同超胞与收敛参数；
- 多 MLIP 排名；
- 有限温度 MD；
- reward 优化后的 OOD 与不确定性审计。

## 早期停止条件

若代理声子在 OOD 生成样本上不校准，不应把它直接用于 end-to-end RL；先做主动筛选和校准。

---

# P1：实验测量条件下的晶体后验采样

## What

给定组成和实验测量 \(y\)，从：

\[
p(s\mid A,y)
\propto
p_\theta(s\mid A)p(y\mid s,A)
\]

采样多个测量一致候选。

## Why

真实结构解析往往具有多解性；数据库 reference 只是一个观测。  
实验似然提供了比抽象“目标性质 condition”更明确的科学约束。

## How

- 预训练晶体 prior；
- 可微或近似可微 PXRD/PDF 前向模型；
- diffusion posterior sampling、SMC 或 variational posterior；
- 仪器噪声、峰展宽、取向和多相混合建模；
- posterior calibration 与 coverage。

## Killer experiments

- 合成数据上真后验覆盖；
- 多晶型不可辨识案例；
- 前向模型失配；
- 与传统 indexing/Rietveld/CSP 搜索比较；
- 真实盲测而非只做反演训练集。

## 早期停止条件

若模型只输出单一先验高概率结构、不能反映多解不确定性，应定位为 measurement-guided ranking，而非后验采样。

---

# P1：Science-preserving 的数据选择、配比与合成

## What

在有限训练预算下，如何提高数据效用而不删除科学上困难但必须保留的能力层：

\[
\max_{D'\subseteq D}
\text{learning utility}(D')
\quad
\text{s.t.}\quad
\mathrm{Coverage}_k(D')\ge c_k
\]

其中 \(k\) 表示氧化物、不同价态、空间群、低对称结构、高力区域等科学能力分层。

## Why

纯 AI 数据选择容易通过少选难样本提高平均分，却让模型丧失真实科学能力。  
例如氧化物难并不意味着应当少选氧化物，而可能意味着该层需要更多高价值数据。

## How

1. Science 定义不可丢能力层；
2. 每层内部用梯度、影响函数、不确定性或覆盖做选择；
3. 用 DFT/实验/受验证合成填补缺口；
4. 动态配比保证最坏层性能；
5. 报告 macro、worst-group 和能力保持，而非只报告 micro average。

## Killer experiments

- 按化学族/价态/原型的 worst-group；
- 移除难层后平均分提高但 OOD 崩溃；
- 合成数据是否改变真实 DFT 性能；
- 数据量控制下是否只是重复采样。

## 早期停止条件

若能力分层仅由模型聚类、无法对应科学语义，应避免强声称“science-aware”；先做可解释分层和专家审计。

---

# P2：真正的 self-improving scientific loop

## What

模型通过主动获得新的外部物理信息，而不是只把自己的生成结果再次 SFT：

\[
\text{Generate}
\rightarrow
\text{Relax}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Select DFT/experiment}
\rightarrow
\text{Update}
\]

## Why

固定 evaluator 上的自训练容易：

- 放大模型偏差；
- reward hacking；
- 降低分布覆盖；
- 把 on-policy RL 或 rejection-SFT 重新命名为自提升。

真正自提升需要获得此前未知的标签或反例。

## How

查询函数可结合：

\[
a(s)
=
\mu_{\mathrm{utility}}(s)
+
\kappa\sigma_{\mathrm{oracle}}(s)
+
\eta d(s,\mathcal A)
\]

其中：

- \(\mu\)：潜在低能/性质价值；
- \(\sigma\)：认知不确定性；
- \(d\)：相对 archive 的新 basin 或新结构距离。

## Killer experiments

- 同 DFT 预算下与随机查询、uncertainty-only、energy-only 比较；
- 每轮新发现 basin 数；
- oracle 校准是否改善；
- 是否只重复查询相同结构族；
- 增益是否来自累计数据量，而非选择策略。

## 早期停止条件

若没有外部高保真标签回流，使用“self-improving scientific discovery”需要谨慎；应称为 policy alignment 或 iterative filtering。

---

# 研究优先级建议

| 优先级 | 问题 | 首个最小实验 | 失败后的安全退路 |
|---|---|---|---|
| P0 | 有限预算多势阱 CSP | 固定组成的小规模 basin archive + 同预算基线 | 转向 benchmark / evaluator |
| P0 | 全局—局部分解 | 中间状态分支采样与 basin 熵 | 显式层级搜索 |
| P0 | evaluator robustness | 双 MLIP + 小批 DFT 排名 | 做校准/active learning |
| P1 | 轨迹数据价值 | endpoint/noise/trajectory 等量消融 | 定位为 pre-relaxer |
| P1 | 目标分布 | 可枚举小体系的 basin 频率 | discovery heuristic |
| P1 | 动力学稳定 | 分层 phonon 验证 | 只做筛选，不做 RL |
| P1 | 实验后验 | 合成 PXRD 多解测试 | measurement-guided ranking |
| P1 | Science-preserving data | 分层最坏组评估 | 数据审计工具 |
| P2 | 真正自提升闭环 | 等 DFT 预算 active query | iterative filtering |

---

## 当前建议的主线

首先集中在三个 P0 问题：

1. **任务重定义：** 单参考恢复 → 有限预算多势阱发现；
2. **机制重定义：** 全局模式分配 → 局部物理修正；
3. **证据重定义：** 单一 reward → evaluator-robust、多保真验证。

LLM、Diffusion、SI、GFlowNet 或 GRPO 都只能在这三个问题定义之后被选择。  
先有职责，再选工具；先有杀手实验，再投入训练。
