# MatterGen之后的三篇子刊案例

## 28. Chemeleon：文本引导化学空间探索

Nature Communications 16, 4379 · 2025

将组成与晶系的文字要求转成候选，再用物理计算判断材料资格

**数据。** MP-40：32,525个结构，≤40原子；按时间留出708个测试结构

**条件表示。** 组成与晶系生成文本；Crystal CLIP对齐文本与晶体图，FiLM/CFG将条件传入去噪器

**生成基座。** DiffCSP式周期等变扩散：联合生成元素、坐标与晶格；原子数另行给定

**AI评测。** 每题20次采样；一般文本下参考结构恢复率由6%升至20%（BERT与Crystal CLIP对照）

**物理案例。** Li–P–S–Cl：SMACT选组成，MACE预筛，DFT相图；四个选定四元结构声子无虚频

文本接口把组成和结构偏好放在同一句描述里；本文实证主要是化学式与晶系。MP2023.11.01的32,525个结构来自实验记录：原胞≤40原子、E_hull<0.25 eV/atom、边长≤20 Å，剔除常温气体。2018年8月2日后的708条作为未来测试。GPT-3.5按组成与晶系为每结构生成五种改写。
模型先对齐材料BERT和晶体图嵌入，再以FiLM和CFG输入DiffCSP式去噪器。每题给文本和原子数、采20次；一般文本的参考恢复率为BERT 0.06、Crystal CLIP 0.20。计量为软条件。
应用先用SMACT挑781种Li–P–S–Cl组成，再采样、MACE预弛豫和预筛、VASP/PBE相图计算。原文报告相对原MP参考包17个更低能及435个E_hull<0.15 eV/atom候选，前者含二/三元相，部分含分子片段或空穴；并入新包后Fig.5a的250个四元亚稳结构是另一统计。四个选定四元结构用PBEsol/PhononMaker计算声子，无虚频。Table1中metastability是未弛豫MACE与同组成参考真值的能量差窗口，按原文单列。

[Park, H., Onwuli, A. & Walsh, A. Exploration of crystal chemical space using text-guided generative artificial intelligence. Nature Communications 16, 4379 (2025). DOI:10.1038/s41467-025-59636-y.](https://www.nature.com/articles/s41467-025-59636-y)

## 29. SCIGEN：把功能图案嵌入晶体

Nature Materials 25, 223–230 · 2025在线发表／2026卷期

把与电子行为相关的原子排列作为条件，生成与之兼容的完整材料

**基座与规模。** 复用MP-20训练的DiffCSP；约千万提案经预筛后，选26,000个做DFT

**约束方法。** 每步把带噪图案按mask并入去噪状态，约束目标子晶格，补全周围原子与晶胞

**结构筛选。** 残余力与小畸变筛选、MP-20外新颖性和批内去重后，保留3,018个结构

**电子功能。** Lieb图案候选的DFT能带出现费米能附近平带，建立几何与电子行为的联系

**实验验证。** Ti–Pd–Bi/Sb提案指导合成；实物计量与占位变化，磁性为顺磁／抗磁，输运为金属

晶格几何影响电子跳跃和磁性挫折。SCIGEN以三角、蜂窝、kagome、Lieb层为外部结构条件：每步先给图案加入当前噪声，再与自由部分按mask合并，用既有DiffCSP继续去噪，无需为图案重新训练底座。
正式论文Data availability报告1,006万生成、101万预筛，从中选26,000个做DFT；24,743得到弛豫输出。SI §12/Table3按残余力、小畸变、MP-20外及去重进一步保留3,018。这个统计检验结构保持和新颖性，其物理定义与凸包SUN分开。
Lieb候选的DFT平带在费米能上方约0.1–0.2 eV；材料Ce3NaTb4、CeDy3NdYb见arXiv:2407.04557v1 Fig.4。实验选材结合化学判断：TiPdBi三角图案与TiPdSb方格图案提示Ti–Pd–Bi/Sb探索；衍射精修得到TiPd0.22Bi0.88与Ti0.5Pd1.5Sb，出现无序、计量及空间群变化。SQUID分别显示顺磁／抗磁，四探针电阻率显示金属，约2 K未见超导。来源为正式SI §10.1–10.7。
正式SI：https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41563-025-02355-y/MediaObjects/41563_2025_2355_MOESM1_ESM.pdf
Lieb原始能带：https://arxiv.org/html/2407.04557v1

[Okabe et al. Structural constraint integration in a generative model for the discovery of quantum materials. Nature Materials 25, 223–230 (2026); published online 22 September 2025. DOI:10.1038/s41563-025-02355-y.](https://www.nature.com/articles/s41563-025-02355-y)

## 30. Chemeleon2：用物理奖励改变生成分布

Nature Machine Intelligence 8, 1087–1099 · 2026

在连续潜空间中用GRPO优化近凸包资格、新颖性和多样性

**模型与物理反馈。** VAE编码晶体，DiT在潜空间生成。
GRPO用物理与多样性奖励
更新去噪策略。

**收益与结构覆盖。** N：62.3% → 97.5%
U：99.4% → 88.7%
生成收益伴随唯一性下降

**性质条件与物理检验。** 目标带隙3 eV，512个候选中82个同时满足mSUN和2.7–3.3 eV带隙（DFT）。

Chemeleon2先以VAE把元素、位置、晶格编码为连续潜变量，再训练latent DiT；GRPO将去噪步骤作为策略轨迹。奖励来自MACE-MPA-0估计的凸包能量差、AMD距离描述的新颖性/唯一性、以及组成和结构嵌入的批次多样性。
Fig.3在Alex-MP-20训练后每模型生成10,000个原始结构，不进行几何优化；mSUN要求E_hull<0.1 eV/atom。图中15.9→61.3是同一Chemeleon2基座加入RL前后的比较；metastability为51.2→72.1，N为62.3→97.5，U为99.4→88.7。
Fig.6使用43,295个带隙标签，目标3 eV，每模型512样本；RL样本中82个同时具有mSUN资格与2.7–3.3 eV的DFT带隙。原始样本mSUN为45.3%；附录另报告DFT弛豫后mSUN 60.8%、metastability 85.5%。1,000个结构的MLFF/DFT能量比较见Supplementary Fig.21。这里体现奖励改变生成能力和目标命中，原始势模型协议与MatterGen的弛豫DFT协议各自保留。

[Park, H. & Walsh, A. Guiding generative models to uncover diverse and novel crystals via reinforcement learning. Nature Machine Intelligence 8, 1087–1099 (2026). DOI:10.1038/s42256-026-01262-4.](https://www.nature.com/articles/s42256-026-01262-4)
