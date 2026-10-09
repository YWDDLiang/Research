---
title: "Crystal Structure Prediction by Joint Equivariant Diffusion"
slug: "diffcsp"
year: 2023
venue: "NeurIPS 2023"
category: "条件 CSP"
audit_role: "任务形式化/机制"
paper_url: "https://arxiv.org/abs/2309.04475"
project_url: "https://github.com/jiaor17/DiffCSP"
last_verified: "2026-09-03"
---

# Crystal Structure Prediction by Joint Equivariant Diffusion

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

把给定组成的 CSP 形式化为晶格与分数坐标的联合扩散，并通过周期 E(3) 等变网络处理晶体几何。

出处：2023 · NeurIPS 2023；条件 CSP。

[论文](https://arxiv.org/abs/2309.04475) · [官方/作者项目](https://github.com/jiaor17/DiffCSP)

首轮状态：已发表；首轮审计基于论文和官方实现。

## 1. Scientific problem

给定组成后，如何在具有周期、旋转、平移和置换对称的连续空间中预测晶格与原子位置。

## 2. Mathematical task

输入为元素组成或原子种类集合，输出为晶格 L 与分数坐标 X；目标近似学习 p(X,L|A)，标准评测则把样本与数据库参考结构匹配。

## 3. Data-generating process

主要使用稳定结构终态数据；一个组成往往只保留一个或少量数据库参考，真实低能多晶型集合没有被完整观测。

## 4. Core mechanism

分别对晶格和分数坐标构造噪声过程，使用周期 E(3) 等变网络联合去噪，使坐标表示天然适配周期边界。

## 5. Claim–evidence alignment

在 Perov-5、MP-20、MPTS-52 等标准 CSP 口径上提高 Match Rate、降低 RMSE；支持其几何机制有效，但不等于完整覆盖势能面。

## 6. Hidden assumptions

数据库参考结构可作为唯一目标；StructureMatcher 容差对应科学正确性；同组成的训练与测试分布不存在严重多晶型泄漏。

## 7. Strongest alternative explanation

提升可能主要来自分数坐标、联合训练和更强等变 backbone，而不是扩散范式本身。

## 8. Missing baseline

相同网络容量的回归/flow、检索与离子替换初始化、传统 CSP 在等能量评估预算下的比较。

## 9. Killer experiment

对每个组成构建多个 DFT/高可信 MLIP 低能盆地，比较 Top-K basin coverage；若只恢复单参考而遗漏其他低能盆地，则它解决的是 reference recovery 而非完整 CSP。

## 10. Contribution type

对固定组成晶体生成的数学形式化与等变机制贡献强，是后续 conditional CSP 的核心基线。

首轮角色：任务形式化/机制。历史六维记录：[2, 1, 2, 1, 1, 0]。

## 11. Transferable abstraction

可迁移抽象是 p(X,L|A) 的周期商空间建模，以及晶格与坐标联合但可区分的状态设计。

## 12. Final verdict

重要基础工作，但它把“数据库参考恢复”近似为“CSP”的任务假设应在新研究中被主动拆开。

首轮使用建议：用作固定组成模型基线、状态参数化和标准数据接口。

具体结论范围：不能仅凭 Match Rate 声称理解或探索多峰势能面。

### 首轮留下的后续问题

在 MP-20 polymorph split 上测 Top-1、Top-20、METRe、不同盆地数与等预算传统搜索。
