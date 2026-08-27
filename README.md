# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-27 16:57:28 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration](https://arxiv.org/abs/2608.24938v1)

**Authors**: Juntong Wu, Yifei Liu, Junyi Chen, Siqi Fan, Chaoran Feng, Minghao Li, Liujie Zhang, Weihang Chen, Li Yuan  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 111.0  
**Type**: new  
**ArXiv ID**: 2608.24938v1  

#### Abstract
Mixture-of-Experts (MoE) models scale capacity for strong quality while keeping per-token compute bounded through sparse expert activation. Yet low-latency MoE serving is increasingly challenging, because it spans two inference phases with fundamentally different bottlenecks: prefill is dominated by...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration
1. 论文的主要贡献和创新点
✅ 解决的问题：MoE模型的预填充与解码阶段存在不同瓶颈——预填充阶段以token级专家计算为主，解码阶段受批量激活专家集的内存流量约束；现有无训练加速方法仅优化单一资源代理，或仅处理token执行的专家、或仅处理批量激活的专家集，或丢弃排除专家的贡献、或仅隐式近似排除专家贡献，存在局限性。
🚀 提出的新方法与思路
**Unified Expert Folding Framework**：将MoE模型的预填充和解码两个推理阶段均转化为预算受限的输出近似问题，执行阶段特定的受限专家集，通过校准标量投影器将预算外专家的贡献投影到保留的专家，实现两个阶段的联合加速。
**Pairwise Scalar Projector Calibration**：在无标签数据上校准得到两两标量投影器矩阵，推理时使用该投影器将排除专家的贡献折叠到保留专家；其中预填充加速对应token级Top-K折叠，解码加速对应批量级专家池折叠，两个阶段仅保留专家的选择方式不同，排除专家贡献通过同一折叠机制恢复。该方法实现为vLLM的即插即用插件，包含轻量专家折叠CUDA内核。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 加速覆盖范围 | 同时支持MoE模型的预填充与解码两个阶段的加速处理 |
| 专家贡献处理 | 采用统一折叠机制处理预算内/外专家贡献，无需丢弃或仅隐式近似排除专家贡献 |
| 训练依赖性 | 无训练过程，可即插即用集成到现有推理框架 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为MoE模型预填充与解码阶段的推理加速，评估指标包括TTFT（初token生成时间）、TPOT（每token生成时间）、平均模型质量，其中TTFT、TPOT为越低越好，平均模型质量为越高越好。
| 指标 | 含义 |
| --- | --- |
| TTFT | 初token生成时间，↓越低越好 |
| TPOT | 每token生成时间，↓越低越好 |
| 平均模型质量 | 模型输出与预期的匹配程度，↑越高越好 |
⚔️ 基线方法对比：论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总：论文未报告

4. 关键结论和发现
- 主要发现：
  1. ExFold可实现MoE模型预填充与解码阶段的联合加速。
  2. 采用无标签数据校准的标量投影器，可有效恢复排除专家的贡献，维持较高的模型质量。
  3. ExFold作为vLLM插件具备轻量、即插即用的特性。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：ExFold是一种无训练的统一专家折叠框架，可即插即用于vLLM，同步加速MoE模型的预填充与解码阶段，同时保留接近原模型的输出质量。

</details>

---

### 2. [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving](https://arxiv.org/abs/2608.23962v1)

**Authors**: Srikanta Datta Tumkur, Mehar Simhadri, Anshu Bansal, Jay Iyer, Sai Pavan Kumar, Sai Kapil Kumar, Ramesh Nampelly, Raj Dandekar  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 86.0  
**Type**: new  
**ArXiv ID**: 2608.23962v1  

#### Abstract
When an LLM serving deployment runs out of KVcache room, there are two well-established ways out. Tensor parallelism shards the weights and the KV cache across two, four, or eight devices, buying memory headroom at the price of an all-reduce on every layer and a hardware bill that grows with the dev...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
当LLM serving部署的KV缓存空间耗尽时，两种成熟解决方案（张量并行与KV压缩）分别被研究，但现有研究存在核心矛盾：两类方案分别报告内存比、吞吐量曲线，未放在同一成本轴上对比；各自存在固有缺陷，张量并行需随设备增长提升成本且每一层需全归约操作，KV压缩以小质量损失换空间但未与张量并行做统一成本比较。
🚀 提出的新方法与思路
**成本归一化对比框架**：构建“每百万令牌的成本对延迟”的统一成本轴，将张量并行配置（degree 1到8）与KV压缩配置（16/8/4-bit，保留比率低至0.25）置于该轴对比，使用校准了A100、A40、H100硬件的分析器（profiled simulator）开展研究，寻找两种方案的成本等效临界点。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 成本效率 | KV压缩的成本比张量并行低1.20x至2.00x |
| 每美元容量提升 | KV压缩的每美元容量是花费8倍GPU的张量并行方案的16.5倍，后者仅为1.21倍 |
| 延迟调控 | 张量并行是唯一能改善延迟的手段，KV压缩会使每令牌延迟增加8%至93% |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
任务为内存受限的LLM serving（KV缓存空间耗尽时的部署策略选择），评估指标及箭头含义如下：
| 指标 | 含义 |
| --- | --- |
| 每百万令牌成本 | ↓ 越低越好 |
| 延迟 | ↓ 越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 张量并行（degree 1~8） | 硬件扩展方案 | 分片权重与KV缓存，每一层需执行全归约操作，硬件成本随设备数量增长，是唯一能改善延迟的部署手段 |
| KV压缩（16/8/4-bit，保留比率0.25~1） | 缓存压缩方案 | 基于量化和驱逐在单GPU上原位缩减缓存空间，以小幅质量损失换取内存节省，会增加每令牌的延迟 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 在Llama-2 7B、70B模型及A100、A40、H100三种GPU的实验中，KV压缩的成本比张量并行低1.20x至2.00x；
  2. 80GB设备对应的策略边界约为36B参数（模型大小相对设备内存），模型大小低于该边界时KV压缩占优，额外GPU为不必要的开销；高于该边界时（如Llama-2 70B），张量并行是必要入场券，因为KV压缩不触及权重资源，Llama-2 70B在单A100上无法实现；
  3. 张量并行是唯一能改善部署延迟的手段，KV压缩是唯一能提升每美元对应容量的手段。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ **总结一句话**：该研究构建统一成本轴对比张量并行与KV压缩两种内存受限LLM serving的KV缓存耗尽解决方案，发现KV压缩成本更低、每美元容量提升更高，仅当模型大小超过80GB设备约36B参数时需采用张量并行，且张量并行是唯一可改善部署延迟的手段。

</details>

---

### 3. [BanglaMamba: Exploring State Space Models for Bangla Fake News Detection](https://arxiv.org/abs/2608.25190v1)

**Authors**: M. K. Khalidi Siam  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 66.5  
**Type**: new  
**ArXiv ID**: 2608.25190v1  

#### Abstract
Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media. While transformer-based models such as BanglaBERT achieve strong performance for Bangla text classification, their quadratic co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：BanglaMamba: Exploring State Space Models for Bangla Fake News Detection
1. 论文的主要贡献和创新点
✅ 解决的问题：Bangla假新闻检测是重要的NLP任务，现有基于Transformer的模型（如BanglaBERT）虽性能优异，但二次计算复杂度导致其难以适配长文档处理，不适用于资源受限环境；从头训练的BERT模型性能低于预训练BanglaBERT，且针对Bangla假新闻检测的高效模型研究不足。
🚀 提出的新方法与思路：**BanglaMamba**，该模型基于Mamba架构（即State Space Models），专为Bangla假新闻检测任务设计，通过State Space Models的线性复杂度解决Transformer的计算缺陷，同时兼顾与传统BERT相当的任务性能。
🔍 相比现有方法的优势：
维度 | 优势
--- | ---
核心性能 | 与从头训练的CustomBERT性能相当，满足假新闻检测的基础需求
计算效率 | 推理吞吐量约为BERT-based模型的2.2倍，推理峰值GPU内存降低49%，适配资源受限的部署场景
泛化能力 | 弱于大规模预训练的BanglaBERT，需进一步优化跨数据集迁移效果
2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为Bangla假新闻检测（文本分类任务）；评估指标为Macro-F1，越高越好（↑）。
⚔️ 基线方法对比：
方法 | 类型 | 特点
--- | --- | ---
BanglaBERT | 预训练Transformer模型 | 基于大规模预训练，主任务性能最优，但计算复杂度高
CustomBERT | 从头训练的BERT模型 | 无大规模预训练，性能介于BanglaBERT与BanglaMamba之间
BanglaMamba | 基于Mamba的状态空间模型 | 本文提出的高效模型，兼顾性能与计算效率
3. 主要实验结果和性能指标
📊 定量结果汇总
**Bangla假新闻检测主任务性能（Macro-F1）**
方法 | Macro-F1 | 备注
--- | --- | ---
BanglaBERT | 0.9260 ✅ | 预训练Transformer，主任务性能最优
CustomBERT | 0.9057 | 从头训练BERT模型
BanglaMamba | 0.9029 | 本文提出的Mamba模型
💡 结论：BanglaBERT在Bangla假新闻检测主任务上性能最优，BanglaMamba性能接近从头训练的CustomBERT。

**推理效率对比**
效率指标 | BanglaMamba | BERT-based模型 | 优势幅度
--- | --- | --- | ---
推理吞吐量 | 约2.2倍 | 基准 | 约2.2×更高
推理峰值GPU内存 | 约0.51倍 | 基准 | 降低49%
💡 结论：BanglaMamba的计算效率显著优于BERT-based模型，更适配资源受限的部署环境。

**跨数据集泛化性能**
方法 | 跨数据集Macro-F1 | 结论
--- | --- | ---
BanglaBERT | 更优 | 大规模预训练有助于提升跨数据集泛化能力
BanglaMamba | 弱于BanglaBERT | Mamba模型的跨数据集泛化能力不足
💡 结论：预训练带来的泛化优势在Bangla假新闻检测任务中依然明显，BanglaMamba需进一步提升跨数据集泛化能力。

其余实验（鲁棒性/扰动测试、消融实验）：论文未报告
4. 关键结论和发现
- 主要发现：1）本文提出的BanglaMamba在Bangla假新闻检测任务中，性能与从头训练的CustomBERT相当，且相比BERT-based模型，计算效率大幅提升；2）预训练的BanglaBERT主任务性能最优，但其跨数据集泛化能力优于BanglaMamba，说明大规模预训练对提升模型泛化能力的重要性；3）BanglaMamba的推理吞吐量是BERT类模型的约2.2倍，推理峰值GPU内存降低49%，适合资源受限的部署场景。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：BanglaMamba作为基于Mamba架构的状态空间模型，在Bangla假新闻检测中实现了与从头训练BERT相当的性能，同时大幅降低了计算复杂度与内存消耗，适配资源受限环境，但跨数据集泛化能力弱于大规模预训练的BanglaBERT。

</details>

---

### 4. [psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing](https://arxiv.org/abs/2608.25683v1)

**Authors**: Mianjie Yu, Zizhao Mo, Huanyu Qu, Zhirong Qian, Huanle Xu, Cen Li, Zifeng Zhao, Zhi Zhou, Jinhua Zhou, Jun Xie, Chengzhong Xu  
**Category**: cs.DC  
**Published**: 2026-08-27  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2608.25683v1  

#### Abstract
In modern agentic AI training, the system bottleneck is shifting from rollout to update. Emerging sampling strategies such as tree-structured and step-wise RL greatly increase training sample volume while incurring relatively low marginal rollout cost, causing the update phase to dominate the end-to...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing

1. 论文的主要贡献和创新点
✅ 解决的问题
现代agentic AI训练的瓶颈已从rollout阶段转移至update阶段；树状、分步RL等新兴采样策略大幅增加训练样本量，边际rollout成本低，导致update阶段主导端到端执行时间；现有训练系统未利用训练样本间存在的大量前缀冗余，无法解决该阶段的性能瓶颈。

🚀 提出的新方法与思路
**psRL (prefix sharing for RL)**：针对agentic AI训练设计的新型训练系统，利用update阶段的全局可见性与数据不可变性，实现分布式训练的高效工作负载调度与内存管理。
**双前缀共享机制**：引入两种新的前缀共享机制，支持跨GPU worker的灵活细粒度工作负载分发，同时优化前缀复用效果并实现负载均衡。
**自适应KV缓存管理器**：设计新的底层KV缓存管理器，支持自适应块大小分配与动态KV缓存策略，在最大化内存利用率的同时保持高前缀命中率。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 训练吞吐量 | 相比现有agentic AI训练系统性能更优 |
| 执行效率 | 解决训练瓶颈从rollout转向update的问题，降低update阶段主导的端到端执行时间 |
| 内存利用 | 最大化内存利用率，同时保持高前缀命中率 |
| 负载均衡 | 支持跨GPU worker的灵活细粒度工作负载分发，兼顾前缀复用与负载均衡 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 生产轨迹 | 用于训练与评估psRL方法的性能 |

🎯 实验设置与评估指标
任务：agentic AI的训练过程优化
| 指标 | 含义（箭头方向） |
|------|------------------|
| 吞吐量 | ↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 现有agentic AI训练系统 | 基线方法 | 未利用训练样本间的前缀冗余，存在update阶段主导端到端执行时间的瓶颈 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告实验对应的表号、图号等来源信息，未提供除训练吞吐量优于现有系统外的具体指标数值，其余实验内容如下：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 核心问题：agentic AI训练的瓶颈已转移至update阶段，训练样本间的前缀冗余可作为优化训练效率的切入点。
- 方法创新：psRL通过双前缀共享机制与自适应KV缓存管理器，实现高效的分布式训练调度与内存管理，提升训练吞吐量。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：psRL作为针对agentic AI训练的新型系统，利用训练样本间的前缀冗余优化update阶段的工作负载与内存管理，显著提升训练吞吐量，解决现有系统的训练瓶颈。

</details>

---

### 5. [Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention](https://arxiv.org/abs/2608.23834v1)

**Authors**: Sergii Kozyrev (Minima AI, Inc), Davyd Maiboroda (Minima AI, Inc)  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2608.23834v1  

#### Abstract
The key-value (KV) cache is a primary capacity and bandwidth bottleneck in long-context LLM serving. We present Minima-KV, a retention-preserving hierarchy for mixed-format paged attention. Recent and protected Anchor pages remain in FP8, while older non-anchor pages move to packed TQ3; every live-r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention
1. 论文的主要贡献和创新点
✅ 解决的问题
KV缓存是长上下文LLM服务部署中的核心容量与带宽瓶颈；现有部分方法存在需cache尺寸密集影子缓存、压缩后性能下降等缺陷。
🚀 提出的新方法与思路
**Minima-KV混合格式分页注意力架构**：近期受保护的Anchor页保持FP8格式，旧非Anchor页转为packed TQ3格式，确保每个活跃请求页均可寻址；采用格式特定内核计算部分注意力状态，通过全局归一化online-softmax合并，无需cache尺寸密集影子，实现直接异构解码。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV缓存压缩比 | 相对BF16压缩3.50x，相对FP8压缩1.75x |
| 长上下文任务性能 | 16K RULER任务注意力质量匹配密集控制，LongBench v2性能偏差极小 |
| 内存开销 | 无需cache尺寸密集影子缓存，降低额外存储需求 |
| 解码吞吐量 | 单双请求场景下吞吐量损失极小 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RULER | 16K needle-in-a-haystack任务的注意力质量评估 |
| LongBench v2 | 503问长上下文性能评估 |
| 双请求直接解码测试集（2个59008-token请求） | 长双请求场景的压缩与吞吐量测试 |
| 其余数据集 | 论文未报告 |
🎯 实验设置与评估指标
任务：长上下文LLM部署中KV缓存压缩的质量、存储与性能评估。
| 指标 | 含义 | 趋势 |
| --- | --- | --- |
| 注意力KV per 活令牌 | 每个活令牌占用的注意力缓存量 | ↓ 越小越好 |
| LongBench v2性能偏差 | 与无压缩密集控制方法的性能差值 | ↓ 越低越好 |
| 活跃KV压缩比 | 活跃请求KV缓存的压缩倍数 | ↑ 越高越好 |
| 解码吞吐量 | 单位时间处理的请求量 | ↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| BF16基准 | 传统全精度KV缓存 | 性能优异但存储带宽需求大 |
| FP8基准 | 现有低精度KV缓存 | 存储需求低于BF16但未达Minima-KV压缩比 |
| 无压缩密集控制方法 | 参考基准 | 性能匹配Minima-KV但需cache尺寸密集影子 |
| 双请求直接解码控制方法 | 参考基准 | 用于长双请求场景的吞吐量对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Qwen3.6-27B单96GB NVIDIA RTX PRO 6000 Blackwell GPU部署性能（配置绑定）**
| 指标 | 值 | 最优情况 |
| --- | --- | --- |
| 注意力KV per 活令牌 | 18.3 KiB | ✅ 相对BF16压缩3.50x，相对FP8压缩1.75x |
| LongBench v2 16K上下文性能偏差 | -0.80个百分点 | - |
| LongBench v2 32K上下文性能偏差 | -0.60个百分点 | - |
| LongBench v2 64K上下文性能偏差 | -0.40个百分点 | ✅ 偏差最小 |
💡 结论：Minima-KV在Qwen3.6-27B模型上实现了较高的KV压缩率，同时在LongBench v2不同上下文长度下保持了较低的性能偏差。

**表2：59008-token双请求直接解码性能对比**
| 指标 | 值 | 对比基准表现 |
| --- | --- | --- |
| 活跃KV压缩比 | 3.625x | 无压缩控制方法 |
| 吞吐量 | 0.9821x | 无压缩控制方法 |
| 全注意力层覆盖率 | 100% | 无压缩控制方法 |
💡 结论：Minima-KV在长双请求场景下实现了更高的活跃KV压缩比，仅伴随极小的吞吐量损失，且能完整覆盖所有注意力层。

**表3：16K RULER needle-in-a-haystack任务注意力质量**
| 指标 | 结果 | 与密集控制方法对比 |
| --- | --- | --- |
| 注意力质量匹配度 | 无偏差 | 完全匹配密集控制性能 |
💡 结论：Minima-KV的注意力质量与无压缩的密集控制方法相当，满足长上下文任务的保留要求。

其余实验情况：
1. 主 benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① Minima-KV的混合格式Anchor/非Anchor KV缓存方案，无需密集影子缓存即可实现显著的KV压缩；② 在RULER、LongBench v2等长上下文基准任务上，Minima-KV性能损失极小，匹配无压缩密集控制的注意力质量；③ 长双请求场景下，Minima-KV压缩比更高，吞吐量仅略有下降。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：Minima-KV通过混合格式的分页注意力KV缓存压缩方案，在保留长上下文注意力质量的同时，实现了显著的存储压缩，且无需cache尺寸的密集影子，为长上下文LLM部署提供了实用可行的路径。

</details>

---

### 6. [Beyond Pairwise Feedback: Listwise Vision-Language Supervision for Preference-Based Reward Learning](https://arxiv.org/abs/2608.25350v1)

**Authors**: Srivalli Katkuri, Maxwell Kawada, Juan Wachs  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2608.25350v1  

#### Abstract
Vision-language models (VLMs) have emerged as a powerful source of supervision for reinforcement learning, enabling agents to leverage rich semantic knowledge during training. Inspired by the success of preference-based reward learning (PbRL) in reinforcement learning from human feedback (RLHF), vis...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Pairwise Feedback: Listwise Vision-Language Supervision for Preference-Based Reward Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于视觉-语言模型（VLM）的偏好式奖励学习普遍采用Bradley-Terry（BT）模型，仅利用两两（K=2）的观测进行偏好建模，未充分发挥VLM具备的多候选排序能力，限制了偏好监督的价值。

🚀 提出的新方法与思路
**Plackett-Luce (PL) 列表式偏好奖励学习框架**，核心为将VLM生成的多候选列表式排序与Plackett-Luce模型结合，替代传统两两偏好建模，支持K∈{3,4,5}等不同大小的列表式偏好输入，用于训练奖励函数。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 偏好建模能力 | 支持列表式（多候选）偏好，突破传统BT模型仅能处理两两比较的限制，充分发挥VLM的排序能力 |
| 灵活性 | 可根据任务或环境需求选择不同的排名大小K，适配性更强 |
| 性能表现 | 至少一个K∈{3,4,5}的PL奖励模型在平均成功率上等于或优于Pairwise BT、K-wise BT、RL-VLM-F等对比基线 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| Meta-World 操纵任务环境 | 评估提出的偏好奖励学习框架的性能 |

🎯 实验设置与评估指标
任务为在Meta-World机器人操纵任务中训练机器人策略，评估各奖励学习方法的性能。评估指标如下：
| 指标 | 含义 |
|------|------|
| 平均成功率 | 策略完成对应操纵任务的比例，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Pairwise Bradley-Terry (BT) | 偏好模型 | 仅支持K=2的两两偏好比较，为传统方法 |
| K-wise Bradley-Terry | 偏好模型 | 支持任意K大小的偏好比较，作为对比基线 |
| RL-VLM-F | 基线方法 | 现有基于VLM的偏好奖励学习方法，作为对比基准 |
| Oracle | 基准方法 | 最优性能参考，代表该任务的理想性能 |

3. 主要实验结果和性能指标
在Meta-World操纵任务实验中：
- 至少一个K∈{3,4,5}的Plackett-Luce（PL）奖励模型在平均成功率上达到或优于其他对比方法；
- 最佳PL配置的平均成功率为86%，在Drawer Open任务上的性能匹配Oracle基准。
💡 结论：提出的列表式VLM偏好奖励学习方法在Meta-World机器人操纵任务上具有竞争力，且具备灵活性可适配不同排名大小的偏好需求。
其余实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告。

4. 关键结论和发现
- 主要发现：1. 基于列表式VLM偏好的Plackett-Luce奖励学习框架在平均成功率上达到或优于对比基线；2. PL框架支持选择不同的排名大小K，可灵活适配环境；3. 最佳PL配置在Meta-World任务达到86%平均成功率，在Drawer Open任务达到Oracle性能。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出结合VLM生成的列表式偏好与Plackett-Luce模型的奖励学习框架，在Meta-World机器人操纵任务上表现出具有竞争力的性能与灵活性，突破了传统两两偏好建模的限制。

</details>

---

### 7. [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](https://arxiv.org/abs/2608.24658v1)

**Authors**: Zhengyang Zhang, Zijian Zhang, Jiaxuan Gao, Shusheng Xu, Yi Wu, Song Han, Ligeng Zhu  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2608.24658v1  

#### Abstract
Scaling test-time reasoning has substantially improved the problem-solving ability of large language models (LLMs), but standard autoregressive decoding still executes long reasoning traces sequentially, creating severe latency for difficult tasks (up to days and weeks). Parallel reasoning offers a ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
标准自回归解码会将LLM的长推理链顺序执行，导致困难任务延迟极高（可达数天或数周）；现有并行推理系统仅关注子任务并行（分解任务为独立小块并行求解），忽略了另一种关键并行形式——试次并行（多个推测尝试并行探索、验证、聚合竞争假设），这是之前方法的核心缺陷。

🚀 提出的新方法与思路
**并行类型识别与分类**：明确划分LLM推理中的两种并行形式，通过分析确定试次并行是可并行化推理计算的重要组成，且在难题上占比更主导。
**顺序推理转结构化并行轨迹**：借助上下文无关文法，将顺序推理链转换为结构化的并行轨迹。
**PA-GRPO训练框架**：采用并行感知组相对策略优化（Parallelism-Aware Group Relative Policy Optimization, PA-GRPO）训练模型，奖励函数联合平衡准确率、延迟和两种并行性的比率。
**推理阶段并行执行**：推理时通过工具调用执行模型学到的并行结构，将理论上的并行节省转化为实际的墙钟级推理加速。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 并行覆盖范围 | 同时支持子任务并行与试次并行，弥补了现有并行推理仅关注子任务并行的缺陷 |
| 推理效率 | 实现实际的墙钟级加速，降低LLM推理延迟 |
| 性能保持 | 在加速推理的同时维持了竞争力的数学推理准确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AIME24 | 数学推理基准评估 |
| AIME25 | 数学推理基准评估 |

🎯 实验设置与评估指标
任务：在数学推理任务上评估本文方法的推理性能与效率。
| 指标 | 含义（箭头） |
| --- | --- |
| 平均加速度 | 衡量推理速度的提升倍数，↑ 越高越好 |
| 准确率 | 衡量数学推理的正确率，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准自回归解码 | 传统LLM推理方法 | 顺序执行推理链，延迟高，无并行支持 |
| 子任务并行推理系统 | 现有并行推理方法 | 仅支持子任务并行，忽略试次并行 |
| Parason | 本文提出方法 | 同时支持子任务与试次并行，采用PA-GRPO训练，推理时通过工具调用执行并行结构 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表N：主基准性能（数学推理）**
论文未报告
💡 结论：论文未报告

**表N：效率对比**
论文未报告
💡 结论：论文未报告

**表N：跨域/zero-shot迁移实验**
论文未报告
💡 结论：论文未报告

**表N：鲁棒性/扰动测试实验**
论文未报告
💡 结论：论文未报告

**表N：消融实验**
论文未报告
💡 结论：论文未报告

4. 关键结论和发现
- 主要发现：1. 试次并行是LLM推理中可并行化计算的重要并行形式，且在难题上占比更主导；2. 提出的Parason方法能实现LLM推理的实际墙钟加速，同时维持竞争力准确率；3. 基于PA-GRPO的训练框架可联合平衡准确率、延迟和并行性比率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出的Parason方法通过识别并同时利用LLM推理中的子任务并行与试次并行，经PA-GRPO训练后，在AIME24和AIME25数学推理基准上实现了约1.7×的平均推理加速，同时保持了竞争力的准确率。

</details>

---

### 8. [TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving](https://arxiv.org/abs/2608.25523v1)

**Authors**: Hongqiu Ni, Han Tian, Chi Zhang, Guopeng Li, Haisheng Tan  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2608.25523v1  

#### Abstract
Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
多代理LLM服务中前缀缓存存在固有权衡：保留代理的长系统提示KV缓存可加速后续调用，但会减少用于批量处理并发请求的GPU内存；在多阶段工作流中，现有调度器多单独优先即时前缀局部性或整体工作流进度，在共享KV缓存预算下，单独优化任一目标均会因下游延迟或频繁前缀替换延长任务级作业完成时间（JCT）。

🚀 提出的新方法与思路
**TOPAS（Task-Oriented Prefix-Aware Scheduler）**：联合决策需保留的代理前缀与待调度的请求；通过权衡每个任务最长剩余服务路径的预期减少量、下游前缀复用的近期收益（考虑前缀移动及抢占成本）对候选后决策状态评分；引入任务级老化机制防止请求饥饿。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
任务级JCT优化 | 在共享KV缓存预算下平衡前缀保留与并发请求批量处理，避免单独优化即时前缀局部性或整体工作流进度的缺陷，降低任务级作业完成时间
多工作流适配 | 适用于多阶段工作流场景
饥饿预防 | 通过任务级老化机制防止请求饥饿

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
3个合成DAG | 评估TOPAS的调度性能
2个MetaGPT软件开发工作流（MetaGPT-SOP、MetaGPT-TL） | 评估TOPAS的调度性能

🎯 实验设置与评估指标
任务为多代理LLM服务的调度性能评估，核心指标如下：
指标 | 含义（箭头）
--- | ---
mean JCT | 任务级平均作业完成时间，↓越低越好
p99 JCT | 任务级99分位作业完成时间，↓越低越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
各工作负载最优基线（论文未报告具体名称） | 传统多代理LLM服务调度器 | 单独优先即时前缀局部性或整体工作流进度

3. 主要实验结果和性能指标
📊 定量结果汇总
论文提及TOPAS在合成DAG、MetaGPT-SOP、MetaGPT-TL工作负载下相较对应最优基线可降低JCT，但未附带表号、图号等定位信息，无法呈现具体定量数值。各细分实验项：
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- TOPAS通过联合决策前缀缓存与请求调度的策略，可在多代理LLM多阶段工作流中平衡前缀复用与并发请求批量处理，有效降低任务级JCT。
- 任务级老化机制是防止请求饥饿的有效手段。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：TOPAS是一种适用于多代理LLM多阶段工作流的前缀感知调度器，可在共享KV缓存预算下平衡前缀保留与并发请求处理，降低任务级作业完成时间。

</details>

---

### 9. [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](https://arxiv.org/abs/2608.25531v1)

**Authors**: Jihao Zhu, Zhiwei Yang, Wenxiao Zhang, Junqian Zhao, Qi You, Fangqi Wang, Zheyuan Deng, Hanzhe Yang, Yu Liu, Jin B. Hong  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2608.25531v1  

#### Abstract
Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but di...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives
1. 论文的主要贡献和创新点
✅ 解决的问题
人文社科研究需要对小说、剧本、档案等长篇叙事材料做细读，但多数用户难以获取昂贵的专有长上下文模型；直接向紧凑、本地可部署的语言模型输入完整长上下文，存在成本高、难检查、易丢失稀疏证据的痛点，现有长文本相关方法未兼顾本地模型的实用性与推理可解释性的平衡。
🚀 提出的新方法与思路
**Reward-Guided Dual-Agent Framework**：包含Finder与Interpreter两个智能体模块；Finder通过检索引导的分割识别含答案关键线索的段落；Interpreter从选定证据推导答案，生成带段落ID引用的理由，还对高风险问题执行内部自校准；两个智能体均通过奖励引导的强化学习优化，其中Finder的奖励侧重证据保留与忠实的段落ID引用，Interpreter的奖励侧重推理正确性、证据依据性与解释简洁性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 可解释性 | 证据选择与推理过程比端到端提示更可检查 |
| 模型适用性 | 适配紧凑、可本地部署的LLMs，可替代昂贵的专有长上下文模型 |
| 推理可追溯性 | 提供证据覆盖及带段落引用的推理轨迹 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 用于多个长上下文叙事问答与声明验证任务 |

🎯 实验设置与评估指标
任务为长叙事问答与声明验证；论文未报告具体评估指标及含义，仅提及实验在多个长上下文叙事问答和声明验证场景开展。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有相关实验因论文未报告具体表号、数值等信息，均按要求标注：
1. 主benchmark性能：论文未报告
2. 效率对比（FPS/参数量）：论文未报告
3. 跨域/zero-shot迁移：论文未报告
4. 鲁棒性/扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 2-3条主要发现：ClueWeaver通过奖励引导的双智能体框架，在本地端到端语言模型上显著提升了性能，同时提供了可解释的证据推理过程；该框架实现了紧凑本地LLMs在长叙事任务中推理质量与可检查性的平衡。
- 方法局限性：论文未报告
- 未来工作：论文未报告

✅ **总结一句话**：ClueWeaver是针对长叙事问答的奖励引导双智能体框架，可在紧凑本地部署的语言模型上兼顾推理性能与可解释性，适配无法获取昂贵长上下文模型的使用场景。

</details>

---

### 10. [DCGC: Draft-Conditioned Global Correction for Complex Reasoning with Masked Diffusion Models](https://arxiv.org/abs/2608.25428v1)

**Authors**: Minhae Oh, Nakyung Lee, Jungwoo Lee  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2608.25428v1  

#### Abstract
Correcting flawed reasoning traces remains a significant challenge for Large Language Models (LLMs), whose autoregressive generation can propagate early mistakes into subsequent reasoning. We introduce DCGC, a Masked Diffusion Model (MDM) framework for global correction that uses an imperfect soluti...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DCGC: Draft-Conditioned Global Correction for Complex Reasoning with Masked Diffusion Models
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：大语言模型（LLMs）的自回归生成会将早期错误传播至后续推理环节，修正有缺陷的推理轨迹是复杂推理任务中的重大挑战。
现有方法缺陷：标准采样与更简单的分类器引导（CFG）变体性能不足，无法有效应对复杂推理的全局修正需求。

🚀 提出的新方法与思路
**DCGC框架**：一种基于Masked Diffusion Model（MDM）的全局修正框架，以上游求解器生成的不完美解决方案草稿作为辅助上下文，结合任务特定的Supervised Fine-Tuning（SFT）优化模型参数。
**Dynamic Dual-CFG机制**：推理阶段的核心机制，将仅问题分支与问题-草稿联合分支分离，通过相对置信差距缩放草稿条件残差，实现更精准的全局修正。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 复杂推理修正效果 | 在数学、代码、知识推理基准上优于标准采样与简单CFG变体 |
| 任务泛化能力 | 可适配多类复杂推理任务（数学、代码、知识） |
| 模块适用性 | 无需地面真实失败标签即可作为无验证器的全局修正模块，修正低共识上游输出 |
| 主干迁移性 | 性能可迁移至不同的扩散模型主干 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 数学、代码、知识推理基准 | 用于多任务性能评估 |

🎯 实验设置与评估指标
任务说明：面向复杂推理的推理轨迹修正任务，评估修正后的推理结果的准确性。
| 指标 | 含义（箭头标方向） |
| --- | --- |
| 论文未报告 | 论文未报告具体评估指标及定义 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准采样 | 推理基线 | 常规自回归生成采样方法 |
| 简单CFG变体 | 修正基线 | 基础的分类器引导式修正方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文未报告具体实验对应的表号、图号及数值，各实验详情如下：
- 主benchmark性能：论文未报告
- 效率对比：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

💡 结论：DCGC在多类复杂推理任务基准上的性能优于标准采样与简单CFG变体，且具备跨扩散主干的迁移能力，还可作为无验证器模块用于修正无标签场景下的低共识上游推理输出。

4. 关键结论和发现
- 主要发现：1. DCGC可有效解决LLM自回归推理中的错误传播问题，在多类复杂推理任务上表现优于标准采样与简单CFG变体；2. DCGC可作为无需地面真实失败标签的无验证器全局修正模块，针对低共识上游输出进行修正，适配困难推理实例；3. DCGC的修正效果可迁移至不同的扩散模型主干。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DCGC是一种结合Masked Diffusion Model、任务特定SFT与Dynamic Dual-CFG机制的全局修正框架，可在数学、代码、知识等多类复杂推理任务中提升性能，支持跨扩散主干迁移，且无需验证器即可修正低共识的上游推理输出。

</details>

---

### 11. [Recursive Agentic Reasoning](https://arxiv.org/abs/2608.23956v1)

**Authors**: Shengxin Zhang, Xiaomin Wu, Xiyang Wu, Jing Xie  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2608.23956v1  

#### Abstract
Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an ag...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Recursive Agentic Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有测试时推理方法（如迭代细化、分解、重复采样）被孤立评估，导致跨模型、基准、评估管线的性能增益难以比较；不同方法均存在无法横向对比的缺陷。

🚀 提出的新方法与思路
**Recursive Agentic Reasoning Framework**：将测试时推理方法统一为智能体推理轨迹上的三类递归算子，实现多方法的公平对比：
- **GROW**：加深单一推理路径；
- **PRUNE**：分解并重组问题；
- **BRANCH**：采样可选推理路径并从中选择。
采用共享的评估harness，确保所有方法使用相同提示、token预算、 grading代码消除评估干扰。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估公平性 | 统一评估harness消除了不同管线的干扰，支持跨模型、基准的横向对比 |
| 性能表现 | BRANCH算子在多数场景持续优于GROW、PRUNE算子 |
| 鲁棒性 | BRANCH可恢复输出预算耗尽等场景的性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 五个基准 | 用于测试三类递归算子及单遍链式思考基线的性能 |

🎯 实验设置与评估指标
任务为测试时推理问答任务，评估指标为准确率（↑越高越好）。
| 指标 | 含义 |
| --- | --- |
| 准确率 | 模型推理结果的正确比例，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- |
| Single-pass chain-of-thought | 基准方法 | 仅执行单遍推理，无递归算子参与 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体表号、图号，相关定量结果仅在摘要中提及：
- 在14个模型-基准设置中，BRANCH算子准确率平均提升5.98个百分点，且是12个设置的最佳算子；
- GROW算子平均提升2.18个百分点，在2个设置中出现性能下降；
- PRUNE算子平均提升0.94个百分点；
- BRANCH的增益与基准阶段空输出、预算耗尽输出率呈正相关（r=0.72）。

💡 结论：BRANCH算子在多模型-基准设置中展现出稳定的性能优势，其优势源于多路径探索及错误恢复能力。

4. 关键结论和发现
- 主要发现：① 统一评估框架下，BRANCH算子在所有14个模型-基准设置中性能优于基线，且持续优于GROW、PRUNE算子；② BRANCH的优势不仅在于多路径探索，还可恢复输出预算耗尽的场景；③ 配对评分相较于未配对评估，能改变甚至反转测试时计算的比较结论，应作为标准评估协议。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了统一的递归测试时推理算子框架，通过公平对比验证BRANCH算子在多基准与模型上的性能优势，强调配对评分对测试时计算评估的必要性。

</details>

---

### 12. [PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos](https://arxiv.org/abs/2608.24574v1)

**Authors**: Siyao Yan, Bo Han, Jisheng Dang, Bimei Wang, Shude Wang, Hong Peng, Yulan Guo, Jianhuang Lai, Bin Hu,  Tat-SengChua  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2608.24574v1  

#### Abstract
Video multimodal large language models support language guided video segmentation, but they often show spatio temporal inconsistencies, e.g., jitter, drift, and identity switches. These failures are more common when targets are partly hidden or when similar objects appear nearby.One likely reason is...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Video MLLMs在语言引导的视频分割中存在时空不一致问题（抖动、漂移、身份切换），该问题在目标部分被遮挡或附近有相似物体时更突出；核心原因是当前模型训练缺乏显式空间先验，难以随时间维持稳定的空间身份和形状。
🚀 提出的新方法与思路
**PhysMLLMs**：一种训练阶段的先验注入架构，用于为Video MLLMs注入物理启发的空间连续性先验；
**Global Representation Prior Alignment (REPA-Global)**：核心机制，通过离线嵌入缓存和计划蒸馏方案，从冻结的DINOv2教师模型蒸馏全局视觉表示，使学生模型的全局视觉表示与教师模型对齐；该设计保持推理过程不变，不增加推理时间成本。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 视频分割性能 | 提升视频分割掩码质量和跨帧一致性 |
| 推理效率 | 不增加推理时间成本，保持推理过程不变 |
| 单帧图像级定位性能 | 维持可比性能 |
| 通用多模态能力 | 维持可比性能 |
| 挑战性场景表现 | 在小目标、快速运动、遮挡、干扰项、推理查询等挑战性场景中获得更大增益 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未明确报告具体数据集名称 | 用于视频分割性能、单帧Referring图像分割性能及通用多模态性能的评估 |
🎯 实验设置与评估指标
语言引导的视频分割、referring图像分割及通用多模态性能评估
| 指标 | 含义（箭头） |
| --- | --- |
| 论文未明确报告具体指标名称 | 评估视频分割掩码质量、跨帧一致性、单帧referring分割性能、通用VLM性能及挑战性场景性能 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有Video MLLMs | 视频多模态大语言模型 | 存在时空不一致问题，训练缺乏显式空间先验，易在视频分割时出现抖动、漂移、身份切换等问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. 注入物理启发的空间连续性先验（通过REPA-Global机制）可有效提升Video MLLMs的视频分割掩码质量与跨帧一致性，且在小目标、快速运动、遮挡等挑战性场景中增益更显著；2. 该先验注入方法不会损害模型的单帧图像级定位能力及通用多模态性能
- 方法局限性：论文未明确报告
- 未来工作：论文未提及

> ✅ **总结一句话**：PhysMLLMs通过训练阶段注入物理启发的空间连续性先验（REPA-Global机制），在保持推理时间不变且不牺牲单帧/通用多模态能力的前提下，有效提升了视频多模态大语言模型的视频分割质量与跨帧一致性，尤其适配挑战性场景。

</details>

---

### 13. [Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core](https://arxiv.org/abs/2608.24810v1)

**Authors**: Yogesh Kumar  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.24810v1  

#### Abstract
Recent work has applied Mamba style state space models (SSMs) to video anomaly detection, yet existing approaches still rely on buffering clips or windows internally, lack a theoretical account of how temporal memory relates to detection latency, and benchmark efficiency only through GPU throughput ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core
1. 论文的主要贡献和创新点
✅ 解决的问题
现有应用Mamba风格状态空间模型（SSM）的视频异常检测方法，存在三个核心痛点：1. 内部依赖缓存片段或窗口；2. 缺乏时间记忆与检测延迟关系的理论解释；3. 基准效率仅通过GPU吞吐量衡量，而非目标边缘硬件。

🚀 提出的新方法与思路
**Diagonal Linear State Space Recurrence**：设计带输入与状态依赖衰减门的对角线性状态空间循环，采用冻结视觉骨干，通过因果下一个嵌入预测进行自监督训练，实现无前瞻、无片段缓存的严格因果流式检测，每帧的固定大小状态更新的时间和内存复杂度均为O(1)。
**理论推导**：推导了循环衰减谱与检测延迟、可可靠捕捉的最短异常长度的闭式关系。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 流式检测特性 | 严格因果，无前瞻，无片段缓存，状态更新O(1)时间与每帧内存 |
| 延迟响应性 | 实测检测延迟远低于理论预测的settling delay，事件边界门决定响应性 |
| 硬件适配 | 直接在目标边缘硬件Apple M3 Pro上实测端到端效率，而非依赖GPU模拟数据 |
| 可解释性 | 建立衰减谱与检测延迟、最短可捕捉异常的理论关联 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| UCSD Ped2 | 验证方法性能 |
| CUHK Avenue | 验证方法性能 |

🎯 实验设置与评估指标
任务为帧级视频异常检测，采用帧级AUC作为评估指标，数值越高表示性能越好。
| 指标 | 含义 |
| --- | --- |
| 帧级AUC | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有非因果SSM基线 | SSM类方法 | 非因果框架，帧级AUC性能优于提出方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能
论文未提供该部分对应表格编号，仅正文提及数值：
| 方法 | 数据集 | 帧级AUC（%） |
| --- | --- | --- |
| 提出方法 | UCSD Ped2 | 67.9 |
| 提出方法 | CUHK Avenue | 70.2 |
💡 结论：论文提出方法在两个基准数据集上的帧级AUC落后于现有非因果SSM基线。

2. 效率对比
论文未提供该部分对应表格编号，正文给出Apple M3 Pro硬件实测数值：
| 指标 | 数值 |
| --- | --- |
| 单帧端到端延迟（ms） | 0.74 |
| 吞吐量（FPS） | >1300 |
💡 结论：方法在目标边缘硬件上实现极高的检测效率，适配边缘部署需求。

3. 跨域 / zero-shot迁移
论文未报告该实验内容。

4. 鲁棒性 / 扰动测试
论文未报告该实验内容。

5. 消融实验
论文正文提及对衰减率、状态大小、门控机制进行了消融，相关性能变化：
| 消融模块 | 对UCSD Ped2（小训练集）帧级AUC影响 | 对CUHK Avenue（大训练集）帧级AUC影响 |
| --- | --- | --- |
| 衰减率 | 论文未报告具体性能变化 | 论文未报告具体性能变化 |
| 状态大小 | 论文未报告具体性能变化 | 论文未报告具体性能变化 |
| 启用衰减门 | 损害（相对于禁用） | 提升（相对于禁用） |
💡 结论：衰减门的贡献依赖数据集大小，在更大训练集上更有益。

4. 关键结论和发现
- 主要发现：1. 方法理论预测的settling delay（57-59帧）远高于实测检测延迟（1.6帧、18.4帧），说明事件边界门而非基础衰减率决定响应性；2. 在Apple M3 Pro上实现超1300 FPS的检测速度，适配边缘硬件；3. 衰减门对准确率的影响依赖数据集规模，在小训练集上降低性能，大训练集上提升性能。
- 方法局限性：当前在UCSD Ped2和CUHK Avenue两个基准上的帧级AUC未达到现有非因果SSM基线的水平，评估数据集覆盖不足。
- 未来工作：缩小与现有非因果SSM基线的准确率差距，将评估扩展至更大的第三方基准数据集。

> ✅ **总结一句话**：该论文提出一种基于带输入与状态依赖衰减门的对角线性状态空间循环的严格因果流式视频异常检测方法，建立了衰减谱与检测延迟、可捕捉异常长度的理论关系，在边缘硬件实现高效检测，但当前帧级准确率落后于非因果SSM基线。

</details>

---

### 14. [Are LLM-Enhanced GNNs Privacy-Safe?](https://arxiv.org/abs/2608.25727v1)

**Authors**: Longzhu He, Zelang Wen, Chaozhuo Li, Sen Su  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2608.25727v1  

#### Abstract
Large language models (LLMs) have recently advanced graph neural networks (GNNs) by enriching node representations with semantic information, giving rise to LLM-enhanced GNNs that achieve substantial performance gains. However, their vulnerability to privacy attacks, in which adversaries infer sensi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Are LLM-Enhanced GNNs Privacy-Safe?
1. 论文的主要贡献和创新点
✅ 解决的问题：Large Language Models (LLMs)增强的图神经网络（GNNs）虽在图学习任务中性能显著提升，但其对隐私攻击（包括链接推断、标签推断、成员推断三类）的脆弱性尚未得到系统评估，现有研究缺乏针对这类模型隐私风险的全面分析，存在安全隐患。
🚀 提出的新方法与思路：**统一隐私风险评估框架**，该框架包含五个阶段：（1）数据集准备、（2）受害者模型训练、（3）隐私攻击、（4）风险评估、（5）防御分析，用于系统性评估LLM-enhanced GNN的隐私风险，覆盖从数据输入到防御输出的全流程。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估全面性 | 构建覆盖数据准备、攻击实施、风险评估到防御分析的全流程统一框架，而非针对单一环节评估 |
| 目标针对性 | 聚焦LLM-enhanced GNN这一新兴模型类别，系统评估三类核心隐私攻击（链接、标签、成员推断） |
| 实践指导性 | 结合多领域数据集、多攻击方法与多模型配置开展实验，还分析了差分隐私作为防御策略的效果，为安全图学习系统提供实际见解 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 六个真实世界文本属性图数据集（覆盖 diverse domains） | 用于评估LLM-enhanced GNN的隐私风险 |
🎯 实验设置与评估指标：针对LLM-enhanced GNN在链接、标签、成员推断三类隐私攻击下的脆弱性，以及差分隐私防御的隐私-效用权衡展开评估。论文未报告具体评估指标名称，仅明确评估上述两类核心内容。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 浅文本表示基线 | 基线模型 | 用于与LLM-enhanced GNN对比隐私脆弱性 |
| LLM-based特征增强器+GNN backbone（共42种配置） | 受害者模型 | 被设置为隐私攻击的目标模型 |
| 六类代表性隐私攻击方法 | 攻击方法 | 用于实施链接、标签、成员推断三类隐私攻击 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量结果（如表号、数值等），仅通过定性分析得出相关结论。
4. 关键结论和发现
- 主要发现：1. 尽管LLM-enhanced GNN在图学习性能上有提升，但相比浅文本表示基线，其对链接、标签、成员推断三类隐私攻击的脆弱性一致增加；2. 语义富集会放大嵌入空间中与链接、标签、成员相关的信号，使其更易被隐私攻击方法利用；3. 差分隐私作为防御策略可部分缓解LLM-enhanced GNN的隐私风险，但会引入显著的效用下降，存在根本的隐私-效用权衡。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文提出统一隐私风险评估框架，系统揭示LLM增强GNN的隐私脆弱性，分析语义富集对隐私的影响及差分隐私防御的隐私-效用权衡，为安全可信的图学习系统提供实践指导。

</details>

---

### 15. [Multimodal Injury Risk Prediction in Tennis](https://arxiv.org/abs/2608.25126v1)

**Authors**: Francisco Erramuspe Alvarez, Shobharani Polasa, Weihao Qu, Jay Wang, Ling Zheng  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2608.25126v1  

#### Abstract
Machine learning has had a significant positive impact on the prediction of athlete performance and injury risk. Most works in this field rely on subjective observations and expert assessments, which restrict their effectiveness. In sports like soccer, basketball, and wrestling, some studies attempt...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Multimodal Injury Risk Prediction in Tennis
1. 论文的主要贡献和创新点
✅ 解决的问题：现有运动员表现与损伤风险预测研究多依赖主观观察和专家评估，限制了预测效果；足球、篮球等球类领域已有结合可穿戴设备等替代数据的相关尝试，但网球领域此类研究基本未被探索。
🚀 提出的新方法与思路
**Predictive Athlete Readiness framework for Tennis (PART)**：利用机器学习与深度学习技术，处理九名大学网球运动员的多源数据（含生理指标、训练比赛数据、可穿戴设备睡眠数据、每日问卷自我报告信息、跳跃评估、比赛视频动作分析）；捕捉网球运动员的整体健康、损伤风险、身体能力、打法风格四类特征；通过监督学习整合四类特征，实现运动员状况的全面评估及上肢（如肘部）、下肢（如膝盖）等特定身体部位损伤风险的高级预测。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据源整合能力 | 融合多类型数据，突破现有研究仅依赖主观/专家评估的局限 |
| 领域针对性 | 填补网球领域运动员损伤风险与表现预测的研究空白 |
| 预测精细度 | 可针对上肢、下肢等特定身体部位预测损伤风险，而非仅整体风险 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 九名大学网球运动员的多源数据（含生理指标、训练比赛数据、可穿戴设备睡眠数据、每日问卷自我报告信息、跳跃评估、比赛视频动作分析） | 训练和评估PART框架的相关预测任务 |
🎯 实验设置与评估指标
任务：预测网球运动员的整体健康、损伤风险及上肢、下肢特定身体部位的损伤风险；论文未报告具体评估指标。
⚔️ 基线方法对比
论文未报告。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验图表、数值及对应结论细节。

4. 关键结论和发现
- 主要发现：1. PART框架可通过整合多源数据，实现网球运动员整体健康与损伤风险的有效预测，且能覆盖上肢、下肢等特定身体部位的损伤风险；2. PART框架对娱乐级网球运动员同样具有应用潜力，可预防其因错误技术引发的损伤。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：本文提出的多模态PART框架，整合多源数据填补了网球领域运动员损伤风险与表现预测的研究空白，可为大学及娱乐级网球运动员的状况评估与损伤预防提供支持。

</details>

---

### 16. [AFDBench: A Reasoning-First AI Scientist for NationalWeather Service Forecast Discussions](https://arxiv.org/abs/2608.24954v1)

**Authors**: Manmeet Singh, Somnath Luitel, Prabhjot Singh, Manraaj Banga, Naveen Sudharsan, Josh Durkee  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.24954v1  

#### Abstract
Large language models (LLMs) hallucinate numerical values when generating high-stakes meteorological text, posing risks for weather communication. We present AFDBench, an AI meteorologist that generates professional Area Forecast Discussions (AFDs) by reasoning through structured AI weather forecast...

---

### 17. [Drift Variation Autoencoder: Unifying Generation and Representation Learning through Conditional Posterior Flow Matching](https://arxiv.org/abs/2608.25138v1)

**Authors**: Jiarui Cao  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2608.25138v1  

#### Abstract
Stochastic masking, cropping, or modality removal makes deterministic reconstruction an incomplete target: one observation can admit many clean completions. This work takes the corresponding posterior $P(X\mid C)$ as the common statistical object for conditional generation and generatively sufficien...

---

### 18. [DataKernelBench: Can LLMs Optimize Database Queries on GPUs?](https://arxiv.org/abs/2608.25061v1)

**Authors**: Gokul Karthik Kumar, Yotam Perlitz, Corey Lammie, Andrea Giovannini, Katja Hose  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 37.0  
**Type**: new  
**ArXiv ID**: 2608.25061v1  

#### Abstract
GPUs increasingly accelerate database systems, but query-specific peak performance still often relies on hand-written kernels. Existing LLM kernel benchmarks focus on machine learning operators, leaving irregular, heterogeneous, data-movement-heavy database-style operators untested. We introduce Dat...

---

### 19. [Drift-Aware Multimodal User Representation Learning via Multi-Scale Temporal Modeling and Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.25773v1)

**Authors**: Ziqing Qian, Haohang Chen, Shengqi Dang, Yuhan Xiong, Canyu Shen, Jiaying Lei, Nan Cao  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2608.25773v1  

#### Abstract
Understanding user preferences from noisy and temporally evolving social media behaviors is fundamentally challenging due to interest drift, where user preferences shift across time and exhibit both multi-scale temporal patterns and diverse co-existing interests. To address this, we propose DUMoE, a...

---

### 20. [Rollout-Decoded Reconstruction for Long-Horizon Prediction in Latent World Models](https://arxiv.org/abs/2608.25017v1)

**Authors**: Rishi Shah, Rishav Shrestha  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2608.25017v1  

#### Abstract
A latent world model trains its decoder on latents anchored to observations, then deploys it on the model's own free-running rollout, hundreds of steps past the last observation. Rollout-Decoded Reconstruction (RDR) closes this gap with a single loss term that free-runs the model during training exa...

---

### 21. [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](https://arxiv.org/abs/2608.24041v1)

**Authors**: Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang,  Shoushan, Guodong Zhou  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.24041v1  

#### Abstract
Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively t...

---

### 22. [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571v1)

**Authors**: Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2608.24571v1  

#### Abstract
Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-creation systems patch this by prompting a frozen LLM at inference time, leaving the model that writes a tool decoupled from the one that uses it, with no signal that the schemas it produces are schemas it...

---

### 23. [Less can be More: Relieving RAG Bottlenecks via Evidence Frontloading and Pressure-Adaptive Budgeting](https://arxiv.org/abs/2608.25115v1)

**Authors**: Weibin Cai, Reza Zafarani  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.25115v1  

#### Abstract
Existing methods for improving Retrieval-Augmented Generation (RAG) efficiency mainly optimize downstream LLM generation, such as context compression or serving optimization. However, RAG is an end-to-end system, and its bottleneck can shift between upstream reranking and downstream generation under...

---

### 24. [Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction](https://arxiv.org/abs/2608.24001v2)

**Authors**: Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen, Keke Chen  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.24001v2  

#### Abstract
Large language models (LLMs) are increasingly used for future prediction, motivating the use of multiple models as a wisdom-of-the-crowd mechanism. However, simply increasing crowd size does not guarantee effective diversity, as different LLMs may exhibit redundant behaviors. We propose a behavior-a...

---

### 25. [SHSP: Structure-Aware Hierarchical Solution Prediction for Mixed-Integer Linear Programming](https://arxiv.org/abs/2608.25282v1)

**Authors**: Zherong Zhang, Guanlin Li, Chengrui Gao, Haopu Shang, Ke Xue, Jixiang Lu, Weiyong Yang, Chao Qian  
**Category**: cs.LG  
**Published**: 2026-08-27  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.25282v1  

#### Abstract
Mixed-Integer Linear Programming (MILP) is a fundamental optimization paradigm in combinatorial optimization and has been widely applied across real-world domains. Due to its NP-hard nature, obtaining optimal solutions for large-scale or highly constrained MILP instances remains computationally proh...

---

### 26. [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978v1)

**Authors**: Zhengxiang Wang, Owen Rambow  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.23978v1  

#### Abstract
Visual grounding is typically evaluated as a one-shot mapping from an informative referring expression to a visual target. This formulation misses a central property of real-world reference: target information is often incomplete, ambiguous, and established through interaction. We introduce a contro...

---

### 27. [Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks](https://arxiv.org/abs/2608.24258v1)

**Authors**: Su Myat Noe, Ha Thanh Nguyen, May Myo Zin, Ken Satoh  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.24258v1  

#### Abstract
AI systems are increasingly evaluated for legally accountable settings, where correct outputs must also be justifiable against an applicable legal standard. Existing legal-AI benchmarks and LLM-as-judge protocols provide important infrastructure for measuring task performance and open-ended response...

---

### 28. [Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments](https://arxiv.org/abs/2608.24099v1)

**Authors**: Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, Lin Fu, Hong Zhou  
**Category**: cs.AI  
**Published**: 2026-08-27  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.24099v1  

#### Abstract
GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations...

---

### 29. [Adaptive Triggering for Bias Correction in LLM Reasoning](https://arxiv.org/abs/2608.25379v1)

**Authors**: Nayoung Kim, Mickey Mancenido, Huan Liu  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.25379v1  

#### Abstract
Chain-of-thought prompting can expose and amplify demographic stereotypes within an LLM's intermediate reasoning and create a failure mode that final-answer debiasing alone cannot address. Mitigating such bias during generation presents a fundamental timing problem: intervening too late allows biase...

---

### 30. [Overview of SHROOM-Visions 2026: A Shared Task on Hallucination Detection in Large Vision-Language Models](https://arxiv.org/abs/2608.25662v1)

**Authors**: Ra\'ul V\'azquez, Aman Sinha, Chuyuan Li, Claudio Savelli, Eduardo Cal\`o, Emilio Raimond, Stella Frank, Hengyu Luo, Flavio Giobergia, Vincent Segonne, Lorenzo Vaiani, J\"org Tiedemann, Timothee Mickus  
**Category**: cs.CL  
**Published**: 2026-08-27  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.25662v1  

#### Abstract
In 2026, we held the fourth iteration of the SHROOM Shared Task series: SHROOM-Visions (\textbf{S}hared-task on \textbf{H}allucinations and \textbf{R}elated \textbf{O}bservable \textbf{O}vergeneration \textbf{M}istakes in \textbf{Vision} language model\textbf{s}), which is hosted at the UncertaiNLP ...

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
