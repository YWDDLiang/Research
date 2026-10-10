---
title: "Open Materials Generation with Inference-Time Reinforcement Learning"
slug: "omatg-irl"
year: 2026
venue: "ICML 2026"
category: "RL/Flow"
audit_role: "连续时间策略优化"
paper_url: "https://arxiv.org/abs/2602.00424"
project_url: "https://github.com/FERMat-ML/OMatG"
last_verified: "2026-09-03"
---

# Open Materials Generation with Inference-Time Reinforcement Learning

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

直接在 flow 的速度场上构造随机扰动与策略梯度，无需显式 score，并可学习时间依赖 velocity annealing。

出处：2026 · ICML 2026；RL/Flow。

[论文](https://arxiv.org/abs/2602.00424) · [官方/作者项目](https://github.com/FERMat-ML/OMatG)

文献状态：已发表/官方实现并入 OMatG；“首次”主张应按任务边界理解。

## 1. Scientific problem

传统 diffusion RL 依赖 score 或离散转移概率，难直接用于只学 velocity 的 flow 模型。

## 2. Mathematical task

把随机化连续生成动态视为策略，使用终点能量 reward 估计速度场参数梯度；也可优化采样日程。

## 3. Data-generating process

以预训练 OMatG 和代理能量为基础；奖励仍是单点能量而非多晶型集合效用。

## 4. Core mechanism

对 ODE 引入可控 SDE 扰动以保留探索和可微 log-prob/策略梯度，推理时或轻量更新速度场。

## 5. Claim–evidence alignment

能量目标和采样效率实验支持 flow 可进行策略梯度对齐；不证明 energy reward 与真实 CSP coverage 一致。

## 6. Hidden assumptions

随机扰动构造无偏/低方差；composition conditioning 足以保持多样；代理能量可靠。

## 7. Strongest alternative explanation

收益可能来自 annealing schedule、额外随机采样或局部搜索，而非 RL 更新。

## 8. Missing baseline

黑盒 schedule search、CEM、energy guidance、相同随机动态但无梯度、coverage-aware reward。

## 9. Killer experiment

固定能量 oracle 调用，比较 learned annealing 与 Bayesian schedule optimization；同时测 Top-K basin coverage。若能量下降而覆盖降低，CSP 结论不完整。

## 10. Contribution type

将 policy gradient 推到 velocity-only flow 的技术贡献清晰；科学目标仍较窄。

工作定位：连续时间策略优化。六维贡献描述：[1, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

迁移的是连续时间生成器的随机策略化与时间调度学习，可用于力/覆盖等更合理 reward。

## 12. Final verdict

是 flow-RL 的关键直接先例。后续研究的贡献不能停留在“给 flow/diffusion 加 RL”。

研究参考：作为连续时间 RL、noise policy 与时间步分配基线。

具体结论范围：不能把 composition conditioning 当作充分的多样性保护，也不能只看平均能量。

### 相关研究问题

将其策略构造保留，替换为 basin archive/uncertainty-aware reward，比较 energy–coverage Pareto。
