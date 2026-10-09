---
title: "CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction"
slug: "crystalgrpo"
year: 2026
venue: "arXiv 2026"
category: "RL/条件 CSP"
audit_role: "目标重定义/直接先例"
paper_url: "https://arxiv.org/abs/2608.06582"
project_url: ""
last_verified: "2026-09-03"
---

# CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

指出能量不识别参考多晶型、奖励集中损害 Top-N 覆盖，提出联合坐标—晶格策略与 quality/coverage 两种模式。

出处：2026 · arXiv 2026；RL/条件 CSP。

[论文](https://arxiv.org/abs/2608.06582)；首轮未核实项目入口。

首轮状态：2026-08 新预印本；与当前研究想法高度重叠，需优先完整复现和审计。

## 1. Scientific problem

预训练 flow 的 likelihood 不直接优化参考恢复；energy-only RL 与有限预算 Top-N coverage 存在冲突。

## 2. Mathematical task

以联合坐标—晶格 SDE 为策略，reward 组合 MACE 能量、StructureMatcher recovery、轨迹正则与组内 coverage advantage。

## 3. Data-generating process

MP-20/MPTS-52 参考结构作为目标；coverage 指的是参考集合/样本覆盖，不等于未知真实低能盆地全集。

## 4. Core mechanism

CrystalGRPO-Q 优先单样本命中，CrystalGRPO-C 用全轨迹正则和 coverage-aware advantage 维持 Top-20。

## 5. Claim–evidence alignment

多 backbone、数据集上的 Top-1/Top-20 与 RMSE 结果直接支持 quality–coverage trade-off；尚未解决 reference bias、真正多盆地和 DFT 验证。

## 6. Hidden assumptions

参考结构代表目标；StructureMatcher reward 可训练且不可被 exploit；MACE 能量与真实稳定一致。

## 7. Strongest alternative explanation

改善可能来自直接使用测试式参考相似度 reward，使模型更会 benchmark matching，而非更会 CSP 搜索。

## 8. Missing baseline

无 reference reward 的 basin archive、held-out polymorph reward、METRe、传统搜索和 DFT 盆地集合。

## 9. Killer experiment

训练时不提供参考坐标，只提供组成、能量和 archive；若 CrystalGRPO 优势显著消失，说明其主要解决 target recovery 而非 open-ended CSP。

## 10. Contribution type

问题意识非常重要：首次明确把 energy 与 coverage 冲突放到 flow-RL；但目标仍偏 benchmark-aligned。

首轮角色：目标重定义/直接先例。历史六维记录：[2, 1, 2, 1, 2, 0]。

## 11. Transferable abstraction

迁移的是集合级/Top-K 目标和质量—覆盖双模式，不是照搬 StructureMatcher reward。

## 12. Final verdict

是我们原“conditional diffusion+GRPO”设想的强近邻，迫使主线升级为未知 basin-level search。

首轮使用建议：作为最直接 RL baseline 与研究问题对照。

具体结论范围：不能再把 token/step reward 本身当贡献；必须超越参考结构奖励并使用物理盆地定义。

### 首轮留下的后续问题

建立 reference-free relaxed-basin archive，比较 CrystalGRPO-C 与 basin-aware objective 在未知多晶型覆盖上的差异。
