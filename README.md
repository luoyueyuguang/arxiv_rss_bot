# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-03 09:20:40 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs](https://arxiv.org/abs/2607.28848v1)

**Authors**: Jiaxuan Chen, Jianshu She, Ye Yuan, Rajat Ghosh, Karan Gupta, Qirong Ho, Xue Liu, Oana Balmau  
**Category**: cs.DC  
**Published**: 2026-08-03  
**Score**: 68.0  
**Type**: new  
**ArXiv ID**: 2607.28848v1  

#### Abstract
LLM serving systems are provisioned for peak load to meet strict latency targets, leaving substantial GPU compute idle whenever traffic falls below peak. We present DeltaServe, a host-agnostic co-serving design that converts this idle inference capacity into LoRA fine-tuning throughput while preserv...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
LLM serving系统按峰值负载配置GPU资源，流量低于峰值时存在大量GPU计算资源空闲；现有协同 serving方法（如LLMStation）无法同时兼顾高微调吞吐量和100%推理SLO合规性，分开运行推理与微调的基线方案（如vLLM+torchtune）未利用空闲资源，硬件利用率低。

🚀 提出的新方法与思路
**DeltaServe**：是宿主无关的LLM推理与LoRA微调协同 serving设计，核心是将LLM推理场景中的空闲GPU计算资源转化为LoRA微调吞吐量，同时保留推理SLO。它通过仅需多LoRA批处理支持的紧凑钩子接口集成现有推理引擎；利用推理预填与LoRA微调前向传播的共享执行结构；采用SLO感知调度器，仅当存在足够推理余量时才接纳并执行微调任务；调度器由离线校准、在线优化的CUDA-graph感知延迟模型驱动，已集成至vLLM、SGLang、S-LoRA。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 微调吞吐量 | 基于vLLM时是LLMStation的2.9倍，比vLLM+torchtune高39% |
| 推理SLO合规率 | 100%合规，优于LLMStation的85% |
| 资源利用率 | 无需额外硬件，充分利用空闲GPU资源 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Company X生产轨迹 | 协同 serving性能实验评估 |

🎯 实验设置与评估指标
任务为LLM推理与LoRA微调的协同 serving性能测试；指标如下：
| 指标 | 含义 |
| --- | --- |
| 微调吞吐量 | 衡量LoRA微调任务的处理能力，↑越高越好 |
| 推理SLO合规率 | 衡量推理任务满足服务水平目标的比例，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| LLMStation | 基线方法 | 现有协同 serving方案，兼顾推理与微调 |
| vLLM+torchtune | 基线方法 | 推理与微调分开运行的方案，作为性能参照 |
| DeltaServe（vLLM/SGLang/S-LoRA） | 提出的方法 | 集成至多种现有推理引擎的协同 serving方案，利用空闲GPU |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主基准性能（Company X生产轨迹场景）**
| 方法 | 微调吞吐量对比（vs LLMStation） | 微调吞吐量对比（vs vLLM+torchtune） | 推理SLO合规率 |
| --- | --- | --- | --- |
| LLMStation | 1.0x | - | 85% |
| vLLM+torchtune | - | 1.0x | 100% |
| DeltaServe（vLLM） | 2.9x ✅ | 1.39x ✅ | 100% ✅ |
💡 结论：在Company X生产轨迹场景中，基于vLLM的DeltaServe可实现比现有协同 serving方案更高的微调吞吐量，且完全满足推理SLO，无需额外硬件。

论文未报告效率对比（除微调吞吐量外的效率指标）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验相关内容。

4. 关键结论和发现
- 主要发现：① DeltaServe通过协同 serving设计，可在不增加硬件的前提下将LLM推理场景的空闲GPU计算资源转化为LoRA微调吞吐量；② 基于vLLM实现的DeltaServe相比现有基线方案，微调吞吐量提升显著，同时保持100%推理SLO合规性；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；

> ✅ **总结一句话**：DeltaServe是一种宿主无关的LLM推理与LoRA微调协同 serving方案，可利用推理场景的空闲GPU资源提升微调吞吐量，同时保证推理服务水平目标合规性，集成至多种现有推理引擎均能获得优异性能。

</details>

---

### 2. [How Hard Does It Think? Analyzing Step-Aware Reasoning Energy in LLM Chain-of-Thought Trajectories](https://arxiv.org/abs/2607.28674v1)

**Authors**: Hui Wei, Junda Wu, Sheldon Yu, Sizhe Zhou, Yizhu Jiao, Ming Zhong, Bowen Jin, Tong Yu, Shijia Pan, Jiawei Han, Julian McAuley  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2607.28674v1  

#### Abstract
Understanding how computational effort is allocated across individual chain-of-thought (CoT) reasoning steps remains an open challenge: existing interpretability methods rely on output-level signals or collapse processing depth into a single trajectory-level scalar, leaving step-wise effort opaque. ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

How Hard Does It Think? Analyzing Step-Aware Reasoning Energy in LLM Chain-of-Thought Trajectories
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM可解释性方法存在两方面缺陷：一是依赖输出级信号，无法揭示推理过程内部的细节；二是将处理深度简化为单轨迹级标量，导致步骤级的计算投入（effort）处于不透明状态。

🚀 提出的新方法与思路
**Step-Aware Reasoning Energy (SARE)**，是一个几何框架：通过计算相邻Transformer层中token隐状态的Gram矩阵之间的Centered Kernel Alignment (CKA)，在单个Chain-of-Thought（CoT）步骤的粒度上量化计算投入，无需特征向量对齐或集群对应即可捕捉token间的关系结构；同时将该推理能量与推理的语义演进关联，把CoT轨迹建模为潜在语义状态的转换过程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 信号粒度 | 提供CoT推理步骤级的计算投入量化，避免现有方法的输出级或轨迹级信号的局限 |
| 结构捕捉 | 基于CKA捕捉token间的关系结构，无需特征向量对齐或集群对应 |
| 语义关联 | 关联推理能量与推理的语义演进，建模为潜在语义状态转换，更贴合推理本质 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 六个推理基准 | 用于评估SARE在推理步骤级计算投入量化上的有效性 |

🎯 实验设置与评估指标
任务：在三个开放权重LLMs上，分析CoT轨迹的步骤级推理能量及SARE特征的预测性能。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确报告具体指标的定义及方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 输出级置信度基线 | 输出级信号基线 | 依赖模型输出层的置信信号，而非内部步骤级的几何动态信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（推理任务）**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表2：效率对比（FPS/参数量）**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表3：跨域/zero-shot迁移性能**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表4：鲁棒性/扰动测试性能**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

**表5：消融实验结果**
论文未报告
💡 结论：论文未报告相关结果，无法得出对应结论。

仅明确的定性实验结果：在六个推理基准和三个开放权重LLMs上的实验发现：
1. 推理能量在不同步骤类型间分布高度非均匀，存在轨迹级指标无法察觉的阶段式转换；
2. 错误CoT轨迹在关键推理节点的推理能量系统性低于正确轨迹；
3. SARE-based特征在多数设置下匹配或优于输出级置信度基线的性能。

4. 关键结论和发现
- 主要发现：
  1. LLM-CoT推理的步骤级计算投入（能量）呈非均匀分布，存在阶段式转换特性，现有轨迹级指标无法捕捉该特性；
  2. 错误推理轨迹在关键推理节点的计算投入显著低于正确推理轨迹，可作为判断推理正确性的潜在信号；
  3. SARE能够有效捕捉LLM-CoT的内部几何动态，其生成的特征携带了超出表面输出信号的预测信息，性能优于或匹配传统输出级置信度信号。
- 方法局限性：论文未报告明确的局限性内容。
- 未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：本文提出的SARE几何框架，实现了LLM-CoT推理步骤级计算投入的量化，揭示了推理过程中内部动态的非均匀性与预测价值，弥补了现有可解释性方法在步骤级信号捕捉上的不足。

</details>

---

### 3. [Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models](https://arxiv.org/abs/2607.28707v1)

**Authors**: Sara Candussio, Daniel Scalena, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2607.28707v1  

#### Abstract
Entropy-based pruning has been proposed as an effective method for compressing Chain-of-Thought (CoT) reasoning with negligible accuracy loss. We test the robustness of low- and high-entropy CoT step selection methods across various models and reasoning tasks, showing that entropy offers no advantag...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models
1. 论文的主要贡献和创新点
✅ 解决的问题
- 熵剪枝曾被认为是压缩Chain-of-Thought（CoT）且精度损失可忽略的有效方法，但本文针对其鲁棒性提出质疑：低/高熵CoT步骤选择方法在各模型与任务中均未展现出优于随机剪枝的优势；
- 针对token级CoT压缩，现有观点认为保留低熵token有效仅在数学基准任务中成立，本文需明确该特性的本质原因；
- 现有研究可能认为任务信息集中于少数可通过启发式识别的CoT token，本文需验证该观点的正确性。

🚀 提出的新方法与思路
**系统性熵选方法鲁棒性验证思路**：针对低/高熵CoT步骤选择方法，在多种模型与推理任务中开展对比实验，评估其压缩性能是否优于随机剪枝；
**token级熵选压缩特性分析思路**：将CoT压缩从步骤转向token级，分析保留低熵token的效果及适用场景，结合数值token的熵与语义属性解释其仅在数学基准任务中有效的原因；
**CoT信息分布特性探究思路**：设计补token实验，通过补少量带原始激活的CoT token，验证是否能恢复近完整推理性能，明确任务信息的分布特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 熵选方法鲁棒性验证 | 系统性测试了低/高熵CoT步骤选择方法的鲁棒性，证实其无额外性能增益 |
| 压缩场景特性分析 | 明确了token级熵选压缩的适用边界（仅数学基准有效）及本质原因 |
| 推理信息分布验证 | 通过补token实验提供因果证据，推翻任务信息集中于少数启发式token的观点 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体使用的数据集，仅提及数学基准任务相关场景 |

🎯 实验设置与评估指标
实验任务：针对CoT压缩场景，在多种模型与推理任务中，对比不同熵选策略、随机剪枝及全保留策略的性能表现
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体评估指标及方向（如准确率损失、效率指标等） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 低熵CoT步骤选择方法 | 熵选类基线 | 优先保留低熵的CoT步骤以实现压缩 |
| 高熵CoT步骤选择方法 | 熵选类基线 | 优先保留高熵的CoT步骤以实现压缩 |
| 随机剪枝方法 | 对比基线 | 随机选择保留CoT步骤，作为性能参考 |
| 保留低熵token方法 | 熵选类基线 | 优先保留低熵的CoT token以实现压缩 |
| 全trace方法 | 完整策略基线 | 保留所有CoT内容，作为性能上限参考 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：熵选CoT步骤选择方法性能对比（跨模型、跨任务场景）**
论文未报告

💡 结论：在所有评估的模型与任务场景下，低/高熵CoT步骤选择方法的压缩性能均未优于随机剪枝方法。

**表2：token级熵选压缩性能对比（数学基准任务与其他任务）**
论文未报告

💡 结论：保留低熵token的CoT压缩策略仅在数学基准任务中有效，该现象源于数学问题中数值token天生具有低熵特性且同时承担语义表达作用。

**表3：补token实验性能结果（少量激活token补全后）**
论文未报告

💡 结论：仅需补全少量带有原始激活的CoT token即可恢复接近完整推理链的性能，提供了任务信息分布式存在于整个CoT中的因果证据。

4. 关键结论和发现
- 主要发现
1. 低/高熵CoT步骤选择方法在跨模型、跨任务的所有评估场景下，CoT压缩性能均未优于随机剪枝；
2. token级熵选压缩的保留低熵token策略仅在数学基准任务中有效，其本质原因是数学问题中的数值token天生具有低熵特性且兼具语义内容；
3. 任务信息并非集中于少数可通过熵启发式识别的CoT token，而是分布式存在于整个推理链中，仅需补少量带原始激活的CoT token即可恢复近完整性能。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：本文通过系统性实验验证了熵选类CoT压缩方法的局限性，明确了CoT压缩在步骤级与token级的性能特性及推理信息的分布式本质，为后续CoT压缩研究提供了关键实证依据。

</details>

---

### 4. [SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving](https://arxiv.org/abs/2607.29575v1)

**Authors**: Pol G. Recasens, Ferran Agullo, Yue Zhu, Chen Wang, Jordi Torres, Josep Ll. Berral  
**Category**: cs.DC  
**Published**: 2026-08-03  
**Score**: 57.5  
**Type**: new  
**ArXiv ID**: 2607.29575v1  

#### Abstract
Large language model (LLM) serving commonly increases batch size to improve throughput, but performance eventually reaches a deployment-dependent plateau beyond which larger batches provide marginal gains while increasing latency and GPU memory consumption. Previous studies have attributed this beha...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题：LLM Serving中，增大批次（batch）可提升吞吐量，但最终会达到部署依赖的饱和平台，更大批次带来的吞吐量增益极小，反而会增加延迟与GPU显存消耗；此前研究将该行为归因于HBM/DRAM带宽限制，但背后原因仅基于概念论证或高层次性能观测，缺乏详细硬件层面支撑。

🚀 提出的新方法与思路
**SLIM（Saturation-Aware Lightweight Performance Model）**：构建半分析模型，基于Transformer计算与内存流量的分析公式，预测LLM推理的吞吐量与延迟；
**BCA（Batching Configuration Advisor）**：选择满足目标延迟约束的最高吞吐量批处理配置，针对评估的OPT模型，识别出可避免多达55GB的GPU显存分配（吞吐量损失极小）。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 性能建模准确性 | SLIM优于代表性性能建模基线方法 |
| 泛化能力 | SLIM可成功泛化到未见过的运行条件 |
| 饱和归因科学性 | 明确将吞吐量饱和归因于解码阶段注意力核的特性（活跃上下文长度导致算术强度恒定），而非仅概念层面的带宽限制，具备硬件表征支撑 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告

🎯 实验设置与评估指标
任务为LLM Serving的吞吐量与延迟预测及批处理配置优化；
| 指标 | 含义 |
| ---- | ---- |
| 吞吐量 | 越高越好，代表LLM推理的处理能力 |
| 延迟 | 越低越好，代表LLM推理的响应速度 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SLIM | 半分析性能建模方法 | 基于硬件表征的饱和感知模型，用于预测LLM推理的吞吐量与延迟，支持批处理配置优化 |
| 代表性性能建模基线方法 | 传统性能建模方法 | 无硬件层面的饱和归因，性能预测与泛化性弱于SLIM |

3. 主要实验结果和性能指标
论文未报告

4. 关键结论和发现
- 主要发现：1. LLM Serving中吞吐量饱和的核心原因是解码阶段注意力核的特性：活跃上下文长度使注意力核算术强度近乎恒定，引发DRAM带宽饱和，此时计算吞吐量远低于硬件极限；2. 所提SLIM半分析模型的性能预测准确性与泛化性优于代表性基线方法；3. 针对评估的OPT模型，BCA可识别出多达55GB的GPU显存分配可避免，吞吐量损失极小。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：本文提出的饱和感知轻量级性能模型SLIM与批处理配置顾问BCA，解决了LLM Serving中吞吐量饱和的归因难题与高效配置优化问题，提升了性能预测的准确性和泛化性，同时减少了不必要的GPU显存消耗。

</details>

---

### 5. [TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs](https://arxiv.org/abs/2607.28640v1)

**Authors**: Andong Hua, Colton Bishop, Igor Mordatch, Arian Hosseini, Jindong Gu, Aleksandra Faust, Rebecca Roelofs, Yao Qin  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2607.28640v1  

#### Abstract
Multimodal large language models (MLLMs) should generate consistent responses given semantically equivalent inputs across modalities. However, we observe a systematic discrepancy in model predictions under such cross-modal variations. Specifically, we define the modality gap as the difference in mod...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs
1. 论文的主要贡献和创新点
✅ 解决的问题
多模态大语言模型（MLLMs）在语义等价的跨模态输入下生成响应存在系统性差异，该差异被定义为模态 gap；现有方法中的prompt策略、仅缩放训练计算量无法可靠减少该模态 gap。
🚀 提出的新方法与思路
**TokenSwap**：该方法通过将文本概念替换为语义对齐的图像，构造视觉token与文本token交错的序列；基于TokenSwap，将现有基于文本的基准（如MMLU）转化为图像交错的对应基准，得到TokenSwap-Bench。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 基准量化能力 | 构建的TokenSwap-Bench可有效量化MLLMs的模态 gap |
| 模型优化效果 | 训练时融入TokenSwap可有效缓解模态 gap，同时保留纯文本和视觉语言性能 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| TokenSwap-Bench | 用于评估MLLMs的模态 gap |
| 现有基于文本的基准（如MMLU） | 经转化为图像交错基准后，用于评估MLLMs的模态 gap |
🎯 实验设置与评估指标
任务：评估MLLMs在语义等价的文本输入与图像交错输入下的性能差异，即模态 gap 的大小。
| 指标 | 含义（箭头标方向） |
|------|----------------------|
| 模态 gap | 表示模型在文本输入与语义等价图像交错输入下的性能差值，↓ 越小越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Prompt策略 | 常用优化方法 | 无法可靠减少模态 gap |
| 缩放训练计算量 | 模型优化方法 | 无法可靠减少模态 gap |
| TokenSwap-Bench | 新评估基准 | 用于量化MLLMs的模态 gap |
| TokenSwap训练方法 | 模型优化方法 | 可有效减少模态 gap，同时保留其他性能 |
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 主要发现：
1. MLLMs普遍存在模态 gap；
2. 推理模型的模态 gap 小于非推理模型；
3. 单独使用Prompt策略或仅缩放训练计算量无法可靠减少模态 gap；
4. 在训练中加入TokenSwap可有效缓解模态 gap，同时保留纯文本和视觉语言性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：论文提出TokenSwap方法构建了用于量化多模态大语言模型模态 gap的基准TokenSwap-Bench，且训练中应用TokenSwap可有效缓解该 gap 并保留原有性能。

</details>

---

### 6. [ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression](https://arxiv.org/abs/2607.29591v1)

**Authors**: Yuhang Zhan, Lisi Chen, Shuo Shang  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2607.29591v1  

#### Abstract
KV cache compression is essential for efficient long-context inference. Existing eviction methods permanently discard unselected tokens and consequently remove their aggregate contribution to attention. Merging-based alternatives preserve more information but can perturb retained keys and values tha...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression
1. 论文的主要贡献和创新点
✅ 解决的问题
现有KV缓存压缩方法存在两类缺陷：一是驱逐类压缩方法永久丢弃未选token，移除了其对注意力的聚合贡献；二是合并类压缩方法保留更多信息，但会扰动应保持精确的保留键值。

🚀 提出的新方法与思路
**ResKV**：将固定KV缓存预算划分为精确的主缓存和用于重构被省略token贡献的紧凑残差缓存，使主缓存token与残差项参与同一softmax归一化，让残差项恢复注意力的分子与分母质量而非作为事后修正项；设置构造时间的验证代理为每层每个KV头分配残差，解码时间的动态门调整单个查询的残差贡献。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 注意力贡献修复 | 恢复被省略token的注意力分子与分母质量，而非事后修正 |
| 缓存预算利用率 | 在相同保留KV预算下实现广泛性能提升 |
| 解码效率 | 保持压缩解码的实际效率，包含峰值内存使用与长上下文解码吞吐量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongBench | 长上下文推理KV缓存压缩的评估 |
| RULER | 长上下文推理KV缓存压缩的评估 |

🎯 实验设置与评估指标
任务为长上下文推理的KV缓存压缩，论文未报告具体评估指标的含义。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 驱逐类压缩基线方法 | KV缓存压缩方法 | 永久丢弃未选token，移除其对注意力的聚合贡献 |
| 合并类压缩基线方法 | KV缓存压缩方法 | 保留更多信息，但会扰动应保持精确的保留键值 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：ResKV在相同保留KV预算下取得广泛的长上下文推理性能提升，同时保持压缩解码的实际效率。

4. 关键结论和发现
- 主要发现：ResKV通过残差缓存重构被省略token的注意力贡献，在相同保留KV预算下，于LongBench和RULER的query-aware及query-agnostic设置中，取得优于现有基线方法的性能，同时保留压缩解码的实际效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ResKV是一种将固定KV缓存预算划分为精确主缓存与紧凑残差缓存、重构被省略token注意力贡献的KV缓存压缩方法，在相同预算下提升长上下文推理性能的同时保持压缩解码的实际效率。

</details>

---

### 7. [Learning Latent Reasoning Traces for Scalar Reward Models End-to-End](https://arxiv.org/abs/2607.29185v1)

**Authors**: Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, Kun Liang, Weijie Liu, Yunfang Wu  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.29185v1  

#### Abstract
Reward models (RMs) are central to aligning large language models with human preferences via reinforcement learning. Although traditional scalar RMs enable efficient and probabilistic reward modeling, they rely on superficial cues that fail to generalize to complex or out-of-distribution (OOD) tasks...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 《Learning Latent Reasoning Traces for Scalar Reward Models End-to-End》
1. 论文的主要贡献和创新点
✅ 解决的问题
现有不同范式的奖励模型存在核心缺陷：传统scalar reward models（RMs）依赖表面线索，无法泛化到复杂/OOD任务；generative RMs的自然语言评分缺乏scalar RMs的数值灵活性与概率可解释性；现有混合RMs采用off-policy多任务学习，无法保证生成的推理迹主动对齐下游标量奖励预测。

🚀 提出的新方法与思路
**LatentRM**：将中间推理迹学习为离散隐变量，通过端到端的隐式推理空间的on-policy优化，将深度基于推理的评估与精确的下游标量奖励预测紧密耦合。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理与奖励对齐 | 端到端on-policy优化使生成的推理迹主动对齐下游标量奖励预测 |
| 数值灵活性与概率可解释性 | 保留scalar RMs的相关特性 |
| 任务泛化能力 | 结合generative RMs的推理特性，适配复杂、OOD任务及从开放式对话到复杂推理的多任务场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体数据集名称 | 用于分布内与OOD任务的验证、RLHF验证，覆盖开放式对话到复杂推理的任务范围 |

🎯 实验设置与评估指标
实验任务为偏好建模与策略对齐，覆盖开放式对话到复杂推理任务范围。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未明确说明具体评估指标 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统scalar RMs | scalar reward model | 依赖表面线索，泛化性差，无法适配复杂/OOD任务 |
| generative RMs | generative reward model | 依赖推理提升鲁棒性，评分缺乏scalar RMs的数值灵活性与概率可解释性 |
| 现有混合RMs | hybrid reward model | 采用off-policy多任务学习，无法保证推理迹与下游奖励预测主动对齐 |
| LatentRM（本文） | proposed reward model | 端到端on-policy优化，将离散隐式推理迹与下游标量奖励预测紧密耦合，适配多任务场景 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 现有不同范式的奖励模型存在核心缺陷，LatentRM通过端到端on-policy优化与离散隐式推理迹设计，解决了推理迹与下游标量奖励预测的对齐问题。
2. LatentRM兼具generative RMs的推理鲁棒性与scalar RMs的数值灵活性、概率可解释性。
3. LatentRM在偏好建模与策略对齐任务中，整体性能优于传统scalar RMs、generative RMs及现有混合RMs。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：LatentRM是一种将离散隐式推理迹与端到端on-policy优化结合的奖励建模框架，解决了现有奖励模型推理与下游标量奖励预测的对齐问题，兼具泛化性与scalar RMs的核心特性，在偏好建模和策略对齐任务中表现更优。

</details>

---

### 8. [Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems](https://arxiv.org/abs/2607.29076v1)

**Authors**: Yuannuo Feng, Wenyong Zhou, Yuang Ma, Yizhe Chen, Wenshuai Yao, Yuxin Xie, Ngai Wong, Wang Kang  
**Category**: cs.AR  
**Published**: 2026-08-03  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.29076v1  

#### Abstract
Analog compute-in-memory (CIM) arrays have emerged as a promising substrate for energy-efficient LLM inference, particularly for weight-stationary computations in linear layers. However, extending analog CIM to attention mechanisms introduces a fundamental challenge: KV cache operations demand repea...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems

1. 论文的主要贡献和创新点
✅ 解决的问题
模拟计算内存（CIM）数组用于LLM推理时，线性层的权重 stationary 计算能效突出，但将其扩展到注意力机制存在核心挑战：KV缓存操作需重复原位权重更新，与权重 stationary 范式不匹配，导致动态计算面临严重硬件噪声问题，该问题此前未得到充分系统研究；同时发现初始和近期token对硬件噪声的脆弱性显著高于其他token。
🚀 提出的新方法与思路
**分层 token 保护策略**：将初始token和滑动近期token窗口置于高精度数字路径处理，其余大部分KV缓存数据在模拟CIM上处理，针对性保护易受噪声影响的token，降低模拟路径的计算开销。
**协同调度器**：结合模拟编程、所有权转换、批量矩阵向量乘法（bulk-MVM）的tile形成三种机制，控制数字路径的额外开销，平衡计算资源分配。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 平均困惑度（模拟噪声下） | 从基线水平33.91降至11.95，接近干净基线11.06 |
| 动态-KV编程行利用率 | 从23.1%提升至91.2% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | - |
🎯 实验设置与评估指标
任务：模拟CIM上9种LLM的噪声鲁棒推理；指标：平均困惑度（↓越低越好）、动态-KV编程行利用率（↑越高越好）
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | - | - |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表/图：论文摘要（无明确表号）**
| 指标 | 原水平 | 提出方法水平 | 最优值 |
| ---- | ---- | ---- | ---- |
| 平均困惑度（模拟噪声下） | 33.91 | 11.95 | - |
| 动态-KV编程行利用率 | 23.1% | 91.2% | ✅ |
💡 结论：论文提出的方法有效降低了模拟CIM中KV缓存操作引入的硬件噪声影响，大幅提升了动态-KV编程资源利用率，性能接近无噪声的干净基线。
其余实验情况：
- 主benchmark性能（如L2/碰撞率等）：论文未报告
- 效率对比（FPS/参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：仅报告了模拟噪声下的平均困惑度指标
- 消融实验：论文未报告

4. 关键结论和发现
- 初始和近期token对模拟CIM的硬件噪声脆弱性显著高于其余token，是噪声易感性的关键影响因素
- 分层token保护策略结合协同调度器的方案，可在高精度数字路径与模拟CIM间平衡计算开销，实现噪声鲁棒性与资源利用率的双重提升
- 该方法在9种LLM上的平均性能接近干净基线，验证了其针对模拟CIM注意力计算噪声问题的有效性
方法局限性：论文未报告
未来工作：论文未报告
> ✅ **总结一句话**：该论文首次系统研究模拟CIM中LLM动态注意力计算的硬件噪声问题，揭示初始和近期token的脆弱性，提出分层token保护策略与协同调度器，有效降低噪声下的困惑度并大幅提升动态-KV编程行利用率，性能接近干净基线。

</details>

---

### 9. [ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification](https://arxiv.org/abs/2607.28637v1)

**Authors**: Nitiz Khanal  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.28637v1  

#### Abstract
This paper presents our system for the CHiPSAL 2026 shared task on multimodal hate speech and sentiment detection in Nepali memes. We address both subtasks: binary hate speech classification and three-class sentiment analysis. Our approach adapts the Robust Adaptation of Hateful Meme Detection (RA-H...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification

1. 论文的主要贡献和创新点
✅ 解决的问题
需完成CHiPSAL 2026的尼泊尔语模因相关子任务：二元仇恨言论分类、三级情感分析；现有相关方法存在以下缺陷：1）多依赖单独的OCR和翻译管道，易引发错误传播；2）针对低资源南亚语言（如尼泊尔语）的视觉语言模型（VLM）适配方案不足；3）数据类别不平衡问题未得到有效缓解。

🚀 提出的新方法与思路
**Two-Stage VLM Adaptation with Contrastive Learning**：基于RA-HMD框架，选用原生支持天城文的Qwen3-VL-8B-Instruct；采用两阶段训练：第一阶段为LoRA微调搭配MLP投影头，实现生成式分类；第二阶段为对比骨干微调，采用监督InfoNCE损失。
**类别不平衡缓解模块**：针对尼泊尔语模因数据的类别不平衡问题，采用少数类过采样、图像增强、焦点损失三种策略。
**集成推理框架**：将Stage1的token概率与Stage2的分类器分数，用验证调优后的权重进行集成，避免分离OCR/翻译管道导致的错误传播，利用模型原生天城文理解能力。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
错误传播抑制 | 无需单独OCR及翻译管道，消除了该类管道带来的错误传播
低资源语言适配 | 采用原生支持天城文的VLM，适配低资源尼泊尔语模因分类任务

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为CHiPSAL 2026的两个子任务：尼泊尔语模因的二元仇恨言论分类、三级情感分析；评估指标为F1值（↑越高越好）。

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（CHiPSAL 2026子任务）**
| 任务 | F1值 | 排名 |
| --- | --- | --- |
| 仇恨言论检测 | 0.797 ✅ | 第2名 |
| 情感分析 | 0.518 | 第4名 |
💡 结论：本系统在CHiPSAL 2026仇恨言论检测子任务取得第2名，在情感分析子任务取得第4名。
其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等）：论文未报告

4. 关键结论和发现
- 主要发现：1）采用两阶段视觉语言适配结合对比学习的方案，适配低资源尼泊尔语模因分类任务有效；2）利用VLM原生天城文理解能力，可有效消除分离OCR和翻译管道带来的错误传播；3）针对类别不平衡的组合策略对任务有正向作用。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：本系统针对CHiPSAL 2026的尼泊尔语模因仇恨言论检测与情感分析任务，采用两阶段视觉语言适配结合对比学习、原生支持天城文的VLM及集成推理框架，分别取得第2和第4名的成绩，解决了低资源南亚语言模因分类中的错误传播问题。

</details>

---

### 10. [Sample Efficient Hierarchical Reinforcement Learning via Best Policy Identification](https://arxiv.org/abs/2607.29294v1)

**Authors**: Anders Jonsson, Emilie Kaufmann, Gianmarco Tedeschi, Lorenzo Steccanella  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.29294v1  

#### Abstract
We present HBPI-UCRL, a model-based algorithm for hierarchical reinforcement learning (HRL) that learns high-level and low-level policies in parallel. HBPI-UCRL exploits the fact that a high-level transition corresponds to a multi-step transition at the low level. We introduce two conditions on the ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Sample Efficient Hierarchical Reinforcement Learning via Best Policy Identification
1. 论文的主要贡献和创新点
✅ 解决的问题
现有非分层强化学习在稀疏奖励目标导向场景下样本效率较低，并行型分层强化学习（HRL）方法缺乏可学习性理论保证，导致其实际应用中理论支撑不足。
🚀 提出的新方法与思路
**HBPI-UCRL**：一种模型-based的分层强化学习算法，核心是并行学习高层与低层策略；该算法利用“高层转移对应低层多步转移”的特性，引入关于低层动态的两个条件，从而保证并行HRL的可学习性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 样本复杂度 | 在稀疏奖励目标导向设置下，样本复杂度上界严格低于其非分层对应方法，为HRL的经验成功提供理论依据 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
论文未报告具体实验任务与评估指标，如下表所示：
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何具体实验的定量结果，如下：
论文未报告

4. 关键结论和发现
- 主要发现
1. HBPI-UCRL通过并行学习高低层策略，结合低层动态的两个条件，实现了并行HRL的可学习性；
2. 在稀疏奖励目标导向设置下，HBPI-UCRL的样本复杂度优于非分层对应的强化学习算法；
3. 该算法的理论结果为HRL在实际应用中的经验成功提供了理论支撑。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：本文提出了模型-based分层强化学习算法HBPI-UCRL，通过并行学习高低层策略并引入低层动态的相关条件保证可学习性，其在稀疏奖励目标导向场景下的样本效率优于非分层对应方法，为分层强化学习的经验成功提供了理论依据。

</details>

---

### 11. [TokTier: Exact Stateful Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678v1)

**Authors**: Zhenyu Zhang, Zhichao Cao  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.29678v1  

#### Abstract
LLM serving systems cache prompt KV state, yet most front ends still re-tokenize the full request text on every call. The cost lands on coding agents, which resubmit a long transcript after each small tool result, and reuse is hard because even a short append can change token boundaries near the end...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TokTier: Exact Stateful Tokenization for Agentic LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM serving系统缓存了prompt KV状态，但前端在每次调用时仍需重新tokenize完整请求文本；该问题给coding agents带来高成本——每次获取小工具结果后需提交冗长转录文本，且即使短内容追加也会改变前序序列的token边界，导致状态难以复用；同时，传统tokenization方法、缓存基线方案等在agent场景下存在效率或精确性不足的缺陷。

🚀 提出的新方法与思路
**TokTier（精确有状态tokenization服务）**：核心约定为发射的token ID始终与请求文本的完整参考tokenization完全一致；针对会话续篇场景，围绕追加内容重新tokenize小窗口，经每个请求的稳定边界检查后拼接，若失败则加宽token窗口或回退至完整tokenization；针对无可复用前缀的调用场景，将GPT系列的正则预分词分解为本地运行规则，在GPU上执行精确预分词与BPE算法；引入采样影子验证器校验实时流量的tokenization结果，确保正确性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| token化精确性 | 覆盖17个tokenizer家族的全部验证样本中，token ID无分歧 |
| 增量token化效率 | 适配agent的小内容追加场景，提升token化速度 |
| 全序列token化效率 | 完整请求的token化速度优于传统CPU优化方法 |
| LLM serving性能 | 降低时间到第一个token（TTP），提升请求处理吞吐量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 来自两个agent生态的153951次调用 | 分析agent场景下的token化需求特征 |
| 12.4TB真实文本语料 | 验证tokenization的准确性与性能表现 |
| 93000+重放agent步骤 | 验证增量token化的正确性与效率 |
| 1.5×10^10个拆分检查样本 | 跨tokenizer家族的tokenization准确性验证 |
| 17个tokenizer家族 | 覆盖不同类型tokenizer的泛化性验证 |

🎯 实验设置与评估指标
任务为评估面向agentic LLM serving的精确有状态tokenization服务的准确性与性能，评估指标包括token ID分歧率（↓）、token化延迟（↓）、时间到第一个token（TTP，↓）、请求处理吞吐量（↑）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| HF tokenization | 传统CPU tokenization方法 | 无状态，处理完整请求文本 |
| Gigatoken | 基于缓存的基线方法 | 预温的现有最快缓存型tokenization方案 |
| 最快已发表CPU tokenization方法 | 优化型CPU tokenization方法 | 现有最优CPU token化方案 |
| 无状态前端 | 现有LLM serving前端方案 | 每次调用重新tokenize完整请求文本 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：未标注表号（场景：agentic LLM serving的tokenization性能与准确性）**
论文未报告所有定量结果对应的表号、图号、章节或页码，无法定位来源时不给出具体数值；论文通过对比实验发现，TokTier在token化精确性、增量效率、全序列效率及LLM serving性能上均优于现有基线方法。

💡 结论：TokTier在agentic LLM serving场景下实现了精确的token化，且性能显著优于现有方案。

4. 关键结论和发现
- 主要发现：1. TokTier在覆盖17个tokenizer家族的大规模验证中，实现了零token ID分歧的精确tokenization，完美适配agent场景；2. TokTier的增量token化方案适配agent每次小内容追加的特性，能大幅提升LLM serving的请求处理吞吐量并降低延迟；3. TokTier的GPU加速完整token化方案也优于现有最优CPU tokenization方法。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：TokTier是专为agentic LLM serving设计的精确有状态tokenization服务，解决了现有方案在agent场景下token化效率低、状态难复用的问题，在保持token化精确性的同时大幅提升了LLM serving性能。

</details>

---

### 12. [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](https://arxiv.org/abs/2607.28966v1)

**Authors**: Keshu Fu, Keqin Peng, Jun Bai, Shuhan Qin, Chen Li, Junzhu Liang, Yefei Chen, Jiaqi Li, Yuanxin Ouyang  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.28966v1  

#### Abstract
Large language models often improve task performance by generating long reasoning traces, but the resulting computation is frequently wasted on redundant verification and revision. Existing probe-based early-exit approaches mainly inspect explicit self-doubt expressions, leaving many earlier termina...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
- 大语言模型生成的长推理迹中存在冗余验证、修订环节，造成计算资源浪费；
- 现有基于探针的早退方法仅检测明确的自我怀疑表达，未覆盖更多早期终止的机会；
- 将早退范围扩展至普通推理边界虽提升了覆盖度，但中间状态多样性导致预测信息分布在不同隐藏层，现有方法依赖固定层选择或全层表示，计算成本高。

🚀 提出的新方法与思路
**Multi-granular Checkpoint Construction**：从句子、自我怀疑、段落边界构建多粒度的检查点。
**Robust Training Label Derivation**：通过重复答案补全的方式推导鲁棒的训练标签。
**Layer-Adaptive Probe Selection**：学习紧凑的信息探针层子集，而非采用固定层选择或全层表示的昂贵方案。
**Inference-Time Calibrated Confirmation Rules**：推理时结合校准后的预测与检查点特定的确认规则，平衡响应速度与过早退出的风险。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 早退覆盖度 | 扩展至普通推理边界，弥补了现有探针型早退方法仅检测明确自我怀疑表达的覆盖局限 |
| 计算效率 | 减少LLM推理中的冗余计算，缓解长推理迹带来的资源浪费 |
| 训练标签可靠性 | 基于重复补全生成鲁棒训练标签，提升模型训练的准确性 |
| 层自适应能力 | 自动选择紧凑的信息探针层子集，降低全层表示的高昂计算成本 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个基准 | 测试BLADE在多种任务上的性能表现 |
| Qwen3-8B、Qwen3-4B | 测试BLADE在两款Qwen3推理模型上的效果 |

🎯 实验设置与评估指标
任务：高效LLM推理任务，核心目标为在保持推理准确性的同时降低计算开销。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 生成token减少率 | ↑（数值越高，推理效率提升越显著） |
| 任务准确性 | ↑（数值越高，与基线性能越接近） |

⚔️ 基线方法对比
论文未报告具体基线方法的类型及特点，仅提及现有探针型早退方法、扩展推理边界的相关方法作为对比对象。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表号、图号等定位信息，相关定量结果无法准确定位，故所有实验结果均写为论文未报告。

4. 关键结论和发现
- 主要发现：1. BLADE框架可在保留接近基线准确性的前提下实现LLM推理效率的提升；2. 多粒度检查点和自动层选择模块对BLADE的性能具有正向作用。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：BLADE是一种边界扩展且层自适应的动态退出框架，能有效减少LLM推理的冗余计算，在保留推理准确性的同时提升推理效率。

</details>

---

### 13. [Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations](https://arxiv.org/abs/2607.28826v1)

**Authors**: Konur Tholl, Fran\c{c}ois Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.28826v1  

#### Abstract
Autonomous Cyber Operations (ACO) are increasingly important for defending enterprise networks as cyber threats continue to evolve in sophistication. ACO applications commonly employ Reinforcement Learning (RL) agents to learn defensive behaviors through interaction with environments. However, RL ag...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations
1. 论文的主要贡献和创新点
✅ 解决的问题
核心痛点：Reinforcement Learning（RL）代理在Autonomous Cyber Operations（ACO）场景中训练时需大量环境探索，导致行为不稳定，收敛前初始决策效果差，难以快速投入实际防御。
现有方法缺陷：基线RL代理存在上述训练阶段的不稳定性和初始决策差的问题；部分试图改进RL稳定性的教师引导策略，因奖励驱动RL优化与教师防御策略的策略对齐限制，无法持续超越优化后的教师策略。

🚀 提出的新方法与思路
**Prompt-Enhanced LLM Defense Policy**：采用prompt engineering而非fine-tuning技术，使用基于网络安全数据预训练的80亿参数大语言模型（LLM）生成ACO防御决策策略，在修改的CybORG CAGE Challenge 2环境中验证性能。
**Online Policy Distillation Framework**：设计在线策略蒸馏框架，将上述LLM生成的防御策略转移至仅含64910参数的轻量级RL代理，大幅降低模型体积（论文未报告具体减少量级的具体数值，仅提到several orders of magnitude），同时保留防御能力。
**Teacher-Guided RL Stability Strategy Validation**：评估教师引导的RL稳定策略，发现无任何该类策略能持续超越优化后的教师防御策略，明确存在策略对齐限制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 模型规模 | 轻量级RL代理仅64910参数，模型体积远小于原80亿参数LLM，适合部署 |
| 决策性能 | 经prompt engineering优化的LLM策略在修改的CybORG CAGE Challenge 2环境中优于基线RL代理 |
| 部署可行性 | 超轻量级代理可适配低资源部署场景，为ACO防御提供实用路径 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 修改的CybORG CAGE Challenge 2环境 | 构建不同规模（4-12主机）、不同网络配置的ACO场景，用于评估各类防御策略性能 |

🎯 实验设置与评估指标
任务：在4至12台主机、不同网络配置的CybORG场景中，评估所提LLM驱动的防御策略、轻量级RL代理及教师引导RL稳定策略的性能。
指标 | 含义（箭头方向）
论文未报告具体评估指标的定义及对应衡量方向。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 基线RL代理 | RL代理 | ACO领域常用的常规基线代理，训练阶段需大量探索，存在行为不稳定、初始决策效果差的问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告包含具体表号、图号的详细定量性能数值，仅通过摘要提及以下结果：
- **防御策略性能对比（无对应表号）**
| 策略类型 | 性能表现 |
| ---- | ---- |
| Prompt-Enhanced LLM策略 | 优于基线RL代理 |
| Online Policy Distillation生成的轻量级RL代理 | 保持有效防御能力 |
- **跨场景策略表现（无对应表号）**
| 主机规模 | 网络配置 | 策略表现 |
| ---- | ---- | ---- |
| 4-12台 | 不同配置 | 无教师引导RL稳定策略持续超越优化的教师策略 |
- **模型参数对比（无对应表号）**
| 模型类型 | 参数规模 |
| ---- | ---- |
| 原80亿参数LLM | 80亿 |
| 轻量级RL代理 | 64910 |
💡 结论：所提框架可将高性能LLM防御策略压缩为超轻量级RL代理，且教师引导的RL稳定策略存在策略对齐限制。

4. 关键结论和发现
- 核心发现1：基于网络安全数据预训练的LLM，通过prompt engineering即可在ACO防御决策上超越基线RL代理，是可靠的防御知识来源。
- 核心发现2：提出的Online Policy Distillation框架可将LLM的防御策略高效转移至轻量级RL代理，大幅降低模型体积的同时保留防御效果，为部署提供可行方案。
- 核心发现3：奖励驱动的RL优化与教师引导的防御策略间存在策略对齐限制，导致教师引导的RL稳定策略无法持续超越优化的教师策略。

方法局限性：论文未报告具体的评估指标定义、各类策略的具体性能数值（如防御成功率、收敛速度等）；未报告跨域/zero-shot迁移性能、鲁棒性/扰动测试结果及消融实验的详细结论。

未来工作：优化奖励驱动RL与教师防御策略间的对齐机制；提升轻量级RL代理的性能；补充跨场景、鲁棒性等维度的评估。

> ✅ **总结一句话**：该研究通过prompt engineering优化网络安全LLM的ACO防御策略，并经在线策略蒸馏构建超轻量级RL代理，为高性能防御模型的低资源部署提供了实用路径。

</details>

---

### 14. [Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models](https://arxiv.org/abs/2607.28979v1)

**Authors**: Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Soyoung Park, Gwangseon Jang, Sungsu Lim  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2607.28979v1  

#### Abstract
Heterogeneous Large Language Model (LLM) systems increasingly rely on shared contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
异构LLM系统依赖共享上下文、检索证据及多智能体对话历史，但各LLM的KV缓存为模型特有，无法跨架构复用，导致每个模型需重复prefill或存储相同上下文的缓存，限制了多模型推理与长上下文生成的可扩展性；现有跨架构KV缓存翻译方法依赖单一投影路径或全局共享潜在空间，无法适配多样化的源-目标模型映射，存在翻译偏差问题。

🚀 提出的新方法与思路
**Mixture-of-Translators (MoT)**：采用多个translator模块捕捉不同源LLM与目标LLM间的多样化映射，替代单一投影路径或全局共享潜在空间，减少翻译偏差。
**Context Correction Loss**：引入该损失函数，对齐重放的目标LLM轨迹与原生目标轨迹，进一步降低残留翻译误差。
缓存翻译存在两类竞争失败模式：早期注入导致的传播翻译偏移、晚期注入导致的末态偏移，MoT通过混合translator模块与目标侧校正机制解决上述两类问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV缓存跨架构适配 | 支持同构与异构LLM间的KV缓存复用，突破模型特异性限制 |
| 翻译误差控制 | 结合混合translator与Context Correction Loss，解决传播偏移与末态偏移问题，降低残留误差 |
| 多场景应用 | 可支撑多智能体推理、长上下文缓存增强生成，实现质量保留的缓存复用 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 用于验证KV缓存翻译及下游任务性能的数据集 |

🎯 实验设置与评估指标
任务：评估MoT在同构及异构LLM间完成KV缓存翻译后的下游任务性能。
| 指标 | 含义 |
| --- | --- |
| 下游QA准确率 | 越高越好 |
| 抽取式QA F1 | 越高越好 |
| 长上下文生成质量保留率 | 越高越好 |
| 多智能体推理质量保留率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 现有KV缓存翻译方法 | 依赖单一投影路径或全局共享潜在空间，无公开具体特性描述 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（场景：同构与异构LLM间KV缓存翻译）**
| 指标 | 结果 |
| --- | --- |
| 下游QA性能 | MoT可保留下游QA性能（论文未报告具体数值及对应表号） |
| 长上下文生成质量保留率 | MoT实现了较高比例的直接上下文质量保留（论文未报告具体数值及对应表号） |
| 多智能体推理质量 | MoT支持多智能体推理的质量保留（论文未报告具体数值及对应表号） |
💡 结论：MoT可在同构及异构LLM间翻译KV缓存，实现下游任务及多场景应用的质量保留。

以下实验论文未报告：效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验。

4. 关键结论和发现
- 主要发现：1. 异构LLM间的KV缓存复用是提升多模型推理与长上下文生成可扩展性的核心痛点；2. MoT通过混合translator模块与目标侧校正机制，解决了缓存翻译的传播偏移与末态偏移两类问题，实现跨模型缓存的质量保留；3. 现有依赖单一投影路径或全局共享潜在空间的缓存翻译方法存在固有缺陷，无法适配多样化模型映射需求。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出Mixture-of-Translators框架，突破异构LLM间KV缓存的模型特异性限制，通过混合translator模块与Context Correction Loss实现缓存翻译的质量保留，支撑多模型推理与长上下文生成的可扩展应用。

</details>

---

### 15. [Are the Financial Reasoning from LLMs Credible? A Real World Test over Long-Horizon Statements](https://arxiv.org/abs/2607.28661v1)

**Authors**: Xinke Tong, Xuanming Zhang, Tianyi Tang, An Yang, Jiatu Hu, Guojie Lin, Zhenzhen Shi, Lingfeng Zeng, Boyu Yang, Bing Zhao, Hu Wei, Lin Qu, Dayiheng Liu  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.28661v1  

#### Abstract
Do Large Language Models (LLMs) possess genuine structural reasoning, or merely rely on surface-level pattern matching? The financial domain, demanding numerical precision and multi-step logic over long contexts, is an ideal testbed. Existing benchmarks fail to capture real-world industrial complexi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Are the Financial Reasoning from LLMs Credible? A Real World Test over Long-Horizon Statements
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于测试LLMs财务推理能力的基准存在缺陷，多依赖多项选择题或裁剪表格上的单跳问答，未捕捉真实工业环境中复杂的跨报表动态、时间反累计等情况，无法有效区分LLMs是具备真正的结构化推理能力还是仅依赖表面模式匹配。
🚀 提出的新方法与思路
**FinIndices**：通过自动化合成管道结合对抗陷阱，构建了评估未裁剪财务报表（最多32K tokens）数据处理保真度的大规模基准，包含Single-Index计算和Table-Index制表两类任务，用于测试LLMs的复杂领域推理、时间推理和精准度推理能力。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 测试场景 | 针对真实工业级复杂财务场景，覆盖未裁剪财务报表、跨报表动态、时间反累计等现有基准缺失的要素 |
| 测试任务 | 包含Single-Index计算和Table-Index制表两类任务，全面评估不同类型的财务推理能力 |
| 评估难度 | 引入对抗陷阱，增强评估难度，更有效识别LLMs的表面模式匹配依赖问题 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| FinIndices | 评估LLMs在财务推理任务中的结构推理能力，替代现有存在场景缺陷的评估基准 |
🎯 实验设置与评估指标
任务为测试LLMs在包含时间累计/反累计等复杂逻辑的财务报表上的推理性能；评估指标为推理性能得分（越高越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Gemini-3.1-Pro | 商用LLM | 用于测试LLMs财务推理的脆弱性 |
| Supervised Fine-Tuning（SFT） | 对齐方法 | 用于验证结构化逻辑的可恢复性 |
| 现有多选择/单跳QA基准 | 评估基准 | 存在场景局限性，无法捕捉真实财务复杂性 |
3. 主要实验结果和性能指标
📊 定量结果汇总
- 主 benchmark 性能：论文未报告
- 效率对比：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
💡 结论：论文揭示了LLMs在财务推理中的两大严重脆弱性：一是Knowledge Bottleneck，虽在预训练中记忆了公式，但依赖脆弱的模式匹配，移除明确公式提示会导致性能大幅下降，暴露出时间反累计和账户流类型不匹配的缺陷；二是Structural Bottleneck，多指标多周期表生成的高强度认知负荷会消耗推理能力，使LLMs从孤立推导退化为浅层启发式，如取错相邻列、用字面算术替代深层会计调整。Supervised Fine-Tuning（SFT）可大幅提升无提示情况下的财务推理性能，验证了结构化逻辑可通过数据中心对齐部分恢复。
4. 关键结论和发现
- 主要发现：① LLMs在财务推理中存在Knowledge Bottleneck，仅记忆公式的表面模式匹配，缺失对时间累计等深层逻辑的掌握；② 多指标多周期表生成的认知压力会导致LLMs推理能力退化，依赖浅层启发式；③ Supervised Fine-Tuning（SFT）可部分修复LLMs的财务结构化推理能力。
- 方法局限性：论文未报告明确的方法局限性。
- 未来工作：论文未提及具体未来工作方向。
> ✅ **总结一句话**：本论文构建了贴合真实工业场景的财务推理基准FinIndices，揭示了LLMs财务推理的两大结构性缺陷，验证了SFT可部分恢复其财务结构化逻辑，为评估LLMs的可信财务推理提供了重要基准与洞见。

</details>

---

### 16. [TAPR: Enhancing LLM Performance with a Task-Aware Prompt Rewriter](https://arxiv.org/abs/2607.28657v1)

**Authors**: Oliver Savolainen, Emanuele Bastianelli, Hosein Azarbonyad  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.28657v1  

#### Abstract
Large Language Models (LLMs) often require carefully crafted prompts to unlock their full potential, which can be a barrier for non-expert users. This work addresses the challenge by introducing a Task-Aware Prompt Rewriter (TAPR), a model that reformulates user prompts into task-optimized prompts w...

---

### 17. [MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents](https://arxiv.org/abs/2607.29002v1)

**Authors**: Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.29002v1  

#### Abstract
Online shoppers increasingly turn to AI shopping assistants, using images and multi-turn dialogue to express and refine product needs that are difficult to articulate in text alone. However, existing benchmarks largely rely on text-only or synthetic requests, underrepresenting complex real-world sho...

---

### 18. [Beyond Retrieval: Analytic Memory for Multimodal Agents](https://arxiv.org/abs/2607.29440v1)

**Authors**: Zhoujin Tian, Yao Tian, Hao Zhang, Cheng Chen, Yakun Li, Lei Zhang, Xiaofang Zhou  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.29440v1  

#### Abstract
Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions. Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant ...

---

### 19. [Fragility of Value under Imperfect Alignment](https://arxiv.org/abs/2607.28881v1)

**Authors**: Winter Cross  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.28881v1  

#### Abstract
As more responsibility is placed upon AI systems, it becomes increasingly important to guarantee that these systems are aligned with humanity. A common fear in AI safety is that human value is fragile -- that is, optimizing too heavily for an imperfect proxy to human values will lead to a catastroph...

---

### 20. [Sycophancy Undermines Epistemic Vigilance in Cooperative Vision-Language Tasks](https://arxiv.org/abs/2607.29585v1)

**Authors**: Rupak Sarkar, Neha Srikanth, Saloni Gupta, Claire Bonial, Philip Resnik, Rachel Rudinger  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.29585v1  

#### Abstract
To maintain common ground in cooperative conversation, humans iteratively update their beliefs as conversation participants share new information; participants who are epistemically vigilant detect when new information conflicts with prior beliefs and take steps to repair these conflicts. In order f...

---

### 21. [Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL](https://arxiv.org/abs/2607.29246v1)

**Authors**: Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 25.5  
**Type**: new  
**ArXiv ID**: 2607.29246v1  

#### Abstract
Modern large language models (LLMs) are expected not just to answer correctly, but to adapt their behavior to different human values and use cases. As a result, multi-reward reinforcement learning (RL) has become an increasingly important problem for LLMs, where each reward captures a different aspe...

---

### 22. [OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference](https://arxiv.org/abs/2607.29398v1)

**Authors**: Zhikang Xie, Xichen Ye, Yifan Wu, Haoshen Yu, Li chenan, Peizhu Gong, Weizhong Zhang, Cheng Jin  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.29398v1  

#### Abstract
Diffusion models have revolutionized generative tasks but incur high latency due to iterative denoising. While cache-based strategies accelerate inference by reusing intermediate features, they largely rely on static, sample-agnostic schedules. We argue that this rigidity overlooks two facts empiric...

---

### 23. [Learning Stateful Predictive Knowledge From Experience](https://arxiv.org/abs/2607.28638v1)

**Authors**: Yan Song, Xidong Feng, Bo Liu, Xinyu Cui, Haotian Fu, Zichen Liu, Mengyue Yang, Cheng Deng, Jian Zhao, Jun Wang  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.28638v1  

#### Abstract
As large language model (LLM) agents increasingly learn from experience, they primarily rely on trajectory-level reflection to extract insights. Viewed through the lens of predictive knowledge, we argue that this approach operates on episodic hindsight rather than predictive foresight, yielding brit...

---

### 24. [Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning](https://arxiv.org/abs/2607.29211v1)

**Authors**: Xinyan Guan, Jiali Zeng, Chunlei Xin, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Fandong Meng  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.29211v1  

#### Abstract
Large language models generate computationally expensive yet semantically void reasoning on beyond-capability tasks, creating risks where plausible-sounding but incorrect derivations mislead users. We characterize this \textit{futile reasoning} phenomenon through systematic analysis, revealing unive...

---

### 25. [Evidence-Type Competition: When Can Interventional Data Teach Language Models Causal Direction?](https://arxiv.org/abs/2607.29484v1)

**Authors**: Xining Xun  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2607.29484v1  

#### Abstract
Interventional data is widely regarded as the gold standard for teaching models causal reasoning. We test this assumption in a fully controlled synthetic environment pitting observational correlation against causal effect, and find it fails instructively. In Simpson's-paradox worlds, where the two h...

---

### 26. [MMFGU: Multimodal Federated Graph Unlearning](https://arxiv.org/abs/2607.28708v1)

**Authors**: Haodong Lu, Zekai Chen, Weiwei Ji, Shihao Li, Xunkai Li, Xun Wu, Yinlin Zhu, Rong-Hua Li  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.28708v1  

#### Abstract
Multimodal federated graph learning enables clients to collaboratively train graph models over structural, textual, and visual signals without sharing private local data. However, the presence of heterogeneous multimodal content also makes unlearning requests more frequent and fine-grained: users ma...

---

### 27. [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678v1)

**Authors**: Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu  
**Category**: cs.AI  
**Published**: 2026-08-03  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.28678v1  

#### Abstract
Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wis...

---

### 28. [Flow Matching with Missing Data](https://arxiv.org/abs/2607.28698v1)

**Authors**: Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.28698v1  

#### Abstract
Flow matching assumes fully observed training data, which many real-world applications rarely provide. We propose Missing-Data Flow Matching, which treats the missing coordinates of training samples as latent variables and averages the flow matching loss over the values they could take. We first pro...

---

### 29. [Learning Optimal Dynamic Matching via Graph Neural Networks](https://arxiv.org/abs/2607.28925v1)

**Authors**: Genta Okada, Shunya Noda, Junpei Komiyama, Akira Matsushita  
**Category**: cs.LG  
**Published**: 2026-08-03  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.28925v1  

#### Abstract
Dynamic matching markets require decisions about whom to match and when: matching now yields value but removes participants who may create better future opportunities. We develop a value-based reinforcement-learning framework for this problem on finite, evolving weighted graphs. We study an infinite...

---

### 30. [Studying quantization trade-offs for efficient inference deployment in machine translation](https://arxiv.org/abs/2607.29397v1)

**Authors**: Jim Zhao, Sohir Maskey, Koen Oostermeijer, Douglas Orr, Teryn Jones  
**Category**: cs.CL  
**Published**: 2026-08-03  
**Score**: 16.5  
**Type**: new  
**ArXiv ID**: 2607.29397v1  

#### Abstract
Deploying large language models in realistic server environments poses challenges, as the system needs to provide high-quality responses with low latency. Quantization is a common approach to reduce the memory footprint and improve inference efficiency, yet its impact on latency and throughput is ra...

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
