# Roadmap

> 当前版本：Research Craft + Crystal Audit v1 · 2026-09-03

## 已完成：v1 基础框架

- 根 README：研究者方法论、What–Why–How++、数学抽象、反证与证据纪律；
- `crystal/README.md`：43 篇主索引；
- 43 份十二项首轮论文报告；
- 晶体领域数学抽象；
- 去故事化总审计；
- 开放问题；
- CV / AI 跨领域迁移图；
- 多层评价协议；
- 当前有限预算多势阱研究主线；
- 贡献、任务—数据—输出、Claim–Evidence 矩阵；
- 论文 JSON/CSV；
- 模板、Issue form 和自动一致性检查。

## v1.1：逐篇审计深度升级

目标：把首轮结构化审计升级为可追溯的全文/代码审计。

- [ ] 为每篇报告标注 L0–L4 深度；
- [ ] 锁定论文版本与官方代码 commit；
- [ ] 补充作者、DOI/OpenReview、license；
- [ ] 对 2026 预印本做月度元数据复核；
- [ ] 将作者 claim 逐条映射到 table/figure/equation；
- [ ] 为最接近当前主线的 10 篇完成代码级审计。

优先顺序：

1. CrystalGRPO；
2. PackFlow；
3. OMatG-IRL；
4. Chemeleon2；
5. CrysLLMGen；
6. FlowLLM；
7. DAO；
8. All That Structure Matches Does Not Glitter；
9. LeMat-GenBench；
10. PhononBench。

## v1.2：传统 CSP 与 evaluator

- [ ] AIRSS、USPEX、CALYPSO 的问题—算法—预算报告；
- [ ] 原型、离子替换和数据库检索强基线；
- [ ] MACE/CHGNet/MatterSim/ORB/SevenNet evaluator 审计；
- [ ] MLIP ranking flip 与不确定性 protocol；
- [ ] DFT/phonon 多保真验证模板。

## v1.3：可执行 benchmark

- [ ] 选择具有多个已知/可搜索 basin 的 composition 子集；
- [ ] 统一结构标准化；
- [ ] 弛豫后 basin clustering；
- [ ] random/prototype/substitution/generative baseline；
- [ ] energy—coverage—budget 曲线；
- [ ] 多 evaluator 复核；
- [ ] 结果写入 experiment decision records。

## v2：当前主线的机制 Gate

### Gate 1：任务必要性

验证 single-reference/energy-only 与 basin coverage 的错位。

### Gate 2：集合级目标

比较 no training、energy-only、entropy、archive 和 basin-aware objective。

### Gate 3：轨迹信息

比较 endpoint、noise、off-equilibrium 与真实 trajectory。

### Gate 4：离散全局假设

比较 retrieval、rules、small Transformer、LLM 与 oracle \(z\)。

### Gate 5：evaluator robustness

第二 MLIP、DFT 和 phonon representative subset。

只有通过的模块进入联合模型。

## 长期维护

- 每月：核验 watchlist 与 2026 论文版本；
- 每个新项目：先建 direction audit 和 falsification sheet；
- 每个重要实验：建 experiment decision record；
- 每次写论文：更新 Claim–Evidence Ledger；
- 每次判断变化：记录旧结论、新证据和边界变化。
