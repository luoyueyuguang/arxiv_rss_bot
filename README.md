# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-04 09:58:07 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430v1)

**Authors**: Heng Wang, Jielin Qiu, Wenting Zhao, Cheng Qian, Liangwei Yang, Jiawei Han, Heng Ji, Silvio Savarese, Shelby Heinecke, Huan Wang  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 96.0  
**Type**: new  
**ArXiv ID**: 2609.03430v1  

#### Abstract
Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck. Existing KV cache compression methods share one paradigm: score each cached token by some estimate of how much it will matter later, a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 现存KV缓存压缩方法均采用“对缓存token打分并保留得分最高项”的范式，该范式中的选择信号对性能提升贡献极少；
2. 长推理链时KV缓存成为严重内存瓶颈，多数方法未关注KV缓存中prompt的脆弱性，也未利用推理追踪的冗余特性，导致效率与性能的权衡未达最优。
🚀 提出的新方法与思路
**Random Attention**：核心思路为在KV缓存驱逐操作中保留prompt，在每个注意力头（attention head）内采用均匀随机驱逐（uniform random eviction）的策略，全程不计算用于token选择的评分，从而简化驱逐流程并降低计算开销。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| vLLM部署吞吐量 | 比最强现有KV缓存驱逐器高32-43% |
| 性能 | 与最强现有KV缓存驱逐器匹配 |
| 计算开销 | 无需额外计算token选择的评分，减少了驱逐阶段的计算量 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告
🎯 实验设置与评估指标
论文未报告
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 现有KV缓存压缩方法 | KV缓存驱逐方法 | 采用“对缓存token打分，保留得分最高的token”的范式 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
💡 结论：论文未报告

4. 关键结论和发现
- 2-3条主要发现
  1. prompt是KV缓存中最脆弱的部分，不同KV缓存驱逐方法的性能差距主要取决于是否保留prompt；
  2. 推理追踪存在双层面冗余：文本层面模型在推理过程中会重复输出所需内容，注意力头层面每个头独立保留推理追踪的副本；
  3. 只要prompt安全，随机驱逐策略可保留足够的模型所需信息，无需精准选择token的评分信号。
- 方法局限性
论文未报告
- 未来工作
论文未报告

✅ **总结一句话**：提出Random Attention方法，通过保留prompt并在各注意力头内均匀随机驱逐KV缓存token（无需计算token选择评分），在性能匹配最强现有KV缓存驱逐器的前提下，大幅提升vLLM部署的吞吐量，缓解了大模型长链推理时的KV缓存内存瓶颈问题。

</details>

---

### 2. [Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards](https://arxiv.org/abs/2609.03342v1)

**Authors**: Leqi Zheng, Jinbo Su, Fang Niu, Chaokun Wang, Weiping Wang, Jiajun Zhang, Shannan Yan, Jie Wu, Zhaolu Kang, Rong Fu, Hang Zhang  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 82.5  
**Type**: new  
**ArXiv ID**: 2609.03342v1  

#### Abstract
Reinforcement learning from verifiable rewards (RLVR) drives chain-of-thought reasoning in large language models, yet its binary outcome reward cannot distinguish among correct trajectories. Existing dense reward alternatives, from surface heuristics to process reward models, either ignore the exper...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards

1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：现有基于可验证奖励的强化学习（RLVR）采用二元结果奖励，无法区分正确推理轨迹间的差异；现有密集奖励替代方法存在两类缺陷：要么忽略训练语料中已有的专家解，要么需要昂贵的离线标注成本。

🚀 提出的新方法与思路
**Gradient-Aligned Reward (GAR)**：在策略自身的梯度空间中操作，通过截断反向传播经过输出投影层，提取每个rollout的紧凑梯度向量，计算该向量与专家锚梯度的余弦相似度，得到密集的、感知推理的奖励；该方法仅产生不到9%的wall-clock开销，且理论上证明该余弦相似度可分解为预测误差与激活模式因子的乘积，明确了对齐信号的度量特性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 奖励区分性 | 可区分正确轨迹间的差异，弥补二元结果奖励的不足 |
| 标注依赖度 | 无需昂贵的离线标注，可利用训练语料中的专家解信息 |
| 时间开销 | 仅产生不到9%的wall-clock开销，效率较高 |
| 跨域迁移能力 | 无需领域特定数据，可迁移至GPQA Diamond、MMLU-Pro等跨领域基准 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 比赛级数学基准 | 测试模型在核心推理任务上的性能 |
| GPQA Diamond | 测试模型跨领域迁移能力 |
| MMLU-Pro | 测试模型跨领域迁移能力 |

🎯 实验设置与评估指标
任务为LLM推理任务（数学推理等）；评估指标未明确报告具体名称，仅说明性能相对表现与效率占比。
| 指标 | 含义 |
| --- | --- |
| 核心基准性能 | 越高越好（未明确具体指标） |
| 跨域基准性能 | 越高越好（未明确具体指标） |
| wall-clock开销 | 越低越好（数值为占基线方法的比例） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| GRPO | 强化学习方法 | 对比的基准RL方法 |
| 其他基线 | 强化学习方法 | 对比的现有密集奖励方法 |

3. 主要实验结果和性能指标
论文未明确报告具体表号、图号，仅从摘要提取结果：
1. 主benchmark性能：GAR在Qwen3-4B和Qwen3-8B模型的比赛级数学基准上，性能一致优于GRPO及其他基线方法。
2. 效率对比：GAR的wall-clock开销不到9%。
3. 跨域/zero-shot迁移：GAR无需领域特定数据，可成功迁移至GPQA Diamond和MMLU-Pro基准。
4. 鲁棒性/扰动测试：论文未报告。
5. 消融实验：论文未报告。

4. 关键结论和发现
- 主要发现：① Gradient-Aligned Reward（GAR）生成的密集奖励能有效区分正确推理轨迹间的差异，在核心数学推理基准上优于现有方法；② GAR无需领域特定数据，具备良好的跨域迁移能力；③ GAR时间开销极低，效率优势明显。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：论文提出Gradient-Aligned Reward（GAR）方法，基于策略梯度空间的专家锚梯度余弦相似度生成推理感知的密集奖励，在LLM推理任务上性能优于现有基线，具备跨域迁移能力且时间开销低。

</details>

---

### 3. [Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105v1)

**Authors**: Robert Hu  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 70.5  
**Type**: new  
**ArXiv ID**: 2609.04105v1  

#### Abstract
Blackwell's 4-bit floating-point (FP4) tensor cores do not automatically make attention faster because softmax conversion and on-chip dependencies dominate once its matrix products shrink. We address this with \emph{Direct-P} for noncausal inference and a causal path that passes the forward quantiza...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Hardware-Aware FP4 FlashAttention-4
1. 论文的主要贡献和创新点
✅ 解决的问题
Blackwell架构的4-bit浮点（FP4）张量核无法自动加速注意力计算，当矩阵乘积缩小时，softmax转换和片上依赖会主导计算过程，限制性能提升。

🚀 提出的新方法与思路
**Direct-P**：针对非因果推理场景，将注意力分数直接映射到FP4概率，实现高效的前向注意力计算，适配NVIDIA GB200硬件平台。
**因果路径**：针对因果推理场景，从保存的量化查询和键中重构概率，使用8-bit浮点（FP8）梯度操作数；在分布式训练阶段保留FP8概率和值，规避MXFP4带来的训练轨迹发散问题。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 非因果推理前向性能 | 有效突破FP4张量核在小矩阵乘积下的性能瓶颈 |
| 单GPU参数更新效率 | 提升完整单GPU模型参数更新的速度 |
| 分布式训练稳定性 | 保留FP8概率和值，避免训练轨迹发散 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：注意力计算的前向性能、单GPU参数更新效率、分布式训练稳定性的评估
| 指标 | 含义 |
|------|------|
| 前向吞吐量 | 越高越好 |
| 单GPU参数更新加速比 | 越高越好 |
| 训练轨迹发散性 | 无发散为优 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| BF16 | 基准方法 | 采用bfloat16精度 |
| MXFP4 | 对比方法 | 测试后训练轨迹均发散 |
| FP8 | 对比方法 | 分布式训练保留FP8概率和值 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：Blackwell架构的FP4张量核需解决小矩阵乘积下softmax转换与片上依赖主导计算的问题，才能有效加速注意力计算；Direct-P可优化非因果推理前向性能，因果路径可加快单GPU参数更新；分布式训练中保留FP8概率和值可避免MXFP4训练轨迹发散。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出针对非因果推理的Direct-P方法与因果路径，解决Blackwell架构FP4张量核加速注意力时的性能瓶颈，实现前向与单GPU参数更新的效率提升，分布式训练中保留FP8可规避MXFP4的训练发散问题。

</details>

---

### 4. [GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving](https://arxiv.org/abs/2609.03494v1)

**Authors**: Qiankun Ma, Yanjiang Zhou, Zinan Xiong, Haofei Wang, Zhen Song, Yang Xiang, Ziyao Zhang, Hairong Zheng  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 66.0  
**Type**: new  
**ArXiv ID**: 2609.03494v1  

#### Abstract
Long-output reasoning has made the key--value (KV) cache a critical memory bottleneck for efficient LLM serving. Existing KV compression methods usually rely on a predefined per-request budget and adjust only which KV states are retained, leaving the total capacity fixed throughout decoding. However...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
现有KV压缩方法依赖预定义的per-request预算，仅调整保留的KV状态，解码过程中总容量固定；但推理工作负载存在显著需求变化：不同请求所需KV容量不同，单个请求在生成过程中的注意力需求也会演变，导致现有方法无法适配动态需求。

🚀 提出的新方法与思路
**GrowPage**：作为按需KV预算框架，将KV容量视为运行时资源；维护轻量级双时间尺度查询摘要，捕捉近期和长期注意力行为，利用相对注意力工作集估计需求演变；在每个容量边界，要么压缩当前分配内的KV状态，要么在出现更广泛需求时获取额外物理页面；通过集成PagedAttention的页面级内存抽象，保留连续批量处理与前缀缓存。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV容量管理 | 将KV容量视为运行时资源，适配动态变化的推理需求 |
| 原有特性保留 | 集成PagedAttention的内存抽象，保留连续批量与前缀缓存能力 |
| 性能权衡 | 在吞吐量与效率的权衡上优于现有方法 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 推理基准测试 | 评估多模型下GrowPage及对比方法的LLM推理服务性能 |

🎯 实验设置与评估指标
任务：在多模型场景下评估LLM推理服务的性能权衡。论文未报告具体评估指标及含义。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体的表号、图号及定量数值，仅概括提及：在推理基准测试的多模型实验中，GrowPage在性能-吞吐量权衡上优于现有方法。

4. 关键结论和发现
- 主要发现：1）现有KV缓存方法的固定容量设计无法适配LLM推理中动态变化的注意力需求；2）GrowPage通过双时间尺度需求估计及按需KV调整机制，可适配动态需求，同时保留PagedAttention的连续批量与前缀缓存关键特性。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：GrowPage是一种将KV容量作为运行时资源的按需KV预算框架，适配LLM推理的动态注意力需求，保留连续批量与前缀缓存特性，在吞吐量-效率权衡上优于现有方法。

</details>

---

### 5. [Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards](https://arxiv.org/abs/2609.03181v1)

**Authors**: Alejandro Bar\'on Garc\'ia, Feng Wang, Emilia Garcia Casademont, Han Xiao  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 66.0  
**Type**: new  
**ArXiv ID**: 2609.03181v1  

#### Abstract
We present Jina-OCR-v1, an end-to-end document parsing model built to serve on low-budget GPUs. It combines the compressed-vision encoder and the 3B mixture-of-experts decoder of DeepSeek-OCR, which activates about 570M parameters per token, with a FastMTP speculative decoding head that shares a sin...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards
1. 论文的主要贡献和创新点
✅ 解决的问题
低预算GPU部署端到端文档解析模型时，传统方法难以同时兼顾识别性能（如准确率）与解码效率（如处理速度）的核心矛盾；部分模型因参数规模或解码机制限制，在低预算GPU上要么速度缓慢，要么提升速度时会损失识别性能。

🚀 提出的新方法与思路
**Jina-OCR-v1混合架构**：结合DeepSeek-OCR的压缩视觉编码器与3B混合专家（MoE）解码器，实现轻量化与参数激活效率的平衡，每个token仅激活约570M参数。
**FastMTP投机解码头**：递归共享单个草稿块，用于K=3个预测步骤的投机解码，提升解码速度。
**贪心验证机制**：采用贪心验证确保解码过程无性能损失，实现无损失解码。
**后训练策略**：融合指令对齐、难文档鲁棒微调，以及基于可验证密集奖励的GRPO训练；奖励来自公式、表格及结构的确定性检查，提供部分 credit，优化模型性能。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
部署适配性 | 专为低预算GPU（如NVIDIA L4）设计，可在算力有限的硬件上运行
参数效率 | 单token激活仅约570M参数，远低于全激活3B MoE解码器的参数规模
解码速度 | 在NVIDIA L4上，FastMTP投机解码比贪心自回归解码提速1倍
处理吞吐量 | 对比实验中达到最高页面吞吐量2.57页/秒
性能表现 | OmniDocBench v1.6得分91.14、olmOCR-Bench得分83.4，具备优异的文档解析性能
可获取性 | 公开发布于Hugging Face Hub，便于用户使用

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
清理后的公共语料库 | 用于模型训练
有针对性的合成页面 | 用于模型训练

🎯 实验设置与评估指标
任务：端到端文档解析，评估文档识别准确率与处理效率
指标 | 含义
--- | ---
OmniDocBench v1.6得分 | 文档解析性能指标，分数越高性能越好
olmOCR-Bench得分 | 文档解析性能指标，分数越高性能越好
页面吞吐量（页/秒） | 单位时间内处理的文档页面数，数值越高效率越好
解码加速比 | FastMTP投机解码对比贪心自回归解码的速度提升倍数，数值越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
贪心自回归解码 | 自回归解码方法 | 无投机解码机制，在低预算GPU上解码速度较慢

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（文档解析准确率）**
| 数据集 | 得分 |
| --- | --- |
| OmniDocBench v1.6 | 91.14 |
| olmOCR-Bench | 83.4 |
💡 结论：Jina-OCR-v1在主流文档解析基准上取得了较高的识别得分，具备优异的文档解析性能。

**效率对比（低预算GPU场景）**
| 对比项 | 表现 |
| --- | --- |
| FastMTP投机解码 vs 贪心自回归解码 | 在NVIDIA L4上，解码速度提速1倍 |
| Jina-OCR-v1页面吞吐量 | 达2.57页/秒，为对比实验中最高 |
💡 结论：FastMTP投机解码可有效提升低预算GPU上的解码速度，且Jina-OCR-v1具备最优的页面处理效率。

跨域 / zero-shot 迁移
论文未报告

鲁棒性 / 扰动测试
论文未报告

消融实验
论文未报告

4. 关键结论和发现
- 主要发现
1. Jina-OCR-v1通过混合架构、FastMTP投机解码及贪心验证等设计，在低预算GPU上实现了高性能与高效率的平衡。
2. FastMTP投机解码模块可在不损失性能的前提下，显著提升低预算GPU上的解码速度。
3. 基于确定性规则的密集奖励与GRPO结合的后训练策略，有效支撑了模型的性能优化。
- 方法局限性
论文未报告
- 未来工作
论文未报告

> ✅ **总结一句话**：Jina-OCR-v1是一款专为低预算GPU优化的端到端文档解析模型，整合了投机解码、可验证密集奖励等技术，在主流文档解析基准上取得优异性能，同时具备高效的解码速度，且已公开发布便于使用。

</details>

---

### 6. [Margins, Not Windows: Training-Free Per-Step Lossy Speculative Decoding](https://arxiv.org/abs/2609.02897v1)

**Authors**: Oszk\'ar Urb\'an, Young D. Kwon, Stylianos I. Venieris, Cecilia Mascolo  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 59.0  
**Type**: new  
**ArXiv ID**: 2609.02897v1  

#### Abstract
Speculative decoding accelerates LLM inference by drafting candidate tokens and verifying them in parallel. Tree-attention drafters such as EAGLE-3 are widely adopted, yet typically hold two decisions fixed: (1) a strict token-match verification rule and (2) a static draft-tree shape. Prior work rel...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Margins, Not Windows: Training-Free Per-Step Lossy Speculative Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有树注意力起草器（如EAGLE-3）推测解码方法，通常固定严格token匹配验证规则和静态草稿树形状；此前相关工作分别放松这两个决策时，均存在限制假设：训练时的无损失验证需要长草稿链，而自适应树调整仅能在固定token预算下进行。

🚀 提出的新方法与思路
**AdaptiveSpec**：一种训练-free的逐步推测解码方法，分别对上述两个固定决策进行自适应调整：
1. **逐步margin规则**：提出当目标token在草稿token上的概率与其top-1概率的比值超过阈值时，允许不匹配的草稿提议token，不依赖草稿长度或底层起草器架构；
2. **逐步树策略**：基于草稿top-1置信度与捕捉近期草稿-目标一致性的滚动接受历史的融合信号，直接调整草稿树的深度、宽度和节点数，允许总草稿数变化而非仅重新分配，两个调整方向正交，效果可复合。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 吞吐量 | 在SGLang引擎上，比SOTA自回归推测解码方法EAGLE-3实现最高56%的提升 |
| 任务准确率 | 在GSM8K、MATH-500、HumanEval三个任务及三个目标模型上，恢复93%至完全无损的任务准确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| GSM8K | 评估任务准确率 |
| MATH-500 | 评估任务准确率 |
| HumanEval | 评估任务准确率 |

🎯 实验设置与评估指标
任务为大型语言模型推测解码的吞吐量与任务准确率评估，论文未提供详细实验设置表格及具体指标表格。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| EAGLE-3 | 自回归推测解码方法（树注意力起草器） | 固定严格token匹配验证规则和静态草稿树形状，为该工作的对比基线 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表：论文未报告具体表号，仅摘要提及以下结果**
| 指标 | 结果 |
| --- | --- |
| 吞吐量提升 | 比EAGLE-3最高提升56% |
| 任务准确率恢复 | 在GSM8K、MATH-500、HumanEval及三个目标模型上，恢复93%至完全无损 ✅（最优区间） |
💡 结论：AdaptiveSpec方法可同时提升推测解码的吞吐量，且保留接近完全无损的任务准确率。

4. 关键结论和发现
- 主要发现：1）对推测解码的两个固定决策（token匹配规则、草稿树形状）进行逐步自适应调整，可在训练-free条件下实现吞吐量提升与高任务准确率的平衡；2）两个调整方向正交，效果可复合；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；
> ✅ **总结一句话**：AdaptiveSpec是一种训练-free的逐步推测解码方法，通过逐步调整token匹配规则与草稿树策略，在SGLang引擎上比EAGLE-3实现最高56%的吞吐量提升，同时恢复93%至完全无损的任务准确率。

</details>

---

### 7. [PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing](https://arxiv.org/abs/2609.03503v1)

**Authors**: Yangshuo Qi, Chenwei Wang, Zihan Shen, Songlin Sun  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2609.03503v1  

#### Abstract
With the rapid development of the Internet of Things, computation intensive directed acyclic graph (DAG) tasks have become increasingly common in cloud-edge-end collaborative environments. However, cloud, edge, and end nodes are highly heterogeneous in computing capacity, network bandwidth, and ener...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing
1. 论文的主要贡献和创新点
✅ 解决的问题
- 物联网场景下，计算密集型DAG任务在云边端异构节点（计算能力、网络带宽、能耗存在差异）上的调度为NP难问题；
- 传统启发式算法、常规强化学习方法无法捕捉系统资源的时空动态，调度效果不足。

🚀 提出的新方法与思路
**PPO-STGNN**：将近端策略优化（PPO）与时空图神经网络（STGNN）融合，通过STGNN分别提取DAG任务的拓扑特征与物理云边端资源图的时空特征；采用PPO优化调度策略，以最小化完成时间（makespan）、调度长度比（SLR）为目标，同时提升CPU和内存的负载均衡；为加快算法收敛，引入多教师行为克隆机制完成预训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 异构适配 | 支持云边端节点异构特性的适配优化 |
| 特征捕捉 | 可提取DAG任务拓扑与资源图的时空动态特征 |
| 收敛效率 | 多教师行为克隆机制加速算法收敛 |
| 多目标优化 | 可同时优化makespan、SLR，提升CPU、内存负载均衡 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务为云边端环境下的DAG任务调度。
| 指标 | 含义（箭头方向） |
| --- | --- |
| makespan | 完成时间，越低越好（↓） |
| SLR（调度长度比） | 任务调度长度比，越低越好（↓） |
| CPU负载均衡 | 用于衡量CPU资源分配的均衡性，越高越好（↑） |
| 内存负载均衡 | 用于衡量内存资源分配的均衡性，越高越好（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告
**效率对比（FPS/参数量）**：论文未报告
**跨域/zero-shot迁移**：论文未报告
**鲁棒性/扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现：1. PPO-STGNN算法可在云边端DAG任务调度场景中，显著提升CPU和内存的负载均衡，同时维持较低的完成时间；2. 该方法适配动态且异构的云边端DAG调度场景。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：PPO-STGNN将PPO与STGNN结合，通过多教师行为克隆机制预训练，能在云边端异构环境中高效调度DAG任务，兼顾低完成时间、低调度长度比与良好的CPU、内存负载均衡，适用于动态调度场景。

</details>

---

### 8. [CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning](https://arxiv.org/abs/2609.03526v1)

**Authors**: Bo Zeng, Linfeng Gao, Peiqin Lin, Yu Zhao, Mingyan Zeng, Yu Tong, Xintong Wang, Linlong Xu, Longyue Wang, Weihua Luo, Qinggang Zhang, Jinsong Su  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2609.03526v1  

#### Abstract
Multimodal language models achieve near-ceiling scores on food recognition benchmarks, yet it remains unclear whether this success reflects genuine cultural understanding or mere visual matching. To probe this distinction, we introduce CulturalMenuBench, a benchmark of 4,870 items in 10 languages ac...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：多模态语言模型在食物识别基准上接近满分，但无法区分该成功源于真正的文化理解还是仅视觉匹配，存在"知识已具备但无法激活应用"的鸿沟。
🚀 提出的新方法与思路
**CulturalMenuBench**：构建包含4870项、10种语言、18个区域的基准，设置10项任务，配对最终菜肴和分步烹饪图像与食材、过程文本、区域标签，覆盖从基础识别到基于过程的文化归因任务，用于探测前述知识应用鸿沟。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务设计 | 首次针对多模态烹饪推理明确区分视觉匹配与文化知识应用 |
| 覆盖范围 | 含10种语言、18个区域，任务涵盖基础识别至文化归因 |
| 评估能力 | 可有效探测模型的知识应用鸿沟 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| CulturalMenuBench | 评估多模态烹饪推理中的知识应用差距 |
🎯 实验设置与评估指标
实验任务为评估多模态模型的烹饪推理知识应用能力；评估指标为准确率（Accuracy），含义为正确分类/归因的比例，↑越高越好。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文评估的12个模型 | 多模态语言模型 | 在标准食物识别任务上接近满分，在文化归因任务上表现差 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**（来源未明确表/图号）主基准性能**
| 任务类型 | 准确率 |
| ---- | ---- |
| 标准多选择任务 | 超过94% |
| 中国区域菜系归因任务 | 最高为56% |
💡 结论：多模态模型在标准食物识别任务表现优异，但在文化归因任务性能大幅下降，存在知识应用鸿沟。
**（来源未明确表/图号）跨模态分类对比**
| 分类依据 | 准确率差异 |
| ---- | ---- |
| 菜名vs图像分类菜系 | 菜名分类准确率高7-18个百分点 |
💡 结论：模型分类菜系更依赖菜名而非图像，视觉匹配是其优异表现的主要原因。
**（来源未明确表/图号）消融实验**
| 顺序烹饪图像模块 | 过程-grounded任务性能 |
| ---- | ---- |
| 启用 | 性能稳定 |
| 禁用 | 选择性下降 |
💡 结论：基于过程的文化归因任务依赖顺序烹饪图像的输入。
效率对比（FPS / 参数量）：论文未报告
跨域 / zero-shot迁移：论文未报告
鲁棒性 / 扰动测试：论文未报告

4. 关键结论和发现
- 主要发现：1）多模态语言模型存在知识应用鸿沟，标准食物识别任务的优异表现源于视觉匹配而非文化理解；2）模型分类菜系的准确率更多依赖菜名而非图像，与视觉独特性而非文化结构关联；3）基于过程的文化归因任务需要顺序烹饪图像的支持。
- 方法局限性：论文未报告
- 未来工作：需开展将感知、过程与文化语境明确关联的训练
> ✅ **总结一句话**：论文构建的CulturalMenuBench基准揭示，多模态食物识别模型接近满分的表现并非源于真正的文化理解，而是存在知识应用鸿沟，本质是视觉匹配的结果。

</details>

---

### 9. [Spurious Advantage Hidden in GRPO](https://arxiv.org/abs/2609.04063v1)

**Authors**: Jiamian Wang, Samyadeep Basu, Koustava Goswami, Tong Yu, Zhiqiang Tao  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.04063v1  

#### Abstract
Group Relative Policy Optimization (GRPO) is widely studied for reinforcement learning with verifiable rewards, where its advantage estimator assigns each rollout a magnitude from within-group reward statistics. In the common case, this magnitude rewards rollouts that reach the correct answer throug...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Spurious Advantage Hidden in GRPO
1. 论文的主要贡献和创新点
✅ 解决的问题
GRPO应用于具有可验证奖励的强化学习时，其优势估计器基于组内奖励统计为每个rollout分配幅度值；但在三类场景（候选集小的有界答案任务、含有限子情况的开放答案集、搜索智能体通过多路径到同一答案）中，会对通过猜测（而非推理）获得正确结果的rollout分配高幅度的“虚假优势”，误导策略偏向猜测类行为。

🚀 提出的新方法与思路
**SIGNBALANCE**：一种composition-free的优势估计方法，核心操作包括：保留验证器符号、使用全局尺度、通过逐类停止梯度重新缩放恢复零均值平衡。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 有界答案数学任务 | 性能优于GRPO |
| 开放答案数学任务 | 性能与GRPO匹配 |
| 搜索智能体任务 | 性能优于GRPO |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 数学基准 | 用于开展有界答案数学任务、开放答案数学任务实验 |
| 搜索智能体基准 | 用于开展搜索智能体任务实验 |
（注：论文未报告上述基准的具体名称，仅提及类别）

🎯 实验设置与评估指标
任务为可验证奖励下的数学问题求解与搜索智能体优化；论文未报告具体评估指标及方向细节。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| GRPO | 强化学习算法（面向可验证奖励场景） | 基于组内奖励统计分配rollout的优势幅度值，存在虚假优势问题 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未报告具体表号、图号及对应定量数值，故：
- 主基准性能：论文未报告
- 效率对比：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：1. GRPO在可验证奖励的强化学习中存在虚假优势缺陷，易误导策略偏向猜测类行为，该缺陷出现在三类特定任务场景；2. 提出的SIGNBALANCE方法为无组合依赖的优势估计方法，能有效规避虚假优势问题；3. SIGNBALANCE在开放答案数学任务上与GRPO性能相当，在有界答案数学任务及搜索智能体任务上性能优于GRPO。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文指出GRPO在可验证奖励强化学习中存在易误导策略的虚假优势问题，提出了SIGNBALANCE方法并验证其在多数任务场景上的性能优势。

</details>

---

### 10. [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194v1)

**Authors**: Kevin Du, Alexander Hoyle, Laura Ruis, Acyr Locatelli  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.04194v1  

#### Abstract
Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative c...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大量研究将思维链（Chain-of-Thought, CoT）推理轨迹的易读性（legibility）误作为可解释性（interpretability），假设推理步骤的文本编码了其功能重要性，该假设被用于LLM诊断错误、评估忠实性、生成过程奖励模型（process reward models）的步骤级监督等场景，但尚未验证该假设的合理性。
🚀 提出的新方法与思路
首先将推理步骤的重要性操作化为其**优势（Advantage）**——通过蒙特卡洛rollout估计包含该步骤时最终答案正确的期望奖励变化，以此作为步骤重要性的真实基准；在此基础上，评估不同能力的LLM判断高优势步骤的能力，同时验证微调模型作为步骤级评判器（step-level critic）的性能。
🔍 相比现有方法的优势
维度 | 优势
--- | ---
步骤重要性基准构建 | 首次采用蒙特卡洛rollout量化的实际优势作为步骤重要性的真实ground truth，而非依赖主观判断 |
LLM评判能力评估逻辑 | 明确区分推理轨迹的易读性（文本）与实际可解释性（功能重要性），量化LLM判断步骤重要性的误差 |
过程奖励模型指导 | 验证了微调步骤级评判器对错误响应的步骤重要性判断有显著提升，但正确响应仍存在局限，为过程奖励模型的监督信号设计提供依据 |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为评估LLM识别思维链推理轨迹中高优势步骤的能力，评估指标论文未报告
⚔️ 基线方法对比：
方法 | 类型 | 特点
--- | --- | ---
Prevalence Baseline | 基准方法 | 流行度基线（未明确具体定义） |
不同能力的LLM | 对比方法 | 不同能力级别的LLM模型（未明确具体模型） |
微调的步骤级评判器 | 对比方法 | 微调后用于步骤重要性判断的模型（未明确微调细节） |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告任何带表号、图号的定量实验结果
💡 结论：论文未提供带具体来源的定量结论，仅明确定性结论如下：足够能力的LLM优于流行度基线但远低于噪音天花板；微调步骤级评判器在错误响应上有强提升但正确响应仍远低于天花板；步骤重要性仅可部分从推理轨迹文本恢复。

4. 关键结论和发现
- 2-3条主要发现
1. 已验证的LLM能比流行度基线更好地识别高优势步骤，但该能力仍远低于噪音天花板；
2. 微调模型作为步骤级评判器，在错误响应的步骤重要性判断上有显著提升，但针对正确响应的判断仍远低于噪音天花板；
3. 推理步骤的实际重要性仅能部分从推理轨迹的文本中恢复，现有将易读性等同于可解释性的做法缺乏依据。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：这篇论文通过将思维链推理步骤的重要性量化为蒙特卡洛rollout估计的优势作为基准，发现现有LLM难以准确识别高重要性步骤，警示不能将推理轨迹的易读性等同于可解释性，为过程奖励模型等依赖步骤级监督的研究提供关键指导。

</details>

---

### 11. [KhatianDoc: A Human-Verified Benchmark Diagnosing Multimodal LLM Failure on Bengali Legal Land Records](https://arxiv.org/abs/2609.03597v1)

**Authors**: Tasmiad Hasan, Arafat Zaman Ratul, Sarker Sadman Saalim, S. M. Shah Nawaz Hossain, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.03597v1  

#### Abstract
Land ownership in Bangladesh is recorded in Ana-Ganda-Kora-Kranti-Til, a base-16 positional fraction system with dedicated Unicode glyphs, no mainstream font, and no coverage in any OCR pipeline or tokenizer. The handwritten records that carry these fractions, RS Khatians, are the authoritative titl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

KhatianDoc: A Human-Verified Benchmark Diagnosing Multimodal LLM Failure on Bengali Legal Land Records
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：孟加拉国RS Khatian记录使用的Ana-Ganda-Kora-Kranti-Til十六进制分数系统缺乏主流字体、OCR和tokenizer覆盖，这类手写记录是土地产权权威记录且常涉民事诉讼，目前无基准测试机器能否读取这类记录。
现有方法缺陷：
1. 现有OCR和tokenizer未覆盖Ana-Ganda-Kora-Kranti-Til符号，无法处理RS Khatian记录；
2. 缺乏针对孟加拉RS Khatian记录的多模态LLM评估基准，无法诊断模型在该领域的能力缺失；
3. 未对RS Khatian记录的多任务处理（符号识别、十六进制转换、结构化提取、法律QA）进行系统性评估。

🚀 提出的新方法与思路
**KhatianDoc基准**：构建自孟加拉国Munshiganj土地办公室的107份真实RS Khatian记录，包含symbol recognition、base-16-to-decimal conversion、structured field extraction、legal document question answering四个任务，其中legal document question answering附带1634个QA对；ground truth经人工转录后，由土地法律从业者完成完全一致验证，采用位置token进行匿名化以保留多跳问题依赖的指代区分性；实验采用固定zero-shot协议，评估6个多模态LLM（参数范围8B至72B+，含开源与闭源模型）。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 任务覆盖 | 包含RS Khatian记录特有的Ana-Ganda-Kora-Kranti-Til符号识别任务，覆盖四类核心任务 |
| 数据真实性 | 来自真实土地办公室的RS Khatian记录，ground truth经人工转录+土地法律从业者完全验证 |
| 指代保留 | 采用位置token匿名化，保障多跳问题所需的指代区分性 |
| 基准可用性 | 代码和数据（含红acted图像发布）公开，便于模型评估与改进 |
| 问题诊断性 | 可诊断多模态LLM在该领域的能力缺失，而非仅评估性能差距 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| KhatianDoc | 构建四任务测试基准，含107份真实RS Khatian记录，配套1634个QA对，用于评估多模态LLM在指定任务的性能 |

🎯 实验设置与评估指标
任务：采用固定zero-shot协议，评估6个多模态LLM（8B至72B+，含开源与闭源模型）在KhatianDoc基准上的表现，涵盖符号识别、十六进制转换、结构化提取、法律QA任务。
| 指标 | 含义（箭头） |
| --- | --- |
| QA类别正确率 | 衡量模型在对应QA类别的正确答案比例，↓越低越好 |
| 算术精确匹配分数 | 衡量算术任务结果与ground truth的精确匹配程度，↓越低越好 |
| 算术近匹配分数 | 衡量算术任务结果与ground truth的近似匹配程度，↓越低越好 |
| 拒绝评分修正状态 | 修正了原有拒绝评分bug，同时报告修正后与原始分数 |
| Metadata指标 | 用于衡量元数据相关表现，标记为上界（存在inflation） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 6个多模态LLM（8B至72B+） | 多模态大语言模型 | 参数覆盖8B至72B+，包含开源与闭源模型，采用固定zero-shot设置评估 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能
| 指标 | 结果 |
| --- | --- |
| QA类别零正确占比 | 39.3%的分层QA类别集合中，所有模型均给出零正确答案 |
| 算术任务表现 | 所有生成数字结果的模型，性能均差于constant-mean基准，精确匹配与近匹配分数重合，呈现去相关特性 |
| 拒绝评分处理 | 已修正原有拒绝评分bug，同步报告修正后分数与原始分数 |
| Metadata指标状态 | 标记为上界，存在inflation问题 |
💡 结论：多模态LLM在KhatianDoc基准的大部分QA任务上完全无法输出正确答案，算术任务性能未达简单均值基准，核心是模型在该领域存在能力缺失，而非性能差距。

2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：实验采用固定zero-shot协议，论文未报告其他跨域迁移相关结果
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
1. 多模态LLM在孟加拉RS Khatian记录相关任务上存在能力缺失，而非性能差距；
2. KhatianDoc基准中39.3%的QA类别下，所有评估模型均无正确答案；
3. 算术任务中模型表现差于constant-mean基准，精确与近匹配分数重合，呈现去相关特性，无近似性；
4. 实验存在拒绝评分bug，需区分修正后与原始分数，Metadata指标存在inflation需标注为上界。
- 方法局限性：
1. 基准仅覆盖孟加拉国Munshiganj地区的RS Khatian记录，未涉及其他区域或类型的孟加拉法律土地记录；
2. 仅在固定zero-shot设置下评估6个多模态LLM，未测试微调、少-shot等其他设置。
- 未来工作：
1. 扩展KhatianDoc基准的覆盖区域与RS Khatian记录类型；
2. 评估多模态LLM在微调、少-shot等更多设置下的表现；
3. 开发针对Ana-Ganda-Kora-Kranti-Til符号的识别与处理方法；
4. 修正拒绝评分bug，优化Metadata指标的准确性。

> ✅ **总结一句话**：论文提出的KhatianDoc基准是首个针对孟加拉RS Khatian记录的多模态LLM评估基准，经人工验证发现多模态LLM在该领域存在能力缺失，公开的基准为未来模型适配与改进提供了诊断依据。

</details>

---

### 12. [Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models](https://arxiv.org/abs/2609.03493v1)

**Authors**: Xingming Long, Yu Liu, Zhiwei Yang, Hanqi Feng, Shaojie Zhang, Barnabas Poczos, Chao Jiang, Zhenbo Luo, Lei Jiang, Pei Fu  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.03493v1  

#### Abstract
Modern vision-language models (VLMs) can directly answer many image-grounded questions, yet they often struggle with complex queries requiring fine-grained visual details or external knowledge. To acquire this missing evidence, agentic VLMs invoke tools such as image cropping, image search, and text...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现代视觉语言模型（VLM）可直接回答多数图像基础问题，但针对需细粒度视觉细节或外部知识的复杂查询时表现不足；代理型VLM通过调用图像裁剪、图像搜索、文本搜索等工具获取缺失证据，但现有训练范式仅以最终答案正确性评估模型，未对证据获取与利用进行细粒度监督，导致两个关键缺陷：一是模型常发出冗余或偏离目标的工具调用，无法收集必要证据；二是即使调用合适工具，模型也常无法从工具返回的观测中提取所需信息。

🚀 提出的新方法与思路
**NTEP（Necessary Tool-Evidence Path）标注方案**：一种新的标注方案，显式为每个查询指定所需的必要外部证据及对应的工具调用，明确代理需达成的证据获取目标。
**NTEP-R（NTEP Reward）监督机制**：一种监督机制，确保每个工具调用严格推进推理至最终解，具体包含两部分：一是奖励代理对齐调用前的意图与必要证据寻求目标，二是确保工具调用后观测的信息总结与指定的必要证据一致；此外引入non-repeated-goal regularizer，惩罚重复访问已满足的NTEP目标的冗余工具调用。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
细粒度监督能力 | 突破现有仅以最终答案正确性评估的范式，提供针对工具调用和证据利用的细粒度监督
冗余调用抑制 | 引入non-repeated-goal regularizer，有效减少无意义的重复工具调用
推理推进性保障 | 奖励机制确保每个工具调用都服务于向最终解推进的推理过程
信息提取有效性 | 要求工具后观测信息与必要证据对齐，解决现有模型无法提取关键信息的问题

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
七个图像基础基准 | 评估NTEP-8B在统一三工具框架（图像裁剪、图像搜索、文本搜索）下的搜索导向准确率和工具使用效率

🎯 实验设置与评估指标
任务为需调用工具获取外部证据的图像基础复杂查询下的代理型VLM性能评估。
指标 | 含义（箭头方向）
--- | ---
搜索导向准确率 | 模型对需工具调用的查询回答正确的比例，↑越高越好
工具使用效率 | 模型完成查询所需工具调用的合理性（无冗余），↑越高越好

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
现有基于最终答案监督的代理型VLM方法 | 基准方法 | 仅以最终答案正确性为训练和评估标准，缺乏对工具调用和证据利用的细粒度监督

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：论文未报告具体的表编号、图编号及对应的定量数值结果，仅说明NTEP-8B在统一三工具框架内，于七个图像基础基准上显著提升搜索导向准确率和工具使用效率。
💡 结论：NTEP-8B在需外部证据的图像基础复杂查询任务上，相较于现有基准方法实现了性能的显著提升。
**效率对比**：论文未报告
**跨域/zero-shot迁移**：论文未报告
**鲁棒性/扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 现有代理型VLM因缺乏细粒度的工具-证据路径监督，存在冗余工具调用与工具后信息提取不足的核心问题；
- NTEP标注方案与NTEP-R监督机制能有效解决上述问题，在统一三工具框架下，于七个图像基础基准上显著提升模型的搜索导向准确率和工具使用效率；
- 8B参数的NTEP-8B实现了高效的工具调用与证据利用，是代理型VLM性能提升的有效方案。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文提出NTEP标注方案与NTEP-R监督机制，针对代理型VLM工具调用与证据利用监督不足的痛点，在需外部证据的图像基础复杂查询任务上显著提升了模型性能。

</details>

---

### 13. [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515v1)

**Authors**: Bo Zeng, Yu Zhao, Yefeng Liu, Zhihong Lu, Xuanfan Ni, Xintong Wang  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2609.03515v1  

#### Abstract
Decoding-time KV cache compression research focuses heavily on designing better token scoring functions, while the temporal rule that aggregates scores across decode steps is often treated as an implementation detail. Under aggressive KV compression, we find that exponential-moving-average (EMA) agg...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation
1. 论文的主要贡献和创新点
✅ 解决的问题
解码时KV缓存压缩研究多聚焦于设计更优的token评分函数，而跨解码步骤聚合评分的时间规则常被当作实现细节；在激进KV压缩场景下，不同时间聚合策略对不同评分函数的影响存在差异，现有方法未充分关注时间聚合与排名保留这两个关键设计因素，导致方法间稳定性与性能差异难以清晰识别。
各方法缺陷：1）指数移动平均（EMA）聚合会使近似顺序保留的评分函数修改在驱逐集层面难以区分，降低方法间可分辨性；2）KeyDiff、key norm、时间近邻度（recency）及学习得到的scorer会改变token排名，导致性能明显下降；3）全刷新方式的KV驱逐方法吞吐量较低，存在优化空间。

🚀 提出的新方法与思路
**InertiaKV**：一种基于EMA的解码时KV驱逐方法，通过时间聚合保留token的动态权重；
**InertiaKV-Lazy**：InertiaKV的周期刷新变体，调整刷新频率以减少计算开销、提升吞吐量；
**Score-Free解码**：在第一个解码步骤对全上下文进行一次评分，冻结该排名，后续解码过程不再执行任何评分操作。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 解码吞吐量 | InertiaKV-Lazy的解码吞吐量是全刷新InertiaKV的1.34-1.46倍 |
| 评估质量 | Score-Free解码移除后续评分后，平均质量变化仅为+0.03，几乎不降低评估效果 |
| 排名稳定性 | EMA聚合使Value-norm、entropy等评分函数的驱逐集高度相关，排名保留度更高，方法稳定性更强 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongBench | 用于性能评估 |
| LongBench-v2 | 用于性能评估 |
| RULER | 用于性能评估 |
| 六个open-weight backbones | 用于性能评估 |

🎯 实验设置与评估指标
任务：解码时KV缓存压缩下的长文本处理性能评估；
| 指标 | 含义 |
| --- | --- |
| 解码吞吐量 | 越高越好（↑） |
| 平均质量变化 | 越小越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| EMA聚合相关策略 | 时间聚合基线 | 用于对比不同时间聚合规则对评分函数的影响 |
| KeyDiff、key norm、recency、学习scorer | Token评分函数基线 | 用于对比不同评分函数的性能与排名稳定性 |
| 全刷新InertiaKV | KV驱逐基线 | 用于对比InertiaKV-Lazy的吞吐量提升效果 |

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主benchmark性能（L2/碰撞率等）：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告
- 已报告定量结果：1）InertiaKV-Lazy相对全刷新InertiaKV的解码吞吐量为1.34-1.46倍；2）Score-Free解码的平均质量变化为+0.03；以上结果未标注表号、图号等来源，来自论文摘要。
💡 结论：InertiaKV-Lazy可有效提升解码吞吐量，Score-Free解码能在几乎不损失评估质量的前提下减少计算开销，验证了时间聚合与排名保留的重要性。

4. 关键结论和发现
- 激进KV压缩场景下，时间聚合规则对评分函数的稳定性影响显著：EMA聚合下，Value-norm、entropy等评分函数的驱逐集高度相关，方法稳定性强；而KeyDiff、key norm等评分函数会明显改变token排名，导致性能下降；
- 提出的InertiaKV及其变体InertiaKV-Lazy，在激进KV压缩下实现了解码吞吐量的显著提升，Score-Free解码移除后续评分后几乎不影响评估质量，大幅减少了计算开销；
- 时间聚合与排名保留是解码时KV驱逐中需重点关注的设计因素，评分函数质量并非唯一决定性因素，时间规则的选择会显著影响方法性能与稳定性。

- 方法局限性
论文未报告具体基线方法的详细对比数据，也未涉及不同骨干模型或数据集上的性能差异分析；未开展鲁棒性测试，未提供相关结果。

- 未来工作
可探索更优的时间聚合策略，进一步平衡解码时KV驱逐的吞吐量与质量；可对Score-Free解码在更多任务场景下的适用性与优化空间进行深入研究。

> ✅ **总结一句话**：该论文通过研究解码时KV缓存驱逐的时间聚合与排名保留问题，提出InertiaKV及其周期刷新变体InertiaKV-Lazy，在激进压缩场景下实现了1.34-1.46倍的解码吞吐量提升，同时Score-Free解码能在几乎不降低评估质量的前提下减少计算开销，明确了时间聚合与排名保留是KV驱逐的关键设计因素。

</details>

---

### 14. [DE-Venus: A Data-Efficient RLVR Framework for Large Language Models](https://arxiv.org/abs/2609.03324v1)

**Authors**: Shenzhi Yang, Guangcheng Zhu, Kai Tang, Zhengqing Zang, Xing Zheng, Haobo Wang, Yingfan Ma, Bowen Song, Bo Han, Bo An, Lei Feng, Weiqiang Wang, Junbo Zhao, Gang Chen  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 36.5  
**Type**: new  
**ArXiv ID**: 2609.03324v1  

#### Abstract
Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale. Existing methods address sample selection, incomplete supervision, or noisy lab...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

DE-Venus: A Data-Efficient RLVR Framework for Large Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
RLVR可提升大型语言模型（LLM）的推理能力，但其实际规模化受限于昂贵的on-policy rollout成本和大规模获取可靠学习目标的成本；现有方法存在以下缺陷：①分别处理样本选择、不完整监督或噪声标签问题，未统一解决；②将监督逻辑与分布式训练绑定，阻碍了可控对比与方法复用。

🚀 提出的新方法与思路
**统一监督生命周期框架**：将监督视为数据准备与策略优化过程中的演化状态，构建包含三个核心模块的统一数据高效RLVR框架DE-Venus。
**主动数据选择（Active Data Selection）**：分配训练与标注预算。
**弱监督构造（Weak Supervision Construction）**：从未标注示例中推导学习信号。
**训练时监督优化（Training-Time Supervision Refinement）**：过滤或修正不可靠的监督信号。
DE-Venus支持七种代表性方法及数据选择pipeline，将特定方法的决策表述为离线数据集转换或目标、奖励、批次、优势的在线转换，同时保留verl的分布式执行契约。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
监督逻辑组织 | 统一将监督视为数据准备与策略优化的演化状态，解耦方法决策与分布式训练
数据效率 | 仅用10%的标签或13%的相关数据即可实现模型质量的保持或提升
训练收敛速度 | 所选业务配置下收敛步骤减少63%~75%
兼容性与复用性 | 保留verl的分布式执行契约，支持七种代表性方法与数据选择pipeline，便于方法的可控对比与复用

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
公开基准数据集 | 验证模型在通用推理任务上的性能
三个业务场景数据集 | 验证模型在实际业务场景中的有效性

🎯 实验设置与评估指标
任务 | 基于RLVR的LLM推理任务
指标 | 含义（箭头方向）
--- | ---
模型质量 | 衡量LLM推理的质量，越高越好（↑）
收敛步骤 | 训练过程中达到稳定性能所需的步骤数，越低越好（↓）

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

**无对应表**

场景 | 收敛步骤减少比例
--- | ---
业务场景 | 63%~75%

💡 结论：在业务场景中，DE-Venus的所选配置仅用10%的标签或13%的相关数据即可保持或提升模型质量，同时将收敛步骤减少63%~75%。

4. 关键结论和发现
- 主要发现：1. DE-Venus的统一框架将监督逻辑与分布式训练解耦，实现了数据效率与RL训练可扩展性的平衡；2. 在公开基准和业务场景中，DE-Venus仅用少量数据（10%标签/13%相关数据）即可达成或优于原方法的模型质量；3. DE-Venus在业务场景中可显著加快收敛速度，减少63%~75%的收敛步骤。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：DE-Venus是针对LLM的RLVR任务的统一数据高效框架，通过三个核心模块组织监督生命周期，在保留分布式训练兼容性的基础上，仅用少量数据即可保持或提升模型质量并加快收敛，降低训练成本。

</details>

---

### 15. [Tail-Likelihood Reinforcement Learning](https://arxiv.org/abs/2609.02987v1)

**Authors**: Shrinivas Ramasubramanian, Daman Arora, Fahim Tajwar, Guanning Zeng, Qingyang Wu, Zhongzhu Zhou, Chenfeng Xu, Haiwen Feng, Yuda Song, Aarti Singh, Ruslan Salakhutdinov, J. Andrew Bagnell, Jeff Schneider, Andrea Zanette  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2609.02987v1  

#### Abstract
Reinforcement learning typically optimizes average reward. For generative policies, the average can hide an important distinction: two policies can achieve the same mean reward while having very different chances of producing a rare but high-reward rollout. This matters as sampling increases during ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Tail-Likelihood Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有强化学习通常优化平均奖励，对于生成策略，平均奖励会掩盖不同策略产生稀有高回报rollout的概率差异，而训练和推理时采样的收益依赖于保留高回报结果的概率质量，这一问题未被现有方法充分考虑。
🚀 提出的新方法与思路
**Tail-Likelihood Reinforcement Learning（TailRL）**，该方法直接优化奖励覆盖度：不局限于期望奖励，而是将连续奖励转化为一系列二元成功事件，对每个奖励阈值计算策略超过该阈值的概率；核心是最大化随机选择的奖励阈值的对数概率，其梯度会给稀有高回报rollout赋予更多权重，可解释为Best-of-(k)梯度的混合变体；该方法仅需对优势函数做简单修改，可兼容现有强化学习流水线。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 核心优化目标 | 针对奖励上尾覆盖度优化，而非仅关注平均奖励 |
| 稀有样本利用能力 | 显著提升对稀有高回报训练样本的利用，避免次优解 |
| 框架兼容性 | 仅修改优势函数即可适配现有强化学习流程 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务为object localization、maze navigation、GUI grounding、code optimization，论文未报告具体评估指标及含义，故写论文未报告
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 常规平均奖励优化的强化学习方法 | 基线强化学习方法 | 以期望奖励为优化目标，未充分关注稀有高回报rollout的概率 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验的表号、图号或定量数值，故写论文未报告

4. 关键结论和发现
- 主要发现：1. TailRL通过最大化随机奖励阈值的对数概率，有效强化了对稀有高回报训练样本的利用，可帮助模型避免次优解；2. TailRL适配现有强化学习流水线，模型在推理时能从额外样本中获得更多收益。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：TailRL通过直接优化奖励上尾的覆盖度，提升强化学习对稀有高回报样本的利用效率，避免次优解且增强了模型推理时对额外样本的获益能力，同时兼容现有强化学习框架。

</details>

---

### 16. [R$^{2}$Adapter: A Routing and Rewriting Adapter for Efficient Hybrid RAG](https://arxiv.org/abs/2609.02894v1)

**Authors**: Yucan Guo, Miao Su, Saiping Guan, Long Bai, Zhongni Hou, Zixuan Li, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2609.02894v1  

#### Abstract
Retrieval-Augmented Generation (RAG) has become a prevailing paradigm for enhancing Large Language Models (LLMs) with non-parametric knowledge. Vanilla RAG efficiently handles simple queries but struggles with relational or multi-hop reasoning. Graph-based RAG alleviates this issue but incurs higher...

---

### 17. [SGD-KV: Summarization Guided KV Cache Compression](https://arxiv.org/abs/2609.03235v1)

**Authors**: Zeyu Liu, Woomin Song, Xuandi Fu, Sai Muralidhar Jayanthi, Vivek Govindan, Aram Galstyan, Sravan Babu Bodapati, Srikanth Ronanki  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.03235v1  

#### Abstract
Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches. Existing KV cache compression techniques typically rely on simple heuristics, overlooking the distinct functional roles of different attention heads. We pr...

---

### 18. [Landmark-Based Discrimination of Injury-Associated Athlete-Sessions from Minute-Resolution Multimodal Football Monitoring Data](https://arxiv.org/abs/2609.03790v1)

**Authors**: Evangelos Chatzidimitriou, Konstantinos Tserpes  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2609.03790v1  

#### Abstract
Athlete monitoring data may be recorded minute by minute throughout a match or training session, while injury information may only indicate whether the entire session was injury-associated.
  This creates a modelling problem: assigning the same session-level label to every minute would imply that in...

---

### 19. [Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents](https://arxiv.org/abs/2609.03438v1)

**Authors**: Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng, Zheng Wu, Yansi Li, Chuanbiao Song, Jun Lan, Huijia Zhu, Weiqiang Wang, Zhuosheng Zhang  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.03438v1  

#### Abstract
Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CON...

---

### 20. [FPCO-Dialog: A Multi-Turn False-Premise Benchmark for Correction and Cooperation in Vision-Language Models](https://arxiv.org/abs/2609.03331v1)

**Authors**: Jiayuan Ma, Yuqi Lu, Weiyang Guo, Chenrui Wang, Junyi Shu, Xuebo Liu, Min Zhang, Jing Li  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2609.03331v1  

#### Abstract
Vision-language models (VLMs) are increasingly deployed in multi-turn settings where users may describe visual content with incorrect assumptions. Yet existing evaluations rarely isolate how models respond when the same visually grounded false premise persists across dialogue turns. We introduce FPC...

---

### 21. [Learnable composition for neural operators](https://arxiv.org/abs/2609.03069v1)

**Authors**: Zituo Chen, Baiming Zhang, Sili Deng  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.03069v1  

#### Abstract
Neural operators are fast, differentiable surrogates for physical simulation, but their accuracy often degrades when domain geometry, size, or operating conditions differ from training. Supervised adaptation can recover accuracy, but even a small target set requires costly high-fidelity simulations....

---

### 22. [Risk and Anomaly Identification for Distribution Network Optimal Operation Based on Reinforcement Learning and Uncertainty Quantification](https://arxiv.org/abs/2609.03308v1)

**Authors**: Ziqi Zhang  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2609.03308v1  

#### Abstract
Reliable operation of modern distribution networks requires timely identification of operational risks and anomalous events under pervasive uncertainty. In practice, operators must identify risks that are inherent in stochastic yet in-distribution conditions, and anomalies that correspond to out-of-...

---

### 23. [Govern the Model, Not Only the Data: Storage, Circulation, and Learning in Creative AI](https://arxiv.org/abs/2609.03800v1)

**Authors**: Phoenix Perry, George Simms, Elizabeth Wilson, Yasmine Boudiaf, Nick Bryan-Kinns, Tega Brain, R. Luke DuBois, Alix Rule, Rachel Meade Smith, Kelani Nichole, Atharva Pravin Pawar, Rebecca Fiebrink  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.03800v1  

#### Abstract
Federated learning is increasingly presented as a privacy-preserving advance: personal data remain on the device, and only model updates are shared. It borrows the vocabulary of the federated social web, yet inverts its logic, distributing computation while the resulting model stays with whoever con...

---

### 24. [The Impact of Synthetic Data Augmentation on Discourse-Pragmatic Function Classification](https://arxiv.org/abs/2609.03652v1)

**Authors**: Sara Sorahi, Kevin Tang, Reza Kazemian  
**Category**: cs.CL  
**Published**: 2026-09-04  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2609.03652v1  

#### Abstract
Synthetic data augmentation has become a common strategy for addressing class imbalance in NLP, but most approaches focus on the quantity and diversity of generated examples rather than their geometric relationship to real training data. We investigate this question in the context of discourse pragm...

---

### 25. [BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training](https://arxiv.org/abs/2609.03151v1)

**Authors**: Bigyan Ghimire, Jon C. Calhoun  
**Category**: cs.DC  
**Published**: 2026-09-04  
**Score**: 28.5  
**Type**: new  
**ArXiv ID**: 2609.03151v1  

#### Abstract
Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements. Sequence parallelism has emerged as an essential technique for addressing bottlenecks in long sequenc...

---

### 26. [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1)

**Authors**: Sergii Kozyrev, Davyd Maiboroda  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 27.5  
**Type**: new  
**ArXiv ID**: 2609.04098v1  

#### Abstract
Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially...

---

### 27. [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010v1)

**Authors**: Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 27.5  
**Type**: new  
**ArXiv ID**: 2609.04010v1  

#### Abstract
Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution w...

---

### 28. [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1)

**Authors**: Haoyaun Zhu, Jie Zhang  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.04198v1  

#### Abstract
Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campai...

---

### 29. [Frontier LLMs are effective batch optimizers: Assessing reasoning models in continuous and discrete settings](https://arxiv.org/abs/2609.03177v1)

**Authors**: Frank Hu, Shriram Chennakesavalu, David Graff  
**Category**: cs.LG  
**Published**: 2026-09-04  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2609.03177v1  

#### Abstract
Frontier large language models (LLMs) have become attractive priors for optimization due to their large-scale pretraining that enables them to navigate a variety of optimization settings. However, the effectiveness of modern reasoning LLMs in batch optimization settings remains underexplored. Here w...

---

### 30. [GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis](https://arxiv.org/abs/2609.03553v1)

**Authors**: Linh Le, Melanie Bui, My Chiffon Nguyen, Zachary Schlosser, David Williams-King  
**Category**: cs.AI  
**Published**: 2026-09-04  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2609.03553v1  

#### Abstract
Policy analysis requires more than predicting whether a proposal will pass: it requires identifying who will be affected, how those actors respond, and what follows. LLM-based policy simulations model these processes at scale, but their validity is hard to establish when plausible behaviour is never...

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
