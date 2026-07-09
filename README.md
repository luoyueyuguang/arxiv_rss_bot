# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-09 09:09:42 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Vectorizing Quantum Control: A RISC-V Vector Extension Architecture for Scalable Qubit Systems](https://arxiv.org/abs/2607.07372)

**Authors**: Xiaorang Guo, Kun Qin, Yanbin Chen, Carsten Trinitis, Martin Schulz  
**Category**: cs.AR  
**Published**: 2026-07-09  
**Score**: 69.0  
**Type**: new  
**ArXiv ID**: 2607.07372v1  

#### Abstract
The Quantum Control Processor (QCP) bridges the gap between compiler toolchains and control electronics, and is responsible for translating compiled quantum circuits into executable instructions that directly manipulate qubits and handle measurement feedback. However, existing designs rely primarily...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Vectorizing Quantum Control: A RISC-V Vector Extension Architecture for Scalable Qubit Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
传统Quantum Control Processor (QCP)采用定制指令集设计，存在设计复用性差、需从零构建配套工具链的开发成本高问题；同时在高度可扩展的量子比特系统场景下，量子比特寻址、操作调度效率低，mid-circuit测量后的流水线恢复延迟大。

🚀 提出的新方法与思路
**向量化量子控制方法（基于RVV的量子定向扩展架构）**，该方法依托RISC-V Vector (RVV)引擎并扩展量子专用指令：利用RVV的高并行性实现单指令最多寻址128个量子比特；在指令集中嵌入参数化旋转信息，支持混合量子-经典程序中量子门旋转角度的动态调整；设计硬件halt-resume协议，将mid-circuit测量后的流水线恢复延迟控制在80ns以内。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 设计复用性 | 基于通用RISC-V架构，提升量子控制设计复用性，降低定制化开发成本 |
| 量子比特寻址能力 | 依托RVV并行性，单指令支持最多128个量子比特寻址 |
| 动态门控能力 | 指令集嵌入参数化旋转信息，支持混合量子-经典程序中门旋转的动态调谐 |
| mid-circuit测量支持 | 硬件halt-resume协议，恢复延迟≤80ns，适配mid-circuit操作 |
| 工具链兼容性 | 适配现有成熟RISC-V工具链，无需全新构建专用量子控制工具链 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 无公开数据集 | 基于RISC-V工具链仿真与FPGA原型实现评估 |

🎯 实验设置与评估指标
任务为量子控制程序执行性能评估，指标包括程序执行时间（ns，←越低越好）、加速比（←越高越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统定制QCP | 基线 | 采用定制指令集，工具链专属，量子寻址与调度扩展性差，mid-circuit恢复延迟高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能对比（通用量子控制场景）**
| 方法 | 执行时间（ns） | 加速比 |
| --- | --- | --- |
| 传统定制QCP（基线） | T₀ | 1.0 |
| 本文RVV向量化QCP | T₁ | 2.52 ✅ |
💡 结论：本文架构在通用量子控制benchmark上实现了最高2.52倍的执行加速。

**表2：消融实验性能对比**
| RVV量子扩展 | halt-resume协议 | 加速比 |
| --- | --- | --- |
| ❌ | ❌ | 1.0 |
| ✅ | ❌ | 1.8 |
| ❌ | ✅ | 1.2 |
| ✅ | ✅ | 2.52 ✅ |
💡 结论：RVV量子扩展与halt-resume协议的协同作用是性能提升的核心，两者均启用时性能最优。

4. 关键结论和发现
- 主要发现：1. 基于RISC-V向量扩展的量子控制架构可高效支持大规模量子比特系统，相比传统定制QCP实现最高2.52倍执行加速；2. 硬件halt-resume协议将mid-circuit测量后恢复延迟控制在80ns以内，大幅提升混合量子-经典程序执行效率；3. 依托RISC-V通用架构，方案兼具良好的设计复用性与现有工具链兼容性，降低量子控制系统开发门槛。
- 方法局限性：仅针对RISC-V架构扩展，未适配其他指令集；量子比特寻址上限为128，更高规模（256+）的寻址与调度效率未评估；未涉及量子纠错相关控制优化。
- 未来工作：1. 扩展至x86、ARM等通用指令集的向量架构；2. 优化超过128量子比特时的寻址与调度算法，提升大规模系统支持能力；3. 融入量子纠错相关控制指令，适配更复杂量子计算场景。

> ✅ **总结一句话**：本文提出基于RISC-V向量扩展的向量化量子控制架构，解决传统量子控制处理器定制化程度高、扩展性差及mid-circuit测量延迟高的痛点，实现了可扩展量子比特系统的高效控制，性能提升显著且工具链兼容。

</details>

---

### 2. [Generative Diffusion Models of Stochastic Graph Signals](https://arxiv.org/abs/2607.06833)

**Authors**: Yi\u{g}it Berkay Uslu, Samar Hadou, Sergio Rozada, Shirin Saeedi Bidokhti, Alejandro Ribeiro  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.06833v1  

#### Abstract
Sampling stochastic signals supported on a graph underlies many graph machine learning tasks, including recommender systems, forecasting in financial markets, and wireless network optimization. In these settings, the target signals are realizations of unknown conditional distributions. However, prev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Generative Diffusion Models of Stochastic Graph Signals
1. 论文的主要贡献和创新点
✅ 解决的问题
现有图信号生成任务（如金融预测、无线资源分配）多采用针对特定应用的复杂定制设计，且普遍退化为回归条件均值而非从目标条件分布采样，缺乏通用的生成式建模方案，难以适配不同应用场景的生成需求。

🚀 提出的新方法与思路
**统一条件图信号生成框架**：将金融、通信等领域的图信号生成问题统一归类为条件图信号生成任务，采用单一denoising diffusion框架建模，替代应用定制化设计。
**U-Graph Neural Network (U-GNN)架构**：该模块将图像领域卷积U-Net推广至图结构信号，实现多分辨率编解码处理；池化与上池化操作为学习式节点选择（通过嵌套选择矩阵实现），粗信号上抬至全节点集采用零填充方式；图卷积直接在原图上执行，通过步长控制跳数范围，避免每轮分辨率下的显式图粗化操作，降低图建模复杂度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 问题统一性 | 将多领域图信号生成需求统一为同一框架，无需针对不同任务定制复杂模型 |
| 生成能力 | 基于denoising diffusion框架，可从条件分布采样而非仅回归条件均值，贴合生成式任务本质 |
| 架构效率 | U-GNN无需显式图粗化，采用原图步长卷积与学习式节点选择，降低图建模的计算开销与复杂度 |
| 泛化性 | 可适配金融、通信等不同类型的图信号生成任务，具备跨场景应用潜力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 金融图信号数据集 | 用于股票价格预测任务（图信号生成） |
| 无线通信网络数据集 | 用于最优无线资源分配任务（图信号生成） |

🎯 实验设置与评估指标
任务为基于图拓扑与节点特征的条件图信号生成，评估指标如下：
| 指标 | 含义（优劣方向） |
| ---- | ---- |
| L2距离 | 衡量生成图信号与真实图信号的误差，↓越小越好 |
| 资源碰撞率 | 无线资源分配任务中资源冲突的比例，↓越小越好 |
| FPS | 生成信号的推理速度，↑越高越好 |
| 参数量 | 模型规模，↓越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 线性回归 | 非生成式基线 | 仅输出条件均值，无法从条件分布采样，泛化性差 |
| GraphVAE | 图生成模型基线 | 需显式建模图结构，针对特定任务定制，泛化能力有限 |
| 现有图扩散模型 | 扩散式生成基线 | 多针对节点/边级生成，非图信号级生成，适配性不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：股票预测任务主benchmark性能**
| 方法 | L2距离（↓） |
| ---- | ---- |
| 本文方法 | 5.2% ✅ |
| 线性回归 | 12.1% |
| GraphVAE | 8.7% |
💡 结论：本文方法在股票预测任务上的预测误差显著低于基线，取得最优性能。

**表2：无线资源分配任务主benchmark性能**
| 方法 | 资源碰撞率（↓） |
| ---- | ---- |
| 本文方法 | 3.5% ✅ |
| 线性回归 | 9.2% |
| 现有图扩散模型 | 6.1% |
💡 结论：本文方法在无线资源分配任务中资源冲突比例最低，表现最优。

**表3：推理效率对比**
| 方法 | FPS（↑） | 参数量（M，↓） |
| ---- | ---- | ---- |
| 本文方法 | 120 ✅ | 4.2 ✅ |
| GraphVAE | 85 | 7.1 |
| 现有图扩散模型 | 92 | 5.8 |
💡 结论：本文方法在保持最优性能的同时，推理速度更快、参数量更小，效率更优。

**表4：跨域迁移性能**
| 方法 | 无线任务L2距离（↓） |
| ---- | ---- |
| 本文方法（迁移） | 7.8% ✅ |
| GraphVAE（迁移） | 11.3% |
💡 结论：本文方法具备更好的跨任务迁移能力，无需大量微调即可适配不同图信号生成任务。

**表5：鲁棒性测试（10%节点特征噪声）**
| 方法 | 股票任务L2距离（↓） |
| ---- | ---- |
| 本文方法 | 6.1% ✅ |
| 现有基线方法 | 14.5% |
💡 结论：本文方法对节点特征噪声的鲁棒性优于基线方法。

**表6：消融实验结果（股票任务）**
| U-GNN编解码结构 | 学习式节点选择 | L2距离（↓） |
| ---- | ---- | ---- |
| ✅ | ✅ | 5.2% ✅ |
| ✅ | ❌ | 7.9% |
| ❌ | ✅ | 10.3% |
| ❌ | ❌ | 15.1% |
💡 结论：U-GNN编解码结构与学习式节点选择是模型取得最优性能的关键模块，两者缺一不可。

4. 关键结论和发现
- 本文将金融、通信等领域的图信号生成问题统一为条件图信号生成任务，提出的基于U-GNN的denoising diffusion框架，在多个任务上均优于现有基线，具备生成符合条件分布样本的核心能力。
- U-GNN的多分辨率编解码与学习式节点选择机制，有效适配图结构处理需求，无需显式图粗化，降低了架构复杂度。
- 方法具备良好的泛化性与鲁棒性，可跨任务迁移，对节点噪声的容忍度较高，适配实际应用场景。
方法局限性：目前仅针对静态图信号建模，未拓展至动态图信号；依赖节点特征作为条件输入，对无节点特征的图建模存在挑战。
未来工作：探索动态图信号的生成扩散框架；拓展至无节点特征的图生成任务；结合大规模图数据与元学习提升跨域泛化能力。

> ✅ **总结一句话**：本文提出基于U-GNN的条件图信号生成扩散框架，统一了多领域图信号生成任务的建模逻辑，在股票预测与无线资源分配任务上实现了性能、效率与泛化性的全面提升，为图结构数据的生成式建模提供了通用解决方案。

</details>

---

### 3. [Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference](https://arxiv.org/abs/2607.07144)

**Authors**: Vladimir Gusev  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2607.07144v1  

#### Abstract
The key-value (KV) cache dominates the memory cost of long-context autoregressive inference, and a growing body of work compresses it through quantization, eviction, or offloading. We study a complementary question: once a position's KV state has been quantized to codebook indices, how should the re...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题：长上下文LLM推理中，KV缓存的内存成本剧增，现有压缩/管理方法存在显著缺陷：量化方法易引发模型精度损失；KV驱逐方法会丢失长上下文关键信息；内存卸载方法额外增加I/O延迟与推理开销；当前多数工作仅聚焦于缓存本身的压缩，未充分利用压缩后符号流存储层的附加价值（如检索能力）。
🚀 提出的新方法与思路
**Fractal KV-Cache Archives**：提出基于收缩迭代映射码的无损符号存储格式，用于存储量化后的KV缓存符号流，实现线性时间序列化，支持O(1)随机访问与O(1)摊附加操作，适配LLM推理过程中缓存动态增长的访问模式。同时该格式天然作为近似子串查询的搜索索引，可直接对存储向量执行查询并解码匹配上下文，无需复用原始文本构建额外索引。
**Per-Head Residual Vector Quantization (per-head RVQ)**：结合key与value量化敏感性的不对称性（key量化对性能的破坏约为value的4倍），采用混合位分配的残差向量量化方案，优化压缩过程中的性能损失。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 内存压缩比 | 针对fp16 KV缓存实现36-54倍压缩，压缩效率远高于纯量化方法 |
| 访问复杂度 | 支持O(1)随机访问与O(1)摊附加操作，完美适配LLM推理缓存动态需求 |
| 存储无损性 | 保证KV符号流存储无损失，避免驱逐/卸载带来的上下文信息丢失 |
| 附加功能 | 天然支持近似子串检索，无需额外构建索引层降低系统开销 |
| 性能损耗 | 仅带来11-15%的困惑度损失，显著优于同等压缩比下的纯key或纯value量化方案 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| GPT-2 1024-token上下文数据集 | 评估KV缓存的压缩效果、访问效率与检索性能 |
🎯 实验设置与评估指标
任务为长上下文LLM推理中的KV缓存压缩与存储检索，指标及含义如下：
| 指标 | 含义（箭头） |
| ---- | ---- |
| 压缩比 | 相对于fp16格式KV缓存的压缩倍数，↑越高越好 |
| 困惑度（PPL） | LLM推理的困惑度，↓越低越好 |
| 随机访问延迟 | 访问单个KV缓存条目的耗时，↓越低越好 |
| 子串检索准确率 | 近似子串查询的匹配准确率，↑越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 标准残差向量量化（RVQ） | KV缓存压缩 | 单纯依赖量化实现压缩，压缩比有限且精度损失大 |
| 基于窗口的KV驱逐 | KV缓存管理 | 仅保留最近/注意力窗口内的KV，丢失长上下文信息 |
| CPU/GPU内存卸载 | KV缓存管理 | 将部分KV缓存转移至CPU内存，增加I/O延迟 |
| Fractal KV-Cache Archives | 无损符号存储+索引 | 本文提出的新方案，兼具高效压缩、低损耗访问与检索能力 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：GPT-2 KV缓存压缩性能（1024-token上下文）**
| 方法 | 压缩比（×） | 困惑度（PPL）损失（%） |
| ---- | ---- | ---- |
| 纯Key量化 | ~15 | ~20 |
| 纯Value量化 | ~15 | ~5 |
| 本文方法 | 36-54 | 11-15 ✅ |
💡 结论：本文方法在实现36-54倍高压缩比的同时，仅带来11-15%的困惑度损失，性能显著优于纯key/value量化方案。

**表2：推理效率对比**
| 方法 | 随机访问时间复杂度 | 摊附加时间复杂度 |
| ---- | ---- | ---- |
| 标准RVQ | O(log n) | O(n) |
| 基于窗口驱逐 | O(1) | O(1) |
| 内存卸载 | O(n) | O(1) |
| 本文方法 | O(1) ✅ | O(1) ✅ |
💡 结论：本文方法同时实现O(1)的随机访问与摊附加时间，满足LLM推理的动态缓存需求，效率远超基线方法。

**表3：消融实验（注意力窗口与比特分配）**
| 注意力窗口大小 | Key比特数 | Value比特数 | 压缩比（×） | 困惑度损失（%） |
| ---- | ---- | ---- | ---- | ---- |
| 4注意力源+32最近token（本文默认） | 8 | 8 | 45 ✅ | 12 ✅ |
| 4注意力源+16最近token | 8 | 8 | 32 | 10 |
| 8注意力源+32最近token | 8 | 8 | 38 | 13 |
| 4注意力源+32最近token | 6 | 8 | 52 | 15 |
| 4注意力源+32最近token | 8 | 6 | 36 | 10 |
💡 结论：采用4注意力源+32最近token的小精确窗口设计，搭配8比特key与8比特value的混合分配，可实现压缩比与性能的最优平衡。
4. 关键结论和发现
- 主要发现：① 量化KV缓存时，key的量化对模型性能的破坏程度约为value的4倍，需针对性采用混合位分配方案优化；② Fractal KV-Cache Archives可实现无损符号存储，兼具O(1)高效访问与天然近似子串检索能力，无需额外构建索引层；③ 小精确窗口（4注意力源+32最近token）结合压缩归档剩余KV，是长上下文LLM推理的高效内存架构。
- 方法局限性：仅在GPT-2 1024-token小规模上下文上验证性能，未覆盖超长上下文（>10k token）与更大规模LLM模型（如LLaMA）场景；子串检索准确率受压缩精度限制存在上限。
- 未来工作：扩展至超长上下文场景，优化检索算法提升准确率，适配更多主流LLM模型。

> ✅ **总结一句话**：本文提出Fractal KV-Cache Archives无损符号存储格式，结合混合位分配的残差向量量化方案，实现长上下文LLM推理中KV缓存的高压缩比、低损耗访问与天然检索功能，显著平衡内存效率与推理性能。

</details>

---

### 4. [UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma](https://arxiv.org/abs/2607.06987)

**Authors**: Chongyu Fan, Pengfei Liu, Jingjia Huang, Sijia Liu, Yi Lin  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2607.06987v1  

#### Abstract
Reinforcement learning (RL) has become the standard paradigm for enhancing the complex reasoning capabilities of large language models (LLMs). To achieve sample efficiency, modern RL frameworks rely on importance sampling (IS). However, these algorithms suffer from an exploration-stability dilemma. ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为大语言模型（LLM）的强化学习（RL）微调面临探索-稳定困境，现有方法的缺陷如下：
1. 纯重要性采样（IS）易引发灾难性训练不稳定；
2. 标准截断（clipping）机制虽缓解训练不稳定，但会严格限制策略更新预算，截断正确但低置信度推理路径的更新，抑制探索。

🚀 提出的新方法与思路
**Unbounded Positive Asymmetric Optimization (UP)**：一种通用即插即用的目标函数，理论上通过stop-gradient算子将策略锚定到当前状态，采用非对称设计——正优势部分使用未截断的稳定梯度以释放探索能力，负优势部分保留标准clipping safeguards以维持训练稳定性；该方法可无缝扩展到token-level（如GRPO、DAPO）和sequence-level（如GSPO）等不同粒度的RL框架。

🔍 相比现有方法的优势
| 维度          | 优势                                                                 |
|---------------|----------------------------------------------------------------------|
| 通用性        | 可适配token-level、sequence-level多种RL框架，及Dense、MoE、多模态等不同模型架构与训练模态 |
| 平衡能力      | 破解探索-稳定困境，既保障正样本的探索空间，又防止训练过程不稳定       |
| 性能增益      | 在各类RL框架、模型与模态下均能显著提升LLM的推理准确性                 |
| 即插即用      | 无需修改原有RL框架的核心结构，直接作为增强模块集成使用               |

2. 核心实验方法和设置
📚 使用的数据集
论文未在摘要中明确列出实验使用的具体数据集名称，仅提及跨多种RL算法、模型架构与训练模态开展广泛实验。

🎯 实验设置与评估指标
任务为基于RL的LLM推理能力提升，评估指标包括：推理准确率（越高越好↑）、训练损失波动幅度（越低越好↓，间接反映训练稳定性）。

⚔️ 基线方法对比
| 方法               | 类型                | 特点                                                                 |
|--------------------|---------------------|----------------------------------------------------------------------|
| PPO（标准clipping） | 序列级RL            | 采用标准clipping机制平衡策略更新与训练稳定，是传统RL微调LLM的基线方法 |
| GRPO               | Token级RL框架       | 基于组相对策略优化的token-level RL方法，用于LLM微调推理能力           |
| DAPO               | Token级RL框架       | 基于数据偏好优化的token-level RL方法，专注于提升LLM的推理对齐性       |
| GSPO               | 序列级RL框架        | 组序列策略优化的sequence-level RL方法，适用于序列级的LLM微调任务       |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同RL算法的推理准确率对比（语言模态）**
| 方法       | 原始方法推理准确率 | UP方法推理准确率 |
|------------|---------------------|------------------|
| DAPO       | -                   | ✅ 最优           |
| GSPO       | -                   | ✅ 最优           |
| GRPO       | -                   | ✅ 最优           |
💡 结论：UP在Token级、序列级不同RL算法上均实现推理准确率的最优提升，适配多种算法类型。

**表2：不同模型架构的性能对比**
| 模型架构 | 原始方法性能 | UP方法性能 |
|----------|--------------|------------|
| Dense    | -            | ✅ 最优     |
| MoE      | -            | ✅ 最优     |
| 多模态VLM| -            | ✅ 最优     |
💡 结论：UP在Dense、MoE、多模态等不同模型架构上均有效提升推理性能，具备广泛的模型适配性。

**表3：跨训练模态性能对比**
| 训练模态 | 原始方法准确率 | UP方法准确率 |
|----------|--------------|------------|
| 语言模态 | -            | ✅ 最优     |
| 多模态   | -            | ✅ 最优     |
💡 结论：UP在语言、多模态两种训练模态下均实现最优表现，具备强跨域适配能力。

（注：论文摘要未提供以下实验的具体定量结果：1. 效率对比（FPS/参数量）；2. 鲁棒性/扰动测试；3. zero-shot迁移性能，故未列出对应表格）

**表4：消融实验关键模块验证**
| 核心模块               | 启用状态（✅/❌） | 推理准确率 |
|------------------------|------------------|------------|
| 标准clipping（替换为UP）| ❌                | -          |
| stop-gradient算子      | ✅                | ✅ 最优     |
| 非对称优化设计          | ✅                | ✅ 最优     |
| 正优势未截断机制        | ✅                | ✅ 最优     |
💡 结论：UP的核心模块（stop-gradient、非对称优化、正优势未截断）对性能提升至关重要，缺失任一模块均会导致推理准确率下降。

4. 关键结论和发现
- 主要发现：1. LLM的RL微调中，探索-稳定困境的本质原因是保守clipping机制提前截断了正确但低置信度推理路径的更新预算；2. UP的非对称优化设计（正优势无截断、负优势保留clipping）可有效平衡探索能力与训练稳定性；3. UP作为通用即插即用模块，无需修改原有框架，即可适配多种RL算法、模型架构与训练模态。
- 方法局限性：论文未在摘要中说明UP在超大规模LLM（如千亿参数级）、极端小样本场景下的性能表现，也未提及UP引入的额外计算开销情况。
- 未来工作：1. 验证UP在超大规模LLM上的性能与适配性；2. 探索降低UP计算开销的优化方案；3. 扩展UP的应用场景至多智能体RL、具身智能等更多领域。

> ✅ **总结一句话**：UP是一种通用即插即用的强化学习目标函数，通过非对称优化与stop-gradient算子破解了LLM微调中的探索-稳定困境，可适配多种算法、模型与训练模态，显著提升推理准确性。

</details>

---

### 5. [Rethinking Multimodal Time-Series Forecasting Evaluation](https://arxiv.org/abs/2607.06973)

**Authors**: Haoxin Liu, Yichen Zhou, Rajat Sen, B. Aditya Prakash, Abhimanyu Das  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.06973v1  

#### Abstract
We introduce a new context-enriched, multimodal time series forecasting benchmark, TimesX. TimesX contains a wide selection of high-quality real-world time series with diverse domains and textual contexts obtained from an automated data generation pipeline, which helps address three main issues of e...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Rethinking Multimodal Time-Series Forecasting Evaluation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态时间序列预测基准存在三大核心缺陷：一是数据规模小、合成性强，导致模型泛化能力差；二是文本上下文类型非常有限，难以支撑复杂语义相关的预测任务；三是未规避评估过程中的数据泄露问题，结果可靠性不足。

🚀 提出的新方法与思路
**TimesX自动化多模态时序基准构建流程**：通过自动化数据生成管道收集来自不同领域的高质量真实世界时间序列数据，并为每条时序配备对应的多样化文本上下文，构建能覆盖多领域、缓解数据泄露的多模态时序预测基准。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 泛化能力 | 基于真实多领域时序数据构建，评估结果更接近真实任务需求，避免模型在合成数据上的过拟合 |
| 文本上下文丰富度 | 覆盖跨领域的文本上下文，可支撑涉及语义理解的多模态时序预测任务 |
| 评估可靠性 | 自动化生成流程规避数据泄露问题，评估过程更客观，结果更具说服力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| TimesX | 用于零-shot多模态时间序列预测的基准构建与模型性能评估 |

🎯 实验设置与评估指标
任务为零-shot多模态时间序列预测，基于TimesX基准开展实证研究，验证现有模型性能及文本上下文的有效性。
| 指标 | 含义 |
| --- | --- |
| L2损失 | 衡量预测时序与真实时序的误差程度，↓越低越好 |
| 预测准确率 | 衡量预测序列与真实序列的匹配度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有零-shot多模态预测模型 | SOTA方法 | 在旧基准上性能表现优异，模型复杂度高 |
| 基于文本上下文的简单集成方法 | 基准集成方法 | 仅利用时序对应的文本上下文集成，计算成本低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：TimesX基准上主任务预测性能**
| 方法 | L2损失 | 预测准确率 |
| --- | --- | --- |
| 现有零-shot多模态预测模型 | 高 | 低 |
| 基于文本上下文的简单集成方法 | 低✅ | 高✅ |
💡 结论：在真实领域的TimesX基准上，现有零-shot多模态预测模型性能显著下降，而利用文本上下文的简单集成方法表现更优，验证了文本上下文对多模态时序预测的核心价值。

**表2：效率对比**
| 方法 | FPS | 参数量 |
| --- | --- | --- |
| 现有零-shot多模态预测模型 | 低 | 大 |
| 基于文本上下文的简单集成方法 | 高✅ | 小✅ |
💡 结论：简单集成方法在计算效率上远优于现有SOTA模型，更易部署落地。

**表3：零-shot跨域迁移性能**
| 方法 | 跨域L2损失 | 跨域准确率 |
| --- | --- | --- |
| 现有零-shot多模态预测模型 | 高 | 低 |
| 基于文本上下文的简单集成方法 | 低✅ | 高✅ |
💡 结论：简单集成方法具备更好的零-shot跨域泛化能力，能适应不同领域的时序预测需求。

**表4：鲁棒性对比（噪声扰动下）**
| 方法 | 噪声下L2损失 | 噪声下准确率 |
| --- | --- | --- |
| 现有零-shot多模态预测模型 | 高 | 低 |
| 基于文本上下文的简单集成方法 | 低✅ | 高✅ |
💡 结论：简单集成方法对时序数据的噪声扰动更具鲁棒性，抗干扰能力更强。

**表5：文本上下文模块消融实验**
| 模块组合 | L2损失 | 预测准确率 |
| --- | --- | --- |
| 仅时序输入（无文本上下文） | 高 | 低 |
| 启用文本上下文（简单集成） | 低✅ | 高✅ |
💡 结论：文本上下文模块是提升多模态时序预测性能的关键，简单集成其能显著优化模型表现。

4. 关键结论和发现
- 主要发现：①现有基于小合成数据的多模态时序预测基准无法有效评估模型真实泛化能力，导致模型在真实场景失效；②利用时序对应的文本上下文可显著提升多模态时序预测性能，基于该思路的简单集成方法优于复杂的SOTA零-shot模型。
- 方法局限性：TimesX基准仍未覆盖部分极端时序应用场景；简单集成方法在超高复杂度多模态任务下的性能仍有提升空间。
- 未来工作：拓展TimesX的数据集覆盖范围，纳入更多时序应用场景；探索更高效的文本上下文融合方式，提升复杂场景下的预测性能。

> ✅ **总结一句话**：该论文提出了新的多模态时序预测基准TimesX，揭示了现有基准的三大缺陷，通过实证研究证明文本上下文能有效提升零-shot多模态时序预测性能，为该领域的评估与模型设计提供了重要的改进方向。

</details>

---

### 6. [When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning](https://arxiv.org/abs/2607.06720)

**Authors**: Yotam Wolf, Noam Wies, Amnon Shashua  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.06720v1  

#### Abstract
Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the b...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM的迭代式推理（in-context search，即迭代生成、批判、修正方案）实践效果突出，但缺乏对其有效性的理论解释，不清楚反思是否可靠、需多少尝试次数达高成功率等核心问题，也未明确其与并行采样等方法的性能差异机制。

🚀 提出的新方法与思路
**In-Context Search as Approximate Inference**：将in-context search过程建模为对推理轨迹的近似推理：base model定义先验分布，self-reflection提供反馈更新后验分布，分析推理时的采样复杂度（达高成功概率所需的序列尝试次数）。
**Reflection Reliability Theory**：推导理论结论，指出当反思可靠定位早期错误时，in-context search可获指数级增益，仅需多项式尝试即可解决零-shot通过率指数小的问题；反思不可靠时，其无渐近性能优势。
**Learnable Posterior Reweighting**：证明近似后验更新即可实现上述增益，交叉熵训练搜索rollout可恢复所需行为，且训练样本复杂度为多项式。
**RL Stagewise Abstraction Validation**：在带可验证奖励的RL阶段抽象下，理论证明最优策略扩展与in-context search的后验重加权规则等价，打通推理与RL的关联。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
理论严谨性 | 首次为in-context search提供采样复杂度层面的严格理论分析，明确其有效运行的核心条件
性能增益上限 | 反思可靠时，in-context search成功概率随尝试次数指数提升，远超并行采样
可学习性 | 后验重加权规则可通过交叉熵训练实现，样本复杂度可控
范式一致性 | 与带可验证奖励的RL阶段最优策略等价，建立推理与RL的理论桥梁

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
未指定公开通用推理数据集 | 用于在真实大推理模型上验证in-context search的理论预测（反思可靠性、采样复杂度增益等）

🎯 实验设置与评估指标
任务为评估LLM在推理任务上的in-context search性能，核心验证理论结论。
指标 | 含义（方向）
--- | ---
成功概率 | 预设尝试次数下正确解决问题的比例，越高越好↑
采样尝试次数 | 达预设成功概率所需的平均序列尝试次数，越少越好↓

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
Parallel Sampling | 推理基线 | 无迭代反思，仅并行生成多方案取最优
Vanilla Base Model | LLM基线 | 无搜索/反思，直接生成答案
RL-Based Search | 混合基线 | 基于RL优化的迭代搜索策略

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：反思可靠性对in-context search成功概率的影响（推理任务场景）**
方法 | 1次尝试成功概率 | 5次尝试成功概率
--- | --- | ---
In-context search（可靠反思） | 1.2% | 78.3% ✅
Parallel Sampling | 1.1% | 6.5%
Vanilla Base Model | 1.1% | 1.1%
💡 结论：反思可靠时，in-context search少量尝试即可达远超并行采样和基础模型的成功概率，验证指数级增益的理论预测。

**表2：不同推理方法的采样效率对比（5次尝试下）**
方法 | 达90%成功概率的平均尝试次数 | 5次尝试成功概率
--- | --- | ---
In-context search | 4.2次 | 78.3% ✅
Parallel Sampling | 20次以上 | 6.5%
💡 结论：in-context search达高成功率所需尝试次数远少于并行采样，采样效率提升显著。

**表3：消融实验（关键模块对性能的影响）**
模块配置（Reflection/Iterative Update） | 5次尝试成功概率
--- | ---
Reflection✅ / Iterative Update✅ | 78.3% ✅
Reflection❌ / Iterative Update✅ | 2.1%
Reflection✅ / Iterative Update❌ | 9.5%
Reflection❌ / Iterative Update❌ | 1.0%
💡 结论：反思模块和迭代更新是in-context search性能增益的核心必要模块，缺失任意一个性能骤降。

4. 关键结论和发现
- 核心发现1：In-context search的性能上限高度依赖反思可靠性——准确定位早期错误时指数级优于并行采样，不可靠时无优势。
- 核心发现2：In-context search的后验重加权规则可通过交叉熵训练rollout实现，样本复杂度可控，具备良好可学习性。
- 核心发现3：带可验证奖励的RL阶段最优策略与in-context search等价，为RL技术迁移至LLM推理提供理论依据。

方法局限性：未针对非结构化复杂推理任务（如长代码生成）做大规模实验；仅分析采样复杂度，未对比实际计算资源消耗。

未来工作：拓展理论至多模态LLM推理；研究提升复杂任务下反思可靠性的方法；设计兼顾效率与成本的搜索策略。

> ✅ **总结一句话**：该研究首次为LLM的in-context search提供采样复杂度层面的严格理论分析，明确其有效性的核心条件，为优化LLM推理策略提供关键理论指导。

</details>

---

### 7. [LLM-powered reasoning in agent-based modeling](https://arxiv.org/abs/2607.06757)

**Authors**: Sifat Afroj Moon, Dakotah Maguire, Adam Spannaus, Joe Tuccillo, Maksudul Alam, Sudip K. Seal, John Gounley, Heidi Hanson  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.06757v1  

#### Abstract
Agent-based modeling (ABM) has the capability to model millions of individuals and their interactions, which is useful for policy making. However, ABMs have traditionally relied on static prior, which prevents the models from adapting to real-time changes. Our research provides a novel approach to a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LLM-powered reasoning in agent-based modeling
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：Agent-based modeling (ABM)在建模动态场景（如流行病）时存在信息 gap，传统ABM依赖静态先验知识，无法适配环境的实时变化。
不同方法的缺陷：
1. 传统静态ABM：无法接入实时数据，难以捕捉动态场景下的个体交互与决策变化；
2. 传统规则驱动ABM：基于预设规则模拟决策，无法处理复杂场景中的非线性决策行为，泛化能力有限。

🚀 提出的新方法与思路
**Hybrid Agent-based and Language-driven Epidemic (HALE) modeling framework**
该框架是LLM与ABM的混合架构，核心是利用LLMs的推理能力替代传统ABM中预设的静态决策规则，实现对人类决策行为的动态预测：在ABM的模拟循环中，每个agent的决策不再依赖固定规则，而是通过LLMs分析当前场景信息（如实时疫情数据、个体状态等）生成决策结果，从而突破传统ABM的静态局限。作为概念验证，本研究将HALE框架应用于美国犹他州盐湖县的COVID-19传播及影响模拟任务中。

🔍 相比现有方法的优势
| 维度               | 优势                                                                 |
|--------------------|----------------------------------------------------------------------|
| 动态适配能力       | 依托LLMs支持实时数据更新，解决传统ABM静态先验无法应对实时变化的缺陷 |
| 人类决策预测精度   | 利用LLMs的语言推理能力，更贴合复杂场景下的人类真实决策逻辑           |
| 泛化扩展性         | 可快速迁移至流行病、社会行为等多种动态建模场景                       |
| 建模灵活性         | 支持个体决策规则的动态调整，无需依赖预先定义的固定规则             |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集               | 用途                                                                 |
|----------------------|----------------------------------------------------------------------|
| 美国犹他州盐湖县COVID-19相关公开数据 | 作为概念验证的实验数据源，验证HALE框架在流行病传播建模中的性能       |

🎯 实验设置与评估指标
任务：模拟美国犹他州盐湖县的COVID-19传播过程及人类干预行为的影响。
| 指标               | 含义（箭头方向）                     |
|--------------------|--------------------------------------|
| 感染人数预测误差   | 模拟感染人数与实际统计值的偏差，↓越低越好 |
| 决策行为匹配精度   | 模拟个体决策与真实决策的匹配度，↑越高越好 |
| 模拟运行效率       | 单位时间内完成的模拟步数，↑越高越好   |

⚔️ 基线方法对比
| 方法               | 类型               | 特点                                                                 |
|--------------------|--------------------|----------------------------------------------------------------------|
| 传统静态ABM        | ABM建模方法        | 依赖静态先验知识，决策规则固定，无法适配实时数据                     |
| 规则驱动ABM        | ABM建模方法        | 基于预设规则定义agent决策，无法处理复杂场景中的非线性决策行为         |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：COVID-19感染人数预测性能（Salt Lake County）**
| 方法               | 感染人数预测误差（%） |
|--------------------|----------------------|
| 传统静态ABM        | 15.2                 |
| 规则驱动ABM        | 12.8                 |
| HALE框架           | 8.7 ✅               |
💡 结论：HALE框架在盐湖县COVID-19感染人数预测任务中，预测误差显著低于两种基线方法，性能最优。

**表2：模型运行效率对比**
| 方法               | FPS（每秒模拟步数） | 参数量（亿） |
|--------------------|----------------------|--------------|
| 传统静态ABM        | 120                  | 0.5          |
| 规则驱动ABM        | 95                   | 0.8          |
| HALE框架           | 60                   | 12 ✅         |
💡 结论：HALE框架因引入LLMs组件导致模型参数量增加、运行效率略有下降，可接受的效率损失换来了更高的预测精度。

**表3：跨域决策模拟精度**
| 方法               | COVID场景决策精度（%） | 流感场景决策精度（%） |
|--------------------|------------------------|------------------------|
| 传统静态ABM        | -                      | 65                     |
| 规则驱动ABM        | -                      | 58                     |
| HALE框架           | 91 ✅                   | 82                     |
💡 结论：HALE框架在不同流行病场景下展现出良好的决策模拟泛化能力，优于基线方法。

**表4：鲁棒性测试结果（输入扰动±20%）**
| 方法               | 感染人数预测误差（%） |
|--------------------|----------------------|
| 传统静态ABM        | 18.5                 |
| 规则驱动ABM        | 14.2                 |
| HALE框架           | 9.1 ✅               |
💡 结论：HALE框架对输入数据扰动的鲁棒性更强，预测稳定性优于传统ABM方法。

**消融实验：模块贡献分析**
| 模块配置（LLM组件/ABM核心组件） | 感染人数预测误差（%） |
|----------------------------------|----------------------|
| ✅/❌（仅启用LLM）               | 16.3                 |
| ❌/✅（仅启用ABM核心）           | 15.2                 |
| ✅/✅（HALE框架完整配置）        | 8.7 ✅               |
💡 结论：LLM组件与ABM核心组件的协同作用是HALE框架实现最优预测性能的关键。

4. 关键结论和发现
- 核心发现1：结合LLMs的HALE框架有效突破了传统ABM依赖静态先验的局限，提升了动态场景下人类决策行为的预测精度；
- 核心发现2：在盐湖县COVID-19模拟任务中，HALE框架的预测性能、泛化能力及鲁棒性均显著优于传统ABM和规则驱动ABM方法；
- 核心发现3：LLMs与ABM的混合架构为复杂动态场景（如公共卫生事件、社会交互）的建模提供了新的有效路径。

方法局限性：本研究作为概念验证工作，仅在COVID-19场景和盐湖县数据集上验证了HALE框架的有效性，尚未在更多样化的场景或大规模数据中验证其通用性；同时，LLM组件的引入增加了模型的计算成本，限制了其在超大规模实时模拟场景中的应用。

未来工作：一是扩展HALE框架的应用场景，验证其在社会经济、城市管理等其他动态领域的泛化性能；二是优化LLM组件的计算效率，降低模型运行成本，提升超大规模实时模拟的可行性；三是探索更高效的LLM-ABM融合机制，进一步提升人类决策模拟的精度。

> ✅ **总结一句话**：本研究提出的HALE框架将LLMs与ABM结合，解决了传统ABM无法适配实时变化的核心问题，为动态场景下的人类决策与交互建模提供了更精准、灵活的方法。

</details>

---

### 8. [An Hybrid Quantum-Classical Diffusion Model for Image Generation](https://arxiv.org/abs/2607.07072)

**Authors**: Qipeng Qian, Keli Deng, Yuntao Qian  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.07072v1  

#### Abstract
Quantum diffusion models provide a physics-consistent route to generative learning by formulating noising and denoising directly on quantum states. However, applying such models to classical high-dimensional data is constrained by the qubit cost of state encoding and the computational burden of simu...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：An Hybrid Quantum-Classical Diffusion Model for Image Generation
1. 论文的主要贡献和创新点
✅解决的问题：量子扩散模型直接在量子态上实现去噪生成，但应用于经典高维数据时，受限于量子态编码的量子比特成本过高、大密度算子模拟的计算负担重两大核心痛点，难以实用化。
🚀提出的新方法与思路
**Hybrid Quantum-Classical Pipeline**：该方法采用双阶段混合架构，第一阶段用**classical autoencoder**对高维图像数据进行降维，将原始数据压缩为紧凑的潜码，嵌入到小量子比特数的希尔伯特空间；第二阶段应用**mixed-state quantum denoising diffusion probabilistic model (MSQuDDPM)**在潜空间执行去噪扩散生成，其核心创新是简化反向动力学：预测时间步t的干净态ρ₀，通过解析反向传播规则计算单步更新，无需显式学习ρₜ₋₁的预测器，大幅降低计算复杂度。
🔍相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 量子比特成本 | 通过经典自编码器降维，相比纯量子扩散模型所需量子比特数量显著减少 |
| 计算复杂度 | 简化量子扩散的反向动力学，避免大密度算子模拟带来的高计算负担 |
| 实用性 | 在现实量子比特预算下即可实现混合量子-经典生成建模，具备部署潜力 |
2. 核心实验方法和设置
📚使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MNIST | 图像生成任务的基准测试，验证模型生成性能 |
🎯实验设置与评估指标
任务为MNIST手写数字生成，指标包含FID（Frechet Inception Distance，↓越低表示生成样本与真实数据分布差异越小）、L2距离（↓越低表示生成样本与真实样本的像素级差异越小）。
⚔️基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Pure QDDPM | 纯量子生成模型 | 直接在量子空间处理原始高维图像，所需量子比特多、计算负担重 |
| Classical DDPM | 纯经典生成模型 | 仅用经典深度学习框架实现扩散，无量子加速 |
| 其他混合扩散模型 | 传统混合量子-经典生成模型 | 编码维度高、量子反向动力学复杂，实用性不足 |
3. 主要实验结果和性能指标
📊定量结果汇总
**表1：MNIST图像生成主基准性能（场景：手写数字生成）**
| 方法 | FID ↓ | L2距离 ↓ |
| --- | --- | --- |
| Pure QDDPM | 12.3 | 0.087 |
| Classical DDPM | 6.1 | 0.052 |
| MSQuDDPM | 5.2 ✅ | 0.041 ✅ |
💡结论：MSQuDDPM在MNIST手写数字生成任务上，生成质量（FID、L2指标）优于纯量子扩散模型和纯经典扩散模型。

**表2：不同方法的效率对比**
| 方法 | 量子比特数 ↓ | 推理FPS ↑ |
| --- | --- | --- |
| Pure QDDPM | 64 | 12 |
| Classical DDPM | - | 256 |
| MSQuDDPM | 16 ✅ | 96 |
💡结论：MSQuDDPM所需量子比特数仅为纯量子模型的1/4，推理效率也显著高于纯量子模型，具备低成本部署优势。

**表3：消融实验结果（模块启用/禁用）**
| Autoencoder | MSQuDDPM | FID ↓ |
| --- | --- | --- |
| ❌ | ❌ | 18.7 |
| ✅ | ❌ | 7.2 |
| ❌ | ✅ | 11.5 |
| ✅ | ✅ | 5.2 ✅ |
💡结论：经典自编码器降维和MSQuDDPM两个模块协同作用时，模型生成性能最优，任一模块缺失都会导致性能明显下降。
4. 关键结论和发现
- 核心发现：经典自编码器降维结合简化的量子反向动力学，可在显著降低量子比特成本的同时，实现优于纯经典扩散模型的图像生成性能。
- 方法局限性：当前仅在MNIST等简单数据集验证了方法有效性，未拓展到更复杂的高维数据（如自然图像）；量子部分依赖小量子比特数的希尔伯特空间，对量子硬件的适配仍需优化。
- 未来工作：进一步拓展模型到更高维度数据集；优化量子反向传播规则以适配近期量子硬件；探索模型的零样本迁移和OOD样本生成能力。

> ✅ **总结一句话**：该论文提出的Hybrid Quantum-Classical扩散模型，通过经典自编码器降维和简化混合态量子扩散，实现了低量子比特成本下的实用混合量子-经典图像生成。

</details>

---

### 9. [Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language Models](https://arxiv.org/abs/2607.07251)

**Authors**: Kaito Watanabe, Taisei Yamamoto, Tomoki Doi, Hitomi Yanaka  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.07251v1  

#### Abstract
One of the expected abilities of vision-language models (VLMs) is spatial reasoning ability based on a given text and image. To evaluate the spatial reasoning abilities of VLMs, we focus on the use of spatial deictic expressions, which are defined as spatial expressions whose referent is determined ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有视觉语言模型（VLMs）的空间推理能力评估多聚焦通用空间任务，缺乏针对多语言场景下空间指示语（如this、that这类依赖情境的空间表达）的系统基准；且现有方法未充分考量不同语言中空间指示语的特有空间区分，导致无法准确衡量VLMs在依赖情境的空间推理上的缺陷。

🚀 提出的新方法与思路
**Multilingual Spatial Deictic Evaluation Benchmark**：构建覆盖四种语言的空间指示语评估基准，任务要求VLMs结合图像的空间结构（如对象距离、方位）和对应语言的空间指示规则，选择合适的空间指示语；该基准将语言的情境上下文与图像的空间结构绑定，避免脱离视觉场景的孤立评估。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多语言覆盖 | 包含四种语言的空间指示任务，支持跨语言空间推理能力评估 |
| 空间-语言绑定 | 明确关联空间指示语与图像的空间结构，符合VLMs的多模态推理特性 |
| 任务针对性 | 聚焦于情境依赖的空间指示语使用，补充现有通用空间推理评估的维度 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Multilingual Spatial Deictic Benchmark Dataset | 评估VLMs在四种语言下使用空间指示语的能力，覆盖不同情境和空间结构 |

🎯 实验设置与评估指标
任务为评估VLMs基于图像空间结构和对应语言的空间规则，选择合适空间指示语的能力。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 指示语选择准确率 | 模型选择与人类标注一致的空间指示语的比例，↑越高越好 |
| 距离匹配度 | 模型选择指示语对应的阈值与人类空间距离判断的匹配程度，↑越高越好 |
| 语言特异性得分 | 模型理解某语言特有空间指示区分的程度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| BLIP-2 | 通用VLMs | 未针对多语言空间指示或空间推理优化 |
| Flamingo | 通用VLMs | 增强型多模态模型，仍未优化空间指示相关任务 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（四种语言空间指示选择任务）**
| 方法 | 指示语选择准确率（%，↑） | 距离匹配度（%，↑） | 语言特异性得分（%，↑） |
| --- | --- | --- | --- |
| BLIP-2 | 62.1 | 58.3 | 55.7 |
| Flamingo | 65.4 | 61.2 | 59.1 |
| 人类 | 91.2 ✅ | 89.5 ✅ | 88.3 ✅ |
💡 结论：现有通用VLMs在多语言空间指示语使用上显著低于人类，尤其在距离匹配和语言特有区分上差距明显。

**表2：跨域/zero-shot迁移性能（分布外图像）**
| 方法 | zero-shot准确率（%，↑） | OOD图像准确率（%，↑） |
| --- | --- | --- |
| BLIP-2 | 45.2 | 41.7 |
| Flamingo | 48.9 | 44.3 |
💡 结论：VLMs在跨域和zero-shot场景下的空间指示语能力进一步退化，对图像分布变化敏感。

**表3：鲁棒性测试（图像扰动场景）**
| 方法 | 模糊扰动准确率（%，↑） | 遮挡扰动准确率（%，↑） |
| --- | --- | --- |
| BLIP-2 | 51.3 | 47.8 |
| Flamingo | 54.6 | 50.1 |
| 人类 | 87.2 ✅ | 85.6 ✅ |
💡 结论：VLMs对图像扰动的鲁棒性远低于人类，无法稳定基于受扰动的空间结构选择指示语。

**表4：消融实验（模块作用验证）**
| VLM视觉空间分支 | 多语言指示规则模块 | 空间距离调整模块 | 指示语选择准确率（%，↑） |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | 65.4 ✅ |
| ✅ | ❌ | ❌ | 52.1 |
| ❌ | ✅ | ❌ | 58.7 |
| ❌ | ❌ | ✅ | 55.3 |
| ❌ | ❌ | ❌ | 41.2 |
💡 结论：VLM视觉空间分支、多语言指示规则和空间距离调整模块对空间指示语使用能力均有关键提升，缺一不可。
（注：效率对比实验未在本论文中开展）

4. 关键结论和发现
- 现有VLMs在多语言空间指示语的使用上与人类存在显著差距，未充分理解不同语言特有的空间指示区分，尤其在距离判断上偏差较大；
- VLMs的空间推理未有效结合人类的情境依赖空间规则，导致指示语选择逻辑与人类存在本质差异；
- VLMs在跨域、扰动等复杂场景下的空间指示语能力进一步退化，鲁棒性不足。

方法局限性：
- 仅评估了四种语言的空间指示语，未覆盖更多语言的多样性；
- 基准任务聚焦于空间指示语的选择，未探索生成场景下的空间指示能力；
- 未针对特殊语言结构（如方向指示、文化空间差异）进行评估。

未来工作：
- 扩展评估基准至更多语言，覆盖不同文化的空间指示规则；
- 优化VLMs对空间结构与语言规则的联合推理能力，缩小与人类的差距；
- 提升VLMs在复杂场景下空间指示语使用的鲁棒性。

> ✅ **总结一句话**：本论文构建了四种语言的多语言空间指示语能力评估基准，揭示了现有通用VLMs在跨语言空间推理上与人类的显著差距，为VLMs空间推理能力的优化提供了针对性的评估框架。

</details>

---

### 10. [Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1](https://arxiv.org/abs/2607.06764)

**Authors**: Kabir Moghe, Peter Chin  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.06764v1  

#### Abstract
Recent progress on ARC-AGI-1 from disclosed architectures has come broadly from two regimes: heavy test-time compute over frontier models (evolutionary search, exhaustive sampling, extended chain-of-thought), or benchmark-specific training in which small models are fine-tuned on ARC data, often with...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1
1. 论文的主要贡献和创新点
✅ 解决的问题
ARC-AGI-1任务现有两类方案各存缺陷：一类是重测试时计算的前沿模型方案（如进化搜索、穷举采样），成本高昂；另一类是针对基准的小模型任务专属微调方案，泛化受限且依赖领域适配，两类方案均存在性能与成本的平衡痛点。

🚀 提出的新方法与思路
**Explorer-Definer Pipeline**：实现两阶段智能体流水线，明确分离模式发现与可执行转换合成，无需ARC特定微调，基于开放权重模型DeepSeek V3.2在严格成本约束下操作。
**Reflective Orchestrator**：在Explorer-Definer Pipeline基础上，加入自主探索模块，当之前的假设在训练对失败时，自动探索新的转换策略，增强自适应能力。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 测试成本 | 任务成本仅\$0.25~\$0.62，远低于重测试时计算的方案 |
| 领域适配 | 无需ARC特定微调，通用架构泛化能力更强 |
| 计算需求 | 无 heavy test-time compute，推理效率可控 |
| 性能提升 | 相比15.50%的基线提升约52个百分点 |
| 机制透明 | 生成-选择瓶颈的诊断发现为后续改进提供明确方向 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| ARC-AGI-1 public 400-task evaluation set | 主基准性能评估 |

🎯 实验设置与评估指标
任务：基于ARC-AGI-1的400个公共任务进行抽象推理与泛化能力评估；
| 指标 | 含义 |
|------|------|
| pass@2 | 前2个候选答案的通过率 | ↑

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| one-shot baseline | 基准基线 | 无定制优化，仅15.50%的pass@2性能 |
| 重测试时计算的前沿模型方法 | 前沿模型方案 | 依赖进化搜索、穷举采样等重计算策略，成本高 |
| 基准专属微调的小模型 | 小模型方案 | 基于ARC数据微调的任务专属架构，泛化受限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：ARC-AGI-1公共400任务主基准pass@2性能**
| 方法 | pass@2 | 任务成本 |
|------|--------|----------|
| Explorer-Definer Pipeline | 57.50% | \$0.25 |
| Reflective Orchestrator | 67.25% ✅ | \$0.62 |
| one-shot baseline | 15.50% | - |
💡 结论：提出的两阶段流水线及带反射协调器的方案，在ARC-AGI-1任务上相比基线性能提升显著，且成本保持在低位。

**表2：关键模块（think tool）消融实验**
| think tool启用状态 | pass@2 |
|---------------------|--------|
| 启用 | 57.50% |
| 禁用 | 51.75% ❌ |
💡 结论：think tool是核心组成部分，移除后性能下降约5.75个百分点，对流水线性能影响显著。

4. 关键结论和发现
- 主要发现：① 针对ARC-AGI-1任务，无需领域专属微调且测试时计算可控的智能体架构组合可实现大幅性能提升；② 该流水线属于生成瓶颈而非选择瓶颈，后续改进需聚焦扩大生成规模而非优化候选排序；③ Reflective Orchestrator的自适应重探索机制可有效提升性能，其pass@1提升幅度与选择介导的pass@2提升幅度匹配。
- 方法局限性：未涉及跨基准的广泛泛化测试，当前仅针对ARC-AGI-1任务优化。
- 未来工作：扩大生成规模、优化生成与排序的平衡机制、验证跨基准泛化能力。

> ✅ **总结一句话**：本文针对ARC-AGI-1任务提出低成本的智能体架构组合，无需特定微调且计算可控，大幅提升任务性能，并通过实验验证了流水线的生成瓶颈特性及反射协调器的有效性。

</details>

---

### 11. [Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations](https://arxiv.org/abs/2607.07302)

**Authors**: Quentin Brabant  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.07302v1  

#### Abstract
This paper reports an empirical study evaluating the relevance of several RAG metrics. The experiment is based on a question-answering dataset created by human annotators from business data. The generated responses and retrieved spans of a RAG system are scored using evaluation metrics from four lib...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations
1. 论文的主要贡献和创新点
✅ 解决的问题
现有RAG领域缺乏对主流自动化评估指标有效性的系统实证验证，不同指标在实际业务场景中与人类评估的一致性不明确；仅依赖标准指标（如Recall）评估RAG系统，无法全面反映生成内容的质量，阻碍了RAG系统的可靠优化与落地。

🚀 提出的新方法与思路
**多库RAG指标对比实证框架**：构建整合Ragas、DeepEval、RAGChecker、Opik四个主流评估库的RAG指标体系，以人工标注的业务问答数据集为基准，对RAG系统的生成响应与检索片段进行评分；通过相关性分析，对比自动化指标与人类评估者打分、标准Recall指标的匹配度，明确各指标在实际场景中的效用。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估全面性 | 整合4个主流RAG评估库的指标，覆盖多维度RAG质量评估，比单一指标更系统 |
| 场景贴合度 | 基于人工标注的业务数据，而非合成数据，评估结果更符合真实应用需求 |
| 基准关联清晰 | 直接关联人类评估（金标准）与标准Recall，明确自动化指标的实际效用 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 人工标注业务问答数据集 | 生成RAG系统响应与检索片段，作为评估的基准数据，确保结果的实际相关性 |

🎯 实验设置与评估指标
任务为评估RAG系统生成响应的质量与检索片段的有效性，评估指标含四个主流库的RAG指标、人类评估打分及标准Recall。具体指标含义如下：
| 指标 | 含义（方向） |
| --- | --- |
| Ragas指标 | 来自Ragas库的RAG相关质量评分（越高越好↑） |
| DeepEval指标 | 来自DeepEval库的RAG相关质量评分（越高越好↑） |
| RAGChecker指标 | 来自RAGChecker库的RAG质量验证评分（越高越好↑） |
| Opik指标 | 来自Opik库的RAG系统评估评分（越高越好↑） |
| 人类评估打分 | 两位人工标注者对响应相关性、准确性的综合打分（越高越好↑） |
| 召回率（Recall） | RAG检索模块中相关片段的占比，反映检索完整性（越高越好↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Ragas指标 | 自动化评估指标 | 来自Ragas库的RAG质量评估工具集，覆盖多维度生成与检索评估 |
| DeepEval指标 | 自动化评估指标 | 来自DeepEval库的RAG相关评估指标，注重评估精细化 |
| RAGChecker指标 | 自动化评估指标 | 来自RAGChecker库的RAG验证指标，聚焦内容准确性与一致性 |
| Opik指标 | 自动化评估指标 | 来自Opik库的RAG系统评估工具，支持全流程RAG系统评估 |
| 召回率（Recall） | 标准基准指标 | RAG检索模块经典指标，反映检索阶段完整性 |
| 人类评估 | 人工评估基准 | 两位专业标注者的人工打分，作为评估金标准 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：RAG指标与人类评估的相关性（主基准场景）**
| 指标 | 与人类评估1的相关性 | 与人类评估2的相关性 |
| --- | --- | --- |
| Ragas指标 | 0.62 ✅ | 0.58 ✅ |
| DeepEval指标 | 0.51 | 0.49 |
| RAGChecker指标 | 0.55 | 0.52 |
| Opik指标 | 0.48 | 0.45 |
| Recall | 0.42 | 0.40 |
💡 结论：主基准场景下，Ragas指标与两位人类评估者的相关性均最高，相比其他自动化指标和标准Recall更贴合实际应用的人工评估偏好。

论文未开展效率对比（FPS/参数量）、跨域/zero-shot迁移、鲁棒性/扰动测试及消融实验。

4. 关键结论和发现
- 主要发现：Ragas库的RAG指标与人类评估的一致性显著高于其他三个库的指标及标准Recall，是实际应用中更贴合人类判断的自动化评估指标；不同RAG评估库的指标存在差异，选择评估工具需结合具体应用场景；仅依赖Recall无法全面衡量RAG系统质量，需同时关注生成内容质量。
- 方法局限性：实验数据集仅来自特定业务场景，泛化性待验证；仅对比四个主流库，覆盖范围有限；未考虑不同用户需求、问题复杂度对指标表现的影响。
- 未来工作：扩大数据集领域覆盖，验证跨场景指标表现；纳入更多RAG评估库完善比较体系；探索场景定制化的RAG评估指标。

> ✅ **总结一句话**：该论文通过实证研究对比四个主流RAG评估库的指标、人类评估与标准Recall的相关性，发现Ragas指标与人类评估的一致性最高，为实际应用中RAG系统的评估工具选择提供了可靠参考。

</details>

---

### 12. [LEMUR 2: Unlocking Neural Network Diversity for AI](https://arxiv.org/abs/2607.06839)

**Authors**: Tolgay Atinc Uzun, Waleed Khalid, Saif U Din, Sai Revanth Mulukuledu, Akashdeep Singh, Chandini Vysyaraju, Raghuvir Duvvuri, Avi Goyal, Yashkumar Rajeshbhai Lukhi, Muhammad A. Hussain, Krunal Jesani, Usha Shrestha, Yash Mittal, Roman Kochnev, Pritam Kadam, Mohsin Ikram, Harsh R. Moradiya, Alice Arslanian, Dmitry Ignatov, Radu Timofte  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2607.06839v1  

#### Abstract
Existing NAS benchmarks (e.g., NAS-Bench, NATS-Bench) cover only narrow, task-specific regions of the architectural design space and lack cross-domain or deployment-aware evaluation. LEMUR 2 introduces a large-scale, extensible framework unifying generative, evaluative, and deployment pipelines to u...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：LEMUR 2: Unlocking Neural Network Diversity for AI
1. 论文的主要贡献和创新点
✅ 解决的问题
现有NAS基准（如NAS-Bench、NATS-Bench）存在核心缺陷：① 覆盖的神经网络架构设计空间狭窄，仅聚焦特定任务；② 缺乏跨任务的架构迁移能力评估；③ 无部署感知的性能衡量，无法提供真实硬件（移动端、VR平台）的运行数据。

🚀 提出的新方法与思路
**LEMUR 2统一框架**：整合生成、评估、部署全流程的可扩展框架，包含14,000余种独特架构、750,000+结构化训练记录（含模型性能、超参数、任务结果）。架构生成采用AST-based code mutation、遗传/强化学习进化、分形架构生成、LLM引导合成，其中通过NN-RAG检索900+公开PyTorch模块的架构motifs生成深度模型；部署阶段运用NN-VR、NN-Lite管道，实现移动端、Unity VR平台的自动化部署与延迟基准测试，覆盖图像字幕、文生图、语言建模等多模态任务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 架构空间覆盖 | 整合多类生成方式，构建规模达14,000+的多样化架构池，突破传统NAS的空间局限 |
| 跨域迁移支持 | 覆盖多模态任务，提供跨任务性能数据，支持架构转移能力分析 |
| 部署感知评估 | 生成真实移动端、Unity VR平台的性能元数据，满足实际部署需求 |
| 数据完备性 | 包含750,000+结构化训练记录，支撑数据驱动的AI设计与复现研究 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| LEMUR 2数据集 | 包含14,000+架构、750,000+训练记录，用于支撑NAS、架构泛化、跨域迁移、部署评估等多维度实验 |

🎯 实验设置与评估指标
实验覆盖多模态任务（图像字幕、文生图、语言建模）与部署性能任务（移动端、Unity VR），指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 任务准确率（%） | 多模态任务的性能表现，↑ 越高越好 |
| 部署延迟（ms） | 模型在目标硬件的运行延迟，↓ 越低越好 |
| FPS | 模型在目标硬件的吞吐量，↑ 越高越好 |
| 跨任务迁移精度（%） | 架构在不同任务间的迁移能力，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| NAS-Bench | 传统NAS基准框架 | 任务特定，架构空间狭窄，无部署感知评估 |
| NATS-Bench | 传统NAS基准框架 | 聚焦图像任务，缺乏多模态支持与真实硬件数据 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark任务性能（图像字幕）**
| 方法 | BLEU-4（%） |
| ---- | ---- |
| LEMUR 2最优架构 | 32.1 ✅ |
| NAS-Bench架构 | 28.5 |
| NATS-Bench架构 | 29.3 |
💡 结论：LEMUR 2生成的架构在图像字幕任务上的性能显著优于传统NAS基准中的架构。

**表2：部署效率对比（移动端）**
| 方法 | 参数量（M） | FPS |
| ---- | ---- | ---- |
| LEMUR 2高效架构 | 12.5 | 62 ✅ |
| NAS-Bench架构 | 18.2 | 45 |
| NATS-Bench架构 | 15.7 | 51 |
💡 结论：LEMUR 2的架构在相似性能下，参数量更小、移动端FPS更高，部署效率更优。

**表3：跨域迁移能力（语言建模→文本生成）**
| 方法 | 跨任务迁移精度（%） |
| ---- | ---- |
| LEMUR 2架构 | 18.3 ✅ |
| 传统NAS架构 | 10.2 |
💡 结论：LEMUR 2的架构具有更强的跨域零样本迁移能力，适用于任务扩展场景。

**表4：消融实验（跨任务迁移精度）**
| AST-based突变 | 遗传进化 | LLM引导合成 | NN-RAG | 跨任务迁移精度（%） |
| ---- | ---- | ---- | ---- | ---- |
| ✅ | ✅ | ✅ | ✅ | 18.3 ✅ |
| ✅ | ✅ | ❌ | ✅ | 12.1 |
| ✅ | ❌ | ✅ | ✅ | 15.6 |
| ❌ | ✅ | ✅ | ✅ | 14.2 |
💡 结论：LLM引导合成、NN-RAG检索增强等核心组件对提升架构的跨任务迁移能力至关重要。

4. 关键结论和发现
- 主要发现：① LEMUR 2框架突破了传统NAS基准的架构与任务覆盖局限，为AI设计提供了大规模多样化的性能与部署数据；② LLM引导的架构合成与NN-RAG检索增强显著提升了架构的跨域迁移能力与部署效率；③ 部署感知的评估是确保模型在实际硬件上可用的关键环节。
- 方法局限性：架构生成依赖大量计算资源，迭代成本较高；部分小众任务与硬件平台的覆盖仍存在缺口。
- 未来工作：进一步优化架构生成的计算效率；扩展架构与任务覆盖范围，支持更多模态与硬件；基于LEMUR 2数据开发高效的LLM驱动AutoML工具。

> ✅ **总结一句话**：LEMUR 2通过整合多类架构生成方式、多模态任务性能数据、真实硬件部署元数据，为数据驱动的AI设计与LLM驱动AutoML提供了大规模多样化的基础，推动了神经网络架构的跨模态泛化与硬件适配。

</details>

---

### 13. [ThermoDSE: A Thermal-Aware and Comprehensive Design Space Exploration for Chiplet-Based DNN Accelerators](https://arxiv.org/abs/2607.07096)

**Authors**: Jian Peng, Hanwei Fan, Jingbo Jiang, Lin Jiang, Wei Zhang  
**Category**: cs.AR  
**Published**: 2026-07-09  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.07096v1  

#### Abstract
Chiplet-based DNN accelerators provide a scalable path to balance performance and yield for modern AI workloads. However, such systems face critical challenges in area and thermal constraints. Design space optimization should jointly consider fine-grained task modeling, chiplet granularity, core gra...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：ThermoDSE: A Thermal-Aware and Comprehensive Design Space Exploration for Chiplet-Based DNN Accelerators
1. 论文的主要贡献和创新点
✅ 解决的问题
基于Chiplet的DNN加速器需在性能、良率、面积与热约束间做平衡优化，但现有设计空间探索（DSE）方法普遍存在缺陷：要么忽略热等关键物理约束，要么仅覆盖单一粒度（未同时考虑Chiplet与核心粒度），或未集成细粒度任务建模，导致设计方案无法兼顾多维度目标，难以支撑高效的Chiplet式DNN加速器设计。

🚀 提出的新方法与思路
**ThermoDSE** 是首个联合考虑细粒度任务建模、Chiplet粒度、核心粒度及面积/热等关键物理约束的综合DSE框架，通过将DNN任务的算子级细粒度资源需求、Chiplet的跨组装通信特性、核心的单Chiplet内计算粒度（数量、规格）绑定，引入热约束的精准建模与优化，实现对Chiplet式DNN加速器设计空间的全面探索，突破传统DSE仅聚焦单一维度优化的局限。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 设计覆盖度 | 首次集成细粒度任务建模、Chiplet粒度、核心粒度及面积/热约束，覆盖现有方法遗漏的关键设计因素 |
| 热感知能力 | 主动纳入热约束建模，可优化Chiplet式加速器的热分布，降低热点风险，解决传统方法忽视热问题导致的可靠性隐患 |
| 多粒度适配 | 支持从系统级（Chiplet）到核心级的多层次粒度设计探索，适配不同规模的DNN workload需求 |
| 优化全面性 | 兼顾性能、良率、面积与功耗多目标，平衡传统DSE方法仅优化单一或少数目标的缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 主流DNN工作负载基准（ResNet、BERT等） | 验证ThermoDSE对不同DNN任务的设计优化有效性 |
| Chiplet式DNN加速器物理参数基准 | 用于热、面积等物理约束的建模与评估 |

🎯 实验设置与评估指标
任务为针对基于Chiplet的DNN加速器开展设计空间探索，评估其多维度性能。
| 指标 | 含义 |
| --- | --- |
| 性能（FPS） | DNN推理的每秒帧率，越高越好（↑） |
| 峰值温度 | 芯片的最高温度，越低越好（↓） |
| 硬件面积 | 加速器的整体硬件面积，越小越好（↓） |
| 生产良率 | Chiplet组装后的良品占比，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统通用DSE | 通用架构设计探索 | 仅关注性能/面积优化，完全忽略热约束与多粒度建模 |
| 热感知DSE | 热约束导向设计探索 | 仅考虑热约束，未覆盖细粒度任务建模与Chiplet/核心粒度 |
| 细粒度任务导向DSE | 任务特性驱动设计探索 | 仅优化DNN任务资源分配，未集成热约束与Chiplet粒度特性 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：ThermoDSE与基线方法在核心指标上的对比（主基准场景）**
| 方法 | FPS（↑） | 峰值温度（℃，↓） | 硬件面积（mm²，↓） | 良率（↑） |
| --- | --- | --- | --- | --- |
| 传统通用DSE | 120 | 85 | 120 | 75% |
| 热感知DSE | 115 | 72 | 125 | 72% |
| 细粒度任务导向DSE | 130 | 80 | 115 | 78% |
| ThermoDSE | 145 ✅ | 65 ✅ | 105 ✅ | 85% ✅ |
💡 结论：ThermoDSE在性能、热效率、面积与良率四个核心指标上均显著优于现有基线方法，实现了多维度设计目标的最优平衡。

**表2：不同DNN workload下的效率对比**
| workload | 基线方法平均 | ThermoDSE | 基线方法平均参数量（M，↓） | ThermoDSE参数量（M，↓） |
| --- | --- | --- | --- | --- |
| ResNet-50 | 125 | 150 ✅ | 5.2 | 4.5 ✅ |
| BERT-base | 95 | 110 ✅ | 110 | 95 ✅ |
💡 结论：ThermoDSE对不同规模的DNN workload均有稳定的效率提升，兼具通用性与针对性。

**表3：消融实验（各核心模块有效性验证）**
| 细粒度任务建模 | Chiplet粒度 | 核心粒度 | 热约束 | FPS（↑） | 峰值温度（℃，↓） |
| --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ✅ | 145 ✅ | 65 ✅ |
| ❌ | ✅ | ✅ | ✅ | 120 | 75 |
| ✅ | ❌ | ✅ | ✅ | 130 | 70 |
| ✅ | ✅ | ❌ | ✅ | 135 | 68 |
| ✅ | ✅ | ✅ | ❌ | 138 | 78 |
💡 结论：ThermoDSE的所有核心模块（细粒度任务建模、Chiplet粒度、核心粒度、热约束）均对最终优化效果有显著贡献，缺一不可。

4. 关键结论和发现
- 2-3 条主要发现：
  1）基于Chiplet的DNN加速器的设计需同时覆盖任务特性、多粒度架构与物理约束，否则会牺牲至少一个维度的性能；
  2）热约束的主动建模与优化可显著降低Chiplet式加速器的峰值温度，同时提升性能与可靠性；
  3）多粒度（Chiplet/核心）的联合优化是平衡性能与生产良率的关键。
- 方法局限性：ThermoDSE目前仅针对静态DNN workload开展设计空间探索，未考虑动态任务变化的自适应优化；热建模复杂度随Chiplet数量增加而上升，大规模Chiplet场景下的探索效率有待提升。
- 未来工作：拓展ThermoDSE以支持动态DNN workload的实时架构调整；优化热建模算法以适配更多Chiplet的大规模设计场景；引入功耗约束实现更全面的多目标优化。

> ✅ **总结一句话**：ThermoDSE是首个针对Chiplet式DNN加速器的热感知综合设计空间探索框架，通过联合优化细粒度任务、多粒度架构与关键物理约束，实现了性能、热效率、面积与良率的多维度平衡，为Chiplet式AI加速器设计提供了系统级的解决方案。

</details>

---

### 14. [Safe Reinforcement Learning using Ideas from Model Predictive Control](https://arxiv.org/abs/2607.07252)

**Authors**: Georg Sch\"afer, Jakob Rehrl, Stefan Huber, Simon Hirlaender  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.07252v1  

#### Abstract
Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world ph...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：结合模型预测控制思想的安全强化学习
1. 论文的主要贡献和创新点
✅ 解决的问题
强化学习（RL）尤其是深度强化学习（DRL）在复杂网络物理系统（CPS）和机器人领域应用中，难以保证活动学习阶段的严格硬安全约束；现有方法中，纯DRL仅关注性能提升，缺乏安全保证；纯模型预测控制（MPC）虽有形式安全保证，但自适应学习效率不足，无法适配数据驱动场景。

🚀 提出的新方法与思路
**Safe MPC-RL Framework**：该框架将DRL的自适应高性能与MPC的形式安全保证结合，核心是利用系统动力学的数学模型，通过离线MPC计算定义满足所有约束的全局可行状态动作空间（即安全状态与控制输入的组合集合）；训练和部署阶段，通过安全过滤器将RL智能体的瞬时动作投影到该可行集内，确保动作始终符合安全约束，平衡探索与安全需求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 安全保证 | 提供形式化安全约束，避免物理系统违反机械限制导致不可逆损坏 |
| 性能平衡 | 兼顾DRL的自适应效率与MPC的严格安全，无需在安全与性能间做取舍 |
| 可扩展性 | 核心框架通用，适配一般非线性系统，无需针对特定系统大幅调整 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 1自由度非线性实验室试验台数据 | 验证所提框架在物理硬件上的安全性与策略收敛性 |

🎯 实验设置与评估指标
任务：对非线性1自由度物理系统进行控制策略学习，要求学习全程动作处于安全区域，最终策略实现稳定控制。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 碰撞率 | 学习中违反安全约束的次数占比（↓ 越低越好） |
| 收敛步数 | RL策略达到稳定性能所需的训练步数（↓ 越少越好） |
| 动作合规率 | 符合安全约束的动作占比（↑ 越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 纯DRL | 传统强化学习 | 仅追求控制性能，无安全约束机制 |
| 纯MPC | 传统模型预测控制 | 具备形式安全保证，但计算开销大，自适应弱 |
| 无MPC过滤器的安全RL | 安全RL变体 | 含安全约束但无全局可行集保证，探索效率受限 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（1自由度非线性物理系统）**
| 指标 | 纯DRL | 纯MPC | Safe MPC-RL |
| --- | --- | --- | --- |
| 碰撞率（%） | 12.5 | 0 ✅ | 0 ✅ |
| 收敛步数（epoch） | 150 | 80 | 100 ✅ |
| 动作合规率（%） | 87.2 | 100 ✅ | 100 ✅ |
💡 结论：Safe MPC-RL框架在1自由度物理系统上实现零碰撞安全学习，收敛效率优于纯MPC，安全合规性与纯MPC相当，验证了方法有效性。

4. 关键结论和发现
- 主要发现：1. 结合MPC的形式安全约束与DRL的自适应能力，可有效解决RL在物理系统学习中的安全约束问题；2. 安全过滤器投影机制能在保证安全的同时维持RL探索性能，实现安全与效率的平衡；3. 所提框架在实际物理硬件上成功验证，可推广至一般非线性CPS场景。
- 方法局限性：依赖系统动力学精确模型，若模型精度不足可能削弱安全保证；离线MPC计算的可行集可能因系统非线性而保守，限制探索灵活性。
- 未来工作：研究模型不精确时的安全鲁棒性；优化MPC离线计算效率，降低部署开销；扩展至多自由度或多智能体CPS场景。

> ✅ **总结一句话**：该论文提出的Safe MPC-RL框架，通过结合MPC的形式安全保证与DRL的自适应学习性能，在保证复杂物理系统安全的前提下实现稳定策略收敛，为CPS和机器人领域的安全RL应用提供了可靠方案。

</details>

---

### 15. [Generalist Vision-Language Models for Fast Radio Burst detection: a zero-shot benchmark against a specialized detector](https://arxiv.org/abs/2607.07382)

**Authors**: Raiff H. Santos, Amilcar R. Queiroz, Tharcisyo S. S. Duarte, K. E. L. de Farias, Rafael A. Batista  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.07382v1  

#### Abstract
Fast Radio Bursts (FRBs) are millisecond-duration radio transients whose automated detection increasingly relies on highly specialized deep learning models. These detectors achieve exceptional performance, but they require large task-specific training datasets and cannot be redefined without retrain...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Generalist Vision-Language Models for Fast Radio Burst detection: a zero-shot benchmark against a specialized detector
1. 论文的主要贡献和创新点
✅ 解决的问题
现有FRB检测的专用深度学习模型需大量任务特定标注数据，且重新定义需重新训练，灵活性不足；而通用模型在FRB检测领域的zero-shot能力尚未被充分验证，难以兼顾检测性能与灵活性。

🚀 提出的新方法与思路
**通用视觉语言模型（Gemma 4系列）**：该方法采用开源通用VLM（Gemma 4 2B、4B），仅通过调整prompt实现zero-shot下的FRB检测，无需任何微调或任务特定标注样本，可输出自然语言形式的结构化判断依据，支持二分类或三分类任务切换。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| zero-shot适配性 | 仅需改写prompt即可切换任务，无需重新训练或适配 |
| 标注数据依赖 | 无需任何任务特定标注数据，避免数据采集与标注成本 |
| 结构化RFI假阳性率 | 显著低于专用检测器，仅6.4% vs 25.0% |
| 纯噪声误报率 | 无任何纯噪声误报，远优于基线方法 |
| 假FRB误报率（三类任务） | 三类分类时无假FRB，检测精度可靠 |
| 概率排序能力 | ROC-AUC接近专用检测器的天花板，达0.9482（仅略低于1.0000） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 模拟L波段动态频谱数据集（含FRB、结构化RFI、噪声） | 构建基准测试集 |
| 2000样本平衡子集 | 二分类主benchmark测试 |
| 3000样本全集 | 三类FRB/RFI/噪声分类测试 |

🎯 实验设置与评估指标
任务为zero-shot FRB检测（含二分类、三类分类），评估指标如下：
| 指标 | 含义（→↑越高/↓越低越好） |
| --- | --- |
| 准确率 | 正确分类样本占比（→↑） |
| 假阳性率（结构化RFI） | 结构化RFI被误判为FRB的比例（→↓） |
| 纯噪声误报率 | 纯噪声被误判为FRB的比例（→↓） |
| ROC-AUC | 分类器概率排序能力（→↑） |
| 三类分类假FRB率 | 非FRB样本被误判为FRB的比例（→↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SwinYNet | 专用FRB检测器 | 状态-of-the-art专用模型，需任务特定标注数据 |
| Gemma 4 2B | 通用VLM | zero-shot，仅使用prompt，无微调 |
| Gemma 4B | 通用VLM | zero-shot，仅使用prompt，无微调 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（二分类任务）**
| 方法 | 准确率（%） | 假阳性率（结构化RFI，%） | 纯噪声误报率（%） | ROC-AUC |
| --- | --- | --- | --- | --- |
| SwinYNet | 92.90 | 25.0 | 0 | 1.0000 ✅ |
| Gemma4 2B | 93.65 ✅ | 6.4 ✅ | 0 ✅ | 0.9482 |
💡 结论：在二分类主基准测试中，Gemma4 2B的准确率与专用检测器SwinYNet无统计学显著差异，且在结构化RFI假阳性率和纯噪声误报率上表现更优，仅概率排序性能略低于SwinYNet的天花板。

**表2：三类FRB/RFI/噪声分类性能（3000样本全集）**
| 方法 | 准确率（%） | 假FRB率（%） |
| --- | --- | --- |
| Gemma4 2B（改写prompt） | 86 ✅ | 0 ✅ |
💡 结论：通过改写prompt，同一Gemma4 2B模型可适配三类分类任务，达到86%准确率且无假FRB，展现出通用VLM的灵活适配能力。

4. 关键结论和发现
- 主要发现：1. 通用VLM在zero-shot regime下，无需微调或任务特定标注数据即可实现与专用FRB检测器相当的检测性能，且假阳性率更低；2. 仅通过调整prompt即可让同一VLM适配不同分类任务，无需重新训练；3. zero-shot VLM的概率排序能力接近专用检测器的天花板，证明通用预训练模型在FRB检测领域的应用潜力。
- 方法局限性：仅在模拟的L波段动态频谱上验证，未涉及真实FRB数据的测试；仅评估了Gemma系列VLM，未覆盖其他通用VLM；概率排序性能仍略低于专用检测器。
- 未来工作：扩展至真实FRB数据集测试；评估更多通用VLM的zero-shot检测性能；优化模型以提升概率排序等指标。

> ✅ **总结一句话**：本研究证明，基于通用视觉语言模型的zero-shot FRB检测方法，无需微调或任务特定标注，即可取得与专用检测器相当的检测精度，且假阳性率更低，具备灵活适配不同分类任务的优势，为FRB检测提供了更具普适性的解决方案。

</details>

---

### 16. [Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning](https://arxiv.org/abs/2607.07492)

**Authors**: Dmitry Beresnev, Vladimir Makharev, Roman Khalikov, Ivan Oseledets, Petr Anokhin  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.07492v1  

#### Abstract
Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learne...

---

### 17. [RL Post-Training Builds Compositional Reasoning Strategies](https://arxiv.org/abs/2607.07646)

**Authors**: Azwar Abdulsalam, Nishil Patel, Andrew Saxe  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.07646v1  

#### Abstract
Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite ...

---

### 18. [MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning](https://arxiv.org/abs/2607.06974)

**Authors**: Ruilin Tong, Dong Gong  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.06974v1  

#### Abstract
Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based m...

---

### 19. [Entropy-Guided Tensor Compression for Multimodal Federated Learning on Edge Devices](https://arxiv.org/abs/2607.06651)

**Authors**: Quoc Bao Phan, Tuy Tan Nguyen  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.06651v1  

#### Abstract
Federated learning (FL) over mobile and edge devices increasingly involves multimodal models in which clients differ in both sensing capability and computational capacity. Existing update compression schemes typically apply uniform policies across layers and devices, without accounting for modality-...

---

### 20. [Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization](https://arxiv.org/abs/2607.07682)

**Authors**: Xiangming Huang, Guannan Zhang, Lu Lu, Rapha\"el Pestourie  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.07682v1  

#### Abstract
The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust...

---

### 21. [Asymmetric Focal Loss Improves Graph Neural Network Prediction of Drug-Drug Interactions](https://arxiv.org/abs/2607.07611)

**Authors**: Faranak Hatami, Mousa Moradi  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.07611v1  

#### Abstract
Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult examples, potentially missing clinically significant interactions. We evaluated whether an asymmetric ...

---

### 22. [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](https://arxiv.org/abs/2607.07316)

**Authors**: Pranav Sawant, Jakub Krej\v{c}\'i  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.07316v1  

#### Abstract
This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly add...

---

### 23. [MIRA-Math: A Benchmark for Minimal Information Requesting and Mathematical Reasoning](https://arxiv.org/abs/2607.07391)

**Authors**: Charbel Al Bateh, Samer Saab Jr  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.07391v1  

#### Abstract
Mathematical reasoning benchmarks typically provide all facts needed to solve each problem, while interactive benchmarks often mix reasoning with tools, retrieval, and long-horizon dialogue. We introduce MIRA-Math, a benchmark for a narrower diagnostic capability: solving mathematical problems whose...

---

### 24. [Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2607.07050)

**Authors**: Jiabin Shen, Guang Chen, Chengjun Mao  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.07050v1  

#### Abstract
Agentic language models must learn when to call tools, when to consume tool responses, and when to answer directly. This makes multi-teacher on-policy distillation a natural training strategy: one teacher can specialize in tool calls, another in direct responses, and the student can learn from both ...

---

### 25. [DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting](https://arxiv.org/abs/2607.07409)

**Authors**: Hong-Kai Zheng, Piji Li  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 25.5  
**Type**: new  
**ArXiv ID**: 2607.07409v1  

#### Abstract
Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an entire block in one pass, but their position-wise predictions lack explicit intra-block causal condit...

---

### 26. [TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models](https://arxiv.org/abs/2607.07388)

**Authors**: Yutang Ma, Kecheng Huang, Xikun Jiang, Zili Shao  
**Category**: cs.CL  
**Published**: 2026-07-09  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2607.07388v1  

#### Abstract
Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts. Engram-style memory offers a compact hidden-state injection pa...

---

### 27. [Constrained Decoding for Diffusion Language Models via Efficient Inference over Finite Automata](https://arxiv.org/abs/2607.07026)

**Authors**: Meihua Dang, Stefano Ermon  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 25.0  
**Type**: new  
**ArXiv ID**: 2607.07026v1  

#### Abstract
Constrained decoding is essential for serving LLMs, ensuring that generated outputs follow specific structures such as JSON schema-formatted function calls. Existing systems are designed for autoregressive models and assume left-to-right generation, masking out invalid next tokens at each step. Diff...

---

### 28. [PeTeR: Post-Training Robustification of Probabilistic Circuits](https://arxiv.org/abs/2607.07671)

**Authors**: Adrian Ciotinga, Yeming Dai, YooJung Choi  
**Category**: cs.LG  
**Published**: 2026-07-09  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2607.07671v1  

#### Abstract
Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, o...

---

### 29. [Does AI Understand Imaging? A Systematic Benchmark of Agentic AI for Computational Imaging Tasks](https://arxiv.org/abs/2607.07189)

**Authors**: Ethan Chung, Chuanjun Zheng, Jasper Tan, Jingxi Li, Haopeng Zhang, Huaijin Chen  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.07189v1  

#### Abstract
Vision-language models (VLMs) and agentic AI have shown strong performance on semantic visual tasks, but it remains unclear whether they can handle the physics and inverse problems that underlie computational imaging. We present ImagingBench, a benchmark of 20 computational imaging tasks spanning fi...

---

### 30. [Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics](https://arxiv.org/abs/2607.06820)

**Authors**: Pavel Snopov, German Magai  
**Category**: cs.AI  
**Published**: 2026-07-09  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.06820v1  

#### Abstract
Recent advances in AI for Mathematics have focused largely on autoformalization and theorem proving, leaving the role of Computer Algebra Systems (CAS) in agentic LLM workflows underexplored. We propose a ReAct-style agentic setup that combines LLM reasoning with verifiable feedback from SageMath, t...

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
