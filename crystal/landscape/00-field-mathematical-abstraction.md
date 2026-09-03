# 晶体生成领域的数学抽象：从故事到状态、数据、目标与证据

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

## 1. 为什么必须先形式化

“生成稳定的新晶体”包含至少四个彼此不同的问题：

1. 从数据库分布采样；
2. 给定组成恢复数据库参考结构；
3. 在多峰势能面上搜索多个低能局部极小值；
4. 在性质、实验或合成约束下设计候选。

如果不先区分，任何 benchmark 提升都可以被包装成“材料发现”，而模型真正学到什么无法判断。

---

## 2. 晶体不是普通欧氏向量

把晶体写成：

\[
s=(A,X,L)
\]

其中：

- \(A=(a_1,\ldots,a_N)\)：元素或原子种类；
- \(X=(x_1,\ldots,x_N)\in[0,1)^{N\times 3}\)：分数坐标；
- \(L\in\mathbb R^{3\times3}\)：晶格矩阵。

同一物理晶体可由不同表示给出，包括：

- 原子置换；
- 整体周期平移；
- 旋转；
- 周期镜像；
- 晶胞基变换；
- 超胞与原胞选择；
- 某些情况下的对称等价描述。

因此真实状态空间更接近商空间：

\[
\mathcal C =
\{(A,X,L)\}/\sim
\]

而不是 \(\mathbb R^d\)。

### 直接后果

- 普通坐标 RMSE 可能比较两个表示不同但物理等价的晶体；
- 序列模型必须处理表示非唯一性；
- 生成向量场必须尊重周期边界；
- “新结构”必须先排除等价晶胞和简单元素替换；
- lattice 参数化不是一个无关紧要的数值细节。

---

## 3. 五个不同任务

### 3.1 De novo generation

输入可为空或为性质条件 \(y\)：

\[
s\sim q_\theta(A,X,L\mid y)
\]

问题包括组成、原子数、晶格和坐标的联合建模。

科学目标可能是：

\[
\max_{s\sim q_\theta}
U(s;y)
\]

其中 \(U\) 应同时包含目标性质、稳定性、新颖性、多样性和验证成本。

### 3.2 固定组成结构恢复

给定 \(A\)，预测数据库中的参考结构：

\[
(\hat X,\hat L)\sim q_\theta(X,L\mid A)
\]

常见指标是 Match Rate、RMSD 或 top-\(K\) recovery。

这个任务回答的是：

> 模型能否根据数据库统计恢复一个已观测结构？

它不等同于完整 CSP，因为数据库只记录有限多晶型。

### 3.3 多晶型 / CSP 搜索

给定组成和物理条件：

\[
(A,P,T,B)
\]

其中 \(B\) 是能量、力、弛豫或 DFT 调用预算。

定义势能面：

\[
E_A(X,L)
\]

局部极小值集合：

\[
\mathcal M(A)
=
\left\{
m_j:
\nabla E_A(m_j)=0,\ 
\nabla^2 E_A(m_j)\succeq 0
\right\}
\]

低能窗口：

\[
\mathcal M_\Delta(A)
=
\{m_j\in\mathcal M(A):
E_A(m_j)-E_{\min}(A)\le \Delta\}
\]

真实输出是集合而非单点：

\[
\widehat{\mathcal M}_K(A)
=
\{R(s_1),\ldots,R(s_K)\}
\]

其中 \(R\) 是统一弛豫算子。

合理效用应衡量固定预算下覆盖多少个低能独立 basin：

\[
J_B(q)
=
\mathbb E_{s_{1:K}\sim q}
\left[
\sum_j w_j\,
\mathbf 1
\left(
\exists i:\ R(s_i)\in\mathcal B_j
\right)
\right]
\]

### 3.4 逆向材料设计

给定性质或约束 \(y\)：

\[
q_\theta(s\mid y)
\]

但真实设计是带约束、多目标、昂贵 oracle 的决策问题：

\[
\max_{\mathcal S: C(\mathcal S)\le B}
\sum_{s\in\mathcal S}
U(s)
\]

需要区分：

- 模型条件服从；
- 稳定性；
- 新颖性；
- oracle 不确定性；
- 可验证与可合成性。

### 3.5 实验约束的结构后验

给定组成 \(A\) 与 PXRD、PDF、谱学等测量 \(y\)：

\[
p(s\mid A,y)
\propto
p_\theta(s\mid A)
p(y\mid s,A)
\]

目标不是输出唯一结构，而是：

- 覆盖测量下可辨识的多个结构；
- 给出校准的不确定性；
- 处理前向模型误差与多相混合。

---

## 4. 四个容易混淆的分布

### 4.1 数据库分布

\[
p_{\mathrm{db}}(s)
\]

它由实验、DFT、筛选、收敛、发表和数据库纳入机制共同产生。

### 4.2 模型分布

\[
q_\theta(s)
\]

训练 likelihood 或 score 通常让它接近 \(p_{\mathrm{db}}\)，不是直接接近物理平衡分布。

### 4.3 物理分布

理想化地，在给定 \(P,T\) 下：

\[
p_{\mathrm{phys}}(s\mid P,T)
\propto
\mu(s)\exp[-\beta G(s;P,T)]
\]

其中 \(\mu(s)\) 涉及状态测度和简并度。

### 4.4 搜索策略分布

\[
\pi_\theta(s\mid A,B)
\]

它的目标是最大化有限预算下的发现效用，而非准确拟合数据库或 Boltzmann 分布。

### 核心警告

\[
p_{\mathrm{db}}
\neq
p_{\mathrm{phys}}
\neq
\pi^*_{\mathrm{search}}
\]

除非论文建立了额外条件，否则不能把“更好拟合数据库”解释成“更好理解势能面”。

---

## 5. 数据 score、物理 force 与弛豫轨迹不是一回事

扩散/score 模型学习：

\[
\nabla_s \log p_t(s)
\]

物理力是：

\[
F(s)=-\nabla_s E(s)
\]

弛豫器给出离散优化动力学：

\[
s_{k+1}
=
\Phi(s_k,F(s_k),\sigma(s_k),\text{optimizer})
\]

一般情况下：

\[
\nabla_s\log p_t(s)
\neq
-\nabla_s E(s)
\]

因为：

- 数据分布含选择偏差；
- score 随噪声时间 \(t\) 改变；
- 力取决于具体势能与物理条件；
- 优化轨迹还取决于优化器、预条件和晶胞约束。

### 研究含义

“Diffusion 去噪像弛豫”只能作为直觉，不能作为机制结论。  
若要声称物理修正，需要：

- 力/应力/轨迹监督；
- 对应的反事实消融；
- 弛豫步数或最大力下降；
- 更重要的是独立 basin 覆盖是否提高；
- 跨 MLIP/DFT 复核。

---

## 6. 组成、结构与 \(E_{\mathrm{hull}}\)

### 6.1 组成层

组成 \(c\) 决定：

- 化学系统；
- 允许的价态/电荷平衡；
- 竞争相集合；
- 凸包分解约束。

### 6.2 结构层

一个具体结构 \(s\) 的能量高于凸包为：

\[
E_{\mathrm{hull}}(s)
=
E(s)
-
\min_{\lambda_i}
\sum_i\lambda_iE_i
\]

满足：

\[
\lambda_i\ge0,\quad
\sum_i\lambda_i=1,\quad
\sum_i\lambda_i c_i=c(s)
\]

因此：

- 组成可查询已知相与参考凸包；
- 新生成结构的 \(E(s)\) 仍需 MLIP/DFT；
- 仅凭 composition 不能得到该结构的 \(E_{\mathrm{hull}}\)。

### 6.3 正确拆分

**组成合理性：**

- 电荷与价态；
- 元素兼容性；
- OOD 程度；
- 已知竞争相与化学系统先验。

**结构稳定性：**

- 弛豫收敛；
- 能量、力与应力；
- \(E_{\mathrm{hull}}\)；
- 声子/动力学稳定；
- 有限温度自由能。

---

## 7. 单点 reward 为什么与多势阱 CSP 冲突

常见后训练目标：

\[
\max_\theta
\mathbb E_{s\sim q_\theta}[r(s)]
-
\lambda D(q_\theta\Vert q_0)
\]

若：

\[
r(s)=-E(s)
\]

最优策略倾向把概率集中到 evaluator 认为最低的少数结构。

但 CSP 需要：

\[
\text{低能}
+
\text{不同 basin 覆盖}
\]

二者的冲突可写为：

\[
\max_q
\underbrace{\mathbb E_q[-E]}_{\text{质量}}
\quad\text{vs.}\quad
\max_q
\underbrace{H(B(R(s)))}_{\text{势阱覆盖}}
\]

简单样本级 diversity 也不充分，因为两个几何不同的初始结构可能弛豫到同一个 basin。

因此需要：

- 弛豫后聚类；
- archive；
- set-level reward；
- reward-proportional sampling；
- coverage-preserving policy update；
- 固定预算下的 discovery curve。

---

## 8. 一个有意义的 LLM + 连续生成分解

引入离散全局假设：

\[
z=
\text{coarse structural hypothesis / basin family}
\]

分解：

\[
p(X,L\mid A)
=
\sum_z
p_\psi(z\mid A)
p_\theta(X,L\mid A,z)
\]

只有在下列条件成立时，LLM/离散模型才有可辨识贡献：

\[
I(z;B_{\mathrm{final}}\mid A)>0
\]

并且：

\[
H(X,L\mid A,z)
<
H(X,L\mid A)
\]

实验上必须比较：

- 随机 \(z\)；
- 检索/原型 \(z\)；
- 规则 \(z\)；
- 小 Transformer；
- LLM；
- oracle basin label。

若 LLM 不超过检索和小模型，贡献应表述为序列建模或 warm start，而不是材料推理。

---

## 9. 全局探索与局部修正的可辨识分解

可设生成向量场：

\[
v_t(s)
=
v_{\mathrm{global},t}(s)
+
\alpha_t(s)v_{\mathrm{local},t}(s)
\]

其中：

- \(v_{\mathrm{global}}\)：在 basin family 之间迁移或保持多模态；
- \(v_{\mathrm{local}}\)：根据力/应力改进 basin 内几何；
- \(\alpha_t\)：由时间、模型不确定性或 basin commitment 决定。

必须通过干预验证，而不能预设：

1. 保存中间状态 \(S_t\)；
2. 对同一 \(S_t\) 分支采样多条后续；
3. 弛豫并标记最终 basin \(B\)；
4. 估计：

\[
H(B\mid S_t,A)
\]

5. 随 \(t\) 观察 basin branching entropy 是否下降；
6. 单独扰动 lattice、坐标和离散假设，测其因果影响。

只有当早期状态确实决定全局 basin、后期主要降低局部残差时，步骤级 reward 分工才有根据。

---

## 10. 数据是否包含要学习的信息

| 数据 | 提供的信息 | 不能直接提供 |
|---|---|---|
| 稳定结构终点 | 数据库结构分布、局部极小附近样本 | 跨 basin 路径、势垒、失败区域 |
| 终点加随机噪声 | 局部恢复任务 | 真实弛豫动力学 |
| DFT/MLIP 非平衡构型 | 能量、力、应力场局部信息 | 完整低能 basin 权重 |
| 弛豫轨迹 | 特定优化器下的修正过程 | 唯一物理动力学或全局搜索策略 |
| 生成 + reward | evaluator 偏好区域 | evaluator 外真实物理 |
| 实验结构 | 可实现结构证据 | 未记录失败、合成路径与完整相图 |
| 声子 | 局部二阶曲率 | 合成可达性与有限温度全部效应 |

数据选择必须由科学能力分层决定，不能通过删除难体系来制造平均分提升。

---

## 11. 评价器是模型的一部分

生成系统实际是：

\[
\text{proposal}
\rightarrow
\text{relaxation}
\rightarrow
\text{evaluator}
\rightarrow
\text{selection}
\]

因此最终表现可分解为：

\[
U =
U(\text{proposal},
\text{relaxer},
\text{evaluator},
\text{selector},
B)
\]

实验必须问：

- 提升来自更好 proposal，还是更强筛选？
- MLIP 是否对某模型分布更校准？
- 同一候选经第二 MLIP/DFT 后是否保持排序？
- 不同方法是否使用相同 oracle 次数？
- 后处理是否使用了测试组成或数据库信息？

---

## 12. 本领域的最小完整问题定义

一个成熟的晶体生成研究问题至少应写清：

```text
Scientific setting:
  composition / pressure / temperature / experimental constraint

State space:
  atom types / coordinates / lattice / symmetry quotient

Input:
  what information is available at inference time

Output:
  single structure / top-K / calibrated distribution / basin archive

Oracle:
  MLIP / DFT / phonon / experiment and uncertainty

Budget:
  samples / relaxations / force calls / DFT calls / wall-clock

Utility:
  energy, basin coverage, property, novelty, robustness

Data:
  endpoints / trajectories / off-equilibrium / failed samples

Generalization:
  in-distribution / composition OOD / prototype OOD / chemistry OOD

Falsification:
  strongest simple baseline and kill criterion
```

若这些字段缺失，方法名再新，也很难证明它解决了什么。
