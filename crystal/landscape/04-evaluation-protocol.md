# 晶体生成与 CSP 的评价协议

> [返回晶体索引](../README.md) · 版本：v1.0 · 2026-09-03  
> 目标：让“方法提升”能被解释为 proposal、搜索、物理质量或科学发现中的具体变化，而不是 evaluator 与后处理差异。

## 1. 先声明任务

实验报告第一行必须从下列任务中选择，不能只写 “crystal generation”：

- **T1 De novo generation**
- **T2 固定组成单参考结构恢复**
- **T3 固定组成多晶型 / 多势阱 CSP**
- **T4 性质条件逆向设计**
- **T5 实验测量条件下的结构后验**
- **T6 结构预弛豫 / local repair**
- **T7 组成生成**

每项实验必须说明：

```text
Input:
Output:
Oracle:
Budget:
Data split:
Success unit:
Scientific claim:
```

---

## 2. 统一系统边界

所有方法都应被拆成：

\[
\text{proposal}
\rightarrow
\text{dedup}
\rightarrow
\text{relaxation}
\rightarrow
\text{evaluation}
\rightarrow
\text{selection}
\]

### 2.1 Proposal

记录：

- 模型与 checkpoint；
- 训练数据；
- 条件信息；
- temperature/guidance；
- 每个 composition 的原始样本数；
- 采样 NFE / token 数；
- 是否访问数据库或检索库；
- 随机种子。

### 2.2 Dedup

至少报告两次：

1. **弛豫前去重**；
2. **弛豫后 basin 去重**。

只在初始结构上计算 diversity 会高估有效搜索覆盖。

### 2.3 Relaxation

统一：

- MLIP/DFT；
- 优化器；
- cell/position 自由度；
- force/stress tolerance；
- 最大步数；
- 失败处理；
- 是否使用 symmetry constraint。

### 2.4 Evaluation

训练 reward、候选筛选器和最终审计器应尽可能不同：

\[
E_{\mathrm{train}}
\neq
E_{\mathrm{select}}
\neq
E_{\mathrm{audit}}
\]

至少保留一个完全冻结、训练时不可访问的独立 evaluator。

### 2.5 Selection

记录：

- top-\(K\) 规则；
- 是否按能量、uncertainty、novelty 或 ensemble 排序；
- 是否每个组成采用相同配额；
- 是否删除高不确定样本；
- 是否在测试时使用 reference。

---

## 3. 数据划分

### 3.1 最低要求

- 去除精确重复；
- 统一结构标准化；
- 记录 composition overlap；
- 记录 prototype overlap；
- 记录 substitution relation；
- 记录多晶型数量；
- 记录数据时间截断。

### 3.2 建议的四层 split

| Split | train/test 关系 | 测量能力 |
|---|---|---|
| ID-random | 随机划分 | 数据拟合与实现 sanity |
| composition-disjoint | 测试组成未见 | 组成条件泛化 |
| prototype-disjoint | 测试结构家族未见 | 新拓扑/结构模式泛化 |
| chemistry-OOD | 元素组合/化学族外推 | 真正材料外推 |

### 3.3 Polymorph-aware split

同一组成的多晶型必须整体处理，或明确构造：

- train 中已见组成但隐藏某些多晶型；
- test 中参考集合而非单一 reference；
- reference multiplicity；
- 数据库不完整性标记。

随机划分的结果只能支持 ID 拟合，不能支撑真实 CSP claim。

### 3.4 Time split

若要声称发现：

- 以数据库发布日期构造 cutoff；
- 训练只使用 cutoff 前结构；
- 测试使用 cutoff 后新增结构；
- 仍需排除早期论文/其他数据库泄漏；
- 记录模型预训练语料可能访问的结构文本。

---

## 4. 强基线

## 4.1 所有生成任务的最低基线

- 训练集随机采样；
- 最近邻检索；
- composition-matched prototype retrieval；
- 电荷平衡原型枚举；
- 离子/元素替换；
- 随机合法结构；
- 相同 evaluator 下的 rejection sampling；
- best-of-\(N\)。

## 4.2 固定组成 CSP

还应包括：

- AIRSS 或等价随机结构搜索；
- USPEX/CALYPSO 等传统 CSP（可在代表子集）；
- 相同初始 proposal + 统一 relaxer；
- 生成模型无后训练；
- energy-only 后训练；
- entropy/diversity baseline；
- archive/QD baseline。

## 4.3 LLM 模块

必须比较：

- 无 LLM；
- 结构检索；
- 规则原型；
- 小型普通 Transformer；
- 参数量匹配模型；
- 打乱/随机 reasoning；
- 错误条件干预；
- oracle 中间变量。

## 4.4 物理轨迹模块

必须比较：

- 只用稳定终点；
- 等量随机噪声；
- 独立非平衡结构；
- 真实弛豫轨迹；
- energy only；
- energy + force；
- energy + force + stress；
- 外部 relaxer，无生成模型更新。

---

## 5. 预算对齐

不同方法的真实成本包括：

\[
C
=
C_{\mathrm{train}}
+
C_{\mathrm{sample}}
+
C_{\mathrm{MLIP}}
+
C_{\mathrm{DFT}}
+
C_{\mathrm{phonon}}
+
C_{\mathrm{human}}
\]

### 5.1 至少报告四个预算口径

1. 原始候选数；
2. 生成/采样 NFE 或 token FLOPs；
3. MLIP energy/force 调用数；
4. DFT/phonon 调用数。

### 5.2 Discovery curve

不要只在一个预算点报告：

\[
\mathrm{Coverage}(B)
\]

应绘制：

- unique low-energy basin vs oracle calls；
- best energy vs oracle calls；
- target property successes vs cost；
- DFT-confirmed candidates vs cost；
- wall-clock 与 GPU-hour。

### 5.3 Amortized efficiency

若训练成本为 \(C_{\mathrm{train}}\)，每个新 composition 的搜索成本为 \(c_\theta\)，传统方法为 \(c_{\mathrm{search}}\)，需报告 break-even：

\[
N^*
=
\frac{C_{\mathrm{train}}}
{c_{\mathrm{search}}-c_\theta}
\]

否则不能笼统声称 amortized efficiency。

---

## 6. 指标分层

## 6.1 表示与几何合法性

- 可解析结构比例；
- 原子重叠；
- 体积/密度范围；
- composition consistency；
- symmetry consistency；
- 晶胞退化；
- charge/oxidation-state plausibility。

这些只说明结构格式和几何基本合法，不说明稳定。

## 6.2 参考结构恢复

- Match Rate；
- conditional Match Rate；
- RMSD / cRMSE；
- top-\(K\) recovery；
- METRe 或集合级参考覆盖；
- 不同容差敏感性。

必须同时报告 reference multiplicity 与 split。

## 6.3 热力学与局部弛豫

- 初始/弛豫后能量；
- 最大力；
- 最大应力；
- 弛豫收敛率；
- 弛豫步数；
- 形成能；
- \(E_{\mathrm{hull}}\)；
- 两种 MLIP 排名一致性；
- DFT 验证。

### \(E_{\mathrm{hull}}\) 注意

组成只确定竞争相约束；生成结构的能量必须由具体结构评估。  
不能从 Materials Project 中按 composition 查到的已知条目直接替代新结构的 \(E_{\mathrm{hull}}\)。

## 6.4 动力学稳定

- 最低声子频率；
- 虚频模数量/强度；
- PhononScore 等低成本代理；
- DFT phonon 子集；
- 超胞与收敛敏感性；
- 必要时有限温度 MD。

“无虚频”仍不等于可合成。

## 6.5 多势阱覆盖

先定义弛豫后 basin：

\[
b_i
=
\mathrm{Cluster}(R(s_i))
\]

指标：

- unique basin count；
- low-energy unique basin count；
- coverage@\(K\)；
- pass@\(K\)；
- energy-weighted coverage；
- basin entropy；
- duplicate-to-basin ratio；
- marginal new basin per sample；
- coverage AUC vs budget。

### Basin 聚类最少需要

- StructureMatcher / equivalent cell normalization；
- 配位/拓扑指纹；
- 能量窗口；
- 对边界样本做人工或 DFT 复核；
- 多组阈值敏感性。

## 6.6 新颖性

必须拆成层级：

| 层级 | 说明 |
|---|---|
| N0 | 非精确重复 |
| N1 | 非 StructureMatcher 重复 |
| N2 | 非元素替换派生 |
| N3 | 非已知 prototype |
| N4 | 新配位/连通拓扑或新结构 motif |
| N5 | DFT/实验确认的新稳定结构 |
| N6 | 带来新性质或科学机制 |

不要用 N1 支撑 N4–N6 的 claim。

## 6.7 多样性

分别报告：

- composition diversity；
- crystal-system/space-group diversity；
- prototype diversity；
- local coordination diversity；
- relaxed basin diversity；
- property diversity。

样本对距离高不等于 basin 多样。

## 6.8 逆向设计

- condition error；
- success rate；
- Pareto hypervolume；
- stability-conditioned success；
- novelty-conditioned success；
- DFT-confirmed yield；
- calibration / uncertainty；
- per-oracle-call discovery。

## 6.9 分布质量

- property distribution distance；
- element frequency；
- density/volume；
- symmetry；
- FID-like embedding distance；
- precision/recall for distributions；
- mode coverage。

任何 embedding metric 都必须说明编码器与训练数据，否则可能偏好同一表示族。

---

## 7. Evaluator robustness

## 7.1 双模型协议

最低配置：

- **Evaluator A**：训练/筛选；
- **Evaluator B**：冻结独立审计；
- **DFT subset**：代表样本。

报告：

\[
\rho(E_A,E_B),\quad
\rho(E_A,E_{\mathrm{DFT}})
\]

以及 top-\(K\) overlap 和 ranking flip。

## 7.2 不确定性分层

把样本分成：

- 高分、低不确定；
- 高分、高不确定；
- 低分、低不确定；
- 低分、高不确定。

若后训练把大量概率移到“高分、高不确定”区域，优先怀疑 reward exploitation。

## 7.3 Prospective audit

最终 DFT 子集不能只选 evaluator 最喜欢的样本；应包含：

- top reward；
- high uncertainty；
- novel basin；
- random control；
- baseline top candidates；
- 失败/边界样本。

---

## 8. 统计与重复性

### 8.1 随机性

至少记录：

- 训练种子；
- 采样种子；
- split 种子；
- relaxer 初始化；
- evaluator 版本。

### 8.2 置信区间

对比例指标使用 bootstrap 或适当二项区间；  
对 composition 分组的结果，bootstrap 单位应是 composition，而非把所有样本当独立。

### 8.3 配对比较

同一 composition 下比较方法，优先使用 paired effect：

\[
\Delta_i
=
M_i^{(A)}-M_i^{(B)}
\]

并报告：

- 均值/中位数；
- 置信区间；
- 胜率；
- chemistry subgroup；
- worst-group。

### 8.4 多重比较

大量指标和 ablation 时，预先指定 primary endpoint，避免只挑显著结果。

---

## 9. 主结果表的建议结构

### 9.1 固定组成多势阱 CSP

| Method | Proposal cost | MLIP calls | DFT calls | Best energy | Unique low-E basins | Coverage@K | DFT pass | Phonon pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|

### 9.2 De novo

| Method | Valid | Stable-A | Stable-B | DFT stable | N2 novelty | N4 novelty | Basin diversity | Cost |
|---|---:|---:|---:|---:|---:|---:|---:|---:|

### 9.3 LLM contribution

| Proposal | Params | Retrieval access | Basin info | Local quality | Coverage | OOD | Cost |
|---|---:|---|---:|---:|---:|---:|---:|

---

## 10. 必须报告的反证结果

即使结果不利，也要保留：

- 哪些组成下方法不如简单基线；
- 哪些候选跨 evaluator 翻转；
- 哪些 novelty 其实是 substitution-derived；
- energy reward 是否降低 coverage；
- force guidance 是否只减少弛豫步数；
- 对称约束遗漏了哪些低对称 basin；
- LLM 是否与小模型相同；
- 增益是否随预算消失。

负结果决定适用边界，是论文可信度的一部分。

---

## 11. Claim 门槛

### 可以声称“改善 benchmark”

需要：

- 统一 split/代码/采样；
- 统计重复；
- 明确 primary metric。

### 可以声称“核心机制有效”

还需要：

- 危险基线；
- 反事实消融；
- 控制数据、规模、计算；
- 机制变量的直接测量。

### 可以声称“物理质量提高”

还需要：

- 独立 MLIP；
- DFT；
- 必要时 phonon；
- evaluator uncertainty。

### 可以声称“更会 CSP 搜索”

还需要：

- 多势阱输出；
- 同预算传统搜索；
- 弛豫后 basin coverage；
- discovery curve；
- OOD composition/prototype。

### 可以声称“发现新材料”

还需要：

- substitution/prototype-aware novelty；
- DFT 或更高层验证；
- 对竞争相和动力学稳定的分析；
- 最好有 prospective/实验验证；
- 清楚区分新组成、新结构、新性质和新机理。

---

## 12. 最小协议与完整版

## 12.1 最小可行协议

用于早期 idea 筛选：

1. polymorph-aware 小测试集；
2. 原型/离子替换/随机/无模块基线；
3. 相同候选数和 MLIP 调用；
4. 弛豫后 basin 去重；
5. energy—coverage 曲线；
6. 第二 MLIP 小批复核；
7. 一个杀手实验。

## 12.2 论文级协议

在最小协议上增加：

- 多数据集与 OOD split；
- 完整预算曲线；
- 多 seed；
- DFT representative subset；
- substitution-aware novelty；
- phonon subset；
- active/evaluator uncertainty；
- 传统 CSP；
- claim ledger；
- 失败案例和边界。

---

## 13. 实验登记表

每个实验提交前填写：

```yaml
task:
scientific_question:
hypothesis:
falsification:
dataset:
split:
proposal_models:
strong_baselines:
relaxer:
train_evaluator:
selection_evaluator:
audit_evaluator:
candidate_budget:
mlip_call_budget:
dft_budget:
primary_endpoint:
secondary_endpoints:
basin_definition:
novelty_level:
seeds:
stop_condition:
allowed_claim_if_positive:
allowed_claim_if_negative:
```

没有该表的实验不进入论文主证据。
