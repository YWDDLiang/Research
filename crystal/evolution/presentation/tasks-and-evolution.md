# 晶体生成：任务、挑战与路线的文献演化

2026年10月12日。配套30页学术汇报。共同主目标是自主生成中的严格SUN，条件任务用于定位与迁移各路线的能力。

演化表连接的是问题与能力。只有原文确认的方法采用，才在备注中写为直接继承。晶体任务证据、方法基础、评价依据与跨领域启发各自标明。

## 8. C1：科学条件怎样得到正确结构

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2019–2022<br>iMatGen、FTCP、CDVAE | 性质逆设计、结构重构<br>目标性质或潜变量输入 | 建立可解码的周期表示。问题转向目标条件能否在完整结构中实现。 |

| 2024–2025<br>Crystal-LLM、TGDMat、Chemeleon | 文本 / 描述条件生成<br>描述输入，晶体输出 | 把化学及结构描述接入生成。条件中哪些关系得到落实成为新问题。 |

| 2025–2026<br>MatterGen、SCIGEN、PLaID++ | 性质或结构图案约束<br>生成并进行物理评价 | 获得条件候选及物理验证。多种要求的兼容与未见组合继续限制发现。 |

当前任务：同时检验条件命中与稳定新结构数量。主要导向A，并支持B。

任务演化为本综述综合，不把同一行方法视为直接继承。FTCP在具体性质目标中验证逆设计，CDVAE包括生成与性质优化。MatterGen将化学/性质条件接入联合扩散；SCIGEN将结构图案约束接入DiffCSP式生成。TGDMat与Chemeleon支持文本条件，PLaID++支持结构语言与偏好条件设计。MatterGen稳定阈值0.1与本项目严格阈值分别保留。

文献：[R06 imatgen](https://doi.org/10.1016/j.matt.2019.08.017)；[R07 ftcp](https://arxiv.org/pdf/2005.07609v3)；[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R21 crystal_llm](https://arxiv.org/abs/2402.04379)；[R37 TGDMat](https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html)；[R39 Chemeleon](https://www.nature.com/articles/s41467-025-59636-y)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)。

## 9. C2：耦合选择怎样形成和修订

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2022–2024<br>CDVAE、DiffCSP、FlowMM | 周期生成与组成CSP<br>联合生成晶胞和坐标 | 学习几何变量之间的依赖。进一步需要处理元素与几何的相互依赖。 |

| 2024–2025<br>FlowLLM、MatterGen、OMatG | DNG及分阶段生成<br>同时提出化学和结构 | 联合生成与组成先行都有效。问题转为两种组织何时各有优势。 |

| 2025–2026<br>CrysBFN、MCFlow、ANCHOR | 组成CSP、互条件完成<br>冻结CSP的组成探索 | 独立信息进度与组成策略均能改善任务。需要辨认哪类决定值得回改。 |

当前任务：在相同组成和数据条件下，判断几何信息是否改善化学选择。导向A。

FlowMM复用DiffCSP网络并改变生成过程。FlowLLM结合Crystal-LLM与FlowMM。MCFlow的独立模态时间处理多种条件推断；H.8匹配率45.58%与63.14%是CSP接口比较。ANCHOR冻结结构先验并改变组成分布，提供组成策略可能解释增益的强参照。概率分解本身可表示联合分布，当前问题在有限学习条件下的信息利用。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R33 crysbfn](https://arxiv.org/abs/2502.02016)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 10. C3：局部化学怎样组成周期整体

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2018–2023<br>CGCNN、M3GNet、CHGNet | 性质、能量、力的预测<br>完整结构输入 | 局部环境能支持物理预测。需要进一步研究如何用这些知识构造结构。 |

| 2023–2025<br>SLICES、SymmCD、Wyckoff | 周期图解码、对称DNG<br>关系或非等价位点输入 | 把周期连接和对称关系纳入生成。多个局部要求仍共享原子与晶胞。 |

| 2025–2026<br>SCIGEN、Composable、UFO-MGen | 图案约束、概念组合<br>给定配置的结构完成 | 已能组合概念并完成条件结构。下一步区分局部知识与模板信息，识别必要的全局条件。 |

当前任务：固定已学局部环境，改变化学或连接组合，检验整体稳定性。导向B。

CGCNN和MLIP是知识背景，不是组合生成结论。SymmCD和Wyckoff方法学习/构造对称配置。Composable Crystals的邻域concept含坐标及晶格信息，因此concept有效不能独自归因于纯局部化学。UFO-MGen的未见配置试验提供给定scaffold的条件完成证据。晶体局部环境共享原子、边和晶格，需要共同计量和几何实现。

文献：[R05 CGCNN2018](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301)；[R10 M3GNet2022](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R16 slices](https://www.nature.com/articles/s41467-023-42870-7)；[R35 symmcd](https://arxiv.org/abs/2502.03638)；[R36 wyckoffdiff](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html)；[R38 wyckoff_transformer](https://arxiv.org/abs/2503.02407)；[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals](https://arxiv.org/html/2605.14769v2)；[R55 UFO-MGen](https://arxiv.org/html/2609.26547v1)。

## 11. C4：物理反馈怎样改变有效的决定

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2006起<br>USPEX、AIRSS | 指定体系的结构搜索<br>提案后进行物理弛豫 | 能量评价帮助寻找低能结构。每个新体系仍需搜索，经验复用有限。 |

| 2023<br>RL-CSP | 组成条件的搜索决策<br>学习basin-hopping动作 | 根据结果改进动作分布。问题扩展到预训练生成器中的有效选择。 |

| 2025–2026<br>MatInvent、OMatG-IRL、GSS | 性质DNG、CSP后训练<br>生成先验结合物理力 | 奖励或力能改变生成过程。还需理解什么反馈在何种状态下改变终点。 |

当前任务：比较具体结构变化及其完整后果，建立反馈与终点增益的联系。导向C。

物理搜索、改变动作分布、后训练生成模型和推理时引导是不同反馈对象。MatInvent以MatterGen为默认基座，OMatG-IRL更新SI生成场，GSS将先验与物理力用于采样/搜索。当前研究从反馈存在推进到反馈何时能够支持有益的有限决定。项目PDE18零strict gain/loss为相关内部观察，不能外推为所有反馈无效。

文献：[R01 AIRSS2006](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504)；[R02 USPEX2006](https://doi.org/10.1063/1.2210932)；[R14 rlcsp](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R48 irl](https://arxiv.org/html/2602.00424v2)；[R50 gss](https://arxiv.org/html/2604.27636v2)。

## 12. C5：怎样发现并保留不同的合格结果

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2021–2023<br>GFlowNet Foundations | 通用多模态奖励采样<br>奖励定义的终态空间 | 学习按奖励比例采样多个结果。晶体中还需要定义物理资格和身份。 |

| 2024–2026<br>晶体QD、SHAFT | 固定组成的性质覆盖<br>层级对称材料生成 | 用档案或层级策略保留多解。开放化学空间的成功类别继续增加。 |

| 2025–2026<br>PLaID++、Chemeleon2、ANCHOR | 稳定 / 新颖后训练<br>依发现历史探索组成 | 开始联合改变资格与搜索分布。新增成功、重复及遗忘需要分别解释。 |

当前任务：按弛豫后的结构身份，统计首次发现、学会再生成和后续新发现。导向D。

GFlowNet Foundations首稿2021、JMLR2023。QD的性质档案针对选定组成；SHAFT以层级对称选择生成材料，其原文mode资格与严格SUN分开。PLaID++表征/后训练、Chemeleon2的latent RL与ANCHOR组成探索分别改变不同因素。稳定性、多样性和新颖性联合优化已有方法，研究需落在未知合格结果的持续获得与保持。

文献：[R09 gflownet](https://jmlr.org/papers/v24/22-0364.html)；[R23 qd](https://arxiv.org/html/2403.03511v1)；[R30 shaft](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 13. C6：物理计算怎样积累成生成能力

| 演化阶段与论文 | 原文任务 | 已有进展及推进的问题 |

| --- | --- | --- |

| 2013–2023<br>Materials Project、GNoME | 数据库积累、主动学习<br>新计算更新预测模型 | 计算结果跨材料复用。下一步是让信息直接帮助生成选择。 |

| 2025–2026<br>MatInvent、PLaID++、Chemeleon2 | 性质或物理资格后训练<br>终点评价更新生成器 | 计算开始进入模型权重。需要分辨端点记忆与可迁移的结构知识。 |

| 2026<br>OMatG-IRL、flash、ANCHOR | 条件训练后的DNG<br>少步生成、结构语料学习 | 能力可跨任务或采样阶段使用。仍需辨认哪些信息改善新的材料请求。 |

当前任务：控制终点数据与物理投入，检验额外关系信息的迁移价值。导向C和D。

GNoME是物理数据回流的先例，但不是扩散后训练。OMatG-IRL已有CSP式物理训练到DNG的证据。OMatG-flash直接采用RAM，关注少步生成映射。ANCHOR v2 F.6语料由访问组成重放形成，未按稳定/新颖阈值筛选。C关注学习的关系内容，D关注这些信息怎样扩大并保持成功分布。

文献：[R04 MaterialsProject2013](https://doi.org/10.1063/1.4812323)；[R18 GNoME2023](https://www.nature.com/articles/s41586-023-06735-9)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R48 irl](https://arxiv.org/html/2602.00424v2)；[R54 flash](https://arxiv.org/html/2609.26402v1)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 14. 四条路线分别回答什么任务问题

| 路线与挑战 | 主要科学问题 | 直接研究任务 |

| --- | --- | --- |

| A 化学与几何<br>C1、C2 | 双向信息何时改善化学与结构的配对？ | 主任务：自主DNG<br>定位任务：CSP / 互条件完成 |

| B 局部知识组合<br>C3，联系C1 | 局部要求怎样在同一周期结构中成立？ | 主任务：自主DNG<br>定位任务：图案 / 新连接生成 |

| C 从物理反馈学习<br>C4、C6 | 哪些结构响应可以帮助新的材料？ | 物理数据学习后的独立生成<br>跨组成与条件迁移 |

| D 持续多解发现<br>C5、C6 | 新成功怎样学入模型并支持进一步发现？ | 多轮预算内DNG<br>新结果保持与继续发现 |

共同主目标是严格SUN。条件任务分别定位四条路线要学习的能力。

路线A侧重信息利用与联合推断；B侧重组合泛化；C侧重物理关系迁移；D侧重未知成功集合的获得与保持。任务输入输出不同，四方向各自可以构成独立论文。

## 15. A的演化：联合几何到化学与几何协作

| 时间与支持论文 | 原文任务 | 为路线A提供的能力 |

| --- | --- | --- |

| 2022–2024<br>CDVAE、DiffCSP、FlowMM | DNG、组成条件CSP | 联合建模晶胞与位置，支持周期连续生成。 |

| 2024<br>Crystal-LLM、GenMS | 晶体文本生成<br>语言条件的层级搜索 | 语言组织化学提案，连续模型实现几何。 |

| 2024–2025<br>FlowLLM、CrysLLMGen | LLM提案后的几何精修 | 连续模型改善语言提案。连续阶段固定元素，为双向修订提供明确参照。 |

| 2025–2026<br>MatterGen、OMatG、MCFlow | 联合DNG、互条件生成 | 建立化学与几何共同建模及多条件路径，支持比较不同信息组织。 |

演化留下的问题：何时只需更好提案，何时几何证据能帮助改变化学选择？

直接继承：FlowMM采用DiffCSP网络；FlowLLM结合Crystal-LLM式LLaMA先验与FlowMM；CrysLLMGen复用Crystal-LLM提示及DiffCSP式连续模型。GenMS将语言到公式和公式到结构分解。MatterGen、OMatG、MCFlow属于联合/多模态分支，不写成FlowLLM的单线后继。

文献：[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R13 diffcsp](https://arxiv.org/abs/2309.04475)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[R21 crystal_llm](https://arxiv.org/abs/2402.04379)；[R28 GenMS](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)；[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 crysllmgen](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R19 mattergen](https://www.nature.com/articles/s41586-025-08628-5)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)。

## 16. A的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |

| --- | --- | --- |

| FlowLLM、CrysLLMGen<br>晶体混合模型 | 把语言提案接到连续几何生成 | LLM提出可修改的化学 / 占位选择，连续模型构造周期结构。 |

| OMatG、CrysBFN、MCFlow<br>混合变量生成 | 联合表示变量及其当前信息状态 | 让几何与元素更新读取共同状态，比较纯SI与LLM混合方案。 |

| NextStep-1 [T02]<br>文生图与编辑 | AR上下文预测连续token，flow输出细节 | 借鉴离散上下文与连续输出的分工，设计可交换的科学状态。 |

| SFD [T01]<br>ImageNet类别条件 | 分别推进语义与纹理的信息进度 | 借鉴相关变量的信息组织，研究化学和几何何时交换信息。 |

候选基座：LLM + Diffusion / SI。要新增的能力是内容相关的双向修订。

NextStep-1是连续token AR的图像方法，SFD主实验证据为ImageNet类别条件。迁移点是信息组织和方法接口。晶体需要保留元素、位置、晶胞及周期约束。双向信息的增量需与强分阶段和纯混合SI比较。

文献：[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R43 crysllmgen](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R33 crysbfn](https://arxiv.org/abs/2502.02016)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)；[T02 NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale](https://arxiv.org/abs/2508.10711)；[T01 Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion](https://arxiv.org/abs/2512.04926)。

## 17. A的研究任务与可检验主张

中心问题：逐渐形成的几何，能否帮助模型选择更合适的化学？

**主任务DNG。** 模型自主提出组成与结构。用同一弛豫和新颖性规则比较不同生成组织的SUN。

**能力定位。** 给定部分组成或结构，补全另一部分。测试未见的化学与结构组合，观察修订是否改善配对。

**关键比较。** 强组成模型+CSP、纯联合Diffusion / SI、LLM与连续模型双向交互。保持数据与总费用可比。

**论文结果。** 建立信息交换何时有用的规律，并在独立新组合和DNG中保留收益。

研究主张待验证：几何内容应能解释有益修订，而非仅依赖更多采样。互条件完成源于MCFlow，混合模型参照源于FlowLLM/CrysLLMGen，组成搜索参照源于ANCHOR。最终主结果是全独立DNG严格SUN，条件任务用于解释能力。

文献：[R28 GenMS](https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf)；[R29 flowllm](https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html)；[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R43 crysllmgen](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 18. B的演化：局部环境到新整体组合

| 时间与支持论文 | 原文任务 | 为路线B提供的能力 |

| --- | --- | --- |

| 2018–2023<br>CGCNN、M3GNet、CHGNet | 完整晶体的物理预测 | 说明局部环境包含可复用物理信息，提供知识来源与评价工具。 |

| 2022–2023<br>CDVAE、SLICES | 生成及可逆周期表示 | 支持整体结构生成和周期连接表达，使知识可以落实到结构。 |

| 2025<br>SymmCD、WyckoffDiff / Transformer | 对称配置生成与几何解码 | 用非等价位点组织共享约束，减少需要独立生成的自由度。 |

| 2025–2026<br>SCIGEN、Composable、UFO-MGen | 图案嵌入、概念组合<br>新配置条件完成 | 把指定关系嵌入晶体。进一步需要辨认组合成功所需的共同条件。 |

演化留下的问题：学到的局部规律，在改变连接、化学和晶胞后何时仍成立？

阶段表示问题推进，不声称所有工作直接继承。SLICES采用周期商图；Wyckoff Transformer的几何实现包括DiffCSP++解码；SCIGEN实际包装DiffCSP。Composable将邻域concept组合后交给条件DDPM。UFO-MGen采用离散配置与连续flow分工。预测知识的可生成性需要实验建立。

文献：[R05 CGCNN2018](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301)；[R10 M3GNet2022](https://www.nature.com/articles/s43588-022-00349-3)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R08 cdvae](https://arxiv.org/abs/2110.06197)；[R16 slices](https://www.nature.com/articles/s41467-023-42870-7)；[R35 symmcd](https://arxiv.org/abs/2502.03638)；[R36 wyckoffdiff](https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html)；[R38 wyckoff_transformer](https://arxiv.org/abs/2503.02407)；[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals](https://arxiv.org/html/2605.14769v2)；[R55 UFO-MGen](https://arxiv.org/html/2609.26547v1)。

## 19. B的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |

| --- | --- | --- |

| SLICES、SymmCD<br>周期关系与对称表示 | 表示周期连接与非等价位点 | 让多个局部条件指向同一组原子和晶胞。 |

| SCIGEN、Composable Crystals<br>条件扩散生成 | 把图案或concept接入全结构生成 | 组成多个结构要求，并通过周期Diffusion实现。 |

| MCFlow、UFO-MGen<br>条件flow生成 | 互条件完成，或给定配置生成几何 | 提供flow替代基座与新配置完成的比较。 |

| DynFusion / Local Mechanisms<br>多条件融合 / 组合泛化 | 融合不同视觉条件，或干预局部条件依赖 | 按条件内容组织交互，在晶体中保留共享原子和晶格关系。 |

候选基座：显式周期关系的条件Diffusion。新增能力是跨连接方式的稳定组合。

DynFusion §3.2从当前噪声状态预测条件mask，§4.1比较多个空间、主体及混合视觉条件。Bradley的理论针对特定条件组合结构，原实验为CLEVR长度泛化及自然图像探索。晶体中邻域重叠、原子共享、周期晶格与相竞争需要新的条件。方法贡献需说明共享关系怎样改变组合泛化。

文献：[R16 slices](https://www.nature.com/articles/s41467-023-42870-7)；[R35 symmcd](https://arxiv.org/abs/2502.03638)；[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R51 Composable Crystals](https://arxiv.org/html/2605.14769v2)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)；[R55 UFO-MGen](https://arxiv.org/html/2609.26547v1)；[T03 Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)；[T07 DynFusion: Rethinking Condition Fusion for Adaptive Multi-Conditional Text-to-Image Generation](https://wrap.warwick.ac.uk/id/eprint/197869/8/WRAP-DynFusion-rethinking-condition-fusion-multi-conditional-text-to-image-generation-26.pdf)。

## 20. B的研究任务与可检验主张

中心问题：熟悉的局部环境能否构成训练中未见的稳定整体？

**主任务DNG。** 模型自主提出组合方案并完成几何。评价严格稳定性和不同新结构数量。

**能力定位。** 给定多个配位或连接要求，生成同一周期结构。分别留出化学组合、连接方式或原胞复杂度。

**关键比较。** 离子替换 / 整结构检索、条件CSP、独立条件组合、共享周期关系建模。

**论文结果。** 说明共享条件怎样支持知识迁移，在未见组合与DNG中增加稳定新结构。

局部关系以统一邻接定义具体化。熟悉原型中的新稳定化学继续计入成功。复制超胞仅改变表示规模，不能当新整体结构。路线B主张待验证，不预设局部约束越多越好。各条件任务需在后处理后检查是否仍成立。

文献：[R27 SCIGEN](https://www.nature.com/articles/s41563-025-02355-y)；[R31 baselines](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)；[R49 MCFlow](https://proceedings.mlr.press/v306/seong26a.html)；[R51 Composable Crystals](https://arxiv.org/html/2605.14769v2)；[R52 novelty](https://arxiv.org/html/2606.23166v1)；[R55 UFO-MGen](https://arxiv.org/html/2609.26547v1)；[T03 Local Mechanisms of Compositional Generalization in Conditional Diffusion](https://proceedings.mlr.press/v306/bradley26a.html)。

## 21. C的演化：物理搜索到生成器学习

| 时间与支持论文 | 原文任务 | 物理反馈改变的对象 |

| --- | --- | --- |

| 2006–2023<br>AIRSS、USPEX、RL-CSP | 指定体系的低能结构搜索 | 先评价候选，再选择搜索动作。RL-CSP进一步学习动作分布。 |

| 2022–2025<br>CHGNet、GNoME、OpenCSP | 物理预测及压力CSP<br>新物理数据采集 | 计算扩展模型适用的结构和物理环境，主要改善预测与搜索基础。 |

| 2025–2026<br>MatInvent、PLaID++、Chemeleon2 | 性质DNG与物理资格优化 | 终点奖励或偏好开始更新生成器，而非仅筛选当前候选。 |

| 2026<br>OMatG-IRL、flash、GSS | CSP / DNG及少步生成<br>生成先验结合物理搜索 | IRL / flash更新生成场或映射，GSS在搜索中结合先验与物理力。 |

演化留下的问题：除了终点分数，哪些响应内容值得学入模型并迁移到新材料？

OpenCSP基于物理数据与并发学习研究压力CSP，截至原资料为2025预印本。MatInvent默认MatterGen，PLaID++是结构语言偏好训练，Chemeleon2是latent RL。OMatG-IRL基于SI，flash直接采用RAM。GSS主要是生成先验与物理势的混合搜索，不将其写作同一种生成器后训练。

文献：[R01 AIRSS2006](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504)；[R02 USPEX2006](https://doi.org/10.1063/1.2210932)；[R14 rlcsp](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R11 CHGNet2023](https://www.nature.com/articles/s42256-023-00716-3)；[R18 GNoME2023](https://www.nature.com/articles/s41586-023-06735-9)；[R41 opencsp](https://arxiv.org/html/2509.10293v1)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R48 irl](https://arxiv.org/html/2602.00424v2)；[R54 flash](https://arxiv.org/html/2609.26402v1)；[R50 gss](https://arxiv.org/html/2604.27636v2)。

## 22. C的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |

| --- | --- | --- |

| SI理论 [T08]、OMatG、FlowMM<br>连续分布与路径学习 | 学习连接分布的速度场，在周期空间生成结构 | 提供SI / flow基座，保留相同来源的多种可能终点。 |

| MatInvent、OMatG-IRL<br>晶体物理奖励后训练 | 用终点物理效用更新生成器 | 作为标量反馈的强参照，明确额外响应信息增加了什么。 |

| Flow-GRPO / RAM [T04–05]<br>图像生成后训练 | 用终点奖励训练flow / diffusion | 提供可实施的后训练目标。RAM已由OMatG-flash采用。 |

| GSS、CrystAF<br>物理引导 / 分子晶体packing | 比较生成先验、物理介入与修复 | 帮助区分当前样本修复与模型长期学习的作用。 |

候选基座：SI / flow。新增学习对象是结构变化、响应和终点之间的关系。

响应关系学习是当前路线的研究命题，而不是这些原工作已得出的共同结论。Flow-GRPO用在线策略梯度，RAM保持解析加噪回归形式并由终点奖励修正。CrystAF原对象是分子晶体，不用其packing结果充当无机SUN。

文献：[R34 omatg](https://proceedings.mlr.press/v267/hollmer25a.html)；[R26 flowmm](https://proceedings.mlr.press/v235/miller24a.html)；[T08 Stochastic Interpolants: A Unifying Framework for Flows and Diffusions](https://jmlr.org/papers/v26/23-1605.html)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R48 irl](https://arxiv.org/html/2602.00424v2)；[T04 Flow-GRPO: Training Flow Matching Models via Online RL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html)；[T05 Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2605.10759)；[R54 flash](https://arxiv.org/html/2609.26402v1)；[R50 gss](https://arxiv.org/html/2604.27636v2)；[R57 crystaf](https://arxiv.org/html/2609.36398v1)。

## 23. C的研究任务与可检验主张

中心问题：同样的物理投入，怎样帮助更多后续材料请求？

**主任务DNG。** 用物理数据训练后独立生成，检验新的材料请求能否受益。数据采集和训练成本同时计入。

**关系与迁移。** 学习同源结构改变的响应与后果，并在未见组成或条件上检验。

**关键比较。** 在线物理引导、成功端点训练、标量奖励后训练、保留变化与响应关系的训练。

**论文结果。** 辨认哪些物理信息可以迁移，并在计入数据采集和训练费用后提高SUN发现量。

对比保持终点池与物理投入可比，关系学习额外使用来源与实际变化的对应。模型需在新的请求中获益，不能仅重现训练终点。数值弛豫路径保留求解器依赖，生成模型可学习更一般的分布关系。

文献：[R14 rlcsp](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j)；[R18 GNoME2023](https://www.nature.com/articles/s41586-023-06735-9)；[R41 opencsp](https://arxiv.org/html/2509.10293v1)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R48 irl](https://arxiv.org/html/2602.00424v2)；[R54 flash](https://arxiv.org/html/2609.26402v1)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 24. D的演化：多解优化到持续发现

| 时间与支持论文 | 原文任务 | 为路线D提供的能力 |

| --- | --- | --- |

| 2021–2023<br>GFlowNet Foundations | 通用奖励比例采样 | 用生成分布表达多个高质量结果，提供多路径采样基础。 |

| 2024–2026<br>晶体QD、SHAFT | 固定组成的性质档案<br>层级对称材料生成 | 在不同性质或对称选择中探索多解，说明可以显式组织成功集合。 |

| 2025–2026<br>PLaID++、Chemeleon2、MatInvent | 物理或性质目标后训练 | 奖励与表示共同改变稳定性、新颖性和概率集中。 |

| 2025–2026<br>强基线研究、ANCHOR | 替换候选发现<br>冻结CSP下的组成探索 | 强替换和化学访问已能贡献发现，需要分开分配变化与新结构能力。 |

演化留下的问题：搜索遇到的新成功，怎样变成持续可用且能继续扩展的生成能力？

GFlowNet为通用基础，QD与SHAFT任务不同。强基线研究在分别选出的500个MP新颖候选上作DFT，上游提出成本不同。ANCHOR在冻结CSP条件下调节组成策略。其语料重放不必是成功结构，保持原数据定义。

文献：[R09 gflownet](https://jmlr.org/papers/v24/22-0364.html)；[R23 qd](https://arxiv.org/html/2403.03511v1)；[R30 shaft](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R44 matinvent](https://arxiv.org/html/2511.03112v1)；[R31 baselines](https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f)；[R56 anchor](https://arxiv.org/html/2609.33407v2)。

## 25. D的技术依据与具体选择

| 方法支撑 | 原任务中解决什么 | 在晶体中承担什么 |

| --- | --- | --- |

| GFlowNet、SHAFT<br>层级多解生成 | 按奖励保留多个结果和科学选择 | AR / GFlowNet选择组成或对称配置，条件生成器给出多种几何实现。 |

| 晶体QD、ANCHOR<br>档案与历史相关探索 | 保存不同结果，改变下一轮探索分配 | 根据已发现结构选择新区域，并研究固定或更新低层生成器。 |

| Max@K [T06]<br>文生图的预定义模式覆盖 | 按样本对集合覆盖的贡献分配奖励 | 借鉴集合层面学习，晶体类别和资格由物理评价逐步确认。 |

| Structure Matches、LeMat<br>多晶型与生成评价 | 统一结果身份和资格的观察 | 在弛豫后统计不同合格结果，区分首次发现、再生成和进一步发现。 |

候选基座：层级LLM / AR + 条件Diffusion。新增能力是学会新成功并继续发现。

Max@K原任务的目标模式预定义，当前arXiv v2注记WACV2027接收。这里仅用其集合贡献分配机制作迁移参照。Structure Matches的多晶型目标与LeMat的统一框架帮助定义能力，但不替代生成方法。D可以固定低层先研究上层探索，也可研究联合更新。

文献：[R09 gflownet](https://jmlr.org/papers/v24/22-0364.html)；[R30 shaft](https://arxiv.org/html/2411.04323v1)；[R23 qd](https://arxiv.org/html/2403.03511v1)；[R56 anchor](https://arxiv.org/html/2609.33407v2)；[T06 Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/abs/2607.14962)；[R42 glitter](https://arxiv.org/html/2509.12178v2)；[R46 lemat](https://arxiv.org/html/2512.04562v2)。

## 26. D的研究任务与可检验主张

中心问题：多轮发现能否让模型持续获得不同的稳定新结构？

**多轮DNG。** 在开放化学空间连续生成、弛豫和更新模型。每轮保留完整费用与不同合格结构集合。

**保持与迁移。** 分别测量新成功的再生成、旧成功的保留，以及未用于更新的新发现。

**关键比较。** 固定采样、组成重分配、QD / GFlowNet探索、加入生成器持续学习。

**论文结果。** 解释何时只需改变探索分配，何时必须学习新结构关系，并改善同预算下累计SUN数量。

首次发现、新颖于固定参考库、新颖于本项目更新集分别记录。已经学入训练的自发现材料，在下一轮生成时可计入参考库外SUN与保持能力，但不能再次计为研究过程中的首次发现。熟悉框架的新稳定化学仍计有效结果。

文献：[R09 gflownet](https://jmlr.org/papers/v24/22-0364.html)；[R23 qd](https://arxiv.org/html/2403.03511v1)；[R30 shaft](https://arxiv.org/html/2411.04323v1)；[R40 PLaID++](https://arxiv.org/html/2509.07150v4)；[R45 Chemeleon2](https://www.nature.com/articles/s42256-026-01262-4)；[R56 anchor](https://arxiv.org/html/2609.33407v2)；[R42 glitter](https://arxiv.org/html/2509.12178v2)；[R46 lemat](https://arxiv.org/html/2512.04562v2)。

## 27. 项目历史现象怎样进入四条路线

| 历史观察 | 已完成结果 | 对应的研究问题 |

| --- | --- | --- |

| 几何反馈增加稳定终点 | 同512来源已知稳定数<br>plain / restored / detached为76 / 85 / 86 | A / C：什么信息和变化使化学与结构配对更有效？ |

| 指定动作缺少终点事件 | PDE18：128个DEV父来源<br>512配对严格稳定 gain / loss = 0 / 0 | C：反馈必须支持能够改变完整后果的决定。 |

| 稳定性到SUN仍有损失 | PDE22：86个稳定尝试<br>58个稳定新颖，53个独特SUN | D：资格、新颖性与重复分别影响最终发现集合。 |

B的依据主要来自局部环境与组合生成文献，其稳定组合能力需要新的直接证据。

证据来源：https://github.com/YWDDLiang/Research/blob/main/crystal/evidence/historical-evidence.md 。第一行每臂24个能量未知，组成固定，晶胞和位置仍演化。第二行是每个DEV父来源四个未来形成的512配对。第三行为同一项目队列的分解，不能当作通用领域损失比例。

## 完整参考文献

- [R01] Chris J. Pickard, R. J. Needs. High-Pressure Phases of Silane. Physical Review Letters 97, 045504. DOI: 10.1103/PhysRevLett.97.045504. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.045504

- [R02] Artem R. Oganov, Colin W. Glass. Crystal structure prediction using ab initio evolutionary techniques: Principles and applications. Journal of Chemical Physics 124, 244704 (2006). DOI: 10.1063/1.2210932. https://doi.org/10.1063/1.2210932

- [R03] Chris J Pickard, R J Needs. Ab initio Random Structure Searching. Journal of Physics: Condensed Matter 2011. DOI: 10.1088/0953-8984/23/5/053201. https://arxiv.org/abs/1101.3987

- [R04] Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter, David Skinner, Gerbrand Ceder, Kristin A. Persson. Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. APL Materials 1, 011002 (2013). DOI: 10.1063/1.4812323. https://doi.org/10.1063/1.4812323

- [R05] Tian Xie, Jeffrey C. Grossman. Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties. Physical Review Letters 120, 145301. DOI: 10.1103/PhysRevLett.120.145301. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301

- [R06] Juhwan Noh, Jaehoon Kim, Helge S. Stein, Benjamin Sanchez-Lengeling, John M. Gregoire, Alan Aspuru-Guzik, Yousung Jung. Inverse Design of Solid-State Materials via a Continuous Representation. Matter 1(5), 1370–1384. DOI: 10.1016/j.matt.2019.08.017. https://doi.org/10.1016/j.matt.2019.08.017

- [R07] Zekun Ren, Siyu Isaac Parker Tian, Juhwan Noh, Felipe Oviedo, Guangzong Xing, Jiali Li, Qiaohao Liang, Ruiming Zhu, Armin G. Aberle, Shijing Sun, Xiaonan Wang, Yi Liu, Qianxiao Li, Senthilnath Jayavelu, Kedar Hippalgaonkar, Yousung Jung, Tonio Buonassisi. An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties. Matter 5, 314–335 2022. DOI: 10.1016/j.matt.2021.11.032. https://arxiv.org/pdf/2005.07609v3

- [R08] Tian Xie, Xiang Fu, Octavian-Eugen Ganea, Regina Barzilay, Tommi Jaakkola. Crystal Diffusion Variational Autoencoder for Periodic Material Generation. ICLR 2022. https://arxiv.org/abs/2110.06197

- [R09] Bengio, Yoshua, Lahlou, Salem, Deleu, Tristan, Hu, Edward J., Tiwari, Mo, Bengio, Emmanuel. GFlowNet Foundations. Journal of Machine Learning Research 2023. https://jmlr.org/papers/v24/22-0364.html

- [R10] Chi Chen, Shyue Ping Ong. A universal graph deep learning interatomic potential for the periodic table. Nature Computational Science 2, 718–728. DOI: 10.1038/s43588-022-00349-3. https://www.nature.com/articles/s43588-022-00349-3

- [R11] Bowen Deng, Peichen Zhong, KyuJung Jun, Janosh Riebesell, Kevin Han, Christopher J. Bartel, Gerbrand Ceder. CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling. Nature Machine Intelligence 5, 1031–1041. DOI: 10.1038/s42256-023-00716-3. https://www.nature.com/articles/s42256-023-00716-3

- [R12] Luis M. Antunes, Keith T. Butler, Ricardo Grau-Crespo. Crystal structure generation with autoregressive large language modeling. Nature Communications 15, 10570 2024. DOI: 10.1038/s41467-024-54639-7. https://www.nature.com/articles/s41467-024-54639-7

- [R13] Rui Jiao, Wenbing Huang, Peijia Lin, Jiaqi Han, Pin Chen, Yutong Lu, Yang Liu. Crystal Structure Prediction by Joint Equivariant Diffusion. NeurIPS 2023. https://arxiv.org/abs/2309.04475

- [R14] Elena Zamaraeva, Christopher M. Collins, Dmytro Antypov, Vladimir V. Gusev, Rahul Savani, Matthew S. Dyer, George R. Darling, Igor Potapov, Matthew J. Rosseinsky, Paul G. Spirakis. Reinforcement learning in crystal structure prediction. Digital Discovery 2023. DOI: 10.1039/D3DD00063J. https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j

- [R15] Yang, Sherry, Cho, KwangHwan, Merchant, Amil, Abbeel, Pieter, Schuurmans, Dale, Mordatch, Igor, Cubuk, Ekin Dogus. Scalable Diffusion for Materials Generation. ICLR 2024. https://arxiv.org/abs/2311.09235

- [R16] Hang Xiao, Rong Li, Xiaoyang Shi, Yan Chen, Liangliang Zhu, Xi Chen, Lei Wang. An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning. Nature Communications 14, 7027 2023. DOI: 10.1038/s41467-023-42870-7. https://www.nature.com/articles/s41467-023-42870-7

- [R17] Nathan J. Szymanski, Bernardus Rendy, Yuxing Fei, Rishi E. Kumar, Tanjin He, David Milsted, Matthew J. McDermott, Max Gallant, Ekin Dogus Cubuk, Amil Merchant, Haegyeom Kim, Anubhav Jain, Christopher J. Bartel, Kristin Persson, Yan Zeng, Gerbrand Ceder. Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials. Nature 650, E1 (2026). DOI: 10.1038/s41586-025-09992-y. https://www.nature.com/articles/s41586-025-09992-y

- [R18] Amil Merchant, Simon Batzner, Samuel S. Schoenholz, Muratahan Aykol, Gowoon Cheon, Ekin Dogus Cubuk. Scaling deep learning for materials discovery. Nature 2023. DOI: 10.1038/s41586-023-06735-9. https://www.nature.com/articles/s41586-023-06735-9

- [R19] Claudio Zeni, Robert Pinsler, Daniel Zügner, Andrew Fowler, Matthew Horton, Xiang Fu, Zilong Wang, Aliaksandra Shysheya, Jonathan Crabbé, Shoko Ueda, Roberto Sordillo, Lixin Sun, Jake Smith, Bichlien Nguyen, Hannes Schulz, Sarah Lewis, Chin-Wei Huang, Ziheng Lu, Yichi Zhou, Han Yang, Hongxia Hao, Jielan Li, Chunlei Yang, Wenjie Li, Ryota Tomioka, Tian Xie. A generative model for inorganic materials design. Nature 2025. DOI: 10.1038/s41586-025-08628-5. https://www.nature.com/articles/s41586-025-08628-5

- [R20] Yan, Keqiang, Li, Xiner, Ling, Hongyi, Ashen, Kenna, Edwards, Carl, Arróyave, Raymundo, Zitnik, Marinka, Ji, Heng, Qian, Xiaofeng, Qian, Xiaoning, Ji, Shuiwang. Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation. NeurIPS 2024. https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html

- [R21] Nate Gruver, Anuroop Sriram, Andrea Madotto, Andrew Gordon Wilson, C. Lawrence Zitnick, Zachary Ulissi. Fine-Tuned Language Models Generate Stable Inorganic Materials as Text. ICLR 2024. https://arxiv.org/abs/2402.04379

- [R22] Jiao, Rui, Huang, Wenbing, Liu, Yu, Zhao, Deli, Liu, Yang. Space Group Constrained Crystal Generation. ICLR 2024. https://arxiv.org/abs/2402.03992

- [R23] Marta Wolinska, Aron Walsh, Antoine Cully. Illuminating the property space in crystal structure prediction using Quality-Diversity algorithms. Digital Discovery 2024. DOI: 10.1039/D4DD00054D. https://arxiv.org/html/2403.03511v1

- [R24] Cai-Yuan Ye, Hong-Ming Weng, Quan-Sheng Wu. Con-CDVAE: A method for the conditional generation of crystal structures. Computational Materials Today 1, 100003 2024. DOI: 10.1016/j.commt.2024.100003. https://arxiv.org/html/2403.12478v1

- [R25] Zhendong Cao, Xiaoshan Luo, Jian Lv, Lei Wang. Space group informed transformer for crystalline materials generation. Science Bulletin 70, 3522–3533 2025. DOI: 10.1016/j.scib.2025.09.035. https://arxiv.org/abs/2403.15734

- [R26] Miller, Benjamin Kurt, Chen, Ricky T. Q., Sriram, Anuroop, Wood, Brandon M. FlowMM: Generating Materials with Riemannian Flow Matching. ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/miller24a.html

- [R27] Ryotaro Okabe, Mouyang Cheng, Abhijatmedhi Chotrattanapituk, Manasi Mandal, Kiran Mak, Denisse Córdova Carrizales, Nguyen Tuan Hung, Xiang Fu, Bowen Han, Yao Wang, Weiwei Xie, Robert J. Cava, Tommi S. Jaakkola, Yongqiang Cheng, Mingda Li. Structural constraint integration in a generative model for the discovery of quantum materials. Nature Materials 25, 223–230 2026. DOI: 10.1038/s41563-025-02355-y. https://www.nature.com/articles/s41563-025-02355-y

- [R28] Sherry Yang, Simon Batzner, Ruiqi Gao, Muratahan Aykol, Alexander L. Gaunt, Brendan McMorrow, Danilo J. Rezende, Dale Schuurmans, Igor Mordatch, Ekin D. Cubuk. Generative Hierarchical Materials Search. NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/file/447d012bd95b6767a4bfdebf96cdfcc9-Paper-Conference.pdf

- [R29] Anuroop Sriram, Benjamin Kurt Miller, Ricky T. Q. Chen, Brandon M. Wood. FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions. NeurIPS 2024. DOI: 10.52202/079017-1464. https://proceedings.neurips.cc/paper_files/paper/2024/hash/51d317df78eded9eb3c9d3fb1091c279-Abstract-Conference.html

- [R30] Nguyen, Tri Minh, Tawfik, Sherif Abdulkader, Tran, Truyen, Gupta, Sunil, Rana, Santu, Venkatesh, Svetha. Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks. Digital Discovery 2026. DOI: 10.1039/D4DD00392F. https://arxiv.org/html/2411.04323v1

- [R31] Nathan J. Szymanski, Christopher J. Bartel. Establishing baselines for generative discovery of inorganic crystals. Materials Horizons 2025. DOI: 10.1039/D5MH00010F. https://pubs.rsc.org/en/content/articlehtml/2025/mh/d5mh00010f

- [R32] Pierre-Paul De Breuck, Hashim A. Piracha, Gian-Marco Rignanese, Miguel A. L. Marques. A generative material transformer using Wyckoff representation. npj Computational Materials 12, 60 2026. DOI: 10.1038/s41524-025-01940-8. https://www.nature.com/articles/s41524-025-01940-8

- [R33] Wu, Hanlin, Song, Yuxuan, Gong, Jingjing, Cao, Ziyao, Ouyang, Yawen, Zhang, Jianbing, Zhou, Hao, Ma, Wei-Ying, Liu, Jingjing. A Periodic Bayesian Flow for Material Generation. ICLR 2025. https://arxiv.org/abs/2502.02016

- [R34] Hoellmer, Philipp, Egg, Thomas, Martirossyan, Maya M., Fuemmeler, Eric, Shui, Zeren, Gupta, Amit, Prakash, Pawan, Roitberg, Adrian, Liu, Mingjie, Karypis, George, Transtrum, Mark, Hennig, Richard G., Tadmor, Ellad B., Martiniani, Stefano. Open Materials Generation with Stochastic Interpolants. ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/hollmer25a.html

- [R35] Levy, Daniel, Panigrahi, Siba Smarak, Kaba, Sékou-Oumar, Zhu, Qiang, Lee, Kin Long Kelvin, Galkin, Mikhail, Miret, Santiago, Ravanbakhsh, Siamak. SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models. ICLR 2025. https://arxiv.org/abs/2502.03638

- [R36] Kelvinius, Filip Ekström, Andersson, Oskar B., Parackal, Abhijith S., Qian, Dong, Armiento, Rickard, Lindsten, Fredrik. WyckoffDiff – A Generative Diffusion Model for Crystal Symmetry. ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/ekstrom-kelvinius25a.html

- [R37] Kishalay Das, Subhojyoti Khastagir, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, Niloy Ganguly. Periodic Materials Generation using Text-Guided Joint Diffusion Model. ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/24e4e3234178a836b70e0aa48827e0ff-Abstract-Conference.html

- [R38] Kazeev, Nikita, Nong, Wei, Romanov, Ignat, Zhu, Ruiming, Ustyuzhanin, Andrey, Yamazaki, Shuya, Hippalgaonkar, Kedar. Wyckoff Transformer: Generation of Symmetric Crystals. ICML 2025, PMLR 267, 29495–29526. https://arxiv.org/abs/2503.02407

- [R39] Hyunsoo Park, Anthony Onwuli, Aron Walsh. Exploration of crystal chemical space using text-guided generative artificial intelligence. Nature Communications 16, 4379 2025. DOI: 10.1038/s41467-025-59636-y. https://www.nature.com/articles/s41467-025-59636-y

- [R40] Xu, Andy, Desai, Rohan, Wang, Larry, Ritz, Ethan, Hope, Gabriel. PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design. ICML 2026. https://arxiv.org/html/2509.07150v4

- [R41] Wang, Yinan, Wang, Xiaoyang, Wang, Zhenyu, Wu, Jing, Lv, Jian, Wang, Han. OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure. arXiv 预印本 2025. https://arxiv.org/html/2509.10293v1

- [R42] Martirossyan, Maya M., Egg, Thomas, Hoellmer, Philipp, Karypis, George, Transtrum, Mark, Roitberg, Adrian, Liu, Mingjie, Hennig, Richard G., Tadmor, Ellad B., Martiniani, Stefano. All that structure matches does not glitter. NeurIPS Datasets and Benchmarks 2025. https://arxiv.org/html/2509.12178v2

- [R43] Subhojyoti Khastagir, Kishalay Das, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, Niloy Ganguly. LLM Meets Diffusion: A Hybrid Framework for Crystal Material Generation. NeurIPS 2025. DOI: 10.52202/085713-5635. https://proceedings.neurips.cc/paper_files/paper/2025/hash/f789a628fca473e922c806657512a20f-Abstract-Conference.html

- [R44] Chen, Junwu, Guo, Jeff, Fako, Edvin, Schwaller, Philippe. Accelerating inverse materials design using generative diffusion models with reinforcement learning. arXiv 预印本 2025. https://arxiv.org/html/2511.03112v1

- [R45] Hyunsoo Park, Aron Walsh. Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning. Nature Machine Intelligence 2026. DOI: 10.1038/s42256-026-01262-4. https://www.nature.com/articles/s42256-026-01262-4

- [R46] Betala, Siddharth, Gleason, Samuel P., Ramlaoui, Ali, Xu, Andy, Channing, Georgia, Levy, Daniel, Fourrier, Clémentine, Kazeev, Nikita, Joshi, Chaitanya K., Kaba, Sékou-Oumar, Therrien, Félix, Hernandez-Garcia, Alex, Mercado, Rocío, Krishnan, N. M. Anoop, Duval, Alexandre. LeMat-GenBench: A Unified Evaluation Framework for Crystal Generative Models. arXiv 预印本 2025. https://arxiv.org/html/2512.04562v2

- [R47] Peijia Lin, Zihan Zhang, Zhangrui Zhao, Shaohao Rui, Junyi An, Yun-Fei Shi, Fenglei Cao, Weijie Ma, Yutong Lu. Periodic Bayesian Flow Networks with Additive Accuracy. ICML 2026, PMLR 306, 75161–75176. https://proceedings.mlr.press/v306/lin26ar.html

- [R48] Hoellmer, Philipp, Martiniani, Stefano. Open Materials Generation with Inference-Time Reinforcement Learning. ICML 2026. https://arxiv.org/html/2602.00424v2

- [R49] Kiyoung Seong, Sungsoo Ahn, Sehui Han, Changyoung Park. Multimodal Crystal Flow: Any-to-Any Modality Generation for Unified Crystal Modeling. ICML2026, PMLR306:109105–109131. https://proceedings.mlr.press/v306/seong26a.html

- [R50] Qin, Yifang, Shi, Yu, Tan, Junfu, Liu, Chang, Zhang, Ming, Lu, Ziheng. Generative structure search for efficient and diverse discovery of molecular and crystal structures. arXiv 预印本 2026. https://arxiv.org/html/2604.27636v2

- [R51] Nian Liu, Yuwei Zeng, Ryoji Kubo, Nikita Kazeev, Stephen Gregory Dale, Artem Maevskiy, Pengru Huang, Thomas Laurent, Kostya S. Novoselov, Xavier Bresson. Composable Crystals: Controllable Materials Discovery via Concept Learning. arXiv 预印本 2026. https://arxiv.org/html/2605.14769v2

- [R52] Negishi, Masahiro, Walsh, Aron. Substitution-Based Analysis of Structural Novelty for Generative Models of Materials. arXiv 预印本 2026. https://arxiv.org/html/2606.23166v1

- [R53] Wentao Li. Text-guided flow matching enables sample-efficient crystal structure generation. arXiv 预印本 2026. https://arxiv.org/html/2609.01076v2

- [R54] Egg, Thomas, Sullivan, Harry Winston, Tadmor, Ellad B., Martiniani, Stefano. OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery. arXiv 预印本 2026. https://arxiv.org/html/2609.26402v1

- [R55] Jingyi Zhou, Oyshee Chowdhury, Noah Oyeniran, Chongze Hu. Topology-Stratified Materials Discovery with A Flow-Based Generative Model. arXiv 预印本 2026. https://arxiv.org/html/2609.26547v1

- [R56] Hovmand, Emma Lei, Elsborg, Jonas, Kandemir, Melih, Bhowmik, Arghya. Let CSP Be Your ANCHOR: Adaptive Crystal Search over Frozen Structure Priors. arXiv 预印本 2026. https://arxiv.org/html/2609.33407v2

- [R57] Tang, Haocheng, Wang, Junmei, Jin, Wengong. Where Should Physics Enter a Molecular Crystal Generator?. arXiv 预印本 2026. https://arxiv.org/html/2609.36398v1

- [T01] Yueming Pan, Ruoyu Feng, Qi Dai, Yuqi Wang, Wenfeng Lin, Mingyu Guo, Chong Luo, Nanning Zheng. Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion. CVPR 2026. https://arxiv.org/abs/2512.04926

- [T02] NextStep Team. NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale. ICLR 2026. https://arxiv.org/abs/2508.10711

- [T03] Arwen Bradley. Local Mechanisms of Compositional Generalization in Conditional Diffusion. ICML 2026, PMLR 306:9531–9565. https://proceedings.mlr.press/v306/bradley26a.html

- [T04] Jie Liu, Gongye Liu, Jiajun Liang, Yangguang Li, Jiaheng Liu, Xintao Wang, Pengfei Wan, Di Zhang, Wanli Ouyang. Flow-GRPO: Training Flow Matching Models via Online RL. NeurIPS 2025. https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html

- [T05] Andreas Bergmeister, Stefanie Jegelka, Nikolas Nüsken, Carles Domingo-Enrich, Jakiw Pidstrigach. Reinforce Adjoint Matching: Scaling RL Post-Training of Diffusion and Flow-Matching Models. arXiv 2605.10759v2 (2026). https://arxiv.org/abs/2605.10759

- [T06] Ku Onoda, Paavo Parmas, Hiroki Furuta, Soichiro Nishimori, Yuta Oshima, Shohei Taniguchi, Yutaka Matsuo. Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation. arXiv 2607.14962v2 (2026)，原文注记WACV 2027接收. https://arxiv.org/abs/2607.14962

- [T07] Zheng Fang, Lichuan Xiang, Xu Cai, Bing Wang, Bo Yang, Hongkai Wen. DynFusion: Rethinking Condition Fusion for Adaptive Multi-Conditional Text-to-Image Generation. CVPR 2026, 29103–29113. https://wrap.warwick.ac.uk/id/eprint/197869/8/WRAP-DynFusion-rethinking-condition-fusion-multi-conditional-text-to-image-generation-26.pdf

- [T08] Michael Albergo, Nicholas M. Boffi, Eric Vanden-Eijnden. Stochastic Interpolants: A Unifying Framework for Flows and Diffusions. JMLR 26(209):1–80 (2025)，首稿2023. https://jmlr.org/papers/v26/23-1605.html
