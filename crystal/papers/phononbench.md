---
title: "PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability"
slug: "phononbench"
year: 2025
venue: "arXiv preprint"
category: "evaluation"
audit_role: "动力学稳定 Benchmark"
paper_url: "https://arxiv.org/abs/2512.21227"
project_url: "https://github.com/xqh19970407/PhononBench"
last_verified: "2026-09-03"
---

# PhononBench: Benchmarking Crystal Generative Models for Dynamical Stability

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

以声子谱/虚频审计生成晶体的动力学稳定性，证明几何有效和热力学代理通过并不等于局部动力学稳定。

出处：2025 · arXiv preprint；evaluation。

[论文](https://arxiv.org/abs/2512.21227) · [官方/作者项目](https://github.com/xqh19970407/PhononBench)

首轮状态：已审计；数据规模和具体比例在版本间更新，引用数字前需锁定版本

## 1. Scientific problem

晶体生成常以形成能、凸包和结构有效性结束评价，却忽略 Hessian 负模对应的动力学不稳定。

## 2. Mathematical task

在统一弛豫与声子计算协议下，对多个生成模型的大规模样本计算或近似动力学稳定率。

## 3. Data-generating process

多个生成模型候选、统一 MLIP/弛豫设置、声子谱或最低频率标签，以及部分交叉验证。

## 4. Core mechanism

增加二阶局部势能面信息：由能量/力的一阶筛选上升到振动模态与曲率审计。

## 5. Claim–evidence alignment

各版本均支持同一核心观察：相当比例通过常见稳定性/有效性过滤的生成结构仍存在显著虚频，模型间差异明显。

## 6. Hidden assumptions

所用势模型和声子数值设置可准确逼近 DFT；阈值在不同元素体系中可比较；结构弛豫充分。

## 7. Strongest alternative explanation

虚频可能来自 MLIP、超胞、数值精度或未完全弛豫，而非结构真实不稳定；有限温度非谐效应也可能稳定软模。

## 8. Missing baseline

代表子集 DFT phonon、不同 MLIP/超胞/收敛参数、有限温度分子动力学和实验已知相 sanity check。

## 9. Killer experiment

若在分层 DFT 复核中模型排名或稳定标签大幅翻转，则 benchmark 主要测量势模型/数值设置，而非生成器。

## 10. Contribution type

它把动力学稳定正式加入生成评价，是科学证据层的重要扩展，并暴露当前 SUN/热力学筛选的盲区。

首轮角色：动力学稳定 Benchmark。历史六维记录：[2, 2, 1, 2, 2, 1]。

## 11. Transferable abstraction

可迁移为多保真漏斗：先便宜的几何/能量，再不确定性选择声子，最后 DFT/非谐验证。

## 12. Final verdict

这是必须纳入高水平生成论文的评价维度。具体比例应随版本锁定，核心结论比单一数字更可靠。

首轮使用建议：当前项目应对代表性低能独立 basin 做声子复核，并报告从热力学通过到动力学通过的 attrition。

具体结论范围：不能把无虚频直接等同于可合成，也不能把单一 MLIP 的虚频当作最终物理事实。

### 首轮留下的后续问题

建立跨两种 MLIP 与 DFT 的分层声子复核集，分析 reward 优化前后是否只是把样本推入某个势模型盲区。
