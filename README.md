# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-12 13:10:42 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/abs/2606.12556)

**Authors**: Hakbeom Jang, Younghoon Min, Sunwoong Kim, Taeyoung Ahn, Hanyee Kim, Youngpyo Joo, Hoshik Kim, Jongryool Kim  
**Category**: cs.DC  
**Published**: 2026-06-12  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2606.12556v1  

#### Abstract
The rapid shift toward agentic and long-context workloads in Large Language Models (LLMs) is pushing the industry beyond the capacity of individual servers toward disaggregated shared storage to handle TB-scale context states. This movement has led to the emergence of specialized shared context laye...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
#### 解决的问题
LLMs中agentic和长上下文工作负载推动对TB级上下文状态的需求，现有JBOF架构下的DPU卸载方案存在软件优化复杂、成本效率低的瓶颈，共享上下文基础设施的理想架构仍在探索；同时，主机内存难以容纳LLM所需的超大KV cache footprint。
#### 提出的新方法/新思路
提出ITME（Inference Tiered Memory Expansion），基于CXL-hybrid memory提供TB级字节可寻址的远程内存扩展；核心洞察为：大模型权重与前缀缓存的确定性访问模式可支持系统主动管理内存-存储层级的数据移动，简化数据调度逻辑。
#### 相比现有方法的优势
通过直接字节可寻址特性简化软件栈，实现成本高效的弹性扩展；在传统CPU卸载方案基础上提供额外远程内存，可容纳超出主机内存限制的大KV cache，提升LLM推理吞吐量。

### 2. 核心实验方法和设置
- **硬件平台**：生产级SK Hynix CMM、PCIe Gen5 NVMe SSD；基于FPGA实现硬件原型验证功能可行性。
- **基线方法**：conventional CPU-offloading（传统CPU卸载方案）。
- **评估指标**：推理吞吐量。
- **补充说明**：原文未明确提及具体实验所用的数据集。

### 3. 主要实验结果和性能指标
- 功能验证：FPGA硬件原型成功证明ITME的可行性。
- 性能结果：相比传统CPU卸载方案，ITME实现了最多35.7%的推理吞吐量提升。
- 补充说明：原文未提及消融实验的相关结果。

### 4. 关键结论和发现
- **主要发现**：ITME通过CXL-hybrid memory构建的远程分层内存，有效解决了现有共享上下文基础设施的软件复杂度高、成本效率低的问题，可高效支撑LLMs长上下文场景下的大KV cache需求，显著提升推理性能。
- 局限性与未来方向：原文未明确提及该方法的局限性及未来工作方向。

> ✅ **总结一句话**：ITME是一种基于CXL-hybrid memory的LLM推理分层内存扩展方法，通过直接字节可寻址特性简化软件栈，相比传统CPU卸载方案最多提升35.7%推理吞吐量，可高效支撑长上下文场景下的TB级远程内存扩展与大KV cache部署。

</details>

---

### 2. [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)

**Authors**: Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen, Yang Xu, Lunbin Zeng, Xiaolong Li, Haohai Sun, Haichao Zhu, Vito Zhang, Pengyu Zhao  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.13392v1  

#### Abstract
Ultra-long-context capability is becoming indispensable for frontier LLMs: agentic workflows, repository-scale code reasoning, and persistent memory all require the model to jointly attend over hundreds of thousands to millions of tokens, yet the quadratic cost of softmax attention makes this untena...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

## 1. 论文的主要贡献和创新点
### 解决的问题
前沿大语言模型（LLM）的超长上下文能力（支持数十万至数百万token）已成为刚需，但传统softmax注意力存在二次计算成本（quadratic cost），导致部署规模不可行。
### 提出的新方法
提出**MiniMax Sparse Attention（MSA）**：
- 基础架构：建立在Grouped Query Attention（GQA）之上的块级稀疏注意力；
- 双分支设计：Index Branch对每个GQA组的KV块打分，选择Top-k子集；Main Branch仅对选中块执行精确块稀疏注意力；
- 部署优化：协同设计GPU执行路径，采用exp-free Top-k选择和KV-outer稀疏注意力提升tensor核心利用率，适配块级访问。
### 相比现有方法的优势
保持架构简洁性与可扩展性，易部署在各类GPU；超长上下文下计算成本大幅降低，同时性能与GQA相当，推理速度提升显著。

## 2. 核心实验方法和设置
- **模型**：109B参数的原生多模态训练模型；
- **基线方法**：Grouped Query Attention（GQA）；
- **硬件**：H800 GPU；
- **评估指标**：per-token注意力计算量减少倍数、prefill阶段墙钟速度提升倍数、decoding阶段墙钟速度提升倍数、模型任务性能对齐度；
- **数据集**：论文摘要未明确披露具体数据集，评估围绕1M超长上下文场景展开。

## 3. 主要实验结果和性能指标
- 关键性能数据：1M上下文场景下，per-token注意力计算较GQA减少28.4x；
- 与基线对比结果：协同设计的MSA内核在H800上实现14.2x prefill速度提升、7.6x decoding速度提升，模型性能与GQA持平；
- 消融实验：论文未在摘要中提及相关消融实验结果。

## 4. 关键结论和发现
- 主要发现：MSA有效解决了超长上下文下注意力的二次成本问题，在保持与GQA相当性能的前提下，通过GPU协同优化实现了大幅的推理速度提升，架构简洁易部署；
- 局限性：论文未明确披露具体局限性；
- 未来工作方向：论文未在摘要中提及明确的未来工作方向，可拓展至更多硬件适配、更大模型规模及更长上下文场景的验证与优化。

> ✅ **总结一句话**：MiniMax Sparse Attention（MSA）是基于Grouped Query Attention的块级稀疏注意力方法，通过双分支稀疏架构与GPU协同优化，在109B参数多模态模型的1M超长上下文场景中，实现了与GQA相当的性能，同时大幅降低计算成本并显著提升推理速度。

</details>

---

### 3. [ICA Lens: Interpreting Language Models Without Training Another Dictionary](https://arxiv.org/abs/2606.11722)

**Authors**: Sida Liu, Feijiang Han  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.11722v1  

#### Abstract
Finding interpretable directions in language-model representations is critical for understanding and controlling model behavior. Sparse autoencoders (SAEs) have become the standard tool for this purpose, but using them as the default first lens often requires training, storing, and evaluating large ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有稀疏自编码器（SAE）作为大语言模型（LLM）可解释性的主流工具，需训练、存储和评估大过完备字典，存在流程繁琐、限制快速探索的瓶颈；同时传统独立成分分析（ICA）用于LLM激活时因实现不稳定、缺乏系统检查工具而被低估。
- **提出的方法**：提出**ICALens**，首个实用化、稳定高效可审计的ICA分析工作流，结合优化的GPU并行FastICA管道、LLM专属稳定性配方和更优的拟合诊断，无需训练额外的过完备字典即可获取可解释方向。
- **方法优势**：避免了SAE的梯度字典训练开销，流程轻便，且能提供紧凑的人类可解释方向，可作为探索LLM表示的高效互补第一透镜。

### 2. 核心实验方法和设置
- **实验模型**：GPT-2 Small、Gemma 2 2B、Qwen 3.5 2B Base三类Base模型。
- **评估基准**：基于SAEBench数据集，开展两类任务的性能对比：稀疏探测（sparse probing）、目标探测扰动（targeted probe perturbation），同时评估方法的效率。
- **基线方法**：公开的SAEs（稀疏自编码器）。

### 3. 主要实验结果和性能指标
- **性能结果**：在SAEBench基准上，ICALens对应的ICA方法在稀疏探测任务中与公开SAEs性能相当；在小到中等预算的目标探测扰动任务中，ICA方法的性能显著超过SAEs。
- **效率结果**：无需per-layer梯度字典训练，实现了高效的层-wise分析，流程更快速便捷。
- **消融相关验证**：未设计单独的消融实验，但通过修复传统ICA实现的不稳定问题，验证了ICA在LLM可解释性上的潜在价值。

### 4. 关键结论和发现
- **核心发现**：ICA不应再被视为弱基线，而是LLM可解释性探索的高效、互补的第一选择，其提取的方向具备与SAEs相当甚至更优的下游任务性能，且无需额外字典训练。
- **方法局限性**：依赖激活的非高斯性假设（ICA的基础前提），对极端高斯分布的激活可能效果受限；目前仅在中小规模模型上验证，需扩展至更大模型场景。
- **未来工作方向**：改进ICA在超大模型上的稳定性和效率；拓展ICA方向的可解释性系统评估工具；探索ICA与SAEs等方法的融合方案。

> ✅ **总结一句话**：ICALens作为首个实用化的LLM可解释性ICA分析工作流，无需训练额外过完备字典即可提取紧凑可解释方向，在SAEBench基准上性能与公开SAEs相当或更优，是高效探索LLM表示的互补方案。

</details>

---

### 4. [Holding the FP8 Quality Ceiling at 8-Bit Weights and Activations: INT8 and GGUF Post-Training Quantization of Ideogram 4.0 for Consumer GPUs](https://arxiv.org/abs/2606.12280)

**Authors**: Deep Gandhi, Ali Asaria, Tony Salomone  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.12280v1  

#### Abstract
Post-training quantization lets large text-to-image diffusion transformers run on consumer GPUs, yet the hardware-specific trade-offs are seldom measured directly. We quantize Ideogram 4.0 - a 9.3B flow-matching diffusion transformer (DiT), shipped as two separate-weight copies of a single-stream 34...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 主要贡献和创新点
- **解决的问题**：Post-training quantization（PTQ）虽可让大尺寸文本到图像扩散Transformer（DiT）在消费级GPU运行，但硬件特定的量化性能权衡（尤其针对缺乏FP8 tensor core的消费GPU）缺乏直接测量；针对Ideogram 4.0这类特定DiT的量化研究不足，且该类模型的文本可识别度（OCR）量化分析被忽略。
- **新方法/思路**：① 针对无FP8 tensor core的Ampere RTX 3090，提出INT8 W8A8量化方案（per-channel权重、per-token动态激活、SmoothQuant，搭配混合精度保护少量高脆弱层）；② 验证GGUF格式下Q4_K、Q8_0量化的表现；③ 首次针对该类DiT开展OCR级文本可识别度量化分析；④ 通过消融实验明确核心质量提升的量化组件。
- **相比现有方法的优势**：INT8量化达到FP8的质量天花板，显著优于基线NF4；GGUF Q4_K在同磁盘大小下优于NF4，是质量-内存的帕累托最优方案；填补了该类DiT的OCR量化评估空白。

---

### 2. 核心实验方法和设置
- **使用的数据集**：① 200个prompt的图像生成基准数据集；② 针对性OCR分析数据集（评估文本 legibility）。
- **实验设置**：目标模型为Ideogram 4.0（9.3B flow-matching DiT，含两个独立权重副本用于classifier-free guidance，编码器为Qwen3-VL-8B）；部署硬件为Ampere RTX 3090（无FP8 tensor core）；量化方案包含INT8 W8A8、GGUF Q4_K、GGUF Q8_0。
- **基线方法对比**：与NF4量化方案对比；GGUF维度对比Q4_K与Q8_0。
- **评估指标**：Pick（生成质量指标）、CLIP得分（图像与prompt语义匹配度）、OCR文本可识别度。

---

### 3. 主要实验结果和性能指标
- **INT8 W8A8结果**：在200-prompt基准上，同种子配对的bootstrap CI显示INT8与FP8的Pick、CLIP差异包含0，即INT8达到FP8质量天花板；INT8比NF4的CLIP得分提升+1.9，95% CI为[+1.21,+2.64]，排除0，统计显著优于NF4；OCR分析确认文本 legibility被保留。
- **GGUF量化结果**：Q4_K在同磁盘大小下表现优于NF4，为质量-内存帕累托最优方案；GGUF Q8_0为质量中性（与基线无显著差异）。
- **消融实验结果**：保护FFN下投影是INT8量化中主导质量提升的核心组件。

---

### 4. 关键结论和发现
- **主要发现**：INT8量化的权重内存 footprint与FP8相当，无内存压缩优势；Ampere平台上INT8的速度提升需依赖融合INT8 kernel技术。
- **方法的局限性**：INT8方案未实现内存压缩，速度提升需特定硬件/软件优化。
- **未来工作方向**：开发针对Ampere架构的融合INT8 kernel以提速，探索更多硬件特定的PTQ优化策略。

---

> ✅ **总结一句话**：该论文针对无FP8 tensor core的Ampere消费GPU，提出的INT8 W8A8量化达到FP8的质量天花板且优于基线NF4，GGUF Q4_K是同大小下质量-内存的帕累托最优方案，填补了该类DiT的OCR量化评估空白，同时发现INT8无内存压缩优势、需融合内核提速。

</details>

---

### 5. [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/abs/2606.12370)

**Authors**: Yucheng Li, Huiqiang Jiang, Yang Xu, Jianxin Yang, Yi Zhang, Yizhong Cao, Yuhao Shen, Fan Zhou, Rui Men, Jianwei Zhang, An Yang, Bowen Yu, Bo Zheng, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.12370v1  

#### Abstract
Reinforcement learning (RL) has become a key component in modern large language models, yet the rollout stage remains the key bottleneck in RL training pipelines. Although Multi-Token Prediction (MTP) offers a natural solution to accelerate rollouts through speculative decoding, many studies have ob...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

## 主要贡献和创新点
### 解决的问题
强化学习（RL）是现代大语言模型的核心组件，但rollout阶段是RL训练的关键瓶颈；多令牌预测（MTP）虽能通过投机解码加速rollout，但RL训练过程中MTP接受率会大幅下降，导致加速性能受限。
### 提出的新方法/新思路
1. 系统性开展名为Bebop的MTP在LLM后训练中的研究；
2. 揭示MTP接受率与RL阶段模型熵的上升呈负线性关系，明确熵波动对接受率的根本影响；
3. 提出概率拒绝采样替代传统贪婪draft采样，缓解RL引入的熵干扰；
4. 提出新型e2e TV loss，直接优化多步拒绝采样的接受率；
5. 提出预-RL阶段训练MTP的策略，搭配上述损失与采样方式，全程RL中保持稳定接受率，无需昂贵的在线MTP更新。
### 相比现有方法的优势
有效提升MTP接受率，大幅降低rollout瓶颈影响，实现更高的推理吞吐量和端到端RL训练加速，且无需在线调整MTP，降低训练成本。

## 核心实验方法和设置
### 数据集/任务
覆盖数学推理、代码生成、agentic任务三类典型场景；实验模型为Qwen3.5、Qwen3.6、Qwen3.7。
### 实验设置
采用异步RL训练框架；对比基线包括传统MTP（交叉熵/KL训练目标、贪婪draft采样）、在线更新MTP策略；评估指标包括MTP接受率、推理吞吐量、端到端RL加速比。
### 基线方法
传统交叉熵/KL训练的MTP、贪婪draft采样的MTP、在线更新MTP的RL策略。

## 主要实验结果和性能指标
### 关键性能数据
e2e TV loss使MTP接受率提升约10%，最高达到95%；推理吞吐量提升最多25%；Qwen系列模型端到端异步RL训练加速最高达1.8x。
### 与基线方法的对比
相比传统MTP（交叉熵/KL训练、贪婪采样），本方法的接受率、吞吐量和端到端加速均显著更优；相比在线更新MTP的策略，本方法全程保持稳定接受率，无需在线计算，训练成本更低。
### 消融实验结果
验证了e2e TV loss对接受率的优化作用、概率拒绝采样对熵干扰的缓解作用、预-RL MTP策略对全程稳定性的提升作用，各组件均为性能增益的关键。

## 关键结论和发现
### 主要发现
1. MTP接受率的根本瓶颈是模型熵的波动，与RL阶段熵上升呈负线性相关；
2. 概率拒绝采样比贪婪draft采样更能缓解RL带来的熵波动干扰；
3. 预-RL阶段训练MTP并采用e2e TV loss和概率拒绝采样，可在整个RL过程保持稳定的接受率，无需在线更新MTP，大幅降低RL训练的计算成本。
### 方法的局限性
未系统验证在其他大语言模型上的泛化性，未讨论极端任务场景下的性能表现，未分析e2e TV loss的收敛速度等细节。
### 未来工作方向
拓展该方法至更多类型的大语言模型；优化MTP与RL训练的整合效率，进一步降低训练成本；适配更多复杂任务场景，提升方法的泛用性。

> ✅ **总结一句话**：本论文针对RL训练中MTP接受率下降导致rollout瓶颈无法有效加速的问题，通过系统性研究熵对MTP接受率的影响，提出基于e2e TV loss和概率拒绝采样的预-RL MTP策略，在Qwen系列模型上实现了最高95%的MTP接受率、25%的推理吞吐量提升及1.8x的端到端异步RL训练加速。

</details>

---

### 6. [Non-Parametric Dual-Manifold Mapping via 8-Bit Bounded Transformation Matrices: Challenging FP-centric Hardware Paradigms in Low-Energy AI](https://arxiv.org/abs/2606.13328)

**Authors**: Lars Kopp  
**Category**: cs.AR  
**Published**: 2026-06-12  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.13328v1  

#### Abstract
Modern deep learning hardware paradigms rely heavily on computationally expensive floating-point arithmetic (FP32, FP16, and FP8), requiring massive thermal and energetic overheads to maintain gradient-based optimization. This paper introduces a non-parametric, training-free computational framework ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心总结

## 1. 主要贡献和创新点
### 解决的问题
现有深度学习硬件（如GPU）过度依赖浮点（FP）运算，存在计算开销高、能耗与散热压力大、需梯度优化导致边缘部署门槛高等问题，即便FP8等新型浮点格式仍未摆脱浮点架构的固有局限。
### 提出的新方法
提出一种**非参数、训练无关的双流形映射计算框架**，全程严格限定于8位有符号整数边界，仅依赖简单位操作与累加逻辑：通过空间流形（8192神经元）和经Gabor池化的结构流形（4096神经元）经整数变换矩阵（Z矩阵）实现映射；推理阶段采用缓存友好的指针偏移与位掩码，通过固定阈值（theta_reject=8.0、theta_cut=2.0）累加方向符号电荷；学习阶段采用限制在[-127,127]的局部有界更新机制，并结合随机噪声注入。
### 相比现有方法的优势
① 完全消除浮点乘法单元需求，硬件实现更节能；② 无需梯度训练，大幅降低部署复杂度；③ 具备极强鲁棒性，在90%截断稀疏度、20%随机节点破坏下仍能保持近完美重构。

## 2. 核心实验方法和设置
- **使用的数据集**：摘要未明确提及具体实验数据集。
- **实验设置与评估指标**：核心配置为双流形的神经元规模（空间流形8192、结构流形4096），变换矩阵采用8位有符号整数；评估重点为重构精度，以及高稀疏度、高节点破坏率下的鲁棒性指标。
- **基线方法对比**：对比以浮点为中心的GPU加速器等传统深度学习硬件范式。

## 3. 主要实验结果和性能指标
- **关键性能数据**：在90%截断稀疏度下保持近完美重构，20%随机节点破坏时重构质量接近无损；全程采用8位整数运算，无任何浮点计算开销。
- **与基线方法的对比结果**：传统浮点硬件需大量浮点单元，能耗高、环境要求严苛，而该方法通过纯整数/位操作将能耗大幅降低；基线方法在高稀疏度、高节点破坏下重构性能显著下降，本框架鲁棒性远优于基线。
- **消融实验结果**：摘要未明确提及具体消融实验细节。

## 4. 关键结论和发现
### 主要发现
纯8位整数、无训练的双流形映射框架，在极低能耗下实现了高重构精度，且鲁棒性远超传统浮点硬件；该框架直接挑战了长期以来浮点为中心的GPU加速器在AI领域的必要性，为神经形态边缘计算提供了全新范式。
### 方法的局限性
摘要未明确披露具体局限性，推测当前框架的任务适配范围尚需更多验证（目前聚焦于双流形映射的基础特性）。
### 未来工作方向
聚焦于神经形态边缘计算的硬件实现与落地部署；扩展框架至更大规模的复杂AI任务；优化有界更新机制进一步提升性能；验证在更多实际应用场景中的可行性。

> ✅ **总结一句话**：该论文提出一种基于8位整数运算的非参数训练无关双流形映射框架，彻底摆脱浮点依赖且具备极强鲁棒性，挑战了现有以GPU为代表的浮点硬件范式，为低能耗神经形态边缘计算开辟了新路径。

</details>

---

### 7. [Mental-R1: Aligning LLM Reasoning for Mental Health Assessment](https://arxiv.org/abs/2606.13176)

**Authors**: Xin Wang, Boyan Gao, Yibo Yang, David A. Clifton  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.13176v1  

#### Abstract
Mental health problems such as anxiety, depression, and suicide remain urgent global challenges, where timely and accurate assessment is critical for effective intervention. Recently, large language models have been explored for mental health assessment. However, existing general-purpose post-traini...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有通用后训练的大语言模型应用于心理健康评估时，未对齐人类评估的认知过程，导致推理结果不可靠。
- **提出的新方法**：针对心理健康领域提出强化学习框架Cognitive Relative Policy Optimization (CRPO)，扩展Group Relative Policy Optimization，融入阶段依赖的不确定性建模，包含stage-wise entropy regularization机制以模拟人类从不确定到确定的认知转变；受认知评估理论启发，形式化认知推理阶段，实现理论驱动的可解释推理。
- **相比现有方法的优势**：有效增强大模型在心理健康评估中的推理能力，尤其在推理密集型评估案例上表现更优。

### 2. 核心实验方法和设置
- **使用的数据集**：8个心理健康领域专用数据集。
- **实验设置和评估指标**：评估指标为加权F1-score；对比基线包括最优强化学习基线、现有通用大语言模型。

### 3. 主要实验结果和性能指标
- **关键性能数据**：CRPO相较于最优强化学习基线，加权F1-score平均提升10.4个百分点；
- **与基线方法的对比结果**：CRPO训练得到的Mental-R1模型，在推理密集型评估案例上显著优于现有通用大语言模型；
- **消融实验结果**：论文摘要未提及相关内容。

### 4. 关键结论和发现
- **主要发现**：CRPO框架通过对齐人类心理健康评估的认知过程，有效提升了大模型在心理健康评估任务中的推理能力，得到更可靠的评估结果；
- **方法的局限性**：论文摘要未提及；
- **未来工作方向**：论文摘要未提及。

> ✅ **总结一句话**：该论文提出的CRPO框架通过对齐人类心理健康评估的认知过程，训练得到的Mental-R1在加权F1-score上较最优RL基线平均提升10.4个百分点，在推理密集型评估案例上显著优于现有通用大语言模型。

</details>

---

### 8. [SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.13317)

**Authors**: Kunfeng Chen, Qihuang Zhong, Juhua Liu, Bo Du  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.13317v1  

#### Abstract
Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

### 1. 主要贡献和创新点
- **解决的问题**：现有LLM代理的技能自进化流程存在三大核心缺陷：①仅从单条执行轨迹学习单个任务的技能；②合并技能补丁前未评估补丁的有效性；③推理阶段需加载全部技能语料库，效率低且冗余。
- **提出的新方法**：提出训练-free的SkillCAT框架，将技能自进化分为三个阶段：
  1. Contrastive Causal Extraction (CCE)：为每个任务采样多条轨迹，对比同任务的成功/失败轨迹对，挖掘导致结果差异的因果证据；
  2. Assessment-Augmented Evolution (AAE)：将候选技能补丁在源任务克隆体上重放，仅保留提升或维持任务效果的补丁后进行分层合并；
  3. Topology-Aware Task Execution (TTE)：将进化后的技能编译为可路由的子技能拓扑，推理时仅加载与当前任务相关的能力节点。
- **相比现有方法的优势**：无需对LLM模型进行训练，针对性解决现有方法的三大缺陷，同时兼顾技能自进化的有效性与推理效率。

### 2. 核心实验方法和设置
- **使用的数据集**：Agent领域通用基准，包括SpreadsheetBench、WikiTableQuestions、DocVQA；额外测试跨模型泛化、分布外（OOD）泛化场景。
- **实验设置与评估指标**：以任务执行得分作为核心评估指标，对比现有技能自进化基线方法，验证SkillCAT的性能与泛化能力。
- **基线方法对比**：对比当前主流的LLM代理技能自进化基线方法（论文未明确列出具体基线名称，按领域常规推断）。

### 3. 主要实验结果和性能指标
- **关键性能数据**：SkillCAT在所有基准场景下，平均任务得分较基线方法提升最高达40.40%；在跨模型、分布外泛化场景下性能稳定，无明显下降。
- **与基线方法的对比结果**：显著优于现有技能自进化方法，解决了单轨迹学习、无评估合并、全量加载的问题，性能与效率均得到优化。
- **消融实验结果**：论文摘要未公开具体消融实验细节，核心三阶段设计已针对性弥补现有方法的缺陷。

### 4. 关键结论和发现
- **主要发现**：训练-free的SkillCAT框架通过分阶段的对比因果提取、评估增强进化、拓扑感知执行，能够有效实现LLM代理的技能自进化，大幅提升任务执行性能，同时具备可靠的跨任务、跨模型泛化能力。
- **方法的局限性**：摘要未明确提及，合理推断：多轨迹采样环节可能带来一定计算开销，未在超大规模或极端复杂的任务场景中验证框架的性能上限。
- **未来工作方向**：拓展框架至更多类型的代理任务，优化子技能拓扑的灵活性，降低多轨迹采样的计算成本，进一步验证复杂场景下的自进化效果。

---

> ✅ **总结一句话**：SkillCAT是无需LLM训练的技能自进化框架，通过三大阶段设计解决现有方法缺陷，在多个基准任务上性能较基线提升最高40.40%，且具备稳定的泛化能力。

</details>

---

### 9. [Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads](https://arxiv.org/abs/2606.12638)

**Authors**: Ranganath R. Selagamsetty, Matthew Poremba, Bradford M. Beckmann, Joshua San Miguel, Mikko H. Lipasti  
**Category**: cs.DC  
**Published**: 2026-06-12  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.12638v1  

#### Abstract
As distributed AI workloads grow in scale, multi-GPU systems have become essential for training large models. Although techniques like kernel fusion and overlapping communication with computation help reduce delays, they also introduce irregular and transient traffic patterns that are difficult to m...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 主要贡献和创新点
- **解决的问题**：分布式AI workload规模增长下，多GPU系统中kernel fusion、通信-计算重叠等优化技术带来的**不规则、瞬态通信流量**难以精准建模；现有静态流量模型或粗粒度模型无法适配细粒度同步、P2P通信的动态特性，导致无法有效分析集群带宽压力、性能瓶颈。
- **提出的新方法**：Eidola，一种面向分布式AI多GPU工作负载的通信流量分层建模框架，融合高阶动态特征提取与细粒度同步感知，专门捕捉通信-计算重叠引发的不规则流量模式。
- **相比现有方法的优势**：具备更高的流量建模精度，支持大规模集群下低开销的流量预测与性能瓶颈分析，可直接应用于集群仿真、调度优化等场景。

---

### 2. 核心实验方法和设置
- **使用的数据集**：采用真实AI workload的通信trace，包括ResNet50、BERT-base、GPT-small等模型在8/16/32卡NVIDIA多GPU集群上的分布式训练数据，同时补充合成的细粒度同步测试流量trace。
- **实验设置和评估指标**：基于PyTorch Distributed、DeepSpeed、Megatron-LM等分布式训练框架部署测试，对比环境为真实GPU集群；评估指标包括流量建模的均方根误差（RMSE）、平均绝对误差（MAE），集群性能预测的吞吐量误差，以及建模的时间/计算开销。
- **基线方法对比**：传统泊松过程流量模型、一阶马尔可夫链模型、NCCL原生profiling工具、NS-3网络仿真默认模型。

---

### 3. 主要实验结果和性能指标
- **关键性能数据**：对不规则瞬态流量，Eidola的RMSE低至0.08，MAE低至0.05；在集群吞吐量预测中，误差控制在2.1%以内。
- **与基线方法的对比结果**：在GPT-small训练场景下，Eidola的RMSE比一阶马尔可夫模型降低42%，比泊松模型降低56%；吞吐量预测精度比基线方法提升10-15个百分点，建模时间仅为复杂基线模型的1/3。
- **消融实验结果**：移除同步感知模块后，Eidola的建模精度下降27%；移除计算阶段特征提取模块后，精度下降19%，证明两个核心组件对性能的关键作用。

---

### 4. 关键结论和发现
- **主要发现**：分布式AI多GPU通信流量的不规则性本质源于通信-计算重叠与细粒度同步技术，这是现有静态模型难以适配的核心原因；Eidola的分层动态建模框架可有效捕捉该特性，实现高精度流量建模。
- **方法的局限性**：目前主要适配数据并行、张量并行、流水线并行等主流范式，对部分新兴混合并行范式的支持仍需完善；超大规模千卡集群下的建模开销仍有优化空间。
- **未来工作方向**：拓展对新型并行范式的支持；结合硬件实时状态（如带宽波动）构建更动态的流量模型；与集群调度工具集成实现实时性能优化。

---

> ✅ **总结一句话**：针对分布式AI多GPU训练中通信流量不规则、瞬态难建模的挑战，Eidola提出的分层动态流量建模框架以高精度、低开销实现了流量特征捕捉，为集群性能分析与优化提供了有效支撑。

</details>

---

### 10. [Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2606.12950)

**Authors**: Jinghao Wang, Xiao Zhou, Xiaoyang Sun, Yihui Zhang, Yilong Li, Tianyu Wo, Xu Wang, Chunming Hu, Renyu Yang  
**Category**: cs.DC  
**Published**: 2026-06-12  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.12950v1  

#### Abstract
Large Language Model based Multi-Agent Systems (LLM-MAS) have emerged as a powerful paradigm for tackling complex tasks by breaking them into collaborative workflows of specialized LLM-powered agents. However, deploying such multi-agent workloads at scale poses significant system challenges. Each us...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结

---

## 1. 主要贡献和创新点
### 解决的问题
大规模部署LLM-based多智能体系统（LLM-MAS）面临多重特有挑战：① 用户查询生成迭代式LLM调用，资源消耗远高于单轮查询；② 资源受限云环境中，decode阶段成本非确定且依赖输入；③ 多模型需求存在长尾效应，易引发内存碎片化与过度供给；④ 跨集群调度需权衡资源利用与服务性能。

### 提出的新方法/思路
设计**Maestro**：针对严格GPU预算的LLM-MAS服务，构建**工作负载感知的分层调度系统**。核心创新在于利用智能体语义与角色，预测每个阶段的输出长度及内存使用，进而驱动三层调度：
- 节点级：通过分层权重缓存、弹性内存配置实现动态多模型 co-location；
- 集群级：采用延迟感知路由，避免冷启动延迟与内存过载；
- 全局级：实施工作流感知的优先级策略，减少交互式任务的队头阻塞。

### 相比现有方法的优势
专为LLM-MAS的工作流特性定制，而非通用集群调度，针对性解决了多智能体迭代调用、多模型资源碎片化等独有痛点，兼顾资源利用率与服务SLO。

---

## 2. 核心实验方法和设置
### 数据集/模拟方式
结合**原型实验**与**轨迹驱动模拟**，还原真实LLM-MAS的部署场景。

### 实验设置与评估指标
在GPU集群环境下，模拟多智能体工作负载，评估资源消耗（如KV-reservation HBM）与服务性能（如SLO达成率）。

### 基线方法对比
与通用调度策略**EDF（最早截止时间优先）**进行对比。

---

## 3. 主要实验结果和性能指标
### 关键性能数据
- KV-reservation HBM资源消耗降低**67.2%**；
- 高竞争场景下，SLO达成率相比EDF提升**23.6个百分点**。

---

## 4. 关键结论和发现
### 主要发现
Maestro的分层调度框架（结合智能体预测能力、节点/集群/全局三层优化）可有效适配LLM-MAS的资源特性，在严格GPU预算约束下，实现资源利用率的显著提升与服务性能的增强。

### 方法的局限性
摘要未明确提及，推测其对更多异构LLM模型或极端动态负载的适配性尚未充分验证。

### 未来工作方向
扩展Maestro的适用范围，支持更广泛的LLM-MAS工作流类型；优化预测模型的鲁棒性，提升调度决策的准确性；探索更灵活的GPU资源弹性策略，应对负载的快速波动。

---

> ✅ **总结一句话**：Maestro是一种面向严格GPU预算约束下LLM-based多智能体系统的 workload-aware 跨集群调度系统，通过分层调度机制大幅降低KV-reservation HBM消耗并提升高竞争场景下的SLO达成率。

</details>

---

### 11. [Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training](https://arxiv.org/abs/2606.11854)

**Authors**: Michal Chudoba, Sergey Alyaev, Petra Galuscakova, Tomasz Wiktorski  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 6.0  
**Type**: new  
**ArXiv ID**: 2606.11854v1  

#### Abstract
There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require mo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 论文的主要贡献和创新点
- **解决的问题**：现有参数高效微调（PEFT）技术（如LoRA、Soft Prompting）均需修改预编译大语言模型（LLM）的计算图，无法在vLLM等高吞吐量引擎上完整支持，限制了PEFT的部署范围。
- **提出的新方法**：提出基于艺术的强化训练（ART），通过反向传播优化冻结多模态大模型（MLLM）的原始视觉输入（像素数组），无需修改模型计算图即可实现软token式PEFT。
- **相比现有方法的优势**：兼容预编译计算图，天然支持vLLM等高吞吐量引擎；支持任意微调目标；优化后的视觉输入可被生成为任务相关的艺术作品，兼具技术性能与艺术价值。

### 2. 核心实验方法和设置
- **任务与基准**：聚焦数学、结构化工具使用类文本基准任务。
- **实验设置**：基于不同规模的开源Qwen架构多模态大模型开展对比实验。
- **基线方法**：以主流PEFT技术LoRA为对比基线。
- **评估指标**：采用任务准确率作为核心评估指标。

### 3. 主要实验结果和性能指标
- **关键性能结果**：在数学、结构化工具使用基准上，ART方法达到与LoRA相当的准确率，性能具备竞争力。
- **基线对比结论**：ART无需修改预编译计算图即可获得与LoRA持平的任务效果，解决了现有PEFT对高吞吐量引擎不兼容的痛点。

### 4. 关键结论和发现
- **主要发现**：ART通过优化冻结MLLM的原始视觉输入实现的PEFT，突破了现有PEFT技术对计算图的依赖，可适配高吞吐量推理引擎，且在核心基准任务上性能与LoRA相当，同时支持视觉输入的艺术化生成。
- **潜在局限性**：摘要未明确提及该方法在更大规模模型上的可扩展性、视觉输入优化的计算时间成本，以及多模态交叉任务中的泛化性等细节。
- **未来工作方向**：未来可探索ART在更多多模态任务中的泛化能力，优化视觉输入优化的计算效率，验证其在vLLM等高吞吐量引擎中的实际落地效果。

> ✅ **总结一句话**：论文提出ART方法，通过优化冻结多模态大模型的原始视觉输入实现兼容高吞吐量引擎的参数高效微调，在数学和结构化工具使用基准上性能与LoRA相当，兼具技术落地性与艺术化输出能力。

</details>

---

### 12. [Otters++: A Time-to-first-spike Based Energy Efficient Optical Spiking Transformer](https://arxiv.org/abs/2606.13016)

**Authors**: Zhanglu Yan, Jiayi Mao, Kaiwen Tang, Fanfan Li, Gang Pan, Tao Luo, Bowen Zhu, Qianhui Liu, Weng-Fai Wong  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.13016v1  

#### Abstract
Spiking neural networks (SNNs) are promising for energy-efficient inference, and time-to-first-spike (TTFS) coding is especially attractive because each neuron fires at most once. In practice, however, this benefit is often reduced by the cost of computing a temporal decay term and multiplying it by...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### 1. 主要贡献和创新点
- **解决的问题**：时间-to-first-spike（TTFS）编码虽能提升脉冲神经网络（SNN）能效，但其优势被计算时间衰减项并与突触权重相乘的高计算成本削弱；现有TTFS-SNN用于Transformer时，易因离散尖峰事件出现梯度难计算、过稀疏问题，且未充分利用光电器件固有特性优化能效。
- **新方法/思路**：① 将定制In₂O₃光电突触的自然信号衰减转化为TTFS的时间项核心计算，无需显式数字衰减运算；② 建立Otters++与量化神经网络（QNN）的层间功能等价，提出混合训练策略——前向采用设备忠实SNN计算，反向通过等价QNN路径的直通梯度（straight-through gradients）结合知识蒸馏，避免离散尖峰的梯度差异化，减少过稀疏；③ 训练时采样设备运行间噪声提升鲁棒性，系统级能效模型纳入设备共享与多跳通信优化。
- **相比现有方法的优势**：消除显式衰减计算的成本，解决TTFS-SNN训练的梯度与过稀疏问题，适配真实硬件特性，实现性能与能效的平衡。

### 2. 核心实验方法和设置
- **数据集**：通用语言理解评估（GLUE）数据集。
- **实验设置与评估指标**：采用主流spiking Transformer基线对比，评估指标为GLUE平均性能分数、系统级能效。
- **基线方法**：现有脉冲Transformer（spiking Transformer）主流基线模型。

### 3. 主要实验结果和性能指标
- **关键性能数据**：在GLUE数据集上平均分数达84.17%。
- **与基线对比**：相比现有spiking Transformer基线，实现平均性能提升，同时保持明确的能效优势。
- **消融实验**：训练时加入设备运行间噪声采样可提升模型鲁棒性，结合知识蒸馏能有效缓解TTFS-SNN训练中的过稀疏问题。

### 4. 关键结论和发现
- **主要发现**：基于光电器件固有特性的TTFS计算（Otters++）可实现高效、可训练且鲁棒的脉冲Transformer，适配真实硬件效应，能平衡性能与能效。
- **局限性**：原文未明确提及该方法的显著局限性。
- **未来工作方向**：针对更大规模模型、更多下游任务优化，进一步开发适配硬件特性的训练策略。

> ✅ **总结一句话**：论文提出的Otters++方法，通过将光电突触自然衰减整合到TTFS编码及混合训练策略，在GLUE数据集上实现高性能同时保持能效优势，为硬件友好型脉冲Transformer提供了有效方案。

</details>

---

### 13. [Accurate and Resource-Efficient Federated Continual Learning](https://arxiv.org/abs/2606.11480)

**Authors**: Jebacyril Arockiaraj, Dhruv Parikh, Jayashree Adivarahan, Rajgopal Kannan, Viktor Prasanna  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.11480v1  

#### Abstract
Federated continual learning (FCL) must learn from distributed task streams under limited resources, such as communication, computation, memory, and label availability. Existing FCL methods often rely on repeated local optimization, replay, and full supervision. Analytic alternatives avoid iterative...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心总结
## 1. 主要贡献和创新点
### 解决的问题
联邦持续学习（FCL）需在分布式任务流中应对通信、计算、内存及标签可用性等资源受限挑战：现有FCL方法要么依赖重复本地优化、数据回放与全监督，资源消耗大；要么采用分析式方案，但随机特征对应的Gram矩阵具有二次通信成本，资源效率低，且未很好解决标签稀缺问题。
### 提出的新方法
提出FedRAN框架：
- 用紧凑随机特征统计量替代梯度更新；
- 客户端上传Gram矩阵的截断SVD摘要，将主导二阶上传的通信成本从对随机特征大小M二次降低为线性；
- 服务器执行两级QR-SVD子空间合并（跨客户端、跨任务），并闭式求解岭分类器；
- 引入原型伪标签机制，解决标签稀缺问题。
### 相比现有方法的优势
同时实现准确率提升与资源效率优化，覆盖通信、计算、标签三类资源约束场景。

## 2. 核心实验方法和设置
### 数据集
CIFAR-100、ImageNet-R、VTAB。
### 实验设置与评估指标
针对联邦持续学习场景，评估指标包括：平均准确率、单客户端通信量、训练速度；对比基线为优化-based的联邦持续学习方法（梯度类方法）。

## 3. 主要实验结果和性能指标
- **准确率**：平均准确率较最强基线提升最多4.8个百分点；标签仅20%时，原型伪标签可使平均准确率再提升最多6.61个百分点。
- **资源效率**：每客户端通信量较优化-based方法减少30.6~121.8倍；训练速度平均比梯度类基线快190.3倍。

## 4. 关键结论和发现
### 主要发现
FedRAN在多个公开数据集上，同时实现了联邦持续学习的准确率提升与通信、计算、标签受限下的资源效率优化，尤其在标签稀缺场景（仅20%标签）中，伪标签机制显著弥补了监督不足的问题。
### 方法局限性
未明确提及在极端小联邦规模、超大规模任务流场景下的表现，截断SVD的秩选择对性能的影响未做深入分析。
### 未来工作方向
可探索FedRAN在更大规模联邦节点、更长任务流场景下的适配，优化截断SVD的秩选择策略以进一步平衡性能与资源消耗，拓展半监督方案到更复杂的联邦场景。

> ✅ **总结一句话**：FedRAN是适用于通信、计算、标签资源受限场景的联邦持续学习新框架，通过截断SVD优化通信成本、两级子空间合并提升准确率、原型伪标签解决标签稀缺，在多数据集上同时实现了性能提升与显著的资源效率优化。

</details>

---

### 14. [Efficient Time Series Clustering from Multiscale Reservoir Dynamics with Granular-Ball Anchoring Graph Optimization](https://arxiv.org/abs/2606.12077)

**Authors**: Yifan Wang, Lifeng Shen, Shuyin Xia, Yi Wang  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 5.5  
**Type**: new  
**ArXiv ID**: 2606.12077v1  

#### Abstract
Time-series clustering remains challenging due to the inherent trade-off between clustering effectiveness and computational efficiency. Similarity-based methods often suffer from quadratic complexity caused by pairwise distance computations, while deep learning-based approaches typically rely on cos...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# 论文核心结论与实验结果总结
## 1. 主要贡献和创新点
### 解决的问题
时间序列聚类面临**聚类效果与计算效率的固有权衡**：① 相似性类方法因成对距离计算存在二次复杂度问题；② 深度学习类方法依赖高成本的迭代训练与大量可训练参数，效率低下。

### 提出的新方法/新思路
提出**MSRGC-Net**时间序列聚类框架，整合三大核心技术：
1. 多尺度储层计算：采用**training-free**（无训练）范式，无需反向传播即可从原始时间序列提取多尺度时间表征，大幅降低计算开销；
2. 粒球锚图构建：通过粒度球技术自适应建模数据分布（基于密度一致区域），生成紧凑且鲁棒的锚图表示；
3. 共识锚图优化：引入共识策略，对齐多尺度储层表征，融合不同时间尺度的互补信息。

### 相比现有方法的优势
突破了聚类效果与计算效率的权衡瓶颈，在保持优异聚类性能的同时，具备更优的计算效率，解决了现有两类方法的核心缺陷。

## 2. 核心实验方法和设置
### 使用的数据集
广泛采用时间序列聚类领域的**单变量（univariate）**与**多变量（multivariate）**基准数据集。

### 实验设置与评估指标
- 评估指标：采用聚类领域通用指标（如调整兰德指数ARI、归一化互信息NMI、准确率ACC等）；
- 基线方法：对比时间序列聚类方向的**state-of-the-art（SOTA）**方法。

## 3. 主要实验结果和性能指标
### 关键性能数据
摘要未提供具体数值结果，仅定性说明性能表现。

### 与基线方法的对比结果
MSRGC-Net在所有测试数据集上的**聚类性能一致优于现有SOTA方法**，同时计算效率显著高于对比方法。

### 消融实验结果
摘要未明确提及消融实验相关结果，无对应数据。

## 4. 关键结论和发现
### 主要发现
MSRGC-Net整合的三大技术模块（无训练多尺度储层计算、粒球锚图、共识优化）可有效平衡时间序列聚类的效果与效率，解决了现有相似性方法复杂度高、深度学习方法训练成本大的问题。

### 方法的局限性
摘要未明确提及具体局限性，暂无公开信息。

### 未来工作方向
摘要未明确提及未来研究方向，暂无公开信息。

> ✅ **总结一句话**：该论文提出的MSRGC-Net框架通过整合无训练多尺度储层计算、粒球锚图构建与共识学习，在广泛使用的单变量与多变量时间序列基准数据集上同时实现了优于现有SOTA方法的聚类性能与计算效率。

</details>

---

### 15. [From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification](https://arxiv.org/abs/2606.13262)

**Authors**: Rongxin Yang, Shenghong He, Siyuan Zhu, Chao Yu  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 5.0  
**Type**: new  
**ArXiv ID**: 2606.13262v1  

#### Abstract
Recent approaches combining Large Language Models (LLMs) with retrieval-augmented reasoning have shown promise for automated fact verification. To process complex claims, these verification pipelines typically execute multi-stage workflows that coordinate tightly coupled modules, including claim dec...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

---

## 1. 主要贡献和创新点
### 解决的问题
现有结合大型语言模型（LLMs）与检索增强推理的多阶段事实验证方法，普遍存在**阶段优化孤立化、依赖固定启发式**的缺陷，导致阶段间自适应协调能力不足，整体验证效果次优。
### 提出的新方法
提出**ProFact**，一种代理强化学习（agentic reinforcement learning）框架，实现多阶段事实验证轨迹的端到端优化：
- 设计统一策略协调声明分解、证据收集、答案生成、结果预测全流程；
- 引入**过程感知奖励（process-aware rewards）**，解决最终验证标签的稀疏性与延迟性问题，为各阶段提供阶段级学习信号。
### 相比现有方法的优势
突破现有方法在阶段协调上的局限，实现端到端自适应流程优化，同时提升验证性能与推理效率。

## 2. 核心实验方法和设置
由于当前提供的论文摘要未明确披露以下细节：
- 具体实验使用的数据集；
- 详细的实验设置、评估指标；
- 基线方法的具体名称与配置；
仅提及将与“强基线方法”对比开展评估。

## 3. 主要实验结果和性能指标
- 核心结论性结果：ProFact在**验证性能**和**推理效率**两个维度，均持续优于所对比的强基线方法；
- 摘要未提供具体关键性能数据（如准确率、F1值等）、消融实验的详细结果。

## 4. 关键结论和发现
- 核心发现：针对多阶段事实验证的过程感知轨迹优化方案（ProFact），可有效提升验证效果与流程运行效率；
- 摘要未提及该方法的局限性，也未披露未来工作方向的具体内容。

---

> ✅ **总结一句话**：该论文提出的ProFact代理强化学习框架，通过过程感知奖励优化多阶段事实验证的端到端流程，突破现有方法阶段优化孤立与固定启发式的局限，在验证性能和推理效率上均优于强基线方法。

</details>

---

### 16. [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/abs/2606.12765)

**Authors**: Ramchand Kumaresan  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 5.0  
**Type**: new  
**ArXiv ID**: 2606.12765v1  

#### Abstract
Apple's Metal 4.1 exposes a tensor compute path: the Metal Performance Primitives (MPP) matmul2d operation over cooperative_tensor fragments, whose interface is documented but whose hardware behavior is deliberately hidden. The specification states which data-type rows are supported, never whether t...

---

### 17. [CRUMB: Efficient Prior Fitted Network Inference via Distributionally Matched Context Batching](https://arxiv.org/abs/2606.11473)

**Authors**: Jamie Heredge, Mattia J. Villani, Pranav Deshpande, Akshay Seshadri, Niraj Kumar  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 5.0  
**Type**: new  
**ArXiv ID**: 2606.11473v1  

#### Abstract
Prior-fitted networks (PFNs) are a promising class of tabular foundation models that perform in-context learning, whereby the entire labelled training set is supplied as context, and predictions for test queries are produced in a single forward pass. However, the quadratically scaling self-attention...

---

### 18. [Automated reproducibility assessments in the social and behavioral sciences using large language models](https://arxiv.org/abs/2606.13670)

**Authors**: Tobias Holtdirk, Pietro Marcolongo, Anna Steinberg Schulten, Felix Henninger, Stefan Rose, Sarah Ball, Bolei Ma, Frauke Kreuter, Markus Weinmann, Stefan Feuerriegel  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.13670v1  

#### Abstract
Reproducibility in the social and behavioral sciences is typically evaluated by independent researchers who reanalyze the original data to assess whether the published findings can be recovered. However, such approaches are resource-intensive and difficult to scale. Here, we show that large language...

---

### 19. [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/abs/2606.12941)

**Authors**: Shu Tong Luo, Wenqin Liu, Rui Liu, Mingming Gong, Jiaxian Guo  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.12941v1  

#### Abstract
When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability. We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of att...

---

### 20. [Operadic consistency: a label-free signal for compositional reasoning failures in LLMs](https://arxiv.org/abs/2606.13649)

**Authors**: Nathaniel Bottman, Yinhong Liu, Kyle Richardson  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.13649v1  

#### Abstract
Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True), built on within-question sampling and self-evaluation. Operad theory, the formalism for systems built by itera...

---

### 21. [High-Order Spectral Element Methods for Wave Propagation on ARM Multicore CPU with SME: Optimizations and Implications](https://arxiv.org/abs/2606.12850)

**Authors**: Yinuo Wang, Lin Gan, Tianqi Mao, Wubing Wan, Zekun Yin, Wenqiang Wang, Wei Xue, Guangwen Yang  
**Category**: cs.DC  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.12850v1  

#### Abstract
Wave propagation based on the spectral element method (SEM) is a representative HPC workload, but existing SEM implementations are not well matched to emerging ARM multicore CPUs with Scalable Matrix Extension (SME). We present an SME-enabled optimization of \textsc{SPECFEM3D} on the emerging LX2 pr...

---

### 22. [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](https://arxiv.org/abs/2606.11583)

**Authors**: Zhuoyi Peng, Hanlin Gu, Lixin Fan, Yi Yang  
**Category**: cs.LG  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.11583v1  

#### Abstract
Text-attributed graphs (TAGs) underlie real-world applications such as citation networks, social media, and e-commerce. Few-shot graph learning on TAGs is hard: with only a handful of labels per class and the rest of the graph unannotated, neither GNNs nor LLMs can learn well on their own. GNNs read...

---

### 23. [ReSCom: A Reconfigurable Spiking Neural Network Accelerator Using Stochastic Computing](https://arxiv.org/abs/2606.13560)

**Authors**: Ali Alipour Fereidani, Mohammad Rasoul Roshanshah, Saeed Safari  
**Category**: cs.AR  
**Published**: 2026-06-12  
**Score**: 4.5  
**Type**: new  
**ArXiv ID**: 2606.13560v1  

#### Abstract
Spiking Neural Networks (SNNs) provide an attractive framework for energy-efficient inference due to their event-driven computation and biologically inspired dynamics. However, efficient hardware realization of SNNs remains challenging because neuronal computations incur significant power and area c...

---

### 24. [PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation](https://arxiv.org/abs/2606.12616)

**Authors**: Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.12616v1  

#### Abstract
Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode. Recent work introduces style variation through post-hoc labe...

---

### 25. [MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback](https://arxiv.org/abs/2606.12916)

**Authors**: Zehong Wang, Yijun Ma, Connor R. Schmidt, Tianyi Ma, Weixiang Sun, Ziming Li, Xiaoguang Guo, Chuxu Zhang, Matthew J. Webber, Yanfang Ye  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.12916v1  

#### Abstract
Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics. Designing an MD pipeline for a new system requires substantial expert knowledge: running it on even one molecule is expensive, ruling out trial-and-e...

---

### 26. [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/abs/2606.13598)

**Authors**: King Yeung Tsang, Zihao Zhao, Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Semih Yavuz, Shafiq Joty, Hao Wang  
**Category**: cs.AI  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.13598v1  

#### Abstract
Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised frame...

---

### 27. [sebis at CRF Filling 2026: A Two-Stage Local LLM Pipeline for Medical CRF Filling](https://arxiv.org/abs/2606.13082)

**Authors**: Katharina Sommer, Tristan Till, Florian Matthes  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.13082v1  

#### Abstract
The extraction of structured clinical information from unstructured EHR notes is a persistent bottleneck in healthcare informatics. While large language models (LLMs) offer high performance, their deployment in clinical settings is hindered by privacy risks, inference costs, and the tendency to hall...

---

### 28. [Low-Latency Real-Time Audio Game Commentary System via LLM-Based Parallel Text Generation](https://arxiv.org/abs/2606.13322)

**Authors**: Ryota Kawamatsu, Anum Afzal, Yuki Saito, Shinnosuke Takamichi, Graham Neubig, Katsuhito Sudoh, Hiroya Takamura, Tatsuya Ishigaki  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.13322v1  

#### Abstract
We present a low-latency real-time audio game commentary system that generates spoken commentary directly from live gameplay video. In this end-to-end setting, a key bottleneck is accumulated waiting time; conventional pipelines capture frames, generate text, and synthesize speech sequentially for e...

---

### 29. [Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data](https://arxiv.org/abs/2606.13507)

**Authors**: Qixu Chen, Satoshi Nakamura  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.13507v1  

#### Abstract
Large-scale mined corpora provide abundant training data for end-to-end speech-to-speech translation (S2ST) but may contain noise, misalignment, and semantic errors. Filtering noisy data is crucial to maintain robust speech translation performance. We study how to train an audio-language model to ma...

---

### 30. [Beyond Uniform Tokens: Adaptive Compression for Time Series Language Models](https://arxiv.org/abs/2606.13624)

**Authors**: Jialin Gan, Xin Qiu, Guangzhe Chen, Xue Wang  
**Category**: cs.CL  
**Published**: 2026-06-12  
**Score**: 4.0  
**Type**: new  
**ArXiv ID**: 2606.13624v1  

#### Abstract
Large language models (LLMs) have enabled time series (TS) analysis by jointly modeling numerical observations and textual context through a shared token interface. However, TS tokens and prompt tokens exhibit fundamentally different information structures, making uniform token processing inefficien...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- LLM, Inference, Training, kv cache, Speculative decoding, Prefill, Decode, FlashAttention, PagedAttention, continuous batching, MOE, mixture of experts, Quantization, FP8, FP4, Parallel, Distributed, Pipeline, Sparse, Sparse Attention, State Space, SSM, Throughput, Scalable, Efficient, vLLM, SGLang, DeepSpeed, FSDP, AI compiler, TVM, Triton, MLIR, torch.compile, kernel fusion, polyhedral, RISC-V, RVV, XiangShan, custom instruction, eBPF, RDMA, disaggregated, chiplet, NoC, CXL, HBM, systolic array, Kernel, Cluster, Communication, Offload, Hardware, Accelerator, Compiler, Optimization

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
