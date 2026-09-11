# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-11 10:07:25 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Composable CXL Memory as a Kubernetes-Native Shared Memory for LLM Serving](https://arxiv.org/abs/2609.10790v1)

**Authors**: Hongjian Fan, Kevin Zhang, David Habinsky, Sean Dykstra  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 98.0  
**Type**: new  
**ArXiv ID**: 2609.10790v1  

#### Abstract
We present a Kubernetes Dynamic Resource Allocation (DRA) driver that makes composable CXL memory a schedulable cluster resource, and evaluate the resulting shared-memory tier for cross-node KV-cache reuse in LLM serving. The driver composes CXL regions on demand, materializes them as DAX devices on...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：面向LLM服务的Kubernetes原生可组合CXL共享内存

1. 论文的主要贡献和创新点
✅ 解决的问题
LLM serving中跨节点KV缓存复用需求难以满足，现有节点本地缓存（GPU前缀缓存、CPU-DRAM offload）无法实现跨节点复用，导致跨节点场景下需回退全量重计算，且缺乏将可组合CXL内存转化为Kubernetes原生可调度资源的方案。

🚀 提出的新方法与思路
**Kubernetes DRA驱动（Dynamic Resource Allocation Driver）**：该驱动将可组合CXL内存转化为可调度的集群资源，按需组合CXL区域，在各参与主机上以DAX设备形式实现，并通过单一Container Device Interface（CDI）名称注入Pod，使不同节点的Pod可访问同一物理CXL区域。
**vLLM/llm-d共享内存连接器**：该连接器将上述共享CXL区域作为KV缓存层，在共享介质内嵌入槽目录，消除对外部元数据服务的依赖。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 资源调度 | 实现CXL内存作为Kubernetes原生可调度资源，适配容器化集群部署 |
| KV缓存复用 | 支持跨节点KV缓存共享，无需外部元数据服务 |
| 延迟开销 | 跨节点复用延迟与同节点复用延迟差距仅为1-4%，性能损失小 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
本次实验在包含2个节点、512GiB CXL appliance的集群上，以Qwen2.5-7B-Instruct为模型，评估跨节点KV缓存复用对LLM serving性能的影响；评估指标包括首包时间（TTFT，↓越低越好）、外部命中率（外部hit rate，↑越高越好）、共享差距（跨节点复用与同节点复用的延迟比，↓越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GPU前缀缓存 | 节点本地缓存 | 仅支持同节点KV缓存复用，跨节点时回退全量重计算 |
| CPU-DRAM offload | 节点本地缓存 | 仅支持同节点KV缓存复用，跨节点时回退全量重计算 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未提供实验结果对应的表号、图号或具体章节，仅在摘要中描述以下结果：
- 跨节点前缀复用场景下，TTFT降低5.5×--36.6×，外部命中率达95.4--99.5%，共享差距为1--4%；
- 该方法为内存解聚方案，而非预填（prefill）/解码（decode）解聚方案；
- 本次研究为可行性研究，而非性能评估。

💡 结论：将可组合CXL内存转化为Kubernetes原生可调度资源的方案可实现跨节点LLM KV缓存共享，在实验中验证了其降低TTFT、减少跨节点复用延迟的可行性。

4. 关键结论和发现
- 核心发现：在双节点集群上，基于Kubernetes DRA驱动的可组合CXL共享内存方案，结合vLLM/llm-d共享内存连接器，可实现跨节点LLM KV缓存复用，使TTFT显著降低，且跨节点复用延迟仅比同节点高1-4%，外部命中率高；
- 方法局限性：本次研究仅为可行性研究，未进行全面性能评估；
- 未来工作：论文未报告。

> ✅ **总结一句话**：论文提出将可组合CXL内存转化为Kubernetes原生可调度资源的方案，实现跨节点LLM KV缓存共享，验证了其在降低LLM首包时间、减少跨节点复用延迟上的可行性。

</details>

---

### 2. [Taming Bitwise Behavior in GPU Kernels with Tensor Core: Black-Box Reconstruction, Compiler Enforcement, and Static Verification](https://arxiv.org/abs/2609.11356v1)

**Authors**: Ziteng Yang, Nicholas J. Riasanovsky, Warren Deng, Vivek Sarkar  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 77.0  
**Type**: new  
**ArXiv ID**: 2609.11356v1  

#### Abstract
Determinism and numerical reproducibility are increasingly required of GPU kernels in machine learning systems, yet deterministic implementations of the same kernel can still differ bit for bit. Floating-point reduction order is the primary cause, alongside partial-sum precision, fused multiply-add ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Taming Bitwise Behavior in GPU Kernels with Tensor Core: Black-Box Reconstruction, Compiler Enforcement, and Static Verification
1. 论文的主要贡献和创新点
✅ 解决的问题
机器学习系统需要GPU内核的确定性与数值可复现性，但同一内核的确定性实现仍存在逐位差异；差异成因包括浮点归约顺序、部分和精度、融合乘加（FMA）操作、舍入位置；算术选择可能由手动编码、Triton等块级语言选定，或cuBLAS/rocBLAS等闭源码库隐藏；tile形状会影响算术实现可能破坏batch不变性；保留固定运算顺序最多需20%的性能成本，传统自动调参器无法识别逐位等价的配置，导致调参效率低且可能遗漏高性能有效配置。

🚀 提出的新方法与思路
**闭源码库算术黑盒重构**：提出GEMM归约顺序描述符，包含split-K GEMM中K的划分方式；完成首次闭源码库算术实现的黑盒重构，实现位级正确性匹配。
**编译期平衡树归约与数据布局优化**：在Triton lowering阶段强制应用平衡树归约规则，引入数据布局优化，在保证位级确定性的前提下优化内核性能。
**跨ISA逐位等价静态检查**：开发针对编译后GPU内核的可靠静态检查器，是首个支持NVIDIA PTX与AMD GCN的跨ISA位级等价检查工具；将其集成至Triton自动调参器，将调参搜索范围限制在单一逐位等价类内。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 闭源码库分析 | 首次实现闭源码库算术的黑盒位级正确性重构，匹配NVIDIA cuBLAS测试集 |
| 跨ISA验证 | 首个支持NVIDIA PTX与AMD GCN的跨架构逐位等价静态检查器 |
| 调参优化 | 集成后自动缩小Triton调参搜索空间，仅保留逐位等价的有效配置 |
| 性能与确定性平衡 | 多数内核在保证位级确定性的同时，性能接近自由顺序实现 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告具体公开数据集 | 用于验证Triton GEMM在Blackwell、Hopper平台及带融合前序操作的实际LLM形状下的性能与位级正确性 |

🎯 实验设置与评估指标
针对GEMM和归约类GPU内核，验证位级等价性与内核性能，核心评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 位级匹配度 | 目标内核与对比内核的逐位匹配比例（→ 越高越好） |
| 内核性能 | 与cuBLAS、torch.compile等基线方法的性能对比（→ 越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| cuBLAS | 闭源码GPU GEMM库 | NVIDIA提供的高度优化闭源GEMM实现，算术细节隐藏 |
| torch.compile | PyTorch优化编译器 | PyTorch官方优化工具，动态编译用户代码生成GPU内核 |
| 传统自动调参器 | 通用调参工具 | 无法识别内核配置间的逐位等价关系，调参效率低 |
| 原生Triton | GPU内核语言 | 用于编写自定义GPU内核，支持块级运算定义 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**内核性能与等价性验证结果**
| 场景 | 结果 |
| --- | --- |
| 闭源码库匹配性 | 基于该方法的Triton GEMM在Blackwell和Hopper平台的所有测试用例中，与NVIDIA cuBLAS逐位匹配 |
| LLM场景性能 | 针对带融合前序操作的实际LLM形状，性能与torch.compile匹配或更优 |
| 性能优化效果 | 在GB300和H100平台上，27个被测内核中的19个通过优化后，性能达到自由顺序实现的10%以内 |

💡 结论：通过黑盒重构、编译期优化与跨ISA静态检查技术，实现了GPU内核位级确定性与高性能的兼顾，多数内核在保证位级等价的同时性能接近自由顺序实现，同时缩小了自动调参的搜索空间。

4. 关键结论和发现
- 主要发现：1. GPU内核算术的位级行为受归约顺序、部分和精度、融合乘加操作、舍入位置等多因素影响，闭源码库的算术细节可通过黑盒重构实现位级匹配；2. 平衡树归约与数据布局优化可在保持位级确定性的前提下，将多数内核性能提升至接近自由顺序的水平；3. 跨ISA静态逐位等价检查可有效缩小自动调参的搜索空间，减少无效配置的搜索。
- 方法局限性：论文未报告该方法在其他GPU ISA、更大规模GPU内核或非GEMM/归约类内核上的泛化能力，也未提及位级确定性实现相对于自由顺序实现的具体性能损失量化值（仅说明最大成本为20%）。
- 未来工作：扩展跨ISA静态检查器的覆盖范围至更多GPU架构与内核类型；进一步优化位级确定性GPU内核的性能，减少与自由顺序实现的差距；将该技术集成至更多GPU内核开发与调参流程，增强数值可复现性。

> ✅ **总结一句话**：本文提出黑盒重构、编译期强制优化与跨ISA静态检查三类技术，解决了GPU内核位级确定性与高性能难以兼顾的痛点，实现了闭源码库的位级匹配，优化后多数内核性能接近自由水平并缩小了自动调参的搜索范围。

</details>

---

### 3. [PATTON: Enabling Commodity PIM for Production LLM Serving](https://arxiv.org/abs/2609.11392v1)

**Authors**: Hangyeol Kim, Sanghyun Lee, Teokkyu Suh, Joo-Young Kim  
**Category**: cs.AR  
**Published**: 2026-09-11  
**Score**: 76.5  
**Type**: new  
**ArXiv ID**: 2609.11392v1  

#### Abstract
Processing-in-Memory (PIM) is promising for accelerating memory-bound decode attention, but attention acceleration alone is insufficient for production LLM serving, where engines dynamically allocate, populate, share, cache, and reclaim logical KV cache blocks. Supporting this lifecycle on commodity...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PATTON: Enabling Commodity PIM for Production LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
PIM虽可加速内存绑定的解码注意力，但仅靠注意力加速不足以满足生产级LLM serving的需求，因生产LLM引擎需动态处理KV缓存块的分配、填充、共享、缓存、回收全生命周期；在commodity PIM上支持该生命周期需解决物理内存分配、块-地址映射、命令生成的问题。针对Value cache，存在GEMV效率、单token写效率、内存容量三者的核心矛盾：GEMV优化布局将新生成的Value向量分散到各行导致写入成本高；更细粒度的内存共享提升容量利用率但会造成GEMV归约碎片化。

🚀 提出的新方法与思路
**Hierarchical Granule Allocation**：将块大小的Key和Value颗粒与逻辑token块一一映射，固定其物理位置与命令；同时采用更粗的颗粒分组块，以实现高效的GEMV执行与内存利用。
**Commit Zone**：分阶段存储部分Value块，以实现高效的单token写入，之后再将这些块提交到GEMV优化的位置。
PATTON会跟踪这些存储位置，以此生成KV缓存写入以及QK-transpose/SV命令。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 加速性能 | 在attention执行及runtime诱导的prefill重计算场景下实现加速 |
| 能量效率 | 在attention执行及runtime诱导的prefill重计算场景下实现能量效率提升 |
| 硬件兼容性 | 无需修改PIM处理单元 |
| KV缓存命中率 | 与vLLM的原生GPU KV缓存相当 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为生产级LLM serving相关性能评估
| 指标 | 含义 |
| --- | --- |
| 加速倍数 | 越高越好 |
| 能量效率倍数 | 越高越好 |
| KV缓存命中率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 评估的baselines | 对比方法 | 未明确具体类型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
其他实验：
1. 主benchmark性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 提出的PATTON通过层级颗粒分配和Commit Zone设计，解决了Value cache的GEMV效率、单token写效率与内存容量之间的核心冲突，可将生产级LLM引擎与commodity PIM集成。
- PATTON无需修改PIM处理单元，即可实现LLM serving的性能和能量效率提升，同时保持与vLLM原生GPU相当的KV缓存命中率。
- PATTON在attention执行及runtime诱导的prefill重计算场景下获得了性能与能效的提升结果。
方法局限性：论文未报告
未来工作：论文未报告
> ✅ **总结一句话**：PATTON是一种用于将生产级LLM引擎与commodity PIM集成的运行时方案，通过层级颗粒分配和Commit Zone设计，无需修改PIM处理单元即可在指定LLM serving场景下提升性能与能量效率，且保持与vLLM原生GPU相当的KV缓存命中率。

</details>

---

### 4. [Structural Process Supervision for Latent Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.09928v1)

**Authors**: Yiqi Li, Xu Chen, Chen Ju, Jiangchao Yao, Zhaoyang Li, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Yu Wang  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 71.0  
**Type**: new  
**ArXiv ID**: 2609.09928v1  

#### Abstract
Latent reasoning approaches enhance token-level efficiency and robustness by replacing verbose, explicit chain-of-thought (CoT) tokens with compact continuous-space embeddings. However, existing methods lack direct process supervision over these latent embeddings, which often leads to representation...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Structural Process Supervision for Latent Chain-of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有潜在推理方法通过紧凑连续空间嵌入替代冗长显式链-of-thought（CoT）token，提升了token级效率与鲁棒性，但此类方法缺乏对潜在嵌入的直接过程监督，常引发表示崩溃与信息分布不均。

🚀 提出的新方法与思路
**Prototype-Mediated Process Supervision (PMPS)**：引入可学习推理原型作为语义锚点，为潜在推理提供结构过程级监督；将潜在嵌入与显式CoT嵌入投影至共享原型空间，通过原型分配实现不等长表示间的多对多软对齐。
**Progressive Sequential Alignment (PSA)**：进一步引导训练过程，初始阶段利用位置先验鼓励序列对齐结构，随后逐渐放松约束以允许自适应匹配。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 输出效率 | 在指定测试数据集上将输出token长度压缩至显式CoT的一半以下 |
| 推理准确率 | 相比领先的潜在推理基线SIM-CoT，在不同模型家族上取得平均准确率提升 |
| 多场景适配 | 在GPT-2模型上超越显式CoT微调基线CoT-SFT；在更大模型与更具挑战性的任务中，于输出长度相当的同类潜在推理方法里准确率最高 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GSM8K-Aug | 测试输出token压缩效果与基础推理准确率 |
| 更大模型与更具挑战性任务 | 测试方法在复杂场景下的泛化性能 |

🎯 实验设置与评估指标
实验任务为潜在链-of-thought相关推理任务，以推理的输出效率（token长度）和准确性（准确率）为核心评估维度。
| 指标 | 含义 |
| ---- | ---- |
| 输出token长度 | ↓ 越小越好，反映推理输出的压缩效率 |
| 推理准确率 | ↑ 越高越好，反映推理结果的正确性 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| SIM-CoT | 潜在推理基线方法 | 领先的同类潜在推理基线 |
| CoT-SFT | 显式推理基线方法 | 显式链-of-thought微调基线 |
| 其他潜在推理方法 | 潜在推理基线方法 | 同类潜在推理对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号的定量实验表格，仅在摘要中披露PMPS的相关性能表现，具体为：在指定数据集上实现输出token压缩，在不同模型上的准确率表现优于多个基线方法。
💡 结论：提出的PMPS与PSA模块在潜在链-of-thought推理中，兼顾了输出压缩效率与推理准确性，性能优于多数同类方法。

4. 关键结论和发现
- 主要发现：
  1. 针对潜在推理缺乏过程监督引发的表示崩溃与信息分布不均问题，结合PMPS与PSA模块的方法可有效解决该痛点。
  2. 该方法在提升潜在推理效率（压缩输出token长度）的同时，实现了推理准确性的提升，在多个模型及场景下均优于相关基线方法。
  3. 方法在更大模型与复杂任务场景下表现稳定，输出长度相当的前提下，准确率优于其他同类潜在推理方法。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：本文提出的Prototype-Mediated Process Supervision（PMPS）与Progressive Sequential Alignment（PSA）模块，解决了潜在链-of-thought推理中过程监督缺失导致的问题，在提升推理效率与准确性上取得了良好效果。

</details>

---

### 5. [Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning](https://arxiv.org/abs/2609.10177v1)

**Authors**: Mingbo Yang, Wenqiang Wang, Zhaolu Kang, Peng Chen, Yannan Chen, Sunshang Wang, Yan Xiao  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2609.10177v1  

#### Abstract
In-context learning (ICL) is widely used in multimodal large language models (MLLMs) and achieves strong performance across a wide range of multimodal tasks. However, existing multimodal ICL methods often rely on surface level imitation of in-context demonstrations, making it difficult for MLLMs to ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态In-Context Learning（ICL）方法依赖演示的表面层面模仿，难以使多模态大语言模型（MLLMs）将其响应与给定多模态输入所需的推理路径对齐，该局限性在复杂多模态任务中更显著，限制了MLLM的性能提升。

🚀 提出的新方法与思路
**Contrastive Demonstration Modeling**：重新构造每个演示，显式对比相同输入下的次优响应与更优响应，同时纳入揭示响应改进方式的推理路径，使朝向期望响应的推理路径更明确，引导MLLM超越表面层面的模仿。
**Response-Conditioned Retrieval Mechanism**：考虑到有效的响应改进依赖当前响应，引入该机制以选择推理路径与当前响应更相关的演示。
**Lightweight Alignment Controller**：用于预测响应质量，确定是否需要进一步改进。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理路径对齐能力 | 显式关联推理路径与响应，提升响应与多模态输入要求的推理路径的匹配度 |
| 表面模仿规避 | 引导模型超越对演示的表面层面模仿，聚焦于推理路径的学习 |
| 演示匹配准确性 | 基于当前响应选择相关演示，提升演示与当前任务需求的匹配度 |
| 响应改进判断 | 可自主判断是否需要进行响应改进，减少不必要的计算 |
| 多模态任务性能 | 在三类多模态任务（尤其视觉问答VQA）上提升MLLM性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文仅说明实验涉及三类多模态任务，未提及具体数据集名称 |

🎯 实验设置与评估指标
涉及三类多模态任务（重点为视觉问答VQA），评估指标相关信息论文未报告。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未提及具体基线方法名称及类型信息 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有定量结果相关信息论文未报告，具体如下：
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：该研究提出的结合对比演示建模、响应条件检索、轻量对齐控制器的多模态ICL框架，可在多模态任务（尤其视觉问答VQA）上实现MLLM性能的提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的结合对比演示建模、响应条件检索和轻量对齐控制器的多模态In-Context Learning框架，解决了现有方法依赖表面模仿、推理路径对齐困难的问题，在三类多模态任务中实现了MLLM性能的提升，且在视觉问答任务上提升效果尤为显著。

</details>

---

### 6. [Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign](https://arxiv.org/abs/2609.10970v1)

**Authors**: Haoran Jin, Jirong Yang, Zhiheng Zhang, Justin Shin, Barry Lyu, Kangqi Zhang, Yunpeng Liu, Nathan Bleier  
**Category**: cs.AR  
**Published**: 2026-09-11  
**Score**: 60.0  
**Type**: new  
**ArXiv ID**: 2609.10970v1  

#### Abstract
Modern ML workloads, with stringent latency and energy constraints, are increasingly hard to run efficiently on homogeneous commodity hardware. We argue that operator-level disaggregation--tailoring microarchitecture, batching, and memory hierarchy to each operator--is essential to overcome these li...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign
1. 论文的主要贡献和创新点
✅ 解决的问题
现代机器学习工作流对延迟和能效有严格要求，在同构商用硬件上高效运行愈发困难；算子级解聚虽能缓解该问题，但会导致极高的非重复性工程（NRE）成本；基于小芯片的集成可摊薄NRE成本，但小芯片池组成与加速器设计存在循环依赖，制约性能提升。

🚀 提出的新方法与思路
**Fengshui（芯片生态与加速器协同设计框架）**：联合优化芯片池组成与定制应用特定集成电路（BASIC）设计，通过算子级解聚构建BASIC，协同探索芯片与内存异构性、张量融合，以及流水线/张量/专家并行，并结合布局布线验证确保物理实现的可行性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 能效降低比例 | 较同构加速器降低48.5% |
| 能耗成本乘积（EC）降低比例 | 较同构加速器降低88.1% |
| 能耗延迟乘积（EDP）降低比例 | 较同构加速器降低93.0% |
| 能耗延迟成本乘积（EDPC）降低比例 | 较同构加速器降低97.8% |
| 与未受约束异构设计得分偏差 | 偏差在4.1%以内 |
| 数据中心MoE及密集LLM服务prefill能耗降低比例 | 较同构加速器最多降低16.8% |
| 数据中心MoE及密集LLM服务prefill EC降低比例 | 较同构加速器最多降低28.7% |
| 边缘自动驾驶感知场景能耗降低比例 | 实时延迟约束下较同构加速器降低12.0% |
| 边缘自动驾驶感知场景EC降低比例 | 实时延迟约束下较同构加速器降低23.6% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 评估Fengshui在数据中心MoE、密集LLM服务、边缘自动驾驶感知等不同神经网络任务中的性能表现 |

🎯 实验设置与评估指标
针对数据中心MoE、密集LLM服务、边缘自动驾驶感知任务，对比Fengshui生成的BASIC与同构加速器、未受约束异构设计的性能，评估相关能效与延迟指标。
| 指标 | 含义 |
| ---- | ---- |
| 能耗 | ↓ 越低越好 |
| 能耗成本乘积（EC） | ↓ 越低越好 |
| 能耗延迟乘积（EDP） | ↓ 越低越好 |
| 能耗延迟成本乘积（EDPC） | ↓ 越低越好 |
| 与未受约束异构设计得分偏差 | ↑ 越高越接近最优 |
| prefill能耗 | ↓ 越低越好 |
| prefill EC | ↓ 越低越好 |
| 实时延迟约束下的能耗 | ↓ 越低越好 |
| 实时延迟约束下的EC | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 同构加速器 | 商用同构硬件 | 采用统一微架构的通用硬件 |
| 未受约束异构设计 | 理论最优异构设计 | 无小芯片池约束的完全异构设计 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**论文未报告具体表号，仅在摘要中提及相关结果**
💡 结论：Fengshui生成的定制应用特定集成电路（BASIC），在多场景神经网络任务中较同构加速器实现了能效、延迟及成本相关指标的显著优化，且性能接近理论最优异构设计。

4. 关键结论和发现
- 主要发现：
1. Fengshui框架可通过算子级解聚与多维度协同优化，缓解同构硬件在机器学习工作流中的能效与延迟瓶颈，同时降低定制化带来的NRE成本；
2. 仅需8个精心选择的小芯片即可实现接近未受约束异构设计的性能，适配多样化神经网络任务需求；
3. Fengshui在数据中心大模型服务与边缘自动驾驶感知任务中均表现出能效、成本乘积的显著优势，具备良好的场景适配性。
- 方法局限性：
论文未报告
- 未来工作：
论文未报告
> ✅ **总结一句话**：Fengshui是一款联合优化芯片池组成与定制应用特定集成电路设计的协同框架，通过算子级解聚和多维度并行探索，在数据中心、边缘等多样化神经网络任务中大幅优化了能效、延迟及成本乘积，仅需少量小芯片即可获得接近理论最优异构设计的性能。

</details>

---

### 7. [REACH: Controller-Managed Long-Span ECC for HBM AI Inference](https://arxiv.org/abs/2609.10861v1)

**Authors**: Rui Xie, Yunhua Fang, Asad Ul Haq, Linsen Ma, Sanchari Sen, Swagath Venkataramani, Liu Liu, Tong Zhang  
**Category**: cs.AR  
**Published**: 2026-09-11  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2609.10861v1  

#### Abstract
High-Bandwidth Memory (HBM) cost motivates stronger controller protection that can support a wider range of device error rates. Long-span error-correcting codes provide stronger protection at a comparable code rate, but a direct implementation couples small accesses to span-wide state and requires c...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

REACH: Controller-Managed Long-Span ECC for HBM AI Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
HBM成本高昂，需要更强的控制器保护以支持更宽的设备错误率；长跨度ECC可提供更强错误防护且码率相当，但直接实现方案存在耦合小访问到跨度范围状态、需HBM带宽内昂贵解码的缺陷；读主导的LLM解码场景下，传统直接长跨度ECC未适配该场景顺序读支持跨度聚合、稀疏写限制奇偶校验更新流量的特性，存在额外开销。

🚀 提出的新方法与思路
**Controller-Managed Long-Span ECC架构（REACH）**：作为控制器微架构，采用已有的内部码纠正常见错误，识别未解决块，预留长外部码用于已知擦除修复；通过差分奇偶校验减少写流量；协同设计端点，在无需额外数据突发的前提下保留32B事务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 错误防护能力 | 支持宽范围设备错误率，适配读主导LLM解码场景的特性优化 |
| 控制器资源开销 | 相比传统直接长跨度设计，面积和功耗开销更低（论文提及相关数值，无对应图表来源） |
| 吞吐量表现 | 高错误压力下仍能维持可观应用吞吐量，适配HBM的高带宽需求（论文提及相关数值，无对应图表来源） |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为评估HBM控制器在高错误压力下的性能、资源开销；评估指标及含义如下：
| 指标 | 含义 |
| --- | --- |
| 应用吞吐量 | 单位时间内处理的数据量，值越高越好 |
| 控制器面积 | 控制器硬件占用的面积，值越低越好 |
| 建模功耗 | 控制器的功耗值，值越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 直接长跨度设计（direct-long design） | 基线方法 | 传统直接实现长跨度ECC的方案，存在耦合访问、解码开销大等缺陷 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. REACH架构通过分层ECC设计、差分奇偶校验及协同端点设计，在支持强错误防护的同时降低控制器面积与功耗；2. REACH适配读主导LLM解码场景，在高错误压力下仍能维持较高吞吐量；3. 预留长跨度错误恢复处理异常请求的策略，优化了控制器的资源利用效率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：REACH是针对读主导LLM解码场景设计的控制器微架构，通过分层ECC及相关优化设计，在为HBM提供强错误防护的同时，降低了控制器面积与功耗并维持高吞吐量。

</details>

---

### 8. [Rethinking Sparse Formats for RISC-V: A Hierarchical Approach to High-Performance SpMV](https://arxiv.org/abs/2609.11352v1)

**Authors**: Anna Pirova, Anastasia Vodeneeva, Konstantin Kovalev, Alexander Ustinov, Maksim Zagriadskov, Daniil Litvyakov, Arthur Kulik, Evgeny Kozinov, Valentin Volokitin, Iosif Meyerov  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2609.11352v1  

#### Abstract
The sparse matrix-vector multiplication (SpMV) algorithm is a fundamental computational kernel of linear algebra and serves as a building block for numerous applications, primarily iterative solvers for systems of linear equations used in scientific and engineering simulations. This paper compares v...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Rethinking Sparse Formats for RISC-V: A Hierarchical Approach to High-Performance SpMV
1. 论文的主要贡献和创新点
✅ 解决的问题
SpMV算法是线性代数的基础计算内核，是科学与工程模拟中线性方程组迭代求解器的核心组件；现有多种稀疏矩阵存储格式在RISC-V处理器上的向量化SpMV实现未针对性适配架构特性，导致性能未达最优，且不同格式的SpMV性能差异明显，缺乏适配RISC-V的高性能稀疏格式方案。现有8种已确立的稀疏矩阵存储格式均存在未适配RISC-V向量扩展特性、SpMV性能受限的缺陷。

🚀 提出的新方法与思路
**Hierarchical CSR (HCSR)**：对传统CSR稀疏矩阵存储格式进行改进，提出的新型稀疏矩阵存储格式，核心是结合RISC-V架构的向量扩展（RVV）特性优化存储结构，适配RVV 1.0 intrinsics以提升RISC-V处理器上的SpMV计算性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| RISC-V平台SpMV执行时间 | 在所有对比的8种现有稀疏格式中，HCSR的SpMV执行时间最短 |
| SpMV通用加速效果 | 选定合适的稀疏矩阵存储格式可使SpMV计算平均加速（论文未报告该加速比对应具体表号、图号） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告具体的稀疏矩阵数据集细节 | 用于开展SpMV性能对比实验，覆盖广泛类别的稀疏矩阵 |

🎯 实验设置与评估指标
任务：在SpacemiT K1和K3 RISC-V开发板上，对比8种现有稀疏矩阵存储格式与提出的HCSR格式的向量化SpMV性能，SpMV实现基于RVV 1.0 intrinsics。
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| SpMV执行时间 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 8种现有稀疏矩阵存储格式 | 基准方法 | 均为已确立的稀疏矩阵存储格式，用于与HCSR格式进行性能对比 |
| Hierarchical CSR (HCSR) | 提出的新方法 | 针对RISC-V架构优化的改进型CSR格式，采用RVV 1.0 intrinsics实现，对应开源C++库RVVLASparse |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**
论文未报告该实验的相关内容，包括L2、碰撞率等指标的具体数据与对应表号、图号。

**效率对比（FPS / 参数量）**
论文未报告该实验的相关内容，包括FPS、参数量等指标数据。

**跨域 / zero-shot 迁移**
论文未报告该实验的相关内容。

**鲁棒性 / 扰动测试**
论文未报告该实验的相关内容。

**消融实验**
论文未报告该实验的相关内容。

💡 结论：在SpacemiT K1和K3 RISC-V开发板上，提出的HCSR格式在所有对比的8种现有稀疏格式中实现了最短的SpMV执行时间，选择适配RISC-V的稀疏矩阵存储格式可提升SpMV计算效率。

4. 关键结论和发现
- 主要发现：1. 稀疏矩阵存储格式对RISC-V平台的SpMV性能有显著影响；2. 针对RISC-V优化的HCSR格式在各类稀疏矩阵上的SpMV执行时间优于传统CSR格式及其他7种现有稀疏格式；3. 选定适配RISC-V架构的稀疏格式可一定程度上提升SpMV计算效率。
- 方法局限性：论文未报告具体实验所用的稀疏矩阵数据集详情、不同格式性能对比的具体量化数值表，未涉及其他RISC-V平台的性能验证结果，未说明HCSR在大规模稀疏矩阵上的性能表现细节。
- 未来工作：论文未明确提及具体的未来研究方向。

> ✅ **总结一句话**：该论文针对RISC-V处理器的SpMV计算优化，提出改进型稀疏矩阵存储格式Hierarchical CSR（HCSR），基于RVV 1.0 intrinsics实现开源C++库RVVLASparse，在SpacemiT K1和K3 RISC-V开发板上验证了HCSR的最优SpMV性能，可显著提升计算效率。

</details>

---

### 9. [ExaServe: Large-Scale LLM Serving on Exascale HPC Systems](https://arxiv.org/abs/2609.10812v1)

**Authors**: Wenyi Wang, Shu Shi, Yadu Babuji, Ian Foster, Kyle Chard  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.10812v1  

#### Abstract
Cloud-native LLM serving frameworks have made deployment routine in data centers, yet deploying them on leadership-class supercomputers remains an engineering challenge requiring scheduler integration, MPI launch, accelerator selection, node-local weight staging, and platform-specific patches. We pr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ExaServe: Large-Scale LLM Serving on Exascale HPC Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
云原生LLM服务框架在领导力级超级计算机上部署时，需手动处理调度器集成、MPI启动、加速器选择、节点内权重暂存、平台特定补丁等工程步骤，部署流程繁琐、难度大。

🚀 提出的新方法与思路
**ExaServe**：一款可通过pip安装的框架，能够将声明式YAML规范转化为可复现的大规模LLM服务部署方案，适配超级计算机的部署需求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 部署复杂度 | 无需手动处理调度器集成、MPI启动等多类工程步骤，降低超算上LLM服务的部署门槛 |
| 部署可复现性 | 基于声明式YAML规范，支持生成可复现的大规模LLM部署方案 |
| 部署规模支持 | 可在ALCF Aurora超算上实现1到256节点（3072 vLLM replicas）的大规模LLM服务部署 |
| 关键障碍暴露 | 在超算环境中部署LLM服务，同时暴露未来百亿亿级LLM服务需解决的核心瓶颈 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
实验任务为在ALCF Aurora超级计算机上进行大规模LLM服务部署与推理性能测试；评估指标如下：
| 指标 | 含义（箭头） |
| --- | --- |
| 非流式推理请求吞吐量 | 单位为requests/s，越高越好（↑） |
| 非流式推理token吞吐量 | 单位为tokens/s，越高越好（↑） |
| 流式推理请求吞吐量 | 单位为requests/s，越高越好（↑） |
| 控制平面集群启动时间 | 单位为分钟，越低越好（↓） |
| 节点规模 | 单位为节点数，越大越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
仅列出论文明确报告的实验：
**无对应表号（来源：论文摘要）：ALCF Aurora超算上的LLM部署与推理性能**
| 实验场景 | 结果 |
| --- | --- |
| 非流式推理扩展性 | 部署至256节点时接近线性扩展，请求吞吐量约27.1k requests/s，token吞吐量约3.8M tokens/s |
| 流式推理性能 | 中央代理在请求吞吐量约4.7k requests/s时达到性能瓶颈，此时模型服务器仍符合服务水平目标 |
| 控制平面性能 | Ray Serve控制平面存在O(N²)级瓶颈，256节点时集群启动时间约30分钟 |

💡 结论：ExaServe可在ALCF Aurora超算上实现大规模LLM部署，但Ray Serve控制平面的O(N²)瓶颈是超算级LLM服务的关键障碍；

其他实验（主benchmark性能、效率对比、跨域迁移、鲁棒性测试、消融实验）论文未报告。

4. 关键结论和发现
- 主要发现：1. ExaServe可实现超算环境下从1到256节点的可复现大规模LLM服务部署，非流式推理在256节点时接近线性扩展；2. 流式推理中中央代理为性能瓶颈，请求吞吐量约4.7k requests/s时进入性能 plateau；3. Ray Serve控制平面存在O(N²)级扩展性瓶颈，导致256节点时集群启动时间延长至约30分钟；
- 方法局限性：ExaServe依赖的Ray Serve控制平面在超算大规模节点部署时存在O(N²)级瓶颈，显著增加集群启动时间；
- 未来工作：优化超算级LLM服务的控制平面性能，解决现有框架在大规模部署时的扩展性瓶颈；

> ✅ **总结一句话**：ExaServe是一款可通过pip安装的声明式框架，能便捷实现超算上的大规模LLM服务部署，同时暴露了百亿亿级规模下LLM服务需突破的控制平面瓶颈。

</details>

---

### 10. [Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking](https://arxiv.org/abs/2609.10745v1)

**Authors**: Parinthapat Pengpun, Simran Khanuja, Graham Neubig  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.10745v1  

#### Abstract
Multimodal entity linking grounds entity mentions in text and images to knowledge-base entries. These systems degrade on rare entities, but prior work measures rarity primarily through popularity-based metrics such as pageviews. We broaden this view using knowledge-graph structural metrics that capt...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态实体链接系统在稀有实体上性能下降显著，但现有工作主要采用基于流行度的指标衡量实体稀有性，这些指标会遗漏大量稀有实体；同时状态-of-the-art模型在稀有实体切片上的准确率下降明显，现有方法中单独推理无法有效提升稀有实体准确率，单独检索可提升稀有实体准确率但会损害整体准确率，未有效解决多语言环境下的稀有实体链接问题。

🚀 提出的新方法与思路
**Training-Free Iterative VLM Reasoning-Retrieval Framework**：提出无需额外训练的框架，利用具备推理能力的视觉语言模型（VLM）迭代搜索维基百科、动态收集相关证据，以适配多语言多模态实体链接任务，缓解稀有实体下的性能问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 稀有实体链接性能 | 融合推理与检索的互补性，避免单一方法的缺陷，稀有实体性能提升显著 |
| 整体实体链接性能 | 多语言任务下整体性能优于SOTA方法 |
| 多语言适配性 | 可覆盖5种语言的多语言实体链接场景 |
| 训练成本 | 无需额外训练，部署灵活 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MERLIN | 多语言多模态实体链接基准，覆盖5种语言（印地语、印尼语、日语、泰米尔语、越南语） |
| MERLIN-Rare | 论文发布的稀有实体测试切片，用于稀有实体任务的针对性评估 |

🎯 实验设置与评估指标
任务为多模态实体链接；评估指标为准确率，指标方向为越高越好。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有SOTA多模态实体链接系统 | 基线方法 | 采用基于流行度的稀有实体衡量指标，在稀有实体上性能下降明显 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文提出的最佳系统在MERLIN整体任务上优于SOTA方法，在稀有实体切片上优于SOTA方法；
2. 效率对比：论文未报告；
3. 跨域/zero-shot迁移：论文未报告；
4. 鲁棒性/扰动测试：论文未报告；
5. 消融实验：论文明确指出，单独推理无法显著提升稀有实体准确率，仅检索可提升稀有实体准确率但损害整体准确率，推理与检索结合表现最佳。

4. 关键结论和发现
- 主要发现：① 采用不同的稀有性定义会暴露多模态实体链接系统的不同失败模式；② 推理与检索在实体链接任务中具有互补作用；③ 单独的推理或检索无法同时优化稀有实体和整体任务性能，需结合使用；④ 所提框架在多语言多模态实体链接任务上性能优于SOTA方法。
- 方法局限性：论文未报告；
- 未来工作：论文未报告。

> ✅ **总结一句话**：本文提出了一种无需训练的迭代推理检索框架，结合知识图谱结构指标定义稀有实体，在覆盖5种语言的多语言多模态实体链接任务中，稀有实体和整体性能均显著优于现有SOTA方法。

</details>

---

### 11. [GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay](https://arxiv.org/abs/2609.11923v1)

**Authors**: Boning Li, Longbo Huang  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.11923v1  

#### Abstract
Counterfactual regret minimization (CFR) is one of the few large numerical workloads that still runs faster on CPUs than on GPUs. Each iteration sweeps a game tree with up to billions of states in millions of small, interdependent gather and scatter steps issued through a generic tree interface. On ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay
1. 论文的主要贡献和创新点
✅ 解决的问题
Counterfactual Regret Minimization（CFR）是少数运行在CPU上性能优于GPU的大型数值工作负载，其每次迭代遍历含数十亿状态的游戏树时，需通过通用树接口发出数百万个小型、相互依赖的gather与scatter步骤；GPU内核耗时仅微秒，因此内核启动与框架调度占主导运行时间，现有GPU实现性能不及优化的CPU代码。

🚀 提出的新方法与思路
**GPU-CFR编译器与运行时**：利用固定游戏的CFR迭代除数值外所有信息可预先确定的观察，将任意游戏编译为静态数据流，包括扁平边和信息集数组、预计算索引、深度级批处理操作序列，仅求解器状态在迭代间变化。
**静态机会折叠、深度级执行块与双路可达缓存**：将框架操作量减少多达18.1倍。
**CUDA Graph重放**：因形状、索引、缓冲地址从未变化，单次记录迭代后，可通过单图启动完成重放。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
GPU端性能 | 在A100加速器上针对多游戏套件的性能显著优于现有最快GPU端CFR实现
CPU端性能（无加速器） | 八CPU线程环境下性能优于GPU基线实现
结果一致性 | CPU端优化路径可复现参考迭代的位级一致性
回本效率 | 树构建与图捕获操作在第一次求解内即可收回成本

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
八游戏套件（涵盖卡牌游戏、骰子游戏、棋盘游戏） | 用于性能对比测试

🎯 实验设置与评估指标
任务为不同CFR相关实现的性能对比，指标及含义如下：
指标 | 含义
--- | ---
运行速度 | 处理游戏的速度，越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
Prior GPU CFR | GPU实现 | 现有公开GPU端CFR实现
LiteEFG | CPU实现 | 最快开源CPU端CFR实现之一

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体定量数值，仅提及在A100上针对八游戏套件的性能显著优于现有最快GPU端CFR实现，无加速器的八CPU线程下性能优于GPU基线实现
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

💡 结论：GPU-CFR通过静态数据流编译结合CUDA Graph重放，有效提升了CFR的运行性能，尤其在中大型游戏场景下表现优异。

4. 关键结论和发现
- CFR在GPU上性能不及CPU的痛点可通过静态数据流编译与CUDA Graph重放技术有效缓解
- 编译后的游戏表示在无加速器的CPU环境下也能获得显著性能提升
- GPU-CFR在中大型游戏场景下性能超越所有对比的CPU与GPU基线实现

方法局限性：论文未报告
未来工作：论文未报告

✅ **总结一句话**：GPU-CFR通过将游戏编译为静态数据流并利用CUDA Graph重放技术，大幅提升了Counterfactual Regret Minimization的运行速度，在中大型游戏上超越了现有所有对比的CPU与GPU基线实现。

</details>

---

### 12. [M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction](https://arxiv.org/abs/2609.10559v1)

**Authors**: Wenzhe Jin, Haina Tang  
**Category**: cs.LG  
**Published**: 2026-09-11  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2609.10559v1  

#### Abstract
To address the challenges of behavioral multimodality, limited semantic utilization, and long-term error accumulation in vessel trajectory prediction, this paper proposes M3-Former, a multimodal trajectory prediction framework enhanced by large language models (LLMs). The proposed framework incorpor...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction
1. 论文的主要贡献和创新点
✅ 解决的问题
船舶轨迹预测面临行为多模态性挑战、有限语义利用、长期误差累积三大核心痛点，现有方法未有效解决上述问题。

🚀 提出的新方法与思路
**多模态统一表示空间**：通过预训练大型语言模型（LLM）编码船舶静态属性的语义信息，结合自注意力机制将其与动态轨迹特征对齐，构建统一的多模态表示空间。
**双粒度Mixture-of-Experts（MoE）架构**：序列级专家建模全局航行趋势，token级专家细化细粒度机动行为，联合捕捉全局路径规划与局部运动变化。
**转向加权交叉熵损失**：设计该损失函数，缓解稀疏转向样本的长尾分布，提升关键机动场景的预测精度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 长期轨迹预测性能 | 在1-4小时的预测时域下一致优于现有最优基线 |
| 关键场景预测表现 | 提升稀疏转向等关键机动场景的预测精度 |
| 复杂场景鲁棒性 | 减少长期轨迹漂移，增强复杂水道、路线分支场景的预测鲁棒性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 真实世界丹麦AIS数据集 | 船舶轨迹预测任务的实验验证 |

🎯 实验设置与评估指标
任务为长期船舶轨迹预测（预测时域范围1-4小时），评估指标如下：
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| Average Displacement Error (ADE) | 预测轨迹与真实轨迹的平均位移误差，↓越低越好 |
| Final Displacement Error (FDE) | 预测轨迹终点与真实轨迹终点的位移误差，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 最强基线（SOTA） | 现有船舶轨迹预测最优基准方法 | 论文未报告具体基线名称，仅明确作为对比对象 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告具体表号，仅提及所提方法在1-4小时船舶轨迹预测任务中一致优于现有最优基线。
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告具体消融模块设置及定量结果，仅定性验证了语义融合和双粒度MoE的作用。

💡 结论：所提M3-Former在真实丹麦AIS数据集的1-4小时长期船舶轨迹预测任务中，性能优于现有最优基线，语义融合与双粒度MoE可提升预测稳定性与复杂场景鲁棒性。

4. 关键结论和发现
- 主要发现：1. M3-Former有效解决了船舶轨迹预测中的行为多模态、语义利用不足、长期误差累积问题；2. 在1-4小时预测时域内，M3-Former性能优于现有最优基线，且在关键机动场景及复杂水道的预测鲁棒性更好。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：M3-Former通过构建融合LLM编码的船舶静态语义、双粒度MoE架构及转向加权交叉熵损失的多模态Transformer框架，在真实丹麦AIS数据集的1-4小时长期船舶轨迹预测任务中取得优于现有最优基线的性能，同时提升了复杂场景的预测鲁棒性。

</details>

---

### 13. [ConvMem: Convolutional Memory for Long-Context Reasoning](https://arxiv.org/abs/2609.10441v1)

**Authors**: Hongming Zhang, Zhaozhen Gu, Fengshuo Bai, Ming Hao, Qingyang Zhang, Yuanyuan Wang, Shiyang Tang, Yanna Wang, Bo Xu  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.10441v1  

#### Abstract
While Large Language Models (LLMs) have demonstrated impressive capabilities, they often struggle with extremely long contexts due to fixed context limits. To address this, sequential approaches like MemAgent extend the effective context by reading text in segments and iteratively updating a fixed-s...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ConvMem: Convolutional Memory for Long-Context Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有解决LLM长上下文问题的sequential方法（如MemAgent）存在高延迟问题，且需要昂贵的RL训练，易导致在特定数据集上的过拟合。

🚀 提出的新方法与思路
**Hierarchical Convolution Reformulation**：将长上下文推理重新表述为层级卷积，使用针对特定查询提示的LLM作为卷积核，层级化总结文本片段，缩短推理路径（从线性链变为对数树结构）。
**Configurable Strides**：用于确保对证据的鲁棒捕获与传播。
**Skip Connections**：辅助证据的保留与传递，增强鲁棒性。
**Multi-Kernel Convolution**：将复杂查询分解为解耦的语义通道，缓解误差积累，同时实现跨文本片段和推理线程的大规模并行化。
ConvMem是训练-free的框架，无需RL训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练需求 | 训练-free，无需昂贵的RL训练 |
| 并行化能力 | 支持跨文本片段和推理线程的大规模并行化 |
| 过拟合风险 | 避免RL训练模型因参数先验导致的特定数据集过拟合，在OOD任务上表现更优 |
| 推理延迟 | 论文未报告 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RULER-HotpotQA | 长上下文推理任务的评估 |
| RULER-2WikiMultiHopQA | 长上下文推理任务的评估 |

🎯 实验设置与评估指标
任务为长上下文多跳推理，评估指标论文未报告。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| MemAgent | sequential方法 | 需RL训练，高延迟，易过拟合特定数据集 |
| 训练-free基线 | 训练-free方法 | 无RL训练，避免过拟合 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的主benchmark性能数值、效率对比数据、跨域/zero-shot迁移的具体数值、鲁棒性测试结果及消融实验的详细数据。

4. 关键结论和发现
- 主要发现：1. 传统的长上下文sequential推理方法（如MemAgent）存在高延迟、RL训练成本高且易过拟合特定数据集的缺陷；2. ConvMem作为训练-free框架，通过层级卷积优化推理路径（线性链转为对数树），支持大规模并行化，可缓解误差积累；3. ConvMem在OOD任务上避免了RL训练模型的参数先验过拟合问题，性能优于训练-free基线。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：ConvMem是一种训练-free、高度并行的长上下文推理框架，通过层级卷积将线性推理路径优化为对数树路径，缓解误差积累，在OOD任务上避免RL模型的过拟合问题，性能优于训练-free基线。

</details>

---

### 14. [Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs](https://arxiv.org/abs/2609.11744v1)

**Authors**: Joseph Kanichai, Tiziano De Matteis, Animesh Trivedi  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.11744v1  

#### Abstract
Prefix caching can reduce the time to first token (TTFT) of long-context LLM requests by reusing previously computed key-value (KV) states, but for short prefixes or fast GPUs, recomputation can be faster than loading from an external cache. We characterize this tradeoff in vLLM across GPU, CPU, and...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs

1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：前缀缓存通过复用之前计算的KV状态可降低长上下文LLM请求的TTFT，但存在性能权衡——当前缀较短或GPU运算速度较快时，重新计算KV状态的速度会超过从外部缓存加载的速度。
各方法缺陷：
- 现有外部KV缓存方案（如LMCache）的性能分析仅关注设备带宽，未考虑传输粒度、中间内存使用、传输进入请求调度的时机等关键影响因素；
- 原生vLLM的KV Offload实现未进行预加载等优化，磁盘I/O与计算任务未重叠，加载效率存在提升空间。

🚀 提出的新方法与思路
**py-kvcache（vLLM KV Offload连接器）**：针对vLLM设计的KV Offload连接器，集成异步direct I/O、绑定的共享暂存区、感知请求调度的预加载机制；可在请求仍处于等待阶段时提前启动磁盘读取操作，将磁盘I/O与GPU计算任务重叠，从而提升外部KV缓存的加载效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 磁盘加载效率 | 通过I/O与计算重叠机制提升外部缓存加载速度 |
| 适配场景 | 支持GPU、CPU、磁盘三级缓存配合，适用于长上下文、多轮、不规则前缀链等多种工作负载 |
| 部署灵活性 | 将外部KV缓存作为基于硬件配置的设置特定准入决策，适配不同硬件环境 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 合成工作负载 | 用于分析外部KV缓存的性能权衡关系 |
| LongBench、SCBench | 用于评估 irregular prefix chains、multi-turn等工作负载的性能 |
| Bailian trace | 用于生产环境LLM请求的重放测试 |

🎯 实验设置与评估指标
本次任务为vLLM环境下的外部KV缓存性能评估实验。
| 指标 | 含义 |
| ---- | ---- |
| 时间到第一个token（TTFT） | LLM请求生成首个token的时间，↓ 越低越好 |
| 缓存加载速度 | 外部缓存加载KV状态的执行效率 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| LMCache | 外部KV缓存方案 | 现有基于内存的KV缓存方案 |
| 原生vLLM KV Offload | 原生KV卸载实现 | vLLM原生自带的KV Offload方案 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主 benchmark 性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
1. 外部KV缓存的性能不仅取决于设备带宽，还受传输粒度、中间内存使用、传输进入请求调度的时机等多维度因素影响，不能仅以带宽作为唯一评估依据；
2. py-kvcache的异步direct I/O、绑定共享暂存、调度感知预加载设计，通过I/O与计算重叠的方式，可有效提升外部KV缓存的加载效率，适配多种长上下文工作负载；
3. 外部KV缓存是需结合硬件配置的设置特定准入决策：H100这类强GPU可存储足够的前缀，平均请求下GPU内存即可满足需求；弱GPU场景下外部缓存可优化TTFT。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：py-kvcache作为集成异步I/O、预加载等优化的vLLM KV Offload连接器，通过多维度设计提升外部KV缓存性能，其部署需结合硬件配置作为设置特定的准入决策。

</details>

---

### 15. [MultiHuSE: A Multimodal Dataset for Humour Styles and Emotions](https://arxiv.org/abs/2609.11322v1)

**Authors**: Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.11322v1  

#### Abstract
Computational recognition of verbal humour remains a challenging task, requiring an understanding of language, delivery style, emotions, and cultural context. Most existing approaches focus on binary classification and lack datasets that capture psychological dimensions of humour alongside variation...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：MultiHuSE: A Multimodal Dataset for Humour Styles and Emotions
1. 论文的主要贡献和创新点
✅ 解决的问题
现有言语幽默的计算识别研究多聚焦于二元分类，缺乏同时捕捉幽默心理维度及表达多样性的数据集，而幽默识别需理解语言、表达风格、情绪及文化语境等多要素，现有研究存在数据维度单一、难以建模多要素影响的核心痛点。

🚀 提出的新方法与思路
**MultiHuSE多模态幽默数据集构建**：构建包含2407个高清视频、50名人口统计多样性演员演绎的1463个文本样本的多模态数据集，涵盖affiliative、aggressive、self-enhancing、self-deprecating四种心理幽默风格及中性内容，设置情绪标注子集，通过同一文本的多演员演绎捕捉幽默的表达多样性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据覆盖 | 首次构建同时包含四种心理幽默风格及对应情绪标注的多模态数据集，覆盖幽默相关的语言、表达等核心维度 |
| 表达建模 | 提供同一文本的多演员演绎样本，支持系统性分析幽默的表达多样性 |
| 研究支撑 | 可为幽默与情绪关联的心理学研究、人类交际、AI驱动交互等领域提供数据支撑 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MultiHuSE | 用于幽默风格分类及情绪相关的多模态基准实验 |

🎯 实验设置与评估指标
实验任务为幽默风格分类，评估指标为准确率（越高越好）。
| 指标 | 含义 |
| --- | --- |
| 准确率 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Multimodal fusion | 多模态方法 | 融合文本、视频等多模态特征进行幽默风格分类 |
| Unimodal approaches | 单模态方法 | 仅使用单一模态特征的基准对比方法 |
| Text-based approach | 文本单模态方法 | 仅使用文本特征，为最强单模态信号的基准方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文提及幽默风格分类中，multimodal fusion方法性能优于unimodal approaches方法，且对affiliative幽默的识别增益尤为显著；论文未报告该结果对应的表号、章节等来源，不提供量化数值的具体来源标注。
论文未报告效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验等其他实验的相关内容。

4. 关键结论和发现
- 多模态融合方法在幽默风格分类任务中优于单模态方法，文本是幽默识别的单模态最强信号；
- 多模态融合对affiliative幽默的识别提升效果突出；
- MultiHuSE数据集为幽默相关的跨领域研究提供了重要的数据支撑。
- 方法局限性：论文未报告。
- 未来工作：论文提及该数据集可支撑人类交际、幸福感、AI驱动交互等方向的研究，未明确提出具体未来工作方向。

> ✅ **总结一句话**：构建了涵盖多种心理幽默风格、情绪标注及多演员表达多样性的多模态数据集MultiHuSE，为幽默识别、心理学关联研究及AI交互等领域提供了关键数据支撑。

</details>

---

### 16. [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](https://arxiv.org/abs/2609.09664v1)

**Authors**: Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.09664v1  

#### Abstract
Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time. As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computati...

---

### 17. [From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning](https://arxiv.org/abs/2609.10335v1)

**Authors**: Weichen Dai, Rafael Medeiros Cabral, Ziyi Shou, Yan Cao, Xin Shen, Dongcai Lu, Yi Zhou  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.10335v1  

#### Abstract
Plane geometry remains a significant challenge in AI, requiring the integration of visual perception and mathematical reasoning. While Large Multimodal Models (LMMs) naturally handle visuo-linguistic inputs, they are often computationally intensive and opaque. We demonstrate that a pure Large Langua...

---

### 18. [Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward](https://arxiv.org/abs/2609.09776v1)

**Authors**: Eshwar Reddy M, Sourav Karmakar  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2609.09776v1  

#### Abstract
Frontier gains in language-model reasoning come from reinforcement learning on reasoning traces and are concentrated in domains with a cheap, sound verifier. We argue the field's binding constraint is the verification gap: no scalable, incorruptible reward for reasoning outside formal domains. We ma...

---

### 19. [FlexComp: One Model for Every Ratio in Context Compression](https://arxiv.org/abs/2609.11192v1)

**Authors**: Kaiyan Zhao, Zhongtao Miao, Akiko Aizawa, Yoshimasa Tsuruoka  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.11192v1  

#### Abstract
Soft context compression condenses a context into a few memory tokens that a frozen LLM consumes in place of the raw text, but existing compressors fix the compression ratio at training and inference: each deployed ratio requires a separately trained model, and the chosen ratio is applied uniformly ...

---

### 20. [T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks](https://arxiv.org/abs/2609.11042v1)

**Authors**: Junyao Yang, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Zongxia Li, Haitao Mi, Leowei Liang  
**Category**: cs.LG  
**Published**: 2026-09-11  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.11042v1  

#### Abstract
Agent usage is shifting toward long-horizon tasks such as coding and scientific discovery, among which terminal tasks are especially important. We introduce T1, a Mixture-of-Experts model of 122B total trained with reinforcement learning, operating a real shell in a cloud sandbox for up to 300+ tool...

---

### 21. [Robust Multimodal Sentiment Analysis with Incomplete Modalities via Semantic-aware Completeness based Reconstruction](https://arxiv.org/abs/2609.10950v1)

**Authors**: Han-Jun Choi, Byunggill Joe, Saim Shin, Jin Yea Jang  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.10950v1  

#### Abstract
Recent multimodal sentiment analysis studies increasingly adopt text-centric fusion approaches to exploit the rich sentiment information inherent in the textual modality. However, these approaches often suffer from performance degradation during inference due to partially missing or noisy data in re...

---

### 22. [Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](https://arxiv.org/abs/2609.11762v1)

**Authors**: Jordi Luque, Fernando L\'opez, Aleix Sant  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.11762v1  

#### Abstract
Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder ...

---

### 23. [Design and Operation of a Federated GPU Cluster for Digital Humanities within DHinfra.at](https://arxiv.org/abs/2609.10552v1)

**Authors**: Florian Atzenhofer-Baumgartner, David Fleischhacker, Max Resch, Lukas Waldhofer, Michael Otto  
**Category**: cs.DC  
**Published**: 2026-09-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.10552v1  

#### Abstract
We describe the design, implementation, and operation of a small federated GPU cluster built for Digital Humanities (DH) research within the Austrian DHinfra.at project. The system spans two university sites, brokers logins from a national identity federation, and exposes compute through three inter...

---

### 24. [Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with Large Language Models](https://arxiv.org/abs/2609.11135v1)

**Authors**: Ken Chen, Maneesha Perera, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge  
**Category**: cs.LG  
**Published**: 2026-09-11  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.11135v1  

#### Abstract
Short-term photovoltaic (PV) power and global horizontal irradiance (GHI) forecasts are essential for effective dispatch, reserve scheduling, and grid operations. At these forecasting horizons, errors are predominantly driven by cloud induced ramps: relying solely on historical numerical data may st...

---

### 25. [Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations](https://arxiv.org/abs/2609.10866v1)

**Authors**: Tong Li, Saunak Kumar Panda, Yisha Xiang  
**Category**: cs.LG  
**Published**: 2026-09-11  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.10866v1  

#### Abstract
Reinforcement learning (RL) agents deployed in real-world environments are often vulnerable to adversarial perturbations in state observations, creating risks in safety-critical applications. Certification methods can improve robustness against adversarial perturbations by providing lower bounds on ...

---

### 26. [When Noise Fabricates Bias: The Fragility of LLM-as-a-Judge Bias Measurement under Noisy Text](https://arxiv.org/abs/2609.11067v1)

**Authors**: DongHyun Ryu, Jaehyeok Lee, YeongJun Hwang, JinYeong Bak  
**Category**: cs.CL  
**Published**: 2026-09-11  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2609.11067v1  

#### Abstract
Large language models are increasingly used as judges to measure social bias in text, yet the passages they judge are often noisy, containing typos, informal spelling, and broken punctuation. The consequences of such surface noise for social bias measurement remain unclear. To investigate this quest...

---

### 27. [Which Tokens Should SFT Actually Learn? A Token-Trimming Perspective on Mathematical Reasoning](https://arxiv.org/abs/2609.09707v1)

**Authors**: Yaning Jia, Chunhui Zhang, Wenxuan Xu, Xingjian Diao, Xiaoyuan Wang, Soroush Vosoughi  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.09707v1  

#### Abstract
Supervised fine-tuning (SFT) applies a uniform cross-entropy loss to all target tokens, even though different tokens provide unequal learning signals for mathematical reasoning. This uniform treatment can over-sharpen already mastered tokens while amplifying learning pressure on uncertain, low-confi...

---

### 28. [TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards](https://arxiv.org/abs/2609.10315v1)

**Authors**: Rui Sun, Zhan Shi, Bing He  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2609.10315v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) has advanced language-model reasoning in domains such as mathematics and code, where objective answers are inexpensive to check. Diagnostic reasoning over complex data lacks this advantage: establishing the true cause of an anomaly often requires...

---

### 29. [Bio-inspired Learning and Decision-Making with Probabilistic In-Memory Computing Hardware: Part 2](https://arxiv.org/abs/2609.11288v1)

**Authors**: Thomas Dalgaty, Eiji Kawasaki, Miguel de Prado, Tommaso Salvatori, Germain Haugou, Eric Flamand  
**Category**: cs.AR  
**Published**: 2026-09-11  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2609.11288v1  

#### Abstract
This report extends our previous work (Part 1), which introduced an energy-based model for learning and decision-making under uncertainty. The model leverages stochastic Langevin dynamics to continuously evolve approximate probability distributions over neuron states and model weights. However, as n...

---

### 30. [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925v1)

**Authors**: Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang, Shanmin Pang  
**Category**: cs.AI  
**Published**: 2026-09-11  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.09925v1  

#### Abstract
Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens...

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
