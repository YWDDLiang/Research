---
title: "Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning"
slug: "chemeleon2"
year: 2025
venue: "Nature Machine Intelligence 2026"
category: "RL de novo"
audit_role: "多目标对齐"
paper_url: "https://arxiv.org/abs/2511.07158"
project_url: "https://github.com/hspark1212/chemeleon2"
last_verified: "2026-09-03"
---

# Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

在 latent diffusion 上使用 GRPO 与稳定、新颖、多样等可验证多目标奖励，缓解似然采样偏向已知高密度区域的问题。

出处：2025 · Nature Machine Intelligence 2026；RL de novo。

[论文](https://arxiv.org/abs/2511.07158) · [官方/作者项目](https://github.com/hspark1212/chemeleon2)

文献状态：已发表；官方代码已核验。

## 1. Scientific problem

数据库最大似然让模型集中于常见材料，和发现稀有新颖结构的目标错位；单一稳定奖励又会坍缩。

## 2. Mathematical task

以 denoising trajectory 为策略，组内相对优势更新；reward 组合稳定、novelty、diversity 与性质。

## 3. Data-generating process

奖励由结构匹配和 ML 代理构成；训练分布与 novelty reference 决定何为新颖。

## 4. Core mechanism

GRPO 在无需价值网络情况下对多目标终点奖励优化，并通过相对比较与多样性项抑制坍缩。

## 5. Claim–evidence alignment

论文报告 novelty-validity trade-off 改善和条件设计；支持 RL 能改变采样分布，但不自动证明得到真正新拓扑或 DFT 稳定。

## 6. Hidden assumptions

reward 各分量与科学价值一致；群内比较稳定；结构 novelty 指标不被元素替换钻空子。

## 7. Strongest alternative explanation

提升可能由 novelty 计算口径、更多采样和 reward shaping 造成；生成物仍可能是 substitution-derived。

## 8. Missing baseline

rejection sampling、archive sampling、cSUN reward、substitution-aware novelty、相同样本预算的无训练筛选。

## 9. Killer experiment

用 substitution-based novelty 和独立 DFT/phonon 重新评估 RL 前后；若新增候选主要是替换结构或代理失效，则发现性声称应收缩。

## 10. Contribution type

多目标 RL 工程与目标错位讨论有价值；在 2026 已构成必须超越的直接先例。

工作定位：多目标对齐。六维贡献描述：[1, 1, 2, 1, 2, 0]。

## 11. Transferable abstraction

迁移的是把质量—新颖—多样视为多目标 Pareto，而非把一个加权标量当作真目标。

## 12. Final verdict

重要 RL 基线，也提醒我们的新工作不能只做 GRPO+稳定/多样 reward。

研究参考：作为 de novo RL 和 reward hacking 分析对照。

具体结论范围：不能把传统 novelty 奖励当作 genuine structural novelty，也不能用同一模型训练和评价。

### 相关研究问题

在 basin-level archive reward 中加入 substitution-aware 与 evaluator uncertainty，并与 Chemeleon2 复现对比。
