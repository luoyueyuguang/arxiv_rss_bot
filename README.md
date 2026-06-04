# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-04 09:40:38 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.04511)

**Authors**: Yaosheng Fu, Guangxuan Xiao, Xin Dong, Song Han, Oreste Villa  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2606.04511v1  

#### Abstract
Sparse attention reduces compute and memory bandwidth for long-context LLM inference. However, two key challenges remain: (1) KV cache capacity still grows with sequence length, and offloading to CPU memory introduces a PCIe transfer bottleneck; (2) the sparse selection step itself retains $O(T^2)$ ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现代大语言模型（LLM）在处理长上下文任务时面临三大效率挑战：
- **高计算开销**（Prefill 阶段的 attention 计算）
- **高内存带宽压力**（Decode 阶段的 attention 内存访问）
- **KV Cache 容量瓶颈**（Decode 阶段缓存随序列增长而膨胀）

尽管稀疏注意力（Sparse Attention）能缓解前两个问题，但仍存在以下关键挑战：
1. **KV Cache 容量仍随序列长度增长**，若卸载到 CPU 内存会引入 PCIe 传输瓶颈；
2. **稀疏选择步骤本身具有 $O(T)$ 复杂度**，在长上下文中可能成为主导成本。

---

### **提出的新方法与创新点**
SparDA 提出了一种**解耦稀疏注意力架构（Decoupled Sparse Attention）**，通过引入第四个每层投影——**Forecast 投影**（与 Query、Key、Value 并列），实现以下三项核心创新：

#### ✅ **1. 可训练的前瞻稀疏选择（Trainable Lookahead Sparse Selection）**
- 将稀疏选择从当前层的 `Query` 中解耦，由上一层的 `Forecast` 预测下一层所需的 KV 块。
- 实现 **CPU 到 GPU 的 KV 缓存预取（prefetch）与当前层计算重叠**，隐藏 PCIe 传输延迟。

#### ✅ **2. 紧凑型 Forecast 索引器（Compact Forecast Indexer）**
- Forecast 不再需要保留完整的多头结构，在 GQA 架构中每个 GQA 组仅用一个 Forecast Head。
- 显著降低稀疏选择开销，并跳过 softmax 操作，进一步提升效率。

#### ✅ **3. 异步预取 + 持久化 UVA 内核（Asynchronous Prefetch with Persistent UVA Kernel）**
- 使用基于 Unified Virtual Addressing (UVA) 的持久化 Triton 内核，实现高吞吐的异步主机-设备传输。
- 支持大规模批量解码下的高效 KV 块加载。

---

### **相比现有方法的优势**
| 方面 | SparDA vs. 现有方法 |
|------|---------------------|
| **效率** | 超越 Sparse + Offload 基线，Prefill 最高提速 1.25×，Decode 最高提速 1.7× |
| **吞吐量** | 单卡支持更大 batch size，Decode 吞吐最高达非卸载稀疏基线的 **5.3×** |
| **准确性** | 在多个长上下文基准上匹配甚至略优于原始稀疏模型 |
| **系统友好性** | 无需重新训练主干网络，仅需微调 Forecast 投影（<0.5% 参数增量） |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
在两个稀疏预训练的 8B 模型上进行评估：
- **MiniCPM4.1-8B**（基于 InfLLM-V2 架构）
- **NOSA-8B**（在 InfLLM-V2 上增加 query-agnostic eviction head）

评估涵盖四大类长上下文基准：
| 类别 | 数据集 | 说明 |
|------|--------|------|
| 综合理解 | **HELMET**, **LongBench** | 多任务、双语、覆盖回忆、问答、摘要等 |
| 长依赖推理 | **RULER** | 合成任务，测试模型对远距离信息检索能力 |
| 数学推理 | **MATH-500**, **AIME 2024/2025** | 需要链式推理的复杂数学题 |

此外还进行了扩展长度测试（如 RULER 在 32K–128K 序列上的表现）。

---

### **实验设置与评估指标**

#### 🔧 **硬件平台**
- 主要结果基于 **NVIDIA H100 GPU**（80GB HBM3，PCIe Gen5×16）
- 补充结果包含 **A100 GPU** 对比

#### 📊 **评估指标**
| 指标 | 描述 |
|------|------|
| **Accuracy (%)** | 各基准任务的平均准确率 |
| **Throughput (tok/s)** | 每秒生成 token 数，衡量推理速度 |
| **Speedup** | 相对于基线的速度提升倍数 |
| **Feasible Batch Size** | 单卡可运行的最大 batch，反映内存效率 |

#### ⚖️ **对比基线方法**
| 方法 | 特点 |
|------|------|
| **Dense / Dense+** | 全注意力，无 KV 卸载 |
| **Sparse / Sparset** | 原始稀疏注意力，是否启用 KV 卸载 |
| **InfiniGen [11]** | 使用隐藏状态作为代理进行 lookahead prefetch，但不训练 |
| **SparDA (Ours)** | 本文方法，引入可学习 Forecast 进行解耦选择与预取 |

所有方法均在同一推理引擎（NOSI）上实现以保证公平比较。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据汇总**

| 场景 | 性能指标 | SparDA 结果 | 提升幅度 |
|------|----------|-------------|-----------|
| **Prefill 吞吐**（128K, B=4） | tok/s | **17,087.6** (MiniCPM) | 较 Sparse ↑1.25× |
| **Decode 吞吐**（128K, B=16） | tok/s | **705.3** (MiniCPM), **735.0** (NOSA) | 较 Sparse ↑1.7× |
| **最大 Decode 吞吐**（vs. 非卸载） | tok/s | **1000.1** (MiniCPM) | 较 Sparset ↑**5.3×** |
| **参数增量** | 新增参数 | **33.5M** | 占比 **<0.5%** |

> 注：在 A100 上也观察到一致趋势，Prefill 提速约 1.23×，Decode 提速约 1.55×。

---

### **与基线方法的对比结果**

#### ✅ **准确性方面**
- SparDA 在多数任务上**持平或略微超越原始 Sparse 基线**：
  - MiniCPM4.1-8B：平均准确率从 61.4 → **61.7**
  - NOSA-8B：平均准确率从 49.4 → **51.7**（+2.3）
- 在 **RULER 和 Reasoning 任务上提升显著**，尤其在更长序列（如 128K）下优势扩大。
- InfiniGen 因依赖相邻层相似性假设，在部分任务上出现明显退化（如 NOSA-8B 下降 3.8 pts）。

#### ✅ **效率方面**
- **Prefill 阶段**：得益于紧凑 Forecast indexer，block selection 成本最多降低 **2.5×**（128K）。
- **Decode 阶段**：
  - 稀疏选择时间几乎恒定（near-flat），不受序列长度影响；
  - 异步 prefetch 成功掩盖 PCIe 传输延迟，使大 batch 更可行。
- **吞吐量突破**：
  - Sparse 方法在 B>16 时常因 OOM 失败；
  - SparDA 可运行至 B=64 或更高，从而获得数量级更高的总吞吐。

---

### **消融实验结果（Ablation Studies）**

#### 🔍 **压缩窗口 ablation（Table 6）**
- 使用更细粒度的目标压缩窗口（target: lc=2, sc=1）进行训练监督：
  - 显著提升 RULER 和 Reasoning 准确率（MiniCPM 分别 +3.0 和 +2.2）
  - 证明**高分辨率监督信号有助于学习更精细的选择策略**

#### 🔍 **Prefetch CTA 数量调节（Table 7）**
- 小 batch（<32）：16 CTAs 最优
- 大 batch（≥32）：32 或 64 CTAs 更好
- 自适应调度策略（Adaptive Heuristic）接近最优配置，验证其有效性

#### 🔍 **Decode 加速来源分解（Table 10）**
| 方法 | B=4 | B=16 | B=64 |
|------|-----|------|------|
| Sparse | 167.8 | 447.9 | 788.9 |
| SparDA (no prefetch) | 247.3 | 505.9 | 696.9 |
| **SparDA (full)** | **240.2** | **705.3** | **1000.1** |

- 小 batch：加速主要来自 **selection 开销下降**
- 大 batch：**prefetch overlap 成为主要驱动力**（B=64 时贡献 ~40% 额外增益）

---

## **4. 关键结论和发现**

### **主要发现**
1. **稀疏选择可以被建模为一个可学习、可调度的信号**，而非必须绑定于当前 Query。
2. **解耦 selection 与 attention 是提升长上下文推理效率的关键路径**：
   - 实现 lookahead prefetch，有效隐藏 CPU-GPU 数据传输延迟；
   - 支持设计更高效的索引器结构（如单 head per GQA group）。
3. **仅需微调轻量 Forecast 投影即可集成 SparDA**，无需重训整个模型，部署门槛低。
4. **SparDA 在保持甚至提升准确性的前提下，显著提升了 Prefill 和 Decode 效率**，特别是在大 batch 和超长上下文场景下优势巨大。

---

### **局限性**
1. **不是独立的稀疏注意力方法**，而是构建在已有稀疏 backbone（如 InfLLM-V2）之上的增强模块。
2. **准确性受限于基础稀疏模型的质量**，无法修复原始稀疏模式中的根本缺陷。
3. 当前实现在 Layer-0 仍需特殊处理（因无前一层 Forecast），导致稍早 OOM。
4. 尚未应用于 Token-level 稀疏注意力（如 DSA、CSA）或更大规模模型（>8B）。

---

### **未来工作方向**
1. **将 SparDA 扩展至 Token-level Sparse Attention**（如 DeepSeek-V3.2、GLM-5 中的 DSA）。
2. **应用于 Compressed Sparse Attention (CSA) 路径**（如 DeepSeek-V4）。
3. **探索跨更多层的 Forecasting 机制**（如预测 l+2 层）以进一步延长 prefetch 窗口。
4. **结合其他 KV Cache 压缩技术**（如 SnapKV、H2O）形成联合优化方案。

---

> ✅ **代码开源地址**：[https://github.com/NVlabs/SparDA](https://github.com/NVlabs/SparDA)

</details>

---

### 2. [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302)

**Authors**: Haocheng Xia, Mihir Pamnani, Hanxi Fang, Supawit Chockchowwat, Yongjoo Park  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2606.04302v1  

#### Abstract
Key-value (KV) caching accelerates inference of large language models (LLMs) by reusing past computations for generated tokens. Its importance becomes even greater in long-context applications such as retrieval-augmented generation (RAG) and in-context learning (ICL). However, conventional KV cachin...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
在 **Retrieval-Augmented Generation (RAG)** 和 **in-context learning** 等长上下文任务中，**Key-Value (KV) caching** 被广泛用于加速大语言模型（LLM）推理。然而，传统 KV cache 将 **positional encoding**（如 RoPE）直接嵌入缓存中，导致其具有 **position-awareness**（位置感知性），即同一个文档若出现在不同位置，必须重新计算并存储一份新的 KV 缓存副本。

这带来了两个核心问题：
- **内存浪费**：相同内容因位置不同而产生多个 KV 副本。
- **复用受限**：缓存命中率低，尤其在文档访问呈 **Zipf 分布**（少数热门文档频繁出现）时效率低下。

### **提出了什么新方法或新思路**
作者提出 **LazyAttention**，一种全新的注意力机制，通过 **deferred positional encoding**（延迟位置编码）实现 **zero-copy, position-agnostic KV reuse**。

核心思想是：
- **逻辑上解耦 RoPE 与 KV 存储**：KV cache 中不再包含绝对位置信息，而是以“无位置”（NoPE）形式存储。
- **在 attention kernel 内部动态注入位置偏移**：仅在计算 attention score 时，根据 query 和 key 的相对位置实时旋转（rotate）向量。
- **完全避免 HBM 中的位置重编码复制**：一个物理 KV 块可被多个逻辑请求在任意位置复用。

### **相比现有方法的优势**
| 方法 | 是否支持任意位置复用 | 是否需要 KV 复制 | 内存效率 | 计算开销 |
|------|------------------------|------------------|----------|-----------|
| Prefix Caching | ❌ 仅前缀 | ❌ | 低 | 低 |
| Block-Attention / CacheBlend | ✅ 是 | ✅ 需复制并重编码 | 中 | 高（I/O 密集） |
| **LazyAttention (ours)** | ✅ 是 | ❌ **零复制** | **高** | **极低（~0.2% 开销）** |

LazyAttention 在保持数学等价性的前提下，**消除了内存-计算权衡**（memory-compute trade-off），实现了真正的高效复用。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
实验基于四个标准 RAG QA 基准：
- **2WikiMQA**：多段落阅读理解，每段视为独立文档。
- **HotpotQA**：多跳推理，需跨多个支持文档推理。
- **TriviaQA**：长网页上下文问答。
- **NarrativeQA**：基于小说/剧本的长文本理解。

此外还测试了：
- **Long-form Literature Review**（5 篇 ArXiv 论文生成综述）
- **Few-shot Classification**（AG News 数据集上的非 RAG 场景）

### **实验设置和评估指标**
- **硬件平台**：NVIDIA H100（96GB）、A100、A40 GPU。
- **基础框架**：基于 **vLLM** 实现，使用 **Triton** 编写定制化 attention kernels。
- **模型**：
  - 主要：`Tulu3-Block-FT`（基于 Llama-3.1-8B）
  - 扩展：`Llama-3.1-70B-Instruct`, `Qwen3-8B`

#### **评估指标**
| 指标 | 描述 |
|------|------|
| **TTFT (Time-to-First-Token)** | 首个 token 生成时间，反映系统响应速度 |
| **Throughput (req/s)** | 单位时间内处理的请求数 |
| **VRAM Cache Hit Ratio** | KV 块从缓存命中的比例 |
| **End-to-End Latency** | 完整请求处理时间 |
| **Exact Match (EM)** | 生成答案的准确率 |

### **基线方法对比**
- **Prefix Caching**：vLLM 默认前缀缓存。
- **Prompt Cache**：模块化 attention 复用。
- **CacheBlend**：融合缓存知识的 RAG 变体。
- **Block-Attention**：当前最先进块级缓存复用方法。
- **MEPIC-like**：类似设计但 per-token 旋转，引入额外 I/O。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**
| 指标 | LazyAttention | 最优基线（Block-Attention） | 提升倍数 |
|------|---------------|----------------------------|----------|
| **TTFT (Skewed)** | ↓ 1.37× 更快 | 基线 | **1.37×** |
| **Throughput (Skewed)** | ↑ 1.40× 更高 | 基线 | **1.40×** |
| **Cache Hit Ratio (1GB, High Skew)** | 13.57% | 7.27% | **1.86×** |
| **Cache Hit Ratio (No-limit, Mid Skew)** | 29.09% | 27.38% | **1.06×** |
| **Decoding Overhead** | ~0.13% | N/A | 可忽略 |
| **Prefilling Compute Overhead** | ~0.59% (M=128) | N/A | 极低 |

> 在 **Llama-3.1-70B** 上，LazyAttention 相比 CacheBlend 实现 **5.2× TTFT 加速**。

### **与基线方法的对比结果**
- **在 Skewed 文档分布下优势显著**：
  - LazyAttention 利用热门文档高频复用特性，大幅降低 TTFT 和提升吞吐。
  - Block-Attention 因需复制 KV 副本，受 **HBM 带宽限制**，扩展性差。
- **Uniform 分布下仍具竞争力**：
  - 即使复用机会少，LazyAttention 仅引入 **<0.6%** 额外开销，性能接近最优。

### **消融实验结果**
#### **(1) 不同 tile size 敏感性分析（Table 9）**
- 改变 prefilling tile size $ M \in \{64, 128, 256\} $，归一化吞吐变化不超过 **3%**。
- 表明默认配置 $ M=128 $ 具有鲁棒性。

#### **(2) 长上下文扩展性（Table 6）**
- 文档长度从 4K → 16K tokens，LazyAttention 的 TTFT 加速比稳定在 **~4.8–5.0×**。
- 显示其对长上下文具有良好可扩展性。

#### **(3) 数值稳定性验证（Table 7）**
- 序列长度达 **128K tokens** 时，attention logits 与标准方法的最大绝对误差 < $ 3.75 \times 10^{-5} $。
- 证明 **on-the-fly rotation 无累积误差**，数值稳定。

#### **(4) 与其他架构兼容性（Table 8）**
- 在 `Qwen3-8B` 和结合 `Lego-Link` 策略下均取得 **~6.3× TTFT 加速**。
- 表明方法具有良好的通用性和正交性。

---

## **4. 关键结论和发现**

### **主要发现**
1. **Position-agnostic KV reuse 显著提升缓存效率**：
   - 一个物理 KV 块可在任意逻辑位置复用，**缓存命中率最高提升 7.5×**（理论分析）。
2. **Kernel-level deferred encoding 可消除内存瓶颈**：
   - 通过将 RoPE 注入 attention kernel 内部，**避免了昂贵的 KV 复制和 HBM 读写**。
3. **实际开销极低，收益巨大**：
   - 运行时开销仅 **~0.2%**，却带来 **1.37× TTFT 减少** 和 **1.40× 吞吐提升**。
4. **适用于多种场景**：
   - 不仅限于 RAG，在 **few-shot learning**, **parallel hypothesis agents**, **long-form generation** 中同样有效。

### **方法的局限性**
- 当前主要针对 **RoPE-family** 位置编码（如 RoPE, ALiBi, YaRN）。
- 对 **absolute positional encoding** 或 **linear attention** 类模型不适用。
- 需要定制 **attention kernel**，对框架集成有一定工程要求。

### **未来工作方向**
- 扩展至更多类型的 positional encoding（如 ALiBi 的 bias 注入方式）。
- 探索 **multi-modal RAG** 中的 position-agnostic 缓存。
- 结合 **KV compression** 技术进一步优化内存占用。
- 在 **边缘设备** 上部署轻量化版本，支持低功耗 RAG 应用。

---

> **总结**：  
> **LazyAttention** 通过 **kernelized deferred positional encoding**，从根本上解决了 KV cache 的位置依赖问题，实现了 **zero-copy、高命中、低开销** 的缓存复用机制。它不仅提升了 RAG 推理效率，也为 LLM serving 中的内存管理提供了新范式。代码已开源：[https://github.com/illinoisdata/lazy-attention](https://github.com/illinoisdata/lazy-attention)

</details>

---

### 3. [AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484)

**Authors**: Qingxu Fu, Boyin Liu, Shuchang Tao, Zhaoyang Liu, Bolin Ding  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2606.04484v1  

#### Abstract
We present AgentJet, a distributed swarm training framework for large language model (LLM) agent reinforcement learning. Unlike centralized frameworks that tightly couple agent rollouts with model optimization, AgentJet adopts a decoupled multi-node architecture in which swarm server nodes host trai...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现有的 **agentic RL**（基于大语言模型的智能体强化学习）训练框架存在以下关键问题：
- **运行时脆弱性**（Runtime Fragility）：代理（agent）执行环境与模型训练耦合紧密，外部工具（如浏览器、沙箱、数据库）的失败常导致整个训练中断。
- **调试困难**（Debugging Friction）：修改 agent 代码或奖励函数需重启整个训练流程，迭代周期长达 5–10 分钟。
- **多模型支持不足**：主流框架仅支持单一策略模型，难以训练异构多智能体系统（如不同规模的 LLM 协作）。
- **冗余上下文**（Redundant Context）：多轮交互中重复的系统提示、工具定义等造成计算浪费。
- **任务隔离困难**：多任务混合训练（cocktail training）因依赖冲突而难以实现。

### **提出的新方法与思路**
论文提出了 **AgentJet**，一个基于 **swarm 架构** 的分布式训练框架，其核心是 **完全解耦 agent 执行与模型优化**，采用 **client-server 范式**：
- **Swarm Server**（优化节点）：部署在 GPU 集群上，负责模型存储、推理服务、梯度更新。
- **Swarm Client**（采样节点）：可在任意设备（CPU/GPU、笔记本、服务器）上运行，负责执行 agent 工作流、收集轨迹、计算奖励。

### **相比现有方法的优势**
| 特性 | AgentJet | 传统框架（如 OpenRLHF, veRL） |
|------|---------|-----------------------------|
| **架构解耦** | 完全分离训练与执行 | 紧密耦合 |
| **故障容忍** | Client 失败不影响 Server | 整体崩溃风险高 |
| **热插拔调试** | 支持运行中替换 Client | 必须重启训练 |
| **多模型支持** | 支持异构多模型、非共享参数训练 | 通常单模型 |
| **多任务训练** | 支持隔离的 cocktail training | 依赖冲突严重 |
| **上下文效率** | Timeline Merging 减少冗余 | 无优化 |
| **框架无关性** | 支持 LangChain、AgentScope、Raw HTTP 等 | 通常绑定特定框架 |

---

## **2. 核心实验方法和设置**

### **使用的数据集与任务**
- **Werewolves RPG 游戏**：社交推理游戏，用于测试多智能体协作与对抗能力。
- **学术翻译任务**：将英文论文摘要翻译为中文，涉及多 agent 协作（初译、审校、润色）。
- **AppWorld**：交互式编码基准，模拟真实数字任务（如邮件管理、音乐播放）。
- **AIME**：数学推理任务，评估符号推理能力。
- **自建“谁是卧底”游戏**：用于 vibe training 和自动化研究演示。

### **实验设置与评估指标**
| 设置项 | 描述 |
|-------|------|
| **模型** | Qwen3-8B, Qwen3-14B, Qwen3-235B-A22B（静态对手）等 |
| **算法** | GRPO, PPO, DAPO 等 RL 算法 |
| **训练模式** | 共享参数（shared-parameter）、非共享参数（non-shared-parameter）、cocktail training |
| **评估指标** | - 成功率（Success Rate, SR）<br>- Pass@1 / Pass@2（AIME）<br>- 平均奖励（Mean Reward）<br>- 训练速度（Wall-clock time）<br>- 上下文压缩率（Timeline Merging Speedup） |

### **基线方法对比**
- **Single-task Specialist**：每个任务单独训练一个专用模型。
- **Two-stage OPD**（On-Policy Distillation）：先训练多个专家，再蒸馏到一个学生模型。
- **传统 RL 框架**：如 OpenRLHF、veRL（隐含对比）。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### **(1) Werewolves 游戏：共享参数训练**
| 实验 | 可训练角色 | 初始 SR | 最终 SR | 提升 |
|------|-----------|--------|--------|------|
| Exp 1 | WW (7B) | 23.0% | 47.2% | +24.2% |
| Exp 2 | WW (14B) | 40.9% | 64.7% | +23.8% |
| Exp 7 | vl+sr+wt+ht (14B) | 23.9% | 41.6% | +17.7% |

> ✅ **结论**：狼人阵营更易训练；联合训练多个角色可有效提升胜率。

#### **(2) Werewolves 游戏：非共享参数训练**
| 实验 | 模型配置 | 初始 SR | 最终 SR |
|------|---------|--------|--------|
| Exp 3 | 3 × 14B-LoRA（独立训练） | 40.8% | **66.5%** |
| （对比）Exp 2 | 1 × 14B（共享参数） | 40.9% | 64.7% |

> ✅ **结论**：非共享参数训练带来 **+1.8%** 提升，因行为多样性增强欺骗性。

#### **(3) 学术翻译任务**
- **基础模型**：Qwen2.5-7B-Instruct
- **训练后**：正确处理缩写展开、第一人称替换、术语翻译。
- **示例改进**：
  - “we introduce…” → “本文引入…”（去第一人称）
  - “QNVB” → “准牛顿变分贝叶斯(QNVB)”（首次展开）

#### **(4) Cocktail Training（AppWorld + AIME）**
| 任务 | 专用训练（Separate） | Cocktail 训练 | 差距 |
|------|------------------|--------------|------|
| AIME | 0.73 | 0.72 | ≈ |
| AppWorld | 0.68 | 0.58 | -10 pts |

> ⚠️ **结论**：cocktail 训练在 AppWorld 上有性能损失，但优势在于：
> - **统一模型**：一个模型掌握多种技能。
> - **成本更低**：避免 N 次独立训练，节省 GPU 时间与工程开销。

#### **(5) Timeline Merging 性能加速**
| 指标 | 无合并 | 有合并 | 加速比 |
|------|------|-------|--------|
| 平均更新时间 | 2160 ± 171s | 346 ± 13s | **6.25×** |
| LLM 调用次数 | 12.6 ± 1.0 | 11.4 ± 0.7 | ≈ |

> ✅ **结论**：timeline merging 在不损失训练质量的前提下，实现高达 **6.25×** 的训练加速。

#### **(6) 框架无关性验证**
使用四种 agent 框架（OpenAI SDK, LangChain, AgentScope, Raw HTTP）训练同一任务：
- **最终评估奖励差异**：< 0.025
- **最大跨框架差距**：< 0.04

> ✅ **结论**：AgentJet 对 agent 框架完全透明，支持任意 OpenAI 兼容接口。

---

## **4. 关键结论和发现**

### **主要发现**
1. **Swarm 架构显著提升训练鲁棒性与灵活性**：
   - 支持故障容忍、热插拔调试、异构多模型训练。
   - 实现真正的 **REPL-like** 研究范式。

2. **非共享参数训练优于共享参数**：
   - 在社交推理任务中，独立训练的 agent 表现出更高行为多样性，提升欺骗成功率。

3. **Timeline Merging 是高效多轮训练的关键**：
   - 自动合并冗余上下文，实现 **1.5–10×** 训练加速。

4. **Cocktail Training 是低成本多技能模型的有效路径**：
   - 虽略逊于专用模型，但避免了复杂的两阶段蒸馏流程。

5. **自动化研究成为可能**：
   - **A3R**（Alpha Auto Research）模块可自主完成超参搜索、消融分析、报告生成。
   - 案例：自动确定 AIME 任务的最小稳定 batch size（**bs=16**），并发现响应长度（`max_response_length`）对性能影响更大。

### **方法的局限性**
- **Cocktail Training 的性能折衷**：在工具密集型任务（如 AppWorld）上表现不如专用训练。
- **Timeline Merging 的一致性权衡**：文本级匹配（text-level）合并更激进但可能破坏 train-inference 一致性。
- **依赖外部服务稳定性**：虽解耦了 client，但若 reward model 或 API 不可用，仍会影响训练信号。

### **未来工作方向**
- **更智能的 episode 批量调度**：结合动态采样（如 DAPO）与 swarm 协调。
- **跨 client 的联邦式训练机制**：支持隐私保护下的分布式 agent 训练。
- **集成更多 RL 算法**：如 offline RL、imitation learning。
- **扩展至多模态 agent**：支持视觉、语音等感知输入的 swarm 训练。

---

> **总结**：AgentJet 通过 **swarm 架构** 重新定义了 agentic RL 的训练范式，解决了现有框架在 **鲁棒性、灵活性、效率** 上的根本缺陷，为大规模、多任务、自动化 agent 研究提供了坚实基础设施。

</details>

---

### 4. [BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization](https://arxiv.org/abs/2606.04807)

**Authors**: Saket Reddy, Ke Yang, ChengXiang Zhai  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2606.04807v1  

#### Abstract
Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground truth, creating a high-variance, subjective reward landscape. Previous preference-based fine-tuning methods have major trade-offs: Direct Preference Opt...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization

---

## 1. 论文的主要贡献和创新点

### 解决的问题
大型语言模型（LLMs）在预训练过程中会继承来自大规模文本语料的社会偏见（social bias），如种族、性别、社会经济地位等方面的歧视性态度。这类偏见缺乏单一的“正确答案”，导致其奖励信号具有**高方差**（high-variance）和主观性，使得传统的偏好微调（preference-based fine-tuning）方法面临挑战。

现有主流方法存在明显缺陷：
- **DPO**（Direct Preference Optimization）依赖静态的离线偏好对，缺乏探索能力，泛化性差。
- **PPO**（Proximal Policy Optimization）虽支持在线训练，但依赖一个独立的critic model进行价值估计，在噪声大、主观性强的偏见场景下容易产生不稳定的advantage估计，导致训练不稳定。

### 提出的新方法与创新思路
本文提出 **BiasGRPO**，一个基于 **Group Relative Policy Optimization (GRPO)** 的框架，用于稳定在高方差奖励景观中的偏见缓解任务。

**核心思想**是：  
不再依赖critic model来计算advantage，而是对每个prompt生成一组（group）完成（completions），并以该组内所有completion的平均奖励为基准，通过归一化（normalization）得到相对优势（relative advantage）。公式如下：

$$
A_{i,t} = \frac{r_i - \text{mean}(r)}{\text{std}(r)}
$$

这种方法结合了DPO的稳定性与PPO的探索能力。

### 相比现有方法的优势
- ✅ **更高的训练稳定性**：避免了critic model带来的噪声，显著降低reward方差。
- ✅ **更强的泛化能力**：允许模型在线生成多个completion，增强环境探索。
- ✅ **更有效的学习信号**：即使所有completion都带有偏见，也能通过组内比较识别出“相对更优”的输出，从而提取有效学习信号。
- ✅ **模块化设计**：提供了可复用的数据集和轻量级bias-specific reward model，便于集成到多目标RLHF pipeline中。

---

## 2. 核心实验方法和设置

### 使用的数据集
构建了一个包含 **20,999条prompt** 的综合数据集，来源包括：
- **BiasDPO**（10,000条）：原始偏见探测问题 + 合成扩展8,855条，覆盖11个领域（新增Age、Disability、Nationality等）。
- **Civil Comments**（10,000条）：社交媒体评论，按毒性分数分层采样，用于模拟自然语境下的偏见触发。
- **UnQover**（999条）：模糊情境下的偏见诱导问题，用于测试模型在无法确定答案时的行为。

> 所有合成数据均通过GPT-4o、Gemini 2.0 Flash、Claude 4 Sonnet联合生成，并验证其语义多样性（Vendi Score达人类基线的72.79%）。

### 实验设置与评估指标
- **基础模型**：Microsoft Phi-2（2.7B参数），未经过RLHF或任何偏见缓解微调，作为“干净起点”。
- **训练方式**：
  - DPO：使用prompt + favorable/unfavorable completion pair。
  - PPO & GRPO：仅使用prompt + reward model打分。
  - 所有方法训练3个epoch，初始学习率 $10^{-6}$。
- **评估指标**：
  - **BOLD**（Bias in Open-Ended Language Generation）：衡量表征伤害，越低越好。
  - **RealToxicityPrompts (RTP)**：衡量显性敌意，越低越好。
  - **BBQ**（Bias Benchmark for Question Answering）：聚焦模糊情境下的刻板印象识别，越高越好（正确选择“cannot be determined”）。
  - **TruthfulQA**：衡量事实准确性，防止知识退化（knowledge degradation），越高越好。

### 基线方法对比
- **DPO**（含IPO变体）
- **PPO**
- **GRPO**（本文方法）
- 额外对比：**Online DPO**、不同reward model、不同group size（G=2,4,8）、跨模型（Llama 3.2 3B）

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Phi-2模型）

| Benchmark | Base | DPO | PPO | **GRPO** |
|---------|------|-----|-----|----------|
| **BOLD (↓)** | 0.0293 | 0.0222 | 0.0268 | **0.0140** |
| **RTP (↓)** | 0.0282 | 0.0234 | 0.0262 | **0.0198** |
| **BBQ (↑)** | 0.2750 | 0.2823 | 0.2996 | **0.3123** |
| **TruthfulQA (↑)** | 0.3843 | 0.3941 | 0.3929 | **0.3941** |

> ✅ GRPO在所有benchmark上表现最佳，且**未牺牲TruthfulQA性能**，表明无知识退化。

### 与基线方法的对比结果
- **vs DPO**：GRPO在BOLD和RTP上分别降低约40%和15%，优于DPO的平滑但早停的学习曲线。
- **vs PPO**：GRPO训练过程更平稳（reward std仅为PPO的一半），避免了PPO因critic估计不准导致的剧烈波动。
- **vs Online DPO**：GRPO仍显著领先，说明优势不仅来自“在线探索”，更源于**group-relative normalization机制本身**。

### 消融实验结果
#### （1）Reward Model消融
使用第二好的人类标注reward model替代自定义reward model：
- 性能略有下降，但仍远超base model。
- 表明GRPO算法本身鲁棒，只要reward model合理即可有效优化。

#### （2）Group Size消融（G=2, 4, 8）
| Group Size | BOLD ↓ | RTP ↓ | BBQ ↑ | TruthfulQA ↑ |
|------------|--------|-------|-------|--------------|
| G=2        | 0.0243 | 0.0242 | 0.2781 | 0.3868 |
| G=4        | 0.0140 | 0.0198 | 0.3123 | 0.3941 |
| G=8        | 0.0124 | 0.0115 | 0.3781 | 0.4137 |

> ✅ 随着group size增大，性能持续提升，尤其在BBQ和TruthfulQA上；G=2显著弱于G=4，证明**group-relative机制的有效性依赖足够多样化的completion集合**。

#### （3）跨模型验证（Llama 3.2 3B）
- 在Llama上GRPO同样优于DPO和PPO（除BBQ外），验证方法的通用性。
- BBQ性能下降可能因UnQover样本不足，未能充分学习模糊推理。

---

## 4. 关键结论和发现

### 主要发现
1. **GRPO天然适配高方差、主观性的偏见缓解任务**：其group-relative机制能在没有“绝对正确答案”的情况下，依然提供稳定、清晰的学习信号。
2. **训练稳定性显著提升**：GRPO的reward标准差仅为PPO的约一半（0.0668 vs 0.1434），训练曲线平滑上升，无早期饱和或剧烈震荡。
3. **行为层面更安全智能**：
   - 能主动拒绝有毒前提（如“白宫里的圣战者”），转而讲述中立故事。
   - 在涉及性别二元的prompt中，“打破约束”生成“the activist”，体现包容性优先的安全策略。
   - TruthfulQA无退化，证明该行为非理解能力下降所致。
4. **模块化资源贡献大**：
   - 发布了涵盖11个领域的多样化数据集。
   - 提供了一个仅0.1B参数的高效bias reward model，在Spearman相关性上超越现有模型（0.4748 vs 第二名0.3769）。

### 方法的局限性
- 当前实验集中在**3B级别模型**，需进一步验证在更大规模模型（如70B以上）上的效果。
- group size固定为4或8，尚未探索**动态或任务自适应的group sizing策略**。
- 合成数据依赖LLM生成，尽管采用多模型轮换减轻偏差，仍存在潜在循环风险。

### 未来工作方向
- 探索adaptive group size机制，根据不同prompt复杂度动态调整completion数量。
- 将BiasGRPO扩展至多模态或对话系统中的偏见缓解。
- 构建更细粒度、面向特定社会群体的bias reward models。
- 结合其他RLHF技术（如KL控制、entropy regularization）进一步优化训练动态。

--- 

> **总结一句话**：  
> **BiasGRPO通过引入group-relative policy optimization，在无需critic model的情况下实现了比DPO更强的泛化能力和比PPO更高的训练稳定性，为高方差、主观性强的LLM偏见缓解任务提供了一种鲁棒、高效且可扩展的新范式。**

</details>

---

### 5. [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415)

**Authors**: Jiongjiong Gu, Jianfeng Wang, Zidong Han, Yongqiao Wang, Pengfei Xia, Mingjie Zhang, Hong Liu, Yuanyi Xia, Jiajia Chu, Yifeng Tang, Hui Zang, Xin Yao, Qijie Qiu, Yuzhao Wang, Chuanfei Xu, Lin Zhang, Zhuonan Lai, Hongming Huang, Jiawei Qiu, Gong Zhang, Zhong Ming, Weipeng Cao  
**Category**: cs.DC  
**Published**: 2026-06-04  
**Score**: 10.5  
**Type**: new  
**ArXiv ID**: 2606.04415v1  

#### Abstract
Modern AI serving increasingly relies on NPUs for conventional inference and large language model serving. However, current NPU deployments commonly expose physical devices directly to applications, which limits runtime control over scheduling and makes it difficult to adapt execution to phase-level...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location》核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
现代AI服务广泛依赖NPU进行大语言模型（LLM）推理，但当前主流部署方式采用**直接Passthrough模式**，即应用程序直接绑定物理NPU设备。这种模式存在以下问题：
- 缺乏运行时调度控制能力，难以适应LLM执行中不同阶段（prefill vs decode）的资源需求差异。
- **静态PD拆分（PD Disaggregation）** 虽可减少相位干扰，但会导致资源不平衡和不必要的KV-Cache传输。
- **静态PD共存（PD Co-location）** 易引发相位间资源竞争，导致TTFT（Time to First Token）显著升高。

### 🚀 提出的新方法：FlexNPU
提出 **FlexNPU** —— 一种面向Ascend NPU的**透明用户态虚拟化层**，其核心设计包括：
- **AscendCL API拦截**：通过`LD_PRELOAD`注入客户端库，拦截AscendCL调用（如内存分配、stream管理、算子执行等），实现无侵入式虚拟化。
- **用户态Daemon架构**：每个NPU设备由一个FlexNPU Daemon管理，负责虚拟句柄映射、操作调度与资源监控。
- **动态PD共址（Dynamic PD Co-location）**：在不修改模型代码、框架或驱动的前提下，支持运行时根据prefill/decode的资源特征动态调整执行比例。

### 🔍 相比现有方法的优势
| 维度 | 现有方法（如GPU方案） | FlexNPU |
|------|------------------------|--------|
| 平台适配性 | 多基于CUDA/MIG/SM Partition等GPU机制 | 面向Ascend NPU，基于AscendCL通用接口 |
| 透明性 | 常需修改框架或应用逻辑 | 完全透明，无需改动任何上层组件 |
| 控制粒度 | 依赖硬件分区能力 | 用户态调度即可实现时间片级动态调控 |
| 应用场景 | 多聚焦于多租户共享或冷启动优化 | 专为LLM两阶段异构负载优化 |

> ✅ **核心创新**：首次将**透明运行时虚拟化**应用于Ascend NPU，并用于实现**phase-aware的动态PD调度**，填补了非GPU平台高效LLM服务的技术空白。

---

## 2. 核心实验方法和设置

### 📊 使用的数据集与模型
- **主测试模型**：
  - `DeepSeek-R1`：大规模MoE模型，部署于384卡Ascend 910C集群（W8A8量化）
  - `Qwen2.5-7B`：中小规模dense LLM，用于对比共址场景
- **基准测试集**：
  - `gsm8k_gen_0_shot_cot_str_perf`：用于单模型吞吐测试
  - 自定义请求分布模拟真实流量：
    - **1K-1K**：输入/输出长度均为~1K tokens（均衡负载）
    - **1K-4K**：短输入长输出（decode-heavy）

### ⚙️ 实验设置
- **硬件环境**：
  - 华为Ascend 910C NPU集群（最大384卡）
  - 使用标准CANN软件栈
- **部署配置**：
  - **DeepSeek-R1**：采用tensor parallelism + FlexNPU调度
  - **Qwen2.5-7B**：固定batch size和并发数以制造backlog压力
- **对比基线**：
  1. **Native Passthrough**：原生直通模式（评估开销）
  2. **Static PD Disaggregation**：预分配独立prefill/decode实例（如6P2D）
  3. **Static PD Co-location**：同一NPU上静态混合执行，无动态调度

### 📈 评估指标
| 指标 | 含义 |
|------|------|
| **Throughput (tokens/s 或 RPS)** | 系统整体生成吞吐量 |
| **TTFT (Time to First Token)** | 用户感知延迟，反映prefill响应速度 |
| **TPOT (Time Per Output Token)** | 解码效率，反映decode稳定性 |
| **Relative Improvement** | 相对于基线的提升百分比 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据汇总

#### （1）虚拟化开销极低甚至正向收益
| 配置 | 总吞吐（tokens/s） | 相对性能 |
|------|--------------------|----------|
| Native Passthrough | 977.69 | 1.000x |
| FlexNPU Proxy | 988.27 | **1.0108x** (+1.08%) |

> 💡 结果表明：FlexNPU不仅**未引入可观测推理延迟**，反而因异步代理机制提升了计算/通信重叠，轻微提高吞吐。

#### （2）相比Static PD Disaggregation（DeepSeek-R1）
| 工作负载 | 基线吞吐（RPS） | FlexNPU吞吐（RPS） | 提升幅度 |
|---------|------------------|--------------------|----------|
| 1K-1K（均衡） | 489.84 | 618.18 | **+26.33%** |
| 1K-4K（decode-heavy） | 146.63 | 154.18 | **+5.15%** |

> ✅ 在均衡负载下增益显著，说明FlexNPU有效缓解了静态拆分中的资源浪费问题。

#### （3）相比Static PD Co-location（Qwen2.5-7B）
| 输入/输出长度 | TTFT（基线） → FlexNPU | TTFT降幅 | 吞吐变化 | TPOT变化 |
|--------------|------------------------|-----------|------------|------------|
| 256/256 | 109.9s → 0.33s | **↓99.7%** | +3.57% | -2.12% |
| 256/1024 | 488.1s → 0.33s | **↓99.93%** | -0.52% | +0.90% |
| 1024/256 | 118.2s → 8.57s | **↓92.75%** | +3.36% | -1.13% |
| 1024/1024 | 506.5s → 8.31s | **↓98.36%** | +0.16% | +0.71% |

> ✅ **TTFT从数百秒降至亚秒级**，而TPOT几乎不变，证明FlexNPU极大改善了用户体验，且未牺牲解码效率。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **透明虚拟化可行且高效**：
   - AscendCL层级的API拦截可在用户态实现，**零修改应用/框架/驱动**。
   - 虚拟化路径轻量，**无端到端推理开销**，甚至略有性能增益。

2. **动态PD共址优于静态策略**：
   - 相比Static PD Disaggregation，FlexNPU通过动态调度避免资源闲置，**最高提升26.33%吞吐**。
   - 相比Static PD Co-location，FlexNPU通过进程级隔离与调度控制，**降低TTFT超92%**，解决HOL阻塞问题。

3. **互补资源利用是关键**：
   - Prefill为compute-bound，Decode为memory-bandwidth-bound，二者具有天然互补性。
   - FlexNPU利用该特性，在decode带宽饱和时调度prefill使用空闲AI Core，提升整体利用率。

### ⚠️ 局限性
- 当前调度策略较简单，依赖经验性规则而非精确性能建模。
- 尚未集成更细粒度的硬件隔离机制（如未来可能的NPU MIG类功能）。
- 所有实验均在华为Ascend平台完成，跨平台泛化性待验证。

### 🔮 未来工作方向
1. 支持更复杂的**SLO-aware调度策略**（如优先保障TTFT SLA）。
2. 探索**多租户共享下的公平性与隔离性保障**。
3. 结合**CXL或远程内存池**进一步优化KV-Cache管理。
4. 扩展至其他AI workload（如多模态推理、推荐系统）。

---

> 🏁 **总体评价**：  
> FlexNPU展示了**透明运行时虚拟化**作为下一代NPU服务基础设施的潜力。它不仅解决了LLM serving中的核心调度难题，也为构建灵活、高效、响应迅速的AI服务平台提供了实用技术路径。

</details>

---

### 6. [Graph Traversal on Tensor Cores: A BFS Framework for Modern GPUs](https://arxiv.org/abs/2606.05081)

**Authors**: Deniz Elbek, Kamer Kaya  
**Category**: cs.DC  
**Published**: 2026-06-04  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2606.05081v1  

#### Abstract
Modern GPUs have Tensor Cores (TCs) capable of extremely high-throughput matrix operations, yet graph algorithms remain difficult to accelerate because of their irregular and data-dependent execution patterns. This work presents BLEST, a TC-accelerated framework that reformulates Breadth-First Searc...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Graph Traversal on Tensor Cores: A BFS Framework for Modern GPUs

## 1. 论文的主要贡献和创新点

### 解决的问题
现代 GPU 虽然配备了高性能的 **Tensor Cores**（TCs），能够高效执行密集矩阵运算，但图算法（如 **BFS**）因其稀疏、不规则的数据访问模式和负载不平衡等问题，难以有效利用 TCs。传统方法在内存效率、同步开销和负载均衡方面存在显著瓶颈。

### 提出的新方法：BLEST
本文提出了 **BLEST**（Bit-level Efficient Sparse Traversal），一个基于 TC 加速的 BFS 框架，其核心创新包括：

#### （1）Binarized Virtual Slice Sets (BVSS)
- 一种新的图数据结构，将图按列划分为 **slice sets**，并进一步细分为 **Virtual Slice Sets (VSS)**。
- 实现了近乎完美的 **inter-warp load balance**，每个 warp 处理固定数量的 slices，避免了因度分布偏斜导致的负载不均。
- 仅调度与当前 frontier 相关的 VSS，避免了无用计算。

#### （2）优化的 TC 计算布局
- 设计了一种最优的 **TC multiplication layout**，将邻居检查映射到二进制 MMA 指令上。
- 相比之前的工作（如 BerryBees），将所需的 MMA 调用次数减少了 **8×**，极大提升了 TC 利用率。

#### （3）Lazy Vertex-Update 机制
- 引入异步更新策略，延迟对 `level` 和 `visited` 数组的原子写操作，直到每层处理结束。
- 显著减少 **atomic contention** 和 **cache miss**，提升缓存局部性。

#### （4）动态切换机制（Switching）
- 重新定义了 BFS 中的“方向切换”概念，在 TC 和 CUDA Cores 之间动态切换。
- 当未访问顶点数较少时，自动切换到底层 pull-based 的 CUDA Core 实现，以提高效率。

#### （5）图重排序优化
- 对于 **scale-free-like 图**，提出 **JACCARDWITHWINDOWS** 算法，通过窗口内 Jaccard 相似性聚类列，提升 BVSS 压缩率。
- 对于其他图，使用 **RCM**（Reverse Cuthill-McKee）降低带宽，改善缓存局部性。

---

## 2. 核心实验方法和设置

### 数据集
使用了两个基准套件中的 14 个真实世界图：
- **GAP Benchmark Suite**：包括 `GAP-road`, `GAP-twitter`, `GAP-web`, `com-Friendster` 等。
- **SuiteSparse** 中的大规模图，满足 $|V| \geq 2^{23}$ 且 $|E| < 2^{32}$。

代表性图包括社交网络（com-Friendster）、网页图（webbase-2001）、道路网（GAP-road）等。

### 实验设置
- **硬件平台**：
  - Arch-1：NVIDIA H200 GPU（141 GB HBM3e）
  - Arch-2：NVIDIA H100 GPU（64 GB HBM2e），用于大规模实验
- **实现语言**：C++/CUDA
- **评估任务**：
  - 单源 BFS（SS-BFS）
  - 多源 BFS（MS-BFS）
  - 接近中心性（Closeness Centrality）

### 评估指标
- **运行时间**（毫秒或秒）
- **加速比**（Speedup）：相对于基线方法的平均加速倍数
- **内存占用**
- **预处理开销**

### 基线方法对比
- **GAP** [17]：经典 CPU/GPU BFS 实现
- **Gunrock** [10]：基于 frontier 抽象的 GPU 图分析库
- **GSWITCH** [11]：支持动态优化策略切换的 GPU 框架
- **BerryBees** [15]：首个使用 TC 的 BFS 框架（本文主要比较对象）

---

## 3. 主要实验结果和性能指标

### 性能对比结果（SS-BFS）
在单源 BFS 上，BLEST 相比各基线取得显著加速：

| 基线方法       | 平均加速比（Geomean） |
|----------------|------------------------|
| GAP            | **22.0×**               |
| Gunrock        | **7.7×**                |
| GSWITCH        | **8.1×**                |
| BerryBees      | **5.9×**                |

> ✅ **BLEST 是目前文献中最快的 BFS 实现**，即使相比唯一使用 TC 的 BerryBees 也快了近 6 倍。

### 多源 BFS 与接近中心性
- 在多源 BFS 场景下，BLEST 比其单源版本平均快 **2.7×**，得益于内存访问的重叠优化。
- 成功计算了迄今为止最大规模的精确 **Closeness Centrality**：
  - 图：`com-Friendster`（6560 万顶点，36 亿边）
  - 时间：使用 **100 台 H100 GPU**，耗时约 **1 小时**（3,665 秒）
  - 这是首次对如此大规模图进行精确中心性计算。

### 消融实验结果（Ablation Study）

#### SS-BFS 消融（表 4）
从基础版本逐步添加优化，最终版本比 BerryBees 快 **5.9×**：
- **BVSS + Kernel Fusion**：+1.6×
- **+ Optimal TC Layout**：+1.9×（减少 8× MMA 调用）
- **+ Reordering**：+2.5×
- **+ Lazy Update**：+3.9×
- **+ Switching**：最终达 **5.9×**

> 各组件均有贡献，其中 **TC 布局优化** 和 **Lazy Update** 效果最显著。

#### MS-BFS 消融（表 6）
| 版本       | 相比 Naive 的加速比（Geomean） |
|-----------|-------------------------------|
| Naive     | 1.0×                          |
| Alg. 5（无优化） | 0.52×                         |
| + Reindexing | 0.65×                         |
| Full（完整版） | **2.69×**                     |

> 表明 **reindexing** 和 **dynamic slice tracking** 对多源性能至关重要。

---

## 4. 关键结论和发现

### 主要发现
1. **TC 可以高效用于图遍历**：尽管图具有不规则性，但通过 **bit-level SpMSpV** 和 **BVSS** 结构，可以将 BFS 成功映射到 TC 上。
2. **系统性工程优化带来巨大收益**：从数据结构、计算布局、内存访问到动态调度，每一层优化都显著提升性能。
3. **动态切换机制有效**：在小直径图中，自动在 TC 和 CUDA Cores 间切换可逼近理论最优性能。
4. **真实世界大规模图上的可行性**：BLEST 使得在合理时间内完成数十亿边图的精确图分析成为可能。

### 方法的局限性
1. **切换阈值依赖硬件**：公式中的常数 $n=10$ 是为 Hopper 架构调优的，在其他 GPU 上需重新校准。
2. **内存占用随并发数增长**：在 MS-BFS 中，`Levels` 数组大小与并发 BFS 数 $K$ 成正比，可能导致 **OOM**（已在多个大图上发生）。
3. **并非所有图算法都适用**：该方法适用于仅依赖“是否存在连接”的算法（如 BFS、Triangle Counting），但对于需要具体邻居 ID 或路径数的算法（如 Betweenness Centrality）扩展困难。

### 未来工作方向
1. **更鲁棒的切换策略**：设计图自适应或学习驱动的切换机制，减少误判。
2. **降低内存占用**：探索压缩存储或多阶段执行以支持更大规模的 MS-BFS。
3. **扩展至更多图算法**：研究如何将类似思想应用于 PageRank、SSSP、Connected Components 等。
4. **跨架构可移植性优化**：使框架能在不同代际的 GPU（如 Ampere、Ada、Blackwell）上自动调优。

---

> 🔚 **总结**：  
> **BLEST** 通过一系列针对 TC 特性的系统级优化，成功突破了图算法在现代 GPU 上的性能瓶颈，不仅大幅超越现有方法，还实现了以往无法完成的大规模精确图分析任务，为图计算在 AI 时代的硬件适配提供了重要范例。

</details>

---

### 7. [SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction](https://arxiv.org/abs/2606.04691)

**Authors**: Kenfeng Huang, Yi Cai, Xin Wu, Zikun Deng, Li Yuan  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.04691v1  

#### Abstract
Zero-shot information extraction (IE) with large language models (LLMs) has attracted increasing attention due to its flexibility in adapting to new schemas and domains without task-specific training. Existing approaches mainly rely on monolithic prompting, each-type prompting, or multi-agent debate...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction  
**核心结论与实验结果总结**

---

## 1. 论文的主要贡献和创新点

### 解决的问题
现有的 **zero-shot Information Extraction (IE)** 方法在使用 **Large Language Models (LLMs)** 时面临以下挑战：
- **Monolithic prompting**：一次性提取所有实体/关系，容易产生边界错误（boundary errors）和类型混淆（type confusion）。
- **Each-type prompting** 和 **Multi-agent debate**：虽然能细化推理，但会引入跨类型冲突（cross-type conflicts）、冗余的 agent 交互以及高昂的 token 开销。
- **Free-form debate 缺乏结构**：辩论过程无明确逻辑框架，难以系统聚合置信度，导致决策不可靠。

### 提出的新方法
论文提出 **SMADE-IE**（Sparse Multi-Agent Framework with Evidence-Driven Debate），一个稀疏且证据驱动的多智能体框架，用于 zero-shot IE。

#### 核心创新点：
1. **Adaptive Mode Selector（自适应模式选择器）**
   - 动态判断输入样本的复杂度（low/med/high），决定进入两种模式之一：
     - **Global Extraction Mode**：轻量级，适用于简单样本，仅用两个 agent（Universal + Verification）完成提取与验证。
     - **Type-Centric Extraction Mode**：细粒度，适用于复杂样本，为候选类型实例化专用 agent，并通过 Review Agent 补充遗漏类型。
   - 显著减少不必要的 agent 调用和推理噪声。

2. **Evidence-Driven Debate（证据驱动辩论机制）**
   - 将每个冲突预测建模为 **Toulmin-style argument**（Claim, Ground, Warrant, Backing, Rebuttal），使辩论结构化。
   - 引入 **外部证据评分器（external evidence scorer）** 对论据进行量化打分。
   - 使用 **贝叶斯 Beta 更新** 聚合支持与反驳信号，生成基于证据的置信度估计。
   - 支持 **早期停止（early-stopping）**：当后验分布稳定或领先候选优势足够大时终止辩论，提升效率。

3. **Iterative Entity-Relation Alignment (IERA)**
   - 针对 JERE 任务，迭代对齐实体与关系预测，确保本体一致性（ontology consistency）。

### 相比现有方法的优势
| 方面 | SMADE-IE 优势 |
|------|----------------|
| **准确性** | 通过结构化辩论和证据评分，显著提升冲突解决能力，减少误判。 |
| **效率** | 自适应路由 + 稀疏 agent 选择 + 早期停止，大幅降低 token 消耗。 |
| **鲁棒性** | 减少无关类型干扰，避免 free-form debate 中的“噪音淹没有效证据”问题。 |

---

## 2. 核心实验方法和设置

### 数据集
在 **9 个基准数据集** 上进行了评估，涵盖三大任务：

| 任务 | 数据集 | 类型数量 | 平均每样本类型数 |
|------|--------|----------|------------------|
| **NER** | CoNLL03, OntoNotes5, SciERC, CrossRE, REDFM | 3–38 | 1.31–4.72 |
| **RE** | DocRED, SemEval2010, SciERC, CrossRE, REDFM | 8–32 | 0.84–2.77 |
| **JERE** | CoNLL04, NYT | — | — |

> 注：部分数据集仅保留高频类型以符合 zero-shot 设置。

### 实验设置
- **模型**：主干模型为 `GPT-3.5-Turbo-0125`，部分实验使用 `gemini-3-flash-preview` 验证泛化性。
- **框架实现**：基于 **AutoGen** 构建多 agent 协作流程。
- **外部工具**：使用 **AlignScore** 作为外部证据评分器。
- **超参数固定**：最大辩论轮次 `Tmax=3`，早停阈值 `Ostop=0.75`, `ε=0.02`。

### 评估指标
- **F1p**（micro Partial F1）：允许预测与真实标签的 span 边界部分重叠。
- **F1s**（Strict F1）：要求完全匹配 span 和类型。
- 报告 **平均 F1p/F1s** 及各数据集表现。

### 基线方法对比
| 类别 | 方法 | 特点 |
|------|------|------|
| **Monolithic Prompting** | AEiO | 一次性提取所有类型 |
| **Each-Type Prompting** | One-Step, G&O | 每种类型单独提示 |
| **Multi-Agent Debate** | CROSSAGENTIE | 多 agent 辩论解决冲突 |

---

## 3. 主要实验结果和性能指标

### 总体性能对比（Tables 2–4）

#### ✅ NER 结果（Table 2）
| 方法 | Avg. F1p | Avg. F1s |
|------|---------|---------|
| AEiO | 42.65 | 35.27 |
| One-Step | 37.64 | 32.62 |
| G&O | 38.78 | 33.16 |
| CROSSAGENTIE | 45.95 | 40.61 |
| **SMADE-IE (Ours)** | **57.32** | **50.45** |

> **提升显著**：相比最强基线 CROSSAGENTIE，F1p 提升 **11.37**，在 OntoNotes5 上高达 **+20.78**。

#### ✅ RE 结果（Table 3）
| 方法 | Avg. F1p | Avg. F1s |
|------|---------|---------|
| AEiO | 18.54 | 11.08 |
| One-Step | 15.19 | 9.23 |
| G&O | 11.89 | 7.60 |
| CROSSAGENTIE | 11.45 | 7.04 |
| **SMADE-IE (Ours)** | **22.37** | **15.71** |

> 在所有 RE 数据集上均取得最佳成绩，平均 F1p 提升 **10.92**。

#### ✅ JERE 结果（Table 4）
| 方法 | Avg. F1p | Avg. F1s |
|------|---------|---------|
| CROSSAGENTIE | 29.87 | 22.91 |
| **SMADE-IE (Ours)** | **44.33** | **36.98** |

> F1p 提升 **14.46**，显示 IERA 模块在联合抽取中的有效性。

---

### Token 效率对比（Table 6）
| 方法 | CoNLL03 (NER) | REDFM (NER) | DocRED (RE) | CrossRE (RE) |
|------|---------------|-------------|-------------|--------------|
| AEiO | 1,078 | 5,460 | — | — |
| One-Step | 1,407 | 7,673 | 7,615 | 6,846 |
| G&O | 2,304 | 14,202 | 9,271 | 14,312 |
| CROSSAGENTIE | 1,508 | 13,480 | 21,784 | 18,923 |
| **SMADE-IE** | **1,094** | **11,514** | **3,240** | **3,765** |

> SMADE-IE 在简单任务上接近 monolithic 成本，在复杂任务上 token 消耗仅为 CROSSAGENTIE 的 **~1/5 到 1/6**。

---

### 消融实验结果（Table 5）

| 变体 | CoNLL04 F1p/F1s | NYT F1p/F1s |
|------|------------------|------------|
| Full SMADE-IE | 58.44 / 44.74 | 30.22 / 29.22 |
| w/o IERA | 59.03 / 42.73 | 24.94 / 22.47 |
| Type-Centric Only | 59.43 / 40.33 | 29.65 / 28.47 |
| w/o Relevant Type Selection | 48.66 / 34.18 | 27.43 / 26.43 |
| w/o Review Agent | 52.75 / 35.12 | 29.50 / 27.56 |
| w/o Debate | 54.13 / 38.02 | 24.24 / 23.38 |
| Global Only | 52.47 / 40.20 | 16.28 / 14.27 |

> 关键发现：
> - **Debate** 和 **Relevant Type Selection** 对性能至关重要。
> - **IERA** 在 NYT 上带来显著提升（F1p +5.28），说明其在长文本中作用明显。
> - **Review Agent** 有助于恢复被 Router 遗漏的类型。

---

## 4. 关键结论和发现

### 主要发现
1. **稀疏 agent 路由优于全量调用**：Adaptive Mode Selector 能有效识别样本复杂度，避免在简单样本上浪费计算资源。
2. **结构化辩论优于自由辩论**：Toulmin 框架 + 外部证据评分 + 贝叶斯更新，使辩论更聚焦、可靠。
3. **早期停止机制高效**：约 60–88% 的案例通过后验收敛停止，平均辩论轮次仅 **1.75–2.76**（最大 3 轮）。
4. **token 效率显著提升**：得益于稀疏性和早停，SMADE-IE 在保持高性能的同时大幅降低开销。

### 方法的局限性
1. **依赖冻结的外部证据评分器**：AlignScore 的性能上限限制了贝叶斯更新的可靠性。
2. **在长文档密集类型场景下效率优势减弱**：如 REDFM，辩论次数仅减半，未达数量级下降。
3. **实验局限于闭源模型**：主要使用 GPT-3.5-Turbo，未在小型开源模型或多语言场景中验证。

### 未来工作方向
- 探索更高效的 **debate scheduling 策略**。
- 扩展至 **更复杂的 structured extraction 任务**（如事件抽取）。
- 在 **open-source LLMs** 和 **multilingual schemas** 上进行验证。
- 引入 **动态证据评分器微调** 以突破当前瓶颈。

--- 

> **总结**：SMADE-IE 是首个将 **稀疏 agent 路由** 与 **结构化证据驱动辩论** 相结合的 zero-shot IE 框架，在 **性能** 和 **效率** 上全面超越现有方法，为多 agent 协作提供了新的设计范式。

</details>

---

### 8. [When Both Layers Learn: Training Dynamics of Representing Linear Models via ReLU Networks](https://arxiv.org/abs/2606.04476)

**Authors**: Berk Tinaz, Changzhi Xie, Mahdi Soltanolkotabi  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2606.04476v1  

#### Abstract
In this paper, we study the gradient descent dynamics for jointly training both layers of a one-hidden-layer ReLU network to fit a linear target function. Concretely, we consider a realizable setting where inputs are drawn i.i.d. from a Gaussian distribution and labels follow a planted linear model....

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：When Both Layers Learn: Training Dynamics of Representing Linear Models via ReLU Networks**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
该论文研究了在**端到端训练（end-to-end training）**场景下，使用一个单隐藏层 ReLU 网络拟合线性目标函数 $ y = \mathbf{a}^\top \mathbf{x} $ 时，**同时训练输入层（inner layer）和输出层（outer layer）权重**的梯度下降（GD）动态行为。

尽管目标函数是线性的且看似简单，但由于 ReLU 的非线性激活，损失景观（loss landscape）中存在大量**非严格鞍点（non-strict saddle points）**——这些点的梯度为零、Hessian 半正定但有零特征值，导致 GD 可能停滞。因此，从随机初始化出发，GD 是否总能成功逃离坏的驻点并收敛到全局最优解是一个未被充分理解的问题。

### **提出了什么新方法或新思路**
作者提出了一种**精细化的轨迹级分析（trajectory-level analysis）**框架，将 GD 动态划分为三个阶段，并通过严格的数学证明揭示其收敛机制：

1. **对齐阶段（Alignment Phase）**  
   初始小权重下，隐藏层权重 $ \mathbf{w}_1, \mathbf{w}_2 $ 快速与目标方向 $ \pm\mathbf{a} $ 对齐，同时输出层权重 $ v_1, v_2 $ 维持正确的符号模式（如 $ v_1 > 0, v_2 < 0 $）。

2. **增长阶段（Growth Phase）**  
   在保持对齐的前提下，两层参数的范数协同增长，推动有效参数（effective parameters）接近真实尺度，从而远离平坦的鞍点区域。

3. **局部精炼阶段（Local Refinement Phase）**  
   进入良好条件区域后，已对齐的神经元快速收敛至 $ \pm\mathbf{a} $，实现线性速率的快速局部收敛。

此外，作者发展了新的技术工具：
- **轨迹级一致集中不等式（uniform concentration bounds along the trajectory）**：处理有限样本重复使用带来的统计依赖性。
- **不平衡项控制（imbalance control）**：分析内外层权重之间的动态平衡关系。

### **相比现有方法的优势**
| 方向 | 本文优势 |
|------|--------|
| **理论深度** | 首次完整刻画双层联合训练下的三阶段动态，而非仅固定特征或局部分析。 |
| **初始化要求** | 使用标准的小随机初始化（$ \sigma / \sqrt{d} $），无需特殊谱初始化或预处理。 |
| **样本复杂度** | 达到**阶最优（order-wise optimal）**，即 $ n \gtrsim d $，与信息论极限一致。 |
| **避免鞍点机制** | 不依赖噪声扰动或修改更新规则，而是通过自然动力学证明 GD 自动避开非严格鞍点。 |
| **超越 NTK 范式** | 参数显著偏离初始值，属于“主动学习”（active learning）而非“懒惰训练”（lazy training）。 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **合成数据集**：输入 $ \mathbf{x}_i \sim \mathcal{N}(0, I_d) $，标签由线性模型生成：$ y_i = \mathbf{a}^\top \mathbf{x}_i $。
- 固定维度 $ d = 100 $，目标向量 $ \mathbf{a} = \mathbf{e}_1 $（第一标准基向量），保证旋转对称性下的公平性。

### **实验设置**
- **网络结构**：单隐藏层 ReLU 网络，形式为：
  $$
  f(\mathbf{v}, W, \mathbf{x}) = v_1 \text{ReLU}(w_1^\top \mathbf{x}) - v_2 \text{ReLU}(w_2^\top \mathbf{x})
  $$
  隐藏单元数 $ k = 2 $ 或 $ k > 2 $。
- **优化器**：全批量梯度下降（full-batch GD），步长 $ \eta = 0.1 $。
- **初始化**：
  - 权重 $ w_i^{(0)} \sim \mathcal{N}(0, \sigma^2 I_d) $
  - 输出 $ v_i^{(0)} \sim \chi^2(d) $（卡方分布，用于技术便利）
  - 小初始化：$ \sigma = 10^{-8} $；大初始化：$ \sigma = 1 $
- **实现工具**：PyTorch
- **硬件平台**：Intel Xeon Gold 5220R CPU

### **评估指标**
- **角度变化**：$ \angle(\mathbf{w}_1, \mathbf{a}), \angle(\mathbf{w}_2, -\mathbf{a}) $
- **参数范数演化**：$ \|v_1\|, \|w_1\|, \|v_2\|, \|w_2\| $
- **损失值**：population loss 和 empirical loss
- **最终是否收敛到全局最优**：检查 $ \mathbf{w}_1 \approx \mathbf{a}, \mathbf{w}_2 \approx -\mathbf{a} $

### **基线方法对比**
本文为理论驱动工作，未直接对比其他算法，但文中明确指出其设定区别于以下典型方法：
- **NTK 分析**：假设参数不变，无法解释特征学习。
- **谱初始化方法**：需要额外计算，不符合“默认初始化”实践。
- **仅训练一层的方法**：忽略表示学习的本质。
- **带噪声/截断的 GD**：人为干预优化过程。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**
| 设置 | 结果 |
|------|------|
| $ k = 2 $, 小初始化 | 大概率收敛到全局最优；失败通常因 $ v_1^{(0)}, v_2^{(0)} $ 同号（概率约 1/2） |
| $ k = 2 $, 大初始化 | 易陷入非严格鞍点（如 $ (\mathbf{w}_1,\mathbf{w}_2)=(\mathbf{a}, 2\mathbf{a}) $） |
| $ k > 2 $ | 几乎总是收敛到全局最优，即使个体神经元未完全对齐，但可通过聚合恢复 $ \pm\mathbf{a} $ |

### **与基线方法的对比结果**
- **vs 图 1(b)**：大初始化易陷入鞍点；而小初始化可稳定逃离。
- **vs NTK 预测**：NTK 无法预测方向对齐现象，说明其不足以描述实际训练动态。
- **vs 固定特征假设**：若只训一层，不能体现三阶段动态，也无法解释为何 GD 能学会表示。

### **消融实验结果**
虽然没有传统意义上的“消融”，但作者通过多个配置验证了核心机制：
- **不同 $ k $ 值的影响**：$ k=2 $ 存在符号陷阱，$ k>2 $ 更鲁棒。
- **不同初始化尺度**：小初始化是成功的关键。
- **多输出扩展（$ r > 1 $）**：观察到“配对行为”（pairing behavior）——每两个神经元形成 $ (v_i \approx -v_j, \mathbf{w}_i \approx -\mathbf{w}_j) $ 的结构，自然推广了 $ v=\pm1 $ 模式。

---

## **4. 关键结论和发现**

### **论文的主要发现**
1. **三阶段动态普遍存在**：GD 在学习线性函数时表现出清晰的三阶段演化路径：对齐 → 增长 → 精炼。
2. **小初始化至关重要**：适度小的初始化有助于 GD 自然进入有利的动力学路径，避免陷入非严格鞍点。
3. **GD 能自动避开坏驻点**：无需任何外部扰动，GD 动力学本身具有隐式偏向（implicit bias），使其倾向于逃离平坦鞍区。
4. **过参数化提升鲁棒性**：当 $ k > 2 $ 时，即使单个神经元未完美对齐，也能通过节点聚合（node aggregation）恢复目标方向。
5. **多输出下的结构性配对**：在 $ r > 1 $ 场景中，隐藏单元自动形成成对结构，对应正负 ReLU 分支。

### **方法的局限性**
- **仅限于 $ k=2 $ 的理论证明**：当前理论分析集中在精确参数化情形（exact parameterization），尚未覆盖 $ k > 2 $ 的过参数化情况。
- **特定初始化设计**：输出权重采用 $ \chi^2 $ 初始化以提高成功概率，在 $ k=2 $ 下 Gaussian 初始化只能保证常数成功概率。
- **高斯输入假设**：理论依赖于 $ \mathbf{x} \sim \mathcal{N}(0,I) $，对更一般分布的适用性有待验证。
- **仅考虑 population/empirical loss**：未涉及泛化误差分析。

### **未来工作方向**
- 将理论扩展至 **$ k > 2 $ 的过参数化设置**，结合节点聚合思想。
- 探索 **更一般的输入分布** 下的训练动态。
- 研究 **泛化能力** 与三阶段动态的关系（例如是否对齐阶段决定归纳偏置）。
- 将该分析框架应用于 **更深网络或多层联合训练** 场景。
- 探讨如何利用此发现改进初始化策略或优化器设计，提升训练稳定性。

--- 

> ✅ **总结一句话**：  
> 本论文首次系统揭示了双层 ReLU 网络在学习线性函数时的三阶段训练动态，证明了小初始化下 GD 可以以线性速率、阶最优样本复杂度逃离非严格鞍点并收敛到全局最优，为理解神经网络中的特征学习提供了重要理论基础。

</details>

---

### 9. [Imbuing Large Language Models with Bidirectional Logic for Robust Chain Repair](https://arxiv.org/abs/2606.05030)

**Authors**: Zehua Cheng, Wei Dai, Jiahao Sun, Thomas Lukasiewicz  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.05030v1  

#### Abstract
Autoregressive chain-of-thought (CoT) reasoning in large language models (LLMs) is fundamentally forward-directed: each step conditions only on prior tokens. This unidirectional inductive bias renders even capable models susceptible to error snowballing, wherein a single logical or arithmetic mistak...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Imbuing Large Language Models with Bidirectional Logic for Robust Chain Repair

## 1. 论文的主要贡献和创新点

### 解决的问题
大型语言模型（LLM）在进行复杂推理时普遍采用**autoregressive Chain-of-Thought (CoT)** 推理机制，其生成过程是严格前向因果的（forward-directed），即每一步只能依赖之前的 token。这种单向归纳偏置导致一个严重问题：**error snowballing（错误雪崩）**——一旦早期步骤出现逻辑或算术错误，后续所有推理都会基于这个错误前提展开，最终导致整个推理链崩溃。

尽管 LLM 在检测自身错误方面能力较弱，但在已知错误位置的情况下纠正错误的能力较强。这表明限制因素并非模型缺乏推理能力，而是缺少一种能同时利用**起点前提（premise）和终点目标（milestone）** 进行双向约束的机制。

---

### 提出的新方法：Teleological Reasoning Infilling (TRI)

TRI 是一种训练与推理框架，赋予标准 decoder-only Transformer 模型原生的、目标条件化的“桥梁”生成能力。

#### 核心创新点：

1. **Prefix-Suffix-Middle (PSM) 序列架构**
   - 引入三个专用的哨兵 token：`<teleo_premise>`、`<teleo_milestone>`、`<teleo_bridge>`。
   - 将输入重排为 `[Q + <teleo_premise> + P + <teleo_milestone> + S + <teleo_bridge> + M]`。
   - 利用标准 causal attention 机制，使中间桥接序列 `M` 能够同时 attend（attend to）前置前提 `P` 和后置里程碑 `S`，无需修改自注意力结构。

2. **两阶段符号化训练流程**
   - **Supervised Fine-Tuning (SFT)**：在形式数学语料库中提取经过符号验证的 `(Q, P, S, M)` 四元组进行监督微调。
   - **Direct Preference Optimization (DPO)**：使用确定性的符号验证器（如 Lean 4 / Python）作为唯一奖励信号，避免 LLM judge 的奉承偏差（sycophancy）。

3. **双系统推理修复算法（Dual-System Inference Repair）**
   - TRI 不作为独立零样本推理器，而是一个**手术式修复模块**。
   - 流程：
     1. 由因果草稿模型（causal draft model）生成初始推理链；
     2. 符号验证器定位第一个失败点；
     3. TRI 模型仅对损坏段落进行 infilling 修复，保留已验证部分；
     4. 循环直至成功或预算耗尽。

4. **理论保证：拓扑一致性（Topological Consistency）**
   - 在温和的 Lipschitz 平滑假设下，证明 PSM 训练目标可诱导生成的桥接序列以高概率保持与 `P` 和 `S` 的全局一致性。

5. **无需额外结构修改即可实现双向推理**
   - 通过 PSM 重排序，在不改变模型架构的前提下实现了真正的 bidirectional conditioning。

---

### 相比现有方法的优势

| 维度 | TRI | 现有方法（CoT, ToT, MathFimer 等） |
|------|-----|-------------------------------|
| 方向性 | Teleological（目的论导向） | Forward-only 或伪双向 |
| 错误处理 | 手术式修复，保留正确部分 | 重采样、搜索、回溯等全局再生 |
| 验证机制 | 确定性符号验证器（Lean/Python） | LLM judge 或无验证 |
| 效率 | 显著降低 token 开销 | 成本随深度指数增长 |
| 归纳偏置 | 内建双向逻辑约束 | 仅前向传播 |

> ✅ **本质区别**：TRI 将“如何从 A 到 B”的路径插值任务内化到训练过程中，而非依赖推理时的外部包装或搜索策略。

---

## 2. 核心实验方法和设置

### 使用的数据集

| 数据集 | 描述 |
|-------|------|
| **MATH** | 包含 12,500 道竞赛级数学题（AMC/AIME/Olympiad），按难度分为 L1–L5，测试集 5,000 题。重点关注 L4/L5。 |
| **HumanEval-Fix** | 来源于 HumanEval 的代码修复任务，人工注入逻辑错误，共 492 个故障实例，使用 Python 解释器执行单元测试验证。 |
| **Lean-Workbook** | 自然语言数学问题配 Lean 4 形式化证明，测试集 2,500 题，使用 Lean 4 kernel 类型检查验证证明有效性。 |

---

### 实验设置

- **基础模型**：Qwen2.5-72B
- **训练流程**：
  1. **SFT**：在约 780k 来自 MATH 和 Lean-Workbook 的 `(Q,P,S,M)` 四元组上训练 3 轮。
  2. **DPO**：基于 SFT 模型采样候选桥接，用符号验证器构建偏好对，训练 1 轮。
- **推理模式**：greedy decoding（T=0）
- **计算预算**：每题最多 4,096 tokens；TRI 最多允许 3 次修复迭代。

---

### 评估指标

| 指标 | 含义 |
|------|------|
| **Accuracy (%)** | MATH 上答案完全匹配的比例 |
| **Pass@1 (%)** | HumanEval-Fix 中一次修复成功的比例 |
| **PCR (%)** | Proof Completion Rate，Lean-Workbook 上完成可验证证明的比例 |
| **Tok/Prob** | 每道题平均生成 token 数量（衡量效率） |
| **RSR (%)** | Repair Success Rate，初始错误链被成功修复的比例 |
| **V-Calls** | 平均每次推理调用验证器次数（含 EXTRACTMILESTONE 扫描） |

---

### 基线方法对比

| 基线 | 描述 |
|------|------|
| Qwen2.5-72B + CoT | 当前最强开源模型 + 零样本 CoT |
| Qwen2.5-72B + CoT-SC(k=16) | 自洽性集成，k=16 条链投票 |
| Llama-3.1-70B + CoT / ToT(b=5) | Meta 新一代大模型 + CoT / ToT 搜索 |
| InternLM-StepProver + CoT / CoT-SC(k=8) | 当前 Lean-Workbook SOTA 模型 + CoT 及其集成版 |

> ⚠️ 所有基线共享相同 token 预算，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 2）

| 方法 | MATH L5 Acc (%) | HEval-Fix Pass@1 (%) | Lean-WB PCR (%) | Tok/Prob |
|------|------------------|------------------------|------------------|----------|
| Qwen2.5-72B + CoT-SC | 47.3 | 66.8 | 43.1 | 29472 |
| InternLM-StepProver + CoT-SC(k=8) | 46.8 | 60.3 | 51.2 | 15896 |
| **TRI (Full: SFT+DPO+Repair)** | **53.7** | **74.9** | **57.1** | **1268** |
| **相对提升** | **+6.4pp** | **+8.1pp** | **+5.9pp** | **↓31.2%** |

> ✅ TRI 在三项任务上均达到 **state-of-the-art 性能**，且 token 消耗仅为最佳基线的 **69%**。

---

### 与基线方法的对比结果

- **MATH 难度越高，TRI 优势越明显**：
  - L1: +0.8pp
  - L5: +6.4pp  
  ➜ 表明 TRI 特别擅长处理长链条、易出错的复杂推理任务。

- **HumanEval-Fix 提升显著（+8.1pp）**：
  - 即便未专门针对代码预训练，也能泛化至程序修复场景，说明 PSM 目标具有跨领域通用性。

- **Lean-Workbook 超越专用模型（+5.9pp）**：
  - InternLM-StepProver 经过 Lean 数据专项训练，而 TRI 未经此训练仍胜出，说明 PSM 学到了类似 backward-chaining 的结构化推理能力。

- **效率碾压级优势**：
  - CoT-SC(k=16) 消耗 ~29k tokens/问题，TRI 仅需 ~1.3k，节省 **31.2%** 总开销。
  - 在 B=1k token 极限预算下，TRI 准确率仍领先 **+10.2pp**。

---

### 消融实验结果（Table 4）

| 配置 | MATH L5 Acc (%) | HEval-Fix Pass@1 (%) | Tok/Prob |
|------|------------------|------------------------|----------|
| **TRI Full** | 53.7 | 74.9 | 1268 |
| w/o DPO stage (SFT only) | 49.8 | 68.3 | 1534 |
| w/o repair loop (single-pass) | 52.7 | 73.1 | 1267 |
| w/o symbolic verifier (LLM judge) | 46.2 | 64.1 | 1621 |
| PSM → standard FIM | 50.9 | 70.6 | 1349 |

#### 发现：
- **符号验证器最关键**：替换为 LLM judge 导致性能暴跌 7.5pp，证明神经裁判无法可靠识别逻辑漏洞。
- **DPO 至关重要**：去除 DPO 阶段损失 3.9pp，说明仅靠 SFT 容易产生“空洞桥接”（hollow bridges）。
- **PSM 设计优越**：标准 FIM 顺序效果差于 PSM，说明三段式分离设计更有效。
- **首次可验证里程碑最优**：选择最近的 `S` 可最小化桥接长度，提高成功率。

---

## 4. 关键结论和发现

### 主要发现

1. ✅ **错误雪崩可通过目标导向修复缓解**：将推理视为“从已知前提到已知里程碑之间的路径插值”，可从根本上规避前向累积误差。
2. ✅ **PSM 架构可在标准 decoder-only 模型中实现真正双向推理**：无需修改 attention 结构，仅通过序列重排即可让中间内容感知前后上下文。
3. ✅ **符号验证器是高质量训练的关键**：确定性验证信号远优于 LLM judge，是实现高精度的形式保障。
4. ✅ **手术式修复比全局重生成更高效**：只修复错误片段，大幅降低 token 开销（↓31.2%），尤其适合资源受限场景。
5. ✅ **TRI 泛化性强**：在同一框架下统一解决数学推理、代码修复、形式化证明三大任务。

---

### 方法的局限性

1. **依赖外部验证器**：必须存在可判定的符号验证环境（如 Python eval、Lean type checker），难以直接应用于开放域常识推理。
2. **需要草稿模型先生成轨迹**：不能独立用于零样本推理，必须与其他生成模型配合使用。
3. **里程碑提取可能失败**：若后续若干步内无独立可验证节点（如 Lean 中 tactic 不可单独验证），则 fallback 到全段再生。
4. **训练数据依赖形式化语料**：目前依赖 MATH、Lean-Workbook 等高质量结构化数据，难以扩展到非结构化文本任务。

---

### 未来工作方向

1. **扩展至更多领域**：探索 TRI 在科学计算、硬件验证、法律论证等强逻辑领域的应用。
2. **自动里程碑发现增强**：开发更强的子句分割与局部可验证性判断机制，减少 fallback 概率。
3. **轻量化验证器设计**：研究近似但高效的验证代理，降低对完整编译/执行环境的依赖。
4. **结合强化学习**：引入 PRM 或 RLVR 动态优化修复策略，进一步提升修复成功率。
5. **探索 encoder-decoder 架构适配**：研究如何将 TRI 思想迁移到 T5、BART 等双向编码器模型中。

---

> 🔚 **总结一句话**：  
> TRI 通过 **PSM 重排序 + 符号验证驱动的 DPO + 双系统修复循环**，首次实现了在标准 decoder-only LLM 中原生支持**目标导向的双向逻辑推理**，在准确性与效率上全面超越现有 CoT 范式，为构建鲁棒、可信的 AI 推理系统提供了新范式。

</details>

---

### 10. [PE-MHL: Physics-Encoded Modular Hybrid Layers for Scalable Learning of Complex Systems](https://arxiv.org/abs/2606.04290)

**Authors**: Ismail Hassaballa, Mircea Lazar  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.04290v1  

#### Abstract
Hybrid models that combine physics-based and data-driven components have shown strong potential for achieving accuracy and interpretability in control applications. While recent methods have made progress in incorporating physical consistency, challenges remain in scalability, robustness to noise, a...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：PE-MHL: Physics-Encoded Modular Hybrid Layers for Scalable Learning of Complex Systems

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前 **hybrid modeling**（混合建模）方法虽然结合了物理模型的可解释性和数据驱动模型的表达能力，但仍面临以下挑战：
- **Scalability**（可扩展性）不足，难以处理高维或多物理场系统；
- 在噪声环境下，神经网络容易“覆盖”物理模型，导致 **interpretability**（可解释性）丧失；
- 缺乏对模型复杂度增长的理论保障，训练过程不稳定。

### 🚀 提出的新方法：PE-MHL 框架
本文提出 **Physics-Encoded Modular Hybrid Layers (PE-MHL)**，一种渐进式模块化混合建模框架，其核心思想是：
- 以一个 **physics-encoded base model**（物理编码基础模型）为起点；
- 逐步添加轻量级的 **neural sub-models** 来拟合残差（residual errors），每新增一个子模型只增加必要复杂度；
- 所有已训练组件通过 **deviation penalty** 被锚定，防止被后续训练破坏。

### 🔍 相比现有方法的优势
| 方面 | PE-MHL 的优势 |
|------|----------------|
| **可解释性** | 物理模型始终被保留并约束在初始估计附近，避免被神经网络“抵消”；引入 `L_penalty` 显式保护物理分支结构。 |
| **可扩展性与模块化** | 支持按需扩展，适合多物理场系统；每个 sub-model 只学习未被捕捉的残差模式。 |
| **理论保证** | 首次提供 **monotonic non-increasing training error**（训练误差单调不增）及 **convergence guarantee**（收敛性证明）；满足几何衰减条件时误差指数趋零（Corollary 1）。 |
| **训练稳定性** | 比 monolithic neural network 更平滑的优化轨迹，振荡更小，收敛更快。 |

> 💡 创新本质：将 boosting 思想引入 hybrid modeling，同时保持物理一致性与模块独立性，并赋予严格数学支撑。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集
共三个基准任务，从简单到复杂递进验证：

| 数据集 | 类型 | 描述 |
|--------|------|------|
| **Static nonlinear function** [16] | 静态非线性函数 | $ g(x) = \sin(x)(1 - x),\ x \in [0,1] $，叠加高斯噪声（var=0.000468） |
| **Nonlinear NARX system** [17] | 动态系统（仿真） | 差分方程：<br>$ y(k) = 0.5y(k-1) + 0.3u(k-1) + 0.3u(k-1)y(k-1) + 0.5u^2(k-1) $ |
| **Quanser Aero 2 platform** | 真实物理系统 | 两自由度直升机实验平台，仅激活 yaw dynamics；输入电压经 differential drive 控制双电机反向旋转产生偏航力矩 |

### ⚙️ 实验设置
- **训练策略**：逐阶段添加 sub-model，每次冻结前序参数，仅微调新模块输出层 + deviation penalty；
- **初始化**：新 sub-model 输出层采用 **least-squares initialization**；
- **输入构造**：
  - NARX：使用滞后项 $ y(k-1), u(k-1) $
  - Aero 2：使用前 23 步输入和 15 步输出构建 ARX 特征向量 $ x(k) $

### 📊 评估指标
| 指标 | 含义 |
|------|------|
| **Train/Test MAE** | 平均绝对误差 |
| **Train/Test MSE** | 均方误差 |
| **Unit-step response accuracy** | 阶跃响应稳态值偏差比较 |
| **Training loss trajectory** | 观察优化动态稳定性 |

### 🆚 基线方法对比
| 方法 | 描述 |
|------|------|
| **Monolithic Neural Network** | 参数总量与 PE-MHL 所有 sub-models 总和相当的单一大网络（如三层 300 ReLU neurons） |
| **Two-branch hybrid without penalty** | Polynomial + NN 结构但无正则项，用于展示 interpretability 必要性 |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据汇总（来自 Table I 和 Figures）

#### ✅ Quanser Aero 2 实验最终性能（Test Set）
| 指标 | Monolithic NN | **PE-MHL Ensemble** | 提升幅度 |
|------|---------------|--------------------|----------|
| **Test MAE** | 0.0174587 | **0.0031702** | ↓ ~81.8% |
| **Test MSE** | 0.0003348 | **0.0000154** | ↓ ~95.4% |

> ✔️ PE-MHL 在测试集上表现远超等参量的单一神经网络。

#### ✅ NARX 单位阶跃响应（Multisine 输入训练后）
| 模型 | 稳态输出 | 相对于真值（4.0）误差 |
|------|---------|------------------|
| True NARX | 4.0 | — |
| Monolithic NN | 3.95 | ~1.25% |
| **PE-MHL** | **3.97** | **~0.75%** |

> ✔️ PE-MHL 更接近真实动态，具备更强泛化能力。

#### ✅ 训练误差下降趋势（Fig. 10）
- 添加第1–3个 sub-model 时 MSE 显著下降（6.64×10⁻⁵ → 4.98×10⁻⁵）；
- 超过 L=4 后趋于饱和，符合 **diminishing returns** 分析；
- 支持自然早停（natural stopping criterion）。

#### ✅ 训练动态对比（Fig. 11）
- **PE-MHL**：损失曲线平稳下降，每500 epoch 新增 sub-model 后继续优化；
- **Monolithic NN**：震荡剧烈，收敛慢；
> ✔️ 表明 PE-MHL 拥有更好的优化条件（better conditioned residual learning）。

### 🔍 消融实验结果（隐含分析）
- **有无 penalty 对比（Fig. 3 vs Fig. 7）**：
  - 无 penalty 时，polynomial 与 NN 分支互为逆操作，失去物理意义；
  - 加入 `L_penalty` 后，polynomial 保持原始形状，NN 专注拟合残差；
> ⇒ 验证了 **deviation penalty 对 interpretability 至关重要**。

- **sub-model 数量影响**：
  - 前几个 sub-model 贡献显著提升；
  - 后续增益递减，支持有限模块数即可达到最优；
> ⇒ 符合理论预测（Proposition 1 & Corollary 1）

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **PE-MHL 实现了 accuracy 与 interpretability 的统一**：
   - 物理模型结构得以保留；
   - 数据驱动部分专注于“补足残差”，而非重构全部行为。

2. **训练误差单调不增且收敛有理论保障**：
   - 在 persistent excitation 条件下，least-squares 初始化确保 $ E_L \leq E_{L-1} $；
   - 误差增量 $ \Delta_L \to 0 $，支持自然停止规则。

3. **几何衰减成立时误差指数趋零**：
   - 若每个 sub-model 至少消除固定比例剩余误差，则整体误差呈几何级数下降至零。

4. **实际性能全面优于 monolithic 架构**：
   - 更高的预测精度；
   - 更好的泛化能力（test error < train error）；
   - 更稳定的训练过程。

5. **模块化设计带来自校正机制（self-correction）**：
   - 早期组件的小误差可由后期 sub-model 修正，增强鲁棒性。

---

### ⚠️ 方法的局限性
| 局限 | 说明 |
|------|------|
| **依赖良好的 base model 设计** | 若初始物理模型严重偏离真实系统，残差过大，可能需要过多 sub-models 才能补偿。 |
| **sequential training 效率较低** | 不能并行训练所有 sub-models，总训练时间随模块数量线性增长。 |
| **deviation penalty 超参数选择敏感** | $ \lambda_{\text{dev}} $ 过大会限制学习能力，过小则无法锚定旧模型。 |

---

### 🔮 未来工作方向
1. **自动化 sub-model selection 机制**：
   - 开发基于残差统计特征的自动判断准则，决定是否添加新模块。

2. **多物理场系统的扩展应用**：
   - 将不同 sub-models 分配给不同物理域（如 thermal, mechanical, electrical），实现 multi-physics hybrid modeling。

3. **在线/增量学习场景适配**：
   - 探索 PE-MHL 在 streaming data 或 adaptive control 中的应用潜力。

4. **与其他 continual learning 技术融合**：
   - 如结合 **progressive networks** 或 **elastic weight consolidation (EWC)**，进一步提升知识保留能力。

---

## ✅ 总结
**PE-MHL** 是一种兼具 **理论严谨性** 与 **工程实用性** 的 hybrid modeling 框架。它不仅解决了传统混合模型中物理可解释性易丢失的问题，还通过模块化结构实现了 **scalable**, **robust**, 和 **interpretable** 学习，在多个 benchmark 和真实系统上均展现出显著优于 monolithic neural networks 的性能。该工作为复杂系统的建模、控制与故障诊断提供了新的范式。

</details>

---

### 11. [STaR-Quant: State-Time Consistent Post-Training Quantization for Diffusion Large Language Models](https://arxiv.org/abs/2606.04945)

**Authors**: Xin Yan, Aqiang Wang, Zhenglin Wan, Xingrui Yuand Ivor Tsang  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2606.04945v1  

#### Abstract
Diffusion large language models (DLLMs) have recently emerged as a promising alternative to autoregressive LLMs by generating text through iterative masked denoising with bidirectional context. However, their large model sizes and iterative denoising process introduce substantial memory and computat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：STaR-Quant: State-Time Consistent Post-Training Quantization for Diffusion Large Language Models

---

## 1. 论文的主要贡献和创新点

### 解决的问题
**Diffusion Large Language Models (DLLMs)** 虽然在文本生成任务中展现出优于自回归模型（如 LLaMA、Qwen）的并行解码能力和双向上下文建模优势，但其迭代去噪机制和大规模参数带来了显著的内存与计算开销。现有的 **Post-Training Quantization (PTQ)** 方法（如 AWQ、QuaRot）直接应用于 DLLMs 时，在低比特（如 W4A4）量化下性能严重下降。

作者识别出两个关键挑战：
- **State-Dependent Activation Disparity**：在每一步去噪过程中，序列中同时存在 **masked** 和 **unmasked** token，它们的激活值分布差异大（例如 outlier 分布不同），单一量化空间难以有效处理。
- **Temporal Error Accumulation**：由于生成是多步迭代过程，量化误差会在多个时间步间累积，尤其在 attention 中的 `softmax-value` 乘法操作中尤为敏感。

### 提出的新方法
为解决上述问题，论文提出 **STaR-Quant** —— 一种面向 DLLMs 的 state-time 一致的 PTQ 框架，包含两大核心组件：

#### ✅ State-Guided Activation Transformation (SGAT)
- 将隐藏维度分解为 **shared**、**masked-specific** 和 **unmasked-specific** 子空间。
- 对不同状态的 token 应用不同的激活变换路径（通过二元门控实现），使其进入更适合的量化子空间。
- 权重侧保持 **统一静态变换**（unified weight-side transformation），避免重复存储变换后的权重，提升推理效率。

> 📌 创新点：首次将“token 状态”作为激活变换的条件变量，实现状态感知的量化平滑。

#### ✅ Temporal Attention Compensation (TAC)
- 在 attention 输出投影前插入一个轻量级补偿模块。
- 采用 **block-wise affine mapping** 对量化后的 attention 表示进行校正，目标是匹配其与全精度版本的一阶和二阶统计量（均值与协方差）。
- 使用闭式求解（closed-form estimation），结合奇异值平滑与恒等收缩（identity shrinkage）增强稳定性。

> 📌 创新点：不修改 attention 计算本身，而是对输出表示进行事后补偿，有效缓解跨时间步的误差积累。

### 相比现有方法的优势
| 方法 | 是否支持状态感知 | 是否处理时间误差 | 是否保持统一权重 | 推理效率 |
|------|------------------|------------------|--------------------|----------|
| AWQ / SmoothQuant | ❌ | ❌ | ✅ | 高 |
| QuaRot | ❌ | ❌ | ❌（需旋转权重） | 中 |
| DLLMQuant | ⚠️部分考虑 | ⚠️仅限权重量化 | ✅ | 高 |
| **STaR-Quant** | ✅ | ✅ | ✅ | **高 + 可忽略额外开销** |

> ✔️ 在几乎不增加推理延迟的前提下，显著提升低比特量化下的模型保真度。

---

## 2. 核心实验方法和设置

### 使用的模型
- **LLaDA-8B** (Nie et al., 2025)
- **LLaDA-1.5-8B** (Zhu et al., 2025)
- **Dream-7B** (Ye et al., 2025)

均为典型的基于 masked diffusion 的大型语言模型。

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **RTN** (Round-To-Nearest) | Vanilla baseline | 最基础的量化方式 |
| **AWQ** | Activation-aware weight quantization | 保留重要通道权重 |
| **QuaRot** | Rotation-based PTQ | 使用 Hadamard 旋转消除异常值 |
| **DLLMQuant** (+, ++) | DLLM-specific PTQ | 基于 AWQ 或 QuaRot 的改进版，本文最强 baseline |

> 注：DLLMQuant++ 是以 QuaRot 为基础的增强版本。

### 数据集与评估任务
使用 **Winogrande** 数据集中的 128 段用于 calibration（无需微调）。

评估涵盖三大类任务共 9 个 benchmark：
1. **通用知识与推理**
   - TruthfulQA-MC2, ARC-Challenge, HellaSwag, WinoGrande, PIQA, MMLU, C-EVAL
2. **数学推理**
   - GSM8K（多步推理）
3. **代码生成**
   - HumanEval（代码补全）

> 所有任务均报告 **accuracy** 或 **pass@1** 指标，最终取平均分（Avg.）进行比较。

### 量化配置
- 主要实验：**W4A4**（4-bit weights & activations）
- 补充实验：**W8A8**
- 无 fine-tuning，纯 post-training calibration
- 使用 NVIDIA A40 GPU 进行测试

---

## 3. 主要实验结果和性能指标

### 关键性能数据（W4A4）

| Model | Method | Avg. Score | Δ vs FP |
|-------|--------|------------|---------|
| LLaDA-8B | FP16 | 58.99 | – |
| | RTN | 44.23 | -14.76 |
| | AWQ | 48.09 | -10.90 |
| | QuaRot | 51.03 | -7.96 |
| | DLLMQuant++ | 54.29 | -4.70 |
| | **STaR-Quant** | **57.07** | **-1.92** |
| | → **↑ +2.78 pts vs DLLMQuant++** |

| LLaDA-1.5-8B | FP | 69.86 | – |
| | DLLMQuant++ | 64.31 | -5.55 |
| | **STaR-Quant** | **66.93** | **-2.93** |
| | → **↑ +2.62 pts** |

| Dream-7B | FP | 66.94 | – |
| | DLLMQuant++ | 61.90 | -5.04 |
| | **STaR-Quant** | **63.59** | **-3.35** |
| | → **↑ +1.69 pts** |

> 🔺 **STaR-Quant 显著缩小了量化模型与 FP16 的差距，平均仅损失约 2 pts，远优于所有 baseline**

### 细粒度任务表现亮点
- **MMLU & C-EVAL**：大幅领先，说明能更好保留多领域知识。
- **GSM8K & HumanEval**：在复杂推理和代码生成上持续提升，验证了对中间表示稳定性的保护能力。
  - 如在 LLaDA-8B 上，HumanEval 从 28.92 (DLLMQuant++) 提升至 **35.98**，接近 FP 水平（32.92）。

### 消融实验（Ablation Study on LLaDA-8B）

| 方法 | Avg. | Δ↓ vs Full |
|------|------|-----------|
| STaR-Quant (full) | **57.07** | 0.00 |
| w/o TAC | 55.43 | -1.64 |
| w/o SGAT | 56.39 | -0.68 |

> ✅ 证明 **TAC 对抑制时间误差更重要**，但两者互补，联合使用效果最佳。

### TAC 块大小影响（Block Size $g$）

| Block Size $g$ | 4 | 8 | 16 | 32 | 64 |
|------------------|-----|-----|-----|-----|-----|
| Avg. Accuracy | 52.48 | 54.66 | **57.07** | 56.39 | 56.03 |

> ✅ 最佳块大小为 **16**，过大导致协方差估计不稳定，过小则表达能力不足。

### 效率指标（Speed & Memory）

| Model | Speedup (vs FP16) | Memory Saving |
|-------|--------------------|----------------|
| LLaDA | 1.65× | 3.05× |
| LLaDA-1.5 | 1.64× | 3.05× |
| Dream | **1.69×** | **3.14×** |

> 💡 即使引入 TAC 和 SGAT，仍实现高达 **1.66× 平均加速** 和 **超 3× 内存压缩**，适合边缘部署。

---

## 4. 关键结论和发现

### 主要发现
1. **DLLMs 的量化必须考虑“状态”与“时间”双重特性**：
   - 不同 token 状态（masked/unmasked）需要差异化处理；
   - 多步迭代要求控制误差传播路径。

2. **SGAT + TAC 构成了高效的 state-time 一致性框架**：
   - SGAT 解决层内激活分布不一致问题；
   - TAC 解决跨步骤误差累积问题；
   - 二者协同作用，显著提升量化鲁棒性。

3. **无需微调即可实现接近 FP16 性能的 W4A4 量化**：
   - 在多个主流 DLLMs 上验证有效性；
   - 平均准确率损失 < 2 pts，极具实用价值。

### 局限性
- 当前主要针对 **masked-denoising type DLLMs**，是否适用于其他 diffusion 架构（如 continuous diffusion）尚待验证。
- 更激进的量化（如 W3A3、W2A2）仍未解决，可能需要更强的变换或补偿机制。
- TAC 引入的 block-wise affine 映射虽轻量，但仍需专用融合 kernel 才能最大化速度收益。
- 当前状态建模仅为 binary（mask / not mask），未考虑置信度、语义角色等更细粒度状态。

### 未来工作方向
- 扩展到 **multi-modal diffusion models**（如图文生成）；
- 设计 **confidence-aware state modeling**，动态调整变换强度；
- 探索 **finer-grained token states**（如语法角色、位置敏感性）；
- 开发 **hardware-aware fused kernels** 支持 SGAT/TAC 高效执行；
- 结合 **quantization-aware training (QAT)** 进一步突破极限比特。

---

> ✅ **总结一句话**：  
> **STaR-Quant 是首个专为 Diffusion LLMs 设计的 state-time 一致 PTQ 框架，通过 SGAT 实现状态感知激活变换、TAC 抑制时间误差累积，在 W4A4 下实现接近全精度性能，并带来 1.66× 加速与 3.14× 内存节省，推动 DLLMs 向高效部署迈出关键一步。**

</details>

---

### 12. [StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis](https://arxiv.org/abs/2606.04246)

**Authors**: Prashanth Vijayaraghavan, Apoorva Nitsure, Luyao Shi, Ehsan Degan, Vandana Mukherjee  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04246v1  

#### Abstract
Automatic generation of RTL code for digital hardware designs remains challenging due to long-horizon reasoning, multi-step dependencies, and strict correctness constraints in Verilog and VHDL. We present StepPRM-RTL, a novel framework that combines stepwise trajectory modeling, process-reward model...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
自动化的 **Register-Transfer Level (RTL)** 代码生成在硬件设计自动化（EDA）中具有重要意义，但由于以下挑战而极具难度：
- **长程依赖**（long-horizon reasoning）：RTL 设计需要多步、连贯的决策过程。
- **严格的语义正确性要求**：即使语法正确，时序、并发或控制逻辑错误也会导致功能失效。
- **缺乏中间监督信号**：传统方法仅基于最终输出进行评估（outcome-based），无法指导模型学习正确的推理路径。

现有方法如纯提示（prompting）、监督微调（supervised fine-tuning）或基于最终功能验证的方法，在建模复杂设计流程方面表现不足。

---

### 提出了什么新方法或新思路
本文提出 **StepPRM-RTL**，一个结合 **stepwise reasoning**、**Process Reward Modeling (PRM)** 和 **retrieval-augmented fine-tuning (RAFT)** 的新型框架，用于提升 LLM 在 RTL 合成中的性能。

#### 核心创新点包括：

1. ✅ **Step-Level Process Reward Model (StepPRM)**  
   首次将 PRM 应用于 HDL 领域，并定义在**语义有意义的设计步骤粒度**上打分，而非传统的 token-level 打分。每个步骤包含自然语言 rationale 和对应的 code edit，使奖励更符合硬件设计逻辑。

2. ✅ **PRM-Guided MCTS 探索多样化高质量轨迹**  
   引入 **Monte Carlo Tree Search (MCTS)** 进行结构化搜索，利用 StepPRM 提供的 step-level 奖励引导探索替代推理路径，生成超越人工标注轨迹的高价值训练样本。

3. ✅ **检索增强 + 奖励加权微调（RAFT）**  
   将 RAFT 与 StepPRM 结合，通过从代码库中检索相似设计模式作为上下文，并对高奖励轨迹进行加权微调，实现领域知识与推理能力的融合。

4. ✅ **迭代联合优化闭环**  
   构建“轨迹收集 → StepPRM 更新 → MCTS 探索 → RAFT 微调”的闭环训练流程，持续提升策略模型和奖励模型的质量。

---

### 相比现有方法的优势
| 维度 | 传统方法 | StepPRM-RTL |
|------|--------|-------------|
| 监督粒度 | Token-level 或 outcome-only | Step-level 语义级监督 |
| 推理建模 | 黑箱生成 | 显式建模可解释的 step-by-step 推理轨迹 |
| 探索机制 | 无结构采样 | MCTS 支持结构化、有导向的路径探索 |
| 泛化能力 | 依赖大量标注数据 | 利用检索增强和合成轨迹提升泛化 |

> 🌟 **优势总结**：StepPRM-RTL 实现了从“只关注结果”到“理解如何达成正确结果”的转变，显著提升了长程推理能力和功能正确率。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **Verilog-Eval** [11]：包含 156 个来自 HDLBits 的自然语言 → Verilog 任务，配备自检 testbench。
- **VHDL-Eval** [18]：包含 202 个翻译自 Verilog-Eval 的 VHDL 版本任务，同样带验证环境。
- **内部 RTL-IR Corpus**：用于训练初始模型，包含 spec、code 及其 stepwise 分解轨迹。

> ⚠️ 注意：Verilog-Eval 和 VHDL-Eval 是严格 hold-out 的测试集，不参与训练。

---

### 实验设置和评估指标

#### 主要评估指标
| 指标 | 定义 |
|------|------|
| **Pass@1** | 第一次生成的完整 RTL 实现能否通过官方 testbench 验证（即功能正确） |
| **Reasoning Fidelity (%)** | 使用 LLM judge 对比生成的 reasoning 轨迹与标准轨迹的一致性得分，衡量中间推理质量 |

#### 模型架构与实现细节
- **基础模型**：Qwen3-8B-Instruct
- **StepPRM**：基于相同 backbone 的回归头模型，输入为 (spec, partial code, step)，输出 scalar reward
- **Retriever**：Qwen3-Embedding-4B，用于 RAFT 中检索相关设计模板
- **MCTS 设置**：每条 spec 执行 50 次模拟，rollout 深度为 10 步，探索常数 `c_uct=1.5`
- **训练流程**：先监督初始化 → MCTS 扩展轨迹 → StepPRM 再训练 → RAFT 奖励加权微调，循环迭代

---

### 基线方法对比
| 类别 | 基线方法 |
|------|---------|
| **Prompt-based** | Vanilla Prompting (GPT-4o), CoDes (GPT-4o) |
| **Fine-tuning based** | RTLCoder (Mistral), CodeV (CodeQwen), VeriThoughts |
| **RAG-enhanced** | RAG-CodeBERT (GPT-4o), RAG-FT (GPT-4o) |
| **消融变体** | No MCTS, No PRM, Supervised RAFT Only |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（见 Table 2）
| Model | Pass@1 (Verilog) | Pass@1 (VHDL) | Reasoning Fidelity (Verilog) | Reasoning Fidelity (VHDL) |
|-------|------------------|---------------|-------------------------------|------------------------------|
| **StepPRM-RTL (Full)** | **0.857** | **0.786** | **82.5%** | **80.2%** |
| RAG-FT (GPT-4o) | 0.719 | 0.531 | — | — |
| VeriThoughts | 0.755 | — | 60.4% | — |
| RTLCoder | 0.625 | — | — | — |

> 🔺 **相比最佳基线提升超过 10%**（以 Pass@1 计），且在两种语言上均取得 SOTA 表现。

---

### 与基线方法的对比结果
- StepPRM-RTL 在 **Verilog 和 VHDL 上全面领先所有基线**，尤其在复杂任务中优势明显。
- 相比最强的 RAG-FT 方法，Pass@1 提升达 **+13.8pp (Verilog)** 和 **+25.5pp (VHDL)**。
- Prompting 方法（如 GPT-4o）表现较差，说明仅靠预训练知识不足以解决 RTL 合成问题。
- 即使是 finetuned 模型（如 VeriThoughts），也因缺乏 step-level 监督而在推理保真度上落后。

---

### 消融实验结果（Ablation Studies）
| 变体 | Pass@1 (Verilog ↓) | Pass@1 (VHDL ↓) | Reasoning Fidelity ↓ |
|------|--------------------|------------------|------------------------|
| **Full Model** | 0.857 | 0.786 | 82.5% / 80.2% |
| No MCTS (Sampling-only) | 0.810 (-4.7pp) | 0.738 (-4.8pp) | -4.3pp / -3.7pp |
| No PRM (Outcome-only reward) | 0.781 (-7.6pp) | 0.709 (-7.7pp) | -9.4pp / -9.4pp |
| Supervised RAFT Only | 0.796 (-6.1pp) | 0.721 (-6.5pp) | -7.2pp / -7.2pp |

#### 消融分析结论：
1. **MCTS 至关重要**：结构化搜索能有效避免无效路径，提高轨迹质量。
2. **StepPRM 是核心驱动力**：去除 step-level 奖励后性能大幅下降，证明 outcome-only 奖励过于稀疏，难以支撑长程推理。
3. **Reward-weighted RAFT 提升泛化**：单纯复制轨迹不如优先学习高奖励路径。

---

## 4. 关键结论和发现

### 论文的主要发现
1. ✅ **Step-level supervision 显著优于 outcome-only learning**  
   在 RTL 合成这类长程任务中，提供中间反馈至关重要。StepPRM 成功实现了对“好设计决策”的细粒度识别。

2. ✅ **MCTS + PRM 实现高效探索**  
   结构化搜索结合语义奖励，可在合理计算成本下发现高质量的新颖设计路径，缓解 bootstrap bias。

3. ✅ **RAFT + Reward Weighting 提升策略稳定性**  
   检索增强提供上下文支持，奖励加权确保模型聚焦于最优行为序列，二者结合显著优于普通微调。

4. ✅ **框架具备跨语言通用性**  
   在 Verilog 和 VHDL 上均取得优异表现，表明方法不依赖特定语法，适用于多种 HDL。

---

### 方法的局限性
- 当前主要面向单模块 RTL 合成，尚未扩展至多文件、层次化系统设计。
- MCTS 推理开销较高（需多次 rollout），影响部署效率。
- StepPRM 依赖人工构造的高质量轨迹进行初始化，冷启动阶段仍需专家干预。
- 形式化验证未完全集成进 reward shaping，目前主要依赖轻量级语法检查和 AST 对齐。

---

### 未来工作方向
1. **扩展至 hierarchical design**：支持跨模块接口推断与协同综合。
2. ** tighter integration with formal verification**：将等价性检查（equivalence checking）、属性验证（assertion checking）纳入 reward model。
3. **cross-architecture transfer**：研究在 Verilog 上学到的 reasoning pattern 是否可迁移到 VHDL 或 SystemVerilog。
4. **降低 MCTS 开销**：探索蒸馏策略或将 MCTS 策略转化为快速推理 policy。
5. **端到端 trainable 架构**：尝试 joint training StepPRM 与 generator，减少模块间误差传播。

---

## 总结
📌 **StepPRM-RTL 是首个将 step-level process reward modeling 成功应用于 RTL 合成的工作**，通过引入可解释的 stepwise 推理轨迹、结构化搜索（MCTS）与检索增强微调（RAFT），在功能正确性和推理保真度上均实现了显著突破。其实验设计严谨，消融充分，为 LLM-assisted hardware design automation 建立了新的标杆。

</details>

---

### 13. [MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation](https://arxiv.org/abs/2606.04513)

**Authors**: Deguo Xia, Zihan Li, Haochen Zhao, Dong Xie, Yuyao Kong, Xiyan Liu, Jizhou Huang, Mengmeng Yang, Diange Yang  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04513v1  

#### Abstract
Lane-level maps are critical infrastructure for autonomous driving and lane-level navigation, yet constructing and maintaining standardized lane networks for hundreds of cities remains highly labor-intensive. Recent end-to-end vectorized mapping methods can predict lane geometry and topology directl...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

- **问题背景**：高精地图（HD Map）中的 **lane-level map** 是自动驾驶和车道级导航的关键基础设施，但其构建和维护高度依赖人工标注，成本高昂。
- **现有方法局限**：
  - 当前主流的端到端向量化建图方法（如 HDMapNet、VectorMapNet、MapTR 等）虽然能从传感器数据直接预测车道几何与拓扑，但它们将地图规范（mapping specifications）和交通规则作为隐式的、数据集相关的监督信号。
  - 在复杂场景下（如标线磨损、遮挡、光照变化），仅靠视觉证据无法唯一确定正确车道配置，导致模型输出常违反规范，仍需大量人工后编辑（post-editing）。

> 因此，**如何实现“规范合规”且“可规模化”的车道级地图自动化生产**，是工业界尚未解决的核心挑战。

---

### 🚀 提出的新方法与新思路

提出 **MapAgent** —— 一种工业级的 **agentic refinement 框架**，用于城市尺度的 lane-level 地图生成与更新。

#### 核心思想：从“一次性预测”转向“代理式迭代修正”

- 不再将 backbone 模型视为最终输出者，而是将其作为 **draft generator（草稿生成器）**。
- 引入一个 **显式的、基于验证驱动的 Judge-Planner-Worker 代理循环**，对 backbone 输出进行选择性、可控的修正。

#### 框架组成

| 组件 | 功能 |
|------|------|
| **Quality Agent** | 基于 backbone 置信度进行早期筛选，高置信度 tile 直接通过，低置信度进入 refinement loop |
| **Judge Agent**（VLM-based） | 视觉语言模型，联合检查 BEV 图像与草图，诊断错误类型（extra lane, category error 等），输出结构化报告 |
| **Planner Agent** | 工具调用模块，将诊断结果转化为最小化的、工具支持的编辑计划（JSON 格式动作序列） |
| **Worker Agent** | 执行确定性编辑操作（删除、类别修改、平滑、局部重建等），所有操作受可行性门控 Ω 验证 |

> ✅ **创新范式**：`Refinement-on-top-of-backbone`，在冻结 backbone 的前提下，通过轻量级 agent 层提升规范一致性。

---

### 🔍 相比现有方法的优势

| 优势维度 | 具体体现 |
|--------|---------|
| **规范合规性** | 显式引入 mapping specifications 和 traffic regulations 作为硬约束，确保输出符合工业标准 |
| **可解释性与可控性** | 错误诊断、推理过程、编辑动作均结构化，便于调试与审计 |
| **工程实用性** | 仅对困难 tile 触发 refinement，保持整体吞吐量；延迟可控（平均 420ms/tile） |
| **通用性** | 可作为插件式模块应用于不同 backbone（如 GeMap、DuMapNet）之上 |
| **自动化率提升显著** | 在百度地图落地后，全国 360+ 城市的 lane-level map 生产自动化率提升至 **>95%** |

---

## 2. 核心实验方法和设置

### 📚 数据集

- 基于 **Baidu Map Database** 构建的大规模 lane-level 向量地图数据集（DuLD 协议）。
- 包含高质量离线 BEV 图像（由多轨迹相机-LiDAR 融合信号聚合生成）和对应矢量化真值。
- 划分：
  - **训练集**：3,712 张 BEV 图像，59,434 条 lane 实例
  - **测试集**：656 张图像，10,254 条 lane 实例
- 特别构建了一个 **hard subset**，用于评估复杂长尾场景下的表现（如高复杂路口、遮挡、模糊标线）

---

### ⚙️ 实验设置

| 设置项 | 描述 |
|-------|------|
| **Backbone 模型** | 冻结状态下的 `GeMap` 和 `DuMapNet`（均为工业级 BEV 向量化系统） |
| **MapAgent 应用方式** | 作为 post-hoc refinement 模块，不参与 backbone 重训练 |
| **Judge Agent 模型** | 基于 Qwen3-VL-8B-Thinking，经 SFT + GRPO 微调 |
| **最大修正轮次** | $ T = 3 $（bounded budget） |
| **触发机制** | 仅当 backbone 置信度 < 0.7 时启动 refinement（约 30% tile 被处理） |

---

### 📊 评估指标

| 指标 | 定义 |
|------|------|
| **Accuracy** | 完全正确的 lane 比例（匹配 + 类别正确） |
| **Precision / Recall / F1-score** | 基于 lane 级匹配计算，FP 为多余预测，FN 为漏检 |
| **BBox IoU / Mask IoU** | 几何重叠度量 |
| **Cls Acc** | 分类准确率（仅在匹配对上计算） |
| **Runtime** | 单 tile 推理延迟（含 I/O） |
| **Automation Rate** | 无需人工干预完成的 lane 里程占比（实际部署指标） |

---

### 🆚 基线方法对比

| 基线 | 描述 |
|------|------|
| **Base Predictor (w/o MapAgent)** | 仅使用 backbone 输出（GeMap 或 DuMapNet） |
| **w/o Reason** | Judge 仅输出 error type，无结构化推理链 |
| **T=1 / T=2 / T=3** | 控制最大修正轮数，研究迭代收益 |
| **不同 VLM Judge 对比** | 如 InternVL-3.5-8B vs Qwen3-VL-Instruct vs Qwen3-VL-Thinking |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（来自 Table 3）

| Backbone | Method | Accuracy | F1-score | Cls Acc |
|----------|--------|----------|----------|---------|
| GeMap | Original | 52.8% | 69.1% | 91.9% |
| GeMap | + MapAgent (Qwen3-VL-Thinking) | **61.3%** | **76.0%** | **98.1%** |
| DuMapNet | Original | 52.2% | 68.6% | 88.0% |
| DuMapNet | + MapAgent (Qwen3-VL-Thinking) | **63.9%** | **78.0%** | **97.8%** |

> ✅ **一致增益**：MapAgent 在两个不同 backbone 上均带来显著提升，尤其在 **Accuracy 和 Cls Acc** 上改善明显。

---

### 🔬 消融实验结果（Table 2）

| Variant | Accuracy | F1-score | Cls Acc |
|--------|----------|----------|---------|
| Base Predictor | 52.5% | 68.9% | 90.0% |
| w/o Reason | 58.4% | 73.7% | 94.8% |
| T=1 | 58.3% | 73.6% | 94.5% |
| T=2 | 60.3% | 75.2% | 97.5% |
| T=3 | **62.6%** | **77.0%** | **98.0%** |

#### 发现：

- **结构化推理至关重要**：相比仅输出 error type，“Reason + Evidence”使 F1 提升超 3.3%，说明推理链提升了 Planner 的可执行性。
- **迭代有收益但边际递减**：从 T=1 到 T=3，F1 提升约 3.4%，表明多数错误可在 1–2 轮内修复。
- **几何指标稳定**：BBox/Mask IoU 变化极小（<1%），说明 MapAgent 更关注 **语义与拓扑正确性**，而非剧烈变形几何。

---

### 🧠 Judge Agent 自身性能（Table 1）

| Judge Model | Accuracy | No Error P/R | Extra Lane P/R | Category P/R | Geometry P/R | Structure P/R |
|------------|----------|---------------|------------------|----------------|----------------|----------------|
| Qwen3-VL-8B-Thinking (SFT) | 83.55% | 84.39/92.99 | 91.67/81.48 | 88.04/72.97 | 81.25/79.59 | 70.43/88.04 |
| + GRPO | **86.01%** | **92.31/94.90** | **96.15/85.80** | **93.33/81.08** | **87.10/82.65** | 66.67/82.61 |

> ✅ GRPO 进一步对齐下游目标，提升整体判断准确性，尤其是常见错误类型。

---

### ⏱️ 运行效率

- **平均延迟**：420 ms / tile（p95: 920 ms, p99: 1.6 s）
- **Judge Agent**：~230 ms / tile
- **Worker Agent**：~140 ms / tile
- **GPU 内存占用**：~19 GB / A800
- **触发比例**：约 30% 的 tile 需 refinement

> 💡 表明系统具备实时推理能力，适合大规模部署。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **代理式 refinement 范式有效可行**：
   - 将 VLM 与 deterministic tools 结合，可在不破坏 backbone 性能的前提下，显著提升地图规范一致性。
   - “Judge-Planner-Worker” 循环实现了 **可验证、可控制、可审计** 的编辑流程。

2. **结构化推理提升可执行性**：
   - Judge 的 chain-of-thought 推理不仅增强可解释性，更帮助 Planner 生成安全、合法的动作计划。

3. **工业落地效果显著**：
   - MapAgent 已集成至 **Baidu Maps**，支持全国 **360+ 城市** 的 lane-level map 生成与更新。
   - 整体生产自动化率提升至 **>95%**，大幅降低人力成本与更新周期。

4. **特别擅长处理长尾复杂场景**：
   - 在标线模糊、遮挡、拓扑歧义等情况下，backbone 易出错，而 MapAgent 能基于规范先验进行纠正。

---

### ⚠️ 方法的局限性

1. **无法处理极端视觉模糊场景**：
   - 当视觉证据极度缺失时（如完全无标线区域），当前框架倾向于保守处理，避免引入新 lane 或大范围拓扑修改。
   - 当前 Worker 不支持 **lane addition** 或 **non-local topology editing**。

2. **依赖高质量 backbone 初始化**：
   - 若初始预测严重偏离真实布局（如方向错误、位置漂移过大），refinement 可能难以恢复。

3. **工具集封闭**：
   - 所有操作必须通过预定义的 deterministic tools 执行，限制了灵活性。

4. **仍存在少量 bad cases**（见 Appendix D）：
   - 如严重阴影、局部遮挡导致的误删或保留错误片段。

---

### 🔮 未来工作方向

1. **引入不确定性建模与更强先验**：
   - 在极端模糊场景下，结合历史地图、SD map prior 或道路语义先验，辅助决策是否添加车道。

2. **构建统一的 agentic orchestration 框架**：
   - 自主调度多个 specialized backbone（如专用于路口、隧道、乡村道路），融合其预测并统一 refinement。

3. **扩展 Worker 工具集**：
   - 支持有限条件下的 lane insertion 与跨组拓扑调整，同时保证安全性。

4. **探索在线学习机制**：
   - 将人工编辑反馈闭环纳入训练，持续优化 Judge 与 Planner 策略。

---

## 总结

📌 **MapAgent 是首个成功将 agentic AI 范式应用于工业级高精地图生产的系统**，它通过 **“感知-验证-规划-执行”** 的闭环机制，在不牺牲效率的前提下，显著提升了 lane-level map 的规范性与自动化水平。其实验充分、设计严谨，并已在百度地图大规模落地，验证了其 **实用性、有效性与可扩展性**，为未来城市级自动驾驶基础设施建设提供了重要范式参考。

</details>

---

### 14. [MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models](https://arxiv.org/abs/2606.04627)

**Authors**: Zhichao Yang, Yuanze Hu, Haojie Hao, Longkun Hao, Dongshuo Huang, Hongyu Lin, Gen Li, Lanqing Hong, Yihang Lou, Yan Bai  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04627v1  

#### Abstract
Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains o...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前的 **mobile agent** 系统依赖于显式的 **Chain-of-Thought (CoT)** 推理，即通过生成冗长的文本思考过程（如观察、理由、预测）来指导动作决策。这种做法虽然提升了推理能力，但也带来了以下问题：
- **高推理延迟**：需要解码大量中间文本。
- **高上下文开销**：占用更多 context window。
- **高监督成本**：需要人工标注详细的推理轨迹。
- **部署效率低**：在移动设备等资源受限场景下难以高效运行。

### 提出了什么新方法或新思路
论文提出 **MIRAGE**（Mobile agents with Implicit Reasoning And Generative world modEls），其核心思想是将显式文本推理迁移到模型内部的**连续隐空间（latent space）**中进行，实现“隐式推理”（Implicit Reasoning）。具体创新包括：

#### （1）**Latent Chain-of-Thought with APLR**
- 将传统的文本形式的 `<THOUGHT>` 替换为一组可学习的 **continuous latent slots**。
- 引入 **Approximate Parallel Latent Refinement (APLR)**，一种并行化的隐状态优化机制，近似模拟串行的 latent CoT 推理过程。
  - 在训练时通过 $K$ 轮 Jacobi-style 并行更新 refine 所有 latent slots。
  - 理论证明：前 $K$ 个 latent slots 可以精确恢复串行推理的结果，尾部误差有界。

#### （2）**Generative World Model via Q-Former**
- 引入一个轻量级的 **Q-Former world-model head**，对齐 latent reasoning states 与下一帧截图的视觉特征。
- 鼓励 agent 在隐空间中“预测界面状态变化”，从而增强对未来环境动态的理解。
- 使用 stop-gradient 的 frozen vision encoder 提取目标特征，避免像素生成带来的计算负担。

#### （3）**Two-Stage Training Pipeline**
- **Stage 1**: 显式 CoT 微调（SFT），让模型学会结构化推理模式（observation → rationale → predict）。
- **Stage 2**: 隐式 CoT 迁移训练，用 latent slots 替代文本思考，并联合优化 action prediction 和 next-frame feature alignment。

### 相比现有方法的优势
| 维度 | MIRAGE | 传统显式 CoT 方法 |
|------|--------|------------------|
| 输出长度 | 极短（仅输出 action） | 长（含完整 thought 文本） |
| 推理延迟 | 显著降低（first-to-last token latency ↓） | 较高 |
| 部署效率 | 更适合移动端实时交互 | 成本高 |
| 性能 | 匹配甚至超越显式 CoT | 受限于 token 开销 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
1. **AndroidControl** [7]
   - 包含成对的高层指令与底层操作序列。
   - 支持细粒度评估：instruction-following EM 和 action accuracy。
2. **AndroidWorld** [8]
   - 动态、真实设备上的 benchmark。
   - 覆盖 20 个 Android 应用中的 116 个任务实例。
   - 评估端到端的任务完成率（task success rate, SR）。

此外还使用了：
- **AMEX dataset** [32]：提供 104K 高分辨率带标注截图。
- 自采探索轨迹（self-explored trajectories）扩展状态分布。

### 实验设置和评估指标

| 设置项 | 描述 |
|-------|------|
| **Backbone** | Qwen3-VL-4B-Instruct 和 Qwen3-VL-8B-Instruct |
| **Latent Slots** | 4B: 9 slots; 8B: 6 slots |
| **APLR Rounds $K$** | 默认 3 |
| **Loss Weight $\lambda$** | $ \mathcal{L} = \lambda \mathcal{L}_{ce} + (1-\lambda)\mathcal{L}_{wm}, \lambda=0.8 $ |
| **Inference** | 不生成任何 `<THOUGHT>` 文本，只输出 `<ACTION>` |

#### 评估指标
- **AndroidControl**:
  - Exact Match (EM)
  - Action Accuracy
  - Average Generated Tokens per Step
  - First-to-last-token Latency
- **AndroidWorld**:
  - Task Success Rate (SR)
  - Average Steps per Task
  - Average Tokens per Task

### 基线方法对比
- **通用模型**：GPT-4o
- **专用 GUI Agent**：
  - GUI-R1 / UI-R1
  - ShowUI, MAI-UI, UI-Venus-Navi, UI-TARS-7B-SFT, Ferret-UI Lite
- **同规模基线**：Qwen3-VL-4B/8B-Instruct（作为主要比较对象）

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ AndroidControl 结果（Table 1）
| Model | Low-Level EM | Action Acc. | Tokens/step |
|-------|--------------|-------------|------------|
| Qwen3-VL-4B-Instruct | 68.48 | 75.15 | 115.67 |
| **MIRAGE-4B** | **77.59 (+13.3%)** | **91.09 (+21.21%)** | **18.92 (↓83.6%)** |
| Qwen3-VL-8B-Instruct | 77.66 | 82.54 | 79.86 |
| **MIRAGE-8B** | **83.75 (+7.84%)** | **94.62 (+14.64%)** | **18.01 (↓77.5%)** |

> 💡 MIRAGE 在显著减少输出 token 的同时，大幅提升了 action grounding 准确性。

#### ✅ AndroidWorld 结果（Table 2）
| Model | SR (%) | Avg. Tokens/task |
|-------|--------|------------------|
| Qwen3-VL-4B-Instruct | 42.9 | 103.0 |
| **MIRAGE-4B** | **52.6 (+22.6%)** | **31.0 (↓69.9%)** |
| Qwen3-VL-8B-Instruct | 47.6 | 108.0 |
| **MIRAGE-8B** | **57.8 (+21.3%)** | **27.0 (↓75.0%)** |

> 💡 MIRAGE-8B 达到了当前最高的任务成功率，且生成 token 数仅为基线的约 1/4。

### 与其他方法对比
- MIRAGE-4B 在 AndroidWorld 上比 UI-TARS-7B-SFT（7B 参数）高出 **19.0 pp**。
- 推理延迟方面，MIRAGE-4B 的 first-to-last token latency 仅为 **1.7–1.8 秒**，远低于其他模型（普遍 >3 秒）。

### 消融实验结果（Ablation Study）

#### 表格：AndroidWorld 消融（Qwen3-VL-4B）
| Variant | Latent CoT | APLR | WM Head | SR (%) |
|--------|-----------|------|--------|--------|
| Base model | — | — | — | 42.9 |
| Action-only SFT | — | — | — | 31.0 |
| Explicit CoT SFT | × | × | × | 52.6 |
| MIRAGE-4B | √ | √ | √ | **52.6** |

> 🔍 发现：
- 移除思考但不引入 latent reasoning 会导致性能下降（31.0 vs 42.9）。
- **MIRAGE 完整版达到与显式 CoT 相当的性能（52.6）**，但推理更高效。
- 若无 world model 对齐，性能降至 48.2，说明其对补偿 APLR 尾部误差至关重要。

#### 其他敏感性分析
- **Latent slots 数量**：从 9 减至 3 导致 SR 从 52.6 降到 32.8，表明 sufficient latent capacity 是必要的。
- **APLR refinement passes**：从 2 增加到 3 使 MIRAGE-8B 的 SR 从 46.6 提升至 57.8，验证了多轮 refine 的有效性。
- **Loss balance $\lambda$**：设为 0.1（即强化 world model 权重）导致性能下降，说明 action CE 仍是主导目标。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **隐式推理可以匹配显式 CoT 的性能**：MIRAGE 在保留复杂多步推理能力的同时，完全省去了可见的文本思考过程。
2. ✅ **APLR 是高效的 latent refinement 机制**：通过少量并行迭代即可逼近串行推理效果，理论上有误差边界保证。
3. ✅ **World model 对齐提升泛化能力**：Q-Former 头部通过对齐 future screenshot features，增强了 agent 对 GUI 状态转移的建模能力，尤其缓解了 APLR 的尾部误差问题。
4. ✅ **显著提升部署效率**：相比基线，token 生成减少 **75–85%**，延迟降低 **2–3 倍**，更适合实际应用。

### 方法的局限性
- **依赖监督数据**：仍需高质量的显式 CoT 数据进行第一阶段 warm-up。
- **仅建模 feature-level world model**：未生成图像或语义草图，可能限制极端复杂场景下的规划能力。
- **next-frame supervision 限制**：只能预测单步后的界面变化，缺乏长期想象能力。
- **安全与隐私考虑不足**：尚未集成完善的 action safeguard 或 biometric handling 机制。

### 未来工作方向
- 扩展为 **multi-step latent imagination**，支持更长远的策略规划。
- 探索 **unsupervised latent reasoning discovery**，减少对人工标注推理链的依赖。
- 引入 **adaptive latent budget**，根据任务难度动态调整 slot 数量和 refine 次数。
- 结合 **reinforcement learning** 进一步优化决策质量。
- 加强 **real-world deployment safety mechanisms**，如自动 call_user 触发条件设计。

---

> 📌 **一句话总结**：  
> MIRAGE 成功将 mobile agent 的显式 Chain-of-Thought 推理压缩进隐空间，通过 **APLR + Q-Former world model** 实现高效、紧凑且强大的决策系统，在保持甚至超越 CoT 性能的同时，将输出 token 减少 3–5 倍，为移动端智能体的实际落地提供了新范式。

</details>

---

### 15. [LimiX-2M: Mitigating Low-Rank Collapse and Attention Bottlenecks in Tabular Foundation Models](https://arxiv.org/abs/2606.04485)

**Authors**: Yuanrui Wang, Xingxuan Zhang, Han Yu, Mingchao Ming, Gang Ren, Hao Yuan, Li Mao, Yunjia Zhang, Chun Yuan, Peng Cui  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2606.04485v1  

#### Abstract
Tabular foundation models (TFMs) increasingly rival tree ensembles, but their performance is often compute-inefficient: with standard affine scalar tokenization, each feature injects value variation through an essentially one-dimensional channel, and feature IDs/positional signals cannot increase wi...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：LimiX-2M: Mitigating Low-Rank Collapse and Attention Bottlenecks in Tabular Foundation Models

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题

该论文指出当前 **Tabular Foundation Models (TFMs)** 存在两个核心瓶颈：

- **Low-Rank Collapse（低秩坍缩）**：标准的线性标量嵌入（affine scalar tokenization）将每个数值特征映射到高维空间时，仅通过一个一维通道注入值变化，导致浅层表示的有效秩极低（甚至个位数），造成参数冗余和表达能力受限。
- **Attention Bottlenecks（注意力瓶颈）**：现有模型采用 `Feature-Attention → Sample-Attention`（F→S）的顺序，导致：
  - 特征注意力在缺乏跨样本统计信息的情况下进行；
  - 最终预测只使用目标 token，使得部分注意力计算被忽略，训练信号弱。

### 提出了什么新方法或新思路

作者提出 **LimiX-2M**，一个 2M 参数的高效 TFM，其核心是两个创新组件构成的统一框架：

#### （1）**RaBEL：Radial-Basis Embedding Layer**

- 用紧凑的 **RBF（Radial Basis Function）特征** 替代传统的线性投影。
- 将每个标量 $x_{i,j}$ 扩展为多个局部响应（localized responses），提升输入多样性。
- 引入 **Exponent-Gated Mechanism**：
  - 分离数值的“量级”与“模式”，增强对异方差性和多尺度数据的鲁棒性。
  - 实现尺度等变性（scale-equivariance），提高泛化能力。

#### （2）**Reordered Bidirectional Attention Block：S→N→F**

- 将注意力模块顺序从 `F→S→N` 改为 `Sample-Attention → FFN → Feature-Attention`（S→N→F）。
- 优势：
  - **先聚合跨样本上下文**（如列统计、缺失模式），再进行特征混合；
  - 所有注意力计算都直接参与最终预测（通过 attention pooling），避免信号浪费。

### 相比现有方法的优势

- **更高的参数效率**：2M 参数的 LimiX-2M 超越了 7M 参数的 TabPFN-v2 和 27M 参数的 TabICL。
- **更强的表达能力**：通过 RaBEL 显著提升浅层表示的有效秩（effective rank），缓解低秩坍缩。
- **更合理的计算流**：S→N→F 结构确保所有注意力模块都能获得强训练信号并贡献于输出。
- **更低的训练与推理成本**：在 GPU 上推理速度比 TabPFN-v2 快约 2 倍，比 TabICL 快 >10 倍。

---

## 2. 核心实验方法和设置

### 使用的数据集

实验覆盖六大主流 tabular benchmark 套件，涵盖分类与回归任务：

| 类型 | 数据集 |
|------|--------|
| **Classification** | TALENT-CLS, OpenML-cc18, PFN-CLS, TabZilla, TabArena-CLS, BCCO-CLS |
| **Regression** | TALENT-REG, PFN-REG, TabArena-REG, CTR23, BCCO-REG |

共包含：
- **分类**：179 + 62 + 29 + 27 + 33 + 106 = **436 个数据集**
- **回归**：99 + 28 + 13 + 33 + 50 = **223 个数据集**

### 实验设置和评估指标

| 项目 | 设置 |
|------|------|
| **模型架构** | 12 层 Transformer，hidden dimension $d_{\text{model}}=96$，6 个 attention heads |
| **训练方式** | 在合成数据上预训练（基于 SCM/DAG 生成） |
| **评估协议** | 多轮随机种子平均，严格控制超参搜索空间（Optuna） |
| **分类指标** | AUC, Accuracy (Acc.), F1-score |
| **回归指标** | R², RMSE |
| **报告方式** | 报告各数据集上的平均排名（mean rank），越低越好 |

### 基线方法对比

- **Tree-based Methods**：XGBoost, LightGBM, CatBoost, RF
- **Deep Learning Methods**：FT-Transformer, TabNet, SAINT, NODE, ResNet, AutoInt 等
- **Foundation Models**：
  - TabPFN-v2 (7.24M)
  - TabICL (27.10M)
  - Mitra (75.67M)
  - LimiX-16M (16.52M)
- **Ensemble**：AutoGluon

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### （1）综合性能排名（Table 6）

| 模型 | 分类平均排名 | 回归平均排名 | 总体表现 |
|------|---------------|---------------|----------|
| **LimiX-2M (1.92M)** | **第二**（仅次于 LimiX-16M） | **第二** | 在绝大多数 benchmark 上稳居前二 |
| TabPFN-v2 (7.24M) | 第五 | 第四 | 被 LimiX-2M 全面超越 |
| TabICL (27.10M) | 第七 | 第六 | 参数更多但性能落后 |
| Mitra (75.67M) | 第八 | 第七 | 最大模型之一，仍不如 LimiX-2M |

> ✅ **LimiX-2M 是唯一进入 Top-2 的 <2M 参数模型**

#### （2）具体数据集表现（代表性）

| 数据集 | 指标 | LimiX-2M | TabPFN-v2 | 提升 |
|--------|------|-----------|------------|-------|
| **BCCO-CLS** | AUC | **0.858** | 0.843 | +1.5% |
| **BCCO-REG** | R² | **0.785** | 0.772 | +1.3% |
| **OpenML-cc18** | AUC | **0.935** | 0.929 | +0.6% |
| **TabZilla** | AUC | **0.938** | 0.929 | +0.9% |

> 🔺 在所有主要 benchmark 上均优于 TabPFN-v2 和 TabICL

#### （3）推理效率（Table 26）

| 模型 | CPU 推理时间 (ms) | GPU 推理时间 (ms) |
|------|---------------------|--------------------|
| TabPFN-v2 | 51,950 | 352.60 |
| TabICL | 22,162 | 1,749.61 |
| **LimiX-2M** | **17,257** | **171.40** |

> ⏱️ **GPU 推理速度快 2× TabPFN-v2，快 >10× TabICL**

### 与基线方法的对比结果

- **显著优于所有传统树模型和深度模型**（如 XGBoost, LightGBM, FT-Transformer）
- **超越更大规模的 foundation models**：
  - 参数仅为 TabPFN-v2 的 **26%**，性能却更高；
  - 参数仅为 TabICL 的 **7%**，性能全面领先。
- **接近 LimiX-16M 的性能**，但参数少 88%，推理快 2 倍以上。

### 消融实验结果

#### （1）模块消融（Figure 3）

| 配置 | TabArena AUC | TabZilla AUC |
|------|----------------|---------------|
| Baseline | 0.830 | 0.918 |
| +RaBEL | 0.839 | 0.927 |
| +RBA (S→N→F) | 0.840 | 0.929 |
| **LimiX-2M (全)** | **0.843** | **0.931** |

> ✅ RaBEL 和 RBA 各自带来显著增益，联合使用效果最佳。

#### （2）注意力结构对比（Figure 2）

- **FSN（原顺序）**：注意力集中在 self-attention，难以捕捉跨特征依赖。
- **SNF（新顺序）**：注意力更广泛地分配给相关特征，尤其对目标变量的直接原因（如 DAG 中父节点）赋予更高权重。

#### （3）RaBEL 超参分析（Appendix C.3）

- 最优配置：
  - token 维度：32
  - RBF kernels 数量：64
  - 初始化：**orthogonal** 效果最好（AUC 达 89.03%）
  - bandwidth：固定 $ \sigma=1.0 $ 表现最佳

---

## 4. 关键结论和发现

### 论文的主要发现

1. **低秩坍缩是当前 TFM 的根本瓶颈**：
   - 线性嵌入导致浅层表示有效秩极低（Rank@99% 有时 <10）；
   - 即使截断至 rank=20，TabPFN-v2 性能下降有限（见 Table 1），说明严重冗余。

2. **非线性嵌入至关重要**：
   - RaBEL 通过局部 RBF 扩展，显著提升浅层有效秩（Table 5）：
     - Rank@99% 提升 **81.98%**
     - 数值秩提升 **34.6%**

3. **注意力顺序影响巨大**：
   - S→N→F 结构让模型“先看分布，再学关系”，更符合直觉；
   - 所有注意力模块均可贡献于最终预测，训练更稳定。

4. **小模型也能打败大模型**：
   - **LimiX-2M 以 2M 参数实现 SOTA 级别性能**，证明架构设计比单纯堆参数更重要。

### 方法的局限性

- **依赖合成数据预训练**：与 TabPFN 系列一样，需要大量合成任务训练，可能引入领域偏移。
- **未探索更复杂的 basis 函数**：目前仅使用 RBF，未来可尝试 wavelet、polynomial 等混合基函数。
- **对极端稀疏或超高维数据适应性未知**：实验主要集中在中等规模表格数据。

### 未来工作方向

- 探索 **hybrid basis libraries**（混合基函数库）以更好建模周期性、趋势等模式。
- 加强 **self-supervised pretraining**，减少对合成数据的依赖。
- 将 LimiX-2M 扩展到 **更大规模、跨域分布迁移场景**。
- 探索 **scaling laws** 下的小模型高效训练范式。

---

> 📌 **一句话总结**：  
> **LimiX-2M 通过 RaBEL 和 S→N→F 架构革新，在仅 2M 参数下实现了超越 7–75M 参数模型的性能，揭示了“表达力设计”比“参数堆叠”更能突破 tabular foundation models 的瓶颈。**

</details>

---

### 16. [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557)

**Authors**: Momchil Hardalov, Gonzalo Iglesias, Adri\`a de Gispert  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.04557v1  

#### Abstract
Large Language Models can reason over long contexts, yet prefilling millions of tokens is wasteful as much of the content remains static across queries. Cartridges address this by distilling document collections into reusable key-value (KV) caches that eliminate prefilling while preserving accuracy....

---

### 17. [Pseudospectral Bounds for Transient Amplification in Coupled Gradient Descent](https://arxiv.org/abs/2606.04031)

**Authors**: Ahanaf Hasan Ariq  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.04031v1  

#### Abstract
Coupled gradient descent--where the update of one parameter block depends on another--underlies bilevel optimization, two-time-scale stochastic approximation, and adversarial training. When the coupled Jacobian is block-triangular, asymptotic stability is governed by the spectral radii of the diagon...

---

### 18. [RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training](https://arxiv.org/abs/2606.04272)

**Authors**: Rachit Bansal, Clara Mohri, Tian Qin, David Alvarez-Melis, Sham Kakade  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.04272v1  

#### Abstract
The standard LLM training pipeline applies reinforcement learning (RL) only after pre-training and supervised fine-tuning (SFT). We question this status quo by training a LLM from scratch and applying RL, SFT, and SFT followed by RL directly to intermediate pre-training checkpoints. We find that RL ...

---

### 19. [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929)

**Authors**: Jack Sanderson, Yihan Wang, Xiaoqian Lu, Gautam Kamath, Yiwei Lu  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2606.04929v1  

#### Abstract
LLM post-training proceeds through multiple stages, e.g., supervised fine-tuning (SFT) followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO), where each stage draws data from different, potentially untrusted sources. Existing literature assumes data po...

---

### 20. [DLLG: Dynamic Logit-Level Gating of LLM Experts](https://arxiv.org/abs/2606.04378)

**Authors**: Bingnan Li, Zhaoyang Zhang, Xiaoze Liu, Yantao Shen, Shuli Jiang, Shuo Yang, Wei Xia, Zhuowen Tu, Stefano Soatto  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.04378v1  

#### Abstract
Leveraging multiple specialized LLMs can combine complementary strengths, but existing approaches trade adaptability for stability: routing commits prematurely, heuristic ensembling depends on fragile proxies, and parameter merging introduces interference. We propose DLLG (Dynamic Logit-Level Gating...

---

### 21. [SAID: Accelerating Diffusion-Based Language Models via Scaffold-Aware Iterative Decoding](https://arxiv.org/abs/2606.04974)

**Authors**: Na Li, Chengda Wang, Mingju Gao, Hao Tang  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.04974v1  

#### Abstract
Diffusion large language models (DLLMs) enable non-autoregressive generation by iteratively denoising corrupted token sequences with bidirectional context. Despite their ability to update multiple positions in parallel, inference remains costly due to the many denoising steps required for high-quali...

---

### 22. [Federated Learning for Multi-Center Sepsis Early Prediction with Privacy-Preserving](https://arxiv.org/abs/2606.04338)

**Authors**: Xixi Tian, Di Wu, Xiang Liu, Yiziting Zhu, Yujie Li, Xin Shu, Bin Yi  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.04338v1  

#### Abstract
Privacy-sensitive and distributed characteristics of multi-center medical data bring severe obstacles to centralized modeling for accurate early prediction of sepsis. Federated learning (FL) has attracted growing attention as a promising framework for collaborative model development, as it allows mu...

---

### 23. [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](https://arxiv.org/abs/2606.04980)

**Authors**: Wanqi Yang, Yuexiao Ma, Alexander Conzelmann, Xiawu Zheng, Michael W. Mahoney, T. Konstantin Rusch, Shiwei Liu  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2606.04980v1  

#### Abstract
Mixture-of-Experts (MoE) architectures scale model capacity through sparse expert activation, but their deployment remains memory-bound because all expert weights must reside in memory. Mixed-precision quantization can substantially reduce this footprint by assigning different bit-widths to differen...

---

### 24. [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435)

**Authors**: Saroj Mishra  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.04435v1  

#### Abstract
Multi-step agentic retrieval-augmented generation (RAG) pipelines have demonstrated significant capability for complex reasoning tasks, yet remain vulnerable to a class of failure that existing hallucination detection mechanisms systematically miss: cascading hallucination, where errors introduced a...

---

### 25. [Multilingual Long-Form Speech Instruction Following: KIT's Submission to IWSLT 2026](https://arxiv.org/abs/2606.04730)

**Authors**: Enes Yavuz Ugan, Maike Z\"ufle, Yuka Ko, Supriti Sinhamahapatra, Fabian Retkowski, Seymanur Akti, Jan Niehues, Alexander Waibel  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.04730v1  

#### Abstract
With the advent of Large Language Models, single-task and token-based multi-task models have evolved into instruction-based systems that infer task and target language implicitly from natural language prompts. This trend is reflected in IWSLT's Instruction Following Track, which this year introduced...

---

### 26. [Latent Anchor-Driven Test Generation for Deep Neural Networks](https://arxiv.org/abs/2606.04310)

**Authors**: Bin Duan, Matthew B. Dwyer, Guowei Yang  
**Category**: cs.LG  
**Published**: 2026-06-04  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2606.04310v1  

#### Abstract
Deep Neural Networks (DNNs) are increasingly being deployed in security-critical and safety-sensitive applications, which makes rigorous testing essential to identify and mitigate model weaknesses. Existing DNN testing approaches explore either the input space or a learned latent space. While latent...

---

### 27. [Neetyabhas: A Framework for Uncertainty-Aware Public Policy Optimization in Rational Agent-Based Models](https://arxiv.org/abs/2606.04562)

**Authors**: Janani Venugopalan, Gaurav Deshkar, Rishabh Gaur, Harshal Hayatnagarkar, Jayanta Kshirsagar  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.04562v1  

#### Abstract
Purpose The WHO's COVID-19 non-pharmaceutical interventions (e.g., lockdowns, vaccinations) effectively curb transmission but impose heavy economic strains. Existing research often neglects individual behaviors and falsely assumes perfect infection tracking and flawless policy execution, failing to ...

---

### 28. [Plan First, Judge Later, Run Better: A DMAIC-Inspired Agentic System for Industrial Anomaly Detection](https://arxiv.org/abs/2606.04599)

**Authors**: Yongzi Yu, Ao Li, Le Wang, Ziyue Li, Fugee Tsung, Yuxuan Liang, Man Li  
**Category**: cs.AI  
**Published**: 2026-06-04  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.04599v1  

#### Abstract
Large language model (LLM) agents have shown promise in automating complex data-analysis workflows, but their reliable deployment remains challenging in high-stakes industrial scenarios. Industrial anomaly detection (IAD) is essential for manufacturing quality, safety, and efficiency, yet existing L...

---

### 29. [A Systematic Evaluation of Positional Bias in Multi-Video Summarization with MLLMs](https://arxiv.org/abs/2606.04596)

**Authors**: Huangchen Xu, Yuan Wu, Yi Chang  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.04596v1  

#### Abstract
Multimodal Large Language Models (MLLMs) are increasingly used for video understanding, yet their reliability under multi-video inputs remains poorly understood. We study positional bias in multi-video summarization, where the quality of a per-video summary can change with the video's input slot eve...

---

### 30. [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874)

**Authors**: Haoyu Sun, Wenxuan Wang, Mingyang Song, Jujie He, Weinan Zhang, Yang Liu, Yang Yang, Yu Cheng  
**Category**: cs.CL  
**Published**: 2026-06-04  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2606.04874v1  

#### Abstract
Planning is central to LLM agents: before acting, an agent must decompose goals, select tools, reason over constraints, and decide when a task is infeasible. Yet existing agent evaluations often report only end-to-end success, making it difficult to determine whether failures stem from planning or e...

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
