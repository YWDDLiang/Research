---
title: "Crystal Diffusion Variational Autoencoder for Periodic Material Generation"
slug: "cdvae"
year: 2021
venue: "ICLR 2022"
category: "生成基础"
audit_role: "开山/任务坐标系"
paper_url: "https://arxiv.org/abs/2110.06197"
project_url: "https://github.com/txie-93/cdvae"
last_verified: "2026-09-03"
---

# Crystal Diffusion Variational Autoencoder for Periodic Material Generation

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

以 VAE 潜变量组织组成、晶格和原子数，用周期等变图网络通过退火 Langevin 动力学生成坐标，并建立后来广泛沿用的数据集与评价口径。

出处：2021 · ICLR 2022；生成基础。

[论文](https://arxiv.org/abs/2110.06197) · [官方/作者项目](https://github.com/txie-93/cdvae)

首轮状态：已发表；首轮审计基于论文、官方代码与后续评测文献。

## 1. Scientific problem

周期材料只占任意原子排列空间中的极小稳定流形，普通分子生成表示无法同时处理周期性、置换、旋转和平移不变性。

## 2. Mathematical task

输入可为潜变量或性质条件，输出为原子种类、坐标和晶格；学习目标是稳定材料数据库分布的生成模型，而不是直接求解量子力学全局最优。

## 3. Data-generating process

训练数据主要是数据库中的弛豫终态；它包含稳定结构统计规律，却几乎不包含从高能构型到势阱的真实搜索轨迹。

## 4. Core mechanism

将全局结构编码到连续潜变量，预测组成与晶格，再用周期图网络估计坐标噪声分数并迭代去噪。

## 5. Claim–evidence alignment

重构、无条件生成和性质优化上优于当时基线，并提供 MP-20 等数据与指标；这些证据支持其作为周期晶体生成框架，但不足以证明去噪场等于物理力场。

## 6. Hidden assumptions

数据库分布足够代表可实现材料；随机加噪构造的局部邻域能够训练出对真实生成过程有用的向量场；预测稳定性模型在生成分布外可靠。

## 7. Strongest alternative explanation

增益可能主要来自更合适的周期等变表示、较强图网络和后处理，而非 VAE 潜变量或所谓物理去噪本身。

## 8. Missing baseline

同等参数量的无潜变量扩散、传统原型采样加统一 MLIP 筛选、仅终态几何优化初始化。

## 9. Killer experiment

将同一模型的向量场与冻结 MLIP/DFT 力逐点比较，并测试沿模型场积分是否单调降低真实能量；若无相关性，就不能称其学到物理弛豫。

## 10. Contribution type

问题开拓、周期表示、基准基础设施三项贡献都较强；具体生成器会被替换，但它确立的任务坐标系长期存在。

首轮角色：开山/任务坐标系。历史六维记录：[2, 2, 2, 1, 2, 0]。

## 11. Transferable abstraction

最值得迁移的是“先保证状态空间与等价关系正确，再谈生成器”，不是照搬 VAE 或 Langevin 采样。

## 12. Final verdict

这是晶体生成领域的开山型工作。其长期价值高于后来许多小幅提分模型，但稳定数据库 score 与势能梯度必须严格区分。

首轮使用建议：用作领域起点、数据口径来源和不变性检查清单。

具体结论范围：不能把其去噪过程直接解释为沿真实势能面弛豫，也不能用旧 validity 指标代表发现价值。

### 首轮留下的后续问题

在统一去重、polymorph-aware split 和相同 MLIP/DFT 预算下重跑 CDVAE，建立现代审计基线。
