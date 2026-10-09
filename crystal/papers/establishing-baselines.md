---
title: "Establishing Baselines for Generative Discovery of Inorganic Crystals"
slug: "establishing-baselines"
year: 2025
venue: "arXiv preprint"
category: "evaluation"
audit_role: "强基线 / 评价校准"
paper_url: "https://arxiv.org/abs/2501.02144"
project_url: ""
last_verified: "2026-09-03"
---

# Establishing Baselines for Generative Discovery of Inorganic Crystals

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把电荷平衡原型枚举、离子交换等传统方案与现代生成模型放到统一生成—筛选管线中比较，检验生成模型究竟超越了什么。

出处：2025 · arXiv preprint；evaluation。

[论文](https://arxiv.org/abs/2501.02144)；首轮未核实项目入口。

首轮状态：已审计；预印本版本结论需随更新复核

## 1. Scientific problem

晶体生成论文常与弱基线比较，并把后筛选收益归因于生成模型本身，导致模型进步与筛选器进步无法区分。

## 2. Mathematical task

在统一候选预算、稳定性评估器与后筛选设置下，比较简单化学/原型基线和深度生成模型的候选效用。

## 3. Data-generating process

电荷平衡组成/原型、已知材料离子替换、VAE/LLM/扩散生成候选，以及统一机器学习势或稳定性筛选。

## 4. Core mechanism

贡献不是新生成器，而是构造危险且廉价的反事实基线，并要求所有方法共享相同后处理，从而分离 proposal 质量与 evaluator 质量。

## 5. Claim–evidence alignment

论文报告简单离子交换和原型方案在稳定性上具有很强竞争力，同时现代生成模型在某些新颖性或目标性质维度仍有优势；统一筛选能显著改善多类方法。

## 6. Hidden assumptions

统一筛选器在所有方法的分布上同样校准；候选数、弛豫次数和计算成本可公平折算；数据库原型不会造成隐性泄漏。

## 7. Strongest alternative explanation

观察到的差异可能主要来自方法访问的数据库先验不同、候选去重规则不同，或 MLIP 对某些生成分布更友好。

## 8. Missing baseline

AIRSS、USPEX/CALYPSO 等传统 CSP 在同一组成和同一物理评估预算下的比较；substitution-aware novelty，而非仅数据库去重。

## 9. Killer experiment

固定 MLIP/DFT 调用数、墙钟和候选数后，若离子替换/原型枚举达到或超过生成模型的低能独立势阱覆盖，则生成器没有证明搜索价值。

## 10. Contribution type

它改变了基线与证据标准：高分不再足以，必须证明相对简单 proposal 的净增益，并把生成、筛选和数据库先验拆开。

首轮角色：强基线 / 评价校准。历史六维记录：[2, 1, 1, 1, 2, 0]。

## 11. Transferable abstraction

可迁移为任何生成科学任务的三段式审计：proposal → oracle/evaluator → selection；每一段都要有独立基线和成本核算。

## 12. Final verdict

这是高价值评价工作。它未证明传统方法普遍优于生成模型，但证明弱基线和不统一后处理足以制造虚假的方法优势。

首轮使用建议：当前项目必须把离子替换、原型检索、随机结构与同一 MLIP/DFT 管线作为首要基线。

具体结论范围：不能据此声称生成模型没有价值，也不能将预印本中的特定模型排名外推到所有数据集和搜索预算。

### 首轮留下的后续问题

在固定组成、多晶型 aware 的测试集上绘制『独立低能 basin 数—物理评估成本』曲线，并拆分 proposal 与筛选贡献。
