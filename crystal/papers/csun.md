---
title: "cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation"
slug: "csun"
year: 2025
venue: "arXiv preprint (v3 updated 2026)"
category: "evaluation"
audit_role: "连续评价 / 可优化 Reward"
paper_url: "https://arxiv.org/abs/2510.12405"
project_url: ""
last_verified: "2026-09-03"
---

# cSUN: Continuous Stability, Uniqueness, and Novelty Metrics for Crystal Generation

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

将离散阈值式 S.U.N. 扩展为连续可比较分数，减轻阈值跳变，并讨论其作为生成模型后训练信号的用途。

出处：2025 · arXiv preprint (v3 updated 2026)；evaluation。

[论文](https://arxiv.org/abs/2510.12405)；首轮未核实项目入口。

首轮状态：已审计；版本持续更新

## 1. Scientific problem

二元 Stable/Unique/Novel 指标对阈值和微小扰动敏感，无法表达候选离边界多远，也不利于稳定的奖励优化。

## 2. Mathematical task

为稳定性、唯一性和新颖性定义连续分量，再组合成连续候选/集合质量指标。

## 3. Data-generating process

晶体生成样本、稳定性代理、结构距离或相似度、训练/参考数据库及不同阈值下的 SUN 结果。

## 4. Core mechanism

用平滑映射替代硬阈值，保留距离边界的信息，并使 reward 对小变化更连续。

## 5. Claim–evidence alignment

论文展示连续指标能区分同一二元标签内部的质量差异，并可用于更细粒度排序或优化。

## 6. Hidden assumptions

平滑函数与尺度参数具有物理/统计意义；连续性不会诱导模型只在代理边界附近投机；三分量组合反映科学价值。

## 7. Strongest alternative explanation

性能改善可能只是 reward shaping 更易优化，而非最终材料效用更高；连续相似度仍可能遗漏拓扑替换和 evaluator 偏差。

## 8. Missing baseline

独立 DFT/声子、substitution-aware novelty、basin coverage 和人类专家排序；与简单 margin reward 比较。

## 9. Killer experiment

用 cSUN 训练后若 cSUN 提升但 DFT 稳定、真实 novelty 或独立势阱覆盖不升，说明指标被 reward hacking。

## 10. Contribution type

它是评价和优化接口层贡献，解决了二元指标不连续，但没有解决每个分量是否与真实科学目标一致。

首轮角色：连续评价 / 可优化 Reward。历史六维记录：[1, 1, 2, 0, 2, 0]。

## 11. Transferable abstraction

可迁移为后训练的平滑多目标 reward，但必须冻结外部审计指标，避免训练指标与测试指标同源。

## 12. Final verdict

有实用价值，但不应成为论文唯一主贡献。连续化只能改善优化几何，不能自动修复错误的任务定义。

首轮使用建议：可作为当前项目的辅助 reward/诊断量，不应替代 basin-level set objective 与独立 DFT 验证。

具体结论范围：不能声称连续分数更高就意味着更可合成；也不能把平滑后的 novelty 当成真正结构创新。

### 首轮留下的后续问题

比较 energy-only、binary SUN、cSUN 与 basin-aware reward，在相同 KL/采样预算下看独立 DFT 和 coverage 是否一致提升。
