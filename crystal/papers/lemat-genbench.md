---
title: "LeMat-GenBench: A Unified Benchmark for Generative Materials Models"
slug: "lemat-genbench"
year: 2025
venue: "arXiv preprint"
category: "evaluation"
audit_role: "统一生成 Benchmark"
paper_url: "https://arxiv.org/abs/2512.04562"
project_url: "https://github.com/LeMaterial/lemat-genbench"
last_verified: "2026-09-03"
---

# LeMat-GenBench: A Unified Benchmark for Generative Materials Models

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

以统一实现比较多种材料生成模型的有效性、分布一致性、多样性、新颖性与稳定性，突出维度间的系统权衡。

出处：2025 · arXiv preprint；evaluation。

[论文](https://arxiv.org/abs/2512.04562) · [官方/作者项目](https://github.com/LeMaterial/lemat-genbench)

文献状态：预印本与代码均可能更新

## 1. Scientific problem

不同晶体生成论文使用不同数据预处理、采样数、筛选器和指标，导致横向比较失真，且单一综合分数掩盖稳定—新颖—多样性冲突。

## 2. Mathematical task

在统一数据、采样和 evaluator 下，对代表性生成模型进行多维度画像，而非只给单一排行榜。

## 3. Data-generating process

多个公开晶体数据集、约十二类生成模型输出、统一结构处理和稳定性/新颖性/多样性计算工具。

## 4. Core mechanism

标准化 evaluation harness，把模型质量拆成多条 Pareto 轴，并提供可复现代码以减少实现差异。

## 5. Claim–evidence alignment

论文观察到没有模型在所有维度普遍占优，并呈现稳定性、创新性、分布拟合和多样性之间的平均权衡。

## 6. Hidden assumptions

统一 evaluator 对各模型分布同等可靠；选择的维度足以代表科学效用；模型提交样本和 checkpoint 可公平复现。

## 7. Strongest alternative explanation

一些 Pareto 权衡可能由模型训练预算、数据规模、采样温度和后处理不同造成，而非生成范式的内在限制。

## 8. Missing baseline

相同参数量/训练 FLOPs/数据规模的 controlled comparison；同一候选预算下的 DFT、声子与 basin-level 评价。

## 9. Killer experiment

若替换 MLIP、去重口径或采样温度后 Pareto 结论消失，则所谓范式权衡主要是评估/超参效应。

## 10. Contribution type

它提供统一实验基础设施和多目标证据标准，价值在可复现比较而非提出新的科学模型。

工作定位：统一生成 Benchmark。六维贡献描述：[1, 2, 1, 1, 2, 0]。

## 11. Transferable abstraction

可迁移为本 repo 的自动化 leaderboard：所有新方法输出标准候选包，再由冻结 evaluator 和版本化脚本统一计算。

## 12. Final verdict

这是重要的系统性 benchmark。它能降低论文间不可比性，但不能把数据库指标自动转化为真实材料发现能力。

研究参考：当前项目应直接兼容其输入输出接口，并在其维度之外补充多晶型 coverage、计算预算和 evaluator robustness。

具体结论范围：不能从横截面模型排名推出某一生成范式在理论上更优；也不能忽略训练/采样预算差异。

### 相关研究问题

选择 3–5 个最接近基线，以完全相同训练数据与推理预算复现实验，绘制稳定性—novelty—basin coverage 三维 Pareto。
