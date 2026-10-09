---
title: "Stochastic Interpolants: A Unifying Framework for Flows and Diffusions"
slug: "stochastic-interpolants"
year: 2023
venue: "Foundational preprint / journal versions"
category: "cross-domain"
audit_role: "随机桥与生成统一框架"
paper_url: "https://arxiv.org/abs/2303.08797"
project_url: ""
last_verified: "2026-09-03"
---

# Stochastic Interpolants: A Unifying Framework for Flows and Diffusions

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

通过可设计的随机插值连接任意分布，统一确定性 flow 与随机 diffusion，并给出 drift/score 等可学习量。

出处：2023 · Foundational preprint / journal versions；cross-domain。

[论文](https://arxiv.org/abs/2303.08797)；首轮未核实项目入口。

首轮状态：已审计；基础理论持续演化

## 1. Scientific problem

Flow 与 diffusion 常被当成两套方法，缺少统一桥设计语言来控制随机性、端点分布与采样动力学。

## 2. Mathematical task

构造连接源分布和目标分布的随机过程，学习使其边缘分布成立的 drift、score 或相关场。

## 3. Data-generating process

理论分布及图像等实验；训练样本来自端点和插值噪声，而非真实物理轨迹。

## 4. Core mechanism

把 bridge、噪声调度与可逆/随机动力学置于统一公式中，使研究者可在 deterministic 与 stochastic 采样间连续选择。

## 5. Claim–evidence alignment

论文提供理论恒等式、训练目标和实验，说明多类 flow/diffusion 可视为特例。

## 6. Hidden assumptions

插值族足以覆盖目标路径；可学习场的估计误差和数值误差可控；选择的 bridge 符合任务。

## 7. Strongest alternative explanation

实际收益可能来自特定 bridge/solver，而非统一理论本身；在应用中“用了 SI”常只是重新参数化已有路径。

## 8. Missing baseline

相同端点、网络和 NFE 下的 diffusion/flow；不同 bridge 的消融；与任务结构匹配的可预测性指标。

## 9. Killer experiment

若晶体应用只替换损失名称、未改变 base/bridge/随机性且效果可由调参解释，则 SI 没有独立贡献。

## 10. Contribution type

它提供新的数学坐标系，属于开山式机制框架；应用论文的价值取决于是否提出任务特有 bridge。

首轮角色：随机桥与生成统一框架。历史六维记录：[2, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

对晶体最有价值的是设计 global-proposal → low-energy-basin 的混合桥，以及随 basin commitment 调节随机性。

## 12. Final verdict

基础价值很高，但“SI for crystals”已不是新意；不能把统一框架本身冒充领域科学贡献。

首轮使用建议：将其作为实现候选，而把贡献放在多势阱目标、bridge 设计和可证伪的全局/局部分工。

具体结论范围：不能把插值轨迹解释为真实势能弛豫，也不能假设随机性越大就越能覆盖多晶型。

### 首轮留下的后续问题

构造 global/local mixture base，测量不同桥下的 basin transition matrix、coverage—energy Pareto 与采样成本。
