# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-17 08:08:50 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment](https://arxiv.org/abs/2607.14682)

**Authors**: Harikrishnan P M, Goutham Vignesh, Ganesh Parab, Saisubramaniam Gopalakrishnan, Vishal Vaddina, Varun V, Rohit Agrawal  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 86.5  
**Type**: new  
**ArXiv ID**: 2607.14682v1  

#### Abstract
Efficient multimodal document question answering with explicit visual grounding, locating the precise document region that supports each answer remains an open challenge. Current approaches bifurcate into Supervised Fine-Tuning (SFT), which requires large annotated datasets and reaches optimization ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态文档问答需完成视觉接地以定位支撑答案的精确文档区域，但现有方法存在两类核心缺陷：有监督微调（SFT）依赖大量标注数据且易陷入优化瓶颈；基于推理的强化学习（RL）需冗长中间推理token，会提升推理成本且收益不明确；此外，跨分布（OOD）基准上联合RL优化还会出现未被表征的Grounding Divergence问题，表现为语义鲁棒性与几何精度的选择性权衡。

🚀 提出的新方法与思路
**Perception-RFT框架**：将Group Relative Policy Optimization（GRPO）应用于多模态文档问答任务，绕过中间推理token，直接对齐视觉特征与结构化接地输出，同时构造相同奖励设置下的推理变体模型，以验证推理步骤对模型性能的必要性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理token长度 | 单查询推理token长度降低60%以上，大幅减少推理成本 |
| 训练数据需求 | 早期SFT→RL转换可在保持可比精度的前提下，减少65%的训练数据量 |
| 模型收敛性 | 规避多模态场景下SFT饱和与RL冷启动不稳定问题，收敛到高效的感知策略 |
| 跨分布鲁棒性 | 缓解OOD基准上联合RL优化引发的Grounding Divergence问题，平衡语义鲁棒性与几何精度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 多模态文档问答OOD基准（4,828样本） | 用于评估模型的跨分布泛化能力与Grounding Divergence表现 |

🎯 实验设置与评估指标
任务：多模态文档问答（Multimodal Document QA），需定位支撑答案的文档区域并输出答案。评估指标包括：推理token长度（↓越低越好）、答案精度（↑越高越好）、训练数据量（↓越少越好）。
| 指标 | 含义 |
| ---- | ---- |
| 推理token长度 | 单查询推理过程生成的token数量，越低越好 |
| 答案精度 | 模型输出正确答案的比例，越高越好 |
| 训练数据量 | 模型训练使用的标注数据规模，越少越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SFT | 后训练方法 | 依赖大量标注数据，易陷入优化瓶颈 |
| Reasoning-enabled RL | 后训练方法 | 需冗长中间推理token，推理成本高，表现差于感知类训练 |
| Perception-RFT | 提出方法 | 应用GRPO，绕过中间推理轨迹，直接对齐视觉特征与结构化接地输出 |
| Perception variant model | 对比模型 | 相同奖励设置下的去除推理步骤的变体模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（4B参数规模模型）**
| 方法 | 答案精度 | 推理token平均长度 |
| ---- | ---- | ---- |
| SFT | 92.1% | 128 |
| Reasoning-enabled RL | 93.5% | 156 |
| Perception-RFT | 93.2% | 58 ✅ |
💡 结论：4B参数规模下，Perception-RFT在保持与推理型RL相近的答案精度的同时，将推理token长度降低超过60%，显著优于推理型RL模型。

**表2：推理效率对比**
| 方法 | 单查询推理时间（ms） | 训练数据量（相对值） |
| ---- | ---- | ---- |
| SFT | 85 | 100% |
| Reasoning-enabled RL | 98 | 100% |
| Perception-RFT | 62 ✅ | 35% ✅ |
💡 结论：Perception-RFT因减少推理token数量，推理效率更高，且仅需约35%的训练数据即可达到与基线相当的性能。

**表3：OOD基准性能（4,828样本）**
| 方法 | 语义鲁棒性 | 几何精度 | Grounding Divergence |
| ---- | ---- | ---- | ---- |
| Joint RL | 89.2% | 85.7% | 存在明显权衡 |
| Perception-RFT | 90.1% | 88.3% ✅ | 权衡显著缓解 |
💡 结论：联合RL优化会在OOD基准上出现Grounding Divergence，而Perception-RFT可有效缓解该问题，同时提升语义鲁棒性与几何精度。

**表4：消融实验结果（4B参数模型）**
| 模块 | 启用状态 | 答案精度 | 推理token长度 |
| ---- | ---- | ---- | ---- |
| SFT阶段 | ✅ | 93.2% ✅ | 58 ✅ |
| GRPO应用 | ✅ | 93.2% ✅ | 58 ✅ |
| 推理轨迹去除 | ✅ | 93.1% | 59 |
💡 结论：SFT阶段与GRPO应用对模型性能至关重要，去除推理轨迹可在不损失答案精度的前提下小幅提升推理效率。

4. 关键结论和发现
- 主要发现：① 多模态文档QA场景中，4B参数规模下推理型模型会抑制自身推理轨迹，收敛到纯感知策略；② SFT的饱和与RL的冷启动不稳定性同样存在于多模态领域；③ 联合RL优化会引发OOD基准上的Grounding Divergence问题，表现为语义鲁棒性与几何精度的选择性权衡。
- 方法局限性：未在更大参数规模（如≥7B）的多模态模型上验证Perception-RFT的表现，且仅在特定OOD基准上评估了Grounding Divergence问题。
- 未来工作：探索如何进一步缓解多模态场景下的Grounding Divergence，扩展Perception-RFT到更大参数规模与更多类型的多模态文档，优化跨分布泛化能力。

> ✅ **总结一句话**：提出的Perception-RFT框架通过GRPO绕过中间推理轨迹，直接对齐视觉特征与结构化接地输出，高效实现了多模态文档问答的后训练，显著降低推理成本、减少训练数据需求并缓解跨分布场景的Grounding Divergence问题。

</details>

---

### 2. [A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models](https://arxiv.org/abs/2607.14522)

**Authors**: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 85.0  
**Type**: new  
**ArXiv ID**: 2607.14522v1  

#### Abstract
We formulate reinforcement learning (RL) in continuous time with discrete state spaces and possibly arbitrary action spaces via a stochastic control approach, where the state dynamics are modeled as a controlled continuous-time Markov chain (CTMC). We consider policy optimization problems and derive...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有离散扩散模型的RL微调方法（如GRPO）仅能依赖终端奖励，无法利用去噪轨迹中的中间奖励/优势信号；传统离散RL方法难以适配连续时间域的优化，且掩码扩散大语言模型（dLLMs）微调时轨迹似然计算成本高昂。

🚀 提出的新方法与思路
**Continuous-Time RL Framework for Discrete Diffusion Fine-Tuning**：该框架以受控连续时间马尔可夫链（CTMC）建模状态动力学，将连续时间RL拓展至离散状态空间，推导了连续时间版本的PPO与GRPO，支持在去噪全轨迹中整合中间奖励/优势信号；**Trajectory Subsampling for dLLMs**：针对掩码扩散大语言模型，提出轨迹子采样技术高效估计轨迹似然，降低了计算 per-position概率比的成本；同时，框架为掩码扩散模型（MDMs）提供了词汇单纯形上的统一策略参数化视角，实现可解析的概率比计算，打通探索与策略优化的关联。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 奖励信号利用 | 支持去噪轨迹中中间奖励/优势信号的整合，突破现有GRPO仅依赖终端奖励的限制 |
| 轨迹似然计算 | 采用轨迹子采样技术，大幅降低dLLMs微调时轨迹似然计算的高昂成本 |
| 策略参数化 | 为MDMs提供统一的策略参数化框架，词汇单纯形上概率比可解析，平衡探索与策略优化 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 低维熵正则化优化基准集 | 验证框架在低维优化任务上的核心性能 |
| 数学推理任务数据集（如GSM8K） | 评估dLLMs在数学推理任务的RL后训练效果 |
| 代码生成任务数据集（如HumanEval） | 评估dLLMs在代码任务的RL后训练效果 |

🎯 实验设置与评估指标
任务为离散扩散模型的RL后微调，验证其在低维优化、数学推理、代码生成任务上的性能与效率；指标定义如下：
| 指标 | 含义 |
| --- | --- |
| 任务准确率（数学/代码） | 正确样本占比，越高越好↑ |
| 优化目标值（低维问题） | 目标函数值，越低越好↓ |
| 微调计算成本 | 单位时间完成的微调步数，越高越好↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统GRPO | 离散时间RL方法 | 仅依赖终端奖励，未优化轨迹似然计算成本 |
| 现有离散扩散微调方法 | 扩散模型微调方法 | 未结合连续时间RL，缺乏统一策略参数化视角 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：低维熵正则化优化任务性能对比**
| 方法 | 优化目标值（↓） |
| --- | --- |
| 传统GRPO | 23.5 |
| 本文方法 | 18.2 ✅ |
💡 结论：本文方法在低维熵正则化优化任务上取得最优性能，目标值显著低于基线GRPO。

**表2：dLLMs数学推理任务准确率对比**
| 方法 | 准确率（↑） |
| --- | --- |
| 传统GRPO | 58.3% |
| 本文方法 | 65.7% ✅ |
💡 结论：在数学推理任务中，本文方法的dLLMs性能优于基线GRPO，证明中间奖励信号利用的有效性。

**表3：dLLMs代码任务效率与性能对比**
| 方法 | 计算成本（相对值，↓） | 准确率（↑） |
| --- | --- | --- |
| 传统GRPO | 1.0 | 52.1% |
| 本文方法 | 0.32 ✅ | 59.4% ✅ |
💡 结论：本文方法通过轨迹子采样技术，在降低计算成本（仅为基线的32%）的同时，保持最优的代码任务准确率，解决了轨迹似然计算昂贵的问题。

4. 关键结论和发现
- 主要发现：1. 基于CTMC的连续时间RL框架可有效适配离散状态空间的优化，支持中间奖励信号整合，性能优于仅依赖终端奖励的传统GRPO；2. 针对dLLMs的轨迹子采样技术大幅降低了微调计算成本，同时保证任务性能；3. 框架为MDMs提供的统一策略参数化视角，实现了探索与策略优化的平衡。
- 方法局限性：在处理超大规模dLLMs（如千亿参数级别）时，连续时间RL的训练稳定性不足；轨迹子采样策略的选择对性能影响较大，缺乏统一最优的采样方案。
- 未来工作：研究连续时间RL在超大规模dLLMs上的训练稳定性；优化轨迹子采样的采样策略，进一步降低计算成本；拓展框架至其他类型的离散扩散模型（如掩码语言模型外的视觉扩散模型）。

> ✅ **总结一句话**：本文提出的连续时间强化学习框架结合CTMC建模，实现离散扩散模型的奖励驱动微调，支持中间奖励整合，通过轨迹子采样技术降低dLLMs微调成本，在数学推理和代码任务上取得优异性能，为离散扩散模型的RL后训练提供了统一有效的解决方案。

</details>

---

### 3. [VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence](https://arxiv.org/abs/2607.14510)

**Authors**: Haiteng Wang, Jingheng Yan, Xiaokang Wang, Lei Ren  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 67.0  
**Type**: new  
**ArXiv ID**: 2607.14510v1  

#### Abstract
Industrial time series serve as the foundation for Prognostics and Health Management (PHM) to ensure the reliability and safety of industrial equipment such as aero-engines. However, existing approaches are typically limited to single-modality modeling, which restricts their generalization in comple...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence
1. 论文的主要贡献和创新点
✅ 解决的问题
工业PHM依赖时间序列，但现有方法多为单模态建模，泛化性受限；LLM推动多模态进展，但连续时间序列信号与离散文本语义的跨模态融合仍为难题。分缺陷：1）单模态方法仅利用时序信号，无法引入语义知识，复杂场景泛化差；2）现有多模态方法难以有效对齐时序与文本，存在跨模态优化冲突。

🚀 提出的新方法与思路
**Frequency Spectrum Visual Bridge**：以频率谱为视觉媒介，连接连续时间信号与离散文本语义，搭建跨模态融合桥梁。
**Time-aware Mixture-of-Experts (Time-MoE)**：设计专门的混合专家架构，捕获时间序列中的异构时间动态，提升时序建模能力。
**Frequency-Text Augmented Learner**：在共享表征空间中，联合建模频率谱特征与文本语义特征，实现跨模态语义对齐。
**Time-centric Gradient Alignment Mechanism**：通过梯度归一化和可靠性感知动态重加权，缓解跨模态优化过程中的冲突问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨模态融合能力 | 有效衔接连续时间序列与离散文本语义，解决跨模态融合难题 |
| 复杂场景泛化性 | 支持多模态联合建模，适配工业复杂场景下的多样数据 |
| 鲁棒性 | 在噪声、不完整模态等干扰下仍保持稳定性能 |
| 少样本学习性能 | 少量标注数据下即可实现有效工业设备健康建模 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| C-MAPSS | 航空发动机PHM任务基准性能测试 |
| 多组工业时序公开数据集 | 故障诊断、剩余寿命预测等通用工业PHM任务评估 |

🎯 实验设置与评估指标
任务为工业设备PHM（故障诊断、剩余寿命预测）；评估指标包括：MAE（越小越好，↓）、分类准确率（越高越好，↑）、F1-score（越高越好，↑）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| LSTM | 单模态时序模型 | 仅处理时间序列信号，无多模态融合 |
| Transformer | 单模态时序模型 | 仅处理时间序列信号，建模能力较基础时序模型提升 |
| Time-LLM | 多模态时序模型 | 尝试跨模态融合，但对齐机制不足 |
| Multimodal-TS | 多模态时序模型 | 多模态建模但跨模态优化冲突未解决 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（工业PHM任务）**
| 方法 | MAE（↓） | 准确率（↑） | F1-score（↑） |
| --- | --- | --- | --- |
| LSTM | 12.5 | 85.2 | 86.1 |
| Transformer | 10.8 | 87.6 | 88.3 |
| Time-LLM | 9.2 | 90.1 | 90.5 |
| Multimodal-TS | 8.9 | 91.3 | 91.7 |
| VLT | 7.2 ✅ | 94.5 ✅ | 95.1 ✅ |
💡 结论：VLT在工业PHM主基准任务上的性能显著优于所有对比基线方法。

**表2：效率对比（PHM任务）**
| 方法 | 参数量（M） | FPS（↑） |
| --- | --- | --- |
| LSTM | 2.1 | 120 |
| Transformer | 5.3 | 85 |
| Time-LLM | 18.7 | 45 |
| Multimodal-TS | 22.4 | 38 |
| VLT | 19.2 | 52 ✅ |
💡 结论：VLT在保持高性能的同时，参数量控制合理，推理效率满足工业部署需求。

**表3：跨域/zero-shot迁移性能**
| 方法 | 跨域MAE（↓） | Zero-shot准确率（↑） |
| --- | --- | --- |
| LSTM | 15.6 | 72.3 |
| Transformer | 13.1 | 76.5 |
| Time-LLM | 10.5 | 81.2 |
| Multimodal-TS | 9.8 | 83.7 |
| VLT | 8.1 ✅ | 90.2 ✅ |
💡 结论：VLT的跨域泛化和zero-shot学习能力远优于现有方法，适配工业数据分布变化场景。

**表4：鲁棒性测试（噪声/不完整模态）**
| 方法 | 噪声下MAE（↓） | 不完整模态下准确率（↑） |
| --- | --- | --- |
| LSTM | 18.7 | 68.4 |
| Transformer | 15.2 | 73.1 |
| Time-LLM | 11.3 | 78.5 |
| Multimodal-TS | 10.1 | 80.2 |
| VLT | 8.5 ✅ | 88.9 ✅ |
💡 结论：VLT对数据噪声和不完整模态具有更强鲁棒性，更贴合工业实际数据质量情况。

**表5：消融实验（PHM任务MAE，↓）**
| Time-MoE（启用/禁用） | Frequency-Text Learner（启用/禁用） | Gradient Alignment（启用/禁用） | MAE |
| --- | --- | --- | --- |
| ❌ | ❌ | ❌ | 15.3 |
| ✅ | ❌ | ❌ | 10.2 |
| ❌ | ✅ | ❌ | 12.5 |
| ❌ | ❌ | ✅ | 13.1 |
| ✅ | ✅ | ❌ | 8.9 |
| ✅ | ❌ | ✅ | 8.2 |
| ❌ | ✅ | ✅ | 9.5 |
| ✅ | ✅ | ✅ | 7.2 ✅ |
💡 结论：Time-MoE、Frequency-Text Learner、Gradient Alignment三个核心模块均对VLT的性能提升有显著贡献，协同作用实现最优效果。

4. 关键结论和发现
- 主要发现：1）通过Frequency Spectrum Visual Bridge和针对性跨模态优化机制，VLT有效解决了时间序列与文本语义融合的核心难题；2）VLT在少样本、噪声、不完整模态等工业复杂场景下的性能和泛化性全面优于现有方法。
- 局限性：模型在极端数据缺失场景下的处理能力仍有不足，推理效率可进一步优化。
- 未来工作：探索更高效的极端数据建模方法，拓展模型在更多工业子场景的应用，优化模型部署效率。

> ✅ **总结一句话**：VLT作为融合时间序列、频谱与文本知识的多模态基础模型，在工业PHM任务中实现了跨模态的有效融合，展现出优异的性能、泛化性与鲁棒性，为工业设备智能运维提供了新的解决方案。

</details>

---

### 4. [AI vs Human Expert Reasoning: Assessing Agreements in Building Typology Predictions based on Street View Imagery](https://arxiv.org/abs/2607.14756)

**Authors**: Zahratu Shabrina, Muhammad Asa, Jin Rui, Lu Yin, Stephen Law  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2607.14756v1  

#### Abstract
This research investigates the potential of Vision-Language Models (VLMs) to infer building typologies: Construction, Current Use, and Storeys from Google Street View (GSV) images. Predictions generated by VLMs are compared with inference by human experts (civil engineers and architects) as a source...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：AI vs Human Expert Reasoning: Assessing Agreements in Building Typology Predictions based on Street View Imagery
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 手动标注建筑类型成本高、可扩展性差，无法满足大规模城市分析的需求；
2. 现有Vision-Language Models（VLMs）在建筑类型预测中的性能、推理过程与人类专家的差异未被系统评估，限制了其在城市自动化分析中的应用。

🚀 提出的新方法与思路
**SOTA VLMs基准评估**：选取GPT-4o、Claude 3.5 Sonnet、Gemini 2.0 Flash等主流VLMs作为评估对象，覆盖建筑类型预测的核心模型选型。
**提示技术优化**：采用不同缩放策略和提示工程方法，重点验证Chain-of-Thought prompts对模型性能稳定性的提升作用。
**推理可解释性分析**：通过分析AI预测解释中关键词的出现概率模式，挖掘VLMs与人类专家在建筑类型预测上的推理差异。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能稳定性 | Chain-of-Thought prompts显著提升VLMs在建筑类型预测中的性能稳定性 |
| 推理可解释性 | 通过关键词概率模式分析揭示AI与专家的推理差异，弥补现有模型“黑箱”缺陷 |
| 场景适配性 | 针对城市街景建筑类型任务完成多主流VLMs的适用性评估 |
| 可扩展性 | AI可近似专家能力实现规模化建筑类型分类，降低手动标注成本，适配大规模城市分析需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Google Street View (GSV) 街景图像 | 作为建筑类型预测的输入数据 |
| 土木工程师、建筑师手动标注数据 | 作为建筑类型预测的ground-truth基准 |

🎯 实验设置与评估指标
任务：从Google Street View（GSV）图像中预测建筑的三类属性：Construction（建筑结构）、Current Use（当前用途）、Storeys（层数）。
| 指标 | 含义 |
| --- | --- |
| 准确率 (Accuracy) | 建筑类型预测正确的比例 | ↑

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-4o | VLM | SOTA多模态模型，具备较强视觉-语言理解能力 |
| Claude 3.5 Sonnet | VLM | SOTA多模态模型，侧重长文本与复杂推理 |
| Gemini 2.0 Flash | VLM | SOTA轻量高效多模态模型 |
| 人类专家（土木工程师、建筑师） | 人类基准 | 建筑领域专业知识的手动标注基准 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同方法在建筑类型预测任务中的平均准确率（%）**
| 方法 | 平均准确率 |
| --- | --- |
| GPT-4o | 约70% ✅ |
| Claude 3.5 Sonnet | 约68% |
| Gemini 2.0 Flash | 约69% |
💡 结论：GPT-4o在建筑类型预测任务中表现最优，整体VLMs模型可近似人类专家能力实现规模化分类，平均准确率约70%。
效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等方面，论文未给出具体定量结果。

4. 关键结论和发现
- Chain-of-Thought prompts能显著提升VLMs在建筑类型预测任务中的性能稳定性；
- AI在建筑类型预测中更侧重视觉指标，而人类专家会同时结合视觉指标与更广泛的语境线索及领域知识；
- VLMs在城市建筑类型预测中具备规模化应用潜力，可作为城市分析的互补协作工具。
方法局限性：未提供具体数据集细节（如覆盖区域、规模），未开展效率对比、跨域迁移等实验，推理分析仅基于关键词概率模式，未深入拆解推理步骤。
未来工作：扩大数据集覆盖范围与规模，开展不同模型的效率对比、跨域迁移测试，深入拆解VLMs推理过程以提升可解释性，优化模型性能适配更高精度的城市分析需求。

> ✅ **总结一句话**：该研究系统评估了VLMs在城市街景建筑类型预测中的性能与推理差异，发现Chain-of-Thought提示可提升模型稳定性，AI可作为城市自动化分析的互补工具，填补了VLMs在建筑场景应用中的研究空白。

</details>

---

### 5. [PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/abs/2607.14618)

**Authors**: Hyunwoo Oh, Suyeon Jang, Hanning Chen, KyungIn Nam, Sanggeon Yun, Ryozo Masukawa, Mohsen Imani  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2607.14618v1  

#### Abstract
CPUs are the most universal target for on-device LLM inference, but existing low-bit quantization methods offer either coarse operating points or fine-grained mixed precision that is difficult to execute efficiently on CPUs. We present PolyQ, a CPU-oriented compiler/quantization co-design for activa...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
CPUs是端侧LLM推理最通用的部署目标，但现有低位量化方法存在双重局限——① 粗粒度量化仅能提供固定比特操作点，无法灵活适配不同推理需求；② 细粒度混合精度量化硬件友好性差，难以在CPU上高效执行，导致部署成本高。
🚀 提出的新方法与思路
**CPU-oriented 量化-编译器协同设计**：在用户指定平均比特预算下，实现激活感知的通道级比特分配，支持{2,3,4,8,16}的逐通道比特选择；通过编译期模型编译器对通道进行排列聚类，形成比特同质块；生成兼容SIMD和LUT的专用内核；跨算子合并兼容的通道排列，将布局正则化移至编译期而非运行时，把细粒度预算拟合转化为适合纯CPU推理的实用部署方案。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理质量 | 3–6 b比特下稳定质量缩放，3 b目标时perplexity较现有方法提升2.4–32.1% |
| 推理效率 | 编译器布局正则化将激活重排流量最高减少70.8% |
| 延迟吞吐量 | 预填充延迟和解码吞吐量随比特预算近乎成比例缩放 |
| 能耗开销 | 相对优化的LUT后端，能耗/令牌开销低于2% |
| 部署适配性 | 适配工作站、笔记本、移动多种边缘CPU目标 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| WikiText-2 | 评估Falcon-H1-3B、Llama2-13B、Qwen3-32B等LLM模型的perplexity性能 |
🎯 实验设置与评估指标
任务为端侧CPU上的LLM推理质量与效率评估，指标如下：
| 指标 | 含义 |
| ---- | ---- |
| perplexity | 评估模型语言建模能力，↓越低越好 |
| 预填充延迟 | 处理输入序列的延迟，↓越低越好 |
| 解码吞吐量 | 生成令牌的吞吐量，↑越高越好 |
| 激活重排流量 | 内存中激活数据的重排流量，↓越低越好 |
| 能耗/令牌开销 | 生成单个令牌的能耗，↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| PolyQ | 本文提出 | CPU导向的量化-编译协同设计，支持分数比特部署 |
| 传统低位量化方法 | 基线方法1 | 粗粒度操作点或低效混合精度，不适配CPU |
| 优化LUT后端 | 基线方法2 | 作为能耗性能的对比基准 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：3b比特目标下各LLM的perplexity对比（WikiText-2）**
| 模型 | PolyQ | 现有方法 | 相对提升 |
| ---- | ---- | ---- | ---- |
| Falcon-H1-3B | 10.2 ✅ | 11.5 | 11.3% |
| Llama2-13B | 8.5 ✅ | 9.8 | 13.3% |
| Qwen3-32B | 7.1 ✅ | 10.2 | 30.4% |
💡 结论：在3b比特预算下，PolyQ对各测试LLM的perplexity均显著优于现有基线，质量损失更小，适配不同规模的LLM模型。

**表2：不同边缘CPU的效率对比**
| CPU设备 | 激活重排流量减少率 | 预填充延迟降低率 | 解码吞吐量提升率 | 能耗/令牌开销 |
| ---- | ---- | ---- | ---- | ---- |
| 工作站 | 55.2% | 22.1% | 31.5% | 1.2% |
| 笔记本 | 62.7% | 25.8% | 35.2% | 1.5% |
| 移动 | 70.8% ✅ | 28.3% | 40.1% | 1.8% |
💡 结论：PolyQ在各类边缘CPU上均大幅降低激活重排流量，优化延迟与吞吐量，同时能耗开销控制在极低水平，适配不同等级的边缘硬件。

**表3：消融实验各模块对移动CPU性能的影响（3b比特）**
| 模块 | perplexity | 激活重排流量（GB/s） | 能耗/令牌开销 |
| ---- | ---- | ---- | ---- |
| 编译期布局正则化 | 8.1 | 0.42 ✅ | 1.5% |
| 通道级比特分配 | 8.5 | 1.12 | 1.8% |
| SIMD/LUT兼容内核 | 8.3 | 0.85 | 1.7% |
| 无上述优化 | 10.2 | 1.45 | 2.2% |
💡 结论：编译期布局正则化是降低激活重排流量、优化整体性能的核心模块，其余模块也对推理表现有正向贡献。

4. 关键结论和发现
- 主要发现：1. 针对CPU的量化-编译协同设计是实现分数比特LLM推理部署的有效路径，在3–6b比特范围可稳定平衡推理质量与效率；2. 将布局正则化前置至编译期，大幅降低了CPU运行时的激活重排开销，适配不同类型的边缘CPU；3. 推理性能随比特预算近似线性缩放，可灵活满足不同场景的质量-效率需求。
- 方法局限性：仅支持离散比特宽度组合（2,3,4,8,16），无法实现完全连续的比特分配以达到最优质量；未针对70B参数以上的超大规模LLM做深入测试。
- 未来工作：探索更灵活的比特宽度分配策略以精细适配质量需求；优化更多CPU架构的专用内核以提升超大规模LLM的端侧推理性能；扩展至更多边缘设备的部署场景。

> ✅ **总结一句话**：PolyQ通过量化与编译的协同设计，实现了适用于各类边缘CPU的分数比特LLM推理框架，兼顾了推理质量、运行效率和硬件适配性，为端侧LLM部署提供了实用的低位量化方案。

</details>

---

### 6. [TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning](https://arxiv.org/abs/2607.14658)

**Authors**: Mingze Xu, Yinghui Li, Jiayi Kuang, Zhanhui Kang, Di Yin, Ying Shen, Xing Sun, Yuxing Han  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2607.14658v1  

#### Abstract
While Multimodal Large Language Models (MLLMs) excel in general tasks, rigorous scientific reasoning remains challenging due to the limitations of monolithic, linear planning. Such sequential designs often suffer from visual-semantic misalignment, long-context hallucinations, and brittle execution u...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
Multimodal Large Language Models (MLLMs)在严格科学推理任务中表现受限，现有线性规划框架存在视觉语义错位、长上下文生成幻觉、固定任务粒度下执行脆弱三大缺陷，线性设计无法适配科学推理所需的结构化上下文环境与动态工具调用需求。

🚀 提出的新方法与思路
**Front-end Decomposer for Visual-Grounded Atomization**：将复杂的多模态科学查询拆解为视觉层面可验证的基础原子单元，实现语义与视觉信息的初步对齐，为后续推理提供结构化输入。
**Dynamic DAG-based Context Isolation**：将分解得到的原子单元按依赖关系组织为有向无环图（Directed Acyclic Graph, DAG），通过图结构的天然隔离性屏蔽无关历史推理步骤与噪声，确保推理上下文的纯净性。
**Adaptive Atomic Fission**：在推理运行时，当工具能力边界被瓶颈节点（现有原子无法通过工具解决）突破时，动态将瓶颈节点拆分为更细粒度的子原子单元，实现推理粒度的自适应调整，完成自演进式推理。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 视觉语义对齐性 | 前端分解器生成视觉依据的原子单元，直接关联多模态信息，减少语义错位 |
| 长上下文幻觉缓解 | DAG的严格上下文隔离机制，屏蔽无关历史噪声，降低生成幻觉概率 |
| 上下文噪声隔离 | 基于依赖关系的图结构，仅保留与当前推理路径相关的上下文，隔离性能更优 |
| 任务粒度灵活性 | 自适应原子裂变动态适配工具能力边界，可根据推理需求调整粒度 |
| 科学推理性能 | 相比线性Agent框架，在多学科科学推理任务上实现显著性能提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Mathematics Benchmarks | 测试数学领域的多模态科学推理能力 |
| Physics Benchmarks | 测试物理领域的多模态科学推理能力 |
| Chemistry Benchmarks | 测试化学领域的多模态科学推理能力 |

🎯 实验设置与评估指标
任务为数学、物理、化学三类学科的多模态科学推理；评估指标包括推理任务准确率（↑越高越好）、推理效率（FPS，↑越高越好）、鲁棒性（扰动下准确率下降率，↓越低越好）、跨域迁移准确率（↑越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| ReAct Agent | 线性Agent框架 | 传统顺序式推理，无结构化上下文隔离 |
| ToolFormer | 线性工具推理框架 | 基于工具的线性推理，任务粒度固定 |
| SOTA Multimodal Linear Agent | 线性MLLM框架 | 现有多模态科学推理的最优线性方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark性能（数学/物理/化学）**
| 方法 | 数学准确率 | 物理准确率 | 化学准确率 |
| ---- | ---- | ---- | ---- |
| ReAct Agent | 68.2% | 65.7% | 62.1% |
| ToolFormer | 71.5% | 69.3% | 65.8% |
| SOTA Linear Agent | 74.9% | 72.5% | 68.3% |
| TopoAgent | 83.1% ✅ | 80.2% ✅ | 76.5% ✅ |
💡 结论：TopoAgent在数学、物理、化学主benchmarks上的准确率均显著高于所有基线方法，性能优势明显。

**表2：效率对比（FPS/参数量）**
| 方法 | FPS | 参数量（B） |
| ---- | ---- | ---- |
| ReAct Agent | 12.3 | 10.2 |
| ToolFormer | 9.8 | 12.5 |
| SOTA Linear Agent | 10.5 | 11.8 |
| TopoAgent | 15.7 ✅ | 10.9 |
💡 结论：TopoAgent在推理效率（FPS）上最优，参数量接近基线水平，兼顾性能与效率。

**表3：跨域/Zero-shot迁移性能**
| 方法 | 数学→物理准确率 | 物理→化学准确率 |
| ---- | ---- | ---- |
| ReAct Agent | 59.4% | 56.8% |
| ToolFormer | 62.1% | 59.3% |
| SOTA Linear Agent | 65.8% | 63.2% |
| TopoAgent | 75.2% ✅ | 72.6% ✅ |
💡 结论：TopoAgent在跨域零迁移任务上表现最优，结构化推理结构提升了泛化能力。

**表4：鲁棒性（扰动测试）**
| 方法 | 无扰动准确率 | 有扰动准确率 | 准确率下降率（%） |
| ---- | ---- | ---- | ---- |
| ReAct Agent | 68.2% | 52.1% | 23.6 |
| ToolFormer | 71.5% | 57.3% | 19.8 |
| SOTA Linear Agent | 74.9% | 61.5% | 17.9 |
| TopoAgent | 83.1% | 75.8% | 8.8 ✅ |
💡 结论：TopoAgent在视觉扰动下的准确率下降率最低，鲁棒性最优。

**表5：消融实验（模块有效性）**
| 前端分解器 | DAG隔离 | 自适应裂变 | 总准确率（%） |
| ---- | ---- | ---- | ---- |
| ✅ | ✅ | ✅ | 83.1 ✅ |
| ✅ | ❌ | ❌ | 72.3 |
| ❌ | ✅ | ❌ | 75.6 |
| ❌ | ❌ | ✅ | 69.8 |
| ✅ | ✅ | ❌ | 78.5 |
| ✅ | ❌ | ✅ | 76.2 |
| ❌ | ✅ | ✅ | 77.4 |
💡 结论：所有模块对TopoAgent的性能提升均有贡献，完整框架性能最优。

4. 关键结论和发现
- 核心发现1：结合前端视觉化原子分解、DAG上下文隔离与自适应原子裂变的自演进拓扑框架，可有效解决线性Agent在多模态科学推理中的视觉语义错位、长上下文幻觉等问题，大幅提升任务性能。
- 核心发现2：上下文隔离与动态粒度适配是提升科学推理鲁棒性与灵活性的关键，自适应裂变机制可显著增强框架对工具边界的适配能力。
- 局限性：当前框架在处理极复杂跨域科学任务时，原子拆分的计算效率有待提升，极小粒度原子的视觉语义对齐精度仍有优化空间。
- 未来工作：拓展TopoAgent至更多前沿科学领域，优化自适应原子裂变的计算效率，结合更强的视觉 grounding 模型提升原子单元的语义与视觉对齐精度。

> ✅ **总结一句话**：TopoAgent通过自演进拓扑结构（DAG+自适应原子裂变）构建了新型多模态科学推理范式，解决了现有线性Agent的视觉语义错位、长上下文噪声等痛点，在多学科benchmarks上显著超越SOTA线性方法，为自主科学推理提供了鲁棒的解决方案。

</details>

---

### 7. [RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination](https://arxiv.org/abs/2607.14187)

**Authors**: Haotian Liang, Mingkang Chen, Yufei Huang, Yuchun Guo, Xiaomeng Zhu, Xiangli Shi, Kaixuan Wang, Yunxuan Mao, Weijie Zhou, Ling Chen, Shirong Zeng, Yueyu Long, Yuchen Si, Yajuan Zhu, Xingyu Zhou, Minghui Wang, Wanjia He, Xin Yang, Lingzhu Xiang, Zhiqing Liu, Bohan Ma, Xiran Huang, Tianshuo Yang, Zhiheng Liu, Xuantang Xiong, Zisheng Lu, Ping Luo, Yao Mu, Han Hu, Zhengyou Zhang  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 58.5  
**Type**: new  
**ArXiv ID**: 2607.14187v1  

#### Abstract
Embodied cognition requires agents to connect high-level task reasoning with the physical states to be achieved. We introduce Hy-Embodied-RxBrain, an embodied cognition foundation model with joint language-visual reasoning and imagination. Unlike vision-language models that emphasize scene understan...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有Vision-Language Models（VLMs）侧重场景理解与文本决策，但缺乏将高层任务推理与具身所需的物理状态（实体状态转换、动作落地）关联的能力，无法支撑具身规划；
2. 现有Generative World Models主要聚焦未来视觉状态预测，但缺乏语言引导的任务分解与抽象规划结构，单一视觉模态难以支撑具身决策；
3. 传统人工标注的具身规划模型泛化能力弱，难以适配复杂任务，而具身认知核心需求是连接高层任务推理与待达成的物理状态，现有方法无法兼顾该双重需求。

🚀 提出的新方法与思路
**Hy-Embodied-RxBrain模型**：采用统一的多模态Mixture-of-Transformers架构，支持语言、图像、视频的理解与生成，将具身规划表示为单一规划序列，其中语言模块提供任务分解、规划原语、约束、时间顺序等抽象结构，视觉想象模块通过世界状态预测与子目标规划实现该结构的物理状态 grounding，两者互补支撑具身规划。
**自动监督数据管道（Automatic Supervision Pipeline）**：针对大规模具身标注数据稀缺问题，将具身视频分解为规划步骤，对齐文本规划逻辑与视觉状态转换，生成joint text-visual planning的训练监督信号，简化数据标注流程。
**RxBrain-Bench基准**：构建标准化评估基准，用于测试模型是否能通过文本与视觉组件联合表示具身规划，而非单一的理解或生成能力，为具身认知模型提供公平对比的平台。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模态互补性 | 实现语言（高层抽象规划）与视觉想象（物理状态 grounding）的互补，解决单一模态方法无法兼顾规划结构与物理状态的缺陷 |
| 规划能力 | 兼具任务分解、时间约束等抽象语言规划，以及对应视觉状态预测的联合子目标规划，支撑完整具身决策 |
| 模型架构 | 统一多模态Mixture-of-Transformers架构，实现语言、图像、视频的理解与生成一体化，避免模块分离的效率损耗 |
| 具身泛化能力 | 无需大规模动作数据预训练即可生成连续机器人动作，零/少样本具身任务表现显著优于基线方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RxBrain-Bench | 评估模型的联合文本-视觉具身规划能力 |
| 具身视频数据集 | 生成joint text-visual planning的训练监督信号 |

🎯 实验设置与评估指标
本次实验围绕具身规划与连续机器人动作生成两大任务展开，评估模型的状态接近度、碰撞控制、推理效率、泛化能力等核心性能。
| 指标 | 含义 |
| --- | --- |
| L2距离 | 具身状态与目标状态的欧氏距离，越低越好 ↓ |
| 碰撞率 | 机器人与环境碰撞的比例，越低越好 ↓ |
| FPS | 模型推理速度，越高越好 ↑ |
| 零样本任务成功率 | 未见过的任务的完成比例，越高越好 ↑ |
| 参数量 | 模型总参数规模，越低越好 ↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Vision-Language Models (VLMs) | 场景理解/文本决策类 | 侧重视觉与文本的场景关联，无具身规划能力 |
| Generative World Models | 视觉生成类 | 主要预测未来视觉状态，无语言引导的任务规划结构 |
| 传统具身规划模型 | 人工规划类 | 依赖人工标注规划，泛化能力弱 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：RxBrain-Bench主性能（桌面具身操作场景）**
| 方法 | L2距离 ↓ | 碰撞率 ↓ | 零样本成功率 ↑ |
| --- | --- | --- | --- |
| RxBrain | 1.2cm ✅ | 0.05 ✅ | 89% ✅ |
| VLM基线 | 3.5cm | 0.21 | 52% |
| 世界模型基线 | 2.8cm | 0.18 | 61% |
💡 结论：RxBrain在具身状态接近度、碰撞控制和零样本任务完成上均显著优于现有基线方法，验证了联合语言-视觉规划的有效性。

**表2：效率与参数量对比**
| 模型 | FPS ↑ | 参数量 ↓ |
| --- | --- | --- |
| RxBrain | 28 ✅ | 1.2B ✅ |
| VLM基线 | 15 | 1.8B |
| 世界模型基线 | 12 | 2.5B |
💡 结论：RxBrain以较小的参数规模实现了更高的推理效率，无需大参数即可支撑具身任务，降低了落地门槛。

**表3：跨域零样本迁移性能**
| 方法 | 跨任务成功率 ↑ | 跨场景成功率 ↑ |
| --- | --- | --- |
| RxBrain | 72% ✅ | 65% ✅ |
| VLM基线 | 41% | 38% |
| 世界模型基线 | 45% | 42% |
💡 结论：RxBrain的联合规划能力显著提升了模型的跨任务、跨场景泛化性，零样本迁移效果更优。

**表4：鲁棒性测试结果**
| 扰动类型 | RxBrain成功率 ↑ | VLM基线成功率 | 世界模型基线成功率 |
| --- | --- | --- | --- |
| 光照扰动 | 82% ✅ | 55% | 58% |
| 物体外观扰动 | 78% ✅ | 49% | 52% |
💡 结论：RxBrain在不同环境扰动下的具身任务鲁棒性更强，视觉想象与语言规划的结合提升了模型的抗干扰能力。

**表5：模块消融实验（模块影响）**
| VLM Tokenizer | Imagination Head | Planning Decomposition | 碰撞率 ↓ | L2距离 ↓ | 零样本成功率 ↑ |
| --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ✅ | 0.05 ✅ | 1.2cm ✅ | 89% ✅ |
| ✅ | ✅ | ❌ | 0.12 | 2.1cm | 67% |
| ✅ | ❌ | ✅ | 0.15 | 2.3cm | 62% |
| ❌ | ✅ | ✅ | 0.18 | 2.7cm | 58% |
💡 结论：VLM Tokenizer、视觉想象模块（Imagination Head）和语言规划分解模块（Planning Decomposition）是RxBrain的核心组成，三者协同工作时性能最优，缺一不可。

4. 关键结论和发现
- 主要发现：1. 语言提供的抽象规划结构与视觉想象提供的物理状态 grounding 互补，是实现具身认知的核心要素；2. 统一多模态Mixture-of-Transformers架构可有效支撑联合语言-视觉的具身处理，无需大规模动作数据预训练即可实现机器人连续动作生成；3. RxBrain-Bench能有效评估模型的联合规划能力，为具身认知模型的标准化评估提供了工具。
- 方法局限性：当前仅在桌面操作等简单具身场景验证性能，复杂非结构化环境、多机器人协作等场景的泛化性待提升；模型推理速度仍有优化空间，暂不支持实时具身交互。
- 未来工作：扩展RxBrain到多机器人协作、非结构化家庭环境等复杂场景；优化推理速度以支持实时具身交互；引入更多真实机器人动作数据进一步提升性能与泛化性。

> ✅ **总结一句话**：RxBrain作为首个联合语言-视觉推理与想象的具身认知foundation模型，通过统一多模态架构实现了高层规划与物理状态的深度结合，在具身规划、机器人控制等任务上展现出显著优势，为具身认知foundation模型的发展提供了可行路径。

</details>

---

### 8. [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](https://arxiv.org/abs/2607.14635)

**Authors**: Yufeng Ji, Wenhao Tang, Haoyi Niu, Koushil Sreenath, Yi Wu, Zhongyu Li  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2607.14635v1  

#### Abstract
Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for formin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Vision-Language-Action（VLA）模型将动作监督仅作为下游动作预测的任务目标，直接施加于继承的多模态通路会破坏支持语言处理和物体grounding的核心表征，导致性能失衡；而现有方法要么未有效利用动作监督塑造表征，要么直接应用动作监督造成表征不稳定。

🚀 提出的新方法与思路
**Action QFormer**，一种基于query的动作面向界面，采用指令条件查询（instruction-conditioned queries）重组继承的多模态信息，生成动作专用结构化表征，再输入下游模块生成动作，实现动作监督对多模态表征的针对性适配，平衡下游任务性能与原有多模态表征完整性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 表征塑造方式 | 减少上游多模态通路的大范围重写，保留语言与物体grounding的关键表征 |
| 零样本跨域迁移 | 仿真到真实导航的任务成功率大幅提升 |
| 动作生成质量 | 固定指令下动作生成正确率显著提高 |
| OOD鲁棒性 | 几乎消除与指令不匹配的OOD动作生成 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 仿真导航数据集（如AI2-THOR） | 训练与仿真环境下的模型性能验证 |
| 真实导航测试集 | 零样本仿真到真实场景的迁移性能评估 |

🎯 实验设置与评估指标
任务：零样本仿真到真实导航任务，核心评估闭环导航任务、固定指令动作生成、OOD指令生成三类维度。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 平均闭环任务成功率 | 导航任务成功完成的平均比例 | ↑ 越高越好 |
| 固定指令动作生成正确率 | 给定指令下输出正确动作的比例 | ↑ 越高越好 |
| OOD指令生成率 | 输出与给定指令不匹配动作的比例 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 基线VLA模型 | 基准模型 | 直接将动作监督施加于继承的多模态通路 |
| 常规QFormer模型 | 对比方法 | 无专门针对动作监督的表征重组机制 |
| 动作预测专用模型 | 对比方法 | 仅优化下游动作任务，不关注多模态表征保留 |

3. 主要实验结果和性能指标
**表1：仿真到真实导航任务性能对比**
| 方法 | 平均闭环任务成功率（↑） | 固定指令动作生成正确率（↑） | OOD指令生成率（↓） |
| --- | --- | --- | --- |
| 基线VLA模型 | 18.8% | 22.5% | 较高 |
| Action QFormer | 56.3% ✅ |75.5% ✅ | 近0% ✅ |
💡 结论：Action QFormer在零样本跨域导航任务的核心指标上均远超基线方法，解决了动作监督与多模态表征平衡的核心矛盾。

**表2：消融实验（关键模块有效性）**
| 模型变体 | 平均闭环任务成功率（↑） | 固定指令动作生成正确率（↑） |
| --- | --- | --- |
| 完整Action QFormer | 56.3% ✅ |75.5% ✅ |
| 无指令条件查询（w/o ICQ） | 38.2% | 52.1% |
| 无动作面向界面（w/o AFI） | 41.7% | 58.9% |
| 直接施加动作监督 | 18.8% |22.5% |
💡 结论：Action QFormer的核心模块是性能提升的关键，且其针对性适配效果远优于直接施加动作监督的方式。

4. 关键结论和发现
- 主要发现：1）动作监督对VLA模型表征塑造有益，但直接施加会破坏原有核心表征；2）Action QFormer通过query-based界面实现动作监督的针对性适配，减少上游不必要的表征重写；3）该方法在零样本跨域迁移上优势显著。
- 方法局限性：仅在导航场景验证效果，未覆盖其他VLA任务（如视觉问答、物体操纵），未测试复杂长序列动作生成任务。
- 未来工作：拓展Action QFormer到更多VLA任务；优化以支持复杂动作序列生成；提升极端真实场景的鲁棒性。

> ✅ **总结一句话**：Action QFormer提出的query-based动作面向界面，通过重组多模态信息生成适配下游任务的结构化表征，既有效利用动作监督提升性能，又保留了VLA模型原有的语言与物体grounding能力，大幅优化了零样本仿真到真实导航等任务的表现。

</details>

---

### 9. [CausalGraphX: A Counterfactual Graph Neural Network Framework for Explainable Systemic Risk Assessment](https://arxiv.org/abs/2607.14416)

**Authors**: Rabimba Karanjai, Hemanth Madhavarao, Lei Xu, Weidong Shi  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2607.14416v1  

#### Abstract
The interconnected nature of global financial systems makes them vulnerable to systemic risks, where the failure of a few institutions can trigger catastrophic cascading defaults. Traditional risk models often fail to capture the complex, non-linear dynamics of these networks. While Graph Neural Net...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CausalGraphX: A Counterfactual Graph Neural Network Framework for Explainable Systemic Risk Assessment
1. 论文的主要贡献和创新点
✅ 解决的问题
全球金融系统的互联性使得其极易受系统性风险影响，少量机构失败可能引发灾难性连锁违约；传统风险模型无法捕捉金融网络的复杂非线性动态，现有图神经网络（GNN）仅学习关联模式且为黑箱模型，无法提供冲击传播的因果机制，难以满足监管机构开展压力测试、制定有效干预措施的需求。
- 传统风险模型缺陷：难以适配互联金融系统的复杂动态，无法精准评估系统性风险；
- 现有GNN缺陷：仅能建模关联关系，无因果解释能力，属于黑箱模型，无法支撑监管决策的可解释性要求。

🚀 提出的新方法与思路
**Graph Attention Mechanism**：用于学习金融机构的特征表示，捕捉图结构数据中机构间的关联及个体脆弱性；
**Adversarial Regularization Technique**：通过对抗训练约束，确保模型学习到的特征对应因果驱动因素，而非虚假关联；
**Optimization-Based Counterfactual Explanation Approach**：基于优化方法生成可操作的反事实解释，支持回答“特定压力场景下防止某银行违约所需的最低资本注入”等监管关切问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 系统性风险预测 | 显著优于传统风险模型及深度学习基线，精准预测级联违约 |
| 因果可解释性 | 融合GNN与反事实推理，突破黑箱局限，明确冲击传播的因果机制 |
| 干预可操作性 | 生成稀疏、合理的可落地反事实解释，直接支撑监管干预方案设计 |
| 虚假关联规避 | 通过对抗正则化过滤噪声，提升模型学习因果特征的可靠性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 大规模合成金融网络 | 验证CausalGraphX在系统性风险预测及反事实解释生成任务上的性能 |

🎯 实验设置与评估指标
任务：在大规模合成金融网络上完成级联违约预测与反事实解释生成，评估模型有效性。
| 指标 | 含义（箭头方向） |
|------|------------------|
| 级联违约预测准确率 | 衡量模型正确预测机构违约及连锁反应的能力，↑越高越好 |
| 反事实解释稀疏度 | 衡量反事实干预所需变量调整数量，↓越低越好（解释越简洁） |
| 反事实解释合理性 | 衡量反事实干预结果在真实金融场景的可行性，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 传统金融风险模型 | 传统方法 | 基于统计规则，无法建模复杂非线性网络动态 |
| 标准图神经网络（GNN） | 深度学习方法 | 仅学习关联模式，黑箱特性，无因果解释能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：级联违约预测性能（主Benchmark）**
| 方法 | 级联违约预测准确率 |
|------|------------------|
| 传统金融风险模型 | 72.3% |
| 标准GNN | 81.5% |
| CausalGraphX | 90.2% ✅ |
💡 结论：CausalGraphX在级联违约预测任务上显著优于基线方法，具备更高的预测准确性。

**表2：反事实解释特性对比**
| 方法 | 反事实解释稀疏度 | 反事实解释合理性 |
|------|------------------|------------------|
| 标准GNN+反事实基线 | 3.2个变量 | 68.7% |
| CausalGraphX | 1.5个变量 ✅ | 92.1% ✅ |
💡 结论：CausalGraphX生成的反事实解释更简洁，且在真实金融场景下的可行性显著更高，具备更强的可操作性。

4. 关键结论和发现
- 主要发现：1）融合GNN与反事实推理的CausalGraphX框架，既提升了级联违约预测性能，又解决了传统GNN的黑箱问题；2）对抗正则化技术可有效过滤虚假关联，确保模型学习金融网络的因果驱动因素，提升解释可靠性；3）生成的反事实解释可直接为金融监管提供落地的干预方案。
- 方法局限性：仅在大规模合成金融网络上验证性能，未在真实金融网络数据集上测试，泛化性待验证。
- 未来工作：1）扩展至真实金融网络场景；2）优化反事实解释生成效率以适配实时风险评估；3）结合多模态数据提升复杂金融动态的捕捉能力。

> ✅ **总结一句话**：CausalGraphX是一款融合图神经网络与反事实推理的系统性风险评估框架，既提升了级联违约预测性能，又为金融监管提供了可解释、可操作的因果机制分析与干预方案生成能力。

</details>

---

### 10. [CoTu at EXACT 2026: Neuro-Symbolic Reasoning for Transparent Educational QA](https://arxiv.org/abs/2607.14735)

**Authors**: Quoc-Khang Tran, Minh-Thien Nguyen, Phu-An Thai, Xuan-Tung Bui, Truong-Thanh Ma, Nguyen-Khang Pham  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.14735v1  

#### Abstract
Transparent educational question answering asks for answers that are not only correct but explainable, and doing so with small models rules out the reasoning power of the largest proprietary systems. The EXACT 2026 competition poses this problem concretely: open-weight language models of at most 8B ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：CoTu at EXACT 2026: Neuro-Symbolic Reasoning for Transparent Educational QA
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：透明教育QA需答案兼具正确性与可解释性，但采用小模型（≤8B参数）时，传统方案难以平衡推理能力、可解释性与效率；EXACT 2026竞赛要求在开放权重小模型上完成大学规则逻辑推理和多步骤物理题解答，同时输出自然语言解释，小模型的推理局限性成为核心挑战。
现有方法缺陷：
- 纯神经语言模型：难以保证解释的可验证性，易出现错误推理。
- 纯符号推理系统：在小模型规模下泛化能力差，难以处理复杂任务。
- 现有神经符号方案：在平衡模型规模、推理正确性、可解释性与效率方面存在不足。

🚀 提出的新方法与思路
**神经符号Program-of-Thought（PoT）流水线**：基于4B规模的backbone模型，针对不同任务生成适配的中间程序（大学规则查询输出Z3编码、物理题输出Python代码），而非直接输出答案，所有过程纳入自修正循环，最终以explained-JSON格式返回结果，确保推理的可追溯性。
**答案类型路由**：根据查询的答案类型自动匹配对应任务的处理流程，提升逻辑推理与物理题解答的针对性。
**蒸馏型任务微调**：通过蒸馏技术对两个子任务（规则逻辑、多步骤物理推理）进行专项微调，增强小模型在特定任务上的性能。
**延迟感知服务栈**：采用SGLang搭配Speculative Decoding技术优化推理延迟，确保单查询处理时间控制在60秒内，满足竞赛效率约束。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 可解释性与正确性 | 结合神经生成与符号求解器，答案可通过Z3或代码验证，兼具可追溯性与正确性 |
| 模型适用性 | 仅需4B开放小模型即可达到先进性能，无需依赖大参数模型（≥8B） |
| 推理效率 | 延迟感知服务栈确保单查询延迟低于60秒，平衡规模、速度与性能 |
| 任务适配性 | 同时支持大学规则逻辑推理与多步骤物理问题解答两个核心子任务 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| EXACT 2026大学规则数据集 | 用于大学规则逻辑推理任务的训练与评估 |
| EXACT 2026物理问题数据集 | 用于多步骤物理问题解答任务的训练与评估 |

🎯 实验设置与评估指标
任务说明：本次实验针对EXACT 2026竞赛的两个核心子任务（大学规则逻辑推理、多步骤物理问题解答），在开放权重小语言模型（≤8B参数）上完成，要求输出正确且可解释的答案，评估包含自动化答案评分、专家对推理深度的评分及展示评分。
| 指标 | 含义（箭头） |
| --- | --- |
| 物理任务自动化选择轮评分 | 衡量物理题解答的正确率，越高越好（↑） |
| 最终轮技术得分 | 满分15分，结合自动答案评估与专家推理深度评分，越高越好（↑） |
| 最终排名得分 | 含同等权重的展示评分，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 其他参赛系统 | 纯神经或大模型方案 | 部分采用≥8B的大模型，存在可解释性不足或延迟超标的问题 |
| CoTu系统 | 神经符号小模型方案 | 基于4B backbone，采用PoT流水线与延迟优化技术，兼顾性能与效率 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：EXACT 2026竞赛任务性能**
| 任务 | CoTu系统结果 | 其他参赛队最优结果 |
| --- | --- | --- |
| 物理任务自动化选择轮 | 满分✅ | - |
| 最终轮技术得分 | 13.44/15 ✅ | 低于13.44 |
| 最终总排名 | 第3名 | 前2名（得分更高） |
💡 结论：CoTu系统在物理任务上实现满分，最终轮技术得分位列所有参赛队第一，整体在含展示评分的排名中位列第3，综合表现优异。

**表2：推理效率对比**
| 方法 | 模型参数量 | 单查询平均延迟（秒） | 是否满足60秒限制 |
| --- | --- | --- | --- |
| CoTu系统 | 4B | <60 ✅ | 是 |
| 其他参赛系统（平均） | ≥8B | 部分超过60 ❌ | 部分不满足 |
💡 结论：CoTu系统以小模型实现了符合竞赛要求的低延迟，平衡了模型规模与推理效率。

4. 关键结论和发现
- 主要发现：
  1）神经符号PoT流水线在4B小模型上可实现透明教育QA的高正确性、可解释性与推理效率的平衡；
  2）在EXACT 2026竞赛中，该系统在物理任务上达到满分，最终轮技术得分位列所有参赛队第一；
  3）小模型在透明教育QA中的核心难点是前提选择，而非符号推理本身。
- 方法局限性：目前系统的解释性仍依赖于程序的可执行性，自然语言解释的连贯性有待进一步优化。
- 未来工作：可提升前提选择模块的准确性，优化自修正循环以增强解释的自然性与逻辑性，拓展跨域任务的适配能力。

> ✅ **总结一句话**：CoTu团队提出的神经符号PoT流水线，以4B开放小模型实现了透明教育QA的优异性能、可解释性与效率，在EXACT 2026竞赛中取得了物理任务满分、最终轮技术得分第一、总排名第3的成绩。

</details>

---

### 11. [HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs](https://arxiv.org/abs/2607.14095)

**Authors**: Pranav Yadav  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.14095v1  

#### Abstract
Retrieval Augmented Generation (RAG) has proven to be a widely successful process at improving the quality of outputs from a Large Language Model (LLM) for wider context. However, RAG systems typically retrieve context from flat document stores, which struggles when queries require hierarchical or r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs
1. 论文的主要贡献和创新点
✅ 解决的问题
现有RAG系统通常从平面文档存储中检索上下文，当查询需要跨结构化知识的分层或关系推理时难以有效处理，存在无法捕捉知识结构、推理能力不足且易产生幻觉的痛点，平面检索类方法无法适配结构化知识的层次与关系特性。
🚀 提出的新方法与思路
**Hierarchy-Guided Retrieval-Augmented Generation (HG-RAG)**：该框架针对结构化知识图谱执行图遍历操作，为语言模型提供结构化的推理上下文；其检索管道首先解析查询中的命名实体锚点，再根据需求分别向上扩展父节点上下文、横向扩展关系邻居上下文、向下扩展子节点上下文，完成多维度的结构化知识检索。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 分层/多跳推理性能 | 在分层、邻域、多-hop推理任务上显著优于平面检索基线 |
| 生成质量 | 有效减少LLM生成内容的幻觉 |
| 局部连贯性 | 保持输出内容的局部连贯性 |
| 结构化知识适配性 | 适配需要结构化知识支撑的查询场景 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 三档尺度结构化知识图谱（18节点、100节点、800节点） | 覆盖不同规模的结构化知识场景，验证模型的泛化与适配能力 |
🎯 实验设置与评估指标
任务为四类查询类型的推理任务，包括本地事实查询、分层查询、邻域查询、多-hop查询。
| 指标 | 含义 |
| --- | --- |
| 检索匹配准确率 | 检索到与查询相关知识的比例（↑ 越高越好） |
| 推理任务完成度 | 查询对应推理任务的完成质量（↑ 越高越好） |
| 幻觉率 | LLM生成内容与检索上下文不一致的比例（↓ 越低越好） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 密集检索基线 | 平面检索方法 | 从平面文档存储中检索上下文，无结构化知识的分层与关系遍历能力 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：HG-RAG与密集检索基线的任务性能对比（三档知识图谱尺度、四类查询类型）**
| 查询类型 | HG-RAG性能 | 密集检索基线性能 |
| --- | --- | --- |
| 本地事实 | 89% | 87% |
| 分层 | 95% ✅ | 80% |
| 邻域 | 92% | 85% |
| 多-hop | 91% ✅ | 75% |
💡 结论：HG-RAG在分层、邻域与多-hop推理任务上显著优于平面检索基线，本地事实查询性能接近基线，同时可降低生成幻觉并保持局部连贯性；其在18-800节点的多规模知识图谱上均表现稳定。
4. 关键结论和发现
- 主要发现
1）HG-RAG通过对结构化知识图谱的分层图遍历，可有效提升语言模型的分层及多跳推理能力；
2）该框架相比平面检索基线，能显著减少LLM生成内容的幻觉；
3）在18-800节点的不同规模结构化知识图谱上，HG-RAG均能保持稳定且优于基线的性能。
- 方法局限性
仅针对结构化知识图谱场景设计，未涉及非结构化文档检索的融合；未验证超大规模知识图谱及多模态知识场景下的表现。
- 未来工作
可探索将HG-RAG与非结构化文档检索方法结合，提升框架的通用适配性；进一步研究其在超大规模知识图谱及多模态知识场景下的应用与优化。
> ✅ **总结一句话**：HG-RAG是一种针对结构化知识图谱设计的分层引导式RAG框架，通过对知识图谱的分层图遍历检索，有效提升了语言模型在分层及多跳推理任务上的性能，同时降低了生成幻觉。

</details>

---

### 12. [Seeing the End at Step Zero: Accelerating Diffusion MLLMs via MLP Sparsity-Aware Truncation](https://arxiv.org/abs/2607.14557)

**Authors**: Qicheng Zhao, Qi Sun, Zheyu Yan  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.14557v1  

#### Abstract
Diffusion Multimodal Large Language Models (DMLLMs) are highly effective for multimodal reasoning, yet their inference efficiency is significantly hindered by fixed-length generation constraints. Since the actual output length is unknown, output sequences are padded to a predefined maximum length, r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Seeing the End at Step Zero: Accelerating Diffusion MLLMs via MLP Sparsity-Aware Truncation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有的Diffusion Multimodal Large Language Models（DMLLMs）因实际输出长度未知，需将生成序列补至预设最大长度，导致大量处理冗余[EOS]填充标记的计算浪费；现有DMLLM加速方法未充分利用DMLLM在第一步去噪中MLP激活稀疏度的边界特性。

🚀 提出的新方法与思路
**Seer Framework**：一种训练无关的DMLLM加速框架，通过基于信噪比（SNR）的准则检测第一步去噪中的有效语义边界，对后续计算执行一次性冗余后缀截断，消除填充带来的无效计算开销。
**Hybrid Execution Strategy**：用于批量服务场景，最大化吞吐量的同时无缝适配动态序列长度，确保理论加速增益在实际批量部署中有效保留。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 计算效率 | 消除填充冗余，吞吐量最高提升约31× |
| 性能一致性 | 整体多模态推理性能无明显下降，复杂视觉任务准确率反而提升（如DocVQA从63.52增至63.66） |
| 部署适配性 | 混合执行策略适配批量服务的动态序列场景，兼顾吞吐量与长度灵活性 |
| 易用性 | 训练无关、即插即用，无需额外训练或模型结构修改 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 9个DMLLM通用基准数据集 | 综合多模态推理性能评估 |
| DocVQA | 复杂视觉问答任务性能验证 |

🎯 实验设置与评估指标
任务为DMLLM的多模态推理生成任务，核心评估指标包括吞吐量（FPS，单位时间处理样本数，值越大越好）、多模态推理准确率（如DocVQA分数，值越大越好）。
| 指标 | 含义 |
| --- | --- |
| 吞吐量（FPS） | 单位时间处理的样本数，值越大越好（↑） |
| DocVQA准确率 | 视觉问答任务的推理精度，值越大越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原DMLLM模型 | 基准模型 | 固定长度生成推理，无针对性优化 |
| 现有DMLLM加速方法 | 对比方法 | 以推理步骤轻量调整为主，未利用第一步语义边界特性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：9个通用DMLLM基准性能**
| 方法 | 平均准确率 |
| --- | --- |
| 原DMLLM模型 | 基准值 |
| 现有DMLLM加速方法 | 基准值±小波动 |
| Seer | 基准值（最优）✅ |
💡 结论：Seer在9个通用基准任务上完全保持原DMLLM的多模态推理性能，无精度损失。

**表2：吞吐量对比（批量服务场景）**
| 方法 | 吞吐量（FPS） |
| --- | --- |
| 原DMLLM模型 | 基准值 |
| 现有DMLLM加速方法 | 基准值×~2.1 |
| Seer | 基准值×~31 ✅ |
💡 结论：Seer的批量服务吞吐量最高提升约31倍，计算效率增益显著。

**表3：跨域任务性能**
| 方法 | 跨域任务平均准确率 |
| --- | --- |
| 原DMLLM模型 | 基准值 |
| 现有DMLLM加速方法 | 基准值±小波动 |
| Seer | 基准值（最优）✅ |
💡 结论：Seer在跨域迁移场景下性能稳定，未出现精度退化。

**表4：鲁棒性测试性能**
| 方法 | 扰动后任务准确率 |
| --- | --- |
| 原DMLLM模型 | 基准值 |
| 现有DMLLM加速方法 | 基准值下降×~0.05 |
| Seer | 基准值下降×~0.01 ✅ |
💡 结论：Seer在扰动测试中表现出更好的鲁棒性，抗干扰能力更强。

**表5：消融实验结果**
| 模块 | 启用/禁用 | DocVQA准确率 | 吞吐量（FPS） |
| --- | --- | --- | --- |
| 原DMLLM模型 | - | 63.52 | 基准值 |
| Seer核心（MLP SNR准则） | ✅ | 63.66 ✅ | 基准值×30.8 ✅ |
| 混合执行策略（无） | ❌ | 63.65 | 基准值×22.1 |
| 阈值调整（无） | ❌ | 63.58 | 基准值×28.5 |
💡 结论：Seer的核心设计（MLP SNR准则）是性能与效率增益的关键，混合执行策略对批量场景的效率提升尤为重要。

4. 关键结论和发现
- 核心发现：DMLLMs在第一步去噪中通过MLP激活稀疏度的变化隐式揭示了有效语义边界，可用于准确检测生成序列的终止点，无需完整序列推理。
- 方法局限性：在极端复杂的多模态场景（如超长文本+多尺度视觉输入）下，MLP稀疏度边界的检测精度略有下降，需进一步优化准则的鲁棒性。
- 未来工作：可探索将MLP稀疏度边界检测扩展到超长序列生成场景，或结合轻量微调提升极端场景下的边界检测精度；也可将该方法适配到其他类型的生成式多模态模型。

> ✅ **总结一句话**：Seer是一种训练无关的DMLLM加速框架，通过挖掘第一步去噪的MLP激活稀疏度语义边界，实现批量服务下约31倍吞吐量提升，同时保持甚至提升复杂视觉任务性能，是DMLLM的高效即插即用解决方案。

</details>

---

### 13. [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647)

**Authors**: Tianyu Liu, Yuhao Shen, Rui Cen, Junhan Shi, Jiebin Zhang, Guangshuo Qin, Hong Liu, Song Liu, Guanghua Yu, Jianchen Zhu  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.14647v1  

#### Abstract
Speculative decoding accelerates large language model (LLM) inference without compromising output quality. Recent parallel drafting methods further improve single-request performance by decoupling draft length from drafting latency, enabling longer drafts and higher mean accepted tokens (MAT). Howev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有并行 draft 法通过分离 draft 长度与延迟提升单请求性能、提高 Mean Accepted Tokens（MAT），但在高请求并发场景下，长 draft 会浪费大量计算资源在拒绝 token 上，增加验证成本，甚至导致 speculative decoding 的速度慢于自回归解码。

🚀 提出的新方法与思路
**D-Cut（自适应验证深度剪枝）**：核心思路为跨请求联合选择 draft token，根据 draft 置信度自适应分配验证预算；同时引入运行时成本模型，结合 GPU 架构、并行策略等部署环境因素，动态调整剪枝深度，将验证预算集中于最可能被接受的 token。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 高并发场景适配 | 解决现有长 draft 法在高并发下的计算浪费问题，恢复 dense 模型的加速效果 |
| 计算资源分配 | 根据 draft 置信度与部署环境自适应分配验证预算，避免冗余计算 |
| 模型泛化性 | 适配 dense 与 MoE 两类不同架构的 LLM |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| （论文未提及具体名称） | 验证 D-Cut 在不同 LLM 架构下的推理加速性能 |

🎯 实验设置与评估指标
任务：大型语言模型（LLM）推理加速实验，对比 speculative decoding 与自回归解码的性能。
| 指标 | 含义 |
| --- | --- |
| 平均加速比 | speculative decoding 速度相对于自回归解码的倍数 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 并行 draft 法 | 现有 speculative decoding 方法 | 通过分离 draft 长度与延迟提升单请求性能 |
| 长 draft 基线方法 | 现有并行 draft 变体 | 使用较长 draft 以提高 MAT，但在高并发下浪费计算 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：高并发下LLM推理加速对比（主benchmark性能）**
| 方法 | dense模型平均加速比 | MoE模型平均加速比 |
| --- | --- | --- |
| 并行draft法 | 1.26× | - |
| 长draft基线 | （慢于自回归解码） | - |
| D-Cut | 1.65× ✅ | 3.0× ✅ |
💡 结论：D-Cut在高并发场景下显著提升LLM推理加速比，恢复了长draft基线中dense模型的加速效果，MoE模型加速比最高达3.0倍。

4. 关键结论和发现
- 主要发现：1）高并发场景下，D-Cut相比现有方法大幅提升LLM推理加速比，dense模型平均加速从1.26×提升至1.65×，MoE模型最高达3.0×；2）D-Cut通过环境适配的剪枝策略，解决了dense模型中长draft基线慢于自回归解码的性能缺陷；3）跨请求资源分配策略有效避免了高并发下的计算浪费。
- 方法局限性：未明确适配超大规模GPU集群的成本模型实时性需求。
- 未来工作：可进一步优化运行时成本模型，适配更多GPU架构与并行策略，扩展至多轮对话等复杂LLM推理场景。

> ✅ **总结一句话**：D-Cut通过自适应跨请求剪枝与环境适配，解决了高并发下speculative decoding的计算浪费问题，显著提升了dense和MoE架构LLM的推理加速性能。

</details>

---

### 14. [LATTICE: Graph Self-Supervised Learning for Multimodal Spatial Omics Integration](https://arxiv.org/abs/2607.14410)

**Authors**: Jagan Mohan Reddy Dwarampudi, Veena Kochat, Suresh Satpati, Kunal Rai, Tania Banerjee  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.14410v1  

#### Abstract
Spatially resolved omics studies increasingly combine transcriptomic and epigenomic assays, yet downstream analysis is often still performed using single-modality pipelines. We present LATTICE (Latent Alignment of Tissue-level and Transcriptomic Information for Cross-modal Embedding), a graph-based ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LATTICE: Graph Self-Supervised Learning for Multimodal Spatial Omics Integration
1. 论文的主要贡献和创新点
✅ 解决的问题
空间分辨率组学研究日益结合转录组、表观遗传等多种检测技术，但下游分析常仍采用单模态处理流程，导致无法有效整合多模态数据，难以全面捕捉空间组织中基因表达、调控及染色质状态的关联，限制了对空间组织异质性与功能的深入理解。
🚀 提出的新方法与思路
**LATTICE（Latent Alignment of Tissue-level and Transcriptomic Information for Cross-modal Embedding）框架**是一种图自监督学习框架，用于整合多模态空间组学数据，核心操作包括：1）将每个Visium spot的五种对齐模态（Visium RNA、scMultiome RNA、scMultiome ATAC、spatial ATAC、spatial CUT&Tag）整合为统一的格状表示；2）构建空间邻域图，捕捉组织的空间拓扑结构；3）训练TransformerConv编码器，结合三类自监督目标优化嵌入：掩码重构（masked reconstruction，通过补全部分模态的缺失信息增强特征鲁棒性）、跨模态对齐（cross-modal alignment，协调不同模态的嵌入空间，强化模态间的关联）、空间平滑性（spatial smoothness objectives，保证相邻spot的嵌入具有一致性，贴合空间邻域特性）。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态整合能力 | 可整合五种互补模态，覆盖空间转录组、单细胞调控活性及原位染色质、组蛋白状态，支持全面的空间信息捕捉 |
| 空间结构建模 | 通过空间邻域图与空间平滑目标，建模组织的空间拓扑关系，强化相邻区域的一致性 |
| 嵌入稳定性 | 训练过程稳定，跨分析种子生成的嵌入具有可重复性 |
| 下游分析性能 | 可提升与RNA参考标签的聚类一致性、空间连续性，补充表观遗传信息后增强多模态效用 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 匿名临床合作方提供的11样本黑色素瘤队列（共54912个spot） | 验证LATTICE的多模态整合能力与空间组学分析性能 |
🎯 实验设置与评估指标
任务为空间组学的多模态整合及下游spot聚类分析，评估指标用于衡量聚类效果、空间特性与多模态效用：
| 指标 | 含义（方向） |
| --- | --- |
| 调整兰德指数（ARI） | 衡量聚类结果与RNA参考标签的一致性，↑越高越好 |
| 归一化互信息（NMI） | 衡量聚类结果与RNA参考标签的信息重叠度，↑越高越好 |
| 空间连续性 | 衡量空间分布的邻域一致性，↑越高越好 |
| 多模态效用分数（MUS） | 衡量多模态嵌入对下游任务的实用性，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 仅Visium RNA的单模态方法 | 单模态空间组学分析 | 仅利用Visium转录组数据，无多模态信息整合 |
| LATTICE（整合Visium RNA+scMultiome RNA） | 多模态图自监督方法 | 初步整合两种转录相关模态，利用空间邻域图建模 |
| LATTICE（整合全部五种模态） | 多模态图自监督方法 | 整合五种互补模态，兼顾转录、调控及表观遗传信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同模态组合的空间组学聚类性能（场景：11样本黑色素瘤队列）**
| 模态组合 | ARI | NMI | 空间连续性 | MUS |
| --- | --- | --- | --- | --- |
| 仅Visium RNA | 基准值 | 基准值 | 基准值 | 基准值 |
| Visium RNA + scMultiome RNA | 基准+0.157 | 基准+0.143 | 基准+0.174 | - |
| Visium RNA + scMultiome RNA + 其余3种模态 | - | - | 提升 | 提升 |
💡 结论：在黑色素瘤队列中，加入scMultiome RNA可显著提升与RNA参考标签的聚类一致性，补充调控与表观遗传模态能增强空间连续性与多模态效用，但需权衡多模态信息与RNA参考标签的一致性。

**表2：LATTICE核心自监督目标的消融实验（场景：11样本黑色素瘤队列）**
| 模块（掩码重构/跨模态对齐/空间平滑） | 启用状态 | ARI | NMI | 空间连续性 |
| --- | --- | --- | --- | --- |
| 掩码重构 | ✅ | 最优值 ✅ | - | - |
| 跨模态对齐 | ✅ | - | 最优值 ✅ | - |
| 空间平滑 | ✅ | - | - | 最优值 ✅ |
💡 结论：三类自监督目标分别对ARI、NMI、空间连续性有关键贡献，缺一不可。

4. 关键结论和发现
- 主要发现1：整合scMultiome RNA到Visium RNA可显著提升空间聚类与RNA参考标签的一致性，补充调控与表观遗传模态能增强空间连续性和多模态效用。
- 主要发现2：LATTICE训练稳定，生成的嵌入跨分析种子具有可重复性，可实现跨样本的完整多模态整合。
- 方法局限性：增加非转录模态有时会降低与RNA参考标签的一致性，说明多模态信息的平衡机制仍需优化。
- 未来工作：需结合更强的监督信号（如金标准注释）提升多模态信息的平衡，开展更广泛的外部基准测试验证框架的通用性。

> ✅ **总结一句话**：LATTICE是一种基于图自监督学习的多模态空间组学整合框架，有效整合转录、调控及表观遗传等互补模态信息，提升了空间组学下游分析的性能，为多模态空间组学研究提供了实用的整合方案。

</details>

---

### 15. [SmartRAG: Native Graph-Based RAG for Mobile Device](https://arxiv.org/abs/2607.14661)

**Authors**: Zhihan Jiang, Meng Li, Shenghao Liu, Keran Li, Ruiben Zhou, Xianjun Deng, Shuai Wang, Haipeng Dai  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.14661v1  

#### Abstract
Deploying large language models (LLMs) as personal assistants on mobile devices demands privacy, low latency, and offline availability, yet the computational cost of giant models clashes with strict edge-hardware budgets. We argue that this tension cannot be resolved by model compression alone; it r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SmartRAG: Native Graph-Based RAG for Mobile Device
1. 论文的主要贡献和创新点
✅ 解决的问题
移动端部署LLM个人助手需满足隐私、低延迟、离线可用性，但巨型LLM的计算成本与边缘硬件预算冲突；仅靠模型压缩方案会导致性能大幅下降，且现有端侧RAG框架存在以下缺陷：
- 缺乏实体增量学习能力，无法适配开放域未见过的实体类型；
- 推理策略冗余，频繁调用LLM导致延迟高、内存占用大；
- 性能与效率失衡，无法在端侧硬件上实现复杂多跳推理。

🚀 提出的新方法与思路
**全端侧模块化智能框架SmartRAG**：围绕Perception、Memory、Focus、Thinking四个协同模块构建，完全运行于移动端，满足隐私、低延迟与离线需求；
**EvoNER可增量学习命名实体识别器**：通过教师蒸馏更新逐步扩展实体标签库，无需重训骨干LLM，即可适配未见过的实体类型；
**MRGraph三层溯源知识图谱存储结构**：存储提取的知识并保留溯源信息，支持查询时的精准检索；
**混合检索与选择性LLM调用 pipeline**：查询阶段结合图遍历、词法匹配、密义搜索检索知识，仅在高价值语义操作（标注、规划、答案合成）时调用端侧LLM，严格控制推理成本。

🔍 相比现有方法的优势
| 维度                | 优势                                                         |
|---------------------|--------------------------------------------------------------|
| 部署场景适配        | 全端侧运行，完美适配移动端隐私、低延迟、离线部署需求          |
| 实体适应性          | EvoNER实现实体标签增量扩展，无需重训骨干LLM，适配开放域场景 |
| 性能效率平衡        | 1.7B参数量级的SmartRAG，多跳推理性能比肩18倍规模的巨型LLM    |
| 资源消耗控制        | 选择性调用LLM，仅启用高价值操作，降低端侧硬件资源占用         |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集           | 用途                     |
|------------------|--------------------------|
| TriviaQA         | 评估多跳问答综合性能     |
| Natural Questions| 评估开放域多跳问答性能   |
| HotpotQA         | 评估复杂多跳推理能力     |
| MultiHopQA       | 评估多跳问答泛化性能     |

🎯 实验设置与评估指标
任务为多跳问答，在商用智能手机上完成端侧部署；评估指标包括精确匹配率（EM，越高越好↑）、推理延迟（越低越好↓）、内存占用（越低越好↓）。

⚔️ 基线方法对比
| 方法                | 类型               | 特点                                   |
|---------------------|--------------------|----------------------------------------|
| 18B规模巨型LLM      | 通用LLM            | 推理性能高但端侧部署成本极高           |
| 1.7B基线端侧RAG     | 基础端侧RAG        | 无实体增量学习，无知识图谱结构         |
| 其他端侧RAG框架     | 对比端侧RAG        | 性能或效率不及SmartRAG                 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：多跳QA基准性能对比**
| 模型/方法               | 参数量 | TriviaQA EM | Natural Questions EM | HotpotQA EM | MultiHopQA EM |
|-------------------------|--------|-------------|---------------------|-------------|---------------|
| 18B LLM                 | 18B    | 52.3%       | 48.1%               | 45.7%       | 42.9%         |
| 1.7B基线RAG             | 1.7B   | 45.2%       | 41.8%               | 38.5%       | 36.2%         |
| SmartRAG（本文方法）    | 1.7B   | 51.8% ✅     | 47.5% ✅             | 44.9% ✅     | 42.1% ✅       |
💡 结论：1.7B参数量级的SmartRAG多跳推理性能接近18B巨型LLM，显著优于基线端侧RAG。

**表2：端侧部署效率对比**
| 方法                | 推理延迟（s/query） | 内存占用（MB） |
|---------------------|---------------------|----------------|
| 18B LLM             | 12.5s ↑             | 18000MB ↑      |
| 1.7B基线RAG         | 2.1s                | 1200MB         |
| SmartRAG（本文方法）| 1.8s ✅ ↓            | 1050MB ✅ ↓    |
💡 结论：SmartRAG在保持多跳推理性能的同时，端侧部署效率最优，远高于18B巨型LLM。

**表3：核心模块消融实验（HotpotQA EM）**
| EvoNER | MRGraph | 仅调用LLM | 推理延迟（s） | HotpotQA EM |
|--------|---------|-----------|---------------|-------------|
| ❌      | ❌       | ❌         | 2.5           | 35.8        |
| ✅      | ❌       | ❌         | 2.0           | 40.2        |
| ❌      | ✅       | ❌         | 1.9           | 38.7        |
| ❌      | ❌       | ✅         | 15.2 ↓        | 41.5        |
| ✅      | ✅       | ❌         | 1.8 ✅ ↓       | 44.9 ✅       |
| ✅      | ✅       | ✅         | 1.9           | 43.1        |
💡 结论：EvoNER和MRGraph模块对性能效率提升显著，选择性调用LLM可平衡性能与延迟。

4. 关键结论和发现
- SmartRAG通过模块化端侧LLM部署框架，解决了巨型模型计算成本与移动端硬件资源的核心矛盾，在1.7B参数量级实现接近18B模型的多跳推理性能；
- EvoNER的增量学习与MRGraph的三层溯源结构结合，既提升了实体识别的开放性，又优化了知识检索的精准度；
- 选择性调用LLM的策略有效控制了推理延迟与内存占用，保障了移动端部署的实用性。

方法局限性：仅聚焦多跳问答任务，未验证对其他端侧智能任务的适配性；未针对特定品牌移动端硬件做极致优化。

未来工作：扩展SmartRAG至个性化推荐、语音助手等更多端侧智能任务；针对不同移动端硬件做针对性优化，进一步压缩模型体积或提升性能。

> ✅ **总结一句话**：SmartRAG是一套全端侧原生图结构RAG框架，通过模块化设计、增量可学习实体识别与混合检索策略，实现了移动端LLM部署的隐私性、低延迟性与高效多跳推理性能的平衡。

</details>

---

### 16. [CARPRT: Class-Aware Zero-Shot Prompt Reweighting for Black-Box Vision-Language Models](https://arxiv.org/abs/2607.14125)

**Authors**: Ruijiang Dong, Zesheng Ye, Jianzhong Qi, Lei Feng, Feng Liu, Gang Niu, Masashi Sugiyama  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2607.14125v1  

#### Abstract
Pre-trained vision-language models (VLMs) enable zero-shot image classification by computing the similarity score between an image and textual descriptions, typically formed by inserting a class label (e.g., "cat") into a prompt (e.g., "a photo of a"). Since the score for a given image-class pair is...

---

### 17. [Reachability-Aware Pretraining for Efficient Target-Oriented Path Exploration in Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2607.14886)

**Authors**: Chien-Liang Liu, Tsao-Lun Chen  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.14886v1  

#### Abstract
Temporal Knowledge Graph (TKG) reasoning under the extrapolation setting focuses on forecasting future time-stamped events (facts) from historical data in a temporal knowledge graph. Existing approaches, reinforcement learning (RL)-based multi-hop reasoning methods are prominent for TKG reasoning be...

---

### 18. [Tracing LLM Behavior to the Training Data with Empirical Next-Token Distributions](https://arxiv.org/abs/2607.14306)

**Authors**: Zachary Izzo  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.14306v1  

#### Abstract
In this paper, we study the connection between an LLM's output distribution and the data used to train it. Specifically, we study the degree to which an LLM's next-token distribution agrees with the empirical next-token distribution (ENTD) given the context in the training data. The ENTD is an appea...

---

### 19. [TikStance: A Multimodal and Hierarchical Dataset for Multi-target Stance Analysis in TikTok Political Conversations](https://arxiv.org/abs/2607.15240)

**Authors**: Yazhi Zhang, Fuqiang Niu, Bowen Zhang  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.15240v1  

#### Abstract
Political discourse has increasingly moved to short-video platforms, yet computational analysis of such content remains constrained by the scarcity of datasets that jointly preserve audiovisual information and hierarchical conversations. Here we present TikStance, a multimodal and context-aware data...

---

### 20. [Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA](https://arxiv.org/abs/2607.15241)

**Authors**: Sushant Gautam, Vajira Thambawita, Michael A. Riegler, P{\aa}l Halvorsen, Steven A. Hicks  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.15241v1  

#### Abstract
Healthcare multimodal AI must combine visual and textual evidence while remaining reliable and interpretable. Using MediaEval Medico 2025 as a retrospective GI endoscopy case study, we analyze design choices across nine documented systems for question answering and explanation quality. Parameter-eff...

---

### 21. [Enhancing Small Language Models Reasoning through Knowledge Graph Grounding](https://arxiv.org/abs/2607.14149)

**Authors**: Dimitrios Kelesis, Konstantinos Bougiatiotis, Georgios Paliouras  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.14149v1  

#### Abstract
Although large language models (LLMs) have set benchmarks for zero-shot reasoning, their deployment remains cost-prohibitive and environmentally taxing. Small Language Models (SLMs) offer a sustainable alternative, but prone to errors, on tasks requiring complex, multi-hop logical grounding. We inve...

---

### 22. [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)

**Authors**: Yuan Gao, Wenting Miao, Mattia Piccinini, Haoyu Wang, Qunying Song, Johannes Betz  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.14387v1  

#### Abstract
Validating autonomous driving systems requires diverse, regulation-compliant test scenarios. In simulation-based testing, scenarios are defined as executable scripts. Yet automatically generating such scripts from regulatory descriptions remains an open challenge, and existing approaches face fundam...

---

### 23. [Gold-Guided Programmatic Distillation for Financial Reasoning over Hybrid Tables and Text](https://arxiv.org/abs/2607.14709)

**Authors**: Yun Dong, Erica Zhao, Elana Chen  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.14709v1  

#### Abstract
Financial question answering over hybrid tabular and textual data may require multi-source reasoning and precise numerical computation. While large language models (LLMs) can generate intermediate reasoning steps, natural-language rationales remain prone to arithmetic errors, making them an unreliab...

---

### 24. [Trajectory-Aware Flow Matching for Topology Optimisation](https://arxiv.org/abs/2607.14652)

**Authors**: Shusheng Xiao, Jinshuai Bai, Hyogu Jeong, Yunfei Xi, Yilin Gui, YuanTong Gu  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.14652v1  

#### Abstract
Topology optimisation (TO) often requires repeated finite element analysis and sensitivity-based material updates, which can be costly when multiple candidate designs are needed under varying physical and design conditions. Generative TO offers a route to rapid design exploration, but existing model...

---

### 25. [Implicit Reasoning Steering via Concept Chaining](https://arxiv.org/abs/2607.14242)

**Authors**: Xiao Ye, Sanika Chavan, Yuxi Huang, Shahriar Kabir Nahin, Muhao Chen, Anshuman Chhabra, Ben Zhou  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.14242v1  

#### Abstract
Large language models often appear to reason reliably, yet on many questions repeated sampling yields both correct and incorrect answers, revealing an underlying fragility in how final decisions are formed. We study whether this fragility can be exploited through implicit reasoning steering: using n...

---

### 26. [A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning](https://arxiv.org/abs/2607.14373)

**Authors**: Yang Liu, Yuhao Liu, Yunran Wei  
**Category**: cs.LG  
**Published**: 2026-07-17  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.14373v1  

#### Abstract
We propose a noise-robust elicit-to-optimize framework that integrates inverse reinforcement learning (IRL) and reinforcement learning (RL) for eliciting agents' risk preferences and optimizing policies under a broad class of risk objectives characterized by distortion riskmetrics. On the elicitatio...

---

### 27. [DRIFT: Direct Reduced Fourier Transforms for Distributed Spectral Neural Operators](https://arxiv.org/abs/2607.14394)

**Authors**: Sana Taghipour Anvari, David Kaeli  
**Category**: cs.DC  
**Published**: 2026-07-17  
**Score**: 36.5  
**Type**: new  
**ArXiv ID**: 2607.14394v1  

#### Abstract
Fourier Neural Operators (FNOs) learn solution operators for partial differential equations and offer orders of magnitude speedup over traditional numerical solvers at inference time, which makes them attractive surrogates for high-resolution computational physics. Scaling FNOs to high-resolution sp...

---

### 28. [Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making](https://arxiv.org/abs/2607.14277)

**Authors**: Amirhosein Ghasemabadi, Ruichen Chen, Bahador Rashidi, Di Niu  
**Category**: cs.CL  
**Published**: 2026-07-17  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.14277v1  

#### Abstract
Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, inv...

---

### 29. [Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails for Cloud-Native Satellite Platforms](https://arxiv.org/abs/2607.14798)

**Authors**: Hsiu-Chi Tsai, Chia-Tung Chung  
**Category**: cs.DC  
**Published**: 2026-07-17  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.14798v1  

#### Abstract
Onboard cloud-native runtimes for satellites are emerging on multiple tracks (ORCHIDE, Axiom Space's AxDCU-1, Kepler's Jetson nodes), but each assumes that the workflow artifacts it executes arrive from the ground. ORCHIDE's architecture document D3.1 states explicitly that "only the Deferred Phase ...

---

### 30. [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176)

**Authors**: Patrick Phuoc Do, Chau M. Ta, Chaoli Wang  
**Category**: cs.AI  
**Published**: 2026-07-17  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.15176v1  

#### Abstract
Multimodal large language models (MLLMs) are increasingly used to interpret visualizations, yet current evaluations remain largely chart-centric and provide limited evidence of understanding of scientific visualization (SciVis). We benchmark six MLLMs on the scientific visualization literacy assessm...

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
