---
title: "Open Materials Generation with Stochastic Interpolants"
slug: "omatg"
year: 2025
venue: "ICML 2025"
category: "生成基础"
audit_role: "统一机制"
paper_url: "https://arxiv.org/abs/2502.02582"
project_url: "https://github.com/FERMat-ML/OMatG"
last_verified: "2026-09-03"
---

# Open Materials Generation with Stochastic Interpolants

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

以 Stochastic Interpolants 统一 flow 与 diffusion，耦合连续坐标/晶格流和离散元素流，并同步改进 CSP 与 de novo 评测。

出处：2025 · ICML 2025；生成基础。

[论文](https://arxiv.org/abs/2502.02582) · [官方/作者项目](https://github.com/FERMat-ML/OMatG)

首轮状态：已发表；首轮审计基于论文、官方实现与后续 benchmark 使用。

## 1. Scientific problem

晶体生成需要同时处理周期连续变量和离散元素，而扩散与 flow 的路径选择长期被割裂讨论。

## 2. Mathematical task

学习任意 base 到晶体目标分布的可调随机桥；输出条件或无条件晶体，目标仍是数据库分布生成。

## 3. Data-generating process

主要来自常用材料数据库终态；插值路径由人工设定，而不是从真实弛豫/合成轨迹直接观测。

## 4. Core mechanism

将 SI 的可调插值、速度场和随机性适配周期图表示，并用 discrete flow matching 处理元素。

## 5. Claim–evidence alignment

在 CSP 与 DNG 指标上优于纯 flow/diffusion 实现，并成为后续数据集/评测研究常用模型；支持 SI 作为统一工具。

## 6. Hidden assumptions

所选插值族与晶体几何匹配；性能差异不是超参搜索或评测实现变化造成；数据库路径最优性可由终点指标代表。

## 7. Strongest alternative explanation

收益可能来自更广超参空间、离散流实现和评测调优，而非 SI 统一性本身。

## 8. Missing baseline

固定网络、base、NFE 与调参预算的 diffusion/flow/SI；真实弛豫轨迹驱动 bridge；简单线性/OT bridge。

## 9. Killer experiment

在相同计算与调参预算下做路径消融，并检验中间状态的能量、力和 basin identity；若路径只影响数值效率，不能讲物理景观。

## 10. Contribution type

生成机制与统一框架贡献明确；“SI 用于晶体”此后已不再构成新颖点。

首轮角色：统一机制。历史六维记录：[1, 2, 2, 1, 1, 0]。

## 11. Transferable abstraction

可迁移的是 bridge design：明确源分布、目标分布与中间物理语义，而不是只替换一个插值公式。

## 12. Final verdict

重要机制工作，也是对任何新 SI 晶体论文的直接先例。

首轮使用建议：作为当前 SI/flow 强基线和 OMatG-IRL 的基础。

具体结论范围：不能把可调随机桥自动解释为物理路径，也不能再以“首次 SI 晶体生成”为贡献。

### 首轮留下的后续问题

构造 global-proposal/local-relaxation 混合 base，并测 bridge 对跨盆地与盆地内修正的分离作用。
