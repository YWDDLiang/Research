---
title: "Siamese Foundation Models for Crystal Structure Prediction"
slug: "dao"
year: 2025
venue: "Nature Communications 2026"
category: "条件 CSP/物理数据"
audit_role: "数据+双模型系统"
paper_url: "https://arxiv.org/abs/2503.10471"
project_url: "https://github.com/ManlioWu/DAO"
last_verified: "2026-09-03"
---

# Siamese Foundation Models for Crystal Structure Prediction

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

DAO-G 生成结构，DAO-P 预测能量并用于不稳定数据弛豫和采样引导，通过大规模稳定/不稳定结构预训练提升 CSP。

出处：2025 · Nature Communications 2026；条件 CSP/物理数据。

[论文](https://arxiv.org/abs/2503.10471) · [官方/作者项目](https://github.com/ManlioWu/DAO)

首轮状态：已发表；首轮审计基于 Nature Communications、arXiv v2 与官方代码。

## 1. Scientific problem

仅用稳定终态训练限制了 CSP 泛化；能否让生成器与能量模型协同利用不稳定结构和弛豫信息。

## 2. Mathematical task

DAO-P 学能量/性质，DAO-G 学 p(X,L|A)；预训练阶段借助预测器构造/弛豫数据，推理阶段可做能量引导。

## 3. Data-generating process

引入大量稳定与不稳定构型及模型生成的弛豫数据；数据规模、质量、势模型偏差和预训练任务共同作用。

## 4. Core mechanism

双模型互相提供表征与监督：预测器近似势能，生成器扩展候选分布；采用 pretrain-finetune 跨 benchmark。

## 5. Claim–evidence alignment

MP-20/MPTS-52、多晶型和若干真实体系结果支持大规模预训练有效；但部分超高速度比较与 DFT 软件口径需谨慎解释。

## 6. Hidden assumptions

DAO-P 在 OOD 高能结构上准确；模型弛豫不会放大偏差；双模型“协同”超过单纯增加数据。

## 7. Strongest alternative explanation

提升可能主要来自更多非平衡数据和更大模型，而不是 Siamese 架构；能量引导也可能只优化 evaluator。

## 8. Missing baseline

同数据单生成器、同参数独立模型、冻结预测器只做后筛选、其他 MLIP 生成的轨迹。

## 9. Killer experiment

固定数据量与计算，比较联合/独立训练；用第二个 MLIP 与 DFT 验证引导后排名。若换 evaluator 后优势消失，属于 reward overfitting。

## 10. Contribution type

数据扩展与生成—预测双模型系统贡献强，纯架构新颖性次之。

首轮角色：数据+双模型系统。历史六维记录：[1, 2, 2, 2, 1, 0]。

## 11. Transferable abstraction

迁移价值是把“生成、评估、数据扩展”拆成闭环，并明确每次新增信息来自哪里。

## 12. Final verdict

与我们轨迹/物理反馈路线高度相关；必须把数据贡献和模型贡献分离后再借鉴。

首轮使用建议：作为不稳定数据、能量引导和 foundation pretraining 强基线。

具体结论范围：不能把预测器引导称为模型理解真实 PES，不能用单 evaluator 自证。

### 首轮留下的后续问题

在相同 OMat24/LeMat-Traj 子集上比较 DAO 风格预训练、简单轨迹监督和我们的 basin-aware 目标。
