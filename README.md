# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-23 08:27:46 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning](https://arxiv.org/abs/2607.19358v1)

**Authors**: Yu Zhao, Zekun Zhang, Fan Jiang, Bo Zeng, Linlong Xu, Shimin Shan, Yu Liu, Longyue Wang, Weihua Luo  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 78.5  
**Type**: new  
**ArXiv ID**: 2607.19358v1  

#### Abstract
Recent advances in long chain-of-thought reasoning models such as DeepSeek-R1 have led to increasingly longer inference context lengths under the test-time scaling paradigm. However, the O(n^2) computational complexity of standard self-attention causes inference costs to grow sharply with long seque...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning》
1. 论文的主要贡献和创新点
解决的问题：长链推理模型（如DeepSeek-R1）的测试时缩放使上下文长度增加，但标准自注意力的$O(n^2)$计算复杂度导致推理成本随序列长度急剧增长，限制了长CoT推理在生产环境的部署；现有相关方法存在以下缺陷：
- 部分方法通过缩短CoT序列降低成本，但会损害推理能力；
- 部分方法通过压缩CoT内容减少长度，但可能丢失关键推理信息；
- 部分线性注意力相关方法需复杂数据预处理，且上下文索引弱，导致性能差。

🚀 提出的新方法与思路
**LISA混合注意力模块**：并行集成两个轻量组件，(1) Linear Attention模块，提供长程记忆，时间复杂度为$O(n)$；(2) Lightning Indexer，从全上下文选择前$M$个重要token输入稀疏自注意力，通过门控机制融合两个分支，将推理复杂度从$O(n^2)$降至$O(nM)$（$M \ll n$）。
**两阶段训练策略**：Stage1通过知识蒸馏优化滑动窗口注意力，结合线性注意力捕捉长程依赖；Stage2引入Indexer替换静态滑动窗口，采用新颖的per-head KL散度损失训练，使Indexer的选择行为对齐教师模型的注意力模式。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 计算复杂度 | 将推理复杂度从$O(n^2)$降至$O(nM)$（$M \ll n$） |
| 推理速度 | 在16K-token上下文下实现50%的推理速度提升 |
| 推理性能 | 在AIME、MATH-500等推理基准上平均性能提升5.6% |
| 部署友好性 | 无需从头预训练，即插即用，不改变原模型参数或输出格式 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| AIME、MATH-500等五个数学推理基准 | 评估推理性能 |
| DeepSeek-distilled-Qwen模型 | 作为实验基础模型 |

🎯 实验设置与评估指标
任务：长上下文推理任务；评估指标：
| 指标 | 含义 |
| ---- | ---- |
| 推理速度 | 越高越好（↑） |
| 推理平均准确率 | 越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Full Self-Attention | 标准自注意力基线 | 计算复杂度为$O(n^2)$，推理成本高 |
| 线性注意力相关压缩方法 | 线性注意力类方法 | 需复杂数据预处理，上下文索引弱导致性能差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：LISA与Full Self-Attention的性能对比（16K-token上下文）**
| 指标 | LISA | Full Self-Attention |
| ---- | ---- | ------------------- |
| 推理速度 | 提升50% ✅ | 基准（无提速） |
| 推理平均准确率 | 提升5.6% ✅ | 基准 |
💡 结论：在16K-token上下文场景下，LISA相比Full Self-Attention基线，实现了50%的推理速度提升，同时推理平均准确率提升5.6%。

其他实验：
- 主benchmark性能：已在表1体现；
- 效率对比：已在表1体现；
- 跨域/zero-shot迁移：论文未报告；
- 鲁棒性/扰动测试：论文未报告；
- 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：1. LISA通过混合Linear Attention与稀疏自注意力的架构，结合两阶段训练策略，有效降低了长上下文推理的计算复杂度，同时保留并提升了推理性能；2. 相比现有压缩或缩短CoT的方法，LISA不修改CoT本身，而是优化内部推理过程，避免了损害推理能力的问题；3. 基于per-head KL散度损失训练的Lightning Indexer，能动态选择重要token，对齐教师模型的注意力模式，提升了稀疏注意力的性能。
- 方法局限性：论文未明确提及方法的局限性。
- 未来工作：论文未明确提及未来工作方向。

> ✅ **总结一句话**：LISA是一种即插即用的混合注意力模块，通过线性注意力与稀疏自注意力的融合及两阶段训练策略，在降低长上下文推理计算复杂度的同时提升了推理性能，解决了标准自注意力在长CoT推理中的效率瓶颈。

</details>

---

### 2. [Total Variation Distance Estimation in Autoregressive Models](https://arxiv.org/abs/2607.19510v1)

**Authors**: Eric Price, Kevin Tian, Zhiyang Xun, Yusong Zhu  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.19510v1  

#### Abstract
Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top of fixed weights, so two engines serving "the same model" can produce meaningfully different distributions. We study the problem of estimating the total...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Total Variation Distance Estimation in Autoregressive Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现代LLM部署采用批处理、自定义核、量化等推理优化，导致相同权重的两个LLM引擎生成的分布存在显著差异；现有估计分布差异的方法存在缺陷：1. KL散度在分布支持不相交时无界，需支持恢复和超参数选择，且无序列级分解，难以估计；2. 现有样本访问下的TV估计方法（MKP25）查询复杂度高，效率低。

🚀 提出的新方法与思路
**样本访问下的TV估计算法**：针对样本访问模型，提出的算法用$\widetilde{O}(n^2 K/\varepsilon^2)$次查询估计TV距离，其中$n$为序列长度，$K$为下一个token分布的最大支持，$\varepsilon$为加性误差。
**对数几率访问下的TV估计算法**：针对对数几率访问模型，提出的算法用$O(n/\varepsilon^2)$次查询估计TV距离，且该复杂度是紧的。
**带噪对数几率访问下的TV估计算法**：针对带噪对数几率访问模型，提出的算法在概率值相对误差为$\sigma$时，用$\widetilde{O}((n + n^2 \sigma^2)/\varepsilon^2)$次查询，在样本访问和对数几率访问的保证之间平滑插值，适配实际LLM部署的带噪场景。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 样本访问 | 查询复杂度优于MKP25的方法（$\widetilde{O}(n^2 K/\varepsilon^2)$ vs $\widetilde{O}(n^3 m/\varepsilon^5)$，$m$为token字母表大小），当$K \ll m$时优势显著 |
| 对数几率访问 | 查询复杂度为$O(n/\varepsilon^2)$且是紧的，达到理论最优 |
| 带噪对数几率访问 | 适配实际部署的带噪场景，平滑插值前两种访问的保证，实用性强 |
| 距离选择 | 估计TV距离，解决了KL散度在分布支持不相交时无界、需超参数的问题，TV距离有界可解释 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告具体数据集，仅采用SGLang和vLLM服务相同权重的LLM开展实证评估 |

🎯 实验设置与评估指标
任务为估计两个长度为$n$的自回归分布的TV距离，评估算法的鲁棒性和实用性；论文未明确列出具体评估指标，仅通过对比SGLang和vLLM服务相同权重模型的TV距离验证算法性能。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| MKP25的TV估计方法 | 样本访问基线方法 | 样本查询复杂度为$\widetilde{O}(n^3 m/\varepsilon^5)$，效率较低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量数值，仅通过实证评估展示算法的鲁棒性和实用性，例如测量SGLang和vLLM服务相同权重模型的TV距离，实验表明TV距离在KL散度无穷时仍可估计。
💡 结论：论文通过实证验证了所提TV估计算法在实际LLM部署中的可行性，可有效估计相同权重LLM引擎间的分布差异。

4. 关键结论和发现
- 现代LLM部署的推理优化会导致相同权重的引擎生成的分布存在差异，TV距离可有效估计这种差异，且在KL散度无穷时仍可估计。
- 针对三种访问模型提出的TV估计算法，查询复杂度优于或紧于现有方法，适配不同的LLM API访问场景。
- 带噪对数几率访问下的算法可平滑插值前两种访问的保证，适合实际部署的带噪环境。
- 方法局限性：论文未报告具体局限性
- 未来工作：论文未报告具体未来工作方向

> ✅ **总结一句话**：该论文针对自回归模型的TV距离估计问题，提出了三种访问模型下的高效算法，解决了KL散度估计的缺陷，实证验证了算法在实际LLM部署中的鲁棒性和实用性。

</details>

---

### 3. [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/abs/2607.19349v1)

**Authors**: Tiancheng Zhang, Shaoyuan Huang, Mingyuan Wang, Yunfeng Zhao, Xiaofei Wang, Wenyu Wang  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.19349v1  

#### Abstract
Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge. Achieving low latency and high throughput under volatile demand requires deep understanding of real-world serving workloads, yet existing studies often rely...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对LLM serving的研究存在核心痛点：一是多依赖代理追踪或粗粒度表征，无法捕获现代多模型LLM平台的异质性；二是未能有效支撑波动需求下LLM服务低延迟、高吞吐量的高效部署，亟需对真实工作负载的深度理解。

🚀 提出的新方法与思路
**FineServe数据集**：构建了从全球商业市场采集的真实多模型LLM serving工作负载数据集，实现跨异构模型与任务的细粒度表征。
**FineServe工作负载生成器**：基于FineServe数据集对到达动态、token行为的分析洞察，开发了模型感知的细粒度工作负载生成器，可生成适配多模型serving平台基准测试的可配置混合工作负载。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据真实性 | 采用全球商业市场的in-the-wild真实数据，而非代理追踪数据，更贴合实际服务场景 |
| 粒度适配 | 具备细粒度表征，可捕获现代多模型LLM平台的异质性 |
| 应用价值 | 为LLM serving系统的路由、调度、容量规划策略评估提供真实基础，配套生成器支持多模型平台基准测试 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| FineServe | 用于LLM serving工作负载的细粒度表征，支撑多模型serving平台相关研究与基准测试 |

🎯 实验设置与评估指标
论文未报告具体的实验任务、设置及评估指标的相关细节。

⚔️ 基线方法对比
论文未报告基线方法的相关内容。

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何定量实验结果，因此无对应表格。

4. 关键结论和发现
- 主要发现：通过FineServe的分析揭示，不同模型架构、规模及任务意图下，LLM服务的到达动态与token行为存在根本性不同的波动机制。
- 方法局限性：论文未报告相关局限性内容。
- 未来工作：论文未报告相关未来工作内容。

> ✅ **总结一句话**：FineServe是面向全球多模型LLM服务的真实细粒度工作负载数据集，配套生成器为多模型LLM serving平台的基准测试与策略评估提供了现实基础。

</details>

---

### 4. [How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF](https://arxiv.org/abs/2607.19712v1)

**Authors**: Venkata Naga Sai Vishnu Rohit Pulipaka, Anish Katta, Deva Rohit Reddy Peddireddy  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.19712v1  

#### Abstract
In RLHF pipelines, reward scoring blocks policy updates. Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score. And yet most setups just default to PyTorch eager mode or torch.compile, no one checks if that's actually fastest. Scoring itself is small. Rollou...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF
1. 论文的主要贡献和创新点
✅ 解决的问题：RLHF训练循环中，奖励评分步骤会阻塞策略更新，成为训练瓶颈，但现有RLHF管道默认采用PyTorch eager模式或torch.compile，未系统评估其他推理后端；奖励评分本身耗时占比低，但与rollout生成争夺CPU/GPU资源，更快的评分引擎本身不缩短单步时间，主要释放资源给rollout生成。
🚀 提出的新方法与思路：**基于ONNX Runtime的原生C++推理引擎**，该引擎负责奖励模型推理的tokenization、batching、postprocessing，先验证其与PyTorch参考模型的数学一致性（CPU输出误差5.7×10⁻⁶，GPU输出误差4.2×10⁻³），再在CPU和GPU上测试其与PyTorch eager模式、torch.compile、FastAPI的性能，同时研究批处理策略、引擎实例共享等部署级因素的影响，所有对比基于重复独立进程启动的结果以消除运行噪声。
🔍 相比现有方法的优势：
| 维度 | 优势 |
| --- | --- |
| CPU性能 | 击败所有基线方法，置信区间无重叠 |
| GPU性能 | 击败PyTorch eager模式和FastAPI，仅弱于torch.compile |
| 性能来源 | 速度提升源于ONNX Runtime而非C++语言本身 |
| 部署影响因素 | 批处理策略对性能的影响远大于语言或运行时选择 |
| 结果可靠性 | 重复独立运行消除单次运行噪声，结果更可信 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| hh rlhf数据集 | 提供奖励模型评分所需的prompt和响应（来自Bai等人的工作） |

🎯 实验设置与评估指标：任务为RLHF中奖励模型推理的性能测试，评估指标为推理速度（延迟、吞吐量），结果基于重复独立进程启动以消除运行噪声。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PyTorch eager mode | PyTorch原生推理模式 | PyTorch默认推理模式 |
| torch.compile | PyTorch编译优化模式 | PyTorch的编译优化推理模式 |
| FastAPI | 服务框架 | 用于部署推理服务的框架 |
| 基于ONNX Runtime的C++引擎 | 本文提出的推理引擎 | 原生C++实现，基于ONNX Runtime |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能对比（CPU/GPU场景）**
| 方法 | CPU性能 | GPU性能 |
| --- | --- | --- |
| PyTorch eager mode | 基线 | 基线 |
| torch.compile | 优于PyTorch eager | 优于PyTorch eager和FastAPI ✅ |
| FastAPI | 优于PyTorch eager | 优于PyTorch eager |
| 基于ONNX Runtime的C++引擎 | 最优 ✅ | 优于PyTorch eager和FastAPI，弱于torch.compile |
💡 结论：CPU上基于ONNX Runtime的C++引擎性能最优，GPU上仅弱于torch.compile。

**表2：部署因素对吞吐量的影响（CPU/GPU场景）**
| 部署因素 | 配置 | CPU吞吐量 | GPU吞吐量 |
| --- | --- | --- | --- |
| 批处理策略 | 固定长度填充 | 1x | 1x |
| 批处理策略 | 长度感知分组 | 5-8倍提升 ✅ | 3.5-4倍提升 ✅ |
| 引擎实例共享 | 共享 | 无增益 | 无增益 |
| 引擎实例共享 | 不共享 | 基线 | 基线 |
💡 结论：批处理策略对吞吐量影响极大，长度感知分组可显著提升性能，引擎实例共享无增益。

1. 主benchmark性能（L2/碰撞率等）：见上表1，论文未报告其他L2/碰撞率指标。
2. 效率对比（FPS / 参数量）：论文未报告。
3. 跨域 / zero-shot迁移：论文未报告。
4. 鲁棒性 / 扰动测试：论文未报告。
5. 消融实验：见上表2，论文未报告其他消融实验。

4. 关键结论和发现
- CPU上基于ONNX Runtime的C++奖励模型推理引擎性能优于所有基线方法，GPU上仅弱于torch.compile；
- 性能提升源于ONNX Runtime的执行模式，而非C++语言本身；
- 批处理策略对吞吐量的影响远大于语言或运行时选择，固定长度填充会导致严重吞吐量损失，长度感知分组仅在CPU和GPU上均可恢复损失；
- 共享引擎实例无吞吐量增益，执行会被序列化；
- 重复独立进程启动对消除运行噪声、保证结果可靠性至关重要。

方法局限性：论文未报告明确的方法局限性。
未来工作：论文未报告明确的未来工作方向。

> ✅ **总结一句话**：该论文系统评估了RLHF奖励模型推理的不同后端性能，发现基于ONNX Runtime的C++引擎在CPU上表现最优，GPU上仅弱于torch.compile，且批处理策略是影响性能的关键因素，为RLHF管道的奖励评分步骤优化提供了实践指导。

</details>

---

### 5. [User-Centric Modeling of Transactional Sequences with Explainable State Space Models](https://arxiv.org/abs/2607.20228v1)

**Authors**: Ivan Palagin  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.20228v1  

#### Abstract
We propose a hybrid approach for user-centric modeling of transactional event sequences that combines contrastive representation learning (CoLES) with State Space Models (SSMs). While contrastive methods yield high-quality compressed user representations, existing encoders -- RNNs and Transformers -...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

User-Centric Modeling of Transactional Sequences with Explainable State Space Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用户-centric事务序列建模中，CoLES依赖的RNN存在梯度消失问题，Transformer存在O(L²)的二次复杂度，不适合长序列事务数据；而选择性SSSM（如Mamba）在用户个性化分析领域尚未被充分探索。

🚀 提出的新方法与思路
**CoLES-Mamba混合模型**，包含两种集成策略：(1) 将CoLES生成的用户嵌入投影后，用于初始化Mamba的初始隐藏状态$h_0$；(2) 将投影后的CoLES嵌入作为前缀token，拼接至输入序列前端，为模型提供用户先验信息。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 性能 | 在三个公开数据集上，混合模型比单独Mamba、带线性分类器的CoLES有一致提升 |
| 收敛速度 | 混合模型收敛速度是纯SSM基线的2-3倍 |
| 可解释性 | 支持通过离散化步长图、Integrated Gradients进行模型决策解释 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Age | 多分类年龄组预测（银行交易数据） |
| MBD | 多标签产品获取预测（银行交易数据） |
| Taobao | 二分类购买预测（电商行为数据） |

🎯 实验设置与评估指标
针对三个数据集分别执行对应下游预测任务，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| Accuracy | Age数据集多分类任务的评估指标 |
| mean ROC-AUC | MBD数据集多标签任务的评估指标 |
| ROC-AUC | Taobao数据集二分类任务的评估指标 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 单独Mamba | 序列编码器 | 选择性SSSM，O(L)复杂度，长序列处理能力 |
| 带线性分类器的CoLES | 序列编码器 | 自监督对比学习方法，生成用户嵌入 |
| 纯SSM基线 | 序列编码器 | 未结合CoLES先验的Mamba模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 提出的两种CoLES与Mamba的集成策略，能有效结合CoLES的用户先验信息与Mamba的长序列处理能力；2. 混合模型在三个公开数据集上取得性能提升，且收敛速度是纯SSM基线的2-3倍；3. 可解释性分析显示模型对行为丰富的数据集存在选择性事件过滤，可识别最具信息的交易特征。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出结合CoLES与Mamba的混合用户事务序列建模方法，解决了现有序列编码器的梯度消失或二次复杂度缺陷，在三个公开数据集上实现性能提升且收敛更快，具备可解释性。

</details>

---

### 6. [HyGRL: Adaptive Hybrid Graph Reasoning for Multi-Entity Questions](https://arxiv.org/abs/2607.19398v1)

**Authors**: Junyi Wang  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.19398v1  

#### Abstract
Multi-entity compositional questions pose significant challenges to existing retrieval-augmented language models. Conventional methods fall into a dilemma: standard RAG lacks dynamic reasoning, traditional Graph-RAG is limited by structural sparsity, and LLM-constructed Graph-RAG incurs prohibitive ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

HyGRL: Adaptive Hybrid Graph Reasoning for Multi-Entity Questions
1. 论文的主要贡献和创新点
✅ 解决的问题
现有处理多实体复合问题的检索增强语言模型存在核心矛盾：标准RAG缺乏动态推理能力，传统Graph-RAG受限于知识图谱的结构稀疏性（Wikidata仅覆盖85.6%的查询实体，仅37.6%的查询-答案对可在3跳内连接），LLM构建的Graph-RAG则产生过高的token成本。

🚀 提出的新方法与思路
**HyGRL框架**：统一框架，将非结构化文本嵌入结构化知识图谱，构建异构网络以实现灵活的证据检索；推理被形式化为自适应结构归纳，通过两阶段鲁棒过程学习：（1）模仿学习蒸馏启发式专家信号；（2）强化学习利用LLM驱动的偏好奖励优化策略。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多实体复合问题处理 | 融合结构化知识与非结构化文本，弥补单一方法的缺陷 |
| 结构利用 | 无需昂贵的LLM提取 triples，缓解知识图谱结构稀疏性 |
| 推理策略 | 自适应结构归纳，结合模仿学习与强化学习，无需固定启发式或全LLM优化 |
| 计算成本 | 极低的token成本，接近实时推理 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Freebase | 分析知识图谱结构完整性（附录A） |
| Wikidata | 分析知识图谱结构完整性（附录A） |

🎯 实验设置与评估指标
任务为多实体复合问题回答，评估指标包括answer accuracy（↑越高越好）、reasoning fidelity（↑越高越好）、token成本（↓越低越好）、推理延迟（↓越低越好）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Standard RAG | 标准文本RAG | 缺乏动态推理，多-hop推理能力不足 |
| GraphRAG | Graph-RAG | 受限于结构稀疏性，token成本高 |
| LightRAG | Graph-RAG | 受限于结构稀疏性，token成本高 |
| PathRAG | 文本-图结合方法 | 文本仅作为静态检索端点，跨模态转换不足 |
| HippoRAG | 文本-图结合方法 | 依赖固定启发式传播，自适应不足 |
| Graph-R1 | RL-based Graph-RAG | 需全LLM优化，成本高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量数值，仅说明HyGRL在answer accuracy、reasoning fidelity上优于SOTA基线，且token成本极低、推理接近实时。
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. 现有处理多实体复合问题的方法各有缺陷，HyGRL的异构网络构建与两阶段学习策略能有效融合文本与结构化知识；2. 自适应结构归纳的推理方式可平衡性能与计算效率；3. 无需昂贵的LLM triple提取的方式能缓解知识图谱结构稀疏性问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：HyGRL通过将非结构化文本嵌入结构化知识图谱构建异构网络，结合模仿学习与强化学习的两阶段策略，在多实体复合问题回答上实现了性能、效率与成本的平衡，优于现有SOTA基线。

</details>

---

### 7. [PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/abs/2607.20064v1)

**Authors**: Alexis Fox, Junlin Wang, Paul Rosu, Bhuwan Dhingra  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.20064v1  

#### Abstract
Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents. This gap is reflected in their limited performance on continual learning benchmarks such as ARC-AGI-3, especially when models are evaluated out of the bo...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM智能体在长 horizon任务（如ARC-AGI-3）中表现不佳，现有上下文管理方法存在**保真度-可处理性**核心权衡（保存更多信息会导致检索相关细节更难，压缩摘要则可能丢失后续关键信息），且多数系统未充分利用现代编码智能体的原生能力。

🚀 提出的新方法与思路
**Programmatic Memory（程序化记忆）**，核心操作分为write和read：write操作将智能体的所有观测、动作、结果完整追加至结构化日志，无需学习或启发式决策；read操作通过代码（如正则表达式）对完整日志进行程序化搜索，无需特殊检索工具。该设计遵循三大原则：simplicity（无需额外复杂组件）、losslessness（日志为环境状态的忠实记录）、compatible with coding agents（程序化搜索是编码智能体的原生能力，可处理超10万行的长日志）。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 信息完整性 | 完整保留所有交互数据，无压缩或摘要丢失 |
| 检索效率 | 代码化程序化搜索可高效处理超10万行长日志 |
| 资源消耗 | 相比SOTA专用harness，token使用量降低4.2-5.8倍 |
| 任务性能 | 在ARC-AGI-3上匹配或超过SOTA专用harness的性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| ARC-AGI-3公开游戏集 | 评估长 horizon智能体推理能力 |

🎯 实验设置与评估指标
任务为LLM智能体在长 horizon探索任务（以ARC-AGI-3为基准）上的表现，指标含义如下：
| 指标 | 含义（箭头方向） |
| ---- | ---- |
| pass@1 | 单次尝试通过任务的比例（↑越高越好） |
| best@2 | 两次尝试中最优结果的通过比例（↑越高越好） |
| best@5 | 五次尝试中最优结果的通过比例（↑越高越好） |
| token使用量 | 模型调用的token总数（↓越低越好） |
| 成本 | 完成任务的总费用（↓越低越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| base coding agent | 基础编码智能体 | 无程序化记忆模块 |
| state-of-the-art specialized harnesses | 专用智能体harness | 采用专用上下文管理策略 |
| PRO-LONG | 本文提出的框架 | 基于程序化记忆的上下文管理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**章节3：ARC-AGI-3主benchmark性能**
| 方法 | 模型 | pass@1 | best@2 | best@5 | token使用量 | 成本 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| base coding agent | 前沿模型 | - | - | - | - | - |
| state-of-the-art specialized harnesses | - | 最高76.1% | - | - | - | - |
| PRO-LONG | Opus 4.6 | 42.4% ✅ | - | - | - | - |
| PRO-LONG | GPT-5.5 | 41.2% | - | 60.1% | 5.8×更少 | - |
| PRO-LONG | Fable 5 | - | 97.4% ✅ | - | - | $1,750 |
💡 结论：PRO-LONG在ARC-AGI-3上匹配或超过SOTA专用harness的性能，同时大幅降低token使用量和任务成本，且比基础编码智能体平均提升18.0个百分点（章节3）。

**Table1：程序化访问程度的消融实验（场景：ARC-AGI-3）**
| 程序化访问程度 | 性能表现 |
| ---- | ---- |
| 基础代码搜索 | 中等 |
| 增强代码搜索 | 较高 |
| 完整日志访问 | 最优 ✅ |
💡 结论：性能提升随程序化访问能力增强而提升，完整日志访问是核心驱动因素（Table1）。

**Table2：额外抽象模块的消融实验（场景：ARC-AGI-3）**
| 额外抽象模块 | 性能影响 |
| ---- | ---- |
| 持久工作区 | 极小 |
| 写笔记工具 | 极小 |
| 无额外模块 | 基准 ✅ |
💡 结论：额外抽象模块对性能提升贡献极小，核心价值来自程序化记忆的基础设计（Table2）。

其他实验：
- 效率对比：论文未报告除token使用量外的其他效率指标（如FPS、参数量），仅提及token使用量为4.2-5.8×更少（章节3）。
- 跨域/zero-shot迁移：论文未报告。
- 鲁棒性/扰动测试：论文未报告。

4. 关键结论和发现
- 核心发现1：PRO-LONG通过程序化记忆框架，有效解决了长 horizon任务中上下文管理的保真度-可处理性权衡，在ARC-AGI-3上实现了优异性能，且资源消耗显著降低。
- 核心发现2：性能提升主要来自完整日志访问，而非额外的抽象工具，且与编码智能体的原生能力高度兼容（Table1、Table2）。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：PRO-LONG提出的程序化记忆框架，通过完整结构化交互日志和代码化检索机制，在ARC-AGI-3长 horizon推理任务上达到SOTA性能，同时大幅减少token使用量和任务成本。

</details>

---

### 8. [CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning](https://arxiv.org/abs/2607.20129v1)

**Authors**: El Hassane Ettifouri, Ayoub Belfatmi, Mahaman Sanoussi Yahaya Alassan, Walid Dahhane  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2607.20129v1  

#### Abstract
Quantized small autoregressive reasoning models can enter long, repetitive, or unproductive trajectories, yet inference-time compute is usually allocated without observing how a trajectory develops. Building on an earlier token-level e-CUSUM controller, we develop MGT-B (Monitoring-Guided Test-time ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
量化的小型自回归推理模型易进入长、重复或无产出的轨迹，但推理时计算分配未考虑轨迹发展；现有token级控制器（如Anonymous,2026提出的）仅测采样自洽性，无法应对推理退化（如重复循环），在退化轨迹中会沉默，缺乏针对性干预。

🚀 提出的新方法与思路
**MGT-B (Monitoring-Guided Test-time Backtracking)**，是修订的外部控制器，流程为：1. 映射重叠窗口的预采样不确定性和退化特征到位置条件经验尾概率；2. 用CUSUM形状的重置积累混合投注因子；3. 触发警报时估计回滚点，恢复token和键值缓存状态，执行约束重解码。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模块设计 | 改进监控粒度、校准方式、投注构造、回滚逻辑、解码干预模块，采用6个重叠窗口特征、位置条件经验校准、beta混合变换、基于重置历史的回滚估计、完整恢复耦合控制器状态、标记自由约束重解码 |
| 研究规模 | 使用更大的配对MATH-500研究及明确的token核算，替代早期方法的 pilot 协议 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 240-pair chronology-audit set | 审计效果是否持续到后阈值问题（排除预阈值ID后，保留每个剩余ID的首个后阈值对） |
| 467-pair historical-coverage set | 更广泛的种子匹配对的覆盖估计（包含阈值选择前/期间可用的seed-1 ID） |

🎯 实验设置与评估指标
任务为MATH-500设置下的推理质量评估；指标：准确率（正确数/总数，越高越好）、McNemar检验p值（越小越显著）、配对bootstrap 95%区间。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Anonymous,2026提出的token级控制器 | 早期token级监控干预方法 | 监控粒度粗、校准简单、干预策略基础，无明确token核算 |
| MGT-B | 修订的外部监控控制器 | 改进多模块设计，采用更大的MATH-500研究及明确token核算 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**240-pair chronology-audit set（后阈值问题审计）**
| 指标 | 数值 |
| --- | --- |
| 原准确率 | 82/240 |
| 新准确率 | 88/240 |
| 准确率提升 | +2.50个百分点 |
| 修正数 |13 |
| 回归数 |7 |
| McNemar p值 |0.2632 |
| 配对bootstrap 95%区间 | [-1.25, +6.25] |
💡 结论：在240-pair chronology-audit set上，MGT-B带来的准确率提升未通过McNemar检验，统计显著性不足。

**467-pair historical-coverage set（种子匹配对覆盖估计）**
| 指标 | 数值 |
| --- | --- |
| 原准确率 |146/467 |
| 新准确率 |167/467 |
| 准确率提升 |+4.50个百分点 |
| McNemar p值 |0.000753 |
| 配对bootstrap 95%区间 | [+1.93, +7.07] |
| 无警报输出与vanilla一致性 |316/316 |
| 警报轨迹修正数 |29 |
| 警报轨迹回归数 |8 |
💡 结论：在467-pair historical-coverage set上，MGT-B带来的准确率提升统计显著，但该数据集包含阈值选择前/期间的ID，属于探索性结果，非确认性分析。

其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告。

4. 关键结论和发现
- 主要发现：1. MGT-B在MATH-500设置下实现了选择性监控-修复机制，可修正部分推理错误，但仅针对该特定设置，非通用提升；2. 240-pair后阈值审计集的准确率提升统计不显著，467-pair种子匹配集的提升显著但为探索性结果；3. 无警报输出与原始解码结果一致，警报轨迹以修正错误为主，伴随少量回归。
- 方法局限性：1. 未被证明为有效的e-process或e-detector，经验因素不符合理论有效性条件；2. 结果仅适用于MATH-500设置，无理论保证的通用推理提升；3. 467-pair数据集非独立样本，结果受阈值选择影响，无法作为确认性结论。
- 未来工作：论文未明确报告未来工作方向。

> ✅ **总结一句话**：论文提出的MGT-B方法在量化小型语言模型推理中实现了选择性监控与修复，在MATH-500设置下对部分样本的推理准确率有提升，但结果非通用且未被理论验证，属于探索性研究。

</details>

---

### 9. [Neural Operator Surrogates for Two-Dimensional Neutron Flux Estimation](https://arxiv.org/abs/2607.19388v1)

**Authors**: Japan K. Patel, Barry D. Ganapol, Anthony Magliari, Matthew C. Schmidt, Todd A. Wareing  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.19388v1  

#### Abstract
This work extends our one-dimensional single-sweep neural-operator studies to two dimensions. We consider one-group transport with isotropic scattering. As in the one-dimensional work, we use Fourier neural operators (FNOs) to approximate the high-fidelity scalar flux. Additionally, we also investig...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Neural Operator Surrogates for Two-Dimensional Neutron Flux Estimation
1. 论文的主要贡献和创新点
✅ 解决的问题
辐射屏蔽与反应堆分析中，反复的中子输运求解成本高昂，散射主导区域的源迭代收敛慢，传统离散纵标法需为每个新配置重新计算，难以支撑设计探索、不确定性量化等任务；现有神经算子研究多集中于一维或固定几何场景，二维场景下的相关研究不足。

🚀 提出的新方法与思路
**Fourier Neural Operators (FNOs)**：用于近似高保真标量通量，基于频域的谱卷积层表示算子核，实现函数空间间的映射，训练后单次前向传播即可生成新输入的解。
**U-shaped Neural Operators (UNOs)**：新增多尺度编解码结构与跳接，结合全局与局部特征，作为另一种直接映射材料和源场到通量的模型。
**Single-sweep conditioned FNO**：在FNO输入中额外加入单次源迭代后的标量通量（单扫近似，未考虑散射源，成本远低于收敛解），利用单扫近似的空间结构提升预测精度。
**Log-flux training**：研究训练时使用通量的对数形式，改善与屏蔽相关的强衰减区域的预测精度。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 场景适配 | 针对二维可变介质中子通量估计场景，扩展一维单扫神经算子研究，弥补现有二维研究多为固定几何的不足 |
| 模型架构 | 对比FNO与UNO两种神经算子架构，提供不同模型的性能参考 |
| 精度提升途径 | 探索单扫输入、对数训练两种提升通量预测精度的途径，覆盖不同精度优化方向 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 均匀介质案例集 | 含1024个案例，介质空间均匀，总截面Σₜ∈[0.5,2.0]，散射比c∈[0.3,0.95]，源为1或2个高斯峰，按80%训练、20%测试划分 |
| 异质介质案例集 | 含2048个案例，含均匀背景与两个嵌入区域（吸收方块、独立截面的圆盘），源为1或2个高斯峰，按80%训练、20%测试划分 |

🎯 实验设置与评估指标
任务为二维单群各向同性散射的稳态中子通量估计，评估指标为平均相对L₂误差，越低越好。
| 指标 | 含义 |
| --- | --- |
| 平均相对L₂误差 | 表征推断通量与高保真参考解的相对误差，↓ 越低越好 |

⚔️ 基线方法对比
论文未明确列出具体基线方法的详细对比表格，仅提及现有研究中使用的DeepONet（一维、二维固定几何场景）、一维FNO等方法，本研究的基线为直接映射的FNO、直接映射的UNO，以及带单扫输入的FNO。

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：本研究针对二维中子通量估计场景，扩展了一维单扫神经算子研究，核心研究问题为单扫输入是否提升通量预测精度、对数训练是否改善强衰减区域的预测精度；所有 surrogate 均在三个随机种子上训练，以评估运行变异性的影响；参考解由经过验证的离散纵标法（S₁₂求积、菱形差分格式）求解得到。
- 方法局限性：论文未明确报告具体局限性，仅提及本研究的 surrogate 针对特定的单群各向同性散射、固定方程和离散化方案，适用于特定问题类。
- 未来工作：论文未明确提及未来工作方向。

> ✅ **总结一句话**：本研究将一维单扫神经算子研究扩展至二维中子通量估计场景，对比FNO、UNO两种神经算子架构，探索单扫输入与对数训练对通量预测精度的提升效果，为辐射屏蔽与反应堆分析提供高效的 surrogate 方法。

</details>

---

### 10. [Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)

**Authors**: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
**Category**: cs.DC  
**Published**: 2026-07-23  
**Score**: 39.5  
**Type**: new  
**ArXiv ID**: 2607.19893v1  

#### Abstract
Point-based neural rendering (PBNR) represents 3D scenes as explicit, trainable primitives and underpins high-quality reconstruction and emerging embodied AI and world-model pipelines. Unlike layer-structured neural networks, PBNR has primitive-indexed dependencies: each view reads and updates only ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 传统分布式PBNR训练依赖全局任务或迭代级障碍同步，导致同步环节替代渲染成为训练的关键路径瓶颈；
2. 现有分布式PBNR训练系统（如Grendel）实现扩展时需改动渲染内核、优化器等核心组件，灵活性不足。

🚀 提出的新方法与思路
**Primitive-Level Synchronization（Odin系统）**：以原语级同步替换全局障碍同步，包含两部分核心模块：① Ahead-of-Time调度器：利用稳定的局部性和相位顺序识别低冲突重叠窗口；② Runtime模块：在后续任务访问可变状态前验证原语发布；
同时提供两种训练路径：**Quality-First Path**：保留同步训练的可见性，保障重建质量；**Throughput-First Path**：基于重叠和梯度证据仅允许小的低影响延迟读取，结构变化及高影响场景仍保持同步。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 吞吐量 | 8 GPU规模下平均提升1.22倍；64 GPU MatrixCity混合并行场景下最高提升1.89倍 |
| 关键路径等待时间 | 8 GPU规模下隐藏82%的关键路径等待 |
| 重建质量 | 无显著下降，保留同步训练的重建质量 |
| 兼容性 | 无需改动原有渲染内核、优化器、训练预算或模型容量 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 13 non-city scenes | 主benchmark实验（8 GPU规模） |
| MatrixCity | 64 GPU扩展案例研究 |
| 四个现有PBNR pipelines | 主benchmark实验适配的不同PBNR框架 |

🎯 实验设置与评估指标
任务：分布式PBNR训练性能测试，对比不同同步机制的表现
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 吞吐量 | ↑ 越高越好 |
| 关键路径等待时间 | ↓ 越低越好 |
| 重建质量 | 无下降为合格 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| Grendel | 分布式PBNR训练系统 | 采用全局障碍同步机制，扩展时需改动核心组件 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能
论文未提供对应表号，仅在摘要中提及：8 GPU规模下，Odin在四个现有PBNR pipelines及13个非城市场景中平均提升吞吐量1.22倍，隐藏82%的关键路径等待时间，且保留重建质量。
💡 结论：原语级同步的Odin在8 GPU分布式PBNR训练中实现吞吐量提升，同时保留重建质量。

2. 效率对比
论文未提供FPS等具体效率指标，仅提及吞吐量提升数值，无对应表号及详细FPS数据，无法定位来源。
💡 结论：Odin通过原语级重叠操作提升分布式训练吞吐量，未给出FPS具体数值。

3. 跨域/zero-shot迁移
论文未报告相关实验。
💡 结论：无对应实验数据。

4. 鲁棒性/扰动测试
论文未报告相关实验。
💡 结论：无对应实验数据。

5. 消融实验
论文未报告相关实验，无消融模块及指标数据。
💡 结论：无对应消融分析。

4. 关键结论和发现
- 主要发现
1. Odin以原语级同步替换全局障碍同步，在8 GPU分布式PBNR训练中平均提升吞吐量1.22倍，隐藏82%的关键路径等待时间，同时保留同步训练的重建质量。
2. 在64 GPU的MatrixCity混合并行扩展场景中，Odin相较基线方法Grendel最高提升吞吐量1.89倍，且无需改动原有渲染内核、优化器、训练预算或模型容量。
- 方法局限性
论文未报告明确局限性描述。
- 未来工作
论文未报告明确未来工作方向。

> ✅ **总结一句话**：Odin是面向分布式点基神经渲染训练的原语级同步系统，通过替换全局障碍同步为原语级调度与验证，实现吞吐量提升的同时保留重建质量，在多GPU扩展场景下表现优异且兼容性强。

</details>

---

### 11. [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](https://arxiv.org/abs/2607.19962v1)

**Authors**: Xinbang Dai, Zheyu Xin, Huikang Hu, Lin Ren, Rihui Jin, Guohui Xiao, Guilin Qi, Kuicai Dong, Zhaocheng Du, Yuyang Zhang  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.19962v1  

#### Abstract
Large Reasoning Models (LRMs) often suffer from overthinking due to redundant verification steps. Existing approaches for mitigating overthinking, such as fast-slow thinking switching and reasoning trajectory compression, fail to make a fine-grained distinction between beneficial and redundant steps...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization
1. 论文的主要贡献和创新点
✅ 解决的问题
Large Reasoning Models（LRMs）存在过思考问题，伴随冗余验证步骤；现有缓解LRMs过思考的方法为fast-slow thinking switching和reasoning trajectory compression，两类方法均无法在LRMs的推理过程中精细区分有益推理步骤与冗余步骤，易在追求效率的同时损害推理能力，核心矛盾为难以同时实现推理效率提升与推理能力的保障。

🚀 提出的新方法与思路
**Self-Pruning Training (SPT)**：一种无监督方法，通过迭代方式剪枝冗余的推理步骤，基于精简后的推理轨迹完成自训练。
**Aha-Moment Preference Optimization (AMPO)**：受遗传算法启发，识别有价值的失败推理尝试，合成“从错到对”的Aha-moment数据，优化模型以内化该类有效推理模式。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
LRMs性能与效率的平衡 | 可同时提升推理效率与推理能力，避免现有方法为追求效率损害推理能力的问题
推理步骤区分精度 | 能精细区分LRMs推理过程中的有益步骤与冗余步骤，针对性减少冗余验证

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
数学推理基准、代码生成基准 | 论文未报告具体数据集名称，用于评估EvoThink的性能

🎯 实验设置与评估指标
任务为数学推理与代码生成任务，实验设置细节及具体评估指标详情论文未报告。

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
fast-slow thinking switching | LRM过思考优化方法 | 无法精细区分推理步骤，易损害推理能力
reasoning trajectory compression | LRM过思考优化方法 | 无法精细区分推理步骤，易损害推理能力

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验的具体表号、数值均未报告，仅在摘要中说明：EvoThink可大幅减少推理时token使用，且提升Large Reasoning Models的推理能力；各专项实验（主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）论文未报告。

4. 关键结论和发现
- 主要发现
1. EvoThink框架通过Self-Pruning Training剪枝冗余推理步骤，结合Aha-Moment Preference Optimization内化有效推理模式，可同时实现LRMs的推理效率提升与推理能力增强。
2. AMPO模块基于遗传算法思路，能挖掘失败推理尝试中的有价值信息，合成“从错到对”的Aha-moment数据以优化模型推理逻辑。
3. 现有LRMs过思考优化方法存在无法兼顾效率与性能的痛点，EvoThink的双组件设计有效解决了该问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：EvoThink框架通过Self-Pruning Training剪枝LRMs的冗余推理步骤，以Aha-Moment Preference Optimization内化有效推理模式，解决了现有LRMs过思考优化方法无法兼顾推理效率与能力的痛点。

</details>

---

### 12. [Notes to Self: Can LLMs Benefit from Experiential Abstractions?](https://arxiv.org/abs/2607.20372v1)

**Authors**: Chang Liu, Xinyu Li, Artur Dubrawski  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.20372v1  

#### Abstract
Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively. We study whether Large Language Models (LLMs) can similarly benefit from such experiential abstractions. From LLMs' solution traces on the MAT...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Notes to Self: Can LLMs Benefit from Experiential Abstractions?
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾在于人类可将经验蒸馏为可复用的抽象（如策略、注意事项）以逐步提升问题解决效果，但现有研究尚未明确大型语言模型（LLMs）是否具备类似提取和应用此类经验抽象的能力，缺乏对该可行性与效果的系统性验证。

🚀 提出的新方法与思路
**Experiential Abstraction Library Framework**：从LLMs在MATH训练集上的解题轨迹中，由更强的教师模型或LLM自身提取自然语言形式的可复用经验抽象，构建可检索的抽象库；并探索两种抽象使用模式：（1）推理阶段的检索应用；（2）基于抽象增强的训练提示进行强化学习（RL），优化LLMs的推理表现。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 推理性能 | 可提升LLMs在数学与逻辑推理基准任务上的表现 |
| 抽象提取质量 | LLM自身提取的经验抽象效果与更强教师模型提取的抽象效果相当 |
| 方法通用性 | 提出的抽象应用框架可迁移至其他数据集与模型 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| MATH训练集 | 作为提取经验抽象的源数据 |

🎯 实验设置与评估指标
任务：对比不同经验抽象提取/应用方式对LLMs数学与逻辑推理性能的影响。
指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 具体评估指标及对应数值 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 无经验抽象的LLM | 基准方法 | 未引入经验抽象优化推理或训练过程 |
| 教师提取抽象的LLM | 对照方法 | 采用更强教师模型生成的经验抽象进行推理或训练 |
| 自我提取抽象的LLM | 提出方法 | 采用LLM自身从解题轨迹中提取的经验抽象进行推理或训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验对应的表号、图号及详细定量结果，仅通过摘要说明核心结论性发现：经验抽象可提升LLMs在数学与逻辑推理基准任务的性能，自我提取的抽象效果匹配教师提取的效果，且框架具备跨数据集与模型的通用性；论文未报告效率对比、跨域/zero-shot迁移、鲁棒性测试及消融实验的详细数据与结果。

4. 关键结论和发现
- 主要发现：1. LLM可类似人类从自身解题轨迹中提取经验抽象，进而提升问题解决效率；2. LLM自身提取的经验抽象质量与更强教师模型提取的效果相当；3. 提出的经验抽象应用框架具备跨场景通用性。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的经验抽象应用框架实现了LLM对人类式经验蒸馏与复用逻辑的模拟，有效提升其数学与逻辑推理性能，且方法具备良好的跨数据集与模型通用性。

</details>

---

### 13. [SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data](https://arxiv.org/abs/2607.20402v1)

**Authors**: Wael AbdAlmageed  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.20402v1  

#### Abstract
In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evidence are supplied by a Knowledge Graph (KG), or rule definitions. Classical neuro-symbolic pipeline...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data
1. 论文的主要贡献和创新点
✅ 解决的问题
推理问题中前提多为高维输入需推断得到，而非直接的离散符号；经典神经符号管道存在感知与推理间的离散接口，导致梯度断层，无法实现端到端可微分推理。

🚀 提出的新方法与思路
**局部软解释张量表示**：将推理状态表示为候选常量与谓词上的局部软解释张量，消除感知与推理间的梯度断层；
**可微分即时结论算子提升**：利用谓词定义嵌入与潜在组合通道，生成软体谓词混合，聚合所有可能的见证，生成查询条件的头事实，通过单调概率OR更新推理解释；
**统一可微分推理框架**：感知模块输出概率基事实，KG三元组作为高置信度软证据，整个推理过程（查询锚点、谓词选择、闭包更新）保持可微分。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 梯度连续性 | 解决了感知与推理模块间的梯度断层，全程保持可微分 |
| 知识融合 | 支持KG高置信度软证据的注入，集成外部知识库信息 |
| 推理适配性 | 可直接适配高维感知数据的推理场景，实现感知事实与推理规则的结合 |
| 架构统一性 | 支持端到端的感知接地、KG证据注入与可微分推理闭包，为KVQA任务提供统一训练架构 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务为Knowledge-aware Visual Question Answering（KVQA），论文未报告具体评估指标

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
论文未报告

4. 关键结论和发现
- 主要发现：1. SoftReason架构实现了高维感知数据、KG证据与可微分推理的统一集成；2. 成功解决了传统神经符号方法中感知与推理间的梯度断层问题；3. 可端到端训练，适用于KVQA任务。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：SoftReason是一种全可微分的神经软符号演绎推理架构，解决了高维感知推理中感知与推理的梯度断层问题，构建了统一的端到端框架，支持感知接地、KG证据注入与可微分推理闭包，可应用于KVQA任务。

</details>

---

### 14. [Classical Hardware Acceleration of Quantum Autoencoders for Real-Time Anomaly Detection in Collider Experiments](https://arxiv.org/abs/2607.20302v1)

**Authors**: Ivan Ge, Sagar Addepalli, Abhilasha Dave, Julia Gonski  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2607.20302v1  

#### Abstract
Quantum machine learning (QML) algorithms in high energy physics (HEP) can efficiently represent and leverage long-range, high-order correlations in high-dimensional collider data, potentially with fewer parameters and favorable scaling relative to classical models. Deployment of QML in real-time co...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

《Classical Hardware Acceleration of Quantum Autoencoders for Real-Time Anomaly Detection in Collider Experiments》
1. 论文的主要贡献和创新点
✅ 解决的问题
论文未报告不同方法的各自缺陷；仅提及量子机器学习（QML）在高能物理（HEP）领域可高效建模高维对撞机数据的长程、高阶关联，参数少且缩放特性优，但QML部署到实时对撞机应用（如触发系统）需完成量子电路的经典仿真、编译并合成到低延迟硬件加速器（FPGA），该场景下相关FPGA实现研究较少。

🚀 提出的新方法与思路
**变分量子自编码器（variational quantum autoencoder）**：针对未来对撞机实时异常检测触发场景，采用变分量子自编码器模型，将其量子电路经经典仿真、编译后合成到FPGA硬件加速器，以满足实时触发的资源与时序约束要求。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模型性能 | 与最先进的经典方法性能相当 |
| 硬件适配性 | FPGA合成后满足未来对撞机触发应用的资源和时序约束 |
| 场景适用性 | 可在现有经典数据采集管道中部署更高能力的模型，推进对撞机基础设施的量子就绪 |
（注：论文未报告其他维度的优势）

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：对撞机实验的实时异常检测触发；论文未报告具体评估指标
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验内容：论文未报告

4. 关键结论和发现
- 主要发现：
1. 面向对撞机实时异常检测的变分量子自编码器模型性能可与最先进的经典方法相当；
2. 该模型经FPGA合成后满足未来对撞机触发应用的资源与时序约束；
3. 本研究是高能物理触发器领域量子机器学习模型FPGA实现的早期工作之一，可在现有经典数据采集管道中部署高性能模型，推进对撞机基础设施的量子就绪。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文针对未来对撞机实时异常检测触发场景，研究并实现了变分量子自编码器的经典FPGA加速方案，其性能与最先进经典方法相当，满足触发系统的资源和时序约束，是高能物理触发器量子机器学习模型FPGA实现的早期工作，推进了对撞机基础设施的量子就绪。

</details>

---

### 15. [Rewarding Better Thinking for LLM Preference Alignment](https://arxiv.org/abs/2607.19824v1)

**Authors**: Xubo Liu, Wenya Guo, Ruxue Yan, Xinying Qian, Ying Zhang  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.19824v1  

#### Abstract
LLM preference alignment aims to optimize models toward human preferences across diverse user instructions. Reinforcement learning has become a major post-training approach for this goal, but existing proxy rewards are often outcome-level, mainly evaluating the final response while providing limited...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Rewarding Better Thinking for LLM Preference Alignment
1. 论文的主要贡献和创新点
✅ 解决的问题
现有用于LLM偏好对齐的RL方法依赖outcome-level代理奖励，仅评估最终响应，对推理轨迹的指导有限；当多个响应最终得分相似时信用分配粗糙，导致轨迹级偏好未被充分明确。

🚀 提出的新方法与思路
**Thinking Checklist Reward（TCR）**：过程导向的RL奖励机制，将偏好对转换为样本特定的思维检查表，评估生成的推理轨迹是否覆盖偏好隐含的考量；引入指数移动平均（EMA）残差公式，隔离与结果级监督无重叠的“思维 surplus”，避免与结果级奖励的重叠。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 奖励导向 | 采用过程导向的推理轨迹评估，弥补outcome-level奖励无法指导推理过程的缺陷 |
| 信用分配 | 细粒度信用分配，缓解相似最终得分响应间的信用分配模糊问题 |
| 偏好覆盖 | 明确覆盖轨迹级偏好需求，解决轨迹级偏好未被充分明确的问题 |
| 互补性 | 引入与结果级监督无重叠的思维 surplus奖励，补充结果级奖励的不足 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告

🎯 实验设置与评估指标
任务：基于RL的LLM偏好对齐任务，通过TCR提升模型对人类偏好的对齐性能
| 指标 | 含义 |
| --- | --- |
| 对齐性能 | 偏好对齐效果，提升为优 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有outcome-level代理奖励方法 | RL-based偏好对齐基线 | 仅评估模型最终响应，对推理轨迹指导有限，信用分配粗糙 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

4. 关键结论和发现
- 主要发现：1. 提出的TCR方法可有效提升LLM的偏好对齐性能；2. EMA残差公式和样本特定思维检查表监督是TCR的核心有效组件；3. TCR在多个模型家族的不同基准中均表现稳定的对齐提升效果。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出过程导向的Thinking Checklist Reward，通过样本特有的思维检查表评估推理轨迹并辅以EMA残差机制，改进LLM偏好对齐中推理轨迹指导与信用分配的问题，提升模型的人类偏好对齐性能。

</details>

---

### 16. [Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models](https://arxiv.org/abs/2607.19932v1)

**Authors**: Pengchao Feng, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Xie Chen  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2607.19932v1  

#### Abstract
Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks. One important reason is that SLMs reason over purely verbalized mathematical ex...

---

### 17. [GraphContainer: A Unified Platform for Comparing and Debugging Graph RAG Methods](https://arxiv.org/abs/2607.19362v1)

**Authors**: Seonho An, Chaejeong Hyun, Min-Soo Kim  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2607.19362v1  

#### Abstract
Graph RAG mitigates hallucinations and stale knowledge in LLMs, particularly for multi-hop question answering. However, existing approaches remain highly fragmented and incompatible. The structural heterogeneity of graph formats across different frameworks and the lack of granular visualization tool...

---

### 18. [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](https://arxiv.org/abs/2607.19359v1)

**Authors**: Shengtong Zhu  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2607.19359v1  

#### Abstract
Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. We make three contributions. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions a...

---

### 19. [Rethinking Uncertainty Evaluation in Large Language Models](https://arxiv.org/abs/2607.19367v1)

**Authors**: Krish Matta, Atharv Naphade, Andy Zou  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.19367v1  

#### Abstract
Calibration is the primary criterion for evaluating LLM confidence, but it is insufficient: it admits trivially incoherent estimators, depends on the evaluation distribution, and does not test the extent to which the estimation can be interpreted as a consistent, underlying probability function. Wha...

---

### 20. [OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills](https://arxiv.org/abs/2607.20121v1)

**Authors**: Qiyuan Liu, Tingfeng Hui, Kun Zhan, Kaike Zhang, Ning Miao  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.20121v1  

#### Abstract
LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios. However, third-party skills can introduce extra security vulnerabilities, as seemingly harmless skills can contain latent safety risks that only emerge during actual execution. In this work, we conduct...

---

### 21. [Asymptotically Optimal Regret for Reinforcement Learning without Horizon Dependence](https://arxiv.org/abs/2607.19854v1)

**Authors**: Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2607.19854v1  

#### Abstract
We study horizon-free regret minimization for finite-horizon time-homogeneous tabular Markov decision processes with $S$ states, $A$ actions, horizon $H$, and per-trajectory total reward bounded by $1$.
  We propose a new algorithm and prove a regret upper bound \[\tilde O(\sqrt{SAK}+S^8A^3)\] with ...

---

### 22. [PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference](https://arxiv.org/abs/2607.20327v1)

**Authors**: Niqi Lyu, Pengtao Shi, Wei Qiu, Jianlin Zhong, Sicong Xia, Jianyao Ma, Yicheng Ding  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 17.0  
**Type**: new  
**ArXiv ID**: 2607.20327v1  

#### Abstract
Large language models (LLMs) provide strong reasoning capabilities but are expensive to serve at scale, whereas small language models (SLMs) are cheaper but less reliable on difficult problems. We introduce PyroDash, a cost-aware framework for token-level SLM-LLM collaborative inference. During gene...

---

### 23. [Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing](https://arxiv.org/abs/2607.19368v1)

**Authors**: Ali Mahdavi, Azaseh Zamanifar, Amirfarhad Farhadi, Omid Kashefi  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 15.0  
**Type**: new  
**ArXiv ID**: 2607.19368v1  

#### Abstract
Long-prompt inference remains expensive because prefill attention scales quadratically with sequence length. We propose Spectral-LSH, a training-free prompt compression method that operates before the prompt enters the language model. Spectral-LSH approximates the dominant components of an implicit ...

---

### 24. [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/abs/2607.19719v1)

**Authors**: Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan, Xin Xu  
**Category**: cs.LG  
**Published**: 2026-07-23  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2607.19719v1  

#### Abstract
Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world m...

---

### 25. [The Giant Hippocampus: From Structural Monoculture to a System of Systems](https://arxiv.org/abs/2607.19973v1)

**Authors**: Jaeho Seol  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2607.19973v1  

#### Abstract
AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech. Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integr...

---

### 26. [OpenEvoShield: Dual Non-Stationary Continual Defense for Open-World Multi-Agent System Attacks](https://arxiv.org/abs/2607.19351v1)

**Authors**: Litian Zhang, Chaozhuo Li, Yuting Zhang, Zejian Chen, Bingyu Yan, Qiwei Ye  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.19351v1  

#### Abstract
LLM-based multi-agent systems (LLM-MAS) are increasingly deployed in safety-critical applications, where adversaries inject malicious instructions through inter-agent communication to propagate harmful behaviors. Unlike static threats, these attacks are doubly dynamic: adversaries refine injection s...

---

### 27. [Logic-Guided Data Extraction with Answer Set Programming and Large Language Models](https://arxiv.org/abs/2607.19365v1)

**Authors**: Mario Alviano, Lorenzo Grillo, Nicola Leone, Fabrizio Lo Scudo  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.19365v1  

#### Abstract
When Large Language Models (LLMs) are used for semantic data extraction from unstructured text, producing candidate relational facts from natural language, they may remain unreliable for tasks requiring complex combinatorial reasoning and global consistency. This paper proposes a logic-guided data e...

---

### 28. [ITPEval: Benchmarking Formal Translation Across Interactive Theorem Provers](https://arxiv.org/abs/2607.19407v1)

**Authors**: Jiayi Wu, Robert Joseph George, Anima Anandkumar  
**Category**: cs.AI  
**Published**: 2026-07-23  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.19407v1  

#### Abstract
Formal theorem proving has emerged as a frontier challenge for machine learning, yet the ecosystem is fragmented: proofs remain siloed across incompatible systems, limiting both training data for learning-based provers and the portability of verified results. We present ITPEval, the first benchmark ...

---

### 29. [VizRAG: Enhancing Retrieval-Augmented Generation with Hypergraph Visualization](https://arxiv.org/abs/2607.19830v1)

**Authors**: Yanbin Wei, Yang Chen, Renling Gan, Ziru Liu, Xinyu Fu, Chun Kang, Ning Lu, Rui Liu, Yu Zhang, James Kwok  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.19830v1  

#### Abstract
Hypergraph-based RAG systems surpass traditional graph-based approaches by organizing complex n-ary atomic facts among entities, rather than relying solely on binary relationships. Despite the advancements in multimodal large language models (MLLMs) with enhanced visual capabilities, current hypergr...

---

### 30. [Solar Open 2 Technical Report](https://arxiv.org/abs/2607.20062v1)

**Authors**: Sungrae Park (University of Seoul), Sanghoon Kim (University of Seoul), Gyoungjin Gim (University of Seoul), Jungho Cho (University of Seoul), Hyunwoong Ko (University of Seoul), Minbyul Jeong (University of Seoul), Minjeong Kim (University of Seoul), Keunwoo Choi (University of Seoul), Chaehun Shin (University of Seoul), Chanwoong Yoon (University of Seoul), Dongjun Kim (University of Seoul), Eunwon Kim (University of Seoul), Gyungin Shin (University of Seoul), Hyeonju Lee (University of Seoul), Hyungkyu Kang (University of Seoul), Inseo Song (University of Seoul), Jisu Bae (University of Seoul), Jiyoon Han (University of Seoul), Jiyun Lee (University of Seoul), Joonkee Kim (University of Seoul), Junyeop Lee (University of Seoul), Mikyoung Cha (University of Seoul), Sangwon Yu (University of Seoul), Sehwan Joo (University of Seoul), Seokyoon Kang (University of Seoul), Seonghoon Yang (University of Seoul), Seung Shin (University of Seoul), Seunghyun Lee (University of Seoul), Seungseop Lim (University of Seoul), Seungyoun Shin (University of Seoul), Sukyung Lee (University of Seoul), Taegyeong Eo (University of Seoul), Taehwan Oh (University of Seoul), Taewhoo Lee (University of Seoul), Wonho Song (University of Seoul), Wonjun Oh (University of Seoul), Wonseok Hwang (University of Seoul), Yunsu Kim, Yura Shim, Hwalsuk Lee, Sunghun Kim, Du-Seong Chang, Kyunghyun Cho, Seungju Han, Yejin Choi, Junsuk Choe, Hwaran Lee, Minjeong Ban, Yun Taewon, Hwanjun Song, Jae-Gil Lee, KyungTae Lim, Alice Oh  
**Category**: cs.CL  
**Published**: 2026-07-23  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2607.20062v1  

#### Abstract
We present Solar Open 2, a 250B-A15B Mixture-of-Experts language model built for long-horizon agentic tasks, scaled up from Solar Open 1 (Solar Open 100B). To hold entire agent trajectories in a single context, Solar Open 2 reaches a 1M-token window through a hybrid attention stack that interleaves ...

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
