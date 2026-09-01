# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-01 10:34:19 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO](https://arxiv.org/abs/2608.29357v1)

**Authors**: Saeed Khaki, Nima Safaei, Kamal Ginotra  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2608.29357v1  

#### Abstract
Multimodal search agents answer visual questions by interleaving image understanding, web retrieval, tool use, and evidence synthesis. Strong systems exist, but in two expensive regimes: proprietary frontier models such as GPT-5 and Gemini, or large open vision-language backbones trained with substa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO

1. 论文的主要贡献和创新点
✅解决的问题
现有强大多模态搜索代理系统依赖两种高成本场景：一是GPT-5、Gemini等专有前沿模型，二是经大量代理数据与强化学习训练的大型开放视觉-语言骨干模型；而在单节点预算下，将发布的代理轨迹蒸馏到更小骨干模型时，模型的可迁移机制及性能表现尚不明确，小模型代理的核心提升路径与瓶颈未得到系统研究。
🚀提出的新方法与思路
**LiteSearch-VL**：基于Qwen3-VL-2B和Qwen3-VL-4B构建的低计算成本多模态搜索代理。
**Trajectory Distillation**：使用发布的OpenSearch-VL代理轨迹作为蒸馏数据源，传递代理的核心行为范式。
**LoRA Adapters**：采用参数高效的LoRA适配器，适配小模型实现代理功能，降低训练与部署成本。
**Synthetic Step-DPO**：以GPT-5生成的硬负样本为基础，针对提前回答、错误工具使用、查询过弱、重复查询、忽略图像五种局部失败模式，进行步级别偏好优化，修正代理的行为偏差。
🔍相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 部署资源 | 仅需单节点预算，采用参数高效的LoRA适配器，无需大型计算集群 |
| 模型规模 | 基于Qwen3-VL-2B/4B等小模型构建，避免大模型的高训练与推理成本 |
| 核心性能 | 2B模型经全轨迹SFT后性能超过未蒸馏的4B基础模型，4B最优配置性能进一步提升 |

2. 核心实验方法和设置
📚使用的数据集
| 数据集 | 用途 |
| --- | --- |
| SimpleVQA、FVQA、LiveVQA、VDR-Bench-testmini | 用于评估LiteSearch-VL的多模态搜索代理性能 |
🎯实验设置与评估指标
任务为多模态搜索代理回答视觉问题，结合工具使用、信息检索与证据合成完成推理。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| macro Pass@1 | 宏平均Top1通过率，即模型正确通过测试样例的比例 | ↑ |
⚔️基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Off-the-shelf Qwen3-VL-4B base | 基线 | 未经过轨迹蒸馏或偏好优化的原始4B基础模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能
论文未报告表号，其在SimpleVQA、FVQA、LiveVQA、VDR-Bench-testmini四个数据集的12400个GPT-5-judged rollouts上的性能结果如下：
- 全轨迹SFT的Qwen3-VL-2B模型：macro Pass@1为28.4%；
- Off-the-shelf Qwen3-VL-4B base基线模型：macro Pass@1为25.6%；
- LiteSearch-VL的4B最优配置：macro Pass@1为30.8%；
💡结论：全轨迹监督微调是小多模态代理性能提升的核心，合成偏好学习与紧凑工具蒸馏仅作为性能细化手段，可进一步小幅提升最优配置的性能。
2. 效率对比
论文未报告。
3. 跨域/zero-shot迁移
论文未报告。
4. 鲁棒性/扰动测试
论文未报告。
5. 消融实验
论文仅报告了控制VDR step-budget的消融结果：额外的搜索轮次仅将代理的弃权预测转化为wrong_entity错误，并未提升正确答案的比例；其余模块（全轨迹SFT、合成偏好学习、紧凑工具蒸馏）的消融仅描述为细化而非相变提升，未报告具体的模块启用禁用及对应指标的表格内容。

4. 关键结论和发现
- 全轨迹监督微调可将Qwen3-VL-2B模型从几乎无法输出可用答案（1240个rollouts中1237个无答案）提升至28.4%的macro Pass@1，性能超过未蒸馏的Qwen3-VL-4B base模型；合成偏好学习与紧凑工具蒸馏仅能实现性能的细微优化，未触发性能相变。
- LiteSearch-VL的4B最优配置macro Pass@1达30.8%，为当前小模型代理的最优表现。
- 控制VDR步骤预算的消融显示，额外搜索轮次会将弃权转化为错误的实体预测，而非正确答案，明确答案验证是小多模态代理的下一个瓶颈，而非增加搜索深度。
- 方法局限性：论文未报告。
- 未来工作：针对小多模态代理的答案验证瓶颈进行优化，提升代理的推理准确性。

> ✅ **总结一句话**：LiteSearch-VL通过单节点预算下的轨迹蒸馏、参数高效LoRA适配及合成步级别DPO，实现了小模型多模态搜索代理性能的显著提升，明确小代理性能提升的核心路径及后续突破方向。

</details>

---

### 2. [Which one is banana man? Evaluating vision-language models in multi-turn pragmatic interpretation](https://arxiv.org/abs/2608.29571v1)

**Authors**: Alvin Wei Ming Tan, Ben Prystawski, Veronica Boyce  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 72.5  
**Type**: new  
**ArXiv ID**: 2608.29571v1  

#### Abstract
Flexible adaptation to context and shared pragmatic intuitions contribute to smooth human conversation. Iterated reference games---in which players repeatedly pick out novel referents using language---present a test case for agents' ability to perform context-sensitive pragmatic reasoning in multi-t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Which one is banana man? Evaluating vision-language models in multi-turn pragmatic interpretation
1. 论文的主要贡献和创新点
✅ 解决的问题
人类对话依赖对语境的灵活适应和共享语用直觉，迭代参考游戏是测试代理在多轮语言环境中执行语境敏感语用推理能力的案例；但现有研究缺乏对视觉-语言模型在该类多轮语用解释任务中的系统性评估，且发现评估的视觉-语言模型存在能利用先验语境但难以构建有效相关语境的缺陷，导致其缺乏高效语言协作所需的核心技能。

🚀 提出的新方法与思路
论文为评估视觉-语言模型在多轮语用解释中的能力，设计了针对迭代参考游戏的测试方案，通过调整语境的量、顺序、相关性，对比人类与视觉-语言模型在识别人类指代表达意图上的表现。

🔍 相比现有方法的优势
| 维度 | 内容 |
| ---- | ---- |
| 评估维度 | 系统性对比人类与视觉-语言模型在多轮语用解释任务中的表现，补充该领域的实证评估空白 |
| 考察视角 | 通过改变语境的量、顺序、相关性，全面考察模型对语境的适应性 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：在迭代参考游戏中，识别人类在不同语境（量、顺序、相关性变化）下生成的指代表达的意图。
论文未报告具体评估指标

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 人类 | 基准方法 | 表现稳定，为任务提供参照标准 |
| 评估的视觉-语言模型（VLM） | 对比方法 | 能利用先验语境解释人类指代表达，但难以构建有效相关语境 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
论文未报告
2. 效率对比（FPS / 参数量）
论文未报告
3. 跨域 / zero-shot 迁移
论文未报告
4. 鲁棒性 / 扰动测试
论文未报告
5. 消融实验
论文未报告

4. 关键结论和发现
- 人类在迭代参考游戏的指代表达意图识别任务中表现稳定。
- 评估的视觉-语言模型能利用先验语境解释人类的指代表达，但难以构建有效相关语境，无法对这类表达进行有效解释。
- 评估的视觉-语言模型缺乏高效语言协作所需的核心技能。
方法局限性：评估的视觉-语言模型在多轮语用解释任务中无法构建有效相关语境，缺乏对应协作技能。
未来工作：论文未明确提及未来工作方向。

> ✅ **总结一句话**：本论文通过迭代参考游戏任务的实证测试，系统性对比人类与视觉-语言模型的表现，揭示了现有评估的视觉-语言模型在多轮语用解释中难以构建有效相关语境的缺陷，为模型语言协作技能的提升提供了实证依据。

</details>

---

### 3. [HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering](https://arxiv.org/abs/2608.29088v1)

**Authors**: Zafar Ali, Asad Khan, Nimbeshaho Thierry, Nabila Amir, Adam A. Q. Mohammed, Pavlos Kefalas  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2608.29088v1  

#### Abstract
Multimodal question answering remains sensitive to noisy, incomplete, and weakly grounded evidence. Long unstructured contexts can introduce redundancy and encourage unsupported generation, while flat retrieval may overlook relations needed for multi-step reasoning. We present HANIA, a planner-guide...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态问答易受嘈杂、不完整、弱接地证据影响；长非结构化上下文存在冗余，会鼓励无支持生成；平面检索可能遗漏多步推理所需的关系。
🚀 提出的新方法与思路
**冻结VLM驱动的视觉证据提取**：采用冻结的视觉语言模型处理输入图像与文本，提取与问题相关的简洁视觉证据，具备明确弃权能力。
**两组有限状态规划器的证据协调**：构建输入接地的多模态图，应用两组有限状态规划器协调描述性与关系性两类证据。
**覆盖感知证据修剪模块**：基于相关性、图置信度、概念覆盖、模态多样性执行覆盖感知修剪，筛选出包含选定段落、视觉语句与图三元组的紧凑证据集。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 证据处理逻辑 | 引入多模态图结构与规划机制，缓解长上下文冗余及无支持生成问题 |
| 泛化能力 | 无需目标数据集微调，支持零样本场景 |
| 检索性能 | 可保留多步推理所需关系，优于平面检索 |
| 计算效率 | 跳过目标数据集微调与迭代检索环节，降低计算成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ScienceQA | 评估HANIA在接地多模态问答任务上的性能 |
🎯 实验设置与评估指标
任务为多模态接地问答，评估指标及含义如下：
| 指标 | 含义 |
| --- | --- |
| 答案准确率 | 预测答案与正确答案的匹配程度（越高越好） |
| 证据过滤质量 | 筛选证据与问题的相关性及合理性（越高越好） |
| 证据预算敏感性 | 证据数量变化对性能的影响程度（越低越好） |
| 效率 | 方法的计算资源消耗或处理速度（越高效率越好） |
⚔️ 基线方法对比
论文未报告对比的基线方法。
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）结构化证据规划与紧凑图引导检索可实现无需目标数据集微调或迭代检索的多模态问答性能；2）引入多模态图规划机制能有效减少冗余与无支持生成问题；3）HANIA无需目标数据集微调即可完成多模态接地问答，具备一定零样本泛化性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：HANIA是一种规划引导的多模态图证据选择框架，通过冻结VLM提取视觉证据、两组有限状态规划器协调证据及覆盖感知修剪，实现了无需目标数据集微调与迭代检索的高效多模态接地问答。

</details>

---

### 4. [SHAPE of Chain-of-Thought in Math Reasoning](https://arxiv.org/abs/2608.28600v1)

**Authors**: Jonghyun Song, Sangjun Song, Minjae Oh, Haesung Pyun, Sungsik Lee, Yohan Jo  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.28600v1  

#### Abstract
Large language models (LLMs) achieve strong performance on mathematical reasoning benchmarks, yet the mathematically meaningful skills underlying their reasoning remain underexplored. We introduce \texttt{SHAPE}, a framework that analyzes Chain-of-Thought (CoT) trajectories through two lenses develo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SHAPE of Chain-of-Thought in Math Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大语言模型（LLMs）在数学推理基准任务中表现出色，但支撑其推理的数学层面技能未被充分探索；针对Chain-of-Thought（CoT）的传统分析仅聚焦于表层特征，缺乏结合数学专业理论的深度解码，且对后训练是否真正提升数学能力的评估缺乏可靠依据。
现有方法的缺陷：
- 传统CoT分析方法：仅依赖CoT长度、token数量等表层特征，无法解释LLM数学推理的核心技能；
- 数学推理后训练：缺乏基于专业理论的评估手段，难以确认其对数学能力的真实增益。

🚀 提出的新方法与思路
**SHAPE框架**：基于数学教育领域的两个核心视角分析LLM的CoT轨迹：（1）语义空间，即模型对数学问题不断变化的解读（如代数、几何等）；（2）启发式，即模型在语义空间内采取的特定数学动作（如简化问题、倒推法等）。此外，该论文还提出通过促进数学启发式多样性的后训练策略，提升LLM的数学推理准确性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 理论基础 | 结合数学教育专业理论，而非传统CoT的表层特征，实现对LLM数学推理的深度解码 |
| 推理解释性 | 数学启发式相比传统CoT特征，更能有效解释最终答案的正确性 |
| 评估效能 | 可可靠评估后训练手段对LLM数学能力的真实提升效果 |
| 优化方向 | 提出促进启发式多样性的后训练策略，针对性提升数学推理准确性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为分析LLM的数学推理CoT轨迹，评估后训练对LLM数学能力的影响；
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
  1. LLM在数学推理中所使用的数学启发式，相比传统CoT特征，更能解释最终答案的正确性；
  2. LLM通过集中在少数语义空间内进行推理，而非探索多个不同空间，更易得到正确解决方案，该模式与人类数学推理行为一致；
  3. 强化学习会引发LLM在数学推理中对启发式使用的模式寻求（mode-seeking）；
  4. 促进启发式多样性的后训练策略，可有效提升LLM的数学推理准确性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出基于数学教育理论的SHAPE框架，深度解码LLM的数学推理CoT轨迹，揭示了LLM数学推理的核心规律，并通过促进数学启发式多样性的后训练策略，有效提升了LLM的数学推理能力。

</details>

---

### 5. [ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning](https://arxiv.org/abs/2608.28771v1)

**Authors**: Xin Jiang, Minhao Wang, Wen Wu, Zhentao Xie, Shangheng Du, Jinxin Shi, Jiabao Zhao  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.28771v1  

#### Abstract
Large reasoning models achieve strong performance on complex tasks by generating extended chain-of-thought (CoT) traces via reinforcement learning with verifiable rewards (RLVR). While current RLVR methods have achieved strong results with correctness-based reward signals, they provide limited guida...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于强化学习与可验证奖励（RLVR）的LLM推理方法，仅依赖正确性类奖励信号优化，对推理过程本身的质量提供的指导有限，导致内部推理结构未得到充分优化。

🚀 提出的新方法与思路
**Entropy Relief Reward (ERR)**：第一阶段训练所用奖励，奖励值与思考阶段内累积的token级熵降成比例，并按响应长度进行对数归一化，区别于过往抑制熵的方法，ERR奖励不确定性的缓解，同时不约束探索性的高熵状态。
**Robust Relative Efficiency Reward**：第二阶段训练所用奖励，通过双曲正切变换的组内z-score，将每个响应的长度与同组生成的对等响应进行评分。额外的形式分析指出，两个目标的联合优化会在训练早期产生梯度冲突，因此采用顺序式设计解决该问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理过程优化 | 以token级熵降为依据优化LLM内部推理结构，而非仅优化最终结果的正确性 |
| 训练机制 | 采用顺序式两阶段RLVR设计，解决联合优化带来的训练早期梯度冲突问题 |
| 响应质量 | 同时提升推理准确性与响应简洁性 |
| 奖励设计 | ERR奖励不确定性缓解而非抑制，保留推理过程的探索性高熵状态 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 5个未明确命名的基准数据集 | 验证ERR+方法在LLM推理任务上的性能表现 |

🎯 实验设置与评估指标
任务为LLM推理任务，评估推理结果的准确性与响应的简洁性。
| 指标 | 含义 | 方向 |
| ---- | ---- | ---- |
| 推理准确性 | 衡量推理结果的正确程度 | ↑ 越高越好 |
| 响应简洁性 | 衡量响应的长度 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有RLVR方法 | 主流LLM推理方法 | 仅采用正确性类奖励信号优化，未针对推理过程结构优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表格（含具体数值及表号），仅提及：在5个基准数据集上，跨模型骨干实现了推理准确性与响应简洁性的一致提升。
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 核心发现：正确的推理轨迹相较于错误的，在思考阶段表现出更频繁、幅度更大的token级熵降。
- 核心发现：ERR+的两阶段奖励设计可避免联合优化的梯度冲突，在优化推理过程的同时提升响应效率。
- 核心发现：ERR+方法对不同模型骨干均具有性能增益的通用性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ERR+是一种基于RLVR的顺序式两阶段LLM推理框架，通过奖励思考阶段的token级熵降缓解不确定性，同步实现推理准确性与响应简洁性的提升。

</details>

---

### 6. [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://arxiv.org/abs/2608.30252v1)

**Authors**: Tong Yuan, Chengxi Liao, Zeyi Wen  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.30252v1  

#### Abstract
Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency a major bottleneck. Speculative decoding (SD) reduces latency without changing model outputs, but its speedup depends on b...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点是长上下文LLM应用（如文档摘要、多轮代理）的解码延迟成为主要瓶颈，Speculative Decoding（SD）虽可降低延迟，但加速比受限于两类Draft的固有矛盾；现有不同方法的缺陷：
- 现有Lightweight Draft SD方法：draft延迟低，但无法捕捉长程依赖，加速效果受限；
- 现有Strong Independent Draft SD方法：提升了Draft Token接受率，但长前缀下Draft侧KV访问成本增长，抵消了部分收益。

🚀 提出的新方法与思路
**Memory-Augmented Drafting**，该方法为强独立Draft配备压缩的Draft-side KV内存：通过轻量级Adaptor构建并增量更新该内存，以保留Draft的远距离信息与精确最近上下文；目标Verifier保留完整KV缓存，沿用标准接受/拒绝规则，从而保留Speculative Decoding的lossless（无损）保证，无需改变目标模型的输出。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| Draft-side内存占用 | 减少超70% |
| 长前缀下KV访问成本 | 无显著增长 |
| SD保证性 | 保留标准SD的无损保证 |
| 解码加速比（vs自回归解码） | Llama 3.1-8B目标达2.08x，Llama 3.1-70B目标达3.33x |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
任务为长上下文LLM的解码加速，评估指标包含Draft-side内存减少比例、相对于自回归解码的解码加速比。
| 指标 | 含义 |
|------|------|
| Draft-side内存减少比例 | ↑ 越高越好 |
| 解码加速比（vs自回归解码） | ↑ 越高越好 |
针对文档摘要、多轮代理等长上下文LLM应用，测试各方法在32K前缀长度下的解码延迟与加速性能。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Autoregressive Decoding | 基线方法 | 无加速效果，解码延迟高 |
| Lightweight Draft SD | 基线方法 | draft延迟低，但无法捕捉长程依赖，加速有限 |
| Strong Independent Draft SD | 基线方法 | 提升Draft Token接受率，但长前缀下KV访问成本增长 |
| Memory-Augmented Drafting | 本文方法 | 配备压缩Draft-side KV内存，保留SD无损保证，兼具低内存与高加速 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告对应表号、图号，仅报告明确提及的实验结果：
- 场景1：Llama 3.1-8B目标模型，前缀长度达32K：Draft-side内存减少超70%，解码加速比达2.08x（vs自回归解码）；
- 场景2：Llama 3.1-70B目标模型，前缀长度达32K：Draft-side内存减少超70%，解码加速比达3.33x（vs自回归解码）；
💡 结论：该方法在长上下文场景下，可同时大幅降低Draft-side内存占用并提升解码加速比，且保留Speculative Decoding的无损保证。
其余实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. 现有Speculative Decoding方法的Draft存在“轻量则无法捕捉长程依赖，强则内存开销过大”的固有矛盾，限制了长上下文下的解码性能；2. 本文提出的Memory-Augmented Drafting方法有效解决该矛盾，在32K前缀下实现超70%的Draft-side内存减少，以及最高3.33x的解码加速比；3. 该方法保留了Speculative Decoding的无损保证，未改变目标模型的输出；
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的Memory-Augmented Drafting方法，通过为强独立Speculative Draft配备压缩的Draft-side KV内存，在保留SD无损保证的前提下，大幅降低了Draft-side内存占用并提升了长上下文下的解码加速比。

</details>

---

### 7. [CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework](https://arxiv.org/abs/2608.30498v1)

**Authors**: Qi Li, Zhaojie Kang, Yingjie He, Zheng Lin, Hao Zhang, Guangxin Wu, Yan Gong, Rong Fu, Jianyuan Ni  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.30498v1  

#### Abstract
Multimodal Large Language Models (MLLMs) have shown remarkable success in STEM domains, where progress is often driven by vertical, step-by-step deduction under relatively stable symbol systems. Their horizontal, interdisciplinary cultural reasoning, however, remains underexplored.We propose CM2, a ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework
1. 论文的主要贡献和创新点
✅ 解决的问题
Multimodal Large Language Models（MLLMs）在STEM领域表现出色，但在横向跨学科的文化推理方向的研究被低估，现有CoT、典型推理范式等方法在该任务上存在不足。

🚀 提出的新方法与思路
**CM2（Integrated Multi-Agent Framework）** ，该框架基于人类文化解释的认知路径构建，整合了multimodal perception、retrieval-augmented generation、networked reasoning、gated fusion与reward-driven feedback模块。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
多MLLM backbone文化推理性能 | 在CM2D数据集上相比CoT及典型推理范式取得一致提升
模块有效性验证 | 通过ablation实验确认各模块对框架的贡献
跨模态仲裁能力 | 通过冲突分析确认具备真实有效的跨模态仲裁能力

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
CM2D | 测试CM2框架的多模态文化推理性能

🎯 实验设置与评估指标
任务为在CM2D数据集上对多个MLLM backbone进行多模态文化推理任务，论文未报告具体评估指标细节。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
CoT | 推理范式 | 典型的推理方法
典型推理范式 | 基准对比方法 | 现有通用的推理框架

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能 | 论文未报告
2. 效率对比（FPS / 参数量） | 论文未报告
3. 跨域 / zero-shot迁移 | 论文未报告
4. 鲁棒性 / 扰动测试 | 论文未报告
5. 消融实验 | 论文未报告

4. 关键结论和发现
- 2-3条主要发现
  - CM2框架在CM2D数据集上，针对多个MLLM backbone的多模态文化推理性能，相比CoT及典型推理范式取得一致提升；
  - Ablation实验验证了CM2框架各模块对整体性能的贡献；
  - 冲突分析确认CM2框架具备真实有效的跨模态仲裁能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CM2是基于人类文化解释认知路径的多代理集成框架，可提升MLLMs在横向跨学科多模态文化推理任务（CM2D数据集）上的性能，其各模块贡献明确且具备有效的跨模态仲裁能力。

</details>

---

### 8. [Structure Aware Neural Architecture Search for Mixture of Experts](https://arxiv.org/abs/2608.29817v1)

**Authors**: Petr Babkin, Oleg Bakhteev  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.29817v1  

#### Abstract
Neural Architecture Search (NAS) has so far rarely been applied to Mixture-of-Experts (MoE) models, and existing MoE designs leave the alignment between experts and the structure of the data to emerge on its own. We propose an architecture search framework that makes this alignment an explicit searc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Structure Aware Neural Architecture Search for Mixture of Experts》
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有Neural Architecture Search (NAS) 方法：鲜有应用于 Mixture of Experts (MoE) 模型；
- 现有MoE模型设计：专家与数据结构的对齐是自发形成而非显式优化的，无法实现专家分配与架构的联合优化。
🚀 提出的新方法与思路
**Structure Aware NAS for MoE Framework**：将数据簇到专家的分配作为显式搜索变量，与每个专家的架构进行联合优化；将联合优化问题转化为簇感知的似然最大化，证明其等价于隐变量混合的不完全数据极大似然；采用广义 Expectation-Maximisation (EM) 流程求解问题，通过自适应优化的替代项处理原本难以计算的专家质量项；该方法还具备收敛性保证：当替代误差可求和时，迭代收敛，且每个极限点的候选均无法改进真实目标。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 专家-数据对齐 | 将数据簇到专家的分配作为显式搜索变量，而非依赖自发形成的对齐 |
| 联合优化 | 同时优化专家分配与 per-expert 架构，提升MoE整体适配性 |
| 收敛性保证 | 提供迭代收敛的数学证明，极限点无更优候选 |
| 性能表现 | 在无标签信息的任务上，优于同设置的MoE基线和NAS基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 异构图像分类混合数据集 | 验证无域标签设置下的性能 |
| 四域时间序列预测数据集 | 验证跨域任务性能 |
🎯 实验设置与评估指标
异构图像分类、四域时间序列预测两类任务均采用无标签信息的实验设置，指标的具体定义与评估方向未在论文中明确报告。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有MoE基线 | MoE类基线 | 无专家与数据结构显式对齐设计 |
| 现有NAS基线 | NAS类基线 | 未针对MoE模型优化架构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅摘要提及以下内容：在异构图像分类混合基准中，所提方法在未观察域标签的情况下，恢复了95%的潜在域分区；在异构图像分类和四域时间序列预测两个基准上，性能优于同无标签设置的MoE基线和NAS基线。
其余实验项（主benchmark性能的具体指标数值、效率对比、跨域/zero-shot迁移的详细结果、鲁棒性/扰动测试、消融实验）论文均未报告。

4. 关键结论和发现
- 主要发现：1）所提Structure Aware NAS方法无需域标签即可在异构图像分类任务中恢复95%的潜在域分区；2）在无标签的异构图像分类和四域时间序列预测任务中，该方法性能优于MoE与NAS基线；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；

> ✅ **总结一句话**：针对现有NAS鲜有应用于MoE模型、专家与数据结构对齐非显式优化的痛点，提出将数据簇到专家的分配与per-expert架构联合优化的Structure Aware NAS框架，在无标签任务上性能优于同设置基线方法。

</details>

---

### 9. [PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs](https://arxiv.org/abs/2608.30528v1)

**Authors**: Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang, Tianze Xu, Chao Ma, Jihuai Zhu, Jiashun Liu, Xinle Deng, Baohua Dong, Hangcheng Zhu, Ruohui Huang  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.30528v1  

#### Abstract
Reinforcement learning (RL) is used to improve the reasoning abilities of LLMs, while training data span heterogeneous tasks. However, most RL post-training pipelines rely on fixed or manually designed task mixtures, even though task usefulness changes as training progresses. Online curriculum metho...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs

1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于提升LLM推理能力的多任务RL后训练存在两大核心痛点：一是多数RL后训练流水线依赖固定或人工设计的任务混合，未考虑任务的有用性会随训练进程动态变化；二是在线课程方法常以更新幅度定义任务可学习性，忽略该更新是否转化为实际奖励增益，会导致rollout预算被不合理分配给有大但无效更新的任务。

🚀 提出的新方法与思路
**Progress-Augmented Advantage Curriculum (PAC)**：该方法结合两类任务级信号优化多任务RL的课程设计，其一为advantage衍生的可学习性，用于衡量单个任务能诱导的策略更新幅度；其二为近期奖励增益，用于判断该策略更新是否切实提升了任务性能。PAC采用贝叶斯汤普森采样控制器，在GRPO训练过程中动态分配各任务的rollout预算。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务信号设计 | 同时利用advantage衍生可学习性与近期奖励增益，避免无效rollout预算分配 |
| 训练适配性 | 采用在线课程机制，随训练进程动态调整任务混合，适配任务有用性的变化 |
| 性能表现 | 相比随机采样和仅基于advantage的课程基线，可提升多任务RL的样本效率与最终性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文仅提及在多级别推理、多领域推理两种设置下开展评估，未披露具体数据集信息 |

🎯 实验设置与评估指标
实验针对多级别推理、多领域推理两类任务设置开展，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 验证分数 | 对应任务的验证结果，↑ 越高越好 |
| 最终平均得分 | 所有任务的最终验证得分平均值，↑ 越高越好 |
| 所需rollout步数 | 达到可比验证分数所需的rollout数量，↓ 越少越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 随机采样 | 基准方法 | 随机分配rollout预算，无定制化课程设计 |
| 基于advantage的课程基线 | 对比方法 | 仅采用advantage信号设计在线课程的方法 |
| PAC | 提出方法 | 结合advantage信号与近期奖励增益，利用贝叶斯汤普森采样分配rollout的多任务RL课程方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
#### 多级别推理设置
论文未报告
#### 多领域推理设置
论文未报告

4. 关键结论和发现
- 主要发现：① 同时跟踪advantage信号与实际奖励增益的在线课程机制，可有效提升LLM多任务RL的样本效率与最终性能；② 在多级别、多领域推理两类任务中，PAC均优于随机采样和仅基于advantage的课程基线；③ 动态调整任务混合的在线课程，比固定任务混合更适配训练进程中任务有用性的变化。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PAC通过融合advantage衍生可学习性与近期奖励增益，结合贝叶斯汤普森采样优化rollout分配，有效提升了LLM多任务RL的样本效率与最终性能。

</details>

---

### 10. [PathBridger: Subgoal Bridges for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2608.29061v1)

**Authors**: Soohyun Choi, Seonvin Cho, Songnam Hong  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.29061v1  

#### Abstract
Offline goal-conditioned reinforcement learning (GCRL) aims to learn policies for reaching diverse goals entirely from fixed trajectory data. Long-horizon offline GCRL remains challenging because sparse goal-reaching signals must be propagated over many steps, while execution errors cannot be correc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PathBridger: Subgoal Bridges for Offline Goal-Conditioned Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
离线目标条件强化学习（GCRL）在长 horizon 任务中面临核心痛点：仅能从固定轨迹数据学习，需跨多步传播稀疏的目标到达信号，且执行错误无法通过额外环境交互纠正；现有基于子目标、选项、动作 chunk 的分层 GCRL 方法存在缺陷：所选子目标仅指定终点，中间状态空间路径隐式，子目标选择与低级别执行策略之间的接口问题未解决。

🚀 提出的新方法与思路
**PathBridger 分层离线 GCRL 框架**：该方法显式连接子目标选择与短 horizon 执行，核心逻辑是构造通往所选中间终点的状态空间桥，并通过逆动力学模型将该状态空间桥解码为短的可执行动作 chunk。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 状态路径建模 | 显式建模子目标间的状态空间桥 |
| 子目标执行衔接 | 显式连接子目标选择与短 horizon 动作执行 |
| 任务性能 | 在 OGBench 任务上取得强聚合性能，多目标 Cube 操作任务增益显著 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| OGBench | 用于验证 PathBridger 方法的性能 |

🎯 实验设置与评估指标
任务为离线目标条件强化学习的 OGBench 相关任务（含多目标 Cube 操作任务）；论文未报告具体的评估指标类型。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有分层 GCRL 方法 | 离线 GCRL 方法（基于子目标、选项或动作 chunk 的分层方法） | 子目标仅指定终点，中间状态空间路径隐式，子目标选择与执行端脱节 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果的表号、数值等定量细节，仅提及在评估的 OGBench 任务有强聚合性能，多目标 Cube 操作任务增益显著。
💡 结论：论文未报告具体实验结果的定量细节，仅表明 PathBridger 在 OGBench 及多目标 Cube 操作任务上性能良好。

4. 关键结论和发现
- 主要发现：1. PathBridger 可有效解决离线 GCRL 长 horizon 任务中子目标选择与执行端脱节的问题；2. PathBridger 在 OGBench 任务上具有强聚合性能，在多目标 Cube 操作任务上增益尤为明显。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：PathBridger 是一种离线目标条件强化学习的分层方法，通过显式构造子目标间的状态空间桥并结合逆动力学模型解码动作 chunk，解决了长 horizon 任务中子目标选择与执行端脱节的问题，在 OGBench 及多目标 Cube 操作任务上表现出色。

</details>

---

### 11. [Read the Room, Read the Image: Understanding Indirect Speech Acts in Multimodal Visual Contexts](https://arxiv.org/abs/2608.30270v1)

**Authors**: Jaehee Kim, Ji Hoon Chung, Seoyoon Park, Unsol Kim, Kyungwon Park, Ji Hak Kim, Yi-Jun Chen, Hansaem Kim  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2608.30270v1  

#### Abstract
Indirect speech acts (ISAs) require pragmatic reasoning over context, as directive intent can- not be inferred from surface form alone. Prior text-based studies and existing multimodal benchmarks largely overlook this requirement, focusing instead on explicitly encoded context or perceptual recognit...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Read the Room, Read the Image: Understanding Indirect Speech Acts in Multimodal Visual Contexts
1. 论文的主要贡献和创新点
✅ 解决的问题：间接言语行为（ISAs）需要结合语境的语用推理才能推断指令意图，现有文本相关研究及已有的多模态基准大多忽略该核心需求，仅关注明确编码的语境或感知识别，尤其在高语境语言（如韩语）的相关研究中该问题更突出。
🚀 提出的新方法与思路：**READI**，是用于评估ISAs理解的多模态基准；基于语用理论建模分级间接性；将任务形式化为视觉基础的语用问答（V-PQA）；支持英语和韩语的跨语言评估。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 核心痛点解决 | 填补了现有方法忽略ISAs所需语境语用推理的空白 |
| 跨语言支持 | 覆盖英语、韩语两种语言的ISAs评估 |
| 特性贴合度 | 基于语用理论建模分级间接性，适配ISAs的分级特性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| READI | 用于评估多模态模型的ISAs理解能力，支持英语、韩语跨语言评估 |
🎯 实验设置与评估指标
任务为视觉基础的语用问答（V-PQA），用于评估模型对ISAs的理解；论文未报告具体的评估指标及对应含义。
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：
  1. 现有SOTA多模态模型难以完成视觉基础的间接言语行为理解任务；
  2. 模型对间接言语行为的理解性能随间接性升高而下降；
  3. 现有多模态基准未充分关注ISAs所需的语境语用推理，亟需针对该需求的基准。
- 方法局限性：论文未报告
- 未来工作：需开发明确针对语境语用推理的多模态基准，以提升模型对ISAs的理解能力。

> ✅ **总结一句话**：该论文提出多模态基准READI，用于英语和韩语跨语言的视觉基础间接言语行为理解评估，发现现有SOTA多模态模型在该任务上表现困难且性能随间接性升高而下降，强调了针对语境语用推理的基准的必要性。

</details>

---

### 12. [RouteSparse: Input-Conditional Pattern Routing for Budgeted Long-Context Prefilling](https://arxiv.org/abs/2608.29058v1)

**Authors**: Chao Zhang, Yifan Ji, Ziyan Zhang, Kai Song, Fei Lin  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2608.29058v1  

#### Abstract
Dynamic sparse attention can reduce the quadratic cost of long-context prefilling without changing model weights. MInference assigns each attention head one pattern offline and estimates that pattern's sparse indices for every prompt. This design is efficient, but it assumes that a head's preferred ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

RouteSparse: Input-Conditional Pattern Routing for Budgeted Long-Context Prefilling
1. 论文的主要贡献和创新点
✅ 解决的问题
现有动态稀疏注意力方法（如MInference）为每个注意力头离线分配固定稀疏模式，假设其偏好模式和稀疏预算对所有输入都适用，导致长上下文prefilling时速度与精度的平衡不佳，要么速度提升明显但精度损失大，要么精度好但速度提升有限。
🚀 提出的新方法与思路
**输入条件化模式路由（Input-Conditional Pattern Routing）**：将每个注意力头和提示段路由至GPU高效稀疏模式库中的对应模式。
**低代价探针与延迟感知路由器（Low-Cost Probe & Latency-Aware Router）**：低代价探针估计模式的效用与不确定性，延迟感知路由器选择适配的模式和预算，不确定时回退至更密的掩码。
**约束风险最小化与误差证书（Constrained Risk Minimization & Error Certificate）**：将路由建模为约束风险最小化问题，从省略概率质量推导注意力输出的误差证书。
🔍 相比现有方法的优势
维度 | 优势
长上下文任务精度 | 相比固定per-head路由，RULER指标下降仅0.2点，精度损失大幅降低
prefill效率 | 取得6.5×稠密prefill速度，仅比固定per-head路由的7.3×速度略有下降，精度-速度trade-off更优

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
论文未报告具体数据集名称 | 评估方法在长上下文检索、问答、摘要、语言建模任务上的表现
🎯 实验设置与评估指标
实验任务为长上下文相关任务（检索、问答、摘要、语言建模），评估指标如下：
指标 | 含义（箭头）
RULER | 精度下降点数，↓越低越好
Prefill速度倍数（相对于稠密） | 与稠密prefill的速度倍数，↑越高越好
⚔️ 基线方法对比
方法 | 类型 | 特点
MInference | 动态稀疏注意力方法 | 为每个注意力头离线分配固定稀疏模式，假设其对所有输入适用
固定per-head路由 | 现有稀疏注意力路由方法 | 固定每个注意力头的路由选择，不随输入变化

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Llama 3.1-8B-Instruct长上下文任务性能对比（场景：128K-token提示）**
方法 | RULER下降点数 | Prefill速度倍数（×稠密）
RouteSparse | 0.2 ✅ | 6.5
固定per-head路由 | 1.6 | 7.3
💡 结论：RouteSparse在长上下文prefill任务中，实现了优于固定per-head路由的精度（精度损失仅0.2点，远低于固定方法的1.6点），同时保持接近的prefill速度，显著优化了精度与效率的平衡。
其余实验部分：
1. 主benchmark性能：如上表所示
2. 效率对比：如上表所示（prefill速度倍数）
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告具体数值表格，仅证实输入-条件化路由、硬件 profiling、选择性密掩码回退均对精度- latency trade-off有贡献

4. 关键结论和发现
- RouteSparse通过输入条件化的模式路由、选择性密掩码回退等设计，在长上下文prefilling任务中实现了更优的精度与效率平衡，相比固定per-head路由的精度损失大幅降低，速度损失较小。
- 输入条件化路由、硬件 profiling、选择性密掩码回退是该方法取得性能增益的关键组件。
- 方法适用于长上下文检索、问答、摘要、语言建模任务。
方法局限性：论文未报告
未来工作：论文未明确提及

> ✅ **总结一句话**：RouteSparse为注意力头和提示段输入条件化适配GPU高效稀疏模式，结合低代价探针、延迟感知路由及约束风险最小化，在长上下文prefilling任务中实现了更优的精度与效率平衡。

</details>

---

### 13. [Efficient Geothermal Well-Control Optimization via Diffusion-Surrogate Reinforcement Learning](https://arxiv.org/abs/2608.28791v1)

**Authors**: Ruimin Dai, Guodong Chen, Randy Harsuko, Kunpeng Liu, Nori Nakata  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.28791v1  

#### Abstract
Real-time decision-making for enhanced geothermal systems (EGS) is challenging because long-term production periods involve high-dimensional control spaces and a large number of time-consuming high-fidelity hydrothermal simulations. Reinforcement learning provides a natural framework for state-depen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Efficient Geothermal Well-Control Optimization via Diffusion-Surrogate Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：增强型地热系统（EGS）的实时决策因长期生产涉及高维控制空间与大量耗时的高保真热液模拟，直接采用数值模拟器进行策略训练的强化学习方法计算成本过高。
🚀 提出的新方法与思路
**扩散代理环境构建**：利用条件扩散模型学习构建代理环境，用于预测储层温度和压力场的演化；同时训练单独的奖励模型，估计对应的经济回报；将该代理环境与Proximal Policy Optimization（PPO）结合，用于高效的策略训练。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 计算成本 | 大幅减少对耗时的高保真热液模拟的依赖，降低训练计算成本 |
| 控制性能 | 与直接基于模拟器的PPO、现有EGS井筒控制优化方法相比，控制表现具有竞争力 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| fractured EGS benchmark | 用于EGS井筒控制优化的性能实验 |
🎯 实验设置与评估指标
任务：增强型地热系统的长期井筒控制优化。评估指标：论文未报告
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 直接模拟器-based PPO | 现有强化学习方法 | 直接利用数值模拟器训练PPO策略 |
| 现有优化方法 | 现有井筒控制优化方法 | EGS井筒控制领域的现有优化方案 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
4. 关键结论和发现
- 主要发现：
  1. 基于条件扩散模型构建的储层状态预测扩散代理可有效生成代理环境，支持高效的强化学习策略训练；
  2. 提出的扩散代理引导强化学习框架，在EGS井筒控制中与现有方法相比，控制性能具有竞争力，同时大幅降低了对高保真模拟的依赖；
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：该论文提出了一种扩散代理引导的强化学习框架，用于解决增强型地热系统井筒控制优化中计算成本过高的问题，可减少对耗时的高保真热液模拟的依赖，同时保持良好的控制性能。

</details>

---

### 14. [More Perspectives, Stronger Signals: Multi-Perspective Enhancement and Progressive Fusion for Multimodal Entity Representation Learning](https://arxiv.org/abs/2608.29139v1)

**Authors**: Chenyi Xiong, Yan Zhang, Jing Hu, Ziyue Qin, Kui Xiao, Xiaopan Lyu, Xiaoju Hou, Zhifei Li  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.29139v1  

#### Abstract
Learning effective multimodal entity representations is fundamental for reasoning tasks such as multimodal knowledge graph completion (MMKGC). However, existing methods often suffer from semantic over-smoothing within modalities and ineffective noise filtration across modalities, particularly under ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# More Perspectives, Stronger Signals: Multi-Perspective Enhancement and Progressive Fusion for Multimodal Entity Representation Learning

## 1. 论文的主要贡献和创新点
✅ 解决的问题：现有多模态实体表示学习方法存在模态内语义过平滑的缺陷，且跨模态噪声过滤效果不佳，该问题在稀疏或歧义输入条件下尤为凸显，制约了多模态知识图谱补全（MMKGC）等推理任务的效果。

🚀 提出的新方法与思路
**多视角增强机制（Multi-Perspective Mechanism）**：将每个模态分解为互补的视角，通过解耦损失（decoupling loss）约束视角，缓解表示坍塌问题，从而增强细粒度的模态内语义。
**渐进式融合策略（Progressive Fusion Strategy）**：动态校准模态间的交互，使模型能够重点关注有价值的信号，同时抑制噪声或不可靠信号，提升跨模态整合效果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 语义表示质量 | 缓解模态内语义过平滑问题，减少表示坍塌 |
| 跨模态整合能力 | 动态校准模态间交互，有效过滤噪声信号 |
| 下游任务性能 | 在多模态知识图谱补全任务及多个公共基准上取得最优整体性能 |

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| KVC16K | 多模态实体表示学习及多模态知识图谱补全的基准测试 |
| 3个公共基准 | 模型性能的综合对比测试 |

🎯 实验设置与评估指标
任务为多模态实体表示学习，用于多模态知识图谱补全（MMKGC），采用的评估指标包括MRR（Mean Reciprocal Rank）、Hits@1，两类指标越高表示性能越好。

⚔️ 基线方法对比：论文未报告

## 3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（KVC16K）：论文未报告
💡 结论：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

## 4. 关键结论和发现
- 主要发现：1. 提出的PrismF框架通过多视角增强机制与渐进式融合策略，有效解决了现有多模态实体表示学习方法的核心痛点；2. PrismF在3个公共基准上均取得了最强的整体性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：本文提出的PrismF框架通过多视角增强与渐进式融合策略，缓解了多模态实体表示学习中的模态内语义过平滑、跨模态噪声过滤不足的问题，在多模态知识图谱补全任务及多个公共基准上实现了最优整体性能。

</details>

---

### 15. [Toward Latent Language Model Skills Steering and Optimization: An Empirical Study](https://arxiv.org/abs/2608.29459v1)

**Authors**: Xunyi Jiang, Junda Wu, Yuxin Xiong, Sheldon Yu, Tong Yu, David Arbour, Ritwik Sinha, Julian McAuley, Hongyi Wen  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.29459v1  

#### Abstract
Skills, as a useful abstraction for the procedural capabilities of large language models (LLMs), capture how models perform structured, multi-step reasoning and program execution. Existing approaches typically treat skills as explicit, surface-level constructs specified through prompts or programs, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Toward Latent Language Model Skills Steering and Optimization: An Empirical Study
1. 论文的主要贡献和创新点
解决的问题
现有方法通常将大语言模型（LLM）的程序型技能视为通过提示或程序指定的显式表层结构，未探究此类程序能力在模型内部的表征方式，以及能否在隐空间中作为结构化对象被操纵。

🚀 提出的新方法与思路
**Procedural Skill Vector Representation**：本研究通过实证探究程序型LLM技能是否可表征为激活空间中的方向，以及上述方向上的向量空间运算能否表达技能级行为；同时研究技能方向的组合性、对比方向的个性化能力，以及优化轨迹的非单调性等特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 技能表征方式 | 支持在隐空间中对程序型LLM技能进行结构化操纵，突破仅依赖显式提示或程序指定的局限 |
| 技能表达能力 | 可通过向量空间运算实现技能级行为的灵活表达，包括独立技能方向组合为高阶技能、对比方向实现情境条件化个性化 |
| 优化特性挖掘 | 揭示技能方向优化轨迹的非单调特性，可利用中间状态获得超越完全优化解的效果 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未明确报告具体使用的数据集 |

🎯 实验设置与评估指标
任务：探究程序型LLM技能的激活空间向量表征及向量操作对模型行为的影响
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未明确报告具体评估指标 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未明确列出对比的基线方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未在论文中报告具体定量数值、对应图表/章节信息，故相关内容为：
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：①程序型LLM技能可表征为激活空间中的方向，激活单个技能方向可改变模型行为；②独立提取的技能方向可组合成更高阶技能；③对比方向可实现情境条件化的算法个性化；④技能方向的优化轨迹非单调，中间状态常优于完全优化的解决方案。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本实证研究揭示了程序型LLM技能在激活空间的向量组织特性，证明可通过向量空间的相关操作实现技能级行为的直接操纵与个性化优化，为LLM技能的隐空间干预提供了经验支撑。

</details>

---

### 16. [AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning](https://arxiv.org/abs/2608.29988v1)

**Authors**: Hanjun Luo, Qiushi Liu, Jingya Zhang, Haihong Pang, Jiaheng Wen, Yifei Ma, Yu Yao, Chengxi Zhang, Hanrong Zhang, Yankai Chen, Hanan Salam  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.29988v1  

#### Abstract
Large language models (LLMs) achieve strong reasoning performance, which depends critically on inference-time decisions. Yet these decisions are commonly handled by static, one-size-fits-all policies, limiting adaptation to diverse tasks and reasoning stages. Recent adaptive methods partially addres...

---

### 17. [Mitigating Over-Optimization in PRM-Guided Search in Mathematical Reasoning by Optimizing the Guide](https://arxiv.org/abs/2608.30051v1)

**Authors**: Taejong Joo, Diego Klabjan  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.30051v1  

#### Abstract
Process reward models (PRMs) provide dense step-level guidance for search-based reasoning, enabling inference-time compute to be allocated toward promising partial solutions. However, recent evidence suggests that PRM-guided search can over-optimize imperfect process rewards, pruning viable trajecto...

---

### 18. [GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns](https://arxiv.org/abs/2608.30550v1)

**Authors**: Yinwen Lu, Weihao Luo, Yueqi Zhong  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.30550v1  

#### Abstract
Multimodal Sewing pattern generation aims to infer executable sewing patterns from design cues such as sketches and textual descriptions. As an interpretable and simulation-compatible representation, sewing patterns are particularly valuable for digital garment creation. However, existing methods of...

---

### 19. [ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding](https://arxiv.org/abs/2608.29748v1)

**Authors**: Luxi Lin, Zhanpeng Zeng, Shuang Peng, Songwei Liu, Rongrong Ji  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.29748v1  

#### Abstract
Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model. However, after the first rejection, standard prefix-based verification discards the remaining ...

---

### 20. [Where Identity Lives: Localized, Retain-Free Identity Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2608.30649v1)

**Authors**: Kangwook Ko, Jaehyuk Jang, Wonjun Lee, Hee-Seon Kim, Changick Kim  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.30649v1  

#### Abstract
Removing a specific individual's information from multimodal large language models (MLLMs) is often needed after deployment, but existing methods rely on a retain set, which is hardest to obtain at that point, and rebuilding it recreates the privacy exposure that unlearning aims to remove. Forgettin...

---

### 21. [COGTRL: Training LLMs for Scientific Discovery Assistance using Cognitive Traces via Reinforcement Learning](https://arxiv.org/abs/2608.30109v1)

**Authors**: Shrinidhi Kumbhar Santosh Mashetty Divij Handa Kevin Coutinho, Siddharth Sambhaji Ghule, Chitta Baral  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.30109v1  

#### Abstract
Large Language Models (LLMs) trained on extensive scientific research are increasingly integrated as assistants for scientific discovery. However, most research papers omit the fine-grained cognitive process of examining constraints, failed alternatives, and iterative decisions required to achieve t...

---

### 22. [LLMs Interpret, Embeddings Organize, Graphs Emerge: Agent-Driven Compilation of Scientific Knowledge](https://arxiv.org/abs/2608.29612v1)

**Authors**: Shi-Ju Ran, Kun Zhang, Xi Wu, Liu-Si Yang, Wen-Jun Li  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.29612v1  

#### Abstract
Sustained scientific work requires a knowledge substrate that carries interpretation across tasks and preserves paths to source evidence. We call this process \emph{scientific knowledge compilation} and implement it in ASKS, the \emph{Agent-Driven Scientific Knowledge System}. For each source, an LL...

---

### 23. [ScienceArena: Benchmarking LLMs on Latest Scientific Olympiad Competitions](https://arxiv.org/abs/2608.30517v1)

**Authors**: Guangxiang Zhao, Qilong Shi, Xusen Xiao, Wenpu Liu, Yaoming Li, Linfeng Hao, Shuyang Hou, Zijian Guo, Xinrui Zhang, Yuntian Zhao, Zhengyang Wang, Wenrui Liu, Yuhan Wu, Tong Yang, Lin Sun, Xiangzheng Zhang  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.30517v1  

#### Abstract
Benchmark saturation and data contamination increasingly obscure genuine scientific reasoning in frontier LLMs. We introduce \textsc{ScienceArena}, an olympiad-style benchmark from thirteen public science competitions in physics, chemistry, and biology, including IPhO and IChO 2025--2026, IBO 2023, ...

---

### 24. [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897v1)

**Authors**: Jiaqi Su, Cong Pang, Jiawei Hong, Tiankuo Yao, Zixuan Chen, Xin Lou, Lewei Lu  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.29897v1  

#### Abstract
Long-horizon agents need a context manager to compress growing interaction histories into a bounded working context, via passive strategies or active strategies that decide how memory is accessed and reorganized. Meanwhile, prior optical-memory work mainly treats pixels as a dense codec for textuali...

---

### 25. [RL-FAT: Reinforcement Learning for Fair Adversarial Training](https://arxiv.org/abs/2608.29247v1)

**Authors**: Tejaswini Medi, Levan Mikeladze, Margret Keuper  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.29247v1  

#### Abstract
Deep neural networks remain highly vulnerable to adversarial perturbations, and adversarial training (AT) has become a widely used approach for improving robustness. However, improvements in average robust accuracy often mask substantial class-wise disparities: while some classes become more robust,...

---

### 26. [Selection, Representation, and Execution in Sparse Fourier Neural Operators](https://arxiv.org/abs/2608.30070v1)

**Authors**: Abdul Qadir Ibrahim, Martin Burger  
**Category**: cs.LG  
**Published**: 2026-09-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.30070v1  

#### Abstract
Sparse representations are often expected to make models smaller and also reduce inference cost. For Fourier Neural Operators (FNOs), these objectives are not equivalent or do not always align: removing parts of the learned operator can leave the underlying transforms and dense computations unchange...

---

### 27. [RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs](https://arxiv.org/abs/2608.29263v1)

**Authors**: Yuwei Lou, Hao Hu, Yuzhou Jiang, Zongfei Zhang, Liang Wang, Jincai Liu, Jidong Ge, Xianping Tao  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.29263v1  

#### Abstract
Large Language Models (LLMs) often suffer from hallucination and struggle with complex reasoning tasks requiring multi-hop domain knowledge. While integrating Knowledge Graphs (KGs) provides a structured and verifiable information source, current KG-enhanced LLM paradigms usually rely on single-agen...

---

### 28. [Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework for Open-World Geo-Localization](https://arxiv.org/abs/2608.29880v1)

**Authors**: Yutian Jiang, Ruijie Li, Sisuo Lyu, Xixuan Hao, Qingxiang Liu, Yongzi Yu, Yuxuan Liang  
**Category**: cs.AI  
**Published**: 2026-09-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.29880v1  

#### Abstract
Open-world geo-localization requires models to reason over ambiguous visual cues through multi-step reasoning and external knowledge grounding. While recent large vision-language models exhibit strong multimodal reasoning capabilities, existing approaches still suffer from perceptual hallucination a...

---

### 29. [Modality Fault Lines: Structural Corruptions Reveal Fragile Omni-Modal Reasoning](https://arxiv.org/abs/2608.29278v1)

**Authors**: Zhaolu Kang, Meixin Wu, Yu Xue, Yingjie He, Qiming Shi, Lei Wei, Yidi Wang, Richeng Xuan, Zhichao Hu  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.29278v1  

#### Abstract
Omni-modal large language models are increasingly evaluated on clean text--vision--audio inputs, where every channel is present, synchronized, and readily interpretable. Such scores are often taken as evidence of robust cross-modal fusion, but clean evaluation cannot tell whether success depends on ...

---

### 30. [EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning](https://arxiv.org/abs/2608.29835v1)

**Authors**: Peilin Liu, Zhiquan Ji, Jinglong Ping  
**Category**: cs.CL  
**Published**: 2026-09-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.29835v1  

#### Abstract
Large language models (LLMs) often produce fluent but weakly grounded conclusions when reasoning over non-interactive, long-form narratives. A central failure mode is that unsupported intermediate hypotheses can enter the reasoning trajectory and contaminate subsequent inference, especially when evi...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization, Embodied, Embodied AI, Embodied Intelligence, Robotics, Robot, Manipulation, Navigation, Sim-to-real, Simulation, World Model, World Models, Video Generation, Video Prediction, Multimodal, Multi-modal, Vision-Language, Vision Language, VLM, Image-Text, Cross-modal, Cross modal, Text-to-Image, Text-to-Video, Vision Transformer, Visual Understanding

## 📅 Schedule

The bot runs on weekdays at 05:40 UTC via GitHub Actions to fetch the latest papers.

## 🚀 How to Use

1. **Fork this repository** to your GitHub account
2. **Customize the configuration** by editing `config.json`:
   - Add/remove arXiv categories (e.g., `cs.AI`, `cs.LG`, `cs.CL`)
   - Modify keywords to match your research interests
   - Adjust `max_papers` and `days_back` settings
3. **Enable GitHub Actions** in your repository settings
4. **The bot will automatically run on weekdays** and update the README.md

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
