---
title: "SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models"
slug: "symmcd"
year: 2025
venue: "ICLR 2025"
category: "对称生成"
audit_role: "表示/机制"
paper_url: "https://arxiv.org/abs/2502.03638"
project_url: "https://github.com/sibasmarak/SymmCD"
last_verified: "2026-09-03"
---

# SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把晶体拆成不对称单元和作用于其上的对称变换，联合生成两者，以显式表示真实空间群结构。

出处：2025 · ICLR 2025；对称生成。

[论文](https://arxiv.org/abs/2502.03638) · [官方/作者项目](https://github.com/sibasmarak/SymmCD)

首轮状态：已发表；首轮审计基于论文与官方代码。

## 1. Scientific problem

多数坐标级生成器难以产生数据库中常见的非平凡对称性，直接复制空间群标签又缺少生成能力。

## 2. Mathematical task

输出不对称单元及其对称操作，再展开为完整晶体；目标是学习真实结构与对称信息的联合分布。

## 3. Data-generating process

训练依赖结构标准化、空间群解析和 Materials Project 子集；对无序、缺陷或近似对称结构适用性有限。

## 4. Core mechanism

以可解释的对称变换表示减少冗余原子，扩散生成 asymmetric unit 与群作用。

## 5. Claim–evidence alignment

生成结构的对称统计、有效性和预测性质接近真实数据；支持表示的有效性，但热力学/动力学验证仍有限。

## 6. Hidden assumptions

空间群标注稳定；严格对称展开不会排除重要畸变；真实数据的高对称比例不是数据库选择偏差。

## 7. Strongest alternative explanation

结果改善可能主要来自降维与硬约束，而非对称变换表示的泛化。

## 8. Missing baseline

相同降维程度的 prototype/Wyckoff 模型、软对称损失、对称标签打乱。

## 9. Killer experiment

在训练未见空间群、低对称畸变和对称破缺组成上评测；若只能复现已见群统计，则“跨群泛化”有限。

## 10. Contribution type

对称表示和生成机制贡献较强，科学问题仍是已有对称有效性问题。

首轮角色：表示/机制。历史六维记录：[1, 2, 2, 1, 1, 0]。

## 11. Transferable abstraction

抽象是“生成最小自由度 + 群作用恢复完整对象”，可迁移到分子晶体、缺陷超胞和群等变设计。

## 12. Final verdict

比简单增加 space-group token 更扎实，但仍需与未知结构发现和对称破缺能力权衡。

首轮使用建议：作为 symmetry-preserving de novo 强基线。

具体结论范围：不能把真实对称分布匹配等同于发现新结构，也不能忽视标准化器的作用。

### 首轮留下的后续问题

统一比较 SymmCD、WyckoffDiff、WyFormer、SbCD 在对称有效、低能盆地覆盖和破缺能力上的 Pareto。
