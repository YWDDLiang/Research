---
title: "GFlowNet Foundations"
slug: "gflownet-foundations"
year: 2023
venue: "Journal of Machine Learning Research"
category: "cross-domain"
audit_role: "多模态奖励比例采样"
paper_url: "https://jmlr.org/papers/v24/22-0364.html"
project_url: ""
last_verified: "2026-09-03"
---

# GFlowNet Foundations

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

建立生成流网络的理论基础，使组合对象按未归一化奖励比例采样，而不是只寻找单一最优对象。

出处：2023 · Journal of Machine Learning Research；cross-domain。

[论文](https://jmlr.org/papers/v24/22-0364.html)；首轮未核实项目入口。

文献状态：基础方法论文

## 1. Scientific problem

黑盒奖励优化倾向模式坍缩，但科学发现常需要从多个高奖励模式采样并估计多解分布。

## 2. Mathematical task

在有向构造图上学习前向/后向流，使终止对象的边缘概率与正奖励成比例。

## 3. Data-generating process

组合对象构造轨迹、终点奖励；可用 off-policy 采样与不同 flow consistency 目标训练。

## 4. Core mechanism

把局部构造转移的流守恒与终点奖励连接，令多个生成路径的流量聚合到对象概率。

## 5. Claim–evidence alignment

理论与多类组合任务支持 reward-proportional sampling，并解释 trajectory balance 等训练目标。

## 6. Hidden assumptions

状态构造图无有害环或可适配；奖励为正且足够可靠；不同轨迹汇聚到同一对象时可正确归一。

## 7. Strongest alternative explanation

在连续高维晶体中，离散构造和终点归一困难；观察到的多样性也可能来自温度/熵正则，而非 flow matching。

## 8. Missing baseline

熵正则 RL、top-k/quality-diversity、MCMC、archive sampling，以及相同 oracle 预算下的覆盖比较。

## 9. Killer experiment

若在同一 reward 与预算下简单温度采样/质量多样性算法达到相同 basin 分布，GFlowNet 的额外复杂度没有必要。

## 10. Contribution type

它改变了优化目标：从 argmax 转为与 reward 成比例的多模态采样，是多解科学设计的重要抽象。

工作定位：多模态奖励比例采样。六维贡献描述：[2, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

晶体中可把离散全局结构假设或 basin archive 作为对象空间，但连续坐标、弛豫后归并和不确定 reward 需新方法。

## 12. Final verdict

基础思想非常契合多晶型发现，但直接套用并不构成贡献；无机晶体的混合离散—连续、等价性和多保真问题才是难点。

研究参考：作为 energy-only GRPO 的替代目标候选，用于保持低能 basin 的概率覆盖。

具体结论范围：不能声称 reward-proportional 就等于 Boltzmann 物理分布，除非 reward、温度和状态测度有严格定义。

### 相关研究问题

在已知多盆地的小体系上比较 GFlowNet、熵正则 RL、archive reweighting 对目标 basin 分布的 KL 与发现效率。
