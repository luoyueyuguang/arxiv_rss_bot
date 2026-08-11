# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-11 06:59:59 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097v1)

**Authors**: Can Xiao, Sukmin Cho, Junbong We, Zhixiong Niu, Jianyi Cheng, Yiren Zhao, Youngjin Kwon, Yongqiang Xiong, Rui Ma, Junyi Liu  
**Category**: cs.DC  
**Published**: 2026-08-11  
**Score**: 154.0  
**Type**: new  
**ArXiv ID**: 2608.08097v1  

#### Abstract
Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic during LLM token generation, i.e., decode. In p...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM推理服务受内存而非计算约束，长上下文/长形式推理工作负载普及后，KV缓存主导内存占用与流量，HBM容量稀缺，严重限制推理批大小和系统吞吐量。
🚀 提出的新方法与思路
**OasisKV系统**：基于vLLM实现，核心思路是将解码阶段的全KV缓存存储与HBM解耦，通过三大机制缓解HBM压力：1. 利用解码注意力的稀疏性，仅在HBM中保留最相关token的KV条目以用于注意力计算；2. 利用推测解码（SD）生成的前瞻token，精准预测未来重要token；3. 采用高效的注意力背景管道识别重要KV块，从更高容量内存层（如主机内存、远程内存）预取KV块并暂存到HBM，用于下一解码步骤。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| HBM容量压力 | 缓解HBM容量稀缺问题，支持更大推理批大小与更高系统吞吐量 |
| KV内存占用 | 论文未报告 |
| 推理吞吐量 | 论文未报告 |
| 精度损失 | 论文未报告 |
| 解码节点主机内存占用 | 论文未报告 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务：LLM推理服务（包含长上下文、长形式推理、预填-解码分离等场景）
| 指标 | 含义 |
| --- | --- |
| 精度 | 论文未报告 |
| 吞吐量 | 论文未报告 |
| KV内存占用 | 论文未报告 |
| 解码节点主机内存占用 | 论文未报告 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| dense vLLM | 基线方法 | 常规密集KV缓存的vLLM实现，未采用稀疏预取机制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告包含表号、图号的具体实验结果，故各实验小节如下：
**论文未报告：主benchmark性能（L2/碰撞率等）**
该实验未在论文中附带表号/图号，无有效结果数据。
**论文未报告：效率对比（FPS / 参数量）**
该实验未在论文中附带表号/图号，无有效结果数据。
**论文未报告：跨域 / zero-shot迁移**
该实验未在论文中附带表号/图号，无有效结果数据。
**论文未报告：鲁棒性 / 扰动测试**
该实验未在论文中附带表号/图号，无有效结果数据。
**论文未报告：消融实验**
该实验未在论文中附带表号/图号，无有效结果数据。

4. 关键结论和发现
- 核心思路：利用解码注意力稀疏性、推测解码前瞻特性，实现KV缓存跨内存层预取，有效缓解HBM容量压力；
- 论文未报告具体精度-吞吐量-内存的平衡关系的详细结论；
- 论文未报告方法的具体适用边界或特殊场景表现。
方法局限性：论文未报告方法的局限性相关内容。
未来工作：论文未报告未来工作相关内容。

> ✅ **总结一句话**：论文提出OasisKV系统，通过将解码KV缓存与HBM解耦，结合lookahead稀疏预取机制，缓解LLM推理服务中HBM容量稀缺的问题，为提升系统吞吐量提供了新方向。

</details>

---

### 2. [LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving](https://arxiv.org/abs/2608.08382v1)

**Authors**: Shuowei Jin, Xueshen Liu, Jiaxin Shan, Le Xu, Tieying Zhang, Liguang Xie, Z. Morley Mao  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 88.5  
**Type**: new  
**ArXiv ID**: 2608.08382v1  

#### Abstract
As LLM inference shifts to multi-tenant GPU clusters, co-batching improves throughput but obscures per-tenant usage and limits control. Enabling fractional sharing of the inference engine requires a real-time, per-request attribution primitive that is accurate and light enough to run inside the sche...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM推理转向多租户GPU集群时，协批处理提升了吞吐量，但会掩盖各租户的使用情况且限制了控制；实现推理引擎的分数共享需要一种实时、每请求的归因原语，要求准确且轻量，能在调度循环内运行，现有基线方法（token-count方法）无法满足该需求的精度和效率要求。

🚀 提出的新方法与思路
**LLMVisor**：一种屋顶线（roofline）引导的延迟归因模型，通过对与FLOPs和内存I/O流量成比例的特征进行分析，捕捉推理的内存绑定和计算绑定阶段，采用简洁的分段线性形式；该模型可将批处理延迟分解为累加的每请求份额，且能在微秒级高效运行，适配调度循环内的运行需求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 归因精度 | 对比token-count基线，达到接近完美的R²值 |
| 延迟归因误差 | 对比token-count基线，prefill和decode阶段的多百分位延迟归因误差显著降低 |
| 运行效率 | 具备微秒级运行的轻量性，可在调度循环内执行 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为多租户LLM服务场景下的延迟归因，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| R² | 衡量归因模型的拟合精度，越高越好 |
| 延迟归因相对误差（p90/p99） | 衡量不同百分位下的延迟归因误差，越低越好 |
| 运行耗时 | 衡量模型的运行效率，以微秒级为目标，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| LLMVisor | 提出的归因模型 | 屋顶线引导的分段线性模型，实时微秒级运行，支持每请求的延迟归因 |
| token-count基线 | 对比基线方法 | 基于token计数的延迟归因方法，精度和效率表现弱于LLMVisor |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验结果因未提供对应表号、图号或页码，故：论文未报告

💡 结论：论文在覆盖Llama 3.1-8B、Qwen 2.5-14B/32B模型，A100/H100 GPU硬件，不同张量并行度及工作负载组合的多租户LLM服务场景下，验证了LLMVisor的有效性，其性能优于token-count基线方法。

4. 关键结论和发现
- LLMVisor能实现接近完美的拟合度（R²），且可显著降低prefill和decode阶段不同百分位的延迟归因误差；
- LLMVisor是轻量型模型，可在微秒级高效运行，适配调度循环的执行要求；
- 论文的评估覆盖了不同规模的LLM模型、GPU硬件配置及多样化工作负载，验证了LLMVisor的适用性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出的LLMVisor是一种轻量、实时的屋顶线引导延迟归因模型，针对多租户LLM服务场景实现了高精度的每请求延迟归因，在性能上显著优于基于token计数的基线方法。

</details>

---

### 3. [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](https://arxiv.org/abs/2608.08326v1)

**Authors**: Yifan Li, Ruxin Sun, Tongzhou Zhao  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 86.0  
**Type**: new  
**ArXiv ID**: 2608.08326v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective approach for improving multimodal reasoning. However, most existing methods evaluate an entire response using a binary reward based only on final-answer correctness, thereby discarding the supervision available in inte...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning
## 1. 论文的主要贡献和创新点
✅ 解决的问题
现有RLVR（强化学习与可验证奖励）方法大多采用基于最终答案正确性的二元奖励，丢失中间推理步骤的有效监督信息；过程奖励模型通常依赖单独训练的验证器、昂贵的思维链标注或LLM在线判断，计算成本较高。

🚀 提出的新方法与思路
**Structured Step-Level Reward Alignment**：将生成的解决方案表示为推理步骤序列，通过轻量的数值、符号、词汇匹配规则与带过程标签的参考步骤对齐，聚合得到密集过程奖励，结合最终答案一致性和输出有效性奖励，经门控Group Relative Policy Optimization (GRPO)目标优化。
**Rollout Recycling for Complementary Supervision**：将策略rollouts回收用于响应比较和反射式自校正，避免策略更新后直接丢弃rollouts。
**Reflection-Oriented Training Instance Rewriting**：使用强LLM将采样的正确轨迹重写为面向反射的训练实例，增强策略的推理评估与优化能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 计算开销 | 无需额外学习验证器或外部LLM判断，大幅降低多模态强化学习的计算开销 |
| 监督信息利用 | 提供密集过程监督，不丢弃中间推理步骤的有效信息 |
| 组件依赖 | 无需单独训练的验证器或昂贵的思维链标注 |

## 2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

## 3. 主要实验结果和性能指标
📊 定量结果汇总：
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

## 4. 关键结论和发现
- 结构化过程监督与rollout回收结合，可实现高效的自改进多模态推理。
- 该方法无需额外学习验证器或外部LLM，有效降低多模态强化学习的计算开销。
- 论文未报告局限性、未来工作相关内容及具体实验结果数值。

> ✅ **总结一句话**：StructReward是一种计算高效的结构化过程奖励框架，通过对齐推理步骤、回收rollouts及重写面向反射的训练实例，实现带密集过程监督的自校正多模态推理，大幅降低多模态强化学习的计算开销。

</details>

---

### 4. [PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models](https://arxiv.org/abs/2608.09772v1)

**Authors**: Zhanna Mukhametsharip (Saarland University, Germany), Vera Demberg (Saarland University, Germany, Max Planck Institute for Informatics, Germany), Varsha Suresh (Max Planck Institute for Informatics, Germany)  
**Category**: cs.CL  
**Published**: 2026-08-11  
**Score**: 86.0  
**Type**: new  
**ArXiv ID**: 2608.09772v1  

#### Abstract
Large Vision-Language Models (LVLMs) have demonstrated strong performance on multimodal benchmarks, yet it remains unclear whether they genuinely reason about relationships between images and text or rely on superficial correlations, known as shortcut learning. This question is particularly importan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Large Vision-Language Models（LVLMs）在多模态讽刺检测任务中依赖浅层关联（shortcut learning），无法区分语用不一致（pragmatic incongruity）与简单的图像-文本跨模态不匹配，难以真正推理图像文本的深层关系，现有研究也缺乏此类受控基准来评估LVLM的语用推理能力。
🚀 提出的新方法与思路
**PragMatch**，是从MMSD2.0衍生的受控基准，包含3000个图像-文本对，涵盖原始讽刺样例、构造的字面及硬负对；通过系统掩码识别影响模型的shortcut线索，并通过针对性注入实验评估此类线索对模型预测的影响。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 语用-跨模态不匹配分离 | 首次提供基准区分多模态讽刺中的语用不一致与简单图像文本不匹配，填补现有评估空白 |
| 受控基准构建 | 包含3000个多模态对，覆盖原始讽刺样例及各类对照组，支持系统性评估 |
| 浅层线索评估 | 可评估LVLM对词汇、OCR、风格等表层shortcut线索的敏感度，揭示模型预测依赖表面信号的缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| PragMatch（衍生自MMSD2.0） | 作为多模态讽刺检测的受控基准，评估LVLM的语用推理能力（分离语用不一致与跨模态不匹配） |
🎯 实验设置与评估指标
任务为多模态讽刺检测；论文未报告具体评估指标。
⚔️ 基线方法对比
论文未报告所对比的基线方法信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供具体的表、图及对应的定量性能结果，故以下实验项均为论文未报告：主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验。

4. 关键结论和发现
- 主要发现
  1. 现有LVLM在多模态讽刺检测任务中，预测结果对词汇、OCR衍生、风格等浅层shortcut线索高度敏感；
  2. 向模型注入上述表面信号，会导致模型预测发生显著变化，尽管底层图像文本关系未改变；
  3. 提出的PragMatch基准为评估LVLM的多模态语用推理能力提供了系统性测试床，可超越表面图像文本对齐的评估。
- 方法局限性
论文未报告
- 未来工作
论文未报告

✅ **总结一句话**：PragMatch作为分离多模态任务中语用不一致与跨模态不匹配的受控基准，可揭示Large Vision-Language Models依赖浅层线索的缺陷，为评估其深层多模态推理能力提供系统性测试工具。

</details>

---

### 5. [Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis](https://arxiv.org/abs/2608.08935v1)

**Authors**: Kalelo Dukuray, Israel Pina, Evan Perez, Erika Ardiles-Cruz, Jie Wei  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 77.5  
**Type**: new  
**ArXiv ID**: 2608.08935v1  

#### Abstract
This work presents a unified multimodal AI system for damage assessment that integrates retrieval-augmented generation (RAG) models, thermal spectrum perception, vision foundation model pipelines, and exploratory wireless signal sensing. A RAG component is developed to ground a locally hosted langua...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis

1. 论文的主要贡献和创新点
✅ 解决的问题
现有损伤评估方案存在多重痛点：1. 静态few-shot prompting缺乏项目专属专业文档支撑，推理时易产生幻觉；2. 光电EO影像在恶劣光照、天气条件下的成像及分析效果受限；3. 无线传感技术在损伤评估场景的应用潜力尚未被充分挖掘。

🚀 提出的新方法与思路
**检索增强生成（RAG）组件**：构建基于本地部署语言模型的RAG模块，接入包含专业损伤等级分类标准的项目专属文档，缓解推理幻觉；对比向量式RAG与实体关系抽取构建的知识图谱变体RAG，发现图基RAG在跨文档推理类损伤评估查询中表现更优，进而提出融合密集、稀疏与图感知的混合检索方案。
**红外/热成像感知模块**：针对EO影像的局限性，采用红外/热光谱感知实现目标检测与分割，生成候选检测结果以提升多类目标的分割效果；开展红外与可见光谱跟踪实验明确失效模式，为鲁棒目标检测与损伤分析的多模态融合提供依据。
**视觉基础与视觉语言模型（VLM）模块**：利用视觉基础模型、视觉语言模型生成合成损伤影像，并对损伤严重程度进行分类，支撑下游损伤评估模型的训练与验证。
**无线信号感知模块**：开展探索性无线传感研究，验证其在EO和IR传感无效场景下，具备检测存在、运动及事件后环境变化的潜力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理可靠性 | 基于专业文档的RAG方案缓解幻觉，提升推理的事实一致性 |
| 跨文档推理能力 | 混合密集、稀疏、图感知的检索框架，强化需跨文档推理的损伤查询表现 |
| 恶劣场景适应性 | 集成IR/热传感、无线传感，弥补EO影像在恶劣光照、天气下的局限性 |
| 模型支撑能力 | 生成合成损伤影像，为下游损伤评估模型的训练与验证提供支撑 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务包含损伤严重程度分类、合成损伤影像生成、多模态目标检测等，具体实验设置与评估指标论文未报告。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 静态few-shot prompting | 提示工程方法 | 无外部专业文档支撑，易产生推理幻觉 |
| 向量式RAG | 检索增强方法 | 基于向量的检索方案，跨文档推理任务表现弱于图基RAG |
| 图基RAG | 检索增强方法 | 基于实体关系抽取构建知识图谱的检索方案，跨文档推理能力更强 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主benchmark性能：论文未报告
- 效率对比（FPS/参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

💡 结论：论文未报告

4. 关键结论和发现
- 主要发现：1. 动态检索的RAG（尤其混合检索方案）比静态few-shot prompting更能提升损伤评估查询的 grounding 能力与事实一致性；2. 图基RAG在需跨文档推理的损伤评估查询中表现优于向量式RAG；3. 多模态融合（IR/热+EO影像、无线传感+传统传感）可提升损伤评估在恶劣场景的鲁棒性，无线传感具备EO/IR无效场景的应用潜力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的集成多模态AI系统整合RAG、红外/热成像感知、视觉模型、无线信号传感等技术，可解决损伤评估中的推理可靠性、恶劣场景适应性等问题，验证了各模块的应用潜力。

</details>

---

### 6. [VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use](https://arxiv.org/abs/2608.08477v1)

**Authors**: Juan S. Santillana  
**Category**: cs.CL  
**Published**: 2026-08-11  
**Score**: 76.5  
**Type**: new  
**ArXiv ID**: 2608.08477v1  

#### Abstract
We present VectraYX-Vision-1B, a sub-2B vision-language model (VLM) for Spanish/LATAM cybersecurity imagery, coupling a frozen SigLIP-so400m encoder to a 1.04B Spanish/LATAM security decoder via an MLP. To our knowledge, it is the first sub-2B VLM specialized for cyber UI (IDA, Ghidra, Wireshark, Nm...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对西班牙语/LATAM网络安全UI（含IDA、Ghidra等工具界面）的视觉语言模型（VLM）缺失专门的子2B规模模型；当前视觉微调（SFT）存在近零视觉grounding得分的问题，且存在检查点加载bug（未剥离llm.前缀）伪装成训练崩溃；尚不明确729 token视觉块上位置编码（PE）对注意力的影响。
🚀 提出的新方法与思路
**VectraYX-Vision-1B模型架构**：将冻结的SigLIP-so400m编码器通过MLP连接到1.04B的西班牙语/LATAM安全解码器，构建子2B规模VLM，支持西班牙语回答、原生<|think|>结构化推理、通过Model Context Protocol的<|tool_call|>调用工具，可导出为llama.cpp的LLaVA mmproj格式用于物理隔离部署。
**位置编码消融矩阵设计**：设置3种变体（V0：每4层使用NoPE、V1：全部使用RoPE、V2：NoPE+学习2D PE），用于研究729 token视觉块上周期NoPE层对注意力的影响，开源代码、配置和权重以确立该架构问题的优先级。
**问题修复方案**：针对视觉SFT近零得分的问题，提出修复方向（更长SFT步骤、≥60%重放数据、更低学习率），明确检查点加载bug（未剥离llm.前缀）是训练崩溃假象的根源。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模型规模 | 子2B规模，适配多场景部署需求 |
| 语言适配 | 专门面向西班牙语/LATAM网络安全场景，支持西班牙语输出 |
| 功能特性 | 原生支持结构化推理（<|think|>）与工具调用（Model Context Protocol） |
| 部署灵活性 | 支持导出为llama.cpp的LLaVA mmproj格式，可用于物理隔离环境 |
| 研究开放性 | 开源代码、配置、权重，聚焦729 token视觉块的位置编码架构研究 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 14596个跨10个领域的QA对 | 模型训练与评估 |
| 网络安全工具界面（IDA、Ghidra、Wireshark、Nmap、Metasploit、Volatility） | 视觉相关任务的测试数据 |
🎯 实验设置与评估指标
任务为西班牙语/LATAM网络安全UI的视觉问答与推理任务，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| B1-B5 | 文本 backbone、文本控制相关的评估指标（论文未明确具体含义） |
| B6/B7 | 视觉grounding相关的评估指标（论文未明确具体含义） |
| 壁钟时间 | 模型运行的时间消耗（论文未说明评价方向） |
| GGUF效率 | CPU上GGUF格式部署的效率表现（论文未说明评价方向） |
⚔️ 基线方法对比
论文未报告具体基线方法，故表格如下：
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告具体基线方法 | - | - |

3. 主要实验结果和性能指标
📊 定量结果汇总
**视觉grounding性能（工具识别场景，论文提及）**
| 指标 | 当前视觉SFT（400-1900步，~16M tokens）结果 |
| --- | --- |
| B6（工具识别） | 0.08 |
💡 结论：当前视觉SFT在工具识别任务的视觉grounding上表现接近零，忽略图像内容。
其他实验结果：
主benchmark性能：论文未报告
效率对比（FPS / 参数量）：论文未报告具体数值
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告3种变体（V0、V1、V2）的具体性能数值

4. 关键结论和发现
- 主要发现：① VectraYX-Vision-1B是首个针对西班牙语/LATAM网络安全UI的子2B规模VLM；② 当前视觉SFT表现差（B6得分0.08）是因检查点加载bug（未剥离llm.前缀）伪装成训练崩溃；③ 设计了针对729 token视觉块位置编码的3种变体消融矩阵，开源相关资源以推进该架构问题的研究。
- 方法局限性：当前视觉SFT性能不足，存在检查点加载bug，仅提出位置编码的消融方向但未给出具体性能结果。
- 未来工作：① 采用更长SFT步骤、≥60%重放数据、更低学习率修复视觉SFT问题；② 优化检查点加载流程；③ 进一步研究729 token视觉块中位置编码对注意力的影响。

✅ **总结一句话**：论文提出首个针对西班牙语/LATAM网络安全UI的子2B视觉语言模型VectraYX-Vision-1B，排查出视觉SFT表现差的原因为检查点加载bug，给出修复方案并开源相关资源以推进架构研究。

</details>

---

### 7. [Listen, See and Track: Spatio-Temporal Audio-Visual Sound Event Reasoning for Omni-Modal Language Models](https://arxiv.org/abs/2608.09435v1)

**Authors**: Zhi Zeng, Cheng Zhang, Zesheng Yang, Rendong Pi, Jiaying Wu, Di Zhang, Zihan Ma, Guodong Li, Zhou Yang, Yu Xiang, Yifei Zheng, Minnan Luo  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2608.09435v1  

#### Abstract
Understanding dynamic sound sources requires jointly determining what produces a sound, where the source is located, and how it moves over time. Yet existing audio-language models often represent clips as global acoustic events, while vision-language models lack the spatial audio cues needed to loca...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Listen, See and Track: Spatio-Temporal Audio-Visual Sound Event Reasoning for Omni-Modal Language Models》
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为：理解动态声源需联合确定声源产生的事件、位置及随时间的移动，但现有音频语言模型常将音频片段表示为全局声学事件，而视觉语言模型缺乏定位和跟踪单个声源所需的空间音频线索，难以完成该类任务。

🚀 提出的新方法与思路
**构建时空音频问答基准ST-OmniQA**：该基准包含40K条全景视频、400K组问答对，按能力分为四个级别，涵盖声音事件识别、到达方向、声源距离、运动轨迹及时空影音推理，采用同步一阶Ambisonics（FOA）音频，用于评估模型的时空影音推理能力。
**提出ST-Omni-R1模型**：该模型整合FOA推导的语义与轨迹表示、全景视觉上下文，通过渐进式课程学习及推理树强化学习进行训练，以实现对动态声源的时空影音推理。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 基准评估能力 | 构建的ST-OmniQA全面覆盖动态声源推理的核心能力维度 |
| 模型性能与泛化 | 在ST-OmniQA基准四类能力平均语义准确率达77.83%，显著优于最优基线的37.28%；学习到的空间与运动表示可迁移至ST-OmniQA之外的公共空间音频基准 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ST-OmniQA | 评估多模态模型在声音事件识别、声源定位、运动跟踪及时空影音推理等任务上的能力，包含40K全景视频与对应音频、400K问答对 |

🎯 实验设置与评估指标
任务：基于同步全景视频与一阶Ambisonics（FOA）音频的时空音频-视觉问题回答任务。
| 指标 | 含义（↑） |
| --- | --- |
| 平均语义准确率 | 模型回答与问题对应正确答案的匹配程度，数值越高表示性能越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 最优评估基线 | 现有多模态模型 | 在ST-OmniQA基准上的平均语义准确率仅37.28%，推理能力弱于ST-Omni-R1 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能
**表（论文未提及表号，结果来自原文）：ST-OmniQA基准四类能力级别平均语义准确率**
| 方法 | 平均语义准确率 |
| --- | --- |
| ST-Omni-R1 | 77.83% ✅ |
| 最优评估基线 | 37.28% |
💡 结论：ST-Omni-R1在ST-OmniQA基准的时空影音推理任务上的性能显著优于现有最优基线模型。

2. 跨域/zero-shot迁移
论文未报告具体迁移性能数值，仅提及ST-Omni-R1学习到的空间与运动表示可迁移至ST-OmniQA之外的三个公共空间音频基准。

3. 效率对比
论文未报告该实验相关内容。

4. 鲁棒性/扰动测试
论文未报告该实验相关内容。

5. 消融实验
论文未报告该实验相关内容。

4. 关键结论和发现
- 主要发现1：动态声源的时空推理需多模态模型整合视觉空间线索与空间音频线索，现有模型在该整合能力上存在明显缺陷。
- 主要发现2：ST-OmniQA基准可有效评估模型在声音事件、声源定位、运动轨迹及时空推理等核心维度的能力；ST-Omni-R1通过合理的表示整合与训练策略，实现了跨基准的表示泛化能力。
- 方法局限性：论文未明确提及方法的局限性。
- 未来工作：论文未指定具体未来工作方向，可围绕提升多模态模型在时空音频-视觉推理任务上的性能与泛化性开展研究。

> ✅ **总结一句话**：该论文构建了ST-OmniQA时空音频问答基准，提出ST-Omni-R1模型解决多模态模型在动态声源时空影音推理上的短板，且模型的空间与运动表示具有跨基准泛化能力。

</details>

---

### 8. [Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation](https://arxiv.org/abs/2608.08469v1)

**Authors**: Kaichen Zhang, Wei Huang, Keming Wu, Bo Li, Xiaojuan Qi  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 59.5  
**Type**: new  
**ArXiv ID**: 2608.08469v1  

#### Abstract
Existing streaming multimodal models process observations incrementally but still follow a turn-based prefill-then-decode pattern, making them non-duplex: new observations cannot naturally enter an active generation stream. Proactive alternatives use micro-turn polling or external response gates, wh...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有流式多模态模型多遵循turn-based的prefill-then-decode模式，为非双工结构，无法让新观测自然进入活跃生成流；现有的主动式替代方案（如micro-turn polling或外部响应门）存在缺陷：碎片化连续交互，解耦响应时机与语言生成，增加KV缓存友好服务的复杂度。

🚀 提出的新方法与思路
**Aero Realtime双工架构**：构建视频、音频、文本输出共享的时间网格，每个约80ms的音频槽可预测词法token或silence token，使输入与输出能同步推进；通过单一自回归目标学习响应时机与生成内容；推理阶段仅追加最新多模态槽，保留前序输出状态并复用KV缓存，实现高效增量执行。
**完整训练与 serving配方**：包含实时QA构建、槽对齐监督、硬件感知分布式训练、可恢复推理。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 交互连续性 | 支持连续交互，不会碎片化观测与生成流 |
| 响应逻辑统一性 | 响应时机与生成内容由单一自回归目标统一学习，无需额外机制 |
| KV缓存服务友好性 | 增量执行时复用KV缓存，服务复杂度低 |
| 处理延迟 | 处理延迟低，保持在源时间线200ms内 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为低延迟流式多模态生成；评估指标包括中位数处理延迟（↓ 越低越好）、P95处理延迟（↓ 越低越好）、是否在源时间线200ms内（符合要求则达标）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有流式多模态模型 | 流式多模态生成方法 | 采用turn-based的prefill-then-decode模式，非双工结构，新观测无法自然进入活跃生成流 |
| 主动式替代方案（micro-turn polling/外部响应门） | 流式多模态生成方法 | 使用micro-turn polling或外部响应门，会碎片化连续交互，解耦响应时机与语言生成，增加KV缓存友好服务的复杂度 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未补充实验对应表号/图号。论文给出的定量结果：在4张NVIDIA A6000工作站GPU上，Aero Realtime运行20分钟的持续流视频时，中位数处理延迟为84ms，P95处理延迟为173ms，处理延迟保持在源时间线的200ms以内。
💡 结论：Aero Realtime实现了低延迟的双工流式多模态生成，处理延迟满足实时交互的要求。

4. 关键结论和发现
- 主要发现：1. 现有流式多模态模型及主动式替代方案均存在交互碎片化、响应逻辑解耦、KV缓存服务复杂等问题；2. Aero Realtime通过共享时间网格对齐输入输出流的设计，可有效解决上述问题；3. 在4张NVIDIA A6000 GPU的硬件条件下，Aero Realtime能在20分钟的持续流视频生成中保持符合实时要求的低延迟。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：Aero Realtime是一种4B规模的双工流式多模态模型，通过共享时间网格对齐输入输出流，实现了低延迟、符合实时交互要求的流式多模态生成。

</details>

---

### 9. [ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters](https://arxiv.org/abs/2608.07971v1)

**Authors**: Jinghao Wang, Yihang Zhou, Xiaoyang Sun, Chunming Hu, Tianyu Wo, Xu Wang, Albert Y. Zomaya, Renyu Yang  
**Category**: cs.DC  
**Published**: 2026-08-11  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2608.07971v1  

#### Abstract
Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations. This leaves substantial GPU capacity underutilized: training jobs reserve enti...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters
1. 论文的主要贡献和创新点
✅ 解决的问题：现有GPU集群调度器将深度学习训练与离线大语言模型推理视为孤立的资源消费者，采用刚性静态资源分配，导致GPU容量大量闲置，训练作业保留整个设备却存在周期性空闲，离线推理任务因突发需求过度配置GPU，造成资源浪费。
  现有方法的缺陷：① 将两类异构workloads视为孤立资源消费者，未考虑特性差异；② 采用刚性静态资源分配，缺乏弹性；③ 导致GPU利用率低、作业完成时间长、集群吞吐量受限等问题。

🚀 提出的新方法与思路
**Resource Shape Transformation**：将每个作业呈现为一组可行的资源-性能配置集合，使作业具备弹性选择不同资源分配方式的能力。
**Elastic Shadow Pricing**：将多资源分配问题分解为基于动态单资源影子价格的单作业配置选择子问题，简化多资源优化复杂度。
**Interference-Aware Co-location**：使用基于硬件计数器和任务级特征训练的预测器，估计GPU共享场景下不同作业间的成对性能退化情况，保障共置workloads的性能稳定性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 作业性能 | 可降低平均JCT达2.94倍 |
| 集群吞吐量 | 可提升集群吞吐量达2.02倍 |
| GPU资源利用率 | 可将GPU利用率从约25%提升至46% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 作业运行轨迹 | 用于大规模GPU集群的迹驱动模拟实验 |

🎯 实验设置与评估指标
任务为调度GPU集群上的深度学习训练和离线大语言模型推理workloads，评估指标如下：
| 指标 | 含义（箭头方向） |
| --- | --- |
| 平均JCT | 作业完成时间（↓ 越低越好） |
| 集群吞吐量 | 单位时间处理的作业量（↑ 越高越好） |
| GPU利用率 | GPU资源实际使用比例（↑ 越高越好） |

⚔️ 基线方法对比
论文未报告具体基线方法的名称、类型及特点。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的相关实验设计与对应表号，仅在论文摘要中提及如下结果：
**无对应表号：测试床与模拟实验性能结果**
| 指标 | 结果 |
| --- | --- |
| 平均JCT | 降低最多2.94倍 |
| 集群吞吐量 | 提升2.02倍 |
| GPU利用率 | 从约25%提升至46% |
💡 结论：ElastiCo框架在GPU集群的训练与推理workloads共存场景下，可显著缩短作业完成时间、提升集群吞吐量及GPU资源利用率。
其余指定实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告。

4. 关键结论和发现
- 主要发现1：现有GPU集群调度器对训练与推理workloads的孤立静态分配方式，是导致GPU资源利用率低、作业性能差的核心原因。
- 主要发现2：ElastiCo提出的三类机制协同作用，可有效实现GPU的弹性资源共享，大幅提升集群整体性能与资源利用率。
- 主要发现3：ElastiCo在不同规模GPU集群（64-GPU测试床、512-GPU模拟集群）中均表现出显著性能提升。
- 方法局限性：论文未报告具体局限性内容。
- 未来工作：论文未报告具体未来工作内容。

> ✅ **总结一句话**：ElastiCo是一种弹性配置与感知干扰的GPU集群编排框架，通过三类整合机制实现训练与离线推理workloads的安全GPU共享，大幅提升集群性能与资源利用率。

</details>

---

### 10. [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](https://arxiv.org/abs/2608.09230v1)

**Authors**: Yuanchi Zhu, Kang An, Tengyue Wang, Zhongyu Yang, Chenxu Du, Xinqi Yang, Hebao Zhu, Bokai Zhao, Tianyu Liang, Ziliang Wang, Faqiang Qian, Yunli Yang, Weiyang Shi, Qibing Ren  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2608.09230v1  

#### Abstract
Industrial-safety understanding requires more than detecting workers, equipment, and personal protective equipment. Models must also assess compliance, identify hazardous interactions, explain potential accident mechanisms, and recommend preventive actions. Existing safety datasets primarily focus o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge
1. 论文的主要贡献和创新点
✅ 解决的问题
工业安全理解不仅需要检测人员、设备、个人防护装备（PPE），还需评估合规性、识别危险交互、解释潜在事故机制、推荐预防措施；但现有安全数据集仅聚焦视觉感知或孤立违规识别，对基于证据的推理监督不足，难以满足工业安全多维度理解的需求。

🚀 提出的新方法与思路
**场景中心管道**：将标注的工作场所图像转换为可执行的安全场景图，通过对对象、关系、安全规则执行程序生成确定性答案；
**报告中心管道**：从事故报告中提取图表与上下文证据，利用证据图、显式信息边界、多步推理路径、迭代验证构建多模态问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 数据来源 | 结合工作场所场景图像与事故报告知识，现有方法仅提供单一类型数据支撑 |
| 推理覆盖 | 支持感知、合规评估、因果分析等多类型工业安全推理任务，现有方法仅聚焦基础违规识别 |
| 监督机制 | 提供证据导向的多模态推理监督，现有方法缺乏基于证据的推理训练监督 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| SafeSceneReason | 包含110581个场景中心问答对、13114个报告中心问答对，覆盖感知、合规评估等多类型工业安全任务，作为工业安全多模态推理基准与配套训练语料 |

🎯 实验设置与评估指标
任务为工业安全多模态推理任务；论文未报告具体评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 代表性专有视觉-语言（VLM）模型 | 专有模型 | 具备通用视觉语言理解能力 |
| 代表性开源VLM模型 | 开源模型 | 具备通用视觉语言理解能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（1）主benchmark性能：论文未报告
（2）效率对比（FPS / 参数量）：论文未报告
（3）跨域/zero-shot迁移：论文未报告
（4）鲁棒性/扰动测试：论文未报告
（5）消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）通用VLM在工业安全推理任务中存在显著性能差异，在比较性、技术性、多证据推理方面存在持续弱点；2）强通用视觉理解能力无法保证模型具备可靠的工业安全推理能力；3）工业安全推理需结合场景视觉信息与事故报告知识才能有效支撑。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SafeSceneReason是连接工业危害与事故知识的多模态工业安全推理基准，填补了现有数据集缺乏证据型多步推理监督的空白，为工业安全推理研究提供了基础支撑。

</details>

---

### 11. [Jako Tako or Fluent? Presenting PoVisLE: A Polish Vision-Language Evaluation](https://arxiv.org/abs/2608.07763v1)

**Authors**: Anna Ko{\l}os, Grzegorz Statkiewicz, Karolina Seweryn, Katarzyna Kowol, Karolina Piosek, Wojciech Kusa  
**Category**: cs.CL  
**Published**: 2026-08-11  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2608.07763v1  

#### Abstract
Vision-language models (VLMs) have achieved strong performance on tasks such as image captioning, visual question answering, and image-to-text generation. However, they are predominantly trained on English-centric data, which limits their ability to handle culturally grounded visual understanding an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Jako Tako or Fluent? Presenting PoVisLE: A Polish Vision-Language Evaluation
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有视觉语言模型（VLMs）主要在英语中心数据上训练，限制了其处理文化植根的视觉理解的能力，在区域特定含义、符号内容、依赖语境的视觉线索的解释上存在失败问题。
- 现有用于文化能力的评估基准常为模板驱动，聚焦于表面识别，不足以评估文化情境下深层的语言和语用理解。

🚀 提出的新方法与思路
**PoVisLE基准**：提出针对波兰语的单文化视觉语言基准PoVisLE，采用扎根评估范式，在该范式中语言结合视觉语境进行解释，用于评估文化植根的多模态理解；该基准包含1117张图像和2366个人工标注的视觉问答（VQA）对，提供了可控且具有挑战性的资源，用于评估超越表面识别的文化植根的视觉语言理解。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 文化适配性 | 面向波兰语文化情境设计，聚焦文化植根的多模态理解 |
| 评估深度 | 基于扎根评估范式，语言与视觉语境互动，可评估深层语言和语用理解，而非仅表面识别 |
| 资源特性 | 包含特定规模的图像及人工标注VQA对，为相关评估提供可控且具挑战性的资源 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| PoVisLE | 评估超越表面识别的文化植根的视觉语言理解 |

🎯 实验设置与评估指标
论文未报告

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 现有视觉语言模型的英语中心训练模式及现有文化评估基准的表面识别导向，无法满足文化情境下深层视觉语言理解的评估需求。
- PoVisLE是针对波兰语的单文化视觉语言评估基准，可用于评估超越表面识别的文化植根的多模态理解，为相关研究提供了新的可控资源。

- 方法局限性
论文未报告

- 未来工作
论文未报告

> ✅ **总结一句话**：本论文引入了针对波兰语的单文化视觉语言评估基准PoVisLE，为评估超越表面识别的文化植根的多模态理解提供了可控且具有挑战性的资源。

</details>

---

### 12. [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](https://arxiv.org/abs/2608.07959v1)

**Authors**: Keyang Zhong, Kuo Wang, Peng Liu, Quanlong Zheng, Junlin Xie, Zhijia Liang, Yanhao Zhang, Guanbin Li  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.07959v1  

#### Abstract
Ultra-long egocentric video understanding requires reasoning over temporally sparse evidence distributed across hours or days, challenging current multimodal models with limited context and the grounding of key video segments. While Chain-of-Tool-Thought (CoTT) agent systems enable iterative retriev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态模型处理超长自我中心视频推理时受限于有限上下文，Chain-of-Tool-Thought（CoTT）智能体因刚性放大策略缺乏恢复机制，导致错误传播；同时，多轮工具使用智能体训练面临挑战，现有RL方法依赖稀疏结果级奖励，缺乏对扩展决策轨迹的监督，长周期推理信用分配欠佳。

🚀 提出的新方法与思路
**SCOUT（Self-Checking Chain-Of-Tool-thought）框架**：该恢复感知的智能体框架引入自适应策略，评估中间工具观测结果，在探索（区域切换）与利用（放大）间动态权衡，实现极长周期下的鲁棒多跳推理。
**UPS-GRPO（uncertainty-prioritized policy optimization）方法**：用于解决多轮工具使用智能体的训练问题，将探索聚焦于高不确定性的工具后状态，同时维持样本效率；还引入轮级优势分解，整合结果奖励与工具接地的时间对齐奖励，优化信用分配。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 超长周期推理 | 自适应探索-利用权衡减少错误传播，支持极长时空范围的多跳推理 |
| 训练效率 | UPS-GRPO方法集中高不确定性探索，保持样本效率 |
| 信用分配 | 轮级优势分解整合多类奖励，优化长轨迹的信用分配 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| ultra-long egocentric benchmarks | 超长自我中心视频推理任务的性能评估 |

🎯 实验设置与评估指标
任务为超长自我中心视频推理任务，论文未报告具体评估指标的名称及含义。

⚔️ 基线方法对比
论文未报告具体基线方法信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体定量数值。
2. 效率对比：论文未报告具体FPS、参数量等效率指标。
3. 跨域/zero-shot 迁移：论文未报告相关结果。
4. 鲁棒性/扰动测试：论文未报告相关结果。
5. 消融实验：论文未报告具体模块对比的定量结果。

4. 关键结论和发现
- 主要发现：SCOUT在超长自我中心视频基准上达到SOTA，同时在较短时长长视频设置上保持竞争力。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：SCOUT结合UPS-GRPO方法，针对超长自我中心视频推理的错误传播与训练信用分配问题，实现了先进的推理性能。

</details>

---

### 13. [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](https://arxiv.org/abs/2608.08569v1)

**Authors**: Wenxu Jia, Dongjie Fu, Xize Cheng, Fangming Feng, Linjun Li, Wenshi Chen, Yingming Li, Zhou Zhao, Tao Jin  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.08569v1  

#### Abstract
Recent advancements in Speech Large Language Models have demonstrated remarkable capabilities in understanding complex audio tasks. Despite this progress, their long-context inference remains severely bottlenecked by prohibitive KV cache memory demands. Existing text-centric compression methods stru...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference
1. 论文的主要贡献和创新点
✅ 解决的问题：长上下文音频推理场景下，Speech Large Language Models存在KV缓存内存需求过高导致的严重推理瓶颈；现有面向文本的KV缓存压缩方法应用于音频任务时，会破坏语音连续性或丢失关键语义线索，无法适配音频推理需求。
🚀 提出的新方法与思路
**ASR转录语义锚定时序压缩**：利用自动语音识别（ASR）生成的转录文本作为显式语义锚点，对音频token进行时序对齐、压缩与融合，以降低初始KV缓存体积并提升token信息密度。
**时序衰减累积注意力动态过滤**：为进一步提升压缩比，采用基于时序衰减的累积注意力策略，淘汰非必要token，同时缓解早期token偏差问题。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
推理性能 | 在长上下文场景的激进KV缓存压缩下可维持较高性能，短格式音频任务仍保持高保真感知
推理效率 | 可同时优化推理吞吐量与峰值内存开销
2. 核心实验方法和设置
📚 使用的数据集：六个多样化音频基准 | 用于评估VoxZip在各类音频任务上的性能
🎯 实验设置与评估指标：针对Qwen3-Omni开展音频推理任务；评估涉及压缩比、推理吞吐量、峰值内存开销、未压缩基线性能维持率，指标方向：压缩比↑（越高越好）、推理吞吐量↑（越高越好）、峰值内存开销↓（越低越好）、性能维持率↑（越高越好）
⚔️ 基线方法对比：论文未报告详细的基线方法列表及对应特点
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体性能数值及对应表号
2. 效率对比：论文未报告具体效率数值及对应表号
3. 跨域 / zero-shot迁移：论文未报告相关实验
4. 鲁棒性 / 扰动测试：论文未报告相关实验
5. 消融实验：论文未报告相关实验
4. 关键结论和发现
- 主要发现：VoxZip是train-free的两阶段语义锚定KV缓存压缩框架，有效缓解了Speech Large Language Models长上下文音频推理的KV缓存内存瓶颈；VoxZip可兼顾长上下文音频推理性能与短格式音频任务的高保真感知需求；VoxZip在压缩KV缓存的同时可优化推理效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：VoxZip是一种train-free的两阶段语义锚定KV缓存压缩框架，解决了Speech Large Language Models长上下文音频推理中的KV缓存内存瓶颈问题，同时兼顾音频推理性能与推理效率。

</details>

---

### 14. [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](https://arxiv.org/abs/2608.08640v1)

**Authors**: Donghong Jiang, Endian Lin, Luoping Cui, Hanqing Liu, Mingjie Liu, Fan Yang, Hong Wang, Zhao Yang, Chuang Zhu  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.08640v1  

#### Abstract
Large language model agents increasingly rely on reusable skills to extend their capabilities beyond parametric knowl- edge. However, retrieving the appropriate skill from a large- scale library remains challenging because realistic user re- quests are often concise and underspecified, stating only ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：现有大语言模型代理依赖可复用技能扩展能力，但用户请求通常简洁未明确指定所需能力与执行步骤，导致技能检索面临语义 gap；同时现有基准对这类隐含用户请求的覆盖有限，无法为技能检索任务提供充足支撑。
不同方法的缺陷：
- 现有技能检索方法：未充分利用推理增强的训练方式，难以适配隐含用户请求带来的语义模糊问题；
- 现有基准：对隐含用户请求的覆盖不足，无法有效评估技能检索的实际表现。

🚀 提出的新方法与思路
**SkillReason两阶段检索框架**：Stage I采用更强教师模型生成的能力推理追踪作为训练时的监督信号，通过对比学习、检索分布对齐和语言建模三种方式，鼓励检索器将能力推理的逻辑内化至查询表示中；Stage II引入检索引导的GRPO优化目标，鼓励模型探索更适配自身能力、更利于检索的推理轨迹；推理阶段仅对原始查询进行编码，无需执行自回归思维链生成，保证仅查询的高效检索效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 技能检索性能 | 在SkillReason-Bench、SkillRet、SRA-Bench三个基准上达到SOTA性能 |
| 语义适配能力 | 通过推理增强的两阶段训练，更好衔接高层任务目标与技能能力，缩小二者间的语义 gap |
| 推理效率 | 推理阶段无需自回归思维链生成，仅需编码原始查询，保障检索的高效性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| SkillReason-Bench | 提出的跨域基准，包含3729条查询、61228个技能，覆盖9个领域，用于核心测试 |
| SkillRet | 对比测试基准 |
| SRA-Bench | 对比测试基准 |

🎯 实验设置与评估指标
任务为针对隐含用户请求的技能检索，论文未明确报告具体评估指标。

⚔️ 基线方法对比
论文未报告基线方法的具体信息，无法列出相关内容。

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**
论文未报告具体性能指标数值，仅提及SkillReason在SkillReason-Bench、SkillRet和SRA-Bench上达到SOTA性能。

**效率对比**
论文未报告相关效率对比结果。

**跨域 / zero-shot 迁移**
论文未报告相关跨域/zero-shot迁移实验结果。

**鲁棒性 / 扰动测试**
论文未报告相关鲁棒性/扰动测试结果。

**消融实验**
论文未报告相关消融实验结果。

4. 关键结论和发现
- 主要发现：1. 推理增强的两阶段训练可有效缩小高层任务目标与技能能力间的语义 gap；2. SkillReason在多个隐含用户请求的技能检索基准上达到SOTA性能；3. 推理阶段仅编码原始查询的方式保障了检索效率。
- 方法局限性：论文未报告方法的局限性相关内容。
- 未来工作：论文未明确提及未来工作方向。

> ✅ **总结一句话**：SkillReason通过提出推理增强的两阶段技能检索训练框架与SkillReason-Bench跨域基准，有效解决了隐含用户请求下的技能检索问题，在多个基准上达到SOTA性能且保证了检索效率。

</details>

---

### 15. [CMU-Drive and V2V-VLA: Cooperative Multi-agent Unified Driving with Reasoning Benchmark and Vehicle-to-Vehicle Vision-Language-Action Models](https://arxiv.org/abs/2608.07621v1)

**Authors**: Hsu-kuang Chiu, Stephen F. Smith  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2608.07621v1  

#### Abstract
Vision-Language-Action (VLA) models have recently achieved impressive performance for end-to-end autonomous driving, yet existing approaches are primarily designed for an individual single autonomous driving agent with limited support for cooperative perception, reasoning, and planning. We present C...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CMU-Drive and V2V-VLA: Cooperative Multi-agent Unified Driving with Reasoning Benchmark and Vehicle-to-Vehicle Vision-Language-Action Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Vision-Language-Action (VLA)模型主要针对单个自主驾驶智能体，在协同感知、推理、规划方面支持有限。

🚀 提出的新方法与思路
**CMU-Drive**：是一个闭环端到端的基准，用于评估多辆连通自主车辆(CAVs)在涉及背景交通参与者的安全关键驾驶场景下的协同自主驾驶。
**V2V-VLA**：是一种协同VLA模型，通过联合生成驾驶动作、未来路径点、语言推理和通信策略，将协同驾驶整合到单次前向传播中。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
多智能体协同支持 | 支持多辆连通自主车辆的协同感知、推理、规划的闭环端到端评估与模型实现

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
CMU-Drive | 用于协同自主驾驶协同VLA模型的基准评估与实验

🎯 实验设置与评估指标
任务：协同自主驾驶下多智能体协同VLA模型的闭环端到端评估
指标 | 含义
--- | ---
论文未报告 | 论文未报告具体评估指标

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | 论文未报告 | 论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：建立了首个用于协同VLA驾驶的基准和基线，为多智能体闭环端到端协同自主驾驶的相关研究提供了基础。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了CMU-Drive多智能体协同自主驾驶基准和V2V-VLA协同视觉语言动作模型，填补了现有VLA模型在多智能体协同支持上的不足，为协同自主驾驶研究提供了新的基础。

</details>

---

### 16. [Finite Constant Frontiers and Auditable Regret Certificates for Average-Reward Reinforcement Learning](https://arxiv.org/abs/2608.07725v1)

**Authors**: Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb  
**Category**: cs.LG  
**Published**: 2026-08-11  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.07725v1  

#### Abstract
Average-reward reinforcement-learning regret is known up to logarithmic factors, but the numerical content of published guarantees is difficult to compare because probability mode, structural parameter, logarithmic normalization, prior information, and planning assumptions differ. We introduce a con...

---

### 17. [VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge](https://arxiv.org/abs/2608.07994v1)

**Authors**: Wenqi Chen, Haofei Yang, Rui Yang, Fangming Li  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.07994v1  

#### Abstract
Retrieval-Augmented Generation (RAG) is essential for enterprise knowledge question answering (QA), particularly in domains with complex product documentation like telecommunications. However, existing RAG approaches largely overlook the holistic integration of diverse retrieval strengths, leading t...

---

### 18. [Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression](https://arxiv.org/abs/2608.08960v1)

**Authors**: Cheng Fan, Junyi Zhou, Tingzhang Luo, RongJian Xu, Qiyanhui Lu, Mingjian Zhu, Hanting Chen, Jianyuan Guo  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.08960v1  

#### Abstract
Multi-step language-model agents repeatedly process growing interaction histories, leading to substantial context costs. Vision--text compression reduces these costs by rendering history as images, but the resulting modality shift creates a marked capability gap. Through controlled evaluations of hi...

---

### 19. [OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows](https://arxiv.org/abs/2608.08340v1)

**Authors**: Arup Kumar Sarker, Mills Staylor, Aymen Alsaadi, Gregor von Laszewski, Shantenu Jha, Geoffrey Fox  
**Category**: cs.DC  
**Published**: 2026-08-11  
**Score**: 50.0  
**Type**: new  
**ArXiv ID**: 2608.08340v1  

#### Abstract
Agentic retrieval-augmented generation (RAG) systems combine preprocessing, embedding, retrieval, memory access, context construction, generation, and vector-index updates. Although LLM decoding is GPU-bound, the surrounding orchestration layer can still limit end-to-end performance through serializ...

---

### 20. [MELLON - Multimodal Enhanced LLM for Online Navigation](https://arxiv.org/abs/2608.09121v1)

**Authors**: Ruiyu Li, Haoyang Cai, Zhitong Guo, Tong Hu  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.09121v1  

#### Abstract
Web navigation agents are capable of addressing various types of tasks on different websites. Current baselines on web navigation are either unimodal or lack strong reasoning abilities given multimodal inputs. Focusing on the WebShop benchmark, a real-world website simulation, we explore the alignme...

---

### 21. [Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models](https://arxiv.org/abs/2608.09227v1)

**Authors**: Puneet Mathur, Manan Suri, Dinesh Manocha  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.09227v1  

#### Abstract
Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive. While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal ...

---

### 22. [Deferred Audio Pruning with Local Audio-Visual Dynamics for Omni-LLMs](https://arxiv.org/abs/2608.08794v1)

**Authors**: Kyeongyoon Lee, Hongyeob Kim, Youngeun Kim, Sungeun Hong  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.08794v1  

#### Abstract
Omni-modal LLMs jointly process audio, video, and text, but long multimodal sequences incur substantial prefill and KV-cache costs. Existing omni-modal compression methods primarily focus on pre-LLM token reduction, leaving modality-specific compression across the LLM boundary underexplored. We prop...

---

### 23. [Investigating Multimodal Informativity under Different Partner Visibility Conditions in Video-Mediated Dialogue](https://arxiv.org/abs/2608.08915v1)

**Authors**: Esam Ghaleb, Hugh Mee Wong, Kristina Kobrock  
**Category**: cs.CL  
**Published**: 2026-08-11  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.08915v1  

#### Abstract
Situated language use is multimodal and embodied. For example, gestures can carry information that is absent or underspecified in the speech signal, yet dialogue models typically rely on transcripts alone. We study how much referential information gestures and their combination with speech carry in ...

---

### 24. [Dynamic Distribution-Aware Uncertainty Tracking in Vision-Language Representation Learning](https://arxiv.org/abs/2608.09011v1)

**Authors**: Ao Zhou, Zhiwei Jiang, Zifeng Cheng, Cong Wang, Shufan Yang, Haoru Chen, Qing Gu  
**Category**: cs.LG  
**Published**: 2026-08-11  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.09011v1  

#### Abstract
Uncertainty Quantification (UQ) aims to measure the reliability of model predictions, serving as a critical safeguard for deploying Vision-Language Models (VLMs) in safety-critical scenarios. Post-hoc approaches are widely adopted due to their lightweight nature, mapping the outputs of VLMs to uncer...

---

### 25. [When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection Bounds LLM-Judge Failure in Reasoning Pipelines](https://arxiv.org/abs/2608.07813v1)

**Authors**: Yiyao Zhang, Diksha Goel, Hussain Ahmad, Shixun Huang, Jun Shen  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.07813v1  

#### Abstract
An LLM judge deployed inside a reasoning pipeline does not merely measure quality, it decides which answer ships. We show that the cost of that decision depends less on judge accuracy than on the decision rule the judge is embedded in. On frozen candidate pools from four GRPO policies, an unconstrai...

---

### 26. [Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning](https://arxiv.org/abs/2608.07955v1)

**Authors**: Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.07955v1  

#### Abstract
Large vision-language models have achieved strong performance in multimodal reasoning, but they remain unreliable on fine-grained spatial tasks that demand both precise spatial perception and fine-grained geometric computation beyond end-to-end generation. Tool augmentation offers a natural solution...

---

### 27. [Thought-Level Beam Search for Reasoning](https://arxiv.org/abs/2608.08020v1)

**Authors**: Lijie Yang, Hongyin Luo, Tri Dao, Ravi Netravali  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.08020v1  

#### Abstract
Test-time compute scaling is a primary driver of performance in large reasoning models (LRMs), but extreme inefficiency bounds current approaches, shifting the critical question from \emph{how much} compute to spend, to \emph{where} to allocate it. We formalize test-time reasoning as a constrained c...

---

### 28. [CRUISE: Vision-Language Model-Guided Uncertainty-Aware Cross-Modal Sensor Fusion for Robust Autonomous Driving](https://arxiv.org/abs/2608.09202v1)

**Authors**: Junyao Wang, Yulin Xu, Yu Li, Pramod Khargonekar, Mohammad Abdullah Al Faruque  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.09202v1  

#### Abstract
Modern autonomous vehicles are equipped with multiple sensors, such as cameras, LiDAR, and radar, for comprehensive environmental perception. However, robust cross-modal feature fusion remains a critical challenge, as the reliability of each sensor varies significantly across diverse real-world driv...

---

### 29. [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](https://arxiv.org/abs/2608.08168v1)

**Authors**: Bo Cheng, Qiaolin Lu, Yi Chang, Yuan Wu  
**Category**: cs.CL  
**Published**: 2026-08-11  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.08168v1  

#### Abstract
While Large Language Models (LLMs) employing Chain-of-Thought (CoT) exhibit superior reasoning capabilities, the neural mechanisms distinguishing this explicit Thinking mode from direct answer generation (NoThinking mode) remain poorly understood. To deconstruct this cognitive process, we apply Top-...

---

### 30. [Long SKILL Compliance as Logical Reasoning: Closure-Grounded Detection with Scaling-Guided On-Policy Distillation](https://arxiv.org/abs/2608.08146v1)

**Authors**: Shuaitao Zhao, Feng Ni, Lichao Ma, Jiaye Lin, Fei Han, Yang Wei, Lu Pan  
**Category**: cs.AI  
**Published**: 2026-08-11  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.08146v1  

#### Abstract
The increasing complexity of enterprise business scenarios has promoted the widespread adoption of long SKILL documents in agent systems, posing new challenges for compliance detection: large models incur substantial inference costs, while small models may fail to maintain detection accuracy. To add...

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
