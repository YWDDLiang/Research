# 从 CV 与通用 AI 到晶体：迁移的是数学原语，不是方法名称

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

## 1. 跨领域迁移的判定标准

一个跨领域方法 \(A\) 迁移到晶体任务 \(B\)，不能只因为二者都使用“生成”“轨迹”或“反馈”。

至少要建立以下映射：

\[
(\mathcal X_A,\mathcal Y_A,\mathcal L_A,\mathcal O_A)
\longrightarrow
(\mathcal X_B,\mathcal Y_B,\mathcal L_B,\mathcal O_B)
\]

其中：

- \(\mathcal X\)：状态空间；
- \(\mathcal Y\)：目标对象；
- \(\mathcal L\)：训练/优化目标；
- \(\mathcal O\)：可用 oracle 与观测。

有效迁移应回答：

1. 两个领域共享的困难是什么？
2. 原方法利用的结构在晶体中是否存在？
3. 哪个变量对应哪个变量？
4. 哪个假设在晶体中最可能失败？
5. 什么实验能区分“数学机制有效”和“换 backbone 提分”？

---

## 2. 核心迁移矩阵

| 通用方法 | 真正可迁移的数学原语 | 晶体中的合理映射 | 最常见误用 | 决定性实验 |
|---|---|---|---|---|
| Flow Matching | 设计源分布、概率路径和向量场回归 | 设计 crystal base、晶格/坐标路径、basin-conditioned transport | 把 ODE 向量场解释为物理力 | 同 backbone/NFE 只换路径，测路径长度、basin coverage 和 DFT |
| Riemannian Flow Matching | 在内在几何和切空间中生成 | torus 分数坐标、晶格流形、乘积状态空间 | “流形一致”直接等于“物理一致” | 与 wrapped Euclidean、等价晶胞归一化比较边界伪影 |
| Stochastic Interpolants | 可设计随机 bridge，统一 flow/diffusion | global proposal 与 low-energy basin 之间的混合桥 | 只换训练损失名称就声称新范式 | 固定端点/网络，消融 bridge 与随机性，测 basin transition |
| MaskGIT | 置信度驱动的并行迭代离散修正 | 元素、结构 token、粗结构假设的并行重掩码 | 直接套用“早全局、晚细节”图像叙事 | token/轮次干预对最终 basin、lattice、局部环境的影响 |
| GFlowNet | 按 reward 比例而非 argmax 采样多模式 | 低能 basin、离散结构假设或构造图上的概率分配 | 把任意 reward-proportional 分布称为 Boltzmann | 已知 landscape 上比较目标 basin 频率 KL 与等预算 QD/RL |
| Diffusion Posterior Sampling | 生成先验 + 测量 likelihood | \(p(s\mid A,\mathrm{PXRD/PDF})\) | 把单个 measurement-guided 解称为完整后验 | 合成多解数据上的 coverage、calibration 与模型失配 |
| DDPO / policy gradient | 直接优化不可微下游 reward | 晶体候选的性质、稳定性或集合效用 | reward 提升等于科学理解 | 冻结独立 evaluator、同预算 rejection、diversity/basin 审计 |
| Stepwise credit | 给轨迹不同阶段分配不同优势 | 根据 basin commitment 与力下降分配阶段 reward | 未验证就假设早期决定晶格、后期决定坐标 | 中间状态分支采样、时间干预和因果 credit 对比 |
| B²-DiffuRL / branching | 共享前缀的反事实分支估计状态价值 | 从同一中间晶体状态产生多后续并弛豫 | 把更多分支预算的收益归因于学习 | 严格等 oracle/采样预算，与 best-of-N 和 value baseline 比较 |
| Active learning | 用不确定性与价值选择昂贵标签 | 主动选择 DFT/phonon/实验查询 | 只对模型最喜欢的样本做 DFT，放大偏差 | 等 DFT 预算下与随机、uncertainty-only、energy-only 比较 |
| Quality-Diversity | 质量与行为描述符覆盖同时优化 | 低能 + 不同 basin / topology / coordination | 用任意指纹距离代替真实 basin | 弛豫后 archive、描述符敏感性和 DFT 去重 |
| Mixture-of-Experts | 条件路由到不同局部专家 | 不同化学族、结构家族或 basin 专家 | 路由只是增加参数，专家没有分工 | expert swap、routing intervention、OOD family 测试 |
| Hierarchical generative models | 离散全局变量 + 连续局部变量 | \(p(z\mid A)p(X,L\mid A,z)\) | \(z\) 是不可解释 latent，无法证明减少多峰难度 | \(I(z;B\mid A)\)、随机/检索/small model/oracle \(z\) |
| Diffusion Schrödinger bridges | 在参考动力学下最小控制代价运输 | 从 proposal 分布到物理筛选分布的受控桥 | 把参考扩散当真实原子动力学 | 控制代价、路径可解释性和真实弛豫轨迹对照 |
| Energy-based modeling | 用能量定义未归一化密度 | MLIP/DFT 能量与生成 prior 的联合分布 | 直接用 \(e^{-\beta E}\) 忽略状态测度与简并度 | 可枚举体系的 basin weight、温度和测度敏感性 |

---

## 3. Flow Matching：问题不在“Flow 还是 Diffusion”

### 3.1 真正自由度

Flow Matching 的核心自由度是：

- base distribution \(p_0\)；
- target distribution \(p_1\)；
- conditional path \(p_t(x\mid x_0,x_1)\)；
- vector field parameterization；
- numerical solver。

晶体研究应问：

\[
\text{哪个 }p_0\text{ 和 bridge 让目标运输更短、更可分解？}
\]

而不是：

> Flow 是否普遍优于 Diffusion？

### 3.2 有意义的晶体 bridge

可能的 base：

\[
p_0
=
\lambda p_{\mathrm{global\ proposal}}
+
(1-\lambda)p_{\mathrm{local\ perturbation}}
\]

目标：

\[
p_1 =
p_{\mathrm{low-energy\ basin}}
\]

其中：

- global proposal 覆盖不同粗结构模式；
- local perturbation 学习 basin 内修正；
- bridge 的随机性可随 basin commitment 改变。

### 3.3 必须测什么

- 运输路径长度；
- NFE；
- solver error；
- 最终 basin entropy；
- 低能 basin coverage；
- 局部最大力；
- 跨 MLIP/DFT 稳健性。

---

## 4. Stochastic Interpolants：价值在 bridge design

SI 允许：

\[
X_t=I(t,X_0,X_1)+\gamma(t)Z
\]

应用论文只有在 \(I\) 或 \(\gamma\) 反映晶体任务结构时才有新意。

### 合理问题

- 何时需要随机性保持跨 basin 探索？
- 何时应降低随机性进行局部修正？
- 晶格和坐标是否应使用不同 bridge？
- 离散元素/结构假设与连续几何如何耦合？
- bridge 是否可利用真实非平衡轨迹而不把它误作唯一物理路径？

### 无效迁移

- 将标准线性插值换名为 SI；
- 与不同 backbone 的 diffusion 比较；
- 只报告 SUN，不分析 bridge；
- 把插值过程解释成势能下降。

---

## 5. MaskGIT / DLM：先验证 token 的物理职责

图像中的 token 具有网格位置和视觉层级。晶体 token 可能包括：

- 元素；
- 原子数；
- lattice；
- 空间群/Wyckoff；
- 坐标；
- 局部环境；
- 粗拓扑。

但它们的依赖结构不同。

### 需要估计的量

第 \(k\) 类 token \(Z_k\) 对最终 basin \(B\) 的条件信息：

\[
I(Z_k;B\mid A,Z_{<k})
\]

以及 token 干预造成的结果变化：

\[
\Delta_k =
\mathbb E[
d(R(s),R(s^{\mathrm{intervene}(k)}))
]
\]

### 合理的研究问题

- lattice token 是否少但具有高因果影响？
- 空间群 token 是否提高下限却限制破缺模式？
- 并行重掩码是否增加多晶型覆盖，还是只加速采样？
- 置信度是否与物理错误相关？
- segment-level reward 是否比 token-level reward更符合晶体等价性？

### 危险基线

- 随机重掩码；
- 固定顺序；
- 小型 non-LLM Transformer；
- 相同 tokenization 的 AR；
- 相同 NFE 的离散 diffusion。

---

## 6. GFlowNet / Quality-Diversity：多解目标比平均 reward 更重要

### 6.1 为什么适合 CSP

CSP 希望发现多个高质量模式：

\[
q(m_j\mid A)\propto R(m_j)
\]

而不是：

\[
q(m_j\mid A)\rightarrow\delta_{j=j^*}
\]

### 6.2 无机晶体中的新难点

- 状态同时含离散与连续变量；
- 多条生成路径对应同一等价晶体；
- basin 身份通常在弛豫后才知道；
- reward 来自不确定、多保真 oracle；
- 低能结构全集未知；
- 可变原子数与晶胞造成构造图复杂；
- 结构指纹距离不等于 basin。

### 6.3 可能的两层方案

\[
p(z,s\mid A)
=
p_{\mathrm{GFN}}(z\mid A)
p_\theta(s\mid A,z)
\]

- GFlowNet/Quality-Diversity 负责离散结构家族或 archive；
- 连续生成器负责几何实例化；
- 弛豫结果反馈到 \(z\) 的 reward 与新颖性。

### 6.4 决定性实验

在可充分枚举的小体系上比较：

- target basin distribution；
- unique low-energy basin per oracle call；
- mode dropping；
- reward calibration；
- GFlowNet vs entropy-RL vs archive replay vs random/QD。

---

## 7. Diffusion Posterior Sampling：从“性质条件”走向实验问题

### 7.1 科学接口

先验：

\[
p_\theta(s\mid A)
\]

实验似然：

\[
p(y\mid s,A)
\]

后验：

\[
p(s\mid A,y)
\propto
p_\theta(s\mid A)p(y\mid s,A)
\]

### 7.2 适合的测量

- powder XRD；
- pair distribution function；
- 局部配位或谱学摘要；
- 部分晶格参数；
- 多模态组合。

### 7.3 真正难点

- 峰位/峰强的非线性；
- 仪器展宽和取向；
- 多相混合；
- 前向模型系统误差；
- 多晶型不可辨识；
- 晶胞等价和排列；
- 后验 calibration。

### 7.4 不能做的故事跳跃

“重建误差低”不等于“后验正确”。  
需要报告：

- posterior coverage；
- calibration；
- multiple plausible modes；
- measurement consistency；
- prior sensitivity；
- real blind test。

---

## 8. RL：优化器不是研究问题

### 8.1 先定义 reward 的数学对象

样本级：

\[
r(s)
\]

轨迹级：

\[
R(\tau)
\]

集合级：

\[
R(\mathcal S)
\]

basin archive 级：

\[
R(\mathcal A)
\]

这些目标不可互换。

### 8.2 晶体中的合理 credit

若中间状态 \(S_t\) 已经决定最终 basin，则早期 credit 应与 coverage 或 basin choice 相关；  
若晚期只降低局部力，则晚期 credit 应与物理修正相关。

可以写为：

\[
A_t
=
\lambda_t A_t^{\mathrm{basin}}
+
(1-\lambda_t)A_t^{\mathrm{local}}
\]

但 \(\lambda_t\) 必须由轨迹干预实证，而不是手工故事。

### 8.3 RL 必须与简单搜索比较

相同 oracle 预算下比较：

- rejection sampling；
- best-of-\(N\)；
- reward-weighted SFT；
- archive replay；
- evolutionary search；
- entropy-regularized RL；
- GRPO/DDPO；
- inference-time branching。

若简单采样和筛选达到同效，训练模型的必要性不足。

---

## 9. Active learning：真正的“自提升”接口

### 9.1 固定 evaluator 的循环

\[
\text{generate}
\rightarrow
\text{score}
\rightarrow
\text{SFT/RL}
\]

只会更适应已有 evaluator。

### 9.2 获取新知识的循环

\[
\text{generate}
\rightarrow
\text{estimate uncertainty}
\rightarrow
\text{query DFT/experiment}
\rightarrow
\text{update oracle/generator}
\]

查询可综合：

\[
a(s)
=
\mu_{\mathrm{value}}(s)
+
\kappa\sigma_{\mathrm{epistemic}}(s)
+
\eta d(s,\mathcal A)
\]

### 9.3 评价

- 每个 DFT 查询的新 basin 数；
- oracle calibration；
- worst-group error；
- OOD 覆盖；
- generator quality；
- 查询冗余率；
- 跨轮累积成本。

---

## 10. 跨领域论文应该怎样读

对每个 CV / AI 方法，新增以下五个问题：

1. 原论文中的对象和对称性是什么？
2. 性能来自数学原语、数据规模还是工程？
3. 晶体中是否存在相同的结构性困难？
4. 映射后哪个原假设失效？
5. 最小区分实验是什么？

### 示例：错误与正确的迁移表达

**错误：**

> CV 中 stepwise GRPO 有效，所以在晶体 diffusion 每一步加入 reward。

**正确：**

> 终点 reward 的统一 credit 在晶体轨迹中可能错误。先通过中间状态分支采样估计各时间步对最终 basin identity 和局部力的因果贡献；若阶段分工成立，再构造与该贡献匹配的 stepwise advantage。

---

## 11. 当前最有潜力的跨领域组合

### 组合 A：层级 proposal + basin archive + continuous generator

\[
p(z\mid A)
\cdot
p_\theta(X,L\mid A,z)
\]

- 离散模型/GFlowNet：模式分配；
- Flow/SI：模式内几何；
- archive：弛豫后去重；
- active learning：高不确定 basin 的 DFT 查询。

### 组合 B：trajectory intervention + adaptive stochasticity

- 用分支轨迹估计 basin commitment；
- 早期保持较强随机性；
- 后期加入 force/stress repair；
- stochastic schedule 由实证阶段职责决定。

### 组合 C：experimental posterior + CSP prior

- 生成模型提供结构 prior；
- PXRD/PDF 提供 likelihood；
- posterior sampling 输出多解；
- DFT/实验闭环缩小不确定性。

### 组合 D：science-preserving curriculum + multi-fidelity oracle

- 科学能力层定义不能删除的 coverage；
- 层内用 data utility 选择；
- 用 DFT/轨迹补齐缺口；
- 评价 worst-group 和 discovery utility。

---

## 12. 组合被允许进入项目的门槛

每个 A+B 方案需要填写：

```text
A 的输入/输出：
B 的输入/输出：
接口变量 Z：
I(Z; Y | X) 的可测代理：
H(Y | X, Z) 降低的证据：
A 的最简单替代：
B 的最简单替代：
独立职责：
共享预算：
杀手实验：
停止条件：
```

没有这些字段的组合，只能进入 watchlist，不能进入主方法。
