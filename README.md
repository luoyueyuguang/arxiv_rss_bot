# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-24 08:13:00 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization](https://arxiv.org/abs/2607.21013v1)

**Authors**: Lihuang Fang, Yuchen Zou, kebin Jin, Jinghui Qin  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 85.5  
**Type**: new  
**ArXiv ID**: 2607.21013v1  

#### Abstract
Multimodal large language models (MLLMs) have achieved impressive performance in multimodal emotion recognition (MER) tasks and lifted MER to a new level that is complex emotion understanding with advanced video understanding abilities and natural language description. However, existing MLLM-based m...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization
1. 论文的主要贡献和创新点
✅ 解决的问题：现有基于多模态大语言模型（MLLM）的多模态情绪识别（MER）方法，常使用固定prompt感知情绪，忽略多模态输入中情绪源的动态性与复杂性，导致情绪理解不足。
🚀 提出的新方法与思路
**Reinforcement Learning-based Dynamic Agent Specialization框架（EmoAgent-R1）**：分为两个阶段构建与优化：第一阶段采用冷启动策略，通过合成的答案条件化思维链数据与智能体路由数据训练，赋予MLLM初步的情绪识别、推理及智能体路由能力；第二阶段进一步通过强化学习训练，采用智能体选择与智能体专业化的两步智能体工作流优化模型性能；同时提出**Progressive Group-Relative Policy Optimization（P-GRPO）**方法，将基于组的相对优势与PMI启发的渐进式token级调制结合，把稀疏奖励转化为细粒度学习信号，缓解GRPO存在的粗粒度均匀信用分配问题。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 情绪推理性能 | 更强 |
| 优化稳定性 | 提升 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MER benchmarks | 论文未报告具体数据集名称，用于验证模型在多模态情绪识别任务上的性能 |
🎯 实验设置与评估指标
任务为多模态情绪识别（MER）任务，实验设置细节论文未报告；评估指标细节论文未报告，仅指出模型在情绪推理性能与优化稳定性上有提升。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |
3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验结果相关细节（包括表号、图号、具体指标数值等）论文未报告，仅概括性指出模型在MER基准上表现更优。
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：所提出的EmoAgent-R1模型在多模态情绪识别任务中，相比现有MLLM-based MER方法具备更强的情绪推理性能，且优化稳定性有所提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本文提出了基于强化学习的动态智能体专业化框架EmoAgent-R1，通过冷启动策略与改进的Progressive Group-Relative Policy Optimization方法优化MLLM的多模态情绪理解能力，在多模态情绪识别任务中实现了更优的情绪推理性能与更高的优化稳定性。

</details>

---

### 2. [MIRROR: Learning from the Other View for Multi-Modal Reasoning](https://arxiv.org/abs/2607.21552v1)

**Authors**: Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 68.5  
**Type**: new  
**ArXiv ID**: 2607.21552v1  

#### Abstract
Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a m...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《MIRROR: Learning from the Other View for Multi-Modal Reasoning》
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：视觉语言模型（VLMs）在视觉推理（尤其是几何问题）上弱于大语言模型（LLMs），且同一问题的文本、图像、图文混合视图会引发模型表现不一致（如模型可解决文本视图但失败于图像视图，反之亦然），现有多模态后训练未充分挖掘不同视图的互补推理路径与失效模式。

🚀 提出的新方法与思路
**Modality-Informed Reciprocal Reasoning Optimization（MIRROR）**：一种用于多模态推理的自监督强化学习方法，具体流程为：针对每个问题，评估模型在所有视图（文本主导、图像主导、图文混合）下的表现，选取表现最优的视图作为教师，采用反向KL（reverse-KL）目标训练其他视图向该教师学习。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态表现一致性 | 提升不同视图间的推理行为一致性 |
| 几何推理性能 | 在几何推理基准上相比标准RL方法性能更优 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ODA-Data | 研究与利用多模态几何问题的视图互补性，包含同一几何问题的文本主导、图像主导、图文混合视图，划分有训练和评估子集 |

🎯 实验设置与评估指标
任务：多模态几何推理任务
论文未报告具体评估指标名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准RL | 基线方法 | 传统多模态后训练采用的强化学习方法 |
| MIRROR | 提出的方法 | 基于自监督的多视图 reciprocal reasoning 优化方法，通过最优视图教师指导其他视图训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量数值及对应表号，仅提及MIRROR在几何推理基准上相比标准RL性能更优，且不同模态间行为一致性更好。
💡 结论：提出的MIRROR方法在多模态几何推理任务上优于标准RL方法，且提升了不同视图间的推理一致性。

4. 关键结论和发现
- 主要发现：1. 同一几何问题的不同视图会导致模型出现差异表现，存在互补性与失效模式，现有多模态后训练未充分利用该特性；2. MIRROR通过选择最优视图作为教师的训练方式，可有效提升多模态几何推理性能与模态间表现一致性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：提出的MIRROR方法针对多模态几何推理中不同视图表现不一致的痛点，采用自监督强化学习策略利用最优视图指导其他视图，提升了几何推理性能与模态间表现一致性。

</details>

---

### 3. [Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs](https://arxiv.org/abs/2607.20517v1)

**Authors**: Takato Yasuno  
**Category**: cs.LG  
**Published**: 2026-07-24  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2607.20517v1  

#### Abstract
Retrieval-augmented generation (RAG) over heterogeneous PDF collections remains challenging due to multimodal content, domain-specific terminology, and the need for multi-hop reasoning across dispersed evidence. We present Multimodal CoLRAG-TF, a four-axis fusion architecture that integrates dense t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs
1. 论文的主要贡献和创新点
✅ 解决的问题
解决异质PDF集合上检索增强生成（RAG）的难题：此类PDF存在多模态内容、特定领域术语，且需要跨分散证据的多跳推理。
🚀 提出的新方法与思路
**Multimodal CoLRAG-TF**：四轴融合架构，包含四个核心模块：
1. **Dense Text Embeddings**：融合密集文本嵌入；
2. **BM25 Keyword Matching**：融合BM25关键词匹配；
3. **Knowledge-Graph Triple Filtering**：融合知识图谱三元组过滤，从灾难课程PDF中提取11414个OpenIE三元组，用FAISS索引，支持亚秒级三元组查找与相关性信号的分层传播；
4. **Image-Based Similarity**：融合基于图像的相似度。
此外，采用受HippoRAG2启发的粗到细检索器（层级为volume→chapter→block）缩小搜索空间，经贝叶斯优化确定融合权重，其中三元组轴占主导（$\alpha_\text{triple} = 0.44$）以抵消词汇偏差、维持多跳检索质量。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态融合 | 整合密集文本嵌入、关键词匹配、知识图谱三元组过滤、图像相似度四类维度，覆盖复杂PDF的多元内容 |
| 多跳推理 | 通过粗到细检索与三元组过滤的融合，支持跨分散证据的多跳检索 |
| 词汇偏差抵消 | 三元组轴占主导的融合权重设计，抵消词汇偏差 |
| 适用性 | 框架可推广至灾难领域外的复杂PDF场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 43份日本灾难课程PDF | 构建包含2403个块的多模态索引，用于方法的开发与验证 |
| 457对基准数据 | 用于方法的检索性能评估 |
🎯 实验设置与评估指标
任务：复杂PDF的多模态检索与多跳推理
| 指标 | 含义（箭头标方向） |
| --- | --- |
| Retrieval Recall | 检索召回率，越高越好（↑） |
| 多跳答案相似度 | 衡量多跳检索结果与正确答案的匹配度，越高越好（↑） |
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未明确给出对应表号、图号等定位信息，故按要求表述如下：
**主 benchmark 性能**
论文未报告
**效率对比**
论文未报告
**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告

4. 关键结论和发现
- 主要发现：① 三元组过滤的多模态融合是复杂PDF结构化推理的关键，可抵消词汇偏差并维持多跳检索质量；② 受HippoRAG2启发的粗到细检索（volume→chapter→block）能有效缩小搜索空间；③ 融合权重中三元组轴占主导（$\alpha_\text{triple}=0.44$）对优化检索性能至关重要。
- 方法局限性：论文未报告
- 未来工作：该框架可推广至灾难领域外的复杂PDF场景。

> ✅ **总结一句话**：Multimodal CoLRAG-TF提出四轴融合架构，结合粗到细检索与知识图谱三元组过滤，有效解决复杂PDF的多模态内容处理与多跳推理问题，且具备跨领域推广潜力。

</details>

---

### 4. [REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2607.20833v1)

**Authors**: Zhensheng Jin, Xin Dai, Zhenghao Liu, Chaojun Xiao, Huiyuan Xie, Yu Gu, Ge Yu, Maosong Sun  
**Category**: cs.CL  
**Published**: 2026-07-24  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2607.20833v1  

#### Abstract
Large language models increasingly rely on long-form reasoning for complex tasks, yet their reasoning traces may drift away from the supplied context when evidence is sparse, noisy, or in conflict with parametric knowledge. Existing grounding methods either attach citations after generation or encou...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型在复杂任务中依赖长形式推理，但当证据稀疏、噪点多或与参数知识冲突时，其推理轨迹可能偏离提供的上下文；现有的接地方法要么在生成后附加引用，要么鼓励在推理轨迹内检索证据，但通常无法确保引用内容对局部推理和最终答案充分。

🚀 提出的新方法与思路
**REFACT Adaptive Fact Restatement Framework**：该框架训练模型自主判断推理步骤是否需要上下文接地，并决定源事实应重述的粒度，将引用转化为支持答案的中间状态，避免无支持推理与无差别事实复制。
**Two-Stage SFT-to-RL Pipeline**：采用该优化流程，其中citation-utility奖励函数鼓励生成的引用具备格式良好、可溯源、答案充分的特性，提升引用质量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理支撑性 | 确保引用内容对局部推理及最终答案充分 |
| 推理轨迹合规性 | 避免无支持推理与无差别事实复制 |
| Token效率 | 大幅减少推理的Token消耗 |
| 推理质量 | 保留更多答案承载证据，生成更密集而非更长的推理轨迹 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongBench | 长上下文问答测试 |
| LV-Eval | 长上下文问答测试 |
| ConFiQA | 反事实忠实度测试 |

🎯 实验设置与评估指标
任务为长上下文问答与反事实相关推理，指标包括长上下文问答性能（↑ 越高越好）、反事实忠实度（↑ 越高越好）、Token消耗（↓ 越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 生成后附加引用的方法 | 后处理接地方法 | 生成完成后附加引用，但无法确保引用内容的支撑性 |
| 推理内部证据检索的方法 | 内部推理接地方法 | 在推理轨迹内检索证据，但同样无法保证引用内容对局部推理和答案充分 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：论文通过定性描述指出，REFACT在LongBench、LV-Eval、ConFiQA三个数据集上提升了长上下文问答与反事实忠实度，同时大幅降低了Token消耗。

4. 关键结论和发现
- 主要发现：1. REFACT可有效提升长上下文问答性能与反事实忠实度；2. REFACT能显著降低推理过程的Token消耗；3. REFACT以更少的重述事实保留了更多答案承载证据，生成更密集而非冗长的推理轨迹。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：REFACT通过自适应事实重述框架与两阶段优化流程，在提升长链式推理的忠实度与答案支撑性的同时，降低了推理的Token消耗。

</details>

---

### 5. [Domyn-Small: A European 10B Reasoning Language Model](https://arxiv.org/abs/2607.20448v1)

**Authors**: Simone Angarano, Francesco Bertolotti, Federico D'Ambrosio, Michele Resta, Alessandro Rognoni, Nicol\`o Ruggeri, Dario Salvati, Andrea Valenti, Alberto Veneri, Martin Cimmino  
**Category**: cs.CL  
**Published**: 2026-07-24  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2607.20448v1  

#### Abstract
We introduce Domyn-Small, a 10-billion-parameter open-weight reasoning language model released under the MIT license. Domyn-Small is the product of an initial pre-training phase on 9 trillion tokens multilingual data, followed by a post-training pipeline for reasoning, instruction following, and con...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Domyn-Small: A European 10B Reasoning Language Model
1. 论文的主要贡献和创新点
✅解决的问题
1. 现有7-10B级别的开放权重推理语言模型存在性能与效率（如token预算）平衡不足的痛点：部分模型核心推理任务的token预算过高，部分模型效率或性能表现不佳，其余同级别模型也存在类似的平衡缺陷；
2. 缺少一款该规模下兼具高性能、高效性、开放许可及扩展上下文能力的推理语言模型。

🚀提出的新方法与思路
**预训练阶段**：采用9万亿token的多语言数据进行初始预训练，构建模型基础能力。
**Continued Pre-Training (CPT)**：将模型原生上下文窗口翻倍至32K，扩展模型的上下文处理能力。
**SFT with math-focused annealing run**：在CPT后开展聚焦数学领域的退火运行监督微调，强化模型的推理专项能力。
**RL phase with GRPO+DPO+multi-environment GRPO**：采用强化学习阶段，包含带可验证奖励的GRPO、偏好优化（DPO），以及覆盖数学、代码、多选QA、指令跟随、工具调用5个任务域的多环境GRPO，全面提升模型的综合推理与任务适配能力。
**YaRN context extension**：通过YaRN技术，将模型推理时的上下文窗口从原生32K扩展至128K，进一步增强长文本处理适配性。
**Chat-template toggle for dual-mode reasoning**：提供聊天模板切换功能，支持双模式推理，适配不同使用场景。

🔍相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 模型属性 | 100亿参数开放权重推理语言模型，采用MIT许可，可自由使用 |
| 精度-效率平衡 | 在7-10B级同级别推理模型中，核心推理基准的token预算显著更低 |
| 指令跟随能力 | 具备较强的指令跟随性能 |
| 科学推理能力 | 拥有有竞争力的科学推理表现 |
| 上下文窗口 | 原生支持32K tokens上下文，推理时可通过YaRN扩展至128K tokens |
| 开源生态 | 发布模型权重与后训练配方，附带Domyn Swarm（Apache2.0许可）开源框架，支持HPC集群上的可扩展LLM推理 |

2. 核心实验方法和设置
📚使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 9万亿token多语言数据 | 初始预训练阶段使用 |
论文未报告其余训练阶段所用的具体数据集。

🎯实验设置与评估指标
任务：评估推理、指令跟随、上下文扩展等语言模型核心能力。
| 指标 | 含义（箭头） |
| ---- | ---- |
| 核心推理基准的token预算 | ↓ 越低越好 |
| IFEval | ↑ 越高越好 |
| GPQA-Diamond | ↑ 越高越好 |
论文未报告具体评估的任务细节。

⚔️基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Qwen3.5-9B | 推理语言模型 | 7-10B级开放权重推理模型，同级别对比基线 |
| OLMo-3-7B-Think | 推理语言模型 | 7-10B级开放权重推理模型，同级别对比基线 |
| Nemotron-Nano-8B | 推理语言模型 | 7-10B级开放权重推理模型，同级别对比基线 |
| Ministral-3-8B | 推理语言模型 | 7-10B级开放权重推理模型，同级别对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何带有表号、图号、章节或页码来源的定量实验结果，仅在摘要中提及未明确来源的对比结论，按照要求，无法定位来源的定量结果不纳入统计，故：论文未报告

4. 关键结论和发现
- 主要发现：1. Domyn-Small是一款100亿参数的开放权重推理语言模型，经过多阶段训练流程后，在7-10B级同级别推理模型中实现了出色的精度-效率平衡；2. Domyn-Small具备较强的指令跟随与科学推理能力；3. 通过CPT、YaRN技术实现了上下文窗口的有效扩展，支持双模式推理，适配不同应用场景。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：Domyn-Small是一款基于多语言数据预训练+多阶段后训练的10B级开放权重推理语言模型，在同级别模型中实现了优异的精度-效率平衡，支持扩展上下文窗口与双模式推理，并附带相关开源资源，可满足HPC集群的可扩展LLM推理需求。

</details>

---

### 6. [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents](https://arxiv.org/abs/2607.20468v1)

**Authors**: Jehyeok Yeon, Ben Rank, Maksym Andriushchenko  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 48.5  
**Type**: new  
**ArXiv ID**: 2607.20468v1  

#### Abstract
AI agents are increasingly used to automate research and development tasks, yet existing benchmarks typically evaluate them on prescribed workflows or narrow action spaces. Even nominally open-ended tasks can often be solved by retrieving a well-known recipe and tuning a few hyperparameters, making ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents
1. 论文的主要贡献和创新点
✅ 解决的问题
现有评估AI代理的基准多针对规定工作流或狭窄动作空间设计，即使是名义上的开放任务也常通过检索知名配方和少量超参数调优解决，无法区分强结果源于真正的优化还是记忆解，导致难以评估代理在开放AI工程环境中的能力。
🚀 提出的新方法与思路
**InferenceBench**：构建面向LLM推理优化的开放-ended基准，要求AI代理部署OpenAI兼容的推理服务器并在两小时内优化LLM推理速度；基准包含四类优化场景，分别对应预填充延迟、解码延迟、并发请求吞吐量，以及同时平衡三者的综合场景；每个代理获得目标LLM、1张H100 GPU和两小时壁钟时间预算。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
任务开放程度 | 支持开放-ended AI代理任务评估，避免依赖记忆解
场景覆盖范围 | 覆盖四类LLM推理优化核心场景，全面考察代理能力
评估针对性 | 专门针对LLM推理优化任务，匹配AI代理研发需求
效果导向 | 以推理速度提升倍数为核心指标，直接反映优化价值
2. 核心实验方法和设置
📚 使用的数据集 | 论文未报告
🎯 实验设置与评估指标
任务：让AI代理在两小时内完成目标LLM推理服务器的部署及推理速度优化
指标 | 含义（箭头标方向）
--- | ---
推理速度提升倍数 | 越大越好（↑）
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
naive PyTorch baseline | 基准系统 | 未优化的基础PyTorch推理实现
默认设置vLLM | 服务引擎 | 开源服务引擎的原始默认配置
简单超参数搜索 | 调参方法 | 基于超参数搜索的自动调参方法
15个前沿代理配置 | 对比对象 | 用于评估的AI代理集合
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（代理优化效果）**
方法 | 相对于naive PyTorch baseline的加速倍数 | 相对于默认设置vLLM的加速倍数 | 相对于同时间预算简单超参数搜索的加速倍数
--- | --- | --- | ---
15个前沿代理配置 | up to 8.08× | up to 4.05× | 低于同时间预算简单超参数搜索（简单超参数搜索最高为11.53×）
💡 结论：15个前沿AI代理可显著提升LLM推理速度，但相同时间预算下的表现弱于简单超参数搜索方法。
论文未报告 效率对比（FPS / 参数量）
论文未报告 跨域 / zero-shot 迁移
论文未报告 鲁棒性 / 扰动测试
论文未报告 消融实验
4. 关键结论和发现
- 当前AI代理在InferenceBench上的优化瓶颈并非领域知识不足，而是缺少提出多样化优化配置、系统评估方案并提交最优解的能力；具体表现为代理虽枚举诸多相关优化技术，但过度收敛于单一推理框架，仅测试少量不同配置，剩余预算多用于重复测量、修复或微调超参数，而非探索差异化策略。
- InferenceBench可有效反映AI代理在开放AI工程环境中的真实能力，因为依赖记忆解的方法仅能带来有限提升。
- 当前AI代理的优化表现仍弱于同时间预算的简单超参数搜索，存在配置多样性与系统评估能力的短板。
方法局限性：代理在开放LLM推理优化中探索多样化配置的能力不足，导致整体性能弱于简单超参数搜索方法。
未来工作：需提升AI代理在开放LLM推理优化中提出多样化配置、系统评估方案的能力。

> ✅ **总结一句话**：InferenceBench是针对开放-ended LLM推理优化的AI代理评估基准，能有效区分真实优化与记忆解的有限提升，揭示当前AI代理的优化瓶颈在于配置多样性与系统评估能力。

</details>

---

### 7. [SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2607.20511v1)

**Authors**: Keonhee Park, Gunhee Kim  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.20511v1  

#### Abstract
Multimodal Continual Instruction Tuning (MCIT) is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving a sequence of downstream tasks. Prior methods mostly utilize Mixture of Experts or expansion merge approach, primarily focusing on catastrophic forgetting, yet they still suffe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning
1. 论文的主要贡献和创新点
✅ 解决的问题
MCIT（Multimodal Continual Instruction Tuning）是适配多模态大语言模型（MLLMs）至一系列下游任务的关键技术。现有方法多采用混合专家（Mixture of Experts）或扩展合并（expansion merge）思路，核心聚焦于缓解灾难性遗忘问题，但在推理阶段仍存在负干扰：新学习的参数更新会覆盖有用的先验知识，进而降低模型整体性能。

🚀 提出的新方法与思路
**Sign guided adaptive tuning**：训练阶段使用该策略，减少与过往知识的碰撞，以最小的漂移学习当前任务，缓解严重的遗忘问题。
**Sign guided merging**：推理阶段使用该策略，通过选择性缩放显著参数，进一步保留并放大有用的任务特定知识，提升模型的 consolidated 效果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 负干扰抑制 | 显著降低推理阶段的负干扰 |
| 整体性能 | 优于当前最先进（state of the art）的MCIT方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| UCIT | 基准测试 |
| DCL | 基准测试 |

🎯 实验设置与评估指标
任务为多模态持续指令调优（MCIT）。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体指标及其含义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有MCIT方法（采用Mixture of Experts或expansion merge思路） | 持续指令调优方法 | 主要关注灾难性遗忘问题，仍存在推理阶段的负干扰，新学习参数会覆盖先验知识导致整体性能下降 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：名称（场景）**
论文未报告

💡 结论：论文未报告

1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. SiGMA框架通过训练时的符号引导自适应调优与推理时的符号引导合并，可有效减少MCIT中的负干扰，性能优于当前SOTA MCIT方法；2. 该框架能缓解持续学习中的灾难性遗忘问题，减少新任务学习时对先验知识的不必要覆盖。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SiGMA是针对多模态持续指令调优提出的框架，通过符号引导的训练与推理阶段策略，降低负干扰、缓解灾难性遗忘，性能优于当前最先进的多模态持续指令调优方法。

</details>

---

### 8. [DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions](https://arxiv.org/abs/2607.20469v1)

**Authors**: Zishan Shao, Lixun Zhang, Kangning Cui, Yixiao Wang, Ting Jiang, Hancheng Ye, Qinsi Wang, Zhixu Du, Yuzhe Fu, Fan Yang, Danyang Zhuo, Yiran Chen, Hai Helen Li  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.20469v1  

#### Abstract
Large language models (LLMs) handle many tasks with one set of parameters, but under KV-cached inference it is unclear what task-general structure, if any, is used at decode time rather than during prefill. We propose DecodeShare, a protocol that identifies a low-dimensional subspace consistently sh...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions
1. 论文的主要贡献和创新点
✅ 解决的问题：LLM采用同一组参数处理多任务，但KV-cached推理下，解码阶段是否存在任务通用结构尚不明确，而预填充（prefill）阶段的结构已被研究，解码阶段的任务通用结构（若存在）的作用未被明确，无法确定解码阶段的核心因果通道。
🚀 提出的新方法与思路
**DecodeShare协议**：该协议先识别LLM解码阶段隐状态中跨任务一致的低维子空间，再通过仅在解码阶段移除该子空间的干预方式，验证其因果作用。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
性能干扰对比 | 干扰DecodeShare识别的解码共享子空间，其决策性能下降幅度远大于干扰prefill衍生或随机子空间
激活 steering应用 | 解码时间的 steering向量用于下游部署时，信号可靠性高于prefill代理
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：实验任务为LLM解码阶段共享子空间的因果作用与应用研究；论文未报告具体评估指标细节
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
prefill-derived subspace干扰 | 对比基线 | 干扰预填充阶段衍生子空间
random subspace干扰 | 对比基线 | 干扰随机生成的子空间
3. 主要实验结果和性能指标
📊 定量结果汇总
**扰动测试实验**
论文中提到，干扰DecodeShare识别的解码共享子空间，其决策性能下降幅度显著大于干扰prefill衍生或随机子空间，该结果无对应表号。
💡 结论：解码阶段跨任务共享的低维子空间是LLM决策性能的高杠杆因果通道。
**激活 steering对比**
论文中提到，解码时间的 steering向量用于下游部署时，信号比prefill代理更可靠，无对应表号。
💡 结论：解码时间的 steering向量相比prefill代理更适用于下游部署。
4. 关键结论和发现
- LLM解码阶段存在跨任务一致的低维共享子空间，该子空间是解码时的高杠杆因果通道
- 干扰该解码共享子空间对决策性能的影响远大于干扰prefill衍生或随机子空间
- 解码时间的 steering向量用于下游部署时，信号可靠性优于prefill代理
- 论文未报告明确的方法局限性
- 论文未报告明确的未来工作方向

> ✅ **总结一句话**：提出DecodeShare协议识别LLM解码隐状态中跨任务共享的低维子空间，验证其为解码阶段的高杠杆因果通道，且该子空间可提升激活 steering的下游部署可靠性。

</details>

---

### 9. [AI-Driven Multi-Hop Relay Selection for Smart Urban NR-V2X Networks via Learning-to-Optimize Graph Neural Networks](https://arxiv.org/abs/2607.20554v1)

**Authors**: Giambattista Amati, Federica Mangiatordi, Simone Angelini, Emiliano Pallotti, Pierpaolo Salvo  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.20554v1  

#### Abstract
Reliable and low-latency NR-V2X communications are essential for smart mobility in dense urban environments. However, limited Road-Side Unit (RSU) density, frequent non-line-of-sight conditions, and highly dynamic vehicular topologies often prevent many Connected and Automated Vehicles (CAVs) from m...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AI-Driven Multi-Hop Relay Selection for Smart Urban NR-V2X Networks via Learning-to-Optimize Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
城市密集环境下NR-V2X通信要求可靠且低延迟，但存在RSU密度有限、非视距频繁、车辆拓扑高度动态导致单跳连通性不稳定的痛点；现有Mixed-Integer Linear Programming (MILP)方法能生成最优多跳中继决策，但计算复杂度随网络密度急剧增加，无法适配实时应用场景。

🚀 提出的新方法与思路
**Learning-to-Optimize (L2O)框架**：针对实时性不足的问题，采用L2O框架结合图神经网络实现多跳中继的实时选择；
**边感知图同构网络（GINE）**：将车载通信状态建模为属性图，以CAVs和RSUs为节点，候选无线链路融入传播感知特征；利用离线MILP生成最优监督信号，由GINE近似MILP的决策，实现接近常数的推断延迟。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 连通性 | 性能与MILP最优决策相当 |
| 执行效率 | 相比MILP，执行时间降低数个数量级，满足实时需求 |
| 场景扩展性 | 支持大规模城市V2X场景，复用现有车载资产，实现低成本连通性增强 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| SUMO-GEMV2集成模拟管道生成的大规模城市数据集 | 生成实验所需的网络仿真数据 |

🎯 实验设置与评估指标
任务为城市NR-V2X网络的多跳中继选择，保障连通性与低延迟的实时决策；
| 指标 | 含义 |
| ---- | ---- |
| 连通性 | 网络连通状态，↑越高越好 |
| 执行时间 | 决策所需时长，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| MILP | 最优决策方法 | 生成多跳中继的全局最优决策，但计算复杂度高，无法实时运行 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号对应的定量实验数值，仅提及提出方法连通性与MILP oracle相当，执行时间降低数个数量级。
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：基于L2O的边感知GINE框架可在保持与最优MILP方法相当的网络连通性的前提下，大幅缩短中继选择的执行时间，满足城市NR-V2X的实时通信需求；该方法可复用现有车载资源，实现低成本的城市V2X连通性增强。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的基于L2O框架的边感知GINE模型，解决了城市NR-V2X网络多跳中继选择中最优方法实时性不足的问题，在保持连通性接近最优解的同时大幅提升执行效率，适配大规模智能城市V2X场景的实时需求。

</details>

---

### 10. [Optimizing Hypergraph-Based RAG: Toward Better Fact Extraction and Chunk Retrieval](https://arxiv.org/abs/2607.20506v1)

**Authors**: Houda Khrouf, Pedro Fillastre, Sebastiao Correia  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.20506v1  

#### Abstract
GraphRAG enables deeper reasoning by structuring knowledge as graphs but struggles with n-ary facts. HyperGraphRAG uses hypergraphs for richer semantics, improving accuracy, yet relies on error-prone LLM extraction and inefficient standard chunk retrieval. We address this by employing self-consisten...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Optimizing Hypergraph-Based RAG: Toward Better Fact Extraction and Chunk Retrieval
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：GraphRAG在将知识结构化时难以处理n-ary事实；HyperGraphRAG虽提升了准确率，但存在两大缺陷——依赖易出错的LLM抽取机制、采用的标准块检索方式效率低下。

🚀 提出的新方法与思路
**Self-Consistency Prompting**：用于优化HyperGraphRAG中依赖的LLM事实抽取环节，解决抽取结果易出错的问题。
**Personalized PageRank over hypergraph**：用于改进HyperGraphRAG的块检索环节，解决标准块检索低效的问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 事实抽取稳定性 | 通过Self-Consistency Prompting缓解了HyperGraphRAG依赖的LLM事实抽取易出错的问题 |
| 块检索效率 | 采用HyperGraph上的Personalized PageRank算法，优化了HyperGraphRAG原有的低效标准块检索流程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
论文未报告任务的具体内容及评估指标细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：论文未报告
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文针对GraphRAG处理n-ary事实的不足以及HyperGraphRAG依赖易出错的LLM抽取、块检索低效的问题，提出用Self-Consistency Prompting优化事实抽取、用HyperGraph上的Personalized PageRank改进块检索的方法，以提升基于超图的RAG效果。

</details>

---

### 11. [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412v1)

**Authors**: Bartolomeo Bogliolo  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.21412v1  

#### Abstract
Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symboli...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型（LLMs）擅长自然语言的理解与生成，但在多步逻辑推理任务中不可靠，尤其不适用于安全关键或合规敏感领域；近期的神经符号方法虽结合了神经网络与外部符号引擎，但多数为定制化实现，缺乏面向工具增强智能体的标准化交互接口。

🚀 提出的新方法与思路
**Euclid-MCP**：开源的Model Context Protocol（MCP）服务器，通过SWI-Prolog实现确定性逻辑推理；其暴露了简洁的工具接口，支持translate-run-inspect-repair循环，使LLM客户端可委托推理任务，同时保留对证明轨迹与推导日志的完全访问权限。
**Euclid-IR**：引擎无关的中间表示，基于Horn子句逻辑构建，具备人类可读、易于LLMs生成、可直接编译为Prolog或其他符号后端的特点。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 逻辑可靠性 | 提供确定性推理，避免LLMs在逻辑任务中的系统性幻觉 |
| 接口标准化 | 为工具增强智能体提供统一的交互入口 |
| 推理可追溯性 | 保留完整的证明轨迹与推导日志 |
| 后端灵活性 | Euclid-IR可编译为Prolog或其他符号引擎 |
| 性能特性 | 在逻辑推理中提供准确答案，延迟更低、输出更紧凑 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 现实IT安全与合规场景数据集 | 用于评估Euclid-MCP在确定性逻辑推理任务中的性能 |

🎯 实验设置与评估指标
任务：在现实IT安全与合规场景下开展确定性逻辑推理任务；评估指标：论文未明确说明具体评估指标名称及定义，仅提及对比单独LLMs与Euclid-MCP的答案准确性、推理延迟、输出紧凑度。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 单独的LLMs | 纯神经方法 | 小知识基下逻辑推理表现尚可，大知识基下存在系统性逻辑幻觉 |
| Euclid-MCP | 神经符号方法 | 结合LLMs与符号引擎，实现确定性逻辑推理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验均未在论文中提供具体表号、图号或页码对应的数值结果，因此：
**主benchmark性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：① 单独的LLMs在小知识基上的逻辑推理足够可靠，但在大知识基上会出现系统性幻觉；② Euclid-MCP在确定性逻辑推理任务中可提供准确答案，延迟更低、输出更紧凑；③ 语义RAG在规则执行方面本质上不适用。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Euclid-MCP是一款开源的MCP服务器，通过集成SWI-Prolog与引擎无关的Euclid-IR中间表示，为需要确定性逻辑推理的场景提供标准化、可追溯的神经符号工具接口，解决了LLMs多步逻辑推理不可靠及现有神经符号方法缺乏统一交互标准的问题。

</details>

---

### 12. [PortLBM: A Portable Lattice Boltzmann Tool Leveraging SYCL on AMD, NVIDIA, and Intel GPUs](https://arxiv.org/abs/2607.20650v1)

**Authors**: Alexander Strack, Marcel Graf, Alexander Van Craen, Dirk Pfl\"uger  
**Category**: cs.DC  
**Published**: 2026-07-24  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.20650v1  

#### Abstract
The lattice Boltzmann method (LBM) is a well-established approach for simulating fluid flows at the mesoscopic scale. With the stagnation of Moore's law, high-performance computing has shifted toward GPU accelerators, necessitating programming models that ensure both portability and efficiency acros...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PortLBM: A Portable Lattice Boltzmann Tool Leveraging SYCL on AMD, NVIDIA, and Intel GPUs
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：摩尔定律停滞，高性能计算转向GPU加速器，亟需兼顾跨平台可移植性和硬件效率的LBM（格子玻尔兹曼方法）编程工具；现有方案普遍难以在AMD、NVIDIA、Intel等不同厂商GPU间同时满足兼容性、性能优化及易扩展的需求。

🚀 提出的新方法与思路
**PortLBM可扩展框架**：基于SYCL构建的便携式LBM框架，集成跨平台GPU支持与交互式实时可视化功能；支持卡门涡街（Kármán vortex streets）、翼型流动、多孔介质等多类流体模拟场景，且设计上易于扩展新算法与后端。
**性能可移植性评估方案**：围绕三种数据布局（stream、bundle、collision）和四种算法变体，评估其对模拟吞吐量的影响，为异构硬件适配提供依据。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨平台兼容性 | 基于SYCL实现，支持AMD、NVIDIA、Intel三大GPU厂商 |
| 可扩展性 | 架构设计支持轻松扩展新算法与计算后端 |
| 集成功能 | 内置交互式实时可视化，适配多样模拟场景需求 |
| 性能适配性 | 覆盖多类数据布局与算法变体评估，支持硬件特定调优 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | - |

🎯 实验设置与评估指标
任务：在NVIDIA、AMD、Intel三大厂商GPU上，测试PortLBM不同数据布局及算法变体的流体模拟性能；指标为模拟吞吐量。
| 指标 | 含义（↑ 越高越好） |
| --- | --- |
| 吞吐量 | 流体模拟吞吐量，数值越大代表性能越优 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | - | - |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告带有表号、图号或具体数值的定量实验结果，仅得出定性结论：
不存在单一配置可在所有GPU厂商上实现最优性能；stream数据布局在NVIDIA、Intel GPU上性能最佳，因最大化内存带宽；bundle数据布局在AMD GPU上表现最优，因提升缓存效率；双格子（two-lattice）算法变体吞吐量更高，单格子（one-lattice）算法变体更适用于内存受限场景。

4. 关键结论和发现
- 主要发现：1. 异构GPU环境下，PortLBM无通用最优配置，需针对不同厂商GPU进行系统特定调优；2. 数据布局对PortLBM性能影响显著，需根据GPU厂商类型选择适配布局；3. 算法变体选择需权衡吞吐量与内存资源，内存充足时双格子方案更优，内存受限场景下单格子方案更适用。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出了基于SYCL的可扩展便携式LBM框架PortLBM，集成跨GPU支持与实时可视化，通过评估数据布局和算法变体的性能，为异构计算环境下的流体模拟提供了适配性方案。

</details>

---

### 13. [Reliability-Aware LLM Alignment from Inconsistent Human Feedback](https://arxiv.org/abs/2607.20515v1)

**Authors**: Jingyi Huang, Ruohan Zong, Yujun Feng, Liran Ma, Lanyu Shang, Yang Zhang  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.20515v1  

#### Abstract
Reinforcement Learning from Human Feedback (RLHF) is critical for aligning Large Language Models (LLMs) with human preferences. However, its efficacy is often compromised by the inherent inconsistency and subjectivity of human annotations. Existing preference optimization frameworks, such as Direct ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Reliability-Aware LLM Alignment from Inconsistent Human Feedback
1. 论文的主要贡献和创新点
✅ 解决的问题
RLHF是对齐大型语言模型（LLMs）与人类偏好的关键方法，但人类标注存在固有不一致性与主观性，现有偏好优化框架（如Direct Preference Optimization，DPO）将高标注分歧的模糊对与全一致对同等对待，导致模型过拟合不一致的监督信号，对齐效果次优。
🚀 提出的新方法与思路
**Reliability-Guided Preference Optimization (RGPO)**：该框架包含两个核心设计，一是估计标注者可靠性，从嘈杂的人类反馈中推断隐式真实标签，识别稳健偏好；二是设计**可靠性感知一致性优化**，根据标注的共识水平动态调整训练目标，确保模型优先处理高共识监督信号。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 处理不一致反馈 | 区分不同共识水平的标注对，抑制嘈杂信号干扰 |
| 训练目标优先级 | 动态调节训练权重，优先采纳高可靠监督信号 |
| 过拟合风险 | 降低对不一致标注信号的过拟合程度 |
| 对齐性能 | 优于RLHF类基线方法 |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务为LLM对齐，评估指标论文未报告。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| RLHF | LLM对齐基线 | 被广泛采用的传统LLM对齐方法 |
| Direct Preference Optimization (DPO) | 现有偏好优化框架 | 同等对待不同共识水平的标注对 |
| RGPO | 提出的新方法 | 可靠性引导的偏好优化，优先高共识监督信号 |
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：① 人类反馈的不一致性与主观性会削弱RLHF类方法的LLM对齐效果；② 现有偏好优化框架（如DPO）对不同共识水平标注的同等处理会导致模型过拟合嘈杂监督信号；③ RGPO可减少训练数据中的不一致与噪声，对齐性能优于RLHF基线。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：提出的RGPO框架通过估计标注者可靠性并动态调整训练目标，有效缓解人类反馈不一致对LLM对齐的负面影响，对齐性能优于现有RLHF基线方法。

</details>

---

### 14. [PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.21419v1)

**Authors**: Yipeng Shi, Zhipeng Ma, Yue Wang, Qitai Tan, Yang Li, Peng Chen, Zhengzhou Zhu  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.21419v1  

#### Abstract
In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. Howev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
长 horizon LLM agent强化学习中，弱策略重复相似失败，产出无信息的rollout轨迹，制约有效策略优化；现有skill-centric方法聚焦技能本身的优化、过滤或内化复用，未针对演化中的策略设计自适应训练时支持机制，偏离优化需求导致策略性能受限。

🚀 提出的新方法与思路
**Policy-Aware Training Scaffolding（PATS框架）**：将最新策略生成的rollout groups转化为evidence cards，借助任务特定评估调整后续rollout使用的上下文；为弱策略提供具体指导以完成挑战性任务；策略性能提升后，修改或移除冗余上下文以减少对明确指导的依赖，同时保留有用的rollout变化；策略优化采用标准RLVR结合环境奖励，训练阶段的scaffold在部署时丢弃。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 主基准任务性能 | 在ALFWorld和WebShop任务上优于现有强基线 |
| 资源效率 | 在7个搜索增强QA基准任务上，相比基线减少prompt tokens使用，同时保持任务竞争力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ALFWorld | 长horizon LLM agent强化学习主基准实验场景之一 |
| WebShop | 长horizon LLM agent强化学习主基准实验场景之一 |
| 7个搜索增强QA基准 | 搜索类任务性能及资源效率实验场景 |

🎯 实验设置与评估指标
任务：围绕长horizon LLM agent强化学习及搜索增强QA任务展开评估，验证方法的任务性能与资源效率。
| 指标 | 含义 |
| ---- | ---- |
| 主基准任务性能 | 策略完成ALFWorld、WebShop任务的能力，越高越好 |
| QA任务性能 | 7个搜索增强QA基准的任务完成能力，保持竞争力即可 |
| prompt tokens使用量 | 策略生成所需的prompt token数量，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 强基线 | 现有skill-centric强化学习方法 | 聚焦技能本身优化与内化，未设计针对演化策略的自适应训练支持，在任务性能与prompt资源使用上弱于PATS |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主基准实验性能
在ALFWorld和WebShop的长horizon LLM agent任务中，PATS优于现有强基线。
💡 结论：PATS解决了长horizon LLM agent训练中弱策略轨迹低效的痛点，显著提升主基准任务性能。
2. 搜索增强QA基准实验性能
在7个搜索增强QA基准任务中，PATS相比基线减少prompt tokens使用，同时保持任务竞争力。
💡 结论：PATS在非agent类的QA任务场景下同样具备优势，可有效降低prompt资源消耗且不牺牲任务性能。
3. 其他实验
效率对比（FPS / 参数量）：论文未报告；
跨域/zero-shot迁移：论文未报告；
鲁棒性/扰动测试：论文未报告；
消融实验：论文未报告。

4. 关键结论和发现
- 核心发现：针对长horizon LLM agent强化学习中弱策略轨迹无信息的问题，以策略为中心的PATS框架通过动态调整训练scaffold的设计，既提升主基准任务性能，又在QA场景下减少prompt资源消耗且保持竞争力。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：PATS是一种以策略为中心的动态训练脚手架框架，在长horizon LLM agent强化学习主基准任务上优于强基线，且在搜索增强QA基准任务中保持竞争力的同时减少prompt tokens使用。

</details>

---

### 15. [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works](https://arxiv.org/abs/2607.21273v1)

**Authors**: Yu Wang  
**Category**: cs.LG  
**Published**: 2026-07-24  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.21273v1  

#### Abstract
Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works
1. 论文的主要贡献和创新点
✅ 解决的问题
此前研究者认为GRPO框架下，密集预测下一个观测的每步监督可解决LLM智能体的稀疏奖励、长 horizon 问题，但论文发现该方法会导致策略退化，出现“黑暗房间”病理：预测准确率趋近1.0、任务成功率为0、episode 长度固定在最大 horizon，核心矛盾是密集预测奖励在GRPO下非但无法提升性能，反而摧毁策略。

🚀 提出的新方法与思路
**方差轮廓准则**：提出该准则解释黑暗房间病理的成因，指出GRPO的z-scoring会放大密集信号的组内方差，当全失败组占主导时会引发策略退化；该准则可追溯已观测到的策略崩溃，对未开展的实验做出预注册预测，且与已发表的奖励通道成功案例兼容。
**信号消费机制评估**：通过控制信号（仅改变消费机制）的实验发现，奖励通道对任务的增益至多为中性，辅助损失通道的性能提升约20点；洗牌黄金安慰剂组与真黄金组表现无显著差异，说明该增益不依赖正确标签。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 策略稳定性 | 可通过方差轮廓准则提前识别GRPO下密集预测奖励引发的策略崩溃 |
| 信号效能识别 | 明确对比奖励通道与辅助损失通道的实际效能，指出辅助损失通道更适配长 horizon 稀疏奖励的LLM智能体优化 |
| 可解释性 | 提出的准则能解释策略崩溃的成因，且对未开展实验做出可验证的预测 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ALFWorld | 测试GRPO训练的LLM智能体的策略性能，观测黑暗房间病理 |

🎯 实验设置与评估指标
任务为ALFWorld场景下的长 horizon、稀疏奖励的LLM智能体任务；评估指标如下：
| 指标 | 含义（箭头） |
| ---- | ---- |
| 预测准确率 | 智能体预测下一个观测的准确率，越高越好 ↑ |
| 任务成功率 | 智能体完成ALFWorld任务的比例，越高越好 ↑ |
| episode长度 | 智能体单episode的步数，越接近最大horizon越异常 ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GRPO+密集潜在基预测奖励 | 原方法 | 在GRPO下搭配密集预测奖励，会引发黑暗房间病理 |
| 移除std归一化的GRPO | 改进基线 | 移除GRPO的std归一化，任务性能从灾难性转为基线水平 |
| 辅助损失通道方法 | 对比方法 | 性能比奖励通道高约20点 |

3. 主要实验结果和性能指标
**主基准性能（ALFWorld）**：论文未标注表号，仅指出Qwen3-1.7B/4B/8B模型在GRPO+密集预测奖励设置下均出现黑暗房间病理，预测准确率趋近1.0，任务成功率为0，episode长度固定在最大horizon；移除GRPO的std归一化后任务成功率恢复至基线水平。
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验 —— GRPO的std归一化**
| 模块 | 启用（✅）/禁用（❌） | 任务成功率 |
| ---- | ---- | ---- |
| GRPO的std归一化 | ✅ | 0% |
| GRPO的std归一化 | ❌ | 基线水平 ✅ |
💡 结论：GRPO的std归一化是引发黑暗房间病理的关键因素，移除后密集预测奖励不再摧毁策略。

4. 关键结论和发现
- 主要发现：1）GRPO训练的LLM智能体中，密集预测奖励会引发“黑暗房间”病理，导致策略完全退化；2）该病理由GRPO的z-scoring放大全失败组的组内方差导致，可通过方差轮廓准则解释；3）辅助损失通道对任务的性能增益显著高于奖励通道，且不依赖正确标签。
- 方法局限性：论文使用的实验端点为单种子，种子复制和组大小控制实验仍在进行中。
- 未来工作：未明确提及具体未来方向，种子复制、组大小控制等预注册实验正在开展。

> ✅ **总结一句话**：本文揭示了GRPO框架下密集预测奖励会引发LLM智能体的策略崩溃黑暗房间病理，提出方差轮廓准则解释成因，并发现辅助损失通道比奖励通道更适合长 horizon 稀疏奖励任务的优化。

</details>

---

### 16. [Expert Behavior Prior Reinforcement Learning](https://arxiv.org/abs/2607.21302v1)

**Authors**: Gong Gao, Weidong Zhao, Xianhui Liu, Ning Jia  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.21302v1  

#### Abstract
Behavior prior reinforcement learning (BPRL) has emerged as a promising paradigm to improve sample efficiency in online reinforcement learning (RL) by leveraging policy priors derived from offline demonstrations. However, most existing BPRL methods rely on static offline datasets, which often suffer...

---

### 17. [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557v1)

**Authors**: Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.21557v1  

#### Abstract
Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks can...

---

### 18. [X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment](https://arxiv.org/abs/2607.21550v1)

**Authors**: Dongjie Fu, Di Cao, Xize Cheng, Zihan Zhang, Wenxu Jia, Yifu Chen, Shengpeng Ji, Yu Zhang, Tao Jin  
**Category**: cs.LG  
**Published**: 2026-07-24  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.21550v1  

#### Abstract
While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on...

---

### 19. [Isolating LLM Alignment from Regex: Zero Coverage and Metric-Dependent Divergence Under Adversarial Mutation](https://arxiv.org/abs/2607.20494v1)

**Authors**: Alexandre Cristov\~ao Maiorano  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.20494v1  

#### Abstract
Production LLM applications commonly stack a regex filter in front of model-side alignment; prior work found no measurable coverage gain from adding a live Gemini backend behind an active regex filter. We ask whether that ceiling holds when the corpus is \emph{designed to bypass the regex}. We intro...

---

### 20. [FlowEdit: Information-Theoretic Control of LLM Reasoning Flows for Ill-posed Problems Involving Conflicts](https://arxiv.org/abs/2607.20500v1)

**Authors**: Sizhe Tang, Guangyu Jiang, Yu Li, Rongqian Chen, Ioannis G. Kevrekidis, Tian Lan  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.20500v1  

#### Abstract
Large Language Models (LLMs) perform strongly on well-specified reasoning tasks with a feasible answer. However, problems encountered in the open world can become ill-posed due to inconsistent conditions, conflicting statements, or mutually incompatible requirements, admitting no valid responses. We...

---

### 21. [Differentiable Logic Programming to Mitigate Reasoning Shortcuts in Neurosymbolic Systems](https://arxiv.org/abs/2607.21185v1)

**Authors**: Akihiro Takemura (National Institute of Informatics, Tokyo, Japan), Katsumi Inoue (National Institute of Informatics, Tokyo, Japan)  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.21185v1  

#### Abstract
Neurosymbolic (NeSy) systems integrate neural networks with logical reasoning to achieve both generalization and interpretability, but recent work has shown they are susceptible to shortcut reasoning behaviors.  We propose a novel method using matrix-based differentiable logic programming to mitigat...

---

### 22. [TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG](https://arxiv.org/abs/2607.20437v1)

**Authors**: Chahana Dahal, Zuobin Xiong  
**Category**: cs.CL  
**Published**: 2026-07-24  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.20437v1  

#### Abstract
Production Retrieval Augmented Generation (RAG) systems rely on aggregating multiple external documents to answer complex queries. However, the retrieved documents introduce a new threat surface that can be exploited to launch split-knowledge attacks. In this attack, the adversary injects documents ...

---

### 23. [Context-weighted Discrete Flow Matching](https://arxiv.org/abs/2607.21427v1)

**Authors**: Daniil Cherniavskii, Daniel Severo, Karen Ullrich  
**Category**: cs.LG  
**Published**: 2026-07-24  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.21427v1  

#### Abstract
Discrete flow matching provides a flexible framework for generative modeling on discrete structures. However, the standard factorized training objective exposes the model to targets of varying difficulty, mixing well-conditioned, predictable tokens with ambiguous, high-entropy ones. We empirically d...

---

### 24. [SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification](https://arxiv.org/abs/2607.20475v1)

**Authors**: Pragaash Ponnusamy, Shivam Sahni, Jue Wang, Tri Dao  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 28.0  
**Type**: new  
**ArXiv ID**: 2607.20475v1  

#### Abstract
Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding. However, existing implementations either accelerate only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous sampling beha...

---

### 25. [OPOD: On-Policy Omni Distillation](https://arxiv.org/abs/2607.20918v1)

**Authors**: Tong Zhao, Yuyang Hu, Reed Li, Yu Lu, Haibo Shi, Yutao Zhu, Zhicheng Dou  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.20918v1  

#### Abstract
Omni-modal models can handle text, images, and audio in one system, but improving all of these abilities together remains difficult. Training a single model on pooled multimodal data often fails to match models specialized for individual modalities. On-policy distillation (OPD) offers a way to combi...

---

### 26. [Nipping the Butterfly Effect in the Bud: Self-Output Fine-Tuning for Autoregressive Weather Prediction](https://arxiv.org/abs/2607.21080v1)

**Authors**: Yun-Ye Cai, Hsuan-Tien Lin  
**Category**: cs.LG  
**Published**: 2026-07-24  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.21080v1  

#### Abstract
Long-horizon weather forecasting is a fundamental challenge in atmospheric science, for which autoregressive Deep Learning Weather Prediction (DLWP) has emerged as the primary paradigm. Although the autoregressive pipeline is highly scalable and flexible, its prediction errors grow rapidly over long...

---

### 27. [WaveformQA: Benchmarking LLM Temporal Reasoning on Digital Waveforms](https://arxiv.org/abs/2607.20638v1)

**Authors**: Yichuan Liu, Daniel Cummings, Nick Vadlamudi  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.20638v1  

#### Abstract
Large Language Models (LLMs) have demonstrated strong capabilities in code generation and reasoning, yet their ability to perform temporal reasoning over digital waveform data remains largely unexplored. Although reasoning over digital waveforms is a critical bottleneck in design verification, exist...

---

### 28. [Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning](https://arxiv.org/abs/2607.21558v1)

**Authors**: Baihui Wang, Bernard Koch  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.21558v1  

#### Abstract
Building socially calibrated large language models, which can learn from others without simply yielding to them, requires more than reducing sycophancy as a one-dimensional failure mode. Models must distinguish when to incorporate others' perspectives from when to maintain a well-grounded moral judg...

---

### 29. [What is Good? Extracting and Testing Implicit Theories of Literary Quality from LLM Reasoning Traces](https://arxiv.org/abs/2607.20425v1)

**Authors**: Birger Mo\"ell  
**Category**: cs.CL  
**Published**: 2026-07-24  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.20425v1  

#### Abstract
What makes writing "good" remains a persistent question in literary studies and computational linguistics. We present a two-study investigation of how reasoning-enabled LLMs evaluate literary quality.
  In Study 1, we construct a benchmark of 30 real texts spanning six quality tiers, from canonical ...

---

### 30. [AREX: Towards a Recursively Self-Improving Agent for Deep Research](https://arxiv.org/abs/2607.21461v1)

**Authors**: Shuqi Lu, Chaofan Li, Kun Luo, Zhang Zhang, Hui Wang, Hongwang Xiao, Zheng Liu, Lei Xiong, Jiahao Wang, Sen Wang, Xiyan Jiang, Wanli Li, Yuyang Hu, Hongjin Qian, Bingyu Yan, Ziyi Xia, Yingxia Shao, Kang Liu, Zhicheng Dou, Di He, Chaozhuo Li, Qiwei Ye, Zhongyuan Wang, Zheng Liu  
**Category**: cs.AI  
**Published**: 2026-07-24  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.21461v1  

#### Abstract
Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do mo...

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
