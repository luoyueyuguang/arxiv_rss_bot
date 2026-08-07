# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-07 07:10:46 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion](https://arxiv.org/abs/2608.05833v1)

**Authors**: Jiafan Li, Mengxue Yang, Jiaqi Zhu, Liang Chang, Ying Li, Hongan Wang  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 105.0  
**Type**: new  
**ArXiv ID**: 2608.05833v1  

#### Abstract
Knowledge graph completion (KGC) aims to infer missing entities or relations from incomplete graph structures, and has evolved into multimodal knowledge graph completion (MMKGC), where entities are associated with multiple modalities such as text and images. Traditional representation learning appro...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾是现有多模态知识图谱补全（MMKGC）方法的不同缺陷：1）传统嵌入式KGC方法在关系特定证据有限时表现不佳；2）基于LLM的推理方法将图结构线性化为文本提示，模糊结构拓扑且忽略关键视觉信息；3）视觉语言模型（VLMs）虽擅长多模态推理，但无法原生解释节点和边含复杂语义的结构化知识图谱拓扑。

🚀 提出的新方法与思路
**Visual Subgraph Reasoning Framework**：该框架整合三项互补能力以捕捉语义关联：通过表征学习识别全局拓扑依赖，利用VLMs分析本地多模态证据，借助预训练模型内置的常识知识；具体流程为：基于学习到的多模态嵌入，先提取紧凑且查询感知的子图，再经实证比较选定布局策略将子图转换为可视觉解释的图像，最后将可视化子图、实体图像、文本描述及候选答案组合为统一提示，供VLM推理缺失实体。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 结构拓扑保留 | 避免将图结构线性化丢失拓扑信息 |
| 多模态视觉利用 | 显式结合实体视觉信息，克服LLM方法忽略视觉信息的缺陷 |
| 关系证据有限场景适配 | 整合多维度语义关联，缓解传统嵌入式方法在关系证据有限时的性能问题 |
| VLM原生能力调用 | 通过可视化子图的形式适配VLM对结构化信息的理解能力 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
论文未报告具体任务、实验设置及评估指标

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
所有实验相关内容论文未报告，因此：
- 主benchmark性能（L2/碰撞率等）：论文未报告
- 效率对比（FPS/参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：论文未报告
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ViSR-KGC针对多模态知识图谱补全任务，提出整合表征学习、VLM多模态分析及预训练常识的视觉子图推理框架，解决了现有方法存在的拓扑信息丢失、视觉信息忽略及关系证据有限时性能不佳的痛点。

</details>

---

### 2. [Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference](https://arxiv.org/abs/2608.06025v1)

**Authors**: Jiming Su, Hantao Hua, Lujia Yin, Yiping Yao, Feng Zhu  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2608.06025v1  

#### Abstract
In simulation-in-the-loop decision-making systems, reinforcement learning (RL) inference is often constrained by simulator-side execution overhead, where workloads are highly dynamic and sensitive to runtime thread configurations. Existing multithreaded strategies struggle to match thread resources ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
仿真闭环决策系统中，强化学习（RL）推理受仿真端执行开销限制，工作负载高度动态且对运行时线程配置敏感；现有多线程策略无法在执行前或执行中匹配线程资源，导致资源竞争、调度开销和吞吐量降低。分点现有方法缺陷：静态策略无法适配动态工作负载；现有预测类方法性能不足；传统线程策略存在资源竞争与调度开销问题。

🚀 提出的新方法与思路
**AutoThread混合自适应线程调优方法**：该方法以**Physics-Informed Neural Operator (PINO)** 作为线程数预测器，结合**有限源M/M/1排队模型**约束和引导线程数预测，实现动态工作负载下快速准确的线程数估计；进一步引入**负载感知在线微调**机制，补偿预测误差并优化资源分配。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 线程适配能力 | 适配动态工作负载，避免资源竞争与调度开销 |
| 动态预测精度 | 结合物理信息神经网络预测与排队模型约束，提升复杂场景下线程数估计准确性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 评估AutoThread方法的线程调优性能 |

🎯 实验设置与评估指标
实验任务为仿真闭环决策系统中的高性能RL推理，核心目标为缓解仿真执行瓶颈，优化线程配置。
| 指标 | 含义（箭头） |
| --- | --- |
| 平均加速比 | ↑ 越高越好 |
| 平均吞吐量 | ↑ 越高越好 |
| 执行时间降低幅度 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 静态策略 | 传统多线程策略 | 线程配置固定，无法适配动态负载 |
| XGBoost | 现有线程预测方法 | 基于XGBoost的线程数预测模型 |
| Reinforcer | 现有线程预测方法 | 特定的线程数预测方案 |
| 现有SOTA线程调优方法 | 最先进方法 | 同领域当前最优的线程调优方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
💡 结论：因未提供对应实验的表号或正文细节，仅从摘要披露可知AutoThread性能优于静态策略、XGBoost、Reinforcer及现有SOTA线程调优方法。

4. 关键结论和发现
- 核心发现1：任务执行时间与调度时间的比值是确定最优线程数的关键决策因素
- 核心发现2：混合自适应线程调优方案（PINO预测+排队模型约束+在线微调）可适配动态工作负载下的仿真执行瓶颈
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：AutoThread通过集成Physics-Informed Neural Operator预测、有限源排队模型约束与负载感知在线微调，解决仿真闭环RL推理中动态负载的线程资源适配问题，性能优于现有多种线程调优方案。

</details>

---

### 3. [M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding](https://arxiv.org/abs/2608.05817v1)

**Authors**: Hong Jiang, Junnan Zhu, Jingwang Huang, Xiao Sun, Yuming Yang, Jiang Zhong, Ruirui Chen, Jingman Shi, Hao Wu, Nayu Liu, Xinyi Jiang, Kaiwen Wei  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.05817v1  

#### Abstract
Metaphor enables the understanding of abstract concepts through cross-domain mappings while conveying affective attitudes. In multimodal scenarios, visual and textual information jointly construct Target--Source mappings, requiring both conceptual understanding and cross-modal reasoning. However, ex...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：M³R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding
---
1. 论文的主要贡献和创新点
✅ 解决的问题
现有隐喻理解相关基准主要通过孤立子任务评估隐喻理解，且缺乏基于视觉和文本线索的证据性解释，无法有效评估模型是否建立了跨模态的目标-源映射，存在评估维度缺失、评估合理性不足的痛点。

🚀 提出的新方法与思路
**M³R-Bench基准**：构建包含1000个经人类验证的图像-文本实例的统一基准，基于概念隐喻理论和非字面语言理解理论，提供隐喻发生、目标-源映射、情感以及“证据识别-映射建立-情感推理”阶段式解释的联合注释，为多模态隐喻理解提供全面的评估框架。
**M³R-Reasoner**：针对现有模型存在的跨模态证据-映射不匹配问题，提出结合课程式推理监督与任务感知强化学习的方法，使模型推理与隐喻解释实现对齐。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
评估基准 | 具备证据 grounding，提供多维度联合注释，可有效评估模型跨模态映射的合理性
模型性能 | 8B参数规模的M³R-Reasoner在多模态隐喻理解相关指标上优于更大的专有MLLMs

---
2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
M³R-Bench | 作为多模态隐喻理解的基准数据集，用于评估模型的隐喻理解能力

🎯 实验设置与评估指标
任务为统一的多模态隐喻理解任务，评估指标包含四个统一任务指标、视觉证据证明分数、情感证明分数以及平均 rubric 分数。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
主流大型多模态语言模型（如GPT-5.5、Claude-Sonnet-4.6） | 基线模型 | 当前领域主流模型，用于与提出方法对比性能

---
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：论文通过实验验证，8B参数的M³R-Reasoner在相关多模态隐喻理解指标上优于更大的专有MLLMs，解决了现有模型存在的跨模态证据-映射不匹配问题。

---
4. 关键结论和发现
- 主要发现：①现有多模态隐喻理解模型常忽略视觉证据，依赖浅层次文本线索，存在跨模态证据-映射不匹配的问题；②8B参数的M³R-Reasoner在多模态隐喻理解的多个关键指标上优于更大的专有MLLMs，包括视觉证据和情感解释相关指标。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了基于证据的多模态隐喻理解统一基准M³R-Bench与对应的推理方法M³R-Reasoner，有效解决了现有模型的跨模态证据-映射不匹配问题，在相关任务上取得了优于大型专有多模态语言模型的性能。

</details>

---

### 4. [PaDoc: Layout-Grounded Parallel Decoding for Document Parsing](https://arxiv.org/abs/2608.06146v1)

**Authors**: Hao Yu, Jiabo Zhan, Kang Liu, Linnan Zhao, Dongxu Yue, Rui Chen, Jinglin Wang, Chong Sun, Chen Li, Jing Lyu, Chun Yuan  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.06146v1  

#### Abstract
End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-l...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PaDoc: Layout-Grounded Parallel Decoding for Document Parsing
1. 论文的主要贡献和创新点
✅ 解决的问题
现有端到端文档解析器将页面布局和区域内容序列化为自回归序列，解码长度随总内容增长；基于裁剪的两阶段解析器虽具备区域级并行潜力，但存在重复视觉预填充、页面上下文碎片化的缺陷。

🚀 提出的新方法与思路
**布局分支结构设计**：将预测的页面布局视为共享页面表示上的分支结构，为并行解码提供结构基础。
**前缀条件因子分解**：在区域充足假设下，推导布局流与区域内容分支并行推进的前缀条件因子分解，将解码深度降至最长布局-内容路径的长度。
**实现细节**：在单个MLLM中嵌入该因子分解，通过打包变长祖先注意力保留标准下一个token训练所需的可见性，通过掩码并行解码创建分支，由vLLM后端将分支作为并发请求服务，利用缓存驻留的共享前缀实现复用。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 解析性能 | OmniDocBench Full数据集上，端到端整体得分达顶尖水平，布局F1、文本编辑、公式识别指标表现最优 |
| 推理效率 | 384页子集测试中，多并发场景下为最快端到端解析器，有效页面吞吐量提升67.4-118%，P95延迟降低39.2-54.9% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| OmniDocBench Full | 主解析性能测试 |
| OmniDocBench的384页子集 | 推理效率对比测试 |

🎯 实验设置与评估指标
任务：端到端文档解析，评估文档整体解析、元素识别性能及推理效率。
| 指标 | 含义及方向 |
| --- | --- |
| Overall layout F1 | 布局识别F1值，越高越好 |
| Overall | 端到端整体得分，越高越好 |
| Text Edit | 文本编辑指标，越低越好 |
| Formula CDM | 公式识别的CDM指标，越高越好 |
| 有效页面吞吐量 | 单位时间处理的有效页面数，越高越好 |
| P95 latency | 第95百分位延迟，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Sequential SFT基线 | 端到端文档解析器 | 采用自回归序列化解码页面布局和区域内容序列 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（OmniDocBench Full）**
| 指标 | 数值 | 是否最优 |
| --- | --- | --- |
| Overall layout F1 | 91.1 | 否 |
| Overall | 94.24 | ✅ |
| Text Edit | 0.038 | ✅ |
| Formula CDM | 95.59 | ✅ |
💡 结论：PaDoc在OmniDocBench Full数据集上的端到端文档解析性能达到顶尖水平，布局与各元素识别指标表现优异。

**效率对比（384页子集，A800 GPU，五并发水平）**
| 指标 | 相对同骨干Sequential SFT基线的变化 | 是否最优 |
| --- | --- | --- |
| 有效页面吞吐量 | 提升67.4-118% | ✅ |
| P95 latency | 降低39.2-54.9% | ✅ |
💡 结论：PaDoc在多并发场景下的推理效率显著优于基线方法，是当前最快的端到端文档解析器。

其他实验：论文未报告

4. 关键结论和发现
- 主要发现
1. PaDoc通过布局分支结构设计和前缀条件因子分解，在保留全页面上下文的同时实现并行解码，解决了现有端到端文档解析方法的核心痛点。
2. 在OmniDocBench Full数据集上，PaDoc的端到端解析性能达到顶尖，布局F1、文本编辑、公式识别指标均为最优。
3. 在多并发推理场景下，PaDoc的推理效率大幅提升，适配高并发的文档处理需求。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PaDoc是一种布局基础的并行解码文档解析方法，兼顾全页面上下文保留与并行解码优势，在解析性能和推理效率上均显著优于现有端到端文档解析器，尤其适合多并发场景的文档处理任务。

</details>

---

### 5. [TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure](https://arxiv.org/abs/2608.06007v1)

**Authors**: Yuhan Zhou, Yuchu Luo, Hao Nie, Wangrunze Lv, Yu Zhou, Yibo Zhu, Daxin Jiang, Chenren Xu  
**Category**: cs.DC  
**Published**: 2026-08-07  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2608.06007v1  

#### Abstract
Modern LLM infrastructure increasingly manages tensors not only as computation data, but also as persistent states shared across distributed components. Existing systems optimize individual tensor management tasks, such as model weight loading, KV cache management, and checkpoint synchronization, by...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure》
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM基础设施中的张量管理系统针对模型权重加载、KV缓存管理、检查点同步等单个任务做了优化，但任务特定机制与执行引擎、网络、存储后端深度集成，形成孤立孤岛，阻碍张量管理策略在不同LLM工作负载间的复用与组合。
🚀 提出的新方法与思路
**Tensor-as-a-Service (TaaS)** 作为核心抽象层，将张量状态管理与计算逻辑解耦；设计实现TensorCast，该分布式张量管理层提供一流的张量抽象、可编程生命周期原语、分离张量管理策略与执行机制的运行时，集成到vLLM和SGLang，可在各类张量生命周期工作负载中透明利用分布式执行与数据移动。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 系统设计 | 解耦张量管理策略与计算逻辑，避免孤立孤岛 |
| 策略复用性 | 支持跨LLM工作负载的张量管理策略复用与组合 |
| 跨组件优化能力 | 支持实现新的跨组件优化策略 |
| 工作负载适配性 | 适配模型权重物化、权重同步、KV缓存管理、可编程请求路由等多种张量生命周期工作负载 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体使用的数据集内容。
🎯 实验设置与评估指标
任务为在模型权重物化、权重同步、KV缓存管理、可编程请求路由等多种张量生命周期工作负载，以及高度并发多回合agent工作负载下评估性能；
| 指标 | 含义及方向 |
| ---- | ---- |
| 中位数TTFT | 首帧生成时间，越低越好（↓） |
| 其他指标 | 论文未报告 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有专门张量管理系统 | 基线方法 | 针对特定张量管理任务深度集成到执行引擎等后端，性能专门化但策略复用性差 |
| TensorCast | 提出方法 | 解耦张量管理策略与执行机制，支持策略复用与跨组件优化，可集成到vLLM、SGLang |

3. 主要实验结果和性能指标
📊 定量结果汇总
**高度并发多回合agent工作负载下的TTFT性能（场景：多回合agent工作负载）**
| 方法 | 中位数TTFT提升率 | 说明 |
| ---- | ---- | ---- |
| TensorCast实现的可编程策略 | 93.2% ✅ | 高度并发多回合agent工作负载下的性能提升 |
| 现有专门张量管理系统 | 论文未报告 | 未明确给出具体提升率数值 |
💡 结论：TensorCast支持的可编程策略在高度并发多回合agent工作负载下大幅降低中位数TTFT，同时具备与现有专门张量管理系统相当的性能。
其他实验如主benchmark性能、效率对比、跨域迁移、鲁棒性测试、消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：1. 张量生命周期管理是当前LLM基础设施中缺失的核心抽象层，采用TaaS思路解耦张量管理与计算逻辑可解决现有系统形成的孤岛问题；2. TensorCast在各类张量生命周期工作负载中实现了与专门张量管理系统相当的性能，同时支持跨组件优化策略；3. 基于TensorCast实现的可编程策略可在高度并发多回合agent工作负载下将中位数TTFT提升93.2%。
- 方法局限性：论文未报告方法的局限性内容。
- 未来工作：论文未报告具体未来工作内容。
> ✅ **总结一句话**：论文提出TensorCast这一分布式张量管理层，通过解耦张量状态管理与计算逻辑，解决了现有LLM基础设施中张量管理策略复用性差的问题，在多类工作负载中达到与专门系统相当的性能，同时显著提升高度并发多回合agent工作负载下的中位数TTFT。

</details>

---

### 6. [Seeing Is Not Deciding: Can Multimodal LLMs Act as Effective CEOs?](https://arxiv.org/abs/2608.05864v1)

**Authors**: Yuyang Dai, Xueqing Peng, Yuxia Wang, Preslav Nakov, Zhuohan Xie  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.05864v1  

#### Abstract
Large language models are increasingly applied as autonomous decision-making agents. However, in executive business decisions, existing benchmarks are limited to textonly settings. This makes it unclear whether models can perceive visual business evidence and effectively integrate it to improve deci...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Seeing Is Not Deciding: Can Multimodal LLMs Act as Effective CEOs?

## 1. 论文的主要贡献和创新点
✅ 解决的问题：现有将大语言模型应用于自主决策的工作，其基准测试仅局限于纯文本场景，无法验证模型感知、整合视觉业务证据以提升决策质量的能力，在高管商业决策任务上存在评估缺口。

🚀 提出的新方法与思路：**C-SUITEBENCH**：构建受控多模态基准，包含5类决策任务、共50个配对场景（纯文本与多模态两种条件），将9个前沿模型置于首席执行官角色，开展决策能力评估。

🔍 相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 评估场景范围 | 现有方法仅覆盖纯文本决策场景；本基准包含纯文本与多模态配对两种条件，可评估多模态整合下的CEO决策能力 |
| 任务覆盖 | 现有方法未涉及高管商业决策场景；本基准覆盖5类CEO决策任务，适配高管角色设定 |
| 评估方式 | 现有方法未针对CEO角色开展评估；本基准以CEO角色设定评估模型决策能力，更贴合高风险业务决策需求 |

## 2. 核心实验方法和设置
📚 使用的数据集：
| 数据集 | 用途 |
| ---- | ---- |
| C-SUITEBENCH | 包含5类决策任务共50个配对场景（纯文本、多模态条件），用于9个前沿模型作为CEO的多模态决策能力评估 |

🎯 实验设置与评估指标：将9个前沿模型设定为首席执行官角色，在纯文本和多模态配对条件下完成5类商业决策任务；论文未报告具体评估指标的名称、计算方式及对应的量化含义。

⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 9个前沿模型 | 大语言模型/多模态大语言模型 | 作为被评估对象，在CEO角色下开展纯文本与多模态条件的决策任务 |

## 3. 主要实验结果和性能指标
📊 定量结果汇总：
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未提供各视觉模块启用/禁用的对比表格及具体性能指标，仅提及消融实验显示多模态整合悖论源于信号拥挤，每个视觉通道单独有效但组合会破坏约束满足。

## 4. 关键结论和发现
- 主要发现：①多模态输入可一致提升模型的证据导向推理能力，该提升在风险预测和董事会层面论证任务中表现最显著、最可靠；②存在多模态整合悖论：添加视觉业务信息会提升模型的视觉定位能力，但会损害所有9个模型的受限资源分配任务表现；③多模态LLM的视觉感知能力与约束动作能力是可分离的瓶颈，不加选择地增加视觉信息会损害高风险决策的质量。
- 方法局限性：论文未明确报告除多模态整合悖论外的其他局限性。
- 未来工作：针对多模态代理提出选择性视觉接地策略，优化面向高风险高管决策的AI系统性能。

> ✅ **总结一句话**：该研究针对现有纯文本决策基准的缺陷，构建了受控多模态基准C-SUITEBENCH，评估了9个前沿模型作为CEO的决策能力，发现多模态输入对证据导向推理有增益但存在损害受限资源分配的多模态整合悖论，为CEO角色AI系统的优化提供了方向。

</details>

---

### 7. [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](https://arxiv.org/abs/2608.05643v1)

**Authors**: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, Dean F. Hougen  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.05643v1  

#### Abstract
Test-time scaling improves LLM reasoning by using additional inference compute, but wider sampling alone can suffer from diminishing returns: new rollouts often repeat existing answer patterns instead of adding useful reasoning diversity. Verifier-based selection offers an alternative, but its perfo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
测试时缩放技术通过增加额外计算提升LLM推理性能，但存在两大核心痛点：1）宽采样策略面临收益递减问题，新生成的推理轨迹常重复已有答案模式，缺乏有效推理多样性；2）基于外部验证器的选择策略，性能高度依赖外部奖励模型的校准效果，鲁棒性受限。

🚀 提出的新方法与思路
**广度-深度优化框架（Breadth-Depth Refinement Framework）**：该框架无需外部验证器，依托测试时计算实现更高效的推理优化，分为三个核心步骤：首先，采样多个独立的推理轨迹（rollouts），通过广度策略保留多样化初始尝试；其次，对每个采样轨迹执行迭代自我批判与自我修正，通过深度策略修复推理过程中的局部错误；最后，采用多数投票机制聚合所有优化后的候选答案，输出最终结果。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 外部模型依赖 | 无（verifier-free，不依赖外部验证器） |
| 推理多样性与纠错 | 兼具广度采样的多样性与深度修正的错误修复能力，避免宽采样的收益递减问题 |
| 跨方法性能表现 | 在多个数学推理基准上，一致优于greedy decoding、majority voting、verifier-based best-of-N、beam search、lookahead decoding等基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| AIME24 | 数学推理性能评估 |
| AIME25 | 数学推理性能评估 |
| AMC | 数学推理性能评估 |
| OlympiadBench | 数学推理性能评估 |
| MATH500 | 数学推理性能评估 |

🎯 实验设置与评估指标
任务为LLM数学推理准确性评估，采用的评估指标及含义如下：
| 指标 | 含义（箭头方向） |
|------|------------------|
| 准确率 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| greedy decoding | 测试时推理方法 | 单一生成最可能答案，无多样性，易陷入局部最优 |
| majority voting | 测试时推理方法 | 对多个生成答案投票选多数，依赖初始多样性，无纠错能力 |
| verifier-based best-of-N | 测试时推理方法 | 基于外部奖励模型选N个生成答案中的最优，性能受验证器校准影响 |
| beam search | 测试时推理方法 | 保留多个候选轨迹，按概率排序，易重复已有模式 |
| lookahead decoding | 测试时推理方法 | 通过提前预测提升效率，无自我修正功能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**示例实验结果（Qwen2.5-1.5B模型）**
| 基准数据集 | 基于验证器的基线准确率 | 论文方法准确率 |
|------------|------------------------|----------------|
| MATH500 | （最强基线，论文未明确数值） | 58.0% |
| AMC | 25.0% | 32.5% |

💡 结论：在Qwen2.5-1.5B模型上，论文提出的方法在MATH500和AMC基准上相比基于验证器的基线均实现准确率提升，且优于多种现有测试时推理基线方法。

4. 关键结论和发现
- 主要发现：
  1. 测试时计算若用于优化采样轨迹（而非仅增加采样数量或依赖外部验证器），可更有效提升LLM的数学推理性能；
  2. 广度保留多样初始尝试、深度修复局部推理错误的策略，搭配多数投票聚合，能解决宽采样的收益递减问题；
  3. 该方法在AIME24、AIME25、AMC、OlympiadBench、MATH500等多个数学推理基准上，对多种开放权重模型均一致优于基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了一种无外部验证器支持的广度-深度优化框架，通过测试时的多样化采样、迭代自我修正与多数投票聚合，有效提升了LLM在数学推理任务上的性能，优于多种现有测试时推理方法。

</details>

---

### 8. [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.05987v1)

**Authors**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.05987v1  

#### Abstract
Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, pr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有带可验证奖励的强化学习在长 horizon多回合代理任务中，难以对决定结果的少数关键决策进行信用分配；近期的特权自蒸馏方法虽提供更密集的监督，但局部信号如何表示序列信用的问题仍未明确。

🚀 提出的新方法与思路
**递归贝叶斯信念更新机制**：将token级的师生对数概率差距聚合为turn级证据，在对数几率空间递归更新贝叶斯信念状态，把稀疏结果监督转化为turn级信用信号，通过连续状态间的边际信念修订识别关键决策回合。
**无评论家Turn级信用分配方法**：针对代理强化学习设计turn级信用分配方案，无需额外评论家，也无需额外rollouts，完全兼容标准策略优化框架。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务性能 | 在ALFWorld基准上优于GRPO及强自蒸馏基线 |
| 资源需求 | 无需额外评论家，无需额外rollouts，计算开销低 |
| 框架兼容性 | 完全兼容标准策略优化 |
| 关键决策识别 | 可通过边际信念修订有效识别影响结果的关键回合 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ALFWorld、WebShop、Search-QA | 评估AgentOPSD的性能表现 |

🎯 实验设置与评估指标
实验采用Qwen2.5模型的3B和7B参数规模，针对代理强化学习任务开展评估；核心评估指标为任务成功完成率，该指标越高越好（↑）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GRPO | 代理强化学习基线 | 现有主流代理RL方法 |
| 强自蒸馏基线 | 自蒸馏基线 | 近期相关特权自蒸馏方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅覆盖论文明确报告的实验内容：

**表1：ALFWorld性能（场景：ALFWorld）**
| 方法 | Qwen2.5-7B 任务成功率 |
| ---- | ---- |
| AgentOPSD | 89.1% ✅ |
| GRPO | 论文未报告 |
| 强自蒸馏基线 | 论文未报告 |
💡 结论：AgentOPSD在ALFWorld任务上的成功率优于GRPO及强自蒸馏基线。

其他实验结果：
- 主benchmark性能（WebShop、Search-QA）：论文未报告
- 效率对比（FPS、参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：
**表2：消融实验（模块：Turn级聚合、历史依赖递归信念更新）**
| 模块 | 启用状态 | ALFWorld任务成功率 |
| ---- | ---- | ---- |
| Turn级聚合 | ✅ 启用 | ✅ 最优 |
| Turn级聚合 | ❌ 禁用 | ❌ 较差 |
| 历史依赖递归信念更新 | ✅ 启用 | ✅ 最优 |
| 历史依赖递归信念更新 | ❌ 禁用 | ❌ 较差 |
💡 结论：AgentOPSD的性能增益主要来自Turn级聚合和历史依赖递归信念更新两个核心模块。

4. 关键结论和发现
- 主要发现：AgentOPSD在ALFWorld代理任务上相比GRPO及强自蒸馏基线取得了更优的性能；Turn级证据聚合与历史依赖递归信念更新是AgentOPSD性能提升的核心因素。
- 方法局限性：仅在ALFWorld任务上报告了定量结果，未报告WebShop、Search-QA等其他基准的性能数据；未报告效率、跨域迁移、鲁棒性等方面的实验结果。
- 未来工作：论文未报告。

> ✅ **总结一句话**：AgentOPSD是一种面向代理强化学习的无评论家递归自蒸馏方法，通过turn级信用分配将稀疏结果监督转化为有效信号，在ALFWorld基准上实现了优于相关基线的性能表现。

</details>

---

### 9. [Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control](https://arxiv.org/abs/2608.05989v1)

**Authors**: Xinwei Liu, Junyuan Liang, Jianting Zhang, Wuhui Chen  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.05989v1  

#### Abstract
Sample-efficient policy learning from pixels is a long-standing challenge in reinforcement learning (RL). Recent dynamics-based representation learning methods have significantly improved the sample efficiency of model-free visual RL by learning dynamics-aware representations through auxiliary predi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于动力学的表征学习方法分为自预测类（潜空间辅助预测）和观测预测类（观测空间辅助预测），仅依赖单一预测目标的方法在训练数据有限时，于挑战性视觉控制任务表现不佳；其中观测预测类不直接正则化潜表征的长期时间可预测性，自预测类若直接在共享表征上施加预测目标会过度约束表征，无法提升性能。

🚀 提出的新方法与思路
**OG-SPR**：用于视觉连续控制的模型-Free RL算法，学习兼具潜空间时间可预测性、观测级动力学接地性的表征，包含两个核心辅助目标：多步潜空间自预测、下一观测预测；针对直接对共享表征施加潜自预测目标的问题，引入两个轻量适配器用于潜空间自预测，使共享表征能受益于时间预测信号，又不被过度约束。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 表征特性 | 同时支持潜空间时间预测性、观测级动力学接地性 |
| 挑战性任务表现 | 在狗、人形机器人等挑战性视觉控制领域性能增益显著 |
| 样本利用效率 | 在训练数据有限场景下优于单一预测目标的SOTA方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| DeepMind Control Suite | 验证算法性能的基准视觉连续控制任务数据集 |

🎯 实验设置与评估指标
任务为DeepMind Control Suite的28个视觉连续控制任务，评估指标论文未报告具体定义与方向。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告具体基线名称 | 自预测类RL方法 | 依赖潜空间单一预测目标的SOTA方法 |
| 论文未报告具体基线名称 | 观测预测类RL方法 | 依赖观测空间单一预测目标的SOTA方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（DeepMind Control Suite 28个视觉控制任务）**
论文未报告具体实验数据与对应表号，仅提及OG-SPR在该基准上的聚合性能优于SOTA的自预测类、观测预测类RL方法，挑战性领域（狗、人形机器人）增益更明显。
💡 结论：OG-SPR在训练数据有限的挑战性视觉连续控制任务上，整体性能优于仅依赖单一预测目标的SOTA动力学表征学习类RL方法。
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）结合潜空间自预测与观测空间预测的OG-SPR，比单一预测目标的动力学表征学习方法更适配训练数据有限的挑战性视觉连续控制任务；2）直接对共享表征施加自预测目标会过度约束表征，轻量适配器模块可平衡时间预测信号利用与表征灵活性；3）OG-SPR在狗、人形机器人等挑战性视觉控制领域的性能增益显著。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出的OG-SPR算法通过轻量适配器融合潜空间自预测与观测空间预测，在训练数据有限的挑战性视觉连续控制任务上实现了优于SOTA方法的聚合性能。

</details>

---

### 10. [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](https://arxiv.org/abs/2608.05254v1)

**Authors**: Hongbo Ma, Bangji Yang, Yunqian Selina Cheng, Jiajun Fan, Hanwen Zhang, Ge Liu  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2608.05254v1  

#### Abstract
Large language models can derive a plausible mathematical object yet still violate explicit requirements--for example, by omitting a modular reduction, returning a non-integer, or using the wrong encoded answer form. We introduce Constraint-First Reasoning (CFR), a training-free two-stage prompting ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving
1. 论文的主要贡献和创新点
✅ 解决的问题：大语言模型在求解数学问题时，能推导看似合理的数学对象，但常违反问题的显式要求（如遗漏模运算、返回非整数、使用错误的答案编码形式）；现有方法缺乏对答案空间中明确约束的系统性利用。
🚀 提出的新方法与思路
**Constraint-First Reasoning (CFR)**：一种无训练的两阶段提示协议，Stage1提取并总结问题蕴含的约束，Stage2在求解过程中对中间及最终结果进行约束检查。
**Routed-CFR**：一种适配优化机制，仅当纯文本正则路由器检测到限制性提示时，激活上述两阶段CFR协议；否则使用直接链式思考（direct chain-of-thought, CoT）。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练成本 | 无额外训练需求，仅依赖提示协议调整 |
| 约束利用 | 显式提取并校验数学问题答案空间中的约束 |
| 方法适配性 | 自适应触发机制，兼顾通用与约束性问题的求解效率 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AIME | 数学问题求解性能评估 |
| CMIMC | 数学问题求解性能评估 |
| BRUMO | 数学问题求解性能评估 |
| AIMO_AMC | 数学问题求解性能评估 |
| OlympiadBench | 数学问题求解性能评估 |
🎯 实验设置与评估指标：任务为数学问题求解，论文未报告具体评估指标及对应数值，仅提及方法相对直接CoT有性能提升。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Direct CoT | 基线方法 | 采用直接链式思考，无约束检查流程 |
3. 主要实验结果和性能指标
📊 定量结果汇总：论文未报告主benchmark性能的具体定量数值；效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验均论文未报告。
4. 关键结论和发现
- 主要发现：1. CFR作为无训练的提示协议，通过两阶段流程利用答案空间约束，可提升大语言模型的数学问题求解性能；2. Routed-CFR的自适应触发机制，根据正则路由器检测结果选择求解策略，优化了方法的适用性；3. CFR的性能收益依赖于问题中可恢复约束的数量及Stage1约束提取的可靠性，并非通用的数学推理替代方案。
- 方法局限性：该方法并非通用数学推理的替代方案，性能提升效果受可恢复约束的存在及Stage1约束提取准确性的限制。
- 未来工作：论文未报告具体的未来工作方向。
> ✅ 总结一句话：Constraint-First Reasoning (CFR)是一种无训练的两阶段提示协议，通过先提取数学问题的答案空间约束、再在求解中校验结果，结合Routed-CFR的自适应触发机制，可提升大语言模型在数学问题求解上的性能，且性能收益依赖于可恢复约束及Stage1约束提取的可靠性。

</details>

---

### 11. [Operating Multi-Node Full Fine-Tuning on NVIDIA B300: A Field Report on Telemetry-Based Triage, Negative Results, and Operational Hardening](https://arxiv.org/abs/2608.05944v1)

**Authors**: Seon Ho Kim, Ui Jeong Jeon, Su Hyeon Kim, Min Tae Hwang  
**Category**: cs.DC  
**Published**: 2026-08-07  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2608.05944v1  

#### Abstract
We report operational experience full-fine-tuning a 32.76B-parameter dense model (Qwen3-32B) on 16 x NVIDIA B300 (two nodes, FSDP / ZeRO-3) -- among the first published field accounts on this accelerator. We claim no new algorithm. The individual mechanisms we use are established practice; our contr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Operating Multi-Node Full Fine-Tuning on NVIDIA B300: A Field Report on Telemetry-Based Triage, Negative Results, and Operational Hardening
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：1）首次针对NVIDIA B300加速卡进行32.76B参数Qwen3-32B模型的多节点全微调，缺乏适配该硬件的运维方案、故障分诊机制及校准数据；2）现有utilization%读数不可靠（NCCL hang时利用率显示100%），无法准确定位故障类型；3）大规模微调中对NFS存储性能存在普遍误解，认为NFS读必然劣于本地缓存；4）多节点数据并行任务存在长时静默故障（如epoch-end NCCL死锁），缺乏预校验机制。论文未提出新算法，贡献为集成的现场运维经验与新硬件校准测量。

🚀 提出的新方法与思路
**B300电源功耗分诊表**：基于B300板级瓦特数，区分compute/communication/data-starvation/checkpoint-deadlock/idle等故障类型，解决utilization%读数失效的问题。
**受控存储性能验证方法**：设计per-step NFS读与预分词本地缓存的受控A/B对比，纠正NFS存储性能的常见认知误区。
**预运行不变量校验机制**：针对epoch-end NCCL死锁（由各rank token-packing失衡导致），设计短耗时预运行校验网关结合外部监控，将多小时静默故障转为即时拒绝，对应PyTorch Join/equalize-to-minimum实践。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
故障分诊可靠性 | 基于B300板级电源功耗实现，规避utilization%读数失效的问题，可快速定位不同类型故障
存储性能认知 | 纠正“per-step NFS读必然劣于预分词本地缓存”的优化误区，提供真实硬件环境下的存储策略性能参考
多节点运维效率 | 将数据并行任务的多小时静默故障转为即时拒绝，减少GPU时间浪费
硬件校准参考 | 提供B300多节点全微调的性能扩展性参考

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告具体数据集名称 | 用于Qwen3-32B模型全微调，适配页缓存以验证存储争用相关的性能问题

🎯 实验设置与评估指标
任务：32.76B参数Qwen3-32B模型的2节点、16x NVIDIA B300全微调，采用FSDP/ZeRO-3并行策略。
指标 | 含义（箭头）
--- | ---
令牌吞吐量 | 每秒钟处理的令牌数，越高越好
强缩放性能 | GPU数量增加时的性能缩放比，越高越好
GPU小时数 | 微调任务消耗的GPU时间，越低越好
板级电源功耗 | 用于故障类型分诊，无方向

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
per-step NFS读取 | 存储优化策略 | 跨节点数据读取的常见策略
预分词本地缓存读取 | 存储优化策略 | 本地数据缓存的常见策略
PyTorch Join/equalize-to-minimum实践 | 并行同步机制 | 现有多节点数据并行的同步策略

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告。
2. 效率对比（FPS / 参数量）：论文未报告FPS指标，参数量为32.76B（来自论文摘要，未标注来源）。
3. 跨域 / zero-shot 迁移：论文未报告。
4. 鲁棒性 / 扰动测试：论文未报告。
5. 消融实验：论文未报告。

**表N：B300 4/8/16-GPU强缩放性能（全微调场景）**
论文未报告具体表号，仅报告强缩放性能为near-linear（近线性），无具体数值。
结论：B300在4/8/16-GPU多节点全微调场景下的强缩放性能接近线性，符合该硬件在大规模微调场景下的预期。

**表N：存储策略性能对比（per-step NFS读vs预分词本地缓存）**
论文未报告具体表号，仅报告两者性能相当，无具体数值。
结论：当微调语料适配页缓存且任务为compute-bound时，per-step NFS读与预分词本地缓存性能相当，纠正了NFS存储性能必然劣化的常见认知。

**表N：故障处理效果（epoch-end NCCL死锁场景）**
论文未报告具体表号，仅报告预运行校验机制可规避长时静默故障，无具体数值。
结论：针对数据依赖的多节点数据并行任务，预运行不变量校验机制可有效提升运维效率。

4. 关键结论和发现
- 主要发现：1）NVIDIA B300加速卡的utilization%读数不可靠（NCCL hang时利用率显示100%），需基于板级电源功耗进行故障分诊；2）32.76B参数模型全微调中，当语料适配页缓存且任务为compute-bound时，per-step NFS读与预分词本地缓存性能相当，之前报告的“吞吐量崩溃”实为NFS/CPU争用而非存储介质限制；3）针对多节点数据并行任务的预运行不变量校验机制，可将多小时NCCL死锁等静默故障转为即时拒绝，大幅减少GPU时间浪费；4）数据依赖的数据并行任务运维的核心是监控电源功耗而非利用率，仅靠冒烟测试无法保证任务安全。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：这篇论文是NVIDIA B300加速卡上32.76B参数Qwen3-32B模型多节点全微调的现场运维报告，提供了B300电源功耗分诊表、受控存储性能验证方法、预运行不变量校验机制等实用运维经验，纠正了常见优化误区，为新硬件大规模微调提供了参考。

</details>

---

### 12. [Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay](https://arxiv.org/abs/2608.05784v1)

**Authors**: Nossa Iyamu  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.05784v1  

#### Abstract
Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it seg...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay
1. 论文的主要贡献和创新点
解决的问题：
计算机使用智能体当前仅记录用户指令而非实际执行的屏幕操作，需重复推导用户已完成的操作例程；现有LLM摘要处理相同屏幕捕获内容时回答准确率较低，且未测量智能体成本模型所需的Routine Overhead Ratio R、routine recurrence h等关键参数。

🚀 提出的新方法与思路
**Activity Frames 零模型确定性编译管道**：采用无模型的零流程，将本地屏幕捕获流分割为带类型的活动帧；每个活动帧包含应用、站点、时间、输入量以及指向原始行的证据指针；输出为字节一致、可缓存、可机械审计的结果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 记忆处理 | 零模型确定性输出，字节一致、可缓存、可机械审计，避免重复推导例程 |
| 上下文压缩 | 51天原始屏幕捕获可缩减为原大小86倍的提示就绪上下文块，处理仅需68ms |
| 回答准确性 | 智能体读取编译内容时回答准确率达98.4%（95% CI 91.7-99.7%），远高于LLM摘要的66-80% |
| 成本测量 | 首次提供智能体成本模型所需但尚未测量的R、h参数 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 一位专业人员的单用户语料库（128756帧，51个活跃天） | 验证Activity Frames的压缩效率与回答准确性 |

🎯 实验设置与评估指标
任务：将屏幕捕获内容编译为Activity Frames，评估其压缩效率及智能体读取编译内容对当日问题的回答准确性。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 压缩比 | 原始捕获内容与编译后上下文块的大小比值（↑ 越高越好） |
| 处理时间 | 51天原始捕获内容的编译耗时（↓ 越短越好） |
| 回答准确率 | 智能体对当日问题的正确回答比例（↑ 越高越好） |
| 95%置信区间 | 准确率的统计置信范围 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| LLM摘要 | 智能体摘要处理方式 | 读取相同屏幕捕获内容生成摘要后回答问题，准确性较低 |
| mid-tier LLM/frontier LLM | 不同层级大语言模型 | 读取Activity Frames编译后的内容时，mid-tier模型与frontier模型表现匹配 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Activity Frames编译效果（单用户51天语料库）**
| 指标 | 数值 |
| --- | --- |
| 压缩比 | 86x ✅ |
| 处理时间 | 68 ms |
| 回答准确率 | 98.4%（Wilson 95% CI 91.7-99.7%）✅ |
| LLM摘要回答准确率（基线） | 66-80% |
| Routine Overhead Ratio R（首次测量值） | 60-343x |
| In-sample delegable recurrence（首次测量值） | 9.0% |
| Out-of-sample delegable recurrence（首次测量值） | 7.7% |
| 整舰队代币上限场景对应值 | 近8% |

💡 结论：Activity Frames能高效压缩屏幕操作捕获内容，同时保障智能体高回答准确率，首次测量到智能体成本模型所需的关键参数。
其他实验：论文未报告主benchmark性能（除上述已列）、效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验，故均不涉及。

4. 关键结论和发现
- 核心发现1：Activity Frames的零模型确定性编译管道兼具高压缩效率（86x）与高回答准确率（98.4%），处理耗时仅68ms。
- 核心发现2：首次测量到智能体成本模型所需的两个关键参数：Routine Overhead Ratio R的建模上限为60-343x，可委派例程的in-sample复发率为9.0%、out-of-sample为7.7%，对应实现在整舰队代币上限近8%的场景。
- 核心发现3：编译后的例程可脱离模型实现确定性回放，live演示在匹配防护阈值时零模型代币完成播放。
方法局限性：论文未报告。
未来工作：论文未报告。

✅ **总结一句话**：Activity Frames通过零模型确定性编译管道将屏幕操作捕获转换为可审计的活动帧，为智能体提供高准确性的记忆，同时首次测量智能体成本模型所需的关键参数并支持例程的无模型确定性回放。

</details>

---

### 13. [Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging](https://arxiv.org/abs/2608.05541v1)

**Authors**: Yu Gu, Zhi Zheng, Yunpeng Ba, Xialiang Tong, Mingxuan Yuan, Zhenkun Wang  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.05541v1  

#### Abstract
Evolution Strategy (ES) is a promising alternative to gradient-based fine-tuning for resource-constrained Large Language Model (LLM) reasoning. However, directly applying ES to billion-parameter LLMs is highly ineffective. In such high-dimensional parameter spaces, most random perturbations are near...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 直接应用Evolution Strategy（ES）于十亿参数级LLM时，高维参数空间中多数随机扰动与有用更新方向近乎正交，导致优化不稳定，ES难以有效应用于LLM推理；
2. 现有对比基线方法GRPO-LoRA的表现仍有提升空间，且效率待优化。

🚀 提出的新方法与思路
**Hyper-ES**：是一种基于子空间的ES框架，首先执行少量低成本梯度微调以获取下降方向，这些下降方向的张成构成紧凑的适应子空间，可捕获有用的推理更新；之后应用CMA-ES优化层的DARE-TIES合并系数，在该子空间中组合有意义的下降方向，而非在全模型参数空间搜索任意扰动，以此解决ES在高维参数空间的优化劣势，同时保留其在低维优化中的优势。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能 | 在六个数学推理数据集上，Hyper-ES一致优于GRPO-LoRA，性能提升1% |
| 效率 | Hyper-ES所需的占空间的梯度更新比GRPO-LoRA少10% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 六个数学推理数据集 | 评估Hyper-ES在LLM数学推理任务上的性能 |

🎯 实验设置与评估指标
任务：LLM数学推理任务
| 指标 | 含义 |
| --- | --- |
| 论文未报告具体指标名称 | 仅说明Hyper-ES在性能上优于GRPO-LoRA，效率上所需占空间的梯度更新比GRPO-LoRA少10% |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO-LoRA | 基于LoRA结合GRPO的LLM优化方法 | 作为对比基线，性能与效率均弱于Hyper-ES |

3. 主要实验结果和性能指标
📊 定量结果汇总
主benchmark性能：论文未报告具体表号，仅说明在六个数学推理数据集上Hyper-ES性能优于GRPO-LoRA。
效率对比：论文未报告具体表号，仅说明Hyper-ES所需的占空间的梯度更新比GRPO-LoRA少10%。
跨域/zero-shot迁移：论文未报告。
鲁棒性/扰动测试：论文未报告。
消融实验：论文未报告。

💡 结论：在六个数学推理数据集上，Hyper-ES的性能优于对比基线方法GRPO-LoRA，同时具备更高的优化效率。

4. 关键结论和发现
- 发现1：Hyper-ES通过构造由少量梯度微调得到的下降方向张成的适应子空间，有效解决了直接应用ES于高维LLM参数空间时优化不稳定的问题。
- 发现2：Hyper-ES在LLM数学推理任务上，相较基线方法GRPO-LoRA实现了性能提升与效率优化的双重收益。
- 发现3：仅需少量低成本梯度微调即可构建有效的适应子空间，结合CMA-ES优化下降方向的合并系数，可实现高效的LLM推理优化。
- 方法局限性：论文未明确报告方法的局限性。
- 未来工作：论文未提及具体未来工作方向。

> ✅ **总结一句话**：Hyper-ES是针对LLM推理的子空间演化策略框架，通过利用少量梯度微调获得的下降方向构造紧凑适应子空间，优化层的DARE-TIES合并系数，在六个数学推理数据集上表现优于GRPO-LoRA，且所需占空间的梯度更新更少。

</details>

---

### 14. [DBLAST: Dependent Block Drafting for Stochastic Speculative Decoding](https://arxiv.org/abs/2608.05448v1)

**Authors**: Amirmohammad Karimi, Chao Gao, Negar Hassanpour  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.05448v1  

#### Abstract
Speculative decoding accelerates large language models' inference by using a lightweight drafter to propose multiple future tokens and a target model to verify them. While recent block and diffusion-style drafters can predict several positions in a single pass, their training and sampling procedures...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DBLAST: Dependent Block Drafting for Stochastic Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题：现有区块类、扩散类drafter的训练和采样流程通常针对贪心解码优化，或假设draft区块内的token位置条件独立；但在非贪心的随机推测解码场景中，该假设不成立——目标采样分布具有随机性，存在多个合理的文本续篇，导致区块扩散drafter的被接受draft长度随目标分布熵增加而下降。不同方法缺陷：区块/扩散类drafter未适配非贪心随机解码的场景，独立区块采样方法采用的条件独立假设在高熵场景失效。

🚀 提出的新方法与思路
**Dependent Block Drafting**：基于token位置的低秩潜在混合模型构造依赖型draft区块，搭配接受导向的训练目标，该目标直接以期望验证长度为优化方向，而非针对贪心解码的损失。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 接受的draft长度（高熵解码场景） | 相较独立区块采样有提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GSM8K | 对应任务的性能评估 |
| MT-Bench | 对应任务的性能评估 |
| HumanEval | 对应任务的性能评估 |
| creative-writing | 对应任务的性能评估 |

🎯 实验设置与评估指标
本实验针对大语言模型的推测解码加速任务，评估指标：
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| accepted draft length | ↑ 越高越好（指推测解码中被目标模型接受的draft token序列长度） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| independent block sampling | 基线方法 | 采用区块内token位置条件独立的假设，针对贪心解码优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 区块扩散drafter的训练和采样设计适配贪心解码及独立位置假设，在非贪心随机解码场景中存在短板，随目标采样分布熵增大，被接受draft长度下降；② DBLAST方法相较独立区块采样，能在各基准任务上稳定提升被接受的draft长度，在高熵解码场景下效果更突出。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：DBLAST是针对随机推测解码的依赖区块drafting方法，通过低秩潜在混合模型与接受导向训练目标，在高熵解码场景下提升了被目标模型接受的draft长度。

</details>

---

### 15. [Sparse Mutual Information Graph Averaging for Improving Random Indexing Embeddings](https://arxiv.org/abs/2608.05724v1)

**Authors**: Sriram Loganathan, Gokul Anand, Aung Bo Bo, Yourui Shao, William B. Andreopoulos  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.05724v1  

#### Abstract
Sparse word embedding pipelines can avoid dense co-occurrence matrix materialization, dense factorization, and gradient training while still relying on sparse global corpus statistics. This paper studies Random Indexing (RI) vectors refined by weighted averaging on a sparse Positive Pointwise Mutual...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Sparse Mutual Information Graph Averaging for Improving Random Indexing Embeddings
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：弱Random Indexing（RI）初始化的语义嵌入表现差；对PPMI+SVD、Binary+SVD、CBOW、Skip-gram等基线方法使用邻域平均后，在fairytales语料的谷歌家庭类语义类比子集上的准确率反而降低；提出方法在text8数据集上无法与神经基线竞争，在SimLex-999上严格相似度相关性接近零；Bloom filter sketches在测试配置下性能弱于RI。

🚀 提出的新方法与思路
**PPMI top-K图平均**：基于稀疏的正点wise互信息（PPMI）图进行加权平均，采用top-K剪枝策略，是一种用于修复弱RI嵌入的非梯度方法。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 弱RI嵌入修复 | 在fairytales语料的谷歌家庭类语义类比子集上，将RI初始化准确率从19.4±0.7%提升至30.7±2.9%（5个随机种子结果） |
| 非梯度依赖 | 无需梯度训练，基于全局稀疏语料统计量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| fairytales语料 | 测试谷歌家庭类语义类比任务（覆盖272个问题的子集） |
| text8 | 测试本文方法与神经基线的竞争力 |
| SimLex-999 | 测试严格相似度相关性 |

🎯 实验设置与评估指标
任务为语义类比任务（谷歌家庭类子集）及相似度相关性测试，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 语义类比子集准确率 | ↑越高越好 |
| SimLex-999严格相似度相关性 | ↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Random Indexing (RI) | 基础词嵌入方法 | 弱初始化状态 |
| PPMI+SVD | 分解方法 | 邻域平均后在目标子集准确率降低 |
| Binary+SVD | 分解方法 | 邻域平均后在目标子集准确率降低 |
| CBOW | 神经基线方法 | 邻域平均后在目标子集准确率降低 |
| Skip-gram | 神经基线方法 | 邻域平均后在目标子集准确率降低 |
| Bloom filter sketches | 草图方法 | 在测试配置下性能弱于RI |
| PPMI top-K graph averaging | 本文提出方法 | 非梯度修复弱RI嵌入的图平均方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**fairytales语料谷歌家庭类子集语义类比准确率结果**
| 方法 | 准确率 |
| --- | --- |
| Random Indexing (RI) | 19.4±0.7% |
| PPMI top-K graph averaging | 30.7±2.9% ✅ |
| PPMI top-K graph averaging（seed42最优种子） | 34.6% |
💡 结论：本文提出的PPMI top-K graph averaging方法可有效修复弱RI嵌入，在fairytales语料的谷歌家庭类语义类比任务上显著提升准确率，但在text8数据集上无法与神经基线竞争，在SimLex-999上严格相似度相关性接近零，且对其他基线方法的邻域平均操作会降低其在目标子集的类比准确率。

（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验，论文未报告）

4. 关键结论和发现
- 主要发现：① PPMI top-K图平均是非梯度修复弱RI嵌入的有效方法，在fairytales语料的谷歌家庭类子集上，RI的类比准确率从19.4±0.7%提升至30.7±2.9%；② 邻域平均操作会降低PPMI+SVD、Binary+SVD、CBOW、Skip-gram等基线方法在fairytales家庭类子集的类比准确率；③ 本文方法在text8数据集上无法与神经基线竞争，在SimLex-999上严格相似度相关性接近零，Bloom filter sketch在测试配置下性能弱于RI。
- 方法局限性：仅在fairytales语料的特定语义类比子集上验证了有效性，在其他数据集（text8）、任务（相似度相关）及对其他基线方法的适用性上表现不佳。
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的PPMI top-K图平均方法可有效修复弱Random Indexing嵌入，在fairytales语料的谷歌家庭类语义类比任务上显著提升准确率，但在其他数据集和任务上的表现仍待优化。

</details>

---

### 16. [Consistency Has a Computable Blind Spot: A Commutation Theory of Label-Free Reliability for Vision-Language Figure Reading](https://arxiv.org/abs/2608.05675v1)

**Authors**: Rasul Khanbayov, Hasan Kurban  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.05675v1  

#### Abstract
Label-free reliability for vision-language models rests on invariance: perturb the input and a faithful reader's answer should not change. This has a known blind spot, a systematic misreading survives the perturbation and gets certified wrong, which we show is computable, not just real: an error is ...

---

### 17. [Breaking Memory Bottlenecks in Quantum Control Systems for More Precise Experiments and Higher Throughput Computing](https://arxiv.org/abs/2608.06318v1)

**Authors**: Yicheng Guang, Neel Vora, Yilun Xu, Yueqi Chen, Gang Huang  
**Category**: cs.AR  
**Published**: 2026-08-07  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.06318v1  

#### Abstract
As quantum computing continues to demonstrate promise and attract growing attention, there is an increasing need for more precise experiments to advance the development of quantum devices, as well as higher circuit throughput to validate more domain applications. However, this need is hindered by a ...

---

### 18. [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](https://arxiv.org/abs/2608.06243v1)

**Authors**: ZhiYan Hou, Xinyu Tang, Hongyan An, Jianjin Zhang, Weizhen Wang, Yunyun Han, Gengsheng Li, Xiangzhao Hao, Haiyun Guo, Wenbin Hu, Jinqiao Wang, Yafeng Deng  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.06243v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models using automatically verifiable outcome signals, but these signals are typically sparse and at the sequence-level. On-policy self-distillation (OPSD) mitigates this sparsity by querying ...

---

### 19. [On-Policy Delta Distillation for Multilingual Math Reasoning](https://arxiv.org/abs/2608.05802v1)

**Authors**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.05802v1  

#### Abstract
On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD$^2$), for mathematical reasoning in Engl...

---

### 20. [NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering](https://arxiv.org/abs/2608.06292v1)

**Authors**: Jonas Gann, Michael Gertz  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.06292v1  

#### Abstract
Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to spec...

---

### 21. [Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding](https://arxiv.org/abs/2608.05832v1)

**Authors**: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao, Fei Huang, Rui Wang, Shuguang Han, jufeng chen  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.05832v1  

#### Abstract
Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each ...

---

### 22. [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](https://arxiv.org/abs/2608.05571v1)

**Authors**: Mohammad Asadi, Soheil Hor, Bardiya Akhbari, Jack W. O'Sullivan, Tahoura Nedaee, Layne C. Price, Raviteja Anantha, Euan Ashley, Ehsan Adeli  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.05571v1  

#### Abstract
Retrieval-augmented forecasting promises to adapt frozen Time Series Foundation Models (TSFMs) to new domains without fine-tuning, but recent methods typically rely on learned fusion modules, i.e., trained adapters that merge retrieved examples into the backbone's forecast, based on the assumption t...

---

### 23. [LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm](https://arxiv.org/abs/2608.06135v1)

**Authors**: Anjali Gangadhar Katageria, Shobha Rani, Raghu Nandan Sengupta  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2608.06135v1  

#### Abstract
Large Language Models (LLMs) such as ChatGPT and Claude are widely used for information retrieval and problem-solving. Recent work has focused on improving scheduling algorithms to boost throughput while maintaining low latency. However, these approaches often assume Poisson request arrivals with co...

---

### 24. [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](https://arxiv.org/abs/2608.05732v1)

**Authors**: Mehrshad Saadatinia, Parsa Razmara, Ardalan Aryashad, Ali Abbasi, Seyedarmin Azizi  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2608.05732v1  

#### Abstract
Controlling the behavior of large language models (LLMs) remains a critical challenge for AI alignment. Existing steering methods, such as Contrastive Activation Addition (CAA), typically rely on fixed single-layer interventions derived from aggregate activation differences. These methods impose a s...

---

### 25. [RIG-RoPE: Relation- and Instance-Gated Rotary Positional Encoding with Duration-Aware Temporal Coordinates](https://arxiv.org/abs/2608.05154v1)

**Authors**: Donggen Li  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.05154v1  

#### Abstract
Rotary positional encoding (RoPE) is a core component of modern language models and has been extended to multimodal LLMs through multidimensional variants such as multimodal RoPE (M-RoPE), which split positional channels into temporal, height, and width subspaces. This report identifies two limitati...

---

### 26. [BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition](https://arxiv.org/abs/2608.06023v1)

**Authors**: Bojing Hou, Ruohao Li, Yitong Zhu, Hongjun Liu, Luwen Yu, Yuyang Wang  
**Category**: cs.LG  
**Published**: 2026-08-07  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.06023v1  

#### Abstract
To address the limitations of video-based emotion recognition under ambiguous or socially masked behavioral cues, as well as the poor deployability of physiological signals, this paper proposes a reliability-aware physiology-to-video knowledge distillation framework, termed BioKD. The proposed frame...

---

### 27. [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197v1)

**Authors**: Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, Jinyang Huang, Yan Xu, Yasheng Wang, Weinan Zhang, Xingshan Zeng, Weiwen Liu  
**Category**: cs.AI  
**Published**: 2026-08-07  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.06197v1  

#### Abstract
Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement lear...

---

### 28. [PoolBench: A Benchmark for Pooling Strategies in Concept Representation Evaluation for Decoder-Only LLMs](https://arxiv.org/abs/2608.05162v1)

**Authors**: Ayushi Agarwal  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.05162v1  

#### Abstract
Pooling is a consequential but under-examined design choice in decoder-only concept representation work: practitioners must collapse token-level hidden states into a passage-level vector, yet no shared protocol exists for comparing this choice across concepts, models, and tasks. Reported gains are c...

---

### 29. [Cross-Architecture Steering Transfer in Language Models: A Systematic Empirical Study](https://arxiv.org/abs/2608.05164v1)

**Authors**: Ayushi Agarwal  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.05164v1  

#### Abstract
Independently trained large language models may develop shared internal representations of semantic concepts despite architectural differences -- but whether this geometric similarity has functional consequences for cross-model behavioural control remains untested. We present the first systematic ev...

---

### 30. [MoCA: Implicit Social Context Analysis](https://arxiv.org/abs/2608.05825v1)

**Authors**: Wenhao Xu, Kaiwen Zhang, Hao Li, Maowei You, Yongzheng Ji, Siyuan Zuo, Jingxuan Yu, Sina A, Xinyao Tan, Bobo Li, Hao Fei, Mong-Li Lee, Wynne Hsu  
**Category**: cs.CL  
**Published**: 2026-08-07  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.05825v1  

#### Abstract
Human social communication, such as affection and intent, is often conveyed in highly implicit ways, where underlying meanings are expressed through indirect, socially and culturally grounded signals rather than explicit statements. Such implicit social contexts are pervasive in real-world interacti...

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
