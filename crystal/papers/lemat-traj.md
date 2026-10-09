---
title: "LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling"
slug: "lemat-traj"
year: 2025
venue: "arXiv 2025"
category: "数据/轨迹"
audit_role: "数据标准化"
paper_url: "https://arxiv.org/abs/2508.20875"
project_url: "https://github.com/LeMaterial/lematerial-fetcher"
last_verified: "2026-09-03"
---

# LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

统一 Materials Project、Alexandria、OQMD 等来源的 1.2 亿余轨迹构型，协调多种 DFT 泛函和元数据。

出处：2025 · arXiv 2025；数据/轨迹。

[论文](https://arxiv.org/abs/2508.20875) · [官方/作者项目](https://github.com/LeMaterial/lematerial-fetcher)

首轮状态：开放数据/工具发布；跨泛函混用需谨慎。

## 1. Scientific problem

量子轨迹数据碎片化、格式不一，使模型难以利用终态之外的高能、高力和弛豫过程。

## 2. Mathematical task

输入结构，输出能量/力监督或轨迹序列；可用于 MLIP、局部修正器和生成路径建模。

## 3. Data-generating process

聚合多个数据库和 PBE/PBEsol/SCAN/r2SCAN 等泛函；异质性既扩大覆盖，也引入不可直接比较的系统偏差。

## 4. Core mechanism

标准化 schema、过滤质量、保留轨迹上下文，并提供可扩展抓取工具。

## 5. Claim–evidence alignment

对力预测和弛豫任务的微调收益支持轨迹价值；尚不能自动证明轨迹可让生成器学会跨盆地搜索。

## 6. Hidden assumptions

不同来源的能量零点和泛函可协调；轨迹时间顺序代表有意义的优化过程；高力样本不会破坏低能精度。

## 7. Strongest alternative explanation

收益可能只是更多结构覆盖，而不是“轨迹顺序”信息；随机打乱轨迹也许同样有效。

## 8. Missing baseline

相同构型集合但去掉时间顺序、只保留终点+随机噪声、单泛函子集。

## 9. Killer experiment

固定所有结构，比较有序轨迹、打乱轨迹和无序集合监督；若相同，则真正贡献是数据覆盖而非 dynamics。

## 10. Contribution type

大型轨迹数据整合贡献强；对生成方法的意义取决于是否利用顺序、力与盆地信息。

首轮角色：数据标准化。历史六维记录：[1, 2, 1, 1, 1, 0]。

## 11. Transferable abstraction

迁移抽象是区分“构型覆盖”与“轨迹因果顺序”，并为二者设计独立消融。

## 12. Final verdict

对我们极重要，但不能把下载轨迹数据本身当作方法创新。

首轮使用建议：用于训练局部物理修正、定义 basin transition、分析 force/energy 分布。

具体结论范围：不能跨泛函直接混合绝对能量，也不能把几何优化轨迹当作有限温度动力学。

### 首轮留下的后续问题

构建同组成多起点轨迹子集，标注 relaxed basin id，测有序轨迹对 basin-aware 生成的增益。
