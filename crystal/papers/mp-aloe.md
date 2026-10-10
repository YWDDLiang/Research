---
title: "MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials"
slug: "mp-aloe"
year: 2025
venue: "arXiv 2025"
category: "数据/主动学习"
audit_role: "科学分层数据"
paper_url: "https://arxiv.org/abs/2507.05559"
project_url: ""
last_verified: "2026-09-03"
---

# MP-ALOE: An r2SCAN dataset for universal machine learning interatomic potentials

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

以主动学习生成近百万 r2SCAN 非平衡结构，覆盖 89 种元素，并强调极端形变、高温高压和远离平衡力的鲁棒性。

出处：2025 · arXiv 2025；数据/主动学习。

[论文](https://arxiv.org/abs/2507.05559)；首轮未核实项目入口。

文献状态：开放数据论文；未核验独立代码仓库。

## 1. Scientific problem

通用 MLIP 在生成器产生的远离训练分布构型上可能不物理，传统平衡数据不足以约束高力与极端区域。

## 2. Mathematical task

主动学习选择 DFT 查询点，模型学习能量/力；目标是扩大物理势的可信域。

## 3. Data-generating process

采样主要由主动学习策略决定，覆盖高能、高力和极端形变；r2SCAN 一致性较好但计算与元素分布仍不均。

## 4. Core mechanism

通过模型不确定性/失败区域驱动查询，迭代扩充非平衡数据并进行多类鲁棒性 benchmark。

## 5. Claim–evidence alignment

在平衡热化学、远平衡力、极端形变和 MD 稳定性上的表现支持 science-aware 数据选择。

## 6. Hidden assumptions

主动学习不确定性校准；选择器不会忽略罕见但重要区域；r2SCAN 标签适合所有下游。

## 7. Strongest alternative explanation

优势可能来自统一高质量泛函和数据清洗，而非主动学习策略。

## 8. Missing baseline

同规模随机采样、按力/组成分层采样、只用模型 disagreement 但不做 science strata。

## 9. Killer experiment

固定 DFT 预算，对比随机、uncertainty-only 与 science-stratified acquisition；观察困难氧化物等能力是否被牺牲。

## 10. Contribution type

数据采样策略与科学鲁棒性贡献强，直接支持“Science 决定能力不能丢”的原则。

工作定位：科学分层数据。六维贡献描述：[2, 2, 2, 1, 2, 0]。

## 11. Transferable abstraction

迁移的是先定义不可丢失的科学能力分层，再在每层内部做主动选择。

## 12. Final verdict

比仅追求平均误差的数据选择更有研究意义，是我们数据策略的重要模板。

研究参考：用于 evaluator 鲁棒性、主动学习和生成 OOD 安全边界。

具体结论范围：不能为了降低平均误差而少采困难体系，也不能把模型不确定性当作唯一价值函数。

### 相关研究问题

设计 composition × force × coordination × pressure 分层 acquisition，并比较每层最坏性能。
