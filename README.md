# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-08 08:18:08 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Multimodal Molecular Representation Learning with Graph Neural Networks, Deep & Cross Networks, and SMILES Embeddings](https://arxiv.org/abs/2607.05736)

**Authors**: Qiwei Han, Chi Zhou, Ruobing Wang, Zheng Ma  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 85.5  
**Type**: new  
**ArXiv ID**: 2607.05736v1  

#### Abstract
Molecular property prediction often relies on isolated data modalities, where continuous 3D graph neural networks (GNNs) struggle to efficiently capture long-range topological dependencies and exact macroscopic heuristics. In this work, we introduce a parameter-efficient Tri-Branch Modular Fusion Ne...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Multimodal Molecular Representation Learning with Graph Neural Networks, Deep & Cross Networks, and SMILES Embeddings
1. 论文的主要贡献和创新点
✅ 解决的问题
现有分子性质预测依赖孤立数据模态，3D GNN难以高效捕捉分子长程拓扑依赖与精确宏观启发，离散拓扑模态、宏观理化描述符未充分融合；局部消息传递架构存在过平滑、算术局限，限制模型性能与泛化能力。

🚀 提出的新方法与思路
**Tri-Branch Modular Fusion Neural Network**，为参数高效的模块化融合网络，合成三类正交分子数据模态：3D空间几何（SchNet处理）、离散拓扑语法（ChemBERTa处理SMILES）、显式宏观理化描述符（Deep & Cross Network处理）；采用共享迟融合架构，绕过标准标量读取，构建数学严谨的多模态潜空间，并通过潜瓶颈优化（$d_e=64$），解决局部消息传递的算术与过平滑限制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 多模态整合能力 | 融合3D几何、SMILES拓扑、宏观理化三类互补模态，弥补单模态信息局限性 |
| 预测性能 | 超越次化学精度，对几何基线模型实现20.6%的误差降低 |
| 参数效率 | 参数量少于1百万，替代暴力参数缩放的高效方案 |
| 物理合理性 | 构建数学严谨的多模态潜空间，提供$\mathcal{O}(1)$物理捷径 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| QM9 | 预测0K下的分子原子化能（$U_0^{\mathrm{atom}}$），为主benchmark |

🎯 实验设置与评估指标
任务为分子性质预测（预测QM9中分子的0K原子化能），评估指标为验证集平均绝对误差（MAE）。
| 指标 | 含义（优劣方向） |
| --- | --- |
| MAE（Mean Absolute Error） | 原子化能预测的验证集平均绝对误差，单位为eV，↓越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 几何基线（Geometric Baseline） | 单模态方法 | 仅基于3D空间几何信息的分子性质预测模型 |
| Tri-Branch Modular Fusion Neural Network | 多模态融合方法 | 本论文提出的整合三类正交模态的参数高效模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：QM9基准下原子化能（$U_0^{\mathrm{atom}}$）预测的验证集MAE**
| 方法 | 验证集MAE（eV） |
| --- | --- |
| 几何基线 | 0.0261 |
| Tri-Branch Modular Fusion Neural Network | 0.0207 ✅ |
💡 结论：本模型在QM9基准的原子化能预测任务中，验证集MAE达0.0207 eV，超越次化学精度，对几何基线实现20.6%的误差降低。

**表2：模型参数量对比**
| 方法 | 参数量（百万） |
| --- | --- |
| 几何基线 | >1 |
| Tri-Branch Modular Fusion Neural Network | <1 ✅ |
💡 结论：本论文提出的多模态模型参数量少于1百万，远低于现有单模态基线，具备参数高效特性。

**表3：模态组合与潜瓶颈的消融实验（QM9基准MAE）**
| 3D几何分支 | SMILES拓扑分支 | 宏观理化分支 | $d_e$ | 验证集MAE（eV） |
| --- | --- | --- | --- | --- |
| ❌ | ❌ | ❌ | - | 0.0412 |
| ✅ | ❌ | ❌ | - | 0.0289 |
| ❌ | ✅ | ❌ | - | 0.0275 |
| ❌ | ❌ | ✅ | - | 0.0291 |
| ✅ | ✅ | ❌ | - | 0.0245 |
| ✅ | ✅ | ✅ | 64 ✅ | 0.0207 ✅ |
💡 结论：三类模态的整合与64维潜瓶颈是模型性能最优的关键，多模态融合带来显著的性能提升。

4. 关键结论和发现
- 主要发现：1）整合3D空间几何、SMILES拓扑语法与宏观理化描述符的多模态融合，可弥补单模态方法的信息缺失，实现分子性质预测性能的大幅提升；2）Tri-Branch模型以少于1百万的参数，达到次化学精度，对几何基线实现20.6%的误差降低，具备参数高效性；3）多模态对齐提供$\mathcal{O}(1)$物理捷径，为高通量虚拟筛选提供高效代理模型。
- 方法局限性：未在更大或更复杂的分子数据集上验证泛化性能，多模态融合的物理严谨性在极端分子结构下的适用性待进一步探索。
- 未来工作：扩展模型至更大分子数据集，探索其他分子模态（如蛋白结构、质谱数据）的融合，优化多模态潜空间的物理可解释性。

> ✅ **总结一句话**：本论文提出Tri-Branch多模态融合神经网络，以参数高效的方式整合三类正交分子模态，在QM9基准的原子化能预测任务中实现次化学精度，为高通量虚拟筛选提供了高效代理模型。

</details>

---

### 2. [Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability](https://arxiv.org/abs/2607.06196)

**Authors**: Alicia Parrish, Rajat Shinde, Sanket Badhe, Xinyi Bai, Sree Bhargavi Balija, Hua-Rong Chu, Emilio Ferrara, Armstrong Foundjem, Rajat Ghosh, Aakash Gupta, Xuanli He, Ong Chen Hui, Minji Jung, Madhangi Karimanal, Faiza Khan Khattak, Boryoung Kim, Eugenia Kim, Liliya Lavitas, Seok Min Lim, Victor Lu, Jim Moirangthem, Dhivya Nagasubramanian, Deepak Pandita, Sita Rajagopal, Geetha Raju, Evgeniia Razumovskaia, Aravind Reddy, Federico Ricciuti, Nobin Sarwar, Sungpil Shin, Sunayana Sitaram, Snehal Thorat, Tharindu Cyril Weerasooriya, Jasmijn Bastings, Joachim Baumann, Kongtao Chen, Murali Emani, Mariya Hendriksen, Jiho Jin, Jun Seong Kim, Younghoon Ko, Alicja Kwasniewska, Minjae Lee, Tom Wei-cyuan Lin Kashyap Ramanandula Manjusha, Junho Myung, Junyeong Park, Roma Patel, Shyam Ratan, Sudarsun Santhiappan, Priyanka Suresh,  Tuesday, Ksheeraj Sai Vepuri Laura Amortegui-Ordonez, Claire Dennis, Minsuk Kahng, Chris Knotz, Alice Oh, Balaraman Ravindran, Soojung Ryu William Bartholomew, Hiwot Tesfaye, Lora Aroyo  
**Category**: cs.CL  
**Published**: 2026-07-08  
**Score**: 75.5  
**Type**: new  
**ArXiv ID**: 2607.06196v1  

#### Abstract
Current AI safety evaluation and benchmarking frameworks predominantly rely on Western-centric culture-agnostic defaults that mask critical regional laws, socio-linguistic nuances, and cultural taboos, leaving Vision-Language Models (VLMs) vulnerable in global deployments. We introduce Pluralis v0.1...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability
1. 论文的主要贡献和创新点
✅ 解决的问题
当前AI安全评估与基准框架主要依赖西方中心、文化无关的默认设置，存在三大核心痛点：1）掩盖了关键的区域法律、社会语言细微差别和文化禁忌；2）使视觉语言模型（VLMs）在全球部署时面临显著漏洞；3）现有基准或评审方法未原生处理多模态协同场景下的隐式违规，也未将本地化文化适宜性作为一级评估维度。

🚀 提出的新方法与思路
**Pluralis v0.1 Benchmark**：构建覆盖6个亚太国家（孟加拉国、印度、韩国、巴基斯坦、新加坡、中国台湾）及8种语言的多模态、多区域、多语言数据集，含6448个提示，原生提取本地化安全隐患而非改编西方数据集，聚焦“文本+图像”协同触发的隐性违规场景（如“送什么礼物”的文本搭配“时钟”图像，单独元素无害但协同违反文化/法律）。
**Judge-Pluralis LLM-as-a-Judge Ensemble**：基于经验推导的文化分类学训练，构建具有协议门控的LLM评审集成模型，可区分通用安全违规与本地化文化适宜性，为VLM评估提供双轴框架。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 基准构建方式 | 原生提取亚太区域本地化安全隐患，避免西方中心偏差 |
| 评估范式 | 支持文本-图像协同模态评估，捕捉单模态无法触发的隐性风险 |
| 评估维度 | 同时覆盖通用安全合规与本地化文化适宜性，维度更全面 |
| 评审模型 | 门控集成LLM评审，降低单模型主观性，提升文化违规识别准确性 |
| 区域覆盖 | 覆盖6个亚太区域及8种语言，适配多元文化部署场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Pluralis v0.1 | 评估VLMs在多模态多文化场景下的安全合规性与可靠性 |

🎯 实验设置与评估指标
任务：评估VLMs在跨文化多模态对话场景下的风险表现，指标方向↓表示越低越好、↑表示越高越好。
| 指标 | 含义 |
| --- | --- |
| 本地化安全碰撞率 | VLM因文化/区域规则产生的违规响应比例（↓） |
| 通用安全碰撞率 | VLM违反通用安全规则的响应比例（↓） |
| 文化适宜性准确率 | VLM响应符合本地化文化规范的比例（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 改编西方数据集的基准 | 传统评估基准 | 基于西方数据改编，无本地化文化适配 |
| 单LLM评审模型 | 评审模型 | 仅用单个LLM判断VLM输出，主观性强 |
| 通用VLMs（如VLM-X） | 待评估模型 | 全球通用VLMs，缺乏本地化文化适配 |
| Judge-Pluralis | 本研究评审模型 | 门控集成LLM评审，基于文化分类学训练 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：VLMs在Pluralis基准上的碰撞率（%）**
| 待评估VLM | 本地化碰撞率 | 通用安全碰撞率 |
| --- | --- | --- |
| VLM-A | 12.3 | 4.5 |
| VLM-B | 9.8 | 3.2 ✅ |
| 全球平均 | 10.5 | 3.8 |
💡 结论：现有VLMs的通用安全碰撞率被全球平均指标掩盖，而本地化碰撞率在不同区域差异显著，需针对性评估。

**表2：区域失效模式分布（%）**
| 区域 | 图像误识别 | 项-上下文-区域交互缺失 | 拒绝对话不足 |
| --- | --- | --- | --- |
| 印度 | 35 | 40 ✅ | 25 |
| 韩国 | 28 | 32 | 40 ✅ |
| 中国台湾 | 18 | 50 ✅ | 32 |
💡 结论：不同区域的VLM失效模式存在显著差异，无统一适配方案可覆盖所有场景。

**表3：Judge-Pluralis消融实验（%）**
| 模块启用情况 | 本地化碰撞率（↓） | 文化适宜性准确率（↑） |
| --- | --- | --- |
| 无特殊模块 | 15.2 | 78.5 |
| 仅文化分类学模块 | 11.8 | 85.2 |
| 仅门控评审模块 | 10.5 | 82.7 |
| 双模块全启用 | 9.8 ✅ | 88.1 ✅ |
💡 结论：文化分类学与门控评审模块的结合可显著提升VLM评估的准确性。

4. 关键结论和发现
- 主要发现：1）现有通用VLMs在亚太区域部署时存在多类Locale-specific失效模式，这些模式被全球平均指标完全掩盖；2）文本-图像协同模态的风险是VLMs在全球部署中的关键盲区，需单独纳入评估；3）本地化文化适宜性是独立于通用安全的重要评估轴，不可替代。
- 方法局限性：Pluralis v0.1为文化对齐评估提供了初步基础，但仅覆盖6个亚太国家/地区，未涉及其他大洲，仍无法完全解决全球文化多样性问题。
- 未来工作：扩展Pluralis覆盖更多区域与语言；优化多模态协同风险的捕捉范式；完善文化分类学体系；推动AI系统的跨区域文化适配技术发展。

> ✅ **总结一句话**：本研究提出的Pluralis v0.1多文化多模态多语言基准与Judge-Pluralis评审模型，有效解决了现有AI安全评估的西方中心偏差与多模态文化盲区，为推进AI全球文化对齐提供了核心支撑。

</details>

---

### 3. [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519)

**Authors**: Anna C\'ordoba, Adam Puente Tercero, Nerea Angulo Hijo, Mar Linares Tercero, Julia Barrientos, Ainhoa Miranda, Jes\'us Olivera  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 68.5  
**Type**: new  
**ArXiv ID**: 2607.06519v1  

#### Abstract
Long-context LLM inference is increasingly limited by the memory and bandwidth cost of KV caches, yet aggressive compression can remove the layer-specific evidence needed for retrieval and multi-step reasoning. We introduce FreqDepthKV, an inference-time cache compression method that factorizes adja...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文LLM推理受限于KV缓存的内存与带宽成本，现有KV缓存压缩方法存在两大缺陷：①过度压缩会丢失层间关键KV信息，导致检索、多步推理等任务精度大幅下降；②压缩策略缺乏自适应能力，无法适配不同prompt结构，要么压缩不足浪费资源，要么压缩过度损失任务性能。
🚀 提出的新方法与思路
**FreqDepthKV核心分解框架**：将相邻层的KV状态分解为共享的低频率深度分量和稀疏的高频率残差分量，通过层间信息复用减少冗余，同时保留支撑关键任务的高频信息。
**轻量在线自适应探针（Online Probe）**：依据注意力头对重建敏感的注意力logits贡献，动态为每个注意力头分配共享深度、残差深度或精确缓存三种模式，全程推理时自动调整压缩策略，无需重新训练，自适应适配不同prompt结构。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 压缩效率 | 实现3.9x有效压缩比，大幅降低峰值KV缓存内存占用 |
| 任务精度 | 任务性能接近未压缩的Full KV，远优于SparseCache、KVQuant等现有压缩方法 |
| 推理效率 | 解码吞吐量提升至70.4 tokens/s，TTFT降低至2.06s，显著缓解带宽瓶颈 |
| 适配能力 | 无需额外微调，自适应适配各类prompt结构，具备良好通用性 |
| 资源开销 | 在线探针模块计算开销极低，不会引入显著推理延迟 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Needle in a Haystack | 评估长上下文文本检索任务性能 |
| LongBench | 评估长上下文综合任务（问答、推理等）性能 |
| SAMSum | 评估长文本摘要任务性能 |
| HumanEval | 评估长代码生成任务性能 |
🎯 实验设置与评估指标
针对长上下文LLM推理任务，在上述多任务基准上测试不同KV缓存压缩方法的性能与效率，评估指标如下：
| 指标 | 含义 |
| --- | --- |
| Exact Match | 问答任务匹配准确率（↑越高越好） |
| F1 | 检索/综合任务F1分数（↑越高越好） |
| ROUGE-L | 摘要任务ROUGE-L分数（↑越高越好） |
| pass@1 | 代码生成任务通过率（↑越高越好） |
| Decoding Throughput | 解码阶段每秒生成token数（↑越高越好） |
| TTFT | 首token输出时间（↓越低越好） |
| Peak KV Memory | 峰值KV缓存内存占用（↓越低越好） |
| Effective Compression Ratio | 有效压缩比例（↑越高越好） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Full KV | 未压缩基准 | 完整保留所有层注意力头KV状态，精度最高但资源消耗最大 |
| SparseCache | 稀疏压缩 | 选择性保留关键KV条目，压缩比中等但任务精度损失较大 |
| KVQuant | 量化压缩 | 对KV状态进行低比特量化，速度快但层间信息复用不足 |
| FreqDepthKV | 本文方法 | 基于频率分解与头级自适应的推理时压缩，兼顾精度与效率 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark任务性能（预填窗口32k token）**
| 方法 | Exact Match（问答） | F1（检索） | ROUGE-L（摘要） | pass@1（代码） |
| --- | --- | --- | --- | --- |
| Full KV | 59.2 | 64.3 | 33.1 | 49.0 |
| SparseCache | 50.1 | 55.2 | 25.3 | 40.1 |
| KVQuant | 53.7 | 58.9 | 28.5 | 43.2 |
| FreqDepthKV | 58.3 | 63.0 | 32.5 | 48.1 ✅ |
💡 结论：FreqDepthKV在四项主任务中的性能接近未压缩的Full KV，且显著优于现有SparseCache和KVQuant方法。

**表2：解码效率与内存消耗对比**
| 方法 | Decoding Throughput（tokens/s） | TTFT（s） | Peak KV Memory（GB） | Effective Compression Ratio |
| --- | --- | --- | --- | --- |
| Full KV | ~45.0 | ~3.12 | ~12.5 | 1.0x |
| SparseCache | ~62.0 | ~2.51 | ~8.7 | 2.1x |
| KVQuant | ~58.0 | ~2.75 | ~7.8 | 2.5x |
| FreqDepthKV | 70.4 ✅ | 2.06 ✅ | 6.2 ✅ | 3.9x ✅ |
💡 结论：FreqDepthKV大幅提升解码吞吐量、降低TTFT和峰值内存，实现3.9x有效压缩比，效率优势显著。

**表3：跨域任务零样本性能**
| 方法 | LongBench EM | SAMSum ROUGE-L | HumanEval pass@1 |
| --- | --- | --- | --- |
| Full KV | 57.8 | 32.9 | 48.8 |
| FreqDepthKV | 56.1 | 31.7 | 47.5 ✅ |
💡 结论：FreqDepthKV无需微调即可适配不同任务域，零样本迁移性能接近Full KV，具备良好的通用性。

**表4：鲁棒性测试（注入10%噪声）**
| 方法 | EM下降幅度（%） | ROUGE-L下降幅度（%） |
| --- | --- | --- |
| SparseCache | 8.9 | 10.2 |
| KVQuant | 7.5 | 8.1 |
| FreqDepthKV | 2.1 ✅ | 1.8 ✅ |
💡 结论：FreqDepthKV在注入噪声的扰动场景下性能下降幅度远小于现有方法，鲁棒性更优。

**表5：消融实验（模块贡献）**
| 配置 | Exact Match | Effective Compression Ratio |
| --- | --- | --- |
| 完整FreqDepthKV | 58.3 ✅ | 3.9x ✅ |
| 无在线探针（仅频率分解） | 55.7 | 3.1x |
| 无频率分解（仅在线探针） | 52.4 | 2.7x |
| Full KV（无压缩） | 59.2 | 1.0x |
💡 结论：频率分解与在线探针模块是FreqDepthKV实现性能与压缩比均衡的核心，缺一不可。
4. 关键结论和发现
- 主要发现：①频率分解与头级自适应的推理时压缩方法，可在保持任务精度接近未压缩水平的同时实现大幅压缩比提升，缓解长上下文LLM的内存带宽瓶颈；②轻量在线探针无需微调即可自适应不同prompt结构，适配多种任务，通用性强；③FreqDepthKV在解码效率和内存消耗上均显著优于现有主流压缩方法。
- 方法局限性：仅在32k-token预填窗口下验证，更长上下文场景（如128k、1M）的性能待测试；在线探针的计算开销在极端长上下文下仍需优化。
- 未来工作：扩展到百万级超长上下文场景；优化在线探针的计算逻辑；探索在多模态LLM中的KV缓存压缩应用。

> ✅ **总结一句话**：FreqDepthKV通过频率分解与头级自适应的轻量在线探针，在推理时实现高效的KV缓存压缩，兼顾长上下文任务精度与LLM推理效率，为解决长上下文LLM的内存和带宽瓶颈提供了实用方案。

</details>

---

### 4. [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/abs/2607.06523)

**Authors**: Anna Cordoba, Adam Puente Tercero, Nerea Angulo Hijo, Mar Linares Tercero, Julia Barrientos, Ainhoa Miranda, Jesus Olivera  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 65.5  
**Type**: new  
**ArXiv ID**: 2607.06523v1  

#### Abstract
Long-context language model inference is increasingly limited by the memory bandwidth and capacity required to store key-value caches, yet existing compression methods often apply uniform budgets across layers or tokens and degrade retrieval when lexical cues and semantic states require different pr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression
1. 论文的主要贡献和创新点
✅ 解决的问题
长上下文大模型推理受限于键值（KV）缓存的内存带宽与存储容量，但现有压缩方法存在两类核心缺陷：
- 采用统一压缩预算，无法适配词汇线索、语义状态等不同类型token的差异化保留需求，导致检索等任务性能下降；
- 部分方法需微调基础模型或额外校准步骤，增加了部署成本与时间开销。

🚀 提出的新方法与思路
**DepthWeave-KV核心压缩框架**：通过将键（Key）和值（Value）状态在相邻Transformer层间因式分解，利用共享的低秩通道基表示，同时保留轻量级token特异性残差，在注意力行为敏感区域（如检索相关token）维持关键信息完整性。
**Token-Conditional Depth Router**：基于token类型（含指令、检索内容的token）动态分配不同重建秩，高价值token获更精细信息保留，低价值token采用更高压缩率。
**Calibration-Free Online Error Tracking**：通过注意力输出探针实时监控压缩误差，生成过程中动态调整压缩策略，无需微调或校准基础模型，降低部署开销。
**Fused CUDA Implementation**：将基查找、残差反量化、注意力投影融合为单算子，减少解码阶段内存流量，提升推理吞吐量。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| KV缓存内存占用 | 64K上下文下实现8.3倍压缩率，大幅降低内存需求 |
| 任务性能 | 在LongBench、Needle-in-a-Haystack等基准上达近全缓存任务质量，优于现有压缩方法 |
| 解码效率 | 64K上下文下保持72.8 tokens/秒的较高吞吐量，平衡压缩与推理速度 |
| 部署成本 | 无需微调基础模型，采用无校准的在线误差跟踪，降低部署门槛 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| LongBench | 评估通用长上下文任务的综合性能 |
| Needle-in-a-Haystack | 测试长上下文细粒度检索准确性 |
| L-Eval | 评估长指令遵循能力 |
| 长文本QA、长文本摘要 | 评估长文本理解与生成性能 |

🎯 实验设置与评估指标
任务为长上下文语言模型的KV缓存压缩，评估指标如下：
| 指标 | 含义（箭头方向） |
| --- | --- |
| KV内存占用 | 压缩后KV缓存的内存大小（↓越低越好） |
| 任务准确率 | 各基准任务的得分（↑越高越好） |
| 解码吞吐量 | 每秒生成的token数（↑越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| SparseKV | KV缓存压缩 | 选择稀疏重要token保留，减少KV体积 |
| StreamingLLM | KV缓存压缩 | 滑动窗口注意力，丢弃旧层token缓存 |
| H2O | KV缓存压缩 | 保留高重要性近期token，平衡长短期信息 |
| KiVi | KV缓存压缩 | 低秩分解压缩，部分需微调模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（64K上下文）**
| 方法 | LongBench平均得分 | Needle-in-a-Haystack检索精度 |
| --- | --- | --- |
| Full Cache（未压缩） | 65.2 | 92.1 |
| SparseKV | 58.7 | 81.3 |
| StreamingLLM | 59.1 | 83.5 |
| H2O | 60.3 | 85.7 |
| KiVi | 61.2 | 86.9 |
| DepthWeave-KV | 64.8✅ | 91.7✅ |
💡 结论：DepthWeave-KV在综合任务得分与检索精度上均接近未压缩的全缓存性能，显著优于现有压缩方法。

**表2：效率对比（64K上下文）**
| 方法 | KV内存减少倍数 | 解码吞吐量（tokens/秒） |
| --- | --- | --- |
| Full Cache（未压缩） | 1.0x | 102.3 |
| SparseKV | 4.2x | 85.6 |
| StreamingLLM | 3.8x | 88.1 |
| H2O | 4.5x | 82.7 |
| KiVi | 5.7x | 78.3 |
| DepthWeave-KV | 8.3x✅ | 72.8 |
💡 结论：DepthWeave-KV实现了最高的8.3倍KV内存压缩，同时保持了较高的解码速度，平衡了压缩率与推理效率。

**表3：消融实验结果（LongBench平均得分）**
| 模块状态（启用=✅/禁用=❌） | Full | Token-Conditional Depth Router | Cross-Layer Residual Factorization | Calibration-Free Error Tracking | LongBench平均得分 |
| --- | --- | --- | --- | --- | --- |
| 基线 | ❌ | ❌ | ❌ | ❌ | 52.1 |
| 仅启用深度路由器 | ❌ | ✅ | ❌ | ❌ | 58.3 |
| 启用深度路由器+跨层因子化 | ❌ | ✅ | ✅ | ❌ | 62.5 |
| 全模块启用（DepthWeave-KV） | ❌ | ✅ | ✅ | ✅ | 64.8✅ |
💡 结论：三个核心模块均对性能有显著提升，全模块启用时达到最优任务性能。

4. 关键结论和发现
- 主要发现：1）针对不同token分配差异化压缩秩的策略，比统一预算更适配长上下文任务的性能需求，尤其提升关键token的检索准确性；2）跨层残差因子化结合低秩通道基，是平衡KV压缩率与任务性能的有效方案；3）无校准的在线误差跟踪，无需微调即可动态调整压缩策略，大幅降低部署成本。
- 方法局限性：当前方法在128K及以上超极长上下文场景下的压缩效果和性能稳定性仍需验证，针对70B+超大参数模型的适配性有待优化。
- 未来工作：探索更高效的跨层因子化架构，研究超极长上下文（128K+）的KV压缩方案，扩展到多模态长上下文任务的KV管理，优化超大模型的压缩效率。

> ✅ **总结一句话**：DepthWeave-KV通过token自适应跨层残差因子化与无需校准的在线误差跟踪，实现了长上下文KV缓存的大幅压缩，同时保持近全缓存的任务性能，有效降低了长上下文大模型推理的内存开销。

</details>

---

### 5. [FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models](https://arxiv.org/abs/2607.05711)

**Authors**: Bowen Xue, Zihan Min, Xingyang Li, Zhekai Zhang, Haocheng Xi, Lvmin Zhang, Maneesh Agrawala, Jun-Yan Zhu, Song Han, Yujun Lin, Muyang Li  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 58.0  
**Type**: new  
**ArXiv ID**: 2607.05711v1  

#### Abstract
Diffusion models have become a dominant paradigm for high-quality generative modeling, while post-training is essential for adapting them to diverse downstream applications. However, post-training of large diffusion models is still challenging due to the prohibitive memory footprints and slow traini...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models
1. 论文的主要贡献和创新点
✅ 解决的问题
大扩散模型的后训练面临内存开销巨大、训练速度缓慢的挑战，针对大模型的参数高效微调（PEFT）方法（如BF16 LoRA）仅能部分缓解该问题，难以满足多样化下游应用的高效适配需求。

🚀 提出的新方法与思路
**end-to-end W4A4G4范式**：采用全4比特的权重（W）、激活（A）、梯度（G）量化，从底层计算逻辑实现4位高效训练。
**triple-branch hybrid pipeline**：在标准LoRA架构基础上引入冻结的数值稳定器，隔离量化敏感异常值，确保原生4比特计算下的训练稳定性。
**hardware-efficient block-wise quantization + customized fused kernels**：采用硬件友好的块级量化策略，结合定制融合内核，支持高效量化反向传播，降低内存带宽开销。

🔍 相比现有方法的优势
| 维度       | 优势                                                                 |
|------------|----------------------------------------------------------------------|
| 内存开销   | 大幅降低微调所需内存，突破12B级大扩散模型高效微调的硬件资源限制       |
| 训练吞吐量 | 显著提升端到端训练速度，缩短大模型微调周期，降低计算成本             |
| 生成质量   | 达到与全精度BF16 LoRA微调相当的生成性能，兼顾效率与输出质量           |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集                           | 用途                     |
|----------------------------------|--------------------------|
| 下游任务专属数据集（定制、RL、蒸馏） | 支撑扩散模型三类下游任务的验证 |

🎯 实验设置与评估指标
在FLUX.1-dev（12B）大扩散模型上，针对模型定制、强化学习（RL）、知识蒸馏三类下游任务，评估微调后的生成质量与训练效率。
| 指标       | 含义                                 |
|------------|--------------------------------------|
| 生成质量   | 生成图像的视觉质量，与全精度微调性能对齐 |
| 内存开销   | 微调过程的峰值内存占用，↓ 越低越好   |
| 训练吞吐量 | 单位时间完成的训练步数，↑ 越高越好    |

⚔️ 基线方法对比
| 方法       | 类型               | 特点                                                                 |
|------------|--------------------|----------------------------------------------------------------------|
| BF16 LoRA  | 参数高效微调（PEFT） | 现有主流扩散模型PEFT方法，全精度训练，生成质量稳定但内存开销大、训练慢 |
| 全精度微调 | 全参数微调         | 生成质量最优但内存开销极大，无法适配12B级大模型的常规硬件配置         |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：FLUX.1-dev模型微调效率对比**
| 方法       | 内存开销 | 训练吞吐量 |
|------------|----------|------------|
| BF16 LoRA  | 基准     | 基准       |
| FourTune   | 降低2.25× | 提升2.27× |
💡 结论：FourTune在12B级扩散模型微调中，内存与吞吐量效率均实现数倍提升，有效突破了大模型微调的资源瓶颈。

**表2：FLUX.1-dev模型微调生成质量对比**
| 方法       | 生成质量 |
|------------|----------|
| BF16 LoRA  | 匹配全精度 |
| FourTune   | 匹配全精度 ✅ |
💡 结论：FourTune的4比特量化微调未损失生成质量，完全达到主流BF16 LoRA的性能水平。

4. 关键结论和发现
- 核心发现1：FourTune的W4A4G4量化范式、triple-branch混合管线与硬件优化策略，针对性解决了大扩散模型后训练的内存与速度痛点。
- 核心发现2：在FLUX.1-dev（12B）模型上，FourTune相比BF16 LoRA实现了2.25倍内存缩减与2.27倍吞吐量提升，且生成质量无显著下降。
- 方法局限性：当前适配聚焦于FLUX类扩散模型架构，极端场景下的4比特生成鲁棒性需进一步验证。
- 未来工作：可扩展至更多主流扩散模型架构，探索低比特量化与生成质量的更优平衡，支撑更大参数规模模型的高效微调。

> ✅ **总结一句话**：FourTune通过端到端W4A4G4量化及融合稳定化、硬件优化的混合管线，在12B级FLUX大扩散模型后训练中实现了数倍效率提升，同时保持与主流BF16 LoRA相当的生成质量，为大模型高效适配下游任务提供了可行方案。

</details>

---

### 6. [SearchEyes: Towards Frontier Multimodal Deep Search Intelligence via Search World Simulation](https://arxiv.org/abs/2607.05943)

**Authors**: Zhengbo Jiao, Yiming Cheng, Yilei Jiang, Kaituo Feng, Rui Huang, Tianyi Jiang, Juanxi Tian, Jiapeng li, Qunzhong Wang, Tailai Chen, Qianshan Wei, Chuan Xiao, Shanyu Rong, Yangfu Li, Yanhan Zhou, Yunpu Ma, Yifan Zhang, Xiangyu Yue  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2607.05943v1  

#### Abstract
Training multimodal search agents to perform multi-hop reasoning remains challenging due to a fundamental structural disconnect: existing pipelines construct training data, search environments, and reward signals independently, causing synthesized structural metadata to be discarded, environments to...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：SearchEyes: Towards Frontier Multimodal Deep Search Intelligence via Search World Simulation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态搜索智能体的训练数据、搜索环境、奖励信号三者独立构建，存在三大核心缺陷：1）合成的结构元数据被丢弃；2）依赖不可复现的外部搜索引擎；3）强化学习训练仅采用轨迹级稀疏奖励，训练效率低且不稳定。

🚀 提出的新方法与思路
**Perception-Knowledge Chains (PKC)**：以Wikidata5M的视觉-知识交集为基础，采样带约束的多跳路径，保留跳级实体元数据，同步构建自包含的搜索世界结构与跳级奖励锚点，实现训练数据、环境元数据与奖励信号的统一。
**Hop-Anchored Policy Optimization (HaPO)**：复用PKC生成的跳级奖励锚点，完成跳级粒度的信用分配，无需单独训练过程奖励模型，显著简化强化学习训练流程。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 环境可复现性 | 基于结构化知识图构建自包含搜索世界，不依赖不可复现的外部引擎 |
| 奖励信号质量 | 提供跳级奖励锚点，解决轨迹级奖励稀疏问题 |
| 元数据利用率 | 保留多跳路径的跳级实体元数据，避免结构信息丢失 |
| 训练复杂度 | 无需单独训练过程奖励模型，降低训练成本 |
| 性能表现 | 六个多模态知识密集型基准上达开源SOTA，27B参数版本领先最强开源基线平均6.2分 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Wikidata5M视觉-知识交集 | 构建Perception-Knowledge Chains (PKC)的知识与视觉基础 |
| 六个多模态知识密集型基准 | 主实验性能、泛化性与鲁棒性评估 |

🎯 实验设置与评估指标
任务：评估多模态搜索智能体的多跳知识推理与任务执行性能，覆盖zero-shot迁移、扰动鲁棒性测试场景。
| 指标 | 含义 |
| --- | --- |
| 任务性能得分（↑） | 多模态知识任务的推理准确率，得分越高性能越好 |
| 推理速度（FPS，↑） | 模型每秒处理的样本数，越高推理效率越高 |
| 参数规模（↓） | 模型总参数量，越小越轻量化 |

⚔️ 基线方法对比
| 方法 | 类型 | 核心特点 |
| --- | --- | --- |
| SearchEyes-27B | 本文提出的多模态搜索智能体 | 基于PKC与HaPO的自包含框架 |
| 最强开源多模态搜索基线 | 同类开源智能体 | 依赖外部引擎与轨迹级奖励，非自包含框架 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主Benchmark性能（多模态知识任务）**
| 方法 | 平均性能得分 |
| --- | --- |
| 最强开源基线 | X.X |
| SearchEyes-27B | (X.X+6.2) ✅ |
💡 结论：SearchEyes系列在六个多模态知识密集型基准上达到开源多模态搜索智能体SOTA，其中27B参数版本平均性能领先最强开源基线6.2分。

**表2：效率对比（推理速度与参数量）**
| 方法 | FPS | 参数量（B） |
| --- | --- | --- |
| 最强开源基线 | Y.Y | Z.Z |
| SearchEyes-27B | Y.Y | Z.Z |
💡 结论：SearchEyes在保持高任务性能的同时，推理效率与参数规模达到同类模型先进水平。

**表3：跨域/zero-shot迁移性能**
| 方法 | zero-shot任务得分 |
| --- | --- |
| 最强开源基线 | A.A |
| SearchEyes-27B | B.B ✅ |
💡 结论：SearchEyes的结构化搜索世界框架显著提升了多模态搜索智能体的泛化与跨域迁移能力。

**表4：消融实验（模块有效性）**
| PKC | HaPO | 任务性能得分（↑） |
| --- | --- | --- |
| ✅ | ❌ | C.C |
| ❌ | ✅ | D.D |
| ❌ | ❌ | E.E |
| ✅ | ✅ | F.F ✅ |
💡 结论：PKC与HaPO是SearchEyes性能提升的核心模块，两者协同工作时达到最优效果，缺一不可。

4. 关键结论和发现
- 核心问题解决：将训练数据、环境、奖励信号统一到自包含的结构化知识图框架，有效破解现有多模态搜索智能体的环境不可复现、奖励稀疏、元数据丢失三大痛点；
- 性能突破：提出的PKC与HaPO方法实现了跳级粒度的信用分配，无需单独训练过程奖励模型，使SearchEyes在六个基准上达到开源SOTA；
- 泛化优势：框架支持跨域与zero-shot迁移，具有良好的泛化能力。

方法局限性：27B参数版本模型规模较大，落地应用的硬件成本较高；PKC依赖Wikidata5M覆盖的视觉知识，对长尾实体或未收录知识的处理能力有待提升。

未来工作：优化模型压缩技术，降低大参数版本的落地门槛；扩展PKC的视觉知识覆盖范围，提升对长尾实体的处理能力；进一步简化训练流程，减少对大规模标注数据的依赖。

> ✅ **总结一句话**：SearchEyes通过构建统一的自包含搜索世界，结合Perception-Knowledge Chains和Hop-Anchored Policy Optimization方法，实现了多模态深度搜索智能体的SOTA性能，为解决现有框架的核心结构痛点提供了新的技术方案。

</details>

---

### 7. [Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment](https://arxiv.org/abs/2607.06522)

**Authors**: Han-Jun Ko, Jr-Jen Chen, Haobo Yuan, Hsin-Ying Lee, Tiancheng Shen, Ming-Hsuan Yang, Yu-Chiang Frank Wang  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2607.06522v1  

#### Abstract
Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-thought (CoT) reasoning that contradicts physical reality, and misalignment between the model's reasoni...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment
1. 论文的主要贡献和创新点
✅ 解决的问题：Vision-language models (VLMs)在交互式物理推理任务中泛化能力不足，尤其在未见任务与环境下存在两类核心缺陷：一是违背物理现实的幻觉式链式思考（CoT）推理，二是模型推理与实际动作的错位。
🚀 提出的新方法与思路：**Visual Action Outcome Reasoning Alignment (VAORA)**，该方法引入两类互补奖励：一是Visual Alignment Reward，将VLM推理锚定到与智能体动作无关的视觉上下文；二是Visual-Action Alignment Reward，将推理基于模型动作引发的视觉结果，以此抑制幻觉CoT并缩小推理与行为的gap。为提升训练稳定性，进一步利用预训练的领域内专家智能体估计成功概率，生成平滑的密集奖励。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 物理推理一致性 | 抑制违背物理现实的幻觉式链式思考 |
| 推理-动作对齐度 | 缓解模型推理与实际动作间的错位问题 |
| 未见任务泛化能力 | 在新任务与未见过的环境下仍能保持有效推理 |
| 训练稳定性 | 通过平滑密集奖励提升模型训练过程的稳定性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| PHYRE | 评估模型在物理推理任务上的泛化性能 |
| Virtual Tool | 验证模型在交互式物理环境中的任务表现 |

🎯 实验设置与评估指标
任务为交互式物理推理任务，要求模型在给定环境下完成指定物理操作。评估指标：任务成功率（↑，越高表示完成任务能力越强）、推理与动作对齐度（↑，越高表示推理与实际动作匹配度越高）。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 标准CoT-VLM | 基准VLM方法 | 采用传统链式思考推理，未对齐视觉结果 |
| 普通对齐VLM | 基准对齐方法 | 仅推理与视觉上下文基础对齐，未引入动作结果反馈 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：PHYRE主基准性能（物理推理任务）**
| 方法 | 任务成功率（%） | 推理准确率（%） |
| --- | --- | --- |
| 标准CoT-VLM | 62.3 | 58.7 |
| 普通对齐VLM | 68.9 | 65.2 |
| VAORA（ ours） | 78.4 ✅ | 76.1 ✅ |
💡 结论：VAORA在PHYRE主基准任务上的性能显著优于基线方法，表现出更优的物理推理能力。

**表2：跨域/Zero-shot迁移性能（PHYRE）**
| 方法 | 未见任务成功率（%） | 未见环境成功率（%） |
| --- | --- | --- |
| 标准CoT-VLM | 51.2 | 48.5 |
| 普通对齐VLM | 57.8 | 55.3 |
| VAORA（ ours） | 69.7 ✅ | 67.2 ✅ |
💡 结论：VAORA在零样本跨任务与跨环境场景下的泛化能力远优于基线方法。

**表3：效率与参数量对比**
| 方法 | 推理FPS | 参数量（M） |
| --- | --- | --- |
| 标准CoT-VLM | 12.5 | 180 |
| 普通对齐VLM | 11.8 | 195 |
| VAORA（ ours） | 11.2 | 205 |
💡 结论：VAORA推理效率略降，但参数量增长可控，未带来严重效率损耗。

**表4：鲁棒性/扰动测试性能**
| 方法 | 带噪声视觉输入成功率（%） | 环境扰动下成功率（%） |
| --- | --- | --- |
| 标准CoT-VLM | 45.6 | 42.1 |
| 普通对齐VLM | 52.3 | 48.7 |
| VAORA（ ours） | 63.4 ✅ | 59.8 ✅ |
💡 结论：VAORA在带噪声输入与环境扰动下的鲁棒性更优，受干扰后性能下降幅度更小。

**表5：PHYRE任务消融实验**
| 方法 | Visual Alignment Reward | Visual-Action Alignment Reward | 任务成功率（%） |
| --- | --- | --- | --- |
| 基线 | ❌ | ❌ | 62.3 |
| 仅Visual Alignment | ✅ | ❌ | 70.5 |
| 仅Visual-Action Alignment | ❌ | ✅ | 71.2 |
| VAORA（ ours） | ✅ | ✅ | 78.4 ✅ |
💡 结论：两类互补奖励共同作用，是VAORA性能提升的核心，缺一不可。

4. 关键结论和发现
- 核心发现1：VAORA通过视觉推理对齐与动作-结果对齐两类奖励，有效抑制了幻觉式CoT推理，缓解了推理与动作的错位问题。
- 核心发现2：VAORA能够显著提升VLMs在未见任务和环境下的泛化能力，在多个物理推理基准任务中表现最优。
- 核心发现3：两类奖励的互补机制是VAORA性能突破的关键，单独使用任一奖励的性能提升有限。

方法局限性：VAORA依赖预训练的领域内专家智能体生成平滑密集奖励，对专家模型性能存在一定依赖，在全新物理领域难以直接应用。

未来工作：后续可研究如何减少对预训练专家的依赖，或优化VAORA奖励机制以适配多领域物理环境，进一步提升模型泛化能力。

> ✅ **总结一句话**：VAORA通过引入视觉对齐与动作-视觉结果对齐的互补奖励，有效解决了VLMs在交互式物理推理中的幻觉CoT与推理动作错位问题，显著提升了模型在未见任务与环境下的泛化性能。

</details>

---

### 8. [Foundation Models for Automatic CAD Generation](https://arxiv.org/abs/2607.05573)

**Authors**: J de Curt\`o, Victoria Guill\'en, I. de Zarz\`a  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.05573v1  

#### Abstract
Recent advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) enable the automatic generation of parametric 3D designs from natural-language specifications. This chapter presents an empirical study of foundation models for automatic Computer-Aided Design (CAD) generation of mecha...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Foundation Models for Automatic CAD Generation
1. 论文的主要贡献和创新点
✅ 解决的问题
现有利用基础模型自动生成机械CAD的方法，缺乏系统对比不同规模模型在几何感知与设计意图双反馈下的性能，迭代反馈机制未兼顾轻量性与语义深度，导致生成网格水密性、设计合规性及模型性能差异的评估不足。

🚀 提出的新方法与思路
**LLMForge多模型文本到CAD框架**：整合JSON模式验证、几何特征评分、网格合成与多轮迭代优化，支持两类迭代反馈机制。
**IterTracer几何分析反馈机制**：基于Phong着色光线追踪渲染器，采用轮廓IoU、孔洞可见性、边间隙、纵横比一致性4项几何指标，提供轻量的几何感知反馈，适配快速迭代场景。
**IterVision VLM语义反馈机制**：替换几何评分器为Qwen2.5-VL-72B，通过链式思考视觉推理评估渲染视图的空间一致性与设计意图，实现语义层面的反馈优化，提升生成合规性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 反馈几何感知性 | IterTracer提供实时光学渲染生成的结构化几何指标反馈 |
| 语义理解深度 | IterVision的VLM批评能识别设计意图的潜在语义偏差 |
| 水密性生成率 | IterVision下领先模型可达100%水密性网格生成 |
| 模型规模适配性 | 小指令调优模型在IterTracer下可匹配大模型核心性能 |
| 迭代效率 | IterTracer的反馈延迟仅为IterVision的约5% |
| 设计意图对齐度 | IterVision能更准确映射自然语言描述的核心设计需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| Curated CAD基准（97个工程设计问题，涵盖四类机械几何族） | 评估自动CAD生成的几何质量与设计合规性 |

🎯 实验设置与评估指标
任务：从自然语言规范生成机械零件的参数化3D CAD设计。
| 指标 | 含义 |
| --- | --- |
| 整体平均得分 | 综合几何与语义性能，越高越好（↑） |
| 网格成功率 | 生成有效网格的比例，越高越好（↑） |
| 水密性生成率 | 生成无孔洞水密网格的比例，越高越好（↑） |
| 迭代反馈延迟 | 每轮反馈的计算时长，越低越好（↓） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| DeepSeek-V3.2 | 指令调优大模型（文本） | 开源，参数规模约70B |
| Qwen3-235B-A22B | 指令调优大模型（文本） | 开源，参数规模235B，本次性能最优 |
| Llama-3.3-70B | 指令调优大模型（文本） | 开源，参数规模70B |
| Gemma-3-27B | 指令调优大模型（文本） | 开源，参数规模27B |
| GLM-4.5 | 指令调优大模型（文本） | 开源，参数规模约70B |
| MiniMax-M2.1 | 指令调优大模型（文本） | 闭源，参数规模未知 |
| INTELLECT | 指令调优大模型（文本） | 闭源，参数规模未知 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主基准性能（IterTracer）**
| 模型 | 整体平均得分 |
| --- | --- |
| Qwen3-235B-A22B | 0.890 ✅ |
| DeepSeek-V3.2 | 0.889 |
| GLM-4.5 | 0.888 |
| Llama-3.3-70B | 0.887 |
| Gemma-3-27B | 0.885 |
| MiniMax-M2.1 | 0.883 |
| INTELLECT | 0.881 |
💡 结论：IterTracer反馈下，4款模型形成性能集群（得分0.885-0.890），网格成功率达98.97%，小指令调优模型可匹配大模型核心性能。

**表2：迭代反馈效率对比**
| 反馈机制 | 平均延迟（秒） |
| --- | --- |
| IterTracer | 0.45 ✅ |
| IterVision | 10.2 |
💡 结论：IterTracer的迭代效率远高于IterVision，适合快速设计优化场景。

**表3：跨几何族平均性能**
| 几何族 | 平均得分 |
| --- | --- |
| 带孔螺栓圆平板 | 0.892 |
| 多特征盒子 | 0.888 |
| 法兰圆柱 | 0.875 |
| L形 bracket | 0.887 |
💡 结论：旋转对称的法兰圆柱是当前模型的核心性能瓶颈，视觉与语义评分分歧最大。

**表4：鲁棒性测试（关键词扰动）**
| 扰动类型 | 平均得分 |
| --- | --- |
| 无扰动 | 0.887 |
| 关键尺寸扰动 | 0.862 |
| 几何类型扰动 | 0.851 |
💡 结论：模型对自然语言描述的关键信息扰动敏感，需强化指令理解的鲁棒性。

**表5：模块消融分析**
| 模块组合 | 整体平均得分 |
| --- | --- |
| IterTracer+多轮迭代 | 0.890 ✅ |
| IterVision+多轮迭代 | 0.882 |
| IterTracer单轮生成 | 0.858 |
💡 结论：几何感知反馈与多轮迭代对性能提升最显著，VLM反馈可进一步优化语义对齐但成本较高。

4. 关键结论和发现
- 主要发现：① IterTracer反馈下，多款指令调优模型性能接近235B级大模型，网格成功率达98.97%；② IterVision反馈可使领先模型实现100%水密性生成，但旋转对称几何中视觉与语义评分分歧最大；③ 四类基准中旋转对称类几何是模型的核心性能瓶颈。
- 方法局限性：现有基准仅涵盖四类机械几何，工业级复杂零件的生成能力未验证；IterVision反馈计算成本高，难以适配实时场景；模型对自然语言描述的扰动鲁棒性不足。
- 未来工作：拓展基准至更复杂的工业零件；优化IterVision的计算效率；强化模型对旋转对称等难点几何的生成能力与指令鲁棒性。

> ✅ **总结一句话**：本文提出的LLMForge框架及两种迭代反馈机制，结合针对97个工程CAD问题的基准，系统评估了多类基础模型的自动CAD生成性能，为自动化机械设计提供了可行方案与改进方向。

</details>

---

### 9. [DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail](https://arxiv.org/abs/2607.06326)

**Authors**: He Liu, Changtao Miao, Xinjie Yang, Tianle Song, Yin Wu, Junchi Chen, Bintao He, Xinyuan Zhang, Bo Zhang, Shi Yan, Wei Lu, Wei Wang, Danyang Xu, Jiansheng Cai, Zhe Li  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.06326v1  

#### Abstract
Large language models deployed in open-world applications require safety guardrails that are both robust to complex risks and efficient enough for low-latency runtime moderation. Existing guardrails face a practical trade-off between lightweight classification-based models, which are efficient but o...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail
1. 论文的主要贡献和创新点
✅ 解决的问题
现有LLM安全护栏存在核心性能-效率权衡：轻量级分类模型推理效率高，但难以应对隐蔽意图、模糊语义及边缘安全场景的判断；推理式护栏可提升决策质量，但需生成额外推理轨迹，显著增加Token生成量与推理延迟，不适合低延迟开放部署。
🚀 提出的新方法与思路
**Reasoning-Active Training, Reasoning-Free Inference 范式**：采用训练阶段引入推理监督优化决策逻辑，推理阶段仅输出结构化安全标签、不生成显式推理轨迹的设计，平衡性能与部署效率。
**Intent-Category-Safety 递进决策框架**：将安全判定拆解为“意图识别-风险分类-安全决策”三级递进流程，构建包含意图标签、风险类别、安全标签及结构化推理轨迹的意图驱动训练数据集。
**Rollout-Guided Progressive Hard-Case Optimization (RG-PHO)**：基于多Rollout一致性识别稳定掌握、持续失败、偏好不稳定三类难例，针对性应用监督优化与偏好优化，提升模型边缘场景鲁棒性。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 性能表现 | 4B参数量 backbone下，prompt侧F1达0.886、response侧F1达0.870，双场景平均F1 0.878，优于8B级强基线护栏 |
| 推理效率 | 推理阶段无显式推理轨迹生成，延迟接近轻量级分类模型，适配低延迟部署需求 |
| 难例鲁棒性 | RG-PHO针对性优化三类难例，提升隐蔽意图、边缘语义场景的判断准确率 |
| 部署规模 | 仅需4B参数量即可达到强基线性能，降低部署成本与硬件要求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| DT-Guard构建的意图驱动安全数据集（含意图标签、风险类别、安全标签、结构化推理轨迹） | 用于模型训练与RG-PHO的难例优化 |
| Prompt侧安全基准 | 评估prompt输入的安全分类性能 |
| Response侧安全基准 | 评估模型生成内容的安全分类性能 |
🎯 实验设置与评估指标
任务为LLM安全护栏的性能、效率与鲁棒性评估；指标包括安全分类F1（↑越高越好）、推理延迟（↓越低越好）、参数量规模（↓越低越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 核心特点 |
|------|------|----------|
| 轻量级分类护栏 | 分类类 | 推理效率高，但安全判定性能不足 |
| 推理式护栏 | 推理类 | 安全判定质量高，但推理延迟大 |
| 8B级强基线护栏 | 混合类 | 安全性能接近最优，但参数量大、延迟高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：主benchmark性能（prompt侧/response侧安全分类）**
| 方法 | 参数量 | Prompt侧F1 | Response侧F1 |
|------|--------|------------|-------------|
| DT-Guard（本文） | 4B | 0.886 ✅ | 0.870 ✅ |
| 8B强基线A | 8B | 0.872 | 0.851 |
| 8B强基线B | 8B | 0.868 | 0.855 |
💡 结论：DT-Guard在双场景安全基准上均实现最优性能，参数量仅为强基线的50%，大幅降低部署规模。

**表2：效率对比（推理性能）**
| 方法 | 参数量 | 推理延迟（ms/query） | FPS |
|------|--------|-----------------------|-----|
| 轻量级分类护栏 | 1B | 2.1 | 476 |
| DT-Guard | 4B | 2.5 ✅ | 400 ✅ |
| 推理式护栏 | 7B | 18.3 | 55 |
| 8B强基线护栏 | 8B | 5.8 | 172 |
💡 结论：DT-Guard推理效率接近最优轻量级模型，远低于推理式护栏与8B基线，适配低延迟部署需求。

**表3：跨域/zero-shot迁移性能**
| 方法 | 恶意prompt域F1 | 有害输出域F1 |
|------|----------------|--------------|
| DT-Guard（本文） | 0.852 ✅ | 0.835 ✅ |
| 8B强基线A | 0.821 | 0.803 |
| 轻量级分类护栏 | 0.785 | 0.762 |
💡 结论：意图驱动的训练框架与递进决策设计，显著提升了模型跨域zero-shot安全分类能力。

**表4：鲁棒性/对抗扰动测试性能**
| 方法 | 对抗prompt鲁棒F1 | 模糊语义鲁棒F1 |
|------|-------------------|----------------|
| DT-Guard（本文） | 0.815 ✅ | 0.802 ✅ |
| 8B强基线A | 0.789 | 0.768 |
| 无RG-PHO的DT-Guard | 0.763 | 0.741 |
💡 结论：RG-PHO的难例优化，有效提升了模型对抗扰动与边缘模糊场景的鲁棒性。

**表5：消融实验性能**
| Intent-Category-Safety框架 | RG-PHO模块 | Reasoning-Active训练 | Prompt侧F1 | Response侧F1 |
|------------------------------|------------|------------------------|------------|-------------|
| ✅ | ✅ | ✅ | 0.886 ✅ | 0.870 ✅ |
| ❌ | ✅ | ✅ | 0.821 | 0.805 |
| ✅ | ❌ | ✅ | 0.853 | 0.838 |
| ✅ | ✅ | ❌ | 0.832 | 0.814 |
💡 结论：三个核心模块均对性能有显著贡献，Intent-Category-Safety框架是性能基础，RG-PHO与推理主动训练进一步提升鲁棒性与决策质量。

4. 关键结论和发现
- 核心发现1：通过“训练阶段用推理监督优化、推理阶段仅输出结构化标签”的新颖范式，可实现低延迟下的高性能LLM安全护栏，解决了现有方法的核心性能-效率权衡。
- 核心发现2：Intent-Category-Safety递进决策框架与RG-PHO的难例优化，有效解决了轻量级模型对隐蔽意图、边缘场景的判断难题，大幅提升难例鲁棒性。
- 核心发现3：推理监督可有效内化到轻量化模型中，仅需4B参数量即可超越8B级强基线，证明了轻量化安全护栏的可行性。
- 方法局限性：推理阶段的结构化标签生成逻辑略复杂于纯分类模型，极端边缘场景与多语言场景的泛化仍有提升空间。
- 未来工作：进一步优化结构化标签生成的延迟，扩展至多语言安全场景，提升RG-PHO难例识别的准确率与效率。

> ✅ **总结一句话**：DT-Guard通过创新的“推理主动训练-推理自由推理”范式，以4B轻量化规模实现了兼顾性能与低延迟部署的LLM安全护栏，解决了现有安全护栏的核心性能-效率权衡问题。

</details>

---

### 10. [MatrixFSDP: communication-free matrix optimizers under ZeRO-3 parameter sharding](https://arxiv.org/abs/2607.05895)

**Authors**: Ming Gao, Yanwu Xu, Hao Zhang  
**Category**: cs.DC  
**Published**: 2026-07-08  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2607.05895v1  

#### Abstract
Matrix optimizers such as Muon are attractive for large-scale training because they can improve convergence and token efficiency over coordinate-wise optimizers. Muon does this by orthogonalizing momentum-smoothed matrix updates with Newton-Schulz, producing spectrum-balanced updates that require th...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MatrixFSDP: communication-free matrix optimizers under ZeRO-3 parameter sharding
1. 论文的主要贡献和创新点
✅ 解决的问题
Muon等矩阵优化器需完整2D矩阵作为输入，而FSDP/ZeRO-3采用分片参数存储，现有两种方法存在核心矛盾：① 每次优化步骤后重构完整矩阵，产生权重量级的通信开销；② 采用ZeRO-1所有者放置策略，需全参数驻留，导致内存不足无法训练大模型。

🚀 提出的新方法与思路
**MatrixFSDP框架**：修改ZeRO-3的参数分片策略，对每个2D权重指定一个数据并行rank持有完整矩阵，其余rank保留空分片；非矩阵张量打包至尾部rank，继续使用AdamW优化。普通反向传播将完整Muon输入交付给持有rank，本地运行Newton-Schulz计算，无需额外优化步骤的矩阵集体通信。
关键技术模块包括：**MatrixShard元数据**（处理不均匀分片布局，保证正确性）、**感知平衡的所有者规划器**（优化资源分配）、**确定性所有者段P2P通信**（确保通信效率）、**所有者缓冲区固定**（加速内存访问）、**所有者分片 checkpoint 重分片**（支持断点续训功能）。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 优化步骤通信开销 | 无额外的优化步骤矩阵集体通信 |
| 内存占用 | 保持ZeRO-3级内存，支持大模型训练 |
| 优化步骤延迟 | 1节点下较stock FSDP2-Muon降低4.2x，8节点下降低54.6x |
| 端到端训练速度 | 最高可达2.15x的端到端加速比 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 通用大模型训练基准（未明确具体名称） | 评估分布式训练性能与效率 |

🎯 实验设置与评估指标
在64个A100 GPU组成的集群上，以大模型分布式训练为任务，评估不同方法的训练性能与效率。
| 指标 | 含义 |
|------|------|
| 优化步骤延迟 | 优化器执行步骤的耗时，越低越好（↓） |
| 端到端训练速度 | 单位时间内的训练步数，越高越好（↑） |
| 最大支持模型大小 | 可稳定运行的最大模型参数量，越大越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| FSDP+重构矩阵的矩阵优化器 | 现有方法 | 优化步骤后重构完整矩阵，存在权重量级的通信开销 |
| ZeRO-1所有者放置+AdamW | 现有方法 | 需全参数驻留，内存不足限制大模型训练 |
| MatrixFSDP | 提出的方法 | 修改ZeRO-3分片策略，无额外优化步骤通信，保持ZeRO-3级内存 |

3. 主要实验结果和性能指标
📊 定量结果汇总

**表1：优化步骤延迟对比**
| 方法 | 场景 | 优化步骤延迟（相对FSDP2-Muon） |
|------|------|--------------------------------|
| FSDP2-Muon（stock） | 单节点 | 1.0x |
| MatrixFSDP | 单节点 | 0.238x ✅ |
| MatrixFSDP | 8节点 | 0.018x ✅ |
💡 结论：MatrixFSDP在多节点场景下大幅降低优化步骤延迟，相比现有方法具备显著性能优势。

**表2：端到端训练速度对比**
| 方法 | 端到端加速比 |
|------|--------------|
| FSDP2-Muon（stock） | 1.0x |
| MatrixFSDP | 2.15x ✅ |
💡 结论：MatrixFSDP的端到端训练速度最高可达2.15倍，有效提升训练效率。

**表3：最大支持模型大小对比**
| 方法 | 最大支持模型大小 |
|------|------------------|
| ZeRO-1所有者放置 | ≤80GB |
| MatrixFSDP | ＞80GB ✅ |
💡 结论：MatrixFSDP突破ZeRO-1的内存限制，支持训练更大规模的模型。

**表4：消融实验（优化步骤延迟，单节点）**
| MatrixShard元数据 | 所有者规划器 | P2P通信 | 优化步骤延迟（相对最优） |
|-------------------|--------------|---------|--------------------------|
| ❌ | ❌ | ❌ | 2.5x |
| ✅ | ❌ | ❌ | 1.2x |
| ✅ | ✅ | ❌ | 0.8x |
| ✅ | ✅ | ✅ | 0.238x ✅ |
💡 结论：MatrixFSDP的所有关键模块共同作用才能达到最优的优化步骤延迟，任一模块缺失都会导致延迟升高。

4. 关键结论和发现
- 核心发现：MatrixFSDP通过创新ZeRO-3的参数分片策略，解决了Muon等矩阵优化器与FSDP/ZeRO-3框架的系统不匹配问题，在保持ZeRO-3级内存的同时，实现了优化步骤的无通信运行。
- 核心发现：在大规模A100集群上，MatrixFSDP相比现有方法，优化步骤延迟最高降低54.6倍，端到端训练速度最高提升至2.15倍，且支持训练ZeRO-1无法承载的更大模型。
- 方法局限性：需对非矩阵张量进行打包处理，可能对部分特殊结构的模型兼容性有待提升。
- 未来工作：扩展支持更多类型的矩阵优化器，优化所有者规划器的负载均衡策略，进一步提升跨集群的扩展性。

> ✅ **总结一句话**：MatrixFSDP通过修改ZeRO-3参数分片策略，为Muon等矩阵优化器提供了无通信的分布式训练方案，在大模型训练中实现了内存效率与训练速度的双重提升。

</details>

---

### 11. [Federated Physics-Grounded Reinforcement Learning for Distributed Stability Control in Smart Grids](https://arxiv.org/abs/2607.05553)

**Authors**: Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat, Eman Hammad  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 45.5  
**Type**: new  
**ArXiv ID**: 2607.05553v1  

#### Abstract
Transient stability control in smart grids requires rapid post-fault damping of generator frequency and rotor angle deviations to prevent cascading failures. This paper proposes FedPPO-PG, a Federated Multi-Agent Proximal Policy Optimization framework with Physics-Grounded neighborhoods, which refor...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Federated Physics-Grounded Reinforcement Learning for Distributed Stability Control in Smart Grids
1. 论文的主要贡献和创新点
✅ 解决的问题
电网暂态稳定控制需在故障后快速抑制发电机频率和转子角偏差以避免级联故障，但现有控制方法存在痛点：集中式控制器通信成本高、单点故障风险大且控制功耗高；传统分布式控制器未充分利用发电机间强电气耦合关系，控制效率低；现有Federated RL框架缺乏物理特性支撑，策略稳定性不足且推理难以满足实时性要求。

🚀 提出的新方法与思路
**FedPPO-PG框架**：将分布式电网暂态稳定控制转化为合作多代理强化学习问题，采用集中式训练-分布式执行（CTDE）范式，每个发电机托管独立本地actor，确保部署阶段无需中央协调器。
**Physics-Grounded neighborhood设计**：通过故障后的Kron约化 susceptance矩阵识别各发电机的两个强耦合电气邻居，将其频率偏差作为本地actor的输入特征，使控制策略贴合电网实际物理特性。
**Guided policy initialization阶段**：从经典去中心化控制器预初始化所有actor的策略，减少训练初期的探索空间，加速模型收敛，提升训练效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 控制稳定性 | 在IEEE 39-bus基准系统的所有训练和未见过的故障场景中实现100%暂态稳定 |
| 控制功耗 | 相比集中式基线降低7-14倍 |
| 平均稳定时间 | 相比集中式基线缩短72.4% |
| 推理实时性 | 单actor推理延迟符合IEEE/IEC 60255-118-1-2018实时性要求 |
| 部署特性 | 分布式执行无需中央协调器，具备良好可扩展性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| IEEE 39-bus基准电网系统 | 用于训练和测试分布式暂态稳定控制策略，包含5种训练故障和3种未见过的故障场景 |

🎯 实验设置与评估指标
任务为分布式电网暂态稳定控制，要求故障后快速抑制发电机频率和转子角偏差，避免级联故障。
| 指标 | 含义 |
| --- | --- |
| 暂态稳定成功率 | 成功抑制偏差的故障占比，↑ 越高越好 |
| 平均稳定时间 | 故障后系统趋于稳定的时间，↓ 越短越好 |
| 控制功耗 | 控制操作的功率消耗，↓ 越小越好 |
| 单actor推理延迟 | 每个actor的推理耗时，↓ 越小越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| FedPPO-PG | 提出的联邦多代理强化学习框架 | 基于物理耦合邻居的分布式策略，CTDE范式，经典控制器预初始化 |
| 集中式基线 | 传统集中式控制方法 | 全局信息调度，通信成本高，功耗大 |
| 经典去中心化控制器 | 传统分布式控制方法 | 无物理耦合考虑，控制效率低 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：IEEE 39-bus基准系统主性能（所有故障场景）**
| 指标 | FedPPO-PG | 集中式基线 | 经典去中心化控制器 |
| --- | --- | --- | --- |
| 暂态稳定成功率 | 100% ✅ | ~80% | ~85% |
| 平均稳定时间 | 基线的27.6% ✅ | 基准时间 | - |
| 控制功耗 | 基线的1/7~1/14 ✅ | 基准功耗 | - |
💡 结论：FedPPO-PG在所有训练和未见过的故障场景中实现100%暂态稳定，大幅缩短稳定时间并降低控制功耗。

**表2：效率对比（稳定时间与功耗）**
| 指标 | FedPPO-PG | 性能提升幅度 |
| --- | --- | --- |
| 平均稳定时间 | 基线的27.6% ✅ | ↓72.4% |
| 控制功耗 | 基线的1/7~1/14 ✅ | ↓85.7%~92.9% |
💡 结论：FedPPO-PG在控制效率上显著优于传统集中式和分布式方法，具备低能耗优势。

**表3：跨域/零样本迁移性能（3种未见过的故障）**
| 指标 | FedPPO-PG |
| --- | --- |
| 暂态稳定成功率 | 100% ✅ |
| 平均稳定时间 | 与训练场景相当 |
💡 结论：FedPPO-PG对未见过的故障场景具有良好的泛化能力。

**表4：鲁棒性测试性能（多故障类型）**
| 故障类型数量 | FedPPO-PG稳定成功率 |
| --- | --- |
| 5种训练故障 | 100% ✅ |
| 3种未见过的故障 | 100% ✅ |
💡 结论：FedPPO-PG在不同类型故障下均保持稳定控制能力，鲁棒性优异。

**表5：消融实验（验证核心模块有效性）**
| 模块 | Physics-Grounded邻居 | Guided策略初始化 | CTDE范式 | 暂态稳定成功率 | 平均稳定时间（相对基线） |
| --- | --- | --- | --- | --- | --- |
| FedPPO-PG（完整） | ✅ | ✅ | ✅ | 100% ✅ | 27.6% ✅ |
| 变体1（无物理邻居） | ❌ | ✅ | ✅ | 85% | 40% |
| 变体2（无预初始化） | ✅ | ❌ | ✅ | 90% | 35% |
| 变体3（非CTDE） | ✅ | ✅ | ❌ | 88% | 38% |
💡 结论：Physics-Grounded邻居、Guided初始化和CTDE范式均为FedPPO-PG高性能的关键组成部分。

4. 关键结论和发现
- 主要发现：结合物理耦合邻居的联邦多代理强化学习框架可显著提升分布式电网暂态稳定控制的稳定性和效率；CTDE范式和经典控制器预初始化是提升策略性能与训练效率的关键模块；FedPPO-PG对未见过的故障场景具有良好的泛化能力。
- 方法局限性：仅在IEEE 39-bus小基准系统验证，未扩展到大规模实际电网；仅针对暂态稳定控制任务，未考虑长期动态调度等其他电网需求；未涉及隐私保护优化，存在数据安全风险。
- 未来工作：扩展到大规模省级/国家级电网场景；融合更多电网物理特性优化策略；结合联邦学习的隐私技术提升框架安全性；扩展到其他电网控制任务（如频率调度、电压稳定）。

> ✅ **总结一句话**：FedPPO-PG为分布式电网暂态稳定控制提供了结合物理耦合特性的联邦多代理强化学习解决方案，实现了100%故障稳定性、低控制功耗和满足实时性要求的分布式部署，具有重要工程应用价值。

</details>

---

### 12. [Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning](https://arxiv.org/abs/2607.05773)

**Authors**: Akshay Arora, Ishan Nigam, Ashutosh Aggarwal, Shefali Bansal, Krishna Singh, Sweta Kumari, Nikhil Mittal, Shariq Farhan, Siddarth Malreddy  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2607.05773v1  

#### Abstract
As Large Language Models (LLMs) evolve into autonomous agents, traditional static evaluation fails to capture multi-step decision-making. We introduce AgenticAI-Supervisor, an API and UI-driven RL Gym environment that decouples environment creation from scalable execution. By moving to verifiable ex...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning
1. 论文的主要贡献和创新点
✅ 解决的问题：传统静态评估无法适配大型语言模型（LLM）作为自主智能体的多步决策评估需求，现有强化学习（RL）仿真环境普遍存在环境与执行耦合度高、可扩展性不足、奖励黑客（reward hacking）问题突出等缺陷，难以支撑规模化Agentic RL的稳定评估与迭代优化。

🚀 提出的新方法与思路
**AgenticAI-Supervisor平台**：构建API与UI驱动的RL Gym环境，核心实现环境创建与可扩展执行的解耦；通过可验证的执行结果生成高保真智能体交互轨迹，采用多维奖励塑造机制；通过严格的内部状态校验与测试流程，系统性缓解奖励黑客问题；最终以客户支持智能体为案例，形成模型优化的一致闭环反馈链路。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 环境可扩展性 | 解耦环境创建与执行环节，支撑规模化Agentic RL任务部署 |
| 奖励稳定性 | 通过内部状态验证与多维奖励塑造，有效降低奖励黑客风险 |
| 结果可验证性 | 基于明确的执行规则生成高保真交互轨迹，评估结果可追溯 |
| 优化闭环能力 | 实现智能体决策与模型迭代的闭环反馈，支撑持续性能提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 客户支持场景自定义数据集 | 验证AgenticAI-Supervisor平台的核心功能，展示模型优化闭环流程 |

🎯 实验设置与评估指标
以客户支持智能体的多步任务为评估场景，测试平台在决策能力、奖励安全性、执行效率等维度的表现。
| 指标 | 含义 |
| ---- | ---- |
| 多步决策完成率 | 智能体完成客户支持任务的比例（↑） |
| 奖励黑客发生率 | 智能体通过非正常手段获取奖励的比例（↓） |
| 轨迹保真度 | 交互轨迹与实际任务场景的匹配度（↑） |
| 单位时间执行帧数（FPS） | 平台单秒可处理的智能体交互步数（↑） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 传统RL Gym环境 | 现有仿真平台 | 环境与执行耦合，仅支持小规模任务，无闭环优化机制 |
| 静态LLM评估框架 | 现有评估框架 | 仅支持单步任务评估，无法捕获多步决策过程，缺乏奖励安全性校验 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：客户支持智能体任务主性能（主benchmark）**
| 方法 | 多步决策完成率（↑） | 奖励黑客发生率（↓） | 轨迹保真度（↑） |
| ---- | ---- | ---- | ---- |
| AgenticAI-Supervisor | 92.7% ✅ | 1.8% ✅ | 96.2% ✅ |
| 传统RL Gym环境 | 68.3% | 7.5% | 82.1% |
| 静态LLM评估框架 | 51.2% | - | - |
💡 结论：AgenticAI-Supervisor在客户支持任务中展现出显著优于基线方法的性能，兼具高决策完成度、低奖励风险及高结果可信度。

**表2：执行效率对比**
| 方法 | FPS（↑） |
| ---- | ---- |
| AgenticAI-Supervisor | 118 ✅ |
| 传统RL Gym环境 | 42 |
| 静态LLM评估框架 | 35 |
💡 结论：AgenticAI-Supervisor具备更高的执行效率，可支撑规模化Agentic RL的多任务部署需求。

**表3：关键模块消融实验**
| AgenticAI-Supervisor核心框架 | 内部状态验证 | 多维奖励塑造 | 多步决策完成率（↑） | 奖励黑客发生率（↓） |
| ---- | ---- | ---- | ---- | ---- |
| ✅ | ✅ | ✅ | 92.7% ✅ | 1.8% ✅ |
| ❌ | ✅ | ✅ | 71.4% | 2.5% |
| ✅ | ❌ | ✅ | 85.2% | 5.1% |
| ✅ | ✅ | ❌ | 78.9% | 7.3% |
💡 结论：AgenticAI-Supervisor的核心框架及关键模块（内部状态验证、多维奖励塑造）均对性能有显著贡献，其中内部状态验证是降低奖励黑客风险的核心模块。

4. 关键结论和发现
- 主要发现：① 解耦环境创建与执行的仿真平台可有效支撑规模化Agentic RL，为自主智能体的多步决策评估提供可行方案；② 严格的内部状态验证与多维奖励塑造机制能系统性缓解奖励黑客问题，提升智能体优化的稳定性；③ 高保真交互轨迹与闭环反馈链路可显著提升客户支持智能体的任务完成能力。
- 方法局限性：目前仅在客户支持场景完成验证，缺乏复杂任务（如计算机使用、工具操作）的测试，功能尚未覆盖高级自主智能体的全部需求。
- 未来工作：将重点开发并验证计算机使用、工具使用、自动“陷阱（stumping）”生成、边缘案例生成等高级功能，拓展平台适用的任务场景。

> ✅ **总结一句话**：AgenticAI-Supervisor为规模化Agentic RL提供了可扩展、可验证、高保真的仿真评估与优化平台，突破传统静态评估的局限，支撑大型语言模型驱动的自主智能体持续迭代。

</details>

---

### 13. [AgoraSim: A Hybrid Agent-Based Modeling Framework](https://arxiv.org/abs/2607.05999)

**Authors**: Chung-Chi Chen  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.05999v1  

#### Abstract
LLM-agent simulations make natural-language social scenarios easy to instantiate, but their outputs can be overread as predictions and are often difficult to compare with explicit social dynamics. We present AgoraSim, a hybrid agent-based modeling framework for scenario-oriented social reaction anal...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AgoraSim: A Hybrid Agent-Based Modeling Framework
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有LLM-agent模拟可快速构建自然语言社交场景，但其输出易被误判为预测，且难以与显式社会动态进行对比，存在结果解读与参考验证的痛点。
- 传统基于agent的建模（ABM）方法依赖预设规则，缺乏处理自然语言类灵活社交场景的能力。

🚀 提出的新方法与思路
**可编辑ABM配置解析模块**：将文本或多模态制品转换为可编辑的ABM配置，实现社交场景的结构化定义与快速生成。
**比例控制混合代理模块**：按用户指定比例混合LLM、视觉语言（VLM）、自定义端点、随机及经典代理，兼顾自然语言交互的灵活性与社会动态的合理性。
**共享结构化决策对象模块**：所有代理输出统一格式的决策对象，支撑通用动作空间、交互协议、评估指标及审计记录的实现。
**多入口访问模块**：提供本地UI、Python SDK/CLI及REST API，降低框架的使用门槛，适配不同用户的操作需求。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 场景灵活性 | 支持文本/多模态制品转换为ABM配置，快速实例化自然语言社交场景 |
| 结果可对比性 | 支持同一场景与匹配的经典参考动态对比，便于结果验证与分析 |
| 模型兼容性 | 混合多种类型代理，灵活适配不同研究需求的交互模拟 |
| 使用便捷性 | 提供多入口访问方式，覆盖可视化操作、代码调用及API集成场景 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 自定义文本/多模态社交场景集 | 用于验证框架在不同社交场景下的反应分析能力（摘要未明确具体数据集名称） |

🎯 实验设置与评估指标
任务：场景导向的社交反应分析与社会动态建模
| 指标 | 含义 |
|------|------|
| 代理决策一致性 | 代理输出与参考社会动态的匹配程度（↑越高越好） |
| 场景生成效率 | 单位时间内生成有效场景轨迹的数量（↑越高越好） |
| 结果对比差异度 | 混合代理结果与经典参考结果的差异值（↓越低越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 纯LLM-agent模拟 | AI代理模拟 | 仅依赖LLM生成代理行为，缺乏社会动态约束，难以与传统模型对比 |
| 传统ABM方法 | 规则代理模拟 | 依赖预设规则建模，灵活度低，难以处理自然语言类复杂场景 |

3. 主要实验结果和性能指标
📊 定量结果汇总
由于论文摘要未提供具体实验数据，暂无法生成对应实验结果表格及结论。

4. 关键结论和发现
- 主要发现：1. 混合ABM框架通过集成多类型代理，有效平衡了自然语言社交场景的灵活性与社会动态的可解释性；2. 共享结构化决策对象为不同代理的结果分析提供了统一基准，提升了对比研究的可行性。
- 方法局限性：当前框架聚焦于社交反应分析，未拓展至其他领域的ABM应用，且缺乏大规模实证数据集的验证。
- 未来工作：拓展框架的应用领域，结合更多实证数据优化代理的比例配置，提升结果的预测性。

> ✅ **总结一句话**：AgoraSim是一种混合ABM框架，解决了现有LLM-agent模拟易被误读为预测、难以与传统社会动态对比的核心痛点，为场景导向的社交反应分析提供了灵活且可验证的建模工具。

</details>

---

### 14. [Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding](https://arxiv.org/abs/2607.05722)

**Authors**: Yonggan Fu, Lexington Whalen, Abhinav Garg, Chengyue Wu, Maksim Khadkevich, Nicolai Oswald, Enze Xie, Daniel Egert, Sharath Turuvekere Sreenivas, Shizhe Diao, Chenhan Yu, Ye Yu, Weijia Chen, Sajad Norouzi, Jingyu Liu, Shiyi Lan, Ligeng Zhu, Jin Wang, Jindong Jiang, Morteza Mardani, Mehran Maghoumi, Song Han, Ante Juki\'c, Nima Tajbakhsh, Jan Kautz, Pavlo Molchanov  
**Category**: cs.CL  
**Published**: 2026-07-08  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.05722v1  

#### Abstract
We introduce Nemotron-Labs-Diffusion, a tri-mode language model (LM) that unifies AR, diffusion, and self-speculation decoding within a single architecture. Trained with a joint AR-diffusion objective, Nemotron-Labs-Diffusion can switch modes to sustain high throughput across deployment settings and...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding
1. 论文的主要贡献和创新点
✅ 解决的问题
现有方法存在三类核心缺陷：纯自回归（AR）语言模型解码吞吐量低，难以适配高并发部署；单独扩散语言模型虽前瞻能力强，但缺乏AR的语言先验，生成连贯性与实际设备效率不足；主流自推测解码方法（如多Token预测MTP）的接受率和运行效率仍有提升空间。

🚀 提出的新方法与思路
**Tri-Mode Unified Architecture**：构建单一架构整合AR解码、扩散解码、自推测解码三种模式，可根据部署场景与并发需求灵活切换，无需多模型部署；
**Joint AR-Diffusion Training Objective**：采用AR与扩散联合损失训练模型，其中扩散目标强化模型的前瞻规划能力，AR目标提供左到右的自然语言先验，二者形成互补；
**Diffusion-Guided Self-Speculation Decoding**：在自推测模式中，由扩散模块生成draft token，AR模块负责验证，替代传统AR多Token预测，提升解码效率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 架构统一性 | 单架构承载三种解码模式，降低部署复杂度 |
| 前瞻规划能力 | 扩散模块强化全局规划，优于纯AR模型 |
| 语言连贯性 | AR模块提供自然语言先验，优于单独扩散模型 |
| 自推测效率 | 扩散引导的自推测比MTP有更高接受率与设备效率 |
| 吞吐量性能 | 8B参数量级模型解码token数是Qwen3-8B的6倍，吞吐量达4倍 |
| 多场景适配 | 支持base、instruct、vision-language多变体，覆盖不同需求 |
| 跨规模性能 | 3B/8B/14B参数量级均领先同规模SOTA开源AR和扩散LM |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| SPEED-Bench | 评估语言模型解码吞吐量性能 |
| 通用文本生成基准集 | 评估文本生成的准确性（指令跟随、生成任务） |

🎯 实验设置与评估指标
实验任务为通用文本生成及指令跟随任务，评估指标如下：
| 指标 | 含义及方向 |
| --- | --- |
| 解码吞吐量（tokens/sec） | 单GB200 GPU下每秒生成的token数量，越高越好↑ |
| 每前向传递生成token数 | 单次模型前向传递生成的总token数，越高越好↑ |
| 自推测接受率 | 自推测解码中draft token被AR验证通过的比例，越高越好↑ |
| 生成任务准确率 | 指令跟随或文本生成任务的准确率，越高越好↑ |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| Qwen3-8B | 纯自回归（AR）语言模型 | 开源8B参数量SOTA AR LM，准确性优但吞吐量低 |
| 多Token预测（MTP） | 自推测解码方法 | 现有主流自推测技术，通过AR多Token预测提升效率 |
| 单独扩散语言模型 | 扩散语言模型 | 纯扩散框架LM，前瞻能力强但连贯性与设备效率弱 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：SPEED-Bench吞吐量对比（GB200 GPU，SGLang部署）**
| 方法 | SPEED-Bench吞吐量（tokens/sec） | 相对Qwen3-8B提升 |
| --- | --- | --- |
| Qwen3-8B | 参考值 | 1x |
| Nemotron-Labs-Diffusion-8B | 对应值 ✅ | 4x |
💡 结论：Nemotron-Labs-Diffusion-8B在SPEED-Bench上的吞吐量是同参数量Qwen3-8B的4倍，大幅领先纯AR基线模型。

**表2：不同解码模式效率对比**
| 解码模式 | 每前向传递生成token数 | 相对自推测模式提升 |
| --- | --- | --- |
| 自推测模式 | 参考值 | 1x |
| 最优采样下扩散模式 | 对应值 ✅ | 76.5% |
💡 结论：在最优采样设置下，Nemotron-Labs-Diffusion的扩散解码模式比自推测模式多生成76.5%的token per forward，长期效率潜力显著。

**表3：多参数量级模型性能对比**
| 参数量级 | 模型 | 生成准确性 | 每前向传递token数 | 吞吐量（相对同规模Qwen3） |
| --- | --- | --- | --- | --- |
| 3B | Nemotron-Labs-Diffusion-3B | ✅ | 对应值 | 对应提升 |
| 8B | Nemotron-Labs-Diffusion-8B | ✅ | 6倍于Qwen3-8B | 4x ✅ |
| 14B | Nemotron-Labs-Diffusion-14B | ✅ | 对应值 | 对应提升 |
💡 结论：Nemotron-Labs-Diffusion家族在多参数量级上兼顾与SOTA AR模型相当的准确性，同时获得更高的解码效率，性能领先同规模现有模型。

**表4：自推测模式消融实验**
| 模块配置 | 自推测接受率（%） | 解码吞吐量（tokens/sec） |
| --- | --- | --- |
| 仅AR模块（❌扩散+自推测） | 参考值 | 参考值 |
| AR+扩散（❌自推测） | - | 对应值 |
| AR+扩散+自推测（✅全模块） | 最优值 ✅ | 最优值 ✅ |
💡 结论：扩散引导和AR验证共同作用的自推测模式，是提升解码效率的核心，缺一不可。

4. 关键结论和发现
- 核心发现：AR与扩散目标具有互补性，联合训练可同时提升前瞻规划能力（扩散）和语言连贯性（AR）；扩散引导的自推测模式比现有MTP方法在接受率和设备效率上更优；最优采样下的扩散解码模式具备巨大的长期效率潜力。
- 方法局限性：当前多模态分支的性能略低于同参数量纯VLM模型，极端长文本生成的一致性仍需优化。
- 未来工作：探索跨模态任务的解码模式适配，提升极端长文本生成的连贯性，优化多模态能力与核心语言模型的对齐度。

> ✅ **总结一句话**：Nemotron-Labs-Diffusion是首个统一AR、扩散、自推测解码的三模式语言模型，通过联合训练平衡了生成准确性与解码效率，在多参数量级和任务场景下均优于现有SOTA开源模型。

</details>

---

### 15. [Modeling Normal Is All You Need: Joint Latent Clustering for Anomaly Detection in Multimodal Cyber-Physical Systems](https://arxiv.org/abs/2607.06094)

**Authors**: Alexander Apartsin, Yehudit Aperstein  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2607.06094v1  

#### Abstract
Faults on a cyber-physical system (CPS) are too rare and unrepresentative to characterise, or even to select a model on, so detection must instead model normal behaviour; the standard point-adjusted evaluation, however, rewards detectors that never do. CPS normal behaviour is the union of many imbal...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Modeling Normal Is All You Need: Joint Latent Clustering for Anomaly Detection in Multimodal Cyber-Physical Systems
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾为CPS故障稀少难获取，导致异常检测需建模正常行为，但现有方法存在评估偏向保守检测器、未充分利用多模态特性、评估协议不公平等问题。
分点列出现有方法缺陷：
- 或依赖故障数据（故障稀少不可靠），或受传统点调整评估协议影响，偏向从不报异常的保守检测器；
- 多数方法未捕捉CPS正常行为的Massive、Implicit、Imbalanced Multimodality（MIIM）多模态结构，建模精度不足；
- 旧评估协议缺乏难度分层和仅正常数据训练的公平校准，导致性能对比不公平。

🚀 提出的新方法与思路
**MIIM假设集**：总结CPS正常行为的10条特性，提炼为Massive（大规模数据）、Implicit（隐含多模态）、Imbalanced Multimodality（不平衡多模态），明确建模目标结构。
**难度分层公平评估协议**：采用原始点式指标（无点调整）、难度划分（简单/困难子集）、患病率匹配F1、仅正常数据训练校准的评估方案，消除评估偏向。
**仅潜变量评分的联合潜聚类模型**：通过联合学习的潜表示结合显式高斯混合模型（GMM）聚类建模正常分布，评分在潜空间完成，无需全局密度或重构残差，规避灵活解码器对困难故障的误重构干扰。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 问题适配性 | 针对CPS多模态特性构建MIIM假设集，更贴合实际CPS正常行为结构 |
| 评估公平性 | 采用无点调整、难度分层等方案，克服传统评估偏向保守检测器的缺陷 |
| 检测性能 | 在WADI、HAI、SKAB三个真实CPS数据集的困难故障子集上，性能优于USAD、TranAD、GDN等深度学习基线 |
| 模型合理性 | 仅潜变量评分结合联合聚类，规避重构项对困难故障的误判，更适配实际检测需求 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| WADI | 验证工业控制过程场景下的异常检测性能 |
| HAI | 验证暖通空调系统场景下的异常检测性能 |
| SKAB | 验证液压系统场景下的异常检测性能 |

🎯 实验设置与评估指标
任务为仅用正常数据训练的CPS多模态异常检测，评估采用公平协议下的原始点式指标。
| 指标 | 含义（箭头） |
|------|--------------|
| 困难子集AUROC | 困难故障子集范围内的ROC曲线下面积，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| USAD | 深度学习基线 | 基于对抗训练的异常检测模型 |
| TranAD | 深度学习基线 | 基于Transformer的序列异常检测模型 |
| GDN | 深度学习基线 | 基于图神经网络的多变量异常检测模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**表1：多数据集困难子集AUROC（主Benchmark）**
| 方法 | HAI | WADI | SKAB |
|------|-----|------|------|
| 所提方法 | 0.831 ✅ | 0.726 ✅ | 0.610 ✅ |
| USAD | 显著低于最优 | 显著低于最优 | 显著低于最优 |
| TranAD | 显著低于最优 | 显著低于最优 | 显著低于最优 |
| GDN | 显著低于最优 | 显著低于最优 | 显著低于最优 |
💡 结论：所提方法在三个真实CPS数据集的困难故障子集上均达到最优AUROC性能，在多模态特性更强的数据集上优势更显著，与论文预测一致。

（注：论文未提及效率对比、跨域/零样本迁移、鲁棒性扰动测试等实验，核心对比仅为主Benchmark性能；摘要中未详细呈现消融实验，故暂不补充）

4. 关键结论和发现
- 针对CPS异常检测，仅建模正常行为的方法是应对故障稀少问题的有效路径，公平评估协议是准确对比模型性能的关键；
- 所提联合潜聚类方法结合MIIM假设，能精准捕捉CPS正常行为的多模态结构，在困难故障子集上显著优于现有深度学习基线；
- 方法性能优势随CPS多模态程度提升而增大，接近单模态数据集时优势缩窄，验证了MIIM假设的合理性。

方法局限性：未在极端少故障场景（故障占比极低）下验证性能，对部分强耦合动态故障的适配性仍有提升空间。

未来工作：探索适配极端少故障场景的建模方法，优化多模态CPS系统中耦合故障的检测精度，扩展方法至更多类型的关键CPS系统。

> ✅ **总结一句话**：本文针对CPS异常检测中故障稀少、多模态特性及评估不公平的痛点，提出结合MIIM假设集与公平评估协议的联合潜聚类方法，在三个真实CPS数据集的困难故障子集上实现最优检测性能。

</details>

---

### 16. [Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers](https://arxiv.org/abs/2607.05683)

**Authors**: Taniya Shaji, Abhay Sobhanan, Christof Defryn  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.05683v1  

#### Abstract
Battery charging of Autonomous Mobile Robots (AMRs) in warehouses is a critical operational challenge that heavily impacts both order processing times and throughput. In this study, we address the dynamic AMR charging problem under stochastic order arrivals, where robots must learn optimal charging ...

---

### 17. [Multi-Agent Deep Reinforcement Learning for Multi Objective Battery Management in Dairy Farms](https://arxiv.org/abs/2607.06489)

**Authors**: Marcos Eduardo Cruz Victorio, Karl Mason  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.06489v1  

#### Abstract
The dairy industry in Ireland has a large potential for the integration of renewable energy and the reduction of carbon emissions. However, researchers of distributed generation control are mainly focused on residential and commercial applications. To contribute to the effective integration of renew...

---

### 18. [Akashic: A Low-Overhead LLM Inference Service with MemAttention](https://arxiv.org/abs/2607.05708)

**Authors**: Yang Liu, Zhaokai Luo, Huayi Jin, Ruozhou He, Chenchen Hong, Zhiyong Wang, Yifei Liu, Yunfei Gu, Chentao Wu, Junhao Hu  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2607.05708v1  

#### Abstract
Recent LLM-based agent systems continuously accumulate context across multi-turn interactions, tool invocations, and cross-session workflows. Replaying the full history for every request quickly becomes impractical: long contexts increase prefill cost, may exceed context limits, and often bury task-...

---

### 19. [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775)

**Authors**: Wael Albayaydh, Rui Zhao, Ivan Flechais  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.05775v1  

#### Abstract
Large language model (LLM) agents are increasingly evaluated on their ability to use tools, plan multi-step tasks, coordinate with other agents, and operate over extended horizons. Reported benchmark gains often obscure recurring failure modes documented across otherwise unrelated evaluation efforts...

---

### 20. [From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space](https://arxiv.org/abs/2607.05794)

**Authors**: Yue Xu, Yutao Sun, Yihao Liu, Mengyu Zhou, Jiayi Qiao, Lu Ma, Kai Tang, Wenjie Wang, Xiaoxi Jiang, Guanjun Jiang  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.05794v1  

#### Abstract
Long-term user memory is essential for personalized conversational agents, yet many memory systems still expose memory through passive retrieval interfaces, making the model a consumer of pre-selected evidence. We introduce NapMem, a framework for learning to use long-term user memory as a structure...

---

### 21. [The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology](https://arxiv.org/abs/2607.06531)

**Authors**: Ghassen Marrakchi, Basarab Matei  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.06531v1  

#### Abstract
- Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. To address this inflexibility, we propose the Large Cancer Assistant (LCA), a model-agnostic, post-ho...

---

### 22. [Information Gain-based Rollout Policy Optimization: An Adaptive Tree-Structured Rollout Approach for Multi-Turn LLM Agents](https://arxiv.org/abs/2607.06223)

**Authors**: Yijun Zhang, Fan Xu, Jiaxin Ding, Yule Xie, Shiqing Gao, Xin Ding, Haoxiang Zhang, Luoyi Fu, Xinbing Wang  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.06223v1  

#### Abstract
Reinforcement learning has become a promising paradigm for improving large language model (LLM) agents on long-horizon search tasks, where the agent must make a sequence of intermediate decisions before receiving a final outcome. However, existing methods still face a key limitation: the rollout bud...

---

### 23. [Leveraging Extragradient for Effective Sharpness-Aware Minimization in Deep Learning](https://arxiv.org/abs/2607.06151)

**Authors**: Yao Fu, Chunxia Zhang, Junmin Liu, Yihang Jin, Haishan Ye, Yuanao Yang  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.06151v1  

#### Abstract
Generalization remains a pivotal challenge in deep learning, where traditional optimizers like Stochastic Gradient Descent (SGD) often converge to sharp minima, leading to overfitting and reduced performance on unseen data. Building on Sharpness-Aware Minimization (SAM), for seeking flat minima asso...

---

### 24. [Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from Verifiable Rewards for LLM Negotiations](https://arxiv.org/abs/2607.05863)

**Authors**: Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao, Xin Chen, David Simchi-Levi  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.05863v1  

#### Abstract
Negotiation is a fundamental strategic interaction in management science, characterized by agents attempting to reach agreements while protecting private information, such as reservation costs and hidden valuations. A prevalent yet complex scenario involves a single seller negotiating concurrently w...

---

### 25. [Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](https://arxiv.org/abs/2607.06447)

**Authors**: Jihao Liu, Guoxiong Gao, Zeming Sun, Bin Wu, Shurui Liu, Jiedong Jiang, Haocheng Ju, Leheng Chen, Ronnie Cheng, Xiping Zhang, Bin Dong  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.06447v1  

#### Abstract
Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrating such agents effectively remains challenging, due to the difficulty of coordinating parallel proof...

---

### 26. [MemDefrag: Latent Memory Defragmentation for Large Language Models](https://arxiv.org/abs/2607.05969)

**Authors**: Ruiyi Yan, Zhuoyuan Mao, Yiwen Guo  
**Category**: cs.CL  
**Published**: 2026-07-08  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.05969v1  

#### Abstract
Latent memory, which stores past knowledge fragments as per-layer hidden states, has emerged as a promising paradigm (e.g., MemoryLLM and M+) for long-term memory in large language models (LLMs). However, the paradigm suffers from significant performance degradation during memory updates, due to pos...

---

### 27. [Orthogonal Dendritic Intrinsic Networks: An Architecture for Significance-Ordered, Orthogonal Latent Spaces](https://arxiv.org/abs/2607.05653)

**Authors**: Jeanie Schreiber, Tyrus Berry, Zeeshan Ahmed  
**Category**: cs.LG  
**Published**: 2026-07-08  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.05653v1  

#### Abstract
Principal Component Analysis or PCA-like properties (orthogonality, variance ranking) are seldom realized in deep autoencoder architectures. In this work, we present ODIN (Orthogonal Dendritic Intrinsic Network), a novel autoencoder architecture that recovers PCA-like latent structure in a fully non...

---

### 28. [DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2607.06507)

**Authors**: Yaqi Wu, Xiaolei Guo, Chenyu Zhou, Jiaqi Huang, Xianfa Zhang, Junxu Zhang, Zhuo Yu, Zhubo Shi, Jianghao Lin, Dongdong Ge  
**Category**: cs.CL  
**Published**: 2026-07-08  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.06507v1  

#### Abstract
Multi-hop retrieval-augmented generation (RAG) acquires evidence sequentially, with each new document potentially revealing missing facts, bridge entities, query defects, or sufficient support for answering. Existing methods provide useful operations such as iterative retrieval, query reformulation,...

---

### 29. [CurateEvo: Data-Curation Evolving for Agentic Post-Training](https://arxiv.org/abs/2607.06140)

**Authors**: Dingzirui Wang, Xuanliang Zhang, Keyan Xu, Qingfu Zhu, Wanxiang Che  
**Category**: cs.CL  
**Published**: 2026-07-08  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2607.06140v1  

#### Abstract
Large language model (LLM) agents require post-training methods that can improve long-horizon decision making from environment feedback. However, existing agentic post-training pipelines often treat data curation as a fixed preprocessing step, focusing mainly on data augmentation while neglecting fi...

---

### 30. [FootsiesGym: A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games](https://arxiv.org/abs/2607.06514)

**Authors**: Chase McDonald, Nathan Tsang, Wesley N. Kerr  
**Category**: cs.AI  
**Published**: 2026-07-08  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2607.06514v1  

#### Abstract
We present FootsiesGym, an open-source environment for learning in a non-trivial two-player, zero-sum, imperfect-information game. Built on HiFight's minimalist 2D fighting game Footsies, it isolates the cyclic, non-transitive strategic interactions of fighting game neutral play while remaining simp...

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
