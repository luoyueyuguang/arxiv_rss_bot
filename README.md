# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-12 07:23:16 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](https://arxiv.org/abs/2608.10976v1)

**Authors**: Foundation Model Team, XPeng Inc  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 84.5  
**Type**: new  
**ArXiv ID**: 2608.10976v1  

#### Abstract
Vision-Language-Action (VLA) models can connect scene understanding, semantic reasoning, and trajectory generation for autonomous driving. However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optim...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Vision-Language-Action（VLA）模型采用的冗长自然语言Chain-of-Thought（CoT）不适合实时控制，存在开放性、解码成本高、难以优化为面向动作的表示等缺陷。

🚀 提出的新方法与思路
**XCoT-VLA**：用从自动构建的Reason-Action监督中学习到的紧凑可执行CoT token替代描述性推理依据，日志轨迹提供动作证据，场景上下文提供因果语义；预测的XCoT序列保留在上下文，通过共享多模态自注意力约束固定轨迹查询。
**确定性token-function路由**：将Reason FFN应用于XCoT token，Control FFN应用于轨迹查询，通过流匹配实现轨迹生成。
**XCoT Policy Optimization (XCPO)**：作为可选细化扩展，在相同可执行token空间中实现优化。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理表示形式 | 采用紧凑可执行CoT token，替代冗长自然语言CoT |
| 实时性 | 减少自回归推理开销，满足实时规划预算 |
| 轨迹生成适配性 | 直接连接驾驶推理与轨迹生成，更适配自动驾驶场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
自动驾驶轨迹生成任务，评估指标相关内容因无法定位对应来源未报告：
| 指标 | 含义 |
| ---- | ---- |
| 纵向ADE | 论文未报告 |
| 横向FDE | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
因无法定位论文中定量结果对应的表号、图号等来源，所有定量结果均未报告：
- 主benchmark性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：XCoT-VLA通过2-6个紧凑可执行的CoT token完成驾驶相关推理，大幅减少了自回归推理开销；可直接将驾驶推理连接到轨迹生成，提升轨迹生成的适配性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：XCoT-VLA采用从Reason-Action监督学习得到的紧凑可执行CoT token，优化了自动驾驶VLA模型的实时性，实现了推理与轨迹生成的直接衔接。

</details>

---

### 2. [VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus](https://arxiv.org/abs/2608.10665v1)

**Authors**: Rohit Sinha, Kunal Tilaganji, Tanuja Ganu, Nagarajan Natarajan, Amit Sharma, Vineeth Balasubramanian  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.10665v1  

#### Abstract
Multimodal large language models often generate reasoning chains containing subtle errors that lead to incorrect answers. Current verification approaches have notable limitations. Existing approaches either require expensive labelled supervision with inconsistent cross-task performance or aggregate ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现有多模态推理验证方法要么依赖昂贵的带标签监督，跨任务性能表现不一致；
2. 现有验证方法多简单聚合多来源分数，忽略了验证器之间的分歧所携带的关于推理步骤是否有效的关键信息。

🚀 提出的新方法与思路
**VERDICT（Verification via Disagreement-Informed Coupled Thresholding）**：将多模态推理的验证建模为不同冻结验证器之间的耦合评分问题，形式化为具有闭式解的协调博弈；通过该闭式解计算共识分数，实现对推理步骤的分歧感知过滤和稳定感知排序，是首个明确处理跨模态分歧的训练-free多模态推理逐步骤验证方法。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
监督依赖 | 训练-free，无需昂贵的带标签监督
跨任务适配 | 领域无关，无需任务特定的适配
分数利用逻辑 | 分歧感知，利用验证器分歧的关键信息而非简单聚合
验证粒度 | 逐步骤验证，明确判断推理步骤的有效性

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
六个基准（论文未报告具体名称） | 用于VERDICT方法的性能评估

🎯 实验设置与评估指标
任务为多模态推理的逐步骤验证；
指标 | 含义
--- | ---
论文未报告具体指标名称 | 衡量VERDICT对多模态推理性能的提升幅度（论文提及最高提升达+5.95%）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
领域特定批评者（domain-specific critics） | 多模态推理验证方法 | 需要大量监督，性能表现与VERDICT相当
Base模型（base model） | 基础生成模型 | 无额外验证机制，直接输出推理结果
VERDICT | 多模态推理验证方法 | 训练-free，领域无关，分歧感知

3. 主要实验结果和性能指标
📊 定量结果汇总
**表：论文未报告具体表号**
方法 | 相对Base模型的性能提升 | 与领域特定批评者的表现对比
--- | --- | ---
VERDICT | 最高达+5.95% | 表现相当
💡 结论：在六个基准上，VERDICT相比Base模型实现了性能提升，且与需要大量监督的领域特定批评者的表现竞争力相当。

其他实验模块（论文未报告）：
效率对比（FPS/参数量）：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 多模态验证器间的分歧包含推理步骤有效性的关键信息，利用该信息可提升多模态推理验证的性能；2. 提出的VERDICT是首个明确处理跨模态分歧的训练-free逐步骤验证方法，无需任务特定适配即可实现鲁棒验证；3. VERDICT在六个基准上的性能优于Base模型，且与领域特定的监督型批评者竞争力相当。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的训练-free、领域无关的VERDICT方法，通过利用多模态验证器间的分歧信息实现逐步骤验证，性能提升显著，无需昂贵监督即可达到与领域特定监督型批评者相当的效果。

</details>

---

### 3. [VisEditBench: Can Vision-Language Models Edit Visualization Code from Multimodal Feedback?](https://arxiv.org/abs/2608.10408v1)

**Authors**: Mizanur Rahman, Arshia Azimlu, Shadikur Rahman, Md Tahmid Rahman Laskar, Amran Bhuiyan, Shafiq Joty, Enamul Hoque Prince  
**Category**: cs.CL  
**Published**: 2026-08-12  
**Score**: 54.0  
**Type**: new  
**ArXiv ID**: 2608.10408v1  

#### Abstract
Vision-language models (VLMs) have shown strong capabilities in generating visualization code from textual or visual specifications. However, real-world visualization authoring is inherently iterative: users frequently revise existing visualizations to repair flawed charts or adapt them to desired s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

VisEditBench: Can Vision-Language Models Edit Visualization Code from Multimodal Feedback?
1. 论文的主要贡献和创新点
✅ 解决的问题
现有视觉语言模型（VLMs）的能力评估多聚焦于从头生成可视化代码，而现实可视化创作是迭代式过程，需修正错误或调整样式，但针对多模态反馈下的可视化代码编辑任务，缺乏对应的基准与系统性研究。

🚀 提出的新方法与思路
**VisEditBench基准构建**：构建包含1395个人类标注可视化代码编辑任务的基准，覆盖反馈引导修复（基于buggy/标记图表加文本反馈修改代码）和参考引导重样式化（修改代码匹配目标图表）两个贴合现实的场景。
**VisEditAgent框架**：提出一种基于渲染的可视化编辑框架，采用迭代式流程：生成候选编辑、执行代码、验证结果、精炼编辑，该框架基于GPT-4o构建。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 基准构建 | 首个针对多模态反馈场景下可视化代码编辑任务的人类标注基准，覆盖现实可视化工作流与失败案例 |
| 编辑框架 | VisEditAgent引入渲染级迭代反馈，强化编辑过程中的验证与优化，提升可视化编辑的精准度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| VisEditBench | 用于评估VLMs在反馈引导修复、参考引导重样式化场景下的可视化代码编辑性能，共含1395个人类标注任务 |

🎯 实验设置与评估指标
任务为两种可视化代码编辑场景：一是反馈引导修复，即基于buggy或标记的图表结合文本反馈修改可视化代码；二是参考引导重样式化，即修改代码以匹配目标图表图像。
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| pass rate | 编辑任务的通过比例，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Claude-4.6-Sonnet | VLM | 20个SOTA VLMs中整体pass率最佳，达74.46%，但参考引导重样式化场景pass率仅55.71% |
| VisEditAgent | 渲染-grounded编辑框架 | 基于GPT-4o构建，采用迭代生成-执行-验证-精炼流程，用于提升可视化编辑性能 |
| 其他20个SOTA VLMs | VLM | 大部分开源模型的整体pass率低于50% |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（可视化代码编辑场景）**
| 方法 | 整体pass率 | 参考引导重样式化pass率 |
| ---- | ---- | ---- |
| Claude-4.6-Sonnet | 74.46%✅ | 55.71% |
| VisEditAgent（基线） | 67.99% | - |
| 多数开源SOTA VLMs | <50% | 论文未报告 |

💡 结论：现有VLMs在可视化代码编辑任务上整体性能有待提升，尤其是视觉风格适配的参考引导场景，提出的VisEditAgent通过迭代渲染反馈可显著提升编辑性能。

效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 20个SOTA VLMs中，Claude-4.6-Sonnet的整体pass率最高（74.46%），但多数开源模型pass率低于50%；② 参考引导重样式化场景性能弱于反馈引导修复场景，最佳模型在该场景仅达55.71%；③ VisEditAgent基于GPT-4o，通过迭代渲染反馈将整体pass率从55.75%提升至67.99%，证明渲染级反馈对精准编辑的重要性。
- 方法局限性：论文未明确报告具体局限性，仅从结果可见视觉风格适配场景仍有较大性能提升空间。
- 未来工作：可进一步强化视觉风格适配场景的编辑能力，拓展VisEditBench的任务覆盖范围与评估维度。

> ✅ **总结一句话**：VisEditBench构建了首个聚焦多模态反馈下可视化代码编辑的人类标注基准，揭示了现有SOTA VLMs在该任务的性能瓶颈，提出的VisEditAgent框架通过迭代渲染反馈大幅提升了编辑效能。

</details>

---

### 4. [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](https://arxiv.org/abs/2608.10149v1)

**Authors**: Xu Zhang, Chang Xu, Hui Sun, Nan Ma, Zijian Zhang, Peng Wang, Wei Wang, Li Zhao  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.10149v1  

#### Abstract
Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting
1. 论文的主要贡献和创新点
✅ 解决的问题
现有时间序列集成学习方法依赖固定规则或纯数值输入的黑箱模型，未能利用LLM推理生成可解释的样本自适应权重；真实世界时间序列的多样性导致单模型无法在所有样本上取得最优表现，现有集成方法未充分结合LLM的推理能力解决该问题。

🚀 提出的新方法与思路
**结构化输入流水线**：将原始时间序列转换为固定token成本的混合文本-数值表示，支持基于规则的思维链构造（无需API依赖），同时融入检索到的相似样本先验。
**多样多行权重监督方案**：采用标记高效的百分比表格格式，降低数值复杂度以缓解LLM幻觉，为权重提供监督。
**两阶段微调框架（SFT+GRPO）**：结合监督微调（SFT）与生成型强化学习偏好优化（GRPO），通过倒数奖励映射将连续无界的MSE差值转换为有界信号，放大近“准最优”（oracle）的灵敏度，解决回归型GRPO中原始奖励设计的均匀灵敏度及异常值主导的优势压缩问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 可解释性 | 生成自然语言解释 |
| 样本适应性 | 基于LLM推理为不同样本生成定制化的集成权重 |
| 缓解LLM幻觉 | 通过百分比表格格式降低数值复杂度，减少幻觉问题 |
| GRPO优化效果 | 解决回归型GRPO中均匀灵敏度及异常值主导的优势压缩缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 8个基准数据集 | 验证REATS的时间序列预测性能、迁移学习及域外泛化能力 |

🎯 实验设置与评估指标
任务为自适应时间序列预测，论文未明确报告具体评估指标名称及对应标准。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 主流竞争集成基线方法 | 集成学习方法 | 依赖固定规则或纯数值输入的黑箱模型，未利用LLM推理生成可解释权重 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告具体表号、指标数值及最优结果
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未提供具体实验结果，仅提及具备强迁移学习与域外泛化能力
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① REATS在8个基准数据集上优于现有竞争集成基线方法；② REATS可提供自然语言解释；③ REATS具备对未见过候选模型的强迁移学习及域外泛化能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：REATS是一种基于LLM推理的自适应时间序列预测集成学习方法，通过结构化输入流水线、多样权重监督方案及优化的两阶段微调框架，实现可解释的样本自适应权重决策，在多个基准上优于现有集成方法且具备强泛化能力。

</details>

---

### 5. [Rationale-Guided Learning for Multimodal Emotion Recognition](https://arxiv.org/abs/2608.10448v1)

**Authors**: Sujung Oh, Jung Uk Kim, Sangmin Lee  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.10448v1  

#### Abstract
Multimodal emotion recognition in conversation (MERC) requires understanding complex interactions between verbal and non-verbal cues. However, most existing approaches fundamentally treat this as a direct input-output (multimodal cues-emotion labels) mapping problem, overlooking the causal reasoning...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Rationale-Guided Learning for Multimodal Emotion Recognition
## 1. 论文的主要贡献和创新点
✅ 解决的问题：现有多模态对话情感识别（MERC）方法多将任务视为多模态线索到情感标签的直接输入输出映射，忽略了人类解读情感时所使用的因果推理。

🚀 提出的新方法与思路
**RGL框架**：将MERC转化为认知启发的推理任务，基于双过程理论把情感推理分解为直觉感知（System 1）、情境分析（System 2）、整合三个方面；利用MLLM离线生成结构化理由，将其编码为记忆，通过对齐内部表征与类人推理模式指导模型训练，且模型推理阶段无需MLLM。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 情感识别性能 | 在IEMOCAP、MELD基准达到State-of-the-art性能 |
| 推理可解释性 | 模型内部特征可有效为未见过的测试样本检索语义正确的理由 |
| 推理阶段开销 | 推理时无MLLM相关额外开销 |

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| IEMOCAP | 主基准测试 |
| MELD | 主基准测试 |

🎯 实验设置与评估指标
任务为多模态对话情感识别（MERC）；论文未报告具体评估指标。

⚔️ 基线方法对比
论文未报告

## 3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告对应表号，仅提及在IEMOCAP、MELD基准上取得State-of-the-art性能。
💡 结论：RGL框架在MERC任务的IEMOCAP和MELD基准上达到最优性能。

效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验：论文未报告

## 4. 关键结论和发现
- 主要发现：1. 基于双过程理论的RGL框架可将MERC转化为类人推理任务；2. RGL在IEMOCAP和MELD基准上实现MERC的State-of-the-art性能，且推理阶段无需额外MLLM开销；3. RGL的内部特征具备有效检索语义正确理由的能力，可解释性良好。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：提出的RGL框架将多模态对话情感识别转化为认知启发的推理任务，在IEMOCAP和MELD基准上达到最优情感识别性能，推理阶段无MLLM额外开销，同时具备良好的可解释性。

</details>

---

### 6. [Efficient Hypergradient Descent for Inverse Reinforcement Learning](https://arxiv.org/abs/2608.11052v1)

**Authors**: Nikita Sevriukov, Anna Barabanova, Uliana Gagarina, Karina Ivanova, Sofiia Kasaeva, Ilya Levin, Marina Sheshukova  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.11052v1  

#### Abstract
Inverse reinforcement learning (IRL) aims to recover a reward function under which the resulting policy reproduces the behavior observed in expert demonstrations. A natural approach is to formulate IRL as a bilevel optimization problem, in which the inner level corresponds to policy optimization und...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Efficient Hypergradient Descent for Inverse Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
逆强化学习（Inverse Reinforcement Learning, IRL）可建模为双层优化问题，其中内层为学习到的奖励下的策略优化，外层为诱导策略与专家数据的不匹配度；但外层更新所需的超梯度涉及逆海森向量乘积（inverse-Hessian-vector product），该计算在实践中面临高计算挑战，现有相关方法未系统性解决双层优化中超梯度计算的可扩展性瓶颈。

🚀 提出的新方法与思路
**Fisher-structured hypergradient**：证明在内层最优处，内层目标的海森矩阵与策略的Fisher信息矩阵成比例，进而得到与自然超梯度下降（Natural Hypergradient Descent）密切相关的结构化Fisher超梯度，降低超梯度计算复杂度。
**Streaming spectral sketch approximation**：针对大Fisher矩阵的可扩展性瓶颈，采用流式谱sketch近似所需的逆Fisher向量乘积，避免显式构造高维Fisher矩阵。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 策略性能 | 对比一阶随机双层基线，具备具有竞争力的策略性能 |
| 奖励排序质量 | 具备较强的奖励排序质量 |
| 曲率存储复杂度 | Fisher sketching可降低曲率存储复杂度 |
| 计算效率 | 相对于显式Fisher求解器，可提升计算效率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称 | 在离散与连续控制环境中评估方法性能 |

🎯 实验设置与评估指标
任务：在离散和连续控制环境中，评估所提IRL方法的策略性能与奖励排序质量。
| 指标 | 含义 |
| --- | --- |
| 论文未报告具体评估指标类型 | - |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 一阶随机bilevel基线 | 基线方法 | 用于对比所提方法性能的一阶双层优化方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验结果对应表号、图号及数值，仅报告如下定性结果：
1. 在所评估的离散与连续控制环境中，所提方法具备与一阶随机bilevel基线可比的策略性能，且奖励排序质量更强；
2. Fisher sketching可降低曲率存储复杂度，且相对于显式Fisher求解器，能提升计算效率。

4. 关键结论和发现
- 主要发现：
  1. 基于Fisher结构化超梯度的思路可有效缓解IRL双层优化中超梯度计算的高复杂度问题；
  2. 流式谱sketch近似能避免显式构造高维Fisher矩阵，解决了IRL中大规模Fisher矩阵带来的可扩展性瓶颈；
  3. 所提方法在离散与连续控制环境中，相比一阶随机双层基线具备可比的策略性能与更强的奖励排序质量，且计算效率更高。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出了基于Fisher结构化超梯度与流式谱sketch近似的高效超梯度下降方法，解决了逆强化学习双层优化中超梯度计算的高复杂度问题，在离散与连续控制环境中实现了可比的策略性能与更强的奖励排序质量，同时降低了曲率存储复杂度并提升了计算效率。

</details>

---

### 7. [Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance](https://arxiv.org/abs/2608.10434v1)

**Authors**: Cong Chi Nguyen, Trang Mai Xuan, Vu-Duc Ngo, Kim-Ngan Thi Nguyen, Trong-Nghia Nguyen, Thien Van Luong  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.10434v1  

#### Abstract
Machine learning-based Intrusion Detection Systems (IDS) have demonstrated superior performance in securing Unmanned Aerial Vehicle (UAV) networks. However, the 'black-box' nature of these models, combined with the high dimensionality of multimodal cyber-physical data, poses significant interpretabi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance》
1. 论文的主要贡献和创新点
✅ 解决的问题
机器学习驱动的无人机（UAV）网络入侵检测系统（IDS）性能优异，但存在两大痛点：一是模型的“黑箱”特性，二是多模态网络物理数据的高维性，共同带来显著的可解释性挑战；不同现有方法的缺陷为：传统静态可视化XAI仪表盘无法有效呈现多模态特征间的复杂关系，不便于操作人员检查与解释。
🚀 提出的新方法与思路
**LLM驱动的对话式XAI界面**：针对UAV入侵检测的后 incident 审计任务，采用大语言模型（LLM）搭建自然语言交互界面，支持操作人员按需开展调查与信息查询，以弥补传统静态仪表盘的不足。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 感知可用性 | 对话式界面被操作人员感知为比传统XAI仪表盘更有用，可帮助操作人员更轻松地获取与综合相关信息 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告具体数据集，用于开展UAV入侵检测相关的对照实验 |
🎯 实验设置与评估指标
实验任务：对比LLM驱动的对话式XAI界面与传统XAI仪表盘，对UAV入侵检测后 incident 审计任务中操作人员的理解、信任、依赖情况的影响
| 指标 | 含义 |
| --- | --- |
| 感知有用性 | 操作人员对XAI界面易用性与有效性的主观评价 |
| 信任程度 | 操作人员对IDS及XAI输出的信任度 |
| 依赖程度 | 操作人员对XAI建议的依赖程度 |
| 适当自我依赖程度 | 操作人员自主验证IDS输出与XAI信息的程度 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Conversational XAI（LLM驱动） | 提出的新方法 | 基于LLM的自然语言交互，支持按需调查 |
| 传统XAI Dashboard | 基线方法 | 静态可视化呈现可解释信息，仅支持固定格式的检查 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果及对应表号、图号，仅定性提及对话式界面感知更有用、适当自我依赖程度更低的结论。

4. 关键结论和发现
- 主要发现
1. LLM驱动的对话式XAI界面在UAV入侵检测后审计任务中，被操作人员感知为比传统静态XAI仪表盘更有用；
2. 对话式界面提升交互可用性的同时，存在降低操作人员适当自我依赖程度的潜在风险，可能引发过度依赖；
3. 自然语言形式的AI建议更易被操作人员接受，或导致其在IDS错误时减少对底层证据的验证倾向。
- 方法局限性
论文未报告具体局限性
- 未来工作
设计未来XAI系统时，需平衡交互的无缝性与认知强制功能，以促进操作人员的适当依赖。
> ✅ **总结一句话**：本论文通过受控实验对比了LLM驱动的对话式XAI界面与传统仪表盘在UAV入侵检测后审计任务中对操作人员信任和依赖的影响，指出对话式界面虽提升感知可用性，但存在过度依赖的潜在风险，需在设计中平衡交互便捷性与适当依赖的培养。

</details>

---

### 8. [Hierarchical Empirical-Bayes Naive Bayes: Minimax Smoothing and Calibration with AODE Extension](https://arxiv.org/abs/2608.11162v1)

**Authors**: Nguyen Thai Anh, Truong Viet Vu, Tran Thien Thanh, Vo Nguyen Quoc Bao, Ngo Hoang Tu  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.11162v1  

#### Abstract
The Naive Bayes (NB) classifier remains a standard choice for categorical data, yet its widely used smoothing rules, such as Laplace, Lidstone, Krichevsky-Trofimov, and the $m$-estimate, all prescribe a fixed smoothing strength that ignores feature cardinality, sample size, and class imbalance, indu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Hierarchical Empirical-Bayes Naive Bayes: Minimax Smoothing and Calibration with AODE Extension
1. 论文的主要贡献和创新点
✅ 解决的问题
- 核心矛盾：传统Naive Bayes的常用平滑规则存在固有的性能缺陷。
- 具体缺陷：Laplace、Lidstone、Krichevsky-Trofimov、m-estimate等常用平滑规则均采用固定平滑强度，未考虑特征基数、样本量及类别不平衡，在现代高基数表格数据上会产生非零偏差。

🚀 提出的新方法与思路
**HEB-NB（Hierarchical Empirical-Bayes Naive Bayes）**：为每个类-特征条件概率分配Dirichlet先验，通过Type-II最大似然数据自适应学习先验浓度参数，实现类间的原则性信息共享，同时保留闭式推理能力。
**HEB-AODE**：将HEB-NB的自适应平滑策略扩展到AODE（平均单依赖估计器）的结构松弛中，适配单依赖结构的朴素贝叶斯变体。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 偏差控制 | 避免传统固定平滑规则在高基数数据上产生的非零偏差 |
| 平滑强度 | 平滑强度随数据特性自适应调整，无需预设固定值 |
| 类间信息共享 | 通过分层经验贝叶斯机制实现类间的原则性信息共享 |
| 推理效率 | 保留闭式推理，无需复杂迭代优化，推理高效 |
| 概率校准 | 可显著降低预期校准误差（ECE），提升概率预测质量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 31 UCI and OpenML benchmarks | 用于基准测试模型性能，对比不同方法的表现差异 |

🎯 实验设置与评估指标
任务为针对表格数据的分类任务，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 平均Friedman秩 | 模型性能排名指标，秩越低代表性能越好 |
| log-loss | 概率预测的损失指标，值越低代表概率预测越准确 |
| 预期校准误差（ECE） | 概率校准程度指标，值越低代表概率预测校准度越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Laplace平滑 | 平滑规则 | 采用固定平滑强度的传统朴素贝叶斯平滑方法 |
| Lidstone平滑 | 平滑规则 | 采用固定平滑强度的传统朴素贝叶斯平滑方法 |
| Krichevsky-Trofimov平滑 | 平滑规则 | 采用固定平滑强度的传统朴素贝叶斯平滑方法 |
| m-estimate | 平滑规则 | 采用固定平滑强度的传统朴素贝叶斯平滑方法 |
| vanilla AODE | 分类器 | 基于单依赖结构的平均单依赖估计器，无自适应平滑策略 |
| HEB-NB | 提出的模型 | 采用自适应平滑策略的分层经验贝叶斯朴素贝叶斯分类器 |
| HEB-AODE | 提出的模型 | 将HEB自适应平滑策略扩展到AODE结构的分类器 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主benchmark性能：论文未报告对应表号，仅说明在31 UCI和OpenML基准测试中，HEB-NB在概率指标上实现最优平均Friedman秩；高基数数据集上，HEB-NB的log-loss降低最高达22.1%；HEB-AODE较vanilla AODE有一致的性能提升；结合互信息加权的HEB-NB可将top-1预期校准误差（ECE）降低41%-70%。
- 效率对比（FPS/参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现1：HEB-NB通过数据自适应学习Dirichlet先验浓度参数，解决了传统固定平滑规则在高基数表格数据上的非零偏差问题，同时保留了闭式推理和类间信息共享能力。
- 主要发现2：HEB-AODE可将自适应平滑策略迁移到AODE结构，实现较vanilla AODE的一致性能提升。
- 主要发现3：结合互信息加权的HEB-NB可显著降低分类器的预期校准误差，提升概率预测的校准度。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出HEB-NB和HEB-AODE方法，通过自适应分层经验贝叶斯平滑策略解决了传统朴素贝叶斯类模型固定平滑强度导致高基数数据非零偏差的问题，在31 UCI和OpenML基准测试中实现了概率性能和校准度的显著提升。

</details>

---

### 9. [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](https://arxiv.org/abs/2608.10198v1)

**Authors**: Di Wu, Xiaohui Zhu  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 36.5  
**Type**: new  
**ArXiv ID**: 2608.10198v1  

#### Abstract
Latent-space communication allows heterogeneous vision-language model agents to exchange continuous representations without serializing visual and reasoning states into text. Vision Wormhole realizes this approach by translating visual features into a universal latent representation that can be cons...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents
1. 论文的主要贡献和创新点
✅ 解决的问题
Vision Wormhole等VLM智能体的潜通信采用固定大小的密张量传输，未根据消息内容调整通信容量，导致固定密张量的有效信息密度不固定，通信信道存在冗余，原始密传输机制未解决该问题。

🚀 提出的新方法与思路
**Post-Hoc Sparse Autoencoder (SAE)**：对冻结的Vision Wormhole激活进行后处理，拟合稀疏自编码器，采用uint16索引/float16值的稀疏负载形式，设置每个token的活跃系数数量k=4，实现潜通信数据的压缩传输。

🔍 相比现有方法的优势
维度 | 优势
通信数据量 | 显著压缩
下游任务性能 | 几乎无明显下降
特征复用性 | 不同任务间存在较高的特征相似度

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
九个推理基准 | 评估不同通信机制的压缩效果与任务性能

🎯 实验设置与评估指标
在九个推理基准上评估VLM智能体潜通信的效果，指标包括重构性能、下游效用、特征复用度、token级干预效果。
指标 | 含义（箭头）
重构性能 | 衡量激活的还原程度，越高越好
下游效用 | 衡量通信对任务性能的影响，越高越好
特征复用度 | 衡量不同任务共享特征的程度，越高越好
token级干预效果 | 衡量单个token特征的作用，越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
原始float32传输 | 密通信方法 | 采用固定大小密张量，无压缩处理

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
1. Vision Wormhole的潜通信信道存在可压缩冗余，后验稀疏编码可实现显著的通信数据压缩；
2. 该稀疏编码在压缩通信数据的同时，下游任务性能仅发生极小变化；
3. 任务级活跃特征集相似度高，不同任务间复用了大量特征。
- 方法局限性：
论文未孤立出后验稀疏编码相对于位置选择、精度降低、低秩结构或SAE优化效果的增量贡献。
- 未来工作：
需开展匹配载荷的对比实验，开发适配每条消息所用信息的自适应通信机制。

✅ **总结一句话**：该论文针对VLM智能体潜通信中的冗余问题，提出后验稀疏编码方法，大幅压缩了通信数据量且仅带来极小的下游任务性能损失，为高效潜通信提供了可行方案。

</details>

---

### 10. [Scheduling Mixed RL Rollouts Beyond Prefix Locality](https://arxiv.org/abs/2608.11152v1)

**Authors**: Zetao Hong, Song Yuan, Yuanhao Ding, Yibo Zhu, Daxin Jiang, Zhibin Wang, Chen Tian  
**Category**: cs.DC  
**Published**: 2026-08-12  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.11152v1  

#### Abstract
Modern reinforcement learning (RL) post-training pipelines for large language models (LLMs) increasingly combine rollout workloads across multiple domains and feedback paradigms. Prefix-aware routing improves inference efficiency through cache reuse and load balancing, but it does not control how he...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Scheduling Mixed RL Rollouts Beyond Prefix Locality
1. 论文的主要贡献和创新点
✅ 解决的问题
现有prefix-aware路由方法仅优化推理效率（缓存复用、负载均衡），无法控制RLVR、RLHF、agentic rollouts等异构rollout会话共享异步推理服务时对KV缓存容量的竞争，不同会话的序列结构、交互模式、KV驻留时间差异大，调度需兼顾异质性且不改变训练器指定工作负载混合。

🚀 提出的新方法与思路
**MISA-T**，即混合rollout服务的路由层准入策略，整合自适应会话准入、工作负载感知的KV容量分配、驻留时间感知的KV记账三个核心模块，用于应对异构rollout会话的KV缓存竞争问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 异构rollout适配性 | 支持RLVR、RLHF、agentic rollouts等不同范式、结构的rollout会话共享异步推理服务 |
| KV缓存资源管理 | 通过三类感知模块合理分配KV缓存资源，缓解异构会话的KV缓存竞争 |
| 吞吐量提升 | 在rollout-only场景下针对Step3.7、Qwen3.6-35B-A3B提升rollout吞吐量；在50-迭代Step3.7实验中提升rollout吞吐量 |
| 迭代时间优化 | 在50-迭代Step3.7实验中降低平均迭代时间 |
| 工作负载混合保持 | 保持的工作负载混合比例接近训练器指定的目标 |
| 前缀缓存命中率 | 维持高前缀缓存命中率 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
实验任务为混合RL rollout的服务调度性能优化，针对不同模型的rollout服务进行评估。
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| rollout吞吐量 | 越高越好 ↑ |
| 平均迭代时间 | 越低越好 ↓ |
| 前缀缓存命中率 | 越高越好 ↑ |
| 工作负载混合度 | 越接近训练器指定目标越好 |
| 任务分数 | 可比即可 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| sweep-tuned cache-aware vLLM Router | 缓存感知路由方法 | 仅针对前缀局部性优化，未处理异构rollout会话的KV缓存竞争 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表未标注：rollout-only ablation（场景）**
| 方法 | Step3.7 rollout吞吐量提升 | Qwen3.6-35B-A3B rollout吞吐量提升 | 前缀缓存命中率 |
| ---- | ---- | ---- | ---- |
| MISA-T | 53.3% | 43.6% | 维持高 |
💡 结论：在仅rollout的消融实验场景下，MISA-T相比基线方法大幅提升两种模型的rollout吞吐量，同时保持较高的前缀缓存命中率。

**表未标注：匹配的50-迭代Step3.7实验（场景）**
| 方法 | 50-迭代Step3.7 rollout吞吐量提升 | 平均迭代时间降低 | 工作负载混合度 | 任务分数 |
| ---- | ---- | ---- | ---- | ---- |
| MISA-T | 35.6% | 22.8% | 接近训练器目标 | 与基线可比 |
💡 结论：在匹配训练器指定迭代次数的Step3.7实验中，MISA-T在提升rollout吞吐量、降低平均迭代时间的同时，保持的工作负载混合度接近训练器目标，且任务性能与基线相当。

4. 关键结论和发现
- MISA-T作为混合RL rollout服务的路由层准入策略，可有效处理异构rollout会话的KV缓存竞争问题，且能维持较高的前缀缓存命中率。
- MISA-T在不同模型（Step3.7、Qwen3.6-35B-A3B）及不同实验场景下均能提升rollout服务性能，同时保持指定的工作负载混合比例。
- 论文未报告方法的局限性；论文未报告未来工作规划。

> ✅ **总结一句话**：MISA-T是针对混合RL rollout服务的路由层准入策略，通过整合自适应会话准入、工作负载感知KV容量分配、驻留时间感知KV记账三类机制，缓解异构rollout会话的KV缓存竞争，在多场景下提升服务吞吐量与迭代效率，同时保持工作负载混合度与任务性能。

</details>

---

### 11. [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393v1)

**Authors**: Jiahui Han, Yuhui Yao, Xin Wang, Jiafei Cao, Mingxuan Zhang, Danfeng Shan, Huiqi Deng, Guanchu Wang, Xia Hu  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.10393v1  

#### Abstract
Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对视觉-语言动作（VLA）模型的攻击，多依赖像素空间扰动或需要白盒访问，易产生明显人工痕迹，在真实机器人系统中的部署性有限；且VLA模型的对抗鲁棒性尚未被充分探索，存在物理世界危害的安全风险。

🚀 提出的新方法与思路
**DURA（Diffusion-based Unrestricted Robotic Attack）**：这是一种针对VLA模型的基于扩散的无限制机器人攻击方法，支持白盒与黑盒两种攻击设置（黑盒设置仅需目标模型的预测动作）；通过在预训练扩散模型的潜在轨迹上进行优化，生成视觉自然的对抗补丁，引导机器人朝向攻击者指定的目标动作。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 攻击设置 | 支持白盒与黑盒两种攻击设置 |
| 扰动特性 | 生成的对抗补丁视觉自然，无明显人工痕迹 |
| 部署可行性 | 可适配真实物理机器人系统的部署需求 |
| 攻击性能 | 在仿真与真实物理世界环境中均优于现有攻击方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：论文未报告
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验的具体定量数据（含表号、数值等）论文未报告。
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）现有VLA模型的对抗鲁棒性未被充分研究，针对其的攻击可能造成物理世界的危害；2）所提出的DURA攻击可生成视觉自然的对抗补丁，在仿真与真实物理环境中均优于现有攻击方法；3）基于扩散的攻击技术可显著提升VLA机器人攻击的真实部署能力。
- 方法局限性：论文未报告
- 未来工作：需要针对物理部署的VLA模型开发更强的防御机制，以应对这类无限制机器人攻击。

> ✅ **总结一句话**：该研究提出了名为DURA的扩散式无限制机器人攻击方法，解决了现有VLA机器人攻击人工痕迹明显、真实部署受限的问题，揭示了物理部署VLA模型存在的安全风险并呼吁强化防御。

</details>

---

### 12. [ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models](https://arxiv.org/abs/2608.10120v1)

**Authors**: Adrien Schoen, Nachiketa Ratnakar Patil, Arjun Bhagoji, Francesco Bronzino  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.10120v1  

#### Abstract
Modern sequence models, from Transformers to State Space Models, have enabled powerful generative modeling across diverse domains, yet they are typically trained to predict what happens while treating when it happens as a secondary concern. In data-mining settings where events are associated with ex...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有序列模型（包括Transformers、状态空间模型SSM）在训练中通常将事件的时间信息视为次要信号，采用两阶段策略处理带显式时间戳的事件序列：先用模型学习事件的表示，再单独训练一个时序模型学习时间信息。该策略的核心缺陷是**假设为事件预测优化的表示已包含足够的时间结构，但实际该假设不成立**，这会限制模型在时间推理、异常检测、事件时序忠实重建等任务中的表现。
🚀 提出的新方法与思路
**ChronoSSM**：一种自回归状态空间模型，采用共享backbone的联合训练框架，同时建模事件与时间戳，模型的训练目标包含token生成任务和时间生成任务的联合损失。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 时间信息可恢复性 | 联合训练策略可提升冻结表示中事件到达间隔信息的可恢复性 |
| 自回归事件建模性能 | 不会导致内容生成质量的系统性下降 |
| 时序表示质量 | 时间监督能生成更具时间信息的表示，且不显著降低自回归事件建模的性能 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告具体名称 | 实验覆盖四个域，包含密集时间戳监督与部分时间戳监督两种场景 |
🎯 实验设置与评估指标
论文未明确报告具体实验任务、评估指标及指标方向
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 两阶段方法 | 基线方法 | 时序信息仅通过冻结的事件表示单独学习，采用两阶段训练范式 |
| ChronoSSM | 提出方法 | 共享backbone，联合建模事件与时间戳，采用联合训练范式 |
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
- 主要发现
  1. 在包含密集和部分时间戳监督的四个域实验中，ChronoSSM的联合训练策略相比两阶段训练，可提升冻结表示中事件到达间隔信息的可恢复性，且不会导致内容生成质量的系统性下降；
  2. 时间监督可生成更具时间信息的表示，且不会显著降低自回归事件建模的性能。
- 方法局限性
论文未报告
- 未来工作
论文未报告
> ✅ **总结一句话**：ChronoSSM是一种采用共享backbone联合建模事件与时间戳的自回归状态空间模型，其联合训练策略可提升带时间戳的事件序列的时间信息可恢复性，同时不会损害自回归事件的内容生成质量，有效改善了传统两阶段序列模型在时序相关任务中的不足。

</details>

---

### 13. [Continuous Interaction Diffusion: A Diffusion-Native Runtime for Asynchronous Tool-Augmented Reasoning](https://arxiv.org/abs/2608.10438v1)

**Authors**: Yuhang Cao  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.10438v1  

#### Abstract
Large language models increasingly rely on external tools to access up-to-date information, perform computation, and interact with the outside world. For autoregressive models, tool use naturally fits the generation process: the model emits a tool call, waits for the result, and then continues gener...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Continuous Interaction Diffusion: A Diffusion-Native Runtime for Asynchronous Tool-Augmented Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有适用于自回归模型的工具交互模式（生成工具调用、等待结果、继续生成的stop-and-resume模式）对扩散语言模型（dLLMs）存在限制，会导致工具决策过早（推理未稳定前做出）、有用观察延迟、冗余细化与工具执行，损害任务精度和推理效率。

🚀 提出的新方法与思路
**Continuous Interaction Diffusion (CID)**，是扩散原生的模型-运行时架构，核心是将工具交互整合到迭代去噪过程中：分离出模型只读的事实通道、以Typed Cognitive Tensor表示的思想通道、显示通道；信息需求可在文本或JSON格式的工具调用完全序列化前产生，允许感知绑定启动外部读取操作的同时，模型仍可继续去噪；返回的结果会被投影到不断演化的思想状态，能够修正早期的认知和显示区域；持久绑定机制复用静态结果以避免重复的外部执行，当来源信息变化时可按需刷新。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 工具决策时机 | 不强制过早做出工具决策，避免推理未稳定时的错误选择 |
| 效率提升 | 将工具延迟与模型计算重叠，减少等待时间 |
| 冗余减少 | 复用静态结果，降低重复的外部工具执行开销 |
| 认知能力 | 新证据到达后可保留之前的有效计算，支持修正早期认知和显示区域 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 核心设计针对dLLMs工具交互的痛点，将工具交互嵌入迭代去噪流程，实现异步工具增强推理。
- 方法局限性：本文首次提出相关架构，仅聚焦于只读工具场景，未涉及其他类型工具的支持与验证，也未开展实验验证性能效果。
- 未来工作：可扩展至非只读工具场景，进一步完成架构的性能验证与优化等。

> ✅ **总结一句话**：提出了扩散原生的持续交互扩散（CID）架构，适配扩散语言模型的并行细化特性改进工具交互模式，解决了现有stop-and-resume模式对dLLMs工具利用的限制，通过多通道设计实现工具延迟重叠计算、减少冗余执行并支持认知修正。

</details>

---

### 14. [MIDAS: Mutual Information Disentanglement with Uncertainty-Aware Fusion for Incomplete Multimodal Sentiment Analysis](https://arxiv.org/abs/2608.09986v1)

**Authors**: Yuhua Wen, Yingying Zhou, Qifei Li, Yingming Gao, Zhengqi Wen, Jianhua Tao, Ya Li  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.09986v1  

#### Abstract
Most existing multimodal sentiment analysis approaches assume access to complete multimodal inputs. However, real-world applications frequently encounter incomplete or corrupted modalities, posing a critical challenge. Although several methods have been proposed to tackle this issue, they mainly rel...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：MIDAS: Mutual Information Disentanglement with Uncertainty-Aware Fusion for Incomplete Multimodal Sentiment Analysis
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态情感分析方法多假设输入完整，但真实应用中常出现模态不完整或损坏的情况；现有方法依赖数据插补和启发式协调约束，无法有效从非完整多模态数据中提取和利用任务相关信息。

🚀 提出的新方法与思路
**变分建模策略**：用多元高斯隐变量表示每个模态，将其分解为共享因子和独有因子。
**极小极大目标函数**：最小化共享空间与独有空间之间的互信息以实现稳定解耦，同时最大化跨模态共享空间间的互信息以增强语义对齐。
**不确定性感知融合机制**：利用后验方差作为可靠性指标，在融合过程中自适应加权隐特征，确保模态不完整时仍能实现鲁棒的特征集成。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 适用场景 | 适配真实世界中多模态情感分析的模态不完整/损坏场景 |
| 表征能力 | 通过互信息解耦提取共享和独有任务相关信息，突破现有方法依赖数据插补和启发式约束的局限 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 三个广泛使用的多模态情感分析数据集 | 验证MIDAS在多模态不完整场景下的有效性与鲁棒性 |

🎯 实验设置与评估指标
任务：针对模态不完整的多模态情感分析任务
评估指标：论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 竞争基线方法 | 多模态情感分析相关方法 | 依赖数据插补或启发式协调约束 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：MIDAS在多种不完整的多模态设置下，相比竞争基线方法取得了稳定且显著的性能提升；通过互信息解耦和不确定性感知融合策略，有效应对了真实场景中多模态数据不完整的问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MIDAS是针对多模态情感分析模态不完整场景的统一框架，通过互信息解耦和不确定性感知融合策略，有效提取并利用任务相关的多模态信息，实现了优于现有基线方法的性能。

</details>

---

### 15. [What Actually Serializes GPU LZ77 Decode: Three Decoders, Three Mechanisms, and an Encode-Time Lever That Removes the Last One](https://arxiv.org/abs/2608.10188v1)

**Authors**: Yakiv Shavidze  
**Category**: cs.DC  
**Published**: 2026-08-12  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.10188v1  

#### Abstract
The sequential part of GPU LZ77 decode is not where the field assumes it is. Across three decoder architectures on an H100 we measure that parse, not copy, holds 64-72% of device-resident decode time; that bounding back-reference chain depth - provable, and costing 0.006% in ratio - moves latency by...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：What Actually Serializes GPU LZ77 Decode: Three Decoders, Three Mechanisms, and an Encode-Time Lever That Removes the Last One
1. 论文的主要贡献和创新点
✅ 解决的问题：现有领域普遍认为GPU LZ77解码的串行瓶颈位于copy环节，该研究通过实验证实此认知错误，parse环节才是主串行瓶颈，占设备驻留解码时间的64-72%，纠正了解码优化方向的偏差。
🚀 提出的新方法与思路
**Parse串行瓶颈定位**：通过在H100 GPU上的实验测量，明确GPU LZ77解码的串行瓶颈为parse而非copy环节；
**回引用链深度限制策略**：提出限制回引用链深度的优化策略，仅产生0.006%的ratio开销，且不会导致文件的延迟峰值；
**自重叠匹配并行化策略**：发现自重叠匹配为周期填充而非依赖链，可并行化处理，实现匹配层2.75-8.42x的bit-perfect性能提升；
**编码器距离历史移除策略**：提出编码器可移除四个条目的距离历史，仅产生0.540%的ratio开销，生成的依赖-free parse序列从4条命令扩展至706条，减少解码依赖。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 串行瓶颈定位 | 纠正领域误判，明确parse为GPU LZ77解码的主串行瓶颈，优化方向更精准 |
| 回引用优化 | 极低开销且不影响文件延迟峰值，避免常规优化的副作用 |
| 匹配层性能 | 并行化自重叠匹配，实现2.75-8.42x的bit-perfect匹配层提速 |
| 解码依赖减少 | 编码器级优化，仅0.540% ratio开销即可大幅增加依赖-free parse序列长度 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：实验在H100 GPU上对三个解码器架构进行测试，任务为GPU LZ77解码性能评估；指标包括设备驻留解码时间（越低越好）、ratio开销（越低越好）、匹配层加速比（越高越好）、延迟峰值变化（越低越好）
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未明确给出各结果对应的表号、图号或章节，仅按论文摘要原文描述如下：
- parse占设备驻留解码时间的64-72%
- 限制回引用链深度的策略导致延迟最多变化2.8%，且对文件自身的延迟峰值无影响
- 自重叠匹配可实现匹配层2.75-8.42x的bit-perfect提速
- 编码器移除距离历史的策略产生0.540%的ratio开销
- 依赖-free parse序列从4条命令扩展至706条
- 总线效率为4.4%，合并写速度提升39倍
- 所有可复现结论均有机器可检查记录，代码克隆的标记发布在无GPU情况下17项检查全部通过
💡 结论：GPU LZ77解码的串行瓶颈为parse环节，自重叠匹配可并行化提升解码性能，编码器可通过移除距离历史优化解码流程

4. 关键结论和发现
- 核心串行瓶颈发现：GPU LZ77解码的串行瓶颈是parse而非领域此前假设的copy，占设备驻留解码时间的64-72%，是解码性能优化的核心方向
- 匹配层优化发现：自重叠匹配本质为周期填充而非依赖链，可并行化处理，实现2.75-8.42x的bit-perfect匹配层提速，大幅提升解码效率
- 编码器优化发现：编码器移除四个条目的距离历史仅产生0.540%的ratio开销，即可生成更长的依赖-free parse序列，减少解码依赖
方法局限性：论文未明确报告具体局限性，仅提及当前总线效率为4.4%
未来工作：可聚焦提升GPU LZ77解码的总线效率，优化数据传输环节的性能

> ✅ **总结一句话**：该论文通过在H100 GPU上对三种LZ77解码器的系统实验，纠正了领域对GPU LZ77解码串行瓶颈位置的误判，提出了匹配层并行化与减少解码依赖的编码器优化策略，为提升GPU LZ77解码性能提供了关键方向。

</details>

---

### 16. [Boundary-Seeking Policy Gradient for Safe Reinforcement Learning](https://arxiv.org/abs/2608.10204v1)

**Authors**: Chenhua Fan, Jiahui Zhu, Yuhang Zhang, Honghao Wei  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.10204v1  

#### Abstract
Safe reinforcement learning maximizes reward subject to safety constraints. For Constrained Markov Decision Processes, the linear-programming view over occupancy measures implies that whenever the constraint is active at optimality, the optimal policy lies exactly on the constraint boundary, yet sta...

---

### 17. [IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning](https://arxiv.org/abs/2608.10634v1)

**Authors**: Zefeng Liang, Jie Qiao, Ruichu Cai, Weilin Chen, Zhifeng Hao  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.10634v1  

#### Abstract
Model-based reinforcement learning (MBRL), which learns environment dynamics to generate synthetic experience, is a promising approach to sample-efficient decision making. Numerous methods have been developed to improve dynamics prediction and policy optimization for MBRL through uncertainty estimat...

---

### 18. [Reinforcement Learning-Based Laser Cutting Machine Parameter Optimization](https://arxiv.org/abs/2608.10549v1)

**Authors**: Khanh Quan Pham, Majid Kundroo, Geunwoo Ban, Seongho Bae, Taehong Kim  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.10549v1  

#### Abstract
Achieving high accuracy in laser-based cutting of optical films requires careful tuning of parameters such as focal length and laser power beam, adjusted according to the specific properties of each film type. Trial-and-error based traditional methods are used to find the most suitable cutting param...

---

### 19. [V-FiLLM: Verified Financial LLM Reasoning Benchmark](https://arxiv.org/abs/2608.11047v1)

**Authors**: Alicia Larsen, Victoire Laurent, Aulia Kharis Rakhamsari, Lara Turgut, Nino Antulov-Fantulin  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.11047v1  

#### Abstract
While existing benchmarks have made substantial progress in evaluating LLMs across STEM domains, financial reasoning over structured data remains comparatively less explored. We introduce V-FiLLM, a framework that generates financial reasoning benchmarks from executable computation trees grounded in...

---

### 20. [SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models](https://arxiv.org/abs/2608.10538v1)

**Authors**: Chenhao Dang, Siyuan Xiong, Conghui He, Weijia Li  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.10538v1  

#### Abstract
Agent skills represent a standardized format for packaging procedural knowledge and domain expertise, serving within agent harness systems as an essential mechanism to continually constrain a language model's behavior space for repeatable, high-quality task execution. However, because strong closed-...

---

### 21. [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](https://arxiv.org/abs/2608.10928v1)

**Authors**: Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat, Soumyabrata Pal, Ramasuri Narayanam, Dinesh Manocha  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.10928v1  

#### Abstract
Large Reasoning Models (LRMs) improve performance by allocating additional inference-time compute to generate extended chain-of-thought reasoning. However, recent studies reveal that sequential test-time scaling often yields diminishing or even negative returns, as longer traces exhibit increased un...

---

### 22. [Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding](https://arxiv.org/abs/2608.10207v1)

**Authors**: Xin Dong, Vikash V. Gayah  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.10207v1  

#### Abstract
Bus bunching degrades service regularity and increases passenger waiting in high-frequency transit. Existing reinforcement-learning-based holding controllers primarily rely on instantaneous operational variables or route-specific stop identifiers, which provide limited information about the function...

---

### 23. [MUSE: A Full-Text Cross-Domain Knowledge Base of Scientific Problems, Solutions, and Rationales](https://arxiv.org/abs/2608.10974v1)

**Authors**: Tsofia Cohen, Tom Hope  
**Category**: cs.CL  
**Published**: 2026-08-12  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.10974v1  

#### Abstract
Scientific papers contain fine-grained records of problem solving: authors mention technical obstacles and methods that were used to address them, often along with reasoning on why those methods were chosen. We introduce MUSE (Mining Underlying Scientific Explanations), a full-text, multi-domain res...

---

### 24. [The Multilingual Quantization Tax: Structural Collapse and Typological Fragility in Edge SLMs](https://arxiv.org/abs/2608.09941v1)

**Authors**: Mohammad Wathiq Soualhi  
**Category**: cs.CL  
**Published**: 2026-08-12  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.09941v1  

#### Abstract
While 4-bit weight quantization is critical for deploying Small Language Models (SLMs) on edge devices, evaluations of the resulting performance degradation-the quantization tax-remain overwhelmingly English-centric. We present a zero-shot multilingual evaluation of 4-bit quantization across the Gem...

---

### 25. [GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning](https://arxiv.org/abs/2608.10494v1)

**Authors**: Xin Xiao, Jiang Zhong, Junnan Zhu, Yingchao Feng, Peijin Wang, Yidan Zhang, Kaiwen Wei  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.10494v1  

#### Abstract
Earth observation (EO) agents construct scientifically valid tool workflows and ground their conclusions in current geospatial evidence. This is challenging because EO workflows are constrained by sensing semantics, product dependencies, spatial and temporal compatibility, and parameter requirements...

---

### 26. [REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base Construction from LLMs](https://arxiv.org/abs/2608.10963v1)

**Authors**: Thanh-Dan Bui, Thanh-Trung Do, Tuan-Phong Nguyen  
**Category**: cs.CL  
**Published**: 2026-08-12  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2608.10963v1  

#### Abstract
We present the REAP system for the AKBC Shared Task 2026 on constructing knowledge bases from language models in a closed-book setting, subject to a budget of at most 32B parameters and no model fine-tuning. Our system combines structured chain-of-thought reasoning, relation-specific query strategie...

---

### 27. [Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration](https://arxiv.org/abs/2608.10372v1)

**Authors**: Lening Zhao, Qipeng Zhan, Li Shen  
**Category**: cs.LG  
**Published**: 2026-08-12  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.10372v1  

#### Abstract
Post-hoc calibration aligns a classifier's predicted confidences with its empirical accuracy without retraining. An ideal calibrator should correct nonlinear miscalibration, scale gracefully to large label spaces, and preserve the original predictions; existing methods typically violate at least one...

---

### 28. [Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence](https://arxiv.org/abs/2608.10720v1)

**Authors**: Haoyu Zhang, Zhipeng Li, Xiaoying Tang, Tianshu Yu, Yiwen Guo  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 16.0  
**Type**: new  
**ArXiv ID**: 2608.10720v1  

#### Abstract
Omni-modal dialogue models can understand multimodal inputs and synthesize spoken replies, yet their responses remain visually disembodied. We introduce \textbf{Ex-Omni-2D}, an omni-modal dialogue framework that generates a coordinated response comprising text, personalized speech, and reference-con...

---

### 29. [SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training](https://arxiv.org/abs/2608.11034v1)

**Authors**: Zhuang Wang  
**Category**: cs.DC  
**Published**: 2026-08-12  
**Score**: 16.0  
**Type**: new  
**ArXiv ID**: 2608.11034v1  

#### Abstract
In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin. Existing diagnosis often relies on in-process monitors that cannot report after the trainer blocks or terminates, or on post-mortem logs that preserve on...

---

### 30. [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915v1)

**Authors**: Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Wang, Kelong Mao, Hao Sun, Zhiyao Luo, Jiankai Tang, Lei Li, Jiadong Guo, Minheng Ni, Weicong Lin, Chenxi Yang, Hongxiang Gao, Zhenghua Chen, Yang Bai, Min Wu, Jun Cheng, Huazhu Fu, Dacheng Tao, Bang Liu  
**Category**: cs.AI  
**Published**: 2026-08-12  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2608.10915v1  

#### Abstract
After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural...

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
