# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-26 06:11:11 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21808v1)

**Authors**: Suifeng Zhao, Zida Liu, Xinyu Lei, Lei Sun, Jun Gao, Sujian Li  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 94.5  
**Type**: new  
**ArXiv ID**: 2608.21808v1  

#### Abstract
Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
当前Multimodal RAG及基于SFT的方法存在跨模态推理稳健性不足的核心痛点，其中Multimodal RAG方法存在引用与生成答案脱钩的缺陷，基于SFT的方法存在视觉引用不精确的缺陷，共同导致多模态大语言模型（MLLMs）的可追溯性与可验证性不足。
🚀 提出的新方法与思路
**Agentic Refinement模块**：该模块用于视觉引用任务，通过迭代检索、推理和递归裁剪逐步缩小搜索空间，将视觉引用从静态步骤转化为动态的、证据驱动的推理过程。
**Citation-enhanced Reward机制**：在强化学习范式中整合过程级反馈与结果级反馈，实现对答案准确性与源可追溯性的协同优化。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 引用与答案的协同优化 | 有效实现引用精度与答案质量的联合提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Wiki-VISA | 本实验的基准测试数据集 |
| FinRAGBench-V | 本实验的基准测试数据集 |
| MMLongBench-Doc | 本实验的基准测试数据集 |
🎯 实验设置与评估指标
论文未报告
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的定量实验结果及对应表格（无明确数值、表号信息）

4. 关键结论和发现
- 主要发现：MCite-RL框架通过Agentic Refinement模块和Citation-enhanced Reward机制，在Wiki-VISA、FinRAGBench-V、MMLongBench-Doc等多模态RAG基准上有效实现了引用精度与答案质量的联合优化。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MCite-RL是一种引用增强的智能体强化学习框架，解决了现有多模态RAG方法视觉引用不精确或引用与答案脱钩的问题，可在多个基准上协同提升引用精度与答案质量。

</details>

---

### 2. [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning](https://arxiv.org/abs/2608.22479v1)

**Authors**: Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, Qin Zhang, Ziyue Qiao, Xiao Luo  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 94.0  
**Type**: new  
**ArXiv ID**: 2608.22479v1  

#### Abstract
Retrieval-augmented generation (RAG) enables LLMs to access external knowledge for answering knowledge-intensive questions. For complex multi-hop questions, multi-turn retrieval-augmented reasoning extends RAG into an iterative process that repeatedly searches for and integrates evidence across docu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于agentic RAG的强化学习方法通常采用最终答案奖励，存在监督信号稀疏的问题，且未考虑模型是否实际获取了所需的证据链，无法满足多跳检索增强推理对证据获取的要求。

🚀 提出的新方法与思路
**Graph-Trajectory-Augmented RL Framework**：该框架从实体-文档图中采样连通文档路径，合成多跳QA轨迹，通过部署的检索器验证这些轨迹以获取可执行的轨迹级监督信号；随后使用Group Relative Policy Optimization（GRPO）优化检索策略，采用轨迹引导奖励函数，该奖励同时鼓励生成准确答案和获取目标证据文档，最后在自然QA实例上进行答案奖励训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 推理性能 | 在多跳和简单QA基准上均优于基于RL的RAG基线 |
| 证据链覆盖 | 显著提升证据链覆盖能力 |
| 监督信号质量 | 提供轨迹级监督，解决仅用最终答案奖励导致的监督信号稀疏问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 三个多跳QA基准 | 评估多跳检索增强推理性能 |
| 两个简单QA基准 | 评估简单问答性能 |

🎯 实验设置与评估指标
任务：多轮检索增强推理，包含多跳和简单QA任务。论文未报告具体评估指标名称及细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 基于RL的RAG基线 | 对比基线 | 采用最终答案奖励的强化学习方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告具体定量数值、对应表号或图号。
**效率对比**：论文未报告。
**跨域/zero-shot迁移**：论文未报告。
**鲁棒性/扰动测试**：论文未报告。
**消融实验**：论文未报告。

4. 关键结论和发现
- 主要发现：GTA-RAG在三个多跳和两个简单QA基准上均优于基于RL的RAG基线；GTA-RAG能显著提升证据链覆盖；轨迹级监督结合GRPO的框架可有效优化多轮检索增强推理。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：GTA-RAG是一种结合图轨迹增强强化学习与轨迹级监督的多轮检索增强推理框架，可提升推理性能和证据链覆盖，优于现有基于RL的RAG基线。

</details>

---

### 3. [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving](https://arxiv.org/abs/2608.23962v1)

**Authors**: Srikanta Datta Tumkur, Mehar Simhadri, Anshu Bansal, Jay Iyer, Sai Pavan Kumar, Sai Kapil Kumar, Ramesh Nampelly, Raj Dandekar  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 86.0  
**Type**: new  
**ArXiv ID**: 2608.23962v1  

#### Abstract
When an LLM serving deployment runs out of KVcache room, there are two well-established ways out. Tensor parallelism shards the weights and the KV cache across two, four, or eight devices, buying memory headroom at the price of an all-reduce on every layer and a hardware bill that grows with the dev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
当LLM serving部署的KV缓存空间耗尽时，两种成熟解决方案（张量并行与KV压缩）分别被研究，但现有研究存在核心矛盾：两类方案分别报告内存比、吞吐量曲线，未放在同一成本轴上对比；各自存在固有缺陷，张量并行需随设备增长提升成本且每一层需全归约操作，KV压缩以小质量损失换空间但未与张量并行做统一成本比较。
🚀 提出的新方法与思路
**成本归一化对比框架**：构建“每百万令牌的成本对延迟”的统一成本轴，将张量并行配置（degree 1到8）与KV压缩配置（16/8/4-bit，保留比率低至0.25）置于该轴对比，使用校准了A100、A40、H100硬件的分析器（profiled simulator）开展研究，寻找两种方案的成本等效临界点。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 成本效率 | KV压缩的成本比张量并行低1.20x至2.00x |
| 每美元容量提升 | KV压缩的每美元容量是花费8倍GPU的张量并行方案的16.5倍，后者仅为1.21倍 |
| 延迟调控 | 张量并行是唯一能改善延迟的手段，KV压缩会使每令牌延迟增加8%至93% |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
任务为内存受限的LLM serving（KV缓存空间耗尽时的部署策略选择），评估指标及箭头含义如下：
| 指标 | 含义 |
| --- | --- |
| 每百万令牌成本 | ↓ 越低越好 |
| 延迟 | ↓ 越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 张量并行（degree 1~8） | 硬件扩展方案 | 分片权重与KV缓存，每一层需执行全归约操作，硬件成本随设备数量增长，是唯一能改善延迟的部署手段 |
| KV压缩（16/8/4-bit，保留比率0.25~1） | 缓存压缩方案 | 基于量化和驱逐在单GPU上原位缩减缓存空间，以小幅质量损失换取内存节省，会增加每令牌的延迟 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 在Llama-2 7B、70B模型及A100、A40、H100三种GPU的实验中，KV压缩的成本比张量并行低1.20x至2.00x；
  2. 80GB设备对应的策略边界约为36B参数（模型大小相对设备内存），模型大小低于该边界时KV压缩占优，额外GPU为不必要的开销；高于该边界时（如Llama-2 70B），张量并行是必要入场券，因为KV压缩不触及权重资源，Llama-2 70B在单A100上无法实现；
  3. 张量并行是唯一能改善部署延迟的手段，KV压缩是唯一能提升每美元对应容量的手段。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：该研究构建统一成本轴对比张量并行与KV压缩两种内存受限LLM serving的KV缓存耗尽解决方案，发现KV压缩成本更低、每美元容量提升更高，仅当模型大小超过80GB设备约36B参数时需采用张量并行，且张量并行是唯一可改善部署延迟的手段。

</details>

---

### 4. [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](https://arxiv.org/abs/2608.22140v1)

**Authors**: Jiaqian Zhu, Yang Zhang, Junhua Ding, Xiaowei Yu  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 82.5  
**Type**: new  
**ArXiv ID**: 2608.22140v1  

#### Abstract
Large Language Models (LLMs) achieve strong reasoning performance, but their robustness to realistic lexical corruption remains poorly understood. We evaluate four open-weight instruction-tuned models and frontier models across four reasoning benchmarks under keyboard noise, character swaps, and fil...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM具备较强推理性能，但对现实场景中词汇损坏的鲁棒性研究不足；现有推断策略仅针对单一损伤通道修复，无法应对词汇扰动引发的性能损失。

🚀 提出的新方法与思路
**Attention Diversion 机制分析**，该模块通过追踪键盘噪声、字符交换、填充插入三类词汇扰动下LLM的推理变化，发现子词分词碎片化会吸引不成比例的注意力质量，且token内容与注意力分配的耦合性是损伤难以修复的核心；具体通过在四类推理基准上评估四类模型，结合长度匹配控制实验、事实性干预实验验证上述机制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 鲁棒性机制揭示 | 明确词汇扰动损害LLM推理的核心机制（注意力转移），区分字符级扰动与填充插入的影响差异，通过长度匹配控制排除提示长度的干扰，填补现实词汇损坏下LLM鲁棒性研究的空白 |
| 修复失效解释 | 揭示现有单通道修复策略（仅处理内容或注意力）失效的根本原因，为优化LLM鲁棒性提供了理论依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体数据集名称 | 评估四类模型在键盘噪声、字符交换、填充插入三类词汇扰动下的推理性能 |

🎯 实验设置与评估指标
任务为LLM推理性能评估，评估指标为准确率（accuracy），越高越好。
| 指标 | 含义 |
| ---- | ---- |
| accuracy | LLM推理准确率，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| chain-of-thought prompting | 推断策略 | 针对推理过程的中间步骤优化 |
| spell-checking | 推断策略 | 文本拼写错误修复 |
| self-repair | 推断策略 | 模型自我修正扰动损伤 |
| stronger repair models | 推断策略 | 采用更强修复模型处理扰动 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**鲁棒性/扰动测试（场景：词汇扰动对LLM推理的影响）**
论文未报告具体表号及定量数值，根据摘要可知：字符级扰动会显著降低LLM推理准确率，尤其多步骤推理任务受影响更严重；填充插入对推理性能几乎无影响。
💡 结论：字符级词汇扰动对LLM推理性能的损害远大于填充插入，且对多步骤推理的负面影响更显著。

**长度匹配控制实验（场景：排除提示长度的干扰）**
论文未报告具体表号及定量数值，根据摘要可知：长度匹配控制实验证实，子词分词碎片化而非提示长度是导致推理性能下降的原因。
💡 结论：词汇扰动引发的推理损失源于子词分词碎片化，与提示长度无关。

**消融实验（场景：token内容与注意力分配耦合的影响）**
论文未报告具体表号及定量数值，根据摘要可知：单独恢复token内容或注意力分配均无法有效恢复性能：仅恢复内容性能不足，恢复干净注意力但内容受损会加剧性能下降，同时恢复两者可恢复大部分性能差距。
💡 结论：token内容与注意力分配的耦合性是扰动损伤难以修复的核心原因。

**现有推断策略性能恢复实验（场景：Inference-time策略对扰动损伤的修复效果）**
论文未报告具体表号及定量数值，根据摘要可知：chain-of-thought prompting、spell-checking、self-repair、stronger repair models等现有推断策略，均无法一致恢复扰动下的LLM推理性能。
💡 结论：现有仅针对单一通道修复的推断策略无法有效缓解注意力转移带来的性能损失。

4. 关键结论和发现
- 主要发现：1）词汇扰动通过子词分词碎片化引发注意力转移，字符级扰动对LLM推理性能的损害远大于填充插入，且多步骤推理任务受影响更严重；2）token内容与注意力分配存在耦合性，两者共同受损是扰动损伤难以修复的核心原因；3）现有仅针对单一通道修复的推断策略无法有效缓解注意力转移导致的性能损失。
- 方法局限性：论文未报告具体模型性能数据、各扰动类型的定量影响数值、不同推理基准的性能差异等细节，无法全面评估方法的泛化性与有效性。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该实证研究揭示了词汇扰动引发LLM推理性能下降的核心机制，明确了现有修复策略的失效原因，为优化LLM对现实词汇损坏的鲁棒性提供了重要理论依据。

</details>

---

### 5. [CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](https://arxiv.org/abs/2608.23172v1)

**Authors**: Abhilash Nandy, Rahul Seetharaman, Aman Bansal, Rounak Saha, Manav Nitin Kapadnis, Millon Madhur Das, Pawan Goyal, Niloy Ganguly  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 73.5  
**Type**: new  
**ArXiv ID**: 2608.23172v1  

#### Abstract
Large-scale vision-language models (VLMs) have demonstrated remarkable versatility across a wide range of multimodal tasks. However, understanding humor remains challenging because humorous content often depends on subtle interactions among entities, events, context, and implicit relationships acros...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension
1. 论文的主要贡献和创新点
✅ 解决的问题
传统大型视觉语言模型（VLMs）在多模态幽默理解任务上存在局限：幽默内容依赖图像与文本模态间实体、事件、上下文及隐式关系的微妙互动，这类复杂推理链难以通过常规提示或线性Chain-of-Thought推理有效捕捉。

🚀 提出的新方法与思路
**CaRGo-T (Causal Reasoning Graph-of-Thought)**：该推理框架将多模态幽默背后的因果与上下文关系表示为轻量型基于图的推理结构，图被序列化为VLM生成的代码类表示，可被相同或不同VLM解释，以在零样本或上下文学习设置中生成最终预测。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态推理建模 | 采用轻量型图结构，替代常规线性推理或传统提示，有效捕捉跨模态因果与上下文关系 |
| 目标信息相关性 | 生成的推理表示包含更多与任务目标输出相关的信息 |
| 任务性能表现 | 幽默理解任务约提升1-20%，幽默检测任务约提升1-3%，优于现有基于推理的基线方法 |
| 适用场景 | 支持零样本或上下文学习设置，可适配相同或不同VLM |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 涵盖讽刺、反讽、梗图等多种喜剧形式的四个数据集 | 用于幽默理解、幽默检测两个任务的评估 |

🎯 实验设置与评估指标
任务为幽默理解、幽默检测多模态任务，评估指标论文未明确说明具体名称及含义。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确说明评估指标的具体名称及含义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有基于推理的基线方法 | 未明确 | 未明确 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**
论文未报告对应结果的表号、图号等定位信息，仅提及CaRGo-T相比现有推理基线方法，在幽默理解任务上实现约1-20%的性能提升，在幽默检测任务上实现约1-3%的性能提升。
💡 结论：CaRGo-T框架可在多模态幽默相关任务上获得优于现有推理基线方法的性能。

效率对比：论文未报告
跨域/zero-shot迁移：论文未报告具体结果，仅提及框架支持零样本或上下文学习设置
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：①CaRGo-T是针对多模态幽默理解的有效框架，可提升幽默理解与幽默检测任务的性能；②该框架生成的推理表示相比基线方法，包含更多与任务目标相关的信息；③框架支持零样本或上下文学习，可适配不同VLM。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CaRGo-T是一种基于因果推理图结构的多模态幽默理解框架，通过建模跨模态的因果与上下文关系，有效捕捉多模态幽默的复杂互动，实现了幽默理解与检测任务的性能提升，并生成了更具目标相关性的推理表示。

</details>

---

### 6. [WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration and Exploitation](https://arxiv.org/abs/2608.24479v1)

**Authors**: Zihao Wu, Hongyao Tang, Yi Ma, Huizhong Song, Pengyi Li, Yifu Yuan, Fei Ni, Jinyi Liu, Wei Wei, Jianrong Wang, Yan Zheng, Jianye Hao  
**Category**: cs.LG  
**Published**: 2026-08-26  
**Score**: 58.5  
**Type**: new  
**ArXiv ID**: 2608.24479v1  

#### Abstract
Massively parallel simulation changes the data regime in which off-policy reinforcement learning (RL) is trained, challenging stabilizers designed for data-limited replay. Through controlled experiments across eight benchmark families, we show that these stabilizers are data-regime-dependent: parame...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration and Exploitation
1. 论文的主要贡献和创新点
✅ 解决的问题
大规模并行模拟改变了离线强化学习的数据集特征，原有针对数据受限回放设计的稳定器不再适配当前数据 regime，具体缺陷包括：参数归一化在数据丰富时会限制值拟合；clipped double-Q在高吞吐量操作中可被过度保守应用；单一回放加权机制无法适配不同数据规模的场景。

🚀 提出的新方法与思路
**WarpSAC： regime-aware 离线强化学习算法族**，基于受控实验发现设计，核心逻辑为：使用Sample Weight Decay实现高效利用；提供两种适配不同数据 regime的变体：WarpSAC-L（参数归一化开启、带clipped double-Q）用于数据受限的CPU-scale训练，WarpSAC-A（参数归一化关闭、单Q网络）用于数据丰富的GPU并行训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 归一化分数-步AUC提升 | 较FlashSAC在九个CPU-scale环境提升4.5%，在14个GPU-parallel环境提升23.1% |
| UnitreeG1TransportBox-v1任务性能 | 成功率从19.8%提升至96.4% |
| MuJoCo Playground性能 | 标准化 wall-time AUC提升19.1% |
| sim-to-real部署效率 | 相比FlashSAC部署速度提升36.4% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 八个基准族 | 验证不同数据 regime下算法的核心性能 |
| 九个CPU-scale环境 | 测试数据受限场景下算法表现 |
| 14个GPU-parallel环境 | 测试数据丰富场景下算法表现 |
| MuJoCo Playground | 测试算法的 wall-time 性能 |
| UnitreeG1TransportBox-v1任务 | 测试算法的实际控制任务性能 |

🎯 实验设置与评估指标
实验任务为离线强化学习在CPU数据受限、GPU数据丰富两种 regime下的性能、效率及sim-to-real部署测试；具体指标：
| 指标 | 含义 |
| ---- | ---- |
| 归一化分数-步AUC | 越高越好 |
| 任务成功率 | 越高越好 |
| 标准化 wall-time AUC | 越高越好 |
| sim-to-real部署速度 | 越快越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| FlashSAC | 离线RL算法（基线） | 用于与WarpSAC对比的基准算法，适配传统离线RL场景 |
| 传统数据受限适配的离线RL稳定器 | 离线RL模块 | 针对数据受限回放设计，不适应数据丰富场景 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（论文未提供表号）**
| 结果内容 | 数值 |
| ---- | ---- |
| CPU-scale环境归一化分数-步AUC提升 | 4.5% ✅ |
| GPU-parallel环境归一化分数-步AUC提升 | 23.1% ✅ |
| UnitreeG1TransportBox-v1任务成功率提升 | 从19.8%升至96.4% ✅ |
| MuJoCo Playground标准化 wall-time AUC提升 | 19.1% ✅ |

💡 结论：WarpSAC在CPU、GPU两类数据 regime下的核心基准性能均显著优于基线FlashSAC，适配不同数据规模的机制有效。

- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 离线RL的稳定器具有数据 regime 依赖性：参数归一化适配数据受限回放覆盖，但数据丰富时会限制值拟合；clipped double-Q在高吞吐量操作中可放松适用；Age-biased replay weighting在各 regime（尤其有限网络容量时）可提升学习效率。2. 针对不同数据 regime设计差异化的稳定器及算法变体，是提升可扩展离线RL性能的有效路径。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：WarpSAC是基于离线RL数据 regime特性设计的可扩展算法族，通过CPU/GPU场景的差异化适配，在多基准测试及sim-to-real部署中显著优于基线FlashSAC。

</details>

---

### 7. [Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention](https://arxiv.org/abs/2608.23834v1)

**Authors**: Sergii Kozyrev (Minima AI, Inc), Davyd Maiboroda (Minima AI, Inc)  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2608.23834v1  

#### Abstract
The key-value (KV) cache is a primary capacity and bandwidth bottleneck in long-context LLM serving. We present Minima-KV, a retention-preserving hierarchy for mixed-format paged attention. Recent and protected Anchor pages remain in FP8, while older non-anchor pages move to packed TQ3; every live-r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
KV缓存是长上下文LLM服务部署中的核心容量与带宽瓶颈；现有部分方法存在需cache尺寸密集影子缓存、压缩后性能下降等缺陷。
🚀 提出的新方法与思路
**Minima-KV混合格式分页注意力架构**：近期受保护的Anchor页保持FP8格式，旧非Anchor页转为packed TQ3格式，确保每个活跃请求页均可寻址；采用格式特定内核计算部分注意力状态，通过全局归一化online-softmax合并，无需cache尺寸密集影子，实现直接异构解码。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV缓存压缩比 | 相对BF16压缩3.50x，相对FP8压缩1.75x |
| 长上下文任务性能 | 16K RULER任务注意力质量匹配密集控制，LongBench v2性能偏差极小 |
| 内存开销 | 无需cache尺寸密集影子缓存，降低额外存储需求 |
| 解码吞吐量 | 单双请求场景下吞吐量损失极小 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RULER | 16K needle-in-a-haystack任务的注意力质量评估 |
| LongBench v2 | 503问长上下文性能评估 |
| 双请求直接解码测试集（2个59008-token请求） | 长双请求场景的压缩与吞吐量测试 |
| 其余数据集 | 论文未报告 |
🎯 实验设置与评估指标
任务：长上下文LLM部署中KV缓存压缩的质量、存储与性能评估。
| 指标 | 含义 | 趋势 |
| --- | --- | --- |
| 注意力KV per 活令牌 | 每个活令牌占用的注意力缓存量 | ↓ 越小越好 |
| LongBench v2性能偏差 | 与无压缩密集控制方法的性能差值 | ↓ 越低越好 |
| 活跃KV压缩比 | 活跃请求KV缓存的压缩倍数 | ↑ 越高越好 |
| 解码吞吐量 | 单位时间处理的请求量 | ↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| BF16基准 | 传统全精度KV缓存 | 性能优异但存储带宽需求大 |
| FP8基准 | 现有低精度KV缓存 | 存储需求低于BF16但未达Minima-KV压缩比 |
| 无压缩密集控制方法 | 参考基准 | 性能匹配Minima-KV但需cache尺寸密集影子 |
| 双请求直接解码控制方法 | 参考基准 | 用于长双请求场景的吞吐量对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Qwen3.6-27B单96GB NVIDIA RTX PRO 6000 Blackwell GPU部署性能（配置绑定）**
| 指标 | 值 | 最优情况 |
| --- | --- | --- |
| 注意力KV per 活令牌 | 18.3 KiB | ✅ 相对BF16压缩3.50x，相对FP8压缩1.75x |
| LongBench v2 16K上下文性能偏差 | -0.80个百分点 | - |
| LongBench v2 32K上下文性能偏差 | -0.60个百分点 | - |
| LongBench v2 64K上下文性能偏差 | -0.40个百分点 | ✅ 偏差最小 |
💡 结论：Minima-KV在Qwen3.6-27B模型上实现了较高的KV压缩率，同时在LongBench v2不同上下文长度下保持了较低的性能偏差。

**表2：59008-token双请求直接解码性能对比**
| 指标 | 值 | 对比基准表现 |
| --- | --- | --- |
| 活跃KV压缩比 | 3.625x | 无压缩控制方法 |
| 吞吐量 | 0.9821x | 无压缩控制方法 |
| 全注意力层覆盖率 | 100% | 无压缩控制方法 |
💡 结论：Minima-KV在长双请求场景下实现了更高的活跃KV压缩比，仅伴随极小的吞吐量损失，且能完整覆盖所有注意力层。

**表3：16K RULER needle-in-a-haystack任务注意力质量**
| 指标 | 结果 | 与密集控制方法对比 |
| --- | --- | --- |
| 注意力质量匹配度 | 无偏差 | 完全匹配密集控制性能 |
💡 结论：Minima-KV的注意力质量与无压缩的密集控制方法相当，满足长上下文任务的保留要求。

其余实验情况：
1. 主 benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① Minima-KV的混合格式Anchor/非Anchor KV缓存方案，无需密集影子缓存即可实现显著的KV压缩；② 在RULER、LongBench v2等长上下文基准任务上，Minima-KV性能损失极小，匹配无压缩密集控制的注意力质量；③ 长双请求场景下，Minima-KV压缩比更高，吞吐量仅略有下降。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Minima-KV通过混合格式的分页注意力KV缓存压缩方案，在保留长上下文注意力质量的同时，实现了显著的存储压缩，且无需cache尺寸的密集影子，为长上下文LLM部署提供了实用可行的路径。

</details>

---

### 8. [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](https://arxiv.org/abs/2608.24658v1)

**Authors**: Zhengyang Zhang, Zijian Zhang, Jiaxuan Gao, Shusheng Xu, Yi Wu, Song Han, Ligeng Zhu  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.24658v1  

#### Abstract
Scaling test-time reasoning has substantially improved the problem-solving ability of large language models (LLMs), but standard autoregressive decoding still executes long reasoning traces sequentially, creating severe latency for difficult tasks (up to days and weeks). Parallel reasoning offers a ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
标准自回归解码会将LLM的长推理链顺序执行，导致困难任务延迟极高（可达数天或数周）；现有并行推理系统仅关注子任务并行（分解任务为独立小块并行求解），忽略了另一种关键并行形式——试次并行（多个推测尝试并行探索、验证、聚合竞争假设），这是之前方法的核心缺陷。

🚀 提出的新方法与思路
**并行类型识别与分类**：明确划分LLM推理中的两种并行形式，通过分析确定试次并行是可并行化推理计算的重要组成，且在难题上占比更主导。
**顺序推理转结构化并行轨迹**：借助上下文无关文法，将顺序推理链转换为结构化的并行轨迹。
**PA-GRPO训练框架**：采用并行感知组相对策略优化（Parallelism-Aware Group Relative Policy Optimization, PA-GRPO）训练模型，奖励函数联合平衡准确率、延迟和两种并行性的比率。
**推理阶段并行执行**：推理时通过工具调用执行模型学到的并行结构，将理论上的并行节省转化为实际的墙钟级推理加速。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 并行覆盖范围 | 同时支持子任务并行与试次并行，弥补了现有并行推理仅关注子任务并行的缺陷 |
| 推理效率 | 实现实际的墙钟级加速，降低LLM推理延迟 |
| 性能保持 | 在加速推理的同时维持了竞争力的数学推理准确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AIME24 | 数学推理基准评估 |
| AIME25 | 数学推理基准评估 |

🎯 实验设置与评估指标
任务：在数学推理任务上评估本文方法的推理性能与效率。
| 指标 | 含义（箭头） |
| --- | --- |
| 平均加速度 | 衡量推理速度的提升倍数，↑ 越高越好 |
| 准确率 | 衡量数学推理的正确率，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准自回归解码 | 传统LLM推理方法 | 顺序执行推理链，延迟高，无并行支持 |
| 子任务并行推理系统 | 现有并行推理方法 | 仅支持子任务并行，忽略试次并行 |
| Parason | 本文提出方法 | 同时支持子任务与试次并行，采用PA-GRPO训练，推理时通过工具调用执行并行结构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主基准性能（数学推理）**
论文未报告
💡 结论：论文未报告

**表N：效率对比**
论文未报告
💡 结论：论文未报告

**表N：跨域/zero-shot迁移实验**
论文未报告
💡 结论：论文未报告

**表N：鲁棒性/扰动测试实验**
论文未报告
💡 结论：论文未报告

**表N：消融实验**
论文未报告
💡 结论：论文未报告

4. 关键结论和发现
- 主要发现：1. 试次并行是LLM推理中可并行化计算的重要并行形式，且在难题上占比更主导；2. 提出的Parason方法能实现LLM推理的实际墙钟加速，同时维持竞争力准确率；3. 基于PA-GRPO的训练框架可联合平衡准确率、延迟和并行性比率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的Parason方法通过识别并同时利用LLM推理中的子任务并行与试次并行，经PA-GRPO训练后，在AIME24和AIME25数学推理基准上实现了约1.7×的平均推理加速，同时保持了竞争力的准确率。

</details>

---

### 9. [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704v1)

**Authors**: Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.22704v1  

#### Abstract
Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs. Prefill-only KV compression methods permanently discard audio KV positions once evicted, with no pathway to recover them during decoding. We show this is fragile on long-form audio: prefill attention concentrates near ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题：长音频输入下，KV缓存是语音大模型的主要内存成本；仅预填充阶段的KV压缩方法会永久丢弃置换后的音频KV位置，解码阶段无法恢复，在长音频场景中表现脆弱；同时预填充注意力集中于音频开头（注意力汇效应）、解码注意力分布广泛且二者重要性排名重叠性弱，加剧了该类方法的失效问题。
🚀 提出的新方法与思路
**WnW (Waxing-and-Waning KV cache)**：通过离线校准将KV头分为anchor、tidal、fixed三类角色；Anchor头保留在GPU中作为解码时的重要性观测者；Tidal头保留CPU驻留的补充部分，基于聚合的anchor头得分分块召回；Fixed头仅保留GPU子集，其余永久丢弃。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 内存效率 | 仅在GPU保留20%的音频token，同时可实现接近全缓存的模型准确率 |
| 泛化性 | 结果可推广至不同语言、任务和领域 |
| 时间开销 | CPU-GPU召回带来的解码时间开销小 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LibriSpeech-Long | 评估各KV缓存优化方法的性能 |
🎯 实验设置与评估指标
任务为长语音相关的语音大模型任务；使用两个3B的backbone：Voxtral-mini-3b和Qwen2.5-Omni-3B；评估指标为模型准确率（越高越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 仅预填充KV压缩方法 | 基线方法 | 永久丢弃置换后的KV位置，解码阶段无法恢复，在长音频场景中易失效 |
| Full-Cache | 对照方法 | 完整保留所有KV缓存，无内存压缩，无提前失效风险 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**
论文未提供具体表号或定量数值，仅提及在LibriSpeech-Long数据集上，WnW保留近Full-Cache准确率，而预填充-only基线无法终止。
💡 结论：WnW可在长音频场景下实现接近全缓存的性能，解决了仅预填充压缩方法在长音频上失效的问题。
**效率对比（FPS / 参数量）**
论文未报告FPS、参数量的具体定量数据，仅说明CPU-GPU召回的解码时间开销小。
💡 结论：WnW的CPU-GPU召回机制带来的额外时间开销较低。
**跨域 / zero-shot 迁移**
论文未提供具体跨域/zero-shot迁移的定量数据，仅提及结果可推广至不同语言、任务和领域。
💡 结论：WnW的性能具有跨场景的泛化能力。
**鲁棒性 / 扰动测试**
论文未报告相关实验。
**消融实验**
论文未报告相关实验。
4. 关键结论和发现
- 主要发现：
  1. 长音频语音大模型中，预填充注意力存在集中于音频开头的注意力汇效应，解码注意力分布广泛，二者的KV重要性排名重叠性弱，导致仅预填充的KV压缩方法在长音频场景中失效。
  2. WnW通过分类KV头为anchor、tidal、fixed三类角色，平衡了内存占用与模型性能，仅在GPU上保留20%的音频token即可实现接近全缓存的精度。
  3. WnW的CPU-GPU召回机制带来的解码时间开销小，且性能可推广至不同语言、任务和领域。
- 方法局限性：论文未报告方法的局限性。
- 未来工作：论文未报告未来工作方向。

> ✅ 总结一句话：WnW是针对长语音大模型设计的KV缓存优化方法，通过分类KV头角色平衡内存占用与性能，在长音频场景下实现近全缓存的精度，且具有良好的跨场景泛化性与低额外开销。

</details>

---

### 10. [Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models](https://arxiv.org/abs/2608.22312v1)

**Authors**: Wenyun Li, Guiping Cao, Xiangyuan Lan, Zheng Zhang  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.22312v1  

#### Abstract
Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal represen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
MLLMs安全对齐存在漏洞，文本空间学习的安全行为无法可靠迁移到融合后的跨模态表示，导致多模态输入可通过潜在语义线索被利用。
🚀 提出的新方法与思路
**Text-Anchored Semantic Perturbation Attack (TA-SPA)**：一种黑盒jailbreak攻击框架，核心是在文本锚定的语义空间中优化可迁移扰动，包含两个核心模块。
**Text-Anchored Semantic Factorization (TASF)**：TA-SPA的组成模块，作用是鼓励跨模态语义因子与模态特定残差分离。
**Semantic-Preserving Augmentation (SPA)**：TA-SPA的组成模块，作用是在保持语义一致性的前提下多样化有害目标锚点。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 攻击类型 | 黑盒攻击框架 |
| 攻击效果 | 具备强攻击有效性 |
| 可迁移性 | 攻击可迁移至商用MLLMs |
| 防御鲁棒性 | 在代表性防御下表现有竞争力 |
2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
任务：MLLM的可迁移jailbreak攻击；指标：论文未报告
⚔️ 基线方法对比
论文未报告
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（场景）**
论文未报告
💡 结论：论文未报告
**表2：效率对比（场景）**
论文未报告
💡 结论：论文未报告
**表3：跨域/zero-shot迁移（场景）**
论文未报告
💡 结论：论文未报告
**表4：鲁棒性/扰动测试（场景）**
论文未报告
💡 结论：论文未报告
**表5：消融实验（场景）**
论文未报告
💡 结论：论文未报告
4. 关键结论和发现
- 主要发现：1. MLLMs的跨模态融合表征存在安全漏洞，文本空间的安全行为无法可靠迁移，可通过潜在语义线索发起jailbreak攻击；2. TA-SPA框架具备强攻击有效性和跨商用MLLMs的可迁移性，在代表性防御下表现有竞争力；3. TASF模块实现了预期的语义因子分解，但未达到完全解耦的效果。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：本文提出TA-SPA黑盒攻击框架，通过TASF和SPA模块优化文本锚定语义空间的可迁移扰动，实现对商用MLLMs的有效可迁移jailbreak攻击，且在代表性防御下表现有竞争力，为表征层面安全对齐提供了研究动机。

</details>

---

### 11. [EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21946v1)

**Authors**: Can Xie, Yuyi Zhou, Wen Yang, Ziyi zhang, Siyao Song, Yingzhuo Deng, Shuo Ren, Jiajun Zhang  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.21946v1  

#### Abstract
Reinforcement learning with outcome-based objectives such as GRPO enables LLM-based agents to solve complex, long-horizon tasks, yet the reusable exploration patterns embedded in interaction trajectories are largely discarded after a single policy update. Existing experience-augmented approaches ret...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有基于结果目标的强化学习方法（如GRPO）可使LLM智能体解决复杂长视距任务，但交互轨迹中的可重用探索模式在单次策略更新后即被丢弃；
- 现有经验增强方法在推理时检索历史指导，却未考虑策略的演化能力，还会产生对外部检索的持续依赖。

🚀 提出的新方法与思路
**EDGE框架**：将检索到的经验视为训练时的临时支架，逐步将其收益内化到参数化策略中。具体操作包括：将每个rollout组划分为经验条件与经验自由的轨迹，仅估计并接纳轨迹带来的正边际收益（无需额外采样）；通过反KL目标，将上述诱导的行为蒸馏至基础策略的经验支持中。
**协同演化的经验库**：随策略演化，综合新出现的失败模式的指导信息，同时修剪经验库中的过时条目。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 经验利用方式 | 将经验从推理时的外部检索转为训练时的策略内化，无需依赖外部检索 |
| 策略适配性 | 考虑策略的演化能力，仅接纳正边际收益，避免对策略产生负向影响 |
| 推理性能保留 | 移除外部经验后仍能保留脚手架的性能 |
| 任务表现 | 在指定基准任务上优于基线方法GRPO |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| ALFWorld | 用于测试智能体任务解决能力的基准环境 |
| WebShop | 用于测试智能体任务解决能力的基准环境 |

🎯 实验设置与评估指标
任务说明：在ALFWorld和WebShop基准环境中测试LLM智能体的任务解决性能。
| 指标 | 含义（箭头） |
|------|------------|
| 任务成功率 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| GRPO | 基线强化学习方法 | 基于结果目标的LLM智能体强化学习方法 |
| EDGE | 本文提出的方法 | 经验蒸馏引导探索的强化学习框架 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（场景：ALFWorld、WebShop）**
论文未报告对应表号的具体数值，仅提及EDGE在7B模型规模下于上述任务上相比GRPO性能更优，推理时移除外部经验仍保留脚手架性能的大部分。
💡 结论：EDGE在ALFWorld和WebShop任务上相比基线方法GRPO有性能提升，且推理时对外部经验的依赖较低。
**效率对比**：论文未报告
**跨域/zero-shot迁移**：论文未报告
**鲁棒性/扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：EDGE框架可有效将检索到的经验内化至参数化策略，解决了现有经验增强方法对外部检索的依赖问题，同时避免了未考虑策略演化的缺陷；EDGE在ALFWorld和WebShop基准任务上相比GRPO实现了性能提升；EDGE推理时对外部经验的依赖程度较低，移除外部经验后仍能保留大部分性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：EDGE是一种经验蒸馏引导智能体强化学习探索的框架，通过将训练时检索的经验内化至参数化策略，解决了现有经验增强方法依赖外部检索且未适配策略演化的问题，在ALFWorld和WebShop基准任务上相比GRPO实现了更优性能，且推理时对外部经验的依赖较低。

</details>

---

### 12. [Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching](https://arxiv.org/abs/2608.22332v1)

**Authors**: Murat Dura, Serkan \"Ozt\"urk, Selma Tekir  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.22332v1  

#### Abstract
Large Language Models (LLMs) demonstrate remarkable problem-solving capabilities when guided by Chain-of-Thought (CoT) prompting, yet the internal mechanisms underlying these improvements remain poorly understood. In this work, we investigate where CoT-related causal effects emerge across the genera...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有研究对Chain-of-Thought（CoT）提升LLM问题解决能力的内部机制（尤其是因果效应在推理轨迹中的分布）理解不足；
2. 传统的单静态token位置激活patching方法无法表征CoT推理中跨token的时间分布效应。

🚀 提出的新方法与思路
**Sequential Activation Patching框架**：追踪CoT条件下的注意力头激活跨token位置，采用词性（Part-of-Speech）引导的分析来聚合激活效应。
**Sequential Multi-Head Patching**：用于评估分布式注意力头集的联合贡献，同时结合跨问题和随机激活控制手段验证识别结果的可靠性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 时间分布效应表征 | 可刻画CoT推理中跨token位置的时间分布因果效应，弥补传统静态单token方法的缺陷 |
| 注意力头联合贡献评估 | 支持评估分布式注意力头集在CoT推理中的联合作用，更贴合CoT的分布式特性 |
| 激活效应聚合 | 通过词性引导的分析实现跨token激活效应的有效聚合，提升分析的针对性 |
| 因果性验证 | 结合跨问题和随机激活控制，增强识别的注意力头功能重要性的验证可信度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：分析Chain-of-Thought推理的内部机制，识别对最终答案计算有贡献的注意力头
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：
无对应表号，实验设置为对识别出的注意力头进行零消融；结果显示该类头对成功生成答案具有功能重要性，且涉及推理轨迹维护、答案锚定、示例-目标分离、数值生成等多种重叠机制。
💡 结论：识别出的注意力头在CoT推理及最终答案生成中发挥关键作用，对应存在多种与CoT相关的核心机制。

4. 关键结论和发现
- 主要发现
  1. CoT相关的因果效应呈现分布式特征，跨越推理轨迹的多个token位置；
  2. 与CoT计算相关的注意力头参与推理轨迹维护、答案锚定、示例-目标分离、数值生成等多种关键机制；
  3. LLM中存在支持CoT推理的分布式推理子电路。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出Sequential Activation Patching框架与Sequential Multi-Head Patching方法，弥补了传统静态激活patching无法表征CoT时间分布效应的缺陷，揭示了CoT推理的分布式注意力机制及相关子电路，为LLM中CoT的机制可解释性提供了新思路。

</details>

---

### 13. [GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding](https://arxiv.org/abs/2608.21832v1)

**Authors**: Md Abrar Jahin, Md Rizwan Parvez  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2608.21832v1  

#### Abstract
Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding

1. 论文的主要贡献和创新点
✅ 解决的问题
现有GUI grounding基准无法隔离视觉语言模型是否将关系语言绑定到正确元素，无法诊断空间推理失败；多数视觉语言模型在该任务上表现有限，多数预测偏离指定候选区域，失败根源未被明确区分。

🚀 提出的新方法与思路
**GUI-Primitives基准**：构建含7种空间关系（左/右、上/下、包含、对齐、邻近、列表序号、遮挡）的994项对比指令对，固定截图和锚点，改变关系表达式使正确目标在两个指定候选间移动；验证196项子集（5名注释者，well-formedness κ=0.94，target selection κ=0.79）；分类预测所属候选区域，区分失败源于候选定位还是关系理解；提出标记两个指定候选的oracle诊断方法以提升选择准确率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 基准设计 | 对比指令对固定截图和锚点，精准隔离空间推理失败的根源 |
| 诊断能力 | 区分预测落在候选区域内外，明确不同空间关系的推理难度差异 |
| 性能评估 | 提供基于候选区域分类的表现分析，定位任务瓶颈 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GUI-Primitives | 视觉语言GUI grounding任务的空间推理诊断基准，含994项对比指令对，覆盖7种空间关系 |

🎯 实验设置与评估指标
任务：视觉语言模型将自然语言指令与GUI截图中的界面元素匹配定位
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 严格点在框准确率 | 越高越好 |
| 条件目标选择准确率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 19种视觉语言模型 | 待评估模型 | 测试GUI grounding任务的空间推理表现 |
| ScreenSpot-Pro | 探索性基准方法 | 与GUI-Primitives基准准确率存在关联 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**
论文未报告对应表号，无法提供精确定量数值；论文提及19个视觉语言模型的严格点在框准确率表现有限、部分预测偏离候选区域、不同关系下目标选择表现存在差异、与ScreenSpot-Pro准确率存在关联及标记候选可提升选择准确率，但未明确具体数值。
💡 结论：GUI-Primitives可有效诊断视觉语言模型在GUI grounding中的空间推理失败，多数失败源于候选定位而非关系理解，标记候选的oracle方法仅为诊断手段，不可部署。

效率对比：论文未报告
跨域 / zero-shot 迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 视觉语言模型在GUI grounding的空间推理任务中表现有限，失败多源于候选定位而非关系理解；
- GUI-Primitives基准中，不同空间关系的推理难度不同，部分关系（如包含、遮挡）下表现较差；
- 基准准确率与ScreenSpot-Pro准确率存在关联，标记指定候选可大幅提升目标选择准确率但为oracle诊断方法，无法实际部署。

方法局限性：仅为诊断基准，未提供可部署的空间推理解决方法；未报告效率、跨域迁移、鲁棒性等测试结果。

未来工作：开发针对难推理关系的GUI grounding方法；拓展GUI-Primitives基准以支持更多场景和关系类型。

> ✅ **总结一句话**：论文提出的GUI-Primitives基准有效诊断了视觉语言模型在GUI grounding任务中的空间推理失败，揭示多数失败源于候选定位而非关系理解，标记候选的oracle方法可提升目标选择准确率但不可部署。

</details>

---

### 14. [Recursive Agentic Reasoning](https://arxiv.org/abs/2608.23956v1)

**Authors**: Shengxin Zhang, Xiaomin Wu, Xiyang Wu, Jing Xie  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.23956v1  

#### Abstract
Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an ag...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Recursive Agentic Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有测试时推理方法（如迭代细化、分解、重复采样）被孤立评估，导致跨模型、基准、评估管线的性能增益难以比较；不同方法均存在无法横向对比的缺陷。

🚀 提出的新方法与思路
**Recursive Agentic Reasoning Framework**：将测试时推理方法统一为智能体推理轨迹上的三类递归算子，实现多方法的公平对比：
- **GROW**：加深单一推理路径；
- **PRUNE**：分解并重组问题；
- **BRANCH**：采样可选推理路径并从中选择。
采用共享的评估harness，确保所有方法使用相同提示、token预算、 grading代码消除评估干扰。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估公平性 | 统一评估harness消除了不同管线的干扰，支持跨模型、基准的横向对比 |
| 性能表现 | BRANCH算子在多数场景持续优于GROW、PRUNE算子 |
| 鲁棒性 | BRANCH可恢复输出预算耗尽等场景的性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个基准 | 用于测试三类递归算子及单遍链式思考基线的性能 |

🎯 实验设置与评估指标
任务为测试时推理问答任务，评估指标为准确率（↑越高越好）。
| 指标 | 含义 |
| --- | --- |
| 准确率 | 模型推理结果的正确比例，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- |
| Single-pass chain-of-thought | 基准方法 | 仅执行单遍推理，无递归算子参与 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号、图号，相关定量结果仅在摘要中提及：
- 在14个模型-基准设置中，BRANCH算子准确率平均提升5.98个百分点，且是12个设置的最佳算子；
- GROW算子平均提升2.18个百分点，在2个设置中出现性能下降；
- PRUNE算子平均提升0.94个百分点；
- BRANCH的增益与基准阶段空输出、预算耗尽输出率呈正相关（r=0.72）。

💡 结论：BRANCH算子在多模型-基准设置中展现出稳定的性能优势，其优势源于多路径探索及错误恢复能力。

4. 关键结论和发现
- 主要发现：① 统一评估框架下，BRANCH算子在所有14个模型-基准设置中性能优于基线，且持续优于GROW、PRUNE算子；② BRANCH的优势不仅在于多路径探索，还可恢复输出预算耗尽的场景；③ 配对评分相较于未配对评估，能改变甚至反转测试时计算的比较结论，应作为标准评估协议。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了统一的递归测试时推理算子框架，通过公平对比验证BRANCH算子在多基准与模型上的性能优势，强调配对评分对测试时计算评估的必要性。

</details>

---

### 15. [PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos](https://arxiv.org/abs/2608.24574v1)

**Authors**: Siyao Yan, Bo Han, Jisheng Dang, Bimei Wang, Shude Wang, Hong Peng, Yulan Guo, Jianhuang Lai, Bin Hu,  Tat-SengChua  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.24574v1  

#### Abstract
Video multimodal large language models support language guided video segmentation, but they often show spatio temporal inconsistencies, e.g., jitter, drift, and identity switches. These failures are more common when targets are partly hidden or when similar objects appear nearby.One likely reason is...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Video MLLMs在语言引导的视频分割中存在时空不一致问题（抖动、漂移、身份切换），该问题在目标部分被遮挡或附近有相似物体时更突出；核心原因是当前模型训练缺乏显式空间先验，难以随时间维持稳定的空间身份和形状。
🚀 提出的新方法与思路
**PhysMLLMs**：一种训练阶段的先验注入架构，用于为Video MLLMs注入物理启发的空间连续性先验；
**Global Representation Prior Alignment (REPA-Global)**：核心机制，通过离线嵌入缓存和计划蒸馏方案，从冻结的DINOv2教师模型蒸馏全局视觉表示，使学生模型的全局视觉表示与教师模型对齐；该设计保持推理过程不变，不增加推理时间成本。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 视频分割性能 | 提升视频分割掩码质量和跨帧一致性 |
| 推理效率 | 不增加推理时间成本，保持推理过程不变 |
| 单帧图像级定位性能 | 维持可比性能 |
| 通用多模态能力 | 维持可比性能 |
| 挑战性场景表现 | 在小目标、快速运动、遮挡、干扰项、推理查询等挑战性场景中获得更大增益 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未明确报告具体数据集名称 | 用于视频分割性能、单帧Referring图像分割性能及通用多模态性能的评估 |
🎯 实验设置与评估指标
语言引导的视频分割、referring图像分割及通用多模态性能评估
| 指标 | 含义（箭头） |
| --- | --- |
| 论文未明确报告具体指标名称 | 评估视频分割掩码质量、跨帧一致性、单帧referring分割性能、通用VLM性能及挑战性场景性能 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有Video MLLMs | 视频多模态大语言模型 | 存在时空不一致问题，训练缺乏显式空间先验，易在视频分割时出现抖动、漂移、身份切换等问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. 注入物理启发的空间连续性先验（通过REPA-Global机制）可有效提升Video MLLMs的视频分割掩码质量与跨帧一致性，且在小目标、快速运动、遮挡等挑战性场景中增益更显著；2. 该先验注入方法不会损害模型的单帧图像级定位能力及通用多模态性能
- 方法局限性：论文未明确报告
- 未来工作：论文未提及

> ✅ **总结一句话**：PhysMLLMs通过训练阶段注入物理启发的空间连续性先验（REPA-Global机制），在保持推理时间不变且不牺牲单帧/通用多模态能力的前提下，有效提升了视频多模态大语言模型的视频分割质量与跨帧一致性，尤其适配挑战性场景。

</details>

---

### 16. [PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression](https://arxiv.org/abs/2608.23843v1)

**Authors**: Zizhong Wang, Jieying Wang, Zhao Zhang, Jiajia Li  
**Category**: cs.LG  
**Published**: 2026-08-26  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.23843v1  

#### Abstract
Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache. KV cache compression addresses this problem by reducing the storage cost of previous tokens. Among existing approaches, low-rank compression is particularly attractive ...

---

### 17. [Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core](https://arxiv.org/abs/2608.24810v1)

**Authors**: Yogesh Kumar  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.24810v1  

#### Abstract
Recent work has applied Mamba style state space models (SSMs) to video anomaly detection, yet existing approaches still rely on buffering clips or windows internally, lack a theoretical account of how temporal memory relates to detection latency, and benchmark efficiency only through GPU throughput ...

---

### 18. [Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models](https://arxiv.org/abs/2608.22753v1)

**Authors**: Bohan Yu, Pengfei Cao, Chen Han, Chenxi Zhou, Zhiheng Zhang, Zhiyang Xie, Wenhao Teng, Xiangwen Liao, Jun Zhao, Kang Liu  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.22753v1  

#### Abstract
Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale. To evaluate this capability, we introduce RuleWorld, a large-scale benchmark that reformulates rules as globally reusable abstra...

---

### 19. [HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning](https://arxiv.org/abs/2608.21863v1)

**Authors**: Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, Wei Lin, Guojun Yin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.21863v1  

#### Abstract
Tool-Integrated Reasoning (TIR) is a fundamental capability for LLM agents to solve complex tasks by interacting with external tools iteratively. Reinforcement Learning (RL) has become the dominant paradigm for enabling this capability. However, existing approaches typically assign uniform trajector...

---

### 20. [The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning](https://arxiv.org/abs/2608.21871v1)

**Authors**: Jing Yu, Shengchao Chen, Yiyun Tan  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.21871v1  

#### Abstract
Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejectin...

---

### 21. [Knowing Isn't Always Saying: When Do Spatial Encodings Reach Answers in Vision-Language Models?](https://arxiv.org/abs/2608.22916v1)

**Authors**: Zeyu Wang, Xinming Xu  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.22916v1  

#### Abstract
Vision-language models are known to encode spatial information in their hidden states, yet often fail to use it when answering. However, it remains unclear when and where this encoded information reaches the answer. We address this with direction patching, a class-conditioned causal intervention app...

---

### 22. [Semantic Reasoning Denoising: Correcting Language Model Reasoning with Semantic Operators](https://arxiv.org/abs/2608.22090v1)

**Authors**: Yujiao Yang  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.22090v1  

#### Abstract
Large language models can produce fluent reasoning traces whose local semantic errors propagate to an incorrect conclusion, while unconstrained self-correction may preserve, amplify, or introduce errors. Existing diffusion language models provide iterative refinement, but usually define noise as tok...

---

### 23. [L\\"etzCross: A Cross-Lingual Page-Level Benchmark for Multimodal Retrieval over Luxembourgish Documents](https://arxiv.org/abs/2608.21714v1)

**Authors**: Omar El Bachyr, Fred Philippy, Laura Maria Bernardy, Saad Ezzini, Jacques Klein, Tegawende Bissyande  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2608.21714v1  

#### Abstract
Recent page-image retrievers such as ColPali have improved retrieval over visually rich documents, yet little is known about how they behave in cross-lingual, low-resource settings. We introduce L\"etzCross, a benchmark for cross-lingual page-level retrieval over Luxembourgish PDF documents, with do...

---

### 24. [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](https://arxiv.org/abs/2608.24041v1)

**Authors**: Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang,  Shoushan, Guodong Zhou  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.24041v1  

#### Abstract
Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively t...

---

### 25. [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571v1)

**Authors**: Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.24571v1  

#### Abstract
Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-creation systems patch this by prompting a frozen LLM at inference time, leaving the model that writes a tool decoupled from the one that uses it, with no signal that the schemas it produces are schemas it...

---

### 26. [Mitigating Bias in Large Vision-Language Models via Counterfactual Ensemble Decoding](https://arxiv.org/abs/2608.21415v1)

**Authors**: Yisong Xiao, Aishan Liu, Yongxin Huang, Zonghao Ying, Shiji Zhao, Tianlin Li, Yong Han, Jian Yang, Xianglong Liu  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.21415v1  

#### Abstract
Large Vision-Language Models (LVLMs) have achieved remarkable performance across a wide range of tasks; however, they often inherit social biases from their training data, resulting in biased behavior when processing portraits from different social groups. Existing debiasing approaches typically com...

---

### 27. [Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction](https://arxiv.org/abs/2608.24001v1)

**Authors**: Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen, Keke Chen  
**Category**: cs.AI  
**Published**: 2026-08-26  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.24001v1  

#### Abstract
Large language models (LLMs) are increasingly used for future prediction, motivating the use of multiple models as a wisdom-of-the-crowd mechanism. However, simply increasing crowd size does not guarantee effective diversity, as different LLMs may exhibit redundant behaviors. We propose a behavior-a...

---

### 28. [SAVER: Selective Auditing of Verbal Evidence for Error Recovery in VLM Change Reasoning](https://arxiv.org/abs/2608.22857v1)

**Authors**: Youdi Li  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.22857v1  

#### Abstract
Vision-language models (VLMs) frequently fail at visual change reasoning, even when their vision encoders contain sufficient information. We observe that correct VLM outputs tend to contain explicit verbal evidence (object names, colors, spatial locations) that supports the claimed change, while inc...

---

### 29. [SeisMamba: Low-Latency Single-Station Seismic Magnitude Estimation for Spatially Distributed Earthquake Early Warning](https://arxiv.org/abs/2608.24561v1)

**Authors**: Quenton Yeo, Zhaoge Bi, Linghan Huang, Luke Stephen Higgins, Flora Salim, Huaming Chen  
**Category**: cs.LG  
**Published**: 2026-08-26  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.24561v1  

#### Abstract
Rapid earthquake magnitude estimation is central to earthquake early warning, yet many operational systems depend on dense regional seismic networks and region-specific calibration. This creates a spatial coverage barrier for high-risk areas with sparse sensing infrastructure. Single-station learnin...

---

### 30. [GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering](https://arxiv.org/abs/2608.22634v1)

**Authors**: Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib, Yordanos Tessema, Chang-Tien Lu  
**Category**: cs.CL  
**Published**: 2026-08-26  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.22634v1  

#### Abstract
Current work on improving reliability in large language model (LLM)- generated answers has primarily leveraged Retrieval-Augmented Generation (RAG), knowledge-graph augmentation, and reinforcement learning. While these methods are adept at enhancing and measuring reliability through semantic similar...

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
