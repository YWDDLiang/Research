---
title: "PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals"
slug: "phononscore"
year: 2026
venue: "arXiv preprint"
category: "evaluation"
audit_role: "多保真动力学评分"
paper_url: "https://arxiv.org/abs/2607.08518"
project_url: "http://phononbench.cn/phononscore/"
last_verified: "2026-09-03"
---

# PhononScore: Efficient Multi-Fidelity Scoring of Dynamical Stability for Generated Crystals

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

提出更低成本的多保真声子/动力学稳定评分和重排方案，使大规模生成候选的二阶稳定性筛选更可行。

出处：2026 · arXiv preprint；evaluation。

[论文](https://arxiv.org/abs/2607.08518) · [官方/作者项目](http://phononbench.cn/phononscore/)

首轮状态：已审计；2026 新预印本与在线项目

## 1. Scientific problem

完整声子计算昂贵，导致动力学稳定只能在很小候选子集上做事后验证，难以参与搜索和重排。

## 2. Mathematical task

学习或组合多层精度信号，对候选的动力学稳定性进行成本可控的评分与优先级排序。

## 3. Data-generating process

生成晶体、不同精度的声子/曲率标签、结构与势能特征，以及高保真验证子集。

## 4. Core mechanism

以 coarse-to-fine/multi-fidelity 方式融合廉价代理和昂贵声子标签，在固定预算下优先查询最有价值候选。

## 5. Claim–evidence alignment

论文报告该评分能提高筛选效率和重排质量，并提供面向生成模型评估的在线资源。

## 6. Hidden assumptions

训练分布涵盖生成模型的 OOD 候选；代理误差可校准；高低保真标签之间关系在不同化学体系中稳定。

## 7. Strongest alternative explanation

排序提升可能来自与 benchmark 使用同源势模型或数据；模型会学习化学体系捷径而非真实曲率。

## 8. Missing baseline

完全独立的 DFT phonon、不同生成器 OOD split、不同 MLIP，以及随机/能量/最大力重排基线。

## 9. Killer experiment

在 prospective OOD 候选上若低成本评分不能富集 DFT 无虚频结构，或被 RL 明显利用漏洞，则其搜索价值不成立。

## 10. Contribution type

它主要改变计算效率和 evaluator 接口，使动力学信号有机会进入大规模生成循环。

首轮角色：多保真动力学评分。历史六维记录：[1, 2, 2, 2, 2, 0]。

## 11. Transferable abstraction

可迁移为当前项目的分层 oracle，但应与不确定性估计和主动查询绑定，而不是当作唯一 reward。

## 12. Final verdict

有较强工程与评价价值；尚不能说明用其优化后的模型会在真实 DFT 下可靠提升。

首轮使用建议：可作为 archive 重排的第二层筛选，并保留冻结的 DFT/不同模型 holdout 作防 reward hacking 审计。

具体结论范围：不能声称代理分数等于声子稳定，更不能由动力学稳定直接推出热力学稳定或可合成性。

### 首轮留下的后续问题

用完全未参与训练的化学族做 prospective 生成—重排—DFT phonon 验证，报告富集率、校准误差与成本。
