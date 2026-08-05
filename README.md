# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-05 08:16:32 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning](https://arxiv.org/abs/2608.03161v1)

**Authors**: Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, Md. Tanvir Raihan  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 93.5  
**Type**: new  
**ArXiv ID**: 2608.03161v1  

#### Abstract
Lecture videos distribute knowledge across speech, slide text, diagrams, equations, and presentation order, which transcript-only retrieval does not fully preserve. This paper presents an evidence-grounded multimodal pipeline that transcribes lectures, selects semantic anchors, applies optical chara...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对讲座视频的检索方法多基于转录文本，然而讲座知识分布在语音、幻灯片文本、图表、公式及演示顺序等多模态维度，仅文本检索无法充分保留这些跨模态知识，存在知识获取不完整的痛点。

🚀 提出的新方法与思路
**Evidence-Grounded Multimodal Pipeline**：该流程依次执行以下操作：转录讲座语音内容，选择语义锚点，应用光学字符识别（OCR）处理相关文本，使用视觉语言模型（VLM）提取仅由转录数据、OCR结果或视觉证据支撑的概念与类型化关系；对提取到的概念与关系提及进行验证后，规范化为带有溯源信息（provenance-rich）的知识图谱。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
多模态知识保留能力 | 相比仅依赖文本的检索方法，可完整保留分布在语音、幻灯片文本、图表、公式及演示顺序中的跨模态知识
知识可审计性 | 构建的知识图谱附带溯源信息，具备可审计性

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
三个神经网络相关讲座的多模态数据（含演讲语音、幻灯片文本及对应视觉内容） | 用于验证所提多模态知识图谱构建管线的有效性

🎯 实验设置与评估指标
任务为多讲座教育推理场景下的知识图谱构建及检索测试；评估指标包括端点覆盖率（越高越好↑）、检索任务的Top-1准确率（越高越好↑）、Top-3准确率（越高越好↑）、Top-5平均召回率（越高越好↑）

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
该部分未提及对应结果的表号、图号、章节或页码，仅陈述论文明确提供的内容：
- 处理规模：所提管线在三个神经网络讲座数据上，共处理3118帧、756个转录片段、559个锚点；
- 提取成果：共保留1022个概念提及、312个关系提及，最终得到172个规范概念、282个关系，端点覆盖率为90.38%；
- 检索测试：针对三个问题的初步检索测试，取得100%的Top-1准确率、100%的Top-3准确率及100%的平均Top-5召回率。

💡 结论：所提证据接地多模态管线在神经网络讲座数据上实现了跨模态知识的有效整合，产出的规范知识图谱具备较高的端点覆盖率，且在检索测试中表现优异。

其他实验结果：
主benchmark性能：论文未报告
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 所提出的证据接地多模态知识图谱构建管线，可有效提取讲座中经转录、OCR或视觉多模态证据支撑的概念与关系，构建出具备溯源性的知识图谱；
- 该管线在三个神经网络讲座数据上运行有效，最终产出的知识图谱具备较高的端点覆盖率；
- 基于该管线构建的知识图谱开展的初步检索测试，实现了100%的Top-1、Top-3准确率及100%的平均Top-5召回率。
方法局限性：论文未明确报告
未来工作：论文未提及

> ✅ **总结一句话**：论文提出了一种证据接地的多模态知识图谱构建管线，针对神经网络讲座数据完成跨模态知识的有效整合与溯源知识图谱构建，核心贡献为可审计的构建方法而非SOTA性能，初步检索测试表现优异。

</details>

---

### 2. [When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference](https://arxiv.org/abs/2608.03741v1)

**Authors**: Przemyslaw Forys, Haoran Wu, Can Xiao, Jiayi Nie, Tony Liu, Rika Antonova, Timothy Jones, Robert Mullins, Wayne Luk, Aaron Zhao, George A. Constantinides  
**Category**: cs.DC  
**Published**: 2026-08-05  
**Score**: 82.0  
**Type**: new  
**ArXiv ID**: 2608.03741v1  

#### Abstract
Agentic inference now dominates the LLM inference landscape, requiring LLMs to actively engage in multi-turn interactions with tool-calling capabilities. This introduces a more complex workload for the underlying inference system: serving stages such as prefill and decode exhibit substantially diffe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference

1. 论文的主要贡献和创新点
✅ 解决的问题
Agentic inference需支撑多轮交互与工具调用，其prefill、decode等服务阶段行为差异大，需不同计算与内存带宽资源，单一同质GPU系统难以适配；当前异构系统中各组件最优硬件设计的问题未被充分研究。

🚀 提出的新方法与思路
**HeteroPanacea**：提出一种名为HeteroPanacea的新型异构服务模拟框架，支持三个维度的系统级模拟：1）disaggregated quantization；2）自动化的设备内与设备间并行化调度；3）PDAF（prefill-decode-attention-FFN）NPU架构异构性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 系统级模拟覆盖度 | 支持跨disaggregated quantization、并行调度、PDAF NPU架构异构三个维度的agentic LLM服务系统级模拟，可评估异构系统各组件的最优硬件设计 |
| 服务性能量化 | 可模拟不同服务拆分方式下的吞吐量表现，为异构系统优化提供量化依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体使用的数据集及用途 |

🎯 实验设置与评估指标
任务：agentic LLM推理服务的异构系统性能模拟，评估指标为吞吐量（↑越高越好）
| 指标 | 含义 |
| ---- | ---- |
| 吞吐量 | 反映agentic LLM服务的处理能力，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统GPU服务 | 同质系统 | 使用当前GPU的传统服务方式，无PDAF阶段拆分 |
| 异构拆分服务 | 异构系统 | 基于disaggregation思路的服务，含不同prefill-decode、PDAF阶段拆分方式 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**
论文未报告

**效率对比（FPS / 参数量）**
论文未报告

**跨域 / zero-shot 迁移**
论文未报告

**鲁棒性 / 扰动测试**
论文未报告

**消融实验**
| 模块名称 | 对应模型架构（影响disaggregation增益的相关模块） | 吞吐量增益（最优/最差） |
| ---- | ---- | ---- |
| 论文未明确列出具体模块与指标细节 | 论文未提供具体模块与指标的对应关系 | 论文未报告具体指标的最优/最差值，仅提及开展了相关消融研究 |

4. 关键结论和发现
- Agentic LLM推理服务中，prefill-decode拆分的异构部署可提升吞吐量，4-way Prefill Decode Attention FFN disaggregation是不同模型间提升吞吐量最一致的方式
- 模拟框架HeteroPanacea可支撑跨维度的异构服务性能评估，为异构系统最优硬件设计提供参考
- 论文开展了模型架构与disaggregation增益关系的消融研究，但未报告具体细节

- 方法局限性
论文未报告

- 未来工作
论文未报告

> ✅ **总结一句话**：本文提出异构LLM服务模拟框架HeteroPanacea，通过模拟disaggregation下的PDAF架构异构，验证了异构拆分可提升agentic LLM推理吞吐量，为异构系统各组件最优硬件设计提供了量化评估依据。

</details>

---

### 3. [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555v1)

**Authors**: Hyungkyu Ham, Junhyeong Bae, Seungheon Lee, Myeongjae Jeon, Gwangsun Kim  
**Category**: cs.AR  
**Published**: 2026-08-05  
**Score**: 71.5  
**Type**: new  
**ArXiv ID**: 2608.03555v1  

#### Abstract
This paper presents a heterogeneous decode-phase serving system that relocates the KV cache out of GPU memory, motivated by the retrieval-based sparse attention that recent frontier LLMs adopt to serve million-token contexts. It partitions a decode step by operation type: GPU nodes hold the model we...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有面向检索式稀疏注意力的LLM服务，其采用的PIM/PNM设计的假设已不再适用于该场景，导致服务效率无法满足需求。
2. GPU-only基线方法在服务级目标下的吞吐量每TDP表现有待提升，训练相关的稀疏注意力方法运行效率也有改进空间。

🚀 提出的新方法与思路
**KARAT (KV-cache-resident Accelerator for Retrieval-based ATtention)**：通用近内存处理（PNM）设计，结合大LPDDR容量与适配检索索引器的通用计算，满足针对检索式稀疏注意力衍生的四项设计要求，操作强度优于针对低强度GEMV的原有PIM/PNM设计，可兼容多样化稀疏注意力算法。
**OFMS (Opportunistic, Fine-grained Micro-batch Scheduling)**：优化微批处理的调度方法，将专家all-to-all操作隐藏在另一微批的GEMM操作之后，减少微批交替产生的流水线气泡。
**CMR (Context-length-aware Micro-batch Rebalancing)**：微批重新平衡方法，考虑上下文长度的差异，均衡各微批的token数量，提升整体处理效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 服务效率（吞吐量每TDP） | 相较于GPU-only基线有显著提升 |
| 算法兼容性 | 支持多样化稀疏注意力算法，优于固定功能单元设计 |
| 流水线效率 | 通过OFMS和CMR减少了微批处理的流水线气泡 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| real agentic traces | 实际代理场景下的性能评估 |
| three state-of-the-art models | 不同模型的性能泛化评估 |

🎯 实验设置与评估指标
任务为针对百万token上下文的检索式稀疏注意力的解码阶段异构LLM服务。
| 指标 | 含义 |
| --- | --- |
| 吞吐量每TDP | 服务效率，越高越好（↑） |
| 训练式稀疏注意力方法改进度 | 方法运行效率，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPU-only baseline | 基础服务方法 | 仅使用GPU执行所有操作 |
| 现有PIM/PNM设计 | 内存附近处理方法 | 针对低强度GEMV设计，不适用检索式稀疏注意力场景 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅在论文明确包含时覆盖以下实验，未提及的写“论文未报告”：
- 主benchmark性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告
> 注：摘要中提及的2.09-6.13x、1.36-3.21x改进未明确对应表/图/章节，按要求无法定位来源，故不给出具体数值。

4. 关键结论和发现
- 组合KARAT、OFMS、CMR的异构LLM服务系统，在检索式稀疏注意力场景下可有效提升服务效率并兼容多样化算法。
- 针对检索式稀疏注意力的异构架构设计，需适配该场景的操作特性，原有PIM/PNM设计的假设已不适用。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：论文提出面向检索式稀疏注意力解码阶段的异构LLM服务系统，结合KARAT通用PNM设计、OFMS微批调度与CMR微批平衡方法，在服务效率和算法兼容性上实现显著提升。

</details>

---

### 4. [LowRank-SSM: Hardware-Software Co-Design for Rank-Reduced Mamba Acceleration on FPGA](https://arxiv.org/abs/2608.02954v1)

**Authors**: Haocheng Xu, Bhardwaj Bhat, Yu-an Chou, Zhiheng Chen, Leyao Han, Yifan Zhang, Ye Qiao, Saptarshi Mitra, Sitao Huang  
**Category**: cs.AR  
**Published**: 2026-08-05  
**Score**: 70.0  
**Type**: new  
**ArXiv ID**: 2608.02954v1  

#### Abstract
State Space Models(SSMs) such as Mamba and Mamba-2 achieve linear-time autoregressive inference, making them attractive for latency-sensitive and resource-constrained deployment. Yet their large input and output projection layers impose quadratic weight memory and off-chip bandwidth costs that bottl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LowRank-SSM: Hardware-Software Co-Design for Rank-Reduced Mamba Acceleration on FPGA
1. 论文的主要贡献和创新点
✅ 解决的问题：State Space Models（如Mamba、Mamba-2）虽具备线性时间自回归推理，适合低延迟、资源受限部署，但输入输出投影层的大权重带来二次权重内存与片外带宽开销，序列长度≥1024时该开销占每token运行时的60%以上；现有SSM加速器通过量化或激活稀疏性减少此类开销，但未将投影秩作为显式硬件设计变量，未探索准确性-吞吐量的系统权衡。
🚀 提出的新方法与思路
**软件端低秩分解与带状秩分配算法**：在软件侧采用后训练截断SVD分解输入输出投影权重，提出贪心带状秩分配算法，搜索每一带的秩向量，在满足用户指定的准确性约束下最小化权重存储。
**硬件端混合秩全流水线FPGA加速器**：在Xilinx Versal VC1902 FPGA上架设全流水线加速器，包含双路径投影（低秩路径与全秩路径）、融合选择性扫描单元、5个独立AXI主bundle以饱和DDR4带宽且无总线争用；通过每一带的运行时秩掩码实现零架构开销的全64层混合秩执行。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 吞吐量 | 相比SOTA提升2.19倍 |
| 能效比 | 相比SOTA提升2.03倍（功率与准确性相当） |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为Mamba模型在FPGA上的部署加速，评估指标为吞吐量（tokens/s，↑越高越好）、能效比（↑越高越好）
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有SSM加速器 | 现有SSM FPGA加速器 | 通过量化或激活稀疏性减少投影开销，未将投影秩作为显式硬件设计变量 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告
**效率对比**：混合秩INT8设计在Xilinx Versal VC1902（400MHz）下达到7.89 tokens/s，吞吐量较SOTA提升2.19倍，能效比较SOTA提升2.03倍（功率与准确性相当）
**跨域/zero-shot迁移**：论文未报告
**鲁棒性/扰动测试**：论文未报告
**消融实验**：论文未报告
💡 结论：LowRank-SSM框架通过软硬件协同设计，在满足准确性约束的前提下，实现了Mamba模型在FPGA上的显著吞吐量与能效提升。
4. 关键结论和发现
- 核心发现：将投影秩作为显式硬件设计变量，结合软件端低秩分解与硬件端混合秩执行，可在约束准确性的同时降低内存与带宽开销，提升FPGA上SSM的加速性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：LowRank-SSM通过软硬件协同设计，在FPGA上实现了Mamba模型的高效加速，兼顾准确性约束的同时，显著提升了吞吐量与能效比。

</details>

---

### 5. [SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs](https://arxiv.org/abs/2608.03573v1)

**Authors**: Kejian Zhu, Zhuoran Jin, Shangqing Tu, Hongbang Yuan, Yushi Bai, Kang Liu, Juanzi Li, Jun Zhao  
**Category**: cs.CL  
**Published**: 2026-08-05  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2608.03573v1  

#### Abstract
Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) exhibit fundamentally different behaviors in enhancing multi-task reasoning for large language models (LLMs). Our preliminary experiments revealed a phenomenon: SFT suffers from severe task conflicts under multi-stage training, whereas RL ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
1. SFT用于LLM多任务学习时，多阶段训练下存在严重任务冲突；
2. 现有研究未明确解释SFT与RL在多任务LLM训练中出现任务冲突、稳定共存的根本机制；
3. 缺乏解耦多任务训练以提升效率与灵活性的训练范式。

🚀 提出的新方法与思路
**Parallel-RL**：基于多任务梯度干扰的理论分析，提出的解耦多任务训练范式，核心是利用RL诱导的稀疏近似正交的跨任务参数更新特性，解耦多任务训练过程，解决SFT的任务冲突问题，同时提升多任务训练的效率与灵活性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多任务训练稳定性 | SFT多阶段训练存在严重任务冲突，RL可实现跨任务稳定共存 |
| 梯度干扰机制 | SFT梯度干扰为norm-limited（随绝对梯度幅度缩放），RL梯度干扰为variance-limited（受优势归一化与在线策略优化的梯度方差限制） |
| 参数更新特性 | RL诱导的跨任务参数更新稀疏且近似正交 |
| 训练效率与灵活性 | Parallel-RL解耦多任务训练，显著提升效率与灵活性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：提升LLM的多任务推理能力；指标及含义：论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SFT | 监督微调方法 | 多阶段多任务训练下存在严重任务冲突 |
| RL | 强化学习方法 | 多任务训练下可实现稳定共存 |
| Parallel-RL | 提出的训练范式 | 解耦多任务训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现
 1. 多任务LLM训练中，SFT存在严重任务冲突，而RL可实现跨任务稳定共存；
 2. SFT与RL梯度干扰机制存在本质差异：SFT梯度干扰为norm-limited，RL梯度干扰为variance-limited，该差异使得RL能生成近似正交的跨任务优化方向；
 3. RL诱导的跨任务参数更新稀疏且近似正交，是其可稳定多任务训练的核心原因。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文通过理论分析与实证验证揭示了SFT和RL在多任务LLM训练中任务表现差异的内在机制，并提出解耦多任务训练的Parallel-RL范式，以提升多任务训练的效率与灵活性。

</details>

---

### 6. [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](https://arxiv.org/abs/2608.03893v1)

**Authors**: Taekyung Heo, Rasoul Shafipour, Ritchie Zhao, Maximilian Golub, Mohammad Mahdi Kamani, Ritika Borkar, Makesh Tarun Chandran, Pantea Zardoshti, Bita Darvish Rouhani  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2608.03893v1  

#### Abstract
Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch. We propose cross-model KV cache transfer, where the receiver reuses the source's KV c...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse
1. 论文的主要贡献和创新点
✅ 解决的问题
生产部署中，LLM家族需在不同大小模型间进行切换，用于成本质量级联、对话中途切换、路由分配等场景，每次切换都会迫使接收模型重新执行预填充（prefill），造成不必要的开销。

🚀 提出的新方法与思路
**Closed-Form Ridge Mapper**：针对跨模型KV缓存转移设计的线性映射方案，核心流程分为三步：1. 对每个目标层，选择top-k个最具预测性的源层，拼接这些源层的KV作为输入；2. 映射前移除键的RoPE（旋转位置嵌入），使拟合具备位置无关性，可跨不同上下文长度复用；3. 使用包含500条FineWeb-Edu序列（每条1024 token）的小型校准集，拟合岭回归模型。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 部署效率 | 映射速度比重新预填充快2.7-25倍 |
| 精度保留 | 六组跨模型对中，四组可保留接收模型独立预填充准确率的73%-98% |
| 上下文适配 | 移除RoPE的设计使映射可跨不同上下文长度复用 |
| 多轮稳定性 | 在多轮对话交接场景下表现稳定 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| FineWeb-Edu | 小型校准集，用于拟合跨模型KV缓存的岭回归模型 |

🎯 实验设置与评估指标
任务：验证跨模型KV缓存转移的适配性，核心评估复用源模型KV缓存后接收模型的性能保留情况与效率提升。
| 指标 | 含义 |
| ---- | ---- |
| 性能保留率 | 复用KV缓存后的接收模型准确率与自身独立预填充准确率的比值，越高越好 |
| 映射速度提升倍数 | 重新预填充耗时与线性映射耗时的比值，数值越大效率越高 |
| HellaSwag准确率 | 通用语言推理能力评估指标，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 重新预填充（re-prefill） | 基准方法 | 需执行接收模型完整预填充流程，耗时高 |
| 非线性MLP映射 | 辅助修复方法 | 在线性映射失效场景下，可提升HellaSwag准确率保留率，最多提升37个百分点 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**Qwen3 14B→32B跨模型对线性映射的方差解释能力（来自摘要描述）**
| 指标 | 数值 |
| ---- | ---- |
| 单个源层解释目标键的方差占比 | 56% |
| 单个源层解释目标值的方差占比 | 32% |
| top-k个源层解释目标键的方差占比 | 79% |
| top-k个源层解释目标值的方差占比 | 65% |
💡 结论：同KV头数、每头维度匹配的跨模型KV对存在较强线性相关性，多源层可进一步提升对目标KV的预测能力。

**六组跨模型对的线性映射性能（来自摘要描述）**
| 指标 | 数值 |
| ---- | ---- |
| 线性映射性能保留率（四组有效场景） | 73%-98% |
| 线性映射失效场景数量 | 2组 |
| 非线性MLP对失效场景的HellaSwag准确率提升 | 最多+37pp |
| 线性映射相对重新预填充的速度提升 | 2.7-25倍 |
💡 结论：线性映射在多数跨模型场景可高效保留接收模型精度，结合非线性MLP可修复部分失效场景的精度损失。

其余实验类内容：论文未报告跨域/zero-shot迁移、鲁棒性扰动测试、消融实验的相关结果。

4. 关键结论和发现
- 主要发现：1. 当LLM家族的源模型与目标模型的KV头数、每头维度匹配时，跨模型KV对存在显著线性结构，单个源层可解释目标KV的部分方差，多源层可进一步提升解释能力；2. 提出的闭形式岭映射可在多数跨模型场景实现高效KV缓存复用与高比例精度保留，速度显著优于重新预填充；3. 线性映射失效场景下，非线性MLP可有效恢复精度。
- 方法局限性：论文未报告除线性映射在六组跨模型对中存在两组失效场景外的其他局限性细节。
- 未来工作：论文未明确提及未来工作相关内容。

> ✅ 总结一句话：该论文提出的闭形式岭映射跨模型KV缓存转移方法，可让LLM家族切换时复用源模型KV缓存以跳过预填充，在多数场景实现高比例精度保留与显著效率提升，结合非线性MLP可修复精度失效场景，为生产中LLM的灵活部署切换提供可行方案。

</details>

---

### 7. [Muon Meets Mamba: Spectral Optimization for State Space Models](https://arxiv.org/abs/2608.03941v1)

**Authors**: Arslan Battalov, Karim Kramin, Alexander Markotenko, Sofia Sinitsina  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 64.0  
**Type**: new  
**ArXiv ID**: 2608.03941v1  

#### Abstract
Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We comp...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Muon Meets Mamba: Spectral Optimization for State Space Models
1. 论文的主要贡献和创新点
✅ 解决的问题
Muon作为近期提出的优化器，其现有性能验证几乎仅针对Transformer模型，在状态空间模型上的表现尚未有充分报道，缺乏针对这类模型的适配性研究。

🚀 提出的新方法与思路
**受控协议对比实验**：采用控制变量法，仅调整不同权重组使用Muon训练的设置，对比Muon与AdamW在Mamba-2 130M模型上的性能表现，探究Muon在状态空间模型中的应用特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 权重组适配 | Muon应用于输出投影的表现显著优于应用于输入投影或同时应用于两者 |
| token效率 | 该优势在两个语料库、两个token预算下均成立，且训练超过计算最优点后仍持续 |
| 性能机制 | 排除条件数作为Muon性能提升的核心原因，性能提升与输入投影的条件数改善无关 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体名称，仅提及2个语料库 | 用于训练Mamba-2 130M模型，评估Muon与AdamW的性能表现 |

🎯 实验设置与评估指标
任务：论文未明确具体任务类型，仅开展Mamba-2 130M模型训练的对比实验
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告具体评估指标的定量定义 | 仅涉及token效率、计算最优点、条件数等相关指标维度 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| AdamW | 优化器 | 对比基准优化器 |
| Muon | 优化器 | 待评估的新型优化器，通过Newton-Schulz迭代正交化权重矩阵的更新，在谱范数下执行最速下降 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主实验（论文未提供表号）**
场景：在Mamba-2 130M模型上，控制不同权重组应用Muon训练的设置，对比AdamW的性能
结果：
1. Muon应用于输出投影单独训练时，性能优于Muon应用于输入投影训练或同时应用于两者的情况，核心优势为token效率；
2. 该token效率优势在两个语料库、两个token预算下均成立，且在训练超过计算最优点后仍持续存在；
3. Muon会降低其所训练投影的条件数，但性能提升的原因并非更好的输入投影，该投影并非Muon性能提升的关键因素。
💡 结论：在Mamba-2状态空间模型中，仅将Muon应用于输出投影即可获得最优的token效率表现，该特性与条件数无关，且在多种训练设置下保持稳定。
（其余实验如效率对比、跨域迁移等：论文未报告）

4. 关键结论和发现
- 主要发现：① Muon在状态空间模型Mamba-2上的性能与权重组选择高度相关，仅应用于输出投影时的token效率最优；② 该优势在不同语料库、token预算及训练阶段（超过计算最优点）均持续存在；③ Muon对训练投影条件数的优化并非性能提升的核心机制，性能提升的关键与输入投影的条件数无关。
- 方法局限性：仅针对Mamba-2 130M模型开展研究，未覆盖其他状态空间模型；未报告具体定量性能数值、数据集名称、任务类型等细节；未深入分析Muon在状态空间模型上性能表现的深层机制。
- 未来工作：可扩展研究Muon在更多状态空间模型上的应用；进一步探究Muon在状态空间模型上性能提升的内在机制，而非仅依赖谱范数或条件数。

> ✅ **总结一句话**：论文通过控制变量实验明确了优化器Muon在状态空间模型Mamba-2中应用于输出投影时可获得最优token效率，补充了Muon在非Transformer模型上的适配性研究，完善了其应用场景的验证。

</details>

---

### 8. [Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning](https://arxiv.org/abs/2608.02993v1)

**Authors**: Subrat Prasad Panda, Blaise Genest, Arvind Easwaran  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2608.02993v1  

#### Abstract
(Flat) Reinforcement Learning (RL) agents face significant challenges in environments with sparse rewards that require long-horizon reasoning. A compelling approach to improve sample efficiency is to incorporate knowledge into learning and decision-making. In standard Hierarchical RL (HRL), knowledg...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：Flat Reinforcement Learning (RL)智能体在稀疏奖励、长周期推理的环境中样本效率极低；现有标准分层强化学习（HRL）采用固定不可更新的知识形式，无法有效利用探索过程中习得的增量知识，导致样本效率提升受限。

🚀 提出的新方法与思路
**Neurosymbolic HRL with Incremental Knowledge (InK)**：该方法的高层符号组件基于可更新的增量知识（InK）表示执行符号规划（如$D^*$算法），低层goal-conditioned神经模块通过奖励塑形学习运动原语，实现神经符号结合的分层强化学习框架，高效利用探索积累的知识。
**Belief World Tree Search**：为在给定世界先验知识时实现最优符号规划，提出该方法用于上述神经符号框架的高层规划环节。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 知识利用 | 支持增量知识动态更新，解决标准HRL知识固定无法适配探索过程的问题 |
| 规划能力 | 结合$D^*$符号规划与Belief World Tree Search，实现高效长周期推理 |
| 样本效率 | 整合增量知识的框架可显著提升稀疏奖励长周期环境下的样本效率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|------|------|
| 导航任务相关环境 | 验证所提方法的样本效率提升效果 |

🎯 实验设置与评估指标
任务为导航任务，论文未明确报告评估指标及含义，故：
| 指标 | 含义 |
|------|------|
| 论文未报告 | 论文未报告评估指标相关内容 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Flat RL | 单层强化学习 | 无分层结构，稀疏奖励长周期环境样本效率低 |
| 标准HRL | 分层强化学习 | 知识采用固定不可更新形式，无法利用增量知识 |
| 本文方法（Neurosymbolic HRL with InK） | 神经符号分层强化学习 | 支持增量知识更新，结合符号规划与神经运动原语 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文仅提及“Experiments on navigation tasks demonstrate that incorporating InK substantially improves sample efficiency”，未报告具体表号、数值等定量结果，故：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现：
  1. 在导航任务中，整合增量知识的神经符号分层强化学习框架可显著提升稀疏奖励长周期环境下的样本效率；
  2. Belief World Tree Search能支持在给定世界先验知识时的最优符号规划，适配高层符号推理需求。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出结合增量知识（InK）的神经符号分层强化学习方法，通过高层基于可更新增量知识的符号规划与低层goal-conditioned神经运动原语的结合，解决了长周期稀疏奖励环境下分层强化学习样本效率不足的问题，经导航任务验证可显著提升样本效率。

</details>

---

### 9. [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](https://arxiv.org/abs/2608.03292v1)

**Authors**: Le Xiang, Zhicheng Guan, Hong Chen, Xiaocong Lin, Zhenghua Lei, Teng Hu, Bolei He, Long Zeng  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2608.03292v1  

#### Abstract
Long Document Visual Question Answering (LongDocVQA) requires Multimodal Large Language Models (MLLMs) to locate, integrate, and reason over heterogeneous document elements distributed across multiple pages. Existing approaches, including end-to-end MLLMs, retrieval-augmented generation (RAG) pipeli...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文总结：DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：
长文档视觉问答（LongDocVQA）要求多模态大语言模型（MLLMs）定位、整合、推理跨多页的异质文档元素，现有端到端MLLMs、检索增强生成（RAG）管道、文档代理等方法均缺乏显式机制，无法表示和验证推理过程中逐步构建的 grounded 证据，进而限制了答案准确性与可追踪性。

🚀 提出的新方法与思路
**分层证据图推理框架**：将长文档视觉问答转化为显式证据图推理任务，逐步执行证据定位、结构化文档解析、证据图推理，实现显式证据来源溯源。
**两阶段训练框架**：采用两阶段训练优化模型能力，第一阶段为联合监督微调（SFT），初始化证据定位和图推理能力；第二阶段为任务特定的Group Relative Policy Optimization（GRPO），结合专用奖励进一步优化上述能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 答案准确性 | 在多个长文档VQA基准上性能优于现有开源基线与专有MLLMs |
| 可追踪性 | 构造带节点级溯源的显式证据图，支持透明可验证的推理 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MMLongBench-Doc | 长文档视觉问答主基准性能测试 |
| LongDocURL | 长文档视觉问答主基准性能测试 |
| SlideVQA | 长文档视觉问答主基准性能测试 |

🎯 实验设置与评估指标
任务为长文档视觉问答（LongDocVQA），论文未报告具体评估指标名称，仅提及采用上述三个基准进行测试。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 端到端MLLMs | 现有方法类别 | 缺乏显式证据表示与验证机制 |
| 检索增强生成（RAG）管道 | 现有方法类别 | 缺乏显式证据表示与验证机制 |
| 文档代理 | 现有方法类别 | 缺乏显式证据表示与验证机制 |
| Qwen3-VL-8B-Instruct | 骨干模型 | DocTrace所采用的基础模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文仅在摘要中提及实验结果，未提供对应结果的表号信息：
1. 主benchmark性能：论文提及DocTrace在MMLongBench-Doc、LongDocURL、SlideVQA三个基准上性能优于Qwen3-VL-8B-Instruct骨干模型及其他基线方法，但未提供对应表号，无法获取具体定量数值；
2. 效率对比（FPS/参数量）：论文未报告；
3. 跨域/zero-shot迁移：论文未报告；
4. 鲁棒性/扰动测试：论文未报告；
5. 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：将长文档视觉问答建模为显式证据图推理任务，可同时提升答案准确性与推理可追溯性；分层证据图推理框架与两阶段训练策略能够有效优化长文档视觉问答任务性能。
- 方法局限性：论文未报告
- 未来工作：论文未明确说明

> ✅ **总结一句话**：DocTrace通过分层证据图推理框架与两阶段训练策略，解决了现有长文档视觉问答方法缺乏显式证据溯源的问题，在多个基准上实现了性能与可追溯性的双重提升。

</details>

---

### 10. [TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning](https://arxiv.org/abs/2608.03276v1)

**Authors**: Wonpyo Park, Seung-won Hwang  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2608.03276v1  

#### Abstract
Long-context inference with large language models is constrained by the linear growth of the key-value cache to sequence length. While pruning offers mitigation, prevailing methods determine query-specific token importance that cannot be reused across unseen queries. In contrast, we introduce TaskPr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文大语言模型推理受到KV缓存随序列长度线性增长的约束；现有基于剪枝的KV缓存优化方法是查询特定的，无法在未见过的查询中复用。
🚀 提出的新方法与思路
**TaskPress框架**：采用任务引导的查询无关KV缓存淘汰策略，不针对单个查询优化缓存，而是基于高级任务引导构建可复用的内存表示；将该任务引导作为prefill阶段的元查询，用于在下游查询发出前过滤不相关的token。
**零成本token重要性代理**：利用量化尺度因子作为零成本信号，检测有影响力的表示异常值，作为token重要性的高效代理。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 查询复用性 | 查询无关，可复用至未见过的下游查询 |
| 计算开销 | 利用零成本信号实现token重要性检测，无额外计算开销 |
| 缓存特性 | 可生成紧凑、能跨不同查询复用的KV缓存 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未说明具体数据集的相关信息 |
🎯 实验设置与评估指标
长上下文相关任务（论文未报告具体任务名称），论文未报告具体评估指标及其含义
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
4. 关键结论和发现
- 主要发现
    - TaskPress解决了现有KV缓存剪枝方法查询特定、无法跨查询复用的缺陷，通过任务引导构建可复用的内存表示适配不同查询需求。
    - 利用量化尺度因子作为零成本信号检测表示异常值，可高效实现token重要性的代理，无需额外计算开销。
    - TaskPress在各类长上下文任务中，能够生成紧凑且跨不同查询复用的KV缓存。
- 方法局限性
    论文未报告
- 未来工作
    论文未报告
> ✅ **总结一句话**：TaskPress是一种任务引导的查询无关KV缓存压缩框架，通过任务引导构建可复用内存表示，依托量化尺度因子实现零成本的token重要性检测，缓解了长上下文大语言模型推理中KV缓存随序列长度线性增长的问题，可生成能跨不同查询复用的紧凑KV缓存。

</details>

---

### 11. [FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs](https://arxiv.org/abs/2608.03852v1)

**Authors**: Amin Farajzadeh, Melike Erol-Kantarci  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2608.03852v1  

#### Abstract
This paper proposes FedCritic-MIMO, a communication-efficient serverless federated multi-agent reinforcement learning framework for AI-native resource control across independently deployable cell-level controllers in open and disaggregated 6G RANs. Controllers share no trainer, retain local actors a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs
1. 论文的主要贡献和创新点
✅ 解决的问题
开放和解耦6G RAN的复用1多小区大规模MIMO OFDMA部署场景中，各RAN控制器需联合管理用户调度、每流功率分配、波束成形、干扰及长期QoS，但现有方法或通信开销大、性能不足，或依赖集中式架构难以适配低控制器间信令限制，无法有效平衡性能与通信成本。
🚀 提出的新方法与思路
**FedCritic-MIMO框架**：通信高效的无服务器联邦多智能体强化学习框架，各控制器保留本地演员和个性化评论者，无共享训练器，仅交换兼容的共享评论者参数，适配无服务器架构。
**无线感知事件触发机制**：基于无线感知的触发规则，控制对等节点间评论者参数交换时机，减少不必要通信开销。
**自适应分层top-k稀疏评论者交换与误差反馈**：采用分层top-k策略仅交换部分评论者参数，结合误差反馈保证参数准确性，进一步降低通信量。
**平衡干扰感知融合规则**：结合各控制器的干扰情况，对交换的评论者参数进行平衡融合，保障协同优化效果。
**理论保证**：建立固定策略、冻结目标评论者回归模型下，平衡压缩对等评论者递归的有限时间平稳性和一致性保证。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能-通信权衡 | 在启发式、独立学习、集中式训练、通信-ablation基线中最优 |
| held-out吞吐量 | 最高 |
| 用户速率分布 | 改善 |
| 平均SINR | 提升 |
| QoS满意度 | 提高 |
| 每比特干扰成本 | 在学习基线中最低 |
| 评论者通信开销 | 相比无压缩分布式评论者交换降低76% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务：针对复用1的多小区大规模MIMO OFDMA部署场景，各RAN控制器协同管理用户调度、功率分配、波束成形、干扰及长期QoS。
| 指标 | 含义 |
| --- | --- |
| held-out吞吐量 | ↑越高越好 |
| 用户速率分布 | 改善用户速率分布（越优越好） |
| 平均SINR | ↑越高越好 |
| QoS满意度 | ↑越高越好 |
| 每比特干扰成本 | ↓越低越好 |
| 评论者通信开销 | ↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 启发式 | 基准对比方法 | 基于启发式规则的资源控制方案 |
| 独立学习 | 学习类基线方法 | 各控制器独立学习，无协作机制 |
| 集中式训练 | 学习类基线方法 | 采用集中式轨迹收集、参数服务器聚合的训练架构 |
| 通信-ablation基线 | 消融实验基线 | 用于验证通信模块有效性的对比方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验的具体表号、图号、章节或页码，仅提及在强干扰耦合的复用1仿真场景下的结果：FedCritic-MIMO在启发式、独立学习、集中式训练、通信-ablation基线中实现最优的性能-通信权衡；其held-out吞吐量最高，用户速率分布及平均SINR得到改善，QoS满意度提升，每比特干扰成本在学习基线中最低，且评论者通信开销相比无压缩分布式评论者交换降低76%。
💡 结论：FedCritic-MIMO可在有限的控制器间信令约束下，实现开放解耦6G RAN中多小区资源的协同控制，相较于对比基线能取得更优的性能-通信平衡。

4. 关键结论和发现
- 主要发现：1. FedCritic-MIMO通过对等节点间的兼容共享评论者参数交换，无需集中式轨迹收集或参数服务器聚合，即可实现各RAN控制器的协同，适配开放解耦6G RAN的无服务器架构需求；2. 在强干扰耦合的复用1多小区仿真场景下，FedCritic-MIMO的性能-通信权衡优于对比基线，在held-out吞吐量、QoS、通信效率等方面均有显著提升；3. 无线感知事件触发、自适应分层top-k稀疏评论者交换与误差反馈、平衡干扰感知融合是该框架实现性能提升的关键技术模块。
- 方法局限性：论文未报告具体的方法局限性。
- 未来工作：论文未报告具体的未来工作计划。

> ✅ **总结一句话**：FedCritic-MIMO是面向开放解耦6G RAN的通信高效无服务器联邦多智能体强化学习框架，通过低信令开销的对等节点间兼容共享评论者参数交换，实现多小区资源的协同控制，性能优于对比基线。

</details>

---

### 12. [CastFSR: A Fast--Slow--Reflect Agentic Reasoning Framework for Context-Aware Time Series Forecasting](https://arxiv.org/abs/2608.03031v1)

**Authors**: Xiaoyu Tao, Mingyue Cheng, Bokai Pan, Chuang Jiang, Huanjian Zhang, Tian Gao, Yaguo Liu, Qi Liu, Enhong Chen  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.03031v1  

#### Abstract
Time series forecasting is fundamental to decision-making in complex systems, where future dynamics are influenced not only by historical observations but also by evolving contextual features. Recent advances in large language models (LLMs) have extended forecasting beyond numerical extrapolation to...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CastFSR: A Fast--Slow--Reflect Agentic Reasoning Framework for Context-Aware Time Series Forecasting
1. 论文的主要贡献和创新点
✅ 解决的问题
现有结合大语言模型（LLM）的时间序列预测方法，在进行上下文感知预测时，缺乏明确的机制来识别相关上下文、推理上下文对未来动态的影响、验证预测结果是否符合时间与领域约束，难以满足复杂系统决策的需求。

🚀 提出的新方法与思路
**CastFSR框架**：将上下文感知时间序列预测建模为Fast-Slow-Reflect的agentic工作流。其中，快速思考阶段（Fast）对观测进行分析，选择轻量级预测器构建数据驱动的预测先验；慢 deliberation阶段（Slow）检索上下文证据，自适应确定有信息的回溯窗口，推理上下文如何重塑未来动态；反思阶段（Reflect）迭代优化预测，确保预测结果在时间、上下文和领域上的一致性。该框架支持两种部署方式：使用现成LLM的无训练推理，以及通过两阶段SFT与强化学习策略将协调能力迁移至紧凑LLM。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 上下文处理能力 | 具备明确的相关上下文识别、上下文影响推理、预测验证的机制 |
| 部署灵活性 | 支持off-the-shelf LLM的无训练推理，也可通过两阶段SFT与强化学习适配紧凑LLM |
| 预测性能 | 在公共数据集上一致优于代表性基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 公共数据集 | 验证CastFSR在上下文感知时间序列预测任务上的性能 |

🎯 实验设置与评估指标
任务：上下文感知时间序列预测
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 代表性基线方法 | 未知 | 未知 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：CastFSR是适用于上下文感知时间序列预测的agentic推理框架，在公共数据集上一致优于代表性基线方法
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CastFSR提出的Fast-Slow-Reflect agentic工作流解决了现有LLM-based时间序列预测方法缺乏上下文识别、推理与验证机制的痛点，支持灵活部署且在公共数据集上性能优于代表性基线。

</details>

---

### 13. [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](https://arxiv.org/abs/2608.03467v1)

**Authors**: Zhe Cao, Miaowen Wen, Fangjiong Chen  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.03467v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) com- monly optimizes each correct completion as an independent learning signal. In GRPO, this completion-level uniformity creates structure-level skew: recurring correct solution forms accumulate positive coefficient mass in proportion to how oft...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO
1. 论文的主要贡献和创新点
✅ 解决的问题
带可验证奖励的强化学习（RLVR）在GRPO中采用completion层面均匀优化，导致结构层面偏差：重复的正确解形式因采样次数多积累更多正系数，罕见解形式获得信用有限，形成多重性诱导的结构层面信用集中（multiplicity-induced structure-level credit concentration）问题。
🚀 提出的新方法与思路
**Cue-GRPO**：通过确定性策略提示（Strategy Cues）构造rollout-local的已验证正确轨迹划分，无需辅助模型推理，实现稀有解形式的信用再分配。
**Credit Redistribution (CR) under Judge Partitions (JP)**：可基于judge导出划分的信用再分配机制，适配不同划分逻辑。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| AIME重复采样性能 | 在高采样预算下提升显著，在Qwen2.5-Math-7B和Llama-3.1-8B-Instruct上均有效 |
| 训练开销 | 仅增加6%的wall-clock训练开销，属于低开销方案 |
| 适用场景 | 适配竞赛数学类的带可验证奖励的强化学习场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AIME | 评估数学竞赛任务下的重复采样性能 |
🎯 实验设置与评估指标
任务为：带可验证奖励的强化学习（RLVR）下的数学竞赛相关序列生成任务。
| 指标 | 含义 |
| --- | --- |
| AIME repeated-sampling performance | 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO | 强化学习算法 | 每个正确完成视为独立学习信号，存在结构层面信用集中问题，为对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：仅提到Cue-GRPO仅增加6%的wall-clock训练开销 over GRPO，无对应图/表号
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① Cue-GRPO在高采样预算下对AIME重复采样性能的提升最为显著；② 信用再分配机制（CR under JP）可依托judge导出的划分实现；③ 基于Strategy Cues的方法是低开销的RLVR设计，适配竞赛数学任务。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：该论文针对GRPO中重复正确解引发的信用集中问题，提出Strategy Cues辅助的低开销信用再分配方法，在数学竞赛任务的高采样预算下显著提升重复采样性能，且仅增加少量训练开销。

</details>

---

### 14. [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](https://arxiv.org/abs/2608.03119v1)

**Authors**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.03119v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) improves LLM reasoning but typically relies on ground-truth (GT) answers, limiting scalability. Voting-based label-free RLVR replace gold supervision with answer-level consensus from model samples. However, collapse arises when the same answer-le...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR
1. 论文的主要贡献和创新点
✅ 解决的问题
1）传统基于可验证奖励的强化学习（RLVR）方法依赖于 ground-truth（GT）答案，限制了模型的可扩展性；
2）现有基于投票的无标签RLVR方法存在缺陷：其使用相同的答案级信号既用于奖励估计又用于驱动token级策略优化，会导致模型出现collapse，模型倾向于直接强化答案标记而非提升推理能力。

🚀 提出的新方法与思路
**OM-GRPO（Outcome-Masked Group Relative Policy Optimization）**：该方法将奖励估计与策略优化解耦，通过掩码答案跨度上的梯度，同时借助软共识信号保留答案级奖励，从而将优化压力从答案标记转移至推理过程。
**Contrast-Augmented Reward**：该方法通过对现有轨迹进行低成本成对比较来细化奖励估计，无需额外的rollout操作。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 通用性能 | 在多种推理基准及三个不同大语言模型（LLM）骨干网络上，OM-GRPO始终优于现有无标签RLVR方法 |
| 优化稳定性 | OM-GRPO实现了与基于GT奖励的监督训练相当的优化稳定性 |
| Test-Time Training适配性 | 在Test-Time Training场景下，OM-GRPO相较于多数投票方法性能更优 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文仅提及使用多种推理基准（diverse reasoning benchmarks）开展实验，未明确具体数据集名称 |

🎯 实验设置与评估指标
任务：针对大语言模型（LLM）的推理任务，开展无标签RLVR方法的性能与稳定性测试。
评估指标：论文未明确报告具体评估指标的含义（无标注指标箭头方向或类型），仅提及性能对比与稳定性相关结果。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 现有无标签RLVR方法 | RLVR方法 | 采用答案级共识作为监督信号，但存在优化collapse问题 |
| 基于GT奖励的监督训练方法 | RLVR方法 | 依赖ground-truth答案，可扩展性受限，但性能稳定 |
| 多数投票方法 | RLVR方法 | 现有无标签RLVR的基准对比方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. **主基准性能（未标注来源）**：OM-GRPO在多种推理基准及三个不同LLM骨干网络上，始终优于现有无标签RLVR方法，且性能与基于GT奖励的监督训练相当，优化过程稳定；该结果未标注对应表号/图号。
2. **Test-Time Training场景性能（未标注来源）**：OM-GRPO在Test-Time Training场景下性能优于多数投票方法，具体提升数值未标注对应来源。
3. 效率对比（FPS / 参数量）：论文未报告
4. 跨域 / zero-shot迁移：论文未报告
5. 鲁棒性 / 扰动测试：论文未报告
6. 消融实验：论文未报告

💡 结论：上述实验结果来自论文摘要提及的内容，未明确标注具体来源信息。

4. 关键结论和发现
- 主要发现：1）OM-GRPO通过解耦奖励估计与策略优化，有效缓解了现有无标签RLVR方法的优化collapse问题；2）Contrast-Augmented Reward无需额外rollout即可细化奖励估计，降低了实现成本；3）OM-GRPO在多种推理基准和LLM骨干网络上性能优异，优化稳定，适配Test-Time Training场景。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的OM-GRPO无标签RLVR框架，通过解耦奖励估计与策略优化、引入无需额外rollout的对比增强奖励，在多种推理任务及LLM骨干网络上实现了优于现有无标签RLVR方法的性能，优化稳定且适配Test-Time Training场景。

</details>

---

### 15. [Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes](https://arxiv.org/abs/2608.03839v1)

**Authors**: Tao Jin, Phuong Minh Nguyen, Zhenzhu Yan, Teeradaj Racharak, Naoya Inoue  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.03839v1  

#### Abstract
Training-free speculative decoding drafts by matching an exact suffix of the context against a pool of earlier context. That lookup misses correct drafts already in the pool, most visibly on tool-calling traffic, where a request repeats almost everything but the few values minted for it, and where o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes
1. 论文的主要贡献和创新点
✅ 解决的问题：现有训练自由的精确匹配式投机解码drafting方法，在工具调用场景下存在核心矛盾——单token错误会导致池（pool）中已存在的正确草稿被丢弃，该问题源于寻址能力不足而非覆盖范围不够，具体表现为工具调用流量中，除少量新值外请求重复内容，错误token会直接丢弃其后方的正确续文。
🚀 提出的新方法与思路
**Semantic Re-keying Draft Source**：利用验证器（verifier）在每个已提交token处已计算的隐藏状态，对原始上下文池进行重新键化，生成第二个语义级草稿源，替代传统精确匹配的草稿生成逻辑。
**Merge with Lexical Drafter Tree**：设计合并机制，让上述语义草稿源可集成到现有词汇级草稿器的树结构中，兼容原有的草稿执行流程。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 匹配池与预算下的accepted length | 相比三个已发布草稿器基线，提升24-29% |
| API-Bank解码速度 | 达到4.4倍自回归解码速度，优于训练自由基线（3.9倍）及训练方法EAGLE-3（2.0倍） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 含密集工具调用基准的十个基准（ten benchmarks） | 定位现有训练自由精确匹配drafting方法的失效位置 |
| API-Bank | 开展解码效率对比实验 |
🎯 实验设置与评估指标
任务：训练自由投机解码性能评估，核心对比不同方法的接受长度与解码速度。
| 指标 | 含义与方向 |
|------|------------|
| accepted length | 模型最终接受的token序列长度，越高越好↑ |
| 自回归解码速度倍数 | 相比标准自回归解码的速度倍数，越高越好↑ |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Exact-match drafter | 训练自由方法 | 现有训练自由投机解码方法，通过精确匹配上下文后缀查找草稿 |
| 最强训练自由基线 | 训练自由方法 | 论文中对比的训练自由类强基线，API-Bank上解码速度为3.9倍 |
| EAGLE-3 | 训练方法（非训练自由） | 现有训练类投机解码方法，API-Bank上解码速度为2.0倍 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**匹配池与预算下的accepted length提升**
论文未报告具体表号，仅提及Oilbird在匹配池与预算条件下，相比三个已发布drafter基线，accepted length提升24-29%，为该场景最优。
💡 结论：Oilbird可有效提升投机解码的接受长度，优于三个对比的已发布drafter基线。

**API-Bank解码速度对比**
论文未报告具体表号，仅提及Oilbird在API-Bank上的自回归解码速度倍数为4.4x，为该场景最优。
💡 结论：Oilbird在API-Bank场景下的解码速度显著高于现有训练自由基线及训练类方法EAGLE-3。

主benchmark性能（除accepted length外的指标）：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 现有训练自由精确匹配式投机解码在工具调用场景的失效，核心是寻址问题而非覆盖问题，在密集工具调用基准中，该方法会丢失池内约一半的正确草稿。
- Oilbird通过基于验证器已计算的隐藏状态重新键化池并合并到词汇草稿树，有效提升了投机解码的接受长度。
- Oilbird在API-Bank上的解码速度优于现有训练自由基线与训练方法EAGLE-3。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：本文提出的训练自由投机解码方法Oilbird，通过利用验证器已计算的隐藏状态重新构建语义草稿源并合并到现有词汇草稿树，解决了传统训练自由方法在工具调用场景下的寻址失效问题，在匹配池与预算下提升了接受长度，并在API-Bank上实现了更高的解码速度。

</details>

---

### 16. [HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents](https://arxiv.org/abs/2608.02650v1)

**Authors**: Zian Zhai, Xingyu Tan, Gaowang Zou, Xiaoyang Wang, Wenjie Zhang  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.02650v1  

#### Abstract
Large language model (LLM) agents increasingly rely on external tools to complete complex real-world tasks. However, reliable tool-use planning remains challenging due to the limitations of implicit reasoning and the evolving nature of real-world execution environments. Existing tool-use agents typi...

---

### 17. [Screenshots or Tools? Eliciting Tool Use and Managing Multimodal Context in Hybrid GUI-MCP Computer-Use Agents](https://arxiv.org/abs/2608.03327v1)

**Authors**: Siqi Fan, Minghao Li, Xiaoqian Ma, Wenhui Tan, Xiusheng Huang, Juntong Wu, Liujie Zhang, Shuo Shang, Weihang Chen  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.03327v1  

#### Abstract
Hybrid computer-use agents can act through screenshots or call text tools. We find that having a tool available does not settle which way the effect goes. Under one identical GUI-MCP harness on the OSWorld-MCP benchmark (309 tasks), the same MCP tools improve a reasoning model by +4.0pp and degrade ...

---

### 18. [Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks](https://arxiv.org/abs/2608.03502v1)

**Authors**: Christophe D. Hounwanou, John Emeka Eze, Ya\'e Ulrich Gaba  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.03502v1  

#### Abstract
Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents. However, LLM-based agents struggle with long-horizon sequential decision tasks that require precise action optimization and environment interaction. Rei...

---

### 19. [Simulation-free and finite-time diffusion model](https://arxiv.org/abs/2608.03117v1)

**Authors**: Kentaro Kaba, Masayuki Ohzeki, Yuki Sughiyama  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.03117v1  

#### Abstract
The performance of generative diffusion models is determined by the choice of the reference diffusion process connecting the empirical and prior distributions. Conventional approaches typically trade off simulation-free training against finite-time generation. We propose a framework for designing th...

---

### 20. [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](https://arxiv.org/abs/2608.03077v1)

**Authors**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi  
**Category**: cs.CL  
**Published**: 2026-08-05  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.03077v1  

#### Abstract
Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation st...

---

### 21. [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](https://arxiv.org/abs/2608.03838v1)

**Authors**: Zhinan Liu, Jie Li, Mingyu Kang, Jiayi Ji  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.03838v1  

#### Abstract
Reasoning-based guard models improve LLM safeguards, but decoding explicit rationales for every interaction makes them costly to deploy. Although latent-reasoning methods reduce token generation by moving reasoning into continuous states, they remain underexplored for safety moderation and lack an i...

---

### 22. [Maglev: Sliding Recurrent Memory](https://arxiv.org/abs/2608.02870v1)

**Authors**: Bo Liu, Qiang Liu  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.02870v1  

#### Abstract
We introduce \ours{}, a recurrent Transformer architecture with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training. \ours{} consists of two coupled models: a prefiller $Q$, which leverages full attention\footnote{In practice, we use interleaved...

---

### 23. [Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement](https://arxiv.org/abs/2608.03733v1)

**Authors**: Chunyang Jiang, Pingping Zhang, Yuzhi Zhao, Wenao Ma, Zhijian Hou, Mengyang Wu, Yiyang Cai, Senkang Hu, Sitong Cheng, Chi-Min Chan, Wei Xue, Yike Guo  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.03733v1  

#### Abstract
Multimodal large language models (MLLMs) have achieved remarkable performance across vision-language tasks, but their progress depends heavily on large-scale, high-quality multimodal data that are costly to annotate. Self-augmentation offers a promising alternative by enabling models to expand their...

---

### 24. [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](https://arxiv.org/abs/2608.03782v1)

**Authors**: Ruihan Li, Jiyang Tan, Kailin Jiang, Huining Li, Hengyang Lu, Yu Huang, Qian Li, Yuntao Du  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.03782v1  

#### Abstract
Hallucination remains a critical challenge for developing trustworthy Multimodal Large Language Models (MLLMs). While existing benchmarks mainly focus on entity, attribute, and relation hallucinations, knowledge-related failures are often investigated separately, lacking a unified evaluation framewo...

---

### 25. [ArtECulture: Benchmarking Culture-Conditioned Visual Emotion Understanding in Multimodal Large Language Models](https://arxiv.org/abs/2608.03358v1)

**Authors**: Xiaolin Chen, Xuemeng Song, Wenhao Shi, Xianjing Han, Mong-Li Lee, Wynne Hsu  
**Category**: cs.CL  
**Published**: 2026-08-05  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.03358v1  

#### Abstract
Existing visual emotion understanding methods typically ignore cultural variations in emotional perception. We introduce culture-conditioned visual emotion understanding, a task that predicts the culture-specific emotional perception of a given image and explains the underlying rationale. Although r...

---

### 26. [Bayesian Data Reweighting Improves Multimodal Retrieval for Knowledge-Based Visual Question Answering](https://arxiv.org/abs/2608.02907v1)

**Authors**: Jingchen Sun, Shaobo Han, Ruiyi Zhang, Naresh Kumar Devulapally, Ming Liu, Yitao Long, Vishnu Suresh Lokhande, Changyou Chen  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.02907v1  

#### Abstract
Multimodal retrievers are essential for knowledge-based visual question answering, where they retrieve external evidence for image-question pairs. However, existing contrastive training methods typically treat all unmatched query-document pairs as equally informative negatives, which is problematic ...

---

### 27. [Schedule-Informed Temporal Fusion Forecasting of Hourly Airport Security-Checkpoint Throughput](https://arxiv.org/abs/2608.02950v1)

**Authors**: Yinxiao Zhang, Sen Wang, Yi Gao  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.02950v1  

#### Abstract
Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints. This study develops a framework that converts known flight schedules into temporally aligned signals for forec...

---

### 28. [Rethinking Modality Reliability in Multimodal Sentiment Analysis with Incomplete Observations](https://arxiv.org/abs/2608.03611v1)

**Authors**: Chunlei Meng, Jacqueline J. Pang, Pengbin Feng, Zhenyu Yu, Chun Ouyang, Zhongxue Gan  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.03611v1  

#### Abstract
Multimodal Sentiment Analysis (MSA) integrates text, audio, and vision to infer human affect, yet real-world multimodal observations are often incomplete. Existing methods for incomplete-observation MSA mainly follow two paradigms. Reconstruction-based methods recover missing information from observ...

---

### 29. [GeoID-PINN: Identifiability-Aware Regional Epidemic Inference with Geographic Coupling](https://arxiv.org/abs/2608.02633v1)

**Authors**: Weixiong Hua, Fan Bu  
**Category**: cs.LG  
**Published**: 2026-08-05  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.02633v1  

#### Abstract
Regional surveillance data reflect local transmission, reporting, seeding, and external infection pressure, which are difficult to identify separately. We introduce GeoID-PINN, a physics-informed neural network (PINN) for susceptible-infectious-recovered-deceased (SIRD) dynamics. The model represent...

---

### 30. [AI World Cup 2026: Benchmarking Large Language Models for End-to-End Football Tournament Prediction](https://arxiv.org/abs/2608.03416v1)

**Authors**: Jonaid Shianifar, Iias Faiud  
**Category**: cs.AI  
**Published**: 2026-08-05  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.03416v1  

#### Abstract
Large language models (LLMs) are now regularly asked to forecast real-world events, but comparisons are often difficult because models receive different information, use different tools, and are evaluated under different rules. This paper reports the completed \emph{AI World Cup} benchmark, in which...

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
