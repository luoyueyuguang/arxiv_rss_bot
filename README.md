# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-03 10:12:20 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Scaling Inference Prefill with High-Radix Photonic Interconnects](https://arxiv.org/abs/2609.01821v1)

**Authors**: Arulselvan Madhavan, Peter Carson, Taylor Groves, Thomas Graham  
**Category**: cs.DC  
**Published**: 2026-09-03  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2609.01821v1  

#### Abstract
With the rise of inference as today's dominant AI workload, the industry is transitioning to high-bandwidth photonic interconnects to meet the large scale-up requirements of increasingly complex Mixture-of-Experts (MoE) models. This paper quantifies the benefits of 3D-integrated photonic interconnec...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Scaling Inference Prefill with High-Radix Photonic Interconnects
1. 论文的主要贡献和创新点
✅ 解决的问题：当前推理已成为AI领域的主流工作负载，工业界需依赖高带宽互联满足Mixture-of-Experts (MoE)模型大规模扩展的需求，但存在核心矛盾：需同时保障Large Language Model (LLM)聊天的高并发吞吐量，以及推理、agentic AI所需的大上下文窗口；现有铜基GPU系统受限于电气固有扩展pod限制，无法有效降低time-to-first-token，大规模集群性能不足。
🚀 提出的新方法与思路：**3D集成光电互联**，将3D集成的光电互联技术应用于LLM推理预填场景，通过模拟不同上下文规模的MoE模型，对比现有铜基GPU系统的性能，解决大规模集群下的互联瓶颈问题。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| --- | --- |
| 高批处理压力场景延迟 | 提升2.1--3.2x |
| 通信受限配置性能 | 提升2.8--5.8x |
| 生产级平台加速比 | 达到2.2--4.5x |
| GPU集群规模支持 | 可支持1152-GPU，突破电气系统扩展pod限制 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标
任务：评估3D集成光电互联在不同上下文规模的MoE模型推理预填场景下的性能，对比现有铜基GPU系统
| 指标 | 含义（箭头） |
| --- | --- |
| 延迟 | ↓ 越低越好 |
| 性能提升倍数 | ↑ 越高越好 |
| 加速比 | ↑ 越高越好 |
| 支持的GPU规模 | ↑ 越大越好 |
实验设置：模拟三种MoE模型，分别为短上下文（1K--8K tokens）、中上下文（128K tokens）、长上下文（1M tokens），对比对象为现有铜基GPU系统和采用高带宽集成光子学的系统
⚔️ 基线方法对比：
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 铜基GPU系统 | 基线方法 | 现有电气互联方案，受限于固有扩展pod限制，大规模集群性能不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 3D集成光电互联可在高批处理压力场景下显著降低推理预填的延迟，在通信受限配置下大幅提升性能；2. 该方案可支持1152-GPU规模的集群，突破电气系统的固有扩展pod限制，在生产级平台实现明显加速；3. 该方案可适配短、中、长不同上下文规模的MoE模型的推理预填需求
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：该论文提出的3D集成光电互联方案，可解决LLM推理预填场景下高并发吞吐量与大上下文窗口的权衡难题，突破铜基互联的扩展限制，实现显著的性能提升。

</details>

---

### 2. [MemeCULT-1K: Benchmarking South Asian Cultural Context and Humor Understanding of Multimodal Models](https://arxiv.org/abs/2609.01772v1)

**Authors**: Tawsif Tashwar Dipto, Mehedi Ahamed, Radib Bin Kabir, Mueeze Al Mushabbir, Mohammed Saidul Islam, Mir Rayat Imtiaz Hossain, Md Tahmid Rahman Laskar, Sabbir Ahmed  
**Category**: cs.CL  
**Published**: 2026-09-03  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2609.01772v1  

#### Abstract
Meme understanding goes beyond recognizing visual content or literal text; it requires implicit cultural knowledge and pragmatic inference that most vision-language models still lack. We introduce MemeCULT-1K, a multilingual benchmark of 1,000 South Asian memes in Bengali, English, and Hindi, where ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MemeCULT-1K: Benchmarking South Asian Cultural Context and Humor Understanding of Multimodal Models
1. 论文的主要贡献和创新点
✅ 解决的问题：现有视觉语言模型（VLMs）在meme理解任务中仅能识别视觉内容或字面文本，缺乏对隐含文化知识与语用推理的能力，难以完成文化语境下的幽默理解。
🚀 提出的新方法与思路
**MemeCULT-1K多模态基准**：构建包含1000个南亚多语言（孟加拉语、英语、印地语）meme的基准数据集，每个meme配对对应文化背景说明及3个人类撰写的解释，同时补充54个孟加拉语方言meme的评估子集。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 文化语境覆盖 | 针对南亚文化场景，覆盖多语言meme的文化上下文需求 |
| 区域适配性 | 新增孟加拉语方言meme子集，适配南亚区域方言的评估需求 |
| 评估场景设计 | 提供meme-only（仅视觉文本）与context-aware（带文化背景）两种评估场景 |
| 标注质量保障 | 每个meme配备文化背景说明与多个人类解释，提升评估准确性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MemeCULT-1K主基准 | 评估VLMs对南亚多语言meme的文化语境与幽默理解能力 |
| MemeCULT-1K补充集（54个孟加拉语方言meme） | 补充评估南亚区域方言meme的理解能力 |

🎯 实验设置与评估指标
实验任务为评估13款流行VLMs在meme-only和context-aware两种设置下的文化语境与幽默理解能力。
| 指标 | 含义 |
| --- | --- |
| SBERT相似度 | 衡量生成的meme解释与标准答案的语义相似度，↑越高越好 |
| BLEURT | 衡量生成的meme解释的流畅性与相关性，↑越高越好 |
| LLM-as-a-Judge评分 | LLM对生成meme解释合理性的评分，满分5，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 13款流行VLMs | 分为闭源、开源两类 | 均为当前主流多模态模型，用于meme理解的基准评估 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告所有对应明确表号的实验表格，仅在摘要中提及添加最小文化上下文可提升所有模型与语言的性能，但无对应表号、图号定位来源，因此无法生成规范表格。
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
💡 结论：添加最小程度的文化上下文对所有测试的VLMs在meme理解任务中的性能具有一致的提升作用，不同类型模型的缺陷类型存在差异。

4. 关键结论和发现
- 主要发现：① 提供最小文化上下文可显著提升VLMs在meme理解任务中的性能，且该提升作用在所有模型与语言中一致；② 闭源模型的主要错误集中于实体与参考识别，开源模型的瓶颈为更广泛的文化知识缺口，语言与音系层面的失败是两类模型共有的对上下文抗性最强的问题。
- 方法局限性：现有主流VLMs在南亚文化语境下的meme理解能力不足，尤其是对区域方言meme的理解有待提升。
- 未来工作：需开展明确的文化知识集成相关研究，以解决模型在文化适配meme理解任务中的缺陷。
> ✅ **总结一句话**：该论文提出了首个针对南亚文化语境的多语言meme理解基准，揭示了主流VLMs在文化知识与语用推理能力上的短板，为多模态模型的文化适配研究提供了关键基准支撑。

</details>

---

### 3. [DiDrive: A Risk-Aware Hierarchical Diffusion Framework for Safe Offline Reinforcement Learning in Autonomous Driving](https://arxiv.org/abs/2609.01609v1)

**Authors**: Qisong Guo, Jingtang Chen, Zhilin Chen, Pei Xu, Mingjian Fu, Wenxi Liu, Yuanlong Yu  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.01609v1  

#### Abstract
While diffusion models effectively capture multimodal behavioral priors for autonomous driving, offline reinforcement learning (RL) policies remain susceptible to distribution shift, heavy-tailed risk signals, out-of-distribution (OOD) action generation, and high-dimensional state redundancy. To add...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DiDrive: A Risk-Aware Hierarchical Diffusion Framework for Safe Offline Reinforcement Learning in Autonomous Driving
1. 论文的主要贡献和创新点
解决的问题
扩散模型虽可有效捕获自动驾驶的多模态行为先验，但离线强化学习（RL）策略仍面临分布偏移、重尾风险信号、分布外（OOD）动作生成、高维状态冗余等问题，难以满足安全自动驾驶的需求。

🚀 提出的新方法与思路
**Risk-Aware Hierarchical Diffusion (RHDif) architecture**：针对状态空间的高维冗余问题，在状态空间采用低层风险门控编码器与高层上下文调制器，过滤环境冗余信息，聚焦安全关键威胁。
**3DICE policy optimization paradigm**：针对动作空间的OOD高估与梯度振荡问题，在动作空间通过样本内校准引导、时空优化、基于集成的候选排序实现策略优化，缓解上述问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 状态处理 | 过滤高维环境冗余，聚焦安全关键威胁 |
| 动作优化 | 缓解OOD高估与梯度振荡问题，提升动作合理性 |
| 场景适配 | 在复杂高密交通场景中表现更优 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| CARLA benchmark | 模型性能评估 |

🎯 实验设置与评估指标
任务：自动驾驶安全离线强化学习任务
| 指标 | 含义 |
| ---- | ---- |
| 成功率 | 越高越好 |
| 平均奖励 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| IQL | 离线RL方法 | - |
| CQL | 离线RL方法 | - |
| Diffusion-QL | 扩散RL方法 | - |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（CARLA场景）**
因无法定位结果对应表号/图号，不给出具体数值，仅明确DiDrive在复杂、高密度（60辆车）的CARLA交通场景中性能优于基线方法IQL、CQL、Diffusion-QL。
💡 结论：DiDrive在复杂高密的交通场景下的表现优于现有主流离线RL及扩散RL基线方法，为安全自动驾驶决策提供了可靠路径。

其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：1）DiDrive通过RHDif与3DICE的协同架构，有效解决了离线RL应用于自动驾驶时存在的分布偏移、OOD动作生成、高维状态冗余等多种挑战；2）在复杂高密交通场景中，DiDrive的性能优于IQL、CQL、Diffusion-QL等基线方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DiDrive是一种结合Risk-Aware Hierarchical Diffusion架构与3DICE策略优化范式的安全离线强化学习框架，有效应对自动驾驶离线RL的核心挑战，在CARLA高密交通场景中表现优于现有主流基线方法。

</details>

---

### 4. [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1)

**Authors**: Yida Zhang, Zhiyong Gao, Shuaibing Yue, Jie Li, Rui Wang  
**Category**: cs.DC  
**Published**: 2026-09-03  
**Score**: 50.0  
**Type**: new  
**ArXiv ID**: 2609.02514v1  

#### Abstract
Deploying Large Language Models (LLMs) on edge devices typically relies on model compression or split inference. However, compression degrades reasoning capabilities, while split inference suffers from severe Wide Area Network (WAN) communication bottlenecks. Edge-cloud speculative decoding emerges ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
部署大语言模型(LLM)到边缘设备时，现有方案存在核心矛盾：模型压缩会降低推理能力，分割推理面临广域网(WAN)通信瓶颈；边缘云投机解码虽为替代方案，但不稳定的WAN会导致预测拒绝，触发管道停滞和网络回退，抵消协作增益。

🚀 提出的新方法与思路
**Probabilistic State Cache**：利用边缘设备的非饱和计算资源主动构建概率状态缓存，将网络范围的管道刷新转化为O(1)本地内存查找。
**Asymmetric Communication Protocol**：为节省带宽，采用非对称通信协议，上行传输最小的主链索引，下行传输紧凑的稀疏分布数据。
**Network-Aware Lagrangian-Optimized Resource Allocation Strategy**：引入网络感知的拉格朗日优化资源分配策略，动态最大化本地缓存命中率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理能力退化 | 避免模型压缩方法带来的推理能力下降问题 |
| WAN通信瓶颈 | 解决分割推理面临的WAN通信瓶颈，避免边缘云投机解码中预测拒绝导致的管道停滞与网络回退 |
| 缓存处理效率 | 将网络操作转化为本地O(1)查找，提升处理效率 |
| 带宽适应性 | 具有带宽免疫性，在受限WAN带宽下仍维持良好性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体使用的数据集 | 论文未报告 |

🎯 实验设置与评估指标
（任务：LLM协作推理的性能评估）
| 指标 | 含义 |
| --- | --- |
| 吞吐量 | LLM推理的每秒处理能力，↑越高越好 |
| 缓存命中率 | 本地状态缓存的命中比例，↑越高越好 |
| WAN带宽 | 衡量通信链路的带宽限制程度，数值越低代表越受限 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 模型压缩 | LLM部署技术 | 降低模型/计算量但退化推理能力 |
| 分割推理 | LLM部署技术 | 缓解边缘计算压力但面临WAN通信瓶颈 |
| 边缘云投机解码 | 协作式LLM推理技术 | 利用边缘小模型 draft token，但不稳定WAN下性能退化 |
| AceSpec | 提出的新框架 | 解决现有方案的核心缺陷，兼顾通信效率与推理性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验对应的表号、图号等来源信息，无法提供具体定量数值。
💡 结论：论文提及AceSpec实现了较好的吞吐量提升，在受限WAN带宽条件下仍能维持接近峰值的推理性能。

4. 关键结论和发现
- 主要发现：AceSpec通过概率状态缓存将网络操作转化为本地高效查找，解决了边缘云协作LLM推理中WAN波动导致的性能退化问题；其非对称通信协议和拉格朗日资源分配策略兼顾了通信效率与缓存性能；AceSpec具有带宽免疫性，在WAN受限场景下仍能维持良好推理性能。
- 方法局限性：论文未报告明确的方法局限性。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：AceSpec是一种非对称边缘云协作框架，通过概率状态缓存、非对称通信协议和网络感知的拉格朗日优化资源分配策略，解决了现有LLM部署方案的推理能力退化与WAN通信瓶颈问题，实现了高效的协作式LLM推理。

</details>

---

### 5. [CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling](https://arxiv.org/abs/2609.01864v1)

**Authors**: Zhengxiong Li, Tsung-Wei Huang, Umit Ogras  
**Category**: cs.DC  
**Published**: 2026-09-03  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2609.01864v1  

#### Abstract
NVIDIA distributed shared memory (DSMEM) enables direct shared-memory access within a thread block cluster. However, cluster synchronization, remote access, and resource costs make it difficult to determine when DSMEM improves performance. To fill this gap, we propose CREDIT, a cost-guided framework...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling
1. 论文的主要贡献和创新点
✅ 解决的问题
1. NVIDIA分布式共享内存（DSMEM）技术可实现线程块集群内的直接共享内存访问，但存在集群同步、远程访问、资源成本等问题，导致难以确定DSM EM何时能提升性能；2. 现有优化工具（torch.compile、Triton）及非DSMEM CUDA基线无法实现对DSMEM的高效适配，难以在各类工作负载上获得持续性能提升。

🚀 提出的新方法与思路
**profiling-driven characterization**：通过分析驱动的特征提取，识别可能从DSMEM技术中获益的工作负载模式；
**reduction-reuse workload transformation**：将DSMEM技术应用于归约-复用类型的工作负载；
**cost model based on profiling data**：基于profiling数据构建成本模型，用于判定DSMEM技术的适用盈利范围。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| DSMEM盈利能力预测 | 预测准确率达91.7% |
| RTX 5090性能加速 | 几何平均加速比1.466x，优于torch.compile、Triton及非DSMEM CUDA基线 |
| H100性能加速 | 几何平均加速比1.318x，优于torch.compile、Triton及非DSMEM CUDA基线 |
| 多工作负载适配 | 在全部6项测试工作负载上均实现优于对比基线的性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告具体数据集，仅提及在多种工作负载上开展评估 |

🎯 实验设置与评估指标
任务：评估CREDIT框架对DSMEM盈利能力的识别能力及在各类工作负载上的性能提升效果
| 指标 | 含义（箭头） |
| --- | --- |
| DSMEM盈利能力预测准确率 | 衡量对DSMEM适用场景的预测准确性，越高越好 |
| RTX 5090几何平均加速比 | CREDIT在RTX 5090上相对于对比基线的几何平均性能提升倍数，越高越好 |
| H100几何平均加速比 | CREDIT在H100上相对于对比基线的几何平均性能提升倍数，越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| torch.compile | 基线方法 | 现有主流GPU性能优化框架 |
| Triton | 基线方法 | 现有GPU编程优化工具 |
| optimized non-DSMEM CUDA baseline | 基线方法 | 未使用DSMEM技术的优化CUDA实现 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告对应定量结果的表号，具体定量结果如下：
1. DSMEM盈利能力预测准确率：91.7%
2. RTX 5090几何平均加速比：1.466x
3. H100几何平均加速比：1.318x
4. 多工作负载性能：在全部6项测试工作负载上，CREDIT均优于torch.compile、Triton及optimized non-DSMEM CUDA基线
💡 结论：CREDIT框架在DSMEM盈利能力预测和各类工作负载性能提升上均优于现有对比方法

4. 关键结论和发现
- 主要发现：1. CREDIT框架可准确识别DSMEM适用的工作负载模式，对DSMEM盈利能力的预测准确率达91.7%；2. 在RTX 5090和H100两种GPU上均能实现优于现有优化工具和基线的持续性能加速
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的CREDIT框架解决了DSMEM技术难以确定适用场景的问题，通过成本引导的方法实现对归约-复用工作负载的DSMEM优化，在多款GPU和多类工作负载上均获得了优于现有优化工具的性能表现。

</details>

---

### 6. [Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment](https://arxiv.org/abs/2609.01962v1)

**Authors**: Anirudh Malik, M Sparsh Mehra, Poojith Devan  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.01962v1  

#### Abstract
Ultra-low-bit language models can reduce storage and memory bandwidth, but a nominal "1.58-bit" label does not fully describe the stored representation, retained capability, or runtime behavior.
  We study an end-to-end post-training conversion of Qwen, an instruction-tuned 4B-parameter model, using...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment
1. 论文的主要贡献和创新点
✅ 解决的问题
超低比特语言模型的标称“1.58-bit”标签无法完整描述存储表示、模型能力及运行时行为；现有量化方案存在存储压缩与模型能力保留失衡，部署端推理效率存在不确定性。

🚀 提出的新方法与思路
**KOTMS旋转**：对权重进行变换，适配后续三值化操作；
**E2M-ATQ三值化**：实现权重的三值离散化，为量化核心模块；
**GPTQ-style误差补偿（来自TWLA）**：缓解量化误差，提升模型能力保留度；
采用权重-only量化方式，激活保持16位精度，省略ILA-AMP以适配权重-only场景。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 有效比特表征 | 端到端核算量化后有效比特为1.641每权重，比标称标签更准确表征存储特性 |
| 存储压缩效果 | 可将模型存储从8.29 GiB压缩至3.96 GiB，且压缩后模型困惑度基本不变 |
| 能力保留控制 | 结合误差补偿，在覆盖模型81.62%参数的情况下，保留部分任务的教师性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| BoolQ、ARC-Challenge | 评估量化后模型的任务能力保留 |
| WikiText-2、PTB、C4 | 评估量化后模型的语言建模困惑度 |

🎯 实验设置与评估指标
任务：Qwen3-4B的权重-only后训练三值化量化与部署特性全方面评估
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 有效比特 per weight | 表征量化后权重的实际存储比特数 |
| 任务准确率 | 越高越好 |
| 机会校正教师性能保留率 | 越高越好 |
| 困惑度 | 越低越好 |
| 模型存储大小 | 越小越好 |

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**有效比特与参数覆盖结果**（场景：Qwen3-4B权重-only三值化）
| 指标 | 数值 |
| --- | --- |
| 有效比特 per 量化线性权重 | 1.641 |
| 目标参数占比 | 81.62% |
💡 结论：采用KOTMS旋转+E2M-ATQ三值化+TWLA误差补偿的权重-only量化，实现约1.64位有效权重比特，覆盖模型81.62%参数，完成存储压缩准备。

**任务能力保留结果**（场景：10项任务的准确率对比）
| 方法 | 准确率 |
| --- | --- |
| 原始模型 | 64.5% ✅ |
| 量化后模型 | 54.7% |
| 补充信息 | BoolQ任务的机会校正教师性能保留率为84.6%，ARC-Challenge任务为43.8% |
💡 结论：量化后整体任务准确率下降，能力退化不均，不同任务的性能保留度差异显著。

**语言模型困惑度结果**（场景：WikiText-2、PTB、C4数据集）
| 数据集 | 原始模型困惑度 | 量化后模型困惑度 |
| --- | --- | --- |
| WikiText-2 | 13.639 | 18.748 |
| PTB | 24.700 | 31.992 |
| C4 | 19.831 | 28.966 |
💡 结论：量化后各数据集困惑度均上升，语言建模能力出现下降。

**存储压缩与部署结果**（场景：模型打包部署）
| 指标 | 数值 |
| --- | --- |
| 原始模型存储大小 | 8.29 GiB |
| 打包后模型存储大小 | 3.96 GiB |
| 补充信息 | 打包后模型困惑度基本不变；第三方打包尝试为有损，未纳入主结论；打包后模型的端到端任务准确率、生成吞吐量未基准；Triton GEMV微基准速度为FP16 cuBLAS的1/4.6 |
💡 结论：打包可大幅压缩存储，但当前打包方案未验证端到端核心部署性能，无法确认压缩可提升推理效率。

其余实验项（主benchmark性能、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告

4. 关键结论和发现
- 主要发现：① 针对Qwen3-4B的权重-only后训练三值化方案，可实现约1.64位有效权重比特，覆盖81.62%参数，存储压缩至原约47.8%；② 量化后整体任务准确率下降，能力退化不均，不同任务的机会校正教师性能保留率差异显著；③ 存储压缩打包后模型困惑度基本不变，但端到端任务性能、生成吞吐量未验证，初步微基准显示推理速度更慢，无法确认压缩可提升推理效率。
- 方法局限性：仅采用权重-only量化，未涉及激活量化；打包后模型的核心部署性能未验证；部分任务的性能保留度不足（如ARC-Challenge仅保留43.8%）。
- 未来工作：需验证打包后模型的端到端任务性能与生成吞吐量；优化量化方案以提升低保留度任务的能力；探索更高效的部署实现方案。

> ✅ **总结一句话**：本论文针对Qwen3-4B提出的权重-only后训练三值化方案，实现了存储大幅压缩，同时保留部分任务能力但退化不均，且压缩未带来端到端推理速度提升，需进一步完善部署相关性能验证。

</details>

---

### 7. [SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology](https://arxiv.org/abs/2609.02292v1)

**Authors**: Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko, Dmytro Vodianytskyi, Oleksandr Lukashov  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.02292v1  

#### Abstract
The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM数量激增且应用场景多样，但推理端点在质量、价格、延迟、上下文支持等多方面存在显著异质性；手动启发式方法难以维护，无法实现速度、成本、质量间持续有利的权衡；现有模型选择方法多依赖自回归生成、缓存效率低，且难以适配多任务属性需求。

🚀 提出的新方法与思路
**GLiClass-based lightweight router**：采用基于GLiClass的轻量框架，无需自回归生成即可为每个推理模型标签分配适用性评分，降低推理开销。
**Decoder-KV执行路径**：构建0.6B参数的checkpoint，结合Qwen3解码器与浅层双向评分器；保留会话级别的文本Key-Value缓存，仅编码新对话轮次，评估候选标签的临时token时不加入持久缓存，优化计算效率。
**任务本体驱动的策略分离学习**：构建含23个家族、115种任务类型、345种可路由子类型、1173个合成示例、30个正交领域的任务本体；基于此生成150,000个验证器评分任务与15,000个开放式任务，训练Qwen3解码器时明确分离请求预测与per-task属性策略（含资格、成本、缓存复用、安全、主权等），提升模型选择精准度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理开销 | 无需自回归生成，降低模型选择的推理延迟 |
| 缓存效率 | 仅编码新对话轮次，保留会话级KV缓存，不添加临时候选标签token到持久缓存，减少内存占用与计算量 |
| 任务支持能力 | 支持自定义zero-shot标签，还可预测任务类型、难度、推理模式、预期输出长度，适配多样任务需求 |
| 性能表现 | 在指定1000任务子集上聚合top-1分数达0.707，优于最强固定模型的0.696；在六个LiveBench子集上表现优于平均候选模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 自建任务本体衍生数据集 | 含23个家族、115种任务类型、345种可路由子类型、1173个合成示例、30个正交领域，用于生成150,000个验证器评分任务与15,000个开放式任务，支撑Qwen3解码器的请求预测及per-task属性策略训练 |
| LiveBench子集（共6个） | 用于评估SCX Router在实际场景中的模型选择性能 |

🎯 实验设置与评估指标
任务为LLM推理阶段的零样本模型选择，核心目标是实现速度、成本、质量的有利权衡。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 聚合top-1分数 | 所选模型对应任务的性能聚合值 | ↑ 越高越好 |
| LiveBench子集性能 | 在LiveBench各子集上的模型选择性能 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| mean candidate | 基线方法 | 所有候选模型的平均性能，作为性能对比的基准 |
| strongest fixed model | 基线方法 | 单一固定模型的最优性能，作为性能对比的基准 |
| SCX Router | 提出方法 | 轻量GLiClass-based路由器，无需自回归生成，结合Decoder-KV缓存机制，支持任务属性预测与自定义zero-shot标签 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

在指定1000任务子集上，SCX Router的聚合top-1分数为0.707，优于最强固定模型的0.696；在六个LiveBench子集上，SCX Router的性能优于平均候选模型。
💡 结论：SCX Router在LLM推理的零样本模型选择任务中，相比平均候选模型与最强固定模型，实现了更优的性能权衡。

4. 关键结论和发现
- 主要发现：1. 提出的SCX Router作为轻量零样本模型选择方法，通过GLiClass框架与Decoder-KV缓存机制，在保证性能的同时优化了推理效率；2. 基于构建的多维度任务本体生成的训练数据，有效支撑了模型选择策略的学习，分离请求预测与per-task属性提升了适配性；3. 在1000任务子集及六个LiveBench子集上，SCX Router的模型选择性能优于平均候选模型和最强固定模型。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出基于GLiClass的轻量零样本模型选择路由器SCX Router，结合Qwen3解码器与Decoder-KV缓存机制，通过构建的多维度任务本体训练策略，在LLM推理中实现了比平均候选模型和最强固定模型更优的速度-成本-质量权衡。

</details>

---

### 8. [How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?](https://arxiv.org/abs/2609.01798v1)

**Authors**: Wei Hu, Xiaolong Tu, Dawei Chen, Yitao Chen, Kyungtae Han, Haoxin Wang  
**Category**: cs.CL  
**Published**: 2026-09-03  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2609.01798v1  

#### Abstract
Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored. This paper aims to understand how two prompt properties, cognitive load and phrasing pattern, shape the energy...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?
1. 论文的主要贡献和创新点
✅ 解决的问题
端侧大规模语言模型（LLMs）部署日益广泛，能效是关键部署约束，但提示设计对端侧LLM推理能耗的影响尚未得到充分探索。
🚀 提出的新方法与思路
**阶段级能耗分析方法**：开展涵盖提示特性（认知负荷、措辞模式）、数据集、模型、设备的广泛实证研究，采用阶段级分析将推理能耗划分为prefill阶段和decode阶段分别研究。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 研究覆盖维度 | 首次系统探究提示设计特性（认知负荷、措辞模式）对端侧LLM推理能耗的影响，覆盖多类提示特性、数据集、模型与设备 |
| 分析粒度 | 采用阶段级能耗分析，分离prefill与decode阶段的能耗，明确不同提示特性对不同阶段能耗的影响 |
| 研究内容 | 同步开展能量-质量分析，揭示提示设计对端侧LLM推理能效与生成质量平衡的影响差异 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 用于探究提示特性等对端侧LLM推理能耗的影响 |
🎯 实验设置与评估指标
任务：探究提示的认知负荷、措辞模式及其他因素对端侧LLM推理能耗的影响，分析提示设计对应的能量-质量平衡。
| 指标 | 含义（箭头） |
| ---- | ---- |
| 阶段级能耗（prefill/decode） | 推理各阶段的能耗，↓越低越好 |
| 每token能耗 | 单个推理token对应的能耗，↓越低越好 |
| token使用量 | 推理过程中生成的token数量，↓越低越好 |
| 能量-质量平衡 | 推理能效与生成质量的权衡，论文未报告优化方向 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**摘要描述（无对应表）**
| 实验结果 | 具体内容 |
| ---- | ---- |
| 提示特性对能耗的影响 | 认知负荷主要影响每token的能耗，措辞模式主要通过token使用量影响能耗 |
| 能量-质量差异 | 提示设计对端侧LLM推理可达到的能量-质量前沿的影响因模型而异 |
💡 结论：提示特性（认知负荷、措辞模式）对端侧LLM推理能耗的影响机制不同，需结合模型特性进行提示设计以实现能效优化。
未覆盖实验情况：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 提示的认知负荷主要作用于端侧LLM推理的每token能耗；
2. 提示的措辞模式主要通过影响推理过程中的token使用量来作用于总能耗；
3. 提示设计对端侧LLM推理的能量-质量平衡的影响具有模型差异性，不同模型需适配对应提示设计以优化能效。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文系统实证研究了提示特性对端侧LLM推理能耗的影响，揭示了不同提示特性的能耗作用机制，为端侧LLM的模型感知提示设计提供了依据。

</details>

---

### 9. [Induction and Inquiry via Probabilistic Reasoning over Language and Code](https://arxiv.org/abs/2609.01815v1)

**Authors**: Wasu Top Piriyakulkij, Sam Acquaviva, Cassidy Langenfeld, Joshua Tenenbaum, Kevin Ellis  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.01815v1  

#### Abstract
How humans grow and maintain abstract knowledge from the sparse, streaming noisy data of experience is a longstanding challenge in cognitive science. Any computational account must satisfy at least three desiderata: It must be (1) data-efficient and compute-efficient, (2) capture gradations of uncer...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Induction and Inquiry via Probabilistic Reasoning over Language and Code
1. 论文的主要贡献和创新点
✅ 解决的问题
人类从稀疏、流式、带噪声的经验数据中成长和维持抽象知识是认知科学的长期挑战，计算该类知识成长的模型需满足三个核心要求：（1）数据高效与计算高效；（2）捕捉梯度不确定性以支持智能查询与信息收集；（3）灵活表征人类可学习与思考的无限范围概念。现有纯LLMs与经典贝叶斯模型存在缺陷：要么在基础任务中失败，要么无法复现人类行为，要么仅以极高的计算成本成功。

🚀 提出的新方法与思路
**心理程序编码与LLM引导的贝叶斯学习算法**：将符号知识编码为结合自然语言与源代码的心理程序，通过LLM引导的贝叶斯学习算法对心理程序进行顺序推断，以此构建满足核心要求的计算模型。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据与计算效率 | 相较于纯LLMs与经典贝叶斯模型，避免了过高计算成本，同时具备数据高效性 |
| 不确定性捕捉 | 支持梯度不确定性表征，可支撑智能查询与信息收集 |
| 概念表征灵活性 | 能够灵活表征人类可学习与思考的无限范围概念 |
| 人类行为复现能力 | 成功复现人类归纳学习与主动查询的定量特征（如锚定、花园路径效应） |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告具体使用的数据集

🎯 实验设置与评估指标：论文未报告具体的实验任务与评估指标

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 纯LLMs | 基线方法 | 要么在基础任务中失败，要么无法复现人类行为，要么仅以极高计算成本成功 |
| 经典贝叶斯模型 | 基线方法 | 要么在基础任务中失败，要么无法复现人类行为，要么仅以极高计算成本成功 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表号、图号及对应定量结果数值，仅提到该模型在一系列行为研究中成功复现人类归纳学习和主动查询的定量特征，如锚定、花园路径效应。

💡 结论：该模型可复现人类归纳学习和主动查询的相关定量特征。

4. 关键结论和发现
- 主要发现：1. 所提模型将符号知识编码为结合自然语言与源代码的心理程序，通过LLM引导的贝叶斯学习算法推断心理程序，满足数据/计算高效、捕捉不确定性、灵活表征无限概念三个核心要求；2. 该模型成功复现人类归纳学习与主动查询的定量特征（如锚定、花园路径效应）；3. 该模型相较于纯LLMs与经典贝叶斯模型，解决了任务失败、不复制人类行为或计算成本过高的缺陷。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了一种结合自然语言与源代码的心理程序表征，并通过LLM引导的贝叶斯学习算法顺序推断心理程序的计算模型，满足认知科学中知识成长与维持所需的三个核心要求，成功复现人类归纳学习和主动查询的相关特征，且性能优于纯LLMs与经典贝叶斯模型。

</details>

---

### 10. [DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents](https://arxiv.org/abs/2609.02059v1)

**Authors**: Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park, Xinyi Gu, Zexue He, Soochahn Lee, Rogerio Feris, Yong Jae Lee  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.02059v1  

#### Abstract
Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大语言模型（MLLMs）在图表、文档问答等结构化视觉理解任务上表现良好，但现有基准通常孤立评估图表或文本领域，未探索模型是否具备利用文本上下文选择、解释和聚合图表证据的核心能力。

🚀 提出的新方法与思路
**DocHop基准**：构建用于文档式图像的集成图表-上下文推理基准；采用stochastic logic-first generation pipeline生成，可控制推理深度与视觉密度，覆盖6个任务类别的2074个样本。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理整合能力 | 现有基准孤立评估图表或文本任务，DocHop支持整合文本上下文与图表证据的多步组合推理 |
| 可控性 | 现有基准未提及推理深度与视觉密度的可控性，DocHop可通过生成流程控制上述参数 |
| 任务覆盖 | 现有基准未明确任务类别数量，DocHop包含6个任务类别 |
| 样本规模 | 现有基准未明确样本量，DocHop覆盖2074个用于评估的样本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| DocHop | 用于评估多模态大语言模型的集成图表-上下文多跳推理能力 |

🎯 实验设置与评估指标
任务为针对文档式图像的集成图表-上下文多跳推理问答；评估指标为准确率（↑，越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 各类专有及开源多模态大语言模型（MLLMs） | MLLMs（专有/开源） | 用于DocHop基准的性能评估 |
| 推理增强模型 | 推理增强模型 | 用于DocHop基准的性能对比评估 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主 benchmark 性能：论文未报告
- 效率对比：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
💡 结论：现有多模态大语言模型在文档式图像的集成图表-上下文多跳推理任务上的性能与人类存在显著差距，推理增强模型可提升结果，但性能随推理复杂度增加而下降。

4. 关键结论和发现
- 主要发现：1. DocHop是用于评估模型整合文本上下文与图表证据多跳推理能力的可控基准；2. 现有模型在该任务上性能远低于人类水平；3. 推理复杂度会影响模型在该任务上的性能表现。
- 方法局限性：论文未报告明确的方法局限性细节。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：DocHop是针对信息密集型文档设计的可控基准，用于评估多模态大语言模型整合文本上下文与图表证据的多跳推理能力，现有模型性能与人类存在显著差距，推理增强模型有提升但受复杂度制约。

</details>

---

### 11. [CAT-Flow: Curvature-Adaptive sTeps for Flow Matching](https://arxiv.org/abs/2609.01746v1)

**Authors**: Qinchan Li, Pedro Cisneros-Velarde, Keru Fu, Samuel Antunes Miranda, Sharan Vaswani, Hao Zhang  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2609.01746v1  

#### Abstract
Flow Matching has emerged as a leading framework for generative modeling, powering state-of-the-art systems such as FLUX and Stable Diffusion 3.5. However, the iterative nature of its ODE-based sampling process creates a fundamental efficiency bottleneck: the quality of generated samples is highly s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CAT-Flow: Curvature-Adaptive sTeps for Flow Matching
1. 论文的主要贡献和创新点
✅ 解决的问题
Flow Matching作为领先的生成建模框架，其基于ODE的采样过程存在迭代式特性，导致核心效率瓶颈：生成样本质量高度依赖步长选择，现有文本到图像Flow Matching模型通常需要20到30步才能达到较好质量。

🚀 提出的新方法与思路
**CAT-OT**：训练-free的步长自适应算法，通过向量场时间导数的有限差分近似估计曲率，无需额外神经函数计算。
**CAT-OV**：训练-free的步长自适应算法，通过向量场梯度近似状态空间曲率，无需额外神经函数计算；在合适条件下，两种方法均具有常数阶截断误差界。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 生成效率 | 在四个文本到图像Flow Matching模型上，相比现有步长启发式，减少达到可比质量所需的生成步骤达40% |
| 图像质量 | 优于现有步长启发式的图像质量指标 |
| 计算成本 | 训练-free，无需额外神经函数计算 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为文本到图像生成，基于Flow Matching框架开展；评估指标为图像质量指标（↑ 越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有步长启发式 | 步长选择基线 | 通常需要20-30步生成才能达到较好图像质量，图像质量指标弱于提出方法 |

3. 主要实验结果和性能指标
**论文未报告具体实验表名（文本到图像Flow Matching模型场景）**
| 对比项 | CAT-OV/CAT-OT | 现有步长启发式 |
| --- | --- | --- |
| 图像质量指标 | 更优 | 较弱 |
| 达到可比质量的生成步骤 | 更少（最多减少40%） | 更多 |

💡 结论：提出的CAT-OV与CAT-OT步长自适应算法在四个文本到图像Flow Matching模型上，相比现有步长启发式，可减少生成步骤并提升图像质量。

4. 关键结论和发现
- 主要发现：1. 针对Flow Matching ODE采样的步长选择痛点，提出两种训练-free的步长自适应算法（CAT-OV、CAT-OT），无需额外神经函数计算；2. 两种算法在合适条件下具有常数阶截断误差界；3. 在四个文本到图像Flow Matching模型上，两种算法均优于现有步长启发式。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出两种训练-free的步长自适应算法CAT-OV与CAT-OT，用于Flow Matching的ODE采样，在文本到图像生成任务中相比现有步长启发式可减少最多40%的生成步骤并提升图像质量。

</details>

---

### 12. [DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation](https://arxiv.org/abs/2609.02170v1)

**Authors**: Wei Zhang, Hongji Li, Song Sun, Peng Yu, Xue Yang, Lei Zhao, Peng Jiang  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.02170v1  

#### Abstract
Advertising recommendation requires continuously tuning complex system parameters while balancing commercial returns and user experience. Recent work has introduced large language models (LLMs) with skill documents to assist this labor-intensive process, but skill optimization remains largely prompt...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation
1. 论文的主要贡献和创新点
✅ 解决的问题：广告推荐场景中，现有结合大语言模型（LLM）与技能文档的优化方法仍以prompt驱动为主，缺乏将奖励归因于具体文档编辑动作的机制，存在信用分配、长期结果估计不足的核心痛点。

🚀 提出的新方法与思路
**DMRL（Document-Mediated Reinforcement Learning）**：提出的技能自进化框架，将技能文档优化建模为一系列结构化编辑动作；采用双智能体架构，上层智能体执行受控文档编辑，下层任务智能体保持冻结状态，通过A/B测试评估编辑效果。
**DRPO（Dual-Relative Policy Optimization）**：针对信用分配与长期结果问题，提出的后训练策略优化方法，实现鲁棒且风险感知的优势估计。
**LRP（Long-term Reward Predictor）**：通过解耦表示学习与交叉注意力迁移，建模人口异质性，实现长期结果的有效估计。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 文档编辑归因机制 | 支持将奖励明确归因于具体的文档编辑动作 |
| 信用分配 | 通过DRPO实现鲁棒且风险感知的信用分配 |
| 长期结果估计 | 通过LRP建模人口异质性，实现长期结果的精准估计 |
| 技能优化范式 | 从prompt驱动转变为结构化文档编辑驱动的技能自进化 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为广告推荐系统的技能优化任务
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主基准性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. DMRL通过结构化文档编辑与双智能体架构，解决了现有广告推荐技能优化方法无法归因文档编辑奖励的核心痛点；2. DRPO与LRP组件分别针对性解决了信用分配与长期结果估计不足的问题；3. DMRL在大规模短视频广告平台部署后，在关键广告指标上取得优于SOTA的性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DMRL是一种面向广告推荐技能优化的文档介导强化学习框架，通过结构化文档编辑与双智能体机制，解决了现有prompt驱动方法无法归因文档编辑奖励的问题，在大规模短视频广告平台实现了优于SOTA的性能。

</details>

---

### 13. [Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling](https://arxiv.org/abs/2609.02566v1)

**Authors**: Pritthijit Nath, Sebastian Schemm, Peter Haynes, Emily Shuckburgh, Mark Webb  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.02566v1  

#### Abstract
Machine-learnt corrections can complement numerical weather prediction only if they adapt to the evolving model state while preserving dynamical consistency and numerical stability. To test this within a global forecasting model, we couple the Met Office (UKMO) Unified Model (UM) with distributed RL...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling

## 1. 论文的主要贡献和创新点
✅ 解决的问题
机器学习对数值天气预报的修正需适配演化的模型状态，同时保持动力一致性和数值稳定性，现有修正方法难以同时满足该两项核心需求。

🚀 提出的新方法与思路
**Distributed Model-Agent Coupling with DDPG**，将Met Office Unified Model（UM）与分布式RL代理通过rank-local tensors耦合；采用DDPG actor，其权重在每个大气柱的70个垂直模型层级共享，对模型倾向应用有界的位温修正；训练阶段基于十次nudged训练预报，以UKMO业务分析作为即时反事实目标，推理阶段采用非nudged预报。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 预报一致性 | 耦合工作流可完成训练，且非nudged推理阶段保持数值稳定性 |
| 预报精度 | 可降低部分纬度带的Z500平均绝对误差（MAE）与平均海平面气压（MSLP）误差 |
| 训练效率 | 基于nudged预报提供即时反事实目标，无需额外复杂数据准备 |

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| UKMO operational analysis | 作为训练阶段nudging计算的即时反事实目标 |
| 十次nudged training forecasts | 训练RL策略的输入数据 |
| Matched native UM forecast | 推理阶段的基线对照预报 |

🎯 实验设置与评估指标
任务：评估分布式在线RL策略用于UM数值天气预报偏差修正的有效性
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| Z500 MAE | 500hPa位势高度平均绝对误差，↓越低越好 |
| MSLP error | 平均海平面气压误差，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| native UM forecast | 基准预报方法 | 未应用RL修正的原生UM预报 |

## 3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告定量结果对应的表号、图号，无法定位来源；以下实验类型未在论文中报告：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告
（仅明确报告：耦合工作流成功完成训练，且在评估的非nudged预报案例中保持数值稳定性；RL策略在+6h预报时，相对于匹配的native UM forecast，降低了部分纬度带的Z500 MAE和MSLP误差）

## 4. 关键结论和发现
- 核心发现1：分布式模型-agent耦合的在线RL方法可与全球数值预报模型UM稳定集成，通过对模型倾向施加有界位温修正完成训练并实现非nudged推理。
- 核心发现2：该RL策略在+6h预报场景下，可有效降低部分纬度带的Z500 MAE与MSLP误差，展现了偏差修正的潜力。
- 方法局限性：仅为单案例实验，未报告泛化能力、效率、鲁棒性等关键属性，未开展多场景或多案例验证。
- 未来工作：扩展至更多案例验证、优化方法效率、适配业务数值预报系统的实际需求。

> ✅ **总结一句话**：本文通过分布式模型-agent耦合的DDPG方法，对Met Office Unified Model的模型倾向施加有界位温修正，以单案例实验验证了RL用于数值天气预报偏差修正的可行性与潜力，为业务系统应用奠定基础。

</details>

---

### 14. [TC-Next: Zero-Shot Multimodal Cyclone Forecasting](https://arxiv.org/abs/2609.02085v1)

**Authors**: Zhe Wang, Sijie Chen, Yiming Luo, Daehyun Kim, Chien-Yi Chang  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.02085v1  

#### Abstract
We present TropicalCycloneNext (TC-Next), a multimodal deep learning model that forecasts tropical cyclone track and intensity at $6$-$24$ h leads by leveraging a foundation model's forecast fields of atmospheric kinematic and thermodynamic fields and GridSat infrared satellite imagery. Trained only...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TC-Next: Zero-Shot Multimodal Cyclone Forecasting
1. 论文的主要贡献和创新点
✅ 解决的问题：热带气旋的路径与强度预报中，传统规则型预报器（如TempestExtremes）误差较大，现有专用预报模型泛化性不足，难以在不重新训练的情况下适配不同数值预报系统，单一模态的预报模型无法充分利用多源气象数据的价值。
🚀 提出的新方法与思路：**多模态深度学习模型TC-Next**，利用基础模型的大气运动与热力学场预报数据、GridSat红外卫星影像作为输入，实现热带气旋6-24小时的路径与强度预报；该模型仅在西太平洋的GraphCast预报数据上完成训练，具备zero-shot泛化能力，无需重新训练即可适配其他数值预报系统。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 泛化能力 | 仅在西太平洋GraphCast数据训练后，可zero-shot适配Pangu-Weather、IFS HRES、2025西太平洋WeatherNext Cyclones等不同气象数据，无需重新训练 |
| 预报精度 | 对比传统规则型预报器TempestExtremes，路径误差降低15-44%，强度误差降低3-6倍；对比WeatherNext Cyclones专用直接预报器，2025西太平洋场景下强度误差更低、路径误差相当或更低 |
| 信息利用 | 通过融合多源气象数据，提升各lead时间的路径预报精度及较长lead时间的强度预报精度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 西太平洋GraphCast预报数据 | 训练TC-Next的基础数据集 |
| Pangu-Weather预报数据 | 测试TC-Next泛化能力的数据集 |
| IFS HRES预报数据 | 测试TC-Next泛化能力的数据集 |
| 2025西太平洋WeatherNext Cyclones generic天气场 | 测试TC-Next zero-shot适配WeatherNext Cyclones的数据集 |
| GridSat红外卫星影像 | TC-Next的多模态输入数据 |

🎯 实验设置与评估指标
任务：预报热带气旋6-24小时的路径与强度，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 路径误差 | 热带气旋路径预报的位置误差，↓ 越低越好 |
| 强度误差 | 热带气旋强度预报的数值误差，↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| TempestExtremes | 传统规则型预报器 | 经典的热带气旋路径与强度预报方法，基于规则设计 |
| WeatherNext Cyclones专用直接预报器 | 专用预报模型 | 针对WeatherNext Cyclones设计的热带气旋专用预报方法 |
| GraphCast、Pangu-Weather、IFS HRES | 数值预报系统 | 不同的气象数值预报系统，用于训练或测试TC-Next的性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
**主 benchmark性能（TC-Next对比TempestExtremes，基于GraphCast）**
| 指标 | 性能对比结论 |
| ---- | ---- |
| 路径误差 | 降低15-44% |
| 强度误差 | 降低3-6倍 |
💡 结论：基于GraphCast预报数据训练的TC-Next，对比传统规则型预报器TempestExtremes，路径和强度预报误差均显著降低。

2. 跨域/zero-shot迁移性能
**跨域/zero-shot迁移性能（TC-Next适配Pangu-Weather、IFS HRES）**
| 目标数值预报系统 | 对比对象 | 性能表现 |
| ---- | ---- | ---- |
| Pangu-Weather | TempestExtremes | 性能更优 |
| IFS HRES | TempestExtremes | 性能更优 |
💡 结论：TC-Next无需重新训练，zero-shot适配不同数值预报系统后，性能仍优于传统规则型预报器TempestExtremes。

3. zero-shot适配WeatherNext Cyclones性能
**zero-shot适配WeatherNext Cyclones性能（2025西太平洋场景）**
| 指标 | TC-Next性能 | WeatherNext Cyclones专用直接预报器性能 |
| ---- | ---- | ---- |
| 强度误差 | 所有lead时间更低 | - |
| 路径误差 | 更低或相当 | - |
💡 结论：TC-Next在2025年西太平洋场景下，zero-shot适配WeatherNext Cyclones的generic天气场时，强度预报性能更优，路径预报性能相当或更优。

4. 消融实验
**消融实验（多模态输入对比）**
| 模块（红外卫星影像模态） | 路径误差表现 | 强度误差表现 |
| ---- | ---- | ---- |
| 启用（多模态） | 各lead时间更优 | 较长lead时间更优 |
| 禁用 | 对应性能下降 | 对应性能下降 |
💡 结论：融合红外卫星影像的多模态输入可提升TC-Next的预报性能，尤其对路径误差和较长lead时间的强度误差增益明显。

5. 其他实验
效率对比：论文未报告
鲁棒性/扰动测试：论文未报告

4. 关键结论和发现
- 核心发现1：TC-Next是具备zero-shot跨系统泛化能力的多模态深度学习模型，可显著降低热带气旋6-24小时的路径与强度预报误差，表现优于传统规则型预报器和专用预报模型。
- 核心发现2：多模态输入（融合红外卫星影像）可有效提升TC-Next的预报性能，对各lead时间的路径预报精度及较长lead时间的强度预报精度增益明显。
- 核心发现3：TC-Next仅需在西太平洋GraphCast数据上训练，即可零泛化适配不同的气象数值预报系统，展现出良好的泛用性。
方法局限性：论文未报告明确的方法局限性
未来工作：论文未报告明确的未来工作规划

> ✅ **总结一句话**：TC-Next是一款多模态深度学习模型，具备zero-shot跨系统泛化能力，可显著提升热带气旋6-24小时的路径与强度预报精度，相比传统预报器和专用模型性能更优。

</details>

---

### 15. [Refining Heuristic-Based Bitcoin Address Clustering with Graph Neural Networks](https://arxiv.org/abs/2609.01942v1)

**Authors**: Hugo Schnoering, Roman Bresson, Michalis Vazirgiannis  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2609.01942v1  

#### Abstract
Bitcoin's pseudonymous nature makes it challenging to analyze user-level activity, since a single user may control multiple identifiers (addresses). Existing heuristic-based methods attempt to identify addresses belonging to the same user, but they often produce flat cluster assignments with limited...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Refining Heuristic-Based Bitcoin Address Clustering with Graph Neural Networks
1. 论文的主要贡献和创新点
✅ 解决的问题：比特币的假名特性使得用户级活动分析面临挑战，因为单个用户可能控制多个地址；现有基于启发式的聚类方法生成平面簇分配，模块化有限，且易出现合并不同用户地址的错误。

🚀 提出的新方法与思路
**GNN对比嵌入学习**：提出学习与启发式聚类一致的地址嵌入的方法，该方法带有理论指导直觉，为聚类细化提供可靠的表示基础；
**层次聚类细化**：采用层次聚类对启发式得到的簇进行更精细的分析，并提供用于标记可疑合并的量化标准；
核心贡献还包括公开包含大量簇的比特币交易图数据集，为相关研究提供数据支撑。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 聚类质量 | 细化启发式得到的簇，优化模块化不足的问题 |
| 错误控制 | 提供量化标准，减少启发式聚类中合并不同用户地址的错误 |
| 数据支持 | 公开带大量簇的比特币交易图数据集，降低相关研究的数据获取门槛 |
| 方法合理性 | 基于理论指导构建与启发式一致的嵌入，提升聚类表示的合理性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 公开可用的比特币交易图数据集（含大量簇） | 用于比特币地址聚类相关研究 |

🎯 实验设置与评估指标
任务为比特币地址聚类，论文未报告具体的实验设置与评估指标。

⚔️ 基线方法对比
论文未报告任何基线方法对比的相关内容。

3. 主要实验结果和性能指标
所有实验相关内容均未在论文中报告：
**表N：名称（场景）**
论文未报告
💡 结论：论文未报告具体实验结论。

4. 关键结论和发现
- 主要发现：1）基于GNN对比嵌入结合层次聚类的方法可有效细化启发式比特币地址聚类；2）该方法能提供量化标准标记启发式聚类中的可疑合并；3）公开的带大量簇的比特币交易图数据集为比特币地址聚类研究提供了可用资源。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：该论文提出基于GNN对比嵌入与层次聚类的比特币地址聚类细化方法，优化了现有启发式聚类模块化不足、易合并不同用户地址的问题，并公开了相关研究所需的带大量簇的比特币交易图数据集。

</details>

---

### 16. [SALA: Semantic-Aware Logical Alignment for Complex Reasoning in In-Context Learning](https://arxiv.org/abs/2609.02336v1)

**Authors**: Zhao Ji, Wenqing Chen, Zhixuan Chu, Jianxing Yu, Jingping Liu, Shanhe Zhao, Zibin Zheng  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.02336v1  

#### Abstract
Effective in-context learning (ICL) for complex reasoning relies on selecting the right demonstrations. Traditional retrieval methods based on surface similarity fail to capture the underlying problem-solving logic. Recent logic-based methods address this by matching predefined reasoning steps, but ...

---

### 17. [Source Distribution Estimation by Posterior Averaging](https://arxiv.org/abs/2609.02622v1)

**Authors**: Trung-Dung Hoang, Lisa M. Koch  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.02622v1  

#### Abstract
Simulation-based science often requires a distribution over simulator parameters whose push-forward reproduces a set of real observations: this is the source distribution estimation (SDE) problem. Existing methods fit the source against a likelihood surrogate trained once from a fixed proposal prior...

---

### 18. [IDEEA: training-free Input-Dependent stEEring via Activation cluster matching](https://arxiv.org/abs/2609.02089v1)

**Authors**: Zheng Wang, Muchen Li, Renjie Liao, Yan Leng  
**Category**: cs.CL  
**Published**: 2026-09-03  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2609.02089v1  

#### Abstract
Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independ...

---

### 19. [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236v1)

**Authors**: Yuyao Zheng, Haipeng Sun, Junwei Bao, Lemao Liu, Hongfei Jiang, Yang Song, Dejing Dou  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2609.02236v1  

#### Abstract
Group-based reinforcement learning (RL) has become an effective paradigm for LLM post-training, but in multi-turn agentic tasks with sparse terminal rewards, it often provides coarse credit for intermediate actions. To obtain more fine-grained credit assignment, recent work such as GiGPO introduces ...

---

### 20. [Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems](https://arxiv.org/abs/2609.02264v1)

**Authors**: Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2609.02264v1  

#### Abstract
Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, yet current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the $N \times N$ adjacency space, and a graph-network p...

---

### 21. [Act More, Decide Less: Skill-Guided Adaptive Action Chunking for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.02042v1)

**Authors**: Yanting Yang, Can Jin, Jinman Zhao, Jiahao Wu, Yang Zhou, Zhepeng Wang, Zhendong Wang, Mu Zhou, Dimitris N. Metaxas  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2609.02042v1  

#### Abstract
Large language model (LLM) agents for long-horizon interactive tasks typically follow a ReAct-style protocol, issuing one primitive action per LLM round. While this enables frequent replanning, it is inefficient for long-horizon tasks where many rounds are spent on routine action sequences. A natura...

---

### 22. [Predictors of Loneliness in Older Adults Using Multimodal Analysis of Speech and Language](https://arxiv.org/abs/2609.02606v1)

**Authors**: Vinmay Khandode, Sai Karthik Kosuri, Neil K. R. Sehgal, Adam Greene, Elif Alpoge, Elana Duffy, Matthew Lee Smith, Thomas K. M. Cudjoe, Sharath Chandra Guntuku  
**Category**: cs.CL  
**Published**: 2026-09-03  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.02606v1  

#### Abstract
Loneliness is a critical public health issue among older adults, linked to higher risks of depression, cognitive decline, and mortality. Scalable, objective methods for its detection remain limited, particularly in natural conversational contexts. We analyzed speech and language markers of lonelines...

---

### 23. [MineTRACE: An Evidence-Grounded Interactive Reasoning System for Mineral Prospectivity](https://arxiv.org/abs/2609.02060v1)

**Authors**: Yiran Zhang, Jinwen Liu, Daniel Su, Yisu Chen, Qiang Sun, Chris Gonzalez, Eun-Jung Holden, Marco Fiorentini, Wei Liu, Yihao Ding  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.02060v1  

#### Abstract
Mineral exploration requires integrating heterogeneous geochemical, geophysical, and geological evidence, yet existing prospectivity systems often provide only opaque scores or heatmaps. We present MineTRACE, a web-based system for evidence-grounded exploration of eight commodities: Cu, Au, Ni, W, S...

---

### 24. [PEARL: Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion](https://arxiv.org/abs/2609.02216v1)

**Authors**: Yunchi Yang, Longlong Li, Cunquan Qu  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.02216v1  

#### Abstract
Inductive knowledge graph completion (IKGC) aims to predict missing links involving entities unseen during training, requiring models to learn transferable relational and structural patterns. Existing subgraph- and path-based approaches often encode relational paths independently of their surroundin...

---

### 25. [CAHR-Net: Condition-Adaptive Hysteresis Reconstruction for Compact and Interpretable Magnetic Core Loss Modeling](https://arxiv.org/abs/2609.01991v1)

**Authors**: Chunye Gong, Cong Yao  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.01991v1  

#### Abstract
Magnetic core loss originates in the hysteresis loop: the energy dissipated per excitation cycle equals the loop area, and frequency, temperature, and waveform shape set the loss by reshaping the loop geometry. Most existing models let these conditions act only on a terminal scalar - empirical equat...

---

### 26. [Exact Limits of Random Projections for Preserving Geometry: Distance Recovery, Nearest-Neighbor Rankings, and Covariance Shape in Gaussian Models](https://arxiv.org/abs/2609.02155v1)

**Authors**: Piyush Sao  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.02155v1  

#### Abstract
The Johnson-Lindenstrauss (JL) lemma guarantees that a random projection of $n$ points to
  $m=O(\varepsilon^{-2}\log n)$ dimensions preserves pairwise squared distances within relative
  error $\varepsilon$ with high probability, and this dimension order is asymptotically
  optimal. In high dimensi...

---

### 27. [Cliff: Learning Process Rewards from the First Mistake](https://arxiv.org/abs/2609.02817v1)

**Authors**: Peixuan Han, Runhui Wang, Ketan Ramaneti, Jie Hao, Gerald Friedland, Chris Kong  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2609.02817v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for large language model (LLM) post-training, but its reliance on coarse outcome rewards leads to limited guidance on intermediate reasoning processes. Existing approaches such as process reward modeling and on-...

---

### 28. [ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations](https://arxiv.org/abs/2609.01992v1)

**Authors**: Peiying Zhu, Sidi Chang  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.01992v1  

#### Abstract
Agent evaluations face two distinct evidentiary questions: whether a reported claim is recomputable from retained evidence (sufficiency), and whether the retained records cover the committed experiment set (coverage). Generic logs and hash-linked transcripts answer neither reliably. We introduce Cla...

---

### 29. [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](https://arxiv.org/abs/2609.02253v1)

**Authors**: Jie Ding, Rui Sun, Xinyuan Zhang, Zeyu Zhang, Xin Liu  
**Category**: cs.AI  
**Published**: 2026-09-03  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.02253v1  

#### Abstract
Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-m...

---

### 30. [A Study of Conditional Diffusion Models for Open-Loop Control under Dry Friction and Stiction](https://arxiv.org/abs/2609.01756v1)

**Authors**: Eric Aislan Antonelo  
**Category**: cs.LG  
**Published**: 2026-09-03  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2609.01756v1  

#### Abstract
Diffusion models have recently emerged as expressive generative priors for planning and control. This paper studies Action Diffusion, an action-sequence diffusion formulation used as an open-loop proposal distribution for a point-mass system with dry friction and stiction. In this benchmark, motion ...

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
