# Claim–Evidence Matrix：晶体生成论文能声称到哪一层

> [返回晶体索引](../README.md) · 更新时间：2026-09-03

## 1. 使用原则

论文中的 claim 应形成偏序：

\[
\text{实现正确}
\prec
\text{benchmark 改善}
\prec
\text{机制成立}
\prec
\text{物理质量提高}
\prec
\text{科学发现}
\prec
\text{实验可实现}
\]

低层证据不能自动支撑高层结论。

---

## 2. 常见 claim 与最低证据

| Claim | 最低直接证据 | 危险替代解释 | 必要反证实验 | 不能由此推出 |
|---|---|---|---|---|
| 生成结构更有效 | 统一 parser/几何规则下 validity | 更强后处理、规则更宽松 | 固定后处理；失败类型分解 | 更稳定、更可合成 |
| Match Rate 更高 | 相同 split、容差、采样数和统计 | 同组成/原型泄漏，reference 单一 | polymorph-aware split；容差曲线 | 更会搜索势能面 |
| RMSD 更低 | 等价晶胞/置换归一后的连续误差 | 只拟合 reference，丢失其他 basin | reference set + basin coverage | 能量更低 |
| SUN 更高 | 相同稳定/unique/novel evaluator | 阈值效应、MLIP 偏差、替换 novelty | cSUN、第二 MLIP、substitution audit | 动力学稳定、实验成功 |
| 初始力更低 | 独立 force evaluator | 只学 pre-relaxation | 相同 relaxer 后 basin coverage | 跨 basin 搜索更强 |
| 弛豫能量更低 | 统一 relaxer、同候选预算 | 更多 relax steps，单一 MLIP hacking | 双 MLIP/DFT、调用预算 | 多晶型覆盖更高 |
| \(E_{\mathrm{hull}}\) 更低 | 新结构 DFT/可信 MLIP 能量 + 同化学系统凸包 | 用已知 composition 条目代替新结构能量 | DFT + 竞争相完整性 | 可合成、无虚频 |
| 生成更多多晶型 | 弛豫后 basin 聚类与低能窗口 | 初始几何差异、聚类阈值 | 多口径聚类、DFT/人工边界审查 | 覆盖了所有真实相 |
| 多样性更高 | 多层 diversity，尤其 relaxed basin | pairwise 指纹高但同一 basin | 弛豫后 archive | 质量或 novelty 更高 |
| 结构更新颖 | duplicate + substitution + prototype + topology 分层 | 元素替换、等价晶胞、训练记忆 | time split、专家/拓扑审计 | 新材料或新机理 |
| 动力学更稳定 | 声子/曲率验证 | MLIP/超胞数值误差 | DFT phonon、参数敏感性 | 可合成 |
| 性质条件更准确 | 独立 property oracle | 同源 predictor exploitation | 第二 predictor/DFT/experiment | 稳定或新颖 |
| LLM 提供化学推理 | 对 reasoning 变量的干预；超过检索/小模型 | 训练记忆、warm start、参数量 | shuffle/error intervention；OOD | LLM 理解物理 |
| Diffusion 理解势能面 | 轨迹/force 干预与 basin transition 证据 | score 只是数据密度 | score-force 对齐、真实轨迹、DFT | 去噪轨迹是物理动力学 |
| SI/Flow 更适合晶体 | controlled path/base/NFE 比较 | backbone/solver/数据差异 | 同网络只换路径 | 更物理、更稳定 |
| RL 实现自提升 | 独立 evaluator 与多轮外部新标签 | reward hacking、rejection 效应 | 等预算 best-of-N；DFT 回流 | 获得新科学知识 |
| 模型像 CSP 搜索器 | 固定物理预算下低能 basin discovery curve | 更贵筛选、更多候选 | 传统 CSP/原型/随机同预算 | 通用 CSP 已解决 |
| 模型具有 amortized efficiency | 训练成本 + 每任务成本 + break-even | 忽略预训练/数据/筛选成本 | 随任务数累计成本曲线 | 单个任务更便宜 |
| 发现新材料 | 严格 novelty + DFT/更高层验证 | 已知原型替换、oracle 误差 | prospective blind validation | 可规模化合成 |
| 发现新科学机制 | 可解释规律、反事实和独立验证 | 事后故事、相关性 | 新体系预测与实验/DFT验证 | 普遍定律 |

---

## 3. 论文写作中的三种句子必须分开

### Observation

> 在固定 MLIP-A、候选数 100 和给定 split 下，本方法的平均弛豫能量下降。

这是数据事实。

### Mechanistic inference

> 我们推测该下降来自轨迹监督改善了 basin 内局部修正。

这是需要消融和干预支持的推断。

### Scientific interpretation

> 模型学会沿真实势能面搜索稳定结构。

这是更强解释，需要 force、trajectory、basin 和 DFT 证据；通常不能由第一句直接推出。

---

## 4. Claim ledger 模板

| ID | Claim | 层级 | Primary evidence | Falsifier | Independent audit | Status |
|---|---|---|---|---|---|---|
| C1 |  | benchmark |  |  |  | planned |
| C2 |  | mechanism |  |  |  | planned |
| C3 |  | physics |  |  |  | planned |
| C4 |  | discovery |  |  |  | planned |

状态只允许：

- `planned`
- `supported`
- `partially_supported`
- `falsified`
- `out_of_scope`

不允许使用“基本证明”“趋势较好”等模糊状态。

---

## 5. 当前多势阱主线的 claim 门槛

### C1：任务定义有必要

证据：

- 单参考指标与 basin coverage 的不一致；
- energy-only reward 的 coverage 损失；
- polymorph-aware 数据统计。

反证：

- 若单参考/energy-only 与物理 basin coverage 高度一致，重新定义任务的必要性下降。

### C2：集合级目标有效

证据：

- 等最佳能量或等预算下 unique low-energy basin 增加；
- 多种 basin 口径稳健；
- 不依赖单一 evaluator。

反证：

- entropy/diversity 简单基线同效；
- 增益只来自更多采样。

### C3：global/local 分工成立

证据：

- 中间状态分支熵；
- 模块干预；
- \(z\) 对 basin 的条件互信息；
- local repair 对力/弛豫步数的独立影响。

反证：

- 模块交换或删除不影响对应指标；
- 时间阶段职责不稳定。

### C4：LLM 有独立贡献

证据：

- 超过 retrieval、规则和参数量匹配小模型；
- OOD 下保持；
- reasoning/structured proposal 干预。

反证：

- 小模型同效；
- 只提供数据库记忆；
- \(z\) 不预测 basin。

### C5：物理提升真实

证据：

- 第二 MLIP；
- DFT；
- uncertainty；
- phonon representative subset。

反证：

- evaluator shift 后优势消失。

---

## 6. 写作检查

每个摘要句子应能回答：

- 它属于哪一个 claim 层级？
- 表中的哪项证据直接支持？
- 哪个最危险实验会推翻它？
- 是否把“observed under evaluator”误写为“physical truth”？
- 是否把“not in database”误写为“new structure”？
- 是否把“reward optimized”误写为“self-improving science”？

若无法定位证据，删除或降级表述。
