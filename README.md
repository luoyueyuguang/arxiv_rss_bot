# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-08-06 08:24:16 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [When Prompts Become Pixels: Prompt-Region Grounding for Multimodal Reasoning](https://arxiv.org/abs/2608.04726v1)

**Authors**: Yongxin Wang, Ruizhe Zhou, Yueling Tang, Yingying Zhu, Xuemin Zhao, Xiaojun Chang, Xiaodan Liang  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 74.5  
**Type**: new  
**ArXiv ID**: 2608.04726v1  

#### Abstract
Multimodal large language models increasingly reason over screenshots and documents where the task itself may be written in pixels. Yet benchmarks usually place questions in text, leaving it unclear whether models use the same instruction equally well across channels. We introduce Visualized Task Se...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：When Prompts Become Pixels: Prompt-Region Grounding for Multimodal Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有基准多将多模态任务的指令以文本形式呈现，导致多模态大语言模型（MLLMs）对不同通道的指令利用存在不一致；而当任务以像素形式（视觉问题）呈现时，模型常能正确转录视觉问题却无法有效利用其语义，存在超出光学字符识别（OCR）问题的语义通道gap，上述痛点未被现有工作充分解决。
🚀 提出的新方法与思路
**Visualized Task Semantics（VTS）干预**：将任务问题移动至图像中，同时保持源问题和答案固定，作为控制干预手段，用于验证多模态模型对视觉形式任务的语义利用能力。
**Prompt-Region Grounding方法**：核心设计为对齐问题区域与类型化语义，并从掩码视图恢复问题区域的干净表示，目标是减少多模态模型的语义通道gap，且该方法在推理阶段无需光学字符识别（OCR）或区域元数据支持。
🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 语义通道gap缓解 | 对齐问题区域的类型化语义，从掩码视图恢复问题区域的干净表示 |
| 任务性能保留 | 提升视觉形式任务准确率的同时，保留原文本任务界面的准确率 |
| 训练成本适配 | 在匹配训练成本的前提下实现性能提升 |
2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 4个基准 | 用于开展VTS干预实验，验证多模态模型在视觉形式任务下的性能表现及所提方法的有效性 |
🎯 实验设置与评估指标
实验任务为多模态推理任务，评估指标为准确率（↑ 越高越好）。
| 指标 | 含义 |
| --- | --- |
| 准确率 | 衡量模型完成指定多模态推理任务的正确率，数值越高性能越好（↑） |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 6个MLLMs | 多模态大语言模型 | 存在超出OCR问题的语义通道gap，常可正确转录视觉问题却无法利用其语义 |
3. 主要实验结果和性能指标
📊 定量结果汇总
**主benchmark性能**：所有24个模型-任务对的准确率均出现下降，具体定量数值因无对应图表编号无法定位来源，故未报告。
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
4. 关键结论和发现
- 主要发现：
1. 当多模态推理任务的指令从文本转为像素形式的视觉问题时，MLLMs的推理性能出现下降，且模型常存在转录视觉问题但无法利用其语义的情况，说明存在超出OCR问题的语义通道gap。
2. 所提出的prompt-region grounding方法可在匹配训练成本的前提下提升视觉形式任务的推理准确率，同时保留原文本任务界面的准确率，且推理阶段无需OCR或区域元数据支持。
3. 读取任务文本并将其grounding为推理指令是多模态推理的独立能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文针对多模态大模型在处理像素形式任务时存在的语义通道gap问题，提出Visualized Task Semantics干预方法验证该问题，并提出prompt-region grounding方法缓解该gap，有效提升了模型在视觉任务场景下的推理性能，同时保留了原文本任务的性能。

</details>

---

### 2. [Zero-Instrumentation Dependency Discovery for Guided Microservice Migration Using eBPF](https://arxiv.org/abs/2608.04413v1)

**Authors**: Eshan Trivedi, Chandrahasa Pranava  
**Category**: cs.DC  
**Published**: 2026-08-06  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2608.04413v1  

#### Abstract
Migrating microservices across virtual machines (VMs) without knowledge of their runtime communication patterns risks creating cross-VM hotspots and latency spikes that are difficult to predict from static analysis alone. We use extended Berkeley Packet Filter (eBPF) kernel-level network tracing to ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Zero-Instrumentation Dependency Discovery for Guided Microservice Migration Using eBPF
1. 论文的主要贡献和创新点
✅ 解决的问题：微服务跨虚拟机（VM）迁移时，若缺乏对其运行时通信模式的认知，易产生难以预测的跨VM热点与延迟峰值，静态分析无法有效解决该问题。
🚀 提出的新方法与思路
**Zero-Instrumentation Dependency Discovery**：采用eBPF内核级网络跟踪技术，自动无应用插装地发现微服务间的运行时依赖，生成对应的依赖图。
**Two-pass PID to Port Correlation Algorithm**：使用两阶段进程ID（PID）到端口的关联算法，在共享运行时测试床中恢复全部服务的身份信息。
**Spectral Graph Clustering with Kernighan-Lin Refinement**：结合谱图聚类算法与Kernighan-Lin优化，将服务划分成VM一致的分组，生成流量感知的微服务迁移计划。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 迁移计划流量优化 | 可生成流量感知的迁移计划，降低跨VM流量暴露风险 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 作者自制的单20服务测试床 | 评估依赖发现算法与迁移计划的有效性 |
🎯 实验设置与评估指标
任务：评估无仪器依赖发现技术及流量感知微服务迁移计划的性能与追踪开销
| 指标 | 含义 |
| ---- | ---- |
| 迁移窗口跨VM流量暴露 | ↓ 数值越低表示性能越优 |
| eBPF追踪开销（吞吐量） | 无明确方向，用于评估追踪对系统的影响 |
| eBPF追踪开销（p50延迟） | 无明确方向，用于评估追踪对系统的影响 |
| eBPF追踪开销（p99延迟） | 无明确方向，用于评估追踪对系统的影响 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 字母排序（Alphabetical ordering） | 迁移计划基线 | 作为依赖盲任意排序的确定性代理 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的相关表格内容，所有实验相关定量结果均未附带表号、图号等来源信息，故无法披露具体数值。
💡 结论：基于eBPF的零仪器依赖发现技术可有效识别微服务间的运行时依赖，结合ROI排序的迁移计划可优化迁移相关流量，但在生产级饱和负载下追踪开销较高。

4. 关键结论和发现
- 基于eBPF的内核级网络跟踪无需对应用进行插装，即可自动发现微服务间的运行时依赖。
- 采用ROI排序的流量感知迁移计划可优化微服务跨VM迁移时的跨VM流量暴露。
- eBPF追踪在接近生产饱和的负载下会导致显著的延迟上升，追踪捕获需在非高峰时段或专用采样节点执行。
方法局限性：仅在作者自制的单20服务测试床上完成验证，未声明该方法在生产环境依赖图上的行为。
未来工作：扩展该方法至生产环境的依赖图验证，优化eBPF追踪的性能开销。

> ✅ **总结一句话**：本文提出一种基于eBPF的零仪器微服务运行时依赖发现与流量感知迁移计划技术，可降低微服务跨VM迁移时的跨VM流量暴露，但在生产级饱和负载下追踪开销较高。

</details>

---

### 3. [AsymSpec: Efficient Cloud-Edge Speculative Decoding over Asymmetric Networks](https://arxiv.org/abs/2608.04974v1)

**Authors**: Guotao Yang, Hao Chen, Rui Guo, Xinyu Li, Liang Zheng, Sheng Chen, Yitao Hu, Keqiu Li  
**Category**: cs.DC  
**Published**: 2026-08-06  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2608.04974v1  

#### Abstract
Cloud-edge speculative decoding places a lightweight draft model at an edge gateway and a higher-quality target model in the cloud, but inserts communication into every speculative block. Under a constrained uplink, candidate messages may queue while the verifier is idle. Stop-and-wait scheduling le...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

AsymSpec: Efficient Cloud-Edge Speculative Decoding over Asymmetric Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
- 现有Cloud-edge推测解码中，上行链路受约束时，候选消息排队导致验证器空闲；
- Stop-and-wait调度方式下，边缘计算资源未被充分利用；
- 乐观同请求预取机制在出现拒绝或意外额外token时，会造成依赖工作的浪费。

🚀 提出的新方法与思路
**Asymmetric Verification Protocol**：针对上行链路约束下的验证效率问题，将公共路径的接受上传内容压缩，把仅在拒绝场景使用的丰富修正信息转移至下行链路；通过总变异（TV）证书判断小的目标模型Top-K响应是否足够，若不足则逐步升级到基于proposal的精确恢复，最终回退到全分布场景。
**Confirmed-Prefix Pipeline**：针对调度与工作浪费问题，仅向边缘调度器暴露独立、有效的请求，允许云端对到达的块重新批处理，在另一确认前缀请求就绪时隐藏验证等待，无需使用同请求预取机制。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 上行链路资源利用率 | 压缩公共路径接受消息，避免候选消息排队 |
| 边缘计算资源利用率 | 优化调度，避免Stop-and-wait调度导致的资源闲置 |
| 计算工作效率 | 消除同请求预取的无效工作浪费 |
| 输出token吞吐量 | 相对最强基线显著提升（论文明确提及倍数范围，但无对应来源） |

2. 核心实验方法和设置
📚 使用的数据集：论文未报告
🎯 实验设置与评估指标：任务为Cloud-edge环境下的推测解码任务；评估指标为输出token吞吐量，箭头方向：↑ 越高越好
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 传统Stop-and-wait调度的推测解码方法 | 基线 | 存在边缘计算未充分利用的缺陷 |
| 带乐观同请求预取的推测解码方法 | 基线 | 存在拒绝或意外额外token时工作浪费的缺陷 |
| AsymSpec | 提出方法 | 解决上述基线的核心缺陷 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark性能**：论文未报告
**效率对比（FPS / 参数量）**：论文未报告
**跨域 / zero-shot迁移**：论文未报告
**鲁棒性 / 扰动测试**：论文未报告
**消融实验**：论文未报告
💡 补充说明：论文在摘要中提及，在覆盖三组draft-target对、两个工作负载和三种非对称网络配置的端到端评估中，AsymSpec的输出token吞吐量是最强基线的2.82-28.03倍，但未报告该结果对应的表号、图号等来源信息。

4. 关键结论和发现
- 主要发现：1. AsymSpec提出的两个核心机制可有效解决Cloud-edge非对称网络下推测解码的上行链路排队、边缘计算闲置及同请求预取的工作浪费问题；2. 能在多种场景下实现输出token吞吐量的显著提升。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：AsymSpec通过设计非对称验证协议与确认前缀流水线，优化了云边缘推测解码的资源利用与调度策略，显著提升了输出token吞吐量。

</details>

---

### 4. [CARGO-VL: Counterfactual Arbitration with Risk-Constrained Group Optimization for Vision-Language Models](https://arxiv.org/abs/2608.04509v1)

**Authors**: De Jiang, Zhengyang Zhang, Kehong Yuan, Shaohua Ma  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2608.04509v1  

#### Abstract
Vision-language systems combine images with retrieved text, but these sources can disagree or jointly fail to support an answer. Reliable models must identify the trustworthy source and abstain when neither is adequate. Existing post-training objectives score instances independently and therefore do...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

CARGO-VL: Counterfactual Arbitration with Risk-Constrained Group Optimization for Vision-Language Models
1. 论文的主要贡献和创新点
✅ 解决的问题
现有视觉语言(VL)系统通过图像与检索文本结合推理，但数据源常存在分歧或联合无法支撑答案；现有VL模型的后训练目标对实例进行独立评分，无法在反事实证据变化下保持一致行为，难以可靠识别可信源并在证据不足时中止回答。

🚀 提出的新方法与思路
**CARGO-VL框架**：采用分组相对框架，将对齐、图像正确、文本正确、两者都错(A/V/T/N)四种证据状态作为一个捆绑(bundle)进行优化；其目标函数耦合了条件式正确性与反事实过渡奖励，涵盖答案不变性、源等价性、答案转中止的切换；同时引入primal-dual控制器平衡不安全回答与过度延迟的问题。
**XMC数据集（eXtended Modal Conflict）**：贡献了用于冲突训练的四条件冲突训练资源。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 反事实一致性 | 通过分组优化及反事实过渡奖励，解决现有方法无法在证据变化下保持一致行为的缺陷 |
| 冲突处理能力 | 提升对视觉与文本数据源分歧情况的处理能力，优于独立评分的点式基线 |
| 无支持答案避免 | 减少因数据源无法支撑答案而产生的错误回答 |
| 模态平衡 | 改善视觉与文本模态间的推理平衡 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| XMC（eXtended Modal Conflict） | 四条件冲突训练资源，用于模型冲突场景下的训练 |

🎯 实验设置与评估指标
任务为视觉语言模型的证据仲裁任务，需识别可信数据源并在证据不足时中止回答。
| 指标 | 含义 |
| --- | --- |
| 冲突处理能力 | 评估模型对视觉与文本数据源分歧的处理效果，论文未明确说明方向 |
| 无支持答案避免率 | 评估模型在数据源无法支撑答案时避免错误回答的比例，论文未明确说明方向 |
| 模态平衡度 | 评估模型在视觉与文本模态推理上的平衡程度，论文未明确说明方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| pointwise baselines | 点式基线方法 | 对每个实例进行独立评分，无反事实一致性优化 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能：论文未报告具体数值，仅提及在CMC-Bench和Modality-Bias的跨种子实验中，CARGO-VL在冲突处理、无支持答案避免、模态平衡上优于pointwise baselines。
2. 效率对比：论文未报告。
3. 跨域 / zero-shot 迁移：论文未报告具体数值，仅提及在CMC-Bench和Modality-Bias上的迁移评估。
4. 鲁棒性 / 扰动测试：论文未报告。
5. 消融实验：论文未报告具体消融实验的数值表，仅指出关系过渡信号与自适应风险控制对模型性能有互补增益。

4. 关键结论和发现
- 主要发现：1）CARGO-VL的分组相对优化框架及风险约束的primal-dual控制器，在冲突处理、无支持答案避免、模态平衡上均优于点式基线；2）关系过渡信号与自适应风险控制对模型性能有互补增益；3）反事实一致性是可靠多模态证据仲裁的实用目标。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：CARGO-VL是一种面向视觉语言模型的反事实仲裁框架，通过分组相对优化与风险约束机制，提升了模型在视觉与文本数据源分歧、证据不足场景下的仲裁能力，在多模态证据推理任务上优于点式基线方法。

</details>

---

### 5. [From Non-Convex Self-Concordant Regularization to Scalable Quasi-Newton Training of PINNs](https://arxiv.org/abs/2608.04206v1)

**Authors**: Chenhao Si, Kang An, Shiqian Ma, Ming Yan  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2608.04206v1  

#### Abstract
Physics-informed neural networks (PINNs) often require high-accuracy quasi-Newton refinement to obtain reliable partial differential equation solutions, but their residual objectives can exhibit indefinite, nearly singular, and poorly scaled local curvature. Regularized quasi-Newton methods provide ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

From Non-Convex Self-Concordant Regularization to Scalable Quasi-Newton Training of PINNs
1. 论文的主要贡献和创新点
✅ 解决的问题
PINN训练需高精度准牛顿精修以获得可靠偏微分方程（PDE）解，但PINN的残差目标存在不定、近乎奇异且缩放差的局部曲率，现有两类方法存在缺陷：（1）BFGS等准牛顿方法难以稳定处理这类特殊曲率；（2）正则化准牛顿方法侧重稳定割线模型，自协调方法侧重曲率相关步长选择，两者未有效结合适配PINN训练场景。

🚀 提出的新方法与思路
**SCORE（Self-concordance-inspired quasi-Newton method）**：提出带减量耦合的移位割线几何，用于PINN训练；核心机制为：从学到的逆度量计算单个准牛顿减量，该减量共同确定经强Wolfe测试的候选步，以及用于定义下一个割线几何的自适应移位；该移位位移表示接受步下的平均移位度量作用，无需构造Hessian或计算Hessian-vector乘积；在局部谱等价条件下，证明准牛顿减量和候选步与正移位度量下的对应量可比，匹配度量时可恢复归一化自协调规则；采用强Wolfe接受、 fallback线搜索和标准曲率保障实现全球化策略，不修改底层PINN目标。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 曲率处理能力 | 能处理PINN残差目标的不定、近奇异、缩放差的局部曲率，无需构造Hessian或计算Hessian-vector乘积 |
| 训练精度 | 在多个PDE基准上达到比BFGS、自缩放Broyden基线更低的最终误差 |
| 全球化策略 | 无需改动底层PINN目标即可实现训练全球化 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 黏性Burgers方程 | 基准测试，含消融实验 |
| Kuramoto--Sivashinsky方程 | 基准测试 |
| Korteweg--de Vries方程 | 基准测试 |
| complex Ginzburg--Landau方程 | 基准测试 |

🎯 实验设置与评估指标
任务：训练PINN以求解上述偏微分方程。
| 指标 | 含义 |
| --- | --- |
| 最终误差 | 越低越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| BFGS | 准牛顿方法基线 | 现有用于PINN训练的准牛顿方法 |
| 自缩放Broyden | 准牛顿方法基线 | 现有用于PINN训练的准牛顿方法 |
| SCORE | 本文提出的方法 | 自协调启发的准牛顿方法，带减量耦合的移位割线几何，无需构造Hessian，适配PINN残差目标 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体定量数值，仅定性说明SCORE的最终误差低于BFGS和自缩放Broyden基线。
1. 主 benchmark 性能
论文未报告具体定量数值，仅说明SCORE在黏性Burgers、Kuramoto--Sivashinsky、Korteweg--de Vries、complex Ginzburg--Landau四个PDE上的最终误差低于BFGS和自缩放Broyden基线。
2. 效率对比
论文未报告FPS、参数量等效率指标。
3. 跨域 / zero-shot 迁移
论文未报告相关实验结果。
4. 鲁棒性 / 扰动测试
论文未报告相关实验结果。
5. 消融实验
论文未提供消融实验的具体表号及数值，仅在黏性Burgers方程上定性说明：移位曲率稳定和基于减量的步长选择对PINN的高精度精修有互补贡献。

4. 关键结论和发现
- 核心发现：（1）SCORE方法可有效处理PINN残差目标的特殊局部曲率，无需构造Hessian；（2）SCORE在多个PDE基准上的最终误差低于现有BFGS和自缩放Broyden基线；（3）移位曲率稳定与基于减量的步长选择对PINN高精度精修有互补作用。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。

> ✅ **总结一句话**：本文针对PINN训练中残差目标的特殊局部曲率问题，提出了自协调启发的准牛顿方法SCORE，该方法无需构造Hessian即可稳定处理曲率，在多个PDE基准上实现了比现有准牛顿基线更低的最终误差，且训练全球化策略无需改动底层PINN目标。

</details>

---

### 6. [Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness](https://arxiv.org/abs/2608.04519v1)

**Authors**: Haoting Qian, Qingjie Zhang, Zhicong Huang, Cheng Hong, Han Qiu  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.04519v1  

#### Abstract
Benchmarking machine unlearning methods is critical to understand whether sensitive knowledge is removed from large language models (LLMs) or not. Current unlearning benchmarks include mainly single-hop questions and a narrow set of multi-hop questions. Although effective, they still face two challe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness
1. 论文的主要贡献和创新点
✅ 解决的问题
现有大语言模型（LLM）的遗忘基准主要聚焦单跳问题和窄范围多跳问题，存在两大核心痛点：（1）知识并非完全隔离，多样的多跳推理路径比普通查询更易引发知识泄露；（2）遗忘具有脆弱性，静态评估方式不足以衡量遗忘效果，因为遗忘的知识可通过轻量级后遗忘适配等恢复攻击部分恢复。
🚀 提出的新方法与思路
**\unlearning基准**，用于全面评估LLM在多样多跳推理路径和恢复攻击下的鲁棒知识移除效果，涵盖更丰富的推理路径类型与恢复攻击场景，解决现有基准的不足。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 多跳推理覆盖 | 支持多样多跳推理路径的评估，弥补现有基准多跳问题覆盖窄的不足 |
| 恢复攻击覆盖 | 纳入恢复攻击场景（如轻量级后遗忘适配）评估，解决现有静态评估的局限性 |
| 评估全面性 | 覆盖不同推理场景与恢复攻击的评估，更全面衡量遗忘效果 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 2个精心策划的数据集 | 用于\unlearning基准的评估 |
🎯 实验设置与评估指标
任务：评估LLM在多样多跳推理路径和恢复攻击下的知识移除鲁棒性
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告具体评估指标 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 6种unlearning方法 | 论文未报告 | 论文未报告具体类型及特点 |

3. 主要实验结果和性能指标
📊 定量结果汇总
1. 主 benchmark 性能（L2/碰撞率等）：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告
💡 结论：现有unlearning方法对多跳推理路径和恢复攻击具有脆弱性。

4. 关键结论和发现
- 现有LLM遗忘基准存在多跳推理覆盖不足、未纳入恢复攻击评估的问题，静态评估方式不全面，无法准确衡量遗忘的鲁棒性。
- 现有LLM遗忘方法在面对多跳推理路径和恢复攻击时表现脆弱，未达到鲁棒知识移除的要求。
- 需进一步探索LLM遗忘过程中遗忘质量、鲁棒性与模型效用三者间的权衡关系。
方法局限性：现有遗忘基准的覆盖范围仍有不足，现有遗忘方法在鲁棒性表现上存在明显缺陷。
未来工作：聚焦于提升遗忘方法对多跳推理路径和恢复攻击的鲁棒性，研究遗忘质量、鲁棒性与模型效用间的平衡策略。

> ✅ **总结一句话**：本文提出了新的\unlearning基准，用于评估大语言模型在多样多跳推理路径和恢复攻击下的知识移除鲁棒性，发现现有遗忘方法在该基准下表现脆弱，并指出了需权衡遗忘质量、鲁棒性与模型效用的核心问题。

</details>

---

### 7. [Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning](https://arxiv.org/abs/2608.04646v1)

**Authors**: Ian B. de Haan, Peter van der Putten, Max van Duijn  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.04646v1  

#### Abstract
Large language models (LLMs) have recently shown strong performance on Theory of Mind (ToM) tests, prompting debate about the nature and validity of the underlying capabilities. At the same time, reasoning-oriented LLMs trained via reinforcement learning with verifiable rewards have demonstrated not...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
当前大语言模型（LLMs）在Theory of Mind（ToM）测试上的优异表现引发了关于其背后能力本质与有效性的争议；同时，经带可验证奖励的强化学习训练的推理型LLMs虽在多基准任务中表现提升，但这类模型在ToM任务中的行为特点及能力来源尚未得到针对性研究。

🚀 提出的新方法与思路
**跨方法评估的ToM分析框架**：采用适配版机器心理实验任务与现有成熟ToM基准结果相结合的方式，研究推理型LLMs在ToM任务中的表现，重点分析其对提示变化、任务扰动的鲁棒性。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| ToM能力评估维度 | 不仅衡量任务准确率，还额外关注模型对提示与任务变化的鲁棒性，更全面反映模型能力 |
| 能力归因的准确性 | 可区分模型表现提升来自鲁棒性增强而非新的ToM特定能力，为解决ToM能力本质的争议提供新视角 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 改编后的机器心理实验数据集 | 用于评估推理型LLMs在ToM任务中对提示变化、任务扰动的鲁棒性表现 |
| 已建立的ToM基准数据集 | 用于验证模型在常规ToM任务中的整体表现 |

🎯 实验设置与评估指标
任务：对比经带可验证奖励的强化学习训练的推理型LLMs与普通LLMs，在ToM任务中对提示变化、任务扰动的鲁棒性差异，同时参考ToM任务准确率。
| 指标 | 含义 |
| --- | --- |
| 提示扰动鲁棒性得分 | 越高越好 |
| 任务扰动鲁棒性得分 | 越高越好 |
| ToM任务准确率 | 越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 普通LLM | 通用未定向训练的LLM | 未经过带可验证奖励的强化学习训练，在ToM任务中对提示变化、任务扰动的鲁棒性较低 |
| 推理型LLM | 经带可验证奖励的强化学习训练的LLM | 在多基准任务中表现提升，在ToM任务中对提示变化、任务扰动的鲁棒性更高 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告具体实验表格及对应的数值，仅在摘要中说明核心观察结果：推理型LLMs在ToM任务中对提示变化和任务扰动的鲁棒性相比普通LLMs显著更高。
💡 结论：推理型LLMs在ToM任务中的表现提升至少部分源于其在提示与任务扰动下更易得到正确答案的能力，而非获得了新的ToM特定能力。

4. 关键结论和发现
- 主要发现：① 经带可验证奖励的强化学习训练的推理型LLMs，在ToM任务中相较普通LLMs，对提示变化和任务扰动的鲁棒性更突出；② 这类推理模型在ToM任务中的表现提升核心来自于鲁棒性增强，而非具备新的ToM特定能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本研究通过适配机器心理实验并结合现有ToM基准，揭示经带可验证奖励的强化学习训练的推理型LLMs在ToM任务中的鲁棒性提升，支持其能力提升源于鲁棒性而非新ToM特定能力的结论。

</details>

---

### 8. [Discretization and Statistical Consistency of Functional Flow Matching](https://arxiv.org/abs/2608.04531v1)

**Authors**: Lennon J. Shikhman  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2608.04531v1  

#### Abstract
Functional flow matching is posed on distributions of functions but implemented from finitely many coefficients or point values. Under scattered or adaptive refinement, the resulting conditioning sigma-algebras need not be nested, so martingale convergence does not justify the sensor limit. We prove...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文标题：Discretization and Statistical Consistency of Functional Flow Matching
1. 论文的主要贡献和创新点
✅ 解决的问题
功能流匹配基于函数分布实现，需依赖有限个系数或点值落地；当存在散射或自适应细化时，所得条件σ代数非嵌套，导致鞅收敛无法作为传感器极限的合理性依据。

🚀 提出的新方法与思路
**强L²收敛性证明** 证明每个强一致的有限秩重构序列对应的有限条件速度目标具有强L²收敛性，给出正交投影的定量界，并通过正则空间实现点传感器的扩展。
**端到端Wasserstein界构建** 针对学习到的流，直接耦合到population superposition path，得到无需假设人口有限维ODE唯一性的端到端Wasserstein界。
**归一化求积神经算子验证** 验证归一化求积神经算子的传感器无关常数，包括全局Lipschitz激活的显式幅度递归。
**特殊案例与误差率分析** 通过非对易迹类高斯例子得到投影限制下边界乘数为0、精确条件下为0.72的结果；结合空间正则性-求积证书闭合算子实现项，利用Bernstein论证得到固定模型维度和包络下的超额风险项$\widetilde{O}(n^{-1})$；通过可精确实现的截尾高斯缩放专门化得到显式端到端率。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 收敛性逻辑 | 解决非嵌套条件σ代数导致的鞅收敛失效问题，确立有限条件速度目标的强L²收敛性 |
| 学习流界估计 | 脱离人口有限维ODE唯一性假设，建立更普适的端到端Wasserstein界 |
| 误差率刻画 | 提供显式超额风险率与端到端误差率，明确算法的误差上界特性 |

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
论文未报告 | -

🎯 实验设置与评估指标
论文未报告具体实验任务与评估指标，仅围绕理论层面展开分析

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
论文未报告 | - | -

3. 主要实验结果和性能指标
📊 定量结果汇总
所有相关实验：论文未报告

4. 关键结论和发现
- 针对功能流匹配的离散化一致性痛点，证明强一致有限秩重构序列下有限条件速度目标的强L²收敛性，给出正交投影定量界与点传感器扩展的正则空间路径。
- 学习流的端到端Wasserstein界可脱离人口有限维ODE唯一性假设，降低了流匹配算法的适用限制。
- 非对易迹类高斯例子给出了不同条件下的边界乘数结果，结合Bernstein论证得到显式超额风险率$\widetilde{O}(n^{-1})$。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：这篇论文针对功能流匹配的离散化统计一致性核心痛点，确立了有限条件速度目标的强L²收敛性，构建了无需依赖ODE唯一性的端到端Wasserstein界，推导了一系列显式理论误差率，完善了功能流匹配落地的统计理论基础。

</details>

---

### 9. [Joint UAV Flight and Opportunistic Routing under Reinforcement Learning for Delay-Tolerant Networks](https://arxiv.org/abs/2608.04590v1)

**Authors**: Xiao Wang, Shun-Ren Yang  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2608.04590v1  

#### Abstract
The growing deployment of delay-tolerant networks (DTNs) has made store-carry-forward (SCF) communication indispensable under sparse connectivity.
  However, intermittent contacts, finite buffers, and limited message time-to-live (TTL) often give rise to sparse delivery and congestion, leading to su...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Joint UAV Flight and Opportunistic Routing under Reinforcement Learning for Delay-Tolerant Networks
1. 论文的主要贡献和创新点
✅ 解决的问题
延迟容忍网络（DTN）采用存储-携带-转发（SCF）通信时，存在间歇性连接、有限缓存、消息生存时间（TTL）有限的问题，常导致消息交付稀疏与拥塞，引发端到端性能大幅下降。
现有对比方法的缺陷：论文未报告。

🚀 提出的新方法与思路
**JUROR（Joint UAV flight and Opportunistic Routing）**：基于PPO框架，将联合UAV飞行与机会路由优化问题转化为含序列运动-路由耦合和每步团队奖励的因子化部分可观测马尔可夫决策过程（POMDP）；采用集中式训练与去中心化执行（CTDE）架构，智能体基于本地观测执行去中心化动作，训练时评论家使用全局统计信息，可选多视界热点预测器提供辅助监督。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 网络性能 | 在四种流量模式的仿真中，对PRoPHET和MaxProp方法取得有效增益 |
| 执行架构 | 保留接触受限下的去中心化执行能力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
任务：联合优化延迟容忍网络（DTN）中UAV飞行与机会路由，采用仿真验证性能。
| 指标 | 含义 |
| ---- | ---- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| PRoPHET | 机会路由方法 | 论文未报告 |
| MaxProp | 机会路由方法 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告

💡 结论：论文未报告

4. 关键结论和发现
- 主要发现：所提JUROR方法在四种流量模式的仿真中，相比PRoPHET和MaxProp取得有效性能增益，且保留了接触受限下的去中心化执行能力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：提出基于PPO框架的JUROR方法，通过联合优化UAV飞行与DTN机会路由，在接触受限的去中心化执行场景下提升了网络性能。

</details>

---

### 10. [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139v1)

**Authors**: Yinghui He, Ling Yang, Jiarui Liu, Yongjin Yang, Lechen Zhang, Yingcheng Wu, Zhenfei Yin, Mengdi Wang, Sanjeev Arora  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 34.0  
**Type**: new  
**ArXiv ID**: 2608.05139v1  

#### Abstract
Long-horizon reasoning in recent LLMs demands that the model switch between distinct skills inside a reasoning chain, such as first doing a math derivation, then using the result to plan a schedule. We call such problems cross-skill long-horizon tasks: multi-step tasks whose steps require different ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

### Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题：现有LLM长时序推理相关基准多聚焦于评估单个技能，缺乏衡量模型在推理链中不同技能间切换能力的可量化原则性方法；跨技能长时序任务要求模型在推理中切换不同技能并依赖前期输出，现有方法难以应对该需求。
🚀 提出的新方法与思路
**Skill Entropy**：一种用于量化从一个技能切换到另一技能难度的指标；
**Skill²-Bench**：构建的基于9个可验证且开放式领域的558项技能的跨技能长时序任务基准，每个任务分配任务级Skill Entropy分数并划分成三个难度等级；
**Skill-Entropy RL**：一种强化学习框架，模型在每一步不仅预测答案，还预测所用技能，奖励函数由步骤级正确性与衡量模型预测技能序列和黄金技能序列对齐度的Skill Entropy奖励组合而成。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 跨技能长时序推理评估 | Skill Entropy可量化技能切换难度，Skill²-Bench填补现有基准缺乏跨技能切换能力评估维度的空白 |
| 模型训练 | 将Skill Entropy转化为可复用的训练信号，Skill-Entropy RL可提升模型跨技能长时序推理性能 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| Skill²-Bench | 评估8个前沿模型及4个开源模型的跨技能长时序推理能力，验证基准有效性 |
| OpenR1-Math | 验证Skill Entropy作为训练信号的可复用性 |
🎯 实验设置与评估指标
实验任务：评估LLM在跨技能长时序任务上的性能；评估指标：Skill²-Bench准确率（↑越高越好）。
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有竞争性训练方法 | 训练基线 | 未利用Skill Entropy作为训练信号，跨技能长时序推理性能弱于Skill-Entropy RL训练的模型 |

3. 主要实验结果和性能指标
📊 定量结果汇总
**主 benchmark 性能**
论文未提及该实验对应表号、图号或章节，仅摘要提及：在Skill²-Bench上评估模型发现“技能切换差距”——高Skill Entropy任务的准确率更低；应用Skill-Entropy RL后，模型在Skill²-Bench上的准确率得到提升，且该方法可复用至OpenR1-Math等现成训练数据。
💡 结论：应用Skill-Entropy RL可有效提升模型在跨技能长时序任务上的性能，且Skill Entropy具有可复用性。
其他实验（效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验）：论文未报告。

4. 关键结论和发现
- 主要发现：1. 现有LLM长时序推理基准缺乏跨技能切换能力的评估维度，Skill²-Bench与Skill Entropy可有效弥补该缺失；2. Skill-Entropy RL作为训练信号能显著提升模型跨技能长时序推理性能；3. Skill Entropy作为训练信号具有可复用性，可应用于现成训练数据。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。
✅ 总结一句话：该论文提出Skill Entropy指标与Skill²-Bench基准，开发Skill-Entropy RL训练框架，有效解决现有方法缺乏跨技能长时序推理评估与训练信号的问题，提升了LLM的跨技能长时序推理能力。

</details>

---

### 11. [When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents](https://arxiv.org/abs/2608.04574v1)

**Authors**: Yushi Sun, Yanjie Zhang  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.04574v1  

#### Abstract
Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it ...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

# When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
## 1. 论文的主要贡献和创新点
✅ 解决的问题
Memory增强的VLM agents依赖持久空间知识，但环境变化时该知识会过时（stale）；当前模型在必须调和自信的过时记忆声明与矛盾观测时，能否在演变为安全相关错误前检测冲突，现有研究未充分回答该问题及相关安全影响。

🚀 提出的新方法与思路
使用dynamic FrozenLake测试床，在三种闭源模型、三种开源VLMs的文本和图像输入下，同时开展stale检测任务与下游导航任务，共进行1800次检测运行、12000次文本模式导航剧集（四个LLM导航器，共享50种子规模），系统研究空间记忆stale的影响及相关安全后果。

🔍 相比现有方法的优势
现有研究未系统开展VLM agents中空间记忆stale的实证研究，尤其是结合视觉输入的情况及对下游安全的影响；本文明确了文本可解性与视觉接地的不匹配、stale记忆的安全代价、审计方法的局限性等核心问题，识别了可靠视觉接地与记忆-观测冲突下的动作选择这一核心开放挑战，为后续研究提供参考。

## 2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| dynamic FrozenLake测试床 | 用于开展空间记忆stale检测任务与下游导航任务的动态环境实验 |

🎯 实验设置与评估指标
任务为结合stale检测与下游导航的动态环境实验，评估指标包括stale检测的F1分数、导航任务中的死亡概率（安全相关指标），以及检测运行数量、导航剧集数量。
| 指标 | 含义 |
| --- | --- |
| 视觉F1分数 | 衡量stale检测任务中视觉输入下的检测准确率，无方向 |
| 死亡概率 | 衡量导航任务中因使用过时记忆导致的安全相关失败概率，无方向 |
| 检测运行数量 | stale检测任务的运行次数，无方向 |
| 导航剧集数量 | 导航任务的运行次数，无方向 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 三种闭源模型 | 闭源VLM | 包含GPT-4o等闭源视觉语言模型，用于stale检测与导航任务 |
| 三种开源VLMs | 开源VLM | 开源视觉语言模型，用于stale检测与导航任务 |
| 四个LLM导航器 | LLM导航器 | 用于导航任务的大型语言模型，共享50种子规模 |

## 3. 主要实验结果和性能指标
📊 定量结果汇总
**stale检测任务性能（场景：dynamic FrozenLake环境）**
| 指标 | 数值（论文摘要提供，无对应表号） |
| --- | --- |
| 视觉F1分数 | 跨度为0.067至0.887 |
💡 结论：模型在文本输入下能可靠标记过时条目，但相同网格的视觉输入下检测性能差异极大。

**导航任务安全性能（场景：primary GPT-4o设置）**
| 方法 | 死亡概率相对值 |
| --- | --- |
| 信任原始stale记忆 | 比无记忆设置高两倍多 |
💡 结论：不审计而使用stale记忆会显著增加agent的安全风险。

**审计方法效果（场景：文本模式）**
| 方法 | 安全成本变化 |
| --- | --- |
| 透明读时过滤（审计） | 减少了大量安全成本 |
| oracle stale标签 | 无进一步显著增益 |
| 视觉审计（不可靠） | 过滤无一致益处 |
💡 结论：审计能部分降低安全风险，但未完全解决问题，视觉审计不可靠时无效。

论文未报告 主 benchmark 性能
💡 结论：论文未报告主benchmark性能（如L2、碰撞率）。

论文未报告 效率对比（FPS / 参数量）
💡 结论：论文未报告效率相关指标的对比结果。

论文未报告 跨域 / zero-shot 迁移
💡 结论：论文未报告跨域或zero-shot迁移的相关结果。

论文未报告 鲁棒性 / 扰动测试
💡 结论：论文未报告鲁棒性或扰动测试的相关结果。

论文未报告 消融实验
💡 结论：论文未报告消融实验的相关结果。

## 4. 关键结论和发现
- 2-3条主要发现
1. 文本可解性不代表视觉接地，模型在文本输入下能可靠标记过时条目，却在相同网格的视觉输入下表现差异极大，最弱的模型仍会做出无视图像的流畅自信决策；
2. 不审计而使用过时记忆是安全隐患，信任无审计的过时记忆的agent死亡概率显著高于无记忆的agent；
3. 审计方法能降低部分安全成本，但未完全解决问题，尤其是视觉审计不可靠时，过滤方法无一致益处。
- 方法局限性
论文未报告
- 未来工作
提升VLM agents在记忆-观测冲突下的可靠视觉接地能力与动作选择能力，是记忆增强型VLM agents的核心开放挑战。

✅ **总结一句话**：本文系统实证了空间记忆stale对VLM agents的安全影响，揭示了文本与视觉检测的不匹配、stale记忆的安全代价、审计方法的局限性等关键问题，为相关领域的后续研究明确了核心开放挑战。

</details>

---

### 12. [A Systolic Array Architecture for Nonlinear Activation Functions and Softmax Computation using Chebyshev Polynomials](https://arxiv.org/abs/2608.04734v1)

**Authors**: Benedikt Schaible, Anirudh Suresh Bharadwaj, Ulf Schlichtmann, Jiang Hu  
**Category**: cs.AR  
**Published**: 2026-08-06  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2608.04734v1  

#### Abstract
Neural Network Accelerators have gained popularity in recent years due to their greater efficiency than CPU-based platforms. Often, these accelerators utilize different hardware units for univariate activation functions, such as tanh, and the multivariate softmax, thereby missing opportunities for r...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

A Systolic Array Architecture for Nonlinear Activation Functions and Softmax Computation using Chebyshev Polynomials
1. 论文的主要贡献和创新点
- 解决的问题：现有神经网络加速器通常为不同的单变量激活函数（如tanh）和多变量softmax函数配备独立的硬件单元，导致硬件资源无法有效共享；同时现有基于近似计算的方案存在精度不足、硬件开销大的缺陷。
🚀 提出的新方法与思路
**Chebyshev多项式近似的脉动阵列激活单元架构**，该架构采用脉动阵列结构，利用Chebyshev多项式近似算法，设计可同时支持多类单变量激活函数与softmax函数计算的统一硬件单元，以解决硬件资源复用不足、近似计算性能缺陷的问题。
🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| tanh近似精度（MAE） | 相比CORDIC baseline降低71% |
| 硬件面积 | 相比CORDIC baseline减少4.6% |
| 功耗 | 相比CORDIC baseline减少5.1% |
| softmax近似精度（KL散度） | 相比CORDIC baseline降低44.6%；相比分段线性近似降低79.0% |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 论文未报告 | 论文未报告相关实验所用数据集 |
🎯 实验设置与评估指标
任务为评估支持多类单变量激活函数（含tanh）与softmax计算的硬件单元性能。
| 指标 | 含义（箭头标方向，如 ↓ 越低越好） |
| ---- | ---- |
| MAE | 平均绝对误差，↓ 越低越好 |
| KL散度 | Kullback-Leibler散度，↓ 越低越好 |
| 硬件面积 | 电路硬件面积，↓ 越低越好 |
| 功耗 | 硬件功耗，↓ 越低越好 |
⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| CORDIC baseline | 近似计算方法 | 现有用于激活函数、softmax近似计算的基准方法 |
| 分段线性近似 | 近似计算方法 | 现有用于softmax近似计算的另一种方法 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告主benchmark性能、效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验的相关实验内容及结果，仅在摘要中提及近似计算的相关结果，无对应图表编号。
**定量结果（摘要提及）**
基于Chebyshev多项式的脉动阵列激活单元，计算tanh时的平均绝对误差（MAE）相比CORDIC baseline降低71%，硬件面积减少4.6%，功耗减少5.1%；计算softmax时的KL散度相比CORDIC baseline降低44.6%，相比分段线性近似降低79.0%。
💡 结论：该基于Chebyshev多项式近似的脉动阵列架构，在激活函数与softmax的近似计算性能上，相比现有基线方法实现了计算精度的提升，同时降低了硬件面积与功耗开销。

4. 关键结论和发现
- 主要发现：① 提出的脉动阵列激活单元架构可实现多类单变量激活函数与softmax函数的统一硬件计算，解决了现有加速器硬件资源无法共享的痛点；② 采用Chebyshev多项式近似的该架构，相比CORDIC baseline和分段线性近似方法，具备更高的近似计算精度，且硬件面积与功耗开销更低。
- 方法局限性：论文未报告。
- 未来工作：论文未报告。
> ✅ **总结一句话**：该论文提出了一种基于Chebyshev多项式近似的脉动阵列激活单元架构，可同时支持多类单变量激活函数与softmax函数的统一硬件计算，相比现有基线方法提升了计算精度，降低了硬件面积与功耗开销。

</details>

---

### 13. [K-EXAONE 2.0 Technical Report](https://arxiv.org/abs/2608.04505v1)

**Authors**: Eunbi Choi, Kibong Choi, Sehyun Chun, Seokhee Hong, Junwon Hwang, Hyojin Jeon, Ahra Jo, Hyunjik Jo, Yeonsik Jo, Minhyeok Jung, Doyoung Kim, Heegyu Kim, Joonkee Kim, Seonghwan Kim, Soyeon Kim, Sunkyoung Kim, Yireun Kim, Yongil Kim, Byungoh Ko, Changhun Lee, Dohaeng Lee, Haeju Lee, Jinsik Lee, Kyungmin Lee, Minwoo Lee, Wonkee Lee, Sangha Park, Sungjune Park, Kwangrok Ryoo, Kijung Seo, Minju Seo, Yongwoo Song, Sejong Yang, Heuiyeen Yeen, Stanley Jungkyu Choi, Yemuk Choi, Yongchan Chun, Jiwon Ham, Dasol Hong, Sujeong Im, Kijeong Jeon, Gerrard Jeongwon Jo, Hyeongjun Jo, Yujin Jo, Jiyeon Jung, Naeun Kang, Daeseong Kim, Euisoon Kim, Hayeon Kim, Hyosang Kim, Myoungshin Kim, Unsol Kim, Youchul Kim, Chaeeun Lee, ChaeYoon Lee, Edward Hwayoung Lee, Honglak Lee, Hwansoo Lee, Minkyung Lee, Sangeun Lee, Solji Lim, Woohyung Lim, Chanwoo Moon, Jueun Mun, Jimin Park, Seojeong Park, Yongmin Park, Hyerin Seo, Donghyeon Shin, Donghyun Son, Eunyong Son, Kaehyun Um, Sihoon Yang, Chang En Yea, Sihyuk Yi, Kyungjae Yoo, Chansik Yoon  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2608.04505v1  

#### Abstract
This technical report presents K-EXAONE 2.0, an open-weight multilingual foundation model developed by LG AI Research as a step in our effort toward global frontier-scale foundation models. Rather than training from scratch, we upcycle K-EXAONE and expand its architecture, yielding a Mixture-of-Expe...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

论文总结：K-EXAONE 2.0 Technical Report
1. 论文的主要贡献和创新点
✅ 解决的问题
- 原K-EXAONE模型参数容量有限，无法支撑更高复杂度的任务；
- 原K-EXAONE仅支持6种语言，难以适配多语言应用场景；
- 原K-EXAONE在agentic coding、长上下文理解等特定能力上存在不足，且缺乏基于韩国社会文化语境的安全性优化。

🚀 提出的新方法与思路
**MoE架构扩展**：在原K-EXAONE基础上升级架构，构建混合专家（Mixture-of-Experts, MoE）模型，提升模型整体参数容量与激活参数规模。
**多阶段训练流程**：采用持续预训练、聚焦难度的中期训练、后训练结合的训练流水线，针对性强化模型的推理能力、agentic coding能力、多语言能力及基于韩国社会文化语境的安全性。
**场景适配能力增强**：扩展语言覆盖范围至10种，提升上下文长度支持上限，适配长上下文应用场景。

🔍 相比现有方法的优势
| 维度 | 优势 |
| --- | --- |
| 模型架构 | 采用MoE架构，容量显著提升，适配更高复杂度任务 |
| 语言支持 | 语言覆盖从6种扩展至10种，支持更多语言场景 |
| 长上下文能力 | 支持更长上下文长度，长上下文理解与检索能力突出 |
| 特定能力表现 | 在agentic coding、韩国社会文化语境安全性上有明确优势，在9项评估类别中优于原K-EXAONE，与同类型开源模型有竞争力 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| --- | --- |
| 论文未报告 | 论文未报告 |

🎯 实验设置与评估指标
本实验针对9项反映实际使用的评估类别开展，测试模型多维度应用能力。
| 指标 | 含义 |
| --- | --- |
| 论文未报告 | 论文未报告 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| --- | --- | --- |
| 论文未报告 | 论文未报告 | 论文未报告 |

3. 主要实验结果和性能指标
📊 定量结果汇总
所有实验相关定量结果、表格信息论文未报告：
1. 主 benchmark 性能：论文未报告
2. 效率对比（FPS / 参数量）：论文未报告
3. 跨域 / zero-shot 迁移：论文未报告
4. 鲁棒性 / 扰动测试：论文未报告
5. 消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. K-EXAONE 2.0通过升级架构与多阶段训练，在agentic coding、长上下文理解、韩国语境安全性等核心能力上相比原K-EXAONE有明显提升，与同类型开源模型竞争力相当；
  2. K-EXAONE 2.0的长上下文检索能力、韩国社会文化语境下的安全性表现突出；
  3. K-EXAONE 2.0扩展了多语言覆盖范围与上下文长度支持，具备更广泛的实际应用潜力。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：K-EXAONE 2.0是LG AI Research基于K-EXAONE升级开发的开源多语言MoE基础模型，在agentic coding、长上下文能力、韩国语境安全性等维度较前身明显优化，具备更强的实际应用价值与更广泛应用场景潜力。

</details>

---

### 14. [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](https://arxiv.org/abs/2608.04771v1)

**Authors**: Qiyuan Zhu, Dezhi Li, Pengyu Cheng, Tianle Chen, Jiacheng Wang, Ruijie Shen, Hao Gu, Sida Lin, Zirui Liu, Jiacheng Liu, Sirui Han  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.04771v1  

#### Abstract
Large Reasoning Models (LRMs) excel on complex tasks through long chain-of-thought (CoT) reasoning, but their lengthy intermediate steps cause severe overthinking that inflates inference cost. KV-cache compression is a common solution, yet existing reasoning-oriented methods apply a uniform policy a...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning
1. 论文的主要贡献和创新点
✅ 解决的问题
大型推理模型（LRMs）通过长链式思考（CoT）推理完成复杂任务，但过长的中间步骤导致严重过度思考，大幅增加推理成本；现有推理导向的KV缓存压缩方法存在两处核心缺陷：
① 仅对整个轨迹应用统一压缩策略，未考虑推理过程中不同步骤对上下文丢失的容忍度差异；
② 压缩操作在生成端并非无成本，更小的缓存会导致模型生成更多token，部分抵消压缩带来的效率提升。

🚀 提出的新方法与思路
**Reward-adaptive KV-cache compression**：基于轻量过程奖励估计器对每一步完成步骤评分，高奖励步骤对保留的缓存进行更强压缩，低奖励步骤压缩程度更低，匹配不同步骤的上下文丢失容忍度。
**Reward-banded penalty on reflection tokens**：对反射token施加与奖励相关的惩罚，约束冗余生成，降低压缩在生成端的代价。
**Confidence-based early stopping**：当模型判断推理可靠时触发早停，进一步减少不必要的生成步骤。

🔍 相比现有方法的优势
| 维度 | 优势 |
| ---- | ---- |
| 生成token数 | 对比Full CoT有显著减少 |
| 端到端延迟 | 对比Full CoT有明显降低 |
| 推理准确率 | 与Full CoT基本保持一致 |

2. 核心实验方法和设置
📚 使用的数据集
| 数据集 | 用途 |
| ---- | ---- |
| 六个未明确命名的推理基准 | 评估ReCo在不同推理模型上的推理效率与准确率保持情况 |

🎯 实验设置与评估指标
本实验针对大型推理模型的CoT推理效率问题，基于三个推理模型和六个基准评估ReCo框架的性能与准确率保持能力，评估指标如下：
| 指标 | 含义（箭头标方向） |
| ---- | ---- |
| 生成token数 | 衡量推理产生的中间token数量，↓越低越好 |
| 端到端延迟 | 衡量推理全程耗时，↓越低越好 |
| 推理准确率 | 衡量推理结果的正确性，→越高越好 |

⚔️ 基线方法对比
| 方法 | 类型 | 特点 |
| ---- | ---- | ---- |
| 现有推理导向的KV缓存压缩方法 | 推理压缩方法 | 对整个轨迹应用统一压缩策略，未利用过程奖励适配不同步骤 |
| Full CoT | 全链式思考生成方法 | 无缓存压缩，生成完整的链式思考序列 |

3. 主要实验结果和性能指标
📊 定量结果汇总
论文未报告，无对应表号、图号等来源，无法提供具体定量实验结果。

4. 关键结论和发现
- 主要发现
1. 推理过程中不同步骤对上下文丢失的容忍度存在差异，过程奖励可有效跟踪这种差异，用于优化缓存压缩策略；
2. KV缓存压缩并非完全无成本，压缩操作会在生成端导致更多token生成，部分抵消压缩带来的效率提升；
3. 提出的ReCo框架可在多个推理模型和基准上，在减少推理成本的同时保持推理准确率。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：论文提出Reward-Coordinated Compression（ReCo）框架，通过基于过程奖励的自适应KV缓存压缩、冗余生成惩罚和早停机制，在保持大型推理模型推理准确率的同时大幅提升了推理效率。

</details>

---

### 15. [The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads](https://arxiv.org/abs/2608.04570v1)

**Authors**: Yushi Sun, Yanjie Zhang, Rui Sheng  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2608.04570v1  

#### Abstract
Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined. We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports. We introduce MirageBench, comprising 150 personas balance...

<details>
<summary><strong>🤖 AI Summary (by doubao-seed-2-0-mini-260428)</strong> - Click to expand</summary>

The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads
1. 论文的主要贡献和创新点
✅ 解决的问题
- 个性化LLM依赖的持久记忆构建的用户模型的忠实性从未被系统检验，存在LLM编造超出证据支持的用户属性的过度推理（OI）问题；
- 现有模型的自我监控机制无法可靠反映模型实际的过度推理情况，存在自我监控反转现象，自报告信号不适用于模型选择。

🚀 提出的新方法与思路
**MirageBench基准构建**：构建包含150个用户角色（均衡覆盖刻板、反刻板、中性类型）、6个个性化任务（横跨“想象梯度”）的基准数据集；提出由独立评审员操作的四分类忠实性分类法，经盲人类标注者验证：四分类Cohen's kappa=0.863，二分类Cohen's kappa=0.900；并基于该基准生成覆盖7个家族12个模型的143616条评审用户属性claims的排行榜。

🔍 相比现有方法的优势
维度 | 优势
--- | ---
忠实性评估可靠性 | 提出经盲人类标注验证的四分类与二分类忠实性分类框架，保证评估标准的一致性
基准覆盖全面性 | 包含不同类型用户角色与不同难度的个性化任务，覆盖“想象梯度”以全面评估过度推理风险
模型评估广度 | 覆盖7个家族12个主流LLM的评估，为个性化LLM的忠实性检验提供大规模实验基准

2. 核心实验方法和设置
📚 使用的数据集
数据集 | 用途
--- | ---
MirageBench | 用于评估个性化LLM基于持久记忆构建的用户模型的忠实性，由150个用户角色、6个个性化任务、143616条经过评审的用户属性claims构成

🎯 实验设置与评估指标
任务：评估个性化LLM用户模型的忠实性，核心测量过度推理（OI）的程度
指标 | 含义（方向）
--- | ---
judge-measured OI | 独立评审员判定的过度推理claims占比（过高为负面）
self-assessed OI | 模型自报告的过度推理claims占比（过低报告为负面）
Cohen's kappa | 分类一致性系数，越高一致性越强（↑ 越高越好）
AUROC | 衡量模型内部自审计对自身claims的排序能力，越高性能越好（↑ 越高越好）

⚔️ 基线方法对比
方法 | 类型 | 特点
--- | --- | ---
7个家族共12个主流LLM | 个性化LLM | 具备持久记忆，用于构建用户模型以支撑个性化服务，作为本次评估的基准方法

3. 主要实验结果和性能指标
📊 定量结果汇总
**MirageBench主基准性能（无对应表）**
| 指标 | 数值 |
--- | ---
单模型OI claims占比范围 | 35%--49% |
跨模型OI均值 | 41.6% |
claim加权OI均值 | 41.8% |
任务间OI占比范围 | 27%--59% |

💡 结论：所有评估的个性化LLM均存在普遍的过度推理问题，过度推理比例在不同模型和任务间存在差异。

**Self-Monitoring Inversion结果（无对应表）**
| 指标 | 数值 | 统计信息 |
--- | --- | ---
self-assessed OI与judge-measured OI的秩相关系数rho | -0.60 | 探索性，自举置信区间[-0.90, +0.06]，样本量n=12，p=0.044 |
单个模型自审计AUROC范围 | 0.58--0.83 | - |

💡 结论：存在自我监控反转现象，模型自报告的过度推理情况与实际测量结果负相关，自报告信号不适用于模型比较。

> 效率对比、跨域/zero-shot迁移、鲁棒性/扰动测试、消融实验：论文未报告

4. 关键结论和发现
- 主要发现：
  1. 过度推理（OI）在所有评估的个性化LLM中普遍存在，每个模型的过度推理claims占比达35%--49%，跨模型均值达41.6%；
  2. 存在自我监控反转现象：模型自报告的过度推理情况与评审测量结果负相关，自报告信号不适用于模型选择，尽管单个模型内部自审计对自身claims的排序仍有一定能力（AUROC 0.58--0.83）；
  3. 过度推理具有任务依赖性，占比在27%--59%之间，多轮交互中推断的用户属性呈近似线性积累，极少修订。
- 方法局限性：论文未报告
- 未来工作：论文未报告

> ✅ **总结一句话**：本论文通过构建MirageBench基准，揭示个性化LLM普遍存在编造用户属性的过度推理问题，且模型自我监控机制存在误导性，主张采用外部验证作为个性化LLM的可靠基础。

</details>

---

### 16. [Interoceptive Attention as Dynamic Homeostatic Prioritization in a Foraging Agent](https://arxiv.org/abs/2608.04232v1)

**Authors**: St John Grimbly, Nicolas Kuske, Evert A. Boonstra, Bruce A. Bassett, Charel van Hoof, Rowan Hodson, Benjamin Rosman, Ryan Smith, Mark Solms, Jonathan P. Shock  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.04232v1  

#### Abstract
Biological systems must regulate competing needs under limited perceptual bandwidth, where sharpening one estimate costs the capacity to sharpen the others. Any fixed-budget system therefore has to decide where to allocate its perceptual precision. We study this in a foraging agent that must keep se...

---

### 17. [Reward Structure Shapes the Interaction Between Episodic Exploration and Neural Memory in Reinforcement Learning](https://arxiv.org/abs/2608.05111v1)

**Authors**: Jai Malegaonkar, Rohan Patil, Henrik I. Christensen  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2608.05111v1  

#### Abstract
In partially observable reinforcement learning, agents face a dual bottleneck: they must explore to encounter rewarding states and retain that experience in memory to optimize their policies. Exploration bonuses and memory architectures are traditionally evaluated in isolation, leaving their interac...

---

### 18. [Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools](https://arxiv.org/abs/2608.04719v1)

**Authors**: Atul Anand, Sourav Chattaraj  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2608.04719v1  

#### Abstract
Agent evaluations tell us that a model picked the wrong tool, but rarely why. We introduce canary tools: diagnostic probe tools planted in an agent's Model Context Protocol (MCP) tool set, each engineered to probe one specific tool-selection weakness. A six-type taxonomy (semantic decoys, parameter ...

---

### 19. [Mind the Cap: Output-Budget Regimes Change the Measured Multilingual Reasoning Gap](https://arxiv.org/abs/2608.04160v1)

**Authors**: Ankit Goyal, Jaideep Ray  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2608.04160v1  

#### Abstract
Multilingual evaluations report accuracy at a single output-token cap, but languages need different numbers of tokens to express the same content, so the cap is a hidden experimental variable. We test whether the native-vs-translate gap on MGSM (German, Thai, Swahili) is a token-budget artifact for ...

---

### 20. [RAC: Reference-Aware Activation Compression for Communication-Efficient Split LLM Inference](https://arxiv.org/abs/2608.04991v1)

**Authors**: Guotao Yang, Mingxi Zhao, Haopeng Li, Zhengchao Wang, Sheng Chen, Yitao Hu, Keqiu Li  
**Category**: cs.DC  
**Published**: 2026-08-06  
**Score**: 30.0  
**Type**: new  
**ArXiv ID**: 2608.04991v1  

#### Abstract
Large language model (LLM) agents repeatedly process long, privacy-sensitive contexts, while cloud-only deployment exposes user data beyond the trusted endpoint and fully local deployment often requires costly hardware. Split inference offers a middle ground by executing the model head, tail, and to...

---

### 21. [NSF-HRPT: Neural Semantic Field meets Hierarchical Risk Perception Tree for Safety-Critical Scenario Assessment](https://arxiv.org/abs/2608.04776v1)

**Authors**: Yu Zhao, Jiangyu Pan, Tao Hu, Ming Yin, Fan Yang, Jiangfan Liu, Xiubo Liang  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 27.5  
**Type**: new  
**ArXiv ID**: 2608.04776v1  

#### Abstract
The ability to accurately assess and anticipate risks in safety-critical scenarios is crucial for autonomous driving systems. While existing research has made progress in collision prediction, accurately quantifying risk levels from monocular vision inputs remains challenging due to the complex dyna...

---

### 22. [Strengthening Target-Language Features: SAE-Based Steering for Multilingual Inference](https://arxiv.org/abs/2608.04904v1)

**Authors**: Hongsheng Wang, Phlipp Koehn  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 25.5  
**Type**: new  
**ArXiv ID**: 2608.04904v1  

#### Abstract
Multilingual large language models exhibit substantial performance differences across languages, while existing adaptation methods often require parameter updates and considerable multilingual training data. We propose an inference-time multilingual steering method that uses pretrained sparse autoen...

---

### 23. [Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection](https://arxiv.org/abs/2608.04401v1)

**Authors**: Robin Pan, Raymond Liu, Daniel Fang, Adelina Andrei, Rosa Wu  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 24.5  
**Type**: new  
**ArXiv ID**: 2608.04401v1  

#### Abstract
Mixture-of-Experts (MoE) models enable model scaling while maintaining low inference-time compute by activating only a subset of experts per token. However, conventional routing relies on a fixed top-k selection, forcing the model to spend the same compute regardless of how many experts are relevant...

---

### 24. [WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964v1)

**Authors**: Bohai Gu, Yueyang Yuan, Taiyi Wu, Dazhao Du, Jian Liu, Xiaoyi Pang, Jie Zhang, Xiaocheng Lu, Haobin Zhong, Xiaotong Zhao, Alan Zhao, Song Guo  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.04964v1  

#### Abstract
Interactive video world models are essential for long-horizon planning and exploration, yet they suffer from compounding errors. Post-training methods such as reinforcement learning (RL) can improve these models, but they hit a verification bottleneck: for arbitrary action sequences, no ground-truth...

---

### 25. [EvtGraph: Event-Adaptive Compression for Sparse Temporal Graph Learning in Multimodal Time Series](https://arxiv.org/abs/2608.04368v1)

**Authors**: Ziqian Wang, Tingxiong Xiao, Yuxiao Cheng, Jinli Suo  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 24.0  
**Type**: new  
**ArXiv ID**: 2608.04368v1  

#### Abstract
Multimodal temporal data are inherently irregular and uneven in information density, yet most models rely on uniform discretization, leading to inefficient representations.
  We propose \textbf{EvtGraph}, a unified framework that aligns computation with temporal salience under explicit budget constr...

---

### 26. [Multimodal Spatiotemporal Atmospheric Data Assimilation with Latent Flow-matching](https://arxiv.org/abs/2608.05103v1)

**Authors**: Dibyajyoti Chakraborty, Romit Maulik  
**Category**: cs.LG  
**Published**: 2026-08-06  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2608.05103v1  

#### Abstract
Data assimilation (DA) uses Bayesian inference to update the state of a numerical forecast model with observed data. In this study, we propose a fundamentally different, unified approach to atmospheric data assimilation. We use latent video flow-matching to sample temporally consistent trajectories ...

---

### 27. [From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking](https://arxiv.org/abs/2608.05030v1)

**Authors**: Shaopeng Liang  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2608.05030v1  

#### Abstract
Football score forecasting combines a strong statistical core with a difficult contextual edge. Dynamic Poisson-family models estimate team strength, expected goals, and coherent score probabilities, but do not directly understand roles, tactical matchups, motivation, or how a first goal changes beh...

---

### 28. [Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite](https://arxiv.org/abs/2608.05095v1)

**Authors**: Xiawei Yue, Boran Wang, Xiaoqing Zhang, Shuxin Zheng, Ziwei Zhang  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.05095v1  

#### Abstract
Agents for long term reasoning require a memory that can be efficiently and effectively updated over time, as new facts and external feedback continue to arrive. Recently, graph memory has been adopted to offer structural organization for multi-hop retrieval and reasoning. However, existing methods ...

---

### 29. [ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment](https://arxiv.org/abs/2608.05102v1)

**Authors**: Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen  
**Category**: cs.AI  
**Published**: 2026-08-06  
**Score**: 22.5  
**Type**: new  
**ArXiv ID**: 2608.05102v1  

#### Abstract
Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agents typically treat all steps within a trajectory uniformly during both supervised fine-tuning (SFT) a...

---

### 30. [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](https://arxiv.org/abs/2608.04928v1)

**Authors**: Pedro Ferreira, Wilker Aziz, Ivan Titov  
**Category**: cs.CL  
**Published**: 2026-08-06  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2608.04928v1  

#### Abstract
Chain-of-thought (CoT) reasoning offers a window into the decision-making of large language models (LLMs), which can be monitored for target behaviors by reading the reasoning trace, motivating work on CoT monitorability. Latent CoT approaches, however, replace the explicit tokens with a small numbe...

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
