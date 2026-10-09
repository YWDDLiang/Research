---
title: "Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards"
slug: "b2-diffurl"
year: 2025
venue: "CVPR 2025"
category: "cross-domain"
audit_role: "稀疏奖励 / 分支探索"
paper_url: "https://arxiv.org/abs/2503.11240"
project_url: ""
last_verified: "2026-09-03"
---

# Towards Better Alignment: Training Diffusion Models with Reinforcement Learning Against Sparse Rewards

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

通过反向渐进训练与分支采样改善扩散模型面对稀疏终点奖励时的探索和信用分配。

出处：2025 · CVPR 2025；cross-domain。

[论文](https://arxiv.org/abs/2503.11240)；首轮未核实项目入口。

首轮状态：已审计；会议论文

## 1. Scientific problem

终点 reward 稀疏且高方差，完整轨迹采样昂贵，常规策略梯度难确定哪些中间决策值得保留。

## 2. Mathematical task

在扩散轨迹的不同位置分支采样多个后续结果，并渐进地把 reward 信号向更早时间传播。

## 3. Data-generating process

预训练图像扩散、稀疏 reward 与分支采样轨迹。

## 4. Core mechanism

用共享前缀的反事实分支估计中间状态价值，再按反向课程逐步扩展优化区间。

## 5. Claim–evidence alignment

论文报告在若干对齐目标上提高稀疏 reward 优化效率和结果质量。

## 6. Hidden assumptions

共享前缀分支能近似中间状态价值；额外样本成本可接受；图像 reward 可靠。

## 7. Strongest alternative explanation

收益可能只是更多 best-of-N 样本或课程训练；分支数增加带来的计算优势需公平折算。

## 8. Missing baseline

相同生成调用数的 best-of-N、rejection、Monte Carlo value、stepwise credit 与普通 GRPO。

## 9. Killer experiment

在严格等采样/评估预算下若简单分支重排达到同效，则算法更新本身没有独立价值。

## 10. Contribution type

它提供稀疏奖励下的反事实分支和反向课程思想，属于优化机制增量。

首轮角色：稀疏奖励 / 分支探索。历史六维记录：[1, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

晶体生成的分支弛豫天然昂贵但有物理含义，可用于判断某中间状态是否已经承诺到某个 basin。

## 12. Final verdict

可作为 basin commitment 诊断工具；直接套用做 energy reward RL 的新颖性和科学性都不足。

首轮使用建议：用于设计共享早期轨迹、后续多分支弛豫的实验，以测量搜索树中何时发生势阱分叉。

具体结论范围：不能把更多分支带来的搜索预算收益误写成模型学习收益。

### 首轮留下的后续问题

对同一中间晶体状态采样多个后续并弛豫，估计 basin branching entropy 随时间的变化，再决定是否训练。
