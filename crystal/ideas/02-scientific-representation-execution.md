# R2｜对象绑定与物理响应保持的生成接口

[候选方法](README.md) · [共同评价](../evidence/common-protocol.md) · [文献来源](../evidence/sources-r2.json)

研究假设，尚无该方法的独立实验结果。中心问题是元素、轨道和局部关系怎样成为精确的周期几何，区分科学选择、对象传递与连续执行的作用。

## 1. 科学问题与近邻

[CrysLLMGen](https://arxiv.org/html/2510.23040v1)连接语言生成与固定元素精修；[CrystalReasoner](https://arxiv.org/html/2605.14344v1)使用科学描述及终态奖励；[CrystalREPA](https://arxiv.org/html/2605.08960v1)将MLIP原子特征迁入生成表示。[Composable Crystals](https://arxiv.org/html/2605.14769v1)和[UFO-MGen](https://arxiv.org/html/2609.26547v1)已有局部概念与离散—连续分工。

对象条件可以有用，也可能忠实执行了不合适的关系。研究假设是：同样的科学信息和物理监督下，保留字段所有者及方向响应的接口能更可靠地实现新的化学—结构组合。

## 2. 科学对象与条件实现

CrystalFormer的真实序列为 \(g-(W_i-A_i-X_i)_n-L\)，适合观察站点交错与连续执行；PLaID++式Wyckoff生成提供另一类条件入口。模型选择需保留继承训练曝光。Alex20s的20-site范围指常规胞Wyckoff sites，不应直接解释为20原子。

\[
O=(g,\{(i,W_i,M_i,A_i)\}_{i=1}^{m}),\qquad
y=(\ell,\xi_1,\ldots,\xi_m),\qquad x=\Phi_O(y).
\]
\(\xi_i\)是轨道自由坐标，\(\ell\)是相容晶格参数，\(\Phi_O\)展开空间群对象。给定O可以有多个实现，关系要求仍可能不相容。

新增轨道局部字段 \(S_i\)描述按邻居元素分组的近邻计数、径向bin和低阶配位形状；轨道对字段 \(R_{ij}\)保留接触重数与粗距离。周期跨胞接触参与标签，计数可满足 \(M_i n_{ij}=M_j n_{ji}\)。粗字段保留多种连续实现，避免把完整坐标包装成条件。

连续完成分布可写为
\[
q_\phi(y\mid C,y^0)
=q_\phi(\ell\mid C,y^0)\prod_iq_\phi(\xi_i\mid\ell,C,y^0,\xi_{<i}),
\qquad C=(O,S,R).
\]
原生几何提供draft \(y^0\)，对象node/pair消息明确路由到相应自由度，多模态周期head保留不同实现。

## 3. 关系执行与响应监督

真实结构解析为 \(O^*,y^*,S^*,R^*\)，draft仅作为条件。联合结构分布及完成分布以真实目标监督：
\[
L_{\rm gen}=-\log p_\theta(O^*,S^*,R^*,y^*)
-\log q_\phi(y^*\mid C^*,y^0).
\]
平滑周期邻域算子 \(Q_i,Q_{ij}\)比较解码结构与所属对象的要求，形成 \(L_{\rm bind}\)。自主生成前缀由其完整物理后果更新，不能把任意不相容前缀强配到参考后缀。

在自由坐标和相容应变方向 \(\delta\)上，冻结保守MLIP给出
\[
\Delta_\delta^\pm E(y)
=\frac{E_\psi(\Phi_O(y\pm\epsilon\delta))-E_\psi(\Phi_O(y))}{N},\quad
R_\delta(y)=(\Delta_\delta^+E,\Delta_\delta^-E),
\]
\[
L_{\rm resp}=\mathbb E_\delta\|R_\delta(\hat y)-R_\delta(y^*)\|^2 .
\]
方向按Cartesian位移或无量纲应变归一；奇分量反映方向力/应力，偶分量反映局部曲率。近乎平衡时，偶响应仍可区分软硬几何。总体为生成、绑定和响应三类监督；同teacher特征对齐是直接近邻对照。

## 4. 需要建立的科学结果

主要比较共享O/S/R/draft、完成容量、输出族、chart及 \(\Phi_O\)，改变对象专属路由或物理响应监督。真实可实现条件与模型预测条件的交叉结果定位选择和执行；owner变化限于实际可实现且计数相容的关系配置。

结构相近时，观察方向响应差异是否解释物理转化；在新的化学—轨道组合中，再检验自主生成的终态严格SUN、U/N和不同低能类。继承曝光、局部响应范围、特殊位置的组成变化及松弛后的对称破缺分别记录。

该候选学习对象执行接口。局部知识如何跨周期整体组合见[B](../programs/b-compositional-feasibility.md)，共同形成的表示问题见[A](../programs/a-coformation.md)。
