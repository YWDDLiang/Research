---
title: "Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models"
slug: "omat24"
year: 2024
venue: "arXiv 2024; updated 2026"
category: "数据/MLIP"
audit_role: "数据基础设施"
paper_url: "https://arxiv.org/abs/2410.12771"
project_url: "https://github.com/FAIR-Chem/fairchem"
last_verified: "2026-09-03"
---

# Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models

> 历史首轮记录；原核查日期：2026-09-03。2026-10-09依据既有索引精简文字，没有新增论文核验或复现。
>
> [返回当前研究入口](../README.md)

发布超过 1.1 亿次 DFT 计算，重点覆盖结构与组成多样性，并训练 EquiformerV2 通用势模型。

出处：2024 · arXiv 2024; updated 2026；数据/MLIP。

[论文](https://arxiv.org/abs/2410.12771) · [官方/作者项目](https://github.com/FAIR-Chem/fairchem)

首轮状态：大型开放数据与模型发布；数据版本和许可应按官方页面持续更新。

## 1. Scientific problem

材料 MLIP 缺少公开、广覆盖且含非平衡结构的训练数据，限制稳定性筛选、弛豫与生成反馈。

## 2. Mathematical task

输入原子结构，监督能量、力、应力等；模型目标是学习 DFT 近似器，不直接生成晶体。

## 3. Data-generating process

DFT 结构由多种采样策略产生，包含大量非平衡和高力区域；但仍受泛函、元素覆盖和采样策略约束。

## 4. Core mechanism

以规模化 DFT 数据和 EquiformerV2 训练建立通用 MLIP，并研究数据混合、模型规模与辅助去噪。

## 5. Claim–evidence alignment

Matbench Discovery 等性能支持其作为强 evaluator/relaxer；不能由 aggregate benchmark 保证每个生成 OOD 区域可靠。

## 6. Hidden assumptions

训练 DFT 泛函足以代表目标科学问题；高覆盖等于低 epistemic uncertainty；数据重复和来源偏差已处理。

## 7. Strongest alternative explanation

模型成功可能主要来自巨大数据与计算，而非辅助目标；在特定体系上专用势可能更可靠。

## 8. Missing baseline

更小但 science-stratified 的数据、MACE-MP/MatterSim/CHGNet、跨势模型 disagreement。

## 9. Killer experiment

让多个生成器主动寻找 OMat24 模型高置信但其他 MLIP/DFT 失败的结构；若容易发现，单模型奖励不可被当真值。

## 10. Contribution type

数据规模和开放基础设施贡献极强，是生成后筛选与轨迹监督的重要底座。

首轮角色：数据基础设施。历史六维记录：[1, 2, 1, 2, 2, 0]。

## 11. Transferable abstraction

迁移的是把 evaluator 视为带分布边界的模型，并用数据覆盖/不确定性决定能否用于 RL。

## 12. Final verdict

必须读，但它是物理代理基础设施，不是自动正确的 oracle。

首轮使用建议：用于候选弛豫、力/应力监督和 evaluator ensemble。

具体结论范围：不能只用一个 OMat24 势模型闭环训练再用同模型评价，避免自证与 reward hacking。

### 首轮留下的后续问题

建立 OMat24/MACE/MatterSim/DFT 小集的一致性矩阵，按组成与力范围分层。
