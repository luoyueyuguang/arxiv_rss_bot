# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-06-01 10:45:28 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation](https://arxiv.org/abs/2605.30753)

**Authors**: Zekai Li, Ji Liu, Yiqing Huang, Ziqiong Liu, Dong Li, Emad Barsoum  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2605.30753v1  

#### Abstract
Diffusion-based large language models (dLLMs) support parallel text generation via iterative denoising, yet inference remains latency-heavy because many steps are spent on redundant refinement and repeated remasking of tokens whose final values are already determined. Prior acceleration methods main...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现有的 **diffusion-based large language models (dLLMs)** 虽然支持并行文本生成，但推理过程仍然存在高延迟问题。其主要原因在于：
- 大量去噪步骤被浪费在**已经收敛的 token 上**；
- 传统方法依赖于**step-local 启发式规则**（如固定置信度阈值）来决定是否“固定”某个 token，这类方法对提示词（prompt）、任务类型和位置敏感，容易导致过早提交（降低质量）或过度迭代（增加延迟）；
- 缺乏对 token 去噪轨迹（temporal trajectory）和空间位置（spatial position）的建模。

### 提出的新方法与新思路
本文提出了一种全新的 **trace-aware 解码框架**，将扩散解码视为一个**动态控制问题**，而非一系列独立的阈值判断。核心包括两个模块：

#### ✅ **Temporal-Spatial Parallel Decoding (TSPD)**
- 引入一个轻量级的时序-空间控制器（temporal-spatial controller），利用每个 token 的历史轨迹特征进行决策：
  - **Confidence**（置信度）
  - **Entropy**（熵）
  - **Momentum**（动量，即置信度变化趋势）
  - **Position**（相对位置信息）
- 使用共享的序列感知模型（如 LSTM）捕捉 token 的演化模式（如稳定上升、振荡、延迟收敛等），从而更鲁棒地识别何时可以安全地固定该 token。
- 采用 **STE (Straight-Through Estimator)** 实现离散决策训练，使模型直接学习“fix or continue”的二元动作。

#### ✅ **Confidence Extrapolation (CE)**
- 一种**无需训练、即插即用**的状态空间模块（state-space model），用于预测未来几步的置信度趋势及其不确定性。
- 将 confidence 视为带噪声观测的时间序列，使用类似 Kalman Filter 的机制进行外推。
- 引入**风险感知的前瞻机制（risk-aware horizon selection）**：仅当左上下文足够稳定且预测不确定性较低时才启用外推，避免激进提交。
- 可与任何现有控制器（如 TSPD、Learn2PD 或启发式规则）结合使用。

### 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| **可靠性更强** | 不再依赖单一时间步的局部统计量，而是综合历史轨迹和位置信息，显著提升跨任务、跨位置的泛化能力。 |
| **加速更主动** | CE 支持“前瞻性”提交，在置信度尚未达标但趋势明确时即可提前终止，减少被动等待。 |
| **兼容性强** | 方法完全正交于 KV caching 等系统优化，可叠加使用获得更大提速。 |
| **无训练开销** | CE 是 training-free 模块，TSPD 参数极少（仅约 2K），部署成本极低。 |

---

## 2. 核心实验方法和设置

### 使用的数据集
在多个代表性基准上进行了广泛评估，涵盖不同任务类型：
- **GSM8K**（5-shot）：数学应用题推理
- **MATH**（4-shot）：复杂数学问题求解
- **HumanEval**（0-shot）：代码生成能力
- **MBPP**（3-shot）：编程任务生成

此外还验证了方法在不同 dLLM 架构上的通用性：
- **LLaDA-8B-Instruct**（主实验）
- **Dream-7B**
- **LLaDA-MoE**

### 实验设置
- **生成长度**：256、512 和 1024 tokens
- **Block Size**：32
- **批大小**：1（batch size = 1）
- **解码方式**：greedy decoding（排除采样干扰）
- **评估指标**：
  - **Tokens Per Second (TPS)**：吞吐量
  - **Speedup**：相对于 vanilla dLLM 的加速比
  - **Accuracy**：任务特定准确率（如 GSM8K 准确率）

### 基线方法对比
| 方法 | 是否使用 KV Cache | 类型 |
|------|------------------|------|
| **Vanilla** | ❌ | 原始 dLLM |
| **Fast-dLLM** | ✅ | 启发式 + KV caching |
| **Credit Decoding (CD)** | ✅ | 启发式 + trace credit |
| **Prophet** | ❌ | 学习型控制器（threshold-based） |
| **Learn2PD** | ❌ | 学习型并行解码策略 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（以 LLaDA-8B-Instruct, 256 tokens 为例）

| 方法 | TPS | Speedup | Accuracy |
|------|-----|---------|----------|
| Vanilla | 6.9 | 1.0× | 79.3% |
| Fast-dLLM | 53.8 | 7.8× | 78.5% |
| Learn2PD | 29.0 | 4.2× | 79.1% |
| **Ours (no cache)** | **34.2** | **5.0×** | **79.4%** |
| **Ours (+KV cache)** | **77.3** | **11.2×** | **78.8%** |

> 💡 在 **GSM8K** 上实现 **11.2× 加速**，同时保持几乎不变的准确性。

### 不同模型上的表现（256 tokens）

| 模型 | 方法 | TPS | Speedup | Accuracy |
|------|------|-----|--------|----------|
| Dream-7B | Ours (+cache) | 69.2 | 7.6× | 75.0% |
| LLaDA-MoE | Ours (+cache) | 21.2 | 5.1× | 75.2% |

> 表明方法具有良好的架构通用性，适用于 MoE 等稀疏结构。

### 随生成长度增长的表现（LLaDA-8B-Instruct）

| 生成长度 | 方法 | TPS | Speedup | Accuracy |
|--------|------|-----|--------|----------|
| 512 | Ours (+cache) | 79.0 | 24.7× | 77.6% |
| 1024 | Ours (+cache) | **64.1** | **58.3×** | 78.5% |

> ⬆️ 加速比随生成长度增加而显著提升，说明冗余迭代在长输出中更为严重，本方法收益更大。

### 消融实验结果（GSM8K, 256 tokens）

| 方法 | TPS | Speedup | Accuracy |
|------|-----|--------|----------|
| **Full Model (TSPD + CE)** | **34.2** | **5.0×** | 79.4% |
| w/o TSPD | 20.0 | 2.9× | 79.1% |
| w/o CE | 30.3 | 4.4× | 79.5% |

> - TSPD 提供主要加速（从 2.9× 到 4.4×）
> - CE 进一步带来额外增益（+0.6× speedup）
> - 两者协同作用达到最佳效果

### 特征消融（TSPD 模块）

| 移除特征 | TPS | Speedup | Accuracy |
|--------|-----|--------|----------|
| None (完整) | 30.3 | 4.4× | 79.5% |
| w/o confidence | 19.3 | 2.8× | 78.8% |
| w/o entropy | 28.3 | 4.1× | 79.0% |
| w/o momentum | 29.7 | 4.3× | 79.2% |
| w/o position | 31.1 | 4.5× | **78.5%** |

> - **Confidence 是最关键信号**
> - **Position 虽轻微降低速度，但显著提升 accuracy**，防止后期 token 过早提交

### 与其他控制器结合 CE 的效果（GSM8K）

| 控制器 | +CE 后 TPS 提升 |
|-------|----------------|
| TSPD | 30.3 → 34.2 (+12.9%) |
| Learn2PD | 29.0 → 32.4 (+11.7%) |
| Fast-dLLM | 52.8 → 64.2 (+21.6%) |

> 🔁 **CE 具有通用性**，能为多种控制器提供一致加速，证明其作为 plug-in 模块的有效性。

---

## 4. 关键结论和发现

### 主要发现
1. **Token-wise 去噪轨迹蕴含丰富稳定性信息**：单步置信度不足以判断是否收敛，必须结合历史趋势（如单调上升 vs 振荡）才能可靠决策。
2. **位置效应显著**：靠右的 token 更晚收敛，统一阈值无法适配所有位置 —— 必须引入 spatial awareness。
3. **TSPD 显著优于 step-local 控制器**：通过建模 temporal dynamics 和 positional context，实现了更鲁棒、更高效的 token 固定策略。
4. **CE 实现“主动加速”**：通过状态空间模型预测未来 confidence，可在趋势明确时提前提交，突破被动等待瓶颈。
5. **方法高度兼容系统优化**：与 KV caching 完全正交，组合后可实现高达 **58.3× 的端到端加速**（1024 tokens）。

### 方法的局限性
- **依赖高质量轨迹数据训练 TSPD**：虽然参数少，但仍需收集多步中间状态作为监督信号。
- **CE 对极端非平稳轨迹预测不准**：若 confidence 曲线剧烈波动或突然反转，外推可能失效。
- **当前设计基于 greedy decoding**：未探索在采样（sampling）场景下的适用性。
- **仅在 block-level 并行中验证**：未扩展至任意顺序生成（arbitrary-order generation）场景。

### 未来工作方向
- 探索 **online adaptation** 机制，让控制器适应不同 domain 或 prompt 分布。
- 将 TSPD 与 reinforcement learning 结合，进一步优化长期奖励（如最终 accuracy + speed tradeoff）。
- 扩展至 **multimodal diffusion models** 和 **long-context generation** 场景。
- 设计更复杂的 state-space 或 SSM-based extrapolator 以处理非线性趋势。

---

> 📌 **总体评价**：  
> 本文提出了一个简洁而强大的 trace-aware 框架，从根本上改变了 dLLM 解码控制范式 —— 从“静态阈值判断”转向“动态轨迹感知”。TSPD 与 CE 的组合不仅带来了显著加速（最高达 **58.3×**），而且保持了生成质量，具备极强的实用价值和推广潜力。

</details>

---

### 2. [Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

**Authors**: Marko Kojic, Ivan Bondyrev, Aral de Moor, Joseph Shtok, Petr Borovlev, Kseniia Lysaniuk, Madeeswaran Kannan, Ivan Dolgov, Nikita Pavlichenko  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.31268v1  

#### Abstract
We present Mellum 2, an open-weight 12B-parameter Mixture-of-Experts (MoE) language model with 2.5B active parameters per token. Mellum 2 is a general-purpose language model specialized in software engineering, spanning code generation and editing, debugging, multi-step reasoning, tool use and funct...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# MELLUM 2 Technical Report 核心总结

## 1. 论文的主要贡献和创新点

### 解决的问题
MELLUM 2 旨在解决**代码大模型在高质量能力与部署成本之间的权衡难题**。当前开源 LLM 领域存在两个极端：
- **Dense 模型**（如 4–14B 参数）：推理成本低，但在复杂编码、数学推理等任务上表现有限；
- **大规模 MoE 模型**：质量接近前沿水平，但部署开销巨大，难以在消费级硬件上运行。

MELLUM 2 的目标是构建一个兼具**强大软件工程能力**和**高效推理性能**的开放权重模型，特别适用于集成开发环境（IDE）中的实时辅助场景。

---

### 提出的新方法与架构设计
MELLUM 2 是一个 **12B 总参数、每 token 激活约 2.5B 参数的 Mixture-of-Experts (MoE)** 架构语言模型，专为软件工程任务优化。其核心创新在于一系列以“效率感知”为导向的架构选择：

#### ✅ 主要技术贡献：
1. **效率驱动的 MoE 架构设计**
   - 采用 **64 个专家中激活 8 个**（Top-8 Routing），在保证模型容量的同时控制计算量。
   - 经过系统性消融实验验证，在单张 H100 上可实现与 Qwen2.5-7B 相当甚至更优的吞吐量。

2. **Grouped-Query Attention (GQA) 优化**
   - 使用仅 **4 个 KV 头**（而非标准的 8 或更多），显著降低高并发下的 KV Cache 占用，提升吞吐性能。

3. **Sliding Window Attention (SWA) 分层应用**
   - 在 **每 4 层中有 3 层启用滑动窗口注意力（窗口大小 1,024）**，保留部分全注意力层以维持长程依赖建模能力。
   - 显著减少长序列推理延迟，同时保持上下文理解能力。

4. **Multi-Token Prediction (MTP) 辅助头**
   - 引入一个额外的 MTP 头，用于预测下一个 token 之后的一个 token。
   - 该头作为**训练阶段的辅助目标**，并在推理时移除，可用于 **speculative decoding** 加速生成过程。
   - 实验表明 MTP 能带来显著的质量提升而训练开销仅增加 7%。

5. **双发布变体：Instruct 与 Thinking**
   - 基于同一基础模型，通过不同后训练策略发布两种版本：
     - **Instruct 模型**：直接输出答案；
     - **Thinking 模型**：先输出显式的推理链（reasoning trace），再给出最终答案。

6. **Layer-Selective YaRN 扩展上下文至 128K**
   - 利用 **YaRN 方法**将原生 8K 上下文扩展到 **131,072 tokens（128K）**。
   - 仅对使用全注意力的层进行频率重映射，避免扰动已适配局部窗口的 SWA 层，效果优于全局调整。

7. **高效的训练配方（Training Recipe）**
   - 使用 **Muon 优化器 + FP8 混合精度训练**，结合 **Warmup-Hold-Decay 学习率调度**。
   - 支持在大规模 MoE 场景下的稳定训练，并报告了完整的超参配置。

---

### 相比现有方法的优势
| 特性 | MELLUM 2 | 典型 Dense 模型（如 Qwen2.5-7B） | 大规模 MoE 模型 |
|------|----------|-------------------------------|----------------|
| 每 token 激活参数 | ~2.5B | ~7B | >5B |
| 推理速度（H100） | 吞吐高出 21% | 中等 | 通常较慢 |
| 上下文长度 | 128K（扩展后） | 通常 ≤32K | 可达 128K |
| 功能完整性 | 支持工具调用、函数调用、代理编程 | 一般支持 | 支持 |
| 开放程度 | 完全开放权重 + 训练细节 | 多数开放 | 部分闭源 |
| IDE 友好性 | 设计初衷即为此 | 有尝试 | 不适合 |

> 💡 **优势总结**：MELLUM 2 成功实现了“**小激活参数 + 高质量输出 + 快速推理 + 长上下文 + 开放生态**”的统一，填补了中小型 MoE 编码模型的空白。

---

## 2. 核心实验方法和设置

### 数据集构成
预训练共使用约 **10.6 万亿 tokens**，分为三个阶段的课程学习（Curriculum Learning）：

| 阶段 | Token 数量 | Web (%) | Code (%) | Math (%) | 特点 |
|------|------------|--------|---------|---------|------|
| Phase 1: Foundation | 6.18T | 70% | 23% | 6% | 广泛语言与基础代码理解 |
| Phase 2: Quality Uplift | 2.79T | 44% | 42% | 14% | 引入高质量 SFT、推理、STEM 数据 |
| Phase 3: Capability Sharpening | 1.69T | 23% | 59% | 18% | 进一步强化代码与数学能力 |

#### 数据来源分类：
- **Source Code**：来自公共仓库的许可代码文件、Common Crawl 抽取代码、合成代码数据集（含摘要、测试生成、跨语言翻译等）。
- **Web & General Knowledge**：基于 Common Crawl 的合成网页语料、教育内容、维基改写、百科文章。
- **Mathematical Content**：数学教材、SFT 数学指令数据、多层级数学问答。

此外还引入了 **Fill-in-the-Middle (FIM)** 目标，尤其在代码相关阶段增强编辑能力。

---

### 实验设置与评估指标

#### 模型架构关键参数（见 Table 2）
| 参数 | 值 |
|------|----|
| 总参数量 | ~12B |
| 激活参数量/Token | ~2.5B |
| 专家总数/活跃数 | 64 / 8 |
| 注意力头数 | 32 Query Heads, 4 KV Heads (GQA) |
| FFN 类型 | SiLU-gated MLP |
| 归一化 | RMSNorm |
| 位置编码 | RoPE (θ=500,000) |
| 上下文长度 | 原始 8,192 → 扩展至 131,072 |
| MTP Head | 1 层，损失权重 α=0.1 |

#### 训练基础设施
- **硬件**：32 节点 × 8 H200 GPU
- **并行策略**：Expert Parallelism=8，TP=1，PP=1
- **优化器**：Distributed Muon（Moonlight 设置，extra scale factor=0.2）
- **精度**：BF16 + FP8 混合精度（tensorwise, most-recent amax）
- **批处理大小**：从 2,048 序列逐步增长至 4,096 序列（~33.6M tokens/step）

#### 评估基准与指标
涵盖五大类任务：

| 类别 | 基准 | 主要指标 |
|------|------|---------|
| **代码生成** | HumanEval+, MBPP+, LiveCodeBench v6, MultiPL-E | pass@1, score |
| **数学与推理** | GSM8K, MATH, AIME, GPQA | Exact Match, Accuracy |
| **工具使用** | BFCL v3/v4 | Macro-average accuracy |
| **通用知识** | MMLU, MMLU-Pro, TruthfulQA | Accuracy |
| **安全性** | HarmBench, XSTest | Harmful rate ↓, Safe compliance ↑ |
| **对话能力** | IFEval, MixEval, JetBrains 内部成对胜率 | Strict accuracy, Win rate |

所有模型均在 **greedy decoding** 下评估（除 BFCL 和 LiveCodeBench 使用轻微采样外）。

---

### 基线对比模型
- **Instruct 对比组**：
  - Qwen3.5-4B, Qwen3.5-9B
  - OLMo-3-7B
  - Ministral-3-14B
  - Seed-Coder-8B
- **Thinking 对比组**：
  - Qwen3.5-4B-Thinking, Qwen3.5-9B-Thinking
  - OLMo-3-7B-Thinking
  - Ministral-3-14B-Thinking

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总（Post-Training）

#### 表格 9 & 10 关键指标摘录（单位：%）

| 指标 | MELLUM 2 (RL, Instruct) | 最佳基线 | 结果比较 |
|------|--------------------------|----------|-----------|
| **EvalPlus**（HumanEval+/MBPP+平均） | **78.4** | Qwen3.5-9B: 71.8 | ✅ 显著领先 |
| **LiveCodeBench v6**（Instruct） | 37.2 | Qwen3.5-9B: 63.7 | ❌ 落后 |
| **LiveCodeBench v6**（Thinking） | **69.9 (SFT), 75.1 (SFT)** | Qwen3.5-9B-Thinking: 68.3 | ✅ SFT 已领先 |
| **BFCL v3**（Function Calling） | **66.3 (Instruct), 69.4 (Thinking)** | Qwen3.5-9B-Thinking: 68.5 | ✅ 超越 |
| **BFCL v4**（Agent Tools） | **45.6 (Thinking)** | Qwen3.5-9B-Thinking: 42.7 | ✅ 领先 |
| **AIME**（数学竞赛题） | 41.7 (Instruct), **58.4 (Thinking)** | Qwen3.5-9B-Thinking: 73.4 | ⚠️ 接近但仍有差距 |
| **GSM-Plus**（数学综合） | 80.5 (Instruct), **87.0 (Thinking)** | Qwen3.5-9B-Thinking: 90.7 | ⚠️ 接近 |
| **MMLU-Redux**（通识知识） | 78.1 | Qwen3.5-9B: 91.1 | ❌ 明显落后 |
| **GPQA Diamond**（研究生级科学问答） | 40.9 (Instruct), **57.6 (Thinking)** | Qwen3.5-9B: 81.3 | ❌ 差距较大 |
| **IFEval**（指令遵循） | 75.8 | Qwen3.5-9B: 83.9 | ❌ 落后 |
| **JetBrains Pairwise Win Rate** | **68.1 (Instruct), 69.5 (Thinking)** | Qwen3.5-9B-Thinking: 56.7 | ✅ 显著领先 |
| **HarmBench**（有害性） | 23.1↑ | Ministral-3-14B: 56.5 | ❌ RL 后上升（alignment tax） |
| **XSTest**（安全合规） | 81.2 | Qwen3.5-9B: 97.6 | ❌ 略低 |

---

### 消融实验结果（Ablation Studies）

#### （1）MTP 头的影响（Table 1）
在 14B MoE 模型上训练 105B tokens 的消融显示：
| 基准 | Baseline | +MTP | Δ |
|------|--------|-------|----|
| HumanEval+ | 18.29 | 26.22 | **+7.93** |
| MMLU | 37.49 | 41.06 | +3.57 |
| MMLU-Pro | 19.07 | 22.32 | +3.25 |
| GSM8K | 30.63 | 33.59 | +2.96 |
| BBH | 35.00 | 37.74 | +2.74 |

✅ **结论**：MTP 显著提升多项任务性能，且不损害主任务目标。

#### （2）KV Heads 数量影响（Fig. 2）
- **4 KV Heads** 是最佳平衡点：
  - 少于 4 → 质量下降明显；
  - 多于 4 → KV Cache 占用剧增，严重影响吞吐。

#### （3）专家数量与激活数（Fig. 1）
- **64 专家 × 8 激活** 提供最优性价比。
- 更少激活（如 2）虽快但质量差；更多总参数（>15B）仍可在相同延迟预算内实现。

#### （4）Sliding Window 效果（Fig. 3）
- 使用 **3:1 SWA 模式 + 1,024 窗口**，相比无 SWA 模型大幅降低长输入延迟。
- 在 16K 输入下，MELLUM 2 延迟仅为 Qwen2.5-7B 的 ~70%，吞吐更高。

#### （5）Optimizer 对比（Fig. 4）
- **Muon (Moonlight config)** 在 Dense 和 MoE 架构上均优于 AdamW，收敛更快、最终 loss 更低。
- 特别是在 MoE 场景下稳定性更好。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **MoE 架构可在极低激活参数下媲美更大 Dense 模型的表现**  
   MELLUM 2 仅激活 2.5B 参数，却能在多个推理与编码任务上超越 7B–14B 的 Dense 模型。

2. ✅ **效率导向的设计能显著提升实际部署性能**  
   GQA（4 KV heads）、SWA（3:1）、MTP 等组合使 MELLUM 2 在单 H100 上达到 **5,179 output tokens/s**，比 Qwen2.5-7B 高出 **21% 吞吐**。

3. ✅ **Thinking 模型在算法与数学任务上潜力巨大**  
   尽管 SFT 阶段表现平平，但经过 RL 微调后，Thinking 模型在 AIME 和 LiveCodeBench 上反超多数基线，说明“显式思维”机制有效释放了模型潜能。

4. ✅ **领域对齐的数据设计带来特定优势**  
   在 JetBrains 内部成对评测中，MELLUM 2 获得最高胜率（69.5%），表明其在真实 IDE 场景中具备更强实用性。

5. ⚠️ **广义知识仍是短板**  
   MMLU 和 GPQA 表现明显弱于 Qwen3.5 系列，反映出训练数据偏向代码与工程任务，牺牲了通用知识覆盖。

6. ⚠️ **RL 阶段带来 alignment tax**  
   RLVR 训练提升了功能性能，但也导致 HarmBench 有害性上升（从 8.4 → 23.1），说明偏好优化可能削弱拒绝行为。

---

### 方法的局限性
| 局限 | 描述 |
|------|------|
| **通用知识不足** | 训练数据高度聚焦代码与数学，导致在非技术领域的问答能力受限。 |
| **RL 导致安全性退化** | Reinforcement Learning 阶段放松了拒绝策略，需后续加强 alignment 控制。 |
| **Thinking 模型终止不稳定** | 虽未出现在自身模型中，但在评测其他 Thinking 模型时发现无限推理问题，提示需合理设置 reasoning budget。 |
| **缺乏视觉或多模态支持** | 当前为纯文本模型，无法处理图像或 UI 界面相关内容。 |

---

### 未来工作方向
1. **深化 SWE Agent 训练**  
   直接在仓库级软件工程任务上进行 RL 训练，推动向小型自主编程代理发展。

2. **扩大 RL 基础设施与环境覆盖**  
   构建更丰富的可验证奖励环境，支持更复杂的交互式任务。

3. **重新审视长上下文训练混合策略**  
   当前未能复现 OLMo 3 的 Longmino 数据增益，未来需探索更适合长上下文微调的数据配方。

4. **探索下一代混合架构（如 Mamba/MoE）**  
   当前因推理引擎成熟度放弃 Gated DeltaNet 等结构，未来将随生态完善重新评估。

5. **发布更大规模的 inference-aware Mellum 模型**  
   当前成功验证了“固定推理预算下最大化能力”的设计范式，可扩展至更大模型。

---

### 总结
MELLUM 2 是一款**面向生产部署、效率优先、能力全面的开源 MoE 编码助手模型**。它不仅在架构设计、训练配方、上下文扩展等方面提供了详尽的技术路线图，而且通过严格的消融与对比实验证明了其有效性。虽然在通用知识方面有所妥协，但在其目标领域——**代码生成、调试、工具调用与代理编程**——表现出色，是目前最适合嵌入 IDE 的开放模型之一。

> 📦 **开源承诺**：作者已将 Base、Instruct、Thinking 检查点及完整训练报告在 **Apache 2.0** 协议下公开，极大促进了社区复现与迭代。

</details>

---

### 3. [CoMem: Context Management with A Decoupled Long-Context Model](https://arxiv.org/abs/2605.30842)

**Authors**: Yuwei Zhang, Chengyu Dong, Shuowei Jin, Changlong Yu, Hejie Cui, Hongye Jin, Xinyang Zhang, Hamed Bonab, Colin Lockard, Jianshu Chen, Zhenyu Shi, Jingbo Shang, Xian Li, Bing Yin  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 12.0  
**Type**: new  
**ArXiv ID**: 2605.30842v1  

#### Abstract
Context management enables agentic models to solve long-horizon tasks through iterative summarization of previous interaction histories. However, this process typically incurs substantial decoding overhead for the extra summarization tokens, which significantly affect the end-to-end response latency...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# CoMEM: Context Management with A Decoupled Long-Context Model — 核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

在 **Long-Horizon Agentic Tasks**（如软件工程、科学探索）中，LLM Agent 需要处理极长的交互历史（可达数万甚至数十万 tokens）。然而，随着上下文增长，**KV Cache** 的内存占用和注意力计算开销呈线性甚至超线性增长，导致 **Decoding 阶段成为内存瓶颈（memory-bound）**，显著增加端到端响应延迟，限制系统吞吐。

现有方法存在以下不足：
- **Sliding Window / RAG**：丢失远距离依赖（如初始目标或早期诊断），影响推理连贯性。
- **Sparse Attention / KV Cache Quantization**：虽优化计算效率，但仍需对完整历史进行重复处理，无法根本解决冗余。
- **统一模型同时负责推理与记忆压缩**：大模型承担双重负担，难以并行化。

---

### ✅ 提出的新方法与创新思路

论文提出 **CoMEM**（**Co**ntext **M**anagement with a **d**ecoupled long-context model），其核心思想是：

> **将记忆管理（memory management）从主 Agent 推理流程中解耦，通过一个轻量级、专用的“Memory Model”异步执行历史压缩，从而实现并行化，掩盖上下文处理延迟。**

#### 主要创新点：

1. **Decoupled 架构设计**
   - **Agent Model**：大而强的推理模型，专注于决策生成。
   - **Memory Model**：小而快的长上下文模型（如 Qwen3-4B），专门负责将历史压缩为短摘要 `s_t`。
   - 二者职责分离，可独立优化。

2. **k-step-off 异步流水线（Asynchronous Pipeline）**
   - Memory Model 滞后 `k` 步更新摘要。
   - Agent 在等待新摘要时，使用旧摘要 + 最近 `k` 步原始交互作为输入继续推理。
   - 新摘要完成后，在下一个周期开始前触发一次 **uncached prefill**，其余步骤复用缓存。
   - 实现了 **Memory Compression 与 Agent Inference 的时间重叠**，有效“掩码”（mask）了压缩延迟。

3. **Reward-Driven 对齐训练（Functional Equivalence Reward）**
   - 不追求摘要的语言质量，而是训练 Memory Model 保留对 Agent 决策至关重要的 **Sufficient Statistics**。
   - 使用 **GRPO**（Group Relative Policy Optimization）框架，奖励函数定义为：
     $$
     R(s) = \text{sim}(a_{\text{pred}}, a^*)
     $$
     其中 $a^*$ 是全上下文 Agent 的真实动作，$a_{\text{pred}}$ 是基于摘要生成的动作。
   - 训练完全离线，无需在线环境交互，高效且可扩展。

4. **理论分析支持压缩比边界**
   - 推导出保证净加速的 **最大允许压缩比**：
     $$
     \frac{L_{\text{sum}}}{L_{\text{full}}} < \frac{1}{1 + \frac{W}{Y \cdot S' \cdot P}}
     $$
     表明只要摘要足够短，即可抵消预填充开销。

---

### ✅ 相比现有方法的优势

| 维度 | CoMEM | 传统方法 |
|------|-------|----------|
| **延迟控制** | 通过异步流水线将压缩延迟移出关键路径 | 压缩与推理串行，延迟叠加 |
| **性能保持** | Reward-driven 训练确保摘要保留决策关键信息 | 通用摘要易丢失程序逻辑依赖 |
| **系统灵活性** | 可独立优化 Agent 和 Memory 模型 | 单一模型难以兼顾推理能力与压缩效率 |
| **可扩展性** | 单个 Memory Server 可服务数百并发 Agent | 每个 Agent 自带压缩模块，资源浪费 |

---

## 2. 核心实验方法和设置

### ✅ 数据集

- **SWE-Bench-Verified**（主要评测集）
  - 包含 500 个人工验证的 GitHub issue，用于评估自主代码修复能力。
  - 任务复杂、上下文长，适合测试长期记忆管理。
- **BrowseComp-EN**（泛化性测试）
  - 多步网页搜索与信息提取任务，测试非代码场景下的通用性。

---

### ✅ 实验设置

| 项目 | 设置 |
|------|------|
| **Agent Models** | DeepSWE (32B), Qwen3-Coder-Max (480B), GLM-4.7 (355B) |
| **Memory Model** | Qwen3-4B（基础版、SFT 微调版、GRPO 训练版） |
| **k 值设置** | DeepSWE & Qwen3-Coder-Max: `k=2`；GLM-4.7: `k=4` |
| **摘要长度上限** | 2048 tokens |
| **推理引擎** | vLLM 0.14.0，启用 Prefix Caching 和 Chunked Prefilling |
| **硬件配置** | A100 (80GB) 或 H200 GPU |
| **批大小** | 128 issues/batch 用于测延迟 |

---

### ✅ 评估指标

| 指标 | 含义 |
|------|------|
| `%Resolved` | 成功解决的问题比例（核心效果指标） |
| `Latency (×128/s)` | 处理 128 个 issue 的总推理时间（核心效率指标） |
| `Speedup` | 相对于 Full-Context 基线的加速比 |
| `#Tool Calls` | 平均工具调用次数，反映推理效率 |
| `KV Cache Utilization` | GPU 显存占用情况 |

---

### ✅ 基线方法对比

| 基线 | 描述 |
|------|------|
| **Full-Context** | 标准长上下文推理，不压缩历史 |
| **No Summary** | 移除摘要，仅保留最近交互 |
| **Qwen3-4B (base)** | 使用未微调的小模型直接生成摘要 |
| **Qwen3-4B (SFT)** | 经过监督微调的摘要模型 |
| **GRPOAC** | 本文提出的 Reward-Driven 训练版本 |
| **MemAgent (7B)** | 外部通用记忆压缩模型（Yu et al., 2025）作为对照 |

---

## 3. 主要实验结果和性能指标

### ✅ 关键性能数据（来自 Table 1）

| Agent | Memory | %Resolved | Latency (w/ CPU Offload) | Speedup |
|-------|--------|-----------|--------------------------|---------|
| GLM-4.7 | Full-Context | 69.0 | 5869.42s | 1.00× |
| GLM-4.7 | GRPOAC (CoMEM) | **62.7** | **2821.38s** | **2.08×** |
| Qwen3-Coder-Max | Full-Context | 57.2 | 5129.90s | 1.00× |
| Qwen3-Coder-Max | GRPOAC (CoMEM) | **51.0** | **3594.51s** | **1.43×** |
| DeepSWE | Full-Context | 40.4 | 6390.62s | 1.00× |
| DeepSWE | GRPOAC (CoMEM) | **41.0** | **4400.89s** | **1.45×** |

> 📌 **结论**：CoMEM 在保持接近甚至略优于 Full-Context 性能的同时，实现了 **1.43× ~ 2.08× 的端到端加速**。

---

### ✅ 与基线方法对比

- **相比 Off-the-Shelf/SFT 摘要模型**：
  - GRPOAC 显著提升 %Resolved（如 GLM-4.7 上从 58.3 → 62.7），说明 **任务对齐训练至关重要**。
- **相比 MemAgent (7B)**（Table 5）：
  - CoMEM 在 GLM-4.7 上 **高出 7.9% 分辨率**，且速度更快（2.08× vs 1.80×）。
  - 表明 **专为下游 Agent 决策对齐的记忆模型优于通用压缩模型**。

---

### ✅ 消融实验结果

#### 🔹 敏感性分析（k 值选择）—— Table 4

| k | %Resolved | Speedup |
|----|-----------|---------|
| 1 | 57.2 | 1.53× |
| 2 | **64.2** | 2.07× |
| 4 (default) | 62.7 | **2.08×** |
| 8 | 62.4 | 2.07× |
| 16 | 60.2 | 1.64× |

> ✅ 最佳平衡点在 `k ∈ {2,4,8}`，太小（k=1）导致频繁 uncached prefill；太大（k=16）引入调度开销。

#### 🔹 批大小扩展性 —— Figure 5

- 当 batch size 从 32 增加到 256：
  - Full-Context 延迟从 1206ms → 9684ms（恶化严重）
  - CoMEM 实现 **2.52× 加速**（batch=256）
> ✅ CoMEM 的优势在高并发下更加明显，有效缓解内存带宽瓶颈。

#### 🔹 跨 Scaffold 泛化性 —— Appendix G

- 在 R2E-Gym 上训练的 Memory Model 迁移到 OpenHands Scaffold：
  - %Resolved 仅下降 0.3%（62.7 → 62.4）
> ✅ 表明模型学习的是任务相关语义，而非绑定特定工具模板。

#### 🔹 跨 Backbone 泛化性 —— Appendix I

- 在 Qwen3-Coder-Max 上训练的 Memory Model 直接用于 GLM-4.7：
  - %Resolved 为 61.9%，接近专用训练的 62.7%
> ✅ 支持构建通用 Memory Service 的可行性。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Decoupling + Asynchrony 是解决长上下文延迟的有效范式**  
   将 Memory Management 从 Agent 推理路径中剥离，并通过 k-step-off 流水线实现并行，可显著降低端到端延迟。

2. **Functional Equivalence Reward 比语言质量更重要**  
   摘要不需要“写得好”，只需要能让 Agent 做出和全上下文一致的决策。这种对齐训练方式比 SFT 更有效。

3. **CoMEM 的加速效果随系统负载增强**  
   在高并发、大批量场景下，KV Cache 压力加剧，CoMEM 的优势愈发突出（最高达 **4.95× 峰值单步加速**）。

4. **摘要可以提升性能而不仅是压缩**  
   在 BrowseComp-EN 上，CoMEM 实现 **32.0% 准确率**，超过 Full-Context 的 28.1%，表明结构化摘要有助于过滤噪声、聚焦关键信息。

5. **长期程序依赖被有效保留**  
   案例分析显示，即使经过数十步交互，关键诊断信息（如 `contains_over_clause=True`）仍保留在摘要中，证明 Sufficiency 学习成功。

---

### ⚠️ 局限性

1. **需要额外部署 Memory Model Server**  
   增加系统复杂度，但在大规模部署中可通过共享服务摊薄成本。

2. **k-step-off 引入摘要滞后（staleness）**  
   虽然实验证明容忍度高，但在极端动态环境中可能影响决策。

3. **当前训练依赖高质量参考轨迹**  
   需要 Full-Context Agent 生成的 $a^*$ 作为监督信号，限制了在无强基线场景的应用。

4. **Uncached Prefill 仍是潜在瓶颈**  
   尽管被分摊，但每次摘要更新仍需一次完整 re-encoding，未来可结合 Sparse Attention 进一步优化。

---

### 🔮 未来工作方向

1. **动态调整 k 值**  
   根据上下文变化程度自适应选择更新频率。

2. **联合优化 Memory + Agent 架构**  
   设计更紧凑的 Memory Model 或引入 MoE 结构。

3. **与 Sparse Attention / KV Cache Eviction 结合**  
   如让 Memory Model 使用 H2O 或 StreamingLLM 技术进一步提速。

4. **开放 Memory Model API**  
   构建标准化的“Memory-as-a-Service”平台，供多种 Agent 共享。

5. **探索无监督/弱监督对齐机制**  
   减少对 Full-Context Reference 的依赖。

---

> 💡 **总体评价**：  
> CoMEM 提出了一种**系统级创新**而非单纯算法改进，通过架构解耦和异步流水线，在不牺牲性能的前提下实现显著加速。其实验充分、分析深入，代表了 Long-Horizon Agent 高效部署的一个重要方向。

</details>

---

### 4. [Speculative Pipeline Decoding: Higher-Accruacy and Zero-Bubble Speculation via Pipeline Parallelism](https://arxiv.org/abs/2605.30852)

**Authors**: Yijiong Yu, Huazheng Wang, Shuai Yuan, Ruilong Ren, Ji Pei  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.30852v1  

#### Abstract
Speculative Decoding (SD) accelerates low-concurrency LLM inference by employing a draft-then-verify paradigm. However, mainstream methods typically rely on multi-token prediction, which introduces escalating prediction difficulty and serial drafting latency. To address these, we propose Speculative...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Speculative Pipeline Decoding: Higher-Accuracy and Zero-Bubble Speculation via Pipeline Parallelism*

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题

现有的 **Speculative Decoding (SD)** 方法在加速大语言模型（LLM）推理时面临两个根本性瓶颈：

1. **Compounding Prediction Difficulty（预测难度累积）**  
   多token预测范式中，随着预测步数增加，draft模块依赖自身浅层且未经验证的隐藏状态，导致与目标模型真实分布的偏差迅速扩大（Out-of-Distribution, OOD），后期token接受率急剧下降。

2. **Latency Overhead and Mutual Waiting（延迟开销与相互等待）**  
   传统方法中，draft生成是串行的，必须等draft完成才能启动target模型验证，造成GPU空转；即使并行化（如P-EAGLE），也会引入训练复杂度上升或精度损失。

此外，**PPSD** 虽然尝试利用pipeline parallelism，但其speculation仅基于第一阶段浅层特征，准确率低，且仍串行执行，无法扩展到深层网络。

---

### 提出了什么新方法或新思路

本文提出 **Speculative Pipeline Decoding (SPD)** ——一种全新的 speculative decoding 范式，核心思想是将传统的“多token预测”转变为“基于pipeline并行的单token推测”。

#### 核心创新点：

- ✅ **Multi-Depth Feature Aggregation（多深度特征聚合）**  
  Speculation Module 动态聚合当前pipeline中所有token在不同处理深度下的中间隐藏状态（从embedding到已计算的最深layer），形成更丰富、对齐的目标模型上下文表示。  
  - 数学上保证最大信息缺失被限制在常数 `n`（pipeline stage数），避免误差随长度无界累积。
  - 支持在训练时模拟warm-up和steady-state的不同特征布局，提升泛化能力。

- ✅ **Simultaneous Execution Schedule（同步执行调度）**  
  将Speculation Module的执行窗口前移，在pipeline step开始前就基于输入状态进行推测，实现与target model pipeline step 完全并行执行。
  - 只要Speculation Module的延迟 ≤ 单个pipeline stage时间（即层数 ≤ L/n），其计算可被完全掩盖（latency masking）。
  - 允许使用更深的Transformer结构作为Speculation Module，显著提升预测准确性而不增加端到端延迟。

---

### 相比现有方法的优势

| 维度 | SPD | EAGLE-3 | PPSD |
|------|-----|---------|-------|
| 预测范式 | 单token + pipeline并行 | 多token autoregressive预测 | 单token但浅层早退 |
| 特征来源 | 多深度中间状态聚合 | 多层融合但自回归预测 | 仅第一stage浅层输出 |
| 执行方式 | 并行（zero bubble） | 串行draft → 并行verify | 串行（speculate after pipeline） |
| 可扩展性 | 支持更多stage和更深speculation网络 | draft length受限于OOD | stage增多反而降低性能 |
| 接受率稳定性 | 更高，尤其在high-temperature采样下 | 在T=1时明显下降 | 始终较低 |

> SPD 实现了 **bounded prediction error** 和 **zero-latency speculation** 的统一，突破了传统SD的结构性瓶颈。

---

## 2. 核心实验方法和设置

### 使用的数据集

- **ShareGPT-70k**, **UltraChat-200k**, **SmolTalk**, **SmolTalk-Chinese**  
  混合共约120万样本，最大序列长度为2048，用于训练Speculation Module。

- **评估基准（Evaluation Benchmarks）**：
  - **MT-Bench**：多轮对话任务，高熵输出
  - **GSM8K**：数学推理，中等确定性
  - **HumanEval**：代码生成，高度确定性

---

### 实验设置

- **模型**：Qwen3.5-4B 和 Qwen3.5-9B（均为 L=32 层）
- **推理配置**：
  - 最大生成长度：512
  - 温度设置：T=0（greedy decoding），T=1（random sampling, top-k=50, top-p=1.0）
- **Draft Tree支持**：W=1（标准路径）、W=4（保留top4分支）

---

### 评估指标

由于当前实现基于原生PyTorch，未做底层优化（如Triton kernel、continuous batching），直接测量wall-clock time会失真。因此采用以下理论指标：

#### 🔹 Equivalent Acceptance Length ($L_{\text{acc}}$)

定义为：
$$
L_{\text{acc}} = \frac{N}{K} \cdot n
$$
其中：
- $N$: 总生成token数
- $K$: 实际pipeline forward步数
- $n$: pipeline stage数量

该指标严格反映了**理论加速上限**，且对于SPD而言，其理论速度提升 $S_{\text{spd}} = L_{\text{acc}}$。

#### 对比基线的速度提升公式：

- **EAGLE-3**: $ S_{\text{eagle}} = \frac{L_{\text{acc}} \cdot L}{L_s \cdot m + L} $
- **PPSD**: $ S_{\text{ppsd}} = \frac{L_{\text{acc}} \cdot L}{L_s \cdot n + L} $

> 可见EAGLE和PPSD的速度均受到draft overhead（$L_s$）的制约，而SPD无此限制。

---

### 基线方法对比

| 方法 | 类型 | Speculation Layers ($L_s$) | Draft Steps / Stages |
|------|------|-----------------------------|------------------------|
| **EAGLE-3** | Multi-token drafting | 1 | m=3,7,15 → 实际验证n=4,8,16 |
| **PPSD** | Early-exit self-speculative | 1 | n=4,8,16 stages |
| **Ours (SPD)** | Pipeline speculation | 1,2,4 | n=4,8,16 stages |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自Table 1）

#### 在 Qwen3.5-4B 上（平均三个benchmark）：

| Method | T=0, W=1 | T=1, W=1 | T=0, W=4 | T=1, W=4 |
|--------|----------|----------|----------|----------|
| EAGLE-3 (m=15) | 3.51/**2.39** | 2.65/**1.80** | 4.90/**3.33** | 3.58/**2.44** |
| PPSD (n=16) | 1.93/**1.29** | 1.65/**1.10** | 1.77/**1.18** | 2.02/**1.35** |
| **SPD (n=16, Ls=2)** | **2.83** | **2.48** | **2.84** | **3.44** |

> SPD 在大多数设置下取得最高的 **theoretical speedup**

#### 在 Qwen3.5-9B 上表现更优：

| Method | T=1, W=4 |
|--------|----------|
| EAGLE-3 (m=15) | 3.98 / **2.71** |
| PPSD (n=16) | 2.20 / **1.47** |
| **SPD (n=16, Ls=2)** | **3.83** |

> SPD 达到 **3.83x 理论加速比**，远超其他方法。

---

### 与基线方法的对比结果

- ✅ **SPD consistently outperforms EAGLE-3 and PPSD** in theoretical speedup across most configurations.
- ⚠️ 唯一例外：在 **T=0, W=4** 设置下，EAGLE-3 因raw acceptance length更高，略胜一筹。
- 📈 SPD具有优异的**可扩展性**：
  - 当 `n` 从4增至16，理论加速持续上升；
  - 当 `Ls` 从1增至4，性能进一步提升（无延迟代价）；
- 💡 在 **high-temperature sampling (T=1)** 下，SPD优势尤为明显，因其能更好建模完整logit分布，而非仅拟合top-k。

---

### 消融实验结果

#### 🔹 Input States vs. Output States（推测时机消融）

| Method (n=16, Ls=2) | Raw Acc. Len | Theoretical Speedup |
|---------------------|--------------|----------------------|
| 使用output states（串行） | 3.66–4.78 | ↓ 1.83–2.39 |
| **使用input states（并行，SPD）** | 3.11–4.04 | ↑ **2.63–3.50** |

> 虽然使用output states可以获得更高的原始接受长度，但由于重新引入了串行等待，**实际理论加速大幅下降**，证明SPD的early-start设计至关重要。

#### 🔹 Draft Tree 效果

- 扩展至W=4普遍提升 $L_{\text{acc}}$，尤其在T=1时增益更大。
- PPSD因基础准确率太低，branching反而加剧错误传播，效果不佳。

---

## 4. 关键结论和发现

### 主要发现

1. ✅ **Pipeline parallelism 可以从根本上重构 speculative decoding 范式**，摆脱对多token预测的依赖。
2. ✅ **Multi-depth feature aggregation 显著提升draft accuracy**，并通过限定pipeline长度控制误差边界。
3. ✅ **Early-start speculation 实现零延迟气泡（zero bubble）**，允许使用更深网络提升精度。
4. ✅ SPD 在 **high-temperature、code generation（HumanEval）等低熵任务**中表现最佳，$L_{\text{acc}}$高达 **5.97**（Qwen3.5-9B, T=1, W=4）。
5. ✅ 方法具备良好**可扩展性**：增加stage数或speculation层数均能带来稳定收益。

---

### 方法的局限性

1. **工程实现尚未优化**（Engineering Limitation）  
   当前基于PyTorch原生实现，缺乏：
   - 异步执行
   - 自定义CUDA kernel
   - 内存带宽优化（如paged attention）
   > 导致无法测量真实的end-to-end wall-clock加速。

2. **异构架构负载不均衡问题**（Heterogeneous Load Imbalance）  
   如Qwen3.5中混合标准注意力与线性注意力层，若划分不均会导致pipeline各stage计算量差异，破坏同步性，可能产生新的latency bubble。

3. **训练成本较高**  
   训练时需复制每个token位置为n+1个depth block（见Appendix A），增加了内存和计算开销，尽管这是为了匹配推理时的动态特征输入分布。

---

### 未来工作方向

- 🔧 将SPD集成进主流推理引擎（如 **SGLang**, **vLLM**），通过fused kernel和continuous batching释放全部性能潜力。
- 🔄 探索动态pipeline stage划分策略，适配异构模型结构，缓解load imbalance。
- 🤖 结合更复杂的draft tree结构与value-based verification机制，进一步提升接受率。
- 📦 推广至多模态LLM或长上下文场景，探索其在context distillation中的应用。

---

> **总结**：SPD 是一次对 speculative decoding 范式的根本性革新，它通过 **pipeline parallelism + multi-depth features + parallel speculation** 的组合，实现了更高准确率、零延迟气泡、强可扩展性的新一代解码加速框架，有望成为下一代主流LLM inference引擎的核心组件。

</details>

---

### 5. [UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling](https://arxiv.org/abs/2605.30898)

**Authors**: Kaiyu Huang, Xingyu Wang, Mingze Kong, Zhubo Shi, Yuqian Hou, Hong Xu, Zhongxiang Dai, Minchen Yu, Qingjiang Shi  
**Category**: cs.AI  
**Published**: 2026-06-01  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.30898v1  

#### Abstract
In real-world deployments of large language models (LLMs), balancing inference quality and computational cost has become a central challenge. Existing approaches tackle this trade-off along two largely independent dimensions: model routing, which switches among models of different scales to match re...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：**UNISCALE: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling**

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
在大型语言模型（LLMs）的实际部署中，如何在**推理质量**（inference quality）与**计算成本**（computational cost）之间取得平衡是一个核心挑战。现有方法通常将以下两个维度独立处理：

- **Model Routing**：在不同规模的模型间切换以匹配请求复杂度，但调整粒度粗、变化离散。
- **Test-Time Scaling (TTS)**：在固定模型内通过增加推理时计算量（如更多采样、搜索等）进行细粒度控制，但受限于模型自身容量，存在收益递减。

这种**解耦设计**限制了系统在动态环境中的适应能力。

---

### 🚀 提出的新方法与创新思路

#### （1）提出 **Unified Inference Scaling (UIS)** 范式
将 Model Routing 和 TTS 统一到一个联合决策空间中，定义每个推理配置为四元组：
> $$(M, QP, CP, BS)$$
其中：
- $$M$$：基础模型
- $$QP$$：Question Parallelism（并行子树数）
- $$CP$$：Candidate Parallelism（每步生成候选数）
- $$BS$$：Beam Size（保留路径数）

该统一空间允许跨维度协同优化，既利用 TTS 弥补模型间的性能间隙，又通过路由突破小模型的 TTS 容量天花板。

#### （2）提出 **UNISCALE** 框架
一个基于 **contextual multi-armed bandit** 的在线学习框架，使用 **LinUCB** 算法进行策略学习，实现对 UIS 配置的自适应选择。

其三大核心技术机制确保高效稳定优化：
1. **Path-Aware Early Exiting**  
   利用验证器（verifier）得分实时评估推理路径潜力，提前终止低潜力分支，在不牺牲最终准确率的前提下显著降低计算开销。

2. **Dense Verification Feedback**  
   将稀疏的二值正确性信号（correct/incorrect）扩展为连续的 verifier score 作为奖励反馈，提供更密集、细腻的质量监督信号。

3. **UIS Cost Model**  
   使用 **equivalent FLOPs (eFLOPs)** 统一度量计算与内存访问开销，构建硬件感知的成本模型，保证理论成本与实际资源消耗一致。

---

### 🔍 相比现有方法的优势
| 方面 | 传统方法局限 | UNISCALE 改进 |
|------|---------------|----------------|
| 决策粒度 | 粗粒度（仅模型切换）或受限于单一模型 | 细粒度、连续可调的联合优化空间 |
| 自适应性 | 多为静态规则或离线训练 | 在线学习，持续响应环境漂移（query 分布、目标变化） |
| 成本建模 | 忽略内存瓶颈或异构硬件差异 | eFLOPs 实现跨硬件统一成本度量 |
| 反馈质量 | 依赖稀疏的最终答案正确性 | 利用 verifier score 提供稠密反馈 |

---

## 2. 核心实验方法和设置

### 📚 数据集
- **AIME'24**, **AIME'25**, **MATH-500** 中共抽取 **210 个数学推理任务实例**
- 每个难度等级（Level 1–5）随机采样 30 例，覆盖多样化复杂度

### ⚙️ 实验设置
- **候选模型池**：Qwen3 系列（0.6B, 1.7B, 4B, 8B, 14B, 32B）
- **TTS 参数范围**：
  - $$QP, CP \in \{1,\dots,8\}, QP \times CP \leq 64$$
  - $$BS \in \{1,2,4\}$$
- **验证器（Verifier）**：Skywork-o1-Open-PRM-Qwen-2.5-1.5B
- **执行引擎**：基于 OpenR + vLLM 后端，支持 prefix caching 和 dynamic batching

### 🎯 评估指标
| 类型 | 指标 |
|------|------|
| **静态性能** | 平均 Reward、Accuracy (%)、Cost (Tera-eFLOPs) |
| **动态效率** | Cumulative Regret、Correct Count vs. Cost 曲线 |
| **消融分析** | Reg.@130 / Reg.@210（第130/210步累计遗憾） |

### 🆚 基线方法对比
分为两类：
1. **Multi-armed Bandit 基线**：
   - Random, Greedy, Thompson Sampling (TS), NeuralUCB
2. **Predictive Routing 基线**：
   - MLP, k-NN（基于历史相似查询预测）
   - Oracle（理论最优上界）
   - BEST-Route*（受限的一维 BoN 路由）

此外还比较了两种奖励模式下的表现：
- **Cost-Sensitive**：强调低成本
- **Quality-Priority**：强调高准确率

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（来自 Table 2）

| 方法 | 场景 | Reward | Accuracy (%) | Cost (Tera-eFLOPs) |
|------|--------|--------|--------------|--------------------|
| **UNISCALE (ours)** | TTS Only | **0.7535** | 46.50 | **23.3** |
| Random | TTS Only | 0.6937 | 42.12 | 76.7 |
| **UNISCALE (ours)** | Routing Only | **0.6196** | 29.00 | **82.9** |
| Greedy | Routing Only | 0.5873 | 34.12 | 202.5 |
| **UNISCALE (ours)** | Full UIS | **0.7079** | **57.37** | **49.4** |
| Oracle | Full UIS | 0.8337 | 68.12 | 115.7 |

> ✅ UNISCALE 在所有场景下均取得**最高 Reward** 和**最低 Cost**（除 Oracle 外），尤其在完整 UIS 空间中优势最明显。

---

### 🔁 与基线方法对比结果
- 在 **TTS 子空间**中，UNISCALE 显著优于所有基线，尤其在 Cost-Sensitive 模式下将成本降至 **23.3 Tera-eFLOPs**（仅为 Random 的 ~30%）。
- 在 **Routing 子空间**中，虽与 Greedy 接近，但仍保持稳健优势；且 Greedy 表现良好反向验证了其 reward estimator 的有效性。
- 在 **完整 UIS 空间**中，UNISCALE 实现了：
  - 比 k-NN 提升 **+10.5pp 准确率**
  - 比 TS 节省 **~72% 成本**
  - 累计遗憾（cumulative regret）始终最低，收敛更快

#### 与 BEST-Route* 对比（Table 7）
| 指标 | BEST-Route* | UNISCALE (UIS) | 提升 |
|------|-------------|----------------|-------|
| Accuracy (Cost-Sen.) | 35.00% | **46.25%** | **+11.25pp** |
| Cost (Cost-Sen.) | 1119.8 | **48.2** | **↓95.7%** |
| Accuracy (Qual-Pri.) | 50.63% | **57.50%** | **+6.87pp** |
| Cost (Qual-Pri.) | 3537.7 | **1303.3** | ↓63.1% |

> 💡 表明仅靠一维 TTS（如 Best-of-N）严重限制了优化边界，而联合 UIS 才能释放最大潜力。

---

### 🔍 消融实验结果

#### （1）Action Semantic Representations（表3 & 图9）
- 移除语义表示（w/o Sem.）导致：
  - Reg.@210 上升 12.6%（Cost-Sen.）
  - 准确率差距缩小（从 11.25pp → 4.37pp），说明缺乏泛化能力
- 结论：语义嵌入促进跨动作知识迁移，加速高维空间探索

#### （2）Path-Aware Early Exiting（表4）
| 配置 | Accuracy | Comp. Load | Mem. Access | Cost |
|------|----------|------------|-------------|------|
| Standard TTS | 65.43% | 667.4 TFLOPs | 26.8 TB | 4851.4 |
| w/ Early Exit | 64.52% | **85.0** | **5.9** | **1002.9** |
| 变化 | -0.91pp | ↓87.3% | ↓78.1% | ↓79.3% |

> ✅ 在几乎不影响准确率的情况下，实现近 **80% 的成本下降**

#### （3）Dense Verification Feedback（表5）
| 模式 | 方法 | Accuracy | Cost |
|------|------|---------|------|
| Quality-Priority | w/ Dense FB | **57.50%** | **1303.3** |
| | w/o Dense FB | 51.88% | 2674.9 |
| | 提升 | **+5.62pp** | ↓51.3% |

> ✅ 稠密反馈大幅提升学习效率，有效引导策略逼近高质量配置

#### （4）非平稳环境鲁棒性（表6 & 图7）
模拟四种环境漂移（模型增删、奖励模式切换）：
- 在 **模型移除** 场景中，UNISCALE 迅速重新探索并找到新最优配置，相比 k-NN：
  - 成本 ↓75.1%
  - 准确率 ↑2.50pp
- 在 **奖励模式切换** 中快速再校准策略，regret 恢复速度远超 k-NN

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **Model Routing 与 TTS 应被统一建模**  
   二者具有强互补性：TTS 可平滑路由跳跃，路由可突破 TTS 容量上限。联合优化形成更优的 quality-cost frontier。

2. **UNISCALE 实现了高效的在线自适应决策**  
   基于 LinUCB 的 contextual bandit 框架能在高维异构动作空间中快速收敛，持续追踪最优配置。

3. **效率增强机制至关重要**  
   - Path-Aware Early Exiting 极大减少冗余计算
   - Dense Feedback 提升学习信号密度
   - Semantic Action Embedding 加速跨配置泛化

4. **框架具备强任务泛化性和鲁棒性**  
   在编码任务（LiveCodeBench）上的测试显示，UNISCALE 同样能大幅降低成本（↓59.97%），证明其 task-agnostic 特性。

---

### ⚠️ 局限性
1. **依赖高质量 Process Reward Model (PRM)**  
   当前框架性能受 verifier 质量影响。若 verifier 不可靠，dense feedback 可能引入噪声。
2. **动作空间仍需预定义**  
   虽然支持动态调整，但模型集合和 TTS 参数需预先设定，尚未完全自动化扩展。
3. **延迟敏感场景适用性待验证**  
   尽管总开销仅占 0.91%（见 Table 10），但在极端低延迟服务中仍需进一步压缩 bandit 决策时间。

---

### 🔮 未来工作方向
1. **开发更通用、可迁移的 verifier 机制**，降低对特定 PRM 的依赖。
2. **结合 NAS 或 meta-learning 动态生成新 TTS 策略**，超越手工设计的动作空间。
3. **拓展至联邦学习范式**，支持隐私保护下的跨组织联合推理调度。
4. **集成 speculative decoding 或 token-level routing**，进一步提升推理效率。

---

## 总结一句话
> **UNISCALE 通过将 Model Routing 与 Test-Time Scaling 统一为一个可在线优化的联合决策空间，首次实现了细粒度、自适应、高效率的大模型推理缩放，在多种动态场景下全面超越现有方法，为 Green AI 与普惠智能基础设施提供了新范式。**

</details>

---

### 6. [An Efficient and Scalable Graph Condensation with Structure-Preserving](https://arxiv.org/abs/2605.31016)

**Authors**: Yulin Hu, Fuyan Ou, Ye Yuan  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.31016v1  

#### Abstract
Graph condensation (GC) is pivotal for enabling Graph Neural Networks (GNNs) deployment in resource-constrained scenarios by compressing large-scale graphs into compact synthetic counterparts. Existing GC methods commonly suffer from computational inefficiency due to coupled optimization as well as ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《An Efficient and Scalable Graph Condensation with Structure-Preserving》核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
图神经网络（GNN）在大规模图上训练成本高昂，限制了其在资源受限场景（如神经架构搜索、持续学习）中的应用。**Graph Condensation (GC)** 技术通过将大图压缩为小型合成图来缓解该问题，但现有方法存在以下瓶颈：
- **计算效率低**：多数方法采用耦合优化（coupled optimization），涉及双层甚至三层优化，导致训练缓慢且难以扩展。
- **泛化能力差**：依赖特定 GNN 架构作为“中继模型”（relay model），导致在不同 GNN 上性能不稳定。
- **结构信息保留不足**：难以有效保持原始图的拓扑结构，尤其在高压缩比下。

### 🚀 提出的新方法：SP-ESGC
本文提出 **SP-ESGC (Structure-Preserving Efficient and Scalable Graph Condensation)**，其核心思想是**解耦节点特征压缩与图结构生成**，实现高效、可扩展且结构感知的图压缩。

#### 创新点：
1. **Decoupled Design（解耦设计）**
   - 将节点表示学习与图结构生成分离，避免复杂的 bi-level optimization 和重复 GNN 训练。
   
2. **Heat Kernel Feature Propagation（热核特征传播）**
   - 基于谱图理论，利用热核扩散（heat kernel diffusion）对节点特征进行平滑和增强，融合局部与全局结构信息，提升表示稳定性。

3. **Hybrid Clustering Strategy（混合聚类策略）**
   - 针对每个类别内的节点表示，结合：
     - **Truncated SVD**：提取低秩主成分，降噪；
     - **Random Fourier Features (RFF)**：近似 RBF 核映射，增强非线性判别能力；
     - **Spectral Space Clustering**：在嵌入空间中聚类，获得更具代表性的类内中心（centroids）。

4. **Pre-trained Edge Predictor（预训练边预测器）**
   - 在原图上预训练一个参数化的边预测模型 $ f_\theta $，输入为节点对的拼接特征 $[x_u; x_v]$，输出边存在的概率。
   - 在合成节点上进行 all-pairs 推理，生成稠密邻接矩阵，并通过高分位阈值稀疏化，构建最终图结构。

### 🔍 相比现有方法的优势
| 维度 | SP-ESGC | 现有方法（如 GCond, SFGC, GC-SNTK） |
|------|--------|-------------------------------|
| **效率** | 显著更高，无需反复训练 GNN 或梯度匹配 | 计算开销大，常需双层优化 |
| **可扩展性** | 支持超大规模图（如 Reddit） | 在大图上易出现 OOM 或耗时极长 |
| **泛化性** | 跨多种 GNN 架构表现稳定 | 性能依赖中继模型，泛化差 |
| **结构保持** | 通过边预测器显式建模连接模式 | 多隐式建模，结构保真度有限 |

---

## 2. 核心实验方法和设置

### 📊 数据集
在五个真实世界图数据集上验证，涵盖**直推式（transductive）** 与**归纳式（inductive）** 场景：

| Dataset       | 类型         | #Nodes      | #Edges        | #Classes | #Features |
|---------------|--------------|-------------|----------------|----------|------------|
| **Cora**      | Transductive | 2,708       | 5,429          | 7        | 1,433      |
| **Citeseer**  | Transductive | 3,327       | 4,732          | 6        | 3,703      |
| **Ogbn-arxiv**| Transductive | 169,343     | 1,166,243      | 40       | 128        |
| **Flickr**    | Inductive    | 89,250      | 899,756        | 7        | 500        |
| **Reddit**    | Inductive    | 232,965     | 57,307,946     | 210      | 602        |

> 注：对于归纳式数据集，压缩比例基于训练子图节点数。

### ⚙️ 实验设置
- **压缩比（Condensation Ratio, r）**：定义为 $ r = n / N $，其中 $ n $ 是合成图节点数，$ N $ 是原图节点数。
- 测试三种压缩比（具体值见 Table II），例如 Cora 上测试 1.30%, 2.60%, 5.20%。
- 所有实验在 **NVIDIA GeForce RTX 3050 GPU** 上运行。

### 🎯 评估指标
1. **Node Classification Accuracy (%)**
   - 在合成图上训练 GNN 模型，在原始测试集上评估准确率。
   - 衡量压缩图的信息保留能力。
2. **Condensation Time (seconds)**
   - 图压缩总耗时（含边预测器预训练 + 合成推理）。
   - 衡量方法效率。
3. **Generalization Across GNN Architectures**
   - 在多个 GNN 模型（GCN, SGC, GAT, GraphSAGE, APPNP）上测试性能稳定性。
4. **Ablation Study**
   - 移除关键模块验证各组件作用。

### 🆚 基线方法对比
| 类型 | 方法 |
|------|------|
| **Core-set Methods** | Random, Herding, K-Center |
| **Graph Condensation** | GCond, SGDD, SimGC, GC-SNTK, SFGC |

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（Test Accuracy %）

> 结果摘自 **Table II**

| Dataset       | Ratio   | Best Method     | Accuracy (%) | Whole Dataset |
|---------------|---------|------------------|---------------|----------------|
| **Cora**      | 1.30%   | **SP-ESGC**     | **82.6±0.6**  | 81.2±0.2       |
| **Cora**      | 2.60%   | **SP-ESGC**     | **82.7±0.1**  | 81.2±0.2       |
| **Citeseer**  | 1.80%   | **SP-ESGC**     | **72.8±0.2**  | 71.7±0.1       |
| **Ogbn-arxiv**| 0.25%   | **SP-ESGC**     | **66.7±0.1**  | 71.4±0.1       |
| **Flickr**    | 0.10%   | **SP-ESGC**     | **47.2±0.2**  | —              |
| **Reddit**    | 0.05%   | **SP-ESGC**     | **90.7±0.0**  | 93.9±0.0       |

> ✅ **SP-ESGC 在绝大多数情况下取得最优或次优性能**，尤其在**低压缩比下优势明显**。

---

### ⏱️ 效率对比（Condensation Time）

> 结果摘自 **Table III**，压缩比分别为：Cora(2.60%), Citeseer(1.80%), Ogbn-arxiv(0.25%), Flickr(0.50%), Reddit(0.10%)

| Method     | Cora  | Citeseer | Ogbn-arxiv | Flickr | Reddit     |
|------------|-------|----------|------------|--------|------------|
| GCond      | 653.9 | 940.3    | 13,521.7   | 1,455.6| 20,528.8   |
| SGDD       | 4,848.6| 3,091.2 | 35,179.7   | 26,767.4| 378,220.9 |
| SimGC      | 289.3 | 495.7    | 476.6      | 744.5  | 2,655.9    |
| GC-SNTK    | 92.1  | 69.7     | 28,897.8   | 889.8  | **OOM**    |
| SFGC       | 5,895.8| 3,807.2 | 156,975.2  | 46,706.7| 370,089.0 |
| **SP-ESGC**| **12.4** | **26.4**  | **143.4**   | **22.6** | **162.5**  |

> ✅ **SP-ESGC 运行时间显著低于所有基线**，在 Reddit 上仅为第二快方法（SimGC）的约 **1/16**，展现出卓越的**可扩展性**。

---

### 🔍 消融实验结果（Ablation Study）

> 结果摘自 **Table IV**

| Variant             | Cora   | Citeseer | Ogbn-arxiv | Flickr | Reddit |
|---------------------|--------|----------|------------|--------|--------|
| **SP-ESGC w/o HKP** | 78.6   | 70.4     | 65.4       | 46.7   | 90.5   |
| **SP-ESGC w/o EP**  | 81.9   | 72.5     | 66.0       | 45.8   | 91.1   |
| **SP-ESGC w K-means**| 81.4   | 72.0     | 66.6       | 46.7   | 91.4   |
| **Full SP-ESGC**    | **82.7** | **72.8** | **66.7**   | **47.2** | **91.6** |

> ✅ 完整模型始终最优，说明：
> - **Heat Kernel Propagation (HKP)** 对表示质量至关重要（Cora 下降 >4%）；
> - **Edge Predictor (EP)** 比基于余弦相似度的方法更能捕捉复杂连接模式；
> - **Spectral Clustering + Kernel Expansion** 比 K-means 更适合非线性分布的数据。

---

## 4. 关键结论和发现

### ✅ 主要发现
1. **解耦设计大幅提升效率与稳定性**  
   分离节点压缩与结构生成，避免了昂贵的双层优化，使 SP-ESGC 成为目前最高效的 GC 方法之一。

2. **热核传播提供稳定且富含结构信息的节点表示**  
   基于谱理论的扩散机制有效融合局部与全局信息，优于直接使用原始特征。

3. **预训练边预测器实现结构可迁移性**  
   能从原图中学到通用的“连接规则”，并迁移到合成节点上，显著提升结构保真度。

4. **SP-ESGC 具备强泛化能力**  
   如 Fig. 2 所示，在多种 GNN 架构（GCN, GAT, SAGE 等）上均保持高性能，波动小，而 GCond 在 GAT 上性能明显下降。

5. **适用于大规模图场景**  
   在 Reddit（超 23 万节点）上仍能快速完成压缩且无内存溢出，而 GC-SNTK 已无法运行。

---

### ⚠️ 方法的局限性
- **依赖标签信息进行类内聚类**：当前方法假设节点标签可用，不适用于完全无监督场景。
- **边预测器可能过拟合局部模式**：若原图结构噪声较大，预训练模型可能学到错误连接规律。
- **压缩后图仍为全连接初始化再稀疏化**：理论上可进一步优化结构生成方式以减少冗余计算。

---

### 🔮 未来工作方向
1. **扩展至无监督/自监督图压缩**：去除对标签的依赖，适用于更广泛场景。
2. **动态图压缩**：支持随时间演化的图结构压缩。
3. **多粒度压缩机制**：允许不同类别使用不同压缩强度。
4. **端到端轻量化框架集成**：将 SP-ESGC 与 NAS、联邦学习等系统深度整合，打造全流程高效图学习 pipeline。

---

## 总结
**SP-ESGC** 是一种**高效、可扩展、结构感知**的图压缩框架，通过**解耦设计、热核传播、混合聚类与预训练边预测器**四大核心技术，在多个真实图数据集上实现了**更高压缩效率、更强泛化能力和更优下游任务性能**，特别适合应用于大规模图与资源受限环境下的 GNN 部署。

</details>

---

### 7. [Eigenvectors of Experts are Training-free Non-collapsing Routers](https://arxiv.org/abs/2605.30992)

**Authors**: Giang Do, Hung Le, Truyen Tran  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.30992v1  

#### Abstract
Sparse Mixture of Experts (SMoE) architectures improve the training efficiency of Large Language Models (LLMs) by routing input tokens to a selected subset of specialized experts. Despite their remarkable success, both training and inference in SMoE models suffer from the expert collapse issue (Chi ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Eigenvectors of Experts are Training-free Non-collapsing Routers》核心总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
该论文聚焦于 **Sparse Mixture of Experts (SMoE)** 架构中的**专家坍缩（expert collapse）**问题。在SMoE模型中，路由机制（router）负责将输入token分配给最相关的专家子网络。然而，实践中多个专家会收敛到相似的输出，导致模型容量浪费、表达能力下降，即“representation collapse”现象。

尽管已有研究尝试通过改进路由器设计来缓解此问题，但这些方法通常需要从头训练或微调，计算成本高昂，并且在预训练好的先进SMoE模型上仍难以彻底解决坍缩问题。

### 提出了什么新方法或新思路
作者提出了一种全新的、无需训练的路由框架——**Singular Value Decomposition SMoE (SSMoE)**，其核心思想是：

> **利用专家权重矩阵的特征向量（eigenvectors）作为语义丰富的路由信号，替代或增强传统可学习的router。**

具体而言：
- 对每个专家的FFN层权重进行Gram矩阵构造并执行SVD分解。
- 提取前c个主成分对应的**eigenvectors**，形成“spectral embedding”。
- 将这些eigenvector表示用于构建新的“EV Router”，并与原始router结合，通过加权融合实现最终的专家选择。

### 相比现有方法的优势
| 维度 | 优势说明 |
|------|--------|
| **无需训练** | SSMoE完全基于预训练模型的权重分析，不引入任何额外参数或优化过程，真正实现“training-free”。 |
| **抗坍缩能力强** | 理论证明（Lemma 3.1）表明，eigenvector之间的近似正交性显著降低了专家logits间的相关性，从而有效缓解collapse。 |
| **通用性强** | 在LLM、Vision-Language Model等多种架构和任务中均表现出色。 |
| **资源效率高** | 可与expert dropping策略结合，在减少约23%内存占用的同时保持甚至提升性能。 |

---

## 2. 核心实验方法和设置

### 使用的数据集
#### 大型推理模型（Large Reasoning Models）
- **GPT-OSS-20B / GPT-OSS-120B**：开源MoE语言模型，分别含32和128个专家。
- 推理基准（共8项）：
  - `ARC-C`, `ARC-E`（科学问答）
  - `BoolQ`（二元阅读理解）
  - `GSM8K`（数学应用题）
  - `HellaSwag`（常识推理）
  - `OBQA`（开放书本问答）
  - `PIQA`（物理常识）
  - `WinoGrande`（指代消解）

#### 大型语言模型（LLMs）
- 模型：`OLMoE-7B`, `Qwen-MoE-7B`, `DeepSeekMoE-16B`
- 评估平台：**Massive Text Embedding Benchmark (MTEB)**
  - 包括分类（Classification）、聚类（Clustering）、句子对分类（Pair Classification）、重排序（Re-ranking）、语义相似度（STS）、摘要（Summarization）等任务。

#### 视觉语言模型（Vision-Language Models）
- 模型：`CLIP-MoE`
- 任务：
  - 零样本图像-文本检索（Zero-shot Image-Text Retrieval）：`COCO`, `Flickr30k`
  - 零样本图像分类：`CIFAR-10/100`, `STL-10`, `Caltech101`, `ImageNet-1K/O`

### 实验设置和评估指标
| 类别 | 设置详情 |
|------|--------|
| **评估模式** | 主要采用 **5-shot 和 10-shot in-context learning** 设置，无微调。 |
| **评估指标** | - 分类任务：Accuracy<br>- 聚类：V-Measure<br>- STS：Spearman correlation<br>- 检索任务：Recall@1/@5/@10<br>- 语言建模：Perplexity（WikiText-2） |
| **硬件环境** | H100/H200 GPU，部分实验使用4-bit量化以节省显存。 |

### 基线方法对比
| 方法 | 描述 |
|------|------|
| **Original** | 原始SMoE模型 |
| **RandomDrop** | 随机丢弃25%专家 |
| **Router** | 基于平均相似度的专家丢弃策略 |
| **SMoE / MoEE** | 基于router embedding的标准表示方法 |
| **PromptEOL** | 上下文提示方法，用于in-context learning比较 |
| **Hash-based / Random Routing** | 输入无关的非智能路由策略 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ 大型推理模型（GPT-OSS系列）
| 模型 | 方法 | 平均得分 ↑ | 内存 ↓ | 相对原模型增益 |
|------|------|------------|--------|----------------|
| GPT-OSS-20B | Original | 48.8 | 38.96 GB | — |
| | SSMoE (75%专家) | **54.1** | **30.05 GB** | **+10.9%**, -22.9% 内存 |
| | SSMoE-FULL | 55.2 | 38.96 GB | +6.4% |
| GPT-OSS-120B | Original | 52.6 | 217.61 GB | — |
| | SSMoE | **54.9** | **164.20 GB** | **+4.4%**, -24.5% 内存 |

> 🔥 特别亮点：在`BoolQ`上相对原模型提升达 **24%**，在`GSM8K`上提升 **17%**。

#### ✅ 大型语言模型（MTEB综合表现）
| 模型 | 方法 | Clean Avg ↑ | Corrupt Avg ↑ |
|------|------|-------------|---------------|
| OLMoE-7B | SMoE | 29.9 | 20.6 |
| | MoEE | 35.2 | 21.2 |
| | **SSMoE (Ours)** | **39.7** | **24.8** |
| DeepSeekMoE-16B | SMoE | 32.1 | 22.8 |
| | MoEE | 35.9 | 23.8 |
| | **SSMoE (Ours)** | **41.1** | **27.2** |

> 💡 在干净和噪声环境下均取得SOTA，尤其在`STS`和`Clustering`任务上提升显著。

#### ✅ 视觉语言模型（零样本检索）
| 数据集 | 方法 | R@1 ↑ | 改进幅度 |
|--------|------|-------|----------|
| COCO I2T | CLIP-MoE | 65.0 | — |
| | **SSMoE** | **65.7** | **+1.1%** |
| Flickr I2T | CLIP-MoE | 60.5 | — |
| | **SSMoE** | **61.1** | **+1.0%** |
| （带噪声）COCO I2T | CLIP-MoE | 36.2 | — |
| | **SSMoE** | **37.2** | **+2.8%** |

> 📈 统计检验显示所有改进均为**统计显著**（p < 0.01）。

---

### 消融实验结果

#### 🔍 路由器引导 vs. 平均特征向量
| 方法 | 平均得分 |
|------|---------|
| Original | 48.8 |
| SSMoE w/ Avg EV | 52.7 |
| SSMoE (Full) | **54.1** |

> ✔️ 即使简单平均eigenvector也能带来+3.9分提升，说明eigenvector本身蕴含丰富语义信息；加入router引导进一步提升精度。

#### 🔍 不同TOPC值的影响
| TOPC | Emotion | Toxic | Tweet |
|------|--------|--------|--------|
| 5 | 36.5 | 57.4 | 51.3 |
| 50 | **37.4** | **60.7** | **53.4** |

> ✅ 性能随TOPC增大趋于稳定，推荐设置为~50。

#### 🔍 平衡因子 α 的影响
| α | Emotion | Toxic | Tweet |
|----|--------|--------|--------|
| 0.3 | 27.5 | 61.1 | 49.8 |
| 0.9 | **32.7** | **62.6** | **54.3** |

> ⚖️ 最佳α在 **0.5–0.9** 之间，偏向更多依赖eigenvector信号。

---

## 4. 关键结论和发现

### 主要发现（Key Findings）
1. **Finding 1**:  
   > **专家权重矩阵的eigenvectors编码了丰富的语义信息**，可以作为有效的路由依据，无需依赖可学习router。

2. **Finding 2**:  
   > **并非所有专家都对推理任务必要**，合理地移除冗余专家（如25%）不会损害性能，反而可能因更优路由而提升效果。

3. **Finding 3**:  
   > **eigenvector-based 表示是一种高效且鲁棒的嵌入方式**，在噪声环境下优于复杂表示方法，符合“No Free Lunch”理论。

4. **Finding 4**:  
   > **传统SMoE router在深层出现严重坍缩**，而EV router在整个网络中保持良好正交性，避免了logit相关性累积。

### 方法的局限性
| 局限 | 说明 |
|------|------|
| **数学推理任务敏感于专家数量** | 如`GSM8K`在pruned设置下性能下降明显（Table 16），表明某些任务依赖特定专家池。 |
| **依赖FFN结构完整性** | 若专家被大幅压缩或蒸馏，eigenvector结构可能失真，影响路由质量。 |
| **未探索动态调整α机制** | 当前α为静态超参，未来可考虑根据输入自适应调节。 |

### 未来工作方向
- 将SSMoE思想扩展至其他模块（如attention heads）。
- 结合低秩适配（LoRA）等技术，在微调场景下进一步释放潜力。
- 探索如何自动识别“关键专家”并保留之，用于轻量化部署。
- 将eigenvector路由应用于多模态或多任务持续学习场景。

---

> ✅ **一句话总结**：  
> 本文揭示了**专家权重的谱特性**是解决SMoE坍缩问题的关键，提出的**SSMoE**是一种无需训练、高效稳健的新范式，为下一代稀疏化大模型提供了全新设计视角。

> 🔗 开源地址：[https://github.com/giangdip2410/SSMoE](https://github.com/giangdip2410/SSMoE)

</details>

---

### 8. [Parallel Tempering Initial Sampling in Inference-Time Reward Alignment](https://arxiv.org/abs/2605.30991)

**Authors**: Myeongjun Oh, Gwangho Kim, Sungyoon Lee  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.30991v1  

#### Abstract
Inference-time reward alignment steers pretrained diffusion and flow-based generative models to satisfy user-specified rewards without retraining. Recently, Sequential Monte Carlo (SMC) has emerged as a powerful framework for this task by iteratively filtering and propagating multiple particles. How...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Parallel Tempering Initial Sampling in Inference-Time Reward Alignment**

---

## 1. **论文的主要贡献和创新点**

### ✅ 解决了什么问题

本文针对**Inference-Time Reward Alignment**（推理时奖励对齐）中的一个关键瓶颈：**初始粒子采样质量差导致在复杂奖励景观下性能下降**。

具体来说，现有方法存在两大缺陷：
- **标准SMC方法**（如TDS、DAS）从标准先验 $\mathcal{N}(0, I)$ 初始化粒子，但在高奖励区域极其稀疏或罕见的情况下，这些粒子难以覆盖目标区域。
- **V-Sampler等改进初始化的方法**虽然引入了reward-aware的初始分布，但仍依赖独立的pCNL链，在多模态（multi-modal）奖励景观中容易陷入局部最优（mode trapping），无法有效探索全局高奖励区域。

### ✅ 提出了什么新方法或新思路

提出 **PATHS**（**PArallel Tempering for High-complexity reward Sampling**），一种基于**Parallel Tempering**（并行回火，又称Replica Exchange）的新型初始化框架，用于提升SMC-based推理时对齐的初始粒子质量。

**核心思想**：
- 构建一个温度梯度（temperature ladder），维护多个不同温度下的pCNL采样链：
  - **高温链（Hot chains）**：平坦化奖励景观，促进全局探索；
  - **低温链（Cold chain, $T=1$）**：聚焦于原始reward-aware后验，进行精细优化。
- 定期执行**Metropolis交换**（replica-exchange swap）：允许高温链发现的高奖励状态“跳跃”到低温链，从而打破局部模式陷阱。

### ✅ 相比现有方法的优势

| 方面 | 优势 |
|------|------|
| **探索能力** | 显著增强对稀有、多模态高奖励区域的有限预算下的探索能力 |
| **避免局部陷落** | 通过跨温度信息传递，缓解独立MCMC链的mode trapping问题 |
| **无需额外训练** | 属于inference-time方法，不修改预训练模型参数 |
| **计算匹配公平比较** | 与Best-of-4等多链方法共享相同reward evaluation budget |

---

## 2. **核心实验方法和设置**

### 📚 使用的数据集与任务

实验集中在两个具有**内在复杂奖励景观**的任务上：

#### （1）**Layout-to-Image Generation**
- **目标**：将对象按指定bounding box和空间关系生成图像。
- **挑战**：满足布局约束的配置多样 → 多模态；精确匹配困难 → 尖锐峰值。
- **数据来源**：自定义prompt集合 `selected_prompts_data.json`，按对象数量分简单（≤3）和复杂（=4）子集。

#### （2）**Quantity-Aware Sampling**
- **目标**：生成指定数量的目标对象（如“82 blueberries”）。
- **挑战**：计数偏差即惩罚 → 高奖励区域极窄且分离 → 稀有 + 多峰。
- **数据来源**：`quantity_aware_selected_20.json`，按目标数量分简单（<25）和复杂（≥25）子集。

---

### ⚙️ 实验设置

| 设置项 | 描述 |
|-------|------|
| **基础模型** | FLUX.1-schnell（flow-based diffusion model） |
| **总预算** | 1000次reward model调用（evaluation budget） |
| **分配方式** | 初始化阶段500次，SMC阶段500次（20 particles × 25 steps） |
| **PATHS配置** | 4条温度链（L=4），每链1粒子（C=1），burn-in=65，采样=60步，每5步尝试交换 |
| **温度梯度** | Layout: `{1,2,4,8}`；Quantity: `{1,4,16,64}`（更宽以适应更强探索需求） |

---

### 📊 评估指标

| 任务 | 指标 | 类型说明 |
|-----|------|---------|
| **Layout-to-Image** | - **GroundingDINO+** ↑（布局对齐）<br>- **mIoU** ↑（分割一致性）<br>- **ImageReward** ↑（视觉偏好）<br>- **VQAScore** ↑（文本-图像对齐） | ↑表示越高越好；带†为训练中使用的reward，其余为held-out评估 |
| **Quantity-Aware** | - **T2I-Count+ ↓**（计数误差）<br>- **ImageReward** ↑<br>- **VQAScore** ↑ | ↓表示越低越好 |

---

### 🔁 基线方法对比

| 类别 | 方法 | 说明 |
|------|------|------|
| **Prior-initialized SMC** | TDS [44], DAS [22] | 从标准先验初始化，无reward-aware init |
| **Posterior-initialized** | V-Sampler [50] | 使用pCNL从reward-aware posterior采样 |
| | Best-of-4 | 运行4条独立冷链，选最高reward的一条传入SMC |
| **Proposed** | **PATHS (Ours)** | 多温链 + replica exchange |

> 所有方法控制相同的reward evaluation budget，确保公平比较。

---

## 3. **主要实验结果和性能指标**

### 📈 关键性能数据（来自Table 1）

#### ✅ **Layout-to-Image 结果**

| 子集 | 方法 | GroundingDINO+ | mIoU | ImageReward | VQA |
|------|------|----------------|------|-------------|-----|
| **Overall** | TDS | 0.352 | 0.348 | 0.827 | 0.766 |
| | DAS | 0.297 | 0.299 | 0.872 | 0.774 |
| | V-Sampler | 0.348 | 0.325 | 0.705 | 0.738 |
| | Best-of-4 | 0.363 | 0.355 | 0.826 | 0.771 |
| | **PATHS (Ours)** | **0.376** | **0.366** | **0.949** | **0.797** |
| **Complex** | TDS | 0.261 | 0.287 | 1.034 | 0.618 |
| | DAS | 0.226 | 0.265 | 0.861 | 0.608 |
| | V-Sampler | 0.239 | 0.266 | 0.625 | 0.580 |
| | Best-of-4 | 0.265 | 0.273 | 0.781 | 0.588 |
| | **PATHS (Ours)** | **0.266** | **0.274** | **1.411** | **0.706** |

> 在复杂子集中，PATHS在ImageReward上远超其他方法（+0.63 vs Best-of-4），显示其能更好发现高质量样本。

#### ✅ **Quantity-Aware Sampling 结果**

| 子集 | 方法 | T2I-Count+ ↓ | ImageReward | VQAScore |
|------|------|---------------|-------------|----------|
| **Overall** | TDS | 2.083 | -0.243 | 0.549 |
| | DAS | 1.786 | -0.331 | 0.553 |
| | V-Sampler | 2.412 | 0.048 | 0.645 |
| | Best-of-4 | 1.613 | 0.095 | 0.652 |
| | **PATHS (Ours)** | **1.344** | **0.244** | **0.669** |
| **Complex** | TDS | 3.250 | -0.300 | 0.546 |
| | DAS | 3.108 | -0.325 | 0.555 |
| | V-Sampler | 4.181 | 0.104 | 0.616 |
| | Best-of-4 | 2.463 | 0.170 | 0.608 |
| | **PATHS (Ours)** | **1.725** | **0.202** | **0.657** |

> 在最难的复杂计数任务中，PATHS将平均计数误差从Best-of-4的2.46降至1.72（↓30%），显著优于所有基线。

---

### 🔍 消融实验与关键分析

- **与Best-of-4对比**：尽管两者都使用4条链，但PATHS通过replica exchange实现**在线信息交换**，而Best-of-4是“事后选择”，无法弥补探索不足。
- **温度梯度敏感性分析**（Figure 6）：验证了温度梯度设计的重要性。过窄则探索不足，过宽则耦合弱。最终选择任务适配的梯度（如`{1,4,16,64}`用于quantity任务）。
- **合成实验可视化**（Appendix I）：展示了hot chain如何发现被cold chain遗漏的对象，并通过swap成功转移，cold chain随后在此基础上微调。

---

## 4. **关键结论和发现**

### ✅ 主要发现

1. **初始化至关重要**：即使采用先进的twisting策略（如DAS），若初始粒子未覆盖高奖励区域，后续SMC仍会失败。
2. **多模态奖励需系统性探索**：传统的local MCMC（如pCNL）易陷入局部模式，无法跨越高能量壁垒。
3. **Parallel Tempering有效破局**：通过构建温度梯度和replica exchange，PATHS实现了“热链探索 → 冷链精炼”的协同机制，大幅提升稀有多模态场景下的采样效率。
4. **收益集中在复杂任务**：PATHS在**复杂提示**（多对象、空间关系、高计数）上增益最大，表明其特别适用于高结构性要求的生成任务。

---

### ⚠️ 方法的局限性

1. **仅在多模态奖励下有效**：当奖励景观平滑、单峰时（如纯美学评分），PATHS相比V-Sampler提升有限（见Table 3和Figure 7）。
   - 示例：使用LAION Aesthetic Predictor作为reward时，各方法差异微小。
2. **依赖手工设定温度梯度**：当前温度序列为手动调参，缺乏自适应机制。
3. **计算开销略高**：虽reward eval budget相同，但MCMC迭代次数更多，wall-clock time稍长。

---

### 🔮 未来工作方向

1. **自适应温度调度**：动态调整温度梯度以匹配当前任务难度。
2. **Per-prompt ladder tuning**：根据不同prompt复杂度自动选择最优温度设置。
3. **扩展至更多inference-time control任务**：如instruction following、multi-step reasoning等需要组合泛化的场景。
4. **结合fine-tuning方法**：探索PATHS作为data collector用于offline RL或DPO pipeline的可能性。

---

## ✅ 总结

**PATHS** 是首个将 **Parallel Tempering** 引入 **inference-time reward alignment** 初始采样的方法，解决了传统SMC和V-Sampler在**稀有、多模态奖励景观**下的探索瓶颈。其实验充分证明，在layout-to-image和quantity-aware generation等高复杂度任务中，PATHS能显著提升对齐质量和生成多样性，尤其在复杂提示下表现卓越。该工作强调了**鲁棒初始化**与**跨模式探索**对于下一代可控生成系统的重要性。

</details>

---

### 9. [Fixed-Point Masked Generative Modeling](https://arxiv.org/abs/2605.31215)

**Authors**: Andrea Miele, Yiming Qin, Alba Carballo-Castro, Justin Deschenaux, Pascal Frossard  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.31215v1  

#### Abstract
Masked Generative Models (MGMs) enable parallel decoding and achieve strong performance across modalities, but require full-sequence bidirectional transformers at every step, making training costly and degrading quality under low sampling budgets. Existing work improves efficiency via better sampler...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Fixed-Point Masked Generative Modeling**

## 1. **论文的主要贡献和创新点**

### **解决的问题**
Masked Generative Models (MGMs)，如 MDLM 和 MaskGIT，在文本和图像生成中表现出色，支持并行解码且生成质量高。然而，它们存在以下关键问题：
- **训练成本高昂**：每一步去噪都需要对整个序列进行全双向 Transformer 前向传播，消耗大量 VRAM 且训练缓慢。
- **低采样预算下生成质量差**：在有限的计算资源（如 Transformer 块前向传递次数）下，生成样本的质量显著下降。

现有改进方法（如更优的采样器或轻量架构）通常仍为每个去噪步骤分配固定的计算量，无法动态适应不同步骤的复杂度。

---

### **提出的新方法：FP-MGMs 与 CoFRe 框架**
本文提出了 **Fixed-Point Masked Generative Models (FP-MGMs)**，其核心是将去噪器中的部分层替换为一个**共享权重的固定点求解器 (fixed-point solver)**，从而实现自适应深度和参数减少。

为了使该框架在掩码生成任务中更有效，作者引入了两个关键机制，共同构成了完整的训练到推理框架 **CoFRe**：
1. **Cross-step Consistency Loss (跨步一致性损失)**：
   - 在训练时，对来自同一干净序列但处于不同噪声水平（学生状态更嘈杂，教师状态更干净）的隐藏表示进行对齐。
   - 该损失行为类似于跨时间的自蒸馏 (self-distillation)，能锐化掩码位置的预测，显著提升低预算下的生成质量。

2. **Three-State Reuse (3SR, 三态重用)**：
   - 在推理时，利用上一步的固定点解来热启动当前求解器，但针对三种不同类型的 token 进行差异化处理：
     - **已可见且未变的 token**：完全重用 (`γ=1.0`)。
     - **仍被掩码的 token**：部分重用 (`γ=0.75~0.90`)。
     - **新揭示的 token**：弱重用，更多依赖当前输入 (`γ=0.2`)。
   - 此设计解决了因 token 状态突变导致的旧解不可靠问题。

此外，论文还展示了**预训练模型转换**的可行性：可以将已有的 MGM 检查点通过短时间的微调（distillation）高效地转换为 FP-MGM，避免从头开始训练。

---

### **相比现有方法的优势**
| 特性 | 现有方法 | 本文方法 (CoFRe) |
| :--- | :--- | :--- |
| **计算效率** | 固定深度，计算量恒定 | 自适应深度，共享参数，减少参数量和内存占用 |
| **低预算性能** | 通常较差 | 显著提升，尤其在极低预算下 |
| **训练成本** | 高昂 | 大幅降低训练时间和 VRAM 消耗 |
| **模型复用** | 通常需从头训练 | 支持从预训练检查点快速转换 |

## 2. **核心实验方法和设置**

### **使用的数据集**
- **语言建模**：`OpenWebText (OWT)`，上下文长度 1024。
- **图像生成**：`ImageNette` (ImageNet 的 10 类子集)，分辨率 256×256。

### **实验设置和评估指标**
- **评估协议**：在固定的 **Transformer 块前向传递预算** 下比较生成质量，以公平衡量计算效率。
- **语言生成指标**：
  - **Generative Perplexity (Gen. PPL)**：使用 GPT-2 Large 对生成的样本进行打分，越低越好。
  - **Unigram Entropy**：衡量生成文本的多样性，越高越好。
- **图像生成指标**：
  - **FID (Fréchet Inception Distance)**：越低越好，衡量生成图像与真实图像分布的相似度。
  - **IS (Inception Score)**：越高越好，衡量生成图像的质量和多样性。

### **基线方法对比**
- **语言模型**：
  - `MDLM`：标准的掩码扩散语言模型。
  - `MDLM + SDTT`：经过自蒸馏优化的 MDLM，是强基线。
- **图像模型**：
  - `MaskGIT-Large`：大型的掩码生成图像 Transformer。
  - `MaskGIT-12`：层数减半的轻量版本。

## 3. **主要实验结果和性能指标**

### **关键性能数据与对比结果**

#### **在 OpenWebText 上的语言生成 (预算 96)**
| 方法 | Gen. PPL ↓ | 参数量 #Params | 训练时间 | VRAM |
| :--- | :--- | :--- | :--- | :--- |
| MDLM | 830.8 | 170M | ~139h | 112.4 GiB/GPU |
| MDLM + SDTT | **193.1** | 170M | ~139h + SDTT | 112.4 GiB/GPU |
| **CoFRe** | **101.8** | **104M (-38.8%)** | **~123h + 30k** | **93.4 GiB/GPU (-16.9%)** |

- **结论**：CoFRe 在大幅减少参数、训练时间和内存的同时，将生成困惑度从 193.1 (SDTT) 进一步降至 **101.8**，实现了质的飞跃。

#### **在 ImageNette 上的图像生成 (预算 48)**
| 方法 | FID ↓ | 训练时间 | VRAM |
| :--- | :--- | :--- | :--- |
| MaskGIT-Large | 174.09 | 17h 46m | 72.45 GiB |
| **CoFRe** | **96.73** | **9h 08m (-48.6%)** | **35.74 GiB (-50.7%)** |

- **结论**：CoFRe 将训练时间缩短近一半，VRAM 减少超过一半，并将 FID 从 174 降至 **97**，在所有预算下均优于基线。

---

### **消融实验结果**
1. **固定点架构 (FP-MDLM) 的基础效果**：
   - 仅替换为固定点架构即可在低预算下大幅提升效率，但高预算下性能不如正则化的 MDLM。

2. **Cross-step Consistency (Ccons) 是关键**：
   - 添加 `Ccons` 后，FP-MDLM 在预算 96 下的 Gen. PPL 从 375.6 降至 **104.2**，是性能提升的最大来源。
   - 它使后续的重用策略变得稳定且有效。

3. **Three-State Reuse (3SR) 的有效性**：
   - 与简单的“全重用”相比，3SR 能更好地处理新揭示的 token，避免错误累积。
   - 在 `Ccons` 正则化后，3SR 在中等和高预算下均能进一步提升性能。

4. **预训练模型转换**：
   - 仅用 4% 的原始预训练步数（40k 步）对预训练的 MDLM 进行微调，即可得到优于从头训练的 FP-MDLM 基线的模型。

## 4. **关键结论和发现**

### **主要发现**
1. **固定点架构是高效的基石**：通过共享权重的迭代求解，FP-MGMs 成功减少了参数量、训练时间和内存占用。
2. **跨步一致性至关重要**：`Ccons` 损失是解锁低预算高性能的关键，它通过隐式的自蒸馏机制稳定了训练过程。
3. **智能重用提升推理效率**：3SR 规则使得固定点求解器能够安全、有效地热启动，充分利用历史计算结果。
4. **CoFRe 是一个实用的完整框架**：`FP-MGM + Ccons + 3SR` 构成了一个从训练到推理的端到端解决方案，显著改善了生成模型的成本-质量权衡。

### **局限性**
- **规模限制**：实验仅在 OWT 和 ImageNette 等中等规模数据集上验证，尚未扩展到超大规模模型或数据集。
- **启发式设计**：3SR 中的重用系数和 `Ccons` 的训练时长等需要手动调整，缺乏完全自动化的策略。
- **通用性**：3SR 设计基于单调的掩码解码（token 只揭示不重置），对于支持 remasking 或修订的采样器可能不适用。
- **控制流开销**：固定点求解器增加了循环控制逻辑，在某些硬件上可能不会直接转化为墙钟时间的加速。

### **未来工作方向**
- 探索更高级的停止规则 (adaptive stopping rules) 以进一步优化推理速度。
- 开发适用于非单调解码路径的通用重用策略。
- 将 FP-MGM 扩展到多模态、视频等更复杂的生成任务。
- 研究效率提升与模型安全性、偏见、记忆化风险之间的关系。

</details>

---

### 10. [DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers](https://arxiv.org/abs/2605.30456)

**Authors**: Shraman Pal, Can Li  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.30456v1  

#### Abstract
Many learning tasks in science and engineering are characterized by sparse datasets, which limits the effectiveness of purely data-driven approaches. At the same time, these problems are often accompanied by rich domain knowledge derived from physical laws, operational requirements, and expert heuri...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
许多科学与工程领域的学习任务面临**小样本数据**和**分布偏移**的挑战，纯数据驱动的深度学习模型容易违反已知的物理规律、安全约束或专家规则。虽然领域知识常以逻辑命题和线性不等式形式存在，但现有神经符号（neuro-symbolic）方法通常存在以下缺陷：
- **软约束（Soft enforcement）**：通过损失函数中的惩罚项近似满足规则，无法保证推理时的精确可行性。
- **非可微后处理**：在推理阶段使用非可微的整数规划（ILP）解码，阻碍端到端训练。
- **输入无关规则**：假设规则是全局固定的，无法处理“if-then”型输入依赖规则。

### **提出的新方法**
本文提出了 **DisjunctiveNet**，一个统一的端到端框架，用于在神经网络中**强制执行硬性的、输入依赖的混合整数线性约束（Mixed-Integer Linear Constraints）**。其核心思想包括：
- **规则表示为析取约束（Disjunctive Constraints）**：将每条规则表示为多个线性不等式组的并集（即“有限个线性约束的析取”），对应于多面体的并集。
- **分层凸松弛（Hierarchical Convex Relaxations）**：采用**基本步层次（basic step hierarchy）**，从合取范式（CNF）到析取范式（DNF）进行凸化。
- **凸包重构（Convex Hull Reformulation）**：对 DNF 形式的约束进行凸包重构，得到一个**可微的线性规划（LP）层**，该层既能嵌入神经网络，又能**保证原始逻辑规则的精确满足**。

### **相比现有方法的优势**
| 特性 | DisjunctiveNet | 现有方法（如 Soft Penalty, SATNet, MultiplexNet） |
|------|----------------|-----------------------------------------------|
| **硬约束保证** | ✅ 是（通过 DNF 凸包） | ❌ 否（仅软约束或启发式松弛） |
| **输入依赖规则** | ✅ 支持 | ❌ 多数不支持或受限 |
| **端到端可微** | ✅ 是（通过隐式微分） | ⚠️ 部分支持（如 STE 或扰动优化，但效率低） |
| **逻辑表达能力** | ✅ 等价于 MILP 和 QF-LRA | ⚠️ 有限（如仅支持特定逻辑结构） |

> **关键优势**：DisjunctiveNet 是**首个**能在训练和推理过程中同时保证**硬约束满足**、**输入依赖性**和**端到端可微性**的方法。

---

## **2. 核心实验方法和设置**

### **使用的数据集**
1. **合成冷却控制任务（Synthetic Cooling-Control Problem）**
   - **任务**：预测风扇速度、制冷机水平、泵功率。
   - **规则**：7 条输入依赖的析取规则，例如“高温时需高制冷或高风速”、“需求响应事件时需限电”等。
   - **数据划分**：包含 **IID**（同分布）和 **OOD**（分布偏移）测试集，后者模拟极端工况。

2. **单细胞 RNA 测序分类（scRNA-seq Classification, PBMC3k 数据集）**
   - **任务**：基于基因表达数据分类 8 种细胞类型。
   - **规则**：输入依赖的**标记基因规则（marker-gene rules）**，形如 `G(x) ≥ T ⇒ ∃c ∈ C_r, y_c ≥ p`，即当某基因表达量达标时，必须有相关细胞类型的预测概率足够高。
   - **特点**：数据稀疏、高维、标注成本高。

### **实验设置和评估指标**
- **评估指标**：
  - **预测性能**：MSE（合成任务）、macro-F1（scRNA-seq）。
  - **约束满足率（CSAT）**：满足所有激活规则的样本比例。
- **训练策略**：
  - 所有投影方法（CNF/DNF）均从预训练的基础模型（base NN）进行**微调（fine-tuning）**，以隔离投影层的影响。
- **实现**：使用 Julia 实现，基于 `Flux.jl` 构建神经网络，`DiffOpt.jl` 实现可微优化层。

### **基线方法对比**
| 基线 | 描述 |
|------|------|
| **Base** | 无任何规则约束的神经网络。 |
| **Penalty (Pen)** | 在损失函数中加入规则软惩罚项。 |
| **Fine-tuned Penalty (Fine-Pen)** | 从 base 模型初始化，再用惩罚项微调。 |
| **Rules Only** | 忽略数据，仅随机选择可行规则组合（scRNA-seq）。 |
| **CNF / DNF** | 本文提出的不同松弛强度的投影方法。 |

---

## **3. 主要实验结果和性能指标**

### **关键性能数据**

#### **合成冷却任务（图 3, 4）**
- **CSAT**：
  - **DNF** 在 IID 和 OOD 上均达到 **接近 100%** 的约束满足。
  - **CNF** 满足率显著低于 DNF，尤其在 OOD 上表现更差。
- **MSE**：
  - **DNF 和 CNF** 的 MSE 显著低于 Base 和 Penalty 方法。
  - 在 OOD 设置下，投影方法优势更加明显，表明其具有更强的**泛化能力**。
- **顺序凸化（Sequential Convexification）**：
  - 随着更多规则从 CNF 转换为 DNF，CSAT 单调提升，MSE 下降。
  - 即使只转换少量规则，也能接近 DNF 性能，说明**部分 DNF 化即可捕获大部分逻辑结构**。

#### **scRNA-seq 分类任务（图 5, 表 8–12）**
- **CSAT**：
  - **DNF** 达到 **约 95%** 的约束满足率，远超 Base (~50%) 和 Penalty (~45%)。
  - **CNF** 约为 85%，优于软方法但低于 DNF。
- **Macro-F1**：
  - 在**小样本场景**（如 n=12, 23），**CNF 和 DNF 显著优于 Base 和 Penalty**，说明规则提供了强归纳偏置。
  - 随着数据量增加，Base 模型逐渐追上甚至超过投影方法，但**牺牲了规则满足率**。
- **规则质量验证**：
  - **Rules Only** 基线 F1 极低（~0.16），说明**仅靠规则无法完成准确分类**，必须与数据驱动结合。

### **消融实验结果**
- **CNF vs DNF**：
  - **DNF** 提供最紧的凸松弛，保证**精确规则满足**（Theorem 3.6）。
  - **CNF** 虽然计算高效（线性增长），但可能返回不满足原规则的解。
- **计算开销（表 1, E.3）**：
  - **Base/Penalty**：推理时间 <1 μs。
  - **CNF**：25.03 ms / 样本。
  - **DNF**：28.62 ms / 样本（稍慢，因枚举组合）。
  - 尽管 DNF 最坏情况指数增长，但实际中因许多交集为空，规模可控。

---

## **4. 关键结论和发现**

### **主要发现**
1. **投影层提供强归纳偏置**：在数据稀缺或分布偏移场景下，通过可微投影层融入领域知识，能显著提升模型的**预测性能**和**鲁棒性**。
2. **DNF 保证精确规则满足**：通过在引入 `l1` 投影变量后对 DNF 进行凸包重构，**最优极值点**必然落在原始可行集中，从而**严格满足所有逻辑规则**。
3. **存在精度-可行性权衡**：随着数据量增加，纯数据驱动模型可能在 F1 上超越投影模型，但会严重违反领域规则；而投影模型始终保证高 CSAT。
4. **顺序凸化实用性强**：可在 CNF 和 DNF 之间进行折衷，逐步将关键规则升级为 DNF，平衡计算复杂度与约束紧致性。

### **方法的局限性**
1. **计算复杂度**：
   - **DNF** 的 LP 规模随活跃规则数**指数增长**，在规则过多时不可行。
   - 当前依赖 Simplex 等返回极值点的求解器才能保证精确满足。
2. **规则冲突处理**：
   - 若输入导致规则冲突（可行集为空），当前方法绕过投影，可能导致训练不稳定。
   - 假设规则库是**经过良好验证**且冲突可监控的。
3. **非线性约束**：
   - 当前框架主要处理线性约束，对非线性（如二次、指数）支持有限。

### **未来工作方向**
1. **扩展至非线性约束**：将框架推广至包含凸非线性约束的析取规划，可能借助 SDP 或 SOCP 松弛。
2. **自适应顺序凸化**：设计智能策略（如基于规则重要性或交互强度）动态选择哪些规则进行 DNF 化。
3. **冲突感知学习**：引入机制自动检测、缓解或学习处理规则冲突。
4. **更高效的松弛**：探索近似但更快速的松弛方法，在大规模应用中保持实用性。

---

> **总结**：DisjunctiveNet 提出了一种新颖且严谨的框架，首次实现了在神经网络中**端到端地、精确地**满足**输入依赖的混合逻辑-数值约束**。其实验验证了该方法在小样本和分布外场景下的强大潜力，为科学机器学习中的**可信 AI** 提供了重要工具。

</details>

---

### 11. [Speculative Decoding Across Languages](https://arxiv.org/abs/2605.30580)

**Authors**: Nirajan Paudel, Michael Ginn, Luc De Nardi, Alexis Palmer  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.30580v1  

#### Abstract
Speculative decoding has become a crucial component of large language model (LLM) inference, enabling faster generation by drafting multiple tokens and verifying them in parallel. However, small draft models tend to suffer from disproportionately poor multilingual capabilities. Thus, when generating...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Speculative Decoding Across Languages**

---

## 1. **论文的主要贡献和创新点**

### ✅ 解决了什么问题
该论文聚焦于**多语言场景下 speculative decoding 效率低下**的问题。  
已知小规模 draft model 在非英语语言上的生成能力较差（Conneau et al., 2020），导致在非英语任务中 speculative decoding 的**acceptance rate 显著下降**，从而削弱甚至抵消其加速效果（Yi et al., 2024; Sandler et al., 2025）。此外，tokenization 偏向性使得低资源语言需要更多 tokens，进一步加剧延迟。

### 🚀 提出了什么新方法或新思路
作者系统比较了三种提升多语言 speculative decoding 效率的方法，并提出一个反直觉但有效的发现：

1. **Task-specific distillation**：在目标任务（如英→目标语翻译）上对 draft model 进行知识蒸馏。
2. **General-domain distillation**：在目标语言的单语语料上进行无监督蒸馏。
3. **N-gram draft models**：训练轻量级的 n-gram 模型作为 draft model —— 这是本文最具创新性的尝试。

> 💡 **核心洞见**：尽管 n-gram 模型的 acceptance rate 较低，但由于其推理速度极快（forward pass 时间远低于 LLM），整体仍能实现更高的 speed-up factor。

### 🔍 相比现有方法的优势
- **无需任务特定数据即可泛化**：n-gram 方法仅需单语语料，适用于缺乏平行数据的低资源语言。
- **跨任务鲁棒性强**：n-gram 和 general distillation 能在未见过的任务（如 story generation）上保持良好表现，而 task-specific distilled 模型严重过拟合训练任务。
- **实际部署更高效**：n-gram 模型前向耗时仅 ~0.001s，相比 0.8B LLM (~0.033s)，成本比 $ c = t_{\text{draft}} / t_{\text{target}} $ 极低，带来显著 speed-up。

---

## 2. **核心实验方法和设置**

### 📚 数据集
研究涵盖 **11 种语言**，覆盖不同资源水平、地理区域和语言类型：
- 包括：Amharic, Berber, Cherokee, Guarani, Hawaiian, Igbo, Nepali, Occitan, Quechua, Yoruba, Tamazight
- **机器翻译（MT）任务**：
  - 使用多源平行语料（Table 5），每种语言约 400–5200 条测试句。
  - 来源包括：Tatoeba, OPUS, MENYO-20k, Aya Dataset 等（详见 Table 3）。
- **故事生成（Story Generation）任务**：
  - 构造主题：结合 GloVe 向量匹配名词与形容词（如 “sunlit garden”、“vibrant festival”）。
  - 提示模型用目标语言写故事，共 200 个测试样例。
- **单语语料用于蒸馏与 n-gram 训练**：
  - 规模从数万到千万 token 不等（Table 4），来源如 Leipzig Corpus, Hawaiian Corpus Project 等。

### ⚙️ 实验设置
- **Verifier Model**：Qwen 3.5 9B
- **Draft Models**：
  - Baseline：Qwen 3.5 0.8B（未经微调）
  - Distilled (task)：在翻译任务上蒸馏的 0.8B 模型
  - Distilled (general)：在单语文本上蒸馏的 0.8B 模型
  - N-gram model：基于相同单语文本训练的 bigram 模型（使用 Qwen tokenizer 分词）
- **解码参数**：
  - Top-k=100, top-p=0.9, max 128 tokens
  - 使用 KV caching 加速
  - 对 speculative length $ y \in \{2,3,4\} $ 做超参搜索，报告最优结果

### 📊 评估指标
| 指标 | 定义 |
|------|------|
| **Acceptance Rate ($ \alpha $)** | 被 verifier 接受的 draft token 占比（Monte Carlo 估计） |
| **Speed-up Factor ($ f $)** | 理论加速倍数：<br>$ f = \frac{1 + y(1 - \sqrt[y]{1-\alpha})}{(1 - \alpha)(y c + 1)} $<br>其中 $ c = t_{\text{draft}} / t_{\text{target}} $ |
| **Tokens/sec** | 实际吞吐量（implementation-agnostic 性能度量） |

### 🔁 基线方法对比
| 方法 | 是否任务相关 | 是否需标注数据 | 泛化能力 |
|------|---------------|------------------|-----------|
| Baseline (0.8B) | ❌ | ❌ | 中等 |
| Distilled (task) | ✅ | ✅（需平行语料） | 差（domain-specific overfitting） |
| Distilled (general) | ❌ | ✅（只需单语） | 较好 |
| N-gram model | ❌ | ✅（只需单语） | 最佳（尤其在 cost-sensitive 场景） |

---

## 3. **主要实验结果和性能指标**

### 📈 关键性能数据（平均值）

| 方法 | Acceptance Rate (MT) | Speed-up (MT) | Acceptance Rate (Story) | Speed-up (Story) |
|------|------------------------|----------------|----------------------------|--------------------|
| Baseline (0.8B) | 0.40 | 1.02× | 0.46 | 1.09× |
| Distilled (task) | **0.60** | **1.28×** | 0.43 | 1.03× |
| Distilled (general) | 0.39 | 1.03× | 0.47 | 1.10× |
| **N-gram model** | 0.24 | **1.30×** | 0.30 | **1.39×** |

> ✅ **n-gram 模型虽 acceptance rate 最低，但 speed-up 表现最佳！**

### 🔬 详细分析与对比
- **Translation Task**：
  - Task-specific distillation 显著提升 acceptance rate（↑50%），但在 story generation 上性能退化。
  - N-gram 模型 acceptance rate 仅为 0.24，但因其 forward pass 时间极短（0.001s vs. 0.033s），**cost ratio $ c \approx 0.03 $**，极大提升了 speed-up。
- **Story Generation（out-of-domain）**：
  - Task-specific 模型表现最差（speed-up 仅 1.03×），说明严重过拟合。
  - N-gram 模型在所有语言中除 oci 外均优于 baseline，达到 **1.39× 平均 speed-up**。
- **Throughput（Tokens/sec）**：
  - 图 7 显示 n-gram 在两个任务上都实现了最高的 token 输出速率。

### 🔍 消融实验结果
#### D.3 Draft Model Size（0.8B vs 2B vs 4B）
- 更大的 draft model（2B/4B）通常带来更高 acceptance rate 和 speed-up。
- 但在某些语言（如 amh）上，最大模型反而出现 speed-up 下降，表明存在收益递减。

#### D.5 Distillation Lower Bound
- 利用 KL 散度推导出 acceptance rate 的理论下界：  
  $ \alpha \geq 1 - \sqrt{2 D_{KL}(P \| Q)} $
- 实验验证显示所有蒸馏模型均远超此下界，说明当前 distillation 方法仍有优化空间。

---

## 4. **关键结论和发现**

### ✅ 主要发现
1. **标准 speculative decoding 在非英语语言中效率低下**：
   - 平均 acceptance rate 仅 ~0.4，speed-up 接近 1×，几乎无加速效果。
2. **Task-specific distillation 可提升 in-domain 性能，但泛化能力差**：
   - 在 translation 上有效（↑1.28×），但在 story generation 上退化至不如 baseline。
3. **N-gram draft models 是跨领域高效的替代方案**：
   - 尽管 acceptance rate 低，但因 inference 成本极低，**综合 speed-up 最高（达 1.39×）**。
   - 特别适合有单语语料但缺乏标注数据的低资源语言。
4. **动态切换 draft model 是理想策略**：
   - 根据任务和语言选择最优 draft model（例如：高资源+固定任务用 distilled；通用场景用 n-gram）。

### ⚠️ 局限性
- 所有实验基于 **Qwen 3.5 系列模型**，结果可能不完全迁移到其他架构（如 Llama 或 Mistral）。
- 仅测试 **11 种语言**，且均为现实世界中已有一定数据支持的语言，极端低资源语言（如 <1k tokens）未覆盖。
- 任务范围有限：仅评估 MT 和 story generation，未涉及数学推理、代码生成等复杂任务（参考 Sandler et al., 2025）。
- 生成质量未被量化：作者承认生成内容“very poor quality”，主要关注速度而非语义正确性。

### 🔮 未来工作方向
- 探索 **混合 draft system**：运行时自动选择最佳 draft model（n-gram / distilled / LLM）。
- 设计 **轻量可训练 draft module**：如小型适配器（LoRA）+ 缓存机制，兼顾灵活性与速度。
- 扩展至 **语音、图像等多模态 speculative decoding**。
- 结合 **language-aware tokenization 优化**，缓解 token 数量偏差带来的不公平性（Petrov et al., 2023）。

---

> 📢 **一句话总结**：  
> 在多语言 speculative decoding 中，**不是 accept 更多就好**，而是要追求 **cost-aware efficiency** —— n-gram 模型以极低成本实现最高 speed-up，为低资源语言提供了实用且可扩展的解决方案。

</details>

---

### 12. [dMoE: dLLMs with Learnable Block Experts](https://arxiv.org/abs/2605.30876)

**Authors**: Sicheng Feng, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.30876v1  

#### Abstract
Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive models, offering competitive performance while naturally supporting parallel decoding. However, as dLLMs are increasingly integrated with Mixture-of-Experts (MoE) architectures to scale model c...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：dMoE: dLLMs with Learnable Block Experts

---

## 1. 论文的主要贡献和创新点

### ✅ 解决了什么问题

在 **Diffusion Large Language Models (dLLMs)** 中，随着 **Mixture-of-Experts (MoE)** 架构的引入以扩展模型容量，出现了一个根本性的效率瓶颈：  
- dLLMs 在推理时采用 **block parallel decoding**，即一次处理多个具有双向依赖关系的 token；
- 而传统的 MoE 路由机制是基于 **token-level expert selection**，即每个 token 独立选择专家。

这种“**块级并行解码”与“token级路由”的不匹配**导致：
- 单次前向传播中激活的 **unique experts 数量急剧增加**；
- 推理过程严重受制于 **memory access overhead**，成为主要瓶颈。

---

### ✅ 提出了什么新方法或新思路

作者提出 **dMoE** —— 一种简单而有效的 **block-level MoE 框架**，其核心思想是：

> 将 token-level 的专家分布聚合为 **block-level 的统一专家分布**，并以此指导整个 block 的专家路由，实现更一致、更高效的专家选择。

具体设计包括：
- **Token-level expert score aggregation**：对 block 内所有 token 的 router 权重进行求和归一化，得到 block-level expert scores。
- **Top-p 动态 coreset 选择**：基于 block-level 分数，使用 top-p 准则动态确定候选专家子集（coreset），避免固定大小带来的僵化。
- **Coarse-to-fine routing**：先在 block 级别筛选出共享的专家池，再在此池内执行原始 token-level 路由。
- **Self-distillation 训练范式**：训练时使用相同的路由流程，确保训练与推理一致性。

---

### ✅ 相比现有方法的优势

| 方面 | dMoE 的优势 |
|------|-------------|
| **效率提升** | 显著减少 unique expert 数量，缓解 memory-bound 问题 |
| **性能保持** | 几乎无损保留原模型性能（达 99.11%） |
| **动态适应性** | top-p 设计能自适应不同 denoising step 和 block 的路由集中度变化 |
| **无需额外训练开销** | 方法轻量，仅需微调，兼容性强 |
| **优于近期基线** | 相比 DES 等方法，在同等压缩率下性能下降更小 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

- **MATH500**：数学推理任务
- **GSM8K**：小学数学应用题
- **ARC-C**：科学常识推理
- **MMLU**：多学科知识理解（文中使用其 math 子集）

> 所有数据均通过 **self-distillation** 从 LLaDA2.0-mini 自生成构建，约 700K 样本。

---

### ⚙️ 实验设置和评估指标

| 设置项 | 配置 |
|--------|------|
| **Base Model** | LLaDA2.0-mini（开源 MoE dLLM） |
| **Training** | 微调 2 轮，batch size=4，lr=2e-6，cosine schedule，H100×4 |
| **Block Size** | 32（默认） |
| **Masking Ratio** | [0.3, 0.8] 随机采样 |
| **Top-p threshold** | 训练时设为 0.6 |
| **Inference** | Block diffusion + confidence-based parallel decoding，max len=2048，confidence threshold=0.95 |

#### 评估指标：
- **Accuracy**：各 benchmark 上的准确率
- **Unique Expert Count**：每层平均激活的独特专家数量
- **Memory Footprint**：MoE 参数的显存占用
- **End-to-End Latency**：总推理延迟及 MoE kernel 延迟
- **Speedup**：相比原模型的端到端加速比

---

### 🔁 基线方法对比

| 基线 | 描述 |
|------|------|
| **Original** | 官方配置下的原始 MoE dLLM |
| **Top-4** | 每个 token 只选 4 个专家（而非 8 个） |
| **DES-S** | Sequence-level routing（本文复现） |
| **DES-V** | Vote-based block-level routing（本文复现） |
| **DES-S\*/DES-V\*** | 调整阈值以达到与 dMoE 相当的压缩率 |

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（平均 across 四个 benchmark）

| 指标 | 原始模型 | dMoE (ours) | 提升/降低 |
|------|--------|-----------|----------|
| **Unique Expert Count** | 69.5 | **14.6** | ↓ **79.04%** |
| **Performance Retention** | 83.95% | **83.2%** | 保留 **99.11%** |
| **Memory Usage** | - | ↓ **76.64% ~ 79.84%** | 显著降低 |
| **End-to-End Latency Speedup** | 1.00× | **1.14× ~ 1.66×** | 最高提速 66% |

> 数据来源：Table 2, Figure 5

---

### 🔍 与基线方法的对比结果

| 对比维度 | 结果 |
|---------|------|
| **相同性能水平下** | dMoE 激活专家数比 DES-V 少 **~60–66%** |
| **相同压缩率下（如 ~13 experts）** |  
| - DES-S\*/DES-V\* | 性能大幅下降（仅保留 ~70–75%）  
| - **dMoE (p=0.5)** | 仍保留 **97.5%** 性能 → **显著更优** |
| **极限压缩能力** | dMoE 可压缩至接近理论下限（8 experts/token），仍保持强性能 |

> 图表支持：Figure 6 展示了 dMoE 在 **performance-efficiency trade-off** 上全面领先。

---

### 🔬 消融实验结果

#### ✅ Ablation on Top-p Threshold (`p_train`, `p_test`)

| `p_test` | Unique Experts | Accuracy | 观察 |
|--------|----------------|----------|------|
| 0.4 | 10.3 | 69.8% | 极高压缩，轻微掉点 |
| 0.6 | 14.1 | 71.0% | 平衡点，接近原模型 |
| 0.8 | 27.1 | 74.2% | 几乎无损，压缩有限 |

> 表明 dMoE 具备良好的 **tunability**，可根据硬件资源灵活调节压缩强度。

#### ✅ Ablation on Block Size

| Block Size | 原始专家数 | dMoE 专家数 | 压缩率 | 性能保留 |
|------------|------------|--------------|--------|----------|
| 8 | 31.5 | 14.2 | ↓54.9% | 100% |
| 16 | 48.6 | 15.9 | ↓67.3% | 100.6% |
| 24 | 60.7 | 15.4 | ↓74.6% | 99.5% |
| 32 | 70.0 | 14.1 | ↓79.0% | 99.1% |

> 表明 dMoE 在不同 block size 下均有效，且大 block 更利于聚合增益。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **MoE latency 是 dLLMs 的主要瓶颈**  
   - 实验表明 MoE 占据主导延迟（Figure 2），且与 unique expert count 呈线性正相关。

2. **Token-level routing 在 dLLMs 中存在冗余**  
   - 多个 token 同时激活大量不同专家，造成内存浪费。

3. **Block-level aggregation 是高效且可行的替代方案**  
   - 利用 block 内 token 的共性，可大幅压缩专家集合而不影响性能。

4. **dMoE 实现了近乎无损的极端专家压缩**  
   - 平均激活专家数从 69.5 → 14.6，性能保留率达 **99.11%**。

5. **dMoE 具备良好 tunability 与泛化性**  
   - 可通过调整 `p` 控制压缩程度，适用于不同场景需求。

---

### ⚠️ 方法的局限性

- 当前验证集中在 **language-only** 模态，尚未拓展至 multimodal（如 image/video diffusion）。
- 聚合方式较简单（sum + normalize），未探索更复杂的 attention 或 gating 机制。
- 依赖 self-distillation 进行训练信号构建，可能限制在低质量生成上的表现。

---

### 🔮 未来工作方向（来自 Appendix A）

1. **扩展至其他模态**  
   - 应用于视觉问答（VQA）、视频生成等 multimodal dLLMs。

2. **进一步压缩策略**  
   - 探索让 block 内所有 token **共享同一组专家**（extreme grouping）。
   - 结合 **fewer experts per token**，联合优化计算与内存。

3. **更智能的 block-level routing 机制**  
   - 引入轻量预测模块动态决定是否启用 block-level 路由。

4. **系统级协同优化**  
   - 与 SGLang、Tensor Parallelism 等推理框架深度集成，最大化实际部署收益。

---

> ✅ **代码已开源**：[https://github.com/fscdc/dMoE](https://github.com/fscdc/dMoE)

</details>

---

### 13. [Augmented Lagrangian Predictive Coding](https://arxiv.org/abs/2605.31022)

**Authors**: Jeffrey Seely, Julian Gould  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.31022v1  

#### Abstract
Predictive coding (PC) is a local-learning alternative to backpropagation (BP), training deep networks via local energy-minimization dynamics rather than a global backward pass. We introduce Augmented Lagrangian Predictive Coding (PC-ALM), which maintains PC's inference budget but aligns each weight...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# Augmented Lagrangian Predictive Coding 论文总结

## 1. 论文的主要贡献和创新点

### 解决的问题
现代深度学习依赖 **Backpropagation (BP)** 进行训练，但其全局性（如需要精确的转置权重进行梯度反传）使其在生物神经系统中难以实现。**Predictive Coding (PC)** 作为一种局部学习替代方案，通过能量最小化动态实现层本地更新，但其梯度信号与 BP 存在偏差，尤其在**深层窄网络**（deep narrow networks）中性能显著落后于 BP。

本文旨在解决这一“**PC-BP gap**”问题，即如何在保持 PC 局部性的同时，使学习信号更精确地对齐 BP。

### 提出的新方法：PC-ALM
作者提出了 **Augmented Lagrangian Predictive Coding (PC-ALM)**，这是一种将 PC 置于增广拉格朗日（Augmented Lagrangian, AL）框架下的新方法。

- **核心思想**：PC-ALM 在每个隐藏层引入一个与激活同形状的**层本地拉格朗日乘子**（Lagrange multiplier, `λ`）。该乘子通过双上升法（dual ascent）累积每层的预测误差（prediction error），并将其反馈到局部激活更新中。
- **机制**：在有限推理步数（finite inference budget）内，PC-ALM 交替执行：
  1. **Primal Step**：基于增广拉格朗日函数更新激活状态。
  2. **Dual Step**：更新拉格朗日乘子 `λ ← λ + α * (h - φ(Wh₋₁))`，其中 `α` 是对偶学习率。
- 最终的权重更新基于复合信号 `λ + p*r`（`r` 为最终预测误差，`p` 为惩罚强度）。

### 相比现有方法的优势
- **理论对齐**：在**线性网络**中，PC-ALM 能收敛到与 BP 完全一致的梯度。
- **性能提升**：在非线性网络中，PC-ALM 显著缩小甚至消除了 PC 与 BP 的性能差距，尤其是在 PC 表现最差的深层窄网络上。
- **动力学优势**：相比 PC 缓慢的“扩散式”信用传播（diffusive credit propagation），PC-ALM 实现了更快的“弹道式”信用传播（ballistic credit propagation），信用信号能更均匀、快速地分布到整个网络。
- **计算效率**：相比通过加宽网络来逼近 BP 性能的策略，PC-ALM 在固定宽度下通过增加推理步骤即可达到高对齐度，计算资源利用更高效。

---

## 2. 核心实验方法和设置

### 数据集
- **Fashion-MNIST**
- **MNIST**

### 实验设置和评估指标
- **模型架构**：使用 **Residual MLP** 架构，深度 `L` 和宽度 `N` 在 `{8, 16, 32, 64, 128}` 范围内进行网格搜索 `(N, L) ∈ {8, ..., 128}²`。
- **非线性函数**：测试了 `identity`, `tanh`, `ReLU` 三种激活函数。
- **参数初始化**：采用 Innocenti et al. [2026] 提出的 **mean-field parameterization** 来稳定训练。
- **推理预算**：固定推理步数 `T`，与标准 PC 保持一致（例如 `T = L` 或 `T = 2L`）。
- **评估指标**：
  - 分类准确率（间接反映）。
  - **BP 对齐度**（cosine similarity）：计算 PC-ALM 权重更新方向与真实 BP 梯度方向之间的余弦相似度，这是衡量方法有效性的核心指标。
  - 训练曲线（loss/accuracy 随优化步的变化）。

### 基线方法对比
- **Backpropagation (BP)**：作为性能上限的黄金标准。
- **Standard Predictive Coding (PC)**：作为直接对比的基线方法。
- **PC-ALM**：本文提出的方法。

---

## 3. 主要实验结果和性能指标

### 关键性能数据与对比结果
- **图2 & 图9**：在 Fashion-MNIST 和 MNIST 上，当推理预算为 `T = 2L` 时，**PC-ALM 在所有宽度-深度组合和激活函数下均能完全匹配 BP 的性能**。而标准 PC 在深层窄网络（如 `L=128, N=32`）中性能显著下降。
- **图10**：在 `N=32, L=64` 的设定下，即使在较小的推理预算 `T=64` 下，PC-ALM 的训练曲线也明显优于 PC；当 `T=128` 时，其性能已非常接近 BP。
- **图5**：展示了 PC-ALM 的 BP 对齐度随推理步数的增长。在推理步数约为 `2L` 时，对齐度出现一个明显的“拐点”（inflection point），迅速提升至接近 1.0，表明此时已获得高质量的 BP 对齐梯度。

### 消融实验结果
- **对偶学习率 `α` 的影响**：实验发现 `α` 控制着对齐度拐点出现的位置。较高的 `α` 会使拐点提前（在更少的推理步后达到高对齐度），这与理论预测 `t ~ L / (α√η)` 一致。
- **参数化鲁棒性**：在 **图6 & 图7** 中，作者在 `(N, L)=(32,64)` 固定的情况下，沿“标准参数化到平均场”和“惰性到丰富”两个轴进行插值。结果显示，**PC-ALM 在所有参数化设置下都能稳定跟踪 BP 的性能**，而 PC 在“丰富”参数化区域开始落后，证明了 PC-ALM 更强的鲁棒性。
- **计算效率**：**图8** 对比了两种逼近 BP 的路径：1) 加宽 PC 网络；2) 使用固定宽度的 PC-ALM 并增加推理步数。结果显示，PC-ALM 达到 0.9 的 BP 对齐度所需的计算量（FLOPs）比加宽网络的策略低一个数量级，证明了其更高的效率。

---

## 4. 关键结论和发现

### 主要发现
1.  **理论收敛性**：在**线性网络**中，PC-ALM 的动力学被证明是稳定的，并且能够收敛到与 BP 完全等价的梯度解。
2.  **消除 PC-BP Gap**：在非线性网络中，PC-ALM 成功弥合了 PC 与 BP 之间的性能差距，特别是在深层窄网络这一关键挑战场景下表现卓越。
3.  **新型信用传播机制**：PC-ALM 引入了“**弹道式信用传播**”（ballistic credit propagation）。其复合信号 `λ + p*r` 能够像波前一样快速、均匀地在整个网络中传播，克服了标准 PC 信用信号衰减和集中于输出层附近的“瓶颈”问题。
4.  **高效的局部学习**：PC-ALM 证明了通过简单的层本地动态（primal-dual updates），可以在不牺牲生物合理性的前提下，高效地计算出与 BP 高度对齐的学习信号。

### 方法的局限性
- **理论限制**：目前的收敛性证明和信用波分析仅限于**线性激活函数**和**无偏置项**的网络。对于通用非线性网络（尤其是 ReLU）的严格收敛保证仍是开放问题。
- **实验范围**：实验集中在 **MNIST/Fashion-MNIST** 和 **Residual MLP** 上，缺乏在更大规模数据集（如 ImageNet）、更复杂架构（如 CNN, Transformer）以及多轮完整训练上的验证。
- **内存开销**：由于需要存储每个样本的拉格朗日乘子 `λ`，PC-ALM 的激活内存成本大约是标准 PC 的两倍。
- **未解决的生物学问题**：虽然解决了局部性问题，但仍未解决 **weight transport problem**（权重传输问题），因为梯度计算仍需使用权重矩阵的转置。

### 未来工作方向
- 将 PC-ALM 框架扩展到卷积神经网络（CNN）、注意力机制（Attention）等更复杂的网络架构。
- 探索无需权重转置的变体，以进一步提高生物合理性。
- 在更大规模的数据集和任务上进行全面评估。
- 研究 PC-ALM 在非前馈图（如循环网络）中的应用潜力。
- 深入分析非线性网络中 PC-ALM 的动力学行为，如极限环等复杂现象。

</details>

---

### 14. [EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs](https://arxiv.org/abs/2605.30637)

**Authors**: Yuzhang Xie, Keqi Han, Yunpeng Xiao, Hejie Cui, Guanchen Wu, Ziyang Zhang, Kai Shu, Jiaying Lu, Xiao Hu, Carl Yang  
**Category**: cs.AI  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.30637v1  

#### Abstract
Clinical decision-making (CDM) is central to real-world clinical workflows, where clinicians infer diagnoses, select treatments, or anticipate future health outcomes under incomplete evidence. LLMs are increasingly used to support these decisions due to strong language capabilities, broad biomedical...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前在评估大型语言模型（LLMs）用于**临床决策支持**（Clinical Decision Making, CDM）时存在以下挑战：
- 大多数医学QA基准依赖于教科书、考试题或人工标注，规模小且成本高；
- 现有基于电子健康记录（EHR）的基准多侧重于**信息检索**（如text-to-SQL），而非需要深度推理的**诊断、治疗选择和预后预测**等真实临床任务；
- LLM生成的基准易产生**幻觉**（hallucination），缺乏可靠性验证。

### 提出的新方法与思路
本文提出 **EHRBench** —— 一个自动化、可靠、基于真实EHR数据的大规模临床决策基准，其核心是 **EHR-LLM-KB 交互流水线**：
- **EHR → LLM**：利用专门的医学LLM从原始结构化EHR轨迹中提取潜在的临床关系（如“糖尿病 → 导致 → 肾病”）；
- **LLM → KB**：通过外部生物医学知识库（如UMLS、SemMedDB）对提取的关系进行**系统性验证与增强**，过滤不成立或模糊的关联；
- **模板实例化**：将验证后的模板确定性地转化为多种格式的QA项（MCQ、OEQ），确保多样性与可复现性。

### 相比现有方法的优势
| 维度 | 传统方法 | EHRBench |
|------|--------|----------|
| **数据来源** | 教科书、专家标注 | 真实世界结构化EHR（MIMIC-III/IV, PROMOTE） |
| **构建方式** | 手动标注为主 | 自动化LLM生成 + KB验证 |
| **任务设计** | 阅读理解、事实问答 | 三大推理型CDM任务：诊断、治疗、预后 |
| **可靠性保障** | 依赖专家 | KB驱动的验证与过滤机制 |
| **规模** | 数百至数千 | 近百万（960,067）QA项 |

---

## 2. 核心实验方法和设置

### 数据集
- **MIMIC-III**（1.4版）：38,597患者，53,423次住院
- **MIMIC-IV**（3.1版）：364,627患者，546,028次住院
- **PROMOTE**（私有数据集）：18,561患者，912,706条记录  
所有数据均经过去标识化处理，并通过伦理审查。

### 实验设置与评估指标
#### 三大临床决策任务
| 任务 | 定义 | 示例 |
|------|------|-------|
| **Diagnosis**（诊断） | 在同一就诊中，根据已有诊断推断共病 | 已知“2型糖尿病”，推断“糖尿病肾病” |
| **Treatment**（治疗） | 根据诊断选择合适的治疗方案 | “房颤” → “抗凝治疗” |
| **Prognosis**（预后） | 根据前次就诊情况预测下一次就诊可能出现的诊断 | “高血压+高脂血症” → “缺血性卒中风险” |

#### QA格式
- **Multiple-Choice Questions (MCQ)**：4/5/6选1
- **Open-Ended Questions (OEQ)**：自由文本回答 + 解释

#### 评估指标
- **MCQ**：准确率（Accuracy）
- **OEQ**：
  - **Coverage (RC)**：是否覆盖目标临床关系
  - **ROUGE-1/L**：与参考答案的词法重叠
  - **BERTScore**：语义相似度

### 基线方法对比
共评测 **31个代表性LLM**，分为三类：
1. **开源通用LLM**：`llama3`, `qwen`, `glm4`, `mistral` 系列
2. **医学专用LLM**：`doctor-r1`, `med42`, `ultramedical`, `m1` 系列
3. **HIPAA合规API模型**：`gpt-4.1`, `gpt-5`, `gpt-5.2`

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自Table 1）

| 模型 | Overall Acc (%) | Rank Avg | Dx (%) | Tx (%) | Px (%) |
|------|------------------|---------|--------|--------|--------|
| **gpt-5.2** | **70.91** | **1.69** | 72.02 | 80.13 | 60.59 |
| gpt-4.1 | 69.43 | 2.51 | 69.87 | 80.10 | 58.33 |
| gpt-5 | 69.06 | 3.21 | 68.26 | 80.45 | 58.46 |
| **llama3.3-70b** | 67.28 | 5.23 | 68.35 | 79.05 | 54.44 |
| **qwen3-32b** | 66.78 | 6.54 | 67.97 | 77.34 | 55.04 |

> ✅ **gpt-5.2** 表现最佳，尤其在**治疗任务**上达到 **80.13%** 准确率。

### 与基线方法的对比结果
- **API模型显著优于开源模型**：`gpt-5.2` 比最强开源模型 `llama3.3-70b` 高约 **3.6个百分点**。
- **医学微调模型未普遍优于基础模型**：
  - `m1-32b-1k`（医学微调） vs `qwen2.5-32b`（基础）：63.21% vs 64.97%
  - 表明当前医学领域适配未能有效提升EHR推理能力。
- **任务难度差异明显**：
  - 平均准确率排序：**Tx (69.33%) > Dx (55.02%) > Px (46.67%)**
  - 治疗任务相对直接（药物-适应症关系明确），而预后预测最难（需长期因果推理）。

### 消融实验与鲁棒性分析
#### （1）不同选项数量的影响
- 准确率随选项增加单调下降：
  - 4选1：62.29%
  - 5选1：56.69%
  - 6选1：52.04%
- 说明EHRBench能合理控制题目难度。

#### （2）不同QA生成LLM的影响（E.6节）
- 更换模板生成器（HuatuoGPT vs m1-7b-23k）后，模型排名高度一致（Kendall’s W = 0.937）
- 证明结果**不依赖特定LLM生成器**

#### （3）上下文事件数影响（E.7节）
- 将上下文事件从2个增至6个，模型相对排名不变
- 表明结论对局部上下文长度具有鲁棒性

#### （4）非LLM基线对比（E.5节）
| 模型 | Overall Acc (%) |
|------|------------------|
| SapBERT | 16.5 |
| PubMedBERT | 32.8 |
| llama3-8b | 43.8 |
| gpt-5.2 | 66.8 |
- 嵌入检索模型远低于LLM，表明EHRBench测试的是**推理能力**而非简单匹配。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **EHRBench具备高可靠性与有效性**：
   - 模型表现符合预期能力趋势（gpt-5.2 > gpt-4.1 > llama系列）
   - 支持跨数据源、跨任务、跨格式的一致评估
2. ✅ **治疗任务最容易，预后最难**：
   - 反映真实临床复杂性：治疗指南较明确，而疾病进展更具不确定性
3. ❌ **当前医学微调策略未能显著提升EHR推理性能**
   - 医学LLM在格式输出稳定性上甚至不如通用模型（见`med42-8b`高达25.28%输出错误）
4. ✅ **强LLM在开放问答中也表现出色**：
   - `qwen2.5-32b` 在OEQ上达到 **68.24% RC** 和 **56.25% BERTScore**
   - 显示其具备生成合理临床解释的能力

### 方法的局限性
1. **模态受限**：仅使用结构化诊断、处方、手术，未包含实验室检查、生命体征、影像等重要信息。
2. **上下文窗口固定**：每个问题仅使用少量上下文事件（通常2个），限制了长程依赖建模。
3. **知识库覆盖偏差**：KB验证虽提高精度，但也可能排除一些合理但未被收录的临床实践（如新兴疗法）。
4. **计算成本高**：完整评估近百万QA项对大多数研究者不可行，故采用子集评估。

### 未来工作方向
- 引入更多模态（lab, vitals, imaging）构建多模态EHRBench
- 支持更复杂的**时间序列推理**与**个性化风险预测**
- 开发面向**罕见病**和**个体化医疗**的评估子集
- 探索基于agent的动态交互式评估框架（如模拟医生问诊流程）

---

> 🔗 **资源公开**：EHRBench的代码与数据已开源，详见 [GitHub链接](https://github.com/constantjxyz/EHRBench)

</details>

---

### 15. [Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination](https://arxiv.org/abs/2605.31058)

**Authors**: Jiasheng Zheng, Boxi Cao, Boxi Yu, Yuzhong Zhang, Jialun Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.31058v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) has recently emerged as the cornerstone for shaping the remarkable coding abilities of Large Language Models (LLMs). However, the scalability of RLVR is severely constrained by the scarcity of sufficiently challenging verifiable code tasks that t...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
- **RLVR（Reinforcement Learning with Verifiable Rewards）的数据瓶颈**：尽管 RLVR 已成为提升大语言模型（LLMs）代码能力的关键范式，其可扩展性受限于高质量、高难度且具备可验证测试用例的代码任务稀缺。
- 现有合成方法（如 heuristic seed expansion）仅在语言层面进行扩展，未能突破原始任务的逻辑结构，导致生成的任务缺乏新颖性和挑战性，无法有效推动模型在边缘能力上的探索。

### 提出了什么新方法或新思路
提出 **Atomic Decomposition and Recombination (ADR)** 框架，一种全新的可验证代码任务合成范式：
- **原子分解（Atomic Decomposition）**：将种子任务按预定义的 schema 分解为语义原子元素（如算法思想、输入接口、约束条件等），并通过信息论信号（熵 H 和条件互信息 CMI）自动优化 schema。
- **受控重组（Controlled Recombination）**：以核心元素（core element）为基础，结合示例组合，引导 LLM 进行跨域逻辑元素的可控重组，生成结构上新颖的任务。
- **执行驱动验证（Execution-grounded Validation）**：自动生成 solution code 和 test case generator，并通过沙箱执行过滤无效或不可解任务。
- **对抗性解决方案空间优化（Adversarial Solution Space Refinement）**：生成“近似正确”的错误解（near-miss solutions），并迭代优化测试用例以提高对边界情况的覆盖率。

### 相比现有方法的优势
| 维度 | ADR | 现有方法（如 KodCode, Educational Instruct） |
|------|-----|---------------------------------------------|
| **原创性（Originality）** | 高，通过元素交叉实现结构性创新 | 低，局限于局部修改和语言扰动 |
| **难度（Difficulty）** | 显著更高，逼近模型能力边界 | 接近种子数据分布，难以超越 |
| **多样性（Diversity）** | 更均匀覆盖长尾区域 | 聚焦高密度区域，采样保守 |
| **测试质量（Test Quality）** | 高边界覆盖率，经对抗优化 | 测试简单，易被错误解绕过 |

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **种子数据集（Seed Datasets）**：
  - **TACO**：用于算法编程任务，选取中等及以上难度的 1,710 个问题作为种子。
  - **Package Instruct**：用于工具调用和数据科学任务，随机抽取 5,000 条作为种子。
- **合成数据规模**：
  - 算法任务：从 TACO 种子生成 5,000 条 ADR 合成数据。
  - 工具使用 & 数据科学：各生成 2,000 条。
- **评估基准**：
  - **LiveCodeBench (LCB-v5/v6)**：评估算法编程能力。
  - **BigCodeBench**：评估复杂指令遵循与工具调用能力。
  - **DS-1000**：评估数据科学库使用能力。

### 实验设置和评估指标
#### 评估维度（四维评价体系）
| 指标 | 定义 |
|------|------|
| **Originality** | 与参考数据集（PrimeIntellect/verifiable-coding-problems）的余弦相似度低于阈值的比例，衡量新颖性 |
| **Difficulty** | 多个参考模型（Qwen3-4B/8B/14B）在该数据上的平均表现，越低表示越难 |
| **Diversity** | 最近邻距离的变异系数倒数，反映数据分布均匀性 |
| **Test Quality** | 使用 LLM-as-a-Judge 对测试用例的多样性和边界覆盖打分 |

#### RLVR 训练设置
- **算法**：GRPO（Generalized Reward Policy Optimization）
- **训练步数**：10 epochs，global batch size=128
- **采样策略**：每题 8 rollouts，max response length=8192
- **基础模型**：
  - Qwen2.5-Coder-7B-Instruct
  - Llama-3.1-8B-Instruct
  - Qwen3-8B（Non-thinking）

### 基线方法对比
| 基线类型 | 具体方法 |
|--------|---------|
| **真实数据基线** | TACO（直接用于训练） |
| **合成数据基线** | KodCode、Educational Instruct |
| **无思考模式对比** | Base model without RL |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（Pass@1 %）

#### 表：算法任务性能对比（LCB-v5 / LCB-v6）
| Model | LCB-v5 | LCB-v6 | Average |
|-------|--------|--------|---------|
| Qwen2.5-Coder-7B-Instruct (Base) | 16.17 | 20.21 | 18.19 |
| + TACO (Real) | 22.60 | 23.86 | 23.23 |
| + Educational Instruct (Synthetic) | 19.61 | 21.71 | 20.66 |
| + KodCode (Synthetic) | 22.75 | 23.57 | 23.16 |
| **+ ADR (Ours)** | **25.37†** | **26.14†** | **25.76** |

> † 表示相比所有基线 p < 0.001（McNemar’s test）

#### 表：跨领域性能对比
| Task | Metric | KodCode | ADR (Ours) | Δ |
|------|--------|--------|------------|----|
| Tool Usage (BigCodeBench) | Pass@1 | 41.27 | **41.67** | +0.40 |
| Data Science (DS-1000) | Pass@1 | 39.05 | **42.44** | +3.39 |

### 与基线方法的对比结果
- **ADR 显著优于所有基线**：
  - 在 Qwen2.5-Coder-7B 上，相比最强基线 KodCode 提升 **+2.61% Pass@1**（LCB-v5）。
  - 在 Llama-3.1-8B 上，性能提升达 **+7.38%**，显示强泛化能力。
- **突破原有数据上限**：
  - 现有合成方法无法超越原始真实数据（TACO）性能，而 ADR 不仅超越 TACO，还显著拉开差距。
- **提升模型推理深度**：
  - 如图所示，在 **Pass@8** 指标上，ADR 实现 **+4.79%** 提升，而 KodCode 仅 **+0.60%**，说明 ADR 能真正拓展模型的能力边界。

### 消融实验结果
#### 数据质量评估（Table 2）
| Method | Originality | Difficulty | Diversity | Test Quality |
|--------|-------------|-----------|----------|---------------|
| KodCode | 1.78 | 17.92 | 72.75 | 29.91 |
| Educational Instruct | 6.04 | 20.14 | 46.17 | 37.82 |
| **ADR (Ours)** | **28.91** | **71.89** | **84.36** | **81.36** |

- ADR 在原创性上是基线的 **4.8–16 倍**，在测试质量上接近 **2.7 倍**。
- t-SNE 可视化显示 ADR 数据更广泛地探索了低密度、长尾区域，而非局限于种子附近。

#### ADR 组件有效性分析
- **Info-Guided Schema Optimization**：
  - 经过 3 轮迭代后，validity rate 从 35.0% 提升至 43.0%，diversity 持续上升。
- **Adversarial Solution Space Refinement**：
  - 应用于 5K 任务后，平均测试用例数量从 14.75 → 34.78（↑135.8%），test quality 从 72.91 → 81.36（↑11.6%）。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **传统 heuristic 扩展范式存在根本局限**：保留原任务结构导致无法生成真正新颖的逻辑拓扑，限制了 RLVR 的潜力。
2. **ADR 成功实现了“组合式创新”**：通过原子分解与受控重组，跨越种子数据分布边界，生成具有结构性差异的新任务。
3. **高质量合成数据能持续驱动 RLVR 优化**：
   - ADR 数据在整个训练过程中维持稳定的梯度范数和 KL 散度增长，避免早收敛。
   - 奖励曲线显示 ADR 具有更强的优化潜力（Δreward = 0.45 vs KodCode 的 0.25）。
4. **方法具有强泛化性**：
   - 跨越不同 base model（Qwen、Llama）、不同任务类型（算法、工具、数据科学）均取得一致增益。

### 方法的局限性
- 当前评估集中在特定 benchmark 和中等规模模型上，尚未在超大规模模型（如 70B+）或多语言场景下充分验证。
- 尽管框架自动化程度高，但初始 schema 设计仍需一定领域知识引导。
- 目前聚焦单轮代码生成，未涉及多轮交互式 code agent 场景。

### 未来工作方向
- 将 ADR 扩展到更大规模的 foundation models 和 multilingual environments。
- 探索 ADR 在 **automated software engineering** 和 **multi-turn autonomous problem solving** 中的应用。
- 结合 soft reward 或 rubric-based reward，将 ADR 思路推广至非完全可验证领域。

--- 

> ✅ **总结一句话**：  
> ADR 通过 **atomic decomposition + combinatorial recombination** 范式，打破了传统合成方法的结构性天花板，首次实现了 **可规模化、高原创性、高难度** 的 verifiable code data 生成，为下一代 Code LLM 的 RLVR 训练提供了坚实的数据基础。

</details>

---

### 16. [AdaptR1: Reinforcement Learning Based Adaptive Interleaved Thinking in Multi-hop Question Answering](https://arxiv.org/abs/2605.31062)

**Authors**: Yuxin Wang, Jiahao Lu, Qifeng Wu, Shicheng Fang, Chuanyuan Tan, Yining Zheng, Xuanjing Huang, Xipeng Qiu  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.31062v1  

#### Abstract
Large Language Models (LLMs) have achieved remarkable performance in complex reasoning tasks through Chain-of-Thought (CoT) prompting. However, this approach often leads to ``over-thinking,'' where models generate unnecessarily long reasoning traces for simple queries and incur avoidable inference c...

---

### 17. [Wind Turbine Maintenance Log Labelling Framework: LLM-Driven Data Correction and Enrichment via Semantic Extraction of Reliability Intelligence](https://arxiv.org/abs/2605.31281)

**Authors**: Max Malyi, Jonathan Shek, Alasdair McDonald, Andre Biscaya  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.31281v1  

#### Abstract
As wind turbine fleets age, data-driven reliability engineering is essential to optimise their operation and maintenance for service life extension and levelised cost of energy reduction. Failure event descriptions within historical maintenance logs are a source of valuable reliability intelligence....

---

### 18. [AbstainGNN: Teaching Graph Neural Networks to Abstain for Graph Classification](https://arxiv.org/abs/2605.30786)

**Authors**: Xixun Lin, Zhiheng Zhou, Zhengyin Zhang, Yancheng Chen, Shuai Zhang, Ge Zhang, Shichao Zhu, Lixin Zou, Chuan Zhou, Peng Zhang, Shirui Pan, Yanan Cao  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.30786v1  

#### Abstract
Graph classification is a core task in graph data mining with widespread real-world applications. Recent advances in graph neural networks (GNNs) have led to substantial performance improvements for graph classification. However, existing GNNs are typically forced to make predictions even under high...

---

### 19. [Bandwidth Allocation with Device Partitioning for Federated Learning over Industrial IoT networks](https://arxiv.org/abs/2605.30892)

**Authors**: Kangmin Kim, Jaeyoung Song  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.30892v1  

#### Abstract
We consider a federated learning (FL) system in which Industrial Internet-of-Things (IIoT) devices collaboratively train a global model over wireless channels without sharing local data. In such systems, communication time is a primary bottleneck that constrains overall training efficiency. Unlike c...

---

### 20. [Structure-Induced Information for Rerooting Levin Tree Search](https://arxiv.org/abs/2605.30664)

**Authors**: Jake Tuero, Michael Buro, Laurent Orseau, Levi H. S. Lelis  
**Category**: cs.AI  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.30664v1  

#### Abstract
Subgoal-based policy tree search, which uses a policy to guide search, is effective for complex single-agent deterministic problems but often relies on explicit subgoal generation that can incur substantial overhead and hinders scalability. In this paper, we overcome these limitations by using a lea...

---

### 21. [A Persona-Based Evaluation Framework for Pluralistic Alignment in Generative AI](https://arxiv.org/abs/2605.31021)

**Authors**: Atahan Karagoz  
**Category**: cs.AI  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31021v1  

#### Abstract
Current alignment paradigms for generative artificial intelligence rely predominantly on monolithic benchmarking frameworks that reduce the plurality of human judgment to aggregated statistical baselines, thereby obscuring cultural, demographic, and contextual variability in evaluation. We introduce...

---

### 22. [Knowledge Graph-Enhanced Zero-Shot Topic Classification: A Multi-Strategy Comparative Study](https://arxiv.org/abs/2605.30465)

**Authors**: Shahana Akter, Yatharth Vohra, Ankita Shukla, Souvika Sarkar  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.30465v1  

#### Abstract
Multi-label topic classification without labeled training data is a challenging task, specially when documents contain complex relational information. We present a zero-shot multi-label topic classification framework and systematically investigate how per-article knowledge graph augmentation affects...

---

### 23. [AI for Monitoring and Classifying Data Used in Research Literature](https://arxiv.org/abs/2605.30582)

**Authors**: Rafael Macalaba, Aivin V. Solatorio  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.30582v1  

#### Abstract
While platforms like Google Scholar and Semantic Scholar track citations for academic papers, no comparable infrastructure exists for monitoring dataset usage in research literature, leaving the landscape of data use largely opaque. Addressing this gap is critical for transparency, reproducibility, ...

---

### 24. [Towards Efficient LLMs Annealing with Principled Sample Selection](https://arxiv.org/abs/2605.31175)

**Authors**: Yuanjian Xu, Jianing Hao, Wanbo Zhang, Zhong Li, Guang Zhang  
**Category**: cs.CL  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31175v1  

#### Abstract
The annealing phase is a pivotal convergence stage in LLM pre-training that ultimately determines final model quality. However, effectively selecting training data during this phase remains a key challenge. Current strategies rely on empirical heuristics, such as domain filtering or context extensio...

---

### 25. [Retriever Portfolios: A Principled Approach to Adaptive RAG](https://arxiv.org/abs/2605.31176)

**Authors**: Miltiadis Stouras, Vincent Cohen-Addad, Silvio Lattanzi, Ola Svensson  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31176v1  

#### Abstract
Retrieval-augmented generation (RAG) systems typically rely on a single retriever and a single set of hyperparameters, despite facing highly heterogeneous queries that range from simple factoid questions to complex multi-hop reasoning. We propose a method that automatically selects a small, diverse ...

---

### 26. [Algorithmic Recourse of In-Context Learning for Tabular Data](https://arxiv.org/abs/2605.31272)

**Authors**: Wenshuo Dong, Jiaming Zhang, Shaopneg Fu, Hongbin Lin, Di Wang, Lijie Hu  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31272v1  

#### Abstract
As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals. Many such models operate on tabular data, where features correspond to real-world attributes. Recently, in-conte...

---

### 27. [Survival Reinforcement Learning: Toward Scalable Self-Supervised RL](https://arxiv.org/abs/2605.31273)

**Authors**: Franki Nguimatsia-Tiofack, Fabian Schramm, Th\'eotime Le Hellard, Justin Carpentier  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31273v1  

#### Abstract
While self-supervised Contrastive Reinforcement Learning (CRL) has shown remarkable depth-scaling capabilities, successfully using networks over 64 layers, scaled CRL still struggles with long-horizon goal-conditioned planning due to the uniformity-tolerance dilemma inherent in contrastive losses. W...

---

### 28. [Flow map learning in nonlinear vector autoregressive models: influence of the feature-library structure on the training error](https://arxiv.org/abs/2605.31438)

**Authors**: Markus Gross  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31438v1  

#### Abstract
Time series forecasting often requires learning nonlinear and time-delayed dependencies. A paradigmatic class of forecasting models are nonlinear vector autoregressive processes (NVAR), also known as next-generation reservoir computers (NG-RCs). These models approximate the Koopman operator on the s...

---

### 29. [Scalable Inference-Time Annealing with Surrogate Likelihood Estimators](https://arxiv.org/abs/2605.31498)

**Authors**: Daniel Pe\~naherrera, Rishal Aggarwal, David Ryan Koes  
**Category**: cs.LG  
**Published**: 2026-06-01  
**Score**: 7.0  
**Type**: new  
**ArXiv ID**: 2605.31498v1  

#### Abstract
A long standing challenge in computational chemistry and biophysics is efficiently sampling the Boltzmann distribution of molecules. Advances in generative modeling have been proposed to address the limitations of conventional sampling techniques by eliminating the computational cost of simulation. ...

---

### 30. [LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability](https://arxiv.org/abs/2605.31167)

**Authors**: Tom Lucas, Alessio Buscemi, Alfredo Capozucca, German Castignani, Barbara Delacroix  
**Category**: cs.AI  
**Published**: 2026-06-01  
**Score**: 6.5  
**Type**: new  
**ArXiv ID**: 2605.31167v1  

#### Abstract
Assessing whether Large Language Models outputs are factually grounded, epistemically calibrated, and methodologically reproducible is a prerequisite for responsible AI deployment. Yet auditing LLMs remains inaccessible to non-technical practitioners: existing tools require programming expertise and...

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
