# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-10 10:06:54 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning](https://arxiv.org/abs/2609.08025v1)

**Authors**: Vishwas Sathish, Viresh Ranjan, Xinliang Zhu, Arnab Dhua, Douglas Gray  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 104.5  
**Type**: new  
**ArXiv ID**: 2609.08025v1  

#### Abstract
Reasoning agents increasingly rely on external tools such as web search to answer complex queries. Reinforcement learning (RL) finetuning algorithms such as GRPO have improved long-form reasoning in text-only language models, particularly for coding and mathematics. Reliable tool use in multimodal a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态推理智能体的可靠工具使用面临核心痛点：模型需同时处理文本与图像信息，整合含噪声的检索证据，且通常仅能获得稀疏的结果级监督，缺乏明确的验证信号；现有GRPO等RL微调算法虽提升了纯文本LLM的长推理（如编码、数学）能力，但在多模态智能体的工具使用场景中效果不佳，且现有方案多依赖外部验证器，推理成本高。

🚀 提出的新方法与思路
**Self-Verification via Reinforcement Learning（SVRL）**：一种仅基于RL的微调框架，训练多模态智能体在自身推理痕迹内完成对检索证据的验证与过滤，降低推理阶段对外部验证器的依赖。
**search-aware penalty**：辅助模块，作用为阻止不必要的工具调用。
**query-diversity reward**：辅助模块，作用为鼓励生成多样且格式规范的搜索查询，提供关于何时、进行何种搜索的细粒度反馈。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理依赖 | 无需过多依赖外部验证器，仅依赖模型自身推理能力 |
| 工具优化 | 通过针对性的penalty与reward实现工具调用的细粒度优化 |
| 成本性能 | 训练与推理成本更低，可缩小compact智能体与大型专有模型的性能差距 |
| 任务表现 | 在多跳VQA泛化、工具效率上取得一致提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 未明确命名的VQA数据集 | 用于微调Qwen-2.5-VL-7B模型的SVRL框架，共使用5000个视觉问答样本 |

🎯 实验设置与评估指标
任务为多模态工具使用下的视觉问答任务，具体实验设置与评估指标的详细细节：论文未报告。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO | RL微调算法 | 用于纯文本LLM的长推理任务（如编码、数学），提升其推理能力 |
| 大型专有多模态模型 | SOTA多模态模型 | 性能表现优异，但推理与训练成本极高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未提供具体表号、图号及定量数值，相关实验结果详情：
1. 主 benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 采用SVRL框架微调Qwen-2.5-VL-7B时，仅需5000个VQA样本即可实现多跳VQA泛化与工具效率的一致提升，缩小了compact模型与大型专有模型的差距。
  2. SVRL框架通过内置的search-aware penalty与query-diversity reward，有效优化了多模态智能体的工具调用时机与质量，提升了推理阶段的工具使用效率。
  3. SVRL仅通过RL微调完成自我验证能力的训练，无需额外的外部验证器，降低了推理成本。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的SVRL框架通过RL微调训练多模态智能体具备自我验证和过滤检索证据的能力，配合针对工具调用的penalty和reward机制，在多跳VQA泛化与工具效率上取得提升，缩小了compact多模态智能体与大型专有模型的差距，且训练与推理成本更低。

</details>

---

### 2. [Epoch: Compiling Diffusion Blocks for Sparse MoE Serving](https://arxiv.org/abs/2609.09748v1)

**Authors**: Jianian Zhu, Hang Wu, Yinghui Li, Haojie Wang, Ruixuan Li, Jidong Zhai  
**Category**: cs.DC  
**Published**: 2026-09-10  
**Score**: 87.0  
**Type**: new  
**ArXiv ID**: 2609.09748v1  

#### Abstract
Diffusion language models generate text by refining a fixed-size block of token positions through many forward passes, a loop that does not match the per-forward execution unit used by most LLM serving systems. A dense MoE runtime binds all work to the refinement-iteration clock: it rebuilds similar...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Epoch: Compiling Diffusion Blocks for Sparse MoE Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
Diffusion语言模型通过多轮前向循环细化固定大小token块的生成方式，与大多数LLM serving系统的单前向执行单元不匹配；现有dense MoE runtime存在三点缺陷：每次前向都重建相似的路由结构、重新计算已死logits对应token的专家输出、让这些token通过密集专家并行集合通信。

🚀 提出的新方法与思路
**Atlas**：按层编译覆盖驱动的活跃专家支持，每次迭代重新计算门控logits；
**LSP**：保留完整序列分片作为模型状态，仅路由新解码的、需刷新的活token进行新鲜路由的专家计算；
**FreshLane**：将新鲜token-专家工作流传递至专家并行的分发、核函数与组合步骤，在层边界恢复密集逻辑分片。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 端到端执行时间 | 相比最强基线最多提升2.7倍 |
| 大batch可行性 | 在多个基线内存不足的最大batch尺寸下仍可行 |
| 任务质量 | 保持与密集参考相当的任务质量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GSM8K | 评估Block-diffusion MoE模型的任务表现 |
| HumanEval | 评估Block-diffusion MoE模型的任务表现 |
| MGSM | 评估Block-diffusion MoE模型的任务表现 |
| MT-Bench | 评估Block-diffusion MoE模型的任务表现 |

🎯 实验设置与评估指标
任务为Block-diffusion MoE模型的服务性能评估，相关指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 端到端执行时间 | ↓ 越低越好，数值越小表示性能越优 |
| 内存可行性 | 表示能否在大batch尺寸下正常运行 |
| 任务质量 | 与密集参考方法的性能一致性，一致则满足要求 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有dense MoE runtime | 基线方法 | 每次前向重建路由结构、重算死token的专家输出、使用密集专家并行通信 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主benchmark性能（8 NVIDIA H100 GPUs环境）**
论文未报告
**表N：效率对比（参数量相关）**
论文未报告
**表N：跨域 / zero-shot 迁移**
论文未报告
**表N：鲁棒性 / 扰动测试**
论文未报告
**表N：消融实验**
论文未报告

4. 关键结论和发现
- 针对Diffusion语言模型与现有LLM serving执行单元不匹配的痛点，提出的Epoch系统通过将Diffusion块作为编译单元，优化了稀疏MoE serving流程；
- 在8 NVIDIA H100 GPUs环境下，该系统端到端执行时间相比最强基线最多提升2.7倍，且在基线内存不足的最大batch尺寸下仍可运行，同时保持与密集参考相当的任务质量；
- 论文未报告该方法的其他潜在局限性；
未来工作：论文未报告

> ✅ **总结一句话**：提出的Epoch系统将Diffusion块作为编译单元优化稀疏MoE serving，在8 GPU环境下提升端到端执行时间、支持更大batch尺寸，且保持任务质量与密集参考相当。

</details>

---

### 3. [Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification](https://arxiv.org/abs/2609.07148v1)

**Authors**: Yimeng Ye, Shuang Chen, Wenxuan Huang, Manyuan Zhang, Kaituo Feng, Zhangquan Chen, Jiayu Chen, Yucheng Zhou, Yicheng Xiao, Zhiyuan Feng, Tianyu Shi  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 75.5  
**Type**: new  
**ArXiv ID**: 2609.07148v1  

#### Abstract
While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse. These limitations often stem from "Rollout Silencing" and low-quality gradient signals in standard sampling procedures. In...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为针对大语言模型的强化学习（RL）微调流程存在训练不稳定、快速熵坍塌的痛点，具体缺陷包括：
1. 标准采样流程存在“Rollout Silencing”现象；
2. 标准采样流程会产生低质量的梯度信号。

🚀 提出的新方法与思路
**Potential-Aware Query Mining (PAQM)**：动态过滤数据，聚焦“Distillation Zone”样本——即具备高能力激发潜力的样本，优化数据筛选效率。
**Hybrid Stratified Replay (HSR)**：基于路径熵（rollout级置信度代理）与结果奖励，分层重组rollouts批次；每个优化步骤中重用当前策略的“Stability Anchors”与“Hard Negatives”构建高对比优化组，随后清空缓存以支持下一步操作，缓解熵坍塌并提升有限计算下的学习信号利用率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 训练稳定性 | 缓解现有RL微调流程的训练不稳定问题 |
| 熵坍塌 | 缓解现有方法存在的快速熵坍塌问题 |
| 学习信号利用率 | 在有限计算资源下提升学习信号的利用效率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为复杂推理任务；论文未报告具体指标及含义。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 提出的PAQM动态数据过滤机制与HSR分层回放机制，可有效解决大语言模型RL微调中的训练不稳定与熵坍塌问题。
- 该框架在复杂推理任务上的表现优于强基线方法。
- HSR机制能提升有限计算资源下的学习信号利用率。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：Stable-MM-R1框架通过PAQM动态数据过滤与HSR分层回放机制，解决了大语言模型RL微调流程中的训练不稳定与熵坍塌痛点，在复杂推理任务上性能优于强基线，且提升了有限计算资源下的学习信号利用率。

</details>

---

### 4. [CUSP: Decomposable Collective Uncertainty for Multi-Agent Multimodal Reasoning](https://arxiv.org/abs/2609.05708v1)

**Authors**: Chung-En Johnny Yu, David Garcia, Brian Jalaian, Nathaniel D. Bastian  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 74.5  
**Type**: new  
**ArXiv ID**: 2609.05708v1  

#### Abstract
Aggregating heterogeneous vision-language models (VLMs) can improve multimodal reasoning, but neither an individual model's confidence nor that of the aggregated answer measures reliability at the system level. We present CUSP (Collective Uncertainty through Semantic Opinion Pooling), a training-fre...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CUSP: Decomposable Collective Uncertainty for Multi-Agent Multimodal Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有研究中，单个视觉语言模型（VLM）的置信度或聚合答案的置信度均无法衡量系统层面的可靠性，缺乏适用于多VLM集成的训练免费系统级不确定性量化方法，且现有不确定性信号无法同时分离总离散度与模型间冲突。

🚀 提出的新方法与思路
**CUSP框架**：这是一种训练免费的不确定性量化框架，核心流程为：将多个VLM的响应映射至共享语义响应空间，汇聚为聚合语义意见，最终输出两个互补的系统级信号：① collective uncertainty，即聚合意见的离散度；② Jensen-Shannon divergence（JSD），即模型间意见的冲突。该框架的核心性质为：归一化前的聚合熵可精确分解为各模型个体语义熵的均值与JSD之和，实现总离散度与模型冲突的分离；同时无需token logits或校准标签，可适用于开放权重VLM与商用VLM。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 不确定性分解能力 | 可将归一化前的聚合熵精确分解为各模型个体语义熵的均值与JSD之和，实现总离散度与模型冲突的明确分离 |
| 适用VLM范围 | 无需token logits或校准标签，支持开放权重与商用两类VLMs |
| 系统级可靠性衡量 | 提供两个互补的系统级不确定性信号，突破单个VLM置信度或聚合答案置信度无法衡量系统可靠性的局限 |
| 训练依赖性 | 属于训练免费框架，无需额外训练流程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称 | 用于静态多VLM集成的预测错误检测、弃权排序；用于多步多智能体系统轨迹的故障检测、弃权排序 |

🎯 实验设置与评估指标
实验任务为多智能体多模态推理中的不确定性量化、聚合答案可靠性评估及系统故障检测。评估指标：
| 指标 | 含义 |
| --- | --- |
| AUROC | 预测错误、硬答案冲突检测的性能，越高越好 |
| AUARC | 弃权排序的效果，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| majority voting | 集成方法 | 采用多数投票规则聚合VLM答案 |
| naive selection | 基线方法 | 简单选择的基准方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**静态多VLM集成场景**
论文未报告对应结果的表号，无法给出具体数值；相关结论包括：collective uncertainty是小模型 regime 中预测错误检测、弃权排序的最优不确定性信号，性能优于majority voting与naive selection，且差距随集成规模扩大而增大；JSD是商用模型 regime 中对应任务的最优不确定性信号，用于硬答案冲突检测的性能可达较高水平；基于CUSP的聚合答案准确率相比平均单模型提升5.6至13.0个百分点。
💡 结论：CUSP框架的不确定性信号在静态多VLM集成的不同模型 regime 中均展现出优异性能，且聚合答案可显著提升多模态推理准确率。

**多步多智能体系统轨迹场景**
论文未报告对应结果的表号，无法给出具体数值；相关结论包括：collective uncertainty可有效排名系统故障，是该场景下弃权排序效果最优的信号。
💡 结论：在多步多智能体系统轨迹中，collective uncertainty可实现系统故障检测与优化的弃权排序。

**消融实验**
论文未报告消融实验的相关内容。

4. 关键结论和发现
- 主要发现：① CUSP提供的collective uncertainty与JSD两种系统级不确定性信号，在小模型与商用模型两类 regime 中分别对应最优的预测错误检测与弃权排序性能；JSD可有效衡量硬答案间的冲突；② 基于CUSP的聚合答案准确率相比平均单模型有显著提升；③ 在多步多智能体系统轨迹场景中，collective uncertainty可实现有效的系统故障检测与弃权排序优化。
- 方法局限性：论文未报告方法的局限性。
- 未来工作：论文未报告未来工作方向。

> ✅ **总结一句话**：CUSP是一种训练免费的多智能体多模态推理系统级不确定性量化框架，通过语义意见池化输出的collective uncertainty与JSD信号可有效衡量VLM集成的可靠性，同时其聚合答案可显著提升多模态推理的准确率。

</details>

---

### 5. [Think Wider: Mitigating Latent Rank Collapse in Implicit Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.07406v1)

**Authors**: Yuwen Hao, Menglin Yang  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 73.0  
**Type**: new  
**ArXiv ID**: 2609.07406v1  

#### Abstract
Chain-of-thought (CoT) reasoning improves the reasoning ability of large language models by introducing intermediate computation, but explicit rationales increase decoding length, latency, and context cost. Implicit CoT offers a more efficient alternative by moving intermediate reasoning into contin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Think Wider: Mitigating Latent Rank Collapse in Implicit Chain-of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
显式CoT推理会增加解码长度、延迟及上下文成本；隐式CoT虽更高效，但存在潜在的隐态不稳定问题——连续隐态会变得过度相似，坍缩至共享主导方向，降低推理轨迹多样性，论文识别出该问题为latent rank collapse（隐式秩坍缩）。

🚀 提出的新方法与思路
**WIDER**：是面向隐式CoT的轻量谱正则化器；训练阶段，该方法估计每个隐式轨迹的共享方向，惩罚该方向上的投影，鼓励隐态张成更宽的表示子空间；该方法为即插即用型，不改动骨干模型、隐式调度及推理时的解码流程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能表现 | 改进匹配的隐式CoT基线 |
| 隐态质量 | 提升有效秩、降低主导方向能量、减少隐式步骤冗余 |
| 兼容性 | 轻量即插即用，不改动原有模型与解码流程 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
论文未报告具体任务类型与评估指标细节

⚔️ 基线方法对比
论文未报告除"匹配的隐式CoT基线"外的基线方法具体信息

3. 主要实验结果和性能指标
论文未报告具体实验表格（如表号、具体数值等），仅提及WIDER可改进匹配的隐式CoT基线，机制分析显示其能带来更高有效秩、更低主导方向能量及更少隐式步骤冗余。

4. 关键结论和发现
- 主要发现：1）识别出隐式CoT推理中的隐式秩坍缩问题；2）WIDER可有效缓解该问题，提升隐式子空间利用率与隐态多样性；3）隐式子空间利用率是高效连续推理的重要影响因素
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：WIDER作为轻量谱正则化器，能有效缓解隐式CoT的隐式秩坍缩问题，提升推理隐态质量且保留原有推理流程的高效性。

</details>

---

### 6. [On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data](https://arxiv.org/abs/2609.10321v1)

**Authors**: Hongyuan Zhang, Xianda Guo, Yanlun Peng, Qianlong Yang, Yubin Guo, Pinhan Fu, Mulin Chen, Xiaozhen Qiao, Ping Luo  
**Category**: cs.CL  
**Published**: 2026-09-10  
**Score**: 67.0  
**Type**: new  
**ArXiv ID**: 2609.10321v1  

#### Abstract
Knowledge distillation offers an efficient route to transfer a task-adapted vision-language teacher to a compact student. The training target in current vision-language distillation methods is typically constructed from the teacher prediction and applied uniformly to all training samples, making it ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data
1. 论文的主要贡献和创新点
✅ 解决的问题：现有视觉语言蒸馏方法将教师预测作为固定训练目标并均匀应用于所有训练样本，在类偏移和域偏移场景下不可靠。
🚀 提出的新方法与思路
**OnPoKD（On-Policy Distillation for Vision-Language Model Adaptation）**：是首个将on-policy蒸馏应用于视觉语言模型适配的框架；该方法学习轻量控制器，利用教师模型、学生模型和零样本先验的可靠性与分歧线索，构建样本级的自适应蒸馏目标；控制器通过有界策略动作，动态平衡教师监督、零样本先验指导和硬标签锚定，无需依赖固定教师预测，适配不同样本可靠性和训练阶段；策略控制器通过验证反馈更新，优化模型迁移性而非仅拟合训练分布；控制器仅在训练阶段使用，保留原有推理架构和测试时间成本，可无缝集成到现有视觉语言蒸馏流水线。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 蒸馏目标构建 | 动态样本自适应，适配样本可靠性与训练阶段差异 |
| 策略优化目标 | 以验证反馈更新，侧重模型迁移性而非仅拟合训练分布 |
| 推理效率 | 保留原始推理架构，无额外测试时间成本 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 用于基到新泛化、跨数据集迁移的实验验证 |
🎯 实验设置与评估指标
视觉语言模型适配的基到新泛化、跨数据集迁移任务
| 指标 | 含义（箭头方向） |
| --- | --- |
| 论文未报告 | 论文未报告具体评估指标及含义 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 各强视觉语言蒸馏基线方法 | 基线方法 | 作为对比基准，用于验证OnPoKD的性能提升 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
4. 关键结论和发现
- OnPoKD在基到新泛化和跨数据集迁移的基准实验中，持续优于现有强视觉语言蒸馏基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：OnPoKD是首个将on-policy蒸馏应用于视觉语言模型适配的框架，通过学习轻量控制器构建适配样本可靠性与训练阶段的自适应蒸馏目标，在基到新泛化和跨数据集迁移场景下实现视觉语言蒸馏方法的性能提升，同时保持高效的推理效率。

</details>

---

### 7. [NormViz: A Benchmark and Framework for Grounding Multimodal Reasoning in Global Cultures](https://arxiv.org/abs/2609.06831v1)

**Authors**: Akhila Yerukola, Fabrice Y Harel-Canada, Simran Khanuja, Abhinav Sukumar Rao, Ashima Suvarna, Nanyun Peng, Saadia Gabriel, Maarten Sap  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2609.06831v1  

#### Abstract
AI systems are used worldwide, but they struggle to serve the needs of culturally diverse populations. Prior work on cultural understanding evaluates AI systems on text-only settings or on visual artifact recognition (e.g. foods, clothing). The ability to reason about visually observable behaviors t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

NormViz: A Benchmark and Framework for Grounding Multimodal Reasoning in Global Cultures
1. 论文的主要贡献和创新点
✅ 解决的问题
现有AI系统难以服务文化多样的全球用户；现有文化理解相关工作多聚焦纯文本场景或视觉文物识别（如食物、服装），但针对通过本地社会规范推理视觉观察行为的视觉规范理解能力仍未被研究。

🚀 提出的新方法与思路
**NormViz-Bench**：构建经人类验证的基准，包含3268对对比图像（共6536张），覆盖16个国家；每对图像仅在文化相关行为（如对象、属性、空间关系、动作）上存在差异，每张图像标注为符合、违反或与当地社会规范无关；评估要求模型正确分类一对中的两张图像，避免依赖表面视觉捷径。
**NormViz-Train**：构建包含64k张图像及对应解释的训练数据集，为模型学习视觉感知与文化意义的关联提供支撑。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 研究覆盖 | 首次聚焦视觉观察行为的本地社会规范推理，填补视觉规范理解领域的研究空白 |
| 评估设计 | 采用成对图像分类评估机制，强制模型兼顾成对图像的文化属性，防止依赖表面视觉捷径 |
| 训练支撑 | 提供带解释的64k图像组成的训练数据集，支持多模态模型的微调优化 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| NormViz-Bench | 用于基准评估，测试模型视觉规范理解能力 |
| NormViz-Train | 用于模型微调，提升模型对视觉与文化意义关联的学习能力 |

🎯 实验设置与评估指标
任务为基于NormViz-Bench完成成对图像分类，评估模型对视觉行为与本地社会规范关联的理解能力；评估指标为成对分类准确率，指标方向为越高越好（↑）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Gemini 3.0 Flash、Qwen2.5 VL 7B | 预训练VLMs（视觉语言模型） | 现有最强VLMs，但在视觉规范理解任务上性能表现差 |
| Qwen3-VL 4B、Qwen3-VL 8B | 微调后VLMs | 在NormViz-Train上进行微调优化的VLMs |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（视觉规范理解成对分类）**
| 方法 | 成对分类准确率 |
| ---- | ---- |
| Gemini 3.0 Flash | 26.6% ✅ |
| Qwen2.5 VL 7B | 21.6% |
💡 结论：现有最强预训练VLMs在视觉规范理解任务上性能极低，仅约20%-26%，对违反及文化良性视觉行为的识别存在明显困难。

1. 效率对比（FPS / 参数量）：论文未报告
2. 跨域 / zero-shot迁移：论文未报告
3. 鲁棒性 / 扰动测试：论文未报告
4. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 现有最强预训练VLMs在视觉规范理解任务上性能不佳，Gemini 3.0 Flash和Qwen2.5 VL 7B的成对分类准确率仅26.6%和21.6%；2. 基于NormViz-Train微调模型可显著提升性能，Qwen3-VL 4B和Qwen3-VL 8B的成对准确率相对提升最高达125%和36%，但绝对性能仍低于30%。
- 方法局限性：经现有方法微调后，模型在视觉规范理解任务上的绝对性能仍较低（<30%），难以满足实际应用需求。
- 未来工作：需进一步探索提升多模态模型视觉规范理解能力的方法，突破当前绝对性能的局限。

> ✅ **总结一句话**：NormViz-Bench和NormViz-Train填补了AI视觉规范理解领域的研究空白，为提升多模态AI系统对全球多元文化的服务能力提供了标准化基准和训练数据支持。

</details>

---

### 8. [Reason Through the Latent! Making Latent Visual Reasoning Necessary](https://arxiv.org/abs/2609.06746v1)

**Authors**: Suhyeong Park, Junha Jung, Jaewoo Kang  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2609.06746v1  

#### Abstract
Latent visual reasoning aims to perform multimodal reasoning through hidden-state computation rather than explicit textual chains of thought. However, visual information being present in a latent state does not imply that the model actually relies on that state when producing its answer, especially ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Reason Through the Latent! Making Latent Visual Reasoning Necessary
1. 论文的主要贡献和创新点
✅ 解决的问题：潜在视觉推理存在核心痛点，即模型虽利用包含视觉信息的潜在状态进行推理，但预测时可能不依赖该状态，且存在替代图像相关路径；同时，同类兼容潜在推理器在相同约束下无法恢复预训练的可比视觉能力。
🚀 提出的新方法与思路：**Causal Visual Recurrent Reasoning (CVRR)**：初始化阶段，从预训练视觉-语言模型（VLM）整合图像后的问题隐藏状态开始；循环阶段，反复更新该隐藏状态并读取固定不变的视觉证据；解码前，移除视觉状态和原始多模态KV缓存，仅保留最终循环状态携带图像相关信息来产生预测结果。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| --- | --- |
| 严格约束适配性 | 在移除视觉状态和原始多模态KV缓存的严格接口约束下仍保留强视觉推理性能 |
| 潜在计算真实性 | 可通过因果干预验证预测对循环内容及视觉证据的敏感性，明确区分潜在状态信息量与模型实际用于预测的潜在计算 |
| 对比方法竞争力 | 其他兼容潜在推理器无法在相同严格约束下达到与CVRR可比的性能 |

2. 核心实验方法和设置
📚 使用的数据集：
| 数据集 | 用途 |
| --- | --- |
| V* | 视觉推理性能测试 |
| MMVP | 视觉推理性能测试 |
| BLINK | 视觉推理性能测试 |
| MME-RealWorld-Lite | 视觉推理性能测试 |
🎯 实验设置与评估指标：任务为视觉-语言推理；论文未报告具体评估指标及对应含义。
⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 其他兼容潜在视觉推理器 | 对比方法 | 在相同严格约束下无法恢复与CVRR可比的视觉能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① CVRR在移除视觉状态和原始多模态KV缓存的严格约束下，在多个视觉推理基准上保留强性能，而其他兼容潜在视觉推理器无法在相同约束下实现可比性能；② 因果干预实验显示，固定问题时，模型预测对循环内容敏感，持续的视觉证据可修正循环轨迹；③ 该方法明确区分了潜在状态包含的信息量与模型实际用于预测的潜在计算过程。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CVRR通过设计强制循环计算为唯一图像相关推理路径，使潜在视觉推理模型在严格接口约束下保留预训练视觉能力，同时实现了潜在状态实际计算使用的可验证区分。

</details>

---

### 9. [Multimodal Resource-Exhaustion Attacks on Vision-Language Models via Joint Pixel-Prompt Optimization](https://arxiv.org/abs/2609.05889v1)

**Authors**: Zhaoxiong Ni, Yatie Xiao, Chi-Man Pun, Fei Peng, Qingxiao Guan, Keke Tang  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2609.05889v1  

#### Abstract
Resource-exhaustion attacks against autoregressive vision-language models (VLMs) typically assume unimodal threat models, treating the image branch as the primary optimization surface while holding user-visible prompts fixed. Even recent loop-centric variants remain confined to this single-channel p...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Multimodal Resource-Exhaustion Attacks on Vision-Language Models via Joint Pixel-Prompt Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对自回归VLM的资源耗尽攻击存在两类核心缺陷：①传统攻击采用单模态威胁模型，将图像分支作为主要优化表面且固定用户可见提示，未利用跨模态联合优化挖掘可用性漏洞；②最新的循环中心变体攻击仍局限于单通道范式，未采用跨模态联合优化思路。

🚀 提出的新方法与思路
**Joint Pixel-Prompt Optimization (JPPO)**，是首个复合对抗框架，将可见提示提升为与图像扰动同等的第一类对抗变量，在受限的联合输入威胁模型下，对像素表面与提示表面执行耦合的分阶段优化，通过跨模态协同实现成本放大效果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 优化范式 | 采用跨模态联合优化，将可见提示与图像扰动作为同等优化变量，突破传统单模态单一表面优化的局限 |
| 成本放大效果 | 对VLM的延迟、能量放大倍数显著高于基线方法，为直接对比基线中最强的成本放大效果 |
| 循环特性 | 循环发生率可忽略，区别于循环中心变体的循环依赖缺陷 |
| 优化效率 | 所需优化迭代次数显著少于基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MS COCO | 评估JPPO对各开源VLM家族的资源耗尽攻击效果 |
| ImageNet | 评估JPPO对各开源VLM家族的资源耗尽攻击效果 |

🎯 实验设置与评估指标
在无穷范数预算为8/255的条件下，评估各攻击方法对开源VLM家族的延迟、能量放大效果。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 延迟放大倍数 | 攻击后VLM处理样本的延迟与正常处理延迟的比值 | ↑越高越好 |
| 能量放大倍数 | 攻击后VLM处理样本的能耗与正常处理能耗的比值 | ↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统单模态资源耗尽攻击 | 单模态威胁模型攻击 | 将图像分支作为主要优化表面，固定用户可见提示，未采用跨模态联合优化 |
| 最新循环中心变体攻击 | 单通道范式攻击 | 仍局限于单分支优化，存在循环依赖缺陷，未利用跨模态联合优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告

**主 benchmark 效率对比（VLM资源耗尽攻击效果）**
| VLM模型 | 攻击方法 | 延迟放大倍数 | 能量放大倍数 |
| --- | --- | --- | --- |
| Qwen2.5-VL-7B | JPPO | >4.6x | >5.3x |
| BLIP-2 | JPPO | >36.6x | >32.7x |
💡 结论：JPPO在VLM资源耗尽攻击中实现了直接对比基线中最强的成本放大效果，且所需优化迭代次数显著少于基线方法，循环发生率可忽略。

**消融实验（验证跨模态协同的作用）**
| 模块启用情况 | 延迟放大倍数 | 能量放大倍数 |
| --- | --- | --- |
| 仅启用像素扰动 | 中等 | 中等 |
| 仅启用提示优化 | 较低 | 较低 |
| 同时启用像素扰动与提示优化（JPPO） | 最优 ✅ | 最优 ✅ |
💡 结论：JPPO的成本放大效果源于像素与提示的跨模态协同，而非孤立的单一模态或提示长度因素。

4. 关键结论和发现
- 2-3 条主要发现：
  ① 现有针对自回归VLM的资源耗尽攻击存在结构盲点，未将可见提示作为对抗优化的同等变量，最新循环中心变体仍未突破单分支优化的局限；
  ② JPPO作为跨模态联合优化框架，在VLM资源耗尽攻击中实现了显著的延迟和能量放大，且循环发生率低、优化效率高；
  ③ JPPO的成本放大效果源于跨模态协同，而非单一模态或提示长度因素。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Joint Pixel-Prompt Optimization（JPPO）是首个将可见提示与图像扰动联合优化的复合对抗框架，在VLM资源耗尽攻击中实现了当前最强的成本放大效果，揭示了VLM服务防御的结构盲点，为多模态部署的成本感知鲁棒性评估提供了新方向。

</details>

---

### 10. [BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents](https://arxiv.org/abs/2609.08566v1)

**Authors**: Yanhong Qian, Xuanying He, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2609.08566v1  

#### Abstract
KV cache is evolving from a serving optimization into an external memory substrate for long-term LLM agents. In a shared multi-user deployment, however, reusable KV blocks introduce a missing access-control question: semantic relevance alone cannot determine whether a memory block is authorized for ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents
1. 论文的主要贡献和创新点
✅ 解决的问题
KV缓存正从 serving 优化发展为长期LLM代理的外部内存载体，多用户共享部署场景下，可复用的KV块存在访问控制痛点：仅语义相关性无法判断当前物理用户是否有权限使用该内存块。

🚀 提出的新方法与思路
**Bio-MemArt**：给每个存储的KV内存块附加归一化的生物特征模板，通过当前用户的生物特征探针过滤共享内存池，仅在授权候选池内运行原始MemArt的检索与KV复用流程，同时保留latent-space检索、直接缓存复用、解耦位置编码的特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 安全访问控制 | 为多用户共享KV内存添加物理用户级别的访问控制 |
| 原有KV缓存特性保留 | 保留latent-space检索、直接缓存复用、解耦位置编码能力 |
| 处理效率 | 大幅降低预填token量，维持KV缓存的低token操作模式 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| face benchmarks | 用于长期对话QA任务的面部生物特征评估 |
| palmprint benchmarks | 用于长期对话QA任务的掌纹生物特征评估 |

🎯 实验设置与评估指标
任务为长期对话QA的所有者与非所有者查询条件下的生物特征相关评估与效率测试，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 所有者生物特征成功率 | 所有者查询时的生物特征识别成功比例 |
| 非所有者生物特征成功率 | 非所有者查询时的生物特征误识别比例 |
| 预填token量 | 处理时的预填token数量（↓ 越低越好） |

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
（注：论文未提供表号、图号等来源信息，仅报告定量数值）
**主benchmark性能（无对应表号）**
| 维度 | Face benchmarks | Palmprint benchmarks |
| ---- | ---- | ---- |
| 所有者生物特征成功率 | 95.71% ✅ | 97.60% ✅ |
| 非所有者生物特征成功率 | 0.86% | 2.00% |
💡 结论：Bio-MemArt在面部和掌纹基准测试中对授权用户的生物特征识别准确率极高，对未授权用户的误通过率极低，实现了有效的用户访问控制。

**效率对比（无对应表号）**
| 方法 | 预填token量 |
| ---- | ---- |
| Full-context prompting | 18781.96 |
| Bio-MemArt | 28.57 ✅ |
💡 结论：Bio-MemArt通过生物特征门控大幅降低了长期对话QA任务的预填token量，保留了KV缓存内存的低token操作特性。

其余实验：论文未报告（包括跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等）

4. 关键结论和发现
- Bio-MemArt在实现多用户共享KV内存的物理用户访问控制的同时，保留了KV缓存的核心特性（latent-space检索、直接缓存复用、解耦位置编码）。
- 在面部和掌纹生物特征基准测试中，Bio-MemArt对授权用户识别准确率高，未授权用户误访率极低，具备良好的安全防护效果。
- Bio-MemArt显著减少了长期对话QA任务的预填token量，提升了KV缓存内存的处理效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Bio-MemArt是一种面向多用户LLM代理的生物感知KV缓存内存框架，在为共享KV内存添加物理用户访问控制的同时，保留了KV缓存的原有特性并大幅提升了处理效率。

</details>

---

### 11. [InfluenceField: A Differentiable Field with Interventionally Identifiable Causal Structure for Multimodal World Modeling](https://arxiv.org/abs/2609.07874v1)

**Authors**: Zihao Yang, Zijia Wang, Zhiqiu Huang  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2609.07874v1  

#### Abstract
Multimodal large language models often capture visual-linguistic correlations but struggle to predict how local visual interventions propagate and affect downstream answers. We introduce InfluenceField, an intervention-aware latent field inserted between the visual encoder and language decoder. It l...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

InfluenceField: A Differentiable Field with Interventionally Identifiable Causal Structure for Multimodal World Modeling
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态大语言模型常常捕获视觉-语言相关性，难以预测局部视觉干预的传播方式及其对下游答案的影响，现有方法未有效应对这一痛点。
🚀 提出的新方法与思路
**InfluenceField**：这是一种插入在视觉编码器和语言解码器之间的干预感知潜在场，将补丁特征提升为连续空间表示，通过共享转移算子多步传播定向影响，并预测局部干预效果；训练阶段联合优化语言建模、跨环境不变性、反事实回滚监督与结构正则化；针对非线性有限基总体模型，证明目标对齐的干预监督结合转移算子的单步分离条件，可将可表示内容限制在位置内重参数化，精确恢复完整转移的定向依赖图；线性特例给出精确的部分覆盖特征与有限损失稳定性界，场分析推导系数干预的空间轮廓与共享通道校准结果。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 因果结构识别 | 可实现干预可识别的因果结构的精确恢复 |
| 视觉干预预测 | 能有效预测局部视觉干预的传播及对下游答案的影响 |
| 任务性能提升 | 在CausalVQA数据集上，整体准确率较基础模型提升13.1个百分点，规划和假设类别增益最大 |
| 鲁棒性与一致性 | 性能提升源于因果目标而非模型容量，提升了鲁棒性与事实-反事实一致性 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| CausalVQA | 用于模型在视觉问答任务上的性能评估 |
🎯 实验设置与评估指标
任务为视觉问答（VQA）；评估指标为准确率（overall accuracy），准确率越高表示性能越好，为正向指标（↑）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基础模型（Backbone） | 基线方法 | InfluenceField的基础对比模型 |
| 容量匹配基线 | 对照方法 | 匹配模型容量，用于验证性能提升是否源于因果目标而非模型容量 |
| 结构控制方法 | 对照方法 | 控制结构正则化等因果相关模块，用于验证因果目标对性能的贡献 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：InfluenceField在CausalVQA数据集上的整体准确率较其基础模型提升13.1个百分点，规划和假设类别的增益最大。
**效率对比**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
💡 结论：InfluenceField在CausalVQA视觉问答任务上取得了显著性能提升，且性能提升的核心驱动因素是其包含的因果相关训练目标，而非模型容量的增加。
4. 关键结论和发现
- 主要发现：1. InfluenceField可实现干预可识别的因果结构的精确恢复，有效解决视觉干预传播预测的痛点；2. 其性能提升源于因果目标而非模型容量，验证了因果学习对多模态模型的价值；3. 针对非线性和线性场景分别推导了相关理论界与特征分析结果。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：论文提出的InfluenceField是一种干预感知的潜在场模型，通过在视觉编码器与语言解码器间插入该模型，实现了对视觉干预传播的预测与因果结构的识别，在CausalVQA视觉问答任务上取得了优于基础模型的性能提升，且性能提升源于因果目标而非模型容量。

</details>

---

### 12. [Shift-Accumulate Attention: Multiplier-Free Query--Key Products for Transformer Decoding](https://arxiv.org/abs/2609.09208v1)

**Authors**: Khubaib Ahmed, Amna Noor, Ahsan Ul haq  
**Category**: cs.AR  
**Published**: 2026-09-10  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2609.09208v1  

#### Abstract
Power-of-two (PoT) quantisation turns a multiplication into a bit shift, so far only for the post-softmax attention--value product. The earlier and larger product, S=QK^T, has not been reformulated the same way. We quantise the key cache to a signed power-of-two fixed-point code, so that every scala...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Shift-Accumulate Attention: Multiplier-Free Query--Key Products for Transformer Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题：现有Power-of-two（PoT）量化仅将乘法操作转为比特移位，仅适用于Transformer解码中后softmax阶段的注意力-值乘积；而更早且计算量更大的QK^T乘积S尚未被以相同方式重新量化处理，传统浮点计算依赖乘法，存在计算资源消耗高、KV缓存占用大的痛点。
🚀 提出的新方法与思路
**Shift-Accumulate Attention**：将key cache量化为有符号Power-of-two定点代码，使QK^T中的每个标量乘法转换为符号翻转、比特移位和整数累加操作；引入定点头区F≥e_max，将每个移位索引r=F-e转换为非负左移，保障整数累加的精确性；额外增加子功率尾数扩展，每新增一次移位-加操作可将分数误差减半；采用移位精确在线softmax，其运行最大值存储于整数log2域，使每次缩放操作本身为精确移位；对AV乘积采用log量化。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 小批量解码效率（B=8, T=32k） | RTX 4090上4位核速度为FP16缩放点积注意力的4.60倍，KV缓存大小缩减2.5倍 |
| 大批量解码吞吐量（B=64） | 吞吐量为FP16缩放点积注意力的1.22倍 |
| 与INT8 multiply-accumulate核对比 | 在支持硬件4路INT8点积的GPU上，速度不优于INT8 MAC核；核心优势为消除乘法操作 |
| 同精度下的8位算术替换性能 | 8位Shift代码（每key占1字节）在相同核上，算术替换优势达2.02倍 |
| 误差特性 | 最近Power-of-two量化的相对误差与尺度无关，额外指数位无精度增益，精度提升仅来自尾数项（误差eps_S=0.1302，对应3、4、5位指数位均稳定） |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务：Transformer解码中的注意力计算加速与量化效率优化
| 指标 | 含义（箭头方向） |
| --- | --- |
| 计算加速比 | 对比基准方法的速度提升倍数 ↑ |
| KV缓存压缩比 | 与基准方法相比KV缓存大小的缩减倍数 ↓ |
| 吞吐量 | 解码处理的速率，无明确单位 ↑ |
| 量化误差 | 量化引入的数值误差 ↓ |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| FP16缩放点积注意力 | 现有注意力计算方法 | 传统浮点计算，依赖乘法，缓存与计算消耗高 |
| INT8 multiply-accumulate (MAC)核 | 现有整数计算方法 | 硬件加速的INT8乘累加，无需额外移位处理 |
| 8位Shift代码算术替换 | 同架构整数替换方法 | 每key占1字节，采用移位操作，无乘法 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**Shift-Accumulate Attention 解码性能（RTX 4090, 1.1B Llama decoder）**
| 场景 | 核类型 | 与FP16缩放点积注意力加速比 | KV缓存相对大小 | 与INT8 MAC核加速比 | 同精度8位Shift代码加速比 |
| --- | --- | --- | --- | --- | --- |
| B=8, T=32k | 4位Shift-Accumulate | 4.60x ✅ | 0.4x（缩减2.5倍） | - | - |
| B=64 | 4位Shift-Accumulate | 1.22x | - | - | - |
| 相同tiling | INT8 MAC核 | - | - | 5.29x ✅（Shift-Accumulate在硬件4路INT8 dot GPU上无加速优势） | - |
| 相同精度 | 8位Shift代码 | - | - | - | 2.02x ✅ |
💡 结论：Shift-Accumulate Attention在小批量解码场景下实现显著速度提升与KV缓存压缩，大批量解码下吞吐量略优于FP16方法，但在支持硬件4路INT8点积的GPU上不优于INT8 MAC核，核心优势为消除乘法操作与提升存储密度；论文未报告主benchmark性能（L2/碰撞率）、跨域/zero-shot迁移、鲁棒性/扰动测试及参数量相关结果。
4. 关键结论和发现
- 主要发现：1. Power-of-two（PoT）量化用于Transformer解码核心QK^T乘积时，最近PoT量化的相对误差与输入尺度无关，增加指数位无法提升精度，精度提升仅来自尾数项（误差eps_S=0.1302在3、4、5位指数位均保持稳定）；2. Shift-Accumulate Attention在RTX 4090的1.1B Llama解码中，小批量（B=8, T=32k）4位核速度提升4.60倍、KV缓存缩减2.5倍，大批量（B=64）吞吐量达FP16方法的1.22倍，但在支持硬件4路INT8点积的GPU上，速度不优于INT8 multiply-accumulate核；3. 8位Shift代码的算术替换在相同精度下实现2.02倍算术性能提升，核心优势为存储密度提升与乘法消除，而非原始GPU吞吐量提升。
- 方法局限性：论文未报告该方法在不同模型规模、更长序列长度、不同硬件平台的泛化性能，未提供鲁棒性/扰动测试结果，未涉及参数量相关分析。
- 未来工作：论文未明确提及未来工作方向。
> ✅ **总结一句话**：Shift-Accumulate Attention通过将Transformer解码中QK^T的乘法操作转化为移位累加，实现了注意力计算的速度提升与KV缓存压缩，核心价值为消除乘法依赖并提升存储密度。

</details>

---

### 13. [MetaKV: Adaptive KV Cache Compression for Constrained LLM Inference](https://arxiv.org/abs/2609.07966v1)

**Authors**: Michael Wang, Keith Li, Roozbeh Bostandoost  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.07966v1  

#### Abstract
Key--value (KV) cache compression is an effective way to reduce the memory overhead of large language model (LLM) inference, particularly for long-context workloads. However, existing compression methods make different trade-offs among accuracy, inference latency, and peak KV cache memory utilizatio...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MetaKV: Adaptive KV Cache Compression for Constrained LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题：现有KV缓存压缩方法均采用单一固定的压缩配置，无法适配不同输入提示的需求及用户指定的不同资源（延迟、峰值内存）约束，在准确率、推理延迟、峰值内存之间的权衡缺乏灵活性，存在适配性不足的核心矛盾。
🚀 提出的新方法与思路
**MetaKV自适应KV缓存压缩框架**：针对每个输入提示，基于用户设定的延迟和峰值内存预算，使用轻量预测模型估计各候选KV缓存压缩配置的端到端延迟、峰值内存占用及响应正确概率，最终选择同时满足延迟与内存约束且尽可能保留响应准确率的压缩配置。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 配置适配性 | 针对单个输入提示自适应选择压缩配置，而非采用统一静态配置，适配不同提示的特性 |
| 约束满足能力 | 可同时满足用户指定的延迟与峰值内存双资源约束，而非仅适配单一类型约束 |
| 响应准确率 | 在满足资源约束的前提下，相比最佳静态压缩配置，更能保留LLM的响应正确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 4种数据集（具体名称未报告） | 覆盖数学、科学、常识推理、阅读理解领域，用于评估不同任务下模型的性能表现 |
🎯 实验设置与评估指标
本次实验为评估大语言模型（LLM）在延迟与内存资源约束下的响应性能，采用的评估指标如下：
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| Constrained Success Rate (CSR) | 满足延迟和峰值内存双约束的提示中，LLM响应正确的比例，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| MetaKV | 自适应KV缓存压缩框架 | 可根据输入提示和资源约束自适应选择压缩配置 |
| KVQuant | 静态KV缓存压缩方法 | 采用固定量化规则的KV缓存压缩方法 |
| H₂O | 静态KV缓存压缩方法 | 采用保留重要token机制的固定KV缓存压缩方法 |
| RocketKV | 静态KV缓存压缩方法 | 采用滑动窗口机制的固定KV缓存压缩方法 |
| 未压缩FP16配置 | 无压缩KV缓存配置 | 未使用任何压缩的原始KV缓存配置 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未明确报告各细分实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）的具体表号、图号或章节来源，仅提及MetaKV在延迟与峰值内存的广泛约束范围内，性能优于最佳静态压缩配置。因定量结果未明确标注来源，故未披露具体数值。

4. 关键结论和发现
- 对单个输入提示自适应选择KV缓存压缩配置，能有效平衡LLM推理的延迟、内存占用与响应准确率，适配不同提示的特性与资源约束需求。
- MetaKV在覆盖多种任务与资源约束的场景下，相比最优静态压缩配置，能更好地满足用户指定的延迟与内存双约束，同时保留响应正确率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MetaKV是一种针对LLM约束推理的自适应KV缓存压缩框架，可根据用户指定的延迟和峰值内存预算，为每个输入提示选择适配的压缩配置，有效提升LLM在资源受限场景下满足双约束的响应性能。

</details>

---

### 14. [VLX-VR: An Agentic-Aware Video Reasoning Model](https://arxiv.org/abs/2609.09985v1)

**Authors**: Sheng Li, Peng Liu, Qianqian Zhang, Tiancheng Zhao  
**Category**: cs.CL  
**Published**: 2026-09-10  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2609.09985v1  

#### Abstract
Real-world video understanding requires integrating visual, audio, textual, and temporal evidence distributed across a video. Yet many pipelines use a fixed video context and single-pass inference, limiting adaptive evidence acquisition when observations are incomplete, ambiguous, or conflicting. We...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VLX-VR: An Agentic-Aware Video Reasoning Model
1. 论文的主要贡献和创新点
✅ 解决的问题：现实世界视频理解需要整合视频中分布的视觉、音频、文本和时序证据，但现有多数视频理解管道使用固定视频上下文与单次推理模式，当观测不完整、模糊或冲突时，限制了模型的自适应证据获取能力。
🚀 提出的新方法与思路
**VLX-VR模型**：提出一种agentic-aware视频推理模型，嵌入在由Think--Memory--Observation循环定义的视频推理框架中训练；每一步中，模型确定所需证据，调用read_memory或write_memory，融合返回的观测结果，再决定是否继续推理或输出任务结果；该模型使用包含视频和智能体轨迹的多模态数据，通过强化学习训练以学习证据获取、记忆使用与终止策略。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 自适应证据获取 | 通过Think--Memory--Observation循环实现自适应的视频证据获取，可应对不完整、模糊或冲突的观测场景 |
| 基准性能 | 在MINERVA基准的对比模型中达到最优性能（SOTA） |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MINERVA | 主基准测试 |
🎯 实验设置与评估指标
实验任务为视频推理任务，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 准确率 | 视频推理任务的预测准确率，越高越好（↑） |
| 跨时长准确率方差 | 不同时长分组的准确率方差，越低越好（↓） |
⚔️ 基线方法对比：论文未报告具体基线方法的详细类型与特点
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告具体表号，在MINERVA基准上，模型准确率为78.79%；三个时长分组的准确率分别为76.70%、78.73%、80.92%；跨时长准确率方差为2.97 pp²。
2. 推理轨迹与证据一致性：论文未报告具体表号，在正确回答的样本中，96.20%的VLX-VR推理轨迹与MINERVA参考推理轨迹及其描述的证据一致；所有评估样本中，约75.80%同时满足答案正确性与证据轨迹一致性要求。
其他实验类别（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告
4. 关键结论和发现
- 主要发现：1）VLX-VR在MINERVA基准的对比模型中达到最优性能，且跨不同视频时长组表现稳定；2）正确回答的VLX-VR推理轨迹与MINERVA参考高度一致，多数评估样本同时满足答案正确性与证据轨迹一致性；3）视频推理任务中，计数、状态变化、因果推理及空间感知仍是具有挑战性的任务。
- 方法局限性：计数、状态变化、因果推理、空间感知等视频推理相关任务仍具挑战性。
- 未来工作：针对计数、状态变化、因果推理、空间感知等视频推理的挑战性任务优化模型性能。
> ✅ **总结一句话**：VLX-VR是一种基于Think--Memory--Observation循环的agentic-aware视频推理模型，通过多模态数据与强化学习训练，在MINERVA基准上取得最优性能，推理轨迹符合证据一致性要求，但仍存在部分视频推理任务的挑战。

</details>

---

### 15. [Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning](https://arxiv.org/abs/2609.09030v1)

**Authors**: Mar Gonz\`alez I Catal\`a, Haitz S\'aez de Oc\'ariz Borde, Davide Murari, Carola-Bibiane Sch\"onlieb, Pietro Li\`o, George Monta\~nez  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2609.09030v1  

#### Abstract
Chain-of-thought reasoning provides a structured computation between a model's input and final answer. Yet it is often evaluated through endpoint accuracy, which ignores the path taken to reach that answer. An emerging line of work addresses this limitation using entropy profiles, which track how un...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
Chain-of-thought推理常通过端点准确率评估，忽略推理路径；现有熵轮廓方法仅跟踪推理过程中不确定性的演变，未揭示导致不确定性的竞争假设，无法全面评估LLM推理的动态特性。

🚀 提出的新方法与思路
**Answer-Distribution Trajectories（答案分布轨迹）**，一种受随机动力学启发的表示，跟踪推理过程中模型的完整预测答案分布，比端点和熵摘要更精细，可刻画包含探索、修正、motion和承诺的动态推理特征，还能区分推理成功与失败的不同动态机制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 表示精细度 | 比端点准确率、熵摘要更精细，可捕捉现有方法遗漏的推理路径动态 |
| 可解释性 | 能揭示推理过程中导致不确定性的竞争假设，而非仅跟踪不确定性本身 |
| 区分能力 | 可区分具有相同端点结果或相似熵轮廓的轨迹间的不同推理动态 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 四个推理基准 | 用于LLM推理动态特性的分析实验 |

🎯 实验设置与评估指标
实验任务：分析不同开放权重语言模型在推理过程中的动态特性，评估训练与推理选择对推理动态的影响。
| 指标 | 含义（箭头） |
| ---- | ---- |
| 论文未报告 | 论文未报告具体评估指标及定义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 端点准确率 | 推理评估指标 | 仅关注最终答案的正确性，忽略推理路径的动态过程 |
| 熵轮廓 | 推理分析方法 | 跟踪推理过程中不确定性的演变，未揭示导致不确定性的竞争假设 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：名称（场景）**
论文未报告
💡 结论：论文未报告

4. 关键结论和发现
- 2-3条主要发现：①相同端点准确率和相似熵轮廓的轨迹，存在显著不同的推理动态；②LLM推理的动态特性在不同模型、任务间存在大量差异，且不同目标偏好不同动态；③训练和推理选择会系统地重塑答案分布轨迹所表征的推理动态。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出受随机动力学启发的Answer-Distribution Trajectories表示，能精细刻画LLM推理的动态特性，为分析和评估LLM推理提供了丰富的框架。

</details>

---

### 16. [One Step, One Lead: Mitigating Higher-Order Interference in Multi-Domain Reinforcement Learning via Cross-Step Control](https://arxiv.org/abs/2609.06469v1)

**Authors**: Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Guojun Yin, Wei Lin, Ran He  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.06469v1  

#### Abstract
Reinforcement learning (RL) across multiple domains can broaden the reasoning capabilities of large language models (LLMs), yet joint training often degrades individual-domain performance and can destabilize optimization. Existing work typically diagnoses such interference from a single-step view us...

---

### 17. [Long-Horizon Language Model Reinforcement Learning via Progressive Point Matching](https://arxiv.org/abs/2609.07303v1)

**Authors**: Preston Fu, Kevin Frans, Oleh Rybkin, Sergey Levine, Aviral Kumar  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.07303v1  

#### Abstract
Current paradigms for training language models via reinforcement learning rely heavily on sparse outcome rewards. However, as we pursue tasks that require longer and more complicated trajectories, such strategies result in slow learning. Prior work has attempted to address this problem by rewarding ...

---

### 18. [Compiling VGDL into Causal Models](https://arxiv.org/abs/2609.05459v1)

**Authors**: Mohit Jiwatode, Bodo Rosenhahn, Alexander Dockhorn  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.05459v1  

#### Abstract
Reinforcement learning and large language models often struggle to accurately capture the causal mechanics of game environments. Standard reinforcement learning agents tend to rely on spurious correlations, while large language models are prone to hallucinating game rules. Although causal reinforcem...

---

### 19. [HBFSim: Fast and Faithful Simulation of High-Bandwidth Flash Under Real GPU Execution](https://arxiv.org/abs/2609.09800v1)

**Authors**: Yanpeng Hu, Yiwei Yang, Yuanwu Zhu, Yusheng Zheng, Wei Zhang, Andi Quinn  
**Category**: cs.AR  
**Published**: 2026-09-10  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2609.09800v1  

#### Abstract
Serving a large language model (LLM) is limited by memory capacity. High-Bandwidth Flash (HBF) stacks NAND flash inside the accelerator package, one tier below high-bandwidth memory (HBM); the specification was published on August 3, 2026, and the first inference devices are expected to sample in ea...

---

### 20. [CLAMP: Constrained Decoding for Vision-Language Embodied Planning](https://arxiv.org/abs/2609.08602v1)

**Authors**: Tianyi Ma, Parisa Kordjamshidi  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.08602v1  

#### Abstract
Embodied planning increasingly relies on vision-language models (VLMs) to translate instructions and visual observations into executable action sequences. However, fluent plans are not always executable. A VLM may refer to objects that are not visually observed, select actions whose required afforda...

---

### 21. [Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding](https://arxiv.org/abs/2609.09338v1)

**Authors**: Fengxiang Bie, Yuqing Jian, Yifan Yu, Zhongzhu Zhou, Zelei Shao, Ben Athiwaratkun, Shuaiwen Leon Song, Chenfeng Xu, Xiaoxia Wu, Tianyi Zhang  
**Category**: cs.CL  
**Published**: 2026-09-10  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.09338v1  

#### Abstract
Speculative decoding is critical for accelerating LLM inference. However, the speedup is fragile: drafters are typically trained against a narrow distribution for a single target model, and their acceptance rate collapses under workload shifts. This is a striking inversion of modern LLM development,...

---

### 22. [I Don't Miss You, but I Do: Self-Explanation Faithfulness of Modality Missingness in Vision-Language Models](https://arxiv.org/abs/2609.07596v1)

**Authors**: Aydin Javadov, Daniel Schoess, Florian von Wangenheim  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.07596v1  

#### Abstract
Vision-language models are increasingly used in settings where some input modalities may be unavailable, yet we know little about whether they can faithfully explain how such missing information affects their own predictions. We introduce an interventional protocol for evaluating self-explanations o...

---

### 23. [Online Signature Verification Using Augmented Path Signature and T-Mamba](https://arxiv.org/abs/2609.08276v1)

**Authors**: Ruiling Li, Danyu Yang  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.08276v1  

#### Abstract
Handwritten signature verification is vital for personal authentication across commercial and financial applications. Although deep learning methods are widely adopted for online signature verification (OSV), they often struggle with capturing highly discriminative features and modelling long-range ...

---

### 24. [Data-Centric Post-Training for Financial Reasoning: Mining, Distillation, and Verifiable Learning](https://arxiv.org/abs/2609.10113v1)

**Authors**: Zhirayr Hayrapetyan, Andrei Kalmykov, Denis Kokosinskii, Dmitry Stanishevskii, Dmitry Zmitrovich  
**Category**: cs.CL  
**Published**: 2026-09-10  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.10113v1  

#### Abstract
Financial text, textbooks, and question-answer pairs are abundant, but only a small fraction is directly usable for reasoning-focused post-training. Existing QA pairs often lack explicit reasoning, sufficient context, or reliably verifiable answers, while textbooks must first be transformed into syn...

---

### 25. [Bi-HYCO: Bi-Objective Cooperative Learning for PDE Parameter Identification under Fragmented Observations](https://arxiv.org/abs/2609.06511v1)

**Authors**: Umberto Biccari, Jun Chen, Roberto Morales, Enrique Zuazua  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.06511v1  

#### Abstract
Physical and synthetic models may describe complementary aspects of the same PDE-governed system while receiving different, possibly fragmented, observations. We propose Bi-Objective HYCO (Bi-HYCO), a cooperative framework that retains both representations and their local observational objectives wh...

---

### 26. [A budget-dependent crossover between coverage- and response-based training-set selection for machine-learned interatomic potentials](https://arxiv.org/abs/2609.05877v1)

**Authors**: Jia Bi, Alin-Marin Elena  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.05877v1  

#### Abstract
Selecting compact training sets for machine-learned interatomic potentials requires deciding whether to preserve structural diversity or target configurations on which models disagree. The better choice can depend on how much data is retained, making a comparison at one training-set size insufficien...

---

### 27. [Do Reasoning Representations Help Humans Evaluate LLM Outputs?](https://arxiv.org/abs/2609.09038v1)

**Authors**: Jaewoo Lim, Sungbok Shin, Sanghyun Hong  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.09038v1  

#### Abstract
Reasoning representations are increasingly used as explanations for large language model outputs. Yet they are typically evaluated with model-centric criteria, such as answer accuracy and faithfulness, leaving it unclear whether they help people evaluate model responses. In this work, we study reaso...

---

### 28. [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](https://arxiv.org/abs/2609.07681v1)

**Authors**: Yuval Koren, Assaf Ben-Kish, Raja Giryes, Lior Wolf, Itamar Zimerman  
**Category**: cs.LG  
**Published**: 2026-09-10  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2609.07681v1  

#### Abstract
Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory. In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance. This pape...

---

### 29. [Learning Counterfactual World Models for Embodied Reasoning under Partial Observability](https://arxiv.org/abs/2609.05834v1)

**Authors**: Todd Y. Zhou, Daniel Zhang  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 38.5  
**Type**: new  
**ArXiv ID**: 2609.05834v1  

#### Abstract
World models promise a general route to embodied intelligence: learn predictive dynamics once, then reason, plan, and act with them. Increasingly, the representations beneath such models are pretrained on large-scale video, interaction, and multimodal corpora, which raises a question prediction qual...

---

### 30. [Reasoning-Aware Compression: Identifying and Protecting Vulnerable Reasoning Circuits for Energy-Efficient LLM Deployment](https://arxiv.org/abs/2609.05512v1)

**Authors**: Leonard Twagirayezu, Prasenjit Mitra  
**Category**: cs.AI  
**Published**: 2026-09-10  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2609.05512v1  

#### Abstract
Large Reasoning Models (LRMs) impose substantial energy costs during deployment, yet current compression methods apply uniform quantization across all components, risking damage to critical reasoning circuits. We present a reasoning-aware compression framework that benchmarks quantization conditions...

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
