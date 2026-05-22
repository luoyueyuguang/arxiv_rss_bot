# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-22 08:44:02 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling](https://arxiv.org/abs/2605.21603)

**Authors**: Yi Pan, Yile Gu, Jinbin Luo, Yibo Wu, Ziren Wang, Hongtao Zhang, Ziyi Xu, Shengkai Lin, Baris Kasikci, Stephanie Wang  
**Category**: cs.DC  
**Published**: 2026-05-22  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.21603v1  

#### Abstract
Intra-device parallelism addresses resource under-utilization in ML inference and training by overlapping the execution of operators with different resource usage. However, its wide adoption is hindered by a fundamental conflict with the static, sequential programming model of existing frameworks. I...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
现代大规模机器学习模型（如 LLM 和扩散模型）的执行过程中存在显著的**资源利用率不足**问题。不同算子（operator）具有异构的资源瓶颈（compute-bound、memory-bound、network-bound），在传统**静态、顺序执行模型**下，这些算子被串行执行，导致计算单元、内存带宽或网络等资源频繁空闲。

尽管已有多种 **intra-device parallelism** 策略（如重叠计算与通信、kernel fusion、batch splitting）可提升吞吐量，但它们的集成面临两大挑战：
- **工程成本高**：需对现有系统进行侵入式修改，难以复用。
- **策略非普适**：最优策略高度依赖于 workload、模型架构和硬件，需动态选择。

因此，现有框架（如 vLLM、SGLang）难以灵活、透明地集成这些优化。

---

### **提出了什么新方法或新思路**
论文提出 **DynaFlow**，一个支持**透明且灵活集成 intra-device parallelism** 的框架，其核心思想是：

> **解耦逻辑模型定义与物理执行调度**（decoupling the logical model definition from the physical execution schedule）。

具体设计包括：
- **灵活的前端（Frontend）**：
  - 提供基于注解的图划分接口（`SplitModule`, `SplitFunc`, `dynaflow.mark`），将计算图划分为可调度的子图。
  - 提供**可编程调度器接口**（`split`, `get_ready_ops`, `execute`），允许用户以 Python 原生方式定义动态调度策略。
- **高效的后端（Backend）**：
  - 异步管理复杂的控制流与数据流依赖。
  - 自定义内存管理，通过预分配缓冲区实现**零拷贝（zero-copy）数据重分片**。
  - 兼容低级优化（如 CUDA Graphs、TorchInductor），在子图级别应用这些优化。

---

### **相比现有方法的优势**
| 维度 | 传统方法 | DynaFlow |
|------|--------|----------|
| **集成成本** | 高（需上千行侵入式代码） | 极低（平均 <50 LoC） |
| **灵活性** | 固定策略，难以适应不同场景 | 支持动态、条件化调度（如按 batch size 决策） |
| **兼容性** | 破坏原有优化（如 CUDA Graphs） | 保留并兼容现有优化技术 |
| **表达能力** | 单一策略（如仅重叠或仅融合） | 可组合多种策略（如 TokenWeave = 融合 + 重叠） |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **真实对话数据集**：
  - `ShareGPT`：多样化的输入/输出长度。
  - `LMSYS-Chat-1M`：真实世界对话分布。
  - `Splitwise`：长上下文生成任务。
- **合成数据集**：用于固定输入/输出长度的基准测试（如 512 in, 128 out）。

---

### **实验设置和评估指标**
- **硬件平台**：
  - DGX B200（8×B200 GPU，NVLink）
  - H100 集群（4×H100 GPU，NVLink）
  - 部分实验使用 PCIe 模拟低带宽多节点环境。
- **模型**：
  - Llama-3-8B / 70B
  - Qwen-2.5-72B
  - DeepSeek-V2-Lite（MoE）
  - Mixtral
  - Wan-14B（视频生成）
- **评估指标**：
  - **端到端吞吐量**（throughput）：tokens/s 或 seq/s
  - CPU 执行时间（衡量调度开销）
  - 峰值显存占用
  - 初始化时间与 CUDA Graph 内存开销

---

### **基线方法对比**
| 类别 | 基线方法 |
|------|---------|
| **原始系统** | vLLM、SGLang、Megatron-LM、HuggingFace Transformers 等未修改版本 |
| **手工优化实现** | vLLM 内置的 DBO 实现、原始 TokenWeave 框架 |
| **朴素实现** | 固定阈值的 batch splitting（无动态控制） |
| **消融实验** | 移除 CUDA Graph、移除零拷贝内存管理、使用静态调度等 |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**
| 策略 | 集成系统 | 最大吞吐提升 |
|------|--------|------------|
| **NanoFlow** | vLLM | **1.29x** |
| **NanoFlow** | SGLang | **1.19x** |
| **Dual-Batch Overlap (DBO)** | vLLM | **1.14x** |
| **TokenWeave** | vLLM | **1.21x** |
| **TokenWeave** | HuggingFace Transformers | **1.22x** |
| **Comet** | Megatron-LM | **1.27x** |
| **Communication Overlap** | 多系统 | **1.15x** |

> 在低带宽 PCIe 环境下，DBO 吞吐提升高达 **2.06x**，验证了其在通信受限场景的价值。

---

### **与基线方法的对比结果**
- **优于或匹配手工优化实现**：
  - DynaFlow 实现的 DBO 与 vLLM 原生 DBO 性能相当，**部分 workload 下快 1.1x**。
  - DynaFlow 实现的 Comet 完全匹配原生 Comet 分支的性能。
- **显著优于朴素实现**：
  - 朴素 NanoFlow 在轻负载下性能下降至 **0.56x ~ 0.35x**，而 DynaFlow 动态控制避免退化。
- **更低工程成本**：
  - 表 1 显示，集成 DynaFlow 到各系统仅需 **75–144 LoC**。
  - 实现 6 种策略平均仅需 **11 LoC（划分） + 31 LoC（调度）**。

---

### **消融实验结果**
在 Llama-3-8B + vLLM 上的消融研究（baseline = 1.00x）：
| 配置 | 吞吐提升 |
|------|---------|
| **完整 DynaFlow** | **1.14x** |
| 移除 CUDA Graph | 0.96x（下降 16%） |
| 移除零拷贝内存管理 | 1.10x（下降 3.5%） |
| 使用静态调度（无动态控制） | 1.00x（无收益） |

> 结论：**CUDA Graph 和动态调度是性能增益的关键**，零拷贝内存管理也有显著贡献。

---

## **4. 关键结论和发现**

### **主要发现**
1. **解耦调度与模型定义是可行且高效的**：DynaFlow 成功实现了在不修改模型逻辑的前提下，灵活集成多种 intra-device parallelism 策略。
2. **动态调度至关重要**：静态策略在轻负载或小 batch 场景下可能劣化性能，而 DynaFlow 的运行时决策能力避免了这一问题。
3. **低级优化兼容性不可忽视**：CUDA Graph 和 TorchInductor 对掩盖调度开销至关重要，否则 CPU 成为瓶颈。
4. **统一抽象可覆盖多样化策略**：通过 `execute(..., replace_func=...)` 接口，DynaFlow 可表达重叠、融合、分裂等多种模式。

---

### **方法的局限性**
- **初始化开销较高**：
  - CUDA Graph 捕获耗时 **4.3s**（vs vLLM 的 2.4s）
  - CUDA Graph 内存占用 **1.80 GiB**（vs vLLM 的 0.98 GiB）
- **依赖 TorchDynamo**：对某些自定义算子或 autograd 实现的支持有限（如 Megatron-LM 的 fused backward op 无法捕获）。
- **当前主要面向推理**：虽然支持训练，但多数实验集中在推理场景。

---

### **未来工作方向**
- **降低初始化开销**：采用缓存、增量编译或类似 Medusa 的物化技术。
- **扩展至跨设备调度**：将可编程调度思想推广到 multi-node、multi-GPU 场景。
- **自动策略搜索**：结合 profiling 与强化学习，自动选择最优调度策略。
- **支持更多运行时动态性**：如 MoE 中的 conditional computation、动态 batch composition。

---

> ✅ **开源地址**：[https://github.com/uw-syfi/DynaFlow](https://github.com/uw-syfi/DynaFlow)  
> 📄 **论文链接**：[https://arxiv.org/abs/2605.21603](https://arxiv.org/abs/2605.21603)

</details>

---

### 2. [F-TIS: Harnessing Diverse Models in Collaborative GRPO](https://arxiv.org/abs/2605.22537)

**Authors**: Nikolay Blagoev, O\u{g}uzhan Ersoy, Wendelin Boehmer, Lydia Yiyu Chen  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.22537v1  

#### Abstract
Reinforcement learning methods such as GRPO have seen great popularity in LLM post-training. In GRPO, models produce completions to a set of prompts, which are rewarded, and the policy is updated towards the relatively high reward completions. Due to the auto-regressive nature of models, the generat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：F-TIS: Harnessing Diverse Models in Collaborative GRPO

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在基于 **GRPO**（Group Relative Policy Optimization）的大语言模型（LLM）强化学习后训练中，传统方法通常假设所有参与节点使用**同质模型**（homogeneous models），以保持样本尽可能接近 on-policy。然而，在**去中心化系统**中，不同参与者可能拥有计算资源、模型大小、参数量或任务专长各异的异构模型（heterogeneous models）。这种异构性导致生成的样本高度 off-policy，从而损害 GRPO 的收敛性和最终性能。

此外，即使从相同初始模型出发，由于浮点数非结合性等问题，模型也会逐渐漂移，进一步加剧 off-policy 问题。

### 🚀 提出的新方法：F-TIS
本文提出 **Filtered Truncated Importance Sampling (F-TIS)** ——一种适用于异构模型协作训练的 GRPO 风格训练范式。

- **核心思想**：
  - 结合 **Truncated Importance Sampling (TIS)** 来处理 off-policy 样本带来的偏差。
  - 引入 **Filtering 机制**：仅保留优势值 $A_i > 0$ 或 KL 散度低于阈值 $\gamma$ 的样本用于梯度更新，避免低质量或有害的 off-policy 样本干扰训练。
- 公式改进如下：
  $$
  \mathcal{L}_{\text{GRPO}} = \frac{1}{G} \sum_{i=1}^{G} \min\left( R_{i,g} A_{i,g},\ \text{clip}(R_{i,g}, 1-\epsilon, 1+\epsilon) A_{i,g} \right)
  $$
  其中 $R_{i,g} = \frac{\pi_\theta(a_{i,t}|...)}{\pi_{\text{gen}}(a_{i,t}|...)}$ 是重要性权重，且只有当 $A_i > 0$ 或 $D_{KL}(\pi_\theta || \pi_{\text{gen}}) < \gamma$ 时才参与更新。

### ⭐ 相比现有方法的优势
| 方面 | F-TIS 的优势 |
|------|--------------|
| **支持异构性** | 支持不同模型大小、专业知识、可训练参数子集（如 LoRA）的模型协同训练 |
| **通信效率高** | 只需传输每个 token 的 log-probabilities 和 tokens，通信开销仅为 **8 字节/token** |
| **性能对齐 on-policy** | 在多种异构设置下，最终收敛性能与纯 on-policy 训练相当 |
| **泛化能力提升** | 在部分 out-of-distribution 任务上表现优于单独训练，最高提升达 **12%** |
| **稳定性增强** | 过滤机制有效防止模型崩溃（collapse），显著提高训练稳定性 |

---

## 2. 核心实验方法和设置

### 📚 数据集
- **训练数据集**：**GSM8k**（Cobbe et al., 2021）—— 包含小学数学应用题，广泛用于测试 LLM 推理能力。
- **评估数据集（OOD）**：**MATH-500**（Hugging Face H4, 2025）—— 更难的数学推理数据集，用于测试模型在分布外任务上的泛化能力。

### 🔧 实验设置
- **训练方式**：采用 **vertical decentralized RL** 架构，即每个节点负责一组 prompt 的完整 completion 生成。
- **模型组合测试三种异构场景**：
  1. **Model Size Heterogeneity**  
     - Qwen2.5-1.5B 与 Qwen2.5-3B
     - Qwen2.5-Coder-1.5B 与 Qwen2.5-Coder-3B
  2. **Model Expertise Heterogeneity**  
     - Base 模型 vs Coder 模型（具备代码能力）
  3. **Trainable Parameters Heterogeneity**  
     - 使用 LoRA 微调的模型 vs 完整微调模型
- **超参数**（见 Table 1）：
  - 学习率：$1 \times 10^{-6}$
  - Group size：12
  - Batch size：16 或 24
  - Clip 参数 $\epsilon = 0.2$
  - TIS 常数 $C = 2$
  - KL 过滤阈值 $\gamma = 50$

### 🎯 评估指标
- **Pass@1 accuracy**：greedy decoding 下答案完全正确的比例。
- **验证曲线**：每轮迭代在 held-out 验证集上的准确率变化。
- **MATH-500 性能**：衡量 out-of-distribution 泛化能力。

### 🆚 基线方法对比
| 方法 | 描述 |
|------|------|
| **Alone** | 单个模型独立训练（on-policy 基线） |
| **NoIS** | 不使用任何 importance sampling 的异构训练 |
| **VIS**（Vanilla IS） | 使用标准重要性采样 |
| **TIS** | Truncated Importance Sampling |
| **F-NoIS / F-VIS / F-TIS** | 加入 filtering 机制的变体 |

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（来自 Table 2）

| 设置 | 模型 | MATH-500 准确率 |
|------|------|----------------|
| Alone | 1.5B Base | 0.406 |
| Alone | 3B Base | 0.575 |
| F-TIS | 1.5B Base + 3B Base | 0.47 / 0.54 |
| F-TIS | 1.5B Coder + 3B Coder | 0.47 / **0.59** (+1.5pt) |
| F-TIS | 3B Base + 3B Coder | 0.52 / **0.53** |
| F-TIS | 3B PEFT + 3B Base | **0.513 / 0.56** → PEFT 模型提升明显 |

> 注：多个组合中较小或较弱模型通过协作获得显著增益。

### 🔍 与基线方法对比结果
- **Figure 1 & 2**：NoIS 导致严重性能下降；TIS 明显优于 VIS，尤其对大模型更稳定。
- **Figure 3**：引入 filtering 后（F-NoIS），即使无 IS 也能显著改善训练稳定性，接近 on-policy 表现。
- **Figure 4–9**：在各种异构设置下，**F-TIS 实现与单独训练几乎相同的收敛路径和最终精度**。
- **Figure 11**：F-TIS 明显优于 F-VIS，后者早期收敛快但后期泛化差。

### 🔧 消融实验结果
#### （1）过滤阈值 $\gamma$ 的影响（Figure 10）
- $\gamma = 5$ 或 $10$：小模型初期表现更好（因过滤掉过多噪声）。
- $\gamma = 50$：更适合大模型，允许更多探索空间，长期性能最优。
- 最终选择 $\gamma = 50$ 作为平衡点。

#### （2）横向 vs 纵向协作（Figure 12）
- **Horizontal Collaboration**（各节点为所有 prompts 生成部分 completions）：
  - 导致性能下降，尤其是 3B 模型。
  - 原因：advantage 计算跨多个模型，引入偏差，不利于策略更新。
- **Vertical Collaboration 更优**：每个节点独立完成一组 prompts，advantage 计算更一致。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **异构模型协作是可行的**：通过 F-TIS，不同 size/expertise/trainable-parameter 的模型可以在同一 RL loop 中高效协作。
2. **F-TIS 实现 on-policy 级别性能**：在所有测试场景中，F-TIS 达到与单独 on-policy 训练相当的最终准确率。
3. **泛化能力提升**：在 MATH-500 上，某些模型（特别是原本表现较差者）通过协作获得高达 **12% 的相对提升**。
4. **过滤机制至关重要**：单纯使用 IS（如 VIS/TIS）不足以稳定训练，加入 filtering 才能真正解决 off-policy 噪声问题。
5. **PEFT 模型受益更大**：LoRA 类轻量微调模型在与完整模型协作时性能提升最显著，表明 off-policy 样本能提供有益探索信号。

### ⚠️ 局限性
- 当前实验集中在 **two-node vertical setup**，扩展到大规模多节点系统尚未验证。
- Horizontal collaboration 表现不佳，限制了并行效率的最大化。
- 对极端异构情况（如 1B vs 70B 模型）未进行测试。
- 超参数 $\gamma$ 和 $C$ 需经验调整，缺乏自适应机制。

### 🔮 未来工作方向
- 设计 **adaptive filtering thresholds**，根据训练阶段动态调整 $\gamma$。
- 探索 **secure aggregation** 机制，在保护隐私前提下实现去中心化协作。
- 将 F-TIS 扩展至 **multi-task learning** 场景，让不同专家模型专注不同任务。
- 研究如何将 F-TIS 应用于 **fully decentralized autonomous networks**（如区块链驱动的 AI 训练网络）。

---

## ✅ 总结一句话
> **F-TIS 成功实现了异构 LLM 在 GRPO 框架下的高效协作训练，在保持极低通信成本的同时，达到了与 on-policy 训练相当甚至更优的性能，特别是在 out-of-distribution 推理任务上展现出显著泛化优势。**

</details>

---

### 3. [PALS: Power-Aware LLM Serving for Mixture-of-Experts Models](https://arxiv.org/abs/2605.21427)

**Authors**: Can Hankendi, Rana Shahout, Minlan Yu, Ayse K. Coskun  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2605.21427v1  

#### Abstract
Large language model (LLM) inference has become a dominant workload in modern data centers, driving significant GPU utilization and energy consumption. While prior systems optimize throughput and latency by batching, scheduling, and parallelism, they largely treat GPU power as a static constraint ra...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：PALS: Power-Aware LLM Serving for Mixture-of-Experts Models

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现代数据中心中，**Large Language Model (LLM) 推理**已成为主导性工作负载，带来巨大的 GPU 利用率和能源消耗。尽管已有系统通过 **batching、scheduling 和 parallelism** 优化吞吐量和延迟，但它们通常将 GPU 功耗视为静态约束，而非可调控资源。

这导致两个核心问题：
- **功耗过度配置**：为满足峰值需求而预留过多功率，造成能源浪费；
- **服务质量（QoS）下降**：在功率受限时无法动态调整，导致吞吐不足和服务违规。

尤其对于 **Mixture-of-Experts (MoE)** 模型，其动态路由机制引入显著的通信开销，在高并行度下容易成为通信瓶颈，传统方法难以有效管理功耗与性能的权衡。

---

### 提出了什么新方法或新思路
本文提出 **PALS**（Power-Aware LLM Serving），一种**将 GPU 功率上限（power cap）作为一级控制变量**的运行时系统，**联合优化硬件级功耗限制与软件级推理参数**（如 batch size、parallelism）。

#### 核心创新点：
- **首次将 power cap 引入 LLM 推理调度循环**，将其与 batch size、TP/EP 等软件参数协同控制，形成跨层联合优化。
- 设计了一个**轻量级闭环控制系统**：
  - **离线建模**：构建 power-performance 预测模型（基于 Random Forest）；
  - **在线反馈控制**：结合预测模型与 PID 控制器，实时校正偏差，适应动态负载变化。
- 支持**动态响应外部信号**，如电网需求响应（demand response）、实时电价、碳感知计算等，实现 **grid-interactive AI**。
- **即插即用设计**：集成到 vLLM 框架中，无需修改模型架构或 inference API，部署成本低。

---

### 相比现有方法的优势
| 维度 | 现有方法 | PALS |
|------|--------|------|
| 控制维度 | 单独优化 batching 或 DVFS | 联合优化 power cap + batch + parallelism |
| 功耗角色 | 外部硬约束 | 可控调度维度 |
| 响应能力 | 静态或粗粒度调整 | 500ms 级细粒度闭环反馈 |
| 效率边界 | 局部最优 | 扩展 Pareto 前沿，逼近 Oracle 性能 |
| 适用场景 | 固定功耗预算 | 动态功耗预算、QoS 约束、多节点集群 |

---

## 2. 核心实验方法和设置

### 使用了哪些模型（非数据集）
PALS 主要评估的是不同 LLM 架构下的推理服务性能，因此实验基于多个代表性模型进行测试，包括：

| 模型类型 | 具体模型 |
|---------|--------|
| **Dense Models** | GPT-2, Llama-2-7B, Mistral-7B |
| **MoE Models** | Mixtral-8x7B, Qwen1.5-MoE, DeepSeek-MoE, Phi-3.5-MoE, OLMoE-1B-7B |

这些模型覆盖了从计算密集型（compute-bound）到通信密集型（communication-bound）的不同行为特征。

---

### 实验设置
- **硬件平台**：多节点服务器，每节点配备 4× NVIDIA A100 GPU，通过 NVLink 互联；
- **软件框架**：基于 **vLLM** 实现，利用 PagedAttention 技术提升内存效率；
- **控制周期**：500ms 进行一次 telemetry 采集与配置更新；
- **功耗测量**：使用 NVML 获取 GPU 功耗，并通过 IPMI 校准系统总功耗；
- **工作负载模拟**：采用泊松到达过程生成请求流，模拟真实 LLM 服务中的突发性流量。

---

### 评估指标
| 指标 | 定义 |
|------|------|
| **Tokens/J** | 每焦耳能量处理的 token 数，衡量能效 |
| **Throughput (tokens/s)** | 系统整体吞吐量 |
| **QoS Violation Rate** | 未达到目标吞吐阈值的时间占比 |
| **Power Tracking Error** | 实际功耗与目标功耗之间的偏差 |
| **Normalized Efficiency** | 相对于 baseline 的能效提升倍数 |

---

### 基线方法对比
| 基线方法 | 描述 |
|--------|------|
| **Baseline** | 固定 400W 功耗上限 + 最大 batch size（64），无动态调节 |
| **Adaptive Batch** | 固定功耗上限，仅动态调整 batch size |
| **Adaptive Cap** | 固定 batch size，仅动态调整功耗上限 |
| **Oracle** | 离线穷举搜索所有配置，获取理论最优解（用于上界参考） |
| **PALS** | 联合调整 power cap 与 batch size，带反馈控制 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据
#### ✅ 单节点能效提升（图7）
- PALS 在平均五个 MoE 模型上实现了 **26.3% 的能效提升**（tokens/J ↑）；
- 达到 Oracle 性能的 **95%**，接近理论最优；
- 相比仅调 batch 或仅调 power cap，均有明显优势。

#### ✅ 多节点 QoS 违规减少（图9a）
在三节点、总功耗限制为 4800W 的场景下：
- Baseline 的 QoS 违规率为 **18.7% ~ 35.2%**；
- PALS 将违规率降至 **3.2% ~ 5.3%**；
- 实现 **4× ~ 7× 的 QoS 改善**。

#### ✅ 能源效率提升（图9b）
- 在多节点受限场景下，PALS 提升聚合能效 **12.1%**。

#### ✅ 动态需求响应表现（图10）
在模拟电网 demand response 场景中：
- PALS 能精确跟踪动态功率信号；
- 在低功耗目标下，相比静态 batch 方法，**吞吐量最高提升 22%**；
- 说明其能根据可用算力动态调整 batch size，避免资源闲置。

---

### 消融实验结果
#### 🔍 功耗上限存在“收益递减”现象（图1a）
- 对于 **通信受限模型**（如 Qwen-MoE、OLMoE），超过约 **200W 后 tokens/J 开始下降**；
- 原因：额外功耗主要用于加速 NCCL all-to-all 通信，而非有效计算；
- 表明盲目拉满 GPU 功耗反而降低能效。

#### 🔍 Batch size 是主导因素（图1b）
- 所有模型中，batch size 从 1 增加到 64，能效提升 **1.7× ~ 2.1×**；
- 原因：摊销 kernel launch、attention 计算、通信建立等固定开销；
- MoE 模型受益更大，因其还摊销了专家路由开销。

#### 🔍 并行策略影响最优功耗点（图2 & 图5）
- 高 Tensor Parallelism (TP) 下，通信占比上升，系统更易进入通信瓶颈；
- 此时更低的 power cap 更优；
- 表明 **最优配置依赖 compute-communication ratio**，需动态决策。

#### 🔍 联合控制扩展 Pareto 前沿（图3）
- “HW only”（仅调 power cap）和 “SW only”（仅调 batch/TP）的 Pareto 曲线互不重叠；
- 联合控制（HW+SW）严格支配两者，填补中间空白区域；
- 对 Mixtral-8x7B，联合优化使前沿效率提升 **1.18×**。

---

## 4. 关键结论和发现

### 主要发现
1. **GPU 功耗不应是静态约束，而应是一级调度维度**；
2. **独立优化硬件（DVFS）或软件（batching）均次优**，必须联合控制才能逼近最优效率；
3. **MoE 模型对通信敏感**，增加功耗可能加剧通信瓶颈，反而降低能效；
4. **batch size 是最有效的能效杠杆**，其次是 power cap，最后是 parallelism；
5. **动态闭环控制至关重要**：离线模型提供初始建议，反馈控制器补偿建模误差和负载波动；
6. **PALS 可支持 grid-interactive AI**，响应外部电力信号，推动绿色 AI 发展。

---

### 方法的局限性
1. **仅支持 runtime 可调参数**：如 power cap 和 batch size；TP/EP/DP 需部署前确定，无法在线切换；
2. **预测模型依赖离线剖面**：若线上 workload 分布发生剧烈偏移（如极长 prompt、异常输出长度），可能导致误判；
3. **节点级控制**：未解决跨节点的任务迁移或重调度问题，需与集群调度器（如 DynamoLLM）配合使用；
4. **PID 控制器不能预测突变**：只能纠正稳态误差，对突发负载变化反应有限。

---

### 未来工作方向
1. **引入轻量在线学习机制**：持续更新预测模型，增强对分布漂移的鲁棒性；
2. **不确定性感知控制**：让控制器考虑预测置信度，避免高风险切换；
3. **扩展至 cluster-level**：与 DynamoLLM 类系统协同，实现“集群定预算、节点定策略”的分层控制；
4. **支持更多硬件控制**：如 GPU frequency、memory clock、NVLink throttling；
5. **探索碳感知调度**：结合区域电网碳强度信号，实现 truly sustainable AI serving。

---

> **总结一句话**：  
> PALS 首次将 **GPU power cap** 提升为 LLM 推理调度的一等公民，通过 **软硬协同闭环控制**，在不影响 QoS 的前提下大幅提升能效，为构建 **energy-proportional、grid-interactive 的 AI 服务体系**提供了实用路径。

</details>

---

### 4. [LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation](https://arxiv.org/abs/2605.22054)

**Authors**: Zhuo Chen (equal contribution), Xinzhe Yuan (equal contribution), Jianshu Zhang (Shanghai Artificial Intelligence Laboratory, Shanghai, China, School of Computer Science, Shanghai Jiao Tong University, Shanghai, China), Jinzong Dong (Shanghai Artificial Intelligence Laboratory, Shanghai, China, School of Automation, Central South University, Changsha, China), Ruichen Zhou (College of New Energy and Materials, China University of Petroleum, Beijing, China), Yingchun Niu (College of New Energy and Materials, China University of Petroleum, Beijing, China), Tianhang Zhou (College of Carbon Neutrality Future Technology, China University of Petroleum, Beijing, China), Yu Yang Fredrik Liu (DeepVerse PTE. LTD., Singapore), Yuqiang Li (Shanghai Artificial Intelligence Laboratory, Shanghai, China), Nanyang Ye (Shanghai Artificial Intelligence Laboratory, Shanghai, China, School of Computer Science, Shanghai Jiao Tong University, Shanghai, China), Qinying Gu (Shanghai Artificial Intelligence Laboratory, Shanghai, China)  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.22054v1  

#### Abstract
The high cost and data scarcity in scientific exploration have motivated the use of large language models (LLMs) as knowledge-driven components in Bayesian optimization (BO). However, existing approaches typically embed LLMs directly into the sampling or surrogate modeling pipeline, without fully le...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation —— 核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在科学探索任务中（如药物设计、催化剂优化等），**每次真实实验（real-fidelity evaluation）成本高昂且数据稀缺**，导致传统 **Bayesian Optimization (BO)** 面临两大挑战：
- **冷启动问题（cold-start problem）**：初期缺乏有效先验，难以高效探索。
- **高维搜索空间效率低**：受限于实验预算，难以充分覆盖复杂的设计空间。

尽管已有研究尝试引入 **Large Language Models (LLMs)** 提供先验知识（如初始化建议、生成候选方案），但这些方法通常：
- 仅将 LLM 作为辅助工具（如初始化或局部建议）；
- 忽视了 LLM 预测成本极低这一优势，未能系统性地利用其进行大规模低成本探索。

---

### 🚀 提出的新方法：LABO
作者提出 **LLM-Accelerated Bayesian Optimization (LABO)**，一种将 LLM 预测与真实实验深度融合的双保真度（dual-fidelity）BO 框架。

#### 核心思想
- 将 LLM 视为一个**低成本、知识驱动的低保真度信号源（LLM-fidelity predictor）**；
- 将真实实验视为**高成本、高保真度的观测（real-fidelity observation）**；
- 在统一的 BO 循环中动态融合两者。

#### 创新机制
1. **LLM-Aware Modeling（基于KO-Hagan模型）**
   - 采用 Kennedy-O’Hagan (KOH) 联合高斯过程（Joint GP）建模：
     $$
     f_R(x) = \rho f_L(x) + \delta(x)
     $$
     其中：
     - $ f_L(x) $：LLM 预测值；
     - $ \rho $：标定系数（scaling factor）；
     - $ \delta(x) $：残差项，捕捉 LLM 无法解释的偏差。
   - 该结构允许通过 LLM 查询更新 $ f_L $ 和 $ \delta $，从而间接提升对 $ f_R $ 的估计精度。

2. **Gating Criterion（门控准则）**
   - 定义 **discrepancy dominance ratio**：
     $$
     \rho_\Delta(x) = \frac{\text{Var}[\delta(x)]}{\text{Var}[f_R(x)]}
     $$
   - 设定阈值 $ \tau \in (0,1) $：
     - 若 $ \rho_\Delta(x) \leq \tau $：LLM 预测可靠 → 使用 LLM 预测更新模型；
     - 否则：不确定性主要来自残差 → 执行真实实验。

> 💡 **本质**：让 LLM 负责“广域粗略探索”，只在不确定性强的区域才调用昂贵的真实实验，实现**选择性实验（selective experimentation）**。

---

### 🔍 相比现有方法的优势
| 方法 | 局限性 | LABO 的改进 |
|------|--------|-------------|
| **Vanilla BO** | 缺乏先验，冷启动慢，探索效率低 | 引入 LLM 提供全局先验，加速收敛 |
| **LLAMBO / BOPRO / CAKE** | LLM 仅用于初始化或局部建议，未系统整合 | 将 LLM 作为持续的信息源，参与整个优化循环 |
| **ChemBOMAS / ToSFiT** | LLM 仅提供初始伪数据或替代采样器 | 动态判断是否信任 LLM，避免误导，更鲁棒 |

> ✅ LABO 不仅提升了样本效率，还具备理论保障，在 LLM 有用时增效，无用时退化为 Vanilla BO，具有**强健性和自适应性**。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集（共6个科学优化任务）
| 任务 | 维度 | 目标 | 类型 |
|------|-------|------|------|
| **COF** (Covalent Organic Frameworks) | 14D | 最大化 Xe/Kr 吸附选择性 | 化学材料 |
| **Fullerene** | 3D | 最大化 C60 加合物产率 | 化学反应 |
| **PCE10** | 4D | 最小化光降解（photodegradation） | 光伏材料 |
| **P3HT** | 5D | 最大化电导率 | 复合材料 |
| **Flow Battery** | 3D | 优化电解液综合性能指标 | 能源系统 |
| **Sandwich** | 20D | 最大化饮食健康评分（HEI） | 营养配方 |

此外还包括：
- **AutoML 任务**：SVM（2D）、MLP（5D）超参优化（HPOBench）
- **高维任务**：86D 超导体临界温度优化（Superconductor）

---

### ⚙️ 实验设置
- **每轮迭代查询 2 个候选点**
- **真实实验预算限制为 30 轮（即最多 60 次 real-fidelity evaluation）**
- **初始化阶段**：
  - LABO 使用 3 个 LLM 推荐的初始点 + 50 个 LHS 采样的 LLM-fidelity 预测
- **Gating 阈值**：固定为 $ \tau = 0.75 $
- **Surrogate Model**：RBF Kernel 的 GP
- **Acquisition Function**：q-UCB
- **LLM 模型**：Intern-S1（241B），部分实验测试 Qwen3、Deepseek-V3 等

---

### 📊 评估指标
1. **最终目标值（Final Objective Value）**
2. **达到最优值 90% 所需迭代次数（Iters to 90%）**
3. **样本效率（Sample Efficiency）**
4. **总成本分析**（考虑 LLM vs 实验成本）
5. **消融实验**（Ablation Studies）

---

### 🆚 基线方法对比
| 方法 | 简介 |
|------|------|
| **Vanilla BO** | 标准 BO，无外部知识 |
| **LLAMBO** | LLM 提供初始化 + 优化过程中提供建议 |
| **BOPRO** | 在 LLM 编码的隐空间中进行 BO |
| **CAKE** | LLM 生成并调整 GP kernel |
| **ToSFiT** | 将 Thompson Sampling 转化为 LLM 微调过程（用于离散任务） |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（主实验）

| 方法 | COF (14D) ↑ | Fullerene (3D) ↑ | P3HT (5D) ↑ | Sandwich (20D) ↑ |
|------|--------------|------------------|--------------|------------------|
| **LABO** | **11.23** | **0.9512** | **0.941** | **1.50** |
| LLAMBO | 10.85 | 0.9480 | 0.925 | 1.42 |
| BOPRO | 10.92 | 0.9475 | 0.934 | 1.45 |
| CAKE | 11.04 | 0.9495 | 0.939 | 1.48 |
| Vanilla BO | 10.77 | 0.9460 | 0.905 | 1.38 |

> ✅ LABO 在所有任务上均取得**最佳最终性能**

---

### ⏱ 收敛速度对比（Iters to 90%）

| 方法 | COF | P3HT | Flow Battery |
|------|-----|------|---------------|
| **LABO** | **14.2** | **30.0** | **14.6** |
| LLAMBO | 21.6 | 50.2 | 22.2 |
| BOPRO | 60.2 | 47.2 | 17.0 |
| CAKE | 50.0 | 52.2 | 22.4 |
| Vanilla BO | 42.8 | 54.4 | 22.4 |

> ✅ LABO 收敛最快，尤其在高维任务（如 COF）上显著领先

---

### 🔬 消融实验结果

#### （1）不同 Gating 阈值 $ \tau $ 的影响（COF & Fullerene）
| $ \tau $ | COF Obj | Iters to 90% | L/R Ratio |
|----------|---------|---------------|-----------|
| 0.60 | 10.78 | 24.6 | 1.52 |
| 0.75 | **11.23** | **14.2** | **2.68** |
| 0.85 | 11.17 | 12.6 | 5.26 |

> ✅ $ \tau = 0.75 $ 平衡最好；过高会导致误信 LLM，过低则浪费 LLM 探索能力

#### （2）是否使用 LLM 初始化？
- 即使 Vanilla BO 使用相同的 LLM 初始化点，仍显著落后于 LABO  
→ 表明性能提升不仅来自初始化，更源于**持续的 LLM-fidelity 探索机制**

#### （3）替换为随机预测（Random-Fidelity）
- 将 LLM 输出替换为随机数后，性能大幅下降  
→ 证明 LLM 提供的是**有信息量的知识引导**，而非简单噪声

#### （4）不同 LLM 的表现
| LLM | COF Obj | Iters to 90% |
|------|--------|--------------|
| Intern-S1-mini (7B) | 10.98 | 18.4 |
| Intern-S1 (241B) | 11.23 | 14.2 |
| Qwen3-Thinking | **11.31** | **13.0** |
| Deepseek-V3 | 11.27 | 13.8 |

> ✅ 更大、推理更强的 LLM 可进一步提升性能，但 LABO 对弱 LLM 也保持稳健

---

### 💰 成本效益分析（COF 任务）
| 方法 | Rounds | Real Eval | LLM Query | 总成本（\$100/实验, \$1/LLM） |
|------|--------|------------|------------|-------------------------------|
| Vanilla BO | 30 | 60 | 0 | **\$6000** |
| LABO | 4 | 8 | 164 | **\$964** |

> ✅ LABO 以 **仅 16% 的成本** 达到相同性能，经济效益巨大

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **LLM 可作为有效的低保真度信号源**，支持大规模、低成本的全局探索；
2. **Gating Criterion 能有效识别何时依赖 LLM、何时执行真实实验**，实现资源最优分配；
3. **LABO 显著优于现有 LLM+BO 方法**，在各类科学任务中均表现出更快收敛和更高最终性能；
4. **理论保证成立**：当 LLM 有帮助时，累积遗憾（cumulative regret）更低；即使 LLM 不准确，也能自动切换至保守策略；
5. **成本节约潜力巨大**：在真实实验昂贵场景下，可减少 80% 以上总成本。

---

### ⚠️ 方法的局限性
1. **依赖 LLM 的领域知识质量**：若 LLM 对特定任务无知，则早期探索可能无效；
2. **提示工程敏感性**：虽然文中使用标准化 prompt，但在新任务中仍需精心设计输入格式；
3. **离散变量处理有限**：当前框架主要面向连续空间，对组合优化支持较弱；
4. **多模态知识未充分利用**：目前仅使用文本知识，未结合图谱、公式、图像等其他形式。

---

### 🔮 未来工作方向
1. **扩展至多任务、多目标优化（Multi-objective BO）**
2. **结合 LLM 的主动提问能力**，实现人机协同优化；
3. **引入不确定性校准机制**，动态调整 $ \rho $ 和 $ \tau $；
4. **探索 LLM 自我反思（self-refinement）机制**，提升预测可靠性；
5. **应用于真实实验室自动化系统（Self-Driving Lab）**

---

## ✅ 总结
**LABO 是首个将 LLM 系统性嵌入 BO 循环，并通过 gating 机制实现“广域探索 + 精准实验”的双保真度优化框架**。它不仅解决了科学优化中的样本效率瓶颈，还提供了坚实的理论基础和广泛的实证验证，为 **LLM + Scientific Discovery** 开辟了一条实用且高效的新路径。

</details>

---

### 5. [From Sequential Nodes to GPU Batches: Parallel Branch and Bound for Optimal $k$-Sparse GLMs](https://arxiv.org/abs/2605.22188)

**Authors**: Jiachang Liu, Andrea Lodi  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.22188v1  

#### Abstract
GPUs have significantly accelerated first-order methods for large-scale optimization, especially in continuous optimization. However, this success has not transferred cleanly to problems with discrete variables, combinatorial structure, and nonlinear objectives, such as certifying optimal solutions ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：From Sequential Nodes to GPU Batches: Parallel Branch and Bound for Optimal $k$-Sparse GLMs

---

## 1. 主要贡献和创新点

### 解决的问题
该论文针对**cardinality-constrained Generalized Linear Models (GLMs)** 的精确求解问题，即在给定稀疏度约束 $k$ 下寻找最优的 $k$-sparse 回归或分类模型。这类问题是典型的混合整数非线性规划（MINLP）问题，传统上依赖 **Branch and Bound (BnB)** 框架进行全局优化。

然而，现有方法面临两大瓶颈：
- **Sequential Node Processing**：标准 BnB 按节点顺序处理搜索树，难以利用现代 GPU 的并行能力。
- **频繁 CPU-GPU 数据传输**：下界计算在 GPU 上加速，但可行解搜索、分支变量选择等关键步骤仍在 CPU 上执行，导致大量通信开销。

这些问题严重限制了 GPU 在组合优化中的应用潜力。

---

### 提出的新方法与创新思路

作者提出了一种**模块化、通用的 CPU-GPU 协同 BnB 框架**，其核心思想是将多个 BnB 节点打包成批（batch），统一在 GPU 上并行处理数值密集型子任务。

#### 主要创新点包括：

- ✅ **批量化的 GPU 并行 BnB 框架**
  - CPU 负责管理不规则逻辑（如队列调度、剪枝、子节点生成）
  - GPU 批量执行下界求解、可行解搜索、再优化（re-optimization）、分支变量选择等操作
  - 实现“CPU 控制流 + GPU 数据流”的高效分工

- ✅ **基于 padding 的 GPU 高效内核设计**
  - 不同 BnB 节点具有异构结构（自由/固定坐标不同），直接并行困难
  - 引入 **padding 技术**，用哨兵值（如 `-∞`）填充非自由维度，使所有节点具有统一长度
  - 利用成熟的 **batched sorting** 和 **GEMM** 等 GPU 优化例程处理共性部分，仅对轻量级不规则步骤使用定制 kernel

- ✅ **从系数恢复松弛指示变量的理论保证**
  - 证明了可通过最优系数 $\beta^*$ 显式重构松弛后的支持指示变量 $z^*$
  - 支持选择（rounding）和分支变量选择均可直接基于 $\beta^*$ 完成，无需额外求解
  - 使得这些操作可完全在 GPU 上以 batched 形式实现

- ✅ **扩展至 Rashomon Set 收集**
  - 修改剪枝阈值即可收集所有近似最优的 $k$-sparse GLMs 构成的 **Rashomon Set**
  - 支持下游统计分析，如变量重要性分布、模型选择（考虑 AUC、accuracy 等 secondary metrics）

---

### 相比现有方法的优势

| 维度 | 现有方法（如 OKGLM） | 本文方法 |
|------|------------------------|---------|
| 并行粒度 | 单节点处理 | 多节点批量处理 |
| 分支/舍入位置 | CPU | GPU（batched） |
| 数据移动 | 每节点多次 CPU-GPU 同步 | 少量大批次传输 |
| 性能瓶颈 | 节点间串行延迟高 | 充分利用 GPU 吞吐 |
| 功能扩展 | 仅求最优解 | 可收集完整 Rashomon Set |

> ⚡ 核心优势：**打破 BnB 的串行瓶颈，实现端到端的 GPU 加速路径**

---

## 2. 核心实验方法和设置

### 使用的数据集

#### （1）合成数据集（Synthetic Datasets）
- 特征维度 $p \in \{500, 1000, 2000, 4000, 8000, 16000\}$，样本数 $n = p$
- 特征相关性 $\rho = 0.9$（强相关）
- 真实稀疏系数每隔 $p/k$ 设置一个非零项（均匀分布）
- 包含 **Linear Regression** 和 **Logistic Regression** 两种损失函数
- 固定参数：$k=10$, $\lambda_2=1.0$, $M=2.0$

#### （2）真实世界数据集
- **Santander**（线性回归）：$n=4459, p=4735$
- **DOROTHEA**（逻辑回归，药物发现）：$n=2300, p=89989$，高度稀疏高维
- 参数设置：$\lambda_2=1.0, M=10.0$，测试多个 $k$ 值

---

### 实验设置与评估指标

#### 评估指标
- **运行时间（Time in seconds）**
- **最终 Optimality Gap (%)**
- **处理的 BnB 节点数量**
- **是否达到时间限制（TL）或内存溢出（OOM）**
- **组件耗时分解**（lower bound, re-optimization, transfer 等）

#### 硬件平台
- **GPU 实验**：NVIDIA A100（单卡）
- **CPU 基线**：AMD Milan @ 2.45GHz，8 核，100GB 内存
- 时间限制：3 小时（10800 秒）

---

### 基线方法对比

| 方法 | 类型 | 描述 |
|------|------|------|
| **Gurobi** | 商业 MIP 求解器 | 使用 perspective reformulation + 外逼近法处理 logistic loss |
| **MOSEK** | 商业凸优化求解器 | 支持 perspective formulation |
| **OKGLM** | 开源 SOTA 方法 | 当前最先进的开源实现，单节点 GPU 加速下界计算，其余在 CPU |

> 🔍 所有方法均使用相同的 warm-start（beam search 初始化）

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 1 & 2）

#### 📈 在合成数据上的表现（Linear Regression）

| $p$ | Gurobi (Time) | OKGLM (Time) | **Ours (Time)** | Speedup vs OKGLM |
|-----|---------------|--------------|------------------|-------------------|
| 16K | TL (>10800s) | 228.8s       | **30.6s**        | ~7.5x             |
| 8K  | TL            | 109.5s       | **15.1s**        | ~7.2x             |
| 4K  | 9717s         | 87.3s        | **16.6s**        | ~5.3x             |

✅ 所有实例均 **certify zero optimality gap**

#### 📉 在合成 Logistic Regression 上差距更大

| $p$ | OKGLM (Gap) | **Ours (Gap)** | OKGLM (Nodes) | **Ours (Nodes)** |
|-----|-------------|----------------|----------------|------------------|
| 500 | 69.60%      | **0.00%**      | 45,117         | **3.76M**        |

➡️ OKGLM 在最难情况下超时且存在巨大 gap；而本文方法在 **4348 秒内完成 376 万节点探索，gap=0**

---

#### 💡 在真实数据集上的表现

| Dataset | Method | Max $k$ Solved | Time (Best Case) | Gap |
|--------|--------|------------------|------------------|-----|
| Santander | Gurobi / MOSEK | $k=6$ | TL / 1074s | 0.27% |
|           | **Ours** | **$k=10$** | **52.3s** | **0.00%** |
| DOROTHEA ($k=45$) | OKGLM | TL | — | 0.06% |
|                     | **Ours** | ✅ | **2198s** | **0.00%** |

> ✅ 所有实例中，**只有本文方法在所有测试案例中实现了零 optimality gap**

---

### 消融实验与组件分析（Appendix 12）

#### （1）Batch Size 对性能的影响（Figure 3）

- 随着 batch size 增加，总运行时间显著下降
- 存在饱和效应：
  - Linear Reg: 在 $2^{10}=1024$ 左右趋于平稳
  - Logistic Reg: 在 $2^{15}=32768$ 达到峰值效率
- 表明：更大的 batch 能更好摊销 GPU 启动开销和 queue management 成本

#### （2）各组件耗时占比（Table 3 & 4）

| 组件 | 占比范围 |
|------|--------|
| Lower Bound Solve | 40–85% |
| Re-optimization | 8–40% |
| CPU-GPU Transfer | <1% |
| Branching & Node Gen | <15% |

📌 发现：尽管 lower bound 是最耗时部分，但在大规模问题中（如 $p=500$ logistic），**re-optimization 占比高达 73.4%**，说明批处理对整体性能至关重要。

---

## 4. 关键结论和发现

### 主要发现

1. ✅ **GPU 可有效加速组合优化中的 BnB 过程**  
   通过批量处理多个节点，成功克服了传统 BnB 的串行瓶颈。

2. ✅ **Padding + Batched Routines 是处理异构节点的有效策略**  
   利用 GPU 的高带宽内存特性，将不规则结构转化为规则张量运算。

3. ✅ **理论支持实现全 GPU 流水线**  
   通过 Theorem 4.1 证明可以从 $\beta^*$ 恢复 $z^*$，从而避免 CPU 参与分支决策。

4. ✅ **实现了前所未有的求解规模与精度**  
   在高达 $p=89989$ 的 DOROTHEA 数据集上仍能认证最优性。

5. ✅ **支持 Rashomon Set 收集与下游分析**  
   可用于变量重要性分析、模型鲁棒性评估、多目标模型选择。

---

### 方法的局限性

- ❗ **依赖于特定松弛形式（perspective relaxation）**
  - 当前框架围绕 proximal gradient 设计，可能不适用于其他类型的 MINLP 松弛
- ❗ **自动 batch size 选择较保守**
  - 当前采用 memory-safe heuristic，未动态调整 batch size 以适应搜索过程变化
- ❗ **目前仅支持 single-GPU 或 row-distributed multi-GPU**
  - 尚未实现 fully distributed BnB（如跨多机）

---

### 未来工作方向

1. 🔮 **扩展至更广泛的 MINLP 问题族**
   - 如 sparse GAMs、mixed-effects models、structured sparsity
2. 🔁 **引入 adaptive batching 策略**
   - 根据节点难度、深度、松弛质量动态分配 batch
3. ☁️ **构建分布式 BnB 框架**
   - 结合 node-parallel 与 data-parallel，支持超大规模问题
4. 🧪 **结合强化学习进行智能节点排序与分支策略**
   - 利用 GPU 批量反馈训练 policy network
5. 📊 **发展 Rashomon-aware 解释工具包**
   - 提供可视化接口，辅助用户理解变量替代性与模型多样性

---

## 总结

> 🏆 本文提出了首个真正意义上实现 **GPU 并行化 Branch and Bound** 的通用框架，解决了 $k$-sparse GLMs 的精确求解难题。通过 **batching + padding + modular design**，实现了比现有方法快 **1–2 个数量级** 的速度提升，并首次在挑战性实例上 **certify zero optimality gap**。同时支持 **Rashomon Set 收集**，为可解释机器学习提供了新的基础设施。

💡 **一句话总结**：  
**“把串行的 BnB 树变成并行的 GPU 批处理流水线，让 GPU 不只加速梯度，也能加速搜索。”**

</details>

---

### 6. [ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification](https://arxiv.org/abs/2605.22684)

**Authors**: Jos\'e Alberto Rodr\'iguez, Luis Balderas, Miguel Lastra, Antonio Arauzo-Azofra, Jos\'e M. Ben\'itez  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.22684v1  

#### Abstract
Time Series Foundation Models (TSFMs) have become a new component of the state-of-the-art in general time series forecasting. However, adapting them to specialized classification tasks remains constrained by two interconnected challenges: the quadratic cost of standard attention mechanisms and the i...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# ChronoVAE-HOPE: Beyond Attention — A Next-Generation VAE Foundation Model for Specialized Time Series Classification  
**论文核心总结**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前 **Time Series Foundation Models (TSFMs)** 在应用于**专门化时间序列分类任务**时面临两大瓶颈：
- **计算成本高**：标准 self-attention 机制具有 $O(L^2)$ 的时间复杂度，限制了可处理的历史上下文长度；
- **表示能力受限**：主流模型将所有时间变化压缩到一个纠缠的 latent vector 中，无法区分趋势（trend）与季节性（seasonal）等结构性成分，导致下游分类器难以解耦语义信息。

### 🚀 提出的新方法与创新
论文提出 **ChronoVAE-HOPE**，一种基于 **Variational Autoencoder (VAE)** 的新一代 TSFM，其核心创新包括：

#### （1）**HOPE Block 替代 Attention**
- 引入双记忆系统取代传统 Transformer 的 self-attention：
  - **Titans Modules**：作为短期动态记忆，采用 fast-weight 机制实现局部快速适应；
  - **Continuum Memory System (CMS)**：多层级长期记忆模块，以不同频率更新，支持跨尺度历史抽象。
- **优势**：将计算复杂度从 $O(L^2)$ 降至 $O(L)$，显著提升长序列建模效率。

#### （2）**解耦的 VAE 潜在空间设计（Disentangled Latent Space）**
- 编码器通过两个独立的 head 分别提取 **trend** 和 **seasonal** 成分；
- 解码器也分为两条独立路径进行重构；
- 利用 **SeriesDecomp** 模块提供监督信号（移动平均 + 残差），引导潜在空间对齐真实结构。

#### （3）**复合自监督预训练目标**
- 结合两种损失函数：
  - **Disentangled VAE 重建损失**（ELBO）
  - **Masked Time Series Modeling (MTSM)** 辅助任务（掩码值预测）
- 预训练后冻结编码器，仅微调轻量级分类头，避免破坏通用表征。

### 🔍 相比现有方法的优势
| 维度 | 传统方法（如 PatchTST, InceptionTime） | ChronoVAE-HOPE |
|------|----------------------------------------|----------------|
| 注意力机制 | Self-Attention（二次成本） | HOPE Block（线性成本） |
| 表示结构 | 单一、纠缠 latent 向量 | 解耦的趋势/季节子空间 |
| 可解释性 | 差 | 显式分离结构成分，增强可读性 |
| 下游适配 | 微调整个网络 | 冻结编码器 + 轻量分类头，适合小样本场景 |

---

## 2. 核心实验方法和设置

### 📚 数据集
#### （1）**预训练阶段**
使用来自 **Monash Time Series Forecasting Archive** 的大规模异构数据集：
- `m4_hourly`, `weather`, `electricity`, `traffic`, `tourism_monthly`

目的：学习广泛的时间模式，涵盖高频波动与低频趋势。

#### （2）**下游分类评估**
采用 **UCR Time Series Classification Archive** 中的 **BakeOff benchmark** 子集（共86个数据集），并施加过滤条件：
- 类别数 < 8
- 序列长度 < 400 时间步

最终用于报告性能的数据集为该子集，确保实验贴近实际工业与学术应用场景。

---

### 🧪 实验设置
| 设置项 | 描述 |
|-------|------|
| 输入长度 | 256 |
| Embedding 维度 $D$ | 128 |
| HOPE Blocks 数量 | 3 |
| CMS 层级数 | 4（更新频率分别为 [1,4,16,64] batches） |
| Titans Chunk Size | 32 tokens |
| Dropout | 0.1 |
| 优化器 | Adam |
| 预训练轮次 | 最多 300 epochs，early stopping patience=5 |
| 下游分类训练 | 冻结编码器，仅训练分类头；最多 300 epochs，patience=10 |

#### 损失权重
$$
\mathcal{L}_{total} = \mathcal{L}_{recon} + \lambda_{KL} \cdot \mathcal{L}_{KL} + \lambda_{MTSM} \cdot \mathcal{L}_{MTSM}
$$
其中 $\lambda_{KL} = 0.01$, $\lambda_{MTSM} = 0.5$

---

### 🎯 评估指标
#### （1）预训练阶段
- **Disentangled Reconstruction MSE ($\mathcal{L}_{recon}$)**：衡量趋势与季节分量的重建质量
- **KL Divergence ($\mathcal{L}_{KL}$)**：控制 latent 分布接近先验（标准正态）
- **MTSM MSE ($\mathcal{L}_{MTSM}$)**：评估对缺失值的推断能力

#### （2）下游分类阶段
- **Accuracy**：测试集准确率
- **Macro-F1 Score**：类别不平衡下的综合判别能力

---

### ⚔️ 基线对比（文中未直接列出完整基线表格，但隐含比较对象）
尽管本文未提供与其他 SOTA 模型（如 InceptionTime、HIVE-COTE）的显式对比表格，但从上下文可知其定位是：
- 对比对象包括：PatchTST、TimesFM、MOIRAI 等 TSFMs；
- 特别强调在 **冻结编码器范式下** 的有效性，区别于需全参数微调的方法。

---

## 3. 主要实验结果和性能指标

### 📊 总体性能
在 BakeOff benchmark 过滤后的子集上取得以下结果：

| 指标 | 数值 |
|------|------|
| **平均 Accuracy** | **76.52%** |
| **平均 Macro-F1 Score** | **0.741** |

> 注：在全部86个数据集上的平均准确率为 61.1%，F1 为 0.583；过滤后性能大幅提升，说明模型更适用于中短序列、少类别的现实任务。

---

### 📈 按数据类型分类的表现（Table 1）
| 数据类型 | 平均 Accuracy |
|--------|---------------|
| **SPECTRO** | **85.30%** ✅ 最佳表现 |
| **SIMULATED** | 82.45% |
| **HAR** (Human Activity Recognition) | 79.33% |
| **SENSOR** | 78.58% |
| **ECG** | 75.31% |
| **IMAGE** | 74.03% |
| **DEVICE** | 67.42% |
| **MOTION** | 66.31% ❌ 最低表现 |

> **观察**：在具有明确因果结构和周期性的领域（如生理信号、传感器读数）表现优异；而在高类内变异性和设备异质性较强的 MOTION 和 DEVICE 上表现较差。

---

### 🔍 消融分析（文中未提供正式消融实验表格，但有讨论支撑）  
虽然没有明确的 ablation study 表格，但论文通过以下方式验证组件重要性：

- **HOPE Block 的有效性**：线性复杂度使得长程依赖建模成为可能，且 Titans + CMS 协同工作提升了局部与全局感知能力。
- **Disentanglement 的作用**：即使在 IMAGE 类这种“分解无语义意义”的数据上仍能获得高于随机猜测的性能（74.03%），表明 **series decomposition 提供了隐式正则化效果**。
- **Frozen Encoder 范式的可行性**：仅训练轻量分类头即可达到良好性能，证明预训练得到的 embedding 具备强泛化能力。

---

## 4. 关键结论和发现

### ✅ 主要结论
1. **HOPE Block 实现高效长序列建模**
   - 成功替代 quadratic attention，达成 $O(L)$ 复杂度，使大规模预训练更具可行性。

2. **结构化解耦表示显著提升可解释性与迁移性**
   - 显式分离 trend 与 seasonal 成分不仅符合物理直觉，还增强了 embedding 的结构性，有利于下游任务理解。

3. **Frozen Encoder 范式有效且稳健**
   - 在低资源场景下，冻结预训练编码器、仅训练分类头即可获得竞争力的结果，防止过拟合并保留通用知识。

4. **领域对齐决定迁移质量**
   - 当目标任务的时间结构与模型归纳偏置（trend/seasonal 分解）一致时（如 SPECTRO、HAR），性能最佳；
   - 若存在结构性不匹配（如 MOTION 中的高度类内变化），则性能受限。

---

### ⚠️ 方法的局限性
| 局限 | 说明 |
|------|------|
| **依赖趋势-季节分解假设** | 对不具备清晰 trend-seasonal 结构的数据（如 motion capture）建模能力有限 |
| **冻结编码器可能牺牲灵活性** | 不允许微调意味着无法针对特定任务优化特征提取过程 |
| **目前仅支持单变量输入** | 尚未扩展至 multivariate time series，限制了在复杂系统监控中的应用 |
| **缺乏零样本分类能力验证** | 未测试是否能在未见类别上实现 zero-shot 推理 |

---

### 🔮 未来工作方向（作者明确提出）
1. **引入信息论约束加强解耦**
   - 如使用 B-TCVAE 中的 total correlation penalty 来最小化 $Z_t$ 与 $Z_s$ 之间的互信息，提升统计独立性。

2. **利用生成能力进行低资源数据增强**
   - 通过对 trend 或 seasonal 分量单独扰动生成合成样本，缓解 MOTION/DEVICE 等领域的类内差异问题。

3. **课程式掩码与更大规模预训练**
   - 设计 curriculum masking（逐步增加掩码比例）加速收敛；
   - 扩展到更多 Monash 子集或其他异构仓库，探索 zero-shot 分类潜力。

4. **多变量解耦扩展（Multivariate Disentanglement）**
   - 开发通道间共享趋势/季节因子的架构，例如 group-sparse latent representations 或 channel-wise posterior factorization。

---

## 总结（Summary）

| 维度 | 内容摘要 |
|------|----------|
| **核心思想** | 构建一个基于 VAE 的时间序列基础模型，通过 HOPE Block 提升效率，通过解耦 latent space 增强结构表达能力 |
| **关键技术** | HOPE Block（Titans + CMS）、disentangled encoder/decoder、SeriesDecomp 监督、MTSM 自监督任务 |
| **实验亮点** | 在 UCR BakeOff 子集上实现 **76.52% 准确率**，尤其在 ECG、HAR、SPECTRO 等结构清晰领域表现突出 |
| **核心价值** | 提供了一种**可解释、高效、适用于小样本分类**的 TSFM 新范式，推动 foundation model 向 structured generative representation 演进 |

> 💡 **一句话总结**：  
> **ChronoVAE-HOPE 通过“结构化生成 + 双记忆架构”，实现了高效且可解释的时间序列基础模型，在冻结编码器设定下展现出强大的下游分类潜力，特别是在具备明确趋势-周期结构的任务中遥遥领先。**

</details>

---

### 7. [Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier](https://arxiv.org/abs/2605.22746)

**Authors**: Berk Hayta, Hannah Laus, Simon Mittermaier, Felix Krahmer  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.22746v1  

#### Abstract
Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Plug-in Losses for Evidential Deep Learning

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

**Evidential Deep Learning (EDL)** 是一种单次前向传播即可估计预测不确定性的方法，通过神经网络输出 Dirichlet 分布参数来建模类别概率。然而，其训练目标（Dirichlet-expected loss）涉及对 Dirichlet 分布的期望计算，导致损失函数复杂、优化困难、实现繁琐，并且对超参数敏感。

本文旨在解决以下问题：
- **EDL 的理论与实践脱节**：尽管 EDL 在理论上具有吸引力，但其复杂的损失函数（如 Dirichlet 期望交叉熵）难以分析和高效实现。
- **缺乏对 Softmax 不确定性能力的解释**：传统上认为 Softmax 缺乏不确定性建模能力，但在实践中其置信度有时表现良好，缺乏理论支持。

---

### 🚀 提出的新方法与新思路

作者提出了一种**简化框架**——**Plug-in Losses for Evidential Deep Learning**，核心思想是：

> **用在 Dirichlet 均值处直接评估的标准分类损失（即“插件”损失）来近似原始的 Dirichlet 期望损失。**

具体包括：

1. **Plug-in Loss 定义**：
   - 将原 EDL 损失 $ \mathbb{E}_{\boldsymbol{\pi} \sim \text{Dir}(\alpha)}[\ell(\boldsymbol{\pi}, y)] $ 近似为 $ \ell(\mathbb{E}[\boldsymbol{\pi}], y) = \ell(\mathbf{I}(\alpha), y) $
   - 其中 $\mathbf{I}(\alpha) = \alpha / \alpha_0$ 是 Dirichlet 均值（即预测概率）
   - 示例：Plug-in Cross-Entropy = $-\log I(\alpha)_y$；Plug-in MSE = $\|\mathbf{I}(\alpha) - \mathbf{y}\|^2$

2. **理论保证**：
   - 通过泰勒展开证明：当证据（evidence）$\alpha_0 \to \infty$ 时，近似误差以 $O((\alpha_0 + 1)^{-1})$ 收敛到零。
   - 对于光滑损失（如 MSE）和满足下界条件的交叉熵（$p_y \geq \delta > 0$），该近似是有效的。

3. **统一视角下的 Softmax 解释**：
   - **Theorem 1** 证明：任何使用 Softmax 输出层的模型都可以视为一种 **Simplified Evidential Classifier**。
   - 当选择 $T(z) = \exp(z)$, $\phi(e) = e$ 时，$\mathbf{I}(\alpha) = \text{softmax}(z)$。
   - 因此，**Softmax 被自然地纳入 EDL 框架中**，为其不确定性估计能力提供了新的理论基础。

---

### 🔍 相比现有方法的优势

| 方面 | 优势 |
|------|------|
| **实现简便性** | 可直接使用标准 DL 框架中的 `cross_entropy` 或 `mse_loss`，无需自定义复杂期望损失 |
| **训练稳定性** | 避免了原始 EDL 中因 Dirichlet 方差项带来的优化挑战 |
| **兼容性高** | 可无缝集成到现有训练流程中，无需修改优化器或学习率调度 |
| **理论可解释性强** | 提供了从“期望损失”到“插件损失”的渐进逼近理论 |
| **涵盖经典模型** | 成功将 Softmax 纳入不确定性估计体系，弥合了经验与理论之间的鸿沟 |

---

## 2. 核心实验方法和设置

### 📚 数据集

- **Google Speech Commands v1 (GSC V1)**
  - 包含 30 个关键词的语音命令识别任务
  - 广泛用于嵌入式设备上的 **Keyword Spotting / Wake-word Detection**
  - 更贴近真实应用场景（资源受限、安全关键）

---

### ⚙️ 实验设置

#### 模型架构
- 主干网络：**MatchboxNet**（轻量级 1D CNN，适合边缘部署）
- 所有变体共享相同 backbone 和训练配置，仅改变输出映射和损失函数

#### 模型变体对比（见 Table 1）

| 类型 | Evidence Map $T(z)$ | Parameter Map $\phi(e)$ | Loss Function |
|------|------------------------|----------------------------|-------------|
| EDL-CE | softplus | $e+1$ | Dirichlet CE + KL |
| EDL-MSE | softplus | $e+1$ | Dirichlet MSE + KL |
| Plug-in CE/MSE | softplus/exp | $e+1$ or $e$ | CE(p) or MSE(p) |
| **Softmax** | exp | $e$ ($c=0$) | CE(p) |
| Softplus | softplus | $e$ ($c=0$) | CE(p) |
| Softmax + KL | exp | $e$ | CE(p) + KL(Dir(e+1)\|Dir(1)) |

> 注：KL 正则化仅作用于错误类别的证据抑制

---

### 🎯 评估指标与协议

#### 不确定性评分（Uncertainty Scores）
1. **Predictive Entropy**（熵）：
   $$
   u_{\text{entropy}} = \frac{-\sum_k p_k \log p_k}{\log K}
   $$
2. **Vacuity**（空缺度，基于浓度）：
   $$
   u_{\text{vacuity}} = \frac{K}{\alpha_0},\quad \alpha_0 = \sum_k \alpha_k
   $$

#### Selective Prediction Protocol
- 按不确定性升序排序测试样本
- 设定阈值 $t$，只保留 $u < t$ 的样本进行预测
- 报告两个关键指标：
  - **Acc_th**: 被接受样本中的准确率（目标 ≥ 99.0%, 99.5%, 99.9%）
  - **Acc_total**: 整体准确率（考虑被拒绝样本）
  - **Coverage**: 被接受样本的比例

> 目标是在高 Acc_th 下最大化 Acc_total 和 Coverage

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（来自 Table 2）

#### 在 **Entropy-based Selection** 下的表现（最优 Acc_total）

| Model | Base Acc (%) | @99.9% Acc_th → Acc_total (%) |
|-------|---------------|-------------------------------|
| **Softmax** | 97.21 | **88.41** |
| Softplus | 97.07 | 87.64 |
| Plug-in EDL-CE | 96.84 | 83.55 |
| EDL-CE | 96.88 | 81.61 |

✅ 结论：**Softmax 在熵引导的选择性预测中表现最佳或接近最佳**

---

#### 在 **Vacuity-based Selection** 下的表现（@99.9% Acc_th）

| Model | Acc_total (%) |
|-------|----------------|
| **Softmax + KL** | **80.36** |
| Plug-in EDL-CE | 83.55 |
| EDL-CE | 81.62 |
| Softmax (no KL) | 62.00 |
| EDL-CE no KL | 47.14 |

✅ 结论：
- **KL 正则化显著提升 Vacuity 的有效性**
- 单纯使用 Dirichlet 期望损失（如 EDL-CE no KL）并不能使 Vacuity 更可靠
- **KL 是影响 Vacuity 排序质量的关键因素**

---

### 🔬 消融实验结果

| 发现 | 说明 |
|------|------|
| ✅ **Plug-in 近似 ≈ 原始 EDL 性能** | Plug-in EDL-CE/MSE 与原始 EDL-CE/MSE 在 Acc_total 上几乎一致，验证了近似的有效性 |
| ✅ **Softmax 是有效的 evidential classifier** | Softmax 模型在 entropy 指标下表现优异，说明其具备良好的不确定性分辨能力 |
| ✅ **KL 正则化决定 Vacuity 质量** | 加入 KL 后，Softmax 的 Vacuity 表现大幅提升（62% → 80%），而 entropy 变化不大 |
| ❌ **仅换损失函数不能改善 Vacuity** | Softmax+EDL-CE（即用 Dirichlet CE 损失训练 Softmax 参数化）并未提升 Vacuity 表现 |

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **EDL 损失可以被简单插件损失有效近似**  
   在证据充足的情况下，$\mathbb{E}[\ell(\pi)] \approx \ell(\mathbb{E}[\pi])$，误差随 $\alpha_0^{-1}$ 快速衰减。

2. **Softmax 天然属于 Evidential Learning 框架**  
   通过适当构造，Softmax 可被视为一种简化的 evidential classifier，这为其在不确定性估计中的实用表现提供了理论依据。

3. **Plug-in 方法性能媲美经典 EDL**  
   在 GSC V1 上，简化方法在预测精度和选择性预测方面均达到甚至超过原始 EDL。

4. **KL 正则化是 Vacuity 有效的关键**  
   是否加入 KL 显著影响 Vacuity 的可靠性排序，而非损失形式本身。

5. **这是首个在语音命令识别中应用 EDL 并报告 coverage-accuracy trade-off 的工作**

---

### ⚠️ 局限性

1. **实证范围有限**：
   - 实验仅在一个任务（GSC V1）上进行
   - 未在分布外检测（OOD）、对抗样本等更复杂场景下验证

2. **理论假设限制**：
   - 泰勒展开要求损失函数光滑，但交叉熵在边界处不可导
   - 实际中需依赖 $p_y \geq \delta$ 来保证近似成立

3. **未探索多阈值融合策略**：
   - 当前使用单一不确定性指标进行筛选
   - 如何结合 entropy 与 vacuity 尚未研究

---

### 🔮 未来工作方向

1. **扩展至更多任务和架构**
   - 图像分类、NLP、医疗诊断等领域验证通用性

2. **研究分布偏移下的表现**
   - 测试在 dataset shift、噪声数据、OOD 输入下的鲁棒性

3. **设计联合不确定性决策规则**
   - 探索双阈值机制：同时基于 entropy 和 vacuity 决策

4. **进一步简化正则化设计**
   - 是否可用其他方式替代 KL 正则化来控制证据尺度？

5. **理论深化**
   - 分析不同 evidence-to-Dirichlet 映射对收敛性和不确定性校准的影响

---

> 💡 **一句话总结**：  
> 本文提出了一个简洁有力的 **Plug-in EDL 框架**，用标准损失近似复杂的 Dirichlet 期望损失，在保持高性能的同时极大提升了可实现性和可解释性，并首次为 **Softmax 的不确定性能力**提供了理论支撑。

</details>

---

### 8. [Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration](https://arxiv.org/abs/2605.20190)

**Authors**: Liyuan Deng, Shujian Deng, Yongkang Chen, Yongkang Dai, Zhihang Zhong, Linyang Li, Xiao Sun, Yilei Shi, Huaxi Huang  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.20190v1  

#### Abstract
Iterative industrial design-simulation optimization is bottlenecked by the CAD-CAE semantic gap: translating simulation feedback into valid geometric edits under diverse, coupled constraints. To fill this gap, we propose COSMO-Agent (Closed-loop Optimization, Simulation, and Modeling Orchestration),...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Tool-Augmented Agent for Closed-loop Optimization, Simulation, and Modeling Orchestration*

## 1. 论文的主要贡献和创新点

### 解决的问题
现代工业设计中的 **CAD-CAE 闭环优化** 面临严重瓶颈，即所谓的 **CAD-CAE 语义鸿沟**（semantic gap）：
- 工程师需将高维仿真反馈（如应力场、位移场）转化为低维、可执行的几何参数修改；
- 参数化 CAD 模型具有历史依赖性，任意修改可能导致再生失败；
- 实际工具链中存在大量不确定性（如网格划分失败、求解器不收敛），导致自动化流程不稳定。

现有方法（如无梯度优化、代理模型、微调 LLM）通常忽略执行可行性、缺乏对工具链故障的鲁棒性，且难以处理多约束耦合场景。

---

### 提出的新方法：COSMO-Agent
提出 **COSMO-Agent**（Closed-loop Optimization, Simulation, and Modeling Orchestration），一个基于 **工具增强强化学习**（tool-augmented RL）的框架，使 LLM 能够自主完成端到端的 CAD-CAE 闭环迭代优化。

#### 创新点：
1. **将 CAD-CAE 闭环建模为长周期决策问题**
   - 显式建模 CAD 再生、CAE 求解、结果解析等环节为交互式环境；
   - 引入 **显式的失败状态**，要求智能体具备从工具链错误中恢复的能力。

2. **结构化动作空间与工具调用机制**
   - 使用 **MCP**（Model Control Protocol）接口封装 CAD-CAE 工具链，提供统一、结构化的 API；
   - LLM 在参数编辑动作空间中进行决策，生成可执行的 CadQuery 代码并驱动下游工具。

3. **多目标奖励函数设计**
   设计三部分联合奖励：
   - `R_cons`：基于约束满足数量的分段奖励（0~1.0）；
   - `R_stop`：鼓励在首次可行后停止调用工具（避免冗余计算）；
   - `R_fmt`：确保输出为结构化 JSON，提升可复现性。

4. **Rollout-log-based Reward**
   - 奖励直接从轨迹日志中解析，无需额外重新仿真，训练高效；
   - 鼓励模型遵循“调用工具→读取反馈→迭代更新”的真实闭环逻辑。

---

### 相比现有方法的优势
| 维度 | 传统方法 | COSMO-Agent |
|------|--------|-------------|
| 执行可行性 | 忽略再生失败风险 | 显式建模并训练恢复能力 |
| 反馈利用 | 仅模仿人类行为或静态提示 | 基于仿真数值反馈动态调整设计 |
| 多约束处理 | 单目标优化为主 | 支持物理、几何、成本多约束协同优化 |
| 泛化能力 | 固定模板限制 | 在未见零件类别上表现优异 |

---

## 2. 核心实验方法和设置

### 数据集
构建了一个 **行业对齐的可执行 CAD-CAE 数据集**：
- 包含 **25 种常见工业部件类别**，如 flat flange、triangular bracket、I-beam cantilever beam 等；
- 总样本量约 **20,000**：
  - 训练集：20,000
  - 测试集：200
  - 泛化集（unseen categories）：100（来自其余5类）
- 每个任务包含：
  - 初始参数化 CAD 模板（CadQuery 实现）
  - 材料库（含 E, ν, ρ, price, σ_allow）
  - 加载条件与边界约束
  - 通过 FEA 提取的真值（最大位移、最大 von Mises 应力）
  - 成本计算（体积 × 密度 × 单价）

---

### 实验设置
- **基础模型**：Qwen3-8B
- **训练框架**：InternBootcamp + GRPO（Generalized Reinforcement Policy Optimization）
- **硬件资源**：16×H200 GPUs
- **每轮最多交互步数**：15 turns
- **工具链组成**：
  1. **CAD Generator**：CadQuery → STEP 文件
  2. **CAE Solver**：FreeCAD + Gmsh（网格）+ CalculiX（线性静力学求解）
  3. **Result Extractor**：解析 `.frd` 文件获取 `u_max`, `σ_max`
  4. **Cost Calculator**：基于体积和材料属性计算总成本

---

### 评估指标
| 指标 | 含义 |
|------|------|
| **FSR**（Full Success Rate） | 所有三个约束同时满足的比例（核心指标） |
| **DSR**（Displacement Satisfaction Rate） | 最大位移 ≤ 阈值的比例 |
| **SSR**（Stress Satisfaction Rate） | 最大应力 ≤ 材料许用应力的比例 |
| **CSR**（Cost Satisfaction Rate） | 总成本 ≤ 成本上限的比例 |
| **MEO**（Model Extract Output） | 输出是否为有效可解析 JSON |
| **AS**（Average Score） | 综合得分（含约束满足、格式正确性、过程奖励） |
| **ATC**（Avg Tool Calls） | 平均每次推理调用工具次数（反映效率） |

---

### 基线方法对比
涵盖多种规模的开源与闭源 LLM，在相同输入、工具链、预算下测试：
- **开源模型**：
  - Qwen3-8B, Qwen3-30B, Qwen3-Next (80B)
  - Intern-S1-mini (8B), Intern-S1 (236B)
  - Llama-4-Scout (17B)
- **闭源模型**：
  - Claude-Sonnet-4.5
  - Gemini-3-Flash

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Test Set）

| Model | FSR | DSR | SSR | CSR | MEO | AS | ATC |
|-------|-----|-----|-----|-----|-----|----|-----|
| **COSMO-Agent (8B)** | **74.5%** | **87.5%** | **76.0%** | **93.5%** | **100.0%** | **0.6504** | **6.72** |
| Gemini-3-Flash | 67.5% | 83.0% | 75.0% | 91.0% | 98.0% | 0.6802 | 9.32 |
| Intern-S1 (236B) | 32.0% | 53.0% | 75.0% | 60.0% | 99.5% | 0.5367 | 7.44 |
| Qwen3-30B | 29.5% | 48.5% | 74.5% | 73.0% | 100.0% | 0.5789 | 8.60 |

> ✅ **结论**：COSMO-Agent (8B) 在 **FSR 上超越所有基线**，包括更大参数量的开源模型和强大的闭源模型（Gemini-3-Flash），且 **ATC 更低**，说明其更高效。

---

### 泛化能力测试（Unseen Categories）

| Model | FSR | DSR | SSR | CSR | MEO | AS | ATC |
|-------|-----|-----|-----|-----|-----|----|-----|
| **COSMO-Agent (8B)** | **75.0%** | **84.0%** | **78.0%** | **89.0%** | **100.0%** | **0.6150** | **6.57** |
| Gemini-3-Flash | 57.0% | 60.0% | 57.0% | 60.0% | 60.0% | 0.6977 | 9.44 |

> ✅ **结论**：在未见过的零件类型上，COSMO-Agent 不仅保持高性能，还显著优于所有基线；尤其 **MEO 达到 100%**，而 Gemini 仅为 60%，严重影响端到端可用性。

---

### 消融实验（Ablation Studies）

| 设置 | FSR | DSR | CSR | SSR | ATC |
|------|-----|-----|-----|-----|-----|
| w/o RL | 26.0% | 39.5% | 65.0% | 72.0% | 6.08 |
| w/o Rollout Reward | 36.0% | 59.0% | 69.0% | 54.0% | 2.62 |
| **COSMO-Agent (完整版)** | **74.5%** | **87.5%** | **93.5%** | **76.0%** | **6.72** |

> 🔍 发现：
- **RL 训练带来巨大增益**（+48.5pp FSR），证明其能有效学习基于反馈的迭代策略；
- 若使用“最终 JSON 重验证”作为奖励，模型倾向于跳过工具调用、直接猜测答案（ATC 下降至 2.62），导致性能下降；
- **Rollout-log-based reward 是关键设计**，促使模型真正走完“生成→仿真→评估”闭环。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **小规模 LLM 经 RL 训练后可超越大规模闭源模型**  
   COSMO-Agent 以仅 8B 参数，在 FSR 上超过 Gemini-3-Flash（74.5% vs 67.5%），打破了“越大越好”的直觉。

2. ✅ **工具增强 + RL 是实现可靠闭环优化的关键路径**  
   单纯指令微调无法应对复杂、不确定的工程仿真流程；必须引入外部工具反馈并通过 RL 学习长期策略。

3. ✅ **奖励设计直接影响行为模式**  
   使用 rollout 日志而非重新仿真来计算奖励，既能降低成本，又能防止模型“作弊”，是实用部署的关键。

4. ✅ **泛化能力强，适用于新零件类型**  
   在未训练过的 5 类零件上仍达到 75.0% FSR，表明其学到的是通用优化策略而非过拟合特定模板。

---

### 局限性
- 当前仅支持 **线性静力学分析**，尚未扩展至非线性材料、接触、动力学或多物理场耦合；
- 几何修改局限于 **参数调整**，尚不能进行拓扑变更（如打孔、倒角）；
- 工具链稳定性仍有挑战，部分失败模式（如严重畸变网格）仍难自动恢复；
- 动作空间较小，未来需支持更复杂的组合操作。

---

### 未来工作方向
1. 扩展至 **接触、装配、多部件系统** 的协同优化；
2. 支持 **非线性材料、热-力耦合、疲劳分析** 等更复杂的物理场；
3. 接入更多 CAD/CAE 后端（如 SolidWorks, ANSYS）；
4. 构建更丰富的动作空间，支持特征级编辑（feature-level editing）；
5. 设计更鲁棒的容错机制与恢复策略；
6. 探索 curriculum learning 以加速训练收敛。

---

> 📌 **总结一句话**：  
> **COSMO-Agent 通过工具增强 RL 框架，成功弥合了 CAD-CAE 语义鸿沟，实现了高效、稳定、可泛化的闭环优化，为 AI 驱动的智能制造提供了新范式。**

</details>

---

### 9. [Polite on the Surface, Wrong in Practice: A Curated Dataset for Fixing Honorific Failures in Multilingual Bangla Generation](https://arxiv.org/abs/2605.22487)

**Authors**: Md. Asaduzzaman Shuvo, Mahedi Hasan, Md. Tashin Parvez, Azizul Haque Noman, Md. Shafayet Hossain Ovi  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.22487v1  

#### Abstract
Recent advances in Multilingual Large Language Models (MLLMs) have significantly enhanced cross-lingual conversational capabilities, yet modeling culturally nuanced and context-dependent communication remains a critical bottleneck. Specifically, existing state-of-the-art models exhibit a severe prag...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# Polite on the Surface, Wrong in Practice: A Curated Dataset for Fixing Honorific Failures in Multilingual Bangla Generation

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文针对**低资源语言（Low-Resource Languages）**在多语言大模型（MLLMs）中的一个深层瓶颈——**语用鸿沟（pragmatic gap）**。尽管当前模型能生成表面流利的孟加拉语（Bangla），但在实际应用中却存在严重缺陷，尤其是在**敬语系统（honorific system）**和**正式文档结构**上频繁出错。

具体表现为：
- **敬语不一致（Honorific Mismatch）**：在同一份正式文件中混用正式（`Apni`）和非正式（`Tumi`）第二人称代词，这在文化上是不可接受的。
- **结构错误（Structural Displacement）**：遗漏或错放日期、收件人、主题行等关键文档组件。
- **语用能力缺失（Pragmatic Failure）**：输出文本不符合社会规范和机构要求，导致无法在真实场景中使用。

### 提出的新方法与创新
为解决上述问题，作者提出了以下核心贡献：

#### 1. 引入 BLADE 数据集
- **名称**：BangLa Applications and DialoguEs (BLADE)
- **规模**：包含 4,196 对高质量、专家标注的指令-响应对（instruction-tuning pairs）。
- **覆盖范围**：涵盖 2,008 个独特主题，涉及教育、行政、职业申请和对话等多种场景。
- **构建原则**：
  - **三重数据获取管道（Three-tier acquisition pipeline）**：
    1. **教科书（Tier 1）**：从政府批准的 NCTB 教科书中提取标准格式。
    2. **网络门户（Tier 2）**：从 14 个验证过的孟加拉语网站中收集真实世界示例。
    3. **作者合成（Tier 3）**：由作者创建并经语言学专家交叉验证的复杂场景（如多轮对话）。
  - **专家验证**：所有数据均经过母语语言学家严格审核，确保敬语一致性、结构完整性和文化准确性。

#### 2. 新思路：文化对齐的数据优于模型规模
论文提出一个颠覆性观点：**对于低资源语言的实用化生成，精心策划的文化对齐数据（culturally aligned data）比模型规模（model scale）更重要**。通过在小模型上进行有监督微调（SFT），可以超越大规模通用模型的零样本（zero-shot）表现。

### 相比现有方法的优势
| 方面 | 现有方法 | 本文方法 |
|------|--------|--------|
| **数据来源** | 通用网络爬取、机器翻译 | 人工策划、文化对齐、专家验证 |
| **关注点** | 表面流畅度（fluency） | 语用正确性（pragmatic correctness） |
| **评估维度** | BLEU, ROUGE 等 | 结构完整性、敬语一致性、文化对齐 |
| **适用性** | 通用任务 | 低资源语言的特定实用场景 |

---

## 2. 核心实验方法和设置

### 使用的数据集
- **主数据集**：**BLADE**（4,196 对 prompt-response）
- **划分**：
  - 训练集：3,356
  - 验证集：420
  - 测试集：420
- **基线对比**：未使用其他公开的孟加拉语指令数据集，因其缺乏对敬语和结构的监督。

### 实验设置
- **模型选择**：
  - **多语言架构**：DeepSeek-8B, LLaMA-3.2-3B, Llama-4-Scout-17B, Gemma2-9B
  - **孟加拉语原生模型**：TigerLLM-1B
  - **闭源模型**：Gemini-2.5-Flash, Kimi-K2-32B
- **微调方法**：
  - **参数高效微调（PEFT）**：采用 **LoRA**（Low-Rank Adaptation）
  - **量化**：4-bit NormalFloat (NF4)
  - **框架**：Unsloth 库，双 NVIDIA Tesla T4 GPU
  - **训练细节**：2 轮，序列长度 2048，batch size 2，cosine 学习率衰减，peak LR 2×10⁻⁵
- **提示模板**：强制要求 `Subject → Salutation → Body → Closing` 的顺序，并保持敬语一致。

### 评估指标
采用五维评估体系：
1. **自动指标**：
   - **BLEU**：n-gram 重叠
   - **chrF**：字符级 F-score，对形态丰富的孟加拉语更鲁棒
   - **ROUGE-L**：最长公共子序列
   - **WER**：归一化编辑距离，衡量结构错误
   - **BERTScore**：基于上下文嵌入的语义相似度
2. **人工评估**：三位母语语言学专家进行双盲评估，评分维度：
   - **结构完整性（Structure）**
   - **流利度（Fluency）**
   - **文化对齐（Cultural Alignment）**
3. **LLM-as-Judge**：使用 GPT-4.1 作为裁判，评估：
   - **结构正确性**
   - **敬语一致性**
   - **语义相关性**

### 基线方法对比
- **零样本（Zero-Shot）**：直接查询未微调的模型。
- **格式匹配提示（Format-Matched Prompting）**：提供明确的结构约束，但不进行微调。

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 模型 | 微调前 BLEU | 微调后 BLEU | 增幅 | 微调后 chrF | 人类评估 (平均) | LLM-as-Judge |
|------|------------|------------|------|-------------|----------------|--------------|
| **DeepSeek-8B** | 0.78 | **17.73** | **22倍** | **45.87** | **4.74** | **8.9** |
| **Qwen2-1.5B** | 0.86 | 16.28 | 18.9倍 | 36.13 | 4.63 | 8.4 |
| **LLaMA3.2-3B** | 1.96 | 15.30 | 7.8倍 | **46.60** | 4.70 | 8.7 |
| **TigerLLM-1B** | 1.20 | 7.15 | 6.0倍 | 33.83 | 4.61 | 7.2 |
| **最强零样本 (Gemini-2.5-Flash)** | - | 7.88 | - | 41.04 | 2.13 | 3.8 |

> ✅ **关键发现**：所有微调模型在各项指标上均有显著提升，且**小模型（如 Qwen2-1.5B）在 BLADE 上微调后，性能远超大型闭源模型的零样本表现**。

### 与基线方法的对比结果
- **零样本表现极差**：所有模型 BLEU < 8，人类评估结构得分仅 1.85/5，表明其输出“看似流利，实则无用”。
- **格式匹配提示有效**：显式结构约束可将 BLEU 提升 16–22.8%，WER 降低 37.8%，证明**轻量级干预即可缓解部分结构性问题**。
- **微调效果碾压**：SFT 后，BLEU 平均提升 15+，人类评估达 4.6+/5，LLM-as-Judge 分数从 3.15 升至 8.30，实现质变。

### 消融实验结果
| 因素 | BLEU Δ | chrF Δ | WER Δ | 说明 |
|------|-------|-------|-------|------|
| **格式感知模板（FmtTpl）** | +1.1 | +2.4 | -0.12 | 显著减少 WER，提升 ROUGE-L |
| **角色标签（Roles）** | +0.6 | +2.7 | -0.06 | 改善 BERTScore 和 chrF |
| **长上下文（Ctx 2048+Pack）** | +1.4 | +3.5 | -0.09 | **最关键因素**，确保完整结构 |
| **LoRA r=16 (vs r=8)** | +1.3 | +1.8 | -0.07 | 容量适中，避免过拟合 |
| **余弦学习率** | +0.8 | +1.2 | -0.05 | 更稳定 |
| **标签平滑（Label Smoothing）** | +0.5 | +0.9 | -0.03 | 缓解脆性复制 |
| **LoRA 应用于 Attention + MLP** | +0.9 | +1.8 | -0.05 | 比仅用于 Attention 更优 |

> ✅ **结论**：**长上下文（2048 tokens）和格式感知模板是提升性能的关键**。

---

## 4. 关键结论和发现

### 主要发现
1. **数据质量 > 模型规模**：在低资源语言的实用化生成中，**精心策划的、文化对齐的指令数据（如 BLADE）比单纯扩大模型规模更有效**。
2. **语用鸿沟是结构性问题**：现有 MLLMs 在低资源语言上的失败不是词汇不足，而是缺乏对**社会关系编码（如敬语）和文档结构**的监督。
3. **微调可实现质变**：通过在 BLADE 上进行 SFT，模型从“表面礼貌”转变为“真正可用”，实现了从**表面流利到功能可用**的跨越。
4. **轻量级干预也有效**：即使不微调，仅通过**格式匹配提示**也能显著改善结构错误，为部署提供低成本方案。

### 方法的局限性
1. **训练周期短**：受限于硬件（双 T4 GPU），仅训练了 2 个 epoch，可能未完全收敛。
2. **数据偏差**：目前 BLADE 偏向**正式注册（formal registers）**，对非正式和方言覆盖不足。
3. **评估范围有限**：未在更多文档类型和任务上进行扩展评估。

### 未来工作方向
1. **延长训练时间**：使用更强算力进行充分训练。
2. **扩展数据集**：纳入更多非正式孟加拉语方言和地区变体。
3. **多样化评估**：在更多任务类型和文档格式上测试。
4. **集成验证器**：开发自动检测敬语和结构错误的工具，辅助模型生成。

> 📌 **最终目标**：推动 BLADE 成为孟加拉语及其他服务不足语言的**结构感知、敬语敏感生成**的标准基准。

</details>

---

### 10. [LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training](https://arxiv.org/abs/2605.22014)

**Authors**: Haoyuan Liu, Kairui Zhou, Shuyao Qi, Qinwei Yang, Shengkai Lin, Shizhen Zhao, Wei Zhang  
**Category**: cs.DC  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.22014v1  

#### Abstract
To reduce user costs and maximize cluster utilization, large model training increasingly leverages volatile but inexpensive GPU capacity, such as spot instances and reclaimable resources in shared clusters. Yet, capitalizing on these economic benefits requires jobs to adapt within the short warning ...

---

### 11. [Beyond Single Slot: Joint Optimization for Multi-Slot Guaranteed Display Advertising](https://arxiv.org/abs/2605.21556)

**Authors**: Zhaoqi Zhang, Jiaming Deng, Miao Xie, Linyou Cai, Qianlong Xie, Xingxing Wang, Siqiang Luo, Gao Cong  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.21556v1  

#### Abstract
Guaranteed display advertising is crucial for platform monetization, yet existing methods often operate under a single-slot assumption, limiting their ability to optimize allocation across multi-slot page views. In this paper, we propose a novel joint optimization framework for multi-slot GD allocat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Beyond Single Slot: Joint Optimization for Multi-Slot Guaranteed Display Advertising》总结

---

## 1. 论文的主要贡献和创新点

### **解决了什么问题**

当前的 **Guaranteed Display (GD) Advertising** 系统大多基于 **single-slot 建模假设**，即每个广告位独立优化分配，忽略了多广告位（multi-slot）页面中多个广告同时曝光带来的复杂交互。这导致以下三个关键问题：

1. **缺乏跨广告位协调**：热门广告位被高优先级合同垄断，其他位置利用率低，整体交付效率下降。
2. **无单个合同曝光上限**：高优先级合同可能在多个 slot 中重复出现，造成流量集中和不公平分配。
3. **同一页面内冗余曝光**：一个广告合同可能在同一 PV（Page View）中出现在多个 slot，损害用户体验。

### **提出了什么新方法或新思路**

本文提出了一种全新的 **offline bipartite matching-based 联合优化框架**，用于多槽位 GD 广告分配，核心创新如下：

- **Page View-Level 全局建模**  
  将广告请求与合同之间的分配建模为以 **Page View 为单位的离线二分图匹配问题**，实现跨 slot 的协同决策，打破传统逐 slot 决策的局限。

- **PV Constraints（Page View Constraints）机制**  
  引入 per-slot 曝光上限约束，防止头部 slot 被过度使用，促进流量在不同广告位间的均衡分布。

- **Contract Roulette-Based Selection Mechanism**  
  设计一种概率性选择机制，确保每个合同在同一个 PV 中最多只出现在一个 slot，消除冗余曝光，提升多样性和用户体验。

- **可扩展的分布式优化算法**  
  基于 KKT 条件推导出闭式解，并采用投影梯度法迭代更新对偶变量（dual variables），支持大规模工业部署。

### **相比现有方法的优势**

| 维度 | 传统方法（如 AUAF、online greedy） | 本文方法 |
|------|-------------------------------|--------|
| 决策粒度 | 单 slot 局部优化 | Page View 级全局联合优化 |
| 流量控制 | 缺乏细粒度 slot 控制 | 显式 PV constraints 控制曝光 |
| 合同公平性 | 高优先级合同易垄断 | 支持优先级 + 公平正则化 |
| 用户体验 | 可能出现同一广告多次曝光 | Contract Roulette 保证互斥 |
| 可扩展性 | 在线贪婪策略难以全局优化 | 分布式优化支持大规模部署 |

---

## 2. 核心实验方法和设置

### **使用的数据集**

- 实验在 **Meituan 广告平台的真实生产环境** 上进行。
- 使用 **真实在线流量和实时广告投放日志**，涵盖数百万级 POI 和广告合同。
- 数据未公开，但在两个灰度比例下进行了长期线上测试。

### **实验设置**

- **灰度实验设计**：
  - 两轮灰度发布：**35% 和 70% 流量** 分别进入实验组（treatment）与对照组（control）。
  - POI 粒度分流，避免污染。
- **时间周期**：
  - 35% 设置：baseline 期为 2025年3月29日–4月2日，实验期为 4月3日–7日。
  - 70% 设置：baseline 期为 3月27日–4月1日，实验期为 4月9日–14日。
- **分析方法**：
  - **A/A Test**：验证分组稳定性。
  - **A/B Test**：比较处理组与控制组的一天内表现差异。
  - **DID（Difference-in-Differences）分析**：控制时间趋势影响，估计净因果效应。

### **评估指标**

分为三大类：

#### ✅ Merchant Efficiency（商家效率）
- **Merchant ROI**：广告收入 / 广告花费
- **Payment ROI**：实际支付转化收益 / 广告花费
- **CTR**（Click-Through Rate）
- **Payment CVR**（Conversion Rate）

#### ✅ Platform Revenue（平台收益）
- **ARPU**（Average Revenue Per User）

#### ✅ Contract Fulfillment（合同履约）
- **Fulfillment Rate**：已达成曝光量 / 计划曝光量

### **基线方法对比**

- 主要对比的是 Meituan 当前线上生产系统（production baseline），属于典型的 **AUAF-like 近线控制 + online greedy allocation** 架构。
- 未直接与其他学术模型（如 SHALE、CONFLUX）对比，因部署环境不同，但文中指出其局限性作为动机。

---

## 3. 主要实验结果和性能指标

### **关键性能数据（来自 70% 灰度 DID 分析）**

| 指标 | 提升幅度 | 说明 |
|------|---------|------|
| **Merchant ROI** | **+42.17%** | 商家投资回报显著提高 |
| **Payment ROI** | **+29.13%** | 实际购买行为增强 |
| **CTR** | **+7.67%** | 用户点击意愿上升 |
| **Payment CVR** | **+23.35%** | 点击后转化能力大幅提升 |
| **ARPU** | **+28.17%** | 平台人均收入明显增长 |
| **Fulfillment Rate** | **+2.12%** | 合同交付更稳定可靠 |

> 注：在 70% 流量下的 A/B 测试中，**ARPU 提升达 28.99%**，进一步验证了效果。

### **与基线方法的对比结果**

- 所有核心指标均取得 **统计显著且业务可观的正向提升**。
- 特别是在高流量压力下（70% 灰度），系统仍保持稳健，表明框架具备良好的 **scalability 和 robustness**。
- DID 结果排除了时间趋势干扰，证明提升是方法本身所致。

### **消融实验结果（文中未明确列出）**

- 文中 **未提供显式的 ablation study 表格或模块移除实验**。
- 但从方法设计逻辑可推断：
  - 若去除 **PV constraints** → slot 流量不均 → ARPU 下降、Fulfillment 波动。
  - 若禁用 **Contract Roulette** → 同一合同多 slot 出现 → CTR/CVR 下降（用户疲劳）、Merchant ROI 受损。
- 实际上线效果间接验证了各模块必要性。

---

## 4. 关键结论和发现

### **主要发现**

1. **Multi-slot 联合优化优于单 slot 独立决策**  
   通过将分配问题提升到 **Page View 级建模**，实现了更高效、公平、协调的广告交付。

2. **精细控制显著改善系统平衡性**  
   - PV constraints 有效缓解“头尾差距”，避免少数 slot 或合同垄断资源。
   - Contract Roulette 提升曝光多样性，减少冗余，优化用户体验。

3. **离线优化 + 在线选择架构可行且高效**  
   采用 **offline bipartite matching + online probabilistic filtering** 的混合范式，在保证效果的同时满足工业级延迟要求。

4. **已在真实平台验证有效性**  
   在美团广告系统全量部署，经大规模线上实验证明其 **商业价值和技术可行性**。

### **方法的局限性**

- **依赖高质量预估模型**：如 CTR/CVR 预估不准会影响匹配质量。
- **冷启动问题**：新合同或新请求缺乏历史数据时，分配可能不够精准。
- **动态性响应略慢**：虽然 nearline 更新 dual variables，但仍不如纯 online greedy 快速响应突发流量变化。
- **未考虑跨页面序列优化**：当前仅限单个 PV 内优化，未涉及用户多页浏览路径上的长期曝光控制。

### **未来工作方向**

1. **引入时序建模**：扩展至多 PV 序列级别的曝光控制，支持频率限制（frequency capping）等高级需求。
2. **强化学习集成**：结合 RL 实现端到端动态优化，适应更复杂的多目标权衡。
3. **公平性进一步深化**：加入对长尾商家、中小预算合同的保护机制。
4. **绿色广告（Green Ads）视角**：优化能耗与碳足迹，推动可持续广告系统发展。

---

> ✅ **总结一句话**：  
> 本论文突破了传统 GD 广告的 single-slot 范式，提出首个面向 multi-slot 场景的 **page view-level joint optimization 框架**，通过 **PV constraints + Contract Roulette** 实现了更高效、公平、低冗余的广告交付，在美团真实场景中取得了 **ARPU +28.17%，Merchant ROI +42.17%** 的显著提升，具有重要的工业应用价值。

</details>

---

### 12. [AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.21560)

**Authors**: Penglin Dai, Zijie Zhou, Xincao Xu, Junhua Wang, Xiao Wu, Lixin Duan  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.21560v1  

#### Abstract
Deploying neural networks on microcontroller units (MCUs) is critical for edge intelligence but remains challenging due to tight memory, storage, and computation constraints. Existing approaches, such as model compression and hardware-aware neural architecture search (HW-NAS), often depend on proxy ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems  
**论文核心总结**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在 **Microcontroller Units (MCUs)** 上部署 Neural Networks (NNs) 是实现边缘智能（Edge Intelligence）的关键，但由于 MCUs 存在严格的 **memory、storage 和 computation 资源限制**，传统模型往往无法直接部署。现有方法如 Model Compression 和 Hardware-aware NAS (HW-NAS) 存在以下问题：

- 依赖 **proxy metrics**（如参数量、FLOPs），不能准确反映实际部署可行性；
- 搜索成本高，需数百 GPU 小时；
- 架构设计与实际部署验证脱节，导致“可训练但不可部署”。

AutoMCU 正是为解决这一 **“设计-部署鸿沟”** 而提出。

---

### 🚀 提出的新方法与创新点

AutoMCU 是一个基于 **Large Language Model (LLM)** 的 **Multi-Agent System (MAS)**，用于在 MCU 约束下自动定制神经网络。其核心创新包括：

#### （1）**Feasibility-First 搜索范式**
- 不再以 accuracy-efficiency Pareto 优化为目标，而是将 **backend-verified deployability** 作为首要硬约束。
- 在训练前通过 vendor toolchain（如 STM32Cube.AI）进行 **early feasibility filtering**，避免浪费计算资源在无法部署的模型上。

#### （2）**Hardware-in-the-Loop Architecture Generation (HAG)**
- LLM 生成的候选架构必须是 **structured and constructible** 的 JSON 规格描述；
- 通过工具链提前分析 RAM、Flash 占用及 operator 兼容性，过滤不满足约束的设计。

#### （3）**State-Isolated Multi-Agent Scheduling (MSIM)**
- 引入 **Supervisor Agent** 统一调度 Proposal、Training、Evaluation & Conversion 三个模块；
- 各 Agent **状态隔离**，仅通过结构化摘要通信，提升系统稳定性与可控性；
- 避免共享上下文带来的 token 膨胀与行为漂移。

#### （4）**闭环优化流程**
- 形成 Proposal → Screening → Training → Evaluation → Feedback 的完整闭环；
- 利用历史反馈指导后续提案，实现高效收敛。

---

### 🔍 相比现有方法的优势

| 对比维度 | 传统 HW-NAS / Compression | AutoMCU |
|--------|--------------------------|--------|
| 部署验证 | 最终验证，常失败 | **早期即验证，只训练可行模型** |
| 搜索效率 | 数百 GPU 小时 | **约 1–2 小时** |
| 可靠性 | 依赖 proxy 指标 | **真实 backend 数据驱动** |
| 自动化程度 | 多阶段手动衔接 | **端到端闭环自动化** |
| 稳定性 | 易受搜索策略影响 | **多 Agent 隔离 + 结构化交互，更稳定** |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
- **CIFAR-10 / CIFAR-100**：主基准测试，保留原始 32×32 分辨率以贴近 MCU 实际内存限制；
- **MNIST / FashionMNIST**：用于低资源场景补充验证；
- **NAS-Bench-201**：用于与 LLM-based NAS 方法（GENIUS）公平比较。

> ⚠️ 特别说明：未对图像上采样至 224×224，因会占用高达 147KB RAM，超出多数 MCU 容量。

---

### ⚙️ 实验设置与评估指标

#### 硬件约束条件
- **宽松设置**：RAM ≤ 1024KB, Flash ≤ 1024KB
- **严格设置**：RAM ≤ 256KB, Flash ≤ 512KB
- **极低资源**：RAM ≤ 64KB, Flash ≤ 64KB

#### 主要评估指标
| 指标 | 描述 |
|------|------|
| **Accuracy (%)** | 测试集分类准确率 |
| **RAM Usage (KB)** | 运行时内存占用（由 STM32Cube.AI 报告） |
| **Flash Usage (KB)** | 模型存储大小（含权重与代码） |
| **Search Time (GPU Hours)** | 整体定制耗时 |
| **Search Cost ($)** | 包括 GPU 租赁与 LLM token 消耗 |
| **Failure Rate** | 多 Agent 协作中异常终止的比例 |

#### LLM 配置
- 主要使用 **DeepSeek-V3.2** API；
- 温度设为 0，确保确定性输出；
- 对比实验也测试了 **MiMo-V2-Flash** 与 **Qwen-Plus** 以验证鲁棒性。

---

### 🆚 基线方法对比

| 类型 | 方法 | 简介 |
|------|------|------|
| **MCU-oriented HW-NAS** | `uNAS` | 基于进化算法的约束 NAS，建模 RAM/Flash/延迟 |
| | `ColabNAS` | 基于奥卡姆剃刀原则渐进扩展模型 |
| **LLM-based NAS** | `GENIUS` | 使用 LLM 进行语言引导的迭代搜索 |
| **Open-source NAS Models** | `MCUNet`, `MnasNet`, `FairNAS` | 已发布的轻量化模型 |
| **经典轻量模型** | `MobileNetV2`, `ShuffleNetV2`, `SqueezeNet` | 手工设计的高效架构 |

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（来自 Table I）

#### 在 **CIFAR-10, RAM≤256KB, Flash≤512KB** 设置下：

| 方法 | Accuracy (%) | RAM (KB) | Flash (KB) | Search Time (GPUh) |
|------|---------------|-----------|-------------|---------------------|
| uNAS [20] | 87.88 | 580.92 ❌ | 872.34 ❌ | 173.87 |
| ColabNAS [22] | 56.71 | 162.50 ✅ | 98.35 ✅ | 1.58 |
| **AutoMCU (Ours)** | **87.62 ± 0.52** | **124.84 ± 23.80 ✅** | **466.55 ± 34.61 ✅** | **1.56 ± 1.25** |

> ✅ 表示满足资源约束；❌ 表示超限

👉 AutoMCU 在保持接近 uNAS 的高精度的同时，**RAM 减少 ~79%，Flash 减少 ~47%**，且搜索时间从 **上百小时降至约 1.5 小时**。

---

#### 在 **CIFAR-100** 上的表现（相同严格约束）：

| 方法 | Accuracy (%) | RAM (KB) | Flash (KB) |
|------|---------------|-----------|-------------|
| uNAS | 58.82 | 349.00 ❌ | 1448.15 ❌ |
| ColabNAS | 41.26 | 163.00 ✅ | 371.02 ✅ |
| **AutoMCU** | **58.70 ± 0.71** | **138.21 ± 57.10 ✅** | **481.49 ± 28.43 ✅** |

👉 在更复杂任务上仍能实现 **接近 uNAS 的精度 + 满足部署约束 + 极低搜索开销**。

---

### 🔬 消融实验结果（Table IV）

| 变体 | Accuracy (%) | RAM (KB) | Flash (KB) | Time (GPUh) | Failure Rate |
|------|---------------|-----------|-------------|--------------|---------------|
| **Full AutoMCU** | 87.62 | 124.84 | 466.55 | 1.56 | 0% ✅ |
| w/o MSIM | 87.48 | 111.10 | 463.03 | 1.28 | **50%** ❌ |
| w/o HAG | 82.89 | 108.51 | 299.60 | 3.81 | 0% |
| Baseline (随机搜索 + 共享上下文) | 81.06 | 147.32 | 147.32 | 3.36 | **60%** ❌ |

#### 发现：
- **MSIM** 对系统稳定性至关重要：去除后失败率飙升至 50%，token 消耗翻倍；
- **HAG** 显著提升搜索效率与质量：无 HAG 时精度下降明显，搜索时间增加 2.4 倍；
- 两者结合才能实现 **高效、可靠、低失败率** 的自动化定制。

---

### 💡 超低资源场景表现（Table II）
在 **RAM≤64KB, Flash≤64KB** 下：
- CIFAR-10 达到 **76.36%** 准确率；
- MNIST 达到 **99.23%**；
- FashionMNIST 达到 **91.28%**；
👉 表明 AutoMCU 在极端受限环境下依然有效。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Backend-Verified Feasibility 是关键**
   - 仅靠 proxy metrics 无法保证部署成功；
   - 将 vendor toolchain 集成进优化环路，显著提升“可部署性”。

2. **LLM + Structured Workflow > Black-box Search**
   - GENIUS 等纯 prompt-driven 方法波动大（std 高达 2.28%）；
   - AutoMCU 采用结构化 proposal + 历史反馈机制，在 NAS-Bench-201 上取得更高均值与更低方差（std 仅 0.85%）。

3. **自动化 ≠ 不稳定**
   - 通过 **state-isolated multi-agent design**，实现了长时间运行下的高可靠性（0% 失败率）；
   - 相比共享上下文模式，token 消耗减少近半。

4. **真实设备验证成功**
   - 在 **STM32F407VET6**（低端 Cortex-M4）和 **STM32H723ZGT6**（高端 Cortex-M7）上均成功部署；
   - 模型能自适应不同硬件资源分配容量，实现精度与资源平衡。

---

### ⚠️ 局限性

1. **当前聚焦 Image Classification**
   - 尚未扩展至目标检测、语音识别等 TinyML 任务；
2. **依赖特定 Vendor Toolchain**
   - 当前主要集成 STM32Cube.AI，其他平台需适配；
3. **LLM 成本敏感**
   - 若使用高价 LLM（如 Qwen-Plus），token 成本可能上升；
4. **搜索空间仍有限制**
   - 虽灵活但仍限定于预定义 building blocks（如 GhostBlock、ConvBlock）。

---

### 🔮 未来工作方向

1. **拓展至更多 TinyML 任务**
   - 如 object detection、speech command recognition；
2. **支持更多异构 backend**
   - 集成 TensorFlow Lite Micro、ARM CMSIS-NN、NPU 工具链；
3. **融合更先进的 NAS 与硬件建模技术**
   - 结合 differentiable NAS 或 latency predictor 提升搜索质量；
4. **跨平台迁移能力**
   - 实现一次配置，多 MCU 平台自动适配；
5. **降低 LLM 开销**
   - 探索本地小模型代理或缓存机制。

---

## ✅ 总结

AutoMCU 提出了一种 **面向实际部署可行性的 LLM-based 多智能体框架**，解决了传统方法“训得好却跑不了”的痛点。其实验表明：

> **在严格 MCU 约束下，AutoMCU 可在约 1–2 小时内自动定制出高精度、可部署的模型，性能媲美需数百 GPU 小时的传统 HW-NAS 方法，且稳定性与成功率显著更高。**

该工作推动了 **LLM for Systems** 与 **Automated Edge AI** 的深度融合，为 TinyML 自动化开辟了新路径。

</details>

---

### 13. [stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800)

**Authors**: Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin, Dan Haramati, Damien Scieur, Yann LeCun, Randall Balestriero  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.21800v1  

#### Abstract
World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation —— 论文总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

当前 **World Model** 研究面临三大瓶颈，严重阻碍了可复现性和公平比较：

1. **实现碎片化（Implementation Fragmentation）**  
   不同研究团队各自为政，重复实现相同的算法（如 CEM、MPPI），导致代码不一致、隐藏 bug，难以判断性能提升是源于方法改进还是实现差异。

2. **数据加载瓶颈（Data Bottleneck）**  
   多模态时序数据（视频帧、动作、状态等）的高效加载困难。传统格式如 MP4 随机访问慢，HDF5 存储冗余大，导致 GPU 利用率低（GPU starvation）。

3. **缺乏标准化评估协议（Lack of Standardized Evaluation）**  
   现有基准大多在训练分布内测试，无法有效衡量模型对 **out-of-distribution (OOD)** 和 **zero-shot generalization** 的鲁棒性，掩盖了模型对环境动态理解的根本缺陷。

---

### ✅ 提出了什么新方法或新思路

作者提出 **stable-worldmodel (swm)** —— 一个开源、模块化、端到端的世界模型研究平台，旨在统一整个研究流程。

其核心创新点包括：

#### （1）高性能 Lance 数据层
- 采用 **Lance** 作为默认存储格式，一种专为机器学习优化的列式存储格式。
- 支持原生读写 **MP4、HDF5、LeRobot** 数据，并提供一键转换工具。
- 实现高吞吐、低延迟的随机访问，显著缓解 I/O 瓶颈。

#### （2）干净、可复现的 Baseline 实现
- 提供经过充分测试的现代世界模型和规划器实现，包括：
  - **World Models**: DINO-WM, PLDM, LeWM, TD-MPC2
  - **Planners**: CEM, iCEM, MPPI, GD, PGD, GRASP
- 所有实现均通过统一接口集成，确保公平比较。

#### （3）系统化的鲁棒性评估套件
- 构建覆盖多个领域的环境家族：
  - Classic Control（如 CartPole）
  - MuJoCo（连续控制）
  - Arcade Games（Atari）
  - Robotics（Fetch, Push-T）
  - Open-World（Craftax）
- 引入 **可控的变异因子（Factors of Variation, FoV）**，支持在视觉、几何、物理维度上进行系统扰动：
  - 视觉：颜色、光照、纹理、遮挡
  - 几何：大小、形状、位置
  - 物理：质量、摩擦、重力

---

### ✅ 相比现有方法的优势

| 维度 | 优势 |
|------|------|
| **可复现性** | 统一代码库避免“魔改”实现，所有结果可在相同环境下复现 |
| **效率** | Lance 格式实现最高数据吞吐（>5k samples/sec），优于 HDF5 和 MP4 |
| **评估全面性** | 支持 in-distribution、OOD、zero-shot、long-horizon 等多种评估模式 |
| **灵活性** | 用户可自由替换模型架构，平台仅标准化数据、评估和控制部分 |
| **生态兼容** | 无缝集成 LeRobot、Stable-Baselines3 等主流框架 |

---

## 2. 核心实验方法和设置

### 📦 使用的数据集

- **Push-T**：2D 操作任务，使用 DINO-WM 发布的专家数据集。
- **OGBench**：3D 操作与场景理解。
- **DeepMind Control Suite (DMC)**：标准连续控制任务（如 Cheetah Run, Walker Walk）。
- **Atari (ALE)**：100+ 游戏用于离散控制评估。
- **Craftax**：程序生成的 2D 生存游戏，测试开放世界泛化能力。
- 所有数据均支持转换为 **Lance** 格式以提升加载效率。

---

### ⚙️ 实验设置和评估指标

#### 评估协议
- **Dataset-driven Evaluation**：从已有轨迹中采样起始帧 `o_t` 和目标帧 `o_{t+Δ}`，固定时间偏移 Δ=25，保证目标可达。
- **Episodic Evaluation**：在线随机重置并生成任务。
- **Zero-shot Generalization**：在训练分布外的数据上直接测试，不进行微调。

#### 评估指标
| 指标 | 说明 |
|------|------|
| **Success Rate (SR)** | 主要指标，表示成功到达目标的比例 |
| **Time-to-goal** | 成功任务中的平均步数 |
| **Wall-clock latency per planning step** | 单次规划耗时 |
| **Prediction MSE** | 轨迹级预测误差，用于分析与规划成功率的关系 |

#### 控制变量
- 所有模型在相同数据集上训练。
- 规划器统一使用 **CEM**（除非特别说明），配置为：30 迭代、300 候选、30 精英。
- 规划预算（eval_budget）设为 50 步。

---

### 🔁 基线方法对比

| 方法 | 类型 | 是否使用 MPC |
|------|------|-------------|
| **TD-MPC2** | Reward-driven implicit world model | ✅ |
| **GCBC** | Goal-conditioned Behavioral Cloning | ❌ |
| **PLDM** | JEPA-style latent world model | ✅ |
| **LeWM** | Simplified JEPA with SIGReg | ✅ |
| **DINO-WM** | Frozen DINOv2 encoder + ViT predictor | ✅ |

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（Push-T 任务）

| Method | Success Rate (%) |
|--------|------------------|
| **TD-MPC2** | 12 |
| **GCBC** | 75 |
| **LeWM** | 94 |
| **PLDM** | 78 |
| **DINO-WM** | 92 |

> ✅ **LeWM 和 DINO-WM 表现最佳**，验证了基于预训练视觉特征或简化正则化的有效性。

---

### 🔍 OOD 鲁棒性分析（Push-T）

#### （1）渐进分布偏移下的表现

| 设置 | LeWM SR (%) | PLDM SR (%) |
|------|------------|------------|
| Expert (train) | 88 | 73 |
| Expert (valid) | 84 | 68 |
| Random policy | 51 | 51 |
| Random + FoV | 30 | 30 |

> 🔴 即使轻微扰动，成功率也大幅下降，表明当前模型 **极度依赖训练分布**。

#### （2）单一视觉因子扰动（Table 4）

| FoV | Entity | LeWM (%) | PLDM (%) | DINO-WM (%) |
|-----|--------|----------|----------|-------------|
| Color | Agent | 12.0 | 8.0 | 18.0 |
| Size | Agent | 22.0 | 18.0 | 4.0 |
| Shape | Agent | 26.0 | **52.0** | 18.0 |
| Canvas | Background | 6.0 | 6.0 | 10.0 |

> 💡 **PLDM 对 agent 形状变化异常鲁棒**（52%），但对颜色敏感；**DINO-WM 对 agent 尺寸变化极脆弱**（仅 4%）。

#### （3）背景色连续变化（Fig. 11）

- LeWM 在接近白色或绿色背景时表现良好（与原始环境匹配）。
- 当背景变为红、蓝、紫时，成功率急剧下降。
> 🧠 模型可能依赖特定前景-背景颜色对比，而非几何结构。

---

### 📉 预测误差 vs. 规划成功率

- 图 4 和图 10 显示：**成功与失败轨迹的预测 MSE 分布高度重叠**。
- 即使预测误差很低，也可能规划失败；反之亦然。

> ❗ **预测准确性 ≠ 规划鲁棒性**。当前模型可能学到的是表面相关性，而非真正的动力学规律。

---

### ⚡ 数据加载性能对比（Fig. 3 & 8）

| Format | Local Throughput (samples/sec) | S3 Streaming | Storage Size |
|--------|-------------------------------|--------------|---------------|
| HDF5 (local) | ~1,400 | ~975 | 43.12 GB |
| MP4 (local) | ~1,300 | — | 496 MB |
| **Lance (local)** | **~4,800** | **~3,200** | **13.31 GB** |

> ✅ **Lance 在吞吐量上领先 3–4 倍**，同时保持良好的压缩比，是理想的训练数据格式。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **当前世界模型仍非常脆弱**  
   即使是轻微的颜色、大小、背景变化，也会导致规划成功率断崖式下跌，**zero-shot 泛化能力远未解决**。

2. **预测误差不是可靠指标**  
   低 MSE 并不能保证高成功率，说明模型可能“拟合轨迹但未理解物理”。

3. **Lance 显著提升训练效率**  
   高吞吐数据加载有效缓解 GPU 等待问题，尤其适合大规模、长序列训练。

4. **统一平台极大降低研究门槛**  
   swm 使得研究人员可以专注于模型设计，而无需重复构建数据管道、规划器或评估逻辑。

---

### ⚠️ 方法的局限性

1. **目前主要面向仿真环境**  
   虽支持 LeRobot，但 sim-to-real 迁移尚未深入探索。

2. **FoV 在闭源环境中受限**  
   如 Atari ROMs 只能通过视觉 wrapper 施加扰动，无法修改内部物理参数。

3. **长期规划挑战仍未突破**  
   随着规划步数增加，误差累积严重，大多数模型在长视界任务中表现不佳。

---

### 🔮 未来工作方向

1. **推动 sim-to-real 转移**  
   扩展 swm 支持真实机器人实时交互与在线训练。

2. **支持异步与实时交互**  
   实现更贴近现实世界的流式数据处理与决策。

3. **开展 Scaling Laws 研究**  
   利用 swm 的高效 pipeline 探索世界模型在数据、参数、计算规模上的扩展规律。

4. **构建公开 Leaderboard**  
   跟踪 SOTA 方法进展，促进社区协作与公平竞争。

5. **引入更复杂的物理扰动**  
   如动态摩擦、非刚体变形、接触力学变化等，进一步挑战模型的动力学理解能力。

---

> **总结**：  
> `stable-worldmodel` 不只是一个工具包，更是推动世界模型研究走向 **标准化、可复现、可比较** 的基础设施。它揭示了当前方法在鲁棒性上的根本不足，并为下一代真正“理解世界”的智能体研究提供了坚实平台。

</details>

---

### 14. [PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models](https://arxiv.org/abs/2605.20873)

**Authors**: Ziliang Zhao, Zenan Xu, Shuting Wang, Hongjin Qian, Yan Lei, Minda Hu, Zhao Wang, Shihan Dou, Zhicheng Dou, Pluto Zhou  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.20873v1  

#### Abstract
Planning is a fundamental capability for large language models (LLMs) because such complex tasks require models to coordinate goals, constraints, resources, and long-term consequences into executable and verifiable solutions. Existing planning benchmarks, however, usually treat planning data as fixe...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：PlanningBench**

---

## **1. 主要贡献和创新点**

### **解决的问题**
现有的 LLM 规划（Planning）评测基准存在以下局限：
- **静态固定**：大多数规划数据集是固定的实例集合，缺乏可扩展性和多样性。
- **难度控制粗糙**：难度通常由任务长度、要求数量等表面特征决定，而非结构性因素（如约束耦合、资源稀缺性）。
- **验证困难**：缺少自动化的、细粒度的验证机制，难以支持训练导向的反馈。
- **训练价值有限**：多数基准仅用于评估，无法有效支持强化学习等训练范式。

这些问题导致模型在复杂、真实场景下的规划能力难以被准确评估和持续提升。

### **提出的新方法与思路**
本文提出了 **PlanningBench**，一个面向大语言模型（LLMs）的**可扩展、多样化且可验证的规划数据生成框架**。其核心创新包括：

#### **(1) 基于真实场景的结构化任务与约束分类法（Taxonomy）**
- 从现实规划场景中抽象出超过 **30 种任务类型**，涵盖六大类别：
  - Scheduling and Timetabling
  - Allocation and Matching
  - Shift and Workforce Scheduling
  - Routing and Travel
  - Project and Production Operations
  - Emergency Response and Public Service
- 构建了多层级的**约束分类体系**，分为：
  - General constraints（通用）
  - Task-specific constraints（任务特定）
  - Specialized stateful constraints（状态依赖）
- 每类约束进一步按难度分为 Basic、Medium、Hard 三级，实现**可控难度增强**。

#### **(2) 约束驱动的合成流水线（Constraint-driven Synthesis Pipeline）**
采用闭环生成架构，包含三个组件：
- **Generator**：基于任务-约束配置生成自包含的规划问题。
- **Responder**：调用 LLM 尝试求解。
- **Critic**：根据预定义的 verification checklist 进行自动评分与反馈。
该机制实现了：
- **自适应难度控制**：当当前 Responder 能完全通过时，系统自动增加 Hard 级别约束的比例。
- **质量过滤与修订**：结合人工审核确保数据可用性。

#### **(3) 面向训练与评估的双重用途设计**
- 所有生成实例均附带 **verification checklist**，可用于：
  - 完整解决方案评估（All-pass）
  - 强化学习中的奖励信号构建
- 特别强调 **determinate optimal solutions**（确定性最优解），以提供更清晰、稳定的训练信号。

### **相比现有方法的优势**
| 维度 | 现有方法（如 TravelPlanner, ChinaTravel 等） | PlanningBench |
|------|---------------------------------------------|----------------|
| **数据来源** | 固定收集 | 可控生成 |
| **领域覆盖** | 单一或少数领域（如旅行） | >30 类任务，广泛覆盖 |
| **难度控制** | 表面代理（prompt 长度） | 结构化控制（约束紧度、资源稀缺、目标冲突） |
| **可扩展性** | 有限 | 高度可扩展 |
| **验证支持** | 手动或弱自动化 | 自动化 checklist + 闭环验证 |
| **训练支持** | 缺乏 | 支持 GRPO 等强化学习 |

> ✅ **优势总结**：PlanningBench 将“规划数据”从**静态基准**转变为**可控生成系统**，兼具真实性、多样性、可验证性与训练友好性。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **PlanningBench 自身**：
  - 包含 **467 个生成的评估实例**（用于测试）
  - **300 个训练实例**（用于 RL 训练）
- **外部迁移评估集**（用于检验泛化能力）：
  - **ChinaTravel**（Shao et al., 2024a）
  - **TravelPlanner**（Xie et al., 2024）
- **通用指令遵循与推理基准**：
  - **Multi-Challenge**, **Inverse IFEval**, **Collie**

### **实验设置**

#### **(1) 评估设置**
- **模型范围**：涵盖多个开源与闭源前沿 LLMs，包括：
  - GPT-5.4 系列、Gemini-3-1-pro、Seed-2.0-pro、DeepSeek-V3.2、Qwen3 系列等
- **协议统一**：所有模型使用默认推理参数进行查询。
- **评判模型**：使用 **GPT-oss-120b** 作为 Judge Model 对输出进行 checklist 检查。

#### **(2) 评估指标**
- **All-pass (%)**：计划满足 checklist 中**所有条目**的比例 → 衡量完整解决方案的成功率。
- **Avg-pass (%)**：平均满足的 checklist 条目比例 → 衡量局部合规程度。
- 二者差距揭示了“局部正确 ≠ 全局一致”的关键挑战。

#### **(3) 训练设置（GRPO-based RL）**
- **基础模型**：`Qwen-A3B-30B`
- **训练方式**：GRPO（Group Relative Policy Optimization）
- **对比设置**：
  - **Base Model**：未训练原模型
  - **Human-Authored**：人工编写的数据集（同规模）
  - **Syn-NotDetOptimal**：不强调确定性最优解的合成数据
  - **Syn-PlanningBench**：本文提出的高质量合成数据

---

## **3. 主要实验结果和性能指标**

### **(1) 在 PlanningBench 上的评估结果（表 2）**

| 模型 | All-pass (%) | Avg-pass (%) |
|------|--------------|--------------|
| **GPT-5.4-xhigh** | **63.17** | **92.35** |
| GPT-5.4-high | 58.56 | 84.60 |
| Gemini-3-1-pro | 53.25 | 88.36 |
| Seed-2.0-pro-high | 44.33 | 84.02 |
| Qwen3-30b-moe | 12.15 | 57.40 |
| Qwen3-32b | 0.27 | 30.11 |
| Qwen3-8b | 0.00 | 22.79 |

> 🔍 **关键观察**：
> - 即使最强模型（GPT-5.4-xhigh）也仅有 **63.17% 的 All-pass 率**，说明任务远未饱和。
> - **All-pass 与 Avg-pass 差距显著**（如 GPT-5.4-medium: 90.03% vs 58.09%），表明模型常满足多数约束但仍因小错误失败 → 暴露全局一致性缺陷。

### **(2) 外部迁移性能对比（表 4 & 表 5）**

#### **在外部规划基准上的表现（TravelPlanner & ChinaTravel）**

| 方法 | ChinaTravel All-pass ↑ | TravelPlanner All-pass ↑ |
|------|------------------------|---------------------------|
| Base Model | 50.92 | 28.85 |
| Human-Authored | 52.41 (+1.49) | 33.86 (+5.01) |
| **Syn-PlanningBench** | **58.36 (+7.44)** | **46.86 (+18.01)** |

✅ **结论**：使用 PlanningBench 数据训练后，在未见过的规划任务上取得显著提升，尤其在需要强约束整合的任务中效果明显。

#### **在通用指令基准上的泛化能力（表 5）**

| 方法 | Multi-Challenge ↑ | Inverse IFEval ↑ | Collie ↑ | Avg ↑ |
|------|-------------------|------------------|----------|-------|
| Base Model | 29.18 | 48.72 | 38.33 | 38.74 |
| Syn-NotDetOptimal | 30.28 | 48.02 | 40.17 | 39.49 |
| **Syn-PlanningBench** | **33.09** | **51.14** | **53.17** | **45.80** |

✅ **结论**：PlanningBench 不仅提升规划能力，还增强了模型在复杂指令理解、约束跟踪与全局一致性方面的通用能力。

### **(3) 消融实验与训练动态分析（图 4）**

- **Syn-PlanningBench** 的训练曲线最稳定：
  - Solve-all ratio 上升最快
  - Solve-none ratio 下降最迅速
  - Critic reward 更平滑
- 相比之下，**Syn-NotDetOptimal**（无明确最优解偏好）训练不稳定，solve-all ratio 增长缓慢。

> 📌 **关键发现**：**determinate optimal solutions** 提供了更强的方向性奖励信号，对训练稳定性至关重要。

---

## **4. 关键结论和发现**

### **主要发现**
1. **当前 LLMs 的规划能力仍有显著瓶颈**：
   - 即使最强模型在 PlanningBench 上也无法达到完美 All-pass。
   - 错误主要源于 **Wrong Calculation/Assignment**（占语义错误的 60.9%~83.5%），而非格式问题。

2. **PlanningBench 是有效的训练信号源**：
   - 在未见规划任务（如 TravelPlanner）上实现显著迁移增益。
   - 同时提升通用指令遵循与复杂推理能力（如 Collie +14.84 pts）。

3. **确定性最优解对训练至关重要**：
   - 具有明确最优解的实例能提供更集中、更稳定的奖励信号。
   - “模糊可行”会导致奖励稀疏，不利于全局一致性学习。

4. **结构化难度优于表面复杂度**：
   - 约束耦合、资源稀缺、目标冲突等结构性因素更能反映真实规划挑战。
   - 实验显示 All-pass 随 checklist 数量增加而下降，验证了难度控制有效性。

### **局限性**
- **数据尚未公开**：论文声明数据将于 **2026年6月1日前发布**，目前无法复现。
- **依赖强 LLM 作为 Generator/Critic**：生成质量受限于上游模型能力。
- **文本规划为主**：暂未涉及多模态或具身智能体（embodied agents）的交互式规划。

### **未来工作方向**
- 扩展至 **multi-modal planning** 和 **interactive simulation environments**。
- 探索 **human-in-the-loop refinement** 以进一步提升数据质量。
- 将 PlanningBench 应用于 **agent architecture design** 与 **tool-use policy learning**。
- 构建 **dynamic planning benchmarks**，支持在线调整与反馈。

---

> ✅ **总体评价**：  
> PlanningBench 成功将“规划能力评测”从**静态快照**升级为**动态生成引擎**，不仅提供了新的评估标准，更为 LLM 的**可验证训练**开辟了新路径。其强调的 **structural difficulty control** 与 **determinate objectives** 设计原则，为未来高质量 AI 训练数据的设计提供了重要范式。

</details>

---

### 15. [AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](https://arxiv.org/abs/2605.21082)

**Authors**: Minghao Chen, Xinyi Hu, Zhou Yu, Yufei Yin  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.21082v1  

#### Abstract
Large Language Model (LLM) based agents have demonstrated proficiency in multi-step interactions with graphical user interfaces (GUIs). While most research focuses on improving single-task performance, practical scenarios often involve repetitive GUI tasks for which invoking LLM reasoning repeatedly...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
传统 **LLM-based GUI Agent**（如 ReAct 范式）在处理重复性 GUI 任务时效率低下，每次执行都需要调用昂贵的 LLM 进行推理，导致 **token 开销大、运行时间长**。而传统的 **Robotic Process Automation (RPA)** 虽然运行高效，但依赖人工编写脚本，维护成本高且对界面变化敏感。

本文旨在解决这一矛盾：如何**自动合成高效、鲁棒、可复用的 RPA 函数**，用于处理特定任务类型（task type）的重复性 GUI 自动化任务。

---

### 提出了什么新方法或新思路
作者提出 **AutoRPA**，一个通过 LLM 驱动从交互中合成 RPA 代码的框架。其核心思想是“**蒸馏决策逻辑**”——将 ReAct 式 LLM Agent 在探索过程中的成功轨迹，转化为可复用的 RPA 脚本。

#### 核心创新点：
1. **Translator-Builder Pipeline**
   - **Translator Agent**：将 ReAct Agent 输出的硬编码动作（hard-coded actions，如 `click(index=2)`）转换为软编码动作（soft-coded actions），即基于元素语义属性（如 `text`, `content_description`）动态定位元素的代码片段，提升鲁棒性。
   - **Builder Agent**：基于多个软编码轨迹，利用 **Retrieval-Augmented Generation (RAG)** 机制，从树状结构的轨迹数据库中检索相关信息，综合生成健壮的 RPA 函数。

2. **Hybrid Repair Strategy（混合修复策略）**
   - 当生成的 RPA 代码执行失败时，不直接调试代码，而是启动 **ReAct Agent 从断点继续执行**，产生修复示范。
   - 将该修复轨迹反馈给 Builder Agent，用于迭代优化代码，实现闭环改进。

---

### 相比现有方法的优势
| 方法 | 缺陷 | AutoRPA 的优势 |
|------|------|----------------|
| **ReAct-style Agents** | 每次执行都需 LLM 推理，token 成本高 | 生成后仅执行轻量级 RPA，token 消耗降低 **82%~96%** |
| **Direct Code Generation** | LLM 难以一次性生成长周期、鲁棒的 GUI 代码 | 通过探索-翻译-合成流程，逐步构建可靠代码 |
| **Skill Learning (e.g., ICE, ExpeL)** | 存储原始轨迹作为范例，仍依赖 LLM 决策 | 生成独立可执行的 RPA 函数，无需 LLM 参与运行时决策 |
| **Traditional RPA** | 手工编写，难以适应界面变化 | 自动生成，具备环境适应性和参数泛化能力 |

---

## 2. 核心实验方法和设置

### 使用的数据集
实验在三个 GUI 环境上进行，涵盖移动、网页和模拟场景：
- **AndroidWorld**：真实的 Android 应用环境，包含 20 个应用中的 116 种任务类型，提供截图和 Accessibility Tree。
- **WebArena**：模拟真实网站的网页自动化基准，聚焦 Reddit 域的 19 种任务类型。
- **MiniWoB++**：模拟网页环境，支持键盘鼠标操作。选取其中 9 个有反馈的“困难”任务和共 53 个任务进行测试。

---

### 实验设置和评估指标
- **模型后端**：使用 GPT-4o、GPT-4.1、GPT-5 和 Claude-sonnet-4.5。
- **Building Stage**：
  - 每个任务类型采样 **N=3** 个实例用于构建 RPA。
  - ReAct Agent 最多反思重试 **N_ref=2** 次。
  - Builder Agent 最多重构代码 **M=3** 次以通过验证。
- **Testing Stage**：
  - 使用未见过的任务实例进行测试。
  - 对比“AutoRPA”（允许 fallback 到 ReAct）与“AutoRPA (code only)”（仅使用 RPA 代码）。

#### 评估指标：
- **Success Rate (%)**：任务完成率
- **Execution Time (min)**：平均执行时间
- **Token Consumption (k)**：每任务平均 token 消耗（千）

---

### 基线方法对比
| 类别 | 方法 |
|------|------|
| **ReAct Paradigm** | ReAct+, SeeAct, M3A, SteP |
| **Plan-and-Execute** | RCI, AdaPlanner |
| **Skill Learning + ReAct** | AutoGuide, AutoManual |
| **Advanced Agents** | Agent S3, Gemini-2.5-CU, Mobile-Agent-v3 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### AndroidWorld 结果（GPT-4.1）
| Method | Tokens (k) ↓ | Success (%) ↑ |
|--------|---------------|----------------|
| ReAct+ | 79.9 | 35.2 |
| AutoRPA (code only) | **2.6** | 34.3 |
| **AutoRPA** | **14.7** | **37.0** |

> AutoRPA 在成功率略优的情况下，token 消耗仅为 ReAct 的 **18.6%**。

#### MiniWoB++ 结果（GPT-4.1, Hard Tasks）
| Method | Tokens (k) ↓ | Success (%) ↑ |
|--------|---------------|----------------|
| ReAct+ | 16.2 | 84.4 |
| AutoManual | 23.2 | 91.1 |
| **AutoRPA (code only)** | **1.0** | 80.0 |
| **AutoRPA** | **1.4** | **91.1** |

> AutoRPA 以不到 **10% 的 token 消耗**，达到甚至超越最先进方法的成功率。

#### WebArena 结果（GPT-5）
- AutoRPA 与 SOTA 方法（如 M3A）成功率相当（~51.7%），但 token 消耗从 **>100k 降至 ~30k**。

---

### 与基线方法的对比结果
- **AutoRPA (code only)** 在所有基准上均显著优于 ReAct 范式方法的 token 效率（降低 **82%~96%**）。
- **AutoRPA** 整体表现优于或持平于当前最先进的 GUI Agent，同时保持极低的推理开销。
- 在 MiniWoB++ 上，AutoRPA 是唯一能在仅提供简单演示（如“click-button”）的情况下，成功生成通用 RPA 的方法，而 AdaPlanner 和 AutoManual 依赖大量专家示例。

---

### 消融实验结果（Ablation Study）

#### 表：消融关键组件的影响（AndroidWorld, GPT-4.1）
| Variant | Success (%) |
|--------|-------------|
| **Full AutoRPA** | **51.7** |
| w/o ReAct (直接生成) | 32.5 |
| w/o Translator | 40.2 |
| w/o ReAct in Repair | 45.5 |
| w/o RAG in Builder | 48.8 |

> 结果表明：
> - **ReAct 探索阶段**至关重要，缺失时成功率下降近 20%。
> - **Translator Agent** 显著提升代码鲁棒性。
> - **Hybrid Repair** 和 **RAG** 均对最终性能有正向贡献。

#### 构建任务数量影响（N）
- 随着构建任务数 $N$ 增加，测试成功率持续上升。
- 当 $N \geq 3$ 时，性能趋于稳定，说明少量成功轨迹即可支撑高质量 RPA 生成。

---

## 4. 关键结论和发现

### 主要发现
1. **LLM Agent 的交互轨迹可以被有效“蒸馏”为高效 RPA 代码**，实现从高成本推理到低成本执行的转变。
2. **Translator-Builder Pipeline** 能够将脆弱的硬编码动作转化为基于语义匹配的鲁棒代码。
3. **Hybrid Repair + RAG** 机制显著提升了代码的泛化能力和修复效率。
4. **AutoRPA 在 token 和时间效率上远超现有方法**，同时保持竞争力甚至更优的成功率。
5. 生成的 RPA 代码具有良好的**参数化和逻辑结构**（如条件判断、循环），能应对任务变体和界面变化。

---

### 方法的局限性
1. **依赖强 MLLM 能力**：框架性能受限于底层 LLM（如 GPT-4.1）的能力，弱模型可能无法生成正确轨迹或代码。
2. **对 GUI 环境有要求**：
   - 需提供 DOM 或 Accessibility Tree 以便元素定位。
   - 用户需提供多个同类型任务用于训练。
3. **ReAct Agent 在复杂任务上探索能力有限**：若初始轨迹失败，后续蒸馏无从谈起。
4. **Builder Agent 工具使用不成熟**：存在过度或不足使用 `fetch_info` 工具的问题，影响代码质量。

---

### 未来工作方向
1. **自动化奖励生成与任务探索**：让 LLM Agent 自主生成任务并判断完成状态，减少人工干预。
2. **增强探索能力**：结合 Tree Search 等搜索算法提升 ReAct Agent 在难任务上的成功率。
3. **轻量化部署**：进一步压缩 RPA 代码，适配边缘设备或低资源环境。
4. **跨平台统一接口**：扩展至桌面、IoT 等更多 GUI 场景。
5. **支持在线增量学习**：在部署过程中持续收集新轨迹，动态更新 RPA 函数。

--- 

> ✅ **总结一句话**：  
> **AutoRPA 成功桥接了 LLM Agent 的灵活性与 RPA 的高效性，通过“交互→蒸馏→执行”的范式，为重复性 GUI 任务提供了极具成本效益的自动化解决方案。**

</details>

---

### 16. [DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA](https://arxiv.org/abs/2605.22411)

**Authors**: Jianing Yin, Tan Tang  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.22411v1  

#### Abstract
Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are...

---

### 17. [Riemannian geometry meets fMRI: the advantages of modeling correlation manifolds and eigenvector subspaces](https://arxiv.org/abs/2605.22334)

**Authors**: Mario Severino, Manuela Moretto, Robert A. McCutcheon, Mattia Veronese  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.22334v1  

#### Abstract
Correlation matrices are fundamental summaries of functional brain networks, yet standard analyses often treat entries independently, ignoring the curved geometry of correlation space. Existing geometric methods frequently lack closed-form operations or depend on arbitrary region ordering, limiting ...

---

### 18. [Don't Collapse Your Features: Why CenterLoss Hurts OOD Detection and Multi-Scale Mahalanobis Wins](https://arxiv.org/abs/2605.21493)

**Authors**: Rahul D Ray  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.21493v1  

#### Abstract
The ability to detect out-of-distribution (OOD) inputs is fundamental to safe deployment of machine learning systems. Yet, current methods often rely on feature representations that are optimised solely for classification accuracy, neglecting the distinct requirements of epistemic uncertainty. We in...

---

### 19. [ASAP: Attention Sink Anchored Pruning](https://arxiv.org/abs/2605.22372)

**Authors**: Jaehyuk Lee, Hanyoung Kim, Yanggee Kim, Donghun Lee  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.22372v1  

#### Abstract
Vision Transformers (ViTs) face severe computational bottlenecks due to the quadratic complexity of self-attention at high resolutions. Existing token reduction methods rely on local metrics - such as single-layer attention scores - that are inherently vulnerable to the attention sink phenomenon, wh...

---

### 20. [OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind](https://arxiv.org/abs/2605.20423)

**Authors**: Sharmin Sultana Srishty, Kazi Mahathir Rahman, Malaika Parizat Sakkhi, Samia Shahid Prianna, Shaikhul Islam Sinat  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.20423v1  

#### Abstract
Large Language Models (LLMs) perform well on many language tasks, but their Theory of Mind (ToM) reasoning is still uneven in complex social settings. Existing benchmarks, including ExploreToM, do not always test the recursive beliefs and information asymmetries that make these settings difficult. T...

---

### 21. [Reflective Prompt Tuning through Language Model Function-Calling](https://arxiv.org/abs/2605.21781)

**Authors**: Farima Fatahi Bayat, Moin Aminnaseri, Pouya Pezeshkpour, Estevam Hruschka  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.21781v1  

#### Abstract
Large language models (LLMs) have become increasingly capable of following instructions and complex reasoning, making prompting a flexible interface for adapting models without parameter updates. Yet prompt design remains labor-intensive and highly sensitive to formatting, phrasing, and instruction ...

---

### 22. [Token-weighted Direct Preference Optimization with Attention](https://arxiv.org/abs/2605.21883)

**Authors**: Chengyu Huang, Zhuohang Li, Sheng-Yen Chou, Claire Cardie  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.21883v1  

#### Abstract
Direct Preference Optimization (DPO) aligns Large Language Models with human preferences without the need for a separate reward model. However, DPO treats all tokens in responses equally, neglecting the differing importance of individual tokens. Existing token-level PO methods compute the token weig...

---

### 23. [Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild](https://arxiv.org/abs/2605.22064)

**Authors**: Mao Zheng, Zheng Li, Tao Chen, Bo Lv, Mingrui Sun, Mingyang Song, Jinlong Song, Hong Huang, Decheng Wu, Hai Wang, Yifan Song, Yanfeng Chen, Guanwei Zhang, Guanghua Yu, Yi Su, Hong Liu, Jinxiang Ou, Keyao Wang, Weile Chen, Haozhao Kuang, Kai Wang, Nuo Chen, Zihao Zheng, Chenhao Wang, Bin Xing, Chengcheng Xu, Tinghao Yu, Binghong Wu, Long Xu, Jiacheng Shi, Yunhao Wang, Baifang Chen, Lei Zhang, Qi Yang, Zhao Wu, Jiacheng Li, Lan Jiang, Lanrui Wang, Kai Zhang, Shuaipeng Li, Zhongzhi Chen, Weixuan Sun, Jiaqi Zhu, An Wang, Wei Li, Jun Xia, Weidong Han, Wutian Yang, Litong Hui, Luoguo Jia, Jiajia Wu, Xinpeng Zhou, Tianxiang Fei  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.22064v1  

#### Abstract
Hy-MT2 is a family of fast-thinking multilingual translation models designed for complex real-world scenarios. It includes three model sizes: 1.8B, 7B, and 30B-A3B (MoE), all of which support translation among 33 languages and effectively follow translation instructions in multiple languages. For on...

---

### 24. [BeLink: Biomedical Entity Linking Meets Generative Re-Ranking](https://arxiv.org/abs/2605.22501)

**Authors**: Darya Shlyk, Stefano Montanelli, Lawrence Hunter  
**Category**: cs.CL  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.22501v1  

#### Abstract
Despite recent progress, Biomedical Entity Linking (BEL) with large language models (LLMs) remains computationally inefficient and challenging to deploy in practical settings. In this work, we demonstrate that instruction-tuning of open-source generative models can offer an effective solution when a...

---

### 25. [A Reproducible Log-Driven AutoML Framework for Interpretable Pipeline Optimization in Healthcare Risk Prediction](https://arxiv.org/abs/2605.21528)

**Authors**: Rui Huang, Lican Huang  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.21528v1  

#### Abstract
Accurate and reproducible disease risk prediction remains challenging due to heterogeneous features, limited samples, and severe class imbalance. This study introduces yvsoucom-iterkit, a deterministic and log-driven automated machine learning framework that formulates pipeline optimization as a ful...

---

### 26. [AgForce Enables Antigen-conditioned Generative Antibody Design](https://arxiv.org/abs/2605.21610)

**Authors**: Mansoor Ahmed, Murray Patterson  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.21610v1  

#### Abstract
Antibody design methods condition on antigen structure to generate complementarity-determining regions (CDR), yet a systematic evaluation of baseline methods reveals that they largely ignore the antigen input. We identify three failure modes that explain this behavior. Antigen blindness arises becau...

---

### 27. [Represented Is Not Computed: A Causal Test of Candidate Algorithmic Intermediates in a Transformer](https://arxiv.org/abs/2605.22488)

**Authors**: Ishita Darade, Sushrut Thorat  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.22488v1  

#### Abstract
Structured prompts require integrating components according to task-relevant relations. How a network implements this integration is often hard to judge in language or vision, where those relations are rarely specified precisely enough to define a candidate internal algorithm. Arithmetic offers a cl...

---

### 28. [Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery](https://arxiv.org/abs/2605.22613)

**Authors**: Halil Alperen Gozeten, Xuechen Zhang, Emrullah Ildiz, Ege Onur Taga, Tara Javidi, Samet Oymak  
**Category**: cs.LG  
**Published**: 2026-05-22  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.22613v1  

#### Abstract
Recent LLM-guided evolutionary search methods have shown that iterative program mutation can discover strong algorithms, but they typically optimize each task independently, even when related tasks share reusable structure. We introduce Evolutionary Multi-Task Optimization (EMO) for LLM-guided progr...

---

### 29. [Declarative Data Services: Structured Agentic Discovery for Composing Data Systems](https://arxiv.org/abs/2605.20690)

**Authors**: Shanshan Ye, Duo Lu  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.20690v1  

#### Abstract
Agentic discovery has shown that LLM-driven search can find novel algorithms, designs, and code under benchmark conditions. Translating the paradigm to multi-system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and...

---

### 30. [Towards Resilient and Autonomous Networks: A BlueSky Vision on AI-Native 6G](https://arxiv.org/abs/2605.21395)

**Authors**: Liang Wu, Kelly Wan, Mayank Darbari, Liangjie Hong  
**Category**: cs.AI  
**Published**: 2026-05-22  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.21395v1  

#### Abstract
The proliferation of emerging applications, such as autonomous driving and immersive experiences, demands cellular networks that are not only faster, but fundamentally more resilient and autonomous. This paper presents a BlueSky vision on how Artificial Intelligence will be natively integrated into ...

---

## 🔧 Configuration

This bot is configured to look for papers containing the following keywords:
- kv cache, offload, State Space, SSM, framework, System, Generation, Video, Linear, LLM, RL, RLHF, Inference, Training, Attention, Pipeline, MOE, Sparse, Quantization, Speculative, Efficient, Efficiency, Framework, Parallel, Distributed, Kernel, Decode, Decoding, Prefill, Throughput, Fast, Network, Hardware, Cluster, FP8, FP4, Optimization, Scalable, Communication

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
