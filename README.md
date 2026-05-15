# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-15 08:30:25 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization](https://arxiv.org/abs/2605.14249)

**Authors**: Zhiye Song, Kyungmi Lee, Eun Kyung Lee, Xin Zhang, Tamar Eilam, Anantha P. Chandrakasan  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2605.14249v1  

#### Abstract
We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization. As LLMs scale, predicting and reducing their energy footprint has become critical for sustainability and datacenter operations, yet existing approaches either require production-level c...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
随着 **Large Language Models (LLMs)** 规模不断扩大，其在多 **GPU** 上的推理过程消耗大量能源，对数据中心的可持续性和运营效率构成挑战。然而，现有的能效建模方法存在以下不足：
- 需要实际部署和昂贵的 profiling（如逐个配置运行测试），成本高、周期长；
- 缺乏对 **multi-GPU communication**、**compute-communication overlap** 和 **Mixture-of-Experts (MoE)** 架构中负载不均衡的准确建模；
- 多数工具仅关注延迟（latency）而非能量（energy），且无法支持早期设计探索。

因此，开发者缺乏一个能够在**无需实现代码或访问 GPU** 的情况下，快速预测不同优化策略下能效表现的工具。

---

### **提出了什么新方法或新思路**
本文提出 **EnergyLens** —— 一种端到端的、面向多 GPU 场景的 **LLM 推理能效预测框架**，具备以下核心创新：

#### ✅ **1. 基于 einsum 的高层接口**
- 用户可通过简洁的 `einsum` 表达式描述 LLM 结构（如注意力、FFN 层）、融合策略（fusion）、并行方式（tensor parallelism, expert parallelism）以及计算-通信重叠（overlap）设置。
- 示例：`op("bsm,miKh->bsiKh", parallel="K", label="QKV Projection")`
- 支持在**未实现具体代码前**进行能效探索，极大降低探索门槛。

#### ✅ **2. 分布式能效建模栈（Distributed Energy Modeling Stack）**
- **Empirically-driven Communication Energy Model**：基于实测数据拟合通信内核（如 AllReduce, ReduceScatter）的能量消耗，考虑消息大小和 SM 分配的影响，避免传统带宽模型的误差。
- **Overlap-aware Aggregation**：首次系统建模 **Megatron-style compute-communication overlap** 对能量和延迟的影响，支持 `overlap_stage`, `overlap_SM` 参数调节。
- **Load-imbalance-aware MoE Modeling**：引入有效参数 $ T_{\text{avg}}, E_{\text{avg}} $ 和瓶颈参数 $ T_{\text{max}}, E_{\text{max}} $ 来分别估计能耗与延迟，准确捕捉 MoE 中专家路由不均的问题。

#### ✅ **3. 能量驱动的设计空间探索能力**
- 提供 **ETFT (Energy to First Token)** 和 **EPOT (Energy Per Output Token)** 等能量为中心的指标，支持与传统 TTFT / TPOT 联合分析。
- 可自动识别 **Pareto-optimal 配置**，帮助决策者权衡能效与延迟。

---

### **相比现有方法的优势**

| 方法 | 是否需执行 | 是否支持多 GPU | 是否支持通信建模 | 是否支持 overlap | 是否支持 MoE | 是否提供能量分解 |
|------|------------|------------------|--------------------|------------------|---------------|------------------|
| **Direct Measurement** | 是 | 是 | 是 | 是 | 是 | 是 |
| **TDP-based Estimation** | 否 | 否 | 否 | 否 | 否 | 否 |
| **LLMCO2 (Fu et al.)** | 否 | 否 | 否 | 否 | ❌ 不支持 fused/MoE | ⚠️ 无细粒度归因 |
| **EnergAIzer (Lee et al.)** | 否 | ❌ 单 GPU | ❌ | ❌ | ⚠️ 有限 | ✅ |
| **NeuSight / Li et al.** | 否 | ⚠️ 仅延迟 | ❌ | ❌ | ❌ | ❌ |
| **EnergyLens (本文)** | **否** | ✅ | ✅ | ✅ | ✅ | ✅ |

> ✅ **优势总结**：EnergyLens 是首个支持 **无需实现即可预测多 GPU + MoE + overlap 设置下的能效** 的框架，填补了从架构设计到部署之间的“能效感知”空白。

---

## **2. 核心实验方法和设置**

### **使用的模型与硬件平台**
- **模型**：
  - **Llama3-8B**, **Llama3-70B**（dense）
  - **Qwen3-30B-A3B**（MoE，含 3B 激活参数，A3B 表示每 token 激活 3 个专家）
- **硬件**：
  - 8× **A100-SXM4-80GB** GPUs（用于 TensorRT-LLM 测量）
  - 使用 **NVML** 获取真实 GPU 能耗
  - 使用 **Torch Profiler** 验证通信操作和执行轨迹

---

### **实验设置**
- **评估场景覆盖**：
  - **Prefill Phase**：输入序列长度（ISL）从 256 到 8192，批量大小（batch size）从 1 到 64
  - **Decode Phase**：输出序列长度（OSL）最高至 7680，批大小 1~16
  - 并行配置：TP2/TP4/TP8；MoE 场景下 TP+EP2/EP4
  - Overlap 实验：4-stage overlap，分配 1/4/16 SM 给通信
- **Ground Truth**：
  - 使用 **TensorRT-LLM** 进行真实测量（prefill/decode）
  - Overlap 场景使用 **Megatron-LM v0.15.3** 验证

---

### **评估指标**
- **Mean Absolute Percentage Error (MAPE)**：用于衡量 EnergyLens 预测值与实测值之间的平均相对误差
  - 分别报告 **Energy** 和 **Latency** 的 MAPE
- **Pareto Frontier Recovery Rate**：比较 EnergyLens 预测的 Pareto 最优配置与真实测量结果的一致性
- **Energy Variation Across Configs**：展示不同配置间的最大节能潜力

---

### **基线方法对比**
- **TDP-based Estimation**：假设恒定功耗（如 400W），用延迟乘以 TDP 估算能量
- **LLMCO2**：当前最先进的 LLM 能耗预测器，但不支持 fused kernel 和 MoE
- **Naive Maximum-Overlap Heuristic**：默认启用最大 overlap（如 16 SM 用于通信），作为人工调优的代表

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（MAPE）**

| 模型 | 场景 | Energy MAPE | Latency MAPE |
|------|------|-------------|--------------|
| Llama3-8B | 单卡 | 11.31% | 11.30% |
| Llama3-70B | TP（无 overlap） | 12.18% | 12.39% |
| Llama3-70B | TP + Overlap | **12.97%** | 11.18% |
| Qwen3-30B-A3B | TP+EP | **9.25%** | 21.85% |
| Qwen3-30B-A3B | Decode | 13.19% | 27.16% |

> ✅ 所有场景下 **energy MAPE < 13.2%**，表明预测精度足够用于指导部署决策。

---

### **与基线方法的对比结果**

#### 🔹 **vs. TDP-based 方法**
- 在 decode 阶段，TDP 方法会**高估能耗高达 60%**（见图 9），因为 decode 功耗远低于 prefill。
- EnergyLens 正确捕获了 phase-dependent power 变化。

#### 🔹 **vs. Naive Maximum-Overlap Heuristic**
- 在 32 种场景中，**最大重叠启发式仅恢复 20% 的真实 Pareto 前沿**；
- 而 **EnergyLens 成功恢复 69% 的 Pareto 配置**，无需任何实测；
- 图 8 显示其预测的 Pareto 点全部落在真实前沿上。

#### 🔹 **vs. LLMCO2 / 其他 kernel 模型**
- LLMCO2 无法处理 fused kernel 或 MoE，必须重新训练；
- EnergAIzer 等单卡模型无法扩展到 multi-GPU 通信建模；
- EnergyLens 在保持模块化的同时整合多个 backend（如支持替换为 NeuSight 或 Li et al.）。

---

### **消融实验与关键发现**

#### ✅ **Kernel Fusion 影响评估（Appendix I）**
- 使用 EnergyLens 快速比较 fused vs. unfused 实现：
  - **Prefill 阶段平均节能 4.37%**
  - **Decode 阶段节能达 8.18%**
- 主要收益来自减少内存访问（如 QKV 合并投影）

#### ✅ **Overlap Tuning 敏感性分析**
- 发现并非 always “越多 overlap 越好”：
  - 在低 batch size 或短 ISL 下，过度分配 SM 给通信反而浪费计算资源；
  - 最佳 SM 分配高度依赖 workload 特征；
- EnergyLens 可自动识别最优 overlap 配置。

#### ✅ **MoE Load Imbalance 建模有效性**
- 图 2 显示：decode 时每个 expert 至少处理 16 tokens（tile granularity），导致小 batch 下严重 padding 和利用率低下；
- 使用 $ T_{\text{avg}}, E_{\text{avg}} $ 进行 energy 估计，$ T_{\text{max}}, E_{\text{max}} $ 估计 latency，显著提升准确性。

---

## **4. 关键结论和发现**

### **主要发现**
1. **配置间能效差异巨大**：
   - 在 prefill 和 decode 中观察到高达 **1.47× ~ 52.9× 的能量变化**；
   - 表明盲目选择配置可能导致数十倍能耗浪费。

2. **Disaggregated Serving 更具能效优势**：
   - **Prefill**：偏好 **小 batch + 低 TP**（减少通信开销）；
   - **Decode**：偏好 **大 batch**（提高算术强度）；
   - 两者目标冲突 → 强烈支持将 prefill 与 decode **分离部署**（disaggregated serving）。

3. **Compute-Communication Overlap 难以凭直觉优化**：
   - 最大 overlap 并非总是最优；
   - SM 分配需精细平衡，EnergyLens 可可靠识别 Pareto 最优解。

4. **通信能耗不可忽视**：
   - 在 Llama3-70B + TP8 场景中，**AllReduce 占总能耗 23%**；
   - 忽略通信建模会导致严重误判。

5. **EnergyLens 预测误差远小于配置差异**：
   - 尽管 decode latency MAPE 较高（~25%），但 energy MAPE 始终 <13.2%，足以用于识别高效配置。

---

### **方法的局限性**
- **Decode 阶段 latency 预测误差较高**（MAPE >25%）：
  - 因 decode 中 GEMM 形状极度 skew（如 $ M=1 $），kernel-level 模型普遍不准；
  - 该问题是 backend-agnostic（在 EnergAIzer, NeuSight, Li et al. 上均存在）；
- **依赖高质量 kernel-level backend**：
  - 当前使用 EnergAIzer 作为默认 compute backend；
  - 若底层模型不准（如对 custom kernel 如 TensorRT-LLM 的 dispatch 行为建模不足），会影响最终精度；
- **未建模 CPU / 内存 / NVLink 外部因素**；
- **MoE 路由统计若未知，则假设均匀分布，可能影响精度**。

---

### **未来工作方向**
- 扩展支持更多并行范式：**Pipeline Parallelism**, **Context Parallelism (CP)**（已在 Appendix F 初步验证 CP 支持）；
- 集成更精确的 decode kernel 模型，尤其是针对 small-batch GEMM；
- 支持异构 GPU 和 disaggregated infrastructure（如 GPU + Memory Node）；
- 开发自动化搜索算法，结合 EnergyLens 进行 multi-objective optimization（energy, latency, cost）；
- 推出开源版本，促进社区共建能效建模生态。

---

> 📌 **总结一句话**：  
> **EnergyLens 填补了 LLM 推理能效建模的关键空白——它让开发者能在“写一行代码之前”，就看清哪条路最省电。**

</details>

---

### 2. [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051)

**Authors**: Linghao Kong, Megan Flynn, Michael Peng, Nir Shavit, Mark Kurtz, Alexandre Marques  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2605.15051v1  

#### Abstract
Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel. While prior work demonstrates substantial speedups in isolated or fixed-batch settings, the behavior of SD in p...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：An Interpretable Latency Model for Speculative Decoding in LLM Serving

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前大多数关于 **Speculative Decoding (SD)** 的研究集中在理想化环境（如单请求、固定 batch size）下进行评估，忽略了真实生产环境中 **动态负载变化** 和 **连续批处理（continuous batching）** 对性能的影响。这导致在实际部署中，SD 的加速效果往往不如预期，甚至可能变慢。

本文旨在解决以下关键问题：
- 在真实的 LLM serving 系统中，如何建模 SD 的端到端延迟？
- 为什么 SD 的加速比（speedup）会随着服务器负载增加而下降？
- 如何为不同模型组合、序列长度和负载条件选择最优的 SD 配置？

---

### 🚀 提出的新方法与创新思路

作者提出了一种**可解释的延迟模型（interpretable latency model）**，用于描述在现代 LLM serving 系统中 SD 的行为，其核心思想包括：

#### （1）基于 Little's Law 推断有效 batch size
由于 vLLM 等系统采用 continuous batching，**batch size 不是可控参数，而是由请求速率和延迟共同决定的动态变量**。  
通过应用 **Little's Law**:  
> $ B = \text{RPS} \times L $  
其中 $B$ 是并发请求数（即有效 batch），RPS 是请求率，$L$ 是平均延迟。

该方法无需显式控制 batch size，即可从观测数据中推导出系统的负载状态。

#### （2）将延迟分解为 load-independent 与 load-dependent 成本
提出一个简洁的闭式表达式来建模非投机解码下的延迟：
> $ L = \frac{C_1}{1 - \text{RPS} \times C_2} $

- $C_1$: 负载无关成本（prefill 固定开销）
- $C_2$: 每个请求带来的负载相关增量成本（decode 阶段随并发增长的成本）

这一形式捕捉了从同步执行到接近饱和之间的“稳定前饱和”（pre-saturation）区间的延迟趋势。

#### （3）扩展至 SD 场景的成本分解模型
进一步将 SD 的延迟拆解为三个阶段的成本：
- **Prefill**（$c_{1,p}, c_{2,p}$）
- **Verification**（$c_{1,v}, c_{2,v}$）
- **Drafting**（$c_{1,d}, c_{2,d}$）

结合接受概率 $\alpha$ 和 draft length $k$，构建了一个统一的 speculation-aware 模型：
> $$
L = \frac{
C_{1,p} + \frac{1}{\alpha}(c_{1,v} + k \cdot c_{1,d})
}{
1 - \text{RPS} \cdot \left( C_{2,p} + \frac{1}{\alpha}(c_{2,v} + k \cdot c_{2,d}) \right)
}
$$

该模型明确揭示了 SD 参数如何影响固定成本和负载敏感成本。

#### （4）推广至 Mixture-of-Experts (MoE) 架构
引入 **expert coverage factor** $\theta$ 来建模稀疏专家激活对延迟的影响：
> $ \theta = 1 - (1 - m/M)^T $，其中 $T$ 是 routed token 数量

在低负载时，只有少量专家被激活，计算更高效；高负载时趋于密集模式。该修正显著提升了 MoE 模型的预测精度。

---

### 🔍 相比现有方法的优势

| 维度 | 传统方法 | 本文方法 |
|------|--------|---------|
| **适用场景** | 单请求 / 固定 batch 测试 | 真实动态负载下的连续服务 |
| **可解释性** | 黑箱测量或系统调优 | 明确分离 $C_1$, $C_2$, $\alpha$, $k$ 影响 |
| **泛化能力** | 特定配置优化 | 支持跨 verifier/drafter size、sequence length 外推 |
| **硬件鲁棒性** | 依赖特定 GPU | 在 A100 和 H100 上均有效 |
| **架构兼容性** | 主要针对 dense 模型 | 扩展支持 MoE 模型 |

> ✅ **优势总结**：提供了一个轻量级、可解释、可迁移的建模范式，可用于指导 SD 在真实系统中的配置优化。

---

## 2. 核心实验方法和设置

### 🧪 实验平台与工具链
- **Serving Engine**: `vLLM` (version 0.13.0)，启用 PagedAttention
- **Load Driver**: `GuideLLM` (version 0.5.2)，生成可控 RPS 请求流
- **Hardware**:
  - 多数模型运行于 **单张 NVIDIA A100 SXM**
  - Llama-3.1-70B 使用 4×A100，Qwen3-235B-A22B 使用 8×A100
  - 验证 H100 兼容性时使用 NVIDIA H100

---

### 📊 数据集与输入模拟
- **文本来源**：简·奥斯汀小说 *Pride and Prejudice* 中提取 token 序列
- **Prefill & Decode Lengths**：遍历 {256, 512, 768, 1024} tokens，共 16 种组合
- **SD 参数空间**：
  - Draft length $k$: 1–10 tokens
  - Acceptance rate $\alpha$: 50%–100%，通过覆盖 rejection sampling 强制设定

---

### ⚙️ 模型范围与 SD 类型
| 模型类型 | 模型列表 |
|--------|--------|
| Dense Models | Llama-3.1-8B, Llama-3.1-70B, Qwen3-0.6B～32B, gpt-oss-20b |
| MoE Models | Qwen3-30B-A3B, Qwen3-235B-A22B |
| Drafter 类型 | EAGLE-3（默认）、独立小模型（vanilla SD，如 8B draft 70B） |

> 注：主要分析基于 EAGLE-3 风格的 SD，因其效率更高且 vLLM 支持稳定。

---

### 📈 评估指标
- **主要指标**：
  - End-to-end request latency（均值、p95、p99）
  - Goodness-of-fit: $R^2$ 拟合优度
- **派生指标**：
  - Speedup = $L_{\text{autoregressive}} / L_{\text{SD}}$
  - Effective batch size $B = \text{RPS} \times L$
- **拟合方式**：使用 SciPy 的 `curve_fit` 进行非线性回归

---

### 🔁 实验流程
1. **基准测量**：同步发送请求，获取 base latency
2. **吞吐压测**：多并发请求确定最大稳定 RPS
3. **线性扫频**：在 sync 到 max RPS 间取 8 个均匀间隔的 RPS 点进行测试
4. **排除不稳定区域**：丢弃接近 preemption 的最后一点，聚焦“稳定前饱和”区间

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据与拟合效果

#### （1）延迟模型拟合准确度极高
- 在多种模型、配置下，提出的闭式模型（eq. 1）对非 SD 场景的延迟拟合 $R^2 > 0.96$
- 图1显示多个模型的归一化延迟曲线完美坍缩到理论曲线 $y = 1/(1 - x)$

| 模型 | $R^2$ |
|-----|-------|
| Llama-3.1-8B | 1.00 |
| Qwen3-32B | 1.00 |
| gpt-oss-20b | 0.96 |
| Qwen3-235B-A22B | 0.96 |

> 表明模型具有强泛化性和跨架构一致性。

#### （2）SD 场景下仍保持良好拟合
- 对每个 $(\alpha, k)$ 配置单独拟合，也能坍缩到相同曲线（图2a）
- 引入 speculation-aware 分解后，所有配置可通过统一参数 $C_{1,\text{EFF}}, C_{2,\text{EFF}}$ 描述（图4c）

#### （3）MoE-aware 修正大幅提升低负载预测精度
| 模型 | 原始 $R^2$ → 修正后 $R^2$（低 RPS 区域） |
|------|-------------------------------|
| gpt-oss-20b | 0.902 → 0.997 |
| Qwen3-30B-A3B | 0.830 → 0.976 |
| Qwen3-235B-A22B | 0.906 → 0.989 |

> 说明稀疏专家激活效应必须被显式建模。

#### （4）尾部延迟（p95/p99）也符合模型结构
- 尽管模型假设稳态，但在 p95 层面仍有较好拟合（$R^2 \approx 0.85–0.95$）
- 大模型上 p99 也表现良好（如 Qwen3-32B 达 0.989）

---

### 🔁 与基线方法对比

| 方法 | 是否考虑动态 batch | 是否可解释 | 是否支持 MoE | 是否适用于真实负载 |
|------|------------------|------------|--------------|--------------------|
| Liu et al. [2024] (Goodput Optimization) | ✅ | ❌（黑箱优化） | ❌ | ✅ |
| Vanilla SD evaluation (batch=1) | ❌ | ❌ | ❌ | ❌ |
| Roofline-style models | ❌ | ✅ | ❌ | ❌ |
| **本文模型** | ✅ | ✅ | ✅ | ✅ |

> 本文首次实现了在真实 serving 动态下对 SD 的**可解释建模**。

---

### 🔍 消融实验与关键发现

#### （1）$C_{1,R} < 1$ 但 $C_{2,R} > 1$：解释 speedup 随负载下降的根本原因
- $C_{1,R} = C_{1,\text{SD}} / C_{1,D} < 1$：SD 减少了固定成本（如权重加载摊销）
- $C_{2,R} = C_{2,\text{SD}} / C_{2,D} > 1$（多数情况下）：SD 增加了每请求的负载敏感成本

> 导致公式中 speedup 随 RPS 增大而减小：
> $$
\text{Speedup} = \frac{1}{C_{1,R}} \cdot \left(1 + (1 - C_{2,R}) \cdot \frac{\text{RPS} \cdot C_{2,D}}{1 - \text{RPS} \cdot C_{2,D}}\right)
$$

#### （2）Draft length 存在权衡
- 最小化 $C_{1,R}$ 的最佳 $k$ 较大（利于低负载）
- 最小化 $C_{2,R}$ 的最佳 $k$ 较小（利于高负载）

> 结论：**为 batch=1 设计的最佳 $k$ 并不适合高吞吐场景**

#### （3）Acceptance rate 决定是否能实现“负载增益”
- 当 $\alpha > 90\%$ 时，可能出现 $C_{2,R} < 1$，此时 speedup 随负载上升而增强
- 否则 $C_{2,R} > 1$，speedup 必然随负载衰减

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **SD 的加速收益通常在低负载时最大，在高负载时减弱甚至消失**  
   → 原因是 SD 降低了 $C_1$（固定成本），但增加了 $C_2$（负载敏感成本）

2. **Batch size 不应作为独立变量看待，而应通过 Little’s Law 从 RPS 和 L 反推**

3. **可以通过简单的成本分解模型精确预测 SD 的延迟行为**  
   → 模型参数具备良好的跨模型、跨长度、跨硬件可迁移性

4. **MoE 模型在低负载下延迟低于 dense 模型预测值，源于稀疏专家激活**

5. **draft length 的优化需权衡低负载 vs 高负载性能，不存在全局最优**

6. **该框架可用于在线决策**：实时估计当前 $\alpha$ 和 RPS，预测各 $k$ 下的延迟，动态选择最优配置

---

### ⚠️ 方法的局限性

| 局限性 | 说明 |
|--------|------|
| 仅适用于 pre-saturation 区间 | 排除了 preemption 和极端拥塞情况 |
| 假设稳态与平均行为 | 未建模 bursty workloads 或 request correlation |
| 参数依赖实测拟合 | $C_1, C_2$ 等为系统级 effective 参数，不可直接移植 |
| 假设 constant $\alpha$ | 实际中 acceptance rate 可能随位置或上下文变化 |
| 忽略调度细节 | 抽象了 vLLM 内部调度机制，不适用于极端边缘情况 |

---

### 🔮 未来工作方向

1. **扩展至分布式的 latency modeling**（如 DistServe 架构）
2. **建模 bursty workloads 与 request arrival patterns**
3. **纳入 adaptive drafting、tree verification 等复杂 SD 变体**
4. **发展为自动化 tuning system**：结合 feedback loop 实现 runtime 自适应配置
5. **联合建模 energy efficiency 与 carbon footprint**
6. **探索更精细的 tail latency modeling**（如 queueing network 模型）

---

## 总结

本文提出了首个面向真实 LLM serving 场景的 **可解释 speculative decoding 延迟模型**。它利用 **Little's Law** 和 **cost decomposition** 思想，成功揭示了 SD 在不同负载下的性能演化规律，解释了“为何 speedup 随负载下降”这一普遍现象，并提供了指导实际部署的量化工具。该模型不仅适用于 dense 模型，还可扩展至 MoE 架构，展现了强大的通用性和实用性，为未来智能推理系统的设计与优化奠定了理论基础。

</details>

---

### 3. [BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE](https://arxiv.org/abs/2605.14438)

**Authors**: Juntong Wu, Jialiang Cheng, Qishen Yin, Yue Dai, Yuliang Yan, Fuyu Lv, Ou Dan, Li Yuan  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2605.14438v1  

#### Abstract
Mixture-of-Experts (MoE) architectures enhance the efficiency of large language models by activating only a subset of experts per token. However, standard MoE employs a fixed Top-K routing strategy, leading to redundant computation and suboptimal inference latency. Existing acceleration methods eith...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现有的 **Mixture-of-Experts (MoE)** 模型普遍采用固定的 **Top-K 路由机制**，即每个 token 固定激活 K 个专家。这种策略忽略了不同 token 的语义复杂度差异，导致简单 token 也消耗大量计算资源，造成冗余计算和推理延迟，限制了 MoE 模型的效率潜力。

此外，现有动态路由方法存在以下问题：
- **基于路由 logits 修改的方法**（如 MoE-Dynamic）无法主动跳过高权重但冗余的专家，且有最小激活数量限制。
- **引入特殊专家的方法**（如 AdaMoE 引入 null experts）需要额外超参数和微调，控制不直接。
- **静态合并或剪枝专家的方法** 无法在推理时适应输入变化，高压缩率下性能下降严重。

### 提出了什么新方法或新思路
本文提出 **BEAM (Binary Expert Activation Masking)**，一种新颖的动态路由框架，通过可学习的二值掩码实现细粒度、token 自适应的专家稀疏化。

其核心思想是**解耦专家选择与稀疏化控制**：
- **主路由器 (Primary Router)** 仍负责标准的 Top-K 专家选择和负载均衡。
- **掩码路由器 (Mask Router)** 是一个轻量级、可训练的模块，为每个 token 生成一个二值掩码，作用于 Top-K 候选专家集合上，决定是否真正激活该专家。

具体流程如下：
1. 主路由器选出 Top-K 专家。
2. 掩码路由器生成原始掩码 $ m = \sigma(xW_m) $。
3. 通过固定阈值（如 0.5）将原始掩码二值化 $ \hat{m} \in \{0,1\}^N $。
4. 最终路由权重为 $ g' = g \odot \hat{m} $，实现选择性去激活。

### 相比现有方法的优势
- **直接且主动的稀疏化**：直接对专家进行二值化掩码，能主动跳过冗余专家，而非依赖间接机制。
- **端到端可训练**：通过 **Straight-Through Estimator (STE)** 处理二值化操作的不可导问题，结合辅助的 L1 正则化损失 $ L_{reg} $，实现稀疏性和性能的联合优化。
- **解耦设计避免冲突**：分离路由与稀疏化，主路由器保持原有功能，掩码路由器专注冗余消除，训练更稳定。
- **硬件友好与即插即用**：二值掩码信号便于硬件处理，作者实现了高效的自定义 CUDA 内核，并集成到 **vLLM** 框架中，仅需一行代码修改即可部署。

---

## 2. 核心实验方法和设置

### 使用了哪些模型和数据集
- **模型**：在三个代表性 MoE 模型上进行评估：
  - `Qwen1.5-MoE-A2.7B`
  - `DeepSeekV2-Lite`
  - `Qwen3-30B-A3B`
- **训练数据**：使用 **Tulu 3 SFT Mixture Dataset** 进行监督微调 (SFT)，覆盖推理、编程和常识任务。
- **评估基准**：从 **OpenCompass** 中选取 8 个基准，涵盖三大领域：
  - **推理 (Reasoning)**：MATH, GSM8K, HumanEval (H_Eval)
  - **知识 (Knowledge)**：MMLU, CEVAL, CMMLU
  - **常识 (CommonSense)**：BoolQ, CommonsenseQA (CSQA)

### 实验设置和评估指标
- **硬件环境**：单张 NVIDIA H20 GPU。
- **推理设置**：输入/输出长度固定为 128/32 tokens，测试样本 5000 个。
- **评估指标**：
  - **准确性**：各任务平均准确率 (Avg. Acc.)
  - **加速性能**：
    - Time per Output Token (TPOT)
    - Time to First Token (TTFT)
    - 吞吐量 (Throughput, samples/s)
  - **稀疏性**：平均每 token 激活专家数 (Avg. K)

### 基线方法对比
与五种主流方法对比：
1. **Top-K Reduced**：训练时减小 K。
2. **Top-K Pruning**：训练时用原 K，推理时减小 K。
3. **MoE-Dynamic**：按累积概率阈值激活专家。
4. **AdaMoE**：引入零计算的 null experts。
5. **DynMoE**：使用 sigmoid 门控替代 Top-K。

---

## 3. 主要实验结果和性能指标

### 关键性能数据
- **极高的稀疏性**：在 **极端稀疏** 设置下，BEAM 可将平均每 token 激活专家数降至 **0.11**（Qwen1.5, K=4）、**0.56**（Qwen3, K=8）、**0.48**（DeepSeek, K=6）。
- **优异的性能保留**：在中等稀疏度下，**保留超过 98% 的原始模型性能**；即使在极端稀疏下，仍能保留 **85% 以上** 的性能。
- **显著的加速效果**：
  - **MoE 层 FLOPs 减少高达 85%**。
  - **解码速度提升最高达 2.5×**。
  - **吞吐量提高 1.4×**。

### 与基线方法的对比结果
- **全面优于基线**：在相同稀疏水平下，BEAM 在所有模型和任务上的准确率均显著高于所有基线方法。
- **极端稀疏优势巨大**：
  - 在 Qwen3 上，BEAM (Avg.K=0.56) 比 Top-K Reduced (K=1) 高出 **33.29%** 平均准确率。
  - 在 DeepSeek 上，高出 **32.49%**。
- **稳定性好**：Top-K Pruning 在高压缩下性能急剧下降，而 BEAM 表现稳健。
- **优于动态方法**：MoE-Dynamic 和 AdaMoE 因设计缺陷（如位置偏置、null expert 干扰）导致性能下降明显。

### 消融实验结果
#### (1) 二值化阈值 $ T $ 消融（Table 4）
- 测试 $ T \in \{0.1, 0.3, 0.5, 0.7, 0.9\} $。
- **$ T=0.5 $ 效果最佳**，在稀疏性和性能间取得最好平衡，尤其在常识任务上表现突出。

#### (2) 训练策略消融（Table 5）
- **移除 $ L_{reg} $**：专家激活率大幅上升（Avg.K 从 1.23 升至 6.31），证明正则化对稀疏化的必要性。
- **L1 vs L2 正则化**：L1 在稀疏性和精度上均优于 L2。
- **STE 二值掩码 vs Soft 掩码**：
  - 直接使用 Sigmoid 软掩码（Soft）导致严重性能崩溃（77.14 → 23.56）。
  - 温度退火软掩码（Soft w/ Temp.）部分缓解但仍有 5% 下降。
  - 证明 **STE 是实现有效训练的关键**。

---

## 4. 关键结论和发现

### 主要发现
1. **计算分配高度依赖 token**：BEAM 学会为不同 token 分配不同数量的专家，语义丰富的词（名词、动词）激活更多专家，而模板词（如 "You are a helpful assistant"）几乎不激活任何专家。
2. **层间角色分化**：模型呈现“编码器-解码器”模式——浅层主要用于知识存储，深层用于推理和解码，BEAM 能据此调整层间稀疏性。
3. **决策基于相关性而非排名**：BEAM 会跳过高排名但冗余的专家，也会保留低排名但关键的专家（见 Appendix B.4 图 8），证明其决策基于 **token-expert 相关性**，而非简单的路由权重排序。
4. **负载均衡得以保持**：尽管进行了掩码，但专家利用率分布依然均匀（见 Appendix B.5 图 9），说明 BEAM 不破坏原有的负载均衡机制。

### 方法的局限性
1. **需要后训练微调**：BEAM 需要额外的 SFT 阶段来训练掩码路由器，增加了训练成本。
2. **共享专家限制加速上限**：对于含有大量共享专家的架构（如 Qwen1.5），MoE 层 FLOPs 最多只能减少 50%，因为共享专家无法被 BEAM 跳过。
3. **模型泛化性待验证**：目前仅在三种 MoE 架构上验证，其他设计（如不同门控机制）的有效性尚不明确。
4. **单 GPU 评估**：未测试在多 GPU 专家并行场景下的交互和扩展性。

### 未来工作方向
- 探索无需微调的 BEAM 变体（如冻结主路由器，仅训练掩码路由器）。
- 将 BEAM 扩展到多 GPU 专家并行系统，研究其通信效率。
- 结合 BEAM 与其他高效推理技术（如 speculative decoding, KV cache 优化）。
- 探索 BEAM 在非语言模型（如视觉 MoE）中的应用。

</details>

---

### 4. [Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection](https://arxiv.org/abs/2605.14062)

**Authors**: Anjir Ahmed Chowdhury, Syed Zawad, Feng Yan  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.14062v1  

#### Abstract
While synthetic data generation with large language models (LLMs) is widely used in post-training pipelines, existing approaches typically generate full outputs before applying quality filters, leading to substantial token waste on samples that are ultimately discarded. To address this, we propose M...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
大型语言模型（LLMs）在后训练阶段（如监督微调 SFT 和基于人类反馈的强化学习 RLHF）中广泛用于生成合成数据。然而，传统方法通常先**完整生成整个输出序列**，再进行质量过滤，导致大量 token 被浪费在最终会被丢弃的低质量样本上。

这种“生成后再过滤”的方式不仅计算成本高昂，还可能将错误推理路径引入训练数据，影响下游模型性能。

---

### **提出了什么新方法或新思路**
本文提出 **Multi-Stage In-Flight Rejection (MSIFR)**，一种轻量级、无需训练的框架，能够在生成过程中**分阶段实时检测并终止低质量生成轨迹**，从而避免不必要的 token 开销。

**核心思想**：
- 将生成过程分解为多个阶段（如问题生成、中间解、完整解等）；
- 在每个阶段后插入**轻量级规则验证器（rule-based validators）**，检查：
  - 数学不一致性（arithmetic inconsistency）
  - 幻觉模式（hallucination）
  - 格式违规（formatting violation）
- 若任一阶段失败，则立即中止该样本的生成，节省后续 token 消耗。

---

### **相比现有方法的优势**
| 对比维度 | 现有方法（如 LYNX, DEER, S-GRPO） | MSIFR |
|--------|-------------------------------|-------|
| **目标** | 减少冗余推理（overthinking），提前结束正确但冗长的推理链 | 主动拦截错误推理路径，在早期拒绝无效样本 |
| **机制** | 基于置信度或奖励信号决定是否 early exit | 基于规则的多阶段 in-flight rejection，动态终止故障轨迹 |
| **适用场景** | 单次推理任务（inference-time） | 大规模合成数据构建（dataset construction） |
| **是否需训练** | 部分需要 probe 或 reward model 训练 | 完全无需训练，纯规则驱动 |
| **效率增益来源** | 减少每条序列长度（tokens per sample） | 减少无效样本数量（samples with wasted tokens） |

✅ **关键优势**：MSIFR 与 early-exit 方法正交且可组合，能实现**复合效率提升**。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
在七个涵盖数学推理与科学知识的基准上进行评估：

| 数据集 | 类型 |
|------|-----|
| **GSM8K** | 小学级别数学应用题 |
| **MATH500** | 高难度数学问题子集（来自 MATH） |
| **SVAMP** | 含缺失量的算术文字题 |
| **MAWPS** | 数学单词问题仓库 |
| **MathQA** | 可解释性数学问答 |
| **MMLU-Chem** | 化学领域的 MMLU 子集 |
| **DeepMind Mathematics Dataset** | 综合数学能力测试集 |

---

### **实验设置和评估指标**

#### **模型**
五种开源指令调优 LLM：
- Qwen2.5-7B-Instruct
- Llama-3.1-8B-Instruct
- DeepSeek-7B-Chat
- Phi-3-mini-4k-instruct
- Mistral-7B-Instruct-v0.3

#### **评估流程**
- 使用 **Llama-3-13B-Instruct** 作为 judge model 进行自动评分（1–5 分）
- 接受阈值：得分 ≥ 3
- 人工评估子集（N=100）验证一致性
- 使用 MinHash 检测重复样本

#### **评估指标**
| 指标 | 含义 |
|------|------|
| **Total Token Consumption ↓** | 总生成 token 数量（越低越好） |
| **Eval Accuracy ↑** | 保留样本的平均正确率（越高越好） |
| **Throughput ↑** | 每小时处理的问题-解答对数 |
| **Token Savings %** | 相比传统全生成基线的 token 节省比例 |

#### **基线方法对比**
- **Traditional (Full Generation)**：无 early discard，完全生成后才过滤
- **DEER**：基于熵的 early exit 方法
- **LYNX**：基于 probing 的 early exit 方法
- **MSIFR + LYNX**：组合方法，验证兼容性

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### ✅ **独立 MSIFR 表现**
- **token 消耗减少 11% – 77%**（以 GSM8K 上 Llama-3.1-8B 为例，从 13.17M → 7.46M，↓42%）
- **准确率持平或提升**：多数情况下 Eval Accuracy 不降反升（最高 +8.6 pp）
- **吞吐量显著提高**：最高达 5× 加速（见组合实验）

> 示例：在 GSM8K 上，MSIFR 将 token 使用从 109.09M 降至 24.61M（**↓77.4%**），同时保持 accuracy 在 0.734（vs baseline 0.720）

#### ✅ **与 early-exit 方法组合表现（MSIFR + LYNX）**
| 方法 | Total Token | Throughput | Eval Accuracy |
|------|------------|-----------|--------------|
| Traditional | 109.09M | 3,291 | 0.720 |
| LYNX | 25.14M | 8,588 | 0.738 |
| **MSIFR** | **24.61M** | **15,823** | **0.734** |
| **MSIFR + LYNX** | **23.73M** | **16,605** | **0.735** |

- **总 token 减少 78.2%**
- **吞吐量提升 5.0×**
- **无精度损失**

👉 表明两种机制作用于不同成本轴（early exit 缩短有效序列，MSIFR 拦截无效序列），可叠加优化。

---

### **消融实验结果**

#### 🔍 **中段检查点位置选择（Mid-Solution Cutoff）**
- 测试 30% ~ 80% 生成进度作为第二阶段检查点
- 发现 **50% 是最优平衡点**：
  - 准确率峰值维持（0.57）
  - token 节省达 42%
  - FPR（误删好样本）仅 3.1%，FNR（漏检坏样本）7.4%

> 更早检查（如 30%）虽更安全但节省有限；更晚检查（>60%）虽省更多 token 但开始误删高质量样本。

#### 🧪 **假阳性与假阴性分析（False Positive/Negative Rate）**
| 指标 | 平均值 |
|------|--------|
| **FPR（误删好样本）** | **3.2%** |
| **FNR（漏检坏样本）** | **8.7%** |

- 表明 MSIFR 极少误伤优质样本
- 即使漏检的坏样本，也因后期被拦截而消耗更少 token

---

## **4. 关键结论和发现**

### **主要发现**
1. **任何非平凡的丢弃策略都能严格降低期望 token 消耗**  
   ➤ 只要有一定概率提前终止，就能节省资源（Proposition 3.1）。

2. **in-flight rejection 不会引入系统性偏差**  
   ➤ 条件效用估计构成一个鞅（martingale），确保保留样本的期望质量不变（Proposition 3.2）。

3. **越早拒绝，节省越多**  
   ➤ token 成本随阶段递增，早期拒绝带来超线性节约。

4. **MSIFR 与 early-exit 方法正交且互补**  
   ➤ 可无缝集成，实现高达 **78.2% token 节省 + 5× 吞吐提升**。

5. **准确率不降反升**  
   ➤ 因为提前淘汰了低置信路径，反而提升了保留数据的整体质量。

---

### **方法的局限性**
- **规则依赖性强**：validator 设计是任务特定的，需人工定义领域约束（如数学一致性、格式要求）
- **适应新任务需重新设计验证器**：不能直接迁移，但无需重新训练模型
- **未在 >8B 模型上验证**：当前实验集中在 7–8B 参数模型
- **长文本生成场景需调整阈值**：对于非常长的证明或代码生成，50% cutoff 可能需重新校准

---

### **未来工作方向**
- 自动化 validator 规则生成（例如通过 LLM 自动生成检测逻辑）
- 扩展至多模态合成数据生成（如图文对、代码+注释）
- 结合 learned reward model 实现 hybrid rejection 策略
- 在更大规模模型（如 70B+）上验证有效性
- 探索动态调整各阶段 rejection 阈值的 adaptive 策略

---

## ✅ **总结一句话**
> **MSIFR 提供了一种高效、无偏、无需训练的方法，在生成过程中“及时止损”，大幅降低 LLM 合成数据的成本，同时提升数据质量和系统吞吐量，是构建高质量训练数据集的重要工具。**

</details>

---

### 5. [Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing](https://arxiv.org/abs/2605.14978)

**Authors**: Jie Jiang, Xing Sun  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 11.5  
**Type**: new  
**ArXiv ID**: 2605.14978v1  

#### Abstract
Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model. In practice, speculative efficiency is often bottlenecked by hard-to-draft positions, where an early mismatch truncat...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在 **Speculative Decoding** 中，一个轻量级的 **drafter 模型** 预测多个候选 token（称为 speculative window），由更大的 **target 模型** 并行验证。然而，当前大多数 drafter 模型仍采用 **token-level 的监督学习目标**（如交叉熵）进行训练，这与推理阶段实际追求的 **window-level 效率目标** 不一致。

具体问题包括：
- 即使窗口中大部分 token 正确，**早期 token 的不匹配** 会导致整个窗口被截断，后续 token 全部作废。
- token-level 的训练目标无法直接优化 **accepted prefix length** 和 **end-to-end speedup**，导致训练与推理目标脱节。

### 提出了什么新方法或新思路
本文提出 **PPOW**（Performance-Driven Policy Optimization with Adaptive Windowing），一种基于强化学习的框架，将 drafter 训练从 token-level 仿效转向 **window-level 性能优化**。

#### 主要创新点：
1. **Window-Level RL Framework for Drafter Optimization**
   - 将每个 speculative window 视为一个整体训练单元，使用 **reinforcement learning** 进行优化，奖励信号基于该窗口的实际接受长度和效率。

2. **Performance-Driven Reward Design**
   - **Cost-Aware Speedup Reward**: 奖励与接受长度成正比，同时考虑 drafter 与 target 模型的相对计算成本，更真实反映推理效率。
   - **Distribution-Based Proximity Reward**: 当验证因早期不匹配而失败时，若 draft window 在 target 模型下的累积 log-likelihood 接近最优序列，仍给予部分奖励，提供更密集的反馈。

3. **Adaptive Divergence-Aware Windowing (ADAW)**
   - 动态选择训练窗口，优先采样那些 **confidence-weighted draft-target divergence 较大** 的窗口（即“难窗口”），聚焦于影响 acceptance 的瓶颈位置，提升训练效率。

### 相比现有方法的优势
- **对齐训练与推理目标**：直接优化 speculative decoding 的实际性能指标（如 speedup），而非间接优化 token 预测准确率。
- **更强的鲁棒性**：通过辅助奖励机制，在稀疏奖励场景下仍能有效学习。
- **更高的训练效率**：ADAW 聚焦于关键窗口，避免在已掌握的简单窗口上浪费资源。
- **通用性强**：兼容多种 drafter 架构（如 EAGLE 系列），可在统一解码协议下提升性能。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **MT-Bench**：多轮对话任务
- **HumanEval**：代码生成任务
- **GSM8K**：数学推理任务

此外还补充测试了：
- **X-SUM**：摘要任务
- **WMT14**：机器翻译任务
- **ShareGPT & UltraChat-200k**：用于 Qwen 模型的预训练数据

### 实验设置和评估指标

#### 模型家族
- **LLaMA-3**：8B 和 70B 的 target 模型
- **Qwen3**：8B 和 32B 的 target 模型  
- Drafter 基于 **EAGLE-3** 架构初始化

#### 评估指标
| 指标 | 含义 |
|------|------|
| **Average Acceptance Length (T)** | 每次 speculative verification 成功接受的平均 token 数 |
| **Speedup Ratio** | 相对于标准自回归解码的端到端加速比 |

#### 解码配置
- 温度：0.0 和 1.0
- Speculative window size $ K = 10 $
- 使用 **tree decoding** 和 **rejection sampling** 验证
- 相对计算成本 $ \gamma = 0.12 $

### 基线方法对比
- **EAGLE-3**：基于特征的 drafter，使用监督训练
- **GRIFFIN**：强调 token 对齐的先进 drafter
- **OSD**, **Lookahead**, **FastDraft**：其他 speculative decoding 方法（见附录）
- **Continued Supervised Training (CST)**：作为消融对照，检验是否仅靠更多监督训练即可达到相同效果

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 1）
| Model | Method | T (Mean) | Speedup (Mean) |
|-------|--------|----------|----------------|
| LLaMA-3.1-8B | EAGLE-3 | 6.09 | 3.41× |
| LLaMA-3.1-8B | **PPOW** | **6.40** | **3.46×** |
| LLaMA-3.3-70B | EAGLE-3 | 5.94 | 4.15× |
| LLaMA-3.3-70B | **PPOW** | **6.29** | **4.36×** |
| Qwen3-8B | EAGLE-3 | 6.16 | 3.17× |
| Qwen3-8B | **PPOW** | **6.52** | **3.39×** |
| Qwen3-32B | EAGLE-3 | 5.99 | 3.81× |
| Qwen3-32B | **PPOW** | **6.44** | **3.92×** |

> ✅ **PPOW 在所有模型和任务上均取得最佳性能**，平均 acceptance length 达到 **6.29–6.52**，speedup 达到 **3.39–4.36×**

### 与基线方法的对比结果
- 在 **HumanEval** 和 **GSM8K** 上提升最显著，说明 PPOW 特别适合需要结构化决策的任务。
- 在 **MT-Bench** 上增益较小，可能因为开放对话允许多种合理续写，降低对 drafter 精准性的依赖。
- 相比 **OSD / Lookahead / FastDraft**，PPOW 在 GSM8K 上大幅领先（如 Vicuna-7B 上 T 从 3.53 提升至 6.12）。

### 消融实验结果（Table 4）

| Method | MT-Bench (T) | GSM8K (T) |
|--------|---------------|-----------|
| w/o Rdist | 5.05 | 6.41 |
| w/o ADAW | 4.82 | 6.35 |
| w/o both | 4.38 | 6.05 |
| **PPOW (Full)** | **5.47** | **6.50** |

> 🔍 结果表明：
- **Rdist** 提供更密集反馈，尤其在早期截断时保留学习信号；
- **ADAW** 显著提升训练效率，聚焦“难窗口”；
- 两者协同作用，缺一不可。

### 其他重要实验发现
- **Candidate Group Size Trade-off**（Table 2）：
  - PPOW 在小 candidate group size（如 4）下即可达到高 acceptance length，而 baseline 需要更大 group（如 16）才能接近其性能，说明 PPOW 更高效利用验证资源。
- **vs Continued Supervised Training**（Figure 3 & Table 3）：
  - 继续监督训练初期略有提升，但很快饱和甚至下降；
  - PPOW 持续稳定提升，最终性能更高，证明其优化目标的本质差异。

---

## 4. 关键结论和发现

### 主要发现
1. **Token-level 训练不足以最大化 speculative decoding 效率**，必须转向 **window-level、prefix-sensitive 的优化范式**。
2. **PPOW 成功将 RL 引入 drafter 训练**，通过 performance-driven reward 和 adaptive windowing，显著提升 acceptance length 和 speedup。
3. **ADAW 的有效性得到验证**：切换至 ADAW 后训练 reward 下降、KL divergence 上升，表明模型开始面对更具挑战性的样本，并逐步适应（Figure 4）。
4. PPOW 在 **结构化任务**（如代码、数学）上表现尤为突出，说明其擅长捕捉关键决策路径。

### 方法的局限性
- **训练开销较大**：需维护 frozen target model，执行 grouped rollout 和 speculative verification，资源消耗高于监督训练。
- **超参数较多**：涉及 window size、cost ratio、proximity threshold、KL coefficient 等，需仔细调参。
- **实现复杂度高**：相比简单微调，PPOW 框架更复杂，部署门槛较高。

### 未来工作方向
- 设计 **自适应或 self-tuning 版本** 的 PPOW，减少对人工设定超参数的依赖。
- 将类似思想扩展至其他推理模块，如 **candidate allocation、request scheduling、load balancing** 等，构建端到端优化的 inference pipeline。
- 探索 **更高效的 RL 实现方式**，降低训练成本，推动实用化落地。

---

> 📌 **总体评价**：  
> PPOW 是首个系统性地将 **performance-driven RL** 应用于 speculative decoding 的工作，提出了 **reward design + adaptive sampling** 的双轮驱动机制，实验证明其在多个模型和任务上显著优于现有方法，为未来高效 LLM 推理提供了新的算法视角。

</details>

---

### 6. [GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration](https://arxiv.org/abs/2605.13848)

**Authors**: Yeahia Sarker, Md Rahmat Ullah, Musa Molla, Shafiq Joty  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.13848v1  

#### Abstract
Agentic LLM frameworks that rely on prompted orchestration, where the model itself determines workflow transitions, often suffer from hallucinated routing, infinite loops, and non-reproducible execution. We introduce GraphBit, an engine-orchestrated framework that defines workflows explicitly and de...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文《GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration》总结**

---

## **1. 论文的主要贡献和创新点**

### **解决了什么问题**
当前主流的基于 LLM 的 **Agentic LLM frameworks**（如 LangChain、AutoGen、CrewAI）依赖于 **prompted orchestration**，即由 LLM 自身通过自然语言推理决定工作流的执行路径。这种设计存在三大系统性缺陷：
- **幻觉路由（Hallucinated Routing）**：LLM 可能调用不存在的 agent 或 tool，导致静默失败。
- **无限循环（Infinite Loops）**：agents 之间可能反复调用而无法终止。
- **非确定性执行（Non-reproducible Execution）**：相同输入可能产生不同执行轨迹，影响审计与合规。

此外，上下文不断累积导致 **context bloat**，降低长流程中的推理质量，并且每次决策都需要一次完整的 LLM 推理，效率低下。

---

### **提出了什么新方法或新思路**
作者提出 **GraphBit**，一个**引擎驱动的图式智能体框架（engine-orchestrated agentic framework）**，其核心思想是：
- 将工作流定义为显式的、**有向无环图（DAG）**，所有节点和边都具有类型约束。
- 使用一个高性能的 **Rust 执行引擎** 来控制所有状态转移、工具调用和路由逻辑，而非依赖 LLM 决策。
- 引入 **三层次内存架构（three-tier memory architecture）** 隔离不同阶段的数据，防止上下文污染。

#### **三大核心原则**：
1. **图原生执行（Graph-native Execution）**  
   工作流以 DAG 形式建模，支持并行分支执行和条件控制流。

2. **引擎治理编排（Engine-governed Orchestration）**  
   所有路由决策由执行引擎基于结构化状态谓词做出，彻底消除 LLM 幻觉。

3. **分层内存隔离（Hierarchical Memory Isolation）**  
   - **Tier 1：临时草稿区（Ephemeral Scratch）** —— 单个节点内的临时计算空间，完成后释放。
   - **Tier 2：结构化状态（Structured State）** —— 全局键值存储，记录工作流上下文，支持原子更新。
   - **Tier 3：外部连接器（External Connectors）** —— 统一接口访问数据库/API/文件系统，结果需显式请求，避免自动注入造成 context bloat。

---

### **相比现有方法的优势**
| 维度 | GraphBit | 传统 Prompted Orchestration |
|------|---------|-----------------------------|
| 路由可靠性 | ✅ 引擎强制执行，零幻觉 | ❌ LLM 决策易出错 |
| 执行可重复性 | ✅ 确定性执行 | ❌ 非确定性轨迹 |
| 性能开销 | ✅ 11.9ms 处理延迟 | ❌ 最高达 70ms（如 AutoGen） |
| 上下文管理 | ✅ 分层隔离防膨胀 | ❌ 上下文持续增长 |
| 审计能力 | ✅ 支持全链路追踪 | ❌ 不可审计 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **GAIA benchmark**（Mialon et al., 2023）：面向通用 AI 助手的真实任务评测集，涵盖多步推理、工具使用、网页导航等。
- 从原始 165 个任务中筛选出 **68 个高质量任务** 构成评估子集，排除所有框架均失败的任务以增强区分度。
- 按难度分为三级：
  - Level 1: 29 个单步任务
  - Level 2: 36 个多步推理任务
  - Level 3: 3 个复杂规划任务（含大量工具调用）

### **实验设置**
- **统一 LLM 后端**：所有框架使用相同的 **GPT-5.2** 模型（闭源），温度 = 1.0，max_tokens = 2000。
- **公平配置**：各框架采用其推荐的最佳实践进行等效配置。
- **最大迭代次数限制为 3**，确保比较一致性。
- **硬件环境多样化**：在多种 CPU 架构（Intel/AMD/Apple M1/M4）、操作系统上测试，验证跨平台稳定性。

### **评估指标**
| 指标 | 描述 |
|------|------|
| **Accuracy (%)** | 正确完成任务的比例（双重验证：字符串匹配 + LLM 评估） |
| **Hallucination Rate (%)** | 因框架错误（如路由失败、死循环）导致的失败比例 |
| **Processing Time (ms)** | 框架处理开销（不含 LLM API 延迟） |
| **Throughput (ops/min)** | 每分钟可处理的操作数 |
| **Peak Memory (MB)** | 峰值内存消耗 |
| **CPU Utilization (%)** | 平均 CPU 占用率 |
| **Token Consumption** | 每任务平均输入/输出 token 数量 |

### **基线方法对比**
共对比 **6 个主流框架**：
- **LangChain**
- **LangGraph**
- **CrewAI**
- **Microsoft AutoGen**
- **Pydantic AI**
- **LlamaIndex**

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（整体表现）**

| Framework | Acc.(%) | Hall.(%) | Proc.(ms) | Mem.(MB) | Thpt. (ops/min) |
|----------|--------|--------|-----------|----------|------------------|
| **GraphBit** | **67.6** | **0.0** | **11.9** | **126.1** | **5,025** |
| Pydantic AI | 52.9 | 0.0 | 18.3 | 166.5 | 3,278 |
| LlamaIndex | 50.0 | 0.0 | 15.0 | 165.4 | 4,000 |
| CrewAI | 44.9 | 14.3 | 31.0 | 202.2 | 1,935 |
| LangChain | 38.2 | 41.2 | 36.1 | 234.4 | 1,662 |
| LangGraph | 36.8 | 47.1 | 31.5 | 208.0 | 1,905 |
| AutoGen | 35.3 | 33.8 | 70.0 | 274.8 | 857 |

> ✅ GraphBit 在所有维度全面领先：**准确率最高（67.6%）**，**幻觉率为 0%**，**延迟最低（11.9ms）**，**吞吐量达 5,025 ops/min（3× 于最快基线）**

---

### **按任务类型拆解性能**

| Task Type | Framework | Acc.(%) | Hall.(%) |
|----------|----------|--------|--------|
| **No-Tool**（纯推理） | GraphBit / Others | 57.1 | 0.0 |
| **Document-Augmented** | GraphBit | **68.4** | **0.0** |
| **Web-Enabled**（含搜索） | GraphBit | **69.0** | **0.0** |
| | Pydantic AI | 54.8 | 0.0 |
| | LangGraph | 21.4 | **69.0** |

> 🔍 发现：在需要工具调用的任务中（尤其是 Web 搜索），GraphBit 优势显著；而 LangGraph 的 **69.0% 幻觉率意味着超过三分之二的失败源于框架自身错误**。

---

### **按任务难度分析**

| Framework | Level 1 | Level 2 | Level 3 |
|----------|--------|--------|--------|
| **GraphBit** | **79.3** | **63.9** | **66.7** |
| LangGraph | 48.3 | 27.8 | 0.0 |
| AutoGen | 58.6 | 38.9 | 0.0 |

> 📉 Prompted orchestration 框架随任务复杂度上升性能急剧下降，**GraphBit 表现出更强的鲁棒性和可扩展性**。

---

### **消融实验结果（Ablation Study）**

| Configuration | Acc.(%) | Mem.(MB) | ΔAcc. |
|---------------|--------|---------|-------|
| **Full GraphBit** | **67.6** | **126.1** | — |
| w/o ephemeral scratch | 64.7 | 189.2 | -2.9 |
| w/o structured state | 57.4 | 138.7 | **-10.2** |
| w/o external connectors | 60.3 | 130.4 | -7.3 |
| Single-tier baseline | 52.9 | 247.8 | **-14.7** |

> 🔬 结论：
- **structured state 是最关键组件**，移除后准确率下降超 10 个百分点。
- **内存隔离机制对性能提升至关重要**，单一共享内存模型退化至仅 52.9% 准确率。
- 三者协同作用显著优于任何单一变体。

---

## **4. 关键结论和发现**

### **主要发现**
1. **框架级幻觉是当前 agent 系统的主要瓶颈**，而非 LLM 本身的推理能力。例如 LangGraph 在 Web 任务中高达 69.0% 的失败是由 **hallucinated routing** 导致。
2. **确定性编排（deterministic orchestration）可以同时实现高可靠性和高性能**，无需牺牲灵活性。
3. **GraphBit 的三层次内存架构有效抑制 context bloat**，每任务平均 token 消耗仅为 **1,916**，远低于 Pydantic AI（6,276）和 CrewAI（13,638）。
4. **Rust 引擎带来显著性能增益**：处理延迟低至 11.9ms，吞吐量达 5,025 ops/min，是 AutoGen 的近 6 倍。

---

### **方法的局限性**
- **需要显式 DAG 定义**：用户必须预先设计完整的工作流图，不适合高度动态或开放式任务。
- **评估集中在 GAIA benchmark**，且 Level 3 任务仅 3 个，统计意义有限。
- 所有实验基于同一 LLM（GPT-5.2），未体现各框架在特定模型上的优化潜力。

---

### **未来工作方向**
- 探索 **混合模式（hybrid deterministic + LLM routing）**：保留部分灵活性的同时保障核心路径的可靠性。
- 扩展到更大规模、更多样化的 benchmark（如 AgentBench、SWE-bench）。
- 支持 **动态 DAG 修改** 和运行时任务分解（inspired by DynTaskMAS）。
- 开源 GraphBit 并推动标准化 agent workflow specification。

---

> 💡 **一句话总结**：  
> **GraphBit 通过将 workflow 编排从 LLM 中剥离，交由类型安全的 DAG 引擎执行，并结合分层内存管理，在准确性、可靠性、效率三个维度全面超越现有 agent 框架，为构建可审计、可复现的企业级 agentic 应用提供了新范式。**

🔗 **代码开源地址**：[github.com/InfinitiBit/graphbit](https://github.com/InfinitiBit/graphbit)

</details>

---

### 7. [Precise Verification of Transformers through ReLU-Catalyzed Abstraction Refinement](https://arxiv.org/abs/2605.14294)

**Authors**: Hengjie Liu, Zhenya Zhang, Jianjun Zhao  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.14294v1  

#### Abstract
Formal verification of transformers has become increasingly important due to their widespread deployment in safety-critical applications. Compared to classic neural networks, the inferences of transformers involve highly complex computations, such as dot products in self-attention layers, rendering ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Precise Verification of Transformers through ReLU-Catalyzed Abstraction Refinement**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
- **Transformer 验证中的精度瓶颈**：现有的 Transformer 形式化验证方法（如 [23]）依赖于对非线性操作（如 self-attention 中的 dot product）进行凸松弛（convex relaxation），但这些方法常引入较大的**近似误差（approximation error）**，导致频繁出现**误报（false alarms）**，即模型实际鲁棒但被判定为不安全。
- 特别是，dot product 操作的平面松弛（planar relaxation）虽然高效，但往往不够紧致（suboptimal），限制了验证精度。

### **提出的新方法与新思路**
- 提出 **BuFFeT**（**BoUnd Fusing-based reFinement for Transformers**），一种基于 **ReLU 的抽象精炼（abstraction refinement）框架**，用于提升 Transformer 验证的精度。
- **核心思想**：
  - 将 dot product 的两个互补的平面松弛（一个来自 [23]，另一个为其对偶 bound）通过 **ReLU 函数融合**，形成更精确的非线性上界和下界。
  - 利用经典神经网络验证中成熟的 **ReLU 线性松弛技术**（如 CROWN、DeepPoly 等），将该非线性 bound 转换为可传播的线性约束，从而在保持效率的同时提高精度。
- 具体实现两种变体：
  - **r-BuFFeT**：基于规则选择最优的 ReLU 下界斜率 α，依据输入范围最小化近似误差面积。
  - **o-BuFFeT**：将优化 α 视为一个优化问题，使用梯度下降（如 Adam）迭代搜索最优 α，直到验证成功。

### **相比现有方法的优势**
- **更高的验证精度**：通过融合双平面 bound 并利用 ReLU 进行精细化控制，显著减少了 over-approximation，提升了可验证的最大扰动半径（maximal verified ε）。
- **理论上的完备性保证**：方法在 α ∈ [0,1] 时保持 soundness（即不会漏报）。
- **通用性强**：将 Transformer 验证与经典 NN 验证的技术桥接，使得大量已有的 ReLU 松弛优化技术可迁移至 Transformer 场景。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
- **SST (Stanford Sentiment Treebank)**：电影评论情感分析数据集，二分类任务（正面/负面）。
- **Yelp Polarity**：大规模餐厅评论情感分析数据集，二分类任务。
- 数据统计详见 Table 3：SST 含约 6.7 万训练样本，Yelp 含 56 万训练样本。

### **实验设置**
- **模型架构**：
  - 多种层数的标准 Transformer（N = 1, 2, 3, 6 层）。
  - **TinyBERT**（4 层），作为紧凑型预训练模型代表。
  - 所有模型均仅使用 encoder 结构，适用于文本分类任务。
- **鲁棒性属性**：
  - 考察单个词向量在 L1 范数下的扰动（single-word perturbations）。
  - 定义鲁棒性为：在扰动范围内，模型预测标签不变。
- **总任务数**：共 10 个模型 × 140 个验证任务 = **1400 个验证任务**。

### **评估指标**
- **Maximal verified ε**：能被形式化验证的最大扰动半径，越大表示验证精度越高。
- **Time costs**：每个验证任务的平均耗时，衡量效率。
- **Margin**：分类置信度下界，用于动态观察优化过程。

### **基线方法对比**
- **Baseline**: **CrownBaF [23]** — 当前最先进的 Transformer 验证框架，采用线性松弛策略。
- 对比方法：r-BuFFeT 和 o-BuFFeT。

---

## **3. 主要实验结果和性能指标**

### **关键性能数据与对比结果**

#### ✅ **RQ1: 精度对比（vs. baseline）**
- **总体表现**：在绝大多数任务中，BuFFeT 显著优于 baseline。
- **r-BuFFeT**：
  - 在多数情况下略优于 baseline，尤其在深层模型（N=6）中优势明显。
  - 但在某些情况（如 Yelp-N=6, TinyBERT）下略有 underperformance，因其启发式规则并非全局最优。
- **o-BuFFeT**：
  - **全面领先**：在几乎所有任务中都优于 baseline 和 r-BuFFeT。
  - 可验证的 ε 最大提升可达 **2.7 倍以上**（如 TinyBERT on SST/Yelp）。
  - Boxplot 显示其中位数和最大值均稳定高于其他方法。
- **模型深度影响**：随着 encoder 层数增加（N↑），BuFFeT 的优势愈发显著，说明其精炼机制在复杂模型中累积效果更强。

#### ✅ **RQ2: α 的有效性验证**
- 图 6 展示了 o-BuFFeT 在优化过程中 **Margin 的增长轨迹**：
  - 初始随机 α 导致 Margin 为负（无法验证）。
  - 经过数百步优化后，Margin 跨越 0，成功验证。
  - 在某些 baseline 失败的任务中，o-BuFFeT 成功完成验证，证明了其**迭代优化能力的有效性**。

#### ✅ **RQ3: 效率分析**
- **r-BuFFeT**：
  - 时间开销约为 baseline 的 **1.1–1.7 倍**，效率接近，可接受。
- **o-BuFFeT**：
  - 时间开销较大，为 baseline 的 **33.5–96.9 倍**（见 Table 2）。
  - 原因：每次迭代相当于一次完整传播，需多次迭代才能收敛。
  - 但绝对时间仍在可接受范围内：即使是 6 层模型或 TinyBERT，也能在**几分钟内完成验证**。
  - 开销与模型深度增长关系不大，表明其**可扩展性良好**。

#### 🔁 **消融实验（补充实验 G）**
- **与 LSE [29] 的横向比较**（Table 5）：
  - LSE 改进 softmax 松弛，o-BuFFeT 改进 dot product 松弛。
  - 两者结合（`LSE + o-BuFFeT`）取得最佳效果，**相对增益达 1.61%**，远超单独使用任一方法。
  - 表明不同组件的松弛优化具有**正交性和互补性**，可联合使用以获得更强验证能力。

---

## **4. 关键结论和发现**

### **主要发现**
1. **ReLU 可作为抽象精炼的“催化剂”**：通过 ReLU 表达 dot product 的融合 bound，成功将经典 NN 验证中的成熟技术迁移到 Transformer 验证中。
2. **o-BuFFeT 是最有效的策略**：尽管计算成本更高，但其通过优化 α 能够显著提升验证精度，尤其适用于高难度或深层模型的验证任务。
3. **验证精度随模型复杂度提升而受益更大**：模型越深，抽象误差累积越多，因此精炼机制带来的收益也越显著。
4. **不同松弛技术可组合使用**：dot product 与 softmax 的松弛优化互不冲突，组合使用可进一步提升整体验证性能。

### **方法的局限性**
- **计算开销较高**：尤其是 o-BuFFeT，不适合需要实时验证的场景。
- **依赖输入范围估计质量**：若前期 bound 估计不准，可能影响后续优化效果。
- **当前评估集中于 NLP 分类任务**：尚未在生成式任务或其他模态（如 Vision Transformer）中广泛验证。

### **未来工作方向**
1. **混合策略优化**：例如，用 r-BuFFeT 的结果初始化 o-BuFFeT 的 α，加速收敛。
2. **跨领域应用**：将 BuFFeT 应用于 Vision Transformer、Transformer-based 控制器等其他安全关键系统。
3. **结合分支定界（Branch-and-Bound）**：在 o-BuFFeT 无法验证时启动更精细的 complete verification 方法。
4. **硬件/求解器优化**：探索更高效的优化器配置或专用加速方案以降低 o-BuFFeT 的时间成本。

---

> **总结一句话**：  
> 本文提出了 **BuFFeT**，首次利用 **ReLU** 将 Transformer 中 dot product 的多个平面松弛进行融合，并借助经典 NN 验证技术实现高效且高精度的验证，在大多数任务中显著超越 state-of-the-art 方法，尤其是在深层模型上表现出色，为未来 Transformer 验证研究提供了新的范式。

</details>

---

### 8. [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040)

**Authors**: Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu, Rui Yang, Tao Ge, Alessandrio Sordoni, Xingdi Yuan, Yelong Shen, Pengcheng He, Tong Zhang, Zhou Yu, Jianfeng Gao  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.15040v1  

#### Abstract
Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with environments. Despite major investment, open research remains constrained by infrastructure and training gaps. Many high-performing s...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **Orchard: An Open-Source Agentic Modeling Framework** 论文总结

---

## 1. **论文的主要贡献和创新点**

### **解决的问题**
当前 **Agentic Modeling**（将大语言模型 LLMs 转化为能自主执行复杂任务的智能体）的研究面临以下瓶颈：
- **基础设施封闭**：许多高性能的 Agent 系统依赖于专有代码、模型或服务，缺乏开放性和可复现性。
- **训练框架耦合严重**：现有系统（如 ProRL Agent、MegaFlow）将环境管理（sandbox management）与训练流程、推理调度等深度绑定，导致轨迹数据、训练配方（recipes）和评估协议难以跨领域、跨工具链复用。
- **成本高昂**：托管型沙箱平台（如 E2B、Daytona、Modal）虽然易用，但按秒计费，对大规模强化学习（RL）训练不经济。

### **提出的新方法与新思路**
作者提出了 **Orchard**，一个开源的、可扩展的 **Agentic Modeling 框架**，其核心创新在于：

#### **核心组件：Orchard Env**
- **薄而独立的环境服务**（thin, standalone environment service）：Orchard Env 是一个基于 Kubernetes 的轻量级服务，提供沙箱生命周期管理、命令执行、文件 I/O 和网络策略等基础原语（primitives），通过 REST API 暴露。
- **解耦设计**（decoupled design）：它与 Agent Harness（代理工具链）、训练器（trainer）、推理后端和任务领域完全解耦，实现了“一次部署，处处可用”。
- **关键技术选择**：
  - **运行时代理注入**（Runtime Agent Injection）：通过 Kubernetes Init Container 将执行代理动态注入任意用户提供的 Docker 镜像，无需修改原始镜像，支持异构任务环境。
  - **直接 Pod IP 通信**（Direct Pod-IP Communication）：绕过 Kubernetes API Server，直接向沙箱 Pod 发送执行请求，显著降低延迟。

#### **统一的训练范式**
在 Orchard Env 之上，构建了三个可组合的 **Agentic Modeling Recipes**，涵盖：
- **监督微调**（SFT）
- **在线策略强化学习**（On-policy RL）
- **评估套件**（Evaluation Suite）

这些 Recipe 可以在不同领域（软件工程、GUI 导航、个人助理）复用，验证了环境层作为“可复用基座”的可行性。

### **相比现有方法的优势**
| 维度 | Orchard Env | 现有方案（E2B, Daytona, ProRL 等） |
| :--- | :--- | :--- |
| **开放性** | ✅ 完全开源，可自托管 | ❌ 多为托管服务或闭源 |
| **解耦性** | ✅ 纯粹的环境服务，与上层完全解耦 | ❌ 通常与训练栈或 Agent Harness 深度耦合 |
| **成本** | ✅ 自托管 + Spot 实例，成本低至 Daytona 的 **0.1x** | ❌ 托管服务按秒计费，成本高昂 |
| **延迟** | ✅ 平均命令执行延迟 **0.28s** | ❌ E2B (0.747s), Modal (2.046s) 更高 |
| **可扩展性** | ✅ 支持 1000 个沙箱并行，成功率 100% | ⚠️ 受限于平台能力 |

---

## 2. **核心实验方法和设置**

### **使用的数据集**
Orchard 在三个不同领域进行了验证，使用了多个权威数据集：

1. **软件工程 (Orchard-SWE)**:
   - **SWE-bench Verified** (500 个实例)：人类验证的 GitHub 问题修复基准，主评测集。
   - **SWE-rebench**, **SWE-rebench V2**, **Scale-SWE**：用于轨迹蒸馏的大规模任务源。

2. **GUI 浏览器导航 (Orchard-GUI)**:
   - **WebVoyager**
   - **Online-Mind2Web**
   - **DeepShop**
   - 任务种子来自 **WebGym**，经过五步过滤得到 15,601 个去重的训练任务。

3. **个人助手 (Orchard-Claw)**:
   - **Claw-Eval**：评估多步骤日常工作效率的基准。
   - 任务由 **Claude Opus 4.6** 合成，共 192 个。

### **实验设置和评估指标**
- **模型骨干**（Backbone）：
  - Orchard-SWE & Orchard-Claw: `Qwen3-30B-A3B-Thinking` (~3B active parameters)
  - Orchard-GUI: `Qwen3-VL-4B-Thinking`
- **训练流程**：两阶段 SFT + RL。
- **评估指标**：
  - **SWE-bench**: `resolve rate`（补丁通过测试套件的比例）。
  - **GUI Benchmarks**: `success rate`（任务成功完成率）。
  - **Claw-Eval**: `pass@3`（在三次尝试内成功完成任务的比例）。

### **基线方法对比**
- **SWE 领域**：与 `OpenSWE`, `SWE-Master`, `CoderForge-32B` 等开源 SWE Agent 对比。
- **GUI 领域**：与 `Gemini CUA`, `GPT-5 SoM`, `MolmoWeb`, `Fara-7B` 等对比。
- **通用对比**：与专有系统（如 GPT-4o, Gemini, Claude Opus）进行比较。

---

## 3. **主要实验结果和性能指标**

### **关键性能数据**
| **方法** | **领域** | **模型大小** | **性能** | **备注** |
| :--- | :--- | :--- | :--- | :--- |
| **Orchard-SWE (SFT)** | SWE-bench Verified | 30B-A3B | **64.3%** | 仅 SFT |
| **Orchard-SWE (SFT+RL)** | SWE-bench Verified | 30B-A3B | **67.5%** | SFT + RL，SOTA 开源同尺寸模型 |
| **Orchard-GUI (SFT+RL)** | WebVoyager | 4B | **74.1%** | |
| | Online-Mind2Web | 4B | **67.0%** | |
| | DeepShop | 4B | **64.0%** | |
| | **平均** | 4B | **68.4%** | 超越所有开源模型，媲美 Gemini CUA (69.3%) |
| **Orchard-Claw (SFT+RL)** | Claw-Eval | 30B-A3B | **59.6% pass@3** | |
| | | | **73.9% pass@3** | + ZeroClaw Harness |

### **与基线方法的对比结果**
- **Orchard-SWE**：
  - 显著优于同尺寸的 `Qwen3-Coder-30B` (51.6%) 和 `GLM-4.7-Flash` (59.2%)。
  - 优于更大的密集模型 `OpenSWE-72B` (66.0%)。
- **Orchard-GUI**：
  - 以 **4B 模型** 和 **仅 2.6K 训练任务**，达到 68.4% 的平均成功率。
  - 性能远超 `MolmoWeb-8B` (51.9%) 和 `Fara-7B` (44.6%)。
  - 与专有的 `Gemini CUA` (69.3%) 和 `GPT-5 SoM` (65.8%) 处于同一水平。
- **Orchard-Claw**：
  - 仅用 0.2K 合成任务，达到 59.6% pass@3。
  - 与更强的 `ZeroClaw` Harness 结合，提升至 **73.9% pass@3**，证明了跨 Harness 泛化能力。

### **消融实验结果**
1. **数据规模 vs. 选择策略**：
   - 数据规模的影响远大于选择策略。从 512 到 2048 条轨迹，性能提升超过 8 个百分点，而不同选择策略间的差距不足 3 个百分点。
   - 结论：**“More data is better”**。

2. **Credit-Assignment SFT**：
   - 引入对失败轨迹中“有效进展段”（rise segments）的监督信号，相比仅使用成功轨迹，在 SWE-bench 上带来了 **+1.9%** 的提升。

3. **强化学习 (RL) 的作用**：
   - RL 在 SFT 基础上带来显著提升（Orchard-SWE: 64.3% → 67.5%）。
   - 有趣的是，从一个较弱的 SFT 检查点开始 RL，其在分布外（OOD）任务上的提升更大，表明 RL 具有“广覆盖精炼”的作用。

4. **跨 Harness 泛化**：
   - 单一 Harness 训练的模型在其他 Harness 上表现急剧下降（如 `OpenSWE-32B` 在 Kimi-CLI 上从 62.4% 降至 3.6%）。
   - **Orchard-SWE** 由于在训练中使用了 `OpenHands` 和 `mini-swe-agent` 两种 Harness，表现出优异的泛化能力，最差情况下的性能下降被限制在 19.3 个百分点以内。

---

## 4. **关键结论和发现**

### **主要发现**
1. **环境层是可复用性的基石**：一个**薄、开放、与工具链无关**（harness-agnostic）的环境服务（如 Orchard Env）是实现跨领域、跨工具链、跨训练阶段（蒸馏、RL、评估）数据和方法复用的关键。
2. **基础设施设计直接影响研究效率**：Orchard Env 的低成本和低延迟使得大规模轨迹蒸馏和 RL 训练对学术界变得可行。
3. **多样性是泛化的关键**：在数据层面（多教师、多任务源）和架构层面（多 Harness）引入多样性，能显著提升模型的泛化能力和鲁棒性。
4. **小模型也能有大作为**：Orchard-GUI 证明了一个 4B 的 VLM，通过精心设计的 SFT+RL 流程，可以在复杂的 GUI 任务上媲美甚至超越专有的大模型。

### **方法的局限性**
- **依赖高质量的教师模型**：Orchard-SWE 和 Orchard-GUI 的成功很大程度上依赖于强大的教师模型（如 MiniMax-M2.5, Qwen3.5-397B）来生成高质量的蒸馏轨迹。
- **合成数据的挑战**：Orchard-Claw 使用了人工合成的任务，这可能无法完全反映真实世界的复杂性，且成本较高（每个任务约 4.9 美元）。
- **泛化仍有极限**：尽管跨 Harness 泛化能力很强，但当面对完全未见过的 Harness 或领域时，性能仍会大幅下降。

### **未来工作方向**
- **自动化任务合成**：开发更高效、低成本的方法来生成多样化的训练任务。
- **更通用的 Agent Harness**：探索能够无缝适应多种工具接口的通用 Agent 架构。
- **社区共建**：鼓励社区贡献新的训练 Recipe、任务数据集和评估基准，共同推动开源 Agentic Modeling 的发展。

</details>

---

### 9. [APWA: A Distributed Architecture for Parallelizable Agentic Workflows](https://arxiv.org/abs/2605.15132)

**Authors**: Evan Rose, Tushin Mallick, Matthew D. Laws, Cristina Nita-Rotaru, Alina Oprea  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.15132v1  

#### Abstract
Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, these systems hit critical reasoning, coordination, and computational scaling bottlenecks as the size ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：APWA: A Distributed Architecture for Parallelizable Agentic Workflows

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前基于 **Large Language Models (LLMs)** 的多智能体系统在处理大规模、复杂任务时面临以下瓶颈：
- **推理瓶颈**：随着任务规模增长，LLM 的推理质量和上下文管理能力显著下降。
- **协调瓶颈**：现有系统依赖集中式 **orchestrator** 进行同步消息传递，导致扩展性差，难以支持大规模并行执行。
- **计算瓶颈**：无法有效利用分布式基础设施进行高度并行化的任务分解与执行。
- **通用性不足**：多数系统为特定应用设计，缺乏对异构数据和动态工作流的支持。

这些问题严重限制了多智能体系统在高吞吐量、可并行化任务中的应用潜力。

---

### 提出了什么新方法或新思路
作者提出 **Agent-Parallel Workload Architecture (APWA)** ——一种专为可并行化 **agentic workflows** 设计的分布式多智能体系统架构。

#### 核心创新点：
1. **智能自动任务分解（Intelligent & Automated Task Decomposition）**
   - 利用 **Manager Agent** 动态将复杂任务分解为非干扰的子任务（subtasks），每个子任务可在独立资源上并行执行，无需跨通信。
   - 支持数据驱动、异构、动态规划路径的探索。

2. **分层抽象体系（Hierarchical Abstractions）**
   - **Manager**：负责全局任务规划、状态跟踪和子任务调度。
   - **Worker**：执行具体子任务，具有本地视图和高自主性。
   - **Executor**：基于 **Ray** 构建，实现分布式执行、容错重试、资源调度等底层细节封装。

3. **新型编程抽象**
   - **Subtask Templates**：通过占位符机制批量生成大量子任务，解耦逻辑与数据规模。
   - **Data Tables**：引入类似数据库表的只读序列记录抽象，使 LLM 能高效操作超大规模数据元信息。
   - **Capability Registry**：运行时动态发现和组合功能模块（如 WebSurfer、Code Interpreter），提升灵活性。

4. **去中心化协调模型**
   - Workers 不直接相互通信，仅与 Manager 交互，避免全局协调开销。
   - 支持上千个 Worker 并发执行，显著提升吞吐量。

---

### 相比现有方法的优势
| 特性 | APWA | Magentic-One / Autogen | MegaAgent |
|------|------|------------------------|-----------|
| 并行化程度 | ✅ 高度并行（数千并发） | ❌ 序列执行为主 | ⚠️ 小规模并行 |
| 自动任务分解 | ✅ 动态、数据感知 | ❌ 手动定义流程 | ⚠️ 层级划分但静态 |
| 分布式支持 | ✅ 原生集成 Ray | ❌ 单机为主 | ⚠️ 有限支持 |
| 可扩展性 | ✅ 支持百万级对象 | ❌ 上下文爆炸 | ❌ 协调失败 |
| 异构任务支持 | ✅ 支持多种并行模式 | ⚠️ 有限 | ❌ 困难 |

> **总结优势**：APWA 实现了真正意义上的“大规模并行智能体工作流”，突破了传统 LLM 多智能体系统的性能天花板。

---

## 2. 核心实验方法和设置

### 使用的数据集
论文在三个基准任务上进行了评估：

| 数据集 | 类型 | 描述 |
|-------|------|------|
| **PII-300k** | 敏感信息脱敏 | 对 30 万条非结构化文本进行 PII 检测与红acted，涵盖教育、医疗等领域，共 27 类 PII。 |
| **SchemaBench** | 结构化内容提取 | 从异构格式（LaTeX、XML、CSV、HTML）中提取符合指定 schema 的 JSON 输出。 |
| **SummaryBench** | 层级摘要生成 | 在文学作品（如《罗密欧与朱丽叶》《罗马帝国衰亡史》）上按层级（scene → act → full）生成摘要，测试多轮并行化能力。 |

此外还进行了一个 **WebSurfer 报告合成实验**，要求生成多个主题的技术报告。

---

### 实验设置和评估指标

#### 系统配置
- 单机环境：AMD Ryzen Threadripper PRO 5955WX + 2×RTX 4090 GPU
- 使用模型：`GPT-5.4`, `GPT-5.4-mini`, `GPT-5.4-nano`
- 分布式框架：**Ray**（支持高达数万并发任务）

#### 评估维度
| 维度 | 指标 |
|------|------|
| **Utility（效用）** | - Structural Score（输出格式正确性）<br>- Semantic Score（语义准确性） |
| **Cost（成本）** | - Wall-clock Runtime（真实耗时）<br>- Token Usage（token 消耗）<br>- Monetary Expense（费用） |

---

### 基线方法对比
1. **Direct LLM**  
   - 将全部输入以纯文本形式提交给 LLM，使用结构化生成模式输出结果。
   - 用于衡量无任务分解的上限。

2. **Magentic-One**  
   - 当前最先进的多智能体框架，采用 Orchestrator-Worker 架构，支持文件系统、浏览器、代码解释器等功能。
   - 子任务串行执行，协调由 LLM 控制。

3. **MegaAgent**  
   - 层次化多智能体系统，支持递归创建子团队。
   - 但仍受限于昂贵的 agent-modulated 协调机制。

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总

#### 表格 1：**Failure Rate & Wall-Clock Time（SummaryBench 和 PII-300k）**

| Method | R&J (166kB) | Dynasts (942kB) | Roman (10.5MB) | PII-4096 |
|--------|-------------|------------------|----------------|----------|
| Direct | 0%, 19s     | 60%, 76s         | 100%           | 100%     |
| Magentic-One | 100%       | 100%             | 100%           | 80%, 91s |
| MegaAgent | 80%, 472s    | 80%, 248s        | 70%, 579s      | 70%, 372s |
| **APWA** | **0%, 157s** | **0%, 210s**     | **0%, 329s**   | **0%, 221s** |

> 💡 **观察**：APWA 在所有大任务上均成功完成，而其他方法几乎全部失败；且运行时间随数据增长呈亚线性上升。

---

#### 表格 2：**Structural & Semantic Scores**

| Method | R&J (Str./Sem.) | Roman (Str./Sem.) | PII-4096 (Str./Sem.) |
|--------|------------------|--------------------|------------------------|
| Direct | 1.000 / 0.433    | –                  | –                      |
| Magentic-One | ↑ / ↑          | ↑ / ↑            | 1.000 / 0.179          |
| MegaAgent | 0.140 / 0.043   | 0.160 / 0.016      | 0.250 / 0.000          |
| **APWA** | **0.954 / 0.424** | **0.919 / 0.232** | **0.900 / 0.544**      |

> ✅ APWA 在保持高结构完整性的同时，语义质量远超基线。

---

### 消融实验结果（Ablation Study）

#### 不同模型组合下的性能对比（Table 3）

| Configuration | Structural | Semantic | Runtime (s) | Cost ($) |
|---------------|------------|----------|------------|---------|
| APWA (5.4×mini) | 0.983 | 0.370 | 336 | $6.57 |
| APWA (mini×mini) | 0.897 | 0.394 | **94** | **$0.294** |
| APWA (mini×nano) | 0.916 | 0.408 | **96** | **$0.225** |

> 🔍 发现：
- 使用更小的 worker 模型（如 nano）可大幅降低成本和延迟，同时维持较高语义得分。
- 规划阶段使用更强模型（GPT-5.4）有助于提高整体结构一致性。

---

### WebSurfer 实验结果
- **任务**：生成 10 / 20 / 100 个主题的技术报告。
- **结果**：
  - 所有规模下 **Structural Score ≥ 0.975**
  - **Semantic Score 达到 0.995（100 topics）**
  - 运行时间分别为：143s / 157s / 595s
  - **负载增加 10 倍，运行时间仅增 4.2 倍 ⇒ 显示良好并行扩展性**

---

## 4. 关键结论和发现

### 主要发现
1. **APWA 成功实现了高度可扩展的并行化 agentic 工作流**：
   - 能够动态分解复杂查询为并行子任务，在 **2.5k+ 并发 agents** 下稳定运行。
   - 在数据量增长近两个数量级的情况下仍能保持低失败率和合理响应时间。

2. **传统多智能体系统存在根本性扩展瓶颈**：
   - Magentic-One 因“上下文爆炸”和“协调失败”在大数据集上完全失效。
   - MegaAgent 虽尝试并行，但受限于角色分工而非真正的数据并行。

3. **轻量化 worker + 强规划 manager 是高效策略**：
   - 对简单任务（如摘要）可路由至 LLM-only 路径，吞吐提升 10–100×。
   - 规划质量决定最终输出保真度。

4. **APWA 具备良好的通用性和适应性**：
   - 支持多种并行模式（data-parallel, task-parallel, replication-parallel）
   - 可灵活接入外部工具（如 WebSurfer），构建全 agentic pipeline。

---

### 方法的局限性
1. **不支持 Worker 间直接通信**
   - 所有协调必须经由 Manager，限制了需要协作的子任务场景（如共识决策）。

2. **未验证对更多并行模式的泛化能力**
   - 当前仅测试了几种典型模式，是否适用于任意动态工作流尚待验证。

3. **安全与隐私未被考虑**
   - 高自治性可能带来 prompt injection、恶意工具注入、数据泄露等风险。
   - 缺乏访问控制和审计机制。

4. **依赖外部服务稳定性**
   - 如 Capability Registry、Object Store 等组件若不可靠会影响整体可用性。

---

### 未来工作方向
1. **引入 Worker-to-Worker 通信机制**
   - 在可控范围内允许局部协作，增强表达力。

2. **加强安全性设计**
   - 添加沙箱隔离、权限控制、行为监控等机制，防范滥用。

3. **探索自适应并行策略选择**
   - 让 Manager 能根据任务特征自动选择最优并行模式（MapReduce vs Pipeline vs Tree）。

4. **部署于真实生产环境验证**
   - 在医疗、金融、科研等高价值领域测试其鲁棒性和实用性。

5. **结合 LLM 编译优化技术**
   - 如 **LLM Compiler** 或 **Function Calling Optimization**，进一步降低调度开销。

---

> 📌 **总体评价**：APWA 是首个真正面向“大规模并行化智能体工作流”的系统级架构，填补了当前 LLM 多智能体系统在高吞吐、可扩展场景下的空白，有望成为下一代 agentic computing 的基础设施范式。

</details>

---

### 10. [Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding](https://arxiv.org/abs/2605.14005)

**Authors**: Shuoyang Sun, Chang Da, Hao Fang, Kuofeng Gao, Xinhao Zhong, Yi Sun, Fan Mo, Shu-Tao Xia, Bin Chen  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.14005v1  

#### Abstract
Speculative decoding has become a widely adopted technique for accelerating large language model (LLM) inference by drafting multiple candidate tokens and verifying them with a target model in parallel. Its efficiency, however, critically depends on the average accepted length $\tau$, i.e., how many...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding》总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
该论文揭示了 **Speculative Decoding**（推测性解码）机制中一个此前未被充分认识的**机制级安全漏洞**。尽管 Speculative Decoding 被广泛用于加速大语言模型（LLM）推理，其效率高度依赖于“平均接受长度” $ T $ ——即每次验证步骤中能成功通过目标模型校验的草稿 token 数量。

然而，由于 **drafter 模型对 target model 分布的近似不可避免地存在偏差**（drafter-target mismatch），这种微小的不匹配可被恶意利用：攻击者可通过在输入提示中添加微小扰动，使草稿 token 极易被拒绝，从而导致 $ T $ 崩溃、加速失效，而最终输出语义仍保持正常。这构成了一种新型的 **acceleration-collapse attack**（加速崩溃攻击）。

### 提出了什么新方法或新思路
论文提出了 **MISTLETOE**，一种针对 Speculative Decoding 的**隐蔽加速崩溃攻击方法**，其核心思想是：
- **不改变最终输出内容**，而是破坏“草稿-验证”机制本身；
- 通过优化一个附加在原始 prompt 后的短离散后缀（discrete suffix），诱导 drafter 提出的 token 在 target model 下变得极不可能（高 surprisal），从而降低接受率；
- 同时约束 target model 自身的输出分布变化（semantic preservation），避免引起明显异常。

### 相比现有方法的优势
- **攻击层面新颖**：不同于传统关注输出安全性（如 jailbreak）或隐私泄露的研究，MISTLETOE 首次从**机制鲁棒性角度**出发，指出 Speculative Decoding 的效率机制本身即可成为攻击面。
- **隐蔽性强**：攻击后模型输出的 **perplexity** 和语义质量基本不变，难以被用户察觉。
- **通用性好**：攻击具有跨方法的**可迁移性**，在一个 decoding 方法上生成的对抗后缀可在其他方法上有效转移。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
实验在三个代表性基准上进行，覆盖多种生成任务：
- **MT-Bench**：80 个开放域对话问题，测试指令遵循与多轮交互能力。
- **HumanEval**：随机采样 100 个代码生成样本，测试程序合成能力。
- **GSM8K**：随机采样 100 个数学应用题，测试多步推理能力。

### 实验设置和评估指标
#### 模型与 Speculative Decoding 系统
- **Target Models**：Vicuna-7B 和 Vicuna-13B。
- **Decoding Methods**：
  - Medusa
  - Hydra
  - EAGLE / EAGLE-2 / EAGLE-3

所有模型参数冻结，仅优化附加的离散后缀 $ \delta \in \mathcal{V}^m $，其中 $ m=20 $。

#### 评估指标
- **Average Accepted Length $ T $**：每个 target model 前向传播所提交的平均 token 数，反映机制效率。
- **Speed-up**：相对于标准自回归解码的速度提升倍数。
- **Perplexity (PPL)** 和 **Repetition Rate (Rep-4)**：衡量输出自然性和语义保真度。
- **KL 散度**：用于约束对抗后缀引起的 target distribution 漂移。

#### 对抗优化策略
采用 **null-space projected optimization**：
1. 定义两个目标：
   - $ L_{\text{rej}} $：最大化 target-side draft-token surprisal（拒绝压力）
   - $ L_{\text{sem}} $：限制 KL 散度以保持语义一致性
2. 在连续松弛空间计算梯度 $ g_{\text{rej}}, g_{\text{sem}} $
3. 将拒绝梯度投影到语义保留方向的**零空间**（null space），得到可行更新方向
4. 使用该方向指导离散 token 替换，并通过 **KL-bound veto** 过滤漂移过大的候选

---

## 3. 主要实验结果和性能指标

### 关键性能数据（见 Table 1）
| 数据集       | 平均 Speed-up 下降 | 平均 $ T $ 下降 |
|------------|------------------|---------------|
| MT-Bench   | ↓1.89× (51.7%)  | ↓0.99         |
| HumanEval  | ↓2.12× (48.1%)  | ↓1.21         |
| GSM8K      | ↓2.20× (51.3%)  | ↓1.13         |

> 注：攻击后 speed-up 接近 2×，表明 Speculative Decoding 几乎退化为普通自回归解码。

#### 典型案例表现
- 在 **Vicuna-13B + EAGLE-3** 上：
  - HumanEval 清洁速度提升达 **6.17×**，攻击后降至 **2.77×**
  - $ T $ 从 7.08 降至 3.99
- 即使原本加速较弱的方法（如 Medusa），攻击也显著削弱其性能。

### 与基线方法的对比结果
- 所有 decoding 方法（Medusa、Hydra、EAGLE 系列）均受到严重影响，说明攻击具有**广泛适用性**。
- 攻击效果在原本加速更强的系统上更明显（更多可破坏的接受机会）。

### 消融实验结果（见 Table 2）
| 配置               | Speed-up ↓ | $ T $ ↓ | PPL    | Rep-4 ↓ |
|--------------------|-----------|--------|--------|---------|
| Clean              | 5.47×     | 5.95   | 2.5    | 0.1813  |
| $ L_{\text{rej}} $ only | 3.30×     | 3.41   | 334.1  | 0.0844  |
| $ L_{\text{sem}} $ only | 4.47×     | 4.73   | 213.2  | 0.0634  |
| Naive Joint        | 3.73×     | 4.13   | 196.6  | 0.0952  |
| **Full MISTLETOE** | **1.83×** | **2.79** | **49.2** | **0.0111** |

#### 结论：
- 仅使用 $ L_{\text{rej}} $ 可降速但导致 PPL 激增（输出异常）
- 仅使用 $ L_{\text{sem}} $ 则攻击无效
- **Null-space projected optimization 是关键**：它实现了强攻击力与高输出保真的平衡。

### 可迁移性分析（见 Table 3）
在 EAGLE-3 上训练的对抗后缀迁移到其他方法：
- **Medusa**：MT-Bench 上 speed-up 从 3.68× → **1.03×**
- **Hydra**：HumanEval 上从 4.26× → **1.91×**
- 表明攻击捕获的是跨方法共享的脆弱性（drafter-target agreement 依赖）

---

## 4. 关键结论和发现

### 主要发现
1. **Speculative Decoding 存在机制级安全隐患**：即使输出语义正常，其加速机制仍可能被隐蔽破坏。
2. **Drafter-target mismatch 是可被放大的攻击面**：微小扰动即可引发 acceptance collapse。
3. **Null-space projection 能有效协调冲突目标**：在不牺牲语义的前提下最大化拒绝压力。
4. **攻击具备跨方法泛化能力**：非过拟合于特定 decoding 架构。

### 方法的局限性
- **白盒假设**：当前攻击依赖于访问模型梯度，在完全黑盒场景下需进一步研究。
- **评估范围有限**：目前仅在 Vicuna 系列模型和几种主流 decoding 方法上验证，尚未扩展至更大规模或生产级系统。
- **输出保真度评估不够全面**：仅用 PPL 和 Rep-4 不足以完全刻画语义等价性，缺乏人工或 LLM-based judgment。

### 未来工作方向
- 设计 **black-box 或 query-efficient 版本** 的 MISTLETOE，适用于闭源部署环境。
- 开发针对此类攻击的**防御机制**，例如：
  - 监控 $ T $ 分布异常
  - 检测 drafter-target 匹配度突变
  - 引入更鲁棒的验证规则
- 探索其他 LLM 加速技术（如 Distillation、KV Cache Compression）是否也存在类似机制脆弱性。

---

> ✅ **总结一句话**：  
> MISTLETOE 揭示了 Speculative Decoding 的“高效”背后潜藏“脆弱”，提出了一种通过**语义保持扰动**实现**隐蔽加速崩溃**的新范式，呼吁构建更具鲁棒性的 LLM 推理加速体系。

</details>

---

### 11. [OmniDrop: Layer-wise Token Pruning for Omni-modal LLMs via Query-Guidance](https://arxiv.org/abs/2605.14458)

**Authors**: Yeo Jeong Park, Hyemi Jang, Minseo Choi, Jongsun Lee, Jooyoung Choi, Yongkweon Jeon  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.14458v1  

#### Abstract
Omni-modal large language models have demonstrated remarkable potential in holistic multimodal understanding; however, the token explosion caused by high-resolution audio and video inputs remains a critical bottleneck for real-time applications and long-form reasoning. Existing omni-modal token comp...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# OmniDrop: Layer-wise Token Pruning for Omni-modal LLMs via Query-Guidance — 核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题？

**Omni-modal LLMs**（如 Qwen2.5-Omni）在处理高分辨率音频和视频输入时面临严重的 **token explosion** 问题。例如，一分钟的视频可生成超过 10k 的 audio 和 video tokens，导致计算和内存开销呈 **quadratic 增长**，严重制约了实时推理和长序列理解。

现有 token compression 方法（如 OmniZip、DASH）通常在 **input embedding level** 进行压缩，依赖以下两种假设：
- **audio-video token 的 embedding 相似性** 表示语义对齐；
- **时间共现**（temporal co-occurrence）表示语义相关。

然而，论文指出这两个假设在实践中并不可靠：
- 音频和视频 token 在输入嵌入空间中占据不同子空间，缺乏充分对齐；
- 时间上同时发生的音视频事件可能描述不同场景（如背景音乐与画面无关）。

因此，**input-level pruning 容易误删重要模态特异性信息**，影响下游任务表现。

---

### ✅ 提出了什么新方法或新思路？

论文提出 **OmniDrop**，一种无需训练的、**layer-wise token pruning 框架**，其三大核心创新如下：

#### （1）**Progressive Layer-wise Pruning (PLP)**  
不在输入层剪枝，而是在 **LLM decoder 层内部逐层渐进式剪枝**：
- 浅层保留更多 token，确保跨模态信息充分融合；
- 深层逐步增加剪枝强度，去除冗余 token。
- 剪枝比例按 **sigmoid 函数调度**：  
  $$
  p_l = p_{\text{init}} + (p_{\text{final}} - p_{\text{init}}) \cdot \sigma(l, t_{\text{mid}}, \beta)
  $$

#### （2）**Query-Guided Token Importance**  
以 **text query 作为语义引导信号**，衡量每个 audio/video token 对任务的相关性：
- 计算 text-to-audiovisual attention 得分作为重要性评分；
- 实现 **task-adaptive 剪枝**：音频任务保留更多 audio token，视觉任务反之；
- 避免依赖不可靠的 audio-video 相似性假设。

#### （3）**Temporal Diversity Score (TDS)**  
为防止剪枝过度集中在高注意力区域而导致全局上下文丢失，引入 TDS：
- 识别“关键 chunk”（最高 attention 所在段）；
- 对远离该 chunk 的 token 给予分数提升，鼓励时间多样性；
- 平衡局部聚焦与全局感知。

此外，在进入 LLM 前还进行 **intra-modality pruning**：
- Audio：保留 audio encoder 最后一层高 attention token（OmniZip）；
- Video：使用 TTM 合并相似帧（Dycoke）；

最终实现 **平均仅保留 20%-30% tokens**，仍保持高性能。

---

### ✅ 相比现有方法的优势

| 维度 | OmniZip / DASH | OmniDrop |
|------|----------------|----------|
| **剪枝阶段** | Input-level | **Decoder layer-wise** |
| **指导信号** | Audio-video similarity / temporal co-occurrence | **Text query attention** |
| **任务适应性** | 固定策略 | **动态自适应**（audio/query/video 任务自动调整） |
| **时间上下文保留** | 易丢失远端信息 | 引入 **TDS** 保证多样性 |
| **是否需训练** | 是（部分） / 否 | **完全无需训练** |

> ✅ **优势总结**：更可靠、更灵活、更高效，且适用于多种规模模型（3B/7B）。

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

| 数据集 | 任务类型 | 特点 |
|-------|--------|------|
| **VideoMME** [8] | 视频理解综合评测 | 多领域视频问答，评估整体理解能力 |
| **WorldSense** [13] | 音视频联合问答 | 要求融合 audio 和 video 推理，涵盖 Music, Sports, Tech 等多个领域 |
| **AVUT** [29] | 音频中心视频理解 | 强调声音识别，避免文本捷径，测试纯 audio-driven 任务 |

---

### ⚙️ 实验设置

- **模型**：Qwen2.5-Omni-7B 和 Qwen2.5-Omni-3B（公开可用 Omni-LLM）
- **硬件**：单张 NVIDIA H100 GPU
- **加速技术**：使用 FlashAttention 减少显存占用
- **输入格式**：采用 time-interleaving 结构，每 chunk 包含 video 和 audio tokens
- **token 数量控制**：报告 **平均 token retention ratio**，便于与固定比率 baseline 比较

#### 剪枝调度参数（7B 模型为例）：
| 目标保留率 | $p_{\text{init}}$ | $p_{\text{final}}$ | $t_{\text{mid}}$ | $\beta$ |
|----------|--------------------|---------------------|------------------|--------|
| 30%      | 0.0                | 0.2                 | 0.5              | 20     |
| 20%      | 0.02               | 0.5                 | 0.5              | 20     |

- TDS 从中间层开始启用（7B: layer 14；3B: layer 19）
- 多样性权重 $\lambda_{\text{div}} = 0.2$

---

### 🔁 基线方法对比

| 方法 | 类型 | 核心机制 |
|------|------|---------|
| **OmniZip** [31] | Training-free | Audio-guided compression，基于 audio-video cosine similarity 合并 token |
| **DASH** [18] | Training-free | 利用 audio 边界检测进行动态分段，video pruning 受 audio 控制 |

> 所有方法均在相同预处理流程下运行，确保公平比较。

---

## 3. 主要实验结果和性能指标

### 📊 性能总览（Table 2）

| 方法 | Retained Ratio (%) | VideoMME ↑ | WorldSense ↑ | AVUT ↑ | Prefill Time ↓ | GPU Mem ↓ |
|------|--------------------|------------|---------------|--------|----------------|-----------|
| Full (7B) | 100 | 64.67 | 46.85 | 65.17 | 1.73s | 28.92GB |
| OmniZip (30%) | 30 | 65.85 | 45.55 | 61.76 | 1.06s (-39%) | 25.76GB |
| DASH (30%) | 30 | 65.67 | 45.87 | 60.96 | 1.07s (-38%) | 25.68GB |
| **OmniDrop (30%)** | 30 | **66.52** | **46.60** | **64.01** | **1.05s (-39.9%)** | **25.65GB** |
| **OmniDrop (20%)** | 20 | **66.44** | **46.50** | **63.67** | **1.04s (-40%)** | **25.65GB** |

> ✅ **关键结果**：
- 在 **30% 保留率下，OmniDrop 超越全量 token 模型**（如 VideoMME 66.52 > 64.67）；
- 在 **极端 20% 压缩下，仍优于所有 baseline**，尤其在 AVUT 上领先 **+3.58 pts**（7B setting）；
- **Prefill latency 最多降低 40%**，**GPU memory 最多减少 14.7%**；
- 性能下降极小：从 30% → 20%，平均仅降 **0.18 pts（7B）** vs OmniZip/DASH 下降超 1.0 pts。

---

### 🔍 消融实验结果（Ablation Studies）

#### （1）Progressive Layer-wise Pruning (PLP) vs 固定剪枝

| 方法 | Ratio | WorldSense | AVUT |
|------|------|-----------|------|
| Intra-pruning only | 45% | 46.50 | 64.19 |
| Intra-pruning only | 30% | 44.33 | 59.34 |
| **PLP (Sigmoid)** | 30% | **46.53** | **63.84** |
| **PLP (Sigmoid)** | 20% | **46.25** | **63.32** |

> ✅ PLP 显著恢复因早期剪枝造成的信息损失，证明 **layer-wise 剪枝优于 input-level**。

#### （2）Temporal Diversity Score (TDS) 效果

| 方法 | Ratio | WorldSense | AVUT |
|------|------|-----------|------|
| PLP-Sig | 30% | 46.53 | 63.84 |
| **+ TDS** | 30% | **46.60** | **64.01** |
| PLP-Sig | 20% | 46.25 | 63.32 |
| **+ TDS** | 20% | **46.50** | **63.67** |

> ✅ TDS 在高压缩比下增益更大，说明其对维持 **全局时间上下文** 至关重要。

#### （3）Query Guidance 类型对比（Table 4）

| 方法 | Ratio | WorldSense | AVUT |
|------|------|-----------|------|
| Audio guidance | 30% | 45.59 | 60.84 |
| **Text guidance (Ours)** | 30% | **46.78** | **61.53** |
| Audio guidance | 20% | 43.25 | 56.57 |
| **Text guidance (Ours)** | 20% | **46.19** | **60.55** |

> ✅ **Text-guided pruning 显著优于 audio-guided**，验证 query 是更可靠的 relevance 判断依据。

---

### 🎯 Task-Adaptive Token Retention 可视化（Figure 4）

在不同任务下，OmniDrop 自动调节 audio/video 保留比例：
- **Audio Recognition (AR)**：保留最多 audio tokens；
- **Scene Recognition (SR)**：保留最多 video tokens；
- **Audio Source Localization (ASL)**：平衡保留两者。

> ✅ 无需显式任务标签，即可实现 **modality-adaptive 压缩**。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Input-level audio-video similarity 不足以支撑有效 token pruning**：
   - PCA 和 cosine similarity 分析显示 audio/video embeddings 未充分对齐；
   - 基于相似性的剪枝效果不优于随机采样。

2. **LLM decoder 层中 audiovisual token 的重要性是 query-dependent 且 layer-dependent**：
   - 浅层 attention 分散，需保留更多信息；
   - 中深层 attention 收敛，适合激进剪枝。

3. **OmniDrop 实现高效且鲁棒的 token 压缩**：
   - 在 **20%-30% token 保留率** 下，性能反超 baseline 甚至 full model；
   - 显著降低 latency 和 memory 开销，适合部署。

4. **Query-guidance + TDS 构成通用高效的压缩范式**：
   - 可扩展至其他 multi-modal 任务；
   - 无需训练，即插即用。

---

### ⚠️ 局限性

1. **依赖 text query**：
   - 当前框架必须有 text prompt 才能进行 pruning；
   - 无法应用于仅有 audio-video 输入的无监督场景。

2. **超参数经验设定**：
   - 如 $p_{\text{init}}, p_{\text{final}}, t_{\text{mid}}, \lambda_{\text{div}}$ 等均为人工调优；
   - 缺乏自动化学习机制。

3. **未探索与其他 inference acceleration 技术结合**：
   - 如 KV Cache 压缩、模型量化等。

---

### 🔮 未来工作方向

1. **Develop query-free token selection mechanisms**：
   - 探索直接建模 audio-video semantic 关系的方法；
   - 利用 self-supervised learning 学习跨模态对齐。

2. **Learnable pruning schedules**：
   - 使用 calibration data 自动优化剪枝策略；
   - 将 pruning policy 与模型 jointly fine-tune。

3. **Extend to streaming / real-time scenarios**：
   - 动态调整剪枝强度以适应变化的输入长度和任务需求。

4. **Integration with other efficiency techniques**：
   - 结合 KV Cache 压缩、稀疏 attention、量化等，构建端到端高效 Omni-LLM 推理 pipeline。

---

> 💡 **总体评价**：OmniDrop 提出了一种新颖、实用、无需训练的 layer-wise token pruning 框架，突破了传统 input-level 压缩的局限，为构建高效、响应迅速的 Omni-modal LLMs 提供了强有力的技术路径。

</details>

---

### 12. [A Hardware-Aware, Per-Layer Methodology for Post-Training Quantization of Large Language Models](https://arxiv.org/abs/2605.14929)

**Authors**: Earl Killian  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.14929v1  

#### Abstract
Scaled Outer Product (SOP) is a post-training quantization methodology for large language model weights, designed to deliver near-lossless fidelity at 4.5--6 bits per weight on hardware with per-layer LUT decode. The methodology combines per-layer search of fixed and dynamic codebook pairs selected ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Hardware-Aware, Per-Layer Methodology for Post-Training Quantization of Large Language Models

## 1. 论文的主要贡献和创新点

### 解决的问题
本文旨在解决**大语言模型（LLM）后训练量化（Post-Training Quantization, PTQ）中的精度-存储权衡问题**。传统方法在低比特（如4–6 bpw）下难以保持模型保真度，尤其是面对权重分布中的异常值（outliers）和层间异质性时。此外，现有量化方案往往忽略硬件执行效率，导致理论性能无法在实际系统中兑现。

### 提出的新方法：Scaled Outer Product (SOP)
作者提出了一种名为 **Scaled Outer Product (SOP)** 的硬件感知、逐层优化的PTQ方法，其核心创新包括：

- **灵活的块缩放（Flexible Block Scaling）**  
  在沿 $K$ 维度的每 $g$ 个元素上共享一个缩放因子（scale），实现 `s/g + b` bpw 的平均比特率（例如 $g=16$, 12-bit scale, 6-bit atom → 6.75 bpw）。支持 absmax 和 argmax 两种缩放策略，并引入 **Flayer 整数位移搜索** 来对齐每层的 scale 分布与格式动态范围。

- **激活加权余弦相似度（Activation-Weighted Cosine Similarity, ACos）**  
  提出 ACos 作为比 MSE 更能预测下游困惑度（perplexity）的保真度指标，通过通道范数（channel norms）对误差进行加权，避免低影响通道主导量化分配。

- **双码本配对搜索（Per-Layer Pair Search）**  
  每层从一组固定（NF4, BOF4, Split87, SH4）和自适应（DD4）原子中选择最优的两个码本组合（La, Lb），并通过每块一位元数据选择使用哪个码本重建。该机制允许高度定制化的逐层配置。

- **多级纠错机制**  
  - **OPQ（Outlier Per-Quantum Extraction）**：将高幅值权重提取为稀疏旁路存储。
  - **Wr（Sparse Residual Correction）**：存储激活加权后残差最大的项作为稀疏修正。

- **多重选择背包分配器（Multiple-Choice Knapsack Allocator, MCKP）**  
  在全局比特预算下，联合决定每层是否进行格式提升（promotion）、应用何种纠错，以最大化参数加权的总 ACos。

- **硬件高效输出格式 HIF7/HIF8**  
  设计专用于 SOP 架构的浮点网格 HIF7（80值）和 HIF8（96值），采用 shift-add 结构而非通用浮点单元，提升能效与面积效率。

### 相比现有方法的优势
- **更高的保真度与更低的存储成本**：在 6.5 bpw 下超越 8.0 bpw 的传统 FP8 基线。
- **硬件友好性**：微内核仅依赖 rank-1 outer product 与 Hadamard 积，适配专用矩阵单元。
- **无需梯度或标签数据**：完全基于校准集计算 channel norms，适用于纯 PTQ 场景。
- **逐层自适应性强**：不同模型、不同层可生成不同的码本配置，充分利用统计多样性。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **校准数据集（Calibration Corpus）**：小型文本语料（未指定具体名称，提及 `c4` 数据集用于部分实验），用于计算每层的 **channel norms**。
- **评估数据集**：`wikitext2`（50K tokens），用于测量 KL 散度等下游指标（见附录 C）。

### 实验设置
- **模型家族**：涵盖六个开源 LLM 家族：
  - Gemma-3-1B
  - SmolLM3-3B
  - Llama-3.2-3B
  - Qwen3.5-4B
  - Mistral-7B-v0.3
  - Qwen3-8B
- **块大小（block size）**：默认 $g=16$
- **比特范围**：聚焦于 4.5–6 bpw 区间
- **量化粒度**：逐层（per-layer）决策，非全局统一

### 评估指标
| 指标 | 描述 |
|------|------|
| **Weight Reconstruction MSE** | 权重量化后的均方误差，用于衡量重建质量 |
| **ACos (Activation-Weighted Cosine Similarity)** | 提出的核心保真度代理指标，定义为 $(W, \hat{W})_c / (\|W\|_c \|\hat{W}\|_c)$，其中 $c$ 是 channel norms 向量 |
| **KL Divergence** | 下游输出分布与原始模型的 KL 散度，反映实际任务性能 |
| **bpw (bits per weight)** | 存储开销指标 |

### 基线方法对比
- **主流 FP8 基线**：`E4M3^0sUE8M0` —— 使用 E4M3 atom，每层一个 power-of-two scale，共 8.0 bpw
- **其他对比格式**：
  - 不同 scale 精度（8/10/12-bit）
  - 是否启用 metabit 或 sign bit
  - 是否使用 HIF7 vs E2M3 网格

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ **HIF7 在多种 scale 格式下的重建 MSE（表2）**
所有模型在 12-bit scale 下 MSE 收敛至与 16-bit BF16（E8M7）相当水平，表明 scale 精度在 12-bit 即饱和。

> 示例（Llama-3.2-3B）：
> - UE5M7 (12-bit): 1.84×10⁻⁷
> - E8M7 (16-bit): 1.84×10⁻⁷ → **无进一步收益**

#### ✅ **HIF7 vs E2M3 替代性测试（表3）**
在推荐的 UE4M4 缩放下，E2M3 的 MSE 仅比 HIF7 高 **3.8–4.1%**，远低于理论预测的 ~61%，说明 E2M3 可作为发布友好的替代方案。

#### ✅ **核心对比：Block-scaled FP6 vs Layer-POT FP8（表4）**

| Model | E2M3sUE4M4 (6.5 bpw) | E4M3^0sUE8M0 (8.0 bpw) |
|-------|------------------------|--------------------------|
| Gemma-3-1B | 3.41×10⁻¹ | 4.40×10⁻² |
| Llama-3.2-3B | 2.11×10⁻⁷ | 2.72×10⁻⁷ |
| Mistral-7B | **5.36×10⁻⁹** | **6.89×10⁻⁹** |

👉 **结论**：SOP 推荐的操作点 `E2M3sUE4M4`（6.5 bpw）在**更低 1.5 bpw 存储成本下，实现了优于传统 FP8 基线的权重重建精度**。

#### ✅ **消融实验与关键发现**
- **Scale Format 影响**（表2）：
  - 8-bit：`UE4M4` > `E4M3`（优势 17–20%）
  - 12-bit：所有变体几乎无差别 → **12-bit 足够**
- **Sign Bit vs Metabit 权衡**：
  - 8-bit 容器中二者互斥；12-bit 容器（如 S1E5M5）可同时容纳 sign + metabit，是推荐格式。
- **Flayer 搜索有效性**（附录 D）：
  - 在 `E4M3^0sUE8M0` 上启用 Flayer 后，各层最大 MSE 与平均 MSE 比值与其他 per-block scaling 方法一致，证明其有效吸收了层间动态范围差异，使 per-layer POT scaling 不再脆弱。

---

## 4. 关键结论和发现

### 主要发现
1. **块缩放小原子 + 精细 scale 控制 可取代传统 FP8**  
   推荐操作点 `E2M3sUE4M4`（6.5 bpw）在更低存储下优于 `E4M3^0sUE8M0`（8.0 bpw），打破了“更高比特=更高精度”的直觉，展示了 **Pareto 最优前沿的跃迁**。

2. **逐层自适应设计至关重要**  
   不存在全局最优码本组合，最佳 `(La, Lb)` 对随层、模型、部署目标变化。SOP 利用 SRAM 中的 per-layer LUT 和 metabit 实现灵活切换。

3. **ACos 是更优的保真度代理指标**  
   在 promotion regime 下，ACos 比 MSE/SQNR 更紧密相关于下游 KL，指导资源分配更有效。

4. **Scale 精度在 12-bit 达到饱和**  
   进一步增加 scale 位宽不再降低 MSE，且 S1E5M5（12-bit signed + metabit）成为理想选择。

5. **HIF7 与 E2M3 具有高度可替代性**  
   尽管 HIF7 有更多 codepoints，但 E2M3 能高效捕获 MSE 关键子集，适合公开比较。

### 方法的局限性
- **依赖专用硬件支持**：SOP 微内核依赖 rank-1 outer product 与 scale tile 乘法，需定制矩阵单元支持；若无 FC-SRAM 或 LUT SRAM，面积开销显著上升。
- **未涉及训练阶段**：本文专注于 PTQ，未探讨将 SOP 思路融入训练（如低精度训练）的可能性。
- **复杂度较高**：pair search + MCKP allocation 流程较长，虽可在数秒内完成，但仍高于简单均匀量化。

### 未来工作方向
- **探索 n=3 的可行性**：当前尚无实用的 3-bit codebook，可能需要 Hadamard rotation 等预处理配合。
- **扩展至 activation quantization**：目前 focus on weights，activations 仍假设为较高精度。
- **研究 E2M5 等高 mantissa 格式在训练中的潜力**（附录 C 注释）。
- **开发 sub-7-bit packing 或 tc6 扩展网格** 以进一步压缩或提升精度。
- **结合 LoRA 等微调技术实现端到端低比特微调 pipeline**。

---

> 📌 **总结一句话**：  
> SOP 展示了通过 **硬件感知的设计（block scaling + SOP kernel）**、**逐层自适应搜索（pair + MCKP）** 和 **更合理的保真度指标（ACos）**，可以在 **6.5 bpw** 下实现超越 **8.0 bpw FP8** 的量化效果，为 LLM 部署提供了一个新的高效范式。

</details>

---

### 13. [Conditional Attribute Estimation with Autoregressive Sequence Models](https://arxiv.org/abs/2605.14004)

**Authors**: Erica Stutz, Giacomo Marino, Daniella Meeker, Qiao Liu, Andrew J. Loza  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.14004v1  

#### Abstract
Generative models are often trained with a next-token prediction objective, yet many downstream applications require the ability to estimate or control sequence-level properties. Next-token prediction can lead to overfitting of local patterns during training, underfitting of global structure, and re...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Conditional Attribute Estimation with Autoregressive Sequence Models

## 1. 论文的主要贡献和创新点

### 解决的问题
传统生成模型（如语言模型）通常采用 **next-token prediction** 作为训练目标，这种局部优化策略容易导致：
- 过度拟合局部模式（greedy overfitting）
- 忽视序列级全局属性（sequence-level attributes）的建模
- 在推理阶段难以高效估计或控制序列属性（如情感、正确性、医疗风险等）

许多下游任务需要对序列级属性进行预测或引导生成（steerable generation），但现有方法依赖昂贵的 **Monte Carlo (MC) 采样** 或额外的辅助模型，计算开销大且灵活性差。

---

### 提出的新方法：Conditional Attribute Transformers (CAT)

作者提出 **Conditional Attribute Transformers (CAT)**，一种联合建模 **next-token 概率** 和 **序列级属性条件概率** 的统一框架。

#### 核心思想
在单次前向传播中同时预测：
1. `P(sn | Sa)`：给定前缀序列 $S_a$ 下一个 token 的概率（标准语言建模）
2. `P(a | Sa, sn)`：给定前缀和下一个候选 token 时，序列属性 $a$ 的条件概率

通过共享 Transformer 骨干网络，在最终隐状态上分支两个输出头：
- **Token Head**：负责 next-token 预测
- **Attribute Head + Block**：预测属性（支持 binary/multinomial/numeric）

#### 创新点
- ✅ **无需修改输入序列即可实现属性控制**（vs CTRL、Quark 等需插入 control code）
- ✅ 支持三种关键能力于单一 forward pass：
  1. **Per-token credit assignment**：识别每个 token 对属性值的影响
  2. **Counterfactual analysis**：量化不同 token 选择下的属性变化
  3. **Steerable generation**：基于属性概率引导解码
- ✅ 可集成到预训练过程或用于微调已有模型
- ✅ 显著优于采样方法的速度（约 **105× 加速**）

---

### 相比现有方法的优势

| 方法类别 | 代表 | CAT 的优势 |
|--------|------|-----------|
| **Conditioning-based** | CTRL, Decision Transformers, Quark | 不需修改输入；提供概率化属性估计；允许动态修正错误选择 |
| **Auxiliary Model Guidance** | PPLM, FUDGE, GeDi, DExperts, Director | 更低计算成本；保留完整 Transformer 表达力；避免多模型训练 |
| **Sampling-based** | MC Simulation | 推理速度快几个数量级；无需多次 rollout |

---

## 2. 核心实验方法和设置

### 使用的数据集
论文在三个差异显著的任务上验证 CAT 的有效性：

| 数据集 | 类型 | 属性类型 | 描述 |
|-------|-----|---------|------|
| **Key-to-Door** | 强化学习环境 | Binary (win/lose) | 三房间网格世界，稀疏奖励任务，测试长期信用分配能力 |
| **Amazon Reviews** | 自然语言 | Multinomial (1–5 星评分) | 5.74 亿条商品评论，测试大规模文本中的属性控制 |
| **PhysioNet Sepsis** | 医疗时间序列 | Binary (是否发生脓毒症) + Numeric (未来6小时最大心率) | 4 万 ICU 患者数据，测试临床风险预测能力 |

---

### 实验设置与评估指标

#### 统一架构
- 基于 **nanoGPT** 架构扩展
- 总损失函数为加权组合：
  $$
  \mathcal{L} = \mathcal{L}_{\text{token}} + \lambda \cdot \mathcal{L}_{\text{attr}}
  $$
  - $\mathcal{L}_{\text{token}}$: cross-entropy
  - $\mathcal{L}_{\text{attr}}$: 分类用 CE，回归用 Gaussian NLL
- 训练效率优化：仅对真实 next-token 计算属性损失（避免 $V \times A$ 矩阵展开）

#### 评估维度
| 能力 | 评估方式 |
|-----|----------|
| **Credit Assignment** | 可视化每步动作对应的胜率估计 |
| **Critic Performance** | Partial sequence 上属性预测准确率 / AUC / AP |
| **Counterfactual Analysis** | 替换形容词后属性概率的变化是否符合语义直觉 |
| **Guided Decoding** | 控制生成特定属性文本的成功率、流畅性（perplexity）、多样性（Dist-n） |

---

### 基线方法对比
| 基线 | 类型 | 是否使用 |
|-----|------|--------|
| Random Policy | RL Baseline | ✓ |
| Behavior Cloning | Imitation Learning | ✓ |
| Percentile BC | Filtered Imitation | ✓ |
| Conservative Q-Learning | Offline RL | ✓ |
| Decision Transformers | Sequence-to-Action RL | ✓ |
| CTRL | Prompt Conditioning | ✓ |
| DExperts | Expert/Anti-expert Reweighting | ✓ |
| Director / Director* | Auxiliary Attribute Head | ✓ |
| MC Sampling (GPT/CAT) | Rollout Estimation | ✓ |

---

## 3. 主要实验结果和性能指标

### Key-to-Door: 长期信用分配

| 方法 | Win Rate |
|------|----------|
| Random Policy | 0.031 |
| Behavior Cloning | 0.016 |
| Percentile BC | 0.951 |
| Conservative Q-Learning | 0.133 |
| Decision Transformers | 0.946 |
| **CAT (Ours)** | **0.999** |

- CAT 几乎达到完美性能，并且 **998/999 胜局走最短路径**
- 提供稳定、低方差的 win probability 估计，优于 Decision Transformers

---

### Amazon Reviews: 语言建模与属性控制

#### (1) Next-Token Prediction 性能
- 小模型（7M–270M）：$\lambda > 0$ 略有负面影响
- 大模型（1B 参数）：**CAT ($\lambda=0.15$) 的 perplexity 优于标准 GPT**

> 图 3 显示：当模型足够大时，联合训练反而提升 next-token 表现 —— 表明学习全局结构有助于正则化表示。

#### (2) 属性预测（Partial Review Rating Prediction）
| 方法 | Top-1 Accuracy (@ len=300) | 速度相对 MC |
|------|----------------------------|-------------|
| MC + Standard GPT | ~0.76 | 1× |
| MC + CAT | ~0.78 | 1× |
| Director* | ~0.77 | 快 |
| **CAT (ours)** | **~0.79** | **~105× faster** |

- CAT 在更短时间内实现更高精度
- 属性-only CAT 模型表现较差 → 证明 **joint learning 更优**

#### (3) Counterfactual 分析有效性
- 替换 `good` → `horrible`：
  - ↑ 1-star 概率（+0.09）
  - ↓ 5-star 概率（-0.11）
- 否定上下文（not good）中替换：
  - `not bad` → 提高 5-star 概率（合理：双重否定）
  - `not horrible` → 接近 3-star（“还行”含义）
- 大写增强语义强调（e.g., HORRIBLE 影响更大）

> 表明 CAT 学到了细粒度语义逻辑。

#### (4) Guided Decoding 结果（将 3-star 提示转向 1/5-star）

| 方法 | Accuracy (1★) | Accuracy (5★) | Perplexity (流畅性) |
|------|----------------|----------------|--------------------|
| CTRL | 0.13 / 0.41 | — | 13.68 / 13.45 |
| DExperts | 0.14 / 0.41 | — | 19.24 / 18.99 |
| Director* | 0.58 / 0.65 | — | 46.77 / 48.16 |
| **CAT (ours)** | **0.64 / 0.77** | — | **45.88 / 44.03** |

- CAT 在 **准确性最高** 的同时保持 **更低 perplexity（更流畅）**
- 多样性略低于部分方法，但仍具竞争力

---

### PhysioNet Sepsis: 医疗风险预测

#### 属性预测性能（提前 12 小时预测脓毒症）

| 方法 | ROC AUC | Average Precision (AP) |
|------|--------|------------------------|
| GPT + MC (n=64) | 0.782 | 0.271 |
| Director | 0.688 | 0.277 |
| **CAT (ours)** | 0.757 | **0.448** |

- CAT 的 AUC 略低于 MC-GPT，但在 **高度不平衡场景下 AP 显著领先**
- 说明 CAT 在高召回时仍能维持高精确率，更适合临床预警

#### Counterfactual 敏感性分析
- 升高体温 → 脓毒症风险上升
- 年龄越大（71–87 岁），发热带来的风险增幅越明显（符合医学常识）
- MAP 下降后 DBP 过低 → 引发显著风险跃升（反映生理参数间不一致性）

> 成功捕捉已知临床规则，具备可解释性。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **联合建模 next-token 与 conditional attribute 可提升两者性能**，尤其在大模型下形成协同效应。
2. ✅ CAT 实现了 **credit assignment、counterfactual analysis、steerable generation** 三大功能于一体。
3. ✅ 在稀疏奖励 RL、自然语言生成、医疗预测等多个领域均取得 SOTA 表现。
4. ✅ 属性预测速度比 MC 采样快 **两个数量级以上**，适合实时系统部署。
5. ✅ 模型可通过仅微调 attribute head 扩展至已有预训练模型，具有实用价值。

---

### 局限性
- ❌ 当前仅支持离散 action 空间的 conditional attribute prediction
- ❌ 当前 steering 策略为单步贪婪优化（single-step policy improvement），无法保证全局最优
- ❌ 属性预测依赖于训练分布，外推能力有限

> 这些限制也存在于 Director、DExperts 等类似方法中。

---

### 未来工作方向
- 🔮 扩展至连续动作空间
- 🔮 开发支持 **global optimal policy search** 的算法（而非 greedy selection）
- 🔮 应用于更多生物领域任务：
  - de-novo protein design
  - small-molecule binding 功能预测
  - DNA 序列到调控功能的映射建模
- 🔮 探索更复杂的因果推理结构（如多时间点干预）

---

## 总结

**Conditional Attribute Transformers (CAT)** 是一个简洁而强大的框架，它将序列生成与序列属性预测统一在一个模型中，解决了传统生成模型在属性控制方面的效率与灵活性瓶颈。其实验充分、跨域通用性强，是迈向 **可控生成 + 可解释 AI** 的重要一步。

</details>

---

### 14. [SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration](https://arxiv.org/abs/2605.14089)

**Authors**: Mingda Zhang, Tiesunlong Shen, Haoran Luo, Wenjin Liu, Zikai Xiao, Erik Cambria, Xiaoying Tang  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.14089v1  

#### Abstract
In recent years, a variety of powerful LLM-based agentic systems have been applied to automate complex tasks through task orchestration. However, existing orchestration methods still face key challenges, including strategy collapse under reward maximization, high gradient variance with opaque credit...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration 论文总结

## 1. 论文的主要贡献和创新点

### 解决的问题
当前基于 LLM 的智能体系统在任务编排（task orchestration）方面面临三大挑战：
- **策略崩溃 (Strategy Collapse)**：基于 REINFORCE 的强化学习方法倾向于收敛到单一的奖励最大化模式，丢失了多样化的有效策略，导致系统脆弱且难以适应变化。
- **高梯度方差与信用分配不透明 (High Gradient Variance & Opaque Credit Assignment)**：仅依赖最终奖励会导致信用分配链条过长，难以判断多步轨迹中哪一步对成功或失败负有责任。
- **无指导的技能演化 (Unguided Skill Evolution)**：现有动态技能库的更新机制（如启发式触发、固定时间表或直接用 LLM 判断）缺乏从训练信号中衍生出的原则性指导，无法回答“何时”、“何地”以及“如何”更新技能。

### 提出的新方法：SkillFlow
SkillFlow 是一个**基于流（flow-based）的框架**，将可训练的 Supervisor 作为智能体，在一个包含动态技能库（dynamic skill library）和冻结执行器（frozen executor）的结构化环境中运行。其核心创新在于 **Tempered Trajectory Balance (TTB)** 损失函数和由此驱动的递归技能演化机制。

#### 核心组件
- **Tempered Trajectory Balance (TTB)**：一种回归式的流匹配损失函数。它通过采样与奖励成比例的轨迹来训练模型，而不是将所有概率质量集中在单一最优路径上。这使得模型能够保留多种高奖励的策略路径，避免了策略崩溃。
- **双向策略 (Bidirectional Policies)**：TTB 损失函数同时训练了一个前向策略（forward policy）和一个后见之明的反向策略（hindsight backward policy）。反向策略在零额外推理成本下提供了每一步的信用分配（credit assignment），明确指出哪些决策真正推动了成功。
- **递归技能演化 (Recursive Skill Evolution)**：利用 TTB 训练过程中产生的流诊断信号（flow diagnostics）来自主决定技能库的演化：
  - **何时演化 (When)**：当 TTB 残差（△(T)）的运行均值达到平台期时，触发演化。
  - **如何演化 (What)**：根据技能的边际流（F(s)）来决定是保留、精炼还是删除某个技能。
  - **何处演化 (Where)**：通过步骤重要性（I(t)）定位决策中的关键缺口，指导生成新的技能。

### 相比现有方法的优势
- **多样性与鲁棒性**：通过奖励比例采样，保留了多样化的成功策略，增强了对环境变化的鲁棒性。
- **高效的信用分配**：反向策略提供了透明、低成本的每步信用信号，无需额外的蒙特卡洛采样。
- **自主能力增长**：首次实现了从训练信号到自主能力增长的闭环，技能库的演化由原则性的信号驱动，而非启发式规则。

## 2. 核心实验方法和设置

### 使用的数据集
在 **14 个公开基准数据集**上进行了评估，覆盖四大类任务：
- **问答 (Question Answering)**：HotpotQA, TriviaQA, MuSiQue, NQ-Open
- **数学推理 (Mathematical Reasoning)**：AIME 2026, MedQA, MATH-Hard, GPQA Diamond
- **交互式决策 (Interactive Decision Making)**：WebShop, ALFWorld, ScienceWorld, Mind2Web
- **代码生成 (Code Generation)**：SWE-bench, HumanEval

实验分为 **7 个 In-Distribution (IID)** 和 **7 个 Out-of-Distribution (OOD)** 数据集进行测试。

### 实验设置和评估指标
- **主干模型 (Backbone)**：主要使用 `Qwen3.5-9B` 作为 Supervisor，并在消融实验中测试了其他多个 LLM。
- **训练设置**：采用多轮交互的监督学习范式，Supervisor 与环境交互生成编排轨迹。
- **评估指标 (Metrics)**：
  - **问答**：F1 分数 (F1 Score)
  - **数学推理/选择题**：准确率 (Accuracy)
  - **交互式决策**：平均得分 (Average Score) 和成功率 (Success Rate, SR)
  - **代码生成**：`pass@1` (HumanEval), 解决率 (Resolved Rate, SWE-bench)
  - **网页导航**：步骤准确率 (Step Acc) 和动作 F1 (Action F1)

### 基线方法对比
与四类基线方法进行了比较：
1. **直接 LLM (Direct LLMs)**：`Qwen3.5-9B`, `v4-flash`, `Claude Haiku 4.5`，作为无编排的基准。
2. **微调 (Fine-Tuning)**：`SFT` (监督微调), `GRPO` (Group Relative Policy Optimization)。
3. **搜索式工作流 (Search-Based Workflows)**：`AFlow`，使用 MCTS 探索预定义操作符组合。
4. **RL 智能体 (RL Agents)**：`AgentFlow`, `FlowSteer`, `SkillRL`，代表现有的强化学习智能体框架。

## 3. 主要实验结果和性能指标

### 关键性能数据
- 在 **所有 14 个基准测试**上，SkillFlow 均显著优于所有基线方法。
- 在 **IID 平均 F1** 上，SkillFlow 达到了 **94.14**，相比最强的基线 `FlowSteer` 提升了 **+41.2**。
- 在 **OOD 平均 F1** 上，SkillFlow 达到了 **83.99**，相比 `FlowSteer` 提升了 **+53.5**。
- 在最具挑战性的 `SWE-bench` 上，SkillFlow 的解决率达到 **52.34%**，远超基线。

### 与基线方法的对比结果
- **超越直接 LLM**：即使与更强的 `v4-flash` 和 `Claude Haiku 4.5` 相比，SkillFlow 依然大幅领先，证明其优势源于编排策略的训练方式，而非单纯的模型容量。
- **超越 RL 基线**：在 `WebShop` 和 `ALFWorld` 等需要复杂多步决策的任务上，REINFORCE 类基线因策略崩溃而表现不佳，而 SkillFlow 凭借其多样性得以胜出。
- **超越静态工作流**：`AFlow` 等静态工作流在探索空间耗尽时会失败，而 SkillFlow 的动态技能库使其能持续进化以应对新挑战。

### 消融实验结果
通过移除 SkillFlow 的关键组件验证了各部分的有效性：
- **-TTB**：用 `GRPO` 替代 `TTB` 后，性能在多样性敏感任务（如 AIME, WebShop）上下降最严重，证实了**策略崩溃**是主要失败模式。
- **-Backward policy**：移除反向策略后，性能在多步推理任务（如 AIME, ScienceWorld）上下降更明显，凸显了**每步信用分配**的重要性。
- **-Flow-Guided Evolution**：移除任一流信号（when/where/what）都会独立地导致性能下降，证明了**递归技能演化机制**中三个信号的非冗余性和必要性。

## 4. 关键结论和发现

### 主要发现
1. **奖励比例采样是关键**：SkillFlow 通过 TTB 实现的奖励比例采样，从根本上解决了策略崩溃问题，保留了多样化的成功路径。
2. **零成本信用分配可行**：通过联合训练反向策略，可以在零额外推理成本下获得精确的每步信用信号，极大地提升了训练效率和可解释性。
3. **自主演化闭环已实现**：SkillFlow 首次展示了如何利用训练过程中的内在信号（TTB 残差、步骤重要性、技能流）来驱动技能库的自主演化，形成了一个从训练信号到能力增长的完整闭环。

### 方法的局限性
1. **依赖长上下文记忆**：多轮交互会不断增长历史记录，SkillFlow 的效果依赖于主干模型处理长上下文的能力。如果模型的长程记忆能力不足，后见之明的反向策略性能会下降。
2. **依赖主干模型的推理能力**：SkillFlow 放大了模型已有的分解和工具使用能力，但不能凭空创造新的核心推理技能。如果瓶颈在于基础推理能力，仍需额外的预训练或蒸馏。

### 未来工作方向
- 探索更高效的长上下文建模技术，以支持更长的交互序列。
- 将 SkillFlow 的框架应用于更大规模、更复杂的现实世界任务。
- 研究如何将 SkillFlow 与提升基础推理能力的方法结合，打造更全面的通用智能体。

</details>

---

### 15. [Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding](https://arxiv.org/abs/2605.14305)

**Authors**: Xun Fang, Yunchen Li, Hang Yuan, Zhou Yu  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.14305v1  

#### Abstract
Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions. This paper proposes Factorization-Error-Free ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
现有的 **Discrete Diffusion Language Models (DLLMs)** 在生成过程中通过并行预测多个 token 来提升效率，但通常采用独立的 token-wise 预测方式（如 Xo-prediction），这会引入**因子化误差（factorization error）**。该误差源于将联合分布近似为各 token 独立分布的乘积，忽略了 token 之间的依赖关系，从而损害生成质量。

此外，虽然已有方法尝试缓解此问题（如 ReDi、DDOSP），但往往以显著降低推理速度为代价；而结合 **speculative decoding** 的方法又可能破坏 DLLM 的非自回归特性。

---

### **提出的新方法与创新思路**
本文提出了 **Factorization-Error-Free Discrete Diffusion Language Modeling (FeF-DLLM)**，其核心思想是：

- **消除因子化误差**：  
  改变传统的独立 token 预测范式，转而采用**前缀条件化的 clean token 预测**（prefix-conditioned prediction）。即在预测第 $i$ 个 clean token 时，显式地以之前已恢复的 clean prefix 作为条件，从而保留 token 间的依赖结构，实现对真实后验分布的精确建模。

- **加速推理过程**：  
  引入 **speculative decoding** 到 diffusion denoising 过程中，在每个去噪步内使用一个快速的 draft model 并行生成候选 token 序列，并由 prefix-conditioned 的 target model 从左到右验证这些候选。这样既保持了目标分布的正确性，又大幅提升了推理效率。

---

### **相比现有方法的优势**
| 方面 | FeF-DLLM | 现有方法（如 LLaDA, SSD, DCD） |
|------|----------|-------------------------------|
| **生成质量** | ✅ 显著提升（平均 +5.04 pp） | ❌ 因子化误差导致性能下降 |
| **推理速度** | ✅ 平均 3.86× 加速 | ⚠️ 多数方法难以兼顾速度与精度 |
| **理论保证** | ✅ 可证明生成样本来自真实联合分布 | ⚠️ 多数仅提供启发式改进 |
| **架构兼容性** | ✅ 不改变 forward process 和 reverse transition | ✅ 易于集成到现有 DLLM 框架 |

---

## **2. 核心实验方法和设置**

### **使用的数据集**
训练数据包含约 72k 条 prompt-response 对，覆盖数学与代码任务。测试基准如下：
- **GSM8K**：小学数学应用题
- **MATH**：高难度数学问题
- **HumanEval**：Python 函数级代码生成
- **MBPP**：面向初学者的编程任务

所有评估均基于 **OpenCompass** 统一评测框架，确保可复现性。

---

### **实验设置与评估指标**

#### **模型架构**
- 主干模型：**LLaDA-Instruct**（基于 diffusion 的语言模型）
- FeF-DLLM 在其基础上进行微调，引入 prefix-conditioned 训练目标。

#### **训练细节**
- 优化器：AdamW（weight decay=0.1，lr=1e-5）
- Batch size：global 16（per-device 1，gradient accumulation over 2 steps）
- 精度：bf16 mixed precision
- 训练周期：1 epoch

#### **推理设置**
- **Speculative decoding window size**：默认 16
- **Draft & Target model**：均使用 fine-tuned FeF-DLLM 模型（共享权重）
- **Denoising steps**：测试 step=2 和 step=4 两种配置

#### **评估指标**
| 指标 | 含义 |
|------|------|
| **Accuracy** | 最终任务完成准确率（Pass@1） |
| **Speedup** | 相对于 LLaDA baseline 的 wall-clock 推理加速比（1× 为参考） |

---

### **基线方法对比**
| 方法 | 类型 | 特点 |
|------|------|------|
| **LLaDA [Nie et al., 2025]** | 原始 DLLM | 多 token 并行预测，存在 factorization error |
| **LLaDA/2** | 修改版 LLaDA | 每步解码两个 token，用于公平比较 |
| **SSD [Gao et al., 2025]** | Speculative decoding | 自回归式 speculative，牺牲部分非自回归特性 |
| **DCD [Liu et al., 2024]** | Copula-based correction | 引入额外模型结构，推理慢（~0.4× speed） |
| **DDOSP [Lavenant and Zanella, 2025]** | 动态调度 unmasking | 不改模型，但速度提升有限（~2×） |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据（Table 1）**

| 方法 | GSM8K Acc | MATH Acc | HumanEval Acc | MBPP Acc | **Mean Acc** | **Mean Speedup** |
|------|-----------|----------|----------------|-----------|---------------|------------------|
| LLaDA | 78.60 | 26.60 | 47.60 | 34.20 | 46.75 | 1.00× |
| LLaDA/2 | 76.42 | 25.46 | 32.32 | 35.00 | 42.30 | 1.98× |
| SSD | 77.10 | 34.94 | 43.09 | 39.20 | 48.58 | 2.09× |
| DCD | 78.24 | 26.36 | 50.00 | 37.60 | 48.05 | 0.43× |
| **FeF-DLLM (step=2)** | **79.38** | **36.40** | **48.78** | **42.60** | **51.79** | **3.86×** |
| **FeF-DLLM (step=4)** | **79.68** | **36.56** | **49.39** | **42.60** | **52.06** | **2.33×** |

> ✅ **平均提升 5.04 个百分点准确率，最高达 3.86× 推理加速**

---

### **与基线方法的关键对比**
- 相比 **LLaDA**：在几乎翻倍以上速度下，**全面超越各项任务精度**
- 相比 **SSD**：在 step=2 下仍高出 **3.21 个百分点 Accuracy**，且速度更快
- 相比 **DCD/DDOSP**：在精度相近或更高前提下，**推理速度快 5–9 倍以上**

---

### **消融实验结果**

#### **Ablation 1：训练的作用**
| 方法 | Mean Acc | Speed |
|------|---------|-------|
| FeF-DLLM w/o train | 50.15 | 3.92× |
| FeF-DLLM (full) | **51.79** | 3.86× |

➡️ 微调 + 新推理策略共同作用带来增益，单独使用原模型无法达到最优。

---

#### **Ablation 2：Speculative Decoding 的影响**
| 方法 | Mean Acc | Speed |
|------|---------|-------|
| FeF-DLLM w/o SD | 51.79 | 0.67× |
| FeF-DLLM (with SD) | 51.79 | **3.86×** |

➡️ speculative decoding 几乎无损精度，却带来 **5.7 倍以上的实际加速**（相对顺序解码）。

---

#### **Ablation 3：Draft Model 选择**
| Draft / Verify | Acceptance Rate | Speed |
|----------------|------------------|--------|
| FeF-DLLM / FeF-DLLM | ~63–93% | **2.14×–2.99×** |
| FeF-DLLM w/o train / FeF-DLLM | 略低 | 略慢 |

➡️ 使用相同高质量 draft model 能提高 acceptance rate，进而提升加速效果。

---

#### **Ablation 4：Speculative Window Size**
| Window Size | Mean Speed |
|------------|------------|
| 4 | 0.78× |
| 8 | 1.42× |
| 16 | **2.33×** |

➡️ 更大的 window size 显著提升速度，受限于 GPU 内存未测试更大值。

---

## **4. 关键结论和发现**

### **主要发现**
1. **因子化误差是限制 DLLM 性能的关键瓶颈**：简单增加并行度（如 LLaDA/2）会导致性能下降。
2. **Prefix-conditioned prediction 可彻底消除因子化误差**：理论上可恢复真实 joint 分布。
3. **Speculative decoding 是高效实现 prefix-conditioned 解码的理想机制**：在不牺牲分布正确性的前提下实现高度并行化。
4. **FeF-DLLM 实现了精度与效率的双重突破**：平均 +5.04% 准确率，最高 3.86× 推理加速。

---

### **方法的局限性**
- **计算资源需求更高**：由于引入 speculative decoding 和 prefix conditioning，每次推理需要更多内存和算力。
- **依赖高质量 draft model**：若 draft model 与 target model 差距大，acceptance rate 下降，加速效果减弱。
- **当前实现受设备限制**：最大 speculative window size 受限于 GPU 显存，未能探索更大窗口潜力。

---

### **未来工作方向**
- 设计更轻量化的 draft model 或蒸馏策略，降低部署成本。
- 探索动态调整 speculative window size 的机制。
- 将 FeF-DLLM 扩展至图像、音频等其他离散扩散建模范畴。
- 结合 classifier-free guidance 或 contrastive decoding 进一步提升生成质量。

--- 

> 📌 **总结一句话**：  
> **FeF-DLLM 通过 prefix-conditioned prediction 消除因子化误差，并借助 speculative decoding 实现高效推理，在数学与代码生成任务上实现了“既快又准”的突破性进展。**

</details>

---

### 16. [Uncertainty Quantification for Large Language Diffusion Models](https://arxiv.org/abs/2605.14570)

**Authors**: Artem Vazhentsev, Vladislav Smirnov, David Li, Maxim Panov, Timothy Baldwin, Artem Shelmanov  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.14570v1  

#### Abstract
Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism. Similar to autoregressive LLMs, they remain prone to hallucinations, making reliable uncertainty quantification (UQ) crucial for safe deployment. How...

---

### 17. [MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning](https://arxiv.org/abs/2605.14212)

**Authors**: Yaolun Zhang, Yujie Zhao, Nan Wang, Yiran Wu, Jiayu Chang, Yizhao Chen, Qingyun Wu, Jishen Zhao, Huazheng Wang  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14212v1  

#### Abstract
Automatic multi-agent systems aim to instantiate agent workflows without relying on manually designed or fixed orchestration. However, existing automatic MAS approaches remain only partially adaptive: they either perform training-free test-time search or optimize the meta-level designer while keepin...

---

### 18. [Agentic AI Ecosystems in Higher Education: A Perspective on AI Agents to Emerging Inclusive, Agentic Multi-Agent AI Framework for Learning, Teaching and Institutional Intelligence](https://arxiv.org/abs/2605.14266)

**Authors**: Vidya K Sudarshan, Anushka Sisodia, Reshma A Ramachandra, Sia Batra, Josephine Chong Leng Leng  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14266v1  

#### Abstract
Integration of artificial intelligent (AI) agents in higher education is transforming teaching, learning and administrative processes. Although existing AI agents effectively support individual tasks, their implementation remains fragmented and inefficient for handling the complexity of educational ...

---

### 19. [Prompt Segmentation and Annotation Optimisation: Controlling LLM Behaviour via Optimised Segment-Level Annotations](https://arxiv.org/abs/2605.14561)

**Authors**: Devika Prasad, Luke Gerschwitz, Tong Li, Henry Xiao, Anjin Liu, Coco Wu, Anna Leontjeva, Luiz Pizzato  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14561v1  

#### Abstract
Prompt engineering is crucial for effective interaction with generative artificial intelligence systems, yet existing optimisation methods often operate over an unstructured and vast prompt space, leading to high computational costs and potential distortions of the original intent. We introduce Prom...

---

### 20. [Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in Indian Judicial AI](https://arxiv.org/abs/2605.14665)

**Authors**: Joy Bose  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14665v1  

#### Abstract
Legal reasoning is not semantic similarity search. A court judgment encodes constrained symbolic reasoning: precedent propagation, procedural state transitions, and statute-bound inference. These are properties that vector-based retrieval-augmented generation (RAG) cannot faithfully represent. Hallu...

---

### 21. [Multi-objective application placement in fog computing using graph neural network-based reinforcement learning](https://arxiv.org/abs/2605.14649)

**Authors**: Isaac Lera, Carlos Guerrero  
**Category**: cs.DC  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14649v1  

#### Abstract
We propose a framework designed to tackle a multi-objective optimization challenge related to the placement of applications in fog computing, employing a deep reinforcement learning (DRL) approach. Unlike other optimization techniques, such as integer linear programming or genetic algorithms, DRL mo...

---

### 22. [A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures](https://arxiv.org/abs/2605.14489)

**Authors**: Sergio Vanegas, Lasse Lensu, Fredy Ruiz  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14489v1  

#### Abstract
Building black-box models for dynamical systems from data is a challenging problem in machine learning, especially when asymptotic stability guarantees are required. In this paper, we introduce a novel stability-ensuring and backpropagation-compatible projection scheme based on the Schur decompositi...

---

### 23. [GenAI for Energy-Efficient and Interference-Aware Compressed Sensing of GNSS Signals on a Google Edge TPU](https://arxiv.org/abs/2605.14839)

**Authors**: Thorben Wegner, Lucas Heublein, Tobias Feigl, Felix Ott, Christopher Mutschler, Alexander R\"ugamer  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14839v1  

#### Abstract
Traditional methods for classifying global navigation satellite system (GNSS) jamming signals typically involve post-processing raw or spectral data streams, requiring complex and costly data transmission to cloud-based interference classification systems. In contrast, our proposed approach efficien...

---

### 24. [Fast Adversarial Attacks with Gradient Prediction](https://arxiv.org/abs/2605.14868)

**Authors**: Kamil Ciosek, Aleksandr V. Petrov, Nicol\`o Felicioni, Konstantina Palla  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.14868v1  

#### Abstract
Generating adversarial examples at scale is a core primitive for robustness evaluation, adversarial training, and red-teaming, yet even "fast" attacks such as FGSM remain throughput-limited by the cost of a backward pass. We introduce a family of attacks that eliminates the backward pass by predicti...

---

### 25. [SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/abs/2605.14205)

**Authors**: Zahra Zanjani Foumani, Alberto Castelo, Shuang Xie, Ted Chaiwachirasak, Han Li, Lingyun Wang  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14205v1  

#### Abstract
LLM-based web agents can navigate live storefronts, yet they often collapse to a single "average buyer" policy, failing to capture the heterogeneous and distributional nature of real buyer populations. Existing personalization methods rely on hand-crafted prompt-based personas that are brittle, diff...

---

### 26. [BiFedKD: Bidirectional Federated Knowledge Distillation Framework for Non-IID and Long-Tailed ECG Monitoring](https://arxiv.org/abs/2605.14886)

**Authors**: Zixuan Shu, Tiancheng Cao, Hen-Wei Huang  
**Category**: cs.AI  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14886v1  

#### Abstract
Electrocardiogram (ECG) monitoring in Internet of Medical Things (IoMT) networks is constrained by strict data-sharing regulations and privacy concerns. Federated learning (FL) enables collaborative learning by keeping raw ECG data on devices, but frequent transmissions of high-dimensional model upd...

---

### 27. [Distribution Corrected Offline Data Distillation for Large Language Models](https://arxiv.org/abs/2605.14071)

**Authors**: Yumeng Zhang, Zhengbang Yang, Yevin Nikhel Goonatilake, Zhuangdi Zhu  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14071v1  

#### Abstract
Distilling reasoning traces from strong large language models into smaller ones is a promising route to improve intelligence in resource-constrained settings. Existing approaches face a fundamental trade-off: offline distillation from teacher-generated traces provides high-quality, sample-efficient ...

---

### 28. [Measuring and Mitigating Toxicity in Large Language Models: A Comprehensive Replication Study](https://arxiv.org/abs/2605.14087)

**Authors**: Mokshit Surana, Archit Rathod, Akshaj Satishkumar  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14087v1  

#### Abstract
Large Language Models (LLMs), when trained on web-scale corpora, inherently absorb toxic patterns from their training data. This leads to ``toxic degeneration'' where even innocuous prompts can trigger harmful outputs. This phenomenon poses significant risks for real-world deployments. Thus, necessi...

---

### 29. [Polar probe linearly decodes semantic structures from LLMs](https://arxiv.org/abs/2605.14125)

**Authors**: Pablo J. Diego-Sim\'on, Pierre Orhan, Yair Lakretz, Jean-R\'emi King  
**Category**: cs.CL  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14125v1  

#### Abstract
How do artificial neural networks bind concepts to form complex semantic structures? Here, we propose a simple neural code, whereby the existence and the type of relations between entities are represented by the distance and the direction between their embeddings, respectively. We test this hypothes...

---

### 30. [AIMing for Standardised Explainability Evaluation in GNNs: A Framework and Case Study on Graph Kernel Networks](https://arxiv.org/abs/2605.14884)

**Authors**: Magdalena Proszewska, N. Siddharth  
**Category**: cs.LG  
**Published**: 2026-05-15  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.14884v1  

#### Abstract
Graph Neural Networks (GNNs) have advanced significantly in handling graph-structured data, but a comprehensive framework for evaluating explainability remains lacking. Existing evaluation frameworks primarily involve post-hoc explanations, and operate in the setting where multiple methods generate ...

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
