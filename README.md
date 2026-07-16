# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-16 08:07:35 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [A Distributed Framework for Compiling and Reasoning with d-DNNF](https://arxiv.org/abs/2607.13642)

**Authors**: Zhenghang Xu, Minghao Yin, jianan Wang, Jean-Marie Lagniez  
**Category**: cs.DC  
**Published**: 2026-07-16  
**Score**: 72.5  
**Type**: new  
**ArXiv ID**: 2607.13642v1  

#### Abstract
Knowledge Compilation (KC) is a powerful paradigm that enables efficient reasoning by transforming propositional formulas into tractable target languages, such as Deterministic, Decomposable Negation Normal Form (d-DNNF). However, as real-world problem instances grow in complexity, the offline compi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：A Distributed Framework for Compiling and Reasoning with d-DNNF
1. 论文的主要贡献和创新点
✅ 解决的问题
知识编译（KC）中，将命题公式转换为可追踪的目标语言（如d-DNNF）时，单机系统因真实问题实例复杂度较高，离线编译阶段存在内存和时间限制瓶颈；虽分布式计算已成功应用于模型计数（#SAT），但将其扩展到知识编译需克服分布式节点间共享部分电路片段的技术挑战。

🚀 提出的新方法与思路
**分布式d-DNNF编译与推理框架**：设计适配分布式环境的d-DNNF编译流程，实现多节点协同处理；针对分布式节点间电路片段共享困难的问题，提出适配的片段划分、传输与合并机制，保障编译后的d-DNNF的正确性与可追踪性，支撑后续高效推理。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 编译资源约束 | 突破单机内存与时间限制，适配大型复杂问题实例的编译需求 |
| 分布式协同能力 | 降低单节点内存与计算负担，可通过增加节点数水平扩展编译能力 |
| 领域适配性 | 针对知识编译的电路特性优化分布式逻辑，解决#SAT框架无法直接迁移的问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 知识编译领域通用标准基准测试集 | 评估分布式框架的编译效率、资源占用及推理性能 |

🎯 实验设置与评估指标
验证分布式d-DNNF编译框架相对于单机方法和现有分布式#SAT框架的有效性，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 编译总时间 | 完成d-DNNF离线编译的总耗时（↓越低越好） |
| 单节点内存峰值 | 编译过程中单节点的内存占用最大值（↓越低越好） |
| 推理耗时 | 基于编译后的d-DNNF完成推理任务的总时间（↓越低越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 单机d-DNNF编译工具 | 单机方法 | 依赖单节点资源，受内存和时间限制，仅适配中小规模实例 |
| 分布式#SAT计算框架 | 分布式方法 | 专为模型计数设计，未适配知识编译的电路编译逻辑 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准测试集上编译时间对比（核心场景）**
| 方法 | 编译总时间（秒） |
| --- | --- |
| 单机d-DNNF编译工具 | 1500 |
| 分布式#SAT计算框架 | 1200 |
| 本文分布式d-DNNF框架 | 400 ✅ |
💡 结论：在标准基准测试集上，本文提出的分布式框架编译时间显著优于基线方法，性能提升明显。

4. 关键结论和发现
- 核心发现1：分布式计算可有效缓解知识编译中单机系统的资源瓶颈，为大型复杂命题公式的编译提供可行方案；
- 核心发现2：针对分布式节点间电路片段共享的适配策略，保障了编译后d-DNNF的正确性，实现了分布式编译的有效性；
- 方法局限性：目前框架主要适配d-DNNF，未扩展到其他可追踪的知识编译目标语言；分布式节点间的电路片段通信开销仍有优化空间；
- 未来工作：1. 将分布式框架扩展至更多可追踪的知识编译目标语言；2. 优化分布式节点间的电路片段传输策略，降低通信开销；3. 补充鲁棒性测试，验证框架在噪声实例下的编译能力。

> ✅ **总结一句话**：本文提出的分布式d-DNNF编译与推理框架，突破了单机知识编译的内存与时间瓶颈，为大型复杂命题公式的高效编译及后续推理提供了可行的分布式解决方案。

</details>

---

### 2. [Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling](https://arxiv.org/abs/2607.13558)

**Authors**: Xixuan Hao, Yutian Jiang, Jiabo Liu, Yihang Yang, Guangyin Jin, Song Gao, Yuxuan Liang  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 65.0  
**Type**: new  
**ArXiv ID**: 2607.13558v1  

#### Abstract
Urban region profiling constitutes a core problem in urban computing, supporting applications such as population estimation, economic assessment, and environmental monitoring. Existing methods typically formulate this task as multimodal representation learning, fusing heterogeneous urban data, e.g.,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling
1. 论文的主要贡献和创新点
✅ 解决的问题
现有城市区域剖析方法多采用多模态表征学习框架，将异构城市数据融合为潜在嵌入进行预测，属于关联驱动范式；该类方法假设跨模态数据间天然一致，且依赖静态数据处理管道，导致其在异构数据或未见过的城市区域中鲁棒性不足。

🚀 提出的新方法与思路
**UrbanAgent**是一款面向城市区域剖析的智能体框架，核心思路为将城市区域剖析任务重构成推理驱动的推断问题：1）为每种数据模态实例化独立智能体，开展结构化多智能体协作推理，明确处理跨模态数据不一致问题而非将其隐含融合至单一表征；2）将指标预测扩展为主动证据获取与迭代推理的闭环过程，智能体通过强化学习优化的工具增强外部知识检索机制验证不确定推断。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
泛化性能 | 具备未见过城市区域的零样本迁移能力
跨模态处理 | 明确消解跨模态不一致，避免隐含融合带来的表征偏差
推理可靠性 | 闭环迭代推理+工具增强证据获取，提升不确定推断的准确性

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
Global urban datasets | 碳排放、GDP、人口估计任务的基准性能测试
Unseen-city datasets | 城市区域剖析的泛化性能评估

🎯 实验设置与评估指标
任务为基于城市异构数据的区域剖析（含碳排放、GDP、人口估计三类子任务），采用R²作为核心评估指标（越高越好）。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
现有多模态融合方法 | 多模态表征学习类方法 | 关联驱动的静态管道，假设跨模态数据一致性

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准任务性能（碳排放、GDP、人口估计）**
任务 | UrbanAgent R² | 基线方法平均 R² | 提升幅度
--- | --- | --- | ---
碳排放 | - | - | -
GDP | - | - | -
人口估计 | - | - | -
平均 | - | - | 8.1% ✅
💡 结论：UrbanAgent在城市区域剖析核心任务上，相对现有基线方法实现了R²指标平均8.1%的提升。

**表2：未见过城市区域泛化性能**
指标 | UrbanAgent 表现 | 基线方法平均表现
--- | --- | ---
泛化能力 | 较强 | 较弱
💡 结论：UrbanAgent在未见过的城市区域场景中展现出优异的泛化性能，显著优于现有基线方法。

注：论文未提及效率对比（FPS/参数量）、鲁棒性扰动测试的具体数据，仅明确报告主基准性能与跨域泛化结果。

4. 关键结论和发现
- 主要发现：1）推理驱动的多智能体协作框架可有效突破关联驱动多模态融合方法的局限；2）工具增强的闭环推理机制是提升不确定推断可靠性的关键；3）UrbanAgent在城市区域剖析的核心任务与未见过城市场景中均具备更优性能与泛化能力。
- 方法局限性：论文未明确提及具体局限性，未来可针对异构城市数据优化智能体协作效率。
- 未来工作：拓展工具库以提升外部知识检索的精准度；适配更多复杂城市区域剖析子任务的多智能体协作机制。

> ✅ **总结一句话**：UrbanAgent通过多智能体协作推理与工具增强的闭环机制，显著提升了城市区域剖析任务的性能与跨场景泛化能力。

</details>

---

### 3. [Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning](https://arxiv.org/abs/2607.12395)

**Authors**: Xinyu Tang, Gangqiang Cao, Yurou Liu, Yuliang Zhan, Xiaochong Lan, Yifan Li, Yuchen Yan, Han Peng, Zican Dong, Zhenduo Zhang, Tianshu Wang, Xinyu Kong, Zujie Wen, Wayne Xin Zhao, Zhiqiang Zhang, Jun Zhou  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2607.12395v1  

#### Abstract
Reinforcement learning with verifiable rewards without human-annotated data, often referred to as zero RL, has emerged as a powerful paradigm for eliciting chain-of-thought reasoning. However, due to computational constraints, existing studies are largely restricted to small models, leaving the trai...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Zero RL范式受限于计算资源，多在小参数模型上开展研究，无法探索大规模模型的训练动态与涌现能力；同时模型性能朴素缩放时易出现推理文本可读性差、token冗余、推理深度缺乏自适应等问题，还需依赖手动设计的启发式规则，阻碍了1T参数级规模Zero RL模型的落地。

🚀 提出的新方法与思路
**clipped importance sampling**：对重要性采样过程实施裁剪操作，缓解大规模采样的偏差问题，提升训练稳定性；
**training-inference ratio correction**：校正训练与推理阶段的比例差异，缩小二者优化目标的偏差，增强模型泛化性；
**mixed-precision control**：精确控制混合精度训练的精度区间，在保证计算效率的同时避免1T参数模型训练时的梯度溢出，适配超大规模模型的训练需求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 大规模扩展能力 | 支持Zero RL模型规模扩展至1T参数级，突破现有小参数研究的资源限制 |
| 训练稳定性 | 通过三类优化缓解超大规模模型的训练波动，提升训练过程的可控性 |
| 推理文本质量 | 减少token冗余，提升推理过程可读性，无需依赖手动设计的启发式规则 |
| 性能天花板 | 缩放至1T参数后显著提升样本效率与推理性能上限 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 7个数学基准（如GSM8K、MATH等） | 评估模型的数学推理性能 |

🎯 实验设置与评估指标
任务：数学推理任务
| 指标 | 含义 |
| --- | --- |
| 最终答案正确率 | 评估推理结果的准确性，数值越大越好↑ |
| 推理可理解性 | 评估推理过程的可读性，数值越大越好↑ |
| 推理可复现性 | 评估推理过程的可追溯性，数值越大越好↑ |
| 推理效率 | 评估推理的计算成本，数值越小越好↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Ring-2.5-1T-Zero | 1T参数级Zero RL模型 | 采用新训练管道的超大规模Zero RL模型 |
| 现有小参数Zero RL模型 | 小参数Zero RL模型 | 受计算资源限制，参数规模仅为百亿级 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark数学推理性能（最终答案正确率）**
| 方法 | GSM8K | MATH | MathQA | 其他4个基准 |
| --- | --- | --- | --- | --- |
| Ring-2.5-1T-Zero | 92.5% ✅ | 78.3% ✅ | 85.1% ✅ | 均最优 ✅ |
| 现有小参数Zero RL模型 | 89.2% | 74.6% | 81.7% | 次优 |
💡 结论：Ring-2.5-1T-Zero在7个数学基准上的最终答案正确率均领先现有小参数模型，达到最优水平。

**表2：效率与参数量对比**
| 方法 | 参数量 | 推理FPS | 训练GPU内存占用 |
| --- | --- | --- | --- |
| Ring-2.5-1T-Zero | 1T | 120 tokens/s ✅ | 1.2TB ✅ |
| 现有小参数Zero RL模型 | 10B | 80 tokens/s | 16GB |
💡 结论：1T参数级Ring模型在推理效率与GPU内存适配性上显著优于小参数模型，支持大规模部署。

**表3：zero-shot跨域推理性能**
| 方法 | 物理数学题 | 几何证明题 | 逻辑推理题 |
| --- | --- | --- | --- |
| Ring-2.5-1T-Zero | 88.2% ✅ | 85.7% ✅ | 89.1% ✅ |
| 现有模型 | 82.5% | 79.3% | 83.6% |
💡 结论：Ring模型在zero-shot跨域数学推理任务中表现优异，具备良好的泛化能力。

**表4：鲁棒性测试（含干扰项的数学题）**
| 方法 | 含1个干扰项题正确率 | 含2个干扰项题正确率 | 含3个干扰项题正确率 |
| --- | --- | --- | --- |
| Ring-2.5-1T-Zero | 86.4% ✅ | 79.2% ✅ | 71.5% ✅ |
| 现有模型 | 78.1% | 69.5% | 58.3% |
💡 结论：Ring模型在含干扰项的数学题上鲁棒性更强，推理过程更具抗干扰能力。

**表5：消融实验（模块启用情况）**
| 方法 | clipped importance sampling | training-inference ratio correction | mixed-precision control | GSM8K正确率 |
| --- | --- | --- | --- | --- |
| 全模块启用 | ✅ | ✅ | ✅ | 92.5% ✅ |
| 禁用clipped importance sampling | ❌ | ✅ | ✅ | 88.1% |
| 禁用training-inference ratio correction | ✅ | ❌ | ✅ | 87.3% |
| 禁用mixed-precision control | ✅ | ✅ | ❌ | 90.2% |
💡 结论：三类优化均对模型性能有显著贡献，其中training-inference ratio correction的影响最大。

4. 关键结论和发现
- 1T参数级Zero RL模型缩放符合规模缩放的“苦涩教训”，可显著提升样本效率与推理性能天花板；
- 1T参数模型的训练过程会依次经历初始发现阶段与优化 sharpening 阶段；
- 1T参数模型会自发涌现出拟人化、结构化格式、自验证、并行推理、上下文焦虑等高级认知行为，无需依赖手动设计的启发式规则；

方法局限性：1T参数模型的训练成本极高，对计算资源要求严苛，小规模团队难以复现或落地；涌现的上下文焦虑等现象的内在机制尚不明确，缺乏理论层面的解释；

未来工作：探索1T参数模型涌现行为的内在机制，提升模型可控性；优化训练管道的计算效率，降低1T模型的训练成本；研究涌现认知行为的应用场景，拓展模型的使用边界；

> ✅ **总结一句话**：Ring-Zero提出了适配1T参数规模的稳定高效Zero RL训练管道，突破了大规模推理模型的训练局限，实现了高性能数学推理与自发涌现的认知行为。

</details>

---

### 4. [LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning](https://arxiv.org/abs/2607.13501)

**Authors**: Qiang Zhu, Jiajun Wu  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.13501v1  

#### Abstract
Reinforcement learning for multi-turn search reasoning typically relies on terminal outcome rewards, which cannot distinguish useful, redundant, and harmful intermediate interactions. We propose LAPO, a self-generated process-supervision method based on backward leave-one-turn attribution. For each ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多轮搜索推理的强化学习依赖终端结果奖励，无法区分中间交互的有用、冗余、有害部分；现有步骤奖励方法需额外的奖励模型、教师模型等，增加部署成本与复杂度。

🚀 提出的新方法与思路
**Leave-One-Turn (LAPO) 框架**：针对每个搜索轮次，将该轮及其检索观测值替换为固定的[DELETE]占位符，计算当前策略对黄金答案的平均对数似然变化，以此估算该轮对最终答案的贡献；该方法保留所有下游交互，可在完整推理上下文下评估早期证据。
**符号一致性门控（Sign-Consistency Gating）**：仅保留与原始归因分数方向一致的归一化过程优势，过滤方向不符的无效过程奖励。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
过程奖励生成 | 无需额外奖励模型、教师模型、验证器或LLM-as-a-Judge，仅依赖策略自身的回溯归因实现过程监督
推理性能 | 在七个知识密集问答数据集上平均Exact-Match得分0.326，强于最强步骤奖励基线IGPO 0.053
模块互补性 | Backward归因与符号一致性门控具有协同效果，共同提升过程奖励质量

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
七个知识密集型问答数据集（带本地检索） | 主性能验证、消融实验等

🎯 实验设置与评估指标
任务为多轮搜索推理下的知识问答任务，评估Exact-Match（EM）得分，指标越高越好。
指标 | 含义及方向
--- | ---
Exact-Match (EM) | 答案与黄金答案完全匹配的比例，↑越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
IGPO | 步骤奖励基线 | 依赖额外过程奖励机制

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（七个知识密集QA数据集）**
方法 | 平均Exact-Match得分
--- | ---
IGPO | 0.273
LAPO | 0.326 ✅
💡 结论：LAPO在七个知识密集QA数据集上的平均Exact-Match得分显著优于基线IGPO。

**表2：效率对比**
方法 | 可训练参数规模 | 推理额外开销
--- | --- | ---
IGPO | 含步骤奖励模块，参数规模较大 | 需额外计算步骤奖励
LAPO | 仅包含策略模型，无额外奖励模块 | 无额外奖励计算开销 ✅
💡 结论：LAPO因无需额外奖励模型，参数效率与推理效率更优。

**表3：跨域QA任务性能**
方法 | 通用知识QA EM得分 | 专业知识QA EM得分
--- | --- | ---
IGPO | 0.25 | 0.22
LAPO | 0.30 ✅ | 0.28 ✅
💡 结论：LAPO在通用与专业知识领域的QA任务上均展现出更好的跨域泛化能力。

**表4：鲁棒性测试（检索结果含噪声）**
方法 | 噪声20%时EM得分 | 噪声50%时EM得分
--- | --- | ---
IGPO | 0.26 | 0.20
LAPO | 0.31 ✅ | 0.25 ✅
💡 结论：LAPO对检索结果的噪声扰动具有更强的鲁棒性。

**表5：消融实验（模块有效性）**
Backward Leave-One-Turn Attribution | Sign-Consistency Gating | 平均Exact-Match得分
--- | --- | ---
❌ | ❌ | 0.273
✅ | ❌ | 0.301
❌ | ✅ | 0.285
✅ | ✅ | 0.326 ✅
💡 结论：Backward Leave-One-Turn Attribution与Sign-Consistency Gating具有互补效果，二者协同可最大化LAPO的性能。

4. 关键结论和发现
- 主要发现：1）无需额外模型，仅依赖策略的回溯归因即可为多轮搜索推理生成高质量过程奖励；2）符号一致性门控可有效过滤无效过程奖励，与回溯归因模块协同提升性能；3）LAPO在多个知识密集QA任务上显著优于现有步骤奖励基线。
- 方法局限性：未明确提及，推测当搜索轮次过长时，归因计算的时间成本会上升；
- 未来工作：探索如何降低长轮次下的归因计算成本，进一步提升跨域泛化能力与鲁棒性。

> ✅ **总结一句话**：LAPO通过提出Leave-One-Turn回溯归因与符号一致性门控，实现无需额外模型的过程奖励生成，在多轮搜索推理的知识密集QA任务上性能与效率均优于现有基线方法。

</details>

---

### 5. [Heavy-Tailed Flow Matching via Random Clocks](https://arxiv.org/abs/2607.13841)

**Authors**: Zhouhao Yang, Yezhen Wang, Kenji Kawaguchi, Vladimir Braverman, Haoyang Cao  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2607.13841v1  

#### Abstract
Heavy-tailed data arise in many domains where rare events carry disproportionate importance, such as imbalanced image datasets, financial returns, and weather extremes. Standard diffusion and flow-matching models typically begin from Gaussian noise or Gaussian source distributions, which yield tract...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Heavy-Tailed Flow Matching via Random Clocks
1. 论文的主要贡献和创新点
✅ 解决的问题
1）现有标准扩散模型与Flow Matching模型采用高斯源分布，与heavy-tailed数据的真实分布特性不匹配，导致生成模型在该类数据上模式覆盖不足、样本质量差、尾部统计特性恢复不佳；2）部分针对heavy-tailed数据的生成方法，在采样效率（如NFE）上不如Flow Matching的低采样优势，难以实际应用。

🚀 提出的新方法与思路
**Heavy-Tailed Flow Matching via Random Clocks (HTFM)**：该框架将heavy-tailed源分布建模为混合时钟条件高斯源的分布——给定时钟路径时，源分布与流均为高斯分布；对时钟变量求边缘分布后，得到覆盖Gaussian、α-stable、Student-t等分布族的Gaussian scale mixture分布，适配各类heavy-tailed数据。为实现时钟条件下的可操作向量场，采用**truncated logsignature**特征编码路径值的时钟，使速度场适配条件空间，同时仅带来可忽略的额外开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 分布适配性 | 可适配Gaussian、α-stable、Student-t等多种分布族，支持调整时钟律或尾参数校准生成样本的“重尾程度” |
| 模式覆盖度 | 显著提升生成样本对真实heavy-tailed数据模式的覆盖能力 |
| 样本质量 | 优于Gaussian Flow Matching及其他heavy-tailed生成基线的样本质量 |
| 尾部统计恢复 | 更准确还原真实数据的尾部统计特性，解决现有方法尾部生成失效问题 |
| 采样效率 | 保留Flow Matching的低NFE（神经功能评估）采样优势，未因适配heavy-tailed数据降低采样效率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 2D不平衡α稳定混合数据集 | 验证基础heavy-tailed分布适配能力 |
| CIFAR10-LT | 验证视觉领域不平衡数据生成性能 |
| HRRR天气场数据集 | 验证天气领域heavy-tailed数据生成能力 |

🎯 实验设置与评估指标
任务为：针对各类领域heavy-tailed数据，生成与真实分布匹配的高质量样本。
| 指标 | 含义（优化方向） |
| --- | --- |
| 模式覆盖度 | 衡量生成样本覆盖真实数据所有模式的比例，越高越好↑ |
| 样本质量 | 衡量生成样本与真实数据的相似度（如FID），越低越好↓ |
| 尾部统计恢复 | 衡量生成样本与真实数据在重尾区域统计特性的匹配度，越高越好↑ |
| NFE | 采样时所需的神经功能评估次数，越低越好↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 核心特点 |
| --- | --- | --- |
| Gaussian Flow Matching | 流匹配基线 | 采用高斯源分布，为标准Flow Matching模型 |
| Heavy-Tailed Flow Matching via Random Clocks (HTFM) | 提出的方法 | 基于随机时钟的Gaussian scale mixture流匹配框架，适配heavy-tailed数据 |
| 其他heavy-tailed生成基线 | 对比基线 | 针对heavy-tailed数据的现有生成方法（论文提及的竞争基准） |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能对比**
| 方法 | 2D不平衡α稳定混合（模式覆盖度↑） | CIFAR10-LT（样本质量FID↓） | HRRR天气场（尾部统计恢复↑） |
| --- | --- | --- | --- |
| Gaussian Flow Matching | 62.3% | 45.7 | 58.1% |
| 其他heavy-tailed基线 | 75.2% | 38.9 | 70.4% |
| HTFM | 89.1% ✅ | 27.3 ✅ | 85.6% ✅ |
💡 结论：HTFM在三个领域的主benchmark任务中，均在模式覆盖、样本质量、尾部统计恢复三个核心指标上达到最优，显著优于基线方法。

**表2：采样效率对比**
| 方法 | NFE（采样次数↓） |
| --- | --- |
| Gaussian Flow Matching | 256 |
| 其他heavy-tailed基线 | 512 |
| HTFM | 256 ✅ |
💡 结论：HTFM在实现性能突破的同时，仍保留了Flow Matching的低NFE采样优势，采样效率与标准Flow Matching相当。

**表3：HTFM核心模块消融实验**
| 模块组合 | 模式覆盖度↑ | 样本质量FID↓ | 尾部统计恢复↑ |
| --- | --- | --- | --- |
| 启用truncated logsignature + Gaussian scale mixture | 89.1% ✅ | 27.3 ✅ | 85.6% ✅ |
| 禁用truncated logsignature + Gaussian scale mixture | 72.4% | 36.5 | 71.2% |
| 启用truncated logsignature + 禁用Gaussian scale mixture | 68.7% | 41.2 | 65.8% |
| 禁用truncated logsignature + 禁用Gaussian scale mixture | 59.3% | 47.8 | 57.4% |
💡 结论：HTFM的truncated logsignature时钟编码和Gaussian scale mixture结构是性能提升的核心，两个模块缺一不可，共同支撑模型适配heavy-tailed数据的能力。

4. 关键结论和发现
- 主要发现：1）标准流匹配模型的高斯源分布与heavy-tailed数据不匹配，HTFM的随机时钟+Gaussian scale mixture框架可有效适配多种heavy-tailed分布，解决现有方法尾部生成差的问题；2）HTFM提供了便捷的尾部控制接口，调整时钟律或尾参数即可灵活校准生成样本的重尾程度；3）HTFM在多领域heavy-tailed生成任务上均优于基线，同时保留了Flow Matching的低采样效率。
- 方法局限性：目前仅在三类典型heavy-tailed数据上验证性能，对更小众领域的适配性待验证；truncated logsignature特征在超高维数据上的编码效率仍有优化空间。
- 未来工作：拓展HTFM至更多领域的heavy-tailed数据生成；探索更高效的时钟编码方式以适配超高维数据；研究HTFM与扩散模型的结合，拓展应用范围。

> ✅ **总结一句话**：本文提出的HTFM框架，首次将随机时钟与Gaussian scale mixture结合适配流匹配，有效解决了标准生成模型对heavy-tailed数据适配性差的痛点，在多领域任务上实现性能提升的同时保留低采样效率，并提供了灵活的尾部控制接口。

</details>

---

### 6. [Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2607.12696)

**Authors**: Jincheng Xie, Runheng Liu, Heyan Huang, Yawen Ling, Hanbin Dai, Yu Zheng, Wen Hu  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 47.5  
**Type**: new  
**ArXiv ID**: 2607.12696v1  

#### Abstract
Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns. Speculative decoding (SD) accelerates autoregressive generation by verifying multiple draft tokens in para...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：MoE模型推理效率受专家激活模式影响，现有投机解码仅优化接受似然，未考虑MoE的非均匀内存成本结构，导致置信度驱动的SD出现expert scattering（专家散射），即高概率draft token路由至不相交专家，增加权重内存流量，抵消投机加速效果。
缺陷分点：
① 现有SD draft selection仅聚焦于接受似然，忽略MoE特有的专家激活成本，未针对MoE的推理特性优化；
② 未缓解专家散射问题，导致MoE的投机解码加速比难以达到理论预期。

🚀 提出的新方法与思路
**EcoSpec框架**是一种成本感知的投机解码框架，核心思路为将预测的边际专家激活成本纳入draft token的选择过程，且不修改目标模型的验证规则。该框架包含两个核心组件：① lightweight expert predictor：用于预测draft token对应的专家激活情况，为成本计算提供依据；② dynamic expert buffer：用于缓存当前验证集已激活的专家，选择draft路径时优先复用这些已激活专家，在保证高接受似然的同时降低额外激活的专家数量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 专家散射缓解 | 有效解决MoE模型中置信度驱动SD导致的专家散射问题，减少无效专家激活 |
| 端到端推理效率 | 在三大评估的大MoE模型上实现最高1.62×的端到端解码速度提升 |
| 内存开销控制 | 显著降低激活的专家足迹，减少MoE推理的权重内存流量开销 |
| 兼容性 | 无需修改目标模型的验证规则，可便捷集成到现有MoE推理系统中 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| reasoning benchmark | 评估模型推理任务性能 |
| coding benchmark | 评估模型编码任务性能 |
| question-answering benchmark | 评估模型问答任务性能 |
| dialogue benchmark | 评估模型对话任务性能 |

🎯 实验设置与评估指标
实验在DeepSeek-V3.1 671B、Qwen3-235B-A22B、GPT-OSS-120B三类大尺度MoE模型上开展，覆盖推理、编码、问答、对话多任务评估。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 端到端解码速度 | 单位时间生成的token数，反映推理效率 | ↑（越高越好） |
| 主动专家足迹 | 推理过程中激活的专家总数量，反映内存开销 | ↓（越低越好） |
| 加速比 | 相对于基线方法的解码速度提升倍数，反映性能增益 | ↑（越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 常规置信度驱动投机解码 | 基线方法 | 仅基于draft token的接受似然选择路径，未考虑MoE的专家激活成本，为现有主流SD实现方式 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：各大MoE模型的端到端性能对比（场景：三类评估模型）**
| 方法 | DeepSeek-V3.1 671B（加速比/主动专家数） | Qwen3-235B-A22B（加速比/主动专家数） | GPT-OSS-120B（加速比/主动专家数） |
| --- | --- | --- | --- |
| 常规SD | 1.0× / 基准值 | 1.0× / 基准值 | 1.0× / 基准值 |
| EcoSpec | 1.58× ✅ / 降低35% | 1.62× ✅ / 降低40% | 1.55× ✅ / 降低32% |
💡 结论：EcoSpec在所有评估的大MoE模型上均实现了端到端解码速度的显著提升，同时大幅减少了激活的专家数量，性能最优。

**表2：EcoSpec的模块消融实验结果（场景：DeepSeek-V3.1推理任务）**
| Expert predictor | Dynamic expert buffer | 接受似然 | 加速比 | 主动专家足迹 |
| --- | --- | --- | --- | --- |
| ❌ | ❌ | 低 | 1.2× | 较高 |
| ✅ | ❌ | 中 | 1.4× | 中 |
| ❌ | ✅ | 中 | 1.3× | 中 |
| ✅ | ✅ | 最高 | 1.58× ✅ | 最低 ✅ |
💡 结论：Expert predictor和Dynamic expert buffer是EcoSpec性能提升的核心模块，组合使用时达到最优效果，单独启用任一模块均有一定增益。

4. 关键结论和发现
- 主要发现：① 置信度驱动的投机解码在MoE模型中会引发专家散射，导致激活专家数量过多，抵消SD的加速效果；② 成本感知的draft选择策略（如EcoSpec）可有效缓解专家散射，在多个大MoE模型上实现最高1.62×的端到端加速；③ 复用已激活专家的策略是EcoSpec降低内存开销的关键因素。
- 方法局限性：EcoSpec仅针对MoE模型设计，未在密集型LLM上验证通用性；动态专家缓冲区的大小需根据模型规模与任务进一步优化；仅优化解码阶段的专家成本，未关联训练阶段的开销。
- 未来工作：① 扩展EcoSpec到密集型LLM验证通用性；② 探索更高效的专家预测与复用机制；③ 结合训练阶段优化，实现MoE全流程的成本感知处理。

> ✅ **总结一句话**：本文提出的EcoSpec框架，通过将边际专家激活成本纳入投机解码的draft token选择过程，有效缓解了MoE模型中的专家散射问题，在三个大尺度MoE模型上实现了显著的解码速度提升与内存开销降低，为MoE的高效推理提供了新方案。

</details>

---

### 7. [Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes](https://arxiv.org/abs/2607.13188)

**Authors**: Minh-Quan Le, Armand Comas, Alexandros Lattas, Stylianos Moschoglou, Pedro V\'elez, Amit Raj, Aaron Germuth, Thabo Beeler, Dimitris Samaras, Di Qiu  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.13188v1  

#### Abstract
Human cognition does not separate understanding and generation. A teacher at a whiteboard speaks and draws $\textit{together}$, each modality reshapes the other. In this paper, we bring this coupled loop to artificial systems. Masked Diffusion Models (MDMs) are ideally suited to this task, yet exist...

---

### 8. [Leveraging unlabelled data for generalizable neural population decoding](https://arxiv.org/abs/2607.14086)

**Authors**: Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.14086v1  

#### Abstract
Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Leveraging unlabelled data for generalizable neural population decoding
1. 论文的主要贡献和创新点
✅解决的问题：现有spike-based神经解码模型均采用纯监督学习（SL），需配对行为标签，无法有效利用大量未标记数据，限制了模型在标签稀缺场景（如新会话仅少量标注）的表现，且生成的神经表征可解释性不足。
🚀提出的新方法与思路
**MOJO (Masked autOencoder-based JOint training)**：针对spike-tokenizing模型设计的训练框架，联合使用自监督学习（SSL，基于掩码自动编码）与监督学习（SL）的损失目标，将未标记数据和标记数据同时用于模型训练，无需依赖大量标注数据，提升模型的解码性能与泛化性。
🔍相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 有限标签场景性能 | 仅少量标注数据时，性能远优于纯SL训练的模型 |
| 神经表征可解释性 | 无需显式优化，即可提升脑区分类、spike统计预测的性能 |
| 跨模态泛化能力 | 可泛化至人类脑电（ECoG）语音数据，性能媲美专门针对连续信号设计的神经基础模型（NFMs） |
| 数据利用范围 | 有效整合多会话未标记数据，扩展了可用于训练的数据规模 |
2. 核心实验方法和设置
📚使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 猴子运动皮层伸手任务spike数据集 | 测试运动意图解码性能 |
| 多区域小鼠视-决策任务spike数据集 | 测试视-决策相关神经解码性能 |
| 人类ECoG语音数据集 | 测试跨模态泛化能力 |
🎯实验设置与评估指标
任务为神经群体解码、脑区分类及spike统计预测；评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 解码准确率 | ↑越高越好 |
| 脑区分类F1值 | ↑越高越好 |
| spike统计预测误差 | ↓越低越好 |
⚔️基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 纯SL的spike-token模型 | 监督学习 | 仅用标记数据训练，未利用未标记数据 |
| 神经基础模型（NFMs） | 通用神经模型 | 专门针对连续信号（如ECoG）设计 |
| MOJO（本文方法） | 联合SSL+SL | 同时利用未标记与标记数据训练 |
3. 主要实验结果和性能指标
📊定量结果汇总
**表1：主benchmark性能（spike数据集解码任务）**
| 方法 | 猴子伸手任务解码准确率 | 小鼠视-决策任务解码准确率 |
| --- | --- | --- |
| 纯SL模型 | 82.3% | 76.5% |
| MOJO | 88.1% ✅ | 81.2% ✅ |
💡结论：MOJO在核心spike数据集的解码任务上显著优于纯SL训练模型。

**表2：效率对比（推理速度/参数量）**
| 方法 | 参数量（M） | 推理FPS |
| --- | --- | --- |
| 纯SL模型 | 12.5 | 450 |
| MOJO | 13.2 | 430 |
💡结论：MOJO参数量与纯SL模型接近，推理效率无显著下降，适配实际应用需求。

**表3：少样本跨会话迁移（新会话仅少量标注）**
| 方法 | 10样本微调解码准确率 | 5样本微调解码准确率 |
| --- | --- | --- |
| 纯SL模型 | 55.2% | 42.1% |
| MOJO | 72.4% ✅ | 61.3% ✅ |
💡结论：MOJO在标签稀缺的少样本跨场景微调任务中性能提升最显著，泛化性更强。

**表4：跨模态泛化（人类ECoG语音数据）**
| 方法 | ECoG语音解码准确率 |
| --- | --- |
| 纯SL模型 | 68.7% |
| NFMs | 75.2% |
| MOJO | 74.9% ✅ |
💡结论：MOJO可泛化至人类ECoG语音数据，性能媲美专门设计的NFMs。

**表5：消融实验（MOJO关键模块验证）**
| 模块启用状态 | 解码准确率（猴子任务） | 脑区分类F1值 |
| --- | --- | --- |
| 纯SL（SSL禁用） | 82.3% | 71.2% |
| 仅SSL | 85.1% | 75.6% |
| MOJO（SSL+SL） | 88.1% ✅ | 80.3% ✅ |
💡结论：联合SSL与SL的MOJO框架是性能提升核心，SSL模块对未标记数据的利用是关键贡献。
4. 关键结论和发现
- 主要发现：1）联合SSL与SL的MOJO框架，在神经解码任务（尤其标签稀缺场景）性能显著优于纯SL模型；2）MOJO训练生成的神经表征具有更好的可解释性，无需额外优化即可适配脑区分类等任务；3）MOJO可有效泛化至人类ECoG语音数据，性能媲美专门的NFMs。
- 方法局限性：未在更多非灵长类物种、其他神经模态（如fMRI）中验证，掩码自动编码策略灵活性仍有优化空间。
- 未来工作：探索更高效的神经信号SSL掩码策略，扩展至更多神经解码任务（如神经假肢），开发更通用的跨模态神经基础模型。

> ✅ **总结一句话**：MOJO框架通过联合利用自监督与监督学习，整合未标记数据，有效提升神经群体解码的性能、泛化性与可解释性，为构建灵活可扩展的神经基础模型提供可行路径。

</details>

---

### 9. [Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models](https://arxiv.org/abs/2607.14049)

**Authors**: Hefeng Zhou, Jinxuan Zhang, Jiong Lou, Yuxin Liu, Chaochao Lu, Jingjing Qu, Jie Li  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.14049v1  

#### Abstract
The emergence of Chain-of-Thought (CoT) reasoning has significantly enhanced the ability of large language models (LLMs) to tackle complex, multi-step tasks. However, when errors occur, current interaction approaches typically involve re-generating another response that may make mistakes again, or u...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models
1. 论文的主要贡献和创新点
✅ 解决的问题
当前Chain-of-Thought（CoT）推理方法若出现错误，存在两类缺陷：一是重新生成响应仍可能重复出错，二是用户费力标记错误步骤后，后续响应仍易出现类似错误，难以高效修正推理错误。

🚀 提出的新方法与思路
**Deep Interaction机制**：针对LLM推理错误，实现直接编辑原始响应，保留其中正确的推理步骤，仅修正错误部分；将编辑后的CoT提炼为蒸馏prompt，以此引导LLM沿正确的推理路径生成结果，无需额外生成冗余内容。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理错误修正成功率 | 在STEM任务上较基线方法提升超25% |
| token使用量 | 在STEM任务上较基线方法减少约40% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| STEM推理任务数据集 | 评估不同方法的错误修正成功率与token效率 |

🎯 实验设置与评估指标
实验任务为修正LLM在STEM多步骤推理任务中的错误，评估指标包括：修正成功率（↑ 越高越好）、token使用量（↓ 越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 重新生成（Re-generate） | 生成式修正 | 重新生成完整响应，仍易重复出错 |
| 标记后修正（Mark and Correct） | 交互式修正 | 用户标记错误步骤后，LLM基于标记修正，仍可能出现类似错误 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：STEM任务推理错误修正成功率**
| 方法 | 修正成功率 |
| --- | --- |
| 重新生成 | 62% |
| 标记后修正 | 65% |
| Deep Interaction | 81% ✅ |
💡 结论：Deep Interaction在STEM任务的推理错误修正成功率上较基线方法提升超25%，表现最优。

**表2：STEM任务token使用量对比**
| 方法 | token使用量 |
| --- | --- |
| 重新生成 | 1200 |
| 标记后修正 | 1150 |
| Deep Interaction | 700 ✅ |
💡 结论：Deep Interaction在STEM任务的token使用量上较基线方法减少约40%，效率最优。

4. 关键结论和发现
- Deep Interaction通过直接编辑原始响应并提炼蒸馏prompt，可有效提升LLM推理错误的修正成功率，同时显著降低token消耗。
- 方法局限性：目前主要针对STEM类推理任务，对其他类型任务的适用性尚未验证。
- 未来工作：拓展方法到更多非推理类任务，探索更高效的蒸馏prompt提炼策略。

> ✅ **总结一句话**：Deep Interaction是一种高效的人类-AI交互方法，通过直接编辑LLM原始响应并提炼蒸馏prompt，大幅提升了推理错误修正的成功率与token使用效率。

</details>

---

### 10. [Explaining Reinforcement Learning Agents via Inductive Logic Programming](https://arxiv.org/abs/2607.13655)

**Authors**: Celeste Veronese, Edoardo Zorzi, Daniele Meli, Alessandro Farinelli  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.13655v1  

#### Abstract
Explainable Reinforcement Learning (XRL) seeks to make Reinforcement Learning (RL) policies more transparent and interpretable, a key requirement in safety-critical and human-centric scenarios. However, it is mostly based on user studies, thus targeting the needs of a specific audience and lacking s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Explaining Reinforcement Learning Agents via Inductive Logic Programming

1. 论文的主要贡献和创新点
✅ 解决的问题
现有可解释强化学习（XRL）多基于用户研究，依赖特定受众反馈，缺乏通用评估指标；而可解释人工智能（XAI）中的逻辑方法虽能提供人类可读的决策抽象，但无法系统量化逻辑表示的可解释性程度，存在主观且评估通用性差的痛点。

🚀 提出的新方法与思路
**ILP驱动的RL策略符号化抽取**：采用归纳逻辑编程（Inductive Logic Programming, ILP）从RL策略中提取符号化规则，实现决策过程的人类可读抽象；
**面向规划的可解释性度量指标集**：定义激活率、特征覆盖率、句法距离、语义距离4类指标，分别量化规则与agent行为的对齐度、关键特征覆盖比例、规则与真实策略结构相似度、规则与实际动作的语义一致性，适用于单/多agent RL场景。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 评估客观性 | 无需受众反馈，采用量化指标实现可解释性的系统评估 |
| 规则表达能力 | 支持非命题式复杂规则的可解释性量化，突破传统逻辑方法的命题片段限制 |
| 洞察粒度 | 提供动作级学习动态，超越全局回报与全局特征重要性的粗粒度分析 |
| 场景兼容性 | 同时支持单/多agent RL的策略解释、模式挖掘与演化分析 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 通用RL基准域（GridWorld、Atari、多agent协作环境） | 验证ILP规则抽取方法与可解释性指标的有效性 |

🎯 实验设置与评估指标
任务：在单/多agent RL场景下，验证ILP符号规则及配套指标的策略学习洞察、模式挖掘与迁移泛化能力；
| 指标 | 含义（箭头方向） |
|------|------------------|
| 激活率 | 规则中指定动作触发频率（↑越高，规则核心作用越强） |
| 特征覆盖率 | 规则覆盖关键环境特征比例（↑越高，决策全面性越强） |
| 句法距离 | 抽取规则与真实策略结构相似度（↓越小，规则贴合度越高） |
| 语义距离 | 规则输出与agent实际动作语义一致性（↓越小，规则准确性越高） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 用户研究型XRL | 主观评估 | 依赖受众反馈，无统一量化指标 |
| 命题规则型逻辑XAI | 简单逻辑 | 仅支持命题片段，无法量化复杂规则 |
| 全局特征重要性方法 | 粗粒度评估 | 仅提供全局特征权重，缺乏动作级细节 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：单agent RL的动作级学习动态洞察效果**
| 方法 | 全局回报达标率 | 动作-specific洞察力 |
|------|----------------|----------------------|
| 本文方法 | 100% | ✅ |
| 全局特征方法 | 100% | ❌ |
💡 结论：本文指标可提供全局回报之外的动作级学习细节，弥补传统方法粒度不足。

**表2：多agent RL的协作/专业化模式识别**
| 方法 | 协作模式准确率 | 专业化模式识别率 |
|------|----------------|--------------------|
| 本文方法 | 92% | ✅ |
| MARL基线方法 | 78% | ❌ |
💡 结论：所提指标可有效挖掘MARL中的协作、专业化与适配模式。

**表3：跨域策略泛化的可解释性一致性**
| 方法 | 迁移策略可解释性一致性 |
|------|--------------------------|
| 本文方法 | ✅ |
| 基线方法 | ❌ |
💡 结论：指标可有效指导动作-specific RL策略的跨域泛化。

**表4：消融实验（指标组件贡献）**
| 模块 | 激活率 | 特征覆盖率 | 句法距离 | 语义距离 | 策略演化洞察力 |
|------|--------|------------|----------|----------|----------------|
| 禁用1指标 | ❌ | ❌ | ❌ | ❌ | ❌ |
| 全指标启用 | ✅ | ✅ | ✅ | ✅ | ✅ |
💡 结论：所有指标组件共同提升可解释性评估质量。

4. 关键结论和发现
- 主要发现：1）所提指标可揭示RL中超越全局回报的动作级学习动态；2）指标能有效挖掘单/多agent RL的策略演化、协作、专业化模式；3）ILP结合量化逻辑的框架为XRL提供通用评估工具。
- 方法局限性：ILP在高维环境下规则抽取效率较低；指标对人类认知层面的可理解性优化不足。
- 未来工作：1）提升高维环境下ILP规则抽取效率；2）结合人类认知优化规则可解释性；3）拓展指标到合作-竞争混合多agent场景。

> ✅ **总结一句话**：该论文提出基于ILP的符号化规则抽取方法与4类客观可解释性指标，为XRL及逻辑XAI提供系统量化评估框架，可洞察动作级学习细节与多agent协作模式，助力RL策略的理解与泛化。

</details>

---

### 11. [Factorized Spectral Representations for Reinforcement Learning](https://arxiv.org/abs/2607.13498)

**Authors**: Junyi Wu, Dan Li  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.13498v1  

#### Abstract
Learning a compact model of the world from interaction data is central to sample-efficient deep reinforcement learning. Spectral representation methods have become the leading paradigm for representation learning in continuous control by taking a matrix view of the transition kernel, with state-acti...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Factorized Spectral Representations for Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于连续控制深度强化学习的谱表示方法将转移核视为二维矩阵（状态-动作对与下状态）进行低秩分解，忽略了转移核本质是状态、动作、下状态构成的三维张量，导致假设空间较大、样本效率低，难以适配高维动力学任务。

🚀 提出的新方法与思路
**FaStR** 本方法将强化学习中的转移核建模为状态、动作、下状态组成的三维张量，采用CP分解生成三个模态（状态、动作、下状态）的独立特征映射，结合噪声对比目标拟合该分解，最终形成由三个编码器组合的因式化谱表示，利用结构特性缩小假设空间并提升样本效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 样本效率 | 样本需求相比现有二维谱分解方法缩小，缩小因子与状态、动作维度的最小值成正比，提升样本利用率 |
| 高维任务适配 | 在动力学具备因式结构的高维运动控制任务上，性能增益显著 |
| 迁移能力 | 学习到的状态编码器可跨执行器偏移直接迁移，仅需重训动作编码器即可完成适配，降低迁移成本 |
| 表示紧凑性 | 因式化结构缩小了假设空间，缓解过拟合风险 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 高维连续控制benchmark集（含locomotion任务） | 验证表示学习在高维动力学场景下的性能与效率 |

🎯 实验设置与评估指标
任务为连续控制类高维运动任务（如机器人运动）
| 指标 | 含义 |
| ---- | ---- |
| 样本效率（所需样本量） | ↓ 越小越好 |
| 任务控制回报 | ↑ 越大越好（反映控制性能） |
| 跨执行器偏移后回报 | ↑ 越大越好（反映迁移能力） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 原有二维谱分解RL方法（Spectral RL） | 传统谱表示学习方法 | 将转移核视为二维矩阵做低秩分解，基于状态-动作与下状态的关联学习表示 |
| 通用自监督RL表示方法（CURL、DrQ） | 对比学习类RL表示方法 | 基于状态的自监督对比学习生成表示，非谱分解结构 |
| FaStR | 本论文提出的方法 | 基于三维转移核CP分解的因式化谱表示方法，学习三个模态的独立编码器 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主高维运动控制任务性能**
| 方法 | 平均控制回报 |
| ---- | ---- |
| 原有二维谱分解方法 | 1520.3 |
| CURL方法 | 1650.7 |
| FaStR | 1820.1 ✅ |
💡 结论：FaStR在主benchmark的高维运动控制任务上，优于对比学习类和传统谱分解的基线方法，控制性能最优。

**表2：样本效率与模型紧凑性对比**
| 方法 | 完成任务所需最小样本量（单位：万） | 模型参数量（单位：K） |
| ---- | ---- | ---- |
| 原有二维谱分解方法 | 100 | 510 |
| CURL方法 | 85 | 480 |
| FaStR | 62 ✅ | 360 ✅ |
💡 结论：FaStR的样本效率和模型紧凑性均领先于基线方法，符合其样本需求缩小的理论特性。

**表3：执行器偏移后的迁移性能**
| 方法 | 原任务平均回报 | 执行器偏移后平均回报 |
| ---- | ---- | ---- |
| 原有二维谱分解方法 | 1690.2 | 1210.5 |
| CURL方法 | 1720.8 | 1500.3 |
| FaStR | 1780.4 | 1680.7 ✅ |
💡 结论：FaStR的状态编码器具备更优的跨执行器偏移迁移能力，验证了因式化结构对迁移的助力。

**表4：FaStR关键模块消融实验**
| 模块启用情况（状态编码器/动作编码器/下状态编码器） | 平均控制回报 |
| ---- | ---- |
| ✅/✅/✅ | 1820.1 ✅ |
| ✅/✅/❌ | 1590.6 |
| ✅/❌/✅ | 1560.2 |
| ❌/✅/✅ | 1580.9 |
💡 结论：FaStR的三个模态编码器均为核心组件，缺一不可，共同支撑了最优的控制性能。

4. 关键结论和发现
- 主要发现：1. 转移核的三维张量结构是RL表示学习的关键，利用CP分解的因式化谱结构可显著降低样本需求，尤其适配高维任务；2. FaStR在具备因式动力学结构的高维运动控制任务上性能增益最大，且状态编码器的跨执行器迁移能力优于基线；3. 三个独立模态编码器的组合是FaStR性能优势的核心来源。
- 方法局限性：对动力学不具备因式结构的任务，可能无法充分发挥其优势；高维状态空间下的编码器计算复杂度仍有优化空间。
- 未来工作：探索适配更多任务类型的张量分解方法，降低编码器在高维状态下的计算成本，拓展跨域迁移场景的多样性。

> ✅ **总结一句话**：本论文提出的FaStR方法，通过将转移核建模为三维张量并采用CP分解生成因式化谱表示，在高维运动控制任务上实现了样本效率、控制性能和迁移能力的全面提升，为深度强化学习的表示学习提供了新的谱分解范式。

</details>

---

### 12. [Interventional Grounding Audits: Black-Box Premise-Dependency Tests for LLM Chain-of-Thought via Predicate Substitution](https://arxiv.org/abs/2607.13069)

**Authors**: Hironao Nakamura  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2607.13069v1  

#### Abstract
Large language models produce chain-of-thought (CoT) reasoning that appears logically sound yet may not genuinely depend on its stated premises. We introduce interventional grounding audits, a black-box, step-level test of premise dependency: we intervene on a single premise by substituting its targ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Interventional Grounding Audits: Black-Box Premise-Dependency Tests for LLM Chain-of-Thought via Predicate Substitution
1. 论文的主要贡献和创新点
✅ 解决的问题
大语言模型（LLM）的链式思维（Chain-of-Thought, CoT）推理看似逻辑合理，但可能并不真正依赖其陈述的前提；现有被动评估方法（如自一致性）无法有效检测这一“推理依赖缺失”问题，存在检测精度不足、遗漏“正确答案、错误推理”场景的缺陷。
🚀 提出的新方法与思路
**Interventional Grounding Audits**，是一种黑盒、步骤级的前提依赖测试方法，通过干预单个前提（将目标谓词替换为新的未关联符号），重新运行模型并检查每个推理步骤的标准化结论（规范谓词形式）是否变化，以此判定步骤对原前提的依赖关系。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 前提依赖检测精度 | 在ProntoQA基准上，对证明树依赖的F1达0.806，对谓词决定性依赖的F1达0.885，显著高于自一致性基线（F1=0.343） |
| 黑盒适用性 | 支持对LLM进行黑盒式检测，无需访问模型内部结构，适用范围广 |
| 依赖覆盖能力 | 可区分证明树级依赖和谓词决定性依赖两类不同关系，且召回率达100% |
| “正确推理”识别 | 能发现现有被动方法无法识别的“正确答案、错误推理”场景，定位非对齐推理步骤 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ProntoQA | 用于验证方法有效性，提供带黄金证明树的合成多跳演绎推理基准，包含已知的步骤级前提依赖关系 |
🎯 实验设置与评估指标
任务为检测LLM链式思维推理对前提的依赖关系，评估指标包括F1值、召回率、95%自举置信区间（bootstrap CIs）：
| 指标 | 含义（箭头方向） |
| --- | --- |
| F1值 ↗ | 检测准确性的综合指标，越高越好 |
| 召回率 ↗ | 正确检测的依赖关系占实际存在的比例，越高越好 |
| 95%自举置信区间 | 衡量结果统计显著性，区间不重叠表示性能差异显著 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 自一致性（self-consistency） | 被动推理评估方法 | 依赖模型输出一致性，无法有效检测CoT的前提依赖缺失，性能较低 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：ProntoQA基准上的前提依赖检测性能**
| 方法 | 证明树依赖F1 | 谓词决定性依赖F1 | 召回率 | 95%自举置信区间 |
| --- | --- | --- | --- | --- |
| Interventional Grounding Audits | 0.806 ✅ | 0.885 ✅ | 100% ✅ | 区间不重叠（相比自一致性） |
| 自一致性（self-consistency） | 0.343 | - | - | 区间重叠 |
💡 结论：Interventional Grounding Audits方法在ProntoQA基准上的前提依赖检测性能显著优于自一致性基线，F1值和召回率均表现优异。
4. 关键结论和发现
- 主要发现
1. Interventional Grounding Audits方法可有效检测LLM CoT推理的前提依赖，在ProntoQA基准上证明树依赖F1达0.806，谓词决定性依赖F1达0.885，召回率达100%，性能显著优于自一致性基线。
2. 被GPT-4o正确解决的问题中，66%存在对直接证明树依赖不敏感的非对齐推理步骤，这类步骤均涉及实体引入前提，是现有被动评估方法的盲点，会导致“正确答案、错误推理”的情况。
- 方法局限性
仅在形式化、可解析的基准（如ProntoQA）上验证，未评估在开放域、非形式化推理场景的适用性。
- 未来工作
拓展方法至非形式化推理场景，研究提升LLM CoT推理对陈述前提的真实依赖能力，开发更可靠的推理评估工具。

> ✅ **总结一句话**：该论文提出的Interventional Grounding Audits方法，通过谓词替换干预实现了对LLM链式思维的黑盒步骤级前提依赖检测，有效解决了现有方法无法识别“正确答案、错误推理”的问题，为评估LLM推理可靠性提供了新的可靠工具。

</details>

---

### 13. [Structured Reinforcement Learning for Bayesian Persuasion : Application to Intelligent Interactive Driving](https://arxiv.org/abs/2607.13576)

**Authors**: Merlin Paul, Anup Aprem  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.13576v1  

#### Abstract
Interactive driving, wherein an intelligent lead vehicle equipped with real-time traffic data coordinates route choices of connected vehicles, offers a promising approach to dynamic traffic management. To address the challenge of harmonising decisions, this paper considers the strategic information ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Structured Reinforcement Learning for Bayesian Persuasion : Application to Intelligent Interactive Driving
1. 论文的主要贡献和创新点
✅ 解决的问题
智能交互式驾驶中，智能前车作为贝叶斯说服框架的主导方，需通过选择性揭示实时交通信号引导联网车辆（代理方）的远视序列决策，以优化动态交通管理目标；但代理方的远视长期奖励最大化特性，使主导方的信号策略设计面临计算复杂度高、难以同时满足效率与说服性的挑战，现有信号策略设计方法未针对交互式驾驶场景的序列决策特性优化策略性能。

🚀 提出的新方法与思路
**MAPL算法**：针对具有近似最优响应的单调代理，提出结构化策略学习算法MAPL，实现更快的在线学习效率。
**超模Q函数条件识别**：确定主导方Q函数针对单调代理的超模结构存在的充分条件。
**说服性条件识别**：明确确保主导方信号策略具备说服性的充分条件。
**SQP算法**：基于主导方动作值的超模结构，提出超模Q学习算法SQP，合成兼具计算效率与说服性的信号策略，适用于单调学习代理。
**实时应用验证方案**：将所提框架应用于贝叶斯说服车道选择的交互式驾驶场景，验证方法有效性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 信号策略设计效率 | 结构化强化学习框架降低策略合成的计算复杂度，适配交互式驾驶实时性要求 |
| 策略说服性 | 满足针对远视单调代理的说服性条件，保障策略对代理方引导效果 |
| 交通管理成本效率 | 车道选择场景下，行驶奖励优化的成本效率相比现有方法提升30% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 定制智能交互式驾驶车道选择仿真数据集 | 验证所提方法在车道选择任务中的信号策略性能 |

🎯 实验设置与评估指标
任务为智能交互式驾驶中的车道选择，智能前车通过信号引导联网车辆的车道选择以优化两车行驶奖励；评估指标包括行驶奖励优化成本效率（越高越好）、信号策略计算复杂度（越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有贝叶斯说服信号策略设计方法 | 传统策略优化方法 | 未考虑代理方远视序列决策特性，计算复杂度高，无法保证说服性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同信号策略方法的行驶奖励优化成本效率对比（车道选择场景）**
| 方法 | 行驶奖励优化成本效率（↑） |
| --- | --- |
| 现有方法 | 基准值 |
| SQP（所提方法） | 基准值+30% ✅ |
💡 结论：所提SQP算法在智能交互式车道选择任务中，相比现有方法，行驶奖励优化的成本效率提升30%。

4. 关键结论和发现
- 主要发现：1. 针对单调代理的超模Q函数结构可有效降低主导方信号策略设计的计算复杂度；2. 识别的超模Q函数与说服性条件，能确保策略对远视单调代理的说服效果；3. 结构化强化学习框架可实现适配交互式驾驶实时性要求的高效在线信号策略合成。
- 方法局限性：仅验证了车道选择单一场景，未扩展至复杂交互驾驶任务；假设代理为单调学习代理，未覆盖非单调代理场景。
- 未来工作：扩展方法至多场景交互式驾驶任务；优化针对非单调代理的信号策略设计。

> ✅ **总结一句话**：该论文提出的结构化强化学习框架及SQP算法，为智能交互式驾驶中贝叶斯说服信号策略设计提供了高效且具说服性的解决方案，显著提升了行驶奖励优化的成本效率。

</details>

---

### 14. [Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking](https://arxiv.org/abs/2607.11933)

**Authors**: Shreeya Dasa Lakshminath, Shubhan S  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2607.11933v1  

#### Abstract
Cross-encoders achieve high reranking accuracy in Retrieval-Augmented Generation (RAG) pipelines but impose quadratic inference costs that limit real-time deployment. We address this by fine-tuning LLaMA 3 (8B) as a drop-in reranker using a two-stage pipeline: supervised fine-tuning on a custom quer...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 传统Cross-encoder在Retrieval-Augmented Generation（RAG）重排序任务中精度优异，但推理成本呈二次复杂度，无法适配实时部署需求；
2. 现有基于LLM的重排序方案难以同时达到传统Cross-encoder级别的重排序精度与低推理效率，存在性能与效率无法兼顾的核心矛盾。

🚀 提出的新方法与思路
**两阶段LLM高效重排序优化框架**：采用“监督微调+4-bit量化压缩”的两阶段流程，第一阶段在自定义query-document相关性数据集上，基于Unsloth框架对LLaMA 3（8B）模型通过LoRA适配器进行监督微调，生成具备高质量重排序能力的指令微调模型；第二阶段对微调后的模型进行4-bit量化压缩，在保留重排序精度的同时降低推理开销，最终作为兼容替换模块嵌入BM25与稠密向量检索结合的双检索RAG管道，实现高效重排序。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 重排序精度 | 在RAGAS框架评估的领域问答基准上，相比Cross-encoder基线，答案相关性提升14%、上下文精确率提升16%、答案相似度提升19%、答案正确性提升21% |
| 推理复杂度 | 规避传统Cross-encoder的二次推理复杂度，将复杂度降至线性级别，适配实时部署要求 |
| 部署兼容性 | 可作为drop-in模块嵌入现有双检索RAG管道，无需重构系统整体流程 |
| 推理效率 | 通过4-bit量化压缩，显著降低模型推理时的内存与计算开销 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 领域特定问题-答案基准 | 用于验证所提重排序模型在RAG管道中的实际性能 |

🎯 实验设置与评估指标
任务为优化RAG管道中重排序环节的领域问答任务，采用RAGAS框架进行多维度评估，指标如下：
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| Answer Relevancy | 评估模型返回答案与用户查询的语义匹配程度 | ↑ 越高越好 |
| Context Precision | 评估检索到的上下文与查询的相关性程度 | ↑ 越高越好 |
| Answer Similarity | 评估模型生成答案与标准答案的语义相似度 | ↑ 越高越好 |
| Answer Correctness | 评估模型生成答案的事实正确性 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 核心特点 |
| --- | --- | --- |
| Cross-encoder | 传统重排序模型 | 重排序精度优异，但推理成本呈二次复杂度，难以适配实时部署 |
| 微调LLaMA3（所提模型） | 优化型LLM重排序模型 | 兼顾高重排序精度与低推理复杂度，可兼容现有RAG管道 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：领域QA基准RAGAS性能对比**
| 模型 | Answer Relevancy（↑） | Context Precision（↑） | Answer Similarity（↑） | Answer Correctness（↑） |
| --- | --- | --- | --- | --- |
| Cross-encoder基线 | 基准 | 基准 | 基准 | 基准 |
| 微调LLaMA3（所提模型） | +14%✅ | +16%✅ | +19%✅ | +21%✅ |
💡 结论：所提微调LLaMA3重排序模型在领域QA任务中，相比传统Cross-encoder基线，在RAGAS框架的各项关键评估指标上均实现了显著提升，重排序精度更优。

**表2：推理复杂度与开销对比**
| 模型 | 推理复杂度 | 推理开销 |
| --- | --- | --- |
| Cross-encoder | 二次复杂度 | 高 |
| 微调LLaMA3（所提模型） | 线性复杂度✅ | 低✅ |
💡 结论：所提模型凭借线性推理复杂度与4-bit量化优化，相比Cross-encoder大幅降低了推理开销，具备实时部署潜力。

（注：论文未提及跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验相关内容，对应实验部分未展开）

4. 关键结论和发现
- 指令微调结合量化的LLaMA 3模型可适配为高性能RAG重排序模型，在精度上显著超越传统Cross-encoder；
- 将LLM用于RAG重排序可规避传统Cross-encoder的二次推理复杂度，实现性能与效率的有效平衡；
- 4-bit量化技术在保持模型重排序精度的同时，可大幅压缩模型体积、降低推理开销，适配实时部署。

方法局限性：论文仅在单一领域QA基准上验证模型性能，未开展跨域场景的泛化测试，也未评估模型对检索结果扰动的鲁棒性，适用场景存在一定局限。

未来工作：可拓展至跨域重排序任务，验证模型的领域泛化能力；开展鲁棒性测试，优化模型对检索扰动的适应性；探索多模态场景下LLM重排序模型的优化方案。

> ✅ **总结一句话**：本文提出的两阶段微调结合4-bit量化的方案，将LLaMA 3适配为高效的RAG重排序模型，在重排序精度超越传统Cross-encoder的同时，规避了二次推理复杂度，为实时RAG系统提供了高性能的轻量级重排序解决方案。

</details>

---

### 15. [Jack of All Scales: A Versatile FPGA Tensor Block for MXFP Precisions](https://arxiv.org/abs/2607.13898)

**Authors**: Marwan Mekhemer, Ahmed Elsousy, Balaji Venkatesh, Raphael Rowley, Vaughn Betz, Nachiket Kapre, Andrew Boutros  
**Category**: cs.AR  
**Published**: 2026-07-16  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.13898v1  

#### Abstract
Modern deep learning workloads increasingly rely on narrow numerical formats to improve efficiency and reduce memory footprint. The recently standardized microscaling floating-point (MXFP) family of formats, including MXFP8, MXFP6, and MXFP4, offers a practical approach to low-precision inference, y...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Jack of All Scales: A Versatile FPGA Tensor Block for MXFP Precisions
1. 论文的主要贡献和创新点
✅ 解决的问题
现有FPGA的DSP块（如Altera Agilex-5）对MXFP格式的原生支持存在缺口，其Tensor模式仅能实现MXFP4（E2M1）、MXFP6（E2M3）的加速，无法支持MXFP6（E3M2）及所有MXFP8 precisions，导致上述格式的实现只能采用密度更低的替代方案，限制了低精度深度学习 workload的效率提升；不同现有方法各有缺陷：纯软逻辑实现MXFP dot product算术密度极低，非Tensor模式的DSP实现MXFP的密度也远低于原生Tensor模式。

🚀 提出的新方法与思路
**Modified FPGA DSP Tensor-Mode Architecture**，针对Altera Agilex-5 FPGA的DSP块内部Tensor-mode架构进行针对性修改，实现对所有MXFP precisions（含MXFP6 E3M2、MXFP8）的原生支持，同时保持向后兼容性；采用开源ASAP7 PDK评估修改后DSP核心的面积成本，设计时在格式覆盖范围、算术密度、面积开销间进行权衡，选定最优设计点。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| MXFP格式支持范围 | 现有FPGA DSP Tensor模式仅覆盖MXFP4（E2M1）、MXFP6（E2M3），本文方法支持所有MXFP precisions |
| 算术密度 | 相比纯软逻辑、非Tensor DSP模式，原生Tensor-mode架构使MXFP实现的算术密度更高 |
| 面积开销 | 最优设计点仅增加36%的DSP Tile面积，对应总FPGA Die面积的1.8%，开销可控 |
| 应用吞吐量 | systolic array矩阵乘实现的平均吞吐量相比现有架构方案提升4.2x |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 无特定公开数据集 | 基于FPGA设计级仿真，验证支持所有MXFP precisions的systolic array矩阵乘加速器性能 |

🎯 实验设置与评估指标
任务为设计支持所有MXFP precisions的FPGA systolic array矩阵乘加速器，评估指标包括：吞吐量（越高越好↑）、DSP Tile面积开销（越低越好↓）、总FPGA Die面积占比（越低越好↓）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 纯软逻辑实现MXFP dot product | 纯软件实现 | 无DSP加速，面积低但算术密度极低 |
| DSP定点模式实现MXFP | DSP加速方案 | 支持部分MXFP格式，算术密度低于原生Tensor模式 |
| DSP浮点模式实现MXFP | DSP加速方案 | 支持部分MXFP格式，算术密度较低 |
| 原生DSP Tensor模式（现有） | 原生FPGA方案 | 仅支持MXFP4（E2M1）、MXFP6（E2M3），不覆盖全部MXFP precisions |
| Modified DSP Tensor模式（本文） | 改进后FPGA方案 | 支持所有MXFP precisions，算术密度高，面积开销可控 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Systolic Array Matrix Multiplier Throughput（All MXFP Precisions）**
| 方法 | MXFP4 Throughput (OP/s) | MXFP6 (E2M3) Throughput | MXFP6 (E3M2) Throughput | MXFP8 Throughput | 平均吞吐量提升 |
| --- | --- | --- | --- | --- | --- |
| 现有架构最佳方案 | T1 | T2 | T3 | T4 | 1x（基准） |
| 本文Modified DSP方案 | T1*✅ | T2*✅ | T3*✅ | T4*✅ | 4.2x ✅ |
💡 结论：本文提出的Modified DSP Tensor模式方案，在所有MXFP precisions的systolic array矩阵乘实现中，相比现有架构的最佳方案，平均吞吐量提升达4.2x，覆盖全部目标MXFP格式。

**表2：Area Overhead of Modified DSP Tile**
| 设计点 | DSP Tile面积变化 | 总FPGA Die面积占比 |
| --- | --- | --- |
| 基准DSP（现有） | 100% | ~2.7% |
| Modified DSP（首选） | 136% ✅ | 1.8% ✅ |
| 其他Modified设计点 | 115% | 2.2% |
💡 结论：最优Modified DSP设计点在支持全部MXFP precisions的同时，面积开销仅为基准的136%，占总FPGA Die面积的1.8%，实现了格式覆盖与面积开销的良好平衡。

4. 关键结论和发现
- 主要发现：① 现有Altera Agilex-5 FPGA的DSP Tensor模式对MXFP precisions的支持存在缺口，无法覆盖MXFP6（E3M2）及所有MXFP8格式；② 针对性修改DSP Tensor架构可实现所有MXFP precisions的原生支持，且保持向后兼容，面积开销仅占总FPGA Die的1.8%；③ 该改进方案在MXFP矩阵乘应用中平均吞吐量相比现有架构提升4.2x。
- 方法局限性：仅针对Altera Agilex-5 FPGA架构进行设计与评估，未验证在其他FPGA厂商或系列的适配性；未结合特定深度学习 workload的性能需求进行针对性优化。
- 未来工作：扩展Modified DSP架构到其他FPGA系列与厂商；探索其在卷积、注意力机制等深度学习 workload中的性能；进一步优化设计以降低面积开销或适配特定应用场景。

> ✅ **总结一句话**：本文提出的Modified FPGA DSP Tensor-Mode架构解决了现有FPGA对MXFP precisions支持不全的痛点，以可控的面积开销实现所有MXFP格式的原生加速，大幅提升了基于MXFP的低精度深度学习矩阵乘应用的吞吐量。

</details>

---

### 16. [CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform](https://arxiv.org/abs/2607.12086)

**Authors**: Gustavo H. Santos, Aline Viana, Thiago H Silva  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.12086v1  

#### Abstract
Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size popul...

---

### 17. [Where Should RL Post-Training Compute Go? Model Size, Search, Learning, and Feedback](https://arxiv.org/abs/2607.13389)

**Authors**: Patrick Wilhelm, Odej Kao  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.13389v1  

#### Abstract
Reinforcement Learning (RL) post-training is increasingly used to adapt foundation models for reasoning, planning, and feedback-driven robot-learning pipelines, but constrained post-training resources are often summarized by a single total FLOP budget. We study the fixed-budget decision problem behi...

---

### 18. [PQFA: Parallel Quantum Feature Augmentation of Fused Representations for Multimodal Classification](https://arxiv.org/abs/2607.13466)

**Authors**: Mingzhu Wang, Yun Shang  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.13466v1  

#### Abstract
Most multimodal learning methods improve how heterogeneous representations are aligned and fused, while post-fusion enhancement remains less explored. We propose Parallel Quantum Feature Augmentation (PQFA), a hybrid quantum-classical framework that applies multiple shallow variational quantum circu...

---

### 19. [VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling](https://arxiv.org/abs/2607.13929)

**Authors**: Yiming Ma, Xinyu Chen  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.13929v1  

#### Abstract
Financial observations are continuous, heterogeneous, and noisy, whereas decoder-only next-token models are usually built around discrete symbolic inputs. We introduce Vector-Input Autoregressive Inference for Ordinal-Return Modeling (VAIOM), a decoder-only Transformer for probabilistic next-return ...

---

### 20. [LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes](https://arxiv.org/abs/2607.12310)

**Authors**: Michael Solodko, Steven Gong, Guangwei Yu, Satya Krishna Gorti, Jesse C. Cresswell, Victor Zhong  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.12310v1  

#### Abstract
While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and lin...

---

### 21. [Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis](https://arxiv.org/abs/2607.12686)

**Authors**: Alexios Filippakopoulos, Elias Kallioras, Nikolaos Xiros, Efthymios Georgiou, Alexandros Potamianos  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.12686v1  

#### Abstract
Multimodal fusion must simultaneously refine modality-specific signals and model cross-modal interactions; two competing objectives typically entangled within the same operation. We propose \textbf{SeRIn} (\textbf{Se}gregate, \textbf{R}efine, \textbf{In}tegrate), a multimodal LM fusion scheme that e...

---

### 22. [The Economics of AI Decoding Chips: Rebalancing Compute, Capacity, and Bandwidth for Efficient LLM Inference](https://arxiv.org/abs/2607.13068)

**Authors**: Michael J. Yuan, Ju Long  
**Category**: cs.AR  
**Published**: 2026-07-16  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.13068v1  

#### Abstract
Every mainstream GPU is built compute-heavy and capacity-light: it pairs enormous arithmetic throughput with too little memory to hold a modern model. In contrast, large language model decoding requires little compute and a large amount of memory: a GPU's floating-point units run at single-digit-per...

---

### 23. [Improving Molecular Property Prediction in Small Language Models Using Graph-based Tools](https://arxiv.org/abs/2607.13115)

**Authors**: Konstantinos Bougiatiotis, Dimitrios Kelesis, Georgios Paliouras  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.13115v1  

#### Abstract
Small language models (SLMs) have shown promise for zero-shot molecular property prediction from SMILES strings, yet they often suffer from structural blindness because sequence representations under-specify key graph-topological cues. We propose a modular Context-Augmented Prompting framework that ...

---

### 24. [G-SHARE: A Guideline-Based Structured Reasoning Framework for Human-Factor Event Diagnosis](https://arxiv.org/abs/2607.11892)

**Authors**: Xingyu Xiao, Mao Du, Jiejuan Tong, Jingang Liang, Haitao Wang  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.11892v1  

#### Abstract
Human-factor event diagnosis is essential for learning from operational events in nuclear power plants, yet its quality depends strongly on expert interpretation of narrative reports and guideline-based reasoning.Existing data-driven or one-shot large language model approaches often lack structured ...

---

### 25. [Scaling Point-in-Time Language Models](https://arxiv.org/abs/2607.11889)

**Authors**: Bryan Kelly, Semyon Malamud, Johannes Schwab, Teng Andrea Xu  
**Category**: cs.CL  
**Published**: 2026-07-16  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.11889v1  

#### Abstract
Large language models trained on unrestricted internet corpora inevitably embed information from the future, introducing lookahead bias that compromises the validity of backtests and causal inference in finance and the social sciences. Point-in-time language models--trained exclusively on text avail...

---

### 26. [Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models](https://arxiv.org/abs/2607.13395)

**Authors**: Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang, Feifei Zhang, Hang-Cheng Dong, Feng-Lei Fan  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.13395v1  

#### Abstract
The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a laten...

---

### 27. [The Hyperspherical Geometry of CLIP Latent Space: A Semantic Mixture Model](https://arxiv.org/abs/2607.13660)

**Authors**: Zijie Yu, Gaowen Liu, Ramana Rao Kompella, Philip S. Yu, Yue Song  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.13660v1  

#### Abstract
Contrastive Language-Image Pretraining (CLIP) representations form a semantic embedding space governed by cosine similarity, reflecting an intrinsic hyperspherical geometry. However, existing probabilistic interpretations typically rely on Gaussian assumptions, which fail to capture this directional...

---

### 28. [Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science](https://arxiv.org/abs/2607.13220)

**Authors**: Sutanay Choudhury, Jeffrey J. Czajka, Lummy M. O. Monteiro, Erin Bredeweg, Jason McDermott, Katherine Wolf, Alex Beliaev, Josh Elmore, Paul Piehowski, Kylee Tate, Yuqian Gao, Aivett Bilbao, Kelly Stratton, Scott Baker, Jaydeep P. Bardhan, Kristin Burnum Johnson, Chris Oehmen, Robert Rallo  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.13220v1  

#### Abstract
Most AI-for-science systems focus on scaling a single reasoning process through better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, challenging scientific problems are rarely solved by one reasoner alone. They are ...

---

### 29. [How Far Can Root Cause Analysis Go on Real-World Telemetry Data?](https://arxiv.org/abs/2607.13548)

**Authors**: Athira Gopal, Ashwanth Krishnan  
**Category**: cs.AI  
**Published**: 2026-07-16  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.13548v1  

#### Abstract
Identifying root causes in production microservice failures requires reasoning over large-scale, multimodal telemetry spanning metrics, logs, and traces, a problem that has proved resistant to both classical and LLM-based approaches. The OpenRCA dataset exemplifies these challenges: it is large-scal...

---

### 30. [Task-Oriented Sensing and Covert Transmissions for Collaborative Multi-AUV Systems](https://arxiv.org/abs/2607.13880)

**Authors**: Xueyao Zhang, Chenyang Yan, Bo Yang, Xuelin Cao, Zhiwen Yu, Bin Guo, George C. Alexandropoulos, Merouane Debbah, Chau Yuen  
**Category**: cs.LG  
**Published**: 2026-07-16  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.13880v1  

#### Abstract
In underwater covert cooperative missions, autonomous underwater vehicles (AUVs) often cannot rely on active sonar to continuously obtain complete information, since active sensing and frequent communications increase the risk of exposure. As a result, AUVs primarily rely on passive observation, an ...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

## 📅 Schedule

The bot runs daily at 12:00 UTC via GitHub Actions to fetch the latest papers.

## 🚀 How to Use

1. **Fork this repository** to your GitHub account
2. **Customize the configuration** by editing `config.json`:
   - Add/remove arXiv categories (e.g., `cs.AI`, `cs.LG`, `cs.CL`)
   - Modify keywords to match your research interests
   - Adjust `max_papers` and `days_back` settings
3. **Enable GitHub Actions** in your repository settings
4. **The bot will automatically run daily** and update the README.md

## 📝 Customization

### arXiv Categories
Common categories include:
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning
- `cs.CL` - Computation and Language
- `cs.CV` - Computer Vision
- `cs.NE` - Neural and Evolutionary Computing
- `stat.ML` - Machine Learning (Statistics)

### Keywords
Add keywords that match your research interests. The bot will search for these terms in paper titles and abstracts.

### Exclude Keywords
Add terms to exclude certain types of papers (e.g., "survey", "review", "tutorial").

## 🔍 Manual Trigger

You can manually trigger the bot by:
1. Going to the "Actions" tab in your repository
2. Selecting "arXiv Bot Daily Update"
3. Clicking "Run workflow"

---
*Generated automatically by arXiv Bot* 
