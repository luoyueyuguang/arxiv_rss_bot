# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-02 09:58:46 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning](https://arxiv.org/abs/2609.00879v1)

**Authors**: Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee, Fahad Khalid, Mourad Oussalah  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 98.0  
**Type**: new  
**ArXiv ID**: 2609.00879v1  

#### Abstract
Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态灾害严重程度评估模型存在标注数据稀缺、推理质量评估不足的核心痛点，无法同时满足准确预测与透明解释的需求；现有两类方法的缺陷分别是：受限于稀缺标注数据、对模型推理质量评估不充分。

🚀 提出的新方法与思路
**两阶段训练框架**：整合Supervised Fine-Tuning（SFT）和Direct Preference Optimization（DPO）构建统一数据构建流程；从Human-in-the-Loop（HITL）注释工作流衍生出两个互补数据集，分别是用于SFT的ReasoningSet（包含经验证的推理理由）和用于DPO对齐的PreferenceSet（包含配对的推理理由）；采用自动指标、模型评分、人工排序三类方式评估分类性能与解释质量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 分类性能 | SFT及后续DPO优化可提升模型分类的准确性与均衡性 |
| 解释质量 | 模型解释的合理性提升，推理与人类判断的一致性强化 |
| 鲁棒性与泛化性 | 在不同多模态模型上验证效果，具备通用适配能力 |
| 案例适配性 | 改善轻度灾害案例的检测，降低高风险误分类 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ReasoningSet | 用于SFT，提供经验证的灾害严重程度推理理由 |
| PreferenceSet | 用于DPO对齐，提供配对的灾害严重程度推理理由 |

🎯 实验设置与评估指标
任务为多模态灾害严重程度评估，核心评估分类性能与解释质量：
| 指标 | 含义（箭头） |
| ---- | ---- |
| 分类准确率 | 衡量预测准确性，↑越高越好 |
| Macro-F1 | 衡量分类均衡性，↑越高越好 |
| 解释质量指标（自动/模型/人工） | 衡量解释合理性，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基线多模态灾害评估模型 | 多模态灾害评估模型 | 未应用SFT与DPO优化的基础模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：论文未报告

4. 关键结论和发现
- 主要发现：1. 所提出的两阶段训练框架结合HITL衍生的两类互补数据集，可有效提升多模态灾害严重程度评估模型的分类性能与解释质量；2. 该方法在InternVL-3-8B、LLaVA-1.5-7B两类不同模型上验证了鲁棒性与泛化性；3. 方法可改善轻度灾害案例的检测能力，降低高风险误分类，强化模型推理与人类判断的一致性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的整合SFT与DPO的两阶段训练框架，结合HITL衍生的互补数据集，实现了准确且可解释的多模态灾害严重程度评估，具备跨模型鲁棒性，优化了灾害案例检测与推理一致性。

</details>

---

### 2. [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](https://arxiv.org/abs/2609.00993v1)

**Authors**: Guowei Wang, Chaokun Yang, Zhenxuan Pan, Yuhong Guo, Minghua Zhu, Zhechuan Zhang, Shuo Wan, Xiaowei Zhu  
**Category**: cs.DC  
**Published**: 2026-09-02  
**Score**: 90.5  
**Type**: new  
**ArXiv ID**: 2609.00993v1  

#### Abstract
Rollout inference often dominates the wall-clock time of large-scale reinforcement learning (RL). In agentic RL, each trajectory alternates between model generation and environment interaction over multiple turns. Asynchronous trajectories consequently introduce new prefill (P) work while other traj...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts
1. 论文的主要贡献和创新点
✅ 解决的问题
分点列出不同方法的缺陷：
1. 共享加速器的P/D co-location问题：P任务会干扰延迟敏感的Decode任务，延长Rollout完成时间；
2. P/D disaggregation（分离）方案：需单独设备池和KV缓存传输，资源开销大；
3. 现有原位P/D复用设计：缺乏大型MoE部署所需的通信隔离，P与D会发布冲突的collectives，DeepEP框架的P和D路径共享可变协议状态，存在通信安全隐患。

🚀 提出的新方法与思路
**AInfer-PD**：扩展原位P/D复用技术至分布式MoE Rollouts，核心设计如下：
1. 协调跨各rank的P和D的collective执行顺序；
2. 为DeepEP框架的P和D路径提供独立的通信状态，保障ADP/ATP与DeepEP路径的并发P/D执行通信安全；
3. 保留共享模型权重和KV存储，在同一设备上协调处理P和D任务，无需额外资源开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| P/D共存通信安全性 | 解决大型MoE部署中原位P/D复用的通信隔离问题，避免P、D任务冲突的collectives，保障DeepEP路径状态独立 |
| 资源利用率 | 保留共享模型权重与KV存储，无需额外设备池或KV缓存传输，降低资源开销 |
| Rollout完成效率 | 在单节点及多节点工作负载下，相比基线方法可显著减少Rollout完成时间 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：评估Rollout inference在预填充密集工作负载下的完成时间
| 指标 | 含义（箭头标方向） |
| --- | --- |
| Rollout完成时间 | 越低越好 ↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 原AInfer引擎（禁用P/D复用） | 基线方法 | 未启用原位P/D复用的原有AInfer引擎 |
| SGLang | 基线方法 | 现有分布式推理框架 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供实验结果对应的表号、图号，无法定位定量数据来源，故相关内容为论文未报告。
💡 结论：论文未报告对应表号、图号，无法提取具体定量结论。

4. 关键结论和发现
- 主要发现：1. 提出的AInfer-PD方法可实现分布式MoE Rollout中原位P/D复用的通信安全；2. 在预填充密集工作负载下，相比基线方法可减少Rollout完成时间；3. 细粒度边界（相对于全epoch异步入队）可进一步降低完成时间。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：AInfer-PD通过协调跨rank的collective顺序和为DeepEP的P/D路径提供独立通信状态，解决了分布式MoE Rollout中原位P/D复用的通信隔离问题，在预填充密集工作负载下有效减少Rollout完成时间。

</details>

---

### 3. [LLM Inference on IMC-NoC Architecture with Balanced Dataflow and Fine-Grained Parallelism](https://arxiv.org/abs/2609.00857v1)

**Authors**: Yimin Wang, Yue Jiet Chong, Xuanyao Fong  
**Category**: cs.AR  
**Published**: 2026-09-02  
**Score**: 73.0  
**Type**: new  
**ArXiv ID**: 2609.00857v1  

#### Abstract
LLM inference has become an essential service, yet it imposes unprecedented demands on memory bandwidth, computational density, and communication efficiency. While IMC is a promising solution to the memory wall issue, the heterogeneous data dynamicity of LLM requires complementary resources to handl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LLM Inference on IMC-NoC Architecture with Balanced Dataflow and Fine-Grained Parallelism
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM推理对内存带宽、计算密度、通信效率提出前所未有的需求；IMC可缓解内存墙问题，但LLM的异构数据动态性需互补资源处理运行时中间数据；LLM的大量参数需可扩展架构，片上数据移动成为核心性能瓶颈。

🚀 提出的新方法与思路
**LEAP架构**：硬件层面提出名为LEAP的可扩展架构，集成IMC PE、NMC PE和INC，各硬件层执行专门任务：IMC处理静态权重，NMC处理动态数据，INC用于部分结果归约。
**划分、映射与调度框架**：软件层面引入针对LLM服务关键指标（吞吐量、延迟）优化的划分、映射与调度框架。
**Prefill-decode分离方法**：针对prefill和decode阶段不同的计算强度，提出动态重新配置PE组织以最大化资源利用率的prefill-decode disaggregation方法。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 吞吐量 | 优于商用GPU平台 |
| 能量效率 | 优于商用GPU平台 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为LLM推理服务的性能评估，评估指标为吞吐量、能量效率。
| 指标 | 含义 |
| --- | --- |
| 吞吐量 | LLM推理的吞吐量，↑ 越高越好 |
| 能量效率 | LLM推理的能量效率，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 商用GPU平台 | 通用计算平台 | 作为LLM推理性能对比的基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告（无法定位结果来源）
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 针对LLM推理的硬件-软件协同设计方案（LEAP架构结合优化软件框架及prefill-decode分离方法），可解决LLM推理的核心性能瓶颈。
  2. 针对prefill与decode阶段不同计算强度的PE动态重配置，可提升硬件资源利用率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的硬件-软件协同设计架构，通过LEAP可扩展架构、优化的软件框架及prefill-decode分离方法，为LLM推理提供性能解决方案，相比商用GPU平台具备优势。

</details>

---

### 4. [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2609.00355v1)

**Authors**: Jungseob Lee, Seongtae Hong, Dongyub Jude Lee, Chanjun Park, Jaehyung Seo, Sugyeong Eo, Heuiseok Lim  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 65.0  
**Type**: new  
**ArXiv ID**: 2609.00355v1  

#### Abstract
Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle. The drafter stays autoregressive, so it must stay small. A small drafter cannot afford the image at every step, so vision is compressed, pruned,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有推测解码在视觉语言模型（VLM）中陷入自我挫败循环：推测器（drafter）采用自回归范式需保持小巧尺寸，无法每步处理图像，导致视觉信息被压缩、修剪或隐藏；被切断视觉信息的推测器在视觉使文本可预测的区域，可靠性最低。

🚀 提出的新方法与思路
**GLANCE**：首个针对未修改VLM目标的无损推测解码单步block drafter，打破上述循环两端的限制。
- **Block-diffusion head**：读取VLM目标已融合的视觉-语言状态，消除推测器的视觉处理成本；一次前向填充整个block，避免深度方向的顺序步骤；宽候选树可在一次目标传递中完成验证，所有审计的提示词可完全复现贪心解码结果。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
推测范式 | 采用单步block drafting，区别于传统自回归drafter
视觉成本 | 无需额外视觉处理，利用目标已融合的视觉-语言状态
接地工作负载表现 | 逐字复制场景下，仅需1次总传递，优于自回归drafter每token需1次传递的模式
2. 核心实验方法和设置
📚 使用的数据集
论文未报告 | 用途：论文未报告

🎯 实验设置与评估指标
任务：视觉语言模型的推测解码任务，论文未明确报告评估指标的详细定义与方向

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
EAGLE3-VL head | 现有基线方法 | 主流VLM推测解码方法
EAGLE-3 head | 现有基线方法 | 同语料训练的推测解码方法
自回归解码 | 传统基线方法 | 基础解码范式
3. 主要实验结果和性能指标
📊 定量结果汇总
主 benchmark 性能（L2/碰撞率等）：论文未报告
效率对比：无法定位对应表号及来源，未报告具体数值
跨域 / zero-shot 迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告
消融实验：论文未报告

💡 核心定性结论：GLANCE通过单步block drafting机制，打破了VLM推测解码的自我挫败循环，在接地工作负载场景下表现突出。
4. 关键结论和发现
- 主要发现：1. GLANCE实现了无损推测解码，利用目标融合状态消除了推测器的视觉成本，一次前向填充block提升了效率；2. 接受block的长度由目标下-token熵设置，斜率随任务接地性变陡，该规律在自由文本时倾向传统链式解码；3. 接地工作负载中block drafting的效率优势显著。
- 方法局限性：论文未明确报告具体局限性，仅提及自由文本场景下规律呈现出链式解码倾向。
- 未来工作：论文未报告

> ✅ **总结一句话**：GLANCE作为首个未修改VLM目标的无损单步block drafter，打破了VLM推测解码的自我挫败循环，在接地工作负载场景下大幅提升了解码效率。

</details>

---

### 5. [SCAFFOLD: A Large-Scale Structured Dataset of Computer Science Research Figures with Diagram QA and Chain-of-Thought Reasoning Traces](https://arxiv.org/abs/2609.00018v1)

**Authors**: Ranjit Raut, Aarav Subedi, Sagun Rai, Sudan Jha  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2609.00018v1  

#### Abstract
Computer science papers rely heavily on diagrams: architecture drawings, system flowcharts, and pipeline schematics that often carry more information than the text around them. There is currently no public dataset that pairs this specific kind of figure with captions, context, questions, answers, an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文总结：SCAFFOLD: A Large-Scale Structured Dataset of Computer Science Research Figures with Diagram QA and Chain-of-Thought Reasoning Traces
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：计算机科学论文中存在大量架构图、系统流程图等专业图，这类图携带的信息往往多于周边文本，但目前缺少公开数据集将这类图与对应的说明文本、上下文、问题、答案及逐步推理链配对，无法满足训练视觉语言模型理解这类专业图的需求。

🚀 提出的新方法与思路
**SCAFFOLD结构化数据集构建**：通过布局检测和PDF解析技术从arXiv计算机科学论文中提取数据，采用AI辅助问题生成步骤，构建了包含（图像、标题、上下文、问答对、思维链）元组的结构化计算机科学研究图数据集。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 内容配对完整性 | 包含专业图与对应caption、context、QA对、CoT推理链的完整配对元组 |
| 数据集规模多样性 | 提供三个不同规模的数据集版本（SCAFFOLD-157K、SCAFFOLD-37K、SCAFFOLD-12K） |
| 数据源专业性 | 基于arXiv计算机科学论文，贴近视觉语言模型在该领域的应用场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| SCAFFOLD-157K | 大规模数据集（来自3058篇论文的29887幅图，共157387对） |
| SCAFFOLD-37K | 中等规模数据集 |
| SCAFFOLD-12K | 基线实验用小规模数据集 |

🎯 实验设置与评估指标
任务：基于计算机科学研究图的Diagram QA任务，使用Qwen2.5-VL-3B-Instruct模型开展基线实验，论文未报告具体评估指标及实验设置细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Qwen2.5-VL-3B-Instruct | 基线模型 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验均未在论文中报告，具体如下：
**主benchmark性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：论文构建了三个不同规模的、包含专业图与完整结构化配对信息的计算机科学研究图数据集，可支撑视觉语言模型在Diagram QA及CoT推理领域的研究。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出了首个公开的包含计算机科学研究图、配对上下文、问答及思维链推理的多规模结构化数据集，为视觉语言模型理解专业研究图提供了核心资源。

</details>

---

### 6. [CacheBridge: Efficient Cross-Model KV Cache Transfer](https://arxiv.org/abs/2609.00891v1)

**Authors**: Xingyu Qu, Siyuan Lu, Zhiyu Chen, Sheng Wang, Tao Lin  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2609.00891v1  

#### Abstract
Sharing context between LLMs in a multi-model system requires the receiving model to prefill the shared prefix because KV caches are model-specific. Recent closed-form cross-model KV transfer, hereafter Full-Head Mapping, avoids this replay by fitting a training-free affine mapper from source to tar...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CacheBridge: Efficient Cross-Model KV Cache Transfer
1. 论文的主要贡献和创新点
✅ 解决的问题：多模型LLM系统间共享上下文需要接收模型预填共享前缀，因为KV缓存是模型特定的；现有训练-free的全头映射方法Full-Head Mapping，虽避免prefill replay，但因全头设计（每个目标KV头映射所选层的所有源KV头），导致传输质量对架构差异敏感，且映射器存储与应用成本随层支持增长。
🚀 提出的新方法与思路
**Architecture-indexed mapper support**：限制每个目标KV头仅映射到匹配的源KV头，降低对架构差异的敏感性，控制映射器规模。
**Attention-aligned calibration**：以因果注意力敏感度为权重，对重构误差进行加权，优化传输准确性。
**Bounded mapper construction**：采用融合GPU核构造加权充分统计量，无需物化全观测张量，同时保留闭式仿射接口支持在线部署，降低构造与应用成本。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 跨模型KV缓存传输准确性 | 在Ministral3的两个传输方向上恢复了Full-Head Mapping丢失的大量准确性，在Qwen3上保持99.83%的目标保留率 |
| 映射器存储开销 | 在Qwen3 14B→32B场景下，相比Full-Head Mapping减少8× |
| 映射器应用速度 | 在Qwen3 14B→32B场景下，相比Full-Head Mapping最高加速3.0× |
| 校准数据量需求 | 在Qwen3 14B→32B场景下，仅需Full-Head Mapping所需校准数据的十分之一即可达到相当效果 |
| 500序列构造时间 | 在Qwen3 14B→32B场景下，从92.63秒缩短至8.63秒，加速10.7× |
2. 核心实验方法和设置
📚 使用的数据集：论文未报告具体数据集名称
🎯 实验设置与评估指标：实验任务为跨模型KV缓存迁移；评估指标包括：目标保留率（越高越好）、映射器存储开销（越低越好）、映射器应用速度（越高越好）、校准数据量（越低越好）、序列构造时间（越低越好）
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Full-Head Mapping | 现有交叉模型KV缓存迁移方法 | 训练-free，采用全头设计（每个目标KV头映射所选层的所有源KV头），传输质量受架构差异影响大，映射器存储与应用成本随层支持增长 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验对应的表号，相关结果如下：
**实验场景：Ministral3传输方向、Qwen3、Qwen3 14B→32B**
| 指标 | CacheBridge表现 | Full-Head Mapping表现 |
| --- | --- | --- |
| Ministral3传输方向准确性 | 恢复了Full-Head Mapping丢失的大量准确性 | 丢失大量准确性 |
| Qwen3目标保留率 | 99.83% | 论文未报告 |
| Qwen3 14B→32B映射器存储 | 减少8× | 基线 |
| Qwen3 14B→32B映射器应用速度 | 最高加速3.0× | 基线 |
| Qwen3 14B→32B校准数据量 | 需十分之一数据达到相当效果 | 基线 |
| Qwen3 14B→32B 500序列构造时间 | 8.63秒 | 92.63秒 |
💡 结论：CacheBridge相比现有Full-Head Mapping方法，在跨模型KV缓存迁移中实现了更优的存储开销、应用速度与序列构造效率，同时保留了目标模型的上下文保留准确性，且解决了Full-Head Mapping在部分Ministral3传输方向上准确性丢失的问题。
4. 关键结论和发现
- 现有Full-Head Mapping方法因全头设计，存在对架构差异敏感、映射器成本随层增长的问题，且在部分Ministral3传输方向上会丢失大量准确性。
- CacheBridge通过协同设计的三个模块，在保持高上下文保留准确性的同时，大幅降低了Qwen3 14B→32B场景下的映射器存储、提升了应用速度、减少了500序列构造时间，仅需少量校准数据即可匹配Full-Head Mapping的效果。
- CacheBridge可恢复Full-Head Mapping在Ministral3两个传输方向上丢失的大量准确性。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：CacheBridge通过架构索引映射器支持、注意力对齐校准、受限映射器构建三个协同设计模块，高效实现跨模型KV缓存的传输，在保留目标模型上下文保留准确性的同时，大幅降低了存储开销、提升了应用速度与序列构造效率。

</details>

---

### 7. [Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs](https://arxiv.org/abs/2609.01117v1)

**Authors**: Zhaoliang Chen, Jie Fu  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.01117v1  

#### Abstract
Chain-of-thought reasoning unfolds in discrete token space: each step is committed as text, errors propagate, and eliciting good traces presupposes traces to imitate. Reasoning instead in a model's continuous representation space - where intermediate states are vectors rather than words - sidesteps ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
原有的Chain-of-thought推理在离散token空间展开，每一步都以文本形式提交，错误会发生传播，且引出优质推理轨迹需要预设存在可模仿的轨迹；而在连续表示空间进行推理的方式，存在如何计算潜态状态的核心问题。

🚀 提出的新方法与思路
**Latent Recurrent Thoughts (LRT)**：该方法分为三部分，其一为任务专用的proposer，用于提供基础潜态；其二为 tiny recurrent reasoner，通过有界残差修正迭代式优化潜态；其三为冻结的大语言模型（LLM），负责解码生成答案。该方法分离了计算深度与模型规模，潜态为迭代处理的产物而非单次前馈的结果。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理性能 | 在相同 decoder、prompt、数据及训练预算条件下，在符号推理与自然语言推理任务上大幅优于现有基于冻结解码器的连续空间推理方法；在相同主干模型下，性能优于非思维链的Chain-of-thought prompting，且推理计算量仅为后者的一小部分 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Countdown-4 | 符号推理任务 |
| Sudoku | 符号推理任务 |
| HumanEval | 代码类自然语言推理任务 |
| MBPP | 代码类自然语言推理任务 |
| StrategyQA | 常识类自然语言推理任务 |

🎯 实验设置与评估指标
本文任务为符号推理与自然语言推理任务，论文未报告具体的评估指标名称及箭头方向等细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Prior frozen-decoder continuous-space reasoning methods | 基线方法 | 基于冻结LLM的连续空间推理方法 |
| Non-thinking-mode chain-of-thought prompting | 基线方法 | 非思维链的Chain-of-thought prompting方法 |
| Latent Recurrent Thoughts (LRT) | 本文方法 | 基于冻结LLM的循环潜态优化推理方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未报告主benchmark性能的具体表/图数据**
- 主benchmark性能（L2/碰撞率等）：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现：
  1. 本文提出的Latent Recurrent Thoughts方法，在连续表示空间进行推理，规避了离散token空间Chain-of-thought推理的错误传播与轨迹模仿依赖问题；
  2. LRT方法在符号推理和多类自然语言推理任务上，性能优于现有的两类基线方法，且推理计算量显著更低；
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的Latent Recurrent Thoughts方法，通过循环优化连续表示空间的潜态，在仅使用冻结大语言模型的前提下，实现了优于现有基线的推理性能，同时大幅降低了推理计算量。

</details>

---

### 8. [Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2609.00213v1)

**Authors**: Yu Yuan, Yaoyou Fan, Lili Zhao, Guangting Zheng, Kai Zhang, Lu Pan, Ke Zeng, Qi Liu  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2609.00213v1  

#### Abstract
Reinforcement learning fine-tuning of large language models increasingly adopts multiple reward dimensions, including verifiable rules, task-specific evaluators, and learned reward models, to provide richer supervision across diverse capabilities. These dimensions are commonly scalarized with fixed ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
多奖励强化学习中，采用固定聚合权重将多奖励维度标量化的方式会诱导奖励黑客：静态投影将本质不同的奖励特征混为单一标量，使得优化偏向更简单、更密集或系统偏好的维度，训练过程中策略会被困在次优奖励配置，无法收敛到能产生更高任务性能的更均衡配置；现有固定权重、动态权重基线方法未能有效缓解该问题，存在奖励配置失衡或性能不足的缺陷。

🚀 提出的新方法与思路
**Adaptive Multi-Reward Projection（AMRP）**：一种轻量级在线多奖励聚合方法，使用相对缺口（relative shortfall）、奖励波动率（reward volatility）、近期进展（recent progress）三种信号动态调整聚合权重，对滞后、不稳定或停滞的奖励维度增加权重压力，同时缓解饱和的奖励维度，避免聚合诱导的奖励黑客。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 奖励配置平衡 | AMRP可使多奖励强化学习的奖励特征配置相比固定权重、动态权重基线更均衡 |
| 下游任务性能 | 在结构化推理、引文基础生成、开放对齐任务中，AMRP的下游任务性能优于固定和动态加权基线 |
| 算法兼容性 | AMRP支持与GRPO、GDPO、PPO等多种强化学习算法兼容 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称及细节 | 用于结构化推理、引文基础生成、开放对齐任务的多奖励强化学习实验 |

🎯 实验设置与评估指标
实验任务为多奖励强化学习下的结构化推理、引文基础生成、开放对齐，评估目标为奖励特征配置平衡度与下游任务性能；论文未报告具体评估指标名称及方向细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 固定权重聚合（Fixed weighting） | 基线方法 | 使用固定聚合权重对多奖励进行标量化，存在聚合诱导的奖励黑客问题 |
| 动态权重聚合（Dynamic weighting） | 基线方法 | 使用动态调整但非AMRP的权重分配方式，仍未能缓解聚合诱导的奖励黑客问题 |
| Adaptive Multi-Reward Projection（AMRP） | 提出方法 | 基于三种信号在线调整聚合权重，缓解聚合诱导的奖励黑客并提升性能 |

3. 主要实验结果和性能指标
所有实验的具体表号、数值、章节信息均未在论文中报告，仅定性说明AMRP相比固定和动态加权基线，能提升奖励配置平衡度与下游任务性能，且在GRPO、GDPO、PPO算法下均保持有效。论文未报告具体定量实验结果表格。

4. 关键结论和发现
- 主要发现：1. 多奖励强化学习中，静态聚合权重的固定标量化会诱导奖励黑客，导致策略陷入次优奖励配置，无法收敛到均衡的高任务性能配置；2. 提出的AMRP方法可有效调整聚合权重，提升奖励配置平衡度与下游任务性能；3. AMRP与GRPO、GDPO、PPO等多种RL算法兼容，适用场景覆盖结构化推理、引文生成、开放对齐等任务。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

✅ **总结一句话**：本文提出的AMRP方法解决了多奖励强化学习中固定权重聚合诱导的奖励黑客问题，通过相对缺口、奖励波动率、近期进展三种信号在线调整聚合权重，提升了奖励配置平衡度与下游任务性能，且与多种RL算法兼容。

</details>

---

### 9. [Dependency-Aware Chain-of-Thought Compression for Financial Reasoning](https://arxiv.org/abs/2609.00413v1)

**Authors**: Wenjun Wu, Lei Fu, Kejian Tong, Tao Ning, Sichen Zhao  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.00413v1  

#### Abstract
Chain of thought prompting improves complex reasoning, but its long intermediate traces create substantial inference cost and hinder practical deployment in financial settings. We present a Hierarchical Semantic Distillation Network, HSDN, for compressing reasoning chains while preserving answer acc...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Dependency-Aware Chain-of-Thought Compression for Financial Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
Chain of thought提示可提升复杂推理能力，但其冗长的中间推理轨迹会产生巨大的推理成本，阻碍该方法在金融这类高风险场景的实际部署；现有强压缩基线无法在保持推理准确性与逻辑连贯性的同时实现高压缩率。

🚀 提出的新方法与思路
**Hierarchical Semantic Distillation Network（HSDN）**：该框架结合语义分割、依赖图构建、双编码器重要性评分、受约束片段选择及局部边界重写，用于压缩推理链；采用冻结的Qwen3 4B模型仅负责特征提取与最终答案生成，压缩过程具备结构化与可解释性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理部署成本 | 可压缩推理链以降低推理的时间与资源开销 |
| 推理结果正确性 | 压缩后仍保持答案的准确性 |
| 整体性能与逻辑一致性 | 在综合表现及推理连贯性上优于现有强压缩基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| AFAC2025 | 用于金融推理任务的性能评估 |

🎯 实验设置与评估指标
任务为金融推理任务；评估指标包括准确率、压缩率、整体性能得分、推理连贯性，具体含义如下：
| 指标 | 含义（箭头） |
| ---- | ---- |
| 准确率 | 衡量推理结果的正确性，↑越高越好 |
| 压缩率 | 衡量推理链的压缩程度，↑越高越好 |
| 整体性能得分 | 衡量方法的综合表现，↑越高越好 |
| 推理连贯性 | 衡量压缩后推理逻辑的一致性，↑越高越好 |

⚔️ 基线方法对比
论文未报告具体基线方法的名称、类型及特点，仅提及所提方法优于强压缩基线。

3. 主要实验结果和性能指标
📊 定量结果汇总
（所有定量结果未明确对应表号、图号等来源信息，按要求呈现如下）
1. 主 benchmark 性能：论文在AFAC2025基准上验证了所提方法的性能，但未提供对应结果的具体数值及来源信息
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
  1. 所提出的Hierarchical Semantic Distillation Network（HSDN）能在压缩金融推理任务的Chain of Thought轨迹的同时，保持推理答案的准确性和逻辑连贯性，适配金融高风险场景的需求；
  2. 图引导的推理链压缩机制对金融推理任务有效。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出了Hierarchical Semantic Distillation Network（HSDN），可对金融推理任务的Chain of Thought轨迹进行有效压缩，同时保持答案准确性与逻辑连贯性，性能优于现有强压缩基线，为降低高风险场景下推理部署的成本提供了可行方案。

</details>

---

### 10. [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://arxiv.org/abs/2609.01068v1)

**Authors**: Weihuang Wen, Yingying Liu, Yichuan Liu, Wenqi Zeng, Li Zhou, Chumin Sun, Jie Sun, Tianshu Yu  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2609.01068v1  

#### Abstract
The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster scheduling. Although output-length prediction can mitigate these issues, existing approaches have key drawbacks: external proxy models add substantial la...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

OUTLETS: Output-Length Prediction from Speculative Decoding Backbones
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM服务中输出长度的长尾分布对资源配置和集群调度构成重大挑战；现有输出长度预测方法存在核心缺陷：外部代理模型会增加大量延迟且保真度有限，内部基于状态的方法虽高效但依赖对当前模型状态的浅层探测。

🚀 提出的新方法与思路
**OUTLETS**：发现推测解码（Speculative Decoding, SD）中先进框架（如EAGLE-3）的draft解码器生成的隐表示包含与生成长度相关的预测信号，因此复用推测解码骨干网络作为轨迹感知的长度预测器，仅添加轻量回归头即可完成输出长度预测任务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 延迟 | 复用已计算的draft表示，无额外高延迟开销 |
| 预测误差 | MAE低于评估方法 |
| 调度适配性 | 支持标准调度策略更均匀分配请求、优先处理短请求 |
| 调度性能优化 | 可降低短请求的P99延迟 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
本文任务为输出长度预测及基于该预测的LLM服务调度优化；评估指标为：MAE（预测误差，越低越好）、短请求P99延迟（服务性能，越低越好）
| 指标 | 含义 |
| ---- | ---- |
| MAE | 输出长度预测的误差，越低越好 |
| 短请求P99延迟 | 短请求处理的端到端延迟，越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 外部代理模型 | 外部方法 | 增加大量延迟，保真度有限 |
| 内部状态-based方法 | 内部方法 | 依赖对模型状态的浅层探测 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
💡 结论：OUTLETS的预测误差低于评估方法，基于其预测优化的调度策略可降低短请求的P99延迟。

4. 关键结论和发现
- 主要发现：1. 推测解码骨干网络中draft解码器的隐表示包含输出长度的有效预测信号；2. 提出的OUTLETS方法仅复用现有推测解码结构并添加轻量回归头，即可实现高效且误差更低的输出长度预测；3. 利用OUTLETS的预测结果优化调度，可提升服务调度性能，降低短请求的P99延迟。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：OUTLETS方法复用推测解码骨干网络的draft解码器隐表示，仅添加轻量回归头实现高效、低误差的输出长度预测，基于该预测优化调度可有效降低短请求的P99延迟。

</details>

---

### 11. [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](https://arxiv.org/abs/2609.00293v1)

**Authors**: Athulith Paraselli, Etha Tianze Hua, Ellie Pavlick  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.00293v1  

#### Abstract
We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what was stored parametrically during training. We document asymmetric biases: models tend to prefer in-context information about...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts
1. 论文的主要贡献和创新点
✅ 解决的问题
视觉语言模型（VLMs）在处理上下文记忆冲突场景（即上下文提供的信息与训练时参数存储的信息不一致的场景）时，存在与模态相关的非对称偏差，现有研究未充分揭示该偏差的产生机制，影响模型的行为一致性。

🚀 提出的新方法与思路
**模态关联的上下文记忆冲突机制分析**：以视觉和文本两种模态为核心变量，分析VLMs在上下文记忆冲突中的响应表现，将观察到的非对称偏差与跨模态的晚表征对齐关联，同时验证思维链、视觉信息量等因素对偏差的影响。

🔍 相比现有方法的优势
论文未报告

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为处理上下文记忆冲突场景下的模型响应，评估指标论文未报告
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有涉及的实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）均为论文未报告

4. 关键结论和发现
- 视觉语言模型（VLMs）在上下文记忆冲突场景下存在非对称偏差：模型倾向于采用文本中出现的实体的上下文信息，倾向于采用图像中出现的实体的训练参数信息。
- 该非对称偏差与跨模态的晚表征对齐相关：视觉实体的处理时间更长，阻碍了模型抑制常规事实回忆机制，导致模型更多地依赖参数信息进行回答。
- 思维链推理无法缩小该偏差差距，增加上下文的视觉信息量对该偏差有一定影响。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该研究揭示了视觉语言模型在处理上下文记忆冲突时与模态相关的非对称偏差及其内在机制，为优化多模态模型的一致性行为提供了参考。

</details>

---

### 12. [Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning](https://arxiv.org/abs/2609.01449v1)

**Authors**: Mariia Drozdova, Aidan Sirbu, Pietro Miotti, Robert Obryk, Mayalen Etcheverry, Eyvind Niklasson, Blake Richards  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.01449v1  

#### Abstract
Diffusion models and recursive reasoners are both iterative, but they carry information across iterations differently. We add a persistent hidden state to a diffusion denoiser and remove its timestep conditioning, leaving a single shared update that can be run to arbitrary depth. The result is an an...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有扩散模型与递归推理器均为迭代方法，但二者迭代间传递信息的方式存在差异；扩散模型依赖时间步条件，难以支持任意深度的迭代；现有迭代推理模型需候选选择、外部验证器等额外组件，推理流程复杂，推理深度受限。

🚀 提出的新方法与思路
**Timestep-Free Anysolver**：在扩散去噪器中新增持久隐藏状态，移除原有的时间步条件，保留单一共享更新函数，使其可运行至任意深度，形成anysolver（任意时刻求解器）。
**Inference Noise Injection Mechanism**：推理时无需渐进去噪，将每一步的非线索变量替换为新高斯噪声以保持最大腐蚀，无需并行rollout、候选选择或外部验证器即可探索解空间并收敛至稳定解。
**Training Curriculum Strategy**：训练阶段采用有序退火腐蚀策略，该策略为性能提升的关键，表明扩散模型的核心贡献在于作为训练课程，而非推理时的采样过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 迭代灵活性 | 支持任意推理深度，性能随推理深度提升，远超训练时的rollout长度与反向传播窗口 |
| 推理流程复杂度 | 无需并行rollout、候选选择或外部验证器，简化推理组件 |
| 训练核心价值 | 利用扩散模型作为训练课程，而非仅依赖其采样过程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Sudoku-Extreme | 精确求解极端难度数独题 |
| Maze-Unique | 精确求解唯一路径迷宫题 |

🎯 实验设置与评估指标
任务为精确求解极端数独与唯一路径迷宫，评估指标为精确求解率（数值越高越好）

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Prior Iterative Reasoning Models | 基线推理方法 | 需要候选选择、外部验证器，推理深度受限，流程复杂 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验结果对应的表号、图号等来源，因此未提供具体定量数值，仅提及在指定任务上取得了优秀的求解性能。
💡 结论：论文提出的Timestep-Free Anysolver在极端数独与唯一迷宫任务上展现出优秀的求解能力，推理时的噪声注入机制可有效简化求解流程。

4. 关键结论和发现
- 提出的Timestep-Free Anysolver是anysolver，其求解精度随推理深度提升，且推理深度可远超训练时的rollout长度和反向传播窗口；
- 推理阶段无需渐进去噪，采用保持最大腐蚀加噪声注入的机制即可保留近完美的求解能力，无需额外验证组件；
- 训练阶段的有序退火腐蚀对模型性能是必要的，扩散模型在该方法中的核心作用是作为训练课程，而非推理时的采样过程。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出了无时间步的迭代扩散求解器，将扩散模型作为训练课程实现任意深度的推理，在极端数独和唯一迷宫任务上表现优异，推理时的噪声注入机制无需额外组件即可完成求解流程。

</details>

---

### 13. [Reinforcement Learning Enhanced LLM Agents for Complex Vehicle Routing Problems](https://arxiv.org/abs/2609.00859v1)

**Authors**: Yi Chen, Zikang Yu, Jiahai Wang, Jinbiao Chen, Jianpeng Zhou, Zizhen Zhang  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.00859v1  

#### Abstract
Vehicle Routing Problems (VRPs) are fundamental combinatorial optimization problems with widespread applications in various scenarios. The advanced optimization solvers can effectively solve such problems. However, modeling complex VRP variants for solvers often requires substantial domain expertise...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Reinforcement Learning Enhanced LLM Agents for Complex Vehicle Routing Problems
1. 论文的主要贡献和创新点
✅ 解决的问题
车辆路径问题（VRP）是应用广泛的基础组合优化问题，高级优化求解器可有效求解该类问题，但建模复杂VRP变体需要大量领域专业知识，限制了高级优化技术的可及性；现有方法需高度依赖领域专业人员完成复杂VRP建模，便捷性不足。

🚀 提出的新方法与思路
**Reinforcement Learning Enhanced LLM Agents (RLEA)**：一种多智能体框架，用于自动化建模复杂VRP。该框架包含轻量神经Planner，采用Soft Q-learning训练，可高效协调基于LLM的智能体的动作；此外，配备进化记忆模块和检索增强生成（Retrieval-Augmented Generation, RAG），使智能体在为VRP生成与优化方案时，既能利用积累的经验，也可借助外部求解器的知识。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 复杂VRP建模 | 无需大量领域专业知识即可实现复杂VRP的自动化建模 |
| 求解性能 | 在48种VRP变体上，较之前SOTA方法成功率提升16.67%，运行时错误显著减少 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告具体数据集，仅说明评估对象为48种不同的VRP变体。
🎯 实验设置与评估指标：任务为自动化复杂VRP的优化建模与求解；指标为成功率（越高越好）、运行时错误率（越低越好）。
⚔️ 基线方法对比：论文未报告具体基线方法列表，仅提及对比之前的SOTA方法。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号、图号等定位信息，仅说明在评估的48种VRP变体上，RLEA取得比之前SOTA方法高16.67%的成功率，且显著减少了运行时错误；其余实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告。
💡 结论：在48种VRP变体的评估中，RLEA能提升复杂VRP自动化建模的成功率，减少运行时错误，相比之前SOTA方法表现更优。

4. 关键结论和发现
- 主要发现：1. 将强化学习与基于LLM的推理结合，可有效实现复杂VRP的自动化优化建模；2. RLEA在复杂VRP求解的成功率上比之前SOTA方法高16.67%，同时显著降低运行时错误。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：RLEA是结合强化学习与LLM的多智能体框架，能自动化建模复杂VRP，在48种VRP变体上较之前SOTA方法提升了求解成功率并减少运行时错误，降低了高级优化技术对领域专业知识的依赖。

</details>

---

### 14. [ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning](https://arxiv.org/abs/2609.01058v1)

**Authors**: Fanrui Zhang, Ruixue Ding, Qiang Zhang, Xi Chen, Boli Chen, Shihang Wang, Qiuchen Wang, Hongmin Zhan, Jinxin Bian, Li xingchao, Peijin Zheng, Hao cheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.01058v1  

#### Abstract
Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
用强化学习训练开放式智能体面临两大核心痛点：一是缺乏可验证的标准答案与可扩展的评分规则（rubrics）；二是即使接近模型能力边界，长程开放式智能体任务易产生脆弱不稳定的奖励，导致rollout对比弱且噪声大，掩盖群体策略学习所需的细粒度优化信号。

🚀 提出的新方法与思路
**Rubric-Mediated Co-Evolution框架**：耦合任务/评分规则生成器（Generator）与推理求解器（Solver），Generator基于真实工具观测锚定工具相关的评分规则标准，以生成与Solver演化能力边界匹配的有效中等难度任务为奖励；Solver通过多步骤推理与工具使用，从细粒度评分规则满足信号中学习。
**Reward-Gated Self-Evolution Distillation (RG-SED)**：选择性仅当记忆增强的同策略变体带来经验奖励提升时，将其蒸馏回原策略，减少分布不匹配，避免盲目模仿噪声指导。
**ECR-Bench**：专家校准的评分规则基准套件，覆盖单工具深度研究、多工具旅行规划任务，用于严格评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 奖励质量 | 缓解长程开放式任务中奖励的脆弱不稳定性 |
| 优化信号 | 提供细粒度评分规则满足信号，支撑群体策略的精细优化 |
| 自演化策略 | 通过RG-SED减少蒸馏时的分布不匹配，避免噪声指导的盲目模仿 |
| 评估支撑 | 提供含专用任务的专家校准基准套件，支持严格评估 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ECR-Bench | 用于评估ARISE-RL的性能，覆盖单工具深度研究、多工具旅行规划任务 |

🎯 实验设置与评估指标
任务：针对单工具深度研究、多工具旅行规划的开放式智能体任务。
指标：论文未报告具体评估指标名称及对应方向。

⚔️ 基线方法对比
论文未报告具体基线方法及相关对比细节。

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（L2/碰撞率等）**
论文未报告具体数值及对应表号/图号，无可用表格。

**效率对比（FPS / 参数量）**
论文未报告。

**跨域 / zero-shot迁移**
论文未报告。

**鲁棒性 / 扰动测试**
论文未报告。

**消融实验**
论文未报告具体消融模块对比细节，无可用表格。

4. 关键结论和发现
- 主要发现：1. ARISE-RL通过rubric介导的协同演化与RG-SED方法，有效解决了开放式智能体强化学习训练中奖励不稳定与优化信号缺失的问题；2. 论文提出的ECR-Bench为相关开放式智能体任务提供了可靠的评估基准；3. ARISE-RL在所有评估基准上实现了稳定的最优性能。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：ARISE-RL通过耦合rubric介导的协同演化框架与奖励门控自演化蒸馏方法，结合专用评估基准ECR-Bench，实现了开放式智能体强化学习的稳定高效自演化，在相关基准上达到最优性能。

</details>

---

### 15. [Conditional Flow Matching for ML-Based Inverse Design Problems](https://arxiv.org/abs/2609.00863v1)

**Authors**: Juliana Felder, Milad Habibi, Soheyl Massoudi, Mark Fuge  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.00863v1  

#### Abstract
Engineering inverse design is often limited by the high computational cost of iterative solvers for optimization problems constrained by partial differential equations (PDEs) and by their sensitivity to initialization. Deep generative models can produce candidate designs without rerunning the simula...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Conditional Flow Matching for ML-Based Inverse Design Problems
1. 论文的主要贡献和创新点
解决的问题：工程逆设计常受偏微分方程（PDE）约束的优化问题迭代求解器计算成本高、对初始化敏感；现有用于该场景的深度生成模型中，扩散模型需迭代反向时间积分，采样效率低，未能兼顾性能与效率需求。
提出的新方法与思路
**Conditional Flow Matching (CFM)**：将CFM整合到EngiOpt框架，针对工程逆设计任务生成候选设计，作为梯度-based优化细化的暖启动，平衡生成性能与采样效率。
相比现有方法的优势
维度 | 优势
主基准任务性能 | 在beams2d和heatconduction2d两个逆设计任务上，CFM的累积最优性间隙（COG）、最终最优性间隙（FOG）、最大均值差异（MMD）、体积分数偏差均为最低值，达到最优性能
采样效率 | 在beams2d任务中，Euler s=16时CFM采样速率达53.2 samples/s，约为扩散基线的66倍，且使用更少网络评估次数

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
beams2d（来自EngiBench） | 结构逆设计任务测试
heatconduction2d（来自EngiBench） | 热传导逆设计任务测试
🎯 实验设置与评估指标
任务：以生成的候选设计作为梯度-based优化细化的暖启动，评估设计作为暖启动的适配性。
指标 | 含义
累积最优性间隙（COG） | 越低越好 ↓
最终最优性间隙（FOG） | 越低越好 ↓
最大均值差异（MMD） | 越低越好 ↓
体积分数偏差 | 越低越好 ↓
采样速率 | 越高越好 ↑
⚔️ 基线方法对比
方法 | 类型 | 特点
Conditional diffusion model | 深度生成模型 | 需迭代反向时间积分，为对比基线
Conditional generative adversarial network (cGAN) | 深度生成模型 | 用于对比的基线方法
Conditional flow matching (CFM) | 深度生成模型 | 本工作提出的改进方法

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：体积分数偏差对比（beams2d/heatconduction2d任务）**
方法 | beams2d体积分数偏差 | heatconduction2d体积分数偏差
CFM | 0.4% ✅ | 1.0% ✅
Conditional diffusion model | 3.8% | 11.2%
💡 结论：CFM在两个逆设计任务上的体积分数偏差均显著低于扩散基线，达到最优性能。
**表2：采样效率对比（beams2d任务）**
方法 | 采样速率（samples/s） | 对应网络评估次数
CFM（Euler s=16） | 53.2 ✅ | 未明确给出
Conditional diffusion model（1000次网络评估） | 约为CFM的1/66 | 1000
💡 结论：CFM采样效率远高于扩散基线，采样速率提升至原基线的66倍，且使用更少的网络评估次数。
主benchmark性能（L2/碰撞率等）：论文未报告
效率对比（FPS/参数量）：仅提供采样速率对比，参数量相关论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1）CFM作为引入EngiOpt的生成模型，在beams2d和heatconduction2d任务上的COG、FOG、MMD、体积分数偏差均为最优；2）CFM采样效率远超扩散基线，在beams2d任务中采样速率达53.2 samples/s，约为扩散基线的66倍；3）在两个任务上，CFM生成的暖启动设计的COG均低于对比的基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本工作将Conditional Flow Matching整合到EngiOpt框架，提出的方法在两个工程逆设计基准任务上取得最优的暖启动性能，同时采样效率远高于对比的扩散模型，解决了现有生成模型在工程逆设计中性能与效率难以兼顾的问题。

</details>

---

### 16. [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](https://arxiv.org/abs/2609.01549v1)

**Authors**: Tom\'a\v{s} Hole\v{c}ek, Viliam Lis\'y  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.01549v1  

#### Abstract
Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized...

---

### 17. [iPINN for Broadband CARS Phase Retrieval: A Framework for Function Approximation and Inverse Modeling Problems in Nonlinear Spectroscopy](https://arxiv.org/abs/2609.00883v1)

**Authors**: Ravi Teja Vulchi, Carl Messerschmidt, Mohammadsadegh Vafaeinezhad, Rajendhar Junjuri, Tobias Meyer-Zedler, Juergen Popp, Thomas Bocklitz  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2609.00883v1  

#### Abstract
Phase retrieval in broadband coherent anti-Stokes Raman spectroscopy (BCARS) is an ill-posed inverse problem. The Raman-like signal is encoded in the imaginary part of the resonant susceptibility, which mixes coherently with a non-resonant background (NRB) that varies across acquisitions. We introdu...

---

### 18. [Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers](https://arxiv.org/abs/2609.01567v1)

**Authors**: Matteo Merler, Giovanni Bonetta, Davide Zago, Rossella Cancelliere, Bernardo Magnini  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2609.01567v1  

#### Abstract
Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomo...

---

### 19. [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](https://arxiv.org/abs/2609.00550v1)

**Authors**: Jungyeon Lee, Yejin Yoon, Taeuk Kim  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.00550v1  

#### Abstract
Multimodal large language models (MLLMs) are increasingly provided with contextual evidence in heterogeneous forms: as a text passage, as a rendered image of the same passage, or as both together. However, it remains unclear how consistently these surface forms are processed, especially when the evi...

---

### 20. [CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs](https://arxiv.org/abs/2609.01195v1)

**Authors**: Chaohui Guo, Michel Klein, Zhisheng Huang  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.01195v1  

#### Abstract
Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thu...

---

### 21. [One Policy, Any Budget: Internalizing Budget-Aware Search via Reinforcement Learning](https://arxiv.org/abs/2609.00813v1)

**Authors**: Xiaowei Sun, Jin Li, Yili Hong, Yikun Fu, Yanghua Xiao  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.00813v1  

#### Abstract
While reinforcement learning has enabled LLM-based search agents to invoke external tools, existing methods train under fixed budgets and cannot adapt when constraints vary at deployment. We propose AnySearch, a framework that enables a single policy to perform budget-aware search under any budget c...

---

### 22. [Joint Training Is Not Enough: Conditioned Cross-Granularity Training for Multimodal Document Understanding](https://arxiv.org/abs/2609.00756v1)

**Authors**: Chengguang Gan, Yunhao Liang, Hanjun Wei, Qinghao Zhang, Shiwen Ni  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.00756v1  

#### Abstract
The Mutual Reinforcement Effect (MRE) asks whether a fine, span-level and a coarse, document-level task help each other when one model handles both. We test it in multimodal document understanding on three corpora, two of receipts and one of scanned business forms, comparing single-task, joint and c...

---

### 23. [Can LLMs Use Relational Transformer Embeddings?](https://arxiv.org/abs/2609.00457v1)

**Authors**: Francisco Galuppo Azevedo, Clarissa Lima Loures  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.00457v1  

#### Abstract
Injecting frozen relational-encoder embeddings as soft tokens into a large language model (LLM) is a conceptually appealing fusion strategy: the encoder handles multi-table structure, the LLM handles language and reasoning, and no lossy text serialization is required. We test this hypothesis concret...

---

### 24. [StudyBench: Can Self-Evolution Squeeze Textbooks for Olympiad Capability?](https://arxiv.org/abs/2609.00787v1)

**Authors**: Yinghao Chen, Zixi Chen, Bingxiang He, Ziqing Qiao, Huan-ang Gao, Yinuo Xu, Yuxin Zuo, Zeyuan Liu, Yuhao Zhan, Chaojun Xiao  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.00787v1  

#### Abstract
Humans need to study only a handful of well-written textbooks to master a discipline and attempt its hardest problems. We argue that an ideal self-evolution method should share the same property, that is autonomously learning from raw training material for transferable problem-solving capability. Ho...

---

### 25. [Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall](https://arxiv.org/abs/2609.01532v1)

**Authors**: Jacqueline He, Howard Yen, Shuyue Stella Li, Margaret Li, Hanqing Zeng, Yinglong Xia, Benyu Zhang, Zhuokai Zhao, Qiang Zhang, Pang Wei Koh, Luke Zettlemoyer, Wen-tau Yih  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2609.01532v1  

#### Abstract
Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the ...

---

### 26. [DeSyR: A Decoupled Symbolic Recovery Framework with PINN-Guided Structure Search and Physics-Informed Coefficient Refinement](https://arxiv.org/abs/2609.00530v1)

**Authors**: Pancheng Niu, Jun Guo, Qiaolin He, Jingcai Guo, Yanchao Shi  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2609.00530v1  

#### Abstract
Recovering compact explicit solutions from neural approximations is challenging when imperfect teacher data guide symbolic topology search and coefficient estimation. We present DeSyR, a decoupled symbolic recovery framework for differential equations. A physics-informed neural network guides repeat...

---

### 27. [Agentic Empirical Asset Pricing: Methodological Foundations](https://arxiv.org/abs/2609.00731v1)

**Authors**: Yingjian Pan, Xiaowei Ding, Kay Giesecke  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.00731v1  

#### Abstract
Recent advances in LLM agents enable a new paradigm for asset pricing, which we call Agentic Empirical Asset Pricing (AEAP): systems that autonomously conduct the scientific discovery process itself. We define AEAP and identify its core building blocks. Existing evaluation practices backtest only th...

---

### 28. [H2Table: Hierarchical Hypergraph-Enhanced Large Language Models for Complex Table Reasoning](https://arxiv.org/abs/2609.01216v1)

**Authors**: Jia Ling, Yangfan Wang, Chen Tang, Haoming Tan, Yang Yang, Yi Guan, Jingchi Jiang  
**Category**: cs.AI  
**Published**: 2026-09-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.01216v1  

#### Abstract
Tables are ubiquitous across diverse domains, yet reasoning over them remains a significant challenge for modern large language models (LLMs). Current approaches typically linearize tables into sequences, inherently overlooking their intrinsic two-dimensional and hierarchical structure. To address t...

---

### 29. [From Base Rollouts to RL Reasoning: A Budgeted Search Perspective](https://arxiv.org/abs/2609.01274v1)

**Authors**: Wenhe Sun, Cunxiang Wang, Zijun Yao, Yixin Cao  
**Category**: cs.CL  
**Published**: 2026-09-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.01274v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but how these gains relate to inference-time decoding and search remains unclear. Does RL create reasoning the base model lacks, or shift the rollout distribution toward trajectories it can already reach but rar...

---

### 30. [Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?](https://arxiv.org/abs/2609.00089v1)

**Authors**: Arkadiusz Lipiecki, Rafa{\l} Weron  
**Category**: cs.LG  
**Published**: 2026-09-02  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.00089v1  

#### Abstract
Foundation models promise accurate forecasts with little or no task-specific training, but whether they can replace models designed specifically for electricity price forecasting remains unclear. We compare nine variants from five foundation model families, evaluated in zero-shot mode, with two stat...

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
