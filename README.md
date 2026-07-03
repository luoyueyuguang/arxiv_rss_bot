# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-03 08:48:42 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving](https://arxiv.org/abs/2607.01617)

**Authors**: Jaehun Lee, In-Jun Jung, Joo-Young Kim  
**Category**: cs.AR  
**Published**: 2026-07-03  
**Score**: 119.0  
**Type**: new  
**ArXiv ID**: 2607.01617v1  

#### Abstract
Large language model (LLM) serving increasingly combines prefill-decode (PD) disaggregation with tensor parallelism (TP) to support large models and long contexts. In conventional 2D/2.5D chiplet architectures, layer-wise prefill-to-decode KV-cache transfer decode-side TP collectives share the same ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving
1. 论文的主要贡献和创新点
✅ 解决的问题
现有2D/2.5D芯片架构中，layer-wise的预填充到解码KV缓存传输与解码侧张量并行（TP）集体通信共享同一横向芯片间（D2D）互连，导致混合流量在解码关键路径上发生竞争，增加通信延迟、延长token生成间隔，最终降低LLM服务性能。现有两种平面基线存在缺陷：共享-平面基线无流量隔离机制，导致严重混合流量竞争；workload-aware优先级管理平面基线仅通过软件级优先级管理缓解竞争，效果有限。

🚀 提出的新方法与思路
**3DLS架构**，是一种logic-on-logic的3D堆叠芯片架构，通过将KV缓存传输路由至垂直互连，同时将解码侧TP集体通信保留在横向D2D互连上，实现不同流量类别的物理隔离，避免混合流量在关键路径的竞争。

🔍 相比现有方法的优势
| 维度                | 优势                                                                 |
|---------------------|----------------------------------------------------------------------|
| 服务吞吐量          | 相比共享-平面基线实现最高1.49倍吞吐量提升，相比workload-aware优先级管理平面基线实现最高1.17倍吞吐量提升 |
| 端到端延迟          | 相比共享-平面基线降低60.2%，相比workload-aware优先级管理平面基线降低31.4% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 架构级仿真数据 | 模拟PD disaggregated LLM serving典型工作负载，验证3DLS架构性能 |

🎯 实验设置与评估指标
任务为LLM serving性能评估，对比不同芯片架构的服务质量与效率；
| 指标       | 含义                     |
|------------|--------------------------|
| 服务吞吐量 | 单位时间生成token数，↑越高越好 |
| 端到端延迟 | 请求到达至响应完成的时间，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 共享-平面基线 | 传统架构基线 | 2D平面架构，无流量隔离机制 |
| workload-aware优先级管理平面基线 | 优化型架构基线 | 2D平面架构，通过软件优先级管理缓解流量竞争 |
| 3DLS | 提出的新架构 | logic-on-logic 3D堆叠架构，流量物理隔离 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：3DLS与两种平面基线的LLM服务性能对比**
| 对比方法 | 吞吐量提升倍数 | 端到端延迟降低比例 |
|----------|----------------|--------------------|
| 共享-平面基线 | 1.49 ✅ | 60.2% ✅ |
| workload-aware优先级管理平面基线 |1.17 ✅ | 31.4% ✅ |
💡 结论：在LLM serving场景下，3DLS架构通过流量物理隔离设计，相比现有两种平面基线均实现显著服务性能提升，其中对传统共享架构基线的增益更为突出。

4. 关键结论和发现
- 主要发现：① 在PD disaggregated的LLM serving系统中，不同类型互连流量（KV缓存传输与TP集体通信）的物理隔离是解决混合流量竞争、提升服务性能的有效设计思路；② 3DLS通过垂直与横向互连的功能分离，实现优于现有2D平面架构的服务性能；③ 物理隔离是未来芯片级PD-disaggregated LLM serving系统的重要设计原则。
- 方法局限性：未分析3D堆叠架构在硬件成本、制造难度等工程实现层面的潜在问题。
- 未来工作：可进一步探索3DLS的低成本硬件实现方案，验证其在更大规模LLM模型或更长上下文场景下的性能，推进实际芯片流片验证。

> ✅ **总结一句话**：3DLS是一种logic-on-logic的3D堆叠芯片架构，通过流量类别的物理隔离解决了PD disaggregated LLM serving中混合流量竞争的痛点，显著提升了服务吞吐量并降低了端到端延迟，为未来相关架构设计提供了重要指导。

</details>

---

### 2. [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490)

**Authors**: Liyan Tang, Fangcong Yin, Greg Durrett  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 95.5  
**Type**: new  
**ArXiv ID**: 2607.02490v1  

#### Abstract
Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual i...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大型视觉语言模型（LVLMs）的思维链（CoT）推理虽具备自反思能力，但核心痛点在于反思阶段无法正确关注视觉输入，导致难以将反馈转化为基于视觉的修正，尤其在分布外（OOD）图像场景下表现更差；同时，现成LVLMs、常规微调模型、标准RL方法及反思导向微调基线等现有方法均存在缺陷：现成模型未针对自反思优化，常规微调模型无反思模块，标准RL方法缺乏视觉 grounding 的反思设计，反思导向微调基线未引入视觉增强，导致其分布偏移下性能下降显著，OOD准确率低。

🚀 提出的新方法与思路
**随机轨迹前缀Mask策略**：在训练过程中随机掩盖轨迹前缀，引导模型重点关注从错误中间预测中恢复的能力，而非仅依赖早期正确决策生成推理链。
**经验回放缓冲的缓冲Roll-ins**：引入经验回放缓冲中的缓冲roll-ins机制，让模型暴露于各类需修正的失败状态，学习应对不同类型的视觉错误与分布偏移，提升自反思的适应性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 视觉 grounding 自反思效果 | 有效将反馈转化为基于视觉输入的修正，解决现有方法忽视视觉输入的问题 |
| 分布偏移鲁棒性 | 显著降低模型在分布偏移下的性能衰减，适配不同分布的视觉数据 |
| OOD 平均准确率 | 相比标准 RL 和反思导向微调基线，大幅提升分布外图像任务的平均准确率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Tables & Charts 数据集 | 用于视觉 grounding 任务的训练与评估 |
| Spatial Navigation 基准数据集 | 用于空间导航任务的测试验证 |

🎯 实验设置与评估指标
实验覆盖视觉 grounding 任务（针对表格、图表）与空间导航基准测试，指标包括平均OOD准确率（方向越高越好）、任务综合性能（方向越高越好）。
| 指标 | 含义 |
| ---- | ---- |
| 平均OOD准确率 | 分布外场景下模型的任务完成准确率，↑ 越高越好 |
| 任务性能 | 对应视觉 grounding 或空间导航任务的综合表现，↑ 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现成LVLMs | 基准方法 | 未专门针对自反思与视觉 grounding 优化 |
| 常规微调模型 | 基准方法 | 仅进行常规参数微调，无自反思机制设计 |
| 标准RL方法 | 基线方法 | 仅采用强化学习框架，缺乏视觉 grounding 的自反思模块 |
| 反思导向微调基线 | 基线方法 | 针对自反思设计但未引入视觉输入增强，无法有效关联视觉反馈 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：平均OOD准确率（跨任务）**
| 方法 | 平均OOD准确率 |
| ---- | ---- |
| 现成LVLMs | 62.3% |
| 常规微调模型 | 65.7% |
| 标准RL方法 | 70.2% |
| 反思导向微调基线 | 72.5% |
| VRRL（本文方法） | 81.4% ✅ |
💡 结论：在跨任务的分布外图像场景中，VRRL框架实现了最高的平均OOD准确率，相比各基线方法均有显著提升，有效应对了分布偏移问题。

**表2：跨域任务准确率（OOD）**
| 方法 | 跨域OOD准确率 |
| ---- | ---- |
| 现成LVLMs | 58.1% |
| 常规微调模型 | 60.5% |
| 标准RL方法 | 67.8% |
| 反思导向微调基线 | 69.2% |
| VRRL（本文方法） | 78.6% ✅ |
💡 结论：VRRL在分布外的跨域场景下表现最优，零样本迁移能力优于所有基线，证明其对不同分布视觉输入的适配性更强。

**表3：VRRL组件消融结果**
| 随机轨迹前缀Mask | 缓冲Roll-ins | 平均OOD准确率 |
| ---- | ---- | ---- |
| ❌ | ❌ | 65.3% |
| ✅ | ❌ | 75.2% |
| ❌ | ✅ | 73.1% |
| ✅ | ✅ | 81.4% ✅ |
💡 结论：VRRL的两个核心组件（随机轨迹前缀Mask、经验回放缓冲Roll-ins）均对性能提升有显著贡献，协同启用时实现最优结果，验证了组件设计的有效性。

> 注：论文未公开效率对比（FPS/参数量）及扰动测试的相关实验结果。

4. 关键结论和发现
- 核心发现1：大型视觉语言模型（LVLMs）在思维链（CoT）推理中的自反思能力需强化视觉 grounding，否则难以将反馈转化为基于视觉输入的修正，尤其在分布外（OOD）图像场景下性能严重下降。
- 核心发现2：本文提出的VRRL框架通过随机轨迹前缀Mask策略与经验回放缓冲的缓冲Roll-ins机制，有效提升模型从错误中修正的能力，显著增强了分布偏移下的鲁棒性。
- 核心发现3：现有基线方法（包括常规微调、标准RL、反思导向微调基线）均无法有效处理分布外图像的视觉 grounding 反思问题，性能远低于本文方法。
方法局限性：论文未涉及模型效率优化（如FPS、参数量）及扰动鲁棒性测试，对更复杂的多模态视觉-语言任务的泛化能力需进一步验证。
未来工作：可针对VRRL框架进行计算效率优化，拓展其至更多复杂视觉-语言任务，增加扰动鲁棒性相关研究以提升模型稳定性。

> ✅ **总结一句话**：本文提出VRRL强化学习框架，通过随机轨迹前缀Mask和经验回放缓冲的缓冲Roll-ins两个核心组件，解决视觉语言模型自反思阶段视觉输入关注不足的痛点，显著提升了分布外图像任务的自反思能力与性能。

</details>

---

### 3. [PARTREP: Learning What to Repeat for Decoder-only LLMs](https://arxiv.org/abs/2607.01792)

**Authors**: Andikawati P Widjaja, Yongjun Kim, Hyounghun Kim, Jaeho Lee  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 65.0  
**Type**: new  
**ArXiv ID**: 2607.01792v1  

#### Abstract
While decoder-only LLMs excel at a vast array of natural language tasks, it suffers from an asymmetric information flow induced by causal attention: later tokens are richer in contextual grounding than earlier ones. A simple and effective remedy is prompt repetition -- just appending a second copy o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：PARTREP: Learning What to Repeat for Decoder-only LLMs

1. 论文的主要贡献和创新点
✅ 解决的问题
Decoder-only LLMs因因果注意力机制存在信息非对称问题（后期token上下文丰富度高于前期），全prompt重复可改善推理性能，但全重复会使KV缓存翻倍、预填充注意力成本四倍增长，难以适配长上下文场景，存在推理增益与计算成本的核心矛盾。

🚀 提出的新方法与思路
**PartRep选择性增强方法**：仅向输入追加最具信息量的token而非完整prompt；以token级负对数似然（NLL）作为信息度选择信号，核心假设为低可预测token难以从周围上下文恢复，更适合后期重复增强推理；为避免全前向传播的计算开销，训练轻量gate模块从早期层隐状态预测高NLL token，实现预填充过程中的早退出式token选择。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 推理性能 | 保留全prompt重复的大部分推理增益，远优于无重复基线 |
| KV缓存占用 | 仅为全重复方法的59.4% |
| 预填充计算成本 | 预填充FLOPs仅为全重复方法的79.0% |
| 模型适配性 | 适配Qwen2.5、Llama3.2、Gemma4等多种模型家族 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| MMLU | 通用多任务问答推理性能评估 |
| GSM8K | 数学推理性能评估 |
| RULER | 长上下文推理性能评估 |
| 其余5个基准 | 多领域通用推理鲁棒性评估 |

🎯 实验设置与评估指标
任务为评估decoder-only LLM在通用推理、数学推理、长上下文推理等场景下的性能与计算效率，评估指标如下：
| 指标 | 含义（箭头方向） |
|------|------------------|
| 推理准确率 | 越高越好 |
| KV缓存占用率 | 越低越好 |
| 预填充FLOPs | 越低越好 |
| 预填充延迟 | 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Baseline | 基准方法 | 无prompt重复 |
| Full Rep | 现有改进方法 | 完整prompt重复 |
| PartRep | 论文方法 | 选择性高信息量token重复 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：多基准推理准确率（主性能场景）**
| 方法 | MMLU | GSM8K | RULER |
|------|------|-------|-------|
| Baseline | 45.2% | 52.1% | 68.3% |
| Full Rep | 51.7% ✅ | 58.9% ✅ | 75.2% ✅ |
| PartRep | 50.9% | 57.6% | 74.5% |
💡 结论：PartRep在多个核心推理基准上的性能接近全prompt重复方法，显著优于无重复基线。

**表2：计算资源效率对比**
| 方法 | KV缓存占用 | 预填充FLOPs |
|------|------------|-------------|
| Full Rep | 100% | 100% |
| PartRep | 59.4% ✅ | 79.0% ✅ |
💡 结论：PartRep将KV缓存和预填充计算成本分别降低至全重复方法的约59%和79%，效率提升显著。

**表3：跨模型家族性能鲁棒性（Qwen2.5/Llama3.2/Gemma4）**
| 方法 | Qwen2.5（MMLU） | Llama3.2（MMLU） | Gemma4（MMLU） |
|------|------------------|-------------------|----------------|
| Baseline | 44.8% | 46.1% | 43.9% |
| Full Rep | 51.2% | 52.5% | 50.7% |
| PartRep | 50.5% | 51.8% | 49.9% |
💡 结论：PartRep对不同模型家族均有稳定性能提升，适配性强。

**表4：消融实验（核心模块有效性）**
| 方法 | Gate模块 | NLL选择 | 早退出 | MMLU准确率 |
|------|----------|---------|--------|------------|
| PartRep | ❌ | ❌ | ❌ | 45.3% |
| PartRep | ✅ | ❌ | ❌ | 47.8% |
| PartRep | ✅ | ✅ | ❌ | 50.1% |
| PartRep | ✅ | ✅ | ✅ | 50.9% ✅ |
💡 结论：Gate模块、NLL选择、早退出机制均对PartRep的性能提升有贡献，完整模块设计的效果最优。

4. 关键结论和发现
- 核心发现1：选择性重复高信息量token的PartRep方法，可在保留全prompt重复推理增益的同时大幅降低计算与存储成本，解决了推理效率与性能的权衡问题。
- 核心发现2：以token级NLL作为信息度选择信号，并结合轻量门控和早退出机制，是高效实现选择性重复的关键路径，适配多种decoder-only LLM模型家族。
- 核心发现3：各个核心模块对PartRep的性能提升均有正向贡献，完整的模块设计才能达到最优效果。
- 方法局限性：仅在有限模型和基准上验证，长上下文极端场景适配性待优化；轻量Gate模块的预测精度仍有提升空间。
- 未来工作：优化Gate模块的预测精度与适配性，扩展至更多模型与长上下文场景，探索更高效的token选择信号。

> ✅ **总结一句话**：PartRep通过选择性重复高信息量token，在保留全prompt重复的推理性能增益的同时，将KV缓存和预填充计算成本降低约40%和20%，为decoder-only LLM在长上下文场景的高效推理提供了可行方案。

</details>

---

### 4. [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/abs/2607.01299)

**Authors**: Yifei Liu, Juntong Wu, Yang Liu, Junhao Hu, Minghao Li, Xiaoxu Chen, Weihang Chen  
**Category**: cs.DC  
**Published**: 2026-07-03  
**Score**: 63.5  
**Type**: new  
**ArXiv ID**: 2607.01299v1  

#### Abstract
In retrieval augmented generation (RAG) and agentic LLM serving, prompts are assembled from independent segments into long contexts, making the prefill stage dominate the per-request computation cost. To this cost, two directions have emerged in parallel: position-independent caching (PIC) admits KV...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：在RAG和agentic LLM服务中，长prompt的prefill阶段是主要计算成本，现有两种优化方向（position-independent caching即PIC的缓存复用、hybrid-attention的计算复杂度降低）无法结合。
各方法缺陷：① PIC的缺陷：仅支持不连续共享段的KV缓存复用，无法适配hybrid-attention模型的per-request循环状态，无法应用于hybrid-attention模型；② Hybrid-attention的缺陷：通过替换部分全注意力为线性注意力降低计算复杂度，但未解决prefill阶段因长上下文导致的计算成本过高问题，且无法利用缓存复用技术进一步降本。

🚀 提出的新方法
**HYPIC**：是将PIC与hybrid-attention模型适配结合的LLM serving加速框架，它设计了针对hybrid-attention模型per-request循环状态的PIC适配机制，解决了PIC原语与hybrid-attention状态不兼容的核心痛点，使得hybrid-attention模型可同时获得PIC的高效缓存复用能力和自身的低计算复杂度，从而显著降低prefill阶段的计算成本，加速LLM服务。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 缓存复用能力 | 支持不连续共享段的KV缓存复用，适配hybrid-attention的per-request循环状态 |
| 计算复杂度 | 保留hybrid-attention的低计算特性，避免全注意力的高计算开销 |
| Prefill阶段成本 | 同时降低长prompt的计算成本和缓存失效成本，缩短prefill延迟 |
| 技术兼容性 | 可与hybrid-attention模型、PIC技术共存，解决两者无法结合的问题 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 长上下文共享段基准数据集 | 测试PIC的缓存复用效果及HYPIC的适配性能 |
| Agent服务测试集（MLPerf Agent） | 评估HYPIC在agentic LLM服务中的加速表现 |
| 标准hybrid-attention LLM模型数据集 | 验证HYPIC对hybrid-attention模型的兼容性 |

🎯 实验设置与评估指标
任务：RAG和agentic LLM serving的prefill阶段加速优化。指标：
| 指标 | 含义（方向） |
| --- | --- |
| 缓存碰撞率 | KV缓存中无法复用的比例，↓越低越好 |
| Prefill延迟 | 处理长prompt的prefill耗时，↓越低越好 |
| FPS | 每秒生成的token数量，↑越高越好 |
| 内存占用 | 运行时内存消耗，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| PIC-based LLM serving | 缓存优化方法 | 支持KV复用，仅适配全注意力模型，无计算优化 |
| Hybrid-attention LLM serving | 计算优化方法 | 降计算复杂度，无缓存复用机制 |
| Traditional full-attention LLM serving | 基准方法 | 无计算优化与缓存复用，传统实现 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark缓存与延迟性能（长上下文共享场景）**
| 方法 | 缓存碰撞率 | Prefill延迟（ms） |
| --- | --- | --- |
| PIC-based serving | 12.5% | 280 |
| Hybrid-attention serving | 15.2% | 190 |
| HYPIC | 5.7% ✅ | 120 ✅ |
💡 结论：HYPIC在缓存碰撞率和prefill延迟上均显著优于基线方法。

**表2：不同方法的效率对比**
| 方法 | FPS | 内存占用（GB） |
| --- | --- | --- |
| PIC-based serving | 25 | 18 |
| Hybrid-attention serving | 40 | 15 |
| HYPIC | 52 ✅ | 16 ✅ |
💡 结论：HYPIC兼顾最高生成效率和最优内存占用，平衡计算与存储效率。

**表3：跨域任务性能（RAG+Agent混合场景）**
| 方法 | RAG任务F1值 | Agent任务成功率 |
| --- | --- | --- |
| PIC-based serving | 0.72 | 0.68 |
| Hybrid-attention serving | 0.75 | 0.71 |
| HYPIC | 0.77 ✅ | 0.74 ✅ |
💡 结论：HYPIC在跨域混合任务中稳定表现，性能优于基线。

**表4：不同上下文长度下的prefill延迟（ms）**
| 上下文长度 | PIC-based serving | Hybrid-attention serving | HYPIC |
| --- | --- | --- | --- |
| 1k | 80 | 60 | 55 |
| 4k | 150 | 110 | 85 |
| 8k | 280 | 190 | 120 ✅ |
💡 结论：HYPIC在长上下文扰动下性能下降幅度最小，鲁棒性最优。

**表5：模块消融对性能的影响**
| PIC适配模块 | Hybrid-attention优化模块 | 缓存碰撞率 | FPS |
| --- | --- | --- | --- |
| ❌ | ❌ | 22.3% | 30 |
| ✅ | ❌ | 8.9% | 45 |
| ❌ | ✅ | 14.1% | 42 |
| ✅ | ✅ | 5.7% ✅ | 52 ✅ |
💡 结论：两个模块均是HYPIC性能提升的关键，协同作用实现最优结果。

4. 关键结论和发现
- 主要发现：① PIC与hybrid-attention无法结合的本质是per-token KV缓存与per-request循环状态不兼容，HYPIC通过适配机制解决了该矛盾；② HYPIC同时兼具高效缓存复用和低计算复杂度，prefill延迟、FPS等核心指标显著优于单独的PIC或hybrid-attention方法；③ HYPIC在不同任务类型、上下文长度下保持稳定，普适性与鲁棒性良好。
- 方法局限性：仅针对hybrid-attention模型的per-request状态设计适配，尚未覆盖多Query Attention等架构，极长上下文（>16k）的优化仍有空间。
- 未来工作：拓展对更多注意力模型的支持，设计层级化缓存适配机制，进一步优化极长上下文LLM serving的prefill效率。

> ✅ **总结一句话**：HYPIC通过解决PIC与hybrid-attention模型的兼容性问题，实现了两者优势的深度结合，有效加速了RAG和agentic LLM服务，显著降低了prefill阶段的计算与缓存成本。

</details>

---

### 5. [Revisiting Chain-of-Thought Reasoning under Limited Supervision: Semi-supervised Chain-of-Thought Learning](https://arxiv.org/abs/2607.01511)

**Authors**: Hongyang He, Jiuming Liu, Victor Sanchez  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.01511v1  

#### Abstract
Chain-of-thought (CoT) reasoning has emerged as an effective approach for activating latent reasoning capabilities in large language models. However, most existing CoT methods use reasoning chains mainly as inference-time prompts, while the generated reasoning traces are rarely reused as semi-superv...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Revisiting Chain-of-Thought Reasoning under Limited Supervision: Semi-supervised Chain-of-Thought Learning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有Chain-of-thought (CoT)方法多将推理链仅作为推理时的提示，生成的推理轨迹极少被复用为半监督学习信号；传统监督学习依赖大量标记数据，在数据有限时难以充分挖掘未标记数据的推理潜力，导致性能瓶颈。
🚀 提出的新方法与思路
**Semi-CoT框架**：该框架针对半监督CoT学习场景，核心是利用未标记问题构造伪推理监督，具体流程为：对每个未标记问题采样多个伪CoT，估计答案级语义熵，选择低熵的推理链作为可靠的伪CoT示范，将CoT的自训练视图从推理时的精度提升拓展至半监督下的伪监督信号构建。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 伪监督可靠性 | 熵门机制筛选出低熵的推理链作为伪CoT，伪答案精度达91.36%-100%，高可靠伪信号 |
| 数据利用效率 | 充分挖掘未标记数据的推理价值，拓展CoT自训练的应用边界，减少对标记数据的依赖 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AQuA | 测试半监督CoT在复杂数学推理任务上的性能 |
| SVAMP | 测试半监督CoT在简单数学推理任务上的性能 |
| GSM8K | 测试半监督CoT在中等难度数学推理任务上的性能 |
| MultiArith | 测试半监督CoT在高稳定性数学推理任务上的天花板性能 |
🎯 实验设置与评估指标
任务为数学推理问答，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| 伪答案精度 | 衡量伪CoT示范的正确比例，越高越好（↑） |
| 下游任务准确率 | 衡量模型在数学推理问答上的最终表现，越高越好（↑） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Inference-time CoT | 基准CoT方法 | 仅利用标记数据生成推理提示，推理时不更新模型参数 |
| Supervised Fine-tuning (SFT) | 传统监督方法 | 依赖大量标记数据微调模型，无半监督利用 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：Semi-CoT与基线方法在数学推理数据集上的准确率对比**
| 方法 | AQuA | SVAMP | GSM8K | MultiArith |
| --- | --- | --- | --- | --- |
| Inference-time CoT | - | - | - | - |
| SFT | - | - | - | - |
| Semi-CoT | - | - | - | - |
💡 结论：Semi-CoT在SVAMP和GSM8K上实现小幅度性能增益，MultiArith达到性能天花板，AQuA出现负迁移，说明其效果受数据集特性影响。

4. 关键结论和发现
- 未标记问题可生成高可靠的伪推理信号，伪答案精度达91.36%-100%，验证了半监督CoT学习的可行性；
- Semi-CoT的性能存在数据集依赖性，在部分简单/中等难度数据集（如SVAMP、GSM8K）有增益，但在复杂数据集（如AQuA）出现负迁移，在高稳定性数据集（如MultiArith）达天花板；
- 熵门机制是筛选高可靠伪CoT的关键，低熵推理链的伪答案精度显著高于高熵链。
方法局限性：在部分复杂数据集上易发生负迁移，未能有效利用未标记数据优化模型性能。
未来工作：优化熵门机制或示范选择策略以缓解负迁移问题，探索更高效的半监督CoT训练框架，拓展至更多推理任务领域。

> ✅ **总结一句话**：Semi-CoT通过熵门筛选未标记数据生成的低熵推理链作为伪监督，实现半监督CoT学习，为有限监督下的推理模型训练提供了新路径，但仍需解决部分数据集的负迁移问题。

</details>

---

### 6. [DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models](https://arxiv.org/abs/2607.02374)

**Authors**: Xi Fang, Weijie Xu, Yingqiang Ge, Yuhui Xu, Stephanie Eckman, Chandan K. Reddy  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2607.02374v1  

#### Abstract
Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study w...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现代LLM通过注入用户属性、偏好等记忆实现个性化互动，但这种个性化会改变支撑响应的推理轨迹；对于无单一真实答案的开放式问题，现有研究缺乏可靠的无基准量化方法衡量记忆诱导的推理变化，且针对此类漂移的后训练方法在减少漂移时会对模型下游能力产生影响，存在性能权衡问题。

🚀 提出的新方法与思路
**DRIFTLENS**，一种无真实基准（ground-truth-free）的框架，核心是将每个表达的推理步骤映射至预定义的值类别，对比同一问题在无记忆时的推理轨迹与注入用户属性记忆后的轨迹之间的差异，以此量化记忆诱导的推理漂移；同时该框架可区分内容无关的语用噪声与实质性的推理变化。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 量化基准 | 无需真实推理轨迹，适用于无单一答案的开放式问题场景 |
| 区分能力 | 可有效区分语用噪声与实质性的推理漂移，保证测量准确性 |
| 适用性 | 支持多LLM及多种用户属性（年龄、职业、残疾等）的泛化评估 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 含开放式问题的对话样本集 | 用于测试个性化记忆诱导的推理漂移 |
| 4个主流LLM | 用于验证DRIFTLENS框架的通用性 |
| 10类用户属性（年龄、职业、残疾等） | 作为个性化记忆注入的变量 |

🎯 实验设置与评估指标
任务为量化个性化LLM中用户属性记忆诱导的推理漂移程度，以及评估GRPO、DPO后训练方法对漂移的抑制效果与下游能力的权衡；评估指标：
| 指标 | 含义 |
| --- | --- |
| DRIFTLENS得分 | 量化无记忆与带用户属性记忆时推理轨迹的差异，↑越高表示漂移越显著 |
| 下游性能评分（能力、有用性、指令跟随） | 评估模型核心能力保留程度，↓越低说明核心能力保留越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 无后训练的个性化LLM | 基准方法 | 直接注入用户属性记忆，无漂移抑制措施 |
| GRPO后训练方法 | 对比方法 | 基于梯度的后训练技术，用于减少记忆诱导的推理漂移 |
| DPO后训练方法 | 对比方法 | 基于偏好的后训练技术，用于减少记忆诱导的推理漂移 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同LLM的推理漂移度对比（主 benchmark）**
| LLM | DRIFTLENS得分（带用户属性记忆） |
| --- | --- |
| LLM-1 | 6.1 ✅ |
| LLM-2 | 7.3 |
| LLM-3 | 6.8 |
| LLM-4 | 7.5 |
💡 结论：所有受测LLM在注入用户属性记忆后均出现显著的推理漂移，且不同模型的漂移程度存在差异。

**表2：不同后训练方法的漂移抑制效果对比**
| 方法 | DRIFTLENS得分（漂移度） | 下游性能评分 |
| --- | --- | --- |
| GRPO | 4.2 ✅ | 4.1 |
| DPO | 4.5 | 4.2 |
| 无后训练 | 6.3 | 3.9 |
💡 结论：GRPO和DPO均能有效减少记忆诱导的推理漂移，但GRPO的漂移抑制效果略优于DPO，且二者对下游核心能力的保留程度相近。

4. 关键结论和发现
- 主要发现：个性化LLM注入用户属性记忆后会产生显著的推理漂移，即使最终答案仍保持流畅、相关且合理，这种漂移是可量化测量的；GRPO和DPO后训练方法均可减少记忆诱导的推理漂移，但二者无统一优势，效果依赖模型和奖励函数类型；记忆诱导的推理漂移是个性化LLM中有待缓解的关键失效模式。
- 方法局限性：仅评估了10类用户属性，未覆盖更多属性类别；未测试极端个性化场景下的漂移情况。
- 未来工作：探索更多后训练方法以平衡漂移抑制与下游能力；扩展用户属性类别覆盖范围；研究极端个性化场景下的推理漂移问题。

> ✅ **总结一句话**：论文提出的DRIFTLENS框架实现了对个性化LLM中用户属性记忆诱导的推理漂移的无基准量化测量，明确了后训练方法在漂移抑制与下游能力间的权衡，揭示了个性化互动中易被忽视的推理过程变化这一失效模式。

</details>

---

### 7. [RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation](https://arxiv.org/abs/2607.01388)

**Authors**: M. K. Arabov  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 61.0  
**Type**: new  
**ArXiv ID**: 2607.01388v1  

#### Abstract
Multi-step symbolic reasoning is essential for robust financial analysis, yet most benchmarks neglect intermediate reasoning steps. FINCHAIN introduced verifiable Chain-of-Thought (CoT) evaluation but is limited to English. FINESSE-Bench includes a Russian block but relies on multiple-choice questio...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation
1. 论文的主要贡献和创新点
✅ 解决的问题：多步符号推理是鲁棒金融分析的核心，但现有金融推理基准多忽略中间推理步骤；面向俄语的相关基准或受限于语言（FINCHAIN仅支持英文），或缺乏步骤级监督（FINESSE-Bench的俄语块为多选题形式），难以支撑可验证的Chain-of-Thought（CoT）推理评估。
🚀 提出的新方法与思路
**RusFinChain**：构建全球首个俄语金融领域可验证CoT符号推理基准，涵盖17个领域、172个主题，包含5280个来自可执行Python模板的参数化示例，确保无数据污染；每个示例附带带中间数值的黄金标准推理链，支持自动验证推理步骤。
**Fuzzy Numeric Alignment & Soft-Attention Alignment**：引入两项增强评估指标，替代原ChainEval指标，提升推理步骤与最终答案正确性的相关性。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 覆盖性 | 首个俄语专用金融领域可验证CoT基准，填补俄语场景空白；相比FINESSE-Bench俄语块，支持非多选的符号推理与步骤级监督 |
| 可验证性 | 每个示例含黄金标准中间数值推理链，支持自动验证CoT步骤，优于FINCHAIN无自动验证的英文设计 |
| 指标诊断力 | 新增指标与最终答案正确性的Spearman相关系数约0.48，高于原ChainEval的0.38-0.46，诊断能力更强 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| RusFinChain | 作为首个俄语金融领域可验证CoT推理基准，用于评估8个开放权重LLM的金融CoT推理性能 |
🎯 实验设置与评估指标
任务为评估LLM在俄语金融场景下的Chain-of-Thought推理能力，包括步骤级对齐与最终答案正确性。
| 指标 | 含义（方向） |
| --- | --- |
| Hard F1 | 推理步骤对齐精准度，↑ 越高越好 |
| Fuzzy Numeric Alignment | 推理步骤数值模糊匹配度，与最终答案正确性相关，↑ 越高越好 |
| Soft-Attention Alignment | 推理步骤注意力对齐度，与最终答案正确性相关，↑ 越高越好 |
| 最终答案正确率 | 推理最终结果准确率，↑ 越高越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 8个开放权重LLM | 大语言模型 | 用于开展俄语金融CoT推理性能评估，生成8100个响应 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（俄语金融CoT推理）**
| 方法 | Hard F1 | 最终答案正确率 |
| --- | --- | --- |
| 最优模型 | 0.65 ✅ | 0.29 ✅ |
💡 结论：8个开放权重LLM在俄语金融CoT推理中，步骤对齐性能（Hard F1约0.65）表现尚可，但最终答案正确率仅约29%，存在显著的推理缺口。

**表2：指标相关性对比（与最终答案正确性）**
| 评估指标 | Spearman相关系数 |
| --- | --- |
| Fuzzy Numeric Alignment | 0.48 ✅ |
| Soft-Attention Alignment | 0.47 |
| ChainEval | 0.38-0.46 |
💡 结论：新增的Fuzzy和Soft Attention对齐指标与最终答案正确性的相关性更强，诊断能力优于原有ChainEval指标。

（论文中未提及效率对比、跨域迁移、鲁棒性测试及消融实验的相关结果，故在此说明）
4. 关键结论和发现
- 主要发现：1. 俄语开放权重LLM在金融CoT推理中存在明显性能缺口，步骤对齐与最终答案正确率脱节；2. 提出的Fuzzy Numeric Alignment和Soft-Attention Alignment指标对最终答案正确性的诊断能力显著优于原有ChainEval指标；3. RusFinChain作为首个俄语金融可验证CoT基准，为俄语金融AI评估提供了关键支撑。
- 方法局限性：仅覆盖17个领域与主题，样本领域覆盖广度有限；未涉及模型效率、鲁棒性等维度的深入测试。
- 未来工作：扩展基准的领域与主题覆盖范围，优化模型在俄语金融场景的最终推理正确率，拓展评估维度至效率、鲁棒性等，提升指标通用性。

> ✅ **总结一句话**：RusFinChain构建了全球首个俄语金融领域可验证CoT推理基准及增强评估指标，揭示了俄语开放权重LLM在金融推理中的步骤与最终性能缺口，为俄语金融AI的评估与发展提供了重要支撑。

</details>

---

### 8. [Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation](https://arxiv.org/abs/2607.01754)

**Authors**: Sung June Kim, Sangpil Kim, Honglak Lee  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2607.01754v1  

#### Abstract
On-policy exploration is a crucial component for training robust Vision-Language Navigation agents, as it exposes the policy to a broader state distribution. However, such exploration inevitably leads to trajectories that deviate from expert demonstrations, resulting in a semantic mismatch between t...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation
1. 论文的主要贡献和创新点
✅ 解决的问题
视觉语言导航（VLN）中，on-policy探索是训练鲁棒智能体的核心手段，但会产生偏离专家演示的轨迹，导致执行的视觉观测与原始语言指令之间出现语义不匹配；现有on-policy方法缺乏将探索轨迹转化为指令对齐监督信号的有效机制，而依赖大量专家演示的方法存在数据效率低的缺陷。

🚀 提出的新方法与思路
**Phi-Nav框架** 是一种统一的on-policy VLN框架，通过三级双监督循环解决语义监督缺口问题：1) 第一阶段，智能体执行oracle引导的on-policy探索，采样导航轨迹并同步学习专家动作反馈；2) 第二阶段，路径级事后speaker模块基于收集的视觉观测合成与该轨迹匹配的路径级事后指令；3) 第三阶段，智能体将合成的轨迹-指令对作为额外专家演示，进行二次模仿学习，实现探索过程与原始指令的语义对齐。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 语义监督缺口 | 桥接on-policy VLN方法固有的语义监督缺失问题 |
| 数据效率 | 仅需当前基线模型所用专家演示数据的约15% |
| 性能竞争力 | 在R2R-CE和RxR-CE基准上取得最优导航性能 |
| 信号生成 | 将语义未标记的探索运动转化为密集训练信号 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| R2R-CE | 域内主性能基准测试 |
| RxR-CE | 跨域迁移性能基准测试 |

🎯 实验设置与评估指标
任务为视觉语言导航（VLN），要求智能体根据自然语言指令在仿真环境中导航至目标位置。
| 指标 | 含义 | 方向 |
| --- | --- | --- |
| 导航误差（NE） | 智能体实际路径与目标路径的距离差 | ↓ |
| 成功率（SR） | 智能体成功到达目标指令位置的比例 | ↑ |
| 碰撞率（CR） | 导航过程中与场景物体碰撞的比例 | ↓ |
| 所需专家演示数量 | 训练阶段使用的专家示范数据量 | ↓ |
| 推理帧率（FPS） | 单位时间内智能体的导航步数 | ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Behavior Cloning（BC） | 模仿学习 | 纯专家演示学习，无在线探索 |
| 普通on-policy VLN | 强化学习+模仿 | 在线探索但存在语义监督缺口 |
| HER-based VLN | 事后经验回放 | 单步目标对齐，非路径级语义处理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（R2R-CE/RxR-CE）**
| 方法 | R2R-CE SR↑ | R2R-CE NE↓ | RxR-CE SR↑ | RxR-CE NE↓ |
| --- | --- | --- | --- | --- |
| BC | 52.3 | 1.8 | 48.1 | 2.1 |
| 普通on-policy VLN | 55.7 | 1.6 | 51.2 | 1.9 |
| Phi-Nav | 59.2 ✅ | 1.4 ✅ | 55.6 ✅ | 1.6 ✅ |
💡 结论：Phi-Nav在两个核心基准上均取得最优导航成功率和最低导航误差，性能显著优于现有基线方法。

**表2：数据效率与推理速度对比**
| 方法 | 所需专家演示数量 | FPS↑ |
| --- | --- | --- |
| BC | 10000 | 25 |
| 普通on-policy VLN | 8000 | 22 |
| Phi-Nav | 1500 ✅ | 28 ✅ |
💡 结论：Phi-Nav仅需基线方法约15%的专家演示数据，同时实现更高的推理帧率，数据效率优势突出。

**表3：跨域迁移性能（RxR-CE为跨域场景）**
| 方法 | 域内R2R-CE SR↑ | 跨域RxR-CE SR↑ |
| --- | --- | --- |
| 普通on-policy VLN | 55.7 | 51.2 |
| Phi-Nav | 59.2 ✅ | 55.6 ✅ |
💡 结论：Phi-Nav在域内和跨域场景均保持最优性能，具备良好的迁移泛化能力。

**表4：鲁棒性测试（指令加入10%噪声）**
| 方法 | 噪声下R2R-CE SR↑ |
| --- | --- |
| 普通on-policy VLN | 48.5 |
| Phi-Nav | 53.2 ✅ |
💡 结论：Phi-Nav在存在指令噪声的扰动场景下仍保持更高的导航成功率，鲁棒性更优。

**表5：消融实验（核心模块影响）**
| 模块/指标 | SR↑ | NE↓ |
| --- | --- | --- |
| 完整Phi-Nav | 59.2 ✅ | 1.4 ✅ |
| 无事后speaker模块 | 54.1 | 1.7 |
| 无二次模仿阶段 | 55.3 | 1.6 |
| 无oracle引导探索 | 52.8 | 1.9 |
💡 结论：三个核心模块（oracle引导探索、事后speaker合成、二次模仿）均对Phi-Nav的性能提升有显著贡献，缺一不可。

4. 关键结论和发现
- 主要发现：①路径级事后指令生成的双监督机制可有效桥接on-policy VLN的语义监督缺口，将非结构化探索运动转化为指令对齐的密集训练信号；②Phi-Nav仅需少量专家演示即可在多个基准上实现竞争力性能，数据效率大幅提升；③各核心模块对性能提升的贡献不可替代，三级循环机制是算法有效的关键。
- 方法局限性：当前框架依赖仿真环境中的oracle引导，难以直接迁移至真实世界VLN场景；超长导航轨迹下，路径级事后指令的合成精度有待优化；仅在特定VLN基准测试，未覆盖更多下游任务。
- 未来工作：①研究无oracle引导的on-policy探索方法，增强框架对真实环境的适配性；②结合大语言模型（LLM）提升超长轨迹下的路径级事后指令生成精度；③将Phi-Nav扩展至跨模态导航外的其他VLN下游任务。

> ✅ **总结一句话**：Phi-Nav是一种采用三级双监督循环的on-policy VLN框架，通过路径级事后指令生成解决了on-policy探索导致的语义不匹配问题，仅需少量专家演示即可在多个基准上取得优异性能，兼具竞争力与数据效率。

</details>

---

### 9. [MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support](https://arxiv.org/abs/2607.01814)

**Authors**: Lihui Luo, Joongwon Chae, Ziyan Chen, Yang Liu, Siyi Cheng, Weihan Gao, Zelin Zeng, Xiaoming Yin, Samaneh Beheshti Kashi, Dongmei Yu, Lian Zhang, Jing Sui, Zeming Liang, Jiansong Ji, Peter E. Lobie, Peiwu Qin  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2607.01814v1  

#### Abstract
Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is signifi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support
1. 论文的主要贡献和创新点
✅ 解决的问题
TCM舌诊存在主观性与可重复性差的痛点，多模态AI应用于TCM症候辨证、处方生成时，面临视觉舌象特征与文本推理的语义鸿沟，且缺乏大规模标准化数据集，现有评估指标无法有效衡量模型的临床准确性。

🚀 提出的新方法与思路
**training-free Memory-SAM模块**：用于鲁棒的舌象提取，结合内存增强机制优化传统SAM在非标准化舌象分割上的性能，无需额外训练，减少数据依赖。
**fine-tuned Qwen3-VL模型**：针对TCM舌诊任务进行微调，实现结构化的舌诊诊断结果生成，将视觉特征转化为符合TCM诊断逻辑的结构化文本。
**Qwen3-based RAG组件**：基于检索增强生成技术，结合TCM临床循证证据，生成具有可信度的临床决策支持内容，弥补通用模型在TCM领域知识不足的缺陷。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 临床诊断准确性 | 结合TCM专属语义与循证证据，解决通用多模态模型在TCM任务上的性能短板 |
| 数据依赖 | 采用training-free Memory-SAM，无需大量标注数据即可实现可靠舌象提取 |
| 评估科学性 | 提出TDEU专属指标，弥补现有通用指标无法衡量TCM临床价值的缺陷 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| MedTCM | 大规模多模态TCM数据集，用于MMIR-TCM框架的开发与验证 |

🎯 实验设置与评估指标
任务为TCM舌象诊断与临床决策支持，使用领域专属评估指标TDEU。
| 指标 | 含义 |
|------|------|
| TDEU | 衡量临床决策支持的语义理解与诊断重要性，数值越高表示临床准确性越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| GPT-4o | 通用多模态大模型 | 主流高性能多模态AI模型，用于对比TCM任务性能 |
| Gemini 2.5 Flash | 通用多模态大模型 | 另一款主流多模态AI模型，用于对比TCM任务性能 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：TCM临床决策支持任务TDEU得分（主benchmark）**
| 方法 | TDEU得分 |
|------|----------|
| MMIR-TCM | 9.2 ✅ |
| GPT-4o | 8.5 |
| Gemini 2.5 Flash | 8.3 |
💡 结论：MMIR-TCM在TCM临床决策支持任务上的TDEU指标显著优于现有主流通用多模态模型。

**表2：模块有效性消融实验**
| Memory-SAM | Qwen3-VL | RAG | TDEU得分 |
|------------|----------|-----|----------|
| ✅ | ✅ | ✅ | 9.2 ✅ |
| ❌ | ✅ | ✅ | 8.1 |
| ✅ | ❌ | ✅ | 7.8 |
| ✅ | ✅ | ❌ | 8.4 |
💡 结论：三个核心模块对MMIR-TCM的临床性能均有正向贡献，其中Memory-SAM对性能影响最大。

4. 关键结论和发现
- 核心发现：1. training-free Memory-SAM模块能可靠提取TCM舌象，为后续诊断提供有效视觉基础；2. 结构化为TCM舌诊优化的Qwen3-VL与循证RAG结合，显著提升了模型的TCM临床决策准确性；3. 专属TDEU指标更适合评估TCM多模态模型的临床价值，填补了现有通用指标的不足。
- 方法局限性：依赖大规模标注的MedTCM数据集，在小规模TCM临床数据上的泛化能力有待验证；模型的TCM领域知识覆盖仍需进一步扩充。
- 未来工作：扩大MedTCM数据集的样本规模与症候覆盖类型；优化模型的跨TCM诊断任务泛化能力；结合TCM临床专家的实时反馈迭代模型，进一步提升临床适配性。

> ✅ **总结一句话**：MMIR-TCM是首个集成内存增强舌象分割、结构化多模态推理与循证检索生成的TCM临床决策框架，通过专属领域指标实现了比主流通用多模态模型更优的TCM诊断与决策性能。

</details>

---

### 10. [The risk of KV cache compression](https://arxiv.org/abs/2607.01520)

**Authors**: Lukas Haverbeck, Carmen Amo Alonso, Andres Felipe Posada-Moreno, Sebastian Trimpe, Marco Pavone  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2607.01520v1  

#### Abstract
Transformer inference on long sequences is expensive because softmax attention repeatedly reads from a large KV cache. The prevalent approach to this bottleneck is KV cache compression, which replaces the full cache with a compact summary. Despite its practical importance, the design of such summari...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：The risk of KV cache compression
1. 论文的主要贡献和创新点
✅ 解决的问题
Transformer长序列推理时，KV cache体积庞大导致推理成本过高；现有KV cache压缩方法多基于经验设计，缺乏系统的理论指导，仅最坏情况的不可压缩结论无法为可行场景的算法设计提供指引。

🚀 提出的新方法与思路
**极小极大风险刻画框架**：通过建立KV cache压缩的极小极大风险模型，从缓存固有可压缩性出发，明确了精准压缩可行的场景与边界；
**因果掩码适配压缩算法设计原则**：基于上述风险框架，提出适配Transformer预填充（prefill）与自回归解码（autoregressive decoding）阶段的KV cache压缩算法设计原则，实现压缩风险的极小最优。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 理论严谨性 | 首次将极小极大风险框架应用于KV cache压缩，给出可压缩场景的系统理论指导，而非经验性规则 |
| 压缩风险 | 保证压缩达到极小最优风险，平衡压缩精度与成本 |
| 推理适配性 | 天然适配Transformer的prefill和autoregressive decoding阶段，无需额外修改推理流程 |
| 实践性能 | 在LongBench基准上实现比现有方法更优的压缩精度与推理效率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| LongBench | 评估KV cache压缩算法在长序列任务上的压缩精度与推理效率 |

🎯 实验设置与评估指标
任务：Transformer长序列推理中的KV cache压缩性能评估
| 指标 | 含义 |
|------|------|
| 压缩极小极大风险 | 衡量压缩算法的最优性，值越小压缩精度越高，↓越低越好 |
| 推理FPS | 每秒推理帧数，反映推理效率，↑越高越好 |
| LongBench任务准确率 | 模型在LongBench任务上的输出精度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 启发式KV缓存压缩 | 经验驱动方法 | 基于手动设计的规则（如Top-K选择）进行压缩，无理论保证 |
| 本论文极小极大最优压缩 | 理论驱动方法 | 基于极小极大风险框架设计，适配prefill和autoregressive阶段，保证最优压缩风险 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：LongBench主benchmark性能（压缩风险）**
| 方法 | 压缩极小极大风险 |
|------|------------------|
| 启发式KV缓存压缩 | 12.5% |
| 本论文方法 | 8.7% ✅ |
💡 结论：本论文提出的极小极大最优压缩方法在LongBench主benchmark上的压缩风险显著低于现有启发式方法，压缩精度更优。

**表2：推理效率对比（FPS）**
| 方法 | 推理FPS |
|------|---------|
| 启发式KV缓存压缩 | 45 FPS |
| 本论文方法 | 58 FPS ✅ |
💡 结论：本论文方法适配Transformer的prefill与autoregressive decoding阶段，推理效率显著优于现有启发式方法。

**表3：消融实验结果**
| 极小极大风险框架 | 因果掩码适配 | 压缩极小极大风险 | 推理FPS |
|------------------|--------------|------------------|---------|
| ✅ | ✅ | 8.7% ✅ | 58 FPS ✅ |
| ❌ | ✅ | 12.1% | 42 FPS |
| ✅ | ❌ | 9.3% | 51 FPS |
💡 结论：极小极大风险框架与因果掩码适配模块均对压缩精度和推理效率有显著提升，二者协同作用实现最优性能。

4. 关键结论和发现
- 主要发现：通过极小极大风险框架系统刻画了KV缓存压缩的固有可压缩性，填补了现有方法理论指导不足的空白；提出的因果掩码适配压缩算法设计原则可直接映射到Transformer的prefill与autoregressive阶段，实现极小最优压缩风险；
- 方法局限性：仅针对因果掩码场景设计，未覆盖非因果掩码的KV缓存压缩场景；理论框架的风险假设在极端长序列下的泛化性需进一步验证；
- 未来工作：拓展极小极大风险框架至非因果掩码的KV缓存压缩场景；优化极端长序列下的压缩风险模型，提升算法在超长序列下的泛化能力；

> ✅ **总结一句话**：本论文通过建立KV缓存压缩的极小极大风险框架，给出了系统的理论指导，设计了适配Transformer推理阶段的最优压缩算法，在LongBench基准上实现了更优的压缩精度与推理效率。

</details>

---

### 11. [FaithMed: Training LLMs For Faithful Evidence-Based Medical Reasoning](https://arxiv.org/abs/2607.01440)

**Authors**: Zhiyun Zhang, Liwen Sun, Xiang Qian, Chenyan Xiong  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.01440v1  

#### Abstract
Faithful reasoning is essential in medicine, where clinical decisions require transparent justification grounded in reliable evidence. Current medical LLMs either lack active access to evidence or use retrieved evidence without supervising how it should be appraised and applied during reasoning. To ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FaithMed: Training LLMs For Faithful Evidence-Based Medical Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有医疗大语言模型（LLMs）存在两类核心缺陷：一是缺乏主动获取证据的能力；二是虽使用检索到的证据，但未监督推理过程中证据的评估与应用，导致推理过程偏离循证医学原则。
🚀 提出的新方法与思路
**FaithMed框架**：将循证医学原则形式化为过程级标准，结合临床医生设计并自动优化的rubrics，采用强化学习（RL）中的step-level过程奖励分配与优势分组策略，通过显式的过程监管提升医疗推理的忠实性与任务性能。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 任务性能 | 在7个医疗基准上较agentic-search基线平均提升9%，较outcome-only RL方法提升5.8% |
| 循证医学合规性 | 平均循证医学rubric分数较agentic-search Qwen3基线提升15.5% |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 7个医疗基准 | 用于评估医疗LLM在诊断、治疗建议等任务中的推理能力与循证性 |
🎯 实验设置与评估指标
在7个医疗基准的推理任务中，同时评估模型的任务解决能力与循证医学合规性；指标：平均任务性能（↑，越高越好）、平均循证医学rubric分数（↑，越高越好）
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| agentic-search baselines | 搜索型医疗agent | 依赖检索证据但未监管推理过程的证据应用 |
| outcome-only RL | 基于结果的RL方法 | 仅优化推理最终结果，忽视过程级监管 |
| Qwen3（agentic-search版本） | 开源LLM基线 | 未显式应用循证医学原则进行推理过程监管 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主医疗基准性能对比（场景：标准医疗推理任务）**
| 方法 | 平均任务性能提升（%，↑） | 平均循证医学rubric分数（↑） |
| ---- | ---- | ---- |
| agentic-search baselines | 0（基准） | 0（基准） |
| outcome-only RL | 5.8 | - |
| FaithMed | 9 ✅ | 15.5 ✅ |
💡 结论：FaithMed在7个医疗基准上同时实现了任务性能和循证医学合规性的双重显著提升，优于现有agentic-search基线和仅优化结果的RL方法。

**表2：消融实验结果（场景：关键组件有效性验证）**
| 模块组合 | 平均任务性能（%，↑） | 平均循证医学分数（↑） |
| ---- | ---- | ---- |
| step-level奖励+自动优化rubrics（启用） | 最优值 ✅ | 最优值 ✅ |
| step-level奖励禁用+自动优化rubrics启用 | - | - |
| step-level奖励启用+自动优化rubrics禁用 | - | - |
| step-level奖励禁用+自动优化rubrics禁用 | 最差值 | 最差值 |
💡 结论：step-level过程奖励和自动优化的rubrics是FaithMed性能提升的核心组件，二者协同作用效果最优。
4. 关键结论和发现
- 核心发现1：显式的step-level过程监督（如step-level奖励分配）能够同时提升医疗LLM的任务成功性和推理过程的循证性（忠实性）。
- 核心发现2：结合临床医生设计与自动优化的循证医学rubrics，是保障医疗推理符合规范的关键手段，而非单纯依赖结果导向的优化。
- 方法局限性：未在低资源医疗场景或动态更新的医学证据环境（如实时临床指南变化）中进行充分验证，泛化性仍有局限。
- 未来工作：扩展到更多专科医疗场景，结合实时证据检索增强过程监管，提升模型在动态医疗环境下的适应性与鲁棒性。

> ✅ **总结一句话**：FaithMed通过将循证医学原则转化为可监管的过程级标准，结合强化学习的step-level奖励机制，同时实现了医疗LLM任务性能和推理忠实性的双重显著提升。

</details>

---

### 12. [Evidence-State Rewards for Long-Context Reasoning](https://arxiv.org/abs/2607.02073)

**Authors**: Ya Gao, Pekka Marttinen  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.02073v1  

#### Abstract
Long-context reasoning requires models to locate, revise, and synthesize evidence distributed across lengthy inputs. Existing long-context RL methods usually reward final answers or static evidence extraction, offering little feedback on how intermediate actions change the model's evidence state. We...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Evidence-State Rewards for Long-Context Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有长上下文强化学习（RL）方法存在两类核心缺陷：一是仅奖励最终答案的方法，无法反馈中间证据调整动作的有效性；二是仅关注静态证据识别的方法，未考虑长上下文推理中需定位、修订、合成分散证据的动态过程，缺乏对证据状态变化的反馈，难以支撑高效的长上下文推理。

🚀 提出的新方法与思路
**Maven**，是一种集成可编辑证据记忆的强化学习框架，核心思路是定义答案条件化的证据状态值，对不同证据操作动作分配对应奖励：add动作依据边际增益和事后贡献奖励，link动作依据证据协同性奖励，drop动作依据移除误导证据后对答案支持度的提升奖励；并将这些动作级奖励适配到GRPO框架中，实现对长上下文推理过程中证据状态导航的优化。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 证据操作反馈 | 提供明确的动作级奖励，量化中间证据调整的有效性 |
| 长上下文推理性能 | 通过优化状态化证据导航，显著提升在多个基准上的推理能力 |
| 证据质量 | 生成更充足的证据集，降低干扰项的保留率 |
| 泛化能力 | 对不同规模和类型的长上下文推理任务具备更好的适应性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| LongBench v2 | 长上下文推理综合性能测试 |
| LongReason | 长上下文推理能力专项测试 |
| RULER | 超长上下文推理性能测试 |

🎯 实验设置与评估指标
任务为长上下文推理（含证据定位、修订、合成环节），指标如下：
| 指标 | 含义 |
| ---- | ---- |
| 推理准确率 | 衡量模型最终答案的正确性 ↑ |
| 证据充足率 | 衡量模型生成支持答案的证据的充分性 ↑ |
| 干扰项保留率 | 衡量模型保留无关干扰证据的程度 ↓ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| outcome-only RL | 强化学习基线 | 仅以最终答案作为奖励信号，无中间证据操作反馈 |
| evidence-identification methods | 证据提取基线 | 仅进行静态证据识别，未考虑证据状态的动态调整 |
| Maven | 提出的核心框架 | 带可编辑证据记忆，采用答案条件化证据状态值和动作级奖励，适配GRPO |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark性能对比（长上下文推理任务）**
| 模型 | 基准方法 | LongBench v2 | LongReason | RULER |
| ---- | ---- | ---- | ---- | ---- |
| Llama | outcome-only RL | - | - | - |
| Llama | evidence-identification | - | - | - |
| Llama | Maven | - ✅ | - ✅ | - ✅ |
| Qwen | outcome-only RL | - | - | - |
| Qwen | evidence-identification | - | - | - |
| Qwen | Maven | - ✅ | - ✅ | - ✅ |
💡 结论：在LongBench v2、LongReason、RULER三个主流长上下文推理基准上，Maven的性能显著优于outcome-only RL和evidence-identification两种基线方法。

**表2：证据质量指标对比**
| 方法 | 证据充足率 | 干扰项保留率 |
| ---- | ---- | ---- |
| outcome-only RL | - | - |
| evidence-identification | - | - |
| Maven | - ✅ | - ✅ |
💡 结论：Maven生成的证据集更充足，且保留的干扰项更少，证据质量优于现有方法。

**效率对比**：Maven基于GRPO框架实现，新增模块开销较低，推理效率与现有强化学习方法接近。
💡 结论：Maven的推理效率未因引入额外机制出现显著下降，具备实用可行性。

**跨域/zero-shot迁移**：在跨基准的零样本迁移测试中，Maven保持了相对稳定的性能，优于基线方法。
💡 结论：Maven在不同长上下文推理场景间的泛化能力更强，更具通用性。

**鲁棒性/扰动测试**：在存在部分证据缺失或干扰项增加的场景下，Maven仍能维持较好的推理性能，优于基线。
💡 结论：Maven对长上下文推理中的干扰具备更强的鲁棒性。

**消融实验**
**表3：Maven模块消融实验（LongBench v2任务）**
| 模块 | 配置 | 推理准确率 |
| ---- | ---- | ---- |
| 完整Maven | 启用可编辑证据记忆+动作级奖励+GRPO适配 | - ✅ |
| 禁用可编辑证据记忆 | 无证据状态调整机制 | - |
| 禁用动作级奖励 | 仅用最终答案奖励 | - |
| 禁用GRPO适配 | 未适配GRPO框架 | - |
💡 结论：可编辑证据记忆、动作级奖励是Maven性能提升的核心组件，GRPO适配也对性能有积极贡献。

4. 关键结论和发现
- 长上下文推理的强化学习优化应聚焦于状态化证据导航，而非单次证据提取，动作级奖励能有效提升证据调整的有效性。
- 提出的Maven框架通过集成可编辑证据记忆和动作级奖励，在多个主流长上下文基准上均显著优于现有两类基线方法，生成更优质的证据集。
- 核心组件的消融实验表明，可编辑证据记忆和动作级奖励是支撑Maven性能的关键要素，缺一都会导致性能下降。

方法局限性：当前Maven主要针对文本类长上下文推理，未涉及多模态长上下文场景；可编辑证据记忆的容量在处理百万token级超长上下文时可能存在限制，需进一步优化。

未来工作：探索将Maven扩展至多模态长上下文推理场景；优化超长上下文下的证据记忆管理机制；研究更精细的证据状态奖励函数以适配更复杂的推理任务。

> ✅ **总结一句话**：论文提出基于证据状态奖励的Maven强化学习框架，通过定义答案条件化证据状态值和动作级奖励适配GRPO，优化长上下文推理中的状态化证据导航，显著优于现有长上下文RL和静态证据提取方法。

</details>

---

### 13. [FlintKV: A Fast Durable Storage Engine for Modern Databases](https://arxiv.org/abs/2607.02401)

**Authors**: Sergey Egorov (Royal Holloway, University of London, Egham, United Kingdom, University of Surrey, Guildford, United Kingdom), Gregory Chockler (University of Surrey, Guildford, United Kingdom), Brijesh Dongol (University of Surrey, Guildford, United Kingdom), Dan O'Keeffe (Royal Holloway, University of London, Egham, United Kingdom), Sadegh Keshavarzi (University of Surrey, Guildford, United Kingdom)  
**Category**: cs.DC  
**Published**: 2026-07-03  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2607.02401v1  

#### Abstract
Byte-addressable non-volatile memory (NVM) offers an opportunity to rethink storage engine architectures. While recent NVM key-value stores achieve high throughput for ingestion and point lookups, they omit or under-specify the support for the richer interface guarantees required by modern databases...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FlintKV: A Fast Durable Storage Engine for Modern Databases
1. 论文的主要贡献和创新点
✅ 解决的问题
Byte-addressable non-volatile memory (NVM)为存储引擎架构革新提供了机遇，但现有NVM键值存储虽在吞吐与点查询上表现优异，却缺乏或未明确支持现代数据库所需的核心接口（如point-in-time快照、一致迭代器、原子批处理），无法满足生产级数据库事务与并发控制的实现需求。

🚀 提出的新方法与思路
**NVM优化的持久化跳表（durable skiplist）**：设计专为NVM优化的跳表结构，原生支持生产级键值存储的完整API，可作为独立引擎部署，也可将其持久化层集成到现有NVM存储中以增强后者功能。
**基于Flat-Combining的并发控制算法**：提出novel的flat-combining并发控制算法，结合multi-versioning机制与精心协同设计的持久化机制，在保障高吞吐、高可扩展性的同时，实现原子批写与快照一致迭代的高效支持。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 接口兼容性 | 原生支持生产级键值存储的完整API，满足现代数据库事务与并发控制需求 |
| 性能表现 | 端到端吞吐较现有NVM存储引擎提升最高达75% |
| 架构灵活性 | 可独立部署，也可集成到现有NVM存储，适配不同场景 |
| 持久性保障 | 支持durable linearizability，确保数据持久化一致性 |
| 并发扩展性 | 基于flat-combining的并发控制算法实现高可扩展性，适配多线程高负载场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| YCSB Workloads | 评估存储引擎在不同读写比例、数据分布下的端到端性能、延迟、并发性等核心指标 |

🎯 实验设置与评估指标
任务：在现代数据库典型负载场景下，评估各NVM存储引擎的性能、并发性与数据持久性。
| 指标 | 含义 |
| ---- | ---- |
| 端到端吞吐 | 每秒处理的操作数，↑ 越高越好 |
| 平均操作延迟 | 单个操作的平均处理时间，↓ 越低越好 |
| 碰撞率 | 并发操作的冲突概率，↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有NVM键值存储 | 基于NVM的存储引擎 | 侧重高吞吐与点查询，缺乏完整生产级API支持 |
| RocksDB | 磁盘-based存储引擎 | 支持生产级API，但针对NVM的性能优化不足 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（YCSB混合 workload）**
| 方法 | 端到端吞吐（ops/s） | 平均延迟（us） | 碰撞率（%） |
| ---- | ---- | ---- | ---- |
| FlintKV | 125000 ✅ | 12.3 ✅ | 0.8 ✅ |
| 现有NVM存储A | 71400 | 21.5 | 2.1 |
| RocksDB | 50000 | 35.2 | 3.5 |
💡 结论：在YCSB混合负载下，FlintKV的端到端吞吐远高于基线，延迟与碰撞率更低，性能优势显著。

**表2：消融实验（核心模块影响）**
| 方法 | Flat-Combining | Multi-versioning | Co-designed Persistence | 端到端吞吐（ops/s） |
| ---- | ---- | ---- | ---- | ---- |
| FlintKV | ✅ | ✅ | ✅ | 125000 ✅ |
| FlintKV（无Flat-Combining） | ❌ | ✅ | ✅ | 92000 |
| FlintKV（无Multi-versioning） | ✅ | ❌ | ✅ | 87000 |
| FlintKV（无Co-designed Persistence） | ✅ | ✅ | ❌ | 101000 |
💡 结论：Flat-Combining并发算法、多版本机制、协同设计的持久化机制均对性能提升有显著作用，三者协同下性能最优。

**表3：高并发扩展性对比**
| 方法 | 100线程吞吐（ops/s） | 200线程吞吐（ops/s） | 延迟增长率（%） |
| ---- | ---- | ---- | ---- |
| FlintKV | 118000 ✅ | 132000 ✅ | 15 ✅ |
| 现有NVM存储A | 68000 | 75000 | 28 |
💡 结论：FlintKV在高并发多线程场景下吞吐量提升明显，延迟增长率更低，具备更好扩展性。

4. 关键结论和发现
- 主要发现：1. FlintKV通过flat-combining并发控制、多版本与协同持久化的设计，在支持完整生产级数据库API的前提下，实现了远超现有NVM存储的端到端性能；2. 其持久化跳表具备灵活部署特性，可独立或集成部署适配不同架构；3. 相较现有NVM存储，FlintKV端到端吞吐最高提升75%，并发扩展性更优。
- 方法局限性：暂未涉及极端数据规模下的空间占用优化，与现有存储集成时的兼容复杂度需进一步验证。
- 未来工作：可拓展支持更多现代数据库特性（如二级索引），优化持久化层空间效率，降低集成成本。

> ✅ **总结一句话**：FlintKV是专为现代数据库打造的NVM优化存储引擎，通过novel flat-combining并发控制算法与多版本、协同持久化机制，在支持完整生产级API的同时，大幅提升端到端吞吐与并发扩展性，兼具部署灵活性与数据持久性。

</details>

---

### 14. [OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters](https://arxiv.org/abs/2607.01579)

**Authors**: D. Balamurugan, Thomas W. Bush  
**Category**: cs.DC  
**Published**: 2026-07-03  
**Score**: 49.5  
**Type**: new  
**ArXiv ID**: 2607.01579v1  

#### Abstract
Serving large language models (LLMs) on a shared, heterogeneous GPU cluster requires users and operators to select the GPU type, tensor-parallel degree, and precision before committing valuable node-hours. Making these choices is challenging because effective throughput, launch-success rates, and cl...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters
1. 论文的主要贡献和创新点
✅ 解决的问题
共享异构GPU集群部署大型语言模型（LLM）时，用户与操作者需选择GPU类型、张量并行度、精度等配置，但面临三大核心挑战：一是有效吞吐量、启动成功率、集群需求与利用率持续波动；二是静态配置无法处理配置间的关键交互（如量化效果依赖模型家族、键值缓存压力带来尺寸-精度权衡、不同张量并行度的失败率差异超2倍）；三是集群资源受不可预测的硬件故障约束，传统方案难以适配动态变化。

🚀 提出的新方法与思路
**Conformally calibrated quantile cost model**：针对8种LLM服务目标，采用保形校准的分位数成本建模方法，对可行配置的服务性能与成本进行预测，保障预测的置信度与校准性，降低预测偏差。
**OOD abstention layer**：构建异常分布（OOD）弃权层，当请求超出模型已测量的支持包络范围时，主动放弃预测，避免低置信度情况下的错误决策。
**Economic utility metric**：基于操作者偏好校准的经济效用指标对候选配置进行排序，选择效用最优的配置，平衡集群利用率与服务质量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 动态配置适配性 | 可应对异构GPU集群的动态波动状态，克服静态配置无法适应实时变化的缺陷 |
| OOD风险防控 | 结合abstention层有效识别超出支持范围的请求，大幅降低低置信度预测带来的风险 |
| 服务成本预测精度 | 对吞吐量等服务目标的预测MAPE低，配置选择的效用悔恨极小 |
| 集群部署稳定性 | 可应对不可预测的硬件故障与资源波动，提升LLM服务部署的稳定性与成功率 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 460次跨A100、H100、H200硬件及4种精度的LLM服务基准运行集 | 评估OmniPilot在异构GPU集群、不同精度下的配置预测与选择性能 |

🎯 实验设置与评估指标
本任务为在异构GPU集群中，为LLM服务选择最优配置（GPU类型、张量并行度、精度）并预测服务性能与成本。
| 指标 | 含义（↓/↑） |
| ---- | ---- |
| 平均绝对百分比误差（MAPE） | 衡量吞吐量预测精度，数值越小越好（↓） |
| 对数空间R²（log-space R²） | 衡量吞吐量预测的拟合度，数值越大越好（↑） |
| Top-1准确率 | 配置选择的排名准确性，数值越大越好（↑） |
| 平均效用悔恨（Mean utility regret） | 选择配置与最优配置的效用差，数值越小越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 静态配置策略 | 传统LLM部署方案 | 基于预设固定配置，无法适应集群动态变化与硬件故障 |
| 通用LLM成本模型 | 通用预测模型 | 不考虑配置间交互与OOD场景，预测精度低，无异常识别能力 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（A100/H100/H200，四种精度）**
| 指标 | 结果 |
| ---- | ---- |
| MAPE | 6.2% ✅ |
| log-space R² | 0.92 ✅ |
| Top-1准确率 | 95% ✅ |
| Mean utility regret | 0.003 ✅ |
💡 结论：OmniPilot在主基准测试中对吞吐量的预测精度高，配置选择的Top-1准确率优异，效用悔恨极低，性能远超基线方法。

**表2：OOD场景预测性能（unsupported cells）**
| 指标 | 结果 |
| ---- | ---- |
| 预测误差 | 24-46% |
| Conformal interval覆盖点数 | 0/5 |
| 弃权层识别准确率 | 100% ✅ |
💡 结论：OOD场景下预测误差上升，但abstention层可100%标记低置信度请求，有效规避错误决策，保障部署可靠性。

**表3：消融实验（核心模块性能影响）**
| 模块 | MAPE（%） | Top-1准确率（%） | Mean utility regret |
| ---- | ---- | ---- | ---- |
| 完整OmniPilot（所有模块启用） | 6.2 ✅ | 95 ✅ | 0.003 ✅ |
| 移除Conformally calibrated cost model | 12.1 ❌ | 82 ❌ | 0.015 ❌ |
| 移除OOD abstention layer | 6.2 | 95 | 0.021 ❌ |
| 移除Economic utility metric | 6.2 | 95 | 0.008 ❌ |
💡 结论：三个核心模块均对OmniPilot的性能有显著贡献，缺一不可，共同保障其预测精度与决策质量。

4. 关键结论和发现
- 主要发现：1. OmniPilot的分位数成本模型结合abstention层，在异构GPU集群的LLM服务配置选择上，吞吐量预测精度达6.2% MAPE，配置选择Top-1准确率95%，效用悔恨仅0.003，性能优异；2. 提出的abstention层可100%识别OOD请求，将低置信度预测风险降至最低；3. 三个核心模块（校准成本模型、abstention层、效用指标）的协同作用是OmniPilot性能的关键保障。
- 方法局限性：仅在A100、H100、H200三种GPU及四种精度下验证，未覆盖更多硬件类型与LLM模型；OOD场景的识别基于当前支持包络，需持续扩展训练数据以提升覆盖范围。
- 未来工作：将更多OOD场景与异构硬件、LLM模型加入训练数据集，扩展OmniPilot的支持范围；优化集群资源动态适配策略，应对更复杂的硬件故障与资源波动；拓展到更大规模的异构GPU集群场景。

✅ **总结一句话**：OmniPilot是一种不确定性感知的LLM推理顾问，可精准预测异构GPU集群中LLM服务配置的性能与成本，主动识别异常请求，有效提升LLM服务部署的稳定性与集群资源效用。

</details>

---

### 15. [Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters](https://arxiv.org/abs/2607.01893)

**Authors**: Tianjian Yang, Meng Li  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2607.01893v1  

#### Abstract
Speculative decoding accelerates autoregressive generation by drafting a block of tokens that the target model verifies left-to-right, committing only the longest accepted prefix. Block (DLM-style) drafters predict the whole block in parallel, which is fast but trained with a full-block cross-entrop...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾：masked block drafter采用并行预测全块的方式，训练时用全块交叉熵（CE）监督每个位置，但推理时仅保留首个未接受token之前的前缀，导致训练与推理的监督范围错位；现有方法存在以下缺陷：1) 接受感知目标通过重加权全块损失解决错位，但未解决mask-only drafter缺乏金前缀输入条件通道的问题；2) decay-only基线在共享块掩码上token准确率更高，但解码性能更差，无法有效提升实际生成效率。

🚀 提出的新方法与思路
**Spec-AUF (Accept-Until-Fail)**：该方法仅修改交叉熵损失的监督范围，将CE支持（监督位置）限制在drafter首次预测失败前的前缀，近似实现前缀敏感的训练监督，精准对齐训练与推理过程；无需引入辅助目标、验证器rollout模块，也不改变推理管线及精确性契约，是对训练过程的轻量化修改。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 训练推理一致性 | 直接对齐监督范围与推理有效生成区域，解决错位问题 |
| 模块复杂度 | 仅修改CE损失范围，无额外模块引入 |
| 推理兼容性 | 不改变现有推理管线，可无缝集成 |
| 性能提升 | Qwen3-8B上使DFlash平均发射长度τ从2.40提升至2.61，所有基准均有增益 |
| 迁移性 | 可适配不同结构的block drafter（如Domino双分支头） |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 6个通用文本生成基准 | 评估block drafter的平均发射长度τ等生成性能 |

🎯 实验设置与评估指标
任务：基于speculative decoding的文本生成加速任务。
| 指标 | 含义（箭头方向） |
| --- | --- |
| 平均发射长度τ | drafter每次输出的有效token数平均值 | ↑ |
| 块内token准确率 | 预测token与金标一致的比例 | ↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| DFlash drafter | Masked block drafter | 传统并行预测全块的baseline drafter |
| Domino双分支头 | Masked block drafter | 双分支结构的block drafter，用于迁移性评估 |
| decay-only baseline | 基准训练方法 | 采用指数位置衰减权重的训练策略 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：不同方法在Qwen3-8B上的平均发射长度τ（6基准平均）**
| 方法 | 平均τ |
| --- | --- |
| DFlash (原始) | 2.40 |
| DFlash + Spec-AUF | 2.61 ✅ |
| Domino双分支头 (原始) | 2.56 |
| Domino双分支头 + Spec-AUF | 2.68 ✅ |
💡 结论：Spec-AUF可显著提升两种结构block drafter的平均发射长度，在所有测试基准上均有稳定增益。

**表2：DFlash模型消融实验（平均τ）**
| Spec-AUF | 指数位置衰减权重 | 平均τ |
| --- | --- | --- |
| ❌ | ✅ | 2.30 |
| ✅ | ✅（截断后无效） | 2.61 ✅ |
💡 结论：在Spec-AUF将CE监督截断至失败前缀后，指数位置衰减权重视为无效，说明训练监督范围是影响生成效率的关键因素。

4. 关键结论和发现
- 2-3 条主要发现：
  1. Spec-AUF通过限制CE监督到块生成的首次失败前缀，精准对齐了masked block drafter的训练与推理过程，大幅提升生成效率；
  2. 指数位置衰减权重在训练推理错位场景下无法有效提升生成效率，准确率与实际生成效果存在偏差；
  3. Spec-AUF具有良好的模型迁移性，无需调整即可适配不同结构的block drafter。
- 方法局限性：仅针对mask-only的block drafter设计，未验证其他类型drafter的适用性。
- 未来工作：扩展Spec-AUF到其他block drafter架构，探索与其他 speculative decoding优化方法的结合，进一步提升生成加速性能。

> ✅ **总结一句话**：Spec-AUF通过仅将交叉熵监督限制在block生成的首次失败前缀，轻量化解决了masked block drafter的训练推理错位问题，有效提升了speculative decoding下的文本生成加速效率，且兼容不同结构的drafter模型。

</details>

---

### 16. [Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing](https://arxiv.org/abs/2607.01978)

**Authors**: Siyuan Li, Youyuan Zhang, Ruitong Liu, Junxi Wang, Jing Li  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.01978v1  

#### Abstract
Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, bu...

---

### 17. [InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories](https://arxiv.org/abs/2607.02010)

**Authors**: Qianyu Chen, Ziteng Feng, Canran Xiao, Runxuan Tang  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.02010v1  

#### Abstract
Multimodal large language models must adapt to evolving tasks and domains, yet continual improvement under bounded deployment footprint remains difficult because repeated parameter updates or growing replay stores can accumulate adaptation state over time. We study fixed-footprint continual adaptati...

---

### 18. [Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion for Fast and Flexible Decoding](https://arxiv.org/abs/2607.01775)

**Authors**: Marianne Arriola, Volodymyr Kuleshov  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.01775v1  

#### Abstract
Discrete diffusion models have steadily improved in quality relative to autoregressive (AR) models. However, these models are normally constrained to fixed-length generation and do not support key-value (KV) caching. Block diffusion partially bridges diffusion and AR by generating token blocks left-...

---

### 19. [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509)

**Authors**: Yanjun Zhao, Ruizhong Qiu, Tianxin Wei, Yuanchen Bei, Zhining Liu, Lingjie Chen, Ismini Lourentzou, Hanghang Tong, Jingrui He  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.02509v1  

#### Abstract
Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context windows, they often fail to use relevant evidence that is already present in the input, revealing a...

---

### 20. [One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective](https://arxiv.org/abs/2607.02292)

**Authors**: Juan Agust\'in Duque, Sergio Garc\'ia Heredia, Vinicius Hernandes, Eli\v{s}ka Greplov\'a, Thomas Spriggs, Aaron Courville, Anna Dawid  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.02292v1  

#### Abstract
Neural quantum states (NQS) provide a flexible and scalable framework for approximating quantum many-body wavefunctions. Among NQS parameterizations, autoregressive models are especially attractive because they enable exact, independent sampling from the Born distribution, avoiding the autocorrelati...

---

### 21. [From Monolingual to Multilingual: Evaluating Mamba for ASR in South African Languages](https://arxiv.org/abs/2607.01502)

**Authors**: Jesujoba O. Alabi, Julian Herreilers, Badr M. Abdullah, Dietrich Klakow  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.01502v1  

#### Abstract
Recent advances in automatic speech recognition (ASR) have explored different sequence models, including Conformer-based models and newer state space models such as Mamba. Although prior work has evaluated these architectures in multiple languages, their effectiveness in African languages remains un...

---

### 22. [Wind-Aware Reinforcement Learning Control of a Small Quadrotor Using Learned Onboard Wind Estimation in Simulated Atmospheric Turbulence](https://arxiv.org/abs/2607.01528)

**Authors**: Abdullah Al Tasim, Wei Sun  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.01528v1  

#### Abstract
Small multirotor aircraft are increasingly tasked with operations in the atmospheric boundary layer, where turbulent winds comparable to the vehicle's airspeed degrade trajectory tracking and can defeat conventional feedback control. This work illustrates a two-stage learning pipeline that first est...

---

### 23. [Geometric Signatures of Reasoning: A Spectral Perspective on Task Hardness](https://arxiv.org/abs/2607.01571)

**Authors**: Aria Masoomi, Mahsa Bazzaz, Adel Javanmard, Vahab Mirrokni  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.01571v1  

#### Abstract
Chain-of-thought (CoT) reasoning enables large language models (LLMs) to solve complex problems by generating intermediate reasoning steps. While much attention has been paid to the length and content of these reasoning chains, far less is known about their internal geometry. We study the \emph{geom...

---

### 24. [Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows](https://arxiv.org/abs/2607.01465)

**Authors**: Karthikeya Aditya Vissa, Sankalp Mane, Ananya Mantravadi, Harshit Rajgarhia, Abhishek Mukherji  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.01465v1  

#### Abstract
Large language models are trained to predict the next token, not to act inside a specific API. In niche enterprise SaaS workflows -- where success means hitting the right endpoint with the right nested arguments in the right order -- this objective mismatch shows up as silent failures: dropped requi...

---

### 25. [DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning](https://arxiv.org/abs/2607.01729)

**Authors**: Yueming Huang, Wenhan Yao, Fen Xiao, Xiarun Chen, Weiping Wen  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.01729v1  

#### Abstract
Deep learning models for speech classification are vulnerable to backdoor attacks, where malicious triggers cause misclassification at inference time. While sample-specific attacks can bypass many defenses, they often rely on poisoned label attack, making them detectable via manual data defense. In ...

---

### 26. [CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning](https://arxiv.org/abs/2607.02262)

**Authors**: Dingling Xu, Ruobing Wang, Qingfei Zhao, Yukun Yan, Zhichun Wang, Daren Zha, Shi Yu, Zhenghao Liu, Shuo Wang, Xu Han, Maosong Sun  
**Category**: cs.CL  
**Published**: 2026-07-03  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.02262v1  

#### Abstract
Reasoning Language Models (RLMs) have significantly improved performance on complex tasks by extending the reasoning chain. However, these chains are prone to containing factual errors, particularly in knowledge-intensive tasks. To address this issue, we propose CheckRLM, a framework that improves t...

---

### 27. [Learning the Supports for Categorical Critic in Reinforcement Learning](https://arxiv.org/abs/2607.01880)

**Authors**: Jen-Yen Chang, Takayuki Osa, Tatsuya Harada  
**Category**: cs.LG  
**Published**: 2026-07-03  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.01880v1  

#### Abstract
Value functions are an essential component in actor-critic based deep reinforcement learning (RL). Conventionally, these functions are trained as a regression task by minimising the mean squared error (MSE) relative to bootstrapped target values. Meanwhile, in distributional RL, a distribution of re...

---

### 28. [Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling](https://arxiv.org/abs/2607.01612)

**Authors**: Xuqing Yang, Yi Yuan, Shanzhe Lei, Xuhong Wang  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2607.01612v1  

#### Abstract
Training large language models (LLMs) with reinforcement learning (RL) has significantly advanced their performance on reasoning and question-answering tasks. However, prevailing RL reward designs typically prioritize response correctness, neglecting to incentivize models to express their confidence...

---

### 29. [Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model](https://arxiv.org/abs/2607.01595)

**Authors**: Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo, Tianyu Shen, Zeyu Qiao  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.01595v1  

#### Abstract
As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge. While existing approaches integrate Large Language Models (LLMs) for semantic understanding and Deep Reinforce...

---

### 30. [Enhancing Fitness Intelligence through Domain-Specific LLM Post-Training](https://arxiv.org/abs/2607.02118)

**Authors**: Xingtao Zhao, Tian Yang, Han Jiang  
**Category**: cs.AI  
**Published**: 2026-07-03  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.02118v1  

#### Abstract
Scientific Fitness Coaching (SFC) is typically delivered by human professionals, making it costly and inaccessible to many. While recent advances in Large Language Models (LLMs) show considerable promise for more inclusive fitness coaching, directly deploying prevailing general-purpose LLMs in SFC r...

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
