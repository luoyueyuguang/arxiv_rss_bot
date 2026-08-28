# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-28 17:49:22 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](https://arxiv.org/abs/2608.27351v1)

**Authors**: Yunpeng Ba, Zhi Zheng, Yue Xie, Jiaqing Li, Xialiang Tong, Tao Zhong, Mingxuan Yuan, Zhichao Lu, Xuyang Wu, Zhenkun Wang  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 105.5  
**Type**: new  
**ArXiv ID**: 2608.27351v1  

#### Abstract
Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Opti...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

理解用于LLM推理的进化策略：比GRPO更宽的推理覆盖
1. 论文的主要贡献和创新点
✅ 解决的问题
进化策略（ES）作为一种用于LLM推理的内存高效后训练范式，其优化行为尚未被系统研究，导致难以明确其相较于主流后训练范式（组相对策略优化GRPO）的优势范围；GRPO存在熵崩溃问题，且ES的参数漂移特性、参数更新的功能性影响、超参数设计等方面也缺乏系统分析，限制了其实际应用。

🚀 提出的新方法与思路
**ES机制与特性的系统研究**：通过系统分析ES的动力学与机制，从理论上证明ES种群的verifier-projected Jensen-Shannon多样性有助于更高的Pass@K性能；明确ES能实现更宽的推理覆盖，从而更好挖掘预训练LLM的推理能力；同时发现ES的任务性能增益仅来自稀疏的大 magnitude 参数更新（即功能稀疏性），而非大规模参数移动，且ES的整体参数漂移不会导致灾难性遗忘。
**顺序GRPO-ES训练策略**：将GRPO与ES按顺序组合，发挥GRPO在提升Pass@1指标上的优势，同时结合ES在提升Pass@K指标上的增益，实现两者优势的互补。
**ES超参数设计研究**：探究ES超参数对其有效性的影响，发现更大规模的LLM在应用ES时可采用更小的种群规模。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理覆盖范围 | 可实现比GRPO更宽的推理覆盖，更好挖掘预训练LLM的推理能力 |
| 熵特性 | 不存在GRPO的熵崩溃问题 |
| 性能表现 | 比GRPO达到更高的Pass@K指标，通过顺序GRPO-ES策略可结合GRPO的Pass@1优势 |
| 参数特性 | 任务性能增益仅来自稀疏的大 magnitude 参数更新，整体参数漂移不会导致灾难性遗忘 |
| 超参数适配 | 更大规模的LLM应用ES时，可使用更小的种群规模 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | LLM推理后训练的效果评估 |

🎯 实验设置与评估指标
任务：开展LLM推理的后训练实验，对比分析ES与GRPO的性能及特性。
| 指标 | 含义 |
| --- | --- |
| Pass@1 | 单个样本的推理通过率，越高越好（↑） |
| Pass@K | K个候选样本中至少一个正确的推理通过率，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO | 主流LLM后训练范式 | Pass@1表现较好，存在熵崩溃，Pass@K表现弱 |
| Evolution Strategies (ES) | 内存高效LLM后训练范式 | 内存效率高，无熵崩溃，Pass@K表现优于GRPO，更大规模LLM需更小种群规模 |
| 顺序GRPO-ES训练策略 | 组合后训练策略 | 结合GRPO的Pass@1优势与ES的Pass@K增益 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能对比**（场景：LLM推理后训练）
论文中未报告具体指标数值，仅指出ES的Pass@K高于GRPO，GRPO存在熵崩溃，ES无熵崩溃。
💡 结论：在LLM推理后训练中，ES相比GRPO在更高的Pass@K指标上表现更优，且不存在GRPO的熵崩溃问题。
**效率对比**（场景：ES与GRPO的内存效率）
论文未报告
**跨域/zero-shot迁移**（场景：LLM推理的泛化能力）
论文未报告
**鲁棒性/扰动测试**（场景：ES的稳定性）
论文未报告
**消融实验**（场景：ES的功能稀疏性与参数漂移）
论文未报告

4. 关键结论和发现
- 主要发现：① ES种群的verifier-projected Jensen-Shannon多样性理论上有助于更高Pass@K，实际具备比GRPO更宽的推理覆盖，Pass@K表现更优且无GRPO的熵崩溃问题；② ES的任务性能增益仅来自稀疏的大 magnitude 参数更新，整体参数漂移显著但不会导致灾难性遗忘；③ ES需适配LLM规模设计超参数，更大规模LLM应用ES时可采用更小的种群规模，且是区别于GRPO的独立推理后训练范式。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文系统分析了进化策略（ES）在LLM推理后训练中的特性，发现其具备比组相对策略优化（GRPO）更宽的推理覆盖，可通过顺序GRPO-ES策略结合两者优势，且参数更新具有功能性稀疏性，明确了ES作为独立后训练范式的价值，而非GRPO的内存高效替代方案。

</details>

---

### 2. [VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference](https://arxiv.org/abs/2608.26523v1)

**Authors**: Yan Shi, Xiaochao Wang, Jingchun Gao, Jintao Luo, Xinyi Zhou, Feng Liu, Kui Luo, Xushi Li, Xinjie Guo, Liangjun Feng  
**Category**: cs.DC  
**Published**: 2026-08-28  
**Score**: 104.0  
**Type**: new  
**ArXiv ID**: 2608.26523v1  

#### Abstract
Chunked prefill pipeline parallelism (CPP) is a key technique for LLM inference. However, equal-size chunks exhibit imbalanced latency, as later chunks attend longer prefix KV caches and incur higher attention costs, leading to pipeline bubbles. Existing approaches mitigate this imbalance through dy...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Chunked prefill的Pipeline Parallelism（CPP）采用等大小chunk时，后续chunk因注意力KVCache更长导致延迟更高，引发流水线气泡；已有的动态chunk调整方法（DCPP）通过负载均衡减少气泡，但以调度开销为代价，在长序列场景下开销的负面影响超过收益。

🚀 提出的新方法与思路
**Virtual Pipeline Parallelism (VPP)**：保持chunk大小固定，通过优化流水线布局的虚拟stage实现并行；采用V形虚拟stage遍历策略，将每个chunk的昂贵中间计算stage与相邻chunk的轻量头尾stage重叠，减少流水线气泡；结合异步通信与流水线打包技术，进一步降低通信停顿与跨请求排空气泡。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 长序列吞吐量 | 相比DCPP最高提升13.1% |
| 混合工作负载吞吐量 | 相比DCPP提升6.7% |
| 512K-token DeepSeek-V3.1预填充流水线气泡率 | 相比DCPP从6.4%降至0.1%，降低98.0% |
| 短序列性能 | 保留与基准方法相当的性能 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体使用的数据集名称。

🎯 实验设置与评估指标
任务：长上下文LLM的chunked prefill推理性能评估
| 指标 | 含义 |
| ---- | ---- |
| 吞吐量 | 越高越好 |
| 流水线气泡率 | 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| CPP（Equal-size Chunked Prefill Pipeline Parallelism） | 基线方法 | 采用等大小chunk，因后续chunk注意力KVCache更长导致延迟不平衡，产生流水线气泡 |
| DCPP（Dynamic CPP） | 基线方法 | 通过动态调整chunk大小实现负载均衡减少气泡，但引入调度开销，长序列场景下不利 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**长序列场景性能对比（1M token序列，16 Ascend 910C NPUs）**
| 方法 | 长序列吞吐量提升率 |
| ---- | ---- |
| VPP vs DCPP | 最高13.1% ✅ |
💡 结论：在最长1M token的序列场景下，VPP相比DCPP实现了显著的吞吐量提升。

**混合工作负载性能对比**
| 方法 | 混合工作负载吞吐量提升率 |
| ---- | ---- |
| VPP vs DCPP | 6.7% ✅ |
💡 结论：在混合工作负载场景下，VPP相比DCPP仍保持稳定的吞吐量提升。

**512K-token DeepSeek-V3.1预填充流水线气泡率**
| 方法 | 流水线气泡率 |
| ---- | ---- |
| DCPP | 6.4% |
| VPP | 0.1% ✅ |
💡 结论：在512K-token的DeepSeek-V3.1预填充任务中，VPP大幅降低了流水线气泡率，减少达98.0%。

其余实验（主benchmark性能中的L2/碰撞率、效率对比中的FPS/参数量、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现1：VPP通过固定chunk大小+V形虚拟stage遍历的策略，解决了DCPP中负载均衡与调度开销的冲突，在长序列场景下实现了性能优势。
- 主要发现2：VPP在混合工作负载下仍保持吞吐量提升，同时未损失短序列性能，适用场景更广泛。
- 主要发现3：在512K-token的DeepSeek-V3.1预填充任务中，VPP将流水线气泡率从6.4%降至0.1%，大幅提升了资源利用率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：VPP是一种优化虚拟stage布局的Chunked Prefill并行方法，通过固定chunk大小、重叠相邻stage计算等策略，解决了现有长上下文LLM预填充方法的流水线气泡与调度开销问题，显著提升了吞吐量与资源利用率。

</details>

---

### 3. [AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes](https://arxiv.org/abs/2608.26193v1)

**Authors**: Yibo Wang, Rui Yang, Jisheng Dang, Bimei Wang, Yitao Wu, Pengfei Cao, Wencan Zhang, Hong Peng, Bin Hu, Tat-Seng Chua  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 74.0  
**Type**: new  
**ArXiv ID**: 2608.26193v1  

#### Abstract
Multimodal large language models (MLLMs) achieve strong performance on VQA and scene understanding, yet affective reasoning remains vulnerable to shortcut behavior. Models may predict correct answers while neglecting people-centric cues such as micro expressions and body language, which weakens trac...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有多模态大语言模型（MLLMs）开展情感推理时存在shortcut behavior，虽能预测正确答案，但会忽略微表情、肢体语言等以人为中心的线索，削弱了推理的可追溯性与外部验证能力。
- 现有强化学习（RL）方法多仅奖励上下文或逻辑一致性，未明确强制模型关注人类相关证据。
- 采用LLM作为评判者的评分常出现分数聚类问题，降低了奖励信号的可区分性。

🚀 提出的新方法与思路
**AffectOmni框架**：采用GRPO（Generative Reward Preference Optimization）训练，用于实现可验证的以人为中心的接地情感推理。
**People Focus奖励**：用于鼓励模型在推理过程中主动选择以人为中心的证据，强化对人类相关线索的关注度。
**Temporal Order奖励**：用于引导模型进行具有时间结构的情感推理，优化时间敏感任务的表现。
**within-group comparative scoring**：生成更稳定、区分度更高的奖励信号，解决传统LLM评判评分聚类的问题。
**Thinking Summarizer模块**：将自由形式的推理理由转换为可执行的证据指令，结合SAM3（Segment Anything Model 3）获取像素级的证据区域，为训练循环外部提供可审计的接地接口。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 情感推理可靠性 | 可追溯性与外部验证能力更强，避免忽略以人为中心的关键线索 |
| 奖励信号质量 | 采用组内对比评分，解决LLM评判的分数聚类问题，提升奖励区分度 |
| 时间敏感任务性能 | 引入时间顺序奖励，优化时间结构化推理的表现 |
| 基准任务性能 | 在公开基准上优于7B规模的开源多模态基线模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| IntentBench | 论文中用于验证模型性能的基准数据集之一 |
| Daily Omni | 论文中用于验证模型性能的基准数据集之一 |
| WorldSense | 论文中用于验证模型性能的基准数据集之一 |

🎯 实验设置与评估指标
任务为以人为中心的基于接地的情感推理，评估指标及含义如下：
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 情感识别准确率 | ↑ 越高越好 |
| 时间敏感任务性能 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 开源7B规模基线模型 | 多模态大语言模型基线 | 论文中用于对比的基准模型，为7B规模的开源多模态大语言模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
主benchmark性能：论文未明确报告定量结果对应的表号、图号等来源，无法给出具体数值。
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 论文提出的AffectOmni框架在IntentBench、Daily Omni、WorldSense三个公开基准上，综合性能优于7B规模的开源多模态基线模型。
- 引入People Focus奖励、Temporal Order奖励及within-group comparative scoring，可有效提升模型情感推理的质量与奖励信号的区分度。
- Thinking Summarizer结合SAM3的方案，为情感推理提供了可外部审计的像素级接地证据接口，增强了推理的可验证性。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：论文提出的AffectOmni是一款采用GRPO训练、具备可验证接地证据接口的以人为中心的情感推理框架，在相关公开基准任务上的性能优于7B规模的开源多模态基线模型。

</details>

---

### 4. [SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning](https://arxiv.org/abs/2608.26550v1)

**Authors**: Zhuochun Li, Yuelyu Ji, Yiming Zeng, Daqing He  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2608.26550v1  

#### Abstract
Reinforcement learning-based knowledge distillation has the potential to transfer complex reasoning from teacher to student models, yet it currently faces a critical dilemma: researchers must choose between sparse outcome-based rewards, which provide insufficient logical guidance, or expensive neura...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SPEAR: Distilling Domain-Adaptive Reasoning Skeletons via Sequential Symbolic Alignment in Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
强化学习驱动的知识蒸馏用于转移复杂推理时，研究者面临核心困境：需在稀疏的基于结果的奖励（提供的逻辑指导不足）和昂贵的神经过程奖励模型（PRM，用于过程级密集信号）之间做选择。

🚀 提出的新方法与思路
**SPEAR (Symbolic Process Evaluation and Alignment Reward)**：一种免训练、即插即用的序列级在线策略蒸馏的过程奖励方法；将自然语言推理轨迹投影到领域自适应的符号里程碑，为过程级推理对齐提供高效代理；使用最长公共子序列（LCS）对齐学生探索与教师里程碑，生成密集、感知顺序的奖励信号，无需外部神经验证器即可强制逻辑一致性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练要求 | 免训练、即插即用，无需依赖外部神经验证器 |
| 奖励信号特性 | 提供密集、感知顺序的序列级奖励，支持过程级推理对齐 |
| 资源成本 | 无需使用昂贵的神经过程奖励模型，降低奖励生成成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 数学数据集 | 用于数学推理任务实验 |
| 科学数据集 | 用于科学推理任务实验 |
| 常识推理数据集 | 用于常识推理任务实验 |

🎯 实验设置与评估指标
针对数学、科学、常识推理任务的序列级在线策略蒸馏，评估师生模型的推理对齐效果；论文未报告具体评估指标及方向标注。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 稀疏结果奖励方法 | 基于结果的奖励方法 | 仅提供稀疏结果信号，过程级逻辑指导不足 |
| 神经过程奖励模型(PRM) | 过程级奖励方法 | 生成过程级密集信号，但成本高昂 |
| SPEAR | 过程级奖励方法 | 免训练、即插即用，通过符号里程碑和LCS生成密集顺序感知奖励，无额外神经模型依赖 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的具体数值及对应表号、图号。

4. 关键结论和发现
- 主要发现：1. SPEAR作为免训练的过程奖励方法，有效解决了现有知识蒸馏中奖励信号选择的核心困境；2. SPEAR通过领域自适应符号里程碑与LCS的序列对齐，能为师生模型提供可靠的过程级推理监督，无需外部神经验证器；3. SPEAR在数学、科学、常识推理任务中，通过序列级蒸馏高效缩小了师生模型的推理差距。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：SPEAR是一种免训练、即插即用的过程奖励方法，通过将自然语言推理轨迹映射为领域自适应符号里程碑、结合LCS实现学生与教师推理的序列对齐，在数学、科学、常识推理任务的强化学习驱动知识蒸馏中，以低成本为师生模型提供了无需外部神经验证器的密集顺序感知奖励，有效缩小了师生间的推理差距。

</details>

---

### 5. [Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models](https://arxiv.org/abs/2608.27135v1)

**Authors**: Basel Mousi, Fahim Dalvi, Shammur Chowdhury, Firoj Alam, Nadir Durrani  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.27135v1  

#### Abstract
Multimodal foundation models are increasingly used in speech-first assistants that must interpret spoken queries and produce visually grounded decisions. Yet it remains unclear whether semantically equivalent queries yield consistent judgments across modality (text vs. speech) and language (English ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models
1. 论文的主要贡献和创新点
✅ 解决的问题：多模态基础模型应用于语音优先助手时，语义等价的查询在跨模态（文本vs语音）、跨语言（英语vs阿拉伯语）转换后是否能得到一致判断的问题不明确；现有评估指标（如聚合准确率）无法捕捉上述不一致性，且模型的部分推理失败（碎片化推理）未被充分关注。
🚀 提出的新方法与思路
**Speech-Augmented Visually Grounded Contrastive Triplet Benchmark**：引入该基准，包含来自18个MENA国家的10150张文化相关图像，每张图像配对1条支持陈述和2条看似合理但不支持的替代陈述；同时定义**Contrastive Instability**指标，即模型无法解析triplet内所有陈述的条件率，用于分离模型的碎片化推理与完全失败情况，弥补现有指标的不足。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估指标设计 | 引入Contrastive Instability指标，可有效分离模型的碎片化推理失败与完全失败，弥补聚合准确率无法捕捉跨模态/跨语言一致性问题的不足 |
| 基准覆盖范围 | 覆盖18个MENA国家的文化相关图像，兼顾地域与语言多样性，适配语音与跨语言场景下的多模态评估 |
| 资源开放性 | 公开提供基准供社区使用，推动多模态模型一致性相关研究 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Speech-Augmented Visually Grounded Contrastive Triplet Benchmark | 评估多模态模型在跨模态（文本/语音）、跨语言（英语/阿拉伯语）场景下的triplet级一致性与对比不稳定性 |
🎯 实验设置与评估指标
实验任务为评估多模态模型在文本、语音两种模态，英语、阿拉伯语两种语言下，对图像+陈述triplet的判断一致性；评估指标如下：
| 指标 | 含义 |
| --- | --- |
| Contrastive Instability | 模型无法解析triplet内所有陈述的条件率，该值越高表示模型跨模态/跨语言的一致性越差（↑越高越差） |
⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告
💡 结论：模态和语言切换会引入显著的triplet级不一致性，这类不一致性无法被聚合准确率完全捕捉，语音输入会放大模型的部分推理失败（碎片化推理）

4. 关键结论和发现
- 主要发现：① 多模态模型在跨模态（文本与语音）、跨语言（英语与阿拉伯语）转换时，会产生显著的triplet级判断不一致性；② 现有聚合准确率无法完整反映上述不一致性，语音输入会加剧模型的碎片化推理失败；③ Contrastive Instability指标能有效分离模型的碎片化推理与完全失败情况，更适配多模态一致性评估。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文针对多模态模型跨模态、跨语言转换时的一致性问题，提出了面向MENA地区文化场景的语音增强对比triplet基准与Contrastive Instability评估指标，公开基准供社区使用，发现语音会放大模型的部分推理失败且这类问题未被现有聚合指标覆盖。

</details>

---

### 6. [Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper](https://arxiv.org/abs/2608.26596v1)

**Authors**: Rongjin Li, Yuanxin Liu, Hao Zhou, Fandong Meng, Jie Zhou, Xu Sun  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.26596v1  

#### Abstract
Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or e...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大语言模型（MLLMs）作为科研助手，难以主动检查学术论文、构建全局证据视图，且无法在无预设问题或证据的场景下做出可追溯的判断；现有研究对这类无预设问题和证据的科学错误验证场景，提供的任务范式和训练研究十分有限。

🚀 提出的新方法与思路
**VERA-RL**：针对学术论文科学错误检测任务设计的强化学习框架，遵循Reason--Verify--Scan流程开展工作；
**VERA-13K**：构建的专属数据集，包含12900个样本、4300个匹配链，覆盖科研工作流程中的6类科学错误及广泛的自然科学领域；
细粒度奖励机制：引入针对推理完整性、证据对齐度、错误精度的细粒度奖励，用于模型训练优化。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务适配性 | 支持无预设问题和证据的主动科学错误验证，区别于现有依赖预设问题的范式 |
| 训练支撑 | 构建了覆盖多领域、多错误类别的专属数据集，为任务提供足量数据 |
| 模型优化 | 通过强化学习框架结合细粒度奖励，可有效提升模型的可验证推理能力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| VERA-13K | 用于科学错误检测任务的训练与评估，包含12900个样本、4300个匹配链，覆盖6类科学错误及广泛自然科学领域 |

🎯 实验设置与评估指标
任务为学术论文科学错误检测（需判定论文是否存在错误并给出基于证据的可追溯推理）。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| Scan | 论文未报告 | 论文未报告 |
| 推理完整性 | 论文未报告 | 论文未报告 |
| 证据对齐度 | 论文未报告 | 论文未报告 |
| 错误精度 | 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Gemini 3 Pro | 旗舰多模态大语言模型 | 在Scan指标上与所提方法表现接近 |
| Qwen3-VL-235B-A22B | 旗舰多模态大语言模型 | 在Scan指标上与所提方法表现接近 |
| Qwen3-VL-8B | 小型多模态大语言模型 | 经VERA-RL训练后可提升科学错误检测的可验证推理能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未提供具体实验数据对应的表号、图号等定位信息，仅能从摘要获取以下结果：训练Qwen3-VL-8B使用VERA-RL后，其在可验证推理上的表现大幅提升，在Scan指标上接近Gemini 3 Pro和Qwen3-VL-235B-A22B。

💡 结论：VERA-RL框架可有效提升小型多模态大语言模型在科学错误检测任务上的可验证推理能力，使其在Scan指标上接近旗舰多模态大语言模型。

其他实验模块：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 针对无预设问题和证据的主动科学错误验证场景，VERA-RL强化学习框架结合Reason--Verify--Scan流程能有效提升模型的可验证推理能力；2. VERA-13K数据集覆盖多领域、多错误类型，为该任务提供了充足的训练与评估数据支撑；3. 细粒度奖励机制（推理完整性、证据对齐度、错误精度）对模型训练优化有效。
- 方法局限性：论文未明确报告方法的局限性。
- 未来工作：论文未明确报告未来工作方向。

> ✅ **总结一句话**：本研究提出VERA-RL强化学习框架用于学术论文的主动科学错误验证，结合专属数据集VERA-13K和细粒度奖励机制，可提升多模态大语言模型的可验证推理能力，使其在Scan指标上接近旗舰模型。

</details>

---

### 7. [Reasoning about In-Context Samples for Machine-Translation](https://arxiv.org/abs/2608.27036v1)

**Authors**: Maxime Bouthors, Josep Crego, Fran\c{c}ois Yvon  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.27036v1  

#### Abstract
Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragmen...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Reasoning about In-Context Samples for Machine-Translation
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾是在基于LLM的机器翻译（MT）中，利用in-context samples时，现有替代方法（如标准k-shot、基础drafting）缺乏有效显式推理机制，导致翻译性能有待提升；这些方法均存在性能不足的缺陷。

🚀 提出的新方法与思路
**Fragment-based reasoning framework**：该框架中，模型首先从检索到的相似样例中提取平行源-目标片段，将这些片段作为中间推理轨迹，最终生成翻译；训练该模型时，从大型教师模型中蒸馏出silver fragments和drafts。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 翻译性能 | 显著优于标准k-shot、基础drafting等替代方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 验证fragment-based MT方法的性能 |

🎯 实验设置与评估指标
任务：基于LLM的机器翻译，利用in-context samples进行翻译。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体评估指标名称及含义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 标准k-shot | 基线方法 | 现有利用in-context samples的机器翻译方法 |
| 基础drafting | 基线方法 | 现有利用中间draft的机器翻译方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号、定量结果数值及对应场景；在涉及Qwen3模型家族、超过6种语言、每种语言最多5个领域的实验中，fragment-based MT性能显著优于上述基线方法。

4. 关键结论和发现
- 主要发现：提出的fragment-based reasoning框架结合蒸馏训练，在多语言多领域的基于LLM的机器翻译任务中性能优于标准k-shot、基础drafting等现有方法。
- 方法局限性：论文未明确报告方法的局限性相关内容。
- 未来工作：论文未提及未来工作方向相关内容。

✅ **总结一句话**：该论文提出了一种用于基于LLM的机器翻译的fragment-based reasoning框架，通过从相似样例提取平行源-目标片段作为中间推理轨迹并结合蒸馏训练，在多语言多领域场景下，其性能显著优于标准k-shot、基础drafting等现有方法。

</details>

---

### 8. [SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting](https://arxiv.org/abs/2608.26829v1)

**Authors**: Haizhao Fan, Xinyi Le  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.26829v1  

#### Abstract
Time series forecasting models operate on raw numerical sequences, lacking the semantic knowledge that domain experts implicitly leverage, such as the physical meaning of each variable, its statistical behavior, and its temporal dynamics. Recent efforts to bridge this gap fall into two camps. Some r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting
1. 论文的主要贡献和创新点
✅ 解决的问题：时序预测模型使用原始数值序列，缺失领域专家利用的语义知识（如变量的物理意义、统计行为、时间动态）；现有弥补语义不足的方法分为两类，第一类依赖推理时的大语言模型，计算成本高；第二类采用数据集级的统一文本提示，忽略单个变量的异质语义。

🚀 提出的新方法与思路
**SAGE（Seeing and Augmenting with Grounded Encoding）**：提出的端到端CLIP-based框架，融合时序、跨变量、文本、视觉信息；具体实现包括：CLIP文本编码器处理频率增强补丁和变量token，门控残差路径注入变量特定描述和统计描述符；并行地，冻结的CLIP视觉编码器通过仅训练的对比目标将渲染序列与时序表示对齐，双重使用CLIP补充互补的语义和视觉监督，无需将LLM置于预测循环。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 语义引入方式 | 采用CLIP架构端到端注入语义，无需依赖推理阶段的LLM |
| 语义建模粒度 | 支持变量级异质语义建模，而非数据集级的统一文本提示 |
| 推理计算开销 | 无需将LLM纳入预测循环，降低推理阶段的计算成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 8个长期时序基准、M4 | 验证SAGE的时序预测性能 |

🎯 实验设置与评估指标
任务：长期时间序列预测
指标：论文未报告具体评估指标名称

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基于推理时LLM的时序预测方法 | 语义引入方法 | 依赖推理阶段的LLM，计算成本高 |
| 数据集级统一文本提示的时序预测方法 | 语义引入方法 | 采用统一文本提示，忽略变量异质语义 |
| SAGE | 提出的端到端框架 | CLIP-based，无需推理时LLM，支持变量级语义建模 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主benchmark性能（长期时序预测任务）**
论文未报告具体性能数值，仅提及SAGE在8个长期基准和M4上达到SOTA。
💡 结论：论文未提供具体性能数值，仅明确SAGE在指定基准上实现SOTA。

- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未提供详细表格，仅提及多模态对齐和变量级知识对SAGE的性能有互补增益。

4. 关键结论和发现
- 主要发现：1. 原始时序数值序列缺失语义知识会制约时序预测模型的性能；2. 基于CLIP的端到端框架可在不将LLM置于预测循环的情况下，为时序预测提供互补的语义与视觉监督；3. 变量级细粒度语义建模相比数据集级统一语义提示，更适合异质变量的时序预测任务。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SAGE是一种端到端CLIP-based的视觉-语言时序预测框架，通过融合变量级语义增强与互补多模态监督，在无需推理阶段LLM的情况下实现了指定基准上的SOTA预测性能。

</details>

---

### 9. [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](https://arxiv.org/abs/2608.27142v1)

**Authors**: Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.27142v1  

#### Abstract
Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型（LLMs）在标准化图任务中潜力显著，但对真实世界中节点标识符和任务形式的变化较为脆弱；从含噪声文本中提取拓扑结构时易过拟合表面模式，稳定性差；采用多智能体系统缓解解析失败会导致延迟过高。
🚀 提出的新方法与思路
**GRAIN**：基于强化学习优化的单智能体框架，将推理过程建模为语义解析与工具执行的流水线，由结构不变性奖励（Structure Invariance Reward）引导；该奖励通过验证提取的中间图与真实拓扑结构的一致性，迫使LLM学习鲁棒的文本到结构映射，而非记忆语言人工制品。
**GRIT基准**：专门用于评估模型对名称和叙事变化（linguistic shifts）敏感性的基准。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 真实世界鲁棒性 | 缓解LLM对节点标识符、任务形式变化的脆弱性，避免过拟合表面模式 |
| 效率 | 相比多智能体基线延迟约低24% |
| 结构泛化 | 大幅缩小监督微调（SFT）模型的分布外（OOD）差距，提升泛化能力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| GRIT | 评估模型对名称和叙事变化的敏感性 |
🎯 实验设置与评估指标
任务：处理真实世界图推理中节点标识符、任务形式的变化，解析文本并提取拓扑结构，评估推理相关性能。
| 指标 | 含义 |
|------|------|
| 准确率 | 越高越好 |
| 延迟 | 越低越好 |
| 分布外（OOD）差距 | 越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 多智能体基线 | 多智能体系统 | 可缓解解析失败，但延迟过高 |
| SFT模型 | 监督微调基线 | 原基准模型，对分布变化敏感，OOD差距较大 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主基准性能**
论文未提供对应表号，仅在正文提及：GRAIN比多智能体基线准确率高16.45%，SFT模型的OOD差距从15.77%降至7.80%（即减半）。
💡 结论：GRAIN在主基准任务上的准确率优于多智能体基线，且结构泛化能力显著优于SFT模型。
**效率对比**
论文未提供FPS等具体效率指标，仅在正文提及：GRAIN比多智能体基线延迟约低24%。
💡 结论：GRAIN的推理效率显著优于多智能体基线。
**跨域/零样本迁移**
论文未明确报告跨域/零样本迁移的具体结果，仅在正文提及GRAIN大幅缩小了SFT模型的OOD差距。
💡 结论：GRAIN具有更强的结构泛化能力，可更好地应对分布外数据。
**鲁棒性/扰动测试**
论文未提供对应表号，仅在正文提及：GRAIN在超出训练分布的大型图上仍保持鲁棒性。
💡 结论：GRAIN能适配超出训练分布的大型图数据，鲁棒性良好。
**消融实验**
论文未报告消融实验的相关结果，故不展开。

4. 关键结论和发现
- 主要发现：1. GRAIN通过结构不变性奖励的单智能体强化学习框架，有效提升了LLM在真实世界图推理中对节点和任务形式变化的鲁棒性，避免过拟合表面模式；2. GRAIN在提升推理准确率的同时，显著降低了延迟；3. GRAIN大幅缩小了SFT模型的分布外差距，具备更优的结构泛化能力。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。
> ✅ **总结一句话**：GRAIN是通过结构不变性奖励优化的单智能体强化学习框架，在真实世界图推理任务中，既提升了对节点标识符、任务形式变化的鲁棒性，又在准确率和效率上优于多智能体基线，且结构泛化能力大幅超越SFT模型。

</details>

---

### 10. [Subgraph Filtering for Fair Graph Neural Networks](https://arxiv.org/abs/2608.26437v1)

**Authors**: Haohui Lu, jiyuan Tian, Fangyu Zhou, Shahadat Uddin  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.26437v1  

#### Abstract
Graph neural networks (GNNs) can exhibit unfair behavior even when sensitive attributes are excluded from node features, because graph topology and message passing propagate group-correlated signals under sensitive homophily. Existing fairness-aware GNN methods mainly constrain representations or pr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Subgraph Filtering for Fair Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
GNN即使节点特征中排除敏感属性，也会因图拓扑和消息传递在敏感同质性下传播组相关信号而表现出不公平行为；现有公平感知GNN方法主要在全局层面约束表征或预测分布，未明确控制聚合过程中传递有偏信息的局部结构通路。
🚀 提出的新方法与思路
**SF-GNN框架**：是轻量且与架构无关的公平GNN框架，通过如下步骤缓解结构偏置：1. 结合敏感同质性和结构传播放大器（包括中心节点参与和三元闭合）识别易产生偏置的边；2. 在每个消息传递步骤中引入随机边过滤，选择性降权或移除这些偏置边，同时保留剩余图结构；3. 训练时加入带预热调度的统计 parity 正则化器，稳定优化过程。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 偏置控制层级 | 从全局层面扩展到消息传递的局部结构通路层面，精准缓解结构偏置 |
| 框架特性 | 轻量且架构无关，适配性强 |
| 公平-精度权衡 | 在5个基准数据集上实现一致的公平性提升，同时保持竞争力的预测性能，相比近期公平感知GNN基线具有更好的公平-精度权衡 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 5个基准数据集 | 用于评估SF-GNN的公平性与预测性能 |
🎯 实验设置与评估指标
任务为评估公平感知图神经网络在结构偏置下的公平性与预测性能，具体指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 公平性指标 | 衡量模型公平性（论文未明确具体指标名称） |
| 预测性能指标 | 衡量模型准确性（论文未明确具体指标名称） |
| 效率指标 | 论文未报告 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 近期公平感知GNN基线 | 公平感知GNN方法 | 主要在全局层面约束表征或预测分布，未控制消息传递的局部结构通路 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（表号及具体内容）**
论文未提供具体表号、图号或定量数值，仅提到在5个基准数据集上，SF-GNN实现一致的公平性提升，同时保持竞争力的预测性能，相比近期公平感知GNN基线具有更好的公平-精度权衡。
**效率对比（FPS / 参数量）**
论文未报告
**跨域 / zero-shot 迁移**
论文未报告
**鲁棒性 / 扰动测试**
论文未报告
**消融实验**
论文未报告

4. 关键结论和发现
- 主要发现1：即使节点特征中排除敏感属性，GNN仍会因图拓扑和消息传递的敏感同质性传播组相关信号而产生不公平行为，结构偏置是公平性问题的重要来源。
- 主要发现2：SF-GNN通过识别并过滤消息传递过程中的偏置边缓解结构偏置的思路有效，能在保持预测性能的同时显著提升公平性，实现更好的公平-精度权衡。
- 方法局限性：论文未明确提及具体局限性。
- 未来工作：论文未明确提及。

> ✅ **总结一句话**：Subgraph Filtering for Fair Graph Neural Networks（SF-GNN）是轻量且架构无关的公平GNN框架，通过识别并过滤消息传递过程中的偏置边缓解结构偏置，在5个基准数据集上实现了优于近期公平感知GNN基线的公平-精度权衡。

</details>

---

### 11. [C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning](https://arxiv.org/abs/2608.26870v1)

**Authors**: Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem, R\'emy Cazabet, Pierre Cl\'eau  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2608.26870v1  

#### Abstract
Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such sign...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：现有弱信号检测方法无法捕捉弱信号表现所依托的语义与关系结合结构。
现有方法缺陷：
1. 基于关键词频率的方法，无法捕捉弱信号的语义结构；
2. 基于主题建模的方法，无法捕捉弱信号的关系结构；
3. 基于无类型图拓扑的方法，无法捕捉弱信号的语义与关系结合结构。

🚀 提出的新方法与思路
**C-Unseen框架**：用于动态时间知识图（DTKG）中弱信号检测的自解释框架，包含两个核心模块：
**Rare Subgraphs Extractor**：通过LLM的链式思维（chain-of-thought）推理，识别每个TKG快照中与该快照主导叙事存在张力的子图。
**Weak Signal Alerter**：跟踪上述稀有子图在连续时间步的持续性，从而分离出真正的弱信号。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 弱信号检测效果 | 优于基于关键词频率、主题建模、无类型图拓扑的三类基线方法 |
| 结构捕捉能力 | 可捕获弱信号表现的语义与关系结合结构，弥补了现有方法的缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：在动态时间知识图（DTKG）上进行弱信号检测。
论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 关键词基弱信号检测方法 | 关键词基 | 基于关键词频率进行弱信号检测 |
| 主题基弱信号检测方法 | 主题基 | 基于主题建模进行弱信号检测 |
| 图拓扑基弱信号检测方法 | 图拓扑基 | 基于无类型图拓扑进行弱信号检测 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：C-Unseen框架在DTKG弱信号检测任务上的性能优于基于关键词频率、主题建模、无类型图拓扑的三类基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：C-Unseen是一种基于LLM推理的自解释框架，可有效检测动态时间知识图中的弱信号，性能优于现有三类基线方法。

</details>

---

### 12. [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](https://arxiv.org/abs/2608.26836v1)

**Authors**: Haizhao Fan, Yuchi Xiong, Jize Wang, Xinping Guan, Xinyi Le  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.26836v1  

#### Abstract
Large Language Models (LLMs) have demonstrated remarkable proficiency in natural language understanding, yet they struggle with strict multi-step reasoning, frequently suffering from hallucinations and inconsistency. Existing solutions like Chain-of-Thought (CoT) lack rigorous verification mechanism...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers
1. 论文的主要贡献和创新点
✅ 解决的问题
LLMs具备自然语言理解能力，但在严格多步推理中存在不足，常出现幻觉与不一致问题；现有Chain-of-Thought（CoT）方法缺乏严格验证机制，标准Retrieval-Augmented Generation（RAG）方法往往遗漏逻辑任务固有的复杂结构依赖。

🚀 提出的新方法与思路
**Ontology-based LKG**：将逻辑规则和约束视为第一类拓扑节点，实现对从文本中提取的依赖关系的显式建模。
**Logic Router**：由拓扑感知的混合检索机制支持，动态调度任务到最优符号引擎。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理可验证性 | 具备可验证的推理路径，弥补CoT方法缺乏严格验证机制的缺陷 |
| 结构依赖建模 | 显式建模逻辑任务中固有的复杂结构依赖，避免标准RAG方法遗漏该类依赖 |
| 任务适配性 | 动态调度任务到最优符号引擎，提升逻辑推理任务的适配效率 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为逻辑推理任务，评估指标论文未报告
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体指标 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Chain-of-Thought（CoT） | 提示方法 | 现有常用的逻辑推理提示方案，缺乏严格验证机制 |
| Retrieval-Augmented Generation（RAG） | 检索增强生成方法 | 现有常用的检索增强方案，易遗漏逻辑任务的复杂结构依赖 |
| state-of-the-art prompting | 提示方法 | 当前最先进的逻辑推理提示方案 |
| RAG baseline | 检索增强生成方法 | 当前常用的RAG基线方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验相关具体内容论文未报告，因无具体表号、数值或无法定位来源。

4. 关键结论和发现
- 主要发现：1. SymbolLKG框架在逻辑推理基准上的性能显著优于当前最先进的提示方法和RAG基线；2. Ontology-based LKG与Logic Router的结合可实现更高的推理准确性与可验证性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SymbolLKG是一种结合Ontology-based Logical Knowledge Graph与Logic Router动态调度符号引擎的Neuro-Symbolic架构，可有效提升逻辑推理的性能与可验证性，解决现有LLMs在严格多步推理中的缺陷。

</details>

---

### 13. [Towards Expert Financial QA via Self-Improving RAG](https://arxiv.org/abs/2608.26706v1)

**Authors**: Junjie Xiong, Shawheen Ghezavat, Aum Hirpara  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.26706v1  

#### Abstract
Expert-level financial question answering requires both grounded verification to catch numeric hallucinations and audit trails for regulatory compliance, attributes that standard single-pass RAG systems lack. We take a step toward this goal with Self-Improving RAG, a framework that decomposes docume...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Towards Expert Financial QA via Self-Improving RAG
1. 论文的主要贡献和创新点
✅ 解决的问题
专家级金融问答需要两个关键属性：一是接地验证以捕捉数值幻觉，二是符合监管合规的审计轨迹；现有标准单轮RAG系统的缺陷包括：
1. 缺失接地验证能力，无法有效捕捉数值幻觉
2. 不具备可追溯的审计轨迹，无法满足金融场景的监管合规要求
🚀 提出的新方法与思路
**Self-Improving RAG**：该框架将文档问答任务分解为三个专门代理，分别为Retrieval、Reasoning和Judge，由协调器通过反馈驱动的自我校正机制实现协同；当Judge Agent对答案的评分低于动态阈值时，系统会触发重试，重试策略包括扩大检索范围、使用更严谨的提示词、放宽接受标准。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 专业适配性 | 适配专家级金融问答，满足监管场景的特殊需求 |
| 幻觉抑制 | 具备接地验证能力，可捕捉数值幻觉 |
| 可审计性 | 所有决策都被记录且带置信度分数，支持合规审计轨迹 |
| 改进机制 | Judge评分不足时触发针对性重试，提升答案质量 |
| 部署效率 | 固定检索管道搭配Judge驱动的重试即可达到强效果，无需动态路由 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| FinanceBench | SEC提交文件问答任务（SEC filing QA）的评估 |
🎯 实验设置与评估指标
任务为专家级金融问答（针对SEC提交文件的问答），评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| oracle-guided accuracy | 衡量模型答案与金标准答案的一致性，越高越好（↑） |
| Lazarus Rate | 模型通过针对性重试从初始错误答案中恢复的比例，越高越好（↑） |
⚔️ 基线方法对比
论文未报告基线方法的详细信息，仅提及标准单轮RAG为当前基准方案。
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告各实验对应的表号、图号、章节或页码，无法定位数值来源，因此仅报告论文明确提及的内容，其余实验项均为论文未报告：
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：固定检索管道搭配Judge驱动的重试策略，无需动态路由即可实现较强的实验效果；该框架通过针对性重试可恢复近4成的初始错误答案；所有决策带置信度分数的记录，满足金融监管场景的审计要求。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：Self-Improving RAG框架将文档问答拆解为三个专用代理并结合反馈自我校正，适配专家级金融QA任务，兼具幻觉抑制、可审计性与自我改进能力，符合监管场景要求。

</details>

---

### 14. [Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs](https://arxiv.org/abs/2608.26581v1)

**Authors**: Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng, Zhuang Ma, Anandharaju Durai Raju, Yao Wang, Xing Huang, Hei Yi Mak, Shadan Golestan, Hoang Le, Yonghan Dong, Wei Guo, Yaoyuan Wang  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 40.0  
**Type**: new  
**ArXiv ID**: 2608.26581v1  

#### Abstract
Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs). Recent hardware support for low-precision formats, ranging from MXFP8 to ultra-low-bit formats such as MXFP4 and HiF4, has accelerated research into efficient...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
低比特量化可降低多模态大语言模型（MLLMs）的计算与内存需求，但现有MXFP4、HiF4等极低比特量化方案在视频生成、推理等代表性MLLMs任务上会导致显著性能下降；研究发现激活量化是性能损失的主要来源，其影响远大于权重量化，这一核心瓶颈尚未被充分解决。

🚀 提出的新方法与思路
**Residual Fallback Quantization (RFQ)**：这是一种轻量级激活重构框架，通过辅助量化残差路径补充超低比特激活表示，显式建模并补偿量化误差；该方法无需修改原始模型架构，计算开销可忽略，在保留超低比特计算效率优势的同时提升激活保真度，进而恢复MXFP4、HiF4量化下损失的性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 性能瓶颈定位 | 明确识别激活量化是超低比特MLLM量化性能损失的核心贡献源 |
| 架构兼容性 | 无需修改原始模型架构，适配各类MLLMs |
| 计算开销 | 仅引入可忽略的额外计算开销，保持高效部署特性 |
| 性能恢复效果 | 可显著恢复MXFP4、HiF4量化下的性能，大幅缩小与BF16基准的差距，覆盖生成、推理两类任务 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Wan2.2 | 用于视频生成任务的性能评估 |
| Qwen3-VL | 用于多模态推理任务的性能评估 |

🎯 实验设置与评估指标
任务为多模态大语言模型的量化性能评估，涵盖视频生成、推理两类任务；论文未明确报告具体评估指标的名称及含义。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| MXFP8 | 低比特量化基准 | 接近无损失的性能表现 |
| MXFP4 | 极低比特量化基准 | 计算效率高，但性能下降显著 |
| HiF4 | 极低比特量化基准 | 另一种高效量化方案，性能下降显著 |
| BF16 | 全精度基准方案 | 性能最优，但计算、内存开销大 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：① 激活量化是超低比特（MXFP4、HiF4）多模态大语言模型量化性能损失的核心来源，其贡献远高于权重量化；② 提出的Residual Fallback Quantization（RFQ）是一种轻量级高效的激活重构方案，可补偿超低比特激活量化误差；③ RFQ在Wan2.2、Qwen3-VL上，可显著恢复MXFP4、HiF4量化的性能，大幅缩小与BF16基准的差距。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本研究明确激活量化是超低比特多模态大语言模型量化的核心性能瓶颈，提出无需修改模型架构、开销可忽略的Residual Fallback Quantization（RFQ）框架，可有效恢复MXFP4、HiF4量化下的性能，缩小与全精度基准的差距。

</details>

---

### 15. [Simple Actors and Deep Critics for Scalable Reinforcement Learning](https://arxiv.org/abs/2608.26659v1)

**Authors**: Guhyeon Kang, Jaehwi Lee, Minhae Kwon  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.26659v1  

#### Abstract
Recent progress in offline reinforcement learning (RL) has been driven by expressive generative actors such as diffusion and flow-matching policies, which capture multimodal behavior in offline datasets. However, these actors require multiple denoising or integration steps per action and thus incur ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Simple Actors and Deep Critics for Scalable Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有离线强化学习中的生成式actor（如diffusion、flow-matching策略）需多步去噪或积分生成动作，导致每步决策的部署开销大；传统思路倾向于将模型容量分配给actor（因actor每步运行，critic仅用于训练且部署时会被丢弃），但深MLP critic在离线RL中会出现优化失效、自举噪声放大、值范围漂移三种失败模式，因此实践中critic通常保持较浅，限制了其性能与灵活性。
🚀 提出的新方法与思路：
**Light Actor, deep Critic (LAC)**：针对上述痛点，提出将模型容量优先分配给仅训练用、部署时丢弃的critic；为解决深MLP critic在离线RL中的训练不稳定性，针对三种失败模式分别采用**Residual MLP backbone**解决优化问题、**n-step bootstrap targets**缓解自举噪声放大问题、**Categorical cross-entropy loss**处理值范围漂移问题，结合轻量确定性actor构成LAC方法。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 离线RL性能 | 在OGBench上匹配当前最强的diffusion、flow-matching基线方法 |
| 部署推理效率 | 推理延迟较生成式actor基线低达4倍，且无需蒸馏即可媲美one-step distilled policies的延迟表现 |
| 方法通用性 | 提出的critic改进配方可跨actor参数化迁移 |

2. 核心实验方法和设置
📚 使用的数据集：
| 数据集 | 用途 |
| ---- | ---- |
| OGBench | 验证LAC方法的离线RL性能与部署效率 |
🎯 实验设置与评估指标：任务为离线强化学习任务；评估指标包括离线RL任务性能、推理延迟。
| 指标 | 含义 | 方向 |
| ---- | ---- | ---- |
| 离线RL性能 | 基准任务的决策表现 | ↑ 越高越好 |
| 推理延迟 | 部署时单步动作生成的耗时 | ↓ 越低越好 |
⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Diffusion/flow-matching policies | 生成式actor基线 | 离线RL性能强，但部署延迟高 |
| One-step distilled policies | 蒸馏策略基线 | 性能匹配生成式actor，但延迟高于LAC |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（OGBench离线RL任务）**
论文明确报告：LAC在OGBench上的离线RL性能可匹配最强的diffusion、flow-matching基线方法；其推理延迟较上述强生成式actor基线低达4倍，延迟表现媲美无需蒸馏的one-step distilled policies方法。
💡 结论：LAC在OGBench上兼顾了与当前最强生成式actor基线相当的离线RL性能，以及大幅提升的部署推理效率。
**跨域/zero-shot迁移**：论文报告其critic改进配方可跨actor参数化迁移，结果已验证，具体指标数值未报告。
**效率对比（FPS/参数量）**：仅明确报告推理延迟低达4倍，FPS、参数量等其余效率指标未报告。
**鲁棒性/扰动测试**：论文未报告。
**消融实验**：论文未报告。

4. 关键结论和发现
- 主要发现：
1. 离线RL中，将模型容量优先分配给仅训练使用、部署阶段丢弃的critic，而非部署时运行的actor，是合理的容量分配策略，可在保证性能的前提下显著提升部署效率。
2. 深MLP critic在离线RL中会出现优化失效、自举噪声放大、值范围漂移三种失败模式，对应可采用残差MLP backbone、n-step自举目标、分类交叉熵损失分别解决。
3. 提出的LAC方法在OGBench上实现了性能与强生成式actor基线相当，推理延迟低4倍，且critic配方具备跨actor参数化的通用性。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文针对离线RL中生成式actor部署延迟高的痛点，提出容量分配给深MLP critic的LAC方法，通过三种对应改进解决深critic的训练不稳定问题，在OGBench上实现性能与强基线相当且推理效率大幅提升。

</details>

---

### 16. [Inductive Correlation Clustering with Graph Neural Networks](https://arxiv.org/abs/2608.27153v1)

**Authors**: Francesco Paolo Nerini, Francesco Bonchi, Arijit Khan, Andr\'e Panisson  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.27153v1  

#### Abstract
Correlation Clustering (CC) is a natural formulation of clustering in combinatorial optimization, which uses a graph representation of the input and does not require a pre-specified number of clusters. Given $n$ objects and a pairwise similarity function, the goal is to cluster the objects so that s...

---

### 17. [TelecomGPT-R1: A Unified Open-Source Reasoner for the Telecom Stack](https://arxiv.org/abs/2608.26126v1)

**Authors**: Bohao Wang, Chenwei Wu, Haoyu Li, Hang Zou, Yu Tian, Lina Bariah, Li Wei, Chongwen Huang, Yongliang Shen, Zhaoyang Zhang, Merouane Debbah  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.26126v1  

#### Abstract
Telecommunications is a high-leverage domain for large language model (LLM)-based reasoning because routine engineering workflows require joint grounding in normative specifications, operational telemetry, vendor-specific fault evidence, and exact RF/network calculations. However, current LLM integr...

---

### 18. [Information-Guided Frontier Decoding: Contextual Utility-Driven Commitment in dMLLMs](https://arxiv.org/abs/2608.26641v1)

**Authors**: Xingyou Fang, Jingxing Zhong, Xiaosong Yuan, Xiaofeng Zhang  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.26641v1  

#### Abstract
Decoding quality in diffusion multimodal language models (dMLLMs) depends heavily on the order in which masked tokens are committed. Existing confidence-based strategies prioritize locally easy tokens, but confidence does not necessarily reflect contextual usefulness. As a result, structurally easy ...

---

### 19. [TwinKV: A Composable Repair Pass for KV Cache Eviction via Pairwise Key Redundancy](https://arxiv.org/abs/2608.27128v1)

**Authors**: Hong Chen, Yudong Zeng, Yongwei Huang, Zuhao Ouyang, Junyan Zhang, Xuming Hu  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.27128v1  

#### Abstract
Long-context inference is bottlenecked by the memory footprint of the key-value (KV) cache, especially for small models under tight resource budgets. Existing KV cache eviction methods score tokens using the model's attention distribution or, in attention-free variants, each key's distance from a gl...

---

### 20. [Boosting LLM Exploration via Weak-Model Guidance in RLVR](https://arxiv.org/abs/2608.27420v1)

**Authors**: Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.27420v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for large $k$. While existing methods mitigate this entropy collapse through algorithmic regularizations,...

---

### 21. [The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts](https://arxiv.org/abs/2608.26235v1)

**Authors**: Sachin Gopal Wani, Ajay Dholakia, David Ellison  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.26235v1  

#### Abstract
Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost? We introduce the Token Economy Score (TES), a marginal benchmarking metric that measures the accuracy gain of a reasoning model over a non-rea...

---

### 22. [GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory](https://arxiv.org/abs/2608.26983v1)

**Authors**: Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.26983v1  

#### Abstract
Organizing long-term memory for multimodal agents remains challenging because existing methods either suffer from expensive question-agnostic offline summaries or naive embedding similarity matching that introduces incomplete and redundant context. To address these issues, we propose GraphMemix, a c...

---

### 23. [Mitigating Strong-Modality Collapse in Multimodal Learning via Inverted Asymmetric Fusion](https://arxiv.org/abs/2608.26879v1)

**Authors**: Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.26879v1  

#### Abstract
Fusing multiple modalities is expected to improve model performance. However, on the MultiHuSE dataset, early, late, and symmetric attention fusion often fail to outperform the best unimodal baseline (text). Pathway isolation of a symmetric attention fusion model reveals that the text-pathway accura...

---

### 24. [Disentangling Optimization Scale from Preference Scale in DPO](https://arxiv.org/abs/2608.27032v1)

**Authors**: Ivan Kruzhilov  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.27032v1  

#### Abstract
Direct Preference Optimization (DPO) is a widely used objective for aligning language models from preference data, with the coefficient $\beta$ commonly interpreted as controlling the KL constraint to a reference policy. We show that $\beta$ entangles two distinct roles: it governs the effective inv...

---

### 25. [Beyond Edge Cuts: Activity-Weighted Multicast Hypergraph Mapping for Spiking Neural Networks on Mesh NoCs](https://arxiv.org/abs/2608.26223v1)

**Authors**: Amirreza Khorasanian  
**Category**: cs.AR  
**Published**: 2026-08-28  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.26223v1  

#### Abstract
Mapping spiking neural networks (SNNs) onto neuromorphic many-core platforms is often formulated with graph partitioning and pairwise placement costs. That abstraction is convenient, but it does not match the physical communication event: one spike from a source neuron is delivered to a set of posts...

---

### 26. [EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction](https://arxiv.org/abs/2608.26107v1)

**Authors**: Yu Fu, Yongqi Kang, Yong Zhao, Rongfang Bie  
**Category**: cs.AI  
**Published**: 2026-08-28  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.26107v1  

#### Abstract
Predicting students' academic risk in online education is crucial for enabling timely interventions that can improve retention and learning outcomes. However, existing models often suffer from limited early detection capability and insufficient interpretability, leading to a "black-box" trust crisis...

---

### 27. [RuleWeaver: Benchmarking Rule-Centered Scenario Reasoning for Large Language Models](https://arxiv.org/abs/2608.26832v1)

**Authors**: Bohan Yu, Shi-Yang Li, Pengfei Cao, Jun Zhao, Kang Liu  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.26832v1  

#### Abstract
Large language models (LLMs) are increasingly applied to specialized domains, where effective use of domain expertise often requires reasoning over complex rules in concrete scenarios. However, existing benchmarks only partially evaluate this capability, as they either focus on output-level instruct...

---

### 28. [SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models](https://arxiv.org/abs/2608.27265v1)

**Authors**: Yi Ding, Lijun Huang, Menglin Yang  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.27265v1  

#### Abstract
Latent chain-of-thought models move intermediate reasoning from emitted text into continuous states, improving compactness but hiding the causal object. We introduce SCIT, the Suffix Cache Interchange Test, a causal protocol that constructs exact source-recipient counterfactuals, patches declared ca...

---

### 29. [Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers](https://arxiv.org/abs/2608.27343v1)

**Authors**: Ke Shu, Kira Hinderks, Eetu M\"akel\"a, Mikko Tolonen  
**Category**: cs.CL  
**Published**: 2026-08-28  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.27343v1  

#### Abstract
This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottis...

---

### 30. [Active Curriculum Refinement for Reinforcement Learning](https://arxiv.org/abs/2608.26469v1)

**Authors**: Zhenya Liu, Yuxin Chen  
**Category**: cs.LG  
**Published**: 2026-08-28  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.26469v1  

#### Abstract
In many reinforcement learning (RL) domains, environments are connected by prerequisite relations, such as difficulty-increasing edits or parameter increments, which induce a directed acyclic curriculum graph (DAG). Although this structure is often exploited only implicitly, explicitly modeling it c...

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
