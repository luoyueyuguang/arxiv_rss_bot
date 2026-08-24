# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-24 06:25:32 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21265v1)

**Authors**: Simeng Zhang, Yilong Chen, Wenyuan Zhang, Zhenyu Zhang, Yao Chen, Junyuan Shang, Tingwen Liu  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 75.5  
**Type**: new  
**ArXiv ID**: 2608.21265v1  

#### Abstract
Large language models often rely on Chain-of-Thought (CoT) reasoning to solve complex tasks, but verbose reasoning traces introduce substantial inference overhead. CoT compression shortens generation, yet aggressive compression may disrupt logical coherence and degrade performance. We formalize this...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：Chain-of-Thought（CoT）推理依赖冗长的推理轨迹解决复杂任务，带来巨大推理开销；CoT压缩虽可缩短生成过程，但过度压缩会破坏逻辑一致性、降低性能，该研究将这一trade-off形式化为Context-Generation Substitution Law，提出显式推理上下文可替代部分解码时生成的思路，但现有CoD压缩等方法未有效弥补压缩过程中的信息损失，存在性能缺陷。
🚀 提出的新方法与思路：**Memory-Augmented Compression**，这是一种训练无关的框架，从历史推理轨迹中构造可复用的推理记忆，将该记忆作为prefill侧的检索支架；该记忆并非原始演示，而是总结可复用的推理模式、关键约束和核心操作，用于补偿压缩过程中的信息损失。
🔍 相比现有方法的优势
| 维度 | 优势 |
--- | ---
GSM8K任务准确率 | 相比CoD获得21.4点的准确率提升
MATH任务准确率 | 相比CoD获得28.0点的准确率提升
BBH任务准确率 | 相比CoD获得29.5点的准确率提升
MMLU-Sci任务准确率 | 相比CoD获得6.61点的准确率提升
推理延迟 | 相比标准CoT实现1.14--1.49×的延迟加速
压缩机制兼容性 | 兼容token-level、推理-trace-level、推理-state compression三类压缩机制
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
--- | ---
GSM8K | 数学推理任务
MATH | 数学推理任务
BBH | 复杂推理任务
MMLU-Sci | 科学问答任务
🎯 实验设置与评估指标
一句话：实验针对数学推理、复杂推理、科学问答任务开展，评估指标为准确率（↑越高越好）和延迟加速比（↑越高越好）。
| 指标 | 含义 |
--- | ---
准确率 | 衡量推理结果的正确程度，数值越高表示性能越好
延迟加速比 | 衡量推理速度的提升幅度，数值越大表示推理速度越快
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
--- | --- | ---
Chain-of-Draft（CoD） | 压缩型CoT基线 | 尝试缩短CoT推理轨迹但存在压缩后信息丢失的问题
标准CoT | 传统CoT基线 | 推理轨迹冗长，推理开销大
3. 主要实验结果和性能指标
📊 定量结果汇总
**表：未明确编号（多任务性能与效率对比场景）**
| 评估内容 | 指标值 | 对比基准 |
--- | --- | ---
GSM8K准确率提升 | 21.4点 | CoD
MATH准确率提升 | 28.0点 | CoD
BBH准确率提升 | 29.5点 | CoD
MMLU-Sci准确率提升 | 6.61点 | CoD
推理延迟加速比 | 1.14--1.49× | 标准CoT
💡 结论：Memory-Augmented Compression在多个推理任务上相比CoD压缩方法大幅提升准确率，同时相比标准CoT实现显著的推理速度提升。
其他实验情况：
1. 主 benchmark性能：如上表所示
2. 效率对比：如上表中的延迟加速比项
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- Memory-Augmented Compression的性能提升来源于可复用的推理记忆，而非单纯增加上下文长度。
- 该方法在数学推理、复杂推理、科学问答任务上，相比CoD压缩方法均获得显著的准确率提升，同时实现推理延迟的加速。
- 该框架兼容token级、推理轨迹级、推理状态级三类压缩机制，适用范围较广。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：该论文提出训练无关的Memory-Augmented Compression框架，通过构造和检索可复用的推理记忆弥补CoT压缩的信息损失，在提升多类推理任务准确率的同时降低了推理延迟。

</details>

---

### 2. [Enabling Memory-efficient Im2win Convolution with Multi-precision Support on GPU CUDA and Tensor Cores](https://arxiv.org/abs/2608.20725v1)

**Authors**: Xiang Fu, Jixiang Ma, Xinpeng Zhang, Peng Zhao, Shuai Lu, Xu Tony Liu  
**Category**: cs.DC  
**Published**: 2026-08-24  
**Score**: 64.5  
**Type**: new  
**ArXiv ID**: 2608.20725v1  

#### Abstract
Convolution is a principal computational bottleneck in deep neural networks, and its efficiency depends on tight integration between algorithms and GPU hardware. Existing GPU convolution methods suffer from large memory overhead, poor cache utilization, limited effectiveness across kernel sizes, or ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Enabling Memory-efficient Im2win Convolution with Multi-precision Support on GPU CUDA and Tensor Cores
1. 论文的主要贡献和创新点
解决的问题：卷积是深度神经网络的主要计算瓶颈，其效率依赖于算法与GPU硬件的紧密整合，现有GPU卷积方法存在大内存开销、缓存利用率低、对不同核尺寸效果有限或数值不稳定的缺陷。
提出的新方法与思路：**Im2win卷积范式扩展**：将通用、内存高效（所有核尺寸均具备连续内存访问能力）的im2win卷积范式扩展为可在CUDA核心上以全精度、在张量核心上以半精度高效运行的方案，通过引入zig-zag内存访问、异步数据移动等新内核设计与优化，充分利用硬件加速的半精度矩阵乘累加操作。
相比现有方法的优势：
| 维度 | 优势 |
| ---- | ---- |
| 计算性能 | 在十二种CNN基准测试中，im2win的计算性能高于CUDA核心实现、cuDNN及基于cuBLAS的GEMM卷积方法 |
| 内存开销 | im2win的内存开销低于cuDNN及基于cuBLAS的GEMM卷积方法 |

2. 核心实验方法和设置
使用的数据集：
| 数据集 | 用途 |
| ---- | ---- |
| 十二种CNN基准测试 | 卷积性能评估 |
实验设置与评估指标：
任务：现代GPU架构下深度神经网络卷积运算的性能与内存效率评估。
| 指标 | 含义 |
| ---- | ---- |
| TFLOPS | 计算性能（越高越好） |
| 内存占用 | 内存开销（越低越好） |
基线方法对比：
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| CUDA core实现 | GPU CUDA核心卷积实现 | 存在大内存开销等缺陷 |
| cuDNN | NVIDIA cuDNN库卷积实现 | 存在大内存开销等缺陷 |
| GEMM-based convolution with cuBLAS | 基于cuBLAS的GEMM卷积实现 | 存在大内存开销等缺陷 |

3. 主要实验结果和性能指标
1. 主 benchmark 性能：论文未报告具体每个基准的详细数值，仅报告在十二种CNN基准测试中im2win计算性能高于对比方法，结论：im2win在十二种CNN基准测试中展现出更高的计算性能。
2. 效率对比（FPS / 参数量）：论文未报告FPS、参数量指标，未提供TFLOPS及内存占比相关结果的来源信息，无法给出具体数值，结论：论文未报告FPS、参数量及对应来源明确的TFLOPS与内存占比对比的具体数值。
3. 跨域 / zero-shot 迁移：论文未报告。
4. 鲁棒性 / 扰动测试：论文未报告。
5. 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：1. im2win可作为适配现代GPU架构的统一卷积框架，兼顾高计算性能与低内存开销；2. 多精度支持结合zig-zag内存访问、异步数据移动等优化，可有效提升im2win对GPU硬件资源的利用率。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：该工作扩展im2win卷积范式，实现了兼顾高计算性能与低内存开销的GPU卷积方案，优于现有主流GPU卷积方法。

</details>

---

### 3. [Why2Speak: Faithful Reasoning for Abstaining Action Policies](https://arxiv.org/abs/2608.20670v1)

**Authors**: Shreya Mendi, Brinnae Bent  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2608.20670v1  

#### Abstract
Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Why2Speak: Faithful Reasoning for Abstaining Action Policies
1. 论文的主要贡献和创新点
✅ 解决的问题
多-party对话的干预时机场景中，agent需在发言（执行行动）与沉默（弃权）间决策，该场景存在类别不平衡、动作成本不对称，且暴露推理可能改变被审计策略；当前存在能力-可审计性的核心权衡：现有直接决策策略决策质量高但无可审计的推理，带推理的决策策略有可追溯的推理但决策性能差（尤其真干预机会的召回率低），监督微调（SFT）、强化学习（RL）等方法无法改善推理策略，标准推理可审计方法（概率指标、控制激活探针、推理消融）存在缺陷（概率指标在置信度高的决策下饱和，探针受类别不平衡和文本泄露影响，推理消融混淆推理内容与推理模式变化）。

🚀 提出的新方法与思路
**可行动-弃权Agent的推理型监督评估控制方法**：用于解决标准推理可审计方法的缺陷，实现对需在发言与沉默间决策的Agent的推理型监督的有效评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理可审计评估 | 针对可执行行动或弃权的Agent提供专用控制方法，解决标准推理审计方法的缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为多-party对话场景下Agent判断是否发言（执行行动）或沉默（弃权）的决策任务，论文未报告具体评估指标。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| direct decision policies | 直接决策策略 | 决策质量高，但无推理可供审计 |
| reasoning policies | 带推理的决策策略 | 提供可追溯的推理，但决策性能差，尤其真干预机会的召回率低 |
| supervised fine-tuning | 监督微调 | 要么抑制推理，要么保留推理但不提升决策质量 |
| reinforcement learning | 强化学习 | 无法改善推理策略的决策性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告所有定量结果及对应表号、图号，相关实验内容均来自摘要描述。

4. 关键结论和发现
- 多-party对话场景下，Agent需在发言与沉默间决策，存在能力与推理可审计性的核心权衡，不同决策与训练方法无法同时兼顾两点，各有缺陷。
- 现有标准推理可审计方法存在明显缺陷，无法准确评估暴露推理的忠实性；且暴露推理会直接改变Agent的动作策略，而非仅使其可观测。
- 论文针对需在行动与弃权间决策的Agent的推理型监督评估问题，提供了专用控制方法解决现有方法的缺陷。

方法局限性
论文未报告

未来工作
论文未报告

> ✅ **总结一句话**：论文围绕多-party对话中Agent发言/弃权决策的推理可审计问题，对比不同决策与训练方法表现，揭示了能力-可审计性权衡及现有推理审计方法的缺陷，并提供了相关评估控制方法。

</details>

---

### 4. [Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models](https://arxiv.org/abs/2608.20975v1)

**Authors**: Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 57.5  
**Type**: new  
**ArXiv ID**: 2608.20975v1  

#### Abstract
Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap be...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有理论心智（Theory of Mind, ToM）相关基准测试将ToM推理与具身行为分开评估，未测量社会推理到社会行动的翻译差距；当前多数Vision-Language Models（VLMs）存在无法产生符合ToM顺序约束的行为、显式强制ToM约束未引发可靠对齐行为、信号层面非言语信号方向连贯性缺失、无法解释并响应他人行为等问题，无法完成多模态协调社会行动任务。

🚀 提出的新方法与思路
**MOSAIC基准测试**：构建了受控的多模态基准场景，包含两个具身智能体在合作、竞争两类场景下的交互，任务要求整合言语陈述、空间轨迹、视线方向、面部表情多模态信号，且存在系统变化的ToM约束，用于评估模型将心智状态推理转化为协调社会行动的能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估全面性 | 首次构建基准测试测量社会推理到社会行动的翻译差距，集成多模态信号与系统可变的ToM约束 |
| 评估针对性 | 可定位模型在ToM转化为行动过程中的信号处理、行为输出、交互响应等顺序瓶颈 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 构建受控的多模态社会交互场景，支持对13个模型（含11个VLMs和PCM-LLM）的200次试验/模型评估 |

🎯 实验设置与评估指标
实验任务为：模型作为具身智能体，在合作或竞争的受控场景中，整合言语、空间、视线、面部表情信号，在系统变化的ToM约束下产生协调的社会行动。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 评估核心为ToM约束下的社会行动协调表现，包括行为与预期结果的一致性、非言语信号方向连贯性、对他人行为的解释与响应能力 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PCM-LLM | 结构化架构参考点 | 包含显式ToM模块，在所有实验条件下均成功完成任务 |
| 11个VLMs | Vision-Language Models | 多数模型无法产生符合ToM顺序约束的行为，存在信号和交互响应层面的瓶颈 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（论文未报告表号）**
论文未报告该主benchmark性能的具体表号、指标数值及对应表格，仅定性报告相关结果。
💡 结论：论文未明确针对主benchmark性能给出对应结论，仅定性呈现实验发现。
（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等：论文未报告）

4. 关键结论和发现
- 主要发现：1. 多数VLMs存在ToM推理到协调社会行动的显著差距，无法产生符合ToM顺序约束的行为，即使强制施加显式ToM约束也未引发可靠对齐行为；2. 模型在ToM转化为行动的过程中存在两个顺序瓶颈：多数模型无法产生方向连贯的非言语信号，即使存在非言语信号，也无法解释并响应他人的行为；3. 带有显式信念-行动耦合设计的PCM-LLM在所有实验条件下均成功完成任务，证实显式的信念-行动耦合是该类任务的充分要素。
- 方法局限性：论文未报告该方法的局限性相关内容。
- 未来工作：论文未报告未来工作的具体内容。

> ✅ **总结一句话**：该研究通过提出受控多模态基准MOSAIC，揭示了Vision-Language Models在心智状态推理到协调社会行动翻译中的瓶颈，证实显式信念-行动耦合对完成该类任务的关键作用。

</details>

---

### 5. [Self-Speculation for Faster Reasoning Models](https://arxiv.org/abs/2608.20359v1)

**Authors**: Ravisri Valluri, Tung Nguyen, Aditya Grover  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2608.20359v1  

#### Abstract
Large language models (LLMs) are deployed for increasingly complex tasks involving planning and multi-step decision making, but high-quality performance on these tasks often requires generating long reasoning traces. This is a poor fit for latency-sensitive and interactive applications like voice as...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Self-Speculation for Faster Reasoning Models
1. 论文的主要贡献和创新点
✅ 解决的问题
大型语言模型（LLMs）处理需要长推理轨迹的复杂任务时，生成延迟高，无法适配语音助手、编码代理等延迟敏感的交互式应用；现有加速方法仅聚焦于token级生成，未利用推理工作流的结构。

🚀 提出的新方法与思路
**SSR（Self-Speculation for Reasoning Models）**：这是一种training-free的自推测解码方法，核心思路是利用同模型不同推理预算下的链式思考（CoT）分布：将部分CoT答案分布作为draft，全CoT分布作为verifier；观察到后期部分CoT响应与全预算响应存在更大的语义和词汇重叠，因此可一次性接受更长的draft前缀；额外加入**suffix decoding**模块，用draft初始化后缀缓存，恢复接受前缀之外的有用片段，进一步降低词汇重叠较高任务的延迟。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 延迟优化 | 利用推理轨迹结构实现比仅token级加速方法更大幅度的延迟降低 |
| 结构利用 | 首次结合同模型不同推理预算的CoT分布，挖掘推理工作流的结构信息 |
| 适用性 | 无需额外训练（training-free），可直接应用于现有开源模型 |
| 任务适配性 | 适配结构化、长文本生成任务，处理长推理轨迹带来的延迟问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 多个结构化和长文本生成任务（具体名称未报告） | 评估SSR的性能 |

🎯 实验设置与评估指标
任务为加速LLM的长推理轨迹生成，适配延迟敏感的交互式应用；
| 指标 | 含义 |
| ---- | ---- |
| 总生成延迟 | ↓ 越低越好 |
| 相对延迟改进率 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有token级生成加速方法 | 基线方法 | 聚焦于token级生成，未利用推理工作流结构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果对应的表号、图号或章节来源，仅提及在Qwen3.5和Gemma-4等开源模型上，总生成延迟存在相对改进。
💡 结论：SSR在Qwen3.5、Gemma-4等开源模型上可实现总生成延迟的改进，适配长推理生成任务。
其他实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）均未报告。

4. 关键结论和发现
- 主要发现
1. 同模型不同推理预算下的CoT分布存在语义和词汇重叠，利用该特性可实现更长draft前缀的接受，进而提升推理效率；
2. 加入suffix decoding恢复前缀外的有用片段，可进一步降低高词汇重叠任务的生成延迟；
3. SSR可直接应用于Qwen3.5、Gemma-4等开源模型，适配延迟敏感的交互式应用场景。
- 方法局限性：论文未报告明确的方法局限性。
- 未来工作：论文未报告未来工作方向。

> ✅ **总结一句话**：提出training-free的自推测解码方法SSR，通过利用同模型不同推理预算的CoT结构并结合suffix decoding，可在不额外训练的情况下有效降低长推理生成任务的总延迟，适配延迟敏感的交互式应用场景。

</details>

---

### 6. [RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation](https://arxiv.org/abs/2608.20845v1)

**Authors**: Kyle Wild, Yusuke Takahashi, Asako Uraki  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.20845v1  

#### Abstract
Nearly every retrieval-augmented question-answering system in production ships with a hidden interpreter: on each query a language model re-derives the meaning of raw corpus text and then throws that work away. Cheaper models do not close the gap: per-token prices have fallen by orders of magnitude ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation
1. 论文的主要贡献和创新点
✅ 解决的问题
当前生产中的检索增强问答系统均依赖隐藏的 interpreter，每次查询时语言模型需重新推导原始语料文本的含义后丢弃该工作；per-token价格大幅下降但推理开销上升，因上下文体积增长快于价格下降，这对应现代版全表扫描；数据库早有写时处理的成熟思路，但RAG系统此前未采用该方案。
🚀 提出的新方法与思路
**Ingest-Time Semantic Compilation (ISC)**：将语料的含义编译为可查询的底物，包含两个耦合层：一是增量维护的embeddings，二是编译时经来源验证的原子声明；将该底物作为一级数据库对象，配备独立的DDL、维护契约、迁移契约与成本模型。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 查询资源消耗 | 编译后查询时仅需更少的reader tokens即可达到更高准确率 |
| 底物维护成本 | 增量更新比全量重建便宜33.7倍，同时保持浮点精度跟踪 |
| 问答性能 | 赢下所有32个budget-by-model cells，优于最优传统chunk配置 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 500条held-out广播采访转录本 | 测试ISC方法在RAG问答任务上的核心性能 |
🎯 实验设置与评估指标
任务为RAG问答任务；
| 指标 | 含义 |
| --- | --- |
| 问答正确率 | 越高越好 |
| 查询路径token数 | 越低越好（数值越小表示查询时资源消耗越低） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| best chunk configuration | 传统RAG chunk方法 | 实验中对比的最优传统chunk配置 |
| contextualized-chunk pipeline（带混合检索与重排序） | 改进的传统RAG方法 | 作为强基线，与compiled claims准确率统计无差异，但查询token数极高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**广播采访转录本问答实验**
| 方法 | 问答正确率 | 查询时reader token数 |
| --- | --- | --- |
| ISC的compiled claims | 85.2% ✅（赢下所有32个budget-by-model cells） | 约2.2k |
| best chunk configuration | 72.5% | 16.3k |
| contextualized-chunk pipeline（带混合检索与重排序） | 与compiled claims统计无差异 | 约为compiled claims的21倍 |
**底物维护效率实验**
| 底物更新方式 | 开销对比 | 精度 |
| --- | --- | --- |
| ISC的增量更新 | 比全量重建便宜33.7倍 | 跟踪到浮点精度 |
💡 结论：在held-out的500条广播采访转录本的RAG问答任务中，ISC的compiled claims方法以仅约1/7的查询reader token数达到比最优chunk配置更高的准确率，且赢下所有32个budget-by-model cells；其性能与带混合检索重排序的强基线contextualized-chunk pipeline相当，后者需21倍的查询路径token数；ISC的底物增量维护成本远低于全量重建，同时保持浮点精度。
论文未报告主benchmark性能、效率（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验相关内容。

4. 关键结论和发现
- 主要发现：① ISC范式将RAG核心处理从查询时转移到摄取时，大幅降低查询阶段资源消耗的同时提升问答性能；② 带混合检索重排序的contextualized-chunk pipeline虽准确率接近ISC，但高查询开销本质是自行做了类似编译的工作；③ ISC底物维护效率极高，增量更新成本远低于全量重建且保持精度。
- 方法局限性：论文未报告
- 未来工作：围绕编译规划、读取规划展开的系统层面研究
> ✅ **总结一句话**：本文提出的ISC范式通过将语料编译为可查询的底物，突破传统RAG“查询时重推导”的性能瓶颈，以极低的查询资源消耗实现更高的问答准确率，是数据库写时处理思路在RAG领域的创新应用。

</details>

---

### 7. [AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification](https://arxiv.org/abs/2608.20711v1)

**Authors**: Ji Liu, Puyuan Yang, Rongzhang Zheng, Fan Wang, Jinglin Wang, Muhammad A. Awad, Mortis Huang, Andy Chang, Zekai Li, Zeping Li, Zihao An, Yue Liu, Yuchen Yang, Jianghui Wang, Chushi Chen, Ziqiong Liu, Fuwei Yang, Dong Li, Wen Heng Chung, Shengcai Liu, Emad Barsoum  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2608.20711v1  

#### Abstract
High-performance ML systems increasingly rely on GPU kernels whose editable source is unavailable, generated, or too distant from final machine code to expose remaining optimizations. Existing LLM kernel optimizers and autotuners mainly operate on CUDA, Triton, HIP, or tensor-program source and vali...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM kernel优化器和自动调参工具主要针对CUDA、Triton、HIP或张量程序源码，且基于参考实现进行验证，存在不足：①无法处理内核源码不可用、已生成或与最终机器码脱节的场景；②针对已编译AMDGPU代码对象的优化研究不足，无法在部署二进制为唯一行为预言机的严格场景下优化内核。

🚀 提出的新方法与思路
**Agentic Assembly-Level Optimizer AsmEvo**
给定AMDGPU代码对象K0，依次完成：1. 重建可重汇编的表示；2. 利用长序列智能体提出低级编辑；3. 构建符合应用二进制接口（ABI）的优化代码对象；4. 通过与K0在相同启动条件下的差分验证，接受符合功能等价的候选，集成代码对象恢复、元数据感知重建、基于分析的热窗口编辑、正确性门限时序验证、保守就地补丁回退模块。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 优化场景 | 针对已编译AMDGPU代码对象的汇编级优化，而非源码级优化 |
| 行为验证依据 | 以部署的二进制代码对象为唯一行为预言机，而非依赖参考实现 |
| 源码依赖 | 不依赖可编辑源码，适用于源码不可用、生成或与最终机器码脱节的场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 各种AMD GPU kernels、MI308X上的30个选定KernelBench kernels、MI300X生产负载（含AITer二进制、vLLM/SGLang Triton汇编内核） | 评估AsmEvo在常规基准内核及实际生产工作负载上的优化效果 |

🎯 实验设置与评估指标
任务：优化AMD GPU kernels，在目标GPU（MI308X、MI300X）上评估性能提升。
| 指标 | 含义 |
| --- | --- |
| 几何均值速度提升 | 所有评估内核性能提升倍数的均值，越高越好 |
| 最大速度提升 | 单个内核的最高性能提升倍数，越高越好 |

⚔️ 基线方法对比
论文未报告具体基线方法列表。

3. 主要实验结果和性能指标
📊 定量结果汇总
**KernelBench kernels (MI308X)**
| 指标 | 数值 |
| --- | --- |
| 几何均值速度提升 | 1.35x ✅ |
| 最大速度提升 | 3.88x ✅ |
💡 结论：在MI308X平台的30个KernelBench内核中，AsmEvo优化了29个内核，实现了明显性能提升。

**MI300X生产负载**
| 负载类型 | 几何均值速度提升 | 最大速度提升 |
| --- | --- | --- |
| AITer二进制 | 1.09x ✅ | 1.31x ✅ |
| vLLM/SGLang Triton汇编内核 | 1.18x ✅ | 1.34x ✅ |
💡 结论：在MI300X平台的各类评估生产负载上，AsmEvo对所有评估目标均实现性能提升，且保证功能等价。

其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告。

4. 关键结论和发现
- 主要发现
1. AsmEvo可针对已编译AMDGPU代码对象完成汇编级优化，无需依赖可编辑源码；
2. 在MI308X平台的KernelBench基准内核中，AsmEvo实现29/30内核的性能优化，几何均值1.35x、最大3.88x速度提升；
3. 在MI300X平台的生产负载中，AsmEvo对所有评估目标均实现性能提升，且保持功能等价。
- 方法局限性
论文未报告AsmEvo的局限性。
- 未来工作
论文未明确报告未来工作计划。

> ✅ **总结一句话**：AsmEvo是面向已编译AMDGPU代码对象的代理式汇编级优化方法，通过功能等价验证，可有效提升MI308X和MI300X系列AMD GPU上多款内核的性能。

</details>

---

### 8. [LiLiCorr: Lightweight Likelihood Correlation of Parallel Drafts for Speculative Decoding](https://arxiv.org/abs/2608.20530v1)

**Authors**: Matan Rusanovsky, Yoav Miron, Roy Uziel, Omer Belhasin, Ran Zilberstein, Maor Ashkenazi, Michael Elad  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.20530v1  

#### Abstract
Speculative decoding accelerates language-model inference by drafting future tokens that the target model verifies in parallel. A diffusion-style block head such as DFlash is an attractive drafter, predicting an entire block of future tokens in one forward pass. However, it is trained on per-positio...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LiLiCorr: Lightweight Likelihood Correlation of Parallel Drafts for Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题：用于推测解码的扩散式块头draft模型（如DFlash）基于 per-position marginals训练而非联合块分布，生成的token单个合理但联合不连贯，制约推测解码性能。

🚀 提出的新方法与思路
**LiLiCorr（Lightweight Likelihood Correlation）**：是一种轻量似然关联模型，用于关联draft模型已产生的per-position边际分布。具体实现：1）保留每个位置的top-k token作为候选，联合处理所有候选，为每个候选生成入向量和出向量；2）依据相邻候选中前者出向量与后者入向量的高余弦相似度判定匹配，以此捕获块的联合结构，无需生成完整联合分布；3）仅需一次轻量网络前向即可得到所有向量，成对分数通过成批矩阵运算并行计算，仅贪心走为顺序操作；4）联合训练drafter与LiLiCorr，使drafter学习生成可关联为更长接受序列的优质候选。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 接受长度 | 在vanilla DFlash drafter上，各基准接受长度提升9%至19% |
| 每块延迟 | scoring head仅占约2.8%的每块延迟 |
| 吞吐量 | 在70/72个测试设置中取得最高吞吐量，测试场景涵盖9个基准、2种目标模型大小、贪心/温度1解码，及吞吐量扫描下的6个并发数、2种输入长度、3个熵层级 |
| 长输入泛化 | 扩展至比训练时大一个数量级的输入后，仍保持性能领先 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：推测解码加速语言模型推理任务，针对draft token的联合连贯性优化。
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| 接受长度 | 推测解码中被目标模型验证通过的序列长度，↑越长越好 |
| 每块延迟 | 处理一个draft块的耗时，↓越短越好 |
| 吞吐量 | 单位时间内处理的token数，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| DFlash | 扩散式块头draft模型 | 基于 per-position marginals训练，生成token联合连贯性差 |
| 两种并行的、恢复draft时连贯性的方法 | 对比方法 | 用于与LiLiCorr的吞吐量等性能对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未报告具体表号：主benchmark性能（推测解码任务）**
| 指标 | 结果 |
| ---- | ---- |
| 各基准接受长度提升 | 9%至19% |
| 每块延迟占比 | 约2.8% |
| 吞吐量最优设置占比 | 70/72 ✅ |
| 长输入扩展性能 | 保持领先 |
💡 结论：LiLiCorr可显著提升推测解码的接受长度，同时仅引入极低延迟开销，在多场景下取得优于对比方法的吞吐量性能，且具备良好的长输入泛化能力。

4. 关键结论和发现
- 主要发现：① LiLiCorr通过关联draft token的边际分布，有效捕获块的联合结构，解决了现有draft token联合不连贯的核心问题；② 联合训练drafter与LiLiCorr可生成更优质的候选，进而提升接受长度；③ LiLiCorr在多维度性能上优于DFlash及其他对比方法，吞吐量表现突出。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：LiLiCorr是轻量似然关联模型，通过优化推测解码中draft token的联合连贯性，在提升接受长度的同时保持低延迟，显著增强了推测解码的吞吐量性能。

</details>

---

### 9. [StateSight: Benchmarking Latent Spatial-State Reconstruction in Vision-Language Models](https://arxiv.org/abs/2608.20414v1)

**Authors**: Michelle Lin  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.20414v1  

#### Abstract
Vision-language models are increasingly used for multimodal question answering, yet their ability to reconstruct latent spatial structure from a single image remains difficult to isolate. Broad benchmarks often combine perception, optical character recognition, domain knowledge, linguistic priors, a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：StateSight: Benchmarking Latent Spatial-State Reconstruction in Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有Vision-language models（VLMs）用于多模态问答时，难以隔离评估其从单张图像重建潜在空间结构的能力；
- 广泛使用的通用基准评估将感知、光学字符识别（OCR）、领域知识、语言先验与推理任务混合，无法聚焦空间状态重构能力的评估。

🚀 提出的新方法与思路
**StateSight**：一个基于程序生成的基准，包含Cube-Net对面推理、occluded cube-tower计数、4邻接连通分量计数三个任务系列，每个任务系列各有300个单图像提示，配备确定性oracle标签，采用精确匹配评分机制；
**StateSight-Steps**：配套数据集，包含900个交错的图像文本示例和3600个确定性中间视觉状态。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估针对性 | 聚焦空间状态重构任务，避免混合感知、OCR等其他任务能力 |
| 评分客观性 | 配备确定性oracle标签，采用精确匹配评分，结果可复现 |
| 过程可追溯性 | 配套StateSight-Steps提供中间视觉状态，支持分析空间重构过程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| StateSight | 基准评估，覆盖Cube-Net对面推理、occluded cube-tower计数、4邻接连通分量计数三个任务 |
| StateSight-Steps | 配套用于空间重构过程的分析 |

🎯 实验设置与评估指标
实验任务为三个空间状态重构任务：Cube-Net opposite-face reasoning、occluded cube-tower计数、4-neighbor connected-component counting；评估指标为准确率（↑，数值越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPT-5.5 | API模型 | 模型标识为gpt-5.5 |
| Claude Sonnet5 | 模型 | - |
| 人类基线 | 人类参与者 | 30名参与者，基于60个项目的评估 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅主benchmark性能有报告，其余实验论文未报告：

**表？（论文未报告表号）：StateSight基准三个任务性能**
| 方法 | Cube-Net对面推理准确率 | occluded cube-tower计数准确率 | 4邻接连通分量计数准确率 |
| --- | --- | --- | --- |
| GPT-5.5 | 59.3% | 33.3% | 28.3% |
| Claude Sonnet5 | 53.3% | 18.7% | 7.3% |
| 人类基线 | 80.8% ✅ | 68.8% ✅ | 64.3% ✅ |
💡 结论：在StateSight基准的三个空间状态重构任务中，人类基线的准确率均显著高于GPT-5.5和Claude Sonnet5，两类模型的性能整体较低，且不同任务间存在明显差异。

其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告。

4. 关键结论和发现
- 格式有效的响应可能掩盖VLMs恢复可验证视觉推理所需空间结构的失败；
- StateSight基准的实验结果显示，GPT-5.5和Claude Sonnet5在空间状态重构任务上的表现远低于人类；
- 现有混合多任务的通用基准难以评估VLMs的潜在空间结构重建能力。
方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：论文提出了针对VLMs潜在空间状态重构能力的StateSight基准及配套数据集，实验表明现有模型在该任务上的表现远逊于人类，且格式正确的响应可能掩盖空间结构恢复的缺陷。

</details>

---

### 10. [CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting](https://arxiv.org/abs/2608.20771v1)

**Authors**: Zixi Zhu, Jiayuan Su, Jian Zhang, Yu Lin, Hongwei Wang  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2608.20771v1  

#### Abstract
Search Agents face a severe reliability crisis during reinforcement learning (RL) fine-tuning. Heuristic Top-K retrieval often causes critical evidence loss or noise inclusion, while over-confidence induced by progressive RL leads to hallucinated answers and redundant searches.
  To build highly rel...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting
1. 论文的主要贡献和创新点
✅ 解决的问题
搜索智能体在强化学习（RL）微调过程中存在严重的可靠性危机，核心痛点为两类方法的缺陷：
- 启发式Top-K检索方法：易导致关键证据丢失或引入噪声；
- 渐进式RL微调方法：存在过度自信问题，引发答案幻觉与冗余搜索。

🚀 提出的新方法与思路
**Adaptive Prediction Set (APS)**：作为Conformal Prediction（CP）的特定实现，在检索侧将统计覆盖率转化为动态文档截断规则，构建大小自适应的预测集。
**Adaptive Conformal Inference (ACI)**：作为动态CP算法，在训练端动态构建具有可控覆盖率的预测集以量化答案置信度，将该置信度用于Group Relative Policy Optimization（GRPO）目标中以惩罚低置信度轨迹，确保模型仅从可靠轨迹学习。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理准确性 | 显著提升问答任务的推理准确率 |
| 检索效率 | 大幅减少冗余工具调用 |
| 可靠性保障 | 分别在检索侧与训练侧建立了明确的可靠性保证 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Single-hop QA datasets、Multi-hop QA datasets | 验证CAS框架在单跳、多跳问答任务中的有效性 |

🎯 实验设置与评估指标
任务为单跳与多跳问答（QA）任务，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 推理准确率 | ↑ 越高越好 |
| 冗余工具调用次数 | ↓ 越低越好 |

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 提出的CAS框架通过在检索侧应用Adaptive Prediction Set（APS）、在训练侧应用Adaptive Conformal Inference（ACI）结合Group Relative Policy Optimization（GRPO），有效解决了搜索智能体在RL微调中的可靠性危机；
- 该框架在单跳与多跳问答任务中，同时实现了推理准确率的显著提升与冗余工具调用的大幅减少；
- CAS为构建具备可靠性与高效性的智能体范式提供了新的技术路径。

方法局限性：论文未报告
未来工作：论文未报告

> ✅ **总结一句话**：本文提出了Conformalized Agentic Search（CAS）框架，通过自适应检索与基于置信度的策略加权方法，解决了搜索智能体在RL微调中的可靠性危机，在问答任务上实现了推理准确率提升与冗余搜索减少的双重优化。

</details>

---

### 11. [Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation](https://arxiv.org/abs/2608.20797v1)

**Authors**: Pengshuai Yang, Zijing Gao, Xue Yu, Benhui Zhuang, Bo Yuan, Junlan Feng  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.20797v1  

#### Abstract
Evaluating language-guided mobile agents has recently shifted from rule-based to model-based approaches to achieve scalable and automated assessments. However, existing holistic evaluation paradigms process entire trajectories at once, leading to substantial context overload. Moreover, they primaril...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于评估语言引导移动智能体的自动化评估方法，从规则范式转向模型范式以实现可扩展评估，但存在两个核心痛点：一是采用整体轨迹的处理方式导致严重的上下文过载；二是评估过程主要聚焦于任务完成情况，忽略了移动智能体的操作安全维度。

🚀 提出的新方法与思路
**CRATE**：提出一种两阶段VLM-as-judge框架，兼容开放和闭源模型。采用步骤级结果推理机制，在每个步骤独立提取与任务相关的视觉线索、推理由动作引发的状态变化，生成步骤级文本证据后，通过轨迹级聚合合成用于评估任务完成情况的、有证据支撑的结论。
**CRATE-S**：在CRATE的评估方案基础上扩展得到的移动智能体操作安全评估方法。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估范式 | 采用步骤级处理逻辑，避免整体轨迹处理带来的上下文过载问题 |
| 评估维度 | 扩展出安全评估分支CRATE-S，补充现有方法忽略的操作安全评估维度 |
| 模型兼容性 | 兼容开放源与闭源VLM模型，适用性广 |
| 评估可解释性 | 基于步骤级证据聚合得出评估结论，具备可追溯性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| AndroidWorld | 移动智能体任务完成情况的自动化评估（主benchmark） |
| MobileRisk | 移动智能体操作安全的自动化评估（CRATE-S测试集） |

🎯 实验设置与评估指标
实验任务为语言引导移动智能体的轨迹评估，涵盖任务完成与操作安全两个维度。
| 指标 | 含义 |
| ---- | ---- |
| F1-score | 评估评估结果与基准真值的对齐程度（↑越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SPA-Bench | 自动化评估方法 | 现有采用整体轨迹处理的移动智能体评估方法，为本文的对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能
CRATE（基于Qwen2.5-VL-72B-Instruct）在AndroidWorld数据集上的F1-score为0.833，相比基线方法SPA-Bench提升20%；CRATE-S在MobileRisk数据集上的F1-score为0.697。
💡 结论：CRATE在移动智能体任务完成评估上性能优于现有基线，CRATE-S在操作安全评估上与基准真值具备良好对齐性。

2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 提出的CRATE框架通过步骤级推理与聚合机制，有效解决了现有整体轨迹评估范式的上下文过载问题；② 扩展的CRATE-S框架可支持移动智能体的操作安全评估，填补了现有方法的维度缺失；③ 基于Qwen2.5-VL-72B-Instruct的CRATE任务评估性能优于基线方法SPA-Bench。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出兼容多类型VLM的CRATE与CRATE-S框架，实现了移动智能体轨迹的自动化评估，同时覆盖任务完成与操作安全两个维度，性能优于现有基线方法。

</details>

---

### 12. [Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf](https://arxiv.org/abs/2608.20370v1)

**Authors**: Michael Wang, Yikang Yue, Shaobo Li, Yirui Eric Zhou, Chen Wang, Jian Huang  
**Category**: cs.DC  
**Published**: 2026-08-24  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2608.20370v1  

#### Abstract
We present XPerf, a benchmarking framework that load-tests LLM serving systems with diverse agentic AI workloads. It provides detailed profiling of the serving system and hardware, enabling users to identify performance bottlenecks introduced by agentic workloads. Benchmarking LLM serving systems un...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM serving系统的基准测试面临agentic AI workload带来的核心挑战：agentic应用依赖非确定性LLM输出控制流，导致工作负载模式每次运行都不可预测，无法在不同服务系统上进行稳定的可复现benchmark，也难以精准定位agentic workload带来的性能瓶颈。

🚀 提出的新方法与思路
**XPerf基准框架**：面向LLM serving系统的agentic AI工作负载负载测试，核心采用细粒度trace replay方法以最小化工作负载变异；支持从真实agentic应用收集trace，也可按需合成不同模式的新工作负载，实现工作负载在不同LLM serving系统上的可复现重放；框架默认包含编码、深度研究、问答等多类用例的8款agentic应用。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 工作负载可复现性 | 解决了agentic workload因非确定性输出导致的工作负载模式不可复现问题 |
| 工作负载支撑性 | 可从真实应用收集trace，也可合成自定义模式工作负载，覆盖多类agentic用例 |
| 性能剖析能力 | 提供服务系统与硬件的详细性能剖析，助力定位agentic workload的性能瓶颈 |
| 适配扩展性 | 支持不同LLM serving系统的benchmark，可扩展到更大规模的服务系统 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称，仅内置8款覆盖编码、深度研究、问答等用例的agentic应用 | 支撑agentic workload的负载测试与基准评估 |

🎯 实验设置与评估指标
任务：验证XPerf作为基准框架在agentic AI workload下的有效性，评估其对LLM serving系统benchmark的适用性。
| 指标 | 含义 |
| --- | --- |
| 论文未报告具体量化指标及对应含义 | 无 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
论文仅给出定性实验结论，未提供带表号、图号的具体定量结果，因此各小节如下：
📊 定量结果汇总
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. XPerf可准确重放agentic workload，有效缓解其因非确定性输出导致的工作负载变异问题。
  2. XPerf提供的详细性能剖析，可协助定位agentic workload引入的服务系统与硬件层面的性能瓶颈。
  3. XPerf具备良好的扩展性，可适配更大规模的LLM serving系统，支持不同服务系统的可复现benchmark测试。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出XPerf基准框架，通过细粒度trace replay解决agentic workload下LLM serving系统benchmark的工作负载不可复现问题，支持多类agentic workload的可复现测试与性能分析，助力服务系统调试，且计划开源该框架。

</details>

---

### 13. [Hidden Axis of Uncertainty: Latent-Posterior Alignment in Graph Neural Networks with Bayesian Output Layers](https://arxiv.org/abs/2608.20758v1)

**Authors**: Suk Hoon Choi, Damdae Park, Junhyuk Choi, Hyein Jung, Changsoo Kim, Ung Lee, Kyeongsu Kim  
**Category**: cs.LG  
**Published**: 2026-08-24  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.20758v1  

#### Abstract
Bayesian Neural Networks (BNNs) with Bayesian output layers provide a principled and tractable framework for quantifying predictive uncertainty, yet the mechanisms shaping that uncertainty remain unclear. While conventional theory attributes uncertainty reduction to posterior contraction, the corres...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hidden Axis of Uncertainty: Latent-Posterior Alignment in Graph Neural Networks with Bayesian Output Layers
1. 论文的主要贡献和创新点
✅ 解决的问题：Bayesian Neural Networks (BNNs) with Bayesian output layers为量化预测不确定性提供了原则性且可处理的框架，但不确定性的形成机制仍不明确；传统理论将不确定性减少归因于后验收缩，但该假设未必适用于深度模型；针对带贝叶斯输出层的图神经网络（GNN），传统不确定性解释机制不成立，观测到的不确定性变化不符合后验收缩规律。
🚀 提出的新方法与思路
**Alignment-Guided Learning (AGL)**：在训练过程中显式促进Latent-Posterior Alignment（LPA，即潜在表示向低方差后验方向移动的行为），以此优化模型对预测不确定性的调控。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 预测不确定性 | 可有效降低预测不确定性 |
| 预测准确性 | 训练后模型的预测准确性得到保持 |
| 结构校准 | 改进结构校准，使模型置信度能忠实反映底层数据密度 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体数据集名称及用途
🎯 实验设置与评估指标
任务：针对带贝叶斯输出层的GNN，开展预测不确定性量化相关任务
| 指标 | 含义 |
| --- | --- |
| 预测不确定性 | 衡量预测结果的不确定程度，值越低代表不确定性越小 |
| 预测准确性 | 衡量模型预测的正确程度，值越高代表准确性越好 |
| 结构校准 | 衡量模型置信度与底层数据密度的匹配程度，值越低代表匹配越好 |
⚔️ 基线方法对比
论文未报告具体基线方法及相关对比内容

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表号、图号及定量数值，所有具体实验结果均未提供。

4. 关键结论和发现
- 主要发现：① 在带贝叶斯输出层的GNN中，预测不确定性减少的对应机制为Latent-Posterior Alignment，即潜在表示向低方差后验方向移动，而非传统理论中的后验方差收缩；② Alignment-Guided Learning (AGL)方法可显式促进该对齐行为，实现预测不确定性降低的同时保持预测准确性，并改进结构校准。
- 方法局限性：论文未报告方法的局限性
- 未来工作：论文未报告未来工作内容
> ✅ **总结一句话**：该论文揭示了带贝叶斯输出层的图神经网络（GNN）中预测不确定性形成的Latent-Posterior Alignment机制，提出的AGL方法可有效优化不确定性量化并平衡预测性能，为GNN的不确定性研究提供了新视角。

</details>

---

### 14. [Decoupled Vision-Language System for Multimodal Understanding and Generation](https://arxiv.org/abs/2608.20382v1)

**Authors**: Yifan Xu, Baochen Xiong, Xiaoshan Yang, Donglin Di, Yaowei Wang, Changsheng Xu  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.20382v1  

#### Abstract
We introduce a new architecture design for multimodal large language models (MLLMs), Libra, capable of both multimodal understanding and generation. Libra architecture contains one vision system and one language system, connected by cross-modal bridges. This design decouples self-modal modeling and ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Decoupled Vision-Language System for Multimodal Understanding and Generation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大模型（MLLMs）通常未能有效平衡自模态建模与跨模态交互，难以同时学习视觉、语言各模态的独特表征并维持高效的跨模态理解，无法同时兼顾多模态理解与生成任务的需求。

🚀 提出的新方法与思路
**Libra架构**：包含独立的视觉系统与语言系统，二者通过跨模态桥接连接，核心设计为动态解耦自模态建模与跨模态交互两类任务。
**switch attention模块与switch FFN模块**：动态路由计算流，分别适配自模态建模场景与跨模态交互场景，实现计算资源的精准分配。
此外，针对tokenization、positional encoding与supervision进行了改进，支持两类任务设置：Libra-1为仅理解的图像到文本任务，Libra-2为统一图像到文本理解和文本到图像生成的任务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模态建模平衡 | 动态解耦自模态建模与跨模态交互，兼顾各模态独特表征学习与跨模态交互效率 |
| 多任务适配 | 支持理解与生成统一的任务设置，覆盖图像到文本理解、文本到图像生成两类场景 |
| 架构灵活性 | 视觉与语言系统分离，可分别优化各模态的表征能力 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：论文未报告
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何定量结果

4. 关键结论和发现
- 主要发现：① Libra架构通过解耦自模态与跨模态建模，能实现多模态理解与生成任务的性能双向提升；② 开关注意力与开关FFN模块的动态路由设计，可有效适配不同模态任务的计算需求；③ Libra支持从单一理解任务到统一理解生成任务的扩展。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出的Libra架构通过解耦视觉与语言系统、辅以动态开关计算模块，有效兼顾了多模态理解与生成任务的性能，为多模态大模型的架构设计提供了新方向。

</details>

---

### 15. [Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks](https://arxiv.org/abs/2608.20497v1)

**Authors**: Malak Gamal El-Din, Yifan Zhang, Yasser Shoukry, Sitao Huang, Salma Elmalaki  
**Category**: cs.LG  
**Published**: 2026-08-24  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.20497v1  

#### Abstract
Deploying high-accuracy neural networks on resource-constrained edge devices remains challenging, as existing approaches treat training, compression, and hardware synthesis as separate stages, leaving a gap between software-trained models and efficient end-to-end deployment with limited support for ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks
1. 论文的主要贡献和创新点
✅ 解决的问题：将高精度神经网络部署到资源受限的边缘设备存在挑战，现有方法将训练、压缩、硬件综合视为独立阶段，导致软件训练的模型与高效端到端部署之间存在差距，且对模型可解释性的支持有限。
🚀 提出的新方法与思路
**Bern2Edge框架**：这是一个端到端的框架，使用知识蒸馏技术将预训练的教师前馈网络转换为以Bernstein多项式激活为核心的硬件高效表示；该表示支持两种部署路径，一是基于查找表（LUT）的高保真实现，可在压缩约束下保留模型保真度，二是由Bernstein激活几何特性衍生的符号规则表示，可支持带有显式输入空间约束的可解释推理。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模型可解释性 | 支持生成带显式输入空间约束的符号规则表示 |
| 部署路径灵活性 | 可根据需求选择压缩下的高保真实现或可解释性部署路径 |
| FPGA资源适配 | 可适配不同FPGA设备完成部署 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 无 |
🎯 实验设置与评估指标
本次任务为资源受限边缘设备的神经网络部署任务，具体任务细节未明确说明。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 模型准确率 | ↑越高越好 |
| 部署延迟 | ↓越低越好 |
| BRAM存储资源占用 | ↓越低越好 |
| DSP计算资源占用 | ↓越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| W8A8量化教师 | 量化基线模型 | 权重量化为8位、激活量化为8位的预训练模型 |
| ReLU激活模型 | 精度对比基线 | 以ReLU函数为激活函数的模型，用于精度性能对比 |
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：① 提出的Bern2Edge框架为端到端的边缘神经网络部署方案，通过知识蒸馏将预训练前馈网络转换为硬件高效的Bernstein多项式激活表示；② 该框架提供两种部署路径，可兼顾压缩下的精度保留或推理可解释性；③ 该框架支持在低功耗FPGA设备上完成部署。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出端到端的Bern2Edge框架，借助知识蒸馏技术将预训练教师前馈网络转换为硬件高效的Bernstein多项式激活表示，支持两种部署路径，可实现资源受限边缘设备上的高效神经网络部署，同时具备精度保留或推理可解释性的特性。

</details>

---

### 16. [Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning](https://arxiv.org/abs/2608.20564v1)

**Authors**: Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D. Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, Anirban Roy  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.20564v1  

#### Abstract
Multi-agent LLM systems can improve reasoning by pooling diverse perspectives, but their effectiveness depends on coordinating communication, particularly in hidden-profile settings where each agent holds only part of the evidence required for a correct decision. Existing protocols, including fixed ...

---

### 17. [ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models](https://arxiv.org/abs/2608.21100v1)

**Authors**: Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai, Dawei Feng, Huaimin Wang  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.21100v1  

#### Abstract
While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods o...

---

### 18. [Assessing Triple Modular Redundancy for Wide-Link, Low-Latency NoC Routers: Reliability and Physical Design Challenges](https://arxiv.org/abs/2608.21288v1)

**Authors**: Chen Wu, Michael Rogenmoser, Luca Benini, Angelo Garofalo  
**Category**: cs.AR  
**Published**: 2026-08-24  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.21288v1  

#### Abstract
Protecting the Network-on-Chip (NoC) of physical-AI tile-based accelerators deployed in harsh environments against single-event effects (SEEs) is paramount for preventing NoC failures that can lead to deadlocks and silent data corruption (SDC). Prior work on reliable NoCs has largely focused on narr...

---

### 19. [TreeWY: Speculative Verification for Gated DeltaNet Hybrids](https://arxiv.org/abs/2608.20961v1)

**Authors**: Sneha Murthy Ghantasala  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.20961v1  

#### Abstract
Modern open models are hybrids: most layers are linear-attention (Gated DeltaNet, GDN) layers carrying a small fixed-size recurrent state instead of a growing key-value (KV) cache. This makes ordinary decoding memory-efficient, but hurts speculative decoding. To verify a batch of draft tokens and th...

---

### 20. [Coverage-Driven Verification for Safety-by-Design in AI-Based Collision Avoidance Systems](https://arxiv.org/abs/2608.20864v1)

**Authors**: Thomas Stefani, Johann Maximilian Christensen, Elena Hoemann, Frank K\"oster, Sven Hallerbach  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.20864v1  

#### Abstract
Artificial Intelligence (AI) offers significant potential for future aviation systems; however, its integration into safety-critical applications requires compliance with the aviation sector's stringent safety standards. For AI and Machine Learning (ML)-based systems, the European Union Aviation Saf...

---

### 21. [ImmigrationReason: A Structured Dataset of U.S. Immigration Appeals for Legal Reasoning Research](https://arxiv.org/abs/2608.20391v1)

**Authors**: Amirhossein Afsharrad, Seyed Shahabeddin Mousavi  
**Category**: cs.CL  
**Published**: 2026-08-24  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.20391v1  

#### Abstract
Most legal NLP resources draw from federal case law and focus on coarse classification, leaving administrative adjudication, where the vast majority of government decisions occur, essentially unaddressed. We introduce ImmigrationReason, a large-scale structured dataset derived from 12,375 non-preced...

---

### 22. [Reinforcement Learning for Continuous-Time Jump Markov Decision Processes with Applications to Network Dynamic Pricing](https://arxiv.org/abs/2608.20680v1)

**Authors**: Huiling Meng, Ningyuan Chen, Xuefeng Gao  
**Category**: cs.LG  
**Published**: 2026-08-24  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.20680v1  

#### Abstract
We study reinforcement learning (RL) in Continuous-Time Jump Markov Decision Processes (CTJMDPs) featuring general discrete state spaces (which need not possess a vector space structure) and continuous/discrete action spaces. The setup covers many well-known applications in operations such as multi-...

---

### 23. [Nexus: Depth-Adaptive KV-Cache Splicing and Retrieval-Decoupled Tool Routing for Agentic LLMs on Unified Memory](https://arxiv.org/abs/2608.20397v1)

**Authors**: Mustafa Arslan  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2608.20397v1  

#### Abstract
Agentic large language models (LLMs) on the Model Context Protocol (MCP) re-encode verbose tool schemas every turn, so prefill - quadratic in sequence length - dominates time-to-first-token (TTFT) as the tool registry grows. Nexus's primary lever is to decouple routing from the schema-prefill cost: ...

---

### 24. [SPARC: Single-Pass Scaling for Motion Forecasting with Conformal Bayesian Last Layers](https://arxiv.org/abs/2608.20802v1)

**Authors**: Sakif Hossain, Julian Teusch, J\"org P. M\"uller  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.20802v1  

#### Abstract
Human motion forecasters are increasingly accurate and fast, but reliable deployment requires uncertainty estimates that are structured, calibrated, and efficient. Bayesian and ensemble-based uncertainty estimates often require repeated stochastic inference [15, 26], while conformal calibration alon...

---

### 25. [Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.20631v1)

**Authors**: Quang Dao, Purvi Kathalkar, Kenneth Eaton  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.20631v1  

#### Abstract
Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrad...

---

### 26. [STCO: Conditional Neural Operators for Time-Dependent PDEs](https://arxiv.org/abs/2608.20477v1)

**Authors**: Xingxin Yang, Zhan Zhang, Juan Li  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.20477v1  

#### Abstract
Neural operators have emerged as efficient surrogates for time-dependent physical systems governed by partial differential equations (PDEs), but their future-state predictions are often conditioned only on observed states and static problem descriptors. For control or optimization, however, body mot...

---

### 27. [ReCurveflow: A Flow Matching Framework that Learns Curved Reaction Trajectories to Predict Transition State Geometries](https://arxiv.org/abs/2608.20869v1)

**Authors**: Seungheun Baek, Mogan Gim, Jaewoo Kang  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.20869v1  

#### Abstract
Predicting transition states (TS) in chemical reactions is crucial, as they provide insights into reaction mechanisms. Recent work on TS prediction have focused on flow matching supervised on straight linear paths that do not align with actual reaction trajectories. We propose a novel flow matching-...

---

### 28. [Decoupling Policy Extraction for Offline Reinforcement Learning](https://arxiv.org/abs/2608.20909v1)

**Authors**: Xuyao Lin, Yixiang Shan, Jinru Duan, Tao Yang, Xinyu Zhao, Runyu Lei, Yiming Zhao, Jiaxin Fan, Zongbao Feng, Peng Jia  
**Category**: cs.LG  
**Published**: 2026-08-24  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.20909v1  

#### Abstract
Offline RL methods commonly jointly train the actor and critic, where the critic is used to guide the actor toward higher-value actions. This coupled learning process is well motivated in online RL, where an improved actor collects new data that can further update the actor and the critic. However, ...

---

### 29. [VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences](https://arxiv.org/abs/2608.21357v1)

**Authors**: Elaine Lau, Thanuka Udumulla, Lee Izhaki-Tavor, Francisco Guzm\'an, Nicholas Magazine, Jonas Mueller  
**Category**: cs.AI  
**Published**: 2026-08-24  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.21357v1  

#### Abstract
In professional life sciences workflows, scientists routinely interpret visual artifacts (gel blots, microscopy images, plasmid maps, flow cytometry plots, molecular structures, ...) to inform research decisions. We introduce VIALS, a visual question-answering benchmark with 161 such interpretation ...

---

### 30. [Scalpel3: A High-Performance Data Carving Architecture for Recovery of Fragmented Files](https://arxiv.org/abs/2608.20363v1)

**Authors**: Karley Waguespack, Samuel Goodwin, George Hendrick, Samuel Hildebrand, Thomas Landaiche III, Mingyang Li, Joshua McCain, Tyler Saizan, Jacob Tucker, James M. Ghawaly, Golden G. Richard III  
**Category**: cs.DC  
**Published**: 2026-08-24  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2608.20363v1  

#### Abstract
File carving recovers files from raw storage media without relying on filesystem metadata, a key  capability in digital forensics, data recovery, and digital exploration. Traditional tools such as Foremost, Scalpel v1/2, and PhotoRec handle contiguous files effectively, and some support  fragmented ...

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
