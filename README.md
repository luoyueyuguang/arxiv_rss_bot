# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-20 06:16:01 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [UMER: Unifying Embedding and Ranking via Pair-Aware Discriminative Reasoning for Universal Multimodal Retrieval](https://arxiv.org/abs/2608.18504v1)

**Authors**: Libiao Chen, Xiyang Liu, Yanheng Wei, Tao Wang, Zhenyu Tang  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 74.5  
**Type**: new  
**ArXiv ID**: 2608.18504v1  

#### Abstract
Universal multimodal retrieval aims to support diverse instruction-aware retrieval tasks, demanding both efficient corpus-scale matching and fine-grained semantic reasoning. Recent MLLM-based embedding methods typically derive representations from hidden states, while Chain-of-Thought (CoT) reasonin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

UMER: Unifying Embedding and Ranking via Pair-Aware Discriminative Reasoning for Universal Multimodal Retrieval
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有基于多模态大语言模型（MLLM）的嵌入方法通常从隐藏状态推导表示；
- 现有Chain-of-Thought（CoT）推理采用item-wise方式，单独对查询与候选进行推理，未提供区分正样本与语义易混淆硬负样本的显式证据；
- 对比型嵌入仅能捕捉全局相似性，在需要答案验证、类别判断或细粒度推理的元任务上表现不佳。

🚀 提出的新方法与思路
**Pair-Aware Discriminative Reasoning**：替换item-wise推理方式，通过比较查询-候选对识别指令相关的匹配与差异证据；
联合学习策略：在单一MLLM内同时学习用于高效全局匹配的对比型嵌入，以及用于显式成对相关性判断的判别式排序；
**互补互蒸馏策略**：在嵌入与排序功能间传递可靠的成对偏好。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理机制 | 采用Pair-Aware而非item-wise推理，生成区分正样本与硬负样本的显式证据 |
| 模型架构 | 单MLLM内联合学习对比嵌入与判别式排序，兼顾高效全局匹配与细粒度推理能力 |
| 任务适配性 | 适配需要答案验证、类别判断等的元任务，解决对比型嵌入的局限性 |
| 推理灵活性 | 支持预算可调推理 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MMEB-V2 | 主基准性能测试 |

🎯 实验设置与评估指标
任务为通用多模态检索，论文未报告具体评估指标的含义及具体指标内容。

⚔️ 基线方法对比
论文未报告基线方法的具体信息。

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：MMEB-V2主基准性能（场景：通用多模态检索）**
论文未报告具体数值，仅提及UMER在该基准上达到SOTA性能。
💡 结论：论文未补充其他定量结果相关的具体结论（除SOTA表述外）。
注：效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等内容，论文均未报告。

4. 关键结论和发现
- 主要发现：1. UMER框架在通用多模态检索任务的MMEB-V2基准上达到SOTA性能；2. 其Pair-Aware推理与联合学习策略有效解决了现有方法的痛点；3. 支持预算可调推理，适配不同资源约束的推理需求。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：UMER是通过Pair-Aware Discriminative Reasoning联合学习对比嵌入与判别式排序的通用多模态检索框架，在MMEB-V2基准上达到SOTA性能且支持预算可调推理。

</details>

---

### 2. [FlashAttention for Scalable Vector Architectures](https://arxiv.org/abs/2608.18656v1)

**Authors**: Sonia Rani Gupta, Nikela Papadopoulou, Miquel Peric\`as  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 72.0  
**Type**: new  
**ArXiv ID**: 2608.18656v1  

#### Abstract
Inference with transformer models on CPUs is increasingly important, especially for Small Language Models (SLMs), where vector architectures are emerging as a promising execution substrate. The attention module is a major bottleneck due to high memory bandwidth requirements; FlashAttention mitigates...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# FlashAttention for Scalable Vector Architectures
1. 论文的主要贡献和创新点
✅ 解决的问题
Transformer模型在CPU上的推理（尤其是小语言模型SLMs）中，注意力模块因高内存带宽需求成为核心瓶颈；现有FlashAttention在适配可扩展向量架构时，向量长度利用效率不足，且Q8_0量化层在长向量执行下存在算术摊销受限的问题，限制了长向量架构下的性能提升。

🚀 提出的新方法与思路
**FlashAttention-V**：一种适配可扩展向量架构的分块FlashAttention，通过跨注意力头并行、头间打包（inter-head packing）实现对从短到很长向量的适配，提升向量寄存器利用率与内存访问局部性；已集成至llama.cpp的ggml框架中进行验证。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| Prefill阶段性能 | 在512位向量长度（VL）下，相比标量FlashAttention实现22x-42x的加速；扩展至64车道、4096位VL时，额外获得2x-2.5x的性能增益 |
| Decode阶段性能 | 在512位VL下，相比标量FlashAttention实现8x-11x的加速，且因单token内存绑定执行，性能对向量宽度、车道数的敏感性较低 |
| 硬件适配性 | 在Banana Pi BPI-F3上，跨注意力头的循环重排、循环展开优化有效提升性能，增益随模型规模增大而提升，短上下文、解码阶段增益更显著 |
| 架构兼容性 | 针对RVV、Arm SVE等向量架构，明确现有Q8_0量化格式的结构瓶颈，为后续优化提供依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告用于评估的具体数据集，仅使用TinyLlama、Llama 3.2、Qwen2.5、Pythia-410M等模型进行验证 |

🎯 实验设置与评估指标
任务：Transformer模型的推理，包含Prefill（预填充）与Decode（解码）两个阶段
| 指标 | 含义 |
| ---- | ---- |
| 速度提升倍数（Prefill阶段） | 相比标量FlashAttention的加速比，数值越大性能越好（↑） |
| 速度提升倍数（Decode阶段） | 相比标量FlashAttention的加速比，数值越大性能越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 标量FlashAttention | FlashAttention实现方式 | 作为基准，对比FlashAttention-V的性能表现 |

3. 主要实验结果和性能指标
📊 定量结果汇总
（无对应表号，结果来自论文正文）
| 场景 | 定量结果 | 最优值标识 | 💡 结论 |
| ---- | ---- | ---- | ---- |
| Prefill阶段（512位VL） | 22x-42x speedup over scalar FlashAttention | 论文未明确指定最优值，无标识 | FlashAttention-V在Prefill阶段实现显著加速，性能随向量长度、车道数扩展进一步提升 |
| Prefill阶段（64车道、4096位VL） | 额外2x-2.5x gain | 论文未明确指定最优值，无标识 | 更长向量与更多车道下仍有性能增益，可扩展性良好 |
| Decode阶段（512位VL） | 8x-11x speedup over scalar FlashAttention | 论文未明确指定最优值，无标识 | Decode阶段同样实现大幅加速，且对向量宽度、车道数敏感性低 |
| Banana Pi BPI-F3硬件 | 性能增益随模型规模增大而提升，短上下文、解码阶段增益更显著 | 论文未明确指定最优值，无标识 | 硬件层面的循环重排、跨头循环展开优化有效，适配实际硬件部署 |

消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. FlashAttention-V在Transformer推理的Prefill和Decode阶段均相比标量FlashAttention有显著性能提升，且Prefill阶段随向量长度、车道数扩展仍有增益；Decode阶段性能对向量宽度、车道数敏感性低。2. 在Banana Pi BPI-F3硬件上，跨注意力头的循环重排、循环展开是有效优化策略，性能增益随模型规模增大而提升，短上下文、解码阶段增益更明显。3. 现有Q8_0量化层在长向量执行下存在结构瓶颈，限制算术摊销，该问题在RVV、Arm SVE架构上均存在，是长向量可扩展性的核心挑战。
- 方法局限性：当前Q8_0量化格式无法适配长向量架构的执行需求，成为性能提升的阻碍。
- 未来工作：论文未明确提及具体未来工作方向。

> ✅ **总结一句话**：FlashAttention-V是适配可扩展向量架构的分块FlashAttention，相比标量FlashAttention在Transformer推理的Prefill、Decode阶段实现显著加速，同时明确了现有Q8_0量化格式限制长向量可扩展性的核心问题。

</details>

---

### 3. [Solving Is Not Drawing: A Benchmark for Diagrammatic Reasoning in Olympiad Geometry](https://arxiv.org/abs/2608.18111v1)

**Authors**: Hsien Xin Peng, Anthony Kim, Alvin Li, Calvin Supasanya, Shivank Garg, Kevin Zhu  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 71.0  
**Type**: new  
**ArXiv ID**: 2608.18111v1  

#### Abstract
Foundation models such as GPT and Claude now solve olympiad-level mathematics with remarkable proficiency, so much so that geometry problem solving has become a standard proxy for their mathematical reasoning. Yet solving a geometry problem and drawing the figure it depends on are not the same skill...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Solving Is Not Drawing: A Benchmark for Diagrammatic Reasoning in Olympiad Geometry
1. 论文的主要贡献和创新点
✅ 解决的问题
现有foundation models（如GPT、Claude）具备奥林匹克几何问题的数学推理能力，但解决几何题与绘制题目依赖的正确图表（需包含辅助线、关联等）是不同的技能；目前主流基准（如MathVista、MathVerse）仅测量模型是否得到正确答案，未单独衡量模型构造图表的能力，该能力维度未被评估。

🚀 提出的新方法与思路
**奥林匹克几何图表推理基准**：提出一个开源基准，包含954道自包含的奥林匹克几何问题（其中含297题的hard子集），每道题附带对应解答及人类编写的高保真Asymptote代码格式的图表；同时配套基于文本、代码、图像、VLM、约束的图表推理指标，用于专门衡量模型的图表构造能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 图表构造能力评估 | 现有主流基准未单独评估该能力，本基准专门针对此缺口设计，可独立量化模型的图表构造能力 |
| 评估指标覆盖 | 提供文本、代码、图像、VLM、约束等多类型评估指标，覆盖全面的图表推理维度 |
| 数据质量 | 搭配人类编写的高保真图表，数据适配奥林匹克几何场景的专业需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 954道自包含的奥林匹克几何问题（含297题hard子集） | 用于评估现有foundation models的图表构造能力，每道题附带对应解答及人类编写的高保真Asymptote代码格式的图表 |

🎯 实验设置与评估指标
任务：评估现有foundation models针对奥林匹克几何问题构造图表的能力
| 指标 | 含义（箭头标方向） |
|------|------------------|
| 图表代码编译成功率 | 衡量模型生成的Asymptote代码可成功编译的比例，比例越高代表图表忠实度越高 → ↑越高越好 |
| 论文未报告其他指标的定义细节 | - |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Current foundation models | 基础模型 | 具备奥林匹克几何问题的数学推理能力，但图表构造能力存在差距，已测得的平均编译成功率为36.14% |

3. 主要实验结果和性能指标
📊 定量结果汇总
**无明确表号的定量结果**
| 指标 | 数值 |
|------|------|
| 图表代码平均编译成功率 | 36.14% |
💡 结论：现有foundation models在奥林匹克几何问题的图表构造任务中，平均编译成功率仅为36.14%，存在明显的“会解题但不会画图”的差距。

其他实验：
主benchmark性能（L2/碰撞率等）：论文未报告
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现：
  1. 拥有较强数学推理能力的现有基础模型，并不必然具备构造精确几何图表的能力，二者间存在显著差距。
  2. 主流数学推理基准未单独评估图表构造能力，该维度此前被忽视，本研究填补了这一缺口。
  3. 提出的基准及配套指标可有效评估模型的图表推理能力，为相关研究提供标准化工具。
- 方法局限性：论文未明确提及方法局限性
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文提出了针对奥林匹克几何图表构造任务的开源基准，通过实验揭示了现有基础模型解题与图表构造能力间的显著差距，为图表推理能力的评估提供了标准化方案。

</details>

---

### 4. [Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage](https://arxiv.org/abs/2608.19049v1)

**Authors**: Omar Rady, Mohamed Ayman, Ali Arafa, Mohamed Shalma  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.19049v1  

#### Abstract
Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage
1. 论文的主要贡献和创新点
✅ 解决的问题
现实非凸校园拓扑下的毫米波（mmWave）基站最优部署属于NP难问题，其核心优化目标max-min公平性具有非凸、非平滑性质，单智能体深度强化学习（DRL）方法难以高效求解该问题。论文基准了四种DRL方案用于对比评估，未明确提及各对比方法的固有缺陷。

🚀 提出的新方法与思路
**地理划分多智能体DDPG框架**：将毫米波基站部署问题建模为马尔可夫决策过程（MDP），采用基于地理划分规则的多智能体协作机制，结合DDPG算法优化基站放置策略，以求解非凸拓扑下的NP难部署问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 密集场景性能 | 多智能体DDPG在密集场景下的性能大幅优于单智能体DRL方法 |
| 覆盖能力 | 可实现全覆盖 |
| 公平性 | Jain's公平指数较高 |
| 收敛效率 | 在含400用户的密集场景中具备高效的计算收敛性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ------ | ---- |
| 论文未报告 | 用于毫米波基站部署优化的性能评估 |

🎯 实验设置与评估指标
任务为在现实非凸校园拓扑下完成毫米波基站的最优部署优化。
| 指标 | 含义（箭头） |
| ---- | ---- |
| Jain's公平指数 | 衡量用户间服务公平性，数值越高越好 |
| 覆盖情况 | 衡量是否实现服务覆盖，实现为是、未实现为否 |
| 计算收敛效率 | 衡量算法训练至收敛的速度，越快越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 离散单智能体DQN | 单智能体离散DRL方法 | 基于离散动作空间的DQN框架 |
| 空间划分多智能体DQN | 多智能体DQN方法 | 基于空间划分规则实现多智能体协作 |
| 连续单智能体DDPG | 单智能体连续DRL方法 | 基于连续动作空间的DDPG框架 |
| 地理划分多智能体DDPG | 多智能体DDPG方法 | 本文提出的核心方法，基于地理划分规则实现多智能体协作 |

3. 主要实验结果和性能指标
论文未报告具体表号、图号、章节或页码，仅在摘要中提及相关结果：
1. 主 benchmark 性能：论文未提供对应表号，仅说明多智能体DDPG在密集场景性能优于单智能体方法，且实现全覆盖。
2. 效率对比（FPS / 参数量）：论文未报告。
3. 跨域 / zero-shot 迁移：论文未报告。
4. 鲁棒性 / 扰动测试：论文未报告。
5. 消融实验：论文未报告。

💡 结论：地理划分多智能体DDPG在密集场景的毫米波基站部署任务中，相比单智能体DRL方法具备更优性能，同时实现全覆盖，针对400用户的密集场景收敛高效。

4. 关键结论和发现
- 主要发现：1. 多智能体DDPG框架在密集场景下的毫米波基站部署性能显著优于单智能体DRL方法；2. 所提多智能体方法可实现全覆盖，且在含400用户的密集场景中收敛高效；3. 针对非凸拓扑下的NP难基站部署问题，基于多智能体DRL的方案具备可行性与有效性。
- 方法局限性：论文未报告方法在非密集场景的性能、泛化能力、大规模拓扑下的表现及对扰动的鲁棒性等。
- 未来工作：论文未提及相关内容。

> ✅ **总结一句话**：该论文针对现实非凸校园拓扑下毫米波基站最优部署的NP难问题，将其建模为马尔可夫决策过程并提出地理划分多智能体DDPG框架，经评估该框架在密集场景下性能优于单智能体DRL方法，同时实现全覆盖与高效收敛，证明了多智能体DRL在此类优化问题中的有效性。

</details>

---

### 5. [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](https://arxiv.org/abs/2608.18591v1)

**Authors**: Zishan Ahmad, Vishal Vaddina  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2608.18591v1  

#### Abstract
Uniformly allocating inference reasoning budgets to LLMs is expensive and prone to over-thinking penalties; especially in document tasks where visual layouts drive complexity. To address this, we introduce BudgetDoc, the first multimodal benchmark providing explicit supervision for model-budget-perf...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 《Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference》

1. 论文的主要贡献和创新点
✅ 解决的问题
现有均匀分配LLM推理预算的方法存在两大核心缺陷：一是推理成本过高；二是易出现过度推理惩罚，且未考虑文档任务中视觉布局对推理复杂度的影响，难以适配文档场景的特殊需求。

🚀 提出的新方法与思路
**BudgetDoc**：首个为三个文档任务提供模型-预算-性能权衡显式监督的多模态基准，解决现有基准缺乏预算层面监督的问题。
**DRB (Document-Reasoning Balancer)**：约1B参数的轻量级预飞行估计器，由SigLIP-2与Qwen3-0.6B组合而成，可预测不同预算水平下的有序模型性能，用于动态分配LLM推理预算。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 基准构建 | 首个提供三个文档任务的模型-预算-性能权衡显式监督的多模态基准 |
| 估计器设计 | DRB为轻量级（约1B参数）多模态模型，可实现不同预算水平下的有序模型性能预测 |
| 预算分配 | 支持在多个模型与数据集间动态分配推理预算，多数配置下性能匹配或优于全预算基线且大幅降本 |
| 泛化潜力 | 初步评估显示具备跨模型选择泛化潜力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| BudgetDoc | 用于三个文档任务，提供模型-预算-性能权衡的显式监督 |

🎯 实验设置与评估指标
任务为文档推理的推理预算优化，核心是在保障性能的同时降低推理成本。
| 指标 | 含义 |
|------|------|
| 加权F1 | 衡量模型性能预测或推理性能的准确性，越高越好 |
| 推理成本 | 衡量推理资源消耗，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| always-maximum-budget | 基线方法 | 均匀分配最大推理预算的基准方案，用于对比动态预算分配的效果 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告具体表号的定量数值，仅提及初步评估显示DRB具备跨模型选择泛化潜力
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 提出的BudgetDoc填补了文档任务中模型-预算-性能权衡显式监督基准的空白；
  2. DRB作为轻量级预飞行估计器，支持动态推理预算分配，在多数配置下性能匹配或优于全预算基线且显著降低成本；
  3. DRB具备跨模型选择的泛化潜力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了首个提供文档任务预算性能权衡监督的多模态基准BudgetDoc，以及轻量级LLM推理预算预飞行估计器DRB，可动态分配推理资源，在保障或提升性能的同时降低推理成本，且具备跨模型泛化潜力。

</details>

---

### 6. [DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning](https://arxiv.org/abs/2608.18878v1)

**Authors**: Zijie Meng, Xiwei Dai, Yixuan Tang, Jin Hao, Yang Feng, Fudong Zhu, Xiaoqiang Liu, Shaosheng Cao, Zuozhu Liu  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.18878v1  

#### Abstract
Oral diseases affect billions of people worldwide, underscoring a pressing need for accurate and reliable dental assessment that integrates heterogeneous evidence from domain knowledge, radiographs, intraoral photographs, and 3D dental data. Most existing dental AI systems remain modality- or task-s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning
1. 论文的主要贡献和创新点
✅解决的问题
现有牙科AI系统多为模态或任务特定；近期视觉语言模型虽支持灵活牙科问答，但直接生成的响应证据不明确、无法追溯。

🚀提出的新方法与思路
**证据中心型多智能体框架（DentAgent）**：该框架由Orchestrator协调五个专门化智能体，覆盖多种模态，每个专家利用领域工具将观察结果转换为结构化证据记录；通过证据黑板（Evidence Blackboard）管理这些记录作为共享证据状态，在生成响应前跟踪证据的覆盖情况、差距和冲突，标准化证据表示以整合孤立牙科能力为统一智能体工作流。

🔍相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 诊断性能 | 在四个基准测试中表现领先，多标签诊断任务性能超越高级专家17.3个百分点 |
| 可追溯性 | 采用标准化证据表示，支持跟踪证据的覆盖、差距和冲突，响应证据明确可追溯 |
| 任务整合性 | 将孤立牙科能力整合为统一的多模态智能体工作流，适配多种牙科任务 |

2. 核心实验方法和设置
📚使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 评估多模态牙科推理性能 |

🎯实验设置与评估指标
任务为多模态牙科推理，涉及多标签诊断等牙科评估任务。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确说明具体评估指标 |

⚔️基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未明确说明对比基线的具体类型与特点 | 论文未报告具体基线方法信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表格编号，仅明确：DentAgent在四个基准测试中表现领先，多标签诊断任务的性能超越高级专家17.3个百分点。
💡 结论：DentAgent在多模态牙科推理任务上达到领先性能，多标签诊断能力优于高级人类牙科专家。

其他实验模块：
效率对比（FPS/参数量）：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. DentAgent作为证据中心型多智能体框架，可有效整合多模态牙科证据，实现响应的可追溯性；2. DentAgent在四个基准测试中表现领先，多标签诊断任务性能超越高级专家17.3个百分点；3. 标准化证据表示提升了牙科AI系统的可解释性与可靠性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DentAgent是一种整合多模态牙科证据的证据中心型多智能体框架，实现了领先的多模态牙科推理性能，为人群口腔健康评估和管理提供了技术基础。

</details>

---

### 7. [MAVEN: A Macro-Societal Value Evaluation Framework of Multimodal Content with Compact Aligned Evaluators](https://arxiv.org/abs/2608.18096v1)

**Authors**: Zijuan Zhao, Zheren Fu, Hou Xia, Licheng Zhang, Yi Liu, Zhendong Mao  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 47.5  
**Type**: new  
**ArXiv ID**: 2608.18096v1  

#### Abstract
Assessing whether multimodal content aligns with macro-societal values, such as peace, justice, and freedom, has become an increasingly urgent challenge. Existing frameworks are largely confined to safety-oriented taxonomies, text-only psychometric probes, or single-label classification. Therefore, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：MAVEN: A Macro-Societal Value Evaluation Framework of Multimodal Content with Compact Aligned Evaluators
1. 论文的主要贡献和创新点
✅ 解决的问题
当前评估多模态内容是否符合和平、正义、自由等宏观社会价值的需求迫切，而现有相关框架多局限于安全导向的分类体系，或采用纯文本的心理测量探针，亦或是仅支持单标签分类，存在显著适用性局限。
🚀 提出的新方法与思路
**MAVEN宏观社会价值评估框架**：基于国际人权文书和文化价值理论构建，将价值划分为6个主维度和72个二级指标，支持多级量化评分。
**MacroValue-Bench基准数据集**：在MAVEN基础上构建的经人工验证的多模态基准数据集，用于评估VLMs的宏观社会价值评估能力。
**soft-match metric**：用于在各价值维度评估VLMs评估表现的软匹配指标。
**SA-MDPO（span-adaptive variant of multi-level preference optimization）**：用于评估器蒸馏优化的span自适应多级偏好优化变体。
**training-free multi-role consensus策略**：推理时采用的无训练多角色共识策略。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 宏观社会价值覆盖 | 现有框架多局限于安全导向分类，MAVEN涵盖6个主维度、72个二级指标，支持多级量化评估 |
| 多模态评估支持 | 现有方法多为纯文本探针，MAVEN支持多模态内容的宏观社会价值评估 |
| 评估器效率 | 同性能评估器多为大参数模型，SA-MDPO蒸馏得到的2B评估器参数量小，可媲美同系列8B模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MacroValue-Bench | 用于评估VLMs在宏观社会价值各维度的评估能力 |
🎯 实验设置与评估指标
任务：对多模态内容进行宏观社会价值各维度的量化评估
| 指标 | 含义 |
| ---- | ---- |
| soft-match metric | 衡量VLMs评估结果与标准评估结果的匹配程度 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有开源VLMs | 基线方法 | 公开的各类开源视觉语言模型 |
| 现有闭源VLMs | 基线方法 | 公开的前沿闭源视觉语言模型 |
| 本论文提出的2B evaluator | 提出模型 | 经SA-MDPO蒸馏的紧凑评估器 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验表格及对应数值，仅通过实验得出以下发现：现有开源与闭源VLMs在宏观社会价值判断上存在共享趋势与清晰差异；本论文提出的紧凑2B evaluator可与其同系列的8B模型表现相当，且接近前沿闭源VLMs的表现。

4. 关键结论和发现
- 主要发现：1. 现有开源与闭源VLMs对多模态内容的宏观社会价值判断存在共享趋势与明确差异；2. 基于SA-MDPO蒸馏的紧凑2B评估器在宏观社会价值评估任务上具备优秀性能，可媲美同系列8B模型，接近前沿闭源VLMs。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本论文提出MAVEN宏观社会价值评估框架及配套基准、评估方法与紧凑评估器，解决现有多模态内容宏观社会价值评估框架的适用性局限，实现高效且接近前沿的价值评估能力。

</details>

---

### 8. [Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies](https://arxiv.org/abs/2608.18410v1)

**Authors**: Wei Jiang, Wei Wang  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2608.18410v1  

#### Abstract
Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. S...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies

1. 论文的主要贡献和创新点
✅ 解决的问题
现有Vision-Language-Action (VLA)模型处理长多模态token序列时推理内存与计算开销大；现有效率方法主要聚焦减少视觉token，但激进的token pruning会丢弃token全部表示，较为脆弱；直接将sub-token压缩应用于VLA策略效果不佳，因视觉、语言、控制相关关键信息在多模态表示中分布不同。

🚀 提出的新方法与思路
**Role-Conditioned Sub-Token Routing (RoleSub)**：该方法先减少视觉token，再将每个保留的value表示在正交空间划分为分组，通过轻量路由机制决定保留哪些分组；路由决策基于token表示、学习到的潜在角色表示和语言上下文；该机制也可应用于语言值，无需额外移除token即可压缩视觉和语言表示。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能表现 | 匹配视觉-KV预算时，RoleSub在36项设置的33项中优于仅训练的token控制策略，激进压缩场景下增益最大，同时多数任务保留强控制性能 |
| 压缩效率 | 总KV压缩至原始的9.2--11.3%，无需额外移除token，是token pruning的有效补充 |
| 适配性 | 可同时应用于视觉和语言模态的表示压缩，适配VLA策略多模态特性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LIBERO suites | 评估RoleSub在Vision-Language-Action策略上的控制性能 |

🎯 实验设置与评估指标
任务：基于OpenVLA-OFT-7B模型，评估高效VLA策略在控制任务上的性能与压缩效率。
| 指标 | 含义 |
| --- | --- |
| 控制性能 | 衡量策略完成任务的能力，越高越好 |
| 视觉-KV预算 | 视觉相关KV缓存占用，越低越好 |
（注：论文未明确指标具体名称，以上含义基于摘要表述整理，箭头方向按常规控制任务逻辑设定）

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| trained token-only control | 对比基线策略 | 仅基于token的控制策略，用于性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表（论文未提供具体表号）：RoleSub与基线在LIBERO套件的性能对比**
| 对比维度 | RoleSub | trained token-only control |
| --- | --- | --- |
| 视觉-KV预算匹配下的性能 | 36项设置中的33项表现最优 ✅ | 对比基准 |
| 总KV压缩比例 | 9.2--11.3% ✅ | 压缩比例更高（性能受损） |
💡 结论：RoleSub在匹配视觉-KV预算时，多数LIBERO任务场景中优于仅token控制基线，同时实现较高的总KV压缩比例，且保留强控制性能。
（注：论文未报告消融实验、跨域/zero-shot迁移、鲁棒性/扰动测试、FPS/参数量等实验内容）

4. 关键结论和发现
- 主要发现：1. 匹配视觉-KV预算时，RoleSub在LIBERO套件36项设置中的33项性能优于仅训练的token控制策略，激进压缩场景下增益最显著；2. RoleSub可同时压缩视觉和语言表示，无需额外移除token，总KV压缩至原始的9.2--11.3%时仍保留多数任务的强控制性能；3. 角色条件子token路由机制是token pruning的有效补充，可实现VLA策略高效压缩。
- 方法局限性：论文未报告明确的方法局限性。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：RoleSub通过学习基于角色的子token路由机制，在不额外移除token的情况下高效压缩视觉和语言多模态表示，在匹配视觉-KV预算时多数LIBERO控制任务中表现优于仅token基线，同时实现较高KV压缩比例，为高效VLA策略提供了有效压缩方案。

</details>

---

### 9. [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](https://arxiv.org/abs/2608.18575v1)

**Authors**: Ting-Wei Li, Yuanchen Bei, Xiao Lin, Hanghang Tong  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.18575v1  

#### Abstract
Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outcomes. This motivates the task of Agent Failure Attribution: given a failed multi-agent trajectory, identify the faulty agents and their corresponding...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution
1. 论文的主要贡献和创新点
解决的问题：现有基于LLM的智能体故障归因方法（包括直接prompt、微调合成数据、复杂agentic pipeline及SOTA微调LLMs）存在计算开销大（长上下文处理、昂贵后训练、手工工作流）的问题，且即使放大LLM模型规模，其在现有基准上的准确率依然有限。
🚀 提出的新方法与思路
**AFANet**：轻量级图框架，通过建模多智能体交互轨迹的步骤级语义信号与智能体级关系，完成智能体故障归因任务，无需依赖大语言模型的生成式推理。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 计算开销 | 参数量显著更少、推理成本接近零 |
| in-domain性能 | 匹配或超过包括微调模型在内的LLM基线 |
| 架构鲁棒性 | 在不同GNN架构上性能稳定 |
| OOD适应性 | 可通过廉价的测试时适配进一步提升性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未提及具体数据集名称，用于智能体故障归因的任务场景 |
🎯 实验设置与评估指标
任务：给定失败的多智能体轨迹，识别故障智能体及其对应错误类型。
| 指标 | 含义及方向 |
| ---- | ---- |
| 论文未报告 | 论文未明确报告具体评估指标名称、数值及方向 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基于prompt的LLM故障归因方法 | LLM-based baseline | 存在长上下文处理、手工工作流等高计算开销问题 |
| 微调合成数据的LLM故障归因方法 | LLM-based baseline | 存在昂贵后训练、in-domain准确率有限的问题 |
| 复杂agentic pipeline的LLM故障归因方法 | LLM-based baseline | 存在高计算开销的手工工作流问题 |
| SOTA微调LLMs | LLM-based baseline | 放大模型规模仍难以提升in-domain任务性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（in-domain）**
论文未报告具体表号，仅提及AFANet在in-domain基准上匹配或优于包括微调模型在内的LLM-based baselines。
结论：AFANet在in-domain智能体故障归因任务上的性能可匹配或超过现有主流LLM-based基线方法。

**效率对比（FPS/参数量）**
论文未报告具体效率数值，仅提及AFANet参数量显著更少、推理成本接近零。
结论：AFANet的计算开销远低于现有基于LLM的智能体故障归因方法。

**跨域/OOD迁移性能**
论文未报告具体OOD基准的表号或数值，仅提及AFANet可通过廉价测试时适配进一步提升其在OOD基准上的性能。
结论：AFANet具备良好的OOD适应性，低成本测试时适配可进一步优化其在分布外场景下的表现。

**鲁棒性/扰动测试**
论文未报告具体鲁棒性实验的表号或数值，仅提及AFANet在不同GNN架构上保持鲁棒性能。
结论：AFANet的性能不会随底层GNN架构的变化出现大幅波动，具备良好的架构鲁棒性。

**消融实验**
论文未报告消融实验的具体模块设置及指标结果，故无相关内容。

4. 关键结论和发现
- 主要发现：① 针对智能体故障归因任务，轻量级结构化方法无需依赖昂贵的LLM生成式推理即可实现与现有LLM基线相当或更优的性能；② AFANet在不同GNN架构上性能稳定，具备良好的架构鲁棒性；③ 对AFANet进行廉价的测试时适配，可进一步提升其在OOD基准上的表现。
- 方法局限性：论文未明确报告本方法的局限性。
- 未来工作：论文未明确报告本研究的未来工作方向。

> ✅ **总结一句话**：本研究提出轻量级图框架AFANet，无需依赖昂贵的LLM生成式推理，即可在智能体故障归因任务上实现匹配或优于现有主流LLM基线方法的性能，且具备良好的架构鲁棒性与OOD适应性。

</details>

---

### 10. [What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072v1)

**Authors**: Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong, Zhong Zhang, Maosong Sun, Yankai Lin  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.19072v1  

#### Abstract
Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, itera...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：What is Missing from AI Post-Training AI: An Empirical Analysis
1. 论文的主要贡献和创新点
✅ 解决的问题
当前AI post-training（即AI-for-AI）技术混淆了agent的两种核心能力：execution-level能力（在选定训练策略内迭代调整）与strategy-level能力（根据实验证据调整高层训练判断）；通过分析公开post-training轨迹发现，现有agent的训练策略在执行初期即被锁定，后续全部预算仅用于选定策略内的局部调整，无法开展策略级改进；针对“缺乏经验、缺乏引导、推理计算不足”三种常见性能缺陷解释，系统性干预实验显示这三种因素均非核心问题。
各方法的缺陷：
- 经验驱动脚手架：仅提升execution-level性能，无法改变训练策略；
- 人工引导干预：可临时重定向初始策略，但训练启动后会落回局部调整循环；
- 额外推理计算：仅在易任务上有增益，对最难任务几乎无效果。

🚀 提出的新方法与思路
**策略自发再评估机制**：通过大规模实证分析，明确当前AI post-training agent的核心缺陷并非经验、人工引导或推理计算不足，而是缺乏在执行过程中自发重新评估训练策略的机制，该机制是未来AI-for-AI改进的核心方向。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
能力区分 | 首次明确区分AI post-training中execution-level迭代与strategy-level调整两种核心能力
实证基础 | 基于大规模公开post-training轨迹开展分析，结论具备普适性
缺陷定位 | 系统性排除三种常见解释，精准定位当前AI post-training agent的核心问题

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
大规模公开post-training trajectories | 分析AI post-training agent的策略锁定及局部调整情况

🎯 实验设置与评估指标
任务：AI post-training的性能优化
指标 | 含义
--- | ---
GSM8K分数 | 数学推理任务性能，值越高越好
HumanEval分数 | 代码生成任务性能，值越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
经验驱动脚手架 | 干预方法 | 补充经验以提升execution-level执行效果
人工引导干预 | 干预方法 | 人工介入以调整初始训练策略
增加推理计算 | 干预方法 | 提升agent的推理计算资源

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文实验：不同干预方法的性能提升（场景：GSM8K、HumanEval任务）**
方法 | GSM8K分数提升 | HumanEval分数提升
--- | --- | ---
经验驱动脚手架 | +12.6 points | +40.8 points
人工引导干预 | 论文未报告 | 论文未报告
增加推理计算（易任务） | 论文未报告 | 论文未报告
增加推理计算（最难任务） | 论文未报告 | 论文未报告

💡 结论：经验驱动脚手架可显著提升AI post-training的execution-level性能，但无法改变训练策略；人工引导和增加推理计算的效果随任务类型或难度变化。

其余实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1. 当前AI post-training agent的训练策略在执行初期即锁定，全部后续预算仅用于选定策略内的局部调整，缺失strategy-level的调整能力；2. 补全经验、人工引导、增加推理计算均无法解决核心问题，根本缺陷为缺乏执行过程中自发重新评估训练策略的机制；3. 不同干预方法效果存在差异：经验提升执行不改变策略，人工引导暂时有效但会回到局部调整循环，计算增益仅在易任务存在。
- 方法局限性：论文未报告
- 未来工作：研究如何使AI post-training agent具备在执行过程中自发重新评估训练策略的机制。

✅ **总结一句话**：通过对大规模公开AI post-training轨迹的实证分析，精准定位当前AI-for-AI agent的核心缺陷为执行过程中缺乏自发再评估训练策略的机制，而非经验、引导或推理计算不足。

</details>

---

### 11. [CTTE: An Open Dual-Protocol RISC-V Trace Encoder for N-Trace and E-Trace](https://arxiv.org/abs/2608.18170v1)

**Authors**: Alexander Weiss, Albert Schulz  
**Category**: cs.AR  
**Published**: 2026-08-20  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.18170v1  

#### Abstract
RISC-V standardizes two processor-trace formats, N-Trace and E-Trace, that share a hart-to-encoder instruction trace interface but differ in compression, messages, and framing. To the best of our knowledge, as of August 2026, no publicly available synthesizable N-Trace encoder and no published hardw...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CTTE: An Open Dual-Protocol RISC-V Trace Encoder for N-Trace and E-Trace
1. 论文的主要贡献和创新点
✅ 解决的问题
截至2026年8月，尚未有公开可用的可合成N-Trace编码器，也无已发表的同时支持N-Trace和E-Trace两个后端且共用公共前端的硬件编码器。
🚀 **CTTE**：提出一款开放的SystemVerilog跟踪编码器，包含协议无关的前端，支持选择N-Trace/Nexus或E-Trace后端；实现N-Trace 1.0程序跟踪消息集（两种指令跟踪模式），支持参数化N-Trace地址宽度，遵循RISC-V Trace Control Interface，可在状态重新收敛前宣布输出带宽损失；同时支持源侧进程上下文过滤。
🔍 相比现有方法的优势
| 维度 | 现有方法缺陷 | CTTE优势 |
|------|--------------|----------|
| 协议支持 | 无同时支持N-Trace和E-Trace双后端的公开硬件编码器 | 提供可切换的N-Trace或E-Trace后端，共用同一前端 |
| 可合成性 | 无公开的可合成N-Trace硬件编码器 | 开源可合成的SystemVerilog实现，采用CERN-OHL-S-2.0许可 |
| 可移植性 | 未明确支持多供应商RISC-V核集成 | 已与5家供应商的6个RISC-V核完成集成，专有集成提供Accemic商业许可 |
| 跟踪优化 | 未提及进程上下文过滤的优化效果 | 支持源侧进程上下文过滤，可在固定缓冲区中将目标进程的观察深度翻倍 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 64位RISC-V系统（含双核SMP系统） | 评估CTTE在启动Linux场景下的跟踪编码性能 |
🎯 实验设置与评估指标
实验任务为评估CTTE在RISC-V系统中的跟踪编码性能及进程上下文过滤效果，指标含义如下：
| 指标 | 含义 |
|------|------|
| 每条退役指令的跟踪成本 | 跟踪编码消耗的比特数，↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| - | - | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**实验结果：RISC-V系统跟踪成本（未报告表号）**
| 硬件配置 | 工作负载 | 跟踪成本（bits per retired instruction） |
|----------|----------|------------------------------------------|
| 固定 | 不同工作负载 | 0.21~4.90 |
💡 结论：CTTE的跟踪编码性能受工作负载影响，在固定硬件与配置下，选择合适工作负载可显著降低跟踪成本。

4. 关键结论和发现
- 主要发现：① CTTE是首个公开的支持N-Trace和E-Trace双后端且共用公共前端的可合成RISC-V跟踪硬件编码器；② 源侧进程上下文过滤可在固定缓冲区中将目标进程的观察深度翻倍；③ 不同工作负载下RISC-V系统的跟踪成本差异较大。
- 方法局限性：未报告具体的最优跟踪成本对应的工作负载，未提供与同类双协议编码器的详细性能对比。
- 未来工作：论文未明确报告。
> ✅ **总结一句话**：CTTE是一款开放的双协议RISC-V跟踪编码器，具备共用协议无关前端的N-Trace/E-Trace双后端支持，已集成多供应商RISC-V核，在Linux系统中可通过源侧进程上下文过滤提升目标进程观察深度，跟踪成本受工作负载影响。

</details>

---

### 12. [SingularClip: Preventing Spectral Collapse to Maintain Plasticity in Continual and Reinforcement Learning](https://arxiv.org/abs/2608.18319v1)

**Authors**: Tyler Kastner, Nimrod De La Vega, Amir-massoud Farahmand  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.18319v1  

#### Abstract
Neural networks trained on nonstationary tasks frequently lose the ability to fit new targets, a phenomenon referred to as loss of plasticity. We identify a novel source of plasticity loss due to the growing anisotropy of weight matrices' singular values during training, and analyze this phenomenon ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SingularClip: Preventing Spectral Collapse to Maintain Plasticity in Continual and Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
神经网络在非平稳任务训练过程中，会出现丧失拟合新目标的“可塑性损失”现象；论文识别出该可塑性损失的一个新来源：训练过程中权重矩阵的奇异值各向异性不断增长。

🚀 提出的新方法与思路
**SingularClip**：一种周期性对所有权重矩阵的奇异值进行裁剪的过程，用于缓解上述由奇异值各向异性增长导致的可塑性损失问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务适配性 | 在持续监督学习和深度强化学习的一系列任务中，相较基线方法表现更强 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：在持续监督学习和深度强化学习的一系列任务上进行评估
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未提供具体表号与数值，因此：
论文未报告

4. 关键结论和发现
- 主要发现：1. 非平稳任务训练导致的神经网络可塑性损失存在新诱因，即训练中权重矩阵奇异值各向异性持续增长；2. SingularClip可缓解该诱因带来的可塑性损失。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文识别出非平稳任务训练中神经网络可塑性损失的新来源，提出SingularClip方法，在持续监督学习和深度强化学习的多类任务上相较基线方法表现更优。

</details>

---

### 13. [Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR](https://arxiv.org/abs/2608.18574v1)

**Authors**: Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, Lifeng Fan  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.18574v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) commonly post-trains reasoning models on multiple tasks, while rerunning multitask RLVR (MTRL) as new tasks are added makes capability expansion costly. We therefore study continual RLVR, which updates the existing model as each task arrives. The...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR
1. 论文的主要贡献和创新点
✅ 解决的问题
带可验证奖励的强化学习（RLVR）在新增任务时，采用多任务RLVR（MTRL）进行联合训练的方式存在能力扩展成本高昂的痛点；而普通持续RLVR方法仅更新现有模型，虽存在少量遗忘，但最终性能仍无法达到联合训练的MTRL水平。

🚀 提出的新方法与思路
**Continual Prompt Replay (CPR)**：该方法利用任务间的共享推理结构，通过回放之前任务的提示，并使用当前策略重新生成对应响应，以此提升到达任务及未来任务的学习效果，使模型平均性能可达到MTRL级别。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 最终任务性能 | 平均达到多任务联合训练MTRL级别的性能 |
| 能力扩展成本 | 避免新增任务时重新进行多任务训练，降低了持续学习的训练成本 |
| 性能可靠性 | 是论文中唯一一种平均性能可达到MTRL级别的持续RLVR方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Continual Reasoning Gym | 用于持续RLVR实验的benchmark环境，包含文本和视觉推理任务，组织为五个任务序列 |

🎯 实验设置与评估指标
实验设置：在由Continual Reasoning Gym构建的持续RLVR场景下，针对包含文本和视觉推理任务的五个任务序列，评估不同方法的性能表现。
| 指标 | 含义 | 箭头方向 |
| --- | --- | --- |
| 最终任务性能 | 模型完成所有任务序列后的综合性能 | ↑ 越高越好 |
| 遗忘程度 | 模型对旧任务学习后性能的保留程度 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| MTRL | 多任务联合训练基线 | 对所有任务统一训练，性能表现最优但新增任务时训练成本高 |
| Sequential RLVR | 普通持续RLVR方法 | 每次新任务到来时仅更新现有模型，存在少量遗忘，最终性能低于MTRL |
| CPR | 提出的持续RLVR方法 | 利用共享推理结构，通过回放旧任务提示并重新生成响应提升性能，平均性能达MTRL级别 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 顺序RLVR方法存在少量遗忘，但其最终性能仍显著低于多任务联合训练的MTRL模型；② 遗忘仅能解释MTRL与顺序RLVR之间性能差距的一部分，核心差距源于未利用任务间的共享推理；③ 提出的CPR方法通过回放旧任务提示并重新生成响应，可利用共享推理，平均性能达到MTRL级别，是论文中唯一一种实现该效果的持续RLVR方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文针对持续RLVR中新增任务时多任务RLVR（MTRL）训练成本高、普通顺序更新模型性能不足的痛点，提出基于共享推理的CPR方法，使模型平均性能达到MTRL级别，为持续RLVR的发展提供了新方向。

</details>

---

### 14. [Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning](https://arxiv.org/abs/2608.18767v1)

**Authors**: Shiyu Miao, Yunlong Mao, Zirui Huang, Liang Yao, Tianshuo Zheng, Yanhui Gu, Fan Liu, Sheng Zhong  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.18767v1  

#### Abstract
Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface is a faithful derivative of the client's full-label training objective. This gradient-objective consistency allows a curious server to recover priv...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
梯度匹配攻击（GMAs）在大型语言模型拆分学习（LLM Split Learning）中依赖“拆分接口处暴露的梯度是客户端完整标签训练目标的忠实导数”这一未被充分探索的关键假设，好奇的服务器可通过搜索能产生观测梯度的序列来恢复私有标签，造成隐私泄露风险。

🚀 提出的新方法与思路
**Selective Autoregressive Supervision**：从掩码代理损失而非攻击者假设的完整标签目标中导出暴露梯度，引入目标维度的不一致性，打破梯度与目标的一致性。
**Scale Blinding**：应用随机乘性缩放操作，模糊梯度的自然幅度，引入梯度尺度维度的不一致性。
**Directional Privatization**：通过von Mises-Fisher（vMF）机制随机化梯度方向，同时在方向度量差分隐私（Differential Privacy）保证下保持梯度大小，引入梯度方向维度的不一致性，使攻击者无法通过梯度推导有效标签序列。
**Dual-Track Backpropagation**：保留Top段从所有目标token学习的能力，维持模型优化效用。
**Bottom-Gradient Recovery**：为Bottom段优化恢复有效梯度，确保模型可训练性。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
隐私防护能力 | 打破GMAs依赖的核心梯度-目标一致性，无合理标签序列可解释观测到的梯度
优化效用 | 保留模型训练所需的优化信息，维持模型可训练性
隐私-效用权衡 | 在相当的微调性能下，防护效果优于现有防御方法

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未报告

🎯 实验设置与评估指标
任务设定及评估指标含义：论文未报告
指标 | 含义
--- | ---
论文未报告 | 论文未报告

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | 论文未报告 | 论文未报告

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
论文未报告

4. 关键结论和发现
- 主要发现：Gradient Mirage通过在目标、尺度、方向三个梯度相关维度引入不一致性，成功破坏梯度匹配攻击的核心假设，同时保留了模型训练的优化效用，实现了更优的隐私-效用权衡。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Gradient Mirage是一种针对LLM拆分学习中梯度匹配攻击的防御方法，通过多维度梯度扰动打破攻击者利用梯度恢复私有标签的可能性，同时维持模型训练的优化效用，实现了更优的隐私-效用平衡。

</details>

---

### 15. [Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions](https://arxiv.org/abs/2608.19151v1)

**Authors**: Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.19151v1  

#### Abstract
We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside par...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
1. 论文的主要贡献和创新点
✅ 解决的问题
多元Hawkes过程驱动的随机微分方程的随机控制问题属于非马尔可夫场景，因Hawkes强度的路径依赖特性，该问题无法用仅适用特定马尔可夫核的经典随机控制理论求解。
🚀 提出的新方法与思路
**马尔可夫化近似算法**：开发有限维马尔可夫化过程与算法，将多元Hawkes过程近似为指数核混合形式，证明该近似过程、其强度及问题价值函数收敛至原始非马尔可夫过程与原问题价值；
**Hawkes-CT DDPG算法**：对马尔可夫化后的问题构建连续时间确定性策略梯度学习算法，即Hawkes-CT DDPG，属于模型-free算法，可在未知Hawkes核系数的情况下，通过观测事件时间、SDE解的实现及一组衰减滤波器求解非马尔可夫的Hawkes驱动优化问题。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
问题场景覆盖 | 可处理经典随机控制理论无法适配的多元Hawkes驱动非马尔可夫SDE控制问题
算法属性 | 模型-free的连续时间强化学习算法，无需预先已知Hawkes核系数
观测要求 | 仅需观测事件时间、SDE解实现及一组衰减滤波器，降低了对核系数等潜在参数的观测需求
2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | 论文未明确说明实验使用的具体数据集
🎯 实验设置与评估指标
任务为在simple exponential、Erlang、power-law三种不同类型的Hawkes核下，对比提出的Hawkes-CT DDPG方法与离散时间强化学习技术的性能。论文未报告具体评估指标及指标含义。
⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
离散时间强化学习技术 | 离散时间强化学习方法 | 适用于马尔可夫场景，无法直接处理非马尔可夫Hawkes驱动的控制问题
3. 主要实验结果和性能指标
论文未报告具体的主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性测试、消融实验等定量结果，未提供相关实验的表号、数值等信息。
4. 关键结论和发现
- 主要发现：1. 马尔可夫化近似过程及其收敛性证明为非马尔可夫Hawkes驱动SDE的控制问题提供了可转化为马尔可夫场景的求解路径；2. Hawkes-CT DDPG算法可在未知Hawkes核系数的条件下，通过指定观测序列实现非马尔可夫Hawkes驱动的优化求解；3. 论文对比了提出的方法与离散时间强化学习技术在三种不同Hawkes核下的表现，但未披露具体性能数值。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

✅ **总结一句话**：本文针对多元Hawkes过程驱动SDE的非马尔可夫随机控制难题，提出马尔可夫化近似方法及Hawkes-CT DDPG连续时间强化学习算法，实现未知核系数下的非马尔可夫优化求解。

</details>

---

### 16. [Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving](https://arxiv.org/abs/2608.18084v1)

**Authors**: Zhuo Liu, Ding Yu, Hangfeng He  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.18084v1  

#### Abstract
Theorem proving in real-world Lean 4 projects is challenging because proofs often depend on project-specific context. While iterative refinement can use compiler errors to repair failed proofs, reusing failed attempts requires careful search control: some proofs provide better starting points than o...

---

### 17. [FPGA Lifecycle Management for RISC-V Systems](https://arxiv.org/abs/2608.18156v1)

**Authors**: Tianhai Liu, James J. Hunt  
**Category**: cs.AR  
**Published**: 2026-08-20  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.18156v1  

#### Abstract
FPGA lifecycle management remains tied to proprietary toolchains and host architectures, leaving RISC-V without a vendor-neutral model for scalable bitstream deployment. A host-agnostic control-plane architecture is presented that shifts lifecycle management to the operating-system layer by leveragi...

---

### 18. [Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions](https://arxiv.org/abs/2608.18078v1)

**Authors**: Matthew Riemer, Tommaso Tosato, Amin Memarian, Maximilian Puelma Touzel, Glen Berseth, Irina Rish, Guillaume Dumas  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.18078v1  

#### Abstract
This position paper argues that AI agents with chain-of-thought reasoning capabilities are predisposed to exhibit collusive behavior and should be required to obtain behavioral certification before making decisions that affect economic markets. This is because integrating these agents into society c...

---

### 19. [Multi-stage neural operator learning with application for convolutions](https://arxiv.org/abs/2608.18851v1)

**Authors**: Zhiping Mao, Zhenye Wen, Yong Zhang, Xiaofei Zhao  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.18851v1  

#### Abstract
Convolution integrals widely exist in applications, and to enable fast and accurate computations, this paper introduces two general multi-stage neural operator learning frameworks. The first, Deep Collocation Neural Operator (DCNO), is a supervised approach that iteratively refines the operator appr...

---

### 20. [A Fault-Tolerant Spike-Time Interface for Approximate Agreement in Distributed Neuromorphic Systems](https://arxiv.org/abs/2608.18151v1)

**Authors**: Arman Ferdowsi, Maryam DehghanChenary, Kevin Tierney, Atakan Aral  
**Category**: cs.AR  
**Published**: 2026-08-20  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2608.18151v1  

#### Abstract
Large neuromorphic systems contain many processing tiles that may replicate a shared control parameter such as a threshold reference. If these copies diverge, identical inputs may be processed under different intended settings. We study how tiles can reduce this disagreement when communication carri...

---

### 21. [RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training](https://arxiv.org/abs/2608.18682v1)

**Authors**: Yugu Li, Jimmy Cao, Jianglin Qiao, Siyi Hu  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.18682v1  

#### Abstract
Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, and conduct iterative search beyond single-turn settings. Yet multi-turn RL training remains highly unstable, often causing severe performance degrad...

---

### 22. [ChiroEcho: extending automated bat vocalisation classification beyond the learned taxonomy](https://arxiv.org/abs/2608.18191v1)

**Authors**: Burooj Ghani, Welmoed Eversteijn, Milan van Hirtum, Juan Sebasti\'an Ca\~nas, Vincent J. Kalkman, Dan Stowell, A. Leonie Baier  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.18191v1  

#### Abstract
Bats are key indicators of ecosystem health and are protected throughout Europe, making reliable population monitoring a conservation priority. Their cryptic nocturnal lifestyle makes passive acoustic monitoring essential, yet automated identification remains difficult as echolocation calls vary wit...

---

### 23. [A Unifying Relational Perspective on Expressive Lottery Tickets](https://arxiv.org/abs/2608.18819v1)

**Authors**: Lorenz Kummer, Samir Moustafa, Anatol Ehrlich, Franka Bause, Marco Nennstiel, Przemys{\l}aw Andrzej Wa{\l}\c{e}ga, Nils Morten Kriege  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.18819v1  

#### Abstract
Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is poorly understood. The Strong Expressive Lottery Ticket Hypothesis (SELTH) posits the existence of sparse GNNs that preserve Weisfeiler-Leman (WL) ...

---

### 24. [Pairwise Ranking Outperforms Single-Action RL for Offline Explanation Selection: A Practical Lesson](https://arxiv.org/abs/2608.18531v1)

**Authors**: Tanay Chowdhury, Saeideh Shahrokh Esfahani  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.18531v1  

#### Abstract
Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic. We separate generation from selection: explanations are produced ahead of ti...

---

### 25. [You Are What You Prompt: Prompt Quality, Domain Shift, and Uncertainty in Agrifood Vision-Language Models](https://arxiv.org/abs/2608.18116v1)

**Authors**: Andrea Morales-Garz\'on, Salvador L\'opez-Joya, Miguel L\'opez-P\'erez, Maria J. Martin-Bautista  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2608.18116v1  

#### Abstract
Vision-language models enable zero-shot classification through natural language prompts, but performance is sensitive to prompt formulation, especially in specialized domains. Zero-shot Prompt Ensembling (ZPE) addresses this by weighting prompts by discriminative signal, yet its behavior under domai...

---

### 26. [An Empirical Benchmark of Deep Time-Series Models for Smart Meter Energy Forecasting](https://arxiv.org/abs/2608.18675v1)

**Authors**: Behnaz Kavoosighafi, Maria Eidenskog, Wiktoria Glad, Katerina Vrotsou  
**Category**: cs.LG  
**Published**: 2026-08-20  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.18675v1  

#### Abstract
Accurate forecasting of energy consumption is important for the efficient operation of power systems, with direct implications for operational costs, energy management, and system maintenance. Due to the availability of extensive high-resolution consumption data from smart meters, data-driven method...

---

### 27. [APEX: A Dual-Sparsity Accelerator for Precise and Efficient SNN Inference](https://arxiv.org/abs/2608.19046v1)

**Authors**: Devgokul Bawa Venkatesh, Sreeram Radhakrishnan, Rajshekhar Rakshit, Gopalakrishnan Srinivasan  
**Category**: cs.AR  
**Published**: 2026-08-20  
**Score**: 18.5  
**Type**: new  
**ArXiv ID**: 2608.19046v1  

#### Abstract
Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to Artificial Neural Networks (ANNs), leveraging sparse accumulate operations in the place of power-hungry multiply-and-accumulate operations. ANN-SNN conversion is a widely adopted approach to realize deep SNNs with accu...

---

### 28. [Breaking the weakest link to evade vision language models](https://arxiv.org/abs/2608.18938v1)

**Authors**: Ilan Zini, Boussad Addad, Katarzyna Kapusta  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 16.5  
**Type**: new  
**ArXiv ID**: 2608.18938v1  

#### Abstract
Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains i...

---

### 29. [Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack](https://arxiv.org/abs/2608.18182v1)

**Authors**: Weiwen Xia, Yuxin Cui, E Cao  
**Category**: cs.CL  
**Published**: 2026-08-20  
**Score**: 16.0  
**Type**: new  
**ArXiv ID**: 2608.18182v1  

#### Abstract
Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models. On server CPUs, INT8 quantization offers an attractive latency-throughput-cost trade-off, but users increasingly expect...

---

### 30. [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](https://arxiv.org/abs/2608.18884v1)

**Authors**: Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li  
**Category**: cs.AI  
**Published**: 2026-08-20  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2608.18884v1  

#### Abstract
Reinforcement-learning training of reasoning LLMs (e.g., GRPO) is expensive and requires a controllable environment, committing every contribution to a full training pipeline. We present EvoResearcher, a training-free, inference-time protocol that adds cost-bounded self-reflection to a single frozen...

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
