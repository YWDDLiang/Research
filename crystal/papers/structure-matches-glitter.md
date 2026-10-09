---
title: "All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation"
slug: "structure-matches-glitter"
year: 2025
venue: "NeurIPS 2025 Datasets and Benchmarks"
category: "evaluation"
audit_role: "Benchmark 纠偏 / 多晶型评价"
paper_url: "https://arxiv.org/abs/2509.12178"
project_url: "https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter"
last_verified: "2026-09-03"
---

# All That Structure Matches Does Not Glitter: Evaluating Crystal Structure Generation

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

系统揭示结构匹配、数据重复与随机划分对晶体生成评价的误导，提出多晶型感知划分及 METRe、cRMSE 等补充指标。

出处：2025 · NeurIPS 2025 Datasets and Benchmarks；evaluation。

[论文](https://arxiv.org/abs/2509.12178) · [官方/作者项目](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter)

首轮状态：已审计；会议论文，配套数据持续维护

## 1. Scientific problem

StructureMatcher 的二元命中、重复结构和随机 train/test split 可能把记忆、同组成泄漏或容差效应误判为 CSP 能力。

## 2. Mathematical task

重新设计晶体结构预测/生成的划分与指标，使评价更接近参考结构集合覆盖和连续结构误差，而非单个阈值命中。

## 3. Data-generating process

多数据集的重复/多晶型统计、标准生成模型输出、polymorph-aware split，以及不同匹配容差下的评估结果。

## 4. Core mechanism

通过数据去重、按组成/多晶型组织的划分、集合级匹配和连续误差指标，显式暴露 reference multiplicity 与阈值敏感性。

## 5. Claim–evidence alignment

论文展示常用划分含显著重复和多晶型交叉，模型排名与绝对结果会随匹配定义和划分改变；新指标提供更细粒度比较。

## 6. Hidden assumptions

已知参考集合近似代表待发现的相关多晶型；所选结构距离与匹配容差具有化学意义；数据清洗不会删掉真正不同的相。

## 7. Strongest alternative explanation

排名变化也可能部分来自新划分更 OOD、训练分布发生变化，而不完全是旧指标错误；参考数据库本身仍是不完整观测。

## 8. Missing baseline

弛豫后 basin identity、能量排序、同预算传统 CSP，以及在未观测多晶型上的 prospective DFT 验证。

## 9. Killer experiment

若改变容差、结构表示或弛豫器后 METRe/cRMSE 排名大幅翻转，且与 DFT basin 恢复无关，则新指标也只是在替换代理。

## 10. Contribution type

它重新定义了什么证据才算 CSP/生成进步，是问题与评价层贡献，而不是又一个模型增量。

首轮角色：Benchmark 纠偏 / 多晶型评价。历史六维记录：[2, 2, 1, 0, 2, 0]。

## 11. Transferable abstraction

可迁移到所有多解科学预测：测试标签是世界的一个不完整样本时，应从 single-reference accuracy 转为 set coverage 与不确定性。

## 12. Final verdict

这是当前领域必须优先阅读的 benchmark 论文。它不能解决真实势能面覆盖，但足以否定许多只靠单参考 Match Rate 的强结论。

首轮使用建议：当前 repo 的所有固定组成实验应采用 polymorph-aware split，并同时报告集合匹配、连续误差和弛豫后 basin coverage。

具体结论范围：不能把数据库未记录结构自动判为错误，也不能把新指标等同于真正的物理正确性。

### 首轮留下的后续问题

在 MP-20/更大数据上复现随机划分与多晶型划分的排名变化，并加入 DFT/MLIP basin 标签，检验指标与物理目标的一致性。
