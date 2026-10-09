---
title: "Training Diffusion Models with Reinforcement Learning"
slug: "ddpo"
year: 2023
venue: "ICLR 2024"
category: "cross-domain"
audit_role: "扩散策略优化"
paper_url: "https://arxiv.org/abs/2305.13301"
project_url: "https://github.com/jannerm/ddpo"
last_verified: "2026-09-03"
---

# Training Diffusion Models with Reinforcement Learning

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把扩散去噪过程视作多步决策过程，直接用下游奖励对生成策略进行策略梯度优化。

出处：2023 · ICLR 2024；cross-domain。

[论文](https://arxiv.org/abs/2305.13301) · [官方/作者项目](https://github.com/jannerm/ddpo)

首轮状态：已审计；基础后训练方法

## 1. Scientific problem

最大似然/去噪目标不等同于不可微下游 reward，需要直接优化人类偏好或任务评价器。

## 2. Mathematical task

将每个去噪转移视为策略动作，以终点 reward 估计策略梯度，并保持与预训练生成分布的约束。

## 3. Data-generating process

预训练文生图扩散、图像 reward 模型或可计算目标，以及采样轨迹。

## 4. Core mechanism

推导 denoising diffusion policy optimization，把终点黑盒 reward 反传为多步策略更新。

## 5. Claim–evidence alignment

论文展示在可计算目标与偏好 reward 上可显著提高终点分数，也揭示 reward overoptimization 风险。

## 6. Hidden assumptions

reward 对真实目标可靠；策略梯度方差可控；预训练先验和正则足以防坍缩；状态转移可按 MDP 处理。

## 7. Strongest alternative explanation

提升可能是 evaluator hacking、prompt-specific 过拟合或多样性丧失；相同样本量的 rejection sampling 可能足够。

## 8. Missing baseline

best-of-N/rejection、reward-weighted fine-tuning、PPO/GRPO、DPO，以及外部 evaluator 和多样性审计。

## 9. Killer experiment

若训练 reward 提升但独立 reward/人评/多样性下降，或 rejection sampling 等成本达到同效，则 RL 价值不足。

## 10. Contribution type

它建立了 diffusion 后训练的通用策略优化接口，但没有解决 reward 是否正确。

首轮角色：扩散策略优化。历史六维记录：[2, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

对晶体最重要的启示是先定义集合级科学 reward，再决定策略算法；不能从 DDPO 直接推出 energy reward 合理。

## 12. Final verdict

方法开创性明确，但也提供反面教材：可优化性与科学正确性是两个问题。

首轮使用建议：作为晶体 RL 文献的理论起点，用于推导轨迹级/步骤级 credit 和 KL 约束。

具体结论范围：不能把 reward 上升称为物理理解，也不能忽略候选覆盖和 evaluator shift。

### 首轮留下的后续问题

在同物理调用预算下比较 RL 与 rejection/archive reweighting，并用冻结 DFT/第二 MLIP 与 basin entropy 审计。
