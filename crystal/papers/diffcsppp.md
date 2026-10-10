---
title: "Space Group Constrained Crystal Generation"
slug: "diffcsppp"
year: 2024
venue: "ICLR 2024"
category: "对称约束"
audit_role: "形式化/机制"
paper_url: "https://arxiv.org/abs/2402.03992"
project_url: "https://github.com/jiaor17/DiffCSP-PP"
last_verified: "2026-09-03"
---

# Space Group Constrained Crystal Generation

> 文献分析；资料核查截至2026-09-03。
>
> [返回当前研究入口](../README.md)

将空间群约束分解为晶格对数空间中的基约束与分数坐标的 Wyckoff 位置约束，在 DiffCSP 上实现可控对称生成。

出处：2024 · ICLR 2024；对称约束。

[论文](https://arxiv.org/abs/2402.03992) · [官方/作者项目](https://github.com/jiaor17/DiffCSP-PP)

文献状态：已发表；文献分析基于论文和官方实现。

## 1. Scientific problem

空间群约束形式复杂，直接在连续去噪过程中维持指定对称性并不容易。

## 2. Mathematical task

输入为组成与可选空间群，输出满足相应晶格和 Wyckoff 约束的结构；优化仍是条件结构分布拟合。

## 3. Data-generating process

依赖数据库给出的空间群/Wyckoff 标注和稳定终态，标注误差、标准化选择及低对称结构偏差会传入模型。

## 4. Core mechanism

把群论约束转写成可实现的连续几何子空间，约束晶格与坐标的扩散轨迹。

## 5. Claim–evidence alignment

在 CSP、de novo 和指定空间群生成上显示更好的对称有效性及标准指标；支持约束实现，但不证明高对称总是更科学或更具发现性。

## 6. Hidden assumptions

目标空间群已知且正确；真实低能结构不会因对称破缺而落在约束流形之外；空间群条件收益不是由缩小搜索空间单独造成。

## 7. Strongest alternative explanation

性能提升可能只是 oracle 条件显著降低了任务熵，并非模型更懂晶体。

## 8. Missing baseline

无空间群但参数量相同的模型、错误/模糊空间群条件、允许自发对称破缺的软约束模型。

## 9. Killer experiment

对具有已知低对称畸变或相变的组成，给定高对称父相并测试模型能否发现更低能的破缺结构；若不能，硬约束的上限代价必须明确。

## 10. Contribution type

空间群约束的数学分解具有可复用性；模型增益属于强机制贡献而非新科学问题。

工作定位：形式化/机制。六维贡献描述：[1, 2, 2, 1, 1, 0]。

## 11. Transferable abstraction

迁移重点是把复杂物理约束转成可微、可采样的流形，而不是把 Wyckoff 当作所有晶体任务的默认表示。

## 12. Final verdict

高质量的约束建模工作；它提高下限，也可能限制未知低对称模式的上限。

研究参考：用于对称条件基线、硬/软约束设计和对称破缺研究的对照组。

具体结论范围：不能把对称有效等同于热力学或动力学稳定，也不能假定所有任务都应显式使用 Wyckoff。

### 相关研究问题

设计 soft-to-hard symmetry schedule，与 SbCD 式跨空间群生成比较低能盆地覆盖。
