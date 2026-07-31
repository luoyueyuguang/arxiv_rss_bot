# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-07-31 08:45:41 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/abs/2607.28150v1)

**Authors**: Xuchuan Luo, Jiacheng Shen, Xin Wang, Yangfan Zhou  
**Category**: cs.DC  
**Published**: 2026-07-31  
**Score**: 99.0  
**Type**: new  
**ArXiv ID**: 2607.28150v1  

#### Abstract
Disaggregating the prefill and decoding stages of large language model (LLM) inference into two separate sets of nodes is widely adopted in today's LLM serving systems. However, such an architecture poses significant challenges for self-hosted LLM deployments on rented cloud instances, since transfe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer
1. 论文的主要贡献和创新点
✅ 解决的问题：将LLM的prefill阶段与decoding阶段拆分为两个独立节点的架构，在自托管云实例部署时，跨节点传输海量KV缓存易饱和有限的节点间带宽，带来显著挑战。
🚀 提出的新方法与思路
**profile-based proactive transfer path**：在prefill阶段识别并推送必要的KV缓存条目至decoding节点；
**parallel on-demand transfer path**：在decoding阶段同时获取远程与本地的KV缓存条目；
**speculative transfer path**：最终向decoding节点交付全部KV缓存；
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| time-to-second-token | 可降低该指标 |
| 后续解码性能 | 与典型全KV缓存传输方法相当 |
| 准确率 | 与典型全KV缓存传输方法相当 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |
🎯 实验设置与评估指标
任务为分离式LLM推理
| 指标 | 含义 |
|------|------|
| time-to-second-token | ↓ 越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 典型full KV cache transfer approach | 现有LLM服务架构方法 | 传输全部KV缓存 |
3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告
💡 结论：论文未报告
4. 关键结论和发现
- 核心发现：SmartGen设计的三条KV缓存数据传输路径，可缓解分离式LLM推理中节点间的带宽瓶颈，同时维持与典型全KV缓存传输方法相当的后续解码性能与准确率；
- 方法局限性：论文未报告；
- 未来工作：论文未报告；
> ✅ **总结一句话**：SmartGen是一种面向分离式LLM推理的选择性KV缓存传输引擎，通过三条数据传输路径实现无缝部署，可缓解云实例自托管部署中的节点间带宽瓶颈，在降低time-to-second-token的同时保持相当的后续解码性能与准确率。

</details>

---

### 2. [Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees](https://arxiv.org/abs/2607.28399v1)

**Authors**: Zihan Dong, Rui Qian, Qishi Zhan, Dongshen Peng, Kaixin Li, Yu Li  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 72.5  
**Type**: new  
**ArXiv ID**: 2607.28399v1  

#### Abstract
Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed. We identify the main cause as expensive autoregressive decoding on the decision-time critical path. We propose Adaptive Anticipatory Policy Trees (AAPT), ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees
1. 论文的主要贡献和创新点
✅ 解决的问题
GUI智能体处理瞬态GUI事件时，因决策时间关键路径上的自回归解码成本过高，导致正确动作生成滞后于相关窗口关闭而失败；现有open-loop、predict-and-replan基线方法因执行时仍进行解码，成功率为0。

🚀 提出的新方法与思路
**Adaptive Anticipatory Policy Trees（AAPT）**：无需修改底层模型，在屏幕空闲期间，利用冻结的多模态模型构建带可观察守卫、预授权动作及分支特定截止时间的有界条件策略树，树大小按模型自身解码延迟规划；当事件触发时，轻量观察者匹配变化门控帧到预准备分支，直接执行对应动作，无需生成新文本。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 延迟处理 | 消除了决策时间关键路径上的自回归解码延迟 |
| 执行方式 | 事件触发时无需生成新文本，直接执行预准备动作 |
| 动作正确性 | 不产生不正确动作 |
| 成功率表现 | 在contested decision window内将成功率从0.50提升至0.79 |
| 泛化性 | 可在独立通用多模态模型上复现效果 |

2. 核心实验方法和设置
📚 使用的数据集
论文未报告具体数据集名称，仅开展以下三类试验：
| 试验类型 | 用途 |
| ---- | ---- |
| 配对试验 | 对比AAPT与基线方法的性能 |
| 独立通用多模态模型试验 | 验证AAPT在其他模型上的效果 |
| 外部基准试验 | 测试AAPT与反应式基线的整体性能 |

🎯 实验设置与评估指标
任务为GUI智能体处理瞬态GUI事件时的动作执行测试，评估指标如下：
| 指标 | 含义 |
| ---- | ---- |
| contested decision window内成功率 | 该窗口内智能体正确完成动作的比例（↑越高越好） |
| 错误动作数 | 智能体产生的不正确动作数量（↓越少越好） |
| p值 | 试验结果的统计显著性（↓越小越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| open-loop | 基线方法 | 执行时仍进行解码，成功率为0 |
| predict-and-replan | 基线方法 | 执行时仍进行解码，成功率为0 |
| 反应式基线 | 对比方法 | 实时解码执行，用于外部基准试验对比 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（contested decision window场景）**
AAPT成功率为0.79，基线方法open-loop、predict-and-replan成功率为0；统计检验显示p=1.8×10^-3，AAPT未产生任何不正确动作。
💡 结论：AAPT在该场景下较基线方法大幅提升动作成功率且无错误动作。

独立通用多模态模型试验
126次配对试验中，AAPT的效果复现，统计检验显示p=4.9×10^-13。
💡 结论：AAPT在独立模型上具备良好的泛化性能。

外部基准试验
AAPT与反应式基线的整体性能相当，两者优势互补。
💡 结论：AAPT与反应式基线在整体表现上无显著差异，适用场景各有侧重。

消融实验
论文未提供消融实验的详细表格，仅指出AAPT有效性的三个关键要求：快速观察者解码、有效树规划、准确分支路由；预注册oracle probe指向分支路由为因果瓶颈。
💡 结论：分支路由是AAPT有效性的核心瓶颈，三个关键要求缺一不可。

准备时间扫描
AAPT的性能增益出现在延迟树大小规则预测的区域。
💡 结论：树大小按模型解码延迟规划的规则可有效匹配性能增益的条件。

其他实验相关内容
- 效率对比（FPS/参数量）：论文未报告
- 跨域/zero-shot迁移：论文未报告
- 鲁棒性/扰动测试：论文未报告

4. 关键结论和发现
- 主要发现：1. GUI智能体处理瞬态GUI事件失败的核心原因为决策时间关键路径的自回归解码延迟；2. AAPT通过预构建策略树的方式消除了该延迟，在特定场景下大幅提升成功率且无错误动作；3. 分支路由是AAPT有效性的核心瓶颈。
- 方法局限性：AAPT仅在候选动作可提前枚举的场景下表现优于反应式执行，在动作无法枚举的场景中反应式执行更强，适用场景受限；论文未报告其他局限性。
- 未来工作：可优化AAPT的分支路由环节，或拓展其到候选动作难以枚举的场景；论文未报告更多未来工作方向。

> ✅ **总结一句话**：本文提出的Adaptive Anticipatory Policy Trees方法有效解决了GUI智能体处理瞬态事件时因解码延迟导致的动作失效问题，在可提前枚举候选动作的特定场景下大幅提升了动作成功率且无错误动作，同时明确了分支路由为核心瓶颈，泛化性良好。

</details>

---

### 3. [MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning](https://arxiv.org/abs/2607.26465v1)

**Authors**: Kawai Chung, Chunkit Chan, Yauwai Yim, Yuxuan Liu, Haochen Shi, Weiqi Wang, Qing Zong, Tianshi Zheng, Yixuan Fu, Kai Chung Wong, Hao Liang, Yifan Gao, Xi Yang, Janet Hui-wen Hsiao, Yangqiu Song  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 61.5  
**Type**: new  
**ArXiv ID**: 2607.26465v1  

#### Abstract
Multimodal Large Language Models have sparked significant interest due to their potential for social intelligence; however, their ability to perform sequential motivation reasoning remains insufficiently studied. Existing evaluations predominantly examine static text or isolated visual snapshots, wh...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态大语言模型的序列动机推理能力研究不足，当前评估多聚焦静态文本或孤立视觉快照，未贴合现实世界行为驱动的累积性特征，无法覆盖人类社会理解所需的动态推理需求。

🚀 提出的新方法与思路
**MultivationBench基准构建**，该基准基于Maslow's hierarchy（马斯洛需求层次）和Reiss's basic desires（赖斯基本需求）成熟心理框架，针对故事驱动的视觉叙事设计，要求模型整合累积的多模态上下文以推断演变的动机，填补了序列多模态动机推理评估的空白。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 评估任务适配性 | 聚焦序列多模态场景，贴合现实行为驱动的累积性特征 |
| 评估合理性 | 依托成熟心理学框架，具备动机推理评估的理论基础 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MultivationBench | 用于评估多模态序列动机推理能力的基准数据集 |

🎯 实验设置与评估指标
任务：针对故事驱动的视觉叙事，要求模型整合累积的多模态上下文以推断演变的动机。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告具体评估指标 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能（L2/碰撞率等）**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
💡 所有定量实验的具体结果及对应表号、图号均未在论文中明确报告。

4. 关键结论和发现
- 主要发现：现有多模态大语言模型在MultivationBench基准任务中，难以在序列语境下保持一致的动机推理能力，存在静态识别能力与人类类似社会理解所需的动态推理的关键脱节。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：MultivationBench是首个针对多模态序列动机推理的基准，揭示了现有多模态大语言模型在动态社会理解推理方面的显著不足。

</details>

---

### 4. [RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning](https://arxiv.org/abs/2607.28156v1)

**Authors**: Jingxiang Fan, Junbao Zhuo, Bochao Zou  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.28156v1  

#### Abstract
Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos. However, most methods emphasize what to store rather than how stored memory should be retrieved. When retrieval becomes inaccurate or repeatedly fails to obtain useful evidence,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态长时记忆智能体采用外部记忆缓解长视频有限上下文问题，但多数方法侧重存储内容选择而非检索方式优化；当检索结果不准确或反复失效时，现有智能体缺少从过往任务轨迹诊断失败原因、调整未来搜索策略的机制。

🚀 提出的新方法与思路
**Reflective Retrieval Memory (RRM)**：该方法在实体-centric多模态记忆图基础上新增反思性经验记忆模块，从历史任务轨迹提炼可迁移的程序性检索知识；与保存当前视频事实证据的情景、语义记忆不同，反思性经验记忆捕获跨任务的可复用搜索策略；RRM将检索得到的经验转化为查询级指导，答案生成仅依赖从当前视频中新检索的事实证据；同时引入生命周期管理机制，通过使用频率、复用反馈、时间衰减调控经验记忆，减少冗余与噪声。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 检索策略适配 | 具备从历史任务轨迹诊断检索失败、调整未来搜索策略的能力，弥补现有方法的检索缺陷 |
| 记忆功能划分 | 明确区分反思性经验记忆（程序性检索知识）与情景、语义记忆（事实证据），适配不同推理场景需求 |
| 记忆质量控制 | 引入生命周期管理机制，有效抑制经验记忆中的冗余与噪声 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| M3-Bench-Robot | 长时序多模态推理性能验证 |
| M3-Bench-Web | 长时序多模态推理性能验证 |
| Video-MME-Long | 长时序多模态推理性能验证 |

🎯 实验设置与评估指标
论文未报告具体任务定义、评估指标及对应含义

⚔️ 基线方法对比
论文未报告具体基线方法名称、类型及特点

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量性能指标数值及对应表号，仅提及RRM在M3-Bench-Robot、M3-Bench-Web、Video-MME-Long三个数据集上，相比现有SOTA方法性能更优。
1. 主 benchmark 性能：论文未报告具体数值，仅提及性能优于现有SOTA
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
  1. RRM引入的反思性经验记忆可提炼跨任务的程序性检索策略，助力长时序多模态推理；
  2. 对经验记忆实施使用频率、复用反馈、时间衰减的生命周期管理，可有效降低冗余与噪声；
  3. 功能明确的记忆划分（反思性经验、情景、语义记忆）适配多模态推理的不同需求。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：RRM通过新增反思性经验记忆模块及生命周期管理机制优化长时序多模态推理的检索策略，在多个基准数据集上性能优于现有SOTA方法。

</details>

---

### 5. [LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger](https://arxiv.org/abs/2607.28374v1)

**Authors**: Enjun Du, Hange Zhou, Chenxu Du, Siyi Liu, Zirong Chen, Ziyu Zheng, Yongqi Zhang  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2607.28374v1  

#### Abstract
Multimodal agents for visual question answering increasingly operate as multi-step trajectories that interleave perception, retrieval, and reasoning, yet evaluation still largely reduces to final-answer accuracy. This aggregate signal cannot tell whether a correct answer was reached through grounded...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger
1. 论文的主要贡献和创新点
✅ 解决的问题
现有多模态智能体视觉问答采用感知、检索、推理交替的多步骤轨迹，但评估仅依赖最终答案准确率，无法区分正确答案来自有根据证据、语言先验还是意外错误抵消，导致四类最终准确率掩盖的失败模式（无支撑中间推理、幻影接地、简单查询过度推理、修复时放大）无法被识别。

🚀 提出的新方法与思路
**Structured Evidence Ledger（结构化证据账本）**：将工具输出归一化为结构化账本，作为轨迹状态，下游推理与决策仅可引用活跃账本条目，在实体和数值层面执行接地检查，修复为类型化状态转换且不能引入无工具来源的内容。
**Three-Layer Grounding Protocol（三层接地协议）**：配合上述账本实现实体与数值级的接地合规性约束。
**Adaptive Dual-Path Dispatcher（自适应双路径调度器）**：匹配推理深度与问题复杂度，适配不同任务的推理需求。
**Event-Triggered Verification-and-Repair engine（事件触发的验证修复引擎）**：带有正式的来源非放大保证，用于处理推理过程中的验证与修复。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 轨迹可解释性 | 能区分正确答案的来源（证据/先验/偶然），而非仅依赖最终准确率聚合信号 |
| 隐性错误识别 | 可发现最终准确率无法察觉的四类多模态推理失败模式 |
| 接地合规性 | 强制推理仅引用工具生成的证据条目，实现实体和数值级的严格接地检查 |
| 来源可控性 | 状态转换为类型化操作，无法引入无工具来源的内容，满足来源非放大保证 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 多个多模态推理基准 | 验证LedgerMind在多模态视觉问答任务上的性能 |

🎯 实验设置与评估指标
任务：多模态视觉问答
| 指标 | 含义 |
| --- | --- |
| 答案准确率 | 最终答案的正确比例，↑越高越好 |
| 轨迹级忠实度 | 推理轨迹符合来源约束的程度，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 现有多模态智能体方法 | 多模态智能体 | 仅以最终准确率为评估指标，无法识别轨迹级错误 |
| 主干大语言模型（MLLMs） | 单模态推理模型（适配多模态任务） | 缺乏多步骤推理轨迹的来源约束机制 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验未在摘要中报告具体表号、定量数值等内容，故：
论文未报告

4. 关键结论和发现
- 主要发现：1. 现有多模态智能体视觉问答的最终准确率无法有效反映轨迹忠实度，易掩盖四类隐性失败模式；2. LedgerMind的结构化证据账本机制可同步提升答案准确率与轨迹级忠实度；3. 提出的三类组件（账本、调度器、验证引擎）能针对性解决多模态推理的来源合规问题。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：LedgerMind通过结构化证据账本与来源约束机制，克服了现有多模态智能体视觉问答仅依赖最终准确率评估的缺陷，实现了答案精度与推理轨迹忠实度的协同提升，可识别传统方法无法察觉的隐性推理失败模式。

</details>

---

### 6. [Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory](https://arxiv.org/abs/2607.27919v1)

**Authors**: Rubin Wei, Jiaqi Cao, Jiarui Wang, Junming Zhang, Qipeng Guo, Bowen Zhou, Zhouhan Lin  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2607.27919v1  

#### Abstract
Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently. Memory Decoder introduces a parametric long-term memory module but only studies it at a relatively small scale. In this work, we present Memory ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：《Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory》
1. 论文的主要贡献和创新点
✅ 解决的问题
1. 传统Decoder-only语言模型将长期记忆与推理参数纠缠在单一参数集，难以独立扩展记忆容量；
2. 早期Memory Decoder相关研究仅在小规模尺度开展，当扩展至6.9B参数、300B tokens数据的场景时，标准Faiss索引与检索流程的总开销过高，无法适用。

🚀 提出的新方法与思路
**分布式Faiss索引与检索流水线**：针对大尺度场景下索引和检索成本过高的问题，构建分布式的Faiss索引与检索流程，适配大规模参数与数据的处理需求；
**稀疏批次式kNN分布加载**：配合上述分布式流水线，实现kNN数据的稀疏、批次式加载，进一步降低索引与搜索的总开销。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 参数效率 | 独立扩展预训练记忆模块的参数-性能权衡优于仅扩展基础模型 |
| 轻量模型性能 | 通用记忆可提升轻量模型性能，使其超越参数量更大的基线模型 |
| 领域适配能力 | 不同尺度的基础模型搭配对应领域记忆，各尺度平均性能均有显著提升 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未明确提供具体数据集名称 | 预训练Memory Decoder at Scale模型 |

🎯 实验设置与评估指标
任务为语言模型在多基准测试上的性能评估，评估指标及含义如下：
| 指标 | 含义 |
| --- | --- |
| 17个基准测试平均得分 | ↑ 越高越好 |
| 模型总参数量 | ↓ 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统Decoder-only语言模型（Pythia系列） | 基础语言模型架构 | 长期记忆与推理参数纠缠，记忆容量无法独立扩展 |
| 小规Memory Decoder | 早期记忆模型研究对象 | 仅在小规模尺度验证，无法适配大参数与高数据场景 |
| Pythia-410M、Pythia-12B | 公开基础模型 | 用于对比配对记忆模块后的性能提升 |
| Qwen3 Base系列模型（0.6B~14B） | 公开基础模型 | 用于验证不同尺度下领域记忆的性能提升效果 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未明确报告所有定量结果对应的表号/章节等来源信息，仅能基于摘要内容描述如下：
**主 benchmark 性能**：论文提及配对记忆模块的模型在17个基准测试上的平均性能优于对应基线模型；
**效率对比**：论文提及配对记忆模块的模型在参数量效率上优于更大参数量的基线模型；
**跨域 / zero-shot 迁移**：论文提及域记忆可提升Qwen3 Base系列模型在各领域的平均性能；
**鲁棒性 / 扰动测试**：论文未报告；
**消融实验**：论文未报告。

4. 关键结论和发现
- 主要发现：
  1. 独立扩展预训练记忆模块相比仅扩展基础模型，能获得更优的参数-性能权衡；
  2. 为轻量模型搭配通用记忆，可使其性能超越参数量更大的基线模型；
  3. 为不同尺度的Qwen3 Base模型搭配对应领域记忆，各尺度的平均性能均有显著提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本文将Memory Decoder扩展至6.9B参数并提出分布式Faiss索引检索等适配大尺度的方案，证明独立扩展预训练记忆是提升语言模型性能的高参数效率路径。

</details>

---

### 7. [AHA-Memes: A Fine-Grained Multimodal Benchmark for Understanding Hate in Arabic Memes](https://arxiv.org/abs/2607.27393v1)

**Authors**: Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Abul Hasnat, Md. Rafiul Biswas, Wajdi Zaghouani, Firoj Alam  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2607.27393v1  

#### Abstract
Hateful memes are a growing form of multimodal online harm, where hostile intent is often conveyed through the joint interpretation of images, text, cultural references, and implicit targets. While hateful meme detection has advanced in high-resource languages, Arabic remains underexplored, with exi...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AHA-Memes: A Fine-Grained Multimodal Benchmark for Understanding Hate in Arabic Memes
1. 论文的主要贡献和创新点
✅ 解决的问题
当前高资源语言的仇恨表情包检测研究已取得进展，但阿拉伯语领域相关研究不足，现有阿拉伯语表情包资源主要聚焦宣传或粗粒度有害内容标签，缺乏面向阿拉伯语仇恨表情包的细粒度多标签标注基准。
🚀 提出的新方法与思路
**构建AHA-Memes基准数据集**：构建首个大规模阿拉伯语仇恨表情包基准，包含5K经手动标注的细粒度多标签仇恨类型（攻击策略类）表情包，同时提供约66K银标表情包以支持后续研究；针对多种模型开展基准测试：对text-only、image-only、late-fusion multimodal模型，以及few-shot in-context learning(ICL)模型、open-weight Vision-Language Models(VLMs)和closed-weight VLMs，在零样本与微调设置下进行基准测试。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 数据集特性 | 首个大规模阿拉伯语仇恨表情包基准，含细粒度多标签仇恨类型标注 |
| 覆盖模型范围 | 覆盖文本仅用、图像仅用、多模态late-fusion模型、ICL及open/closed-weight VLMs，支持零样本与微调两类设置 |
| 研究资源支持 | 提供5K手动标注数据和约66K银标数据，配套标注指南与评估脚本 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| AHA-Memes（含5K手动标注仇恨表情包、约66K银标仇恨表情包） | 用于阿拉伯语仇恨表情包检测任务的基准构建与模型评估 |
🎯 实验设置与评估指标
任务为阿拉伯语仇恨表情包的细粒度多标签仇恨类型检测，评估指标论文未报告具体内容。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| text-only模型 | 单模态模型 | 论文未报告具体特点 |
| image-only模型 | 单模态模型 | 论文未报告具体特点 |
| late-fusion multimodal模型 | 多模态模型 | 论文未报告具体特点 |
| few-shot ICL模型 | 基于上下文学习的模型 | 论文未报告具体特点 |
| open-weight VLMs | 开放权重视觉语言模型 | 论文未报告具体特点 |
| closed-weight VLMs | 封闭权重视觉语言模型 | 论文未报告具体特点 |
3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
4. 关键结论和发现
- 2-3条主要发现：
  1. 针对阿拉伯语仇恨表情包检测的研究存在不足，现有相关资源多为粗粒度或宣传类内容；
  2. AHA-Memes基准数据集及配套资源为阿拉伯语仇恨表情包检测研究提供了基础支持；
  3. 文化背景相关因素是阿拉伯语仇恨表情包检测的关键挑战。
- 方法局限性：论文未明确报告方法的具体局限性。
- 未来工作：利用AHA-Memes基准开展更深入的阿拉伯语仇恨表情包检测相关研究。

> ✅ **总结一句话**：该论文构建了首个带细粒度多标签的大规模阿拉伯语仇恨表情包基准AHA-Memes，提供配套数据集与评估工具，为阿拉伯语仇恨表情包检测领域的研究提供了重要支撑。

</details>

---

### 8. [Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models](https://arxiv.org/abs/2607.27506v1)

**Authors**: Shreyas Subramanian, Mecit Gungor, Vikram Elango  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.27506v1  

#### Abstract
Language and embedding models used in RAG systems are conventionally assumed to require large-scale pretraining and explicit grounding supervision. We present B1ade, an efficient RAG architecture comprising two purpose-built components: a compact embedding model and a purpose-built SLM. B1ade-embed,...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题：现有RAG系统存在两大缺陷：① 常规模型依赖大规模预训练，资源消耗极高；② 模型需要显式接地监督，训练设计复杂，提升了部署和使用成本。核心痛点是RAG系统对模型资源和训练监督的要求过高，不利于高效部署。

🚀 提出的新方法与思路
**B1ade高效RAG架构**：包含两个专用组件，分别为B1ade-embed嵌入模型和B1ade-1B小型语言模型（SLM）。其中B1ade-embed是335M参数的检索模型，通过5个预训练编码器的无参数融合构建，无需额外训练；B1ade-1B是1B参数的SLM，在低成本GPU上采用Group Relative Policy Optimization（GRPO）算法训练，训练数据为723M tokens（2.2M examples）的整理后上下文-问题对，奖励仅优化答案相似度。
**自发涌现接地能力**：B1ade-1B在未接受明确源引用监督的情况下，响应中引用检索段落的比例达42.4%，超出训练分布的引用率5.5个百分点，证明接地行为可在RL训练中作为最大化准确率的策略自发出现，无需额外设计显式奖励。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 嵌入模型构建 | B1ade-embed为335M参数，通过无参数融合5个预训练编码器实现，无需额外训练，在5亿参数以下模型中MTEB得分领先 |
| SLM训练效率 | B1ade-1B为1B参数，在低成本GPU上采用GRPO算法训练，训练数据规模适中，训练成本低 |
| 接地能力 | 无明确源引用监督下，响应引用检索段落比例达42.4%，超出训练分布5.5个百分点，接地行为自发涌现 |
| 端到端RAG性能 | 平均得分0.654，比SFT方法提升10.8%，缩小与1.5倍自身大小模型的性能差距 |
| 模型资源 | 整体架构无大规模预训练需求，参数量小，资源占用低 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 723M tokens（2.2M examples）的整理后的上下文-问题对 | 用于B1ade-1B的GRPO训练 |

🎯 实验设置与评估指标
任务：RAG系统的QA性能及端到端RAG综合性能评估
| 指标 | 含义（箭头） |
|------|--------------|
| MTEB得分 | 嵌入模型检索性能（越高越好） |
| PopQA准确率 | 通用QA性能（越高越好） |
| PubMedQA准确率 | 医学QA性能（越高越好） |
| FEVER准确率 | 事实核查性能（越高越好） |
| 端到端RAG平均得分 | 涵盖正确性、完整性、连贯性、忠实性的综合性能（越高越好） |
| 响应引用比例 | 接地能力（越高越好） |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| SFT方法 | 基准训练方法 | 用于对比端到端RAG的性能提升效果 |
| 1.5倍B1ade-1B大小的模型 | 规模对照模型 | 用于对比模型规模对RAG性能的影响 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**：论文未报告表号，B1ade-1B在PopQA上准确率81.82%，PubMedQA上65.8%，FEVER上51.09%。
💡 结论：B1ade-1B在多个标准QA及事实核查基准上取得了可观的性能，无需大规模预训练即可达到较好效果。
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot 迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告

4. 关键结论和发现
- 主要发现
1. 针对常规RAG模型对资源和监督要求过高的痛点，提出的B1ade架构采用专用紧凑组件，无需大规模预训练即可实现高效RAG，资源占用低。
2. B1ade-1B在仅优化答案相似度的RL训练下自发涌现接地行为，证明接地策略可通过最大化准确率的目标自发产生，无需额外设计显式奖励。
3. B1ade-1B在端到端RAG任务中性能优于SFT方法，且缩小了与更大规模模型的性能差距。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出的简约RAG架构B1ade通过专用嵌入模型和SLM设计及GRPO训练策略，在资源有限的情况下实现了高效RAG性能，且SLM自发涌现源引用接地能力。

</details>

---

### 9. [Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control](https://arxiv.org/abs/2607.27914v1)

**Authors**: Takumi Shioda, Kohei Terashima, Tatsuo Nagai  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2607.27914v1  

#### Abstract
Multi-zone variable-air-volume control must balance thermal comfort, indoor air quality, and electricity use across several continuous actuators. Model predictive control and reinforcement learning are widely studied, but deployment typically requires building-specific modeling or training, limiting...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control
1. 论文的主要贡献和创新点
解决的问题：多区VAV控制需平衡热舒适、室内空气质量与电力使用，现有模型预测控制、强化学习等方法依赖建筑特定建模或训练，可扩展性受限；同时现有方法存在不同缺陷：TD3可降低HVAC电力消耗并改善温度与CO₂合规性，GPT-5无建筑特定训练时电力降低更多但会减少通风余量；rollout-verified RFT的评论家内部状态排序不可靠；精确rollout分数无法揭示下一个状态效果与改进方向。
🚀 提出的新方法与思路
**GPT-5 (frontier reasoning model)**：用于实现无建筑特定训练的VAV控制，无需针对特定建筑的建模或训练即可开展控制。
**TD3-guided Reinforcement Fine-Tuning (RFT)**：用于将控制知识迁移至本地部署的open-weight模型，优化open-weight模型的VAV控制性能。
**Deterministic Rollouts**：用于RFT中验证动作，流程为恢复保存的状态、应用一个候选动作、通过TD3评分每个动作，保障RFT动作评估的可靠性。
**Transition-focused supervised fine-tuning (SFT) before value-based RFT**：针对RFT未改变转换误差的问题，提出先进行转换聚焦的监督微调，再开展基于价值的RFT，作为改进思路。
🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 部署可扩展性 | GPT-5无需建筑特定训练，突破VAV控制对特定建筑建模或训练的依赖，提升方法的可扩展性 |
| 多目标平衡能力 | TD3可在降低HVAC电力消耗的同时，改善温度与CO₂合规性，兼顾热舒适、室内空气质量与电力使用 |
| 知识迁移能力 | TD3引导的RFT可将GPT-5等模型的控制知识迁移至本地部署的open-weight模型，实现本地化部署 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| physics-based four-zone emulator | 用于在三个夏季天的场景下，评估多区VAV控制算法的性能 |
🎯 实验设置与评估指标
任务为多区VAV控制，在三个夏季天的physics-based four-zone emulator环境中，平衡热舒适、室内空气质量与电力使用。
| 指标 | 含义 |
|------|------|
| HVAC electricity | HVAC电力消耗，↓ 越低越好 |
| 温度合规性 | 温度达标情况，↑ 越高越好 |
| CO₂合规性 | CO₂达标情况，↑ 越高越好 |
| ventilation margin | 通风余量，↓ 越少越好（GPT-5会导致其减少） |
| 5-minute predictions | 五分钟预测性能，表现越优则越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| Guideline 36-based baseline | VAV控制基准方法 | 基于Guideline 36的标准VAV控制方法，作为性能对比的基准 |
3. 主要实验结果和性能指标
📊 定量结果汇总
主benchmark性能：论文未报告
效率对比：论文未报告
跨域/zero-shot迁移：论文未报告
鲁棒性/扰动测试：论文未报告
消融实验：论文未报告
**多区VAV控制性能（三个夏季天场景）**
| 方法 | HVAC电力消耗变化 | 温度合规性 | CO₂合规性 | 通风余量变化 |
|------|------------------|------------|-----------|--------------|
| Guideline 36-based baseline | - | - | - | - |
| TD3 | 降低4.5% | 改善 | 改善 | - |
| GPT-5（无建筑特定训练） | 降低6.2% ✅ | - | - | 减少 |
💡 结论：无建筑特定训练的GPT-5在HVAC电力降低上的表现最优，但会牺牲通风余量；TD3在降低电力的同时提升温度与CO₂合规性，兼顾多目标性能。
**Rollout-verified RFT性能**
200次RFT步骤后，open-weight控制器的采样动作回报无持续改进；open-weight控制器训练前后的HVAC电力消耗均高于Guideline 36基线；其五分钟预测性能比persistence差；GPT-5的转换预测性能优于该open-weight控制器；rollout-verified RFT的评论家在10个状态中仅5个选择了rollout最佳候选；精确rollout分数无法揭示下一个状态效果与改进方向。
💡 结论：当前的rollout-verified RFT方法无法实现open-weight控制器的持续性能提升，评论家的状态排序不可靠是其失效的重要原因，且精确rollout分数不足以支撑策略优化。
4. 关键结论和发现
- 主要发现：
1. 无建筑特定训练的GPT-5在VAV控制任务中，HVAC电力降低幅度优于TD3和Guideline 36基线，但会导致通风余量减少，存在多目标性能权衡；
2. Rollout-verified的TD3引导RFT方法未能让open-weight控制器实现持续的性能提升，且该open-weight控制器的HVAC电力消耗在训练前后均高于基线，未达到预期优化效果；
3. 精确的rollout动作分数无法揭示下一个状态的影响和改进方向，现有动作评估机制不足以支撑有效的策略优化。
- 方法局限性：
当前的rollout-verified RFT方法因评论家内部状态排序不可靠（10个状态中仅5个选择rollout最佳候选），无法实现策略的持续改进；open-weight控制器的性能仍低于基准方法，未能解决VAV控制对建筑特定建模的依赖问题。
- 未来工作：
1. 尝试在基于价值的RFT前开展转换聚焦的监督微调，解决RFT未改变转换误差的问题；
2. 优化评论家的内部状态排序可靠性，提升动作评估的准确性；
3. 探索更有效的rollout动作分数机制，使其能揭示下一个状态效果与改进方向，支撑策略的有效优化。
> ✅ **总结一句话**：该论文针对多区VAV控制的可扩展性痛点，研究了GPT-5、TD3引导的强化微调及rollout验证方法，发现GPT-5无建筑特定训练可降低HVAC电力但牺牲通风，rollout-verified RFT无法提升open-weight控制器性能，需结合转换聚焦的监督微调优化策略。

</details>

---

### 10. [CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games](https://arxiv.org/abs/2607.26393v1)

**Authors**: Zheng Zhang, Nanjie Yao, Jiarui He, Deheng Ye, Peilin Zhao, Hao Wang  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.26393v1  

#### Abstract
Social deduction games (SDGs) such as Werewolf have become challenging testbeds for AI agents. These games require complex social skills such as reasoning, deception, and collaboration. While recent advances in large language models (LLMs) have driven significant progress in SDG agents, current appr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大型语言模型（LLM）驱动的社交推理游戏（SDG，如狼人杀）代理以文本为核心，未考虑人类社会互动所依赖的多模态特性，存在能力局限。
分点缺陷：① 当前SDG代理多为文本驱动，缺失多模态感知与生成能力；② 未有效结合多模态信息开展社交推理。

🚀 提出的新方法与思路
**CaM-Wolf多模态代理框架**：CaM-Wolf是首个整合多模态感知与生成的社交推理游戏代理，包含三个核心环节：① 多模态感知：处理来自其他玩家的视频输入；② 因果感知推理器（causal-aware Reasoner）：通过强化学习训练，建立可观测玩家行为与隐藏角色之间的逻辑链；③ 多模态生成：通过动画化身呈现自身在游戏中的表现。

🔍 相比现有方法的优势
| 维度 | 优势 |
|------|------|
| 代理模态支持 | 整合多模态感知与生成，区别于现有文本驱动的单模态代理 |
| 社交推理能力 | 通过因果感知推理器建立可观测行为与隐藏角色的逻辑链，优化推理过程 |
| 人类-AI交互质量 | 提升人类与AI代理互动的质量 |
| 游戏性能 | 在社交推理游戏中具有更优的代理游戏表现 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
|--------|------|
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：社交推理游戏（SDG，如狼人杀）中的代理游戏性能测试与人类-AI交互质量评估；指标：论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主benchmark性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① CaM-Wolf作为首个整合多模态感知与生成的社交推理游戏代理，实现了更优的代理游戏性能并增强了人类-AI交互质量；② 因果感知推理器（经强化学习训练）可有效建立玩家可观测行为与隐藏角色的逻辑关联，支撑游戏中的推理过程。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：CaM-Wolf是首个整合多模态感知与生成的社交推理游戏代理，通过因果感知推理器优化社交推理能力，提升了游戏性能与人类-AI交互质量，推进了类人社会动态AI代理的研发。

</details>

---

### 11. [Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis](https://arxiv.org/abs/2607.27790v1)

**Authors**: Wei Chen, Junkai Li, Tongguan Wang, Hui Liu, Feiyue Xue, Chuanxiang Ma, Ying Sha  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2607.27790v1  

#### Abstract
Multimodal Sentiment Analysis (MSA) aims to interpret complex human emotions by integrating natural language with non-verbal modalities. Non-verbal modalities share a structural isomorphism with natural language, as both can be viewed as feature sequences evolving over time. This isomorphism enables...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis
1. 论文的主要贡献和创新点
✅ 解决的问题
现有基于大语言模型（LLM）的多模态情感分析（MSA）方法主要捕捉低层级的表层特征，无法建模由结构变化和上下文交互产生的情感语义，制约了MSA任务的性能提升。

🚀 提出的新方法与思路
**SentiLLM统一框架**：该框架采用Semantic-Aligned Structural Abstraction技术，将多模态中的连续原始信号蒸馏为紧凑、具有语义意义的token，实现非语言模态向文本类token的转化，适配LLM的序列数据理解能力。
**Dual-Stream Salience-Context Calibration Mechanism**：该机制将非语言特征序列解耦为聚焦流（Focus Stream）和环境流（Ambient Stream）；聚焦流由文本先验引导，捕捉显著情感变化（如面部表情），环境流表征稳定的背景状态，通过将动态情感变化与背景状态校准，实现非语言模态向LLM可理解的统一语义空间的投影，且SentiLLM为即插即用模块，仅需少量可训练参数即可提升模型判别性能。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 情感语义建模能力 | 解决了现有LLM-based MSA方法仅捕捉低层级表层特征、无法建模结构变化和上下文交互带来的情感语义的缺陷 |
| 模态适配性 | 可将非语言模态转化为文本类token，实现多模态数据向LLM可理解的统一语义空间的映射 |
| 模块特性 | 即插即用，仅需少量可训练参数即可提升MSA任务的判别性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| MOSI | 主基准性能测试 |
| MOSEI | 主基准性能测试 |
| CH-SIMS | 主基准性能测试 |
| CH-SIMS v2 | 主基准性能测试 |

🎯 实验设置与评估指标
任务：多模态情感分析（Multimodal Sentiment Analysis, MSA）
评估指标：论文未报告

⚔️ 基线方法对比
论文未报告

3. 主要实验结果和性能指标
📊 定量结果汇总
所有定量实验相关内容均论文未报告，因论文仅提及在四个数据集上取得优越性能，但未提供具体表号、数值等细节，故主基准性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验均为论文未报告。

4. 关键结论和发现
- 主要发现：1. Semantic-Aligned Structural Abstraction范式可有效提升MSA任务的性能；2. SentiLLM作为即插即用模块，仅需少量可训练参数即可显著提升模型判别能力；3. Dual-Stream Salience-Context Calibration Mechanism能更好地建模非语言模态的情感语义，适配LLM的处理逻辑。
- 方法局限性：论文未报告
- 未来工作：论文未报告
> ✅ **总结一句话**：SentiLLM通过语义对齐的结构抽象技术和双支路显著性-上下文校准机制，将非语言模态转化为LLM可理解的统一语义空间，为多模态情感分析提供了一种高效的即插即用改进方案，可在少量参数投入下显著提升任务性能。

</details>

---

### 12. [Train Small, Deploy Large: Zero-Shot GNN Transfer Through Geometric Renormalization](https://arxiv.org/abs/2607.27767v1)

**Authors**: Robert Jankowski, Pedro Almagro-Blanco, Mari\'an Bogu\~n\'a, Melanie Weber, M. \'Angeles Serrano  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.27767v1  

#### Abstract
Graph neural networks (GNNs) can operate on large graphs but become infrastructure-sensitive at the scale of millions of nodes and typically require scalable training techniques for even larger graphs. This raises a central question: when can a model trained on a smaller, scaled-down replica of a gr...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Train Small, Deploy Large: Zero-Shot GNN Transfer Through Geometric Renormalization
1. 论文的主要贡献和创新点
✅ 解决的问题
图神经网络（GNN）可处理大图，但在达到百万节点规模时对基础设施敏感，更大规模的图还需要可扩展的训练技术；核心痛点是无法实现小图上训练的模型零样本地部署到全尺寸图，需重新训练。

🚀 提出的新方法与思路
**Zero-Shot GNN Transfer Protocol**，核心是通过几何重归一化（Geometric Renormalization, GR）对图进行粗粒度化处理，将在该缩小后的图副本上训练得到的GNN权重直接迁移至原网络，无需额外训练。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 预测性能 | 在合成及真实网络上，训练于GR缩小副本的模型可保留原尺度的大部分预测性能 |
| 训练成本 | 显著降低训练成本 |
| 跨尺度一致性 | 学习到的表示及预测轨迹在不同尺度下保持对齐 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
论文未报告具体任务类型、评估指标及对应表号，无法列出相关内容

⚔️ 基线方法对比
论文未报告，无法列出相关表格

3. 主要实验结果和性能指标
📊 定量结果汇总
- 主benchmark性能：论文未报告
- 效率对比（FPS / 参数量）：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现
  1. 提出的基于几何重归一化的零样本GNN迁移协议，可将缩小图副本上训练的模型直接部署到全尺寸图，无需重新训练；
  2. 该方法能保留原尺度的大部分预测性能，同时显著降低训练成本；
  3. 跨尺度的学习表示和预测轨迹保持对齐，结构相似性在决定GNN迁移性上比网络大小更重要，为构建尺度等变性图架构提供了方向。
- 方法局限性：论文未报告
- 未来工作：论文未报告
✅ 总结一句话：本论文提出基于几何重归一化的零样本GNN迁移协议，实现了缩小图副本训练模型到全尺寸图的零样本部署，在保留大部分预测性能的同时显著降低训练成本，还揭示结构相似性对GNN迁移性的关键作用，为构建尺度等变性图架构开辟了路径。

</details>

---

### 13. [Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold](https://arxiv.org/abs/2607.27770v1)

**Authors**: Songshuo Lu, Zhi Chen, Yaohua Tang  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2607.27770v1  

#### Abstract
A single reinforcement-learning run can produce a strong reasoner yet an incomplete teacher: it often amplifies only a subset of the valid solution modes. We argue that reinforcement learning (RL)-trained policies should therefore be viewed as local probes of a multi-basin reasoning solution manifol...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold
1. 论文的主要贡献和创新点
✅ 解决的问题
核心矛盾是单强化学习（RL）训练的策略是推理解流形的局部探针，仅覆盖有效解模式的一个子集，属于不完整的全局监督信号；现有单教师方法存在两类缺陷：① 单RL策略仅覆盖部分有效解模式，作为教师可靠性不足；② 多数研究采用单一最优教师，未利用多教师的互补性，无法覆盖更多有效解模式。

🚀 提出的新方法与思路
**Expand-then-compress框架**：核心思路是耦合教师构建与多教师策略蒸馏，分为两个核心阶段及一个关键模块：
- 扩展阶段：采用**Residual Group Relative Policy Optimization (RGRPO)**，从共同初始化训练一系列教师，每一轮训练将后续教师重定向至累计教师联合尚未覆盖的例子；
- 压缩阶段：采用**可靠性-gated Teacher-Union On-policy Distillation (TU-OPD)**，让学生从自身响应前缀学习，每个例子中仅可靠教师参与贡献，采样token的OPD损失按每个例子的教师质量加权；
- 关键模块：**Consensus-Residual Decomposition**，用于保留获胜教师相对于可靠同行的过剩token偏好，防止教师聚合时抑制专门行为。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 教师构建方式 | 构建互补多教师联合，覆盖更多有效解模式 |
| 学生性能 | 生成的Qwen3-1.7B学生在多个任务上优于最强单个教师 |
| 推理效率 | 保留单模型推理，无需多模型集成 |
| 解模式完整性 | 突破单RL教师的局部解覆盖局限，提升解的多样性 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 数学推理对应领域数据集 | 用于评估数学推理任务性能 |
| 代码生成对应领域数据集 | 用于评估代码生成任务性能 |
| 指令遵循对应领域数据集 | 用于评估指令遵循任务性能 |

🎯 实验设置与评估指标
任务为数学推理、代码生成、指令遵循三类NLP任务；论文未报告具体评估指标名称。

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 最强单个教师 | 单教师方法 | 采用单一RL训练的策略，仅覆盖部分有效解模式 |
| Qwen3-1.7B（本方法） | 多教师蒸馏学生方法 | 从互补多教师联合蒸馏得到，保留单模型推理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告对应定量结果的表号、图号等来源信息，仅说明Qwen3-1.7B学生在数学推理、代码生成、指令遵循三个领域均优于最强单个教师，且保留单模型推理。

1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 单RL训练策略是推理解流形的局部探针，仅覆盖部分有效解模式，无法作为全局可靠的单一教师；
  2. 通过扩展构建互补多教师联合再压缩蒸馏的思路，可得到性能优于最强单个教师的单模型学生；
  3. Consensus-Residual Decomposition模块可有效保留教师的专门偏好，避免教师聚合时的专门行为抑制。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出的扩展-压缩框架通过构建互补多教师联合并进行压缩蒸馏，得到的Qwen3-1.7B单模型学生在数学推理、代码生成、指令遵循三类任务上均优于最强单个教师，突破了单RL教师的解模式覆盖局限。

</details>

---

### 14. [Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation](https://arxiv.org/abs/2607.27783v1)

**Authors**: Amruta Parulekar, Jinu Lee, Dilek Hakkani-T\"ur, Hari Sundaram  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2607.27783v1  

#### Abstract
Large Language Models (LLMs) explore problems through chain-of-thought, but this exploration is buried in unstructured prose. On high-stakes tasks, users cannot tell which steps are well-supported, which alternatives were seriously considered, or how the final conclusion compares to those the model ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation
1. 论文的主要贡献和创新点
✅ 解决的问题
当前大语言模型（LLM）的推理过程以非结构化的链式思考呈现，高风险任务中用户无法清晰判断推理步骤的支撑度、备选方案的考量情况，也无法对比最终结论与被舍弃结论的差异；现有的多数投票等方法仅集成LLM的答案，未对推理结构进行整合。

🚀 提出的新方法与思路
**Weighted DAG Aggregation**：从多个LLM的推理链中提取有向无环图（DAG），按步骤被独立轨迹验证的次数作为权重，通过加权合并DAG来集成多LLM的推理结构，返回可检查的“共识推理图”。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 推理集成对象 | 集成LLM的推理结构而非仅答案，输出可检查的共识推理图 |
| 主基准性能 | 在六个基准上超过匹配预算的多数投票基线，MuSR-MM（叙事多跳推理）上精度增益最大达3.1% |
| 单模型性能 | 单模型场景下以相同轨迹预算匹配或超过自一致性（self-consistency）方法 |
| 推理质量相关性 | 加权步骤的权重与LLM judge对推理质量的评分的Spearman ρ为0.30-0.51，呈中等至强正相关 |
| 路径偏好率 | 共识子图的推理路径在五个数据集的头对头比较中，被偏好于多数投票答案的比例为54.4-65.4% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 六个基准（含法定解释、研究生科学、叙事多跳推理、一阶逻辑、MuSR-MM等） | 覆盖不同类型推理任务，用于评估框架的性能 |

🎯 实验设置与评估指标
实验针对六个不同类型推理任务评估方法性能，采用的评估指标及含义如下：
| 指标 | 含义（箭头方向） |
| --- | --- |
| 推理精度 | 衡量推理结论的准确性，↑越高越好 |
| Spearman相关系数（ρ） | 衡量权重与LLM judge评分的相关性，↑越接近1越好 |
| 路径偏好率 | 共识子图路径被偏好于多数投票答案的比例，↑越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| matched-budget majority-vote | 基线方法 | 仅集成LLM答案的多数投票策略，与提出方法的计算预算匹配 |
| self-consistency | 对比方法 | 单模型下集成多条推理链的答案，无结构化推理图输出 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主基准性能（场景：六个推理任务基准）**
| 方法 | MuSR-MM精度增益 | 六基准整体性能（相对多数投票基线） |
| --- | --- | --- |
| matched-budget majority-vote | 0%（基线） | 基准 |
| Reasoning Consensus（提出方法） | +3.1% ✅ | 超过基线 |
💡 结论：在六个不同类型推理任务的主基准测试中，提出的Weighted DAG Aggregation框架的推理性能优于匹配预算的多数投票基线，在叙事多跳推理的MuSR-MM数据集上精度增益达到最大值3.1%。

- 效率对比：论文未报告
- 跨域 / zero-shot 迁移：论文未报告
- 鲁棒性 / 扰动测试：论文未报告
- 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 提出的Reasoning Consensus框架通过加权合并多LLM推理链提取的DAG集成推理结构，在六个基准任务上性能优于匹配预算的多数投票基线，单模型场景下可匹配或超过自一致性方法，同时提供可检查的共识推理图。
  2. 框架中各推理步骤的权重与LLM judge对推理质量的评分呈显著正相关（Spearman ρ=0.30-0.51），共识子图的推理路径在多数头对头比较中更受偏好。
  3. 该框架可用于分析问题的多样化推理视角，提升高风险任务中推理的可解释性。
- 方法局限性：论文未报告
- 未来工作：论文未报告明确的未来工作方向

> ✅ **总结一句话**：该论文提出的Weighted DAG Aggregation框架通过集成多LLM的推理结构（而非仅答案），在保持高推理性能的同时提供可检查的共识推理图，显著提升了高风险推理任务的可解释性与答案可靠性。

</details>

---

### 15. [Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors](https://arxiv.org/abs/2607.28525v1)

**Authors**: Neelam Akula, Surbhi Kumar, Murat Kantarcioglu, Baris Coskunuzer  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2607.28525v1  

#### Abstract
Many real-world graphs support multiple predictive tasks over the same underlying structure, creating an opportunity to reuse supervision across node classification (NC) and link prediction (LP). However, existing evaluations often rely on incompatible splits, observed-graph assumptions, and negativ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors
1. 论文的主要贡献和创新点
✅ 解决的问题
现有针对同图节点分类（NC）与链接预测（LP）跨任务迁移的评估，依赖不兼容的划分规则、观测图假设及负采样规则，导致相关迁移结论不可靠，缺乏统一严谨的评估框架。

🚀 提出的新方法与思路
**leakage-free同图跨任务迁移协议**：正式定义同图NC-LP迁移，设计固定节点与边划分、使用排除评估边的共享消息传递图、采用固定负样本用于LP的无泄漏评估协议，消除评估偏差。
**CoTask Score (CTS)**：提出用于总结共享编码器同时服务NC与LP的联合效用的指标，利用简单数据集统计（尤其同质性）指导机制选择，避免负迁移。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 评估可靠性 | 提供无泄漏的同图跨任务评估协议，解决现有评估规则不兼容导致的结论不可靠问题 |
| 联合效用评估 | 引入CoTask Score，统一量化共享编码器服务多任务的联合价值，避免单一任务评估的局限性 |
| 迁移指导 | 基于数据集统计（如同质性）提供明确的跨任务机制选择指引，降低负迁移风险 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 用于验证同图跨任务迁移规律与方法有效性 |

🎯 实验设置与评估指标
任务为同图下GNN的NC与LP跨任务迁移性能评估，**指标含义**：论文未报告

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告
2. 效率对比：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：① 同图跨任务迁移具有强方向性和可预测性，NC→LP在同配图上始终有益，LP→NC脆弱且天真的表示复用会降低准确率；② LP→NC仅在结构主导的 regime（LP任务容易但NC任务不饱和）时表现为可靠的正迁移，LP可视为结构预训练；③ CoTask Score（CTS）结合同质性等简单数据集统计，可指导共享编码器的机制选择，避免负迁移。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：该论文提出了严谨的同图NC-LP跨任务无泄漏评估协议与CoTask Score，明确了同图下GNN跨任务迁移的方向规律，为提升跨任务迁移的可靠性与实用性提供了核心框架与方法。

</details>

---

### 16. [A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding](https://arxiv.org/abs/2607.27735v1)

**Authors**: Yuesong Liu, Yuan Zeng, Min Lyu, Ruilin Liu, Yu Guo, Yinlong Xu  
**Category**: cs.CL  
**Published**: 2026-07-31  
**Score**: 36.0  
**Type**: new  
**ArXiv ID**: 2607.27735v1  

#### Abstract
Speculative decoding alleviates the memory-bandwidth bottleneck in large language model inference, but its acceleration is jointly constrained by drafting overhead, token acceptance, and speculation length. We present a unified efficiency analysis showing that extending the speculation horizon can r...

---

### 17. [SDO: Structure-Aware Data Organization for Efficient LLM Post-Training](https://arxiv.org/abs/2607.27273v1)

**Authors**: Jinliang Gao, Ning Yang, Hai Wang, Baili Xiao, Pin Lyu  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 35.5  
**Type**: new  
**ArXiv ID**: 2607.27273v1  

#### Abstract
Post-training of large language models is expensive, and existing efficiency improvements mainly focus on selecting informative samples or designing training schedules. However, data organization itself is usually treated as a static preprocessing step: embedding-based grouping methods construct fix...

---

### 18. [Linguistic Monoculture in LLM-Assisted Language Use](https://arxiv.org/abs/2607.27134v1)

**Authors**: Suhas Thejaswi, Juhi Kulshreshta, Lutz Oettershagen  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2607.27134v1  

#### Abstract
Writing and communication are increasingly mediated by large language models (LLMs) that are being used to draft, revise and polish text. Although such assistance can improve clarity and help authors meet institutional expectations, widespread reliance on shared models may reduce population-level va...

---

### 19. [ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents](https://arxiv.org/abs/2607.27879v1)

**Authors**: Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst  
**Category**: cs.AR  
**Published**: 2026-07-31  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2607.27879v1  

#### Abstract
Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute tha...

---

### 20. [Kalman Meets Curriculum: Efficient Dynamic Prompt Selection for Adaptive RL Finetuning](https://arxiv.org/abs/2607.27610v1)

**Authors**: Haodong Zhu, Yangyang Ren, Yanjing Li, Sheng Xu, Haiguang Liu, Linlin Yang, Baochang Zhang  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2607.27610v1  

#### Abstract
Reinforcement learning (RL) finetuning significantly enhances the reasoning capabilities of large language models (LLMs), yet its effectiveness critically depends on selecting prompts of appropriate difficulty for the current policy. This is challenging because prompt difficulty evolves throughout t...

---

### 21. [Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning](https://arxiv.org/abs/2607.27626v1)

**Authors**: Wentao Zhang, Wentao Mo  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.27626v1  

#### Abstract
Safety-critical IoT systems such as industrial closed-loop control, V2X coordination, and remote teleoperation require every sensor's peak Age of Information (peak AoI, also abbreviated PAoI) to stay below a hard per-slot deadline, not merely an average bound. Existing approaches meet this requireme...

---

### 22. [Cybersecurity Detection Classification with Reasoning-enabled Language Models](https://arxiv.org/abs/2607.28460v1)

**Authors**: Amol Khanna, Manu Nandan, Cristian Viorel Popa, Joan Pujol-Roig, Diana Bolocan, Laura Vasilie, Alexandru Apostu, Chase Helwig, Mihaela Gaman, Michael Brautbar, Edward Raff, Chase Midler, Sven Krasser  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2607.28460v1  

#### Abstract
A major issue in Security Operations Centers (SOCs) is alert fatigue, as the number of detections reported is more than staff can triage in a given day. Prior work prompts or fine-tunes large language models (LLMs) to emit a triage label directly, but does not train them to reason about whether a de...

---

### 23. [FedOGL: Combating Catastrophic Forgetting in Federated Open-World Multimodal Graph Learning](https://arxiv.org/abs/2607.27665v1)

**Authors**: Zekai Chen, Haodong Lu, Shihao Li, Weiwei Ji, Xunkai Li, Xun Wu, Yinlin Zhu, Rong-Hua Li  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2607.27665v1  

#### Abstract
Federated graph learning enables collaborative training over decentralized graph data without sharing raw graph information. As such risks evolve, clients must learn emerging classes from private multimodal graph streams, retain historical categories, and reject samples outside the known class space...

---

### 24. [Position: Evaluation Scores Are Perishable Knowledge Claims](https://arxiv.org/abs/2607.26191v1)

**Authors**: Sankalp Gilda, Shlok Gilda  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.26191v1  

#### Abstract
Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results. When these signals are aggregated via averaging, evaluation confidence can then substantially exceed the reliability o...

---

### 25. [CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/abs/2607.26452v1)

**Authors**: Yiming Cai, Fangjie Yu, Meiqing Yu, Ziyue Shi, Pengfei Yuan, Yong Guo  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.26452v1  

#### Abstract
World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure. We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics ...

---

### 26. [Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs](https://arxiv.org/abs/2607.28390v1)

**Authors**: Ankur Naskar, Vaneet Aggarwal  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2607.28390v1  

#### Abstract
Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, exte...

---

### 27. [Queue-Theoretic Admission Control for Multi-Tenant GPU Clusters](https://arxiv.org/abs/2607.28223v1)

**Authors**: Sohan Kunkerkar  
**Category**: cs.DC  
**Published**: 2026-07-31  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.28223v1  

#### Abstract
GPU cluster operators cannot predict how long pending workloads will wait for admission. Existing systems use greedy heuristics with no formal wait time guarantees. We formalize GPU cluster admission as a multi-class, multi-resource queueing network and prove a structural decomposition: the pending ...

---

### 28. [LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts](https://arxiv.org/abs/2607.27787v1)

**Authors**: Ken Ding  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2607.27787v1  

#### Abstract
Reinforcement learning from verifiable rewards (RLVR) for mathematical reasoning suffers from a structural blind spot: on "cliff" prompts-those on which every sampled rollout in a group fails-the group-normalized advantage is identically zero, so GRPO produces no gradient on precisely the prompts at...

---

### 29. [GoGoTB: Agentic RTL Verification with Specification-Grounded Coverage Closure](https://arxiv.org/abs/2607.26181v1)

**Authors**: Xin Xin, Jincheng Lou, Junhui Li, Jinglin Yan, Panda Xiao, Di Wu, Haixiao Li, Weicong Lu, Weijian Fan, Xinyu Qu, Yuxiang Zhao, Min Yu, Zhixiong Di, Yibo Lin  
**Category**: cs.AI  
**Published**: 2026-07-31  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.26181v1  

#### Abstract
Functional verification dominates integrated circuit (IC) front-end engineering effort, and a single missed bug that escapes to silicon can trigger a costly respin. Recent large language models (LLMs) offer new opportunities to automate this process, yet existing LLM-based approaches generate each c...

---

### 30. [Schreier-Coset Graph Rewiring](https://arxiv.org/abs/2607.27479v1)

**Authors**: Aryan Mishra, Randy Martinez, Lizhen Lin  
**Category**: cs.LG  
**Published**: 2026-07-31  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2607.27479v1  

#### Abstract
The information flow in the graph neural networks (GNNs) is fundamentally constrained by over-squashing, where structural bottlenecks impede long range information propagation. Graph-rewiring methods, which modify graph topology, have been extensively used to alleviate this. However, existing approa...

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
