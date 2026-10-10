# R3｜物理后果条件化的原生动作学习

[候选方法](README.md) · [共同评价](../evidence/common-protocol.md) · [文献来源](../evidence/sources-r3.json)

研究假设，尚无该方法的独立实验结果。固定同一候选和物理数据池，研究带原子与时间结构的后果信息，能否比终点标量更有效地学入普通独立生成器。

## 1. 科学问题与近邻

[GSS](https://arxiv.org/html/2604.27636v1)与[OMatG-IRL](https://proceedings.mlr.press/v306/hollmer26a.html)已用物理信息改善搜索或CSP。[OMatGRPO](https://arxiv.org/html/2610.03880v1)直接更新物种通道；[CrystAF](https://arxiv.org/html/2609.36398v1)与[PackFlow](https://arxiv.org/html/2602.20140v1)已做分子晶体物理后训练。[ANCHOR](https://arxiv.org/html/2609.33407v1)还使用搜索访问组成的结构语料训练条件模型。

这一候选方法利用同样物理计算中的过程信息，学习后果条件化动作，再投影到只看当前状态的生成器。它研究有限数据中的信息利用；特权教师自蒸馏已有[SDPO](https://arxiv.org/html/2601.20802v2)先例。

## 2. 状态、原生动作与信息

OMatG的联合物种、周期坐标与晶胞提供候选接口。对坐标SDE、masked-species DFM、cell ODE的配置，状态为 \(s_t=(N,A_t,X_t,L_t,t)\)。可学残差改变坐标drift和物种logits；denoiser、扩散强度、event时钟及cell规则保持一致。新的坐标/物种仍会影响后续cell响应。

从共同parent采有限原生block并记录实际子步。第j个branch的内部状态为 \(s_{b,j,i}\)，物理后果为 \(Y_{b,j}\)；只有起点i=0共享状态。各branch继续完整生成，再按共同物理协议评价。

Y包括raw力/应力、松弛节点的响应与相对能量、raw到松弛终点的位移和相对应变、终点hull与新颖资格。后果保留未知字段。完整未来动作、随机数和绝对终点坐标不作为教师输入；松弛位移也不是native第一步动作。无位移的过程信息对照可区分响应知识与几何复制。

## 3. 受限动作教师与学生投影

教师 \(T_\psi(a\mid s,Y)\)以实际配对动作训练：
\[
L_T=-\mathbb E_{s,a,Y}\log T_\psi(a\mid s,Y).
\]
坐标教师与学生采用同协方差Gaussian mean，species概率在实际unmask支持上训练。cell是共同确定性规则，不添加虚构的cell Gaussian likelihood。原子响应与global stress/energy token进入条件adapter；普通学生只看s。

同parent已知后果按低hull、新颖性utility形成权重，并保留统一回放。rich与scalar比较共享终点字段、权重、容量、回放及动作族，rich额外看到已付费过程信息：
\[
L_S=\mathbb E_b\sum_j w_{b,j}\frac{1}{m_j}
\sum_i {\rm KL}[T_\psi(\cdot\mid s_{b,j,i},Y_{b,j})
\Vert \pi_\theta(\cdot\mid s_{b,j,i})]+\lambda L_{\rm base}.
\]
内部状态只使用自身后果。共享起点可混合不同Y，其Gaussian坐标投影的最优mean为
\[
\mu_S=\sum_j w_j\mu_j .
\]
它可能平均不同有用方向；有限族投影与一般多峰后验并不等价。

理想共享状态下，参考联合分布按 \(\exp(r(Y)/\tau)\)倾斜可产生
\[
\pi_{\rm target}(a\mid s)\propto
\pi_0(a\mid s)\mathbb E[\exp(r(Y)/\tau)\mid s,a].
\]
这是条件指数矩，不是 \(\exp(\mathbb E[r\mid s,a]/\tau)\)，也不直接等同冻结续程的expected-reward最优。该关系解释候选信息目标；真实训练是带后果条件的轨迹加权蒸馏。

## 4. 需要建立的科学结果

主机制比较为同池同权重的rich/scalar学生，以及同futures的直接动作BC或soft targets。endpoint SFT和NFT是其它学习对象对照，不因共用评分就成为同损失。

新的共同后续区分选Y教师、共享起点mean投影及学生的实际收益；独立新seed的严格SUN和不同低能类才建立知识摊销。若教师只重建旧动作，或投影平均掉了有效选择，相应结果应解释能力限制。过程信息对比保留真实力/应力及响应，不增加候选数量来解释收益。

该候选保留原生接口，并在采样时移除特权反馈。更广的物理机会、响应关系及跨请求知识问题见[C](../programs/c-physics-to-knowledge.md)。
