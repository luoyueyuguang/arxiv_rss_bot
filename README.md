# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-05-29 09:04:16 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG

## 📚 Recent Papers

### 1. [Design and Implementation of a Serverless MapReduce Framework for Scalable Data Pipelines](https://arxiv.org/abs/2605.29573)

**Authors**: Angelos Dorotheos Chatzopoulos, Babis Andreou, Kakia Panagidi, Stathes Hadjiefthymiades  
**Category**: cs.DC  
**Published**: 2026-05-29  
**Score**: 12.5  
**Type**: new  
**ArXiv ID**: 2605.29573v1  

#### Abstract
Modern logistics systems tend to generate continuous streams of data from sources such as GPS, IoT sensors, and logistics management systems. The aggregation, processing, and analysis of data have become vital for monitoring operations, optimizing efficiency, and responding quickly to decision makin...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文《Design and Implementation of a Serverless MapReduce Framework for Scalable Data Pipelines》核心总结

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
传统 **MapReduce** 框架（如 Hadoop、Spark）依赖静态分配的集群资源，存在以下问题：
- 资源利用率低，成本高（尤其在负载波动时）
- 配置复杂，运维负担重
- 缺乏弹性伸缩能力，难以应对实时数据流场景

同时，现有的 **Serverless** 平台（如 AWS Lambda）虽然支持按需执行和自动扩缩容（scale-to-zero），但其短暂生命周期、冷启动延迟、有限存储和执行时间等限制，使得直接运行大规模批处理任务（如 MapReduce）面临挑战。

该论文旨在解决：**如何在 Serverless 架构下高效实现可扩展的 MapReduce 数据处理流程**，特别是在物流等需要持续处理数据流的应用场景中。

---

### 🚀 提出的新方法与创新思路

作者设计并实现了一个基于 **Kubernetes + Knative** 的事件驱动型 Serverless MapReduce 框架，具有以下核心创新：

#### （1）**事件驱动的松耦合组件架构**
将 MapReduce 工作流拆分为五个独立服务：
- **Coordinator**：协调整个作业生命周期
- **Splitter**：划分输入数据块
- **Mapper**：并行处理数据，生成中间 key-value 对
- **Reducer**：聚合中间结果
- **Finalizer**：合并最终输出文件

各组件通过 **Apache Kafka** 异步通信，彼此解耦，支持独立扩缩容。

#### （2）**基于 Knative 的 Serverless 实现**
- 所有 Worker 组件（Mapper、Reducer 等）以 **Knative JobSink** 形式部署，支持从零实例动态创建（scale-from-zero）
- Coordinator 为 Knative Service，接收 HTTP 请求触发任务
- 利用 CloudEvents 触发组件间交互，实现事件驱动执行模型

#### （3）**轻量级状态管理机制**
- 使用 **Redis** 存储作业元数据（如分片边界、进度状态）
- 中间数据和最终结果持久化到 **AWS S3**
- 避免函数状态丢失问题，同时保持无状态函数的弹性优势

#### （4）**灵活可配置的工作流**
- 用户可通过 JSON 配置文件定义 Mapper/Reducer 数量、缓冲区大小、是否启用 Combiner/Finalizer 等参数
- 支持仅执行 Map 阶段或完整 MapReduce 流程
- 客户端 Python 包简化提交与监控流程

---

### 🔍 相比现有方法的优势

| 特性 | 传统框架（Hadoop/Spark） | 现有 Serverless MapReduce（如 Corral、PyWren） | 本文方案 |
|------|--------------------------|---------------------------------------------|---------|
| 弹性伸缩 | 固定集群，手动调整 | 自动扩缩，但常绑定特定云厂商（如 AWS Lambda） | 基于 Kubernetes + Knative，跨平台可移植 |
| 成本效率 | 高（持续占用资源） | 按使用计费，成本低 | 同样 pay-per-use，且支持 scale-to-zero |
| 架构灵活性 | 单体式或紧密耦合 | 多数仍依赖特定存储（S3）和计算服务 | 松耦合微服务架构，模块化强 |
| 可维护性 | 运维复杂 | 较好，但受制于 FaaS 限制 | 更易扩展与调试，适合现代云原生环境 |

> ✅ **核心优势**：结合了 MapReduce 的并行处理能力与 Serverless 的弹性、低成本特性，并通过容器化提升了可移植性和可控性。

---

## 2. 核心实验方法和设置

### 📊 使用的数据集
- **Wikipedia 英文文本数据集**（来自 HuggingFace）
- 经过预处理：转小写、去除标点和多余空格，提升单词局部性（locality）
- 输入规模范围：从 10KB 到 10GB，覆盖从小到大的多种负载情况

---

### ⚙️ 实验设置

#### 部署环境
- **Amazon EKS**（Elastic Kubernetes Service）
- 节点配置：5 个 `c4.2xlarge` 工作节点
- 使用 **Knative v1.11**, **Apache Kafka**, **Redis**, **AWS S3**

#### 组件资源配置
- **Mapper 和 Reducer**：作为 Knative JobSink，初始副本数为 0，按需启动
- **Coordinator**：固定一个 Pod（因需响应 HTTP 请求）
- **Splitter / Finalizer**：按需触发，短暂运行

#### 客户端工具
- 自研 Python 客户端包，用于构建镜像、部署服务、提交任务、监控进度（通过查询 Redis 元数据）

#### 评估指标
| 指标 | 描述 |
|------|------|
| **End-to-end Execution Time** | 从任务提交到最终结果生成的总耗时 |
| **Component-wise Latency** | 各阶段（Splitter、Mapper、Reducer 等）的时间开销 |
| **Phase Breakdown** | 每个组件内部的处理、上传、下载时间占比 |
| **Scalability** | 随输入数据增长，系统响应是否呈线性趋势 |
| **Cold Start Impact** | 小数据量下的额外延迟来源分析 |

#### 基线方法对比
未显式对比其他系统（如 Hadoop 或 Spark），而是聚焦于：
- 分析自身架构在不同数据规模下的表现
- 展示 Serverless 方案在真实云环境中运行 MapReduce 的可行性与效率
- 与文献中的 Serverless MapReduce 系统（如 Corral、PyWren）进行定性比较（见 Related Work）

---

## 3. 主要实验结果和性能指标

### 📈 关键性能数据（图6–图8）

#### （1）端到端执行时间（图6）
- 在 **4 Mappers + 2 Reducers** 设置下测试
- 输入从 10KB → 10GB，总执行时间呈现近似**线性增长趋势**
- 例外：极小数据量（<1MB）时非线性上升 → 主要由 **cold start 开销主导**

> 示例：
> - 1GB 输入：约 44 秒
> - 10GB 输入：约 440 秒（~7.3分钟）

#### （2）各组件平均耗时（图7）
- **Mapper 占据最大时间开销**（>60%），原因包括：
  - 数据读取与分块处理
  - 内部排序（sort-by-key）以支持 shuffle 阶段
  - 执行 Combiner 减少中间数据量
  - 分段上传至 S3（multipart upload）
- **Reducer** 时间次之，主要用于 k-way merge 和 reduce 函数执行
- **Coordinator、Splitter、Finalizer** 开销极小，几乎可忽略

#### （3）各阶段时间分解（图8）
- **Mapper 阶段**：
  - 处理时间（processing）为主导
  - 上传时间随 buffer threshold（设为75%）达到后触发
- **Reducer 阶段**：
  - 下载多个 spill 文件耗时显著
  - 合并与 reduce 计算相对高效
- 总体显示：**I/O 和网络传输是瓶颈之一**，尤其在大量中间数据交换时

---

### 🔬 消融实验（隐含分析）

尽管没有明确命名“ablation study”，文中通过以下方式进行了关键因素影响分析：

| 因素 | 发现 |
|------|------|
| **Combiner 启用与否** | 文中虽未量化对比，但指出其能有效减少中间数据体积，降低 S3 存储压力和 Reducer 下载负担 |
| **Buffer Size 设置（50MB）** | 影响内存利用与上传频率；过大可能导致 OOM，过小则增加请求次数 |
| **Cold Starts** | 明确指出在小数据量下严重影响性能，是 Serverless 架构固有问题 |
| **Scale-from-zero 能力** | 实验证明系统可在无负载时归零，在任务到来时快速拉起容器，实现真正按需计算 |

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **Serverless 架构可以有效支持 MapReduce 类型的大规模并行数据处理任务**
   - 尽管存在冷启动等问题，但在中大型数据集上仍表现出良好的可扩展性
   - 结合 Knative + Kubernetes 提供了比纯 FaaS 更灵活的控制能力

2. **松耦合、事件驱动的设计提升了系统的弹性和可维护性**
   - 各组件独立扩缩容，避免资源浪费
   - Kafka 解耦生产者与消费者，增强容错能力

3. **I/O 和中间数据管理是性能关键瓶颈**
   - S3 作为共享存储引入了网络延迟
   - Mapper 输出需频繁排序与上传，成为主要耗时环节

4. **冷启动对小任务影响显著，但大任务中占比下降**
   - 表明该框架更适合中长期运行的批处理任务，而非超短请求

---

### ⚠️ 方法的局限性

| 局限 | 说明 |
|------|------|
| **冷启动延迟** | Knative 容器冷启动带来数百毫秒至数秒延迟，影响小任务响应速度 |
| **FaaS 特性限制** | 执行时间受限于底层平台（虽未达上限，但仍存在潜在风险） |
| **网络密集型操作** | 大量数据经由 S3 传输，带宽可能成为瓶颈 |
| **缺乏细粒度调度优化** | 当前未实现智能任务调度（如亲和性放置、数据本地性优化） |
| **安全性考虑不足** | 多租户环境下函数隔离、依赖安全等问题未深入探讨 |

---

### 🔮 未来工作方向

1. **优化冷启动问题**
   - 探索预热策略（pre-warming）、镜像精简、更快的容器运行时（如 Firecracker）

2. **增强数据局部性（Data Locality）**
   - 尝试将 S3 缓存层引入节点本地（如使用 JuiceFS 或 Alluxio）
   - 减少跨节点数据传输开销

3. **支持更复杂的 DAG 工作流**
   - 当前仅支持简单 MapReduce 流程，未来可扩展为支持 Spark-like DAG 执行引擎

4. **多云与边缘部署适配**
   - 利用 Kubernetes 的可移植性，将框架部署至边缘节点，支持 IoT/Logistics 场景下的近源处理

5. **集成监控与自动调优**
   - 基于 Prometheus/Grafana 实现可视化监控
   - 根据负载自动推荐最优 Mapper/Reducer 数量、buffer 大小等参数

---

## 总结

✅ 本文成功构建了一个**基于 Kubernetes + Knative 的 Serverless MapReduce 框架**，实现了：
- 事件驱动、松耦合的组件化架构
- 动态扩缩容（scale-from-zero）与按需计费
- 在真实云平台（AWS EKS）上的有效运行

📊 实验表明：
- 系统具备良好可扩展性，端到端时间随数据量近似线性增长
- Mapper 是主要性能瓶颈，I/O 和排序开销较大
- 适用于中大规模批处理任务，尤其适合物流、IoT 等连续数据流场景

📌 尽管存在冷启动、网络 I/O 等挑战，但该研究证明了 **Serverless + MapReduce** 在现代云原生环境中的可行性与潜力，为下一代弹性数据处理平台提供了重要参考。

</details>

---

### 2. [Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding](https://arxiv.org/abs/2605.29707)

**Authors**: Jianuo Huang, Yaojie Zhang, Qituan Zhang, Hao Lin, Hanlin Xu, Linfeng Zhang  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 11.0  
**Type**: new  
**ArXiv ID**: 2605.29707v1  

#### Abstract
Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel with the target model. However, its practical speedup is constrained by the trade-off between draft quality and drafting cost: autoregressive drafters model causal dependencies among draft token...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
在 **Speculative Decoding** 中，存在一个核心权衡（trade-off）：
- **Autoregressive drafters**（如 EAGLE 系列）能建模 token 间的因果依赖，生成高质量 draft，获得较长的 **acceptance length**，但其自回归生成方式带来显著的 **sequential overhead**，限制了实际加速效果。
- **Parallel drafters**（如 DFlash）通过单次前向传播并行生成整个 draft block，大幅降低 drafting cost，但忽略了块内 token 的因果依赖，导致 draft 质量下降。

该问题的本质是：**如何在不牺牲 drafting 效率的前提下，保留因果依赖建模能力？**

### 提出了什么新方法或新思路
提出 **Domino**，一种轻量级因果校正框架，**将因果依赖建模与昂贵的自回归 drafting 解耦**（decouple causal modeling from autoregressive drafting）。

其核心设计包括：
- **Parallel Draft Backbone**：采用类似 DFlash 的并行骨干网络，在一次非自回归前向传播中生成整个 block 的初步分布（preliminary draft distributions）。
- **Lightweight Domino Head**：在骨干输出基础上，引入一个轻量级头部进行因果信息注入：
  - **Causal Encoder**：使用轻量 GRU 对已生成的 draft token 进行编码，捕捉前缀依赖。
  - **Low-Rank Correction Head**：通过低秩瓶颈结构对 base logits 进行残差校正（residual correction），避免重复调用完整 LM Head。

### 相比现有方法的优势
- **高效性**：主干保持并行计算，仅在轻量头部引入序列处理，总开销极小（仅增加约 5.3% 参数和 2.8% 延迟）。
- **高质量**：通过因果校正显著提升 acceptance length，优于纯并行方法。
- **兼容性**：无需改变目标模型，可灵活适配不同 backbone。

---

## 2. 核心实验方法和设置

### 使用了哪些数据集
- **训练数据**：`mlabonne/open-perfectblend`，一个包含 1.42M 样本的指令微调数据集，覆盖聊天、数学、代码和通用任务。所有响应由对应的目标模型重新生成，确保质量。
- **评估任务** 分为三类：
  - **Math Reasoning**：GSM8K、MATH、AIME25
  - **Code Generation**：HumanEval、MBPP、LiveCodeBench（LCB）
  - **Dialogue**：MT-Bench、Alpaca

### 实验设置和评估指标
- **目标模型**：Qwen3-4B 和 Qwen3-8B
- **Draft block size**：统一为 16
- **硬件平台**：NVIDIA A100-SXM4-80GB GPUs
- **评估指标**：
  - **Average Acceptance Length (T)**：每轮验证接受的 token 数期望值。
  - **End-to-End Speedup**：相对于标准自回归解码的端到端加速比。
  - **Throughput (TPS)**：在高并发场景下使用 SGLang 测量的吞吐量（tokens per second）。
- **解码策略**：测试了贪婪解码（greedy, T=0）和采样解码（sampling, T=1）两种模式。

### 基线方法对比
| 方法 | 类型 | 特点 |
|------|------|------|
| **Vanilla AR** | 基线 | 标准自回归解码 |
| **EAGLE-3** | Autoregressive Drafter | 自回归生成 draft，建模因果依赖 |
| **DFlash** | Parallel Drafter | 单步并行生成 block，效率高但忽略因果 |
| **DART** | Parallel Drafter | 扩散启发式并行 drafting |
| **FR-Spec** | Vocabulary-Efficient | 减少 full-vocabulary 投影成本 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据
#### 在 Transformers 后端下的端到端加速（低并发）
| 方法 | Qwen3-4B 平均加速 | Qwen3-8B 平均加速 | 平均 Acceptance Length |
|------|------------------|------------------|------------------------|
| DFlash | 4.70× | 4.66× | ~4.0 |
| **Domino (Ours)** | **5.47×** | **5.49×** | **~4.2–7.1** |

> ✅ **最高达 5.49× 端到端加速**（Qwen3-8B + greedy decoding）

#### 在 SGLang 下的高并发吞吐
| 方法 | Qwen3-8B 最大 TPS | 相对于 Baseline 加速 |
|------|------------------|---------------------|
| Baseline | 1713 | 1.0× |
| DFlash | 2801 | 1.6× |
| **Domino** | **3650** | **2.1×** |

> ✅ **最大吞吐加速达 5.8×**（见摘要）

#### 典型任务表现（GSM8K 上）
- Domino 达到 **7.92× speedup**，远超 DFlash 的 5.21× 和 EAGLE-3 的 2.57×。

### 与基线方法的对比结果
- **vs. EAGLE-3**：
  - 尽管 EAGLE-3 有更高的 acceptance length（如 4.86 vs 4.03），但由于其顺序 drafting 开销大，最终 speedup 更低（3.28× vs 3.42× @ DFlash；Domino 进一步提升至 5.49×）。
- **vs. DFlash**：
  - Domino 在几乎相同的 drafting 开销下，**acceptance length 提升 16.6%**，**speedup 提升 12.3%**。
  - 表明轻量因果校正确实有效提升了 draft 质量。

### 消融实验结果
#### （1）训练策略有效性（图4）
| 训练策略 | Average Acceptance Length |
|---------|----------------------------|
| TTT（Training-Time Testing） | 3.80 |
| Teacher Forcing (TF) | 3.96 (+4.2%) |
| TF + Base-Anchored Curriculum | **4.19 (+10.3%)** |

> ✔️ 教师强制（teacher forcing）更符合 speculative 验证机制；
> ✔️ Base-anchored curriculum 防止 backbone 崩溃，稳定训练。

#### （2）Domino Head 的作用（表4）
| 方法 | Avg. Accept Length | Avg. Speedup |
|------|--------------------|--------------|
| w/o Domino Head | 3.49 | 2.84× |
| w/ Domino Head | **4.19** | **3.31×** |

> ✅ Domino Head 贡献了 **+0.7 acceptance length** 和 **+0.47× speedup**，是性能提升的关键组件。

#### （3）相同训练数据下的公平比较（表3）
- 所有模型在 ShareGPT 上训练，固定 draft block size=16。
- 结果显示 Domino 在各项任务上均取得最佳 throughput 和 acceptance length 组合，证明其优势来自架构而非数据偏差。

---

## 4. 关键结论和发现

### 论文的主要发现
1. **因果建模与执行可以解耦**：无需通过完整的自回归流程即可实现有效的因果依赖建模。
2. **轻量因果校正即可显著提升性能**：仅需一个低秩结构的 Domino Head，就能在几乎不增加延迟的情况下大幅提升 acceptance length。
3. **并行 drafting + 因果 refinement 是更优路径**：相比“全自回归”或“完全并行”，Domino 提供了一种新的中间路线，在质量和效率之间取得更好平衡。
4. **Teacher forcing + Curriculum learning 是稳定训练的关键**：提出的训练策略有效解决了 teacher-forced encoding 中的 collapse 问题。

### 方法的局限性
- 当前实现主要适配于 **SGLang** 推理框架，与其他 serving 系统（如 vLLM、TensorRT-LLM）的兼容性尚待验证。
- 实际加速效果受硬件平台影响较大（如内存带宽、kernel 效率），可能需要针对特定设备优化。
- 未涉及训练成本优化，仍需额外训练 draft 模块。

### 未来工作方向
- 探索更高效的 causal encoder 架构（如稀疏 attention、state space models）。
- 将 Domino 思想扩展至其他 speculative decoding 变体（如 tree-based 或 multi-step verification）。
- 研究免训练（training-free）版本的因果校正机制。
- 支持动态 block size 和 adaptive drafting 策略。

--- 

> 🔚 **总结一句话**：  
> **Domino 通过“并行生成 + 轻量因果校正”的解耦设计，在几乎不增加开销的前提下显著提升了 speculative decoding 的 draft 质量，实现了高达 5.8× 的吞吐加速，为高效 LLM inference 提供了一条新路径。**

</details>

---

### 3. [NeuroEdge: Real-Time Hand Gesture Recognition with High-Density EMG Using Deep Learning at the Edge](https://arxiv.org/abs/2605.29326)

**Authors**: Peter Chudinov, Zhenyu Lin, Jay Motamarry, Srihita Panati, Xiaorong Zhang, Zhuwei Qin  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.29326v1  

#### Abstract
High-density electromyography (HD-EMG) has emerged as a powerful modality for decoding fine-grained neuromuscular activity, enabling real-time neural-machine interfaces (NMIs) for applications such as prosthetic control, rehabilitation, and augmented interaction. While deep learning approaches such ...

---

### 4. [A Full-Pipeline Framework for Evaluating Membership Inference Attacks in Machine Learning](https://arxiv.org/abs/2605.29454)

**Authors**: Ding Chen, Xinwen Cheng, Xuyang Zhong, Xinping Chen, Xiaolin Huang, Chen Liu  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 10.0  
**Type**: new  
**ArXiv ID**: 2605.29454v1  

#### Abstract
While Membership Inference Attacks (MIAs) are the prevailing method for identifying training data, their application has expanded into privacy auditing and machine unlearning. Nevertheless, the field lacks a systematic framework for evaluating how different contexts affect MIA efficacy. Without such...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：A Full-Pipeline Framework for Evaluating Membership Inference Attacks in Machine Learning

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前的 **Membership Inference Attack (MIA)** 研究存在两大核心问题：
- **碎片化的评估框架**：不同研究采用不一致的威胁模型（如是否拥有真实成员标签）、数据配置和评估指标，导致结果不可比。
- **脱离实际应用场景**：多数基准测试聚焦于静态模型和简化流程，无法反映真实机器学习生命周期中的复杂性（如微调、机器遗忘等）。

这使得在基准上表现良好的 MIA 方法，在真实部署中可能失效或产生误导性风险评估。

### 提出的新方法与新思路
作者提出一个 **全流水线评估框架 (Full-Pipeline Evaluation Framework)**，系统化地评估 MIA 在整个机器学习流程中的有效性。其核心创新包括：

#### （1）标准化的双威胁模型
- **Audit Mode（审计模式）**：假设攻击者拥有真实成员标签，用于优化超参数（如阈值），衡量理论上的最坏情况隐私泄露。
- **Attack Mode（攻击模式）**：更贴近现实，攻击者无真实标签，只能通过辅助数据集（Daux）训练影子模型来估计超参数。

该区分使不同 MIA 方法可在公平条件下进行比较，并量化其对超参数选择的敏感性。

#### （2）多维度、场景适配的评估指标
引入三种互补指标以适应不同应用需求：
- **Balanced Accuracy**：适用于误报与漏报代价对称的通用场景。
- **TPR @ low FPR**：高置信度泄露检测（如医疗隐私审计），强调极低误报率下的真阳性率。
- **TNR @ low FNR**：高召回筛查任务（如版权检测），强调几乎不遗漏成员样本时的非成员过滤能力。

#### （3）模块化流水线设计
将 ML 流程分解为四个可配置阶段：
1. **Data Preparation**（数据准备）
2. **Architecture Configuration**（架构配置）
3. **Training Algorithm**（训练算法）
4. **Post-Training Modifications**（后训练操作，如微调、机器遗忘）

支持对每个模块独立控制变量，分析其对 MIA 风险的影响。

### 相比现有方法的优势
| 维度 | 传统基准 | 本文框架 |
|------|--------|---------|
| 威胁模型 | 混杂不清（部分有标签，部分无） | 明确定义 Audit / Attack 模式 |
| 评估范围 | 局限于训练完成后的静态模型 | 覆盖完整 ML 生命周期 |
| 指标设计 | 单一（如 AUC） | 多元、面向实际成本不对称场景 |
| 可复现性与公平性 | 差 | 提供统一协议与工具包 |

---

## 2. 核心实验方法和设置

### 数据集
- **CIFAR-10**, **CIFAR-100**（标准图像分类）
- **ImageNet-100**（大规模子集）
- 包含细粒度类别与“超级类”（superclass）变体以研究标签抽象影响
- 引入带噪声标签的数据（mislabeled data）模拟数据质量问题

### 实验设置
- **目标模型**：ResNet-18/34/50, VGG-11, 4-layer CNN, Swin-Tiny 等多种架构
- **训练方式**：
  - 标准 SGD
  - **DP-SGD**（差分隐私训练）
  - 微调（Fine-tuning）
  - 机器遗忘（Machine Unlearning, MU）场景（SalUn 和 SFR-on 方法）
- **MIA 方法覆盖广泛**：
  - ShadowMIA, MLLeaks, Merlin, Metric MIA, LiRA, RMIA, Quantile MIA, Blind-MI 等

### 评估指标
- 主要报告三项指标：
  - **Balanced Accuracy**
  - **TPR @ 0.1% FPR**
  - **TNR @ 0.1% FNR**
- 所有方法均在 **Auditing Mode** 下运行以最大化性能可比性（除非特别说明）

---

## 3. 主要实验结果和性能指标

### 关键性能数据汇总（来自 Tables 3–6）

| 场景 | 最佳 MIA 方法 | 性能表现（Accuracy / TPR@FPR / TNR@FNR） |
|------|---------------|------------------------------------------|
| **标准训练（CIFAR-100）** | Metric MIA (Modified Entropy) | 81.97 / 8.92 / 60.74 |
| **不同架构（Swin-T）** | Metric MIA | 67.93 / 2.36 / 30.74 |
| **DP-SGD 训练** | Metric MIA | 70.34 / 3.06 / 28.00 |
| **微调模型（Fine-tuned）** | Quantile MIA | 72.56 / 1.81 / 0.00 |
| **机器遗忘（Fixed-Data Audit）** | BlindMI One-class | 95.2 / 99.8 / 66.9（平均） |

### 与基线方法的对比结果

#### （1）Metric MIA 表现最强但不稳定
- 在大多数标准训练场景下（如 CIFAR-100, ResNet-18），**Metric MIA**（尤其是基于 Modified Entropy 或 Confidence 的版本）达到最高准确率。
- 但在 **Attack Mode** 下性能显著下降（见 Table 2），表明其严重依赖精确阈值设定，鲁棒性较差。

#### （2）Quantile MIA 最稳定可靠
- 尽管绝对性能略低于 Metric MIA，但 **Quantile MIA** 在以下挑战场景中表现最佳：
  - 攻击模式（Attack Mode）
  - DP-SGD 模型
  - 微调模型
- 其自适应阈值机制使其对分布偏移具有强鲁棒性。

#### （3）RMIA 在极端低 FPR 下领先
- RMIA 利用成对似然比测试，擅长识别极少数高度记忆化的样本。
- 在 **TPR @ 0.1% FPR** 上表现优异，适合高置信度隐私审计。
- 但在 **TNR @ low FNR** 上表现不佳，不适合高召回筛查任务。

#### （4）Blind-MI 在跨模型比较中胜出
- 在机器遗忘的 **Fixed-Data Audit** 中（即判断同一数据集在不同模型中的成员状态），**BlindMI One-class** 表现最优。
- 因其基于几何距离而非逐样本打分，更适合批量分析。

### 消融实验结果

#### （1）威胁模型影响巨大（Table 2）
- 多数 MIA 方法在 Audit vs. Attack 模式间存在显著性能差距（Audit-Attack Gap）。
- **Quantile MIA** 缺口最小，证明其稳定性最强。
- 例如，在 DP-SGD 设置下，LiRA 的攻击模式性能从 64.74% 降至 63.57%，而 Metric MIA 从 68.11% 降至 64.58%，波动更大。

#### （2）过拟合程度决定 MIA 成功率（Figure 7）
- MIA 准确率与模型的 **generalization gap**（训练-测试准确率差）呈强正相关。
- 过拟合越严重 → 成员与非成员输出差异越大 → 更易被推断。
- 例如，在 50% 标签错误的数据上，generalization gap 达 79.72%，MIA 准确率达 87.43%（Table 3）。

#### （3）微调降低 MIA 风险
- 微调模型的学习率小、梯度变化弱，导致成员信号更难捕捉。
- 如 Table 5 所示，多数 MIA 在微调模型上性能接近随机猜测，仅 **Quantile MIA** 仍保持有效（72.56%）。

---

## 4. 关键结论和发现

### 主要发现
1. ✅ **MIA 效果高度依赖上下文**：没有“万能”的最佳 MIA 方法。其性能受威胁模型、数据质量、模型架构、训练算法和后处理步骤共同影响。
2. ✅ **过拟合是 MIA 成功的关键驱动因素**：generalization gap 是预测 MIA 风险的有效代理指标。
3. ✅ **Quantile MIA 是最稳健的选择**：尤其适用于攻击者资源有限的真实世界场景（Attack Mode）。
4. ✅ **Metric MIA 强大但脆弱**：在理想条件下表现最好，但对超参数敏感，迁移能力差。
5. ✅ **RMIA 擅长高置信度检测**：适合需要极高确定性的隐私审计任务。
6. ✅ **BlindMI 适用于跨模型分析**：在机器遗忘等需比较多个模型的场景中最具优势。

### 方法的局限性
- 当前框架主要针对 **分类任务**，未涵盖生成模型（如 LLM）或强化学习。
- 对 **LLM 的 MIA** 通常基于序列级指标（如困惑度），难以与实例级概率方法统一比较。
- 实验集中在图像领域，文本或其他模态的泛化性有待验证。
- 构建影子模型的成本较高，尤其对于大模型。

### 未来工作方向
- 扩展框架至 **Large Language Models (LLMs)** 和 **多模态模型**。
- 探索 **无需影子模型的轻量级 MIA** 方法，提升实用性。
- 结合因果推理等技术，深入理解 MIA 成功的根本机制。
- 开发自动化工具链，支持动态风险监控与防御策略推荐。

---

> 📌 **总结一句话**：  
> 本论文提出了首个覆盖机器学习全生命周期的 MIA 评估框架，揭示了现有方法的性能高度依赖具体上下文，并指出 **Quantile MIA** 是最稳健的选择，同时强调 **过拟合** 是 MIA 成功的核心根源。

</details>

---

### 5. [HTAM: Hierarchical Transition-Attended Memory for Operator Optimization](https://arxiv.org/abs/2605.29734)

**Authors**: Yining Zhang, Mingyang Yi, Chen Wang, Xuwen Xiang, Tianhe Jia, Zedong Dan, Chengqing Zong, Yue Wang  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.29734v1  

#### Abstract
High-performance GPU kernels are essential for efficient LLM deployment, yet optimizing them remains expertise-intensive. Recent LLM-based code generation makes automatic GPU operator generation promising, but operator optimization remains a hardware-aware search problem. Existing LLM-based methods ...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：HTAM: Hierarchical Transition-Attended Memory for Operator Optimization

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前基于 **LLM** 的 GPU 算子优化面临“粒度不匹配”（granularity mismatch）问题：
- **粗粒度提示**（如瓶颈诊断、文本建议）易于检索但过于抽象，难以直接生成可执行的 CUDA 代码；
- **细粒度轨迹**（如完整实现路径）虽具操作性，但导致搜索空间过大、噪声多，且难以泛化。

此外，算子优化是一个**硬件感知的多阶段决策过程**，需要在全局方向选择与具体代码修改之间建立有效衔接。

### 提出了什么新方法或新思路
本文提出 **HTAM**（Hierarchical Transition-Attended Memory），一种用于 LLM-based operator optimization 的**分层记忆框架**，其核心思想是“**由粗到细**”（coarse-to-fine）的优化流程：

- 构建一个 **Hierarchical Transition Graph (HTG)** 来组织历史优化经验：
  - **Global Nodes**：存储高层优化方向（如 Memory Access, Data Reuse, Boundary Handling）；
  - **Local Nodes**：存储具体的策略实现（如 aligned vectorized loads, read-only cache promotion）；
  - **Transition Edges**：记录从一个全局方向转移到另一个方向的经验（何时、为何、风险等）。

- 在每一步进化中：
  1. 基于当前状态和历史前缀，通过 HTG 选择下一个**全局优化方向**；
  2. 检索该方向下的**局部策略记忆**；
  3. 利用这些策略指导 LLM 生成具体的 CUDA 代码。

### 相比现有方法的优势
| 方法 | 缺陷 | HTAM 如何改进 |
|------|------|----------------|
| CudaForge | 使用粗粒度文本提示，太抽象无法执行 | 引入局部策略节点提供可执行代码模板 |
| Robust-KBench | 依赖细粒度实现轨迹，搜索空间大且嘈杂 | 分层结构缩小搜索范围，提升效率 |
| Flat Memory Retrieval | 扁平化记忆，缺乏结构引导 | 显式建模“方向→策略”关系和“方向间转移” |

HTAM 的优势在于：
- **结构化记忆组织**：将优化经验分解为可重用、可组合的模块；
- **过渡感知决策**（Transition-aware）：利用边上的转移经验指导下一步方向，而非孤立决策；
- **降低预探索成本**：通过成对边记忆替代全路径记忆，存储复杂度从 $O(|V|^T)$ 降至 $O(|V|^2)$。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **KernelBench**（主实验）：包含 250 个任务的完整套件
  - Level-1（L1）：100 个单算子任务
  - Level-2（L2）：100 个融合算子任务
  - Level-3（L3）：50 个模型级任务
- **Robust-KBench**（迁移实验）：5 个代表性任务（LayerNorm, RMSNorm, Cross Entropy, Linear, Linear+ReLU），用于跨基准测试泛化能力。

### 实验设置和评估指标
- **硬件环境**：NVIDIA A100-SXM4-80GB, CUDA 12.8, PyTorch 2.9.1+cu128
- **LLM 后端**：主要使用 **DeepSeek-R1**；部分实验测试 DeepSeek-V3/V4-Flash, GPT-4o
- **最大进化步数**：T = 6
- **评估协议**：遵循官方 KernelBench 协议

#### 主要评估指标：
| 指标 | 定义 |
|------|------|
| **Correct** | 正确编译并通过正确性验证的比例 |
| **Fast@1** | 最佳候选既正确又快于 PyTorch eager 参考实现的任务比例 |
| **GeoM Spd.** | 几何平均加速比（相对于 PyTorch eager） |
| **L1/L2/L3 Spd.** | 各层级任务的几何平均加速比 |

### 基线方法对比
分为三类：

#### （1）Vanilla LLM Generation
- 单次生成，无反馈或记忆
- 包括：DeepSeek-R1, DeepSeek-V3, DeepSeek-V4-Flash, Gemini-2.5-Flash-Thinking, OpenAI-o3

#### （2）Vanilla Evolution-based Methods（复现）
- **Best-of-N Sampling**：采样多个并选最优
- **Feedback-only Refinement**：仅用反馈迭代修正
- **Flat Memory Retrieval**：扁平记忆检索（无层次结构）

#### （3）Refined Evolution-based Methods（引用外部结果）
- **KernelBlaster3**（Dong et al., 2026）
- **CudaForgeT**（Zhang et al., 2025）

---

## 3. 主要实验结果和性能指标

### 关键性能数据（来自 Table 1）
| 方法 | Correct | Fast@1 | GeoM Spd. |
|------|--------|--------|-----------|
| **HTAM (Ours)** | **98.4%** | **84.0%** | **1.978×** |
| Flat Memory Retrieval | 89.6% | 58.8% | 1.464× |
| CudaForgeT | 97.6% | 70.8% | 1.677× |
| KernelBlaster3 | 80.2% | 62.8% | 1.756× |

> ✅ HTAM 在所有控制变量下均取得最佳表现。

### 与基线方法的对比结果
- 相比最强复现基线 **Flat Memory Retrieval**：
  - Correct ↑ **+8.8 pp**
  - Fast@1 ↑ **+25.2 pp**
  - GeoM Spd. ↑ **+0.514×**（相对提升约 35%）
- 相比先进系统 **CudaForgeT**：
  - Fast@1 ↑ **+13.2 pp**
  - GeoM Spd. ↑ **+0.301×**

### 分层级性能（L1/L2/L3）
| 方法 | L1 | L2 | L3 |
|------|----|----|----|
| **HTAM** | 1.532× | **2.598×** | 1.909× |

> 🔍 L2 融合算子增益最大，说明 HTAM 特别适合挖掘内存访问、数据复用等复合优化机会。

### 消融实验结果（Table 4）
| 变体 | Correct | GeoM Spd. | ΔGeoM |
|------|--------|-----------|-------|
| **Full HTAM** | 98.4% | 1.978× | 0 |
| w/o hierarchy structure | 89.6% | 1.464× | -0.514× |
| w/o local memory | 71.6% | 0.974× | -1.004× |
| w/o prefix-aware transition | 94.4% | 1.683× | -0.295× |
| w/o updated memory | 96.4% | 1.842× | -0.136× |
| 1-step evolution | 91.2% | 1.428× | -0.550× |

> 🔽 结果表明：
> - **分层结构** 和 **局部记忆** 是最关键的组件；
> - **前缀感知转移机制** 显著影响性能；
> - 多步进化与动态记忆更新不可或缺。

---

## 4. 关键结论和发现

### 主要发现
1. **结构化记忆优于非结构化记忆**  
   单纯增加记忆内容（如 flat retrieval）不如合理组织记忆结构。HTAM 的分层设计显著提升了优化可靠性与效率。

2. **“由粗到细”的决策流程更符合专家直觉**  
   先确定优化方向（what to optimize），再细化实施策略（how to implement），能有效缩小搜索空间并避免错误累积。

3. **转移经验具有可重用性**  
   方向间的转移模式（如 `Memory Access → Instruction Throughput`）可以被建模为图边，并用于指导后续决策，无需存储完整路径。

4. **HTAM 具备良好泛化能力**
   - **跨 LLM 后端**：在 DeepSeek-V4F、DeepSeek-R1、GPT-4o 上均保持高性能（Table 2）；
   - **跨基准迁移**：将在 KernelBench 学到的记忆迁移到 Robust-KBench，平均加速比从 1.20× 提升至 1.58×（Table 3），尤其在归一化类算子上效果显著。

### 方法的局限性
1. **计算与 API 成本限制实验规模**
   - 未穷尽所有 LLM、解码预算、硬件平台；
   - 当前评估集中在 KernelBench 和少量 Robust-KBench 任务。

2. **依赖可执行验证而非形式化证明**
   - 验证基于给定输入的运行时行为，不能保证对所有 shape 或分布都正确；
   - 存在边界 case 漏检风险。

3. **初始 memory schema 需人工设计**
   - 当前 HTG 的 global/local 节点和 transition 边界由人工定义；
   - 对全新硬件架构或算子家族可能需重新适配 schema。

### 未来工作方向
- 扩展至更多硬件平台（如 TPU、NPU）、更广泛的算子族；
- 探索自动构建和演化 HTG 结构的方法（如 clustering-based node discovery）；
- 引入更严格的验证机制（如 property-based testing, symbolic execution）；
- 进一步降低 LLM API 开销，例如通过 distillation 或 agent pruning。

---

> 💡 **总结一句话**：  
> HTAM 通过构建一个**分层的、带转移记忆的图结构（HTG）**，实现了 LLM-based operator optimization 中“**高阶规划 + 低阶执行**”的有效协同，在正确率、成功率和加速比上全面超越现有方法，并展现出良好的可迁移性和实用性。

</details>

---

### 6. [CCS: Clinical Consensus Selection for Radiology Report Generation](https://arxiv.org/abs/2605.30131)

**Authors**: Xi Zhang, Yingshu Li, Zaiqiao Meng, Jake Lever, Edmond S. L. Ho  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 9.5  
**Type**: new  
**ArXiv ID**: 2605.30131v1  

#### Abstract
Radiology report generation (RRG) is commonly formulated as a single-path generation task, where a multimodal large language model (MLLM) produces one decoded report as the final output. While recent progress has largely been driven by scaling training data, model capacity, and retrieval mechanisms,...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# CCS: Clinical Consensus Selection for Radiology Report Generation 论文总结

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
当前的 **Radiology Report Generation (RRG)** 系统大多采用单路径生成（single-path generation）策略，即通过多模态大语言模型（MLLM）逐token生成一份报告作为最终输出。这种模式存在以下瓶颈：
- **推理阶段决策脆弱**：一旦某个解码步骤出错（如遗漏关键发现或生成不支持的观察），无法恢复。
- **忽视候选池中的优质报告**：固定模型在采样时可能生成多个候选报告，其中部分在临床准确性上优于默认输出，但未被选中。
- **现有选择标准不适合医学场景**：传统的 Best-of-N 方法依赖 **perplexity**、**textual similarity** 或 **likelihood**，这些指标偏向流畅性或文本一致性，而非临床正确性。

### 提出了什么新方法或新思路
作者提出 **Clinical Consensus Selection (CCS)** ——一种**解码器无关**（decoder-agnostic）、**无参考**（reference-free）的推理时选择框架，其核心思想是：
> 不直接返回第一个生成的报告，而是从一个 rollout pool 中选择具有最高“临床共识”的报告。

#### CCS 框架流程如下：
1. **Rollout Pool Generation**：对同一输入图像和提示，使用随机解码（如 temperature sampling）生成 $N$ 个候选报告 $\{y_1, ..., y_N\}$。
2. **Pairwise Utility Scoring**：计算每对候选之间的相似度得分 $U(y_i, y_j)$，构建得分矩阵。
3. **Consensus Aggregation**：为每个候选 $y_i$ 计算其与其他 $N-1$ 个候选的平均相似度（consensus score）：
   $$
   s_i = \frac{1}{N-1} \sum_{j \neq i} U(y_i, y_j)
   $$
4. **Final Selection**：选择共识分数最高的报告作为最终输出：
   $$
   y_{ccs} = \arg\max_i s_i
   $$

#### 创新的共识效用函数（Utility Function）
- **Textual Utility**：基于传统文本指标（如 ROUGE-L, BERTScore）计算报告间相似性。
- **Image-Grounded Utility**：使用在医学图文对上微调过的多模态嵌入模型 **Qwen3-VL-Embed**，将报告编码到一个与影像对齐的表示空间中，并用余弦相似度衡量一致性。这使得比较超越表面文本，捕捉是否“基于相同影像证据”。

### 相比现有方法的优势
| 方面 | CCS 的优势 |
|------|-----------|
| **无需训练/修改模型** | 完全在推理阶段操作，适用于任何预训练 MLLM，部署成本低。 |
| **更关注临床正确性** | 引入 image-grounded utility，能识别在症状层面一致且有影像依据的报告。 |
| **Decoder-Agnostic** | 可兼容不同解码策略（sampling / beam search）。 |
| **显著提升临床指标** | 在 RadGraph-F1、RaTEScore 等医学专用指标上表现最优。 |

---

## 2. 核心实验方法和设置

### 使用的数据集
在三个公开胸部X光数据集上进行评估：
- **MIMIC-CXR**：主训练和测试集，包含约16万训练样本。
- **IU-Xray** 和 **CheXpert Plus**：用于跨数据集泛化能力测试，所有模型仅在 MIMIC-CXR 上训练。

### 实验设置
- **Backbone Models**：在多种预训练 RRG MLLMs 上验证通用性，包括：
  - LLaVA-Med
  - LLaVA-Rad
  - Libra
  - 自研 Baseline MLLM（基于 LLaVA 架构）
- **Rollout Pool Size**：默认 $N=8$，温度 $T=0.5$。
- **Image-Grounded Utility 模型**：使用 **Qwen3-VL-Embed-2B**，并在 MIMIC-CXR 图文对上进行微调以适应 RRG 任务。

### 评估指标
分为两类：

#### 文本级指标（Lexical Metrics）
| 指标 | 描述 |
|------|------|
| **ROUGE-L** | 最长公共子序列相似度 |
| **BLEU-4** | 4-gram 精确率带短句惩罚 |
| **BERTScore** | 基于 BERT 的上下文语义相似度 |

#### 医学专用指标（Radiology-specific Metrics）
| 指标 | 描述 |
|------|------|
| **RadGraph-F1** | 基于实体与关系图的 F1 分数 |
| **RaTEScore** | 评估关键诊断概念和解剖细节的正确性 |
| **RadEval-BERT** | 使用医学适配的 ModernBERT 衡量语义一致性 |
| **CheXbert-F1** | 自动标注器提取 14 类疾病状态（present/absent/uncertain）的 F1 分数（分 5-class 和 14-class） |

### 基线方法对比
| 基线方法 | 描述 |
|--------|------|
| **Single Path (Sampling/Greedy)** | 默认单路径生成，作为基础对照。 |
| **Random** | 从 rollout pool 中随机选择一个报告。 |
| **Perplexity** | 选择平均困惑度最低的报告（偏好高置信度输出）。 |
| **Self-Certainty** | 选择负对数似然最小的报告。 |
| **ModeX** | 构建文本相似图并选择聚类中心。 |

---

## 3. 主要实验结果和性能指标

### 关键性能数据（以 MIMIC-CXR 测试集为例）

| Method | ROUGE-L | BLEU-4 | BERTScore | RadGraph-F1 | RaTEScore | RadEval-BERT | CheXbert-F1 (5-class) |
|--------|---------|--------|-----------|-------------|-----------|----------------|-----------------------|
| Sampling | 0.2252 | 0.0534 | 0.5128 | 0.1989 | 0.5165 | 0.2493 | 0.4519 |
| Perplexity | 0.2368 | 0.0694 | 0.5368 | 0.2125 | 0.5295 | 0.2556 | 0.4605 |
| ModeX | 0.2388 | 0.0595 | 0.5268 | 0.2124 | 0.5291 | 0.2577 | 0.4496 |
| **CCS (+Qwen3-VL-Embed)** | **0.2331** | **0.0548** | **0.5268** | **0.2134** | **0.5323** | **0.2585** | **0.4714** |

> ✅ 所有改进均在 $p < 0.05$ 水平下统计显著。

### 与基线方法的对比结果
- **相比 Sampling**：CCS 在所有医学指标上均有显著提升，尤其在 **CheXbert-F1** 上提升达 **+0.0195**。
- **优于通用 Best-of-N 方法**：
  - Perplexity 虽提升文本指标，但医学增益有限；
  - ModeX 在部分指标上接近 CCS，但在 CheXbert 上反而略低于 Sampling；
  - **CCS 是唯一在所有医学指标上一致领先的方案**。
- **跨模型 & 跨数据集一致性**：在 LLaVA-Med、LLaVA-Rad、Libra 等不同 backbone 上，CCS 均带来稳定临床性能提升（见 Table 2）。

### 消融实验结果
#### 不同 Utility 函数的比较（Table 3）
| Utility 类型 | 特点 | 结果 |
|------------|------|------|
| **Textual Utilities**（如 +BERTScore） | 在自身来源指标上表现最好（self-alignment），但对其他医学指标提升有限。 |
| **Image-Grounded Utility**（+Qwen3-VL-Embed） | 综合表现最佳，尤其在 RaTEScore 和 CheXbert 上领先明显。 |
| **w/o Fine-tuning** | 若不使用医学数据微调 Qwen3-VL-Embed，则性能下降，说明领域适配至关重要。 |

#### Rollout Pool Size 影响（Figure 3）
- 随着 $N$ 增加（2→16），CCS 性能持续上升，表明更大的候选池提供更多高质量选项。
- 收益边际递减，故选择 $N=8$ 作为性价比平衡点。

#### Pool-Bounded Oracle 分析
- “理想选择者”（Oracle）能在 rollout pool 中选出远超 single-path 输出的报告。
- 当前 CCS 已显著缩小与 Oracle 的差距，但仍留有提升空间。

---

## 4. 关键结论和发现

### 主要发现
1. **RRG 模型具备潜力但选择机制落后**：固定 MLLM 的 rollout pool 中常含有比默认输出更可靠的报告，说明**推理时的选择策略是当前瓶颈**。
2. **临床共识可有效指导选择**：通过聚合多候选间的“共识”，尤其是基于影像对齐的表示空间中的共识，能选出更符合真实影像的报告。
3. **Image-Grounded Utility 是关键创新**：它提供了一种不同于纯文本相似性的选择轴，在症状级判断上更具判别力。
4. **CCS 具有强通用性和实用性**：无需重新训练，即可即插即用地提升多个主流 RRG 模型的临床质量。

### 方法的局限性
1. **依赖高质量 rollout pool**：若生成过程本身受限（如 beam search 多样性不足），则 CCS 提升有限。
2. **未引入外部知识或人工反馈**：完全依赖模型内部生成与嵌入模型打分，缺乏专家干预或检索增强。
3. **评估仍依赖自动指标**：缺少放射科医生的人工盲评，难以全面反映临床可用性。
4. **计算开销增加**：需生成 $N$ 份报告并计算 $O(N^2)$ 对相似度，实时性要求高的场景需权衡。

### 未来工作方向
- 探索更高效的 consensus aggregation 策略（如基于聚类或排序学习）。
- 将 CCS 与其他技术结合，如 **Retrieval-Augmented Generation (RAG)** 或 **Test-Time Training**。
- 引入 LLM-as-a-judge 或专家评审进行更高可信度评估。
- 扩展至其他医学成像模态（如 CT、MRI）和其他生成任务（如诊断解释、治疗建议）。

---

> 🔍 **一句话总结**：  
> 该论文揭示了 RRG 中“生成能力”与“选择能力”的脱节，提出 **CCS** 框架通过在 rollout pool 中选择最具“临床共识”的报告，在不修改模型的前提下，显著提升了生成报告的临床可靠性，尤其得益于 **image-grounded multimodal embedding** 提供的深层一致性信号。

</details>

---

### 7. [GTA: Generating Long-Horizon Tasks for Web Agents at Scale](https://arxiv.org/abs/2605.29218)

**Authors**: Tenghao Huang, Kung-Hsiang Huang, Prafulla Kumar Choubey, Yilun Zhou, Muhao Chen, Jonathan May, Chien-Sheng Wu  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.29218v1  

#### Abstract
Web agents, which couple language models with browsing and tool-use capabilities, show promise as open web assistants. Yet progress is increasingly limited by the lack of scalable, process-level supervision. Existing benchmarks are largely manually constructed, providing only coarse start-goal annot...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# GTA: Generating Long-Horizon Tasks for Web Agents at Scale — 核心总结

---

## 1. 论文的主要贡献和创新点

### 解决的问题
当前 **Web Agent** 领域面临严重瓶颈：  
- **缺乏可扩展的过程级监督数据**（process-level supervision），现有基准大多依赖人工标注，仅提供起点-终点任务描述，缺少中间执行路径（trajectory）。  
- 自动化生成方法存在三大缺陷：  
  1. **成本高**：依赖 LLM 策略模型反复探索网站（rollout），计算开销大；  
  2. **探索偏差强**：LLM 容易集中在“显眼”页面（如商品详情页），忽略奖励计划、促销等深层功能；  
  3. **任务浅层化**：多数任务退化为单跳检索或表单填写，无法测试多跳推理能力。

这导致 Web Agent 在真实复杂的跨页、多步任务中泛化能力差。

---

### 提出的新方法与思路
作者提出 **GTA**（Generate Long-Horizon Tasks for Web Agents at Scale），一个**可扩展的任务生成与评测框架**，其核心设计包括：

#### （1）四阶段自动化流水线
1. **Crawl**：对公开网站进行广度优先爬取，构建站点图（site graph）；
2. **Retrieve**：基于语义检索选取候选网页作为任务种子；
3. **Generate**：通过 in-context prompting 生成需跨页推理的多跳任务；
4. **Validate**：引入 LLM-based 质量控制协议，确保任务清晰、可解、无歧义，并记录最小可执行路径（gold path）用于确定性回放。

#### （2）关键创新机制
- **解耦爬取与生成**：一次性完成网站图构建后，任务生成无需重复 agent rollouts，显著降低时间与成本；
- **图结构引导生成**：以 site graph 为基础，强制任务涉及多个互连节点，保障组合性（compositionality）；
- **动态可演化的基准生态**：用户可从实时网页持续生成新任务，避免过拟合静态数据集。

---

### 相比现有方法的优势
| 维度 | GTA | Prior Methods (e.g., AgentTrek, NNetNav) |
|------|-----|----------------------------------------|
| **Multi-hop Reasoning** | ✅ 显式构造跨页依赖 | ❌ 多为单跳或拼接查询 |
| **Scalability** | ✅ 图索引摊销成本，边际成本极低 (~$0.10/task) | ❌ 每任务需多次 LLM 探索 (~$0.55/task) |
| **Exploration Coverage** | ✅ 基于检索采样，覆盖更广功能模块 | ❌ 受 LLM 导航偏好影响，探索偏斜 |
| **Executable Trajectories** | ✅ 提供最小点击/滚动/输入路径，支持 step-level diagnostics | ⚠️ 多数无精确轨迹或不可复现 |
| **Dynamic & Evolving** | ✅ 支持基于最新网页内容生成任务 | ❌ 固定快照，易被过拟合 |

> ✅ GTA 是目前唯一同时具备自动任务生成、多跳推理、可执行真值路径、动态扩展和多语言覆盖的基准。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **自建数据集**：在 **50+ 公共网站** 上构建，涵盖五大领域：
  - 医疗健康（CDC, Mayo Clinic, drugs.com）
  - 金融经济（Yahoo Finance, Bloomberg, SeekingAlpha）
  - 电商消费（Under Armour, Casper）
  - 新闻娱乐（ESPN, Facebook, MusicBrainz）
  - 政府资源（NIH, NOAA, DMV）

- **任务规模**：
  - **5,000 个站内任务**（intra-website）
  - **600 个跨站任务**（inter-website，如结合 Mayo Clinic 和 CVS Health 查询药物安全性）

- **多语言支持**：包含英文、意大利语、德语、日语、中文等非英语环境。

---

### 实验设置与评估指标

#### 基线 Agent 对比
| Agent | 描述 |
|-------|------|
| **BrowserUse** | 开源框架，将 LLM 与真实浏览器集成，支持感知-决策-行动循环。 |
| **AgentOccam** | 强调简洁性的 SOTA 方法，通过剪枝动作空间和压缩页面观测提升鲁棒性。 |

#### 评估方式
- **Success Rate**：代理是否成功完成任务并输出正确答案。
- **Human Performance**：人类在相同任务上的表现作为上限参考（达 85%）。
- **Page Coverage Rate**：衡量任务覆盖网站一级功能节点的比例，类比代码覆盖率。
- **Search Baseline**：使用 Google Search API 获取摘要后由 LLM 回答，检验任务是否可被简单搜索解决。

#### 质量验证流程
1. **Multi-hop Validation**：排除“两个独立问题用 and 连接”的伪多跳任务；
2. **Answer Correctness**：LLM verifier 在仅见证据页面下能否复现答案；
3. **Ambiguity Detection**：过滤时间/地点模糊的任务；
4. **Solvability Check**：确保存在一条可行路径能获取全部必要信息。

---

## 3. 主要实验结果和性能指标

### 关键性能数据

| 指标 | 结果 |
|------|------|
| **GTA 任务成功率（Agent）** | BrowserUse: ~14–30%，AgentOccam: ~8–20% |
| **人类任务成功率** | **85%**（显示显著 human-agent performance gap） |
| **Search Engine Baseline 正确率** | **仅 14%**（说明任务不能靠搜索引擎轻易解决） |
| **Page Coverage Rate** | GTA: **77.4%–80.7%**，远高于 AgentTrek (20.2%)、NNetNav (24.3%)、WebDS (11.0%) |
| **多语言任务成功率** | 非英语环境下急剧下降：<br>- 德语：0%（BrowserUse）<br>- 日语：2.9%<br>- 意大利语：0% |

---

### 与基线方法的对比结果

#### ✅ 难度更高
- 在 WebVoyager 和 Mind2Web 上，agents 成功率可达 82% 和 45%，但在 GTA 上普遍低于 30%，表明现有基准已饱和，agent 存在过拟合现象。

#### ✅ 更具现实挑战性
- **跨站任务成功率更低**：
  - Mayo Clinic + WebMD：12.5%
  - CDC + WebMD：8.2%
  - Drugs.com + CVS Health：**仅 4.2%**
- 表明跨域知识整合是重大挑战。

#### ✅ 生成效率更高
- 构建约 2,000 页面索引 + 生成 100 多跳任务 ≈ **$10**，边际成本趋近于零；
- 相比 AgentTrek（$0.55/task），GTA 单任务成本低至 **~$0.10**。

---

### 消融实验与错误分析（Error Analysis）

在 100 个失败案例中，主要失败模式如下：

| 错误类型 | 占比 | 说明 |
|--------|------|------|
| **未能访问所有必需页面** | 90% | 未导航到关键页面，导致信息缺失 |
| **提前终止（Early Stopping）** | 40% | 获取部分信息即作答，未验证完整性 |
| **过度依赖搜索框（Over-reliance on Search Box）** | 40% | 忽视页面结构，盲目使用站内搜索返回无关结果 |

> 这些发现揭示了当前 agents 在长视野推理中的根本弱点：缺乏系统性探索策略、难以判断何时收集足够证据。

---

## 4. 关键结论和发现

### 主要结论
1. **现有 Web Agent Benchmarks 已趋于饱和且存在偏差**：
   - 多数任务可被搜索引擎轻松解决（如 NNetNav 达 100%）；
   - 功能覆盖狭窄，集中在少数高频路径上。

2. **GTA 成功构建了更具挑战性和实用性的多跳任务**：
   - 任务复杂度更高，需跨页整合异构信息（数值、评级、医学警告等）；
   - 支持确定性回放与细粒度诊断，适合训练与评估。

3. **当前 Web Agents 泛化能力严重不足**：
   - 在跨站、多语言、结构复杂场景下表现极差；
   - 暴露了对英语中心化、模板化界面的严重依赖。

4. **自动化生成可以高效且高质量地构建 benchmark**：
   - GTA 实现了全自动化、低成本、高覆盖率的任务生产；
   - 并可通过定期爬取实现“自我演化”，适应网页变化。

---

### 方法的局限性
| 局限 | 说明 |
|------|------|
| **网站覆盖范围有限** | 当前不包含登录后页面、动态 JS 渲染内容或交易流程（出于安全考虑） |
| **依赖爬虫快照** | 网站更新可能导致任务失效（content drift），影响可重现性 |
| **验证仍依赖 LLM** | 尽管有 verifier，但仍可能遗漏细微逻辑错误或领域专业知识漏洞 |
| **任务类型受限** | 聚焦信息查找类任务，未覆盖表单提交、结账等操作密集型行为 |

---

### 未来工作方向
1. **扩展至认证与交互式流程**：开发沙箱环境以安全探索登录态服务；
2. **增强 temporal robustness**：研究如何应对网页结构随时间演变的挑战；
3. **引入 human-in-the-loop 验证**：提升高风险领域（如医疗）任务准确性；
4. **推动通用 Web Agent 架构**：鼓励研发真正具备跨语言、跨域适应能力的智能体。

---

> 📌 **总结一句话**：  
> GTA 不只是一个新数据集，而是一个**可自我演化的 benchmark 生态系统**，它重新定义了 Web Agent 的评测标准——从“能否完成预设路径”转向“能否在开放、动态、真实的网络世界中持续学习与推理”。

</details>

---

### 8. [Learning to Choose: An Empowerment-Guided Multi-Agent System with semantic communication for Adaptive Method Selection](https://arxiv.org/abs/2605.30042)

**Authors**: Geremy Loacham\'in-Suntaxi, Robert Lazar, Dimitrios G. Giovanis, Ioannis G. Kevrekidis, Eleni D. Koronaki  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.30042v1  

#### Abstract
Automating scientific computing workflows requires more than generating executable code: autonomous systems must also select appropriate computational strategies, implement them faithfully, and ensure that the resulting outcomes remain causally attributable to the decisions that produced them. In mu...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Learning to Choose: An Empowerment-Guided Multi-Agent System with Semantic Communication for Adaptive Method Selection*

---

## 1. 论文的主要贡献和创新点

### 解决的问题
该论文旨在解决**科学计算自动化流程中的“语义漂移”（semantic drift）问题**。在多智能体（multi-agent）系统中，尽管策略（policy）可能正确选择了最优的计算方法，但由于智能体间通信不一致，导致最终执行的代码与所选方法不符，从而破坏了“动作-结果”的因果关系。这使得基于奖励信号的学习机制失效，无法准确评估不同方法的真实性能。

此外，现有方法如 ATHENA 框架依赖专家知识注入来约束行为，但在面对多样化、不可预知的方法组合时，其泛化能力受限。

### 提出的新方法与新思路
本文提出了一种**以赋能（empowerment）为指导原则的多智能体框架**，通过以下三大核心组件实现自适应方法选择：

1. **Empowerment 理论驱动的设计原则**  
   将系统整体的“可控性”定义为动作 $A$ 与结果 $O$ 之间的互信息 $I(A; O|x)$。高赋能意味着方法选择能可靠地决定最终输出。为此，必须同时满足两个条件：
   - **统计学习能力**：通过 contextual bandit 学习高质量动作；
   - **通信保真度**：确保动作在传播过程中不被扭曲。

2. **结构化语义通信机制（Structured Semantic Communication）**
   - 引入三种机器可读的 **Scheme** 替代自由文本传递：
     - `ProblemScheme`：编码问题上下文；
     - `MethodScheme`：明确指定方法配置、最小预算、API 接口等；
     - `DiagnosticScheme`：将诊断转化为结构化反馈。
   - 这些 Scheme 保证了跨智能体的信息一致性，避免因理解偏差引发错误。

3. **七层语义检查点（Semantic Checkpoints, CP0–CP7）**
   - 在关键智能体边界部署基于 **cosine similarity** 的语义对齐检测机制；
   - 每个检查点针对特定失败模式（如上下文不一致、代码偏离策略、重复选择等）；
   - 支持动态阈值调整（adaptive thresholding），提升鲁棒性；
   - 其中 CP5 与 Inspector 构成双阶段“连贯性门控”（coherence gate）。

### 相比现有方法的优势
| 维度 | 现有方法（如 ATHENA） | 本工作 |
|------|------------------------|-------|
| **抗语义漂移机制** | 依赖专家知识注入（scaffolding） | 主动检测并纠正（checkpoints） |
| **适用范围** | 需预先编码领域约束 | 更通用，适用于方法不可知场景 |
| **学习信号可靠性** | 易受实现偏差影响 | 通过 CP 保障 $I(A;O|x)$ 不退化 |
| **探索策略灵活性** | 固定 warm-start | 跨会话相似性匹配 + 异常识别引导探索 |

---

## 2. 核心实验方法和设置

### 使用的数据集与任务
实验聚焦于两类典型科学计算任务：
- **Sensitivity Analysis (SA)**：敏感性分析，例如 Ishigami 函数、Sobol G-function（含 8 和 15 输入版本）
- **Uncertainty Quantification (UQ)**：不确定性量化

代表性模型包括：
- Ishigami function: $f(X_1,X_2,X_3) = \sin X_1 + 7\sin^2 X_2 + 0.1X_3^4 \sin X_1$
- Sobol G-function: $f(\mathbf{X}) = \prod_{i=1}^{d} \frac{|4X_i - 2| + a_i}{1 + a_i}$

### 实验设置
- **平台基础**：基于 UQpy 库构建执行环境；
- **LLM 使用**：多个 LLM 协同（Claude Haiku, Mistral 7B）承担不同角色；
- **多智能体架构分组**：
  - Conceptualization Team（解析用户请求）
  - Strategy Team（bandit 决策）
  - Implementation Team（代码生成）
  - Execution & Evaluation Team（运行与评分）

### 评估指标
综合奖励函数 $R_n$ 包括四个部分：
| 成分 | 最大值 | 描述 |
|------|--------|------|
| $R_{\text{integrity}}$ | 35 | 可执行性、API 正确调用、输出完整 |
| $R_{\text{accuracy}}$ | 35 | 收敛性、与解析解的 MAE、一致性约束（如 $S_T \geq S_1$） |
| $R_{\text{details}}$ | 15 | 缺失索引、负方差、警告未处理等惩罚项 |
| $R_{\text{optimality}}$ | 15 | 计算效率（样本数、时间、内存） |

总奖励上限为 **100 分**，目标是达到 $R \geq 85$。

### 基线方法对比
- **No-CP 条件**：所有检查点关闭（阈值设为 -1），作为弱基线；
- **Full Pipeline**：启用全部语义检查点与 Scheme 结构；
- 对比维度包括：
  - 动作-代码一致性（action-code fidelity）
  - 收敛速度
  - 累积 regret
  - 异常问题下的探索行为

---

## 3. 主要实验结果和性能指标

### 关键性能数据

#### ✅ **表 5：检查点消融实验（Adversarial Prompting）**

| 条件 | Bandit 选择 | 实际执行 | 是否匹配 | 总奖励 $R_n$ | CP事件 |
|------|-------------|----------|-----------|--------------|--------|
| No-CP-1 | Sobol | Chatterjee | ❌ | 82 | — |
| No-CP-2 | Sobol | Sobol | ✅ | 74 | — |
| No-CP-3 | Sobol | Morris | ❌ | 61 | — |
| CP-1 | Sobol | Sobol | ✅ | 80 | CP2×1 |
| CP-2 | Sobol | Sobol | ✅ | 70 | CP3×1 |
| CP-3 | Sobol | Sobol | ✅ | 53 | CP2×1 |

> ⚠️ **无检查点时，2/3 实验出现动作-代码不一致**，导致奖励错误归因，严重污染策略更新。

#### ✅ **表 6：方法替换攻击下的鲁棒性测试（Method-Swap Drift）**

| 条件 | 执行方法 | $R_1$ | $R_{\text{accuracy},1}$ | 收敛所需迭代次数 |
|------|---------|--------|--------------------------|------------------|
| no_cp5 | MorrisSensitivity（错误） | 7.0 | 0.0 | 3（经 CVM 恢复） |
| full | PCESensitivity（纠正后） | **95.17** | **43.67** | **1** |

> 💡 启用 CP5 后，系统成功拦截错误实现，并自动修正为合适的 PCE 方法，在单次迭代内达成高性能。

#### ✅ **表 7：高维 Sobol 函数（d=15）上的跨会话知识积累**

| Session | 最佳 $R$ |
|--------|---------|
| Session 1 | 64.2 |
| Session 2 | 68.8 |
| Session 3 | **75.5** |

> 🔁 表明策略具备跨会话记忆能力，随着经验积累，收敛更快、性能更高。

#### ✅ **表 8：CP0 异常检测表现**

| 问题类型 | $d_{in}$ | Archive entries | CP0 相似度 | 初始方法 | $R_1$ |
|--------|--------|---------------|------------|----------|--------|
| Cantilever Beam（熟悉） | 4 | 2 | 0.991 | Sobol | 91.0 |
| Thermal Diffusion（异常） | 20 | 0 | 0.243 | Morris | 72.0 |

> 🧭 CP0 成功识别新问题并激活“先筛选后分解”策略，防止资源浪费。

---

## 4. 关键结论和发现

### 主要发现
1. **语义漂移是多智能体系统学习失败的根本原因之一**  
   即使策略选择正确，若缺乏传播保真机制，奖励信号仍会被污染，导致 bandit 学习噪声而非真实方法质量。

2. **Empowerment 是统一设计原则的有效视角**  
   将“可控性”形式化为 $I(A;O|x)$，自然导出“选择好动作”与“保持动作完整性”的双重需求，指导系统架构设计。

3. **Semantic Checkpoints 显著提升系统鲁棒性与学习效率**  
   - CP2、CP4、CP5 等 blocking checkpoints 能有效阻止错误传播；
   - CP0 实现 warm-start 与 anomaly-directed exploration 的无缝切换；
   - CP7 维持动作多样性，防止过早收敛。

4. **结构化 Scheme 是实现语义一致性的基础设施**  
   替代自由文本通信后，显著降低 LLM 幻觉风险，提高下游智能体决策精度。

### 方法的局限性
- **依赖外部库（UQpy）的知识结构**：当前框架深度绑定 UQpy 的 API 设计，迁移至其他领域需重构模板与 Scheme；
- **LLM 成本较高**：多个 LLM 并行调用带来推理开销；
- **动态阈值调优仍具挑战**：虽引入自适应机制，但极端情况下可能出现误判；
- **目前仅验证于 SA/UQ 场景**：是否可推广至更广泛的科学计算任务有待验证。

### 未来工作方向
1. **结合 GRAFT-ATHENA 的几何记忆结构**  
   将方法嵌入图结构空间，支持跨问题的知识迁移与指纹匹配。

2. **引入更强大的表示对齐技术**  
   如 manifold alignment、alternating diffusion 等，替代简单的 cosine similarity。

3. **融合程序等价性验证与因果干预测试**  
   使用 formal verification 或 intervention-based testing 提升代码正确性保障。

4. **扩展至更多科学计算领域**  
   如优化、反演、参数估计等，验证框架通用性。

5. **研究路径依赖性与策略稳定性**  
   探索不同初始探索序列下策略收敛的一致性（path-dependence score）。

---

> 📌 **总体结论**：  
> 本文提出了一种将 **empowerment 理论** 与 **语义通信机制** 相结合的新型多智能体架构，解决了科学自动化中长期存在的“选择—执行脱节”问题。实验证明，该框架不仅能提高方法选择的准确性与收敛速度，更重要的是**保障了学习信号的因果完整性**，为构建可信、可解释、可持续进化的 AI 科学助手提供了坚实基础。

</details>

---

### 9. [RightNow-Arabic-0.5B-Turbo: An Open Sub-1B Arabic Language Model via Vocabulary Injection and Edge-First Deployment](https://arxiv.org/abs/2605.28827)

**Authors**: Jaber Jaber, Osama Jaber  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.28827v1  

#### Abstract
Open Arabic large language models split into two classes: sub-1B multilingual models that treat Arabic as an afterthought (Qwen2.5-0.5B, Falcon-H1-0.5B), and 7B-70B Arabic-specialized models that require a server to run (Jais, AceGPT, ALLaM, SILMA). The one published attempt at a sub-2B Arabic-speci...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：RightNow-Arabic-0.5B-Turbo: An Open Sub-1B Arabic Language Model via Vocabulary Injection and Edge-First Deployment

---

## 1. 论文的主要贡献和创新点

### ✅ 解决的问题
当前开源的阿拉伯语大语言模型存在明显的两极分化：
- **小模型（<1B 参数）**：如 Qwen2.5-0.5B、Falcon-H1-0.5B，虽然可在边缘设备运行，但将阿拉伯语视为多语言中的次要语言，缺乏专用词表和训练数据。
- **大模型（7B–70B 参数）**：如 Jais、ALLaM、SILMA，虽在阿拉伯语任务上表现优异，但需要服务器级资源（16–140 GB 内存），无法部署于手机、嵌入式设备等边缘场景。

此外，唯一尝试填补这一空白的 **Kuwain-1.5B** 虽提出“语言注入”方法，但未公开权重，不具备可复现性和实用性。

👉 因此，**缺乏一个轻量级、专为阿拉伯语优化且完全开源的 LLM**，限制了阿拉伯语在边缘计算场景的应用。

---

### 🚀 提出的新方法与创新思路

作者提出了 **RightNow-Arabic-0.5B-Turbo**，一个仅 **518M 参数** 的阿拉伯语专用 decoder-only LLM，其核心流程如下：

1. **Vocabulary Injection（词表注入）**
   - 在 Qwen2.5-0.5B 基础上，通过 **SentencePiece unigram 模型** 训练出 32,000 个阿拉伯语子词单元。
   - 与原词表去重后新增 **27,032 个阿拉伯语专属 token**。
   - 使用 **Mean-Subtoken Initialization** 初始化新 token 的 embedding 向量，避免破坏原有语义空间。

2. **Edge-First Deployment Pipeline（面向边缘部署的全流程设计）**
   - **持续预训练（Continued Pretraining）**：在 504M 阿拉伯维基百科 token 上继续训练。
   - **监督微调（SFT）**：使用 129,116 条阿拉伯语指令对，采用 **response-only loss masking**，只对助手回复部分计算损失。
   - **直接偏好优化（DPO）**：基于 6,750 对阿拉伯语偏好数据进行对齐。
   - **Weight Soup Merging**：融合 DPO、SFT 和 Pretrain 三个检查点，提升泛化能力。
   - **GGUF 量化导出**：支持多种量化格式（f16, q8_0, q5_k_m, q4_k_m），最小仅 **398MB**，适配边缘设备。

3. **系统级工程优化**
   - 使用 **FlashAttention varlen packing** 处理变长序列并保留文档边界。
   - 采用 **Liger fused kernels** 加速 RMSNorm、RoPE、SwiGLU 和交叉熵计算。
   - 自定义 **memmap 数据加载器** 避免 HuggingFace Hub 多进程卡顿问题。

---

### 🔍 相比现有方法的优势

| 维度 | 优势 |
|------|------|
| **规模与可用性** | 是目前 **最小的开源阿拉伯语专用 decoder LLM**（518M），远小于同类（7B+），首次实现边缘部署可行性。 |
| **性能表现** | 在 COPA-ar 上 **持平 1.5B 模型（Falcon-H1-1.5B）**，优于所有同级别 <1B 模型。 |
| **效率提升** | 词表优化使阿拉伯语 token fertility 降低 **17.3%**（2.18 → 1.80 tokens/word），显著减少推理 token 数量。 |
| **开放程度** | 完全开源：代码（5,555 行）、权重（bf16/int8/GGUF）、训练脚本、中间检查点全部发布于 HuggingFace。 |
| **推理速度** | 在单张 H100 上使用 llama.cpp 达到 **635 tokens/s（bs=1）**，是 HF generate 的 **8 倍以上**。 |

---

## 2. 核心实验方法和设置

### 📚 使用的数据集

| 类型 | 数据集 | 规模 | 描述 |
|------|--------|-------|------|
| **预训练** | `wikimedia/wikipedia` (ar) | 504M tokens | 经过新 tokenizer 编码后的阿拉伯语维基文本 |
| **SFT** | 合并五个数据集：<br>- `evol-instruct-arabic`<br>- `alpaca-gpt4-arabic`<br>- `sharegpt-arabic`<br>- `CIDAR`<br>- `aya_dataset`（arb 子集） | 129,116 唯一指令对 | 经 MD5 去重后的 ChatML 格式数据 |
| **DPO** | `argilla-dpo-mix-7k-arabic` | 6,750 偏好对 | 包含 chosen/rejected 回复的三元组 |
| **评估** | lm-evaluation-harness 中的三个任务：<br>- `copa_ar`<br>- `arabic_mt_hellaswag`<br>- `arabic_leaderboard_arabic_mmlu` | 共 14,575 题 | 标准化阿拉伯语评测基准 |

---

### ⚙️ 实验设置与评估指标

- **硬件平台**：Nebius gpu-h100-sxm（8×H100 80GB SXM5）
- **训练框架**：
  - FSDP（_HYBRID_SHARD_ZERO2）
  - FlashAttention-2（varlen 支持）
  - Liger Kernel（融合算子加速）
- **评估工具**：`lm-evaluation-harness v0.4.11`
- **评估参数**：
  - `batch_size=2`
  - `max_length=1536`
  - `limit=200` per task
  - `apply_chat_template=True`（若无模板则用原始 prompt）
  - 优先使用 `acc_norm` 指标
- **对比基线**：
  - 同类小模型：Qwen2.5-0.5B-Instruct、Falcon-H1-0.5B-Instruct
  - 更大规模模型：Falcon-H1-1.5B、AceGPT-7B、ALLaM-7B、SILMA-9B

---

## 3. 主要实验结果和性能指标

### 📊 关键性能数据（见 Table 3）

| Model | Params | COPA-ar | HellaSwag-ar | ArabicMMLU | **Mean** |
|-------|--------|---------|--------------|------------|----------|
| Qwen2.5-0.5B-Instruct | 494M | 53.9% | 22.5% | 26.0% | **34.1%** |
| Falcon-H1-0.5B-Instruct | 524M | 44.9% | 23.0% | 24.2% | **30.7%** |
| **Ours (RightNow-Arabic-0.5B-Turbo)** | **518M** | **58.4%** | **26.0%** | 23.2% | **35.9%** |
| Falcon-H1-1.5B-Instruct | 1.5B | 58.4% | 27.5% | 32.7% | 39.5% |
| SILMA-9B-Instruct | 9B | 69.7% | 38.0% | 52.9% | **53.5%** |

#### ✅ 主要结论：
- **在 <1B 类别中全面领先**：平均准确率 **35.9%**，超越所有同级模型。
- **COPA-ar 上媲美 3 倍参数模型**：达到 **58.4%**，与 Falcon-H1-1.5B 并列第一。
- **以极小代价逼近大模型表现**：达到 SILMA-9B（9B）**67.1% 的平均得分**，仅用其 **5.8% 的参数量**。

---

### 🔬 消融实验结果（Weight Soup Ablation）

| Checkpoint | COPA-ar | HellaSwag-ar | ArabicMMLU | Mean |
|-----------|--------|-------------|------------|------|
| DPO checkpoint (baseline) | 58.43% | 24.00% | 23.18% | 35.20% |
| **Soup (DPO 0.5, SFT 0.25, Pretrain 0.25)** | 58.43% | **25.33%** | 23.17% | **35.64%** |
| lerp(DPO, Pretrain, t=0.5) | 58.43% | 24.67% | 23.04% | 35.38% |
| lerp(DPO, SFT, t=0.5) | 57.30% | 23.33% | 23.24% | 34.63% |

#### 发现：
- **Weight Soup 显著提升性能**：相比单独 DPO 检查点，**平均提升 +0.44%**，主要来自 HellaSwag-ar 的增益。
- **最佳配置为线性加权 (0.5, 0.25, 0.25)**，说明保留部分早期知识有助于缓解过拟合。
- **SLERP 与 LERP 效果相近**，在该任务下无明显优势。
- **仅合并 SFT 会劣化性能**，表明并非所有组合都有益。

---

### ⏱️ 推理性能测试（llama.cpp on H100）

| Quantization | Disk Size | Prompt Eval (tok/s) | Generation (tok/s) |
|-------------|-----------|---------------------|--------------------|
| f16         | 988 MB    | 634.0               | 582.4              |
| q8_0        | 525 MB    | 732.8               | 645.7              |
| q5_k_m      | 419 MB    | 718.5               | 633.5              |
| **q4_k_m**  | **398 MB**| **723.6**           | **634.9**          |

- 最小版本仅 **398MB**，适合移动端部署。
- 所有量化版本均超过 **580 tokens/s**，**q8_0 吞吐最高**，**q4_k_m 占用最低**。
- 相比 HuggingFace 默认生成方式（约 82 tok/s），**性能提升达 8 倍**，得益于 CUDA Graph 和 C++ 采样优化。

---

## 4. 关键结论和发现

### ✅ 主要发现

1. **小模型也能做好阿拉伯语建模**  
   只要通过合理的 **词表扩展 + 高效训练流程 + 系统级优化**，即使 0.5B 级别的模型也可以在特定任务（如 COPA-ar）上媲美更大模型。

2. **Tokenizer Efficiency 至关重要**  
   新增 27,032 个阿拉伯语 token 将 fertility 从 2.18 降至 1.80（↓17.3%），直接带来推理速度提升和上下文利用率提高。

3. **Weight Soup 是有效的后处理手段**  
   即使 DPO 阶段信号微弱（loss 几乎不变），通过融合多个检查点仍能稳定提升性能，验证了“模型汤”的鲁棒性。

4. **边缘部署必须端到端考虑**  
   从训练、量化到运行时引擎（llama.cpp），每个环节都需协同优化才能释放小模型潜力。

---

### ⚠️ 局限性

| 问题 | 描述 |
|------|------|
| **知识容量受限** | 在 ArabicMMLU 上落后大模型 29+ 分，说明 **<1B 模型难以承载复杂世界知识**，适用于轻量对话而非知识密集型问答。 |
| **DPO 信号薄弱** | DPO 训练损失几乎未下降（始终接近 ln2），reward margin 接近零，说明当前偏好数据质量不足或规模太小。 |
| **仅支持 MSA（Modern Standard Arabic）** | 对埃及、海湾、黎凡特等方言处理能力差，输出统一为标准阿拉伯语。 |
| **词表优化未达理论极限** | 当前 fertility 下降 17.3%，低于理想值（预计可达 30%），因受限于不能完全替换原 BPE 词表。 |
| **预训练 token 数不足** | 仅 504M tokens / 518M params ≈ 1:1，远低于 Chinchilla 最优比例，限制进一步提升空间。 |
| **GGUF 量化 tile 不对齐** | 因新增词表导致 embedding 行数不匹配，q4_k_m/q5_k_m 实际 bit 数分别为 6.45 和 6.79，未能真正压缩到位。 |

---

### 🔮 未来工作方向

1. **引入更多方言数据** 进行混合预训练，增强对口语化阿拉伯语的理解与生成能力。
2. **构建高质量原生阿拉伯语 DPO 数据集**，替代机器翻译数据，提升对齐效果。
3. **探索第二轮词表注入**，添加高频阿拉伯语短语（multi-word units），进一步降低 fertility。
4. **整合 FineWeb-2-ar 或 CulturaX-ar** 等更大规模语料，突破当前预训练 token 瓶颈。
5. **优化 GGUF 导出流程**，调整词表 padding 使其符合 llama.cpp 的 tile 对齐要求，实现真正的低比特量化。
6. **开发移动端 demo 应用**，验证在 Android/iOS 上的实际部署体验。

---

## 总结

📌 **RightNow-Arabic-0.5B-Turbo** 成功填补了 **轻量级、开源、阿拉伯语专用 LLM** 的空白，证明了通过 **vocabulary injection + edge-first pipeline** 可在极小参数下实现高性能阿拉伯语理解与生成。

💡 其最大意义不仅在于模型本身，更在于提供了一套 **完整、可复现、面向实际部署的语言模型定制范式**，为其他低资源语言的小模型开发提供了宝贵参考。

</details>

---

### 10. [Cluster-Level Attention-Guided Parallel Decoding for Masked Diffusion Language Models](https://arxiv.org/abs/2605.29607)

**Authors**: Heqiang Qi, Wei Huang, Mingyuan Bai, Xiangming Meng  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 9.0  
**Type**: new  
**ArXiv ID**: 2605.29607v1  

#### Abstract
Masked diffusion language models (MDLMs) enable parallel decoding by predicting all masked positions at each denoising step, yet existing training-free samplers usually decide which positions to commit at token-level granularity. We revisit this granularity and observe that reliable predictions ofte...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Cluster-Level Attention-Guided Parallel Decoding for Masked Diffusion Language Models**

---

## 1. **论文的主要贡献和创新点**

### **解决的问题**
现有的 **Masked Diffusion Language Models (MDLMs)** 虽然支持并行解码，但大多数训练无关（training-free）的采样器（samplers）在每一步去噪中以**token-level granularity**决定哪些位置应被提交（commit）。这种逐token决策可能导致：
- **冗余计算**：高置信度的预测常以连续片段（contiguous spans）形式出现，逐个提交效率低下；
- **冲突风险**：即使单个token置信度高，多个强依赖的token同时提交可能引入不一致（incompatible predictions）。

因此，如何在保持生成质量的同时，提升MDLM的**解码吞吐量（throughput）** 是一个关键挑战。

---

### **提出的新方法：CLAD**
本文提出了 **CLAD (Cluster-Level Attention-Guided Decoding)**，一种无需训练的、基于**簇级（cluster-level）** 的并行解码策略，其核心思想是：
1. **将解码单位从token提升为span-level**：
   - 定义 **Confidence-Induced Clusters (CICs)**：将相邻的高置信度masked positions聚合成连续的“可靠片段”作为更新单元。
2. **利用自注意力估计簇间依赖关系**：
   - 复用前向传播中的 **self-attention maps** 构建**稀疏冲突图（sparse conflict graph）**，识别互为强依赖的CIC对。
3. **冲突感知的并行提交**：
   - 将CIC选择建模为 **Maximum-Weight Independent Set (MWIS)** 问题，选择一组无冲突且权重（长度）最大的CIC进行并行提交。

---

### **相比现有方法的优势**
| 维度 | 传统方法（如Vanilla, Fast-dLLM, KLASS） | CLAD |
|------|----------------------------------------|------|
| **解码粒度** | Token-level | **Cluster-level (span-level)** |
| **并行性** | 有限，依赖单个token置信度 | 更高，一次提交多个连续token |
| **依赖建模** | 忽略或仅建模token-level依赖（如DAPD, DAWN） | 显式建模**inter-cluster依赖**，避免冲突 |
| **训练需求** | 所有对比方法均为training-free | ✅ 无需额外训练 |

> ✅ **核心优势**：通过**更大的更新单元 + 注意力引导的冲突检测**，实现更高吞吐量，同时维持生成准确性。

---

## 2. **核心实验方法和设置**

### **使用的模型**
在以下两个主流MDLM系列上进行评估：
- **LLaDA** family: LLaDA-8B-Instruct, LLaDA-1.5
- **Dream** family: Dream-v0-Base-7B, Dream-v0-Instruct-7B

所有方法均**固定模型权重**，仅修改解码策略，确保为 **training-free setting**。

---

### **数据集**
涵盖**数学推理**与**代码生成**两类任务：
| 类别 | 数据集 | 任务描述 |
|------|--------|----------|
| 数学推理 | **GSM8K (5-shot)**, **MATH (4-shot)** | 多步推理，长答案生成 |
| 代码生成 | **MBPP (3-shot)**, **HumanEval (0-shot)** | 根据自然语言描述生成可执行Python代码 |

---

### **评估指标**
| 指标 | 含义 |
|------|------|
| **Accuracy (Acc.)** | 数学任务：最终答案匹配；代码任务：官方unit test通过率（pass rate） |
| **Tokens Per Second (TPS)** | 端到端生成速度，包含prompt处理、解码、后处理 |
| **Speedup** | 相对于Vanilla top-1 decoding的加速比 |

---

### **基线方法对比**
| 方法 | 类型 | 核心机制 |
|------|------|---------|
| **Vanilla** | 基线 | Top-1逐token解码 |
| **Fast-dLLM** | Uncertainty-based | 动态提交置信度高于阈值的token |
| **KLASS** | Stability-based | 结合置信度与跨step分布稳定性 |
| **DAPD**, **DAWN** | Dependency-aware | 利用attention构建token-level依赖图，避免强耦合token同时提交 |

---

## 3. **主要实验结果和性能指标**

### **关键性能数据（来自Table 1 & 8）**
在 **LLaDA-8B-Instruct** 上，CLAD 相比 Vanilla 实现显著加速：
| 任务 | Speedup | Accuracy 变化 |
|------|---------|----------------|
| GSM8K | **4.90×** | +0.08 (≈持平) |
| MATH | **3.76×** | -0.92 (轻微下降) |
| MBPP | **4.89×** | -1.40 |
| HumanEval | **4.24×** | 0.00 |

在 **Dream-v0-Instruct-7B** 上同样表现优异：
| 任务 | Speedup | Accuracy 变化 |
|------|---------|----------------|
| GSM8K | 4.41× | -2.80 |
| MATH | **2.59×** | -1.02 |
| MBPP | **5.52×** | -0.80 |
| HumanEval | **2.86×** | +1.83 |

> 📌 **最高加速达 8.47×**（见MBPP on LLaDA-1.5），且多数情况下准确率与Vanilla相当。

---

### **与基线方法对比**
- **相比Fast-dLLM/KLASS**：CLAD 在所有任务上实现更高 TPS 和 Speedup。
- **相比DAPD/DAWN（token-level依赖感知）**：
  - CLAD 在多数设置下**吞吐量更高**，验证了**cluster-level更新单元的有效性**。
  - 尽管DAPD/DAWN也使用attention，但其仍受限于token粒度，无法充分利用局部一致性。

---

### **消融实验结果（Ablation Study）**
#### （1）组件消融（Table 2）
| 变体 | Acc. | TPS | 说明 |
|------|------|-----|------|
| Vanilla | 40.24 | 16.66 | 基线 |
| +CIC | 36.58 | 76.03 | 仅用CIC → 速度快但准确率暴跌 |
| +CIC +Graph | 36.58 | 66.13 | 加入冲突图但随机选 → 准确率未恢复 |
| **CLAD (全量)** | **40.24** | **70.65** | 加入MWIS选择 → 准确率恢复，速度仍高 |

> ✅ **结论**：**冲突感知的选择（MWIS）至关重要**，否则盲目并行会损害质量。

#### （2）超参数敏感性分析**
- **置信度阈值 T**：较低T → 更多CIC → 更高速度但可能降低准确率；适中T（如0.7–0.75）平衡最佳。
- **Block Size**：在多种block size下CLAD均优于Vanilla，表明其鲁棒性强。
- **生成长度**：在不同长度（128–1024）下CLAD均保持优势，尤其在中等长度收益最大。

---

## 4. **关键结论和发现**

### **主要发现**
1. **高置信预测具有局部连续性**：MDLM解码过程中，可靠预测往往以**连续片段（spans）** 形式出现，支持使用**cluster-level更新单元**。
2. **提升解码粒度可显著加速**：从token-level升级到CIC-level，使每次迭代能提交更多token，大幅减少去噪步数。
3. **注意力可用于估计簇间依赖**：复用self-attention maps构建**冲突图**，有效避免提交相互依赖的CIC，维持生成一致性。
4. **CLAD在多数场景下实现高效与准确的平衡**：平均 **1.77× – 8.47× 速度提升**，同时任务准确率与Vanilla基本持平。

---

### **局限性（Limitations）**
1. **Attention是启发式信号**：
   - Self-attention 并非严格的因果依赖度量，可能存在误判（高attention ≠ 冲突；低attention ≠ 独立）。
2. **效果依赖任务与模型特性**：
   - 当候选更新高度碎片化、簇间依赖密集、或任务需细粒度逐步推理时，并行性受限。
   - 不同MDLM backbone的attention模式差异可能影响CIC有效性。
3. **非普适最优**：
   - CLAD 是一种**实用策略**，而非在所有设置下都绝对最优。

---

### **未来工作方向**
- 探索更精确的**跨簇依赖建模方式**（如轻量微调、探针网络）。
- 结合**语义一致性检测**或**逻辑约束**进一步优化冲突判断。
- 将CLAD思想扩展至其他生成任务（如图像、音频 diffusion models）。

---

> ✅ **总结一句话**：  
> **CLAD 通过将解码单位从 token 提升为 confidence-induced cluster，并利用 attention 指导冲突感知的并行提交，在无需训练的前提下实现了高达 8.47× 的解码加速，同时保持了与 Vanilla 相当的任务性能。**

</details>

---

### 11. [Robust and Efficient Guardrails with Latent Reasoning](https://arxiv.org/abs/2605.29068)

**Authors**: Siddharth Sai, Xiaofei Wen, Muhao Chen  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.29068v1  

#### Abstract
Maintaining the safety of large language models (LLMs) is crucial as they are increasingly deployed in real-world applications. Existing safety guardrails typically rely on single-pass classification or, more recently, distilled reasoning. Reasoning-based guardrails significantly outperform classifi...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：*Robust and Efficient Guardrails with Latent Reasoning*

## 1. 论文的主要贡献和创新点

### 解决的问题
大型语言模型（LLMs）在实际应用中需要部署**安全守卫机制（Guardrails）**以防止生成有害内容。现有的基于显式推理（explicit reasoning）的守卫模型（如 GuardReasoner、ThinkGuard）虽然提升了鲁棒性，但依赖于生成链式思维（Chain-of-Thought, CoT）的中间理由文本，导致显著的**推理延迟和Token开销**，难以满足高吞吐量、实时场景的需求。

### 提出的新方法：CoLAGUARD
本文提出 **CoLAGUARD**，一种将多步安全推理过程内化到连续隐状态空间中的**潜推理（latent reasoning）守卫框架**。其核心思想是通过一个**阶段式训练课程（stage-wise training curriculum）**，逐步将显式的自然语言推理步骤替换为隐状态中的递归计算，从而在推理时避免生成冗长的CoT文本。

### 相比现有方法的优势
- **保持鲁棒性**：继承了显式推理带来的强泛化能力和抗对抗样本能力。
- **大幅提升效率**：
  - 推理速度提升 **12.9×**
  - Token 使用减少 **22.4×**
- **实用性强**：解决了显式推理守卫模型因高成本而难以部署的实际瓶颈，实现了**安全性与效率的联合优化**，而非权衡取舍。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **训练数据**：采用 `GuardReasonerTrain` 数据集（约127,000个样本），该数据集整合了以下多个安全导向数据集，并附带专家模型生成的多步推理轨迹：
  - WildGuard
  - AegisSafety
  - BeaverTails
  - ToxicChat
- **评估基准**：涵盖 **8个安全基准测试**，分为两类共10个任务：
  - **Prompt Harmfulness Detection**（提示有害性检测）
    - ToxicChat
    - OpenAI Moderation
    - Aegis Safety Test
    - HarmBench
    - WildGuardTest
  - **Response Harmfulness Detection**（响应有害性检测）
    - HarmBench
    - SafeRLHF
    - BeaverTails
    - XSTest
    - WildGuardTest

### 实验设置和评估指标
- **主干模型**：基于 Llama 3.1 8B 和 Llama 3.2 3B 进行微调。
- **训练流程**：
  1. **Stage 0（Warm-up）**：先作为显式推理模型训练，学习生成完整的CoT和标签。
  2. **Stage 1–6 + Compression Stage**：逐步用固定数量的**潜步骤（latent steps）** 替换前k个推理步骤，最终实现完全内化的潜推理。
- **关键技术组件**：
  - **Context-Prediction Fusion (CPF)**：缓解原始隐藏状态与词嵌入分布不匹配的问题，稳定潜递归过程。
- **评估指标**：
  - 主要指标：**Macro-F1** 和 Micro-F1
  - 效率指标：**推理时间（ms/query）**、**Completion Token 数量（token/query）**、**EA-F1**（Efficiency-Adjusted F1，综合衡量准确率与效率）

### 基线方法对比
- **闭源API类**：
  - GPT-4o, GPT-4o+CoT, o1-preview
- **开源守卫模型**：
  - Llama Guard 系列（7B/8B）
  - ShieldGemma（2B/9B）
  - WildGuard（7B）
  - Aegis Guard 系列
  - QwQ-preview（32B）
- **显式推理守卫模型**（主要对比基线）：
  - **GuardReasoner**（1B/3B/8B）——使用相同训练数据和监督信号，仅区别在于是否生成显式CoT

---

## 3. 主要实验结果和性能指标

### 关键性能数据
| 模型 | Prompt Macro-F1 | Response Macro-F1 | 平均 Macro-F1 |
|------|------------------|--------------------|----------------|
| Llama Guard 3 (8B) | 79.94 | 71.15 | **75.55** |
| GuardReasoner (8B) | 84.40 | 83.13 | **83.77** |
| **CoLAGUARD (8B)** | **84.23** | **83.33** | **83.78** |

> ✅ CoLAGUARD 在平均 Macro-F1 上**持平甚至略微超越** GuardReasoner，且相比 Llama Guard 3 提升达 **8.24点**。

### 与基线方法的对比结果
- **性能方面**：
  - CoLAGUARD 8B 在多个子任务上表现优异，例如在 WildGuardTest 上取得最佳F1分数（prompt: 89.44, response: 81.23）。
  - CoLAGUARD 3B 已经优于 GuardReasoner 3B，在 prompt 和 response 宏观F1上均有小幅领先。
- **效率方面**（见 Table 4）：
  | 指标 | GuardReasoner (8B) | CoLAGUARD (8B) | 提升倍数 |
  |------|---------------------|------------------|----------|
  | 推理时间 (ms/query) | 4,407.8 | **342.0** | **12.9× 更快** |
  | Token 成本 (token/query) | 289.4 | **12.9** | **22.4× 减少** |
  | EA-F1 | 0.1838 | **2.3601** | 显著更优 |

> 💡 表明 CoLAGUARD 在几乎不损失性能的前提下，实现了**数量级级别的效率飞跃**。

### 消融实验结果
- **Context-Prediction Fusion (CPF) 的作用**：
  - 若移除 CPF，使用 vanilla Coconut 架构，性能下降明显（combined macro-F1 从 83.78 → 81.82）。
  - 验证了 CPF 对提升潜状态表达能力、避免“占位符行为”至关重要。
- **几何分析（UMAP + Cosine Similarity Heatmap）**：
  - Vanilla Coconut 的潜状态跨步相似度极高，表明早期即做出决策并简单传播。
  - CoLAGUARD 的潜状态随递归步数逐渐分化，显示其在持续进行有意义的安全相关表征演化。
- **训练数据规模影响**：
  - 随着训练数据增加（8k → 30k → 127k），CoLAGUARD 性能持续提升，尤其在 prompt 检测任务上收益更大，说明其具备良好的可扩展性。

---

## 4. 关键结论和发现

### 主要发现
1. **潜推理可以有效替代显式CoT**：通过阶段式内化训练，模型能够将复杂的推理逻辑压缩进隐状态中，无需输出自然语言理由即可达到同等甚至更好的判断准确性。
2. **效率与鲁棒性不再对立**：传统观点认为更强的鲁棒性必然带来更高的计算成本。本研究表明，借助潜推理技术，二者可以**协同优化**。
3. **Context-Prediction Fusion 是关键设计**：它解决了潜状态与词嵌入之间的分布偏移问题，使潜递归过程更加稳定和富有语义意义。
4. **潜状态确实在“思考”**：可视化分析表明，CoLAGUARD 的潜状态在递归过程中呈现出渐进式的类别分离趋势，支持其执行了实质性的推理计算。

### 局限性
1. 当前评估集中于**纯文本的提示与响应有害性检测**，未覆盖多语言、多模态、长周期Agent行为等复杂场景。
2. 模型依赖蒸馏得到的推理轨迹，可能继承上游模型的**偏差或覆盖盲区**。
3. 尽管潜状态被证明具有动态演化特性，但其内部决策机制仍缺乏**因果层面的可解释性**，难以精确追溯每一步的作用。

### 未来工作方向
- 扩展至 **multilingual 和 multimodal guardrails** 场景。
- 探索更高效的潜预算调度策略（adaptive latent budget）。
- 引入**因果干预方法**深入解析潜推理路径，增强安全决策的透明度与可控性。
- 结合人类反馈进一步优化潜推理过程的对齐质量。

---

> 📌 **总结一句话**：  
> **CoLAGUARD 成功地将显式推理的安全增益“无损压缩”进高效隐状态运算中，在几乎不牺牲鲁棒性的前提下，实现了超过12倍的速度提升和22倍的Token节省，为可部署的高性能LLM守卫系统提供了新范式。**

</details>

---

### 12. [PassNet: Scaling Large Language Models for Graph Compiler Pass Generation](https://arxiv.org/abs/2605.29357)

**Authors**: Yiqun Liu, Yingsheng Wu, Ruqi Yang, Enrong Zheng, Honglei Qiu, Sijun He, Tai Liang, Jingjing Wu, Yuhan Zhou, Yiwei Zhang, Dongyan Chen, Weihan Yi, Xinqi Li, Siqi Bao  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.29357v1  

#### Abstract
Modern tensor compilers such as TorchInductor deliver substantial speedups on mainstream models, yet face a systematic performance ceiling on long-tail workloads -- our profiling shows that 43% of real-world subgraphs experience end-to-end slowdowns under default compilation. While LLMs offer a path...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# 论文总结：PassNet: Scaling Large Language Models for Graph Compiler Pass Generation

---

## 1. 论文的主要贡献和创新点

### 解决了什么问题
现代张量编译器（如 **TorchInductor**）在主流模型上能带来显著加速，但在“长尾”计算图（long-tail workloads）上表现不佳。作者通过分析发现，在真实社区模型中提取的子图有 **43% 出现端到端性能下降**，8.3% 被严格劣化。这表明当前基于规则的静态优化 pass pipeline 存在系统性瓶颈。

现有 LLM 工作多集中于 **kernel generation**（生成单个算子的 CUDA 内核），但存在以下问题：
- 缺乏可组合性（composability）
- 需手动集成进编译流程
- 不易验证正确性（unconstrained code generation）

因此，如何实现**自动化、可验证、可集成**的图级优化成为关键挑战。

---

### 提出了什么新方法或新思路
本文提出 **PassNet**，是首个面向 **LLM-based compiler pass generation** 的大规模生态系统，其核心创新在于：

#### ✅ 新任务定义：**Pass Generation**
- 给定一个计算子图，要求 LLM 生成一个结构化的 **compiler pass**，包含：
  - `Matcher`：识别可优化的子图模式
  - `Rewriter`：将其替换为等价但更高效的实现
- 该 pass 可直接接入现有编译器 IR 流程（如 MLIR、TorchInductor），保持 `torch.compile` 一键编译体验。

#### ✅ 构建两大基础设施
1. **PassNet-Dataset**
   - 包含从 **100K 真实世界模型**（PyTorch/PaddlePaddle）中提取的 **18,086 个去重后的唯一计算图**
   - 采用 **Recursive Folding** 和 **Execution-driven Prefix Analysis** 生成多层次、多样化的训练子图
   - 支持形状与 dtype 泛化，提升跨硬件泛化能力

2. **PassBench**
   - 由 **200 个长尾融合任务**构成的评测基准，涵盖 **2,060 个子图**
   - 引入 **Error-aware Speedup Score (ES)**：统一衡量 **正确性、稳定性、性能** 的综合指标
   - 设计 **三层防御机制** 抵御 LLM 在评测中的作弊行为（如调用高阶 API 规避实现）

---

### 相比现有方法的优势
| 维度 | 传统方法 / Kernel Generation | PassNet |
|------|-------------------------------|--------|
| 输出形式 | 单独 kernel（不可组合） | 结构化 pass（可集成） |
| 验证方式 | 黑盒输出比对 | 白盒结构检查 + 运行时监控 |
| 可扩展性 | 每个 kernel 手动部署 | 自动匹配并应用到同类子图 |
| 数据基础 | 合成或小规模数据集 | 大规模真实场景图数据 |
| 评估完整性 | 忽视正确性容忍度 | 多容忍度连续反馈信号 |

> 🔍 **核心思想转变**：从“生成代码”转向“生成可复用、可验证的编译器变换逻辑”。

---

## 2. 核心实验方法和设置

### 使用的数据集
- **PassNet-Dataset**
  - 来源：100K 社区开源模型（HuggingFace、timm 等）
  - 类型分布：NLP (63.6%)、CV (27.0%)、Multimodal/Audio/Others
  - 图规模：节点数从 2 到近 30 万，覆盖轻量到 10B 参数大模型
  - 子图类型：
    - Fusible Subgraphs: 129K
    - Classical Subgraphs: 126K
    - Single-operator: 24K
  - 每种子图生成 **10 种形状配置 + 3 种 dtype**（FP32/FP16/BF16）

- **PassBench**
  - 评测任务：200 个长尾融合任务（无重叠于训练集）
  - 子图总数：2,060 个（平均每个任务 10.3 个子图）
  - 分层设计：包含不同 operator 序列、shape、dtype 的组合，提供细粒度反馈

---

### 实验设置和评估指标

#### 评估指标
1. **Error-aware Speedup Score (ESₜ)**  
   对每个子图 $i$ 定义带容错的速度提升得分：
   $$
   s_{t,i} =
   \begin{cases}
   s_i & \text{correct}_t \land s_i \geq 1 \\
   (p+1)^{\log s_i} & \text{correct}_t \land s_i < 1 \\
   b^{1(t < c_i)} & \text{otherwise}
   \end{cases}
   $$
   其中：
   - $s_i$: 实测速度提升
   - $\text{correct}_t$: 在容忍阈值 $t$ 下是否正确（数值误差、编译失败、运行错误）
   - $p, b \in (0,1)$: 惩罚系数（默认 $b=0.1$, $p=0$）

2. **Aggregated Speedup (AS)**
   - 将多个容忍度下的 ESₜ 加权几何平均：
     $$
     AS = \left( \prod_{t=-10}^{E+1} ES_t^{W_t} \right)^{1/\sum W_t}
     $$
   - 权重 $W_t$ 倾斜于严格正确性区间（$t \in [-5,-3]$），防止宽松容忍误导优化方向

3. 其他辅助指标：
   - `fast_1`: 正确且加速 ≥1.0 的比例
   - `Samp.CR`, `Sub.CR`: 样本/子图级正确率
   - `G-Mean Speedup`: 正确子图上的几何平均加速比

---

### 基线方法对比
| 模型类别 | 模型列表 |
|---------|--------|
| **Frontier Models** | GPT-5.4, Claude-Opus-4.6, Claude-Sonnet-4.6 |
| **Open-source Models** | GLM-5.1, MiniMax-M2.7, Qwen3-30B-A3B, Qwen3-4B |
| **Baseline Compilers** | Eager Execution, TorchInductor (`torch.compile`) |

所有实验均在 **NVIDIA A30 GPU** 上进行，使用 **PassAgent** 框架执行迭代优化（最多 50 步），每步获得 AS Score 反馈。

---

## 3. 主要实验结果和性能指标

### 关键性能数据（见 Table 1）

| Model | fast_1(%) | Sub.CR(%) | G-Mean Speedup | AS Score |
|-------|-----------|------------|------------------|----------|
| **Eager** | 100.0 | 100.0 | 1.000 | 1.000 |
| **Inductor** | 20.3 | 85.0 | 0.846 | 0.706 |
| **Claude-Sonnet-4.6** | 9.2 | 61.9 | 0.835 | **0.448** |
| **Claude-Opus-4.6** | 9.8 | 48.6 | **0.922** | 0.410 |
| **Qwen3-30B-A3B** | 0.6 | 11.8 | 0.693 | 0.139 |
| **Qwen3-30B-A3B-SFT** | 5.3 | 48.8 | 0.809 | **0.371** |

---

### 与基线方法的对比结果
1. **所有 LLM 均未超越 TorchInductor**
   - 最佳模型（Claude-Opus-4.6）G-Mean Speedup = 0.922 < 1.0，仍慢于 eager
   - AS Score 最高为 0.448，**比 Inductor 低 37%**

2. **但个体子图上可达 3× 加速**
   - 在某些长尾子图上，LLM 生成的 pass 达到 **3.02× 相对于 Inductor 的加速**
   - 表明 LLM **具备潜力**，但缺乏一致性（consistency）

3. **强判别力与未饱和性**
   - 不同模型间 AS Score 差距达 **3.22×**（Sonnet vs Qwen3-30B）
   - 表明 PassBench 是高度 discriminative 且 genuinely unsaturated 的 benchmark

---

### 消融实验结果
#### ✅ 微调显著提升性能（Distillation 实验）
- 使用 **Claude-Sonnet-4.6** 在 ~4.5K PassNet 轨迹上生成专家轨迹
- 对 **Qwen3-30B-A3B** 进行 SFT（监督微调）
- 结果：
  - AS Score 从 **0.139 → 0.371**（↑ **2.67×**）
  - Sub.CR 从 11.8% → 48.8%
- 表明 **PassNet-Dataset 具备高质量训练价值**

#### ✅ 多轮迭代至关重要
- 单次生成仅捕获最终性能的 **31%–51%**
- 多数成功案例需经历非单调探索路径（fail → pass → fail → pass）
- 说明需要 agent-style iterative refinement

---

## 4. 关键结论和发现

### 主要发现
1. **瓶颈不在能力，而在一致性（Consistency is the bottleneck）**
   - LLM 已能在特定长尾子图上实现高达 **3× 的加速**
   - 但整体性能远低于编译器，主因是 **可靠性差、泛化不稳定**

2. **Pass Generation 是更优抽象**
   - 相比 kernel generation，pass generation 更易于集成、验证和复用
   - 支持 pattern-matching + rewrite 的结构化编程范式

3. **PassBench 是有效且严格的 benchmark**
   - 高判别力（3.22× 模型差距）
   - 引入 **AST 检查、dispatch 拦截、逆序执行验证** 抵御作弊
   - 成功拦截 29%-50% 的 exploitation 尝试

4. **PassNet-Dataset 是有效的训练基础设施**
   - 仅用 ~4K 轨迹即可使小模型接近前沿模型水平
   - 验证了数据驱动优化的可行性

---

### 方法的局限性
1. **当前聚焦推理阶段单 GPU 场景**
   - 未覆盖训练 loop、multi-device、分布式优化
2. **领域偏向 CV/NLP（合计 90.6%）**
   - 对科学计算、生成模型等新兴领域覆盖不足
3. **硬件感知缺失**
   - LLM 缺乏对 register pressure、SRAM 容量等底层约束的理解
4. **反作弊机制无法保证完备性**
   - 新型对抗策略可能绕过当前防御

---

### 未来工作方向
1. **扩展至 multi-device 和 training-loop 优化**
2. **引入 hardware cost model 作为辅助 context**
3. **开展 RL from ES feedback 的强化学习训练**
4. **持续扩充 dataset 至更多领域（如物理模拟、基因组学）**
5. **构建多 agent collaboration 框架用于复杂 pass synthesis**

---

> 🌐 **项目已完全开源**：  
> GitHub 地址：[https://github.com/PaddlePaddle/PassNet](https://github.com/PaddlePaddle/PassNet)  
> 包含完整 dataset、benchmark、evaluation tooling 和 agent scaffold。

</details>

---

### 13. [Moment-KV: Momentum-Based Decode-Time KV Cache Compression for Long Generation](https://arxiv.org/abs/2605.29873)

**Authors**: Soumyadeep Jana, Sagar Nishad, Sanasam Ranbir Singh  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.29873v1  

#### Abstract
Key-Value (KV) cache remains a major bottleneck for deploying Large Language Models (LLMs) in long-generation tasks. Prior work often applies uniform compression across both prefill and decoding caches, but compressing the prefill cache degrades performance by corrupting critical context. While pres...

---

### 14. [Anchorless Diversification for Parallel LLM Ideation](https://arxiv.org/abs/2605.30150)

**Authors**: Fares Nabil Ibrahim, Nafis Saami Azad, Raiyan Abdul Baten  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 8.5  
**Type**: new  
**ArXiv ID**: 2605.30150v1  

#### Abstract
LLMs are increasingly used to generate candidate-idea pools for creative tasks where broad exploration is valuable. Parallel inference can be attractive in this setting when it broadens the pool while retaining quality and cost efficiency. We study inference-time controls for candidate-pool diversif...

<details>
<summary><strong>🤖 AI Summary (by qwen-long)</strong> - Click to expand</summary>

# **论文总结：Anchorless Diversification for Parallel LLM Ideation**

---

## **1. 论文的主要贡献和创新点**

### **解决的问题**
当前在使用 **Large Language Models (LLMs)** 进行创造性任务（如故事构思、产品概念生成、广告语设计）时，常采用 **parallel inference**（并行推理）来生成大量候选想法。然而，由于模型训练和偏好优化的偏差，多个生成结果容易集中在相似的语义区域（semantic basins），导致“看似多样实则重复”的现象，即 **idea diversity collapse**。

传统提升多样性的方法（如基于种子输出的反锚定 anti-anchoring、多智能体辩论等）虽然有效，但依赖于观察已生成样本、共享状态或迭代反馈，增加了推理成本和部署复杂度，削弱了并行生成的效率优势。

---

### **提出的新方法与新思路**
本文提出了两种 **anchorless**（无锚点）的推理时控制策略，无需依赖任何已生成的候选样本即可实现多样化：

1. **Population-referential divergent instruction（群体参照发散指令）**  
   在提示中加入：“*Try to make it stand out from other responses that might be generated for this same task.*”  
   即让模型在不看到实际输出池的情况下，利用其对“可能生成响应”的隐含认知，主动避开高概率区域。

2. **Semantic direction stratification（语义方向分层）**  
   - 先通过一次 **planning call**，让模型为任务提出 5 个互斥且广泛的语义方向（如“科技向”、“情感向”、“讽刺向”等）；
   - 然后将 150 个生成预算平均分配到这五个方向上，并行生成；
   - 每个方向有独立的生成约束指令，确保覆盖不同创意路径。

该方法受 SIMPLESTRAT 启发，但扩展至开放性创意任务，强调“广度探索”而非“恢复真实分布”。

---

### **相比现有方法的优势**
| 特性 | Anchorless 方法 | Anchored 方法（如 self/peer/repr） |
|------|------------------|-------------------------------|
| 是否需要种子输出 | ❌ 不需要 | ✅ 需要（两阶段） |
| 推理成本 | 低（单阶段 + 可选规划调用） | 高（需 seed + regenerate） |
| 并行友好性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 多样性表现 | 强（尤其 strat-diverge） | 强，但性价比下降 |
| 实际部署可行性 | 更高 | 较低（延迟、协调开销） |

> ✅ **核心优势**：在几乎不增加成本的前提下，达到甚至超越部分依赖样本的方法的多样性水平。

---

## **2. 核心实验方法和设置**

### **使用的模型与任务家族**
- **LLMs**: GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Pro
- **任务家族（Task Families）**：
  1. **Stories**（4个提示）：丛林冒险、跳伞失败、短篇恐怖故事、人生最后一秒
  2. **Alternative Uses Task (AUT)**（5个对象）：鞋、按钮、钥匙、铅笔、汽车轮胎
  3. **Slogans**（3个场景）：智能手机、汽水、献血活动

每项任务生成 **150 个候选输出**，共涵盖 12 种 prompt 条件。

---

### **实验设置与生成方法对比**
所有方法均交叉使用两种 **instruction strategies**：
- `neutral`: “Make the response novel and appropriate”
- `diverge`: 在前者基础上添加“stand out from other responses that might be generated”

#### **六种 generation methods 对比**：
| 编号 | 方法 | 类型 | 是否 anchorless |
|-----|------|--------|--------------|
| (i) | `indep` | 独立生成（baseline） | ✅ |
| (ii) | `strat` | 语义方向分层 | ✅ |
| (iii) | `repr` | 代表锚点避免（shared representative anti-anchoring） | ❌ |
| (iv) | `self` | 自我反锚定（self anti-anchoring） | ❌ |
| (v) | `peer1` | 成对同侪反锚定（dyadic peer） | ❌ |
| (vi) | `peer2` | 三人组同侪反锚定（triadic peer） | ❌ |

---

### **评估指标**

#### **多样性指标（Diversity Metrics）**
- `Dpair`: 平均成对语义距离（Mean pairwise semantic distance）
- `Dnn`: 最近邻距离（local redundancy）
- `Dmed`: 到中心点的距离（dispersion）
- `Dmst`: 最小生成树边长均值（global spread）
- `Dent`: 区域熵（normalized region entropy），衡量跨聚类分布均匀性

#### **质量代理（Quality Proxies）**
- **Stories**: MAoSS（自动评分叙事创造力）
- **AUT**: CLAUS（评估替代用途的创造性）
- **Slogans**: 
  - 主要：phrase-level non-template score（基于 n-gram 重用率）
  - 鲁棒性检验：LLM-as-a-judge（GPT-5.4 打分 1–5 分）

#### **其他分析手段**
- **Pool-size rarefaction**：分析多样性随采样数量增长的趋势
- **Full-pipeline token accounting**：计入完整推理链的 token 开销（包括 planning、seed generation、regeneration）
- **Token efficiency**：计算每 100k pipeline tokens 获得的多样性增益

---

## **3. 主要实验结果和性能指标**

### **关键性能数据汇总**

| 方法 | 相对于 `indep-neutral` 的 `Dpair` 提升（GPT-5.4） | Token multiplier (`R_tok`) | 每 100k tokens 的 `Dpair` 增益 |
|------|---------------------------------------------|-----------------------------|-------------------------------|
| `indep-diverge` | +0.04 | ~1.1 | 0.08 |
| `strat-diverge` | **+0.1717** | 1.61 | **0.295** ✅ |
| `peer2-diverge` | +0.1706 | 3.71 | 0.157 |

> 🔥 `strat-diverge` 在 **多样性-质量-效率权衡** 上表现最优。

---

### **与基线方法的对比结果**

#### **(1) `indep-diverge` 是强而廉价的 baseline**
- 所有三个模型上均显著提升 `Dpair`（Claude Sonnet 最高 +0.0622）
- 质量代理（Q₂）保持不变或略有提升
- 推理成本仅增加约 10%，是最低成本的有效干预

#### **(2) `strat-diverge` 实现最强多样性-效率平衡**
- 在 GPT-5.4 和 Gemini 上与最强 peer-anchor 方法（`peer2-diverge`）性能相当
- 在 **Claude Sonnet 上甚至超越所有 anchored 方法**（+0.2526 vs +0.2081）
- 尽管 `peer2-diverge` 总体 token 成本高达 3.7 倍，`strat-diverge` 仅为 1.6 倍
- 因此，在 **token-normalized 效率** 上全面领先

#### **(3) 锚定方法的优势在全链路成本下缩小**
- `repr`, `self`, `peer1`, `peer2` 在最终池多样性上有竞争力
- 但在计入 seed generation 和 regeneration 后，其 token 效率大幅下降
- 尤其是 `repr`（共享代表锚点）在区域熵（Dent）上不如 `strat`

---

### **消融实验与组合效果**

#### **(1) `diverge` 指令具有普适增益**
- 对 `indep`, `strat`, `self`, `peer1`, `peer2` 均带来正向 `Δdiv`（边际提升）
- 表明“群体参照”思维可泛化至多种生成机制

#### **(2) `strat + diverge` 组合最强**
- `strat-diverge` 是所有 anchorless 设置中的最佳配置
- 在 rarefaction 分析中：
  - 达到 `indep-neutral` 完整熵目标仅需 **7.4 个样本**
  - 显著快于 `indep-diverge`（17.9）和 `repr-diverge`（23.6）

#### **(3) Rarefaction 曲线分析**
- `Dpair` AUC：`strat-diverge` > `repr-diverge`（+0.088）
- `Dent` AUC：局部锚定方法略优（`peer1/peer2` ≈ 0.64），但 `strat-diverge` 仍达 0.61
- 表明 `strat` 几乎能匹配依赖具体样本的局部避让能力

---

## **4. 关键结论和发现**

### **主要发现**
1. ✅ **Population-referential instruction 是高效低成本 baseline**  
   仅靠一句“与其他可能生成的结果不同”，就能显著提升多样性而不牺牲质量。

2. ✅ **Semantic direction stratification 是强大的 anchorless 控制信号**  
   一次 planning call 即可组织大规模并行生成，实现接近或优于锚定方法的多样性。

3. ✅ **Anchorless 方法在 token-efficiency 上占优**  
   当考虑完整推理路径时，`strat-diverge` 提供了最佳的 **diversity-quality-compute frontier**。

4. ✅ **strat 与 diverge 可互补增强**  
   两者结合形成最强配置，且仍远低于再生类方法的成本。

5. ✅ **Anchored regeneration 仍有潜力，但性价比下降**  
   虽然 `peer2-diverge` 多样性极高，但高昂的 token 成本限制其实用性。

---

### **局限性（Limitations）**
1. **质量依赖自动代理指标**  
   MAoSS、CLAUS 和 slogan 模板分数虽经验证，但仍无法完全替代人类专家或用户评价。

2. **多样性基于 embedding 空间**  
   结果受 sentence embedding 模型（如 all-mpnet-base-v2）影响，可能存在表征偏差。

3. **任务范围有限**  
   仅测试三种创意任务，未涵盖更长文本、事实约束严格或多模态任务。

4. **固定设计参数**  
   如固定 5 个语义方向、均匀分配预算，未探索自适应分配或动态调整。

---

### **未来工作方向**
- 探索 **adaptive stratification**：根据方向潜力动态分配生成资源
- 构建 **hybrid pipelines**：结合 stratification 与 selective regeneration
- 引入 **human-in-the-loop feedback** 优化语义方向定义
- 扩展至 **multi-modal ideation**（图文联合生成）
- 研究 **long-form 内容的多样性演化过程**

---

> 📌 **一句话总结**：  
> 本文证明，无需依赖已生成样本，仅通过 **发散性指令** 和 **语义方向规划**，即可在极低额外成本下实现高质量、高多样性的并行 LLM 创意生成，为实用化 AI 创作系统提供了新的基准范式。

</details>

---

### 15. [Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling](https://arxiv.org/abs/2605.29262)

**Authors**: Shijie Cao, Yuan Yuan, Jing Liu  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29262v1  

#### Abstract
The Dynamic Flexible Job Shop Scheduling Problem (DFJSP) necessitates a trade-off between instant reaction to stochastic disturbances and global optimization of production goals. Conventional priority rules are insufficiently flexible to handle complex disruptions, whereas learning-based approaches ...

---

### 16. [Revisiting Observation Reduction for Web Agents: Comprehensive Evaluation with a Lightweight Framework](https://arxiv.org/abs/2605.29397)

**Authors**: Masafumi Enomoto, Ryoma Obara, Haochen Zhang, Masafumi Oyamada  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29397v1  

#### Abstract
HTML observations in LLM-based web agents are extremely long, and while many reduction methods have been proposed, it remains unclear which methods reduce overall agent latency while maintaining performance. The main obstacle is the high cost of end-to-end evaluation: in our experiments, evaluating ...

---

### 17. [LiteCoder-Terminal: Scaling Long-Horizon Terminal Environments for Learning Language Agents](https://arxiv.org/abs/2605.29559)

**Authors**: Xiaoxuan Peng, Kaiqi Zhang, Xinyu Lu, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29559v1  

#### Abstract
Mastering terminal environments requires language agents capable of multi-step planning, feedback-grounded execution, and dynamic state adaptation. However, training such agents is currently bottlenecked by a reliance on scraped external repositories, which limits domain diversity, environment contr...

---

### 18. [Bridging Chemists and AI: An Expert-Augmented Framework for Interpretable Route Evaluation](https://arxiv.org/abs/2605.29108)

**Authors**: Yujia Guo, Mikhail Kabeshov, Tat Hong Duong Le, Samuel Genheden, Marco V. Mijangos, Varvara Voinarvoska, Giulia Bergonzini, Ola Engkvist, Samuel Kaski  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29108v1  

#### Abstract
Selecting efficient multi-step synthetic routes is a central challenge in organic synthesis, particularly in medicinal and process chemistry, where route choice directly impacts feasibility, cost, and development efficiency. Data-driven assessment systems often oversimplify the multi-objective natur...

---

### 19. [Solving Integer Linear Programming with Parallel Tempering](https://arxiv.org/abs/2605.29366)

**Authors**: Kyuil Sim, Sanghyeok Choi, Jinkyoo Park  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29366v1  

#### Abstract
Integer Linear Programming (ILP) serves as a versatile framework for modeling a wide range of combinatorial optimization problems, typically addressed by sophisticated exact solvers or heuristics. While learning-based approaches have recently shown their effectiveness, they suffer from poor generali...

---

### 20. [Bastion: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](https://arxiv.org/abs/2605.29727)

**Authors**: Soowon Oh, Nam Cao, Yujin Kim, Hojung Jung, Huzama Ahmad, Sangmin Bae, Se-Young Yun  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.29727v1  

#### Abstract
Block-diffusion drafters have recently emerged as a powerful alternative for speculative decoding by predicting multiple future-token distributions in a single parallel step. However, since these parallel predictions are sampled from position-wise marginals rather than fully conditioned sequences, c...

---

### 21. [Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching](https://arxiv.org/abs/2605.30337)

**Authors**: Alaa Khamis, Alaa Maalouf  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 8.0  
**Type**: new  
**ArXiv ID**: 2605.30337v1  

#### Abstract
Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making ea...

---

### 22. [Battery-Sim-Agent: Leveraging LLM-Agent for Inverse Battery Parameter Estimation](https://arxiv.org/abs/2605.29560)

**Authors**: Jiawei Chen, Xiaofan Gui, Shikai Fang, Shengyu Tao, Shun Zheng, Weiqing Liu, Jiang Bian  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29560v1  

#### Abstract
Parameterizing high-fidelity "digital twins" of batteries is a critical yet challenging inverse problem that hinders the pace of battery innovation. Prevailing methods formulate this as a black-box optimization (BBO) task, employing algorithms that are sample-inefficient and blind to the underlying ...

---

### 23. [DeepTool: Scaling Interleaved Deliberation in Tool-Integrated Reasoning via Process-Supervised Reinforcement Learning](https://arxiv.org/abs/2605.29568)

**Authors**: Yang He, Xiao Ding, Bibo Cai, Yufei Zhang, Kai Xiong, Zhouhao Sun, Bing Qin, Ting Liu  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29568v1  

#### Abstract
Tool-Integrated Reasoning (TIR) extends LLM capabilities by leveraging external environments. However, existing methods lack the deliberation during sequential tool invocation required for strategic planning and self-correction. While RL mitigates this, conventional approaches for Tool-Integrated Re...

---

### 24. [LFQ: Logit-aware Final-block Quantization for Boosting the Generation Quality of Low-Bit Quantized LLMs](https://arxiv.org/abs/2605.29756)

**Authors**: Jung Hyun Lee, June Yong Yang, Jungwook Choi, Eunho Yang  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29756v1  

#### Abstract
As large language models continue to scale, low-bit weight-only post-training quantization (PTQ) offers a practical solution to their memory-efficient deployment. Although block-wise PTQ is capable of matching the full-precision (FP) baseline on basic language modeling and understanding, its quality...

---

### 25. [AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security](https://arxiv.org/abs/2605.29801)

**Authors**: Dongrui Liu, Yu Li, Zhonghao Yang, Peng Wang, Guanxu Chen, Yuejin Xie, Qinghua Mao, Wanying Qu, Yanxu Zhu, Tianyi Zhou, Leitao Yuan, Zhijie Zheng, Qihao Lin, Yimin Wang, Haoyu Luo, Shuai Shao, Chen Qian, Qingyu Liu, Ling Tang, Ruiyang Qin, Qihan Ren, Junxiao Yang, Kun Wang, Zhiheng Xi, Linfeng Zhang, Ranjie Duan, Bo Zhang, Wenjie Wang, Wen Shen, Qiaosheng Zhang, Yan Teng, Chaochao Lu, Rui Mei, Man Li, Jialing Tao, Xi Lin, Tianhang Zheng, Yong Liu, Quanshi Zhang, Lei Zhu, Xingjun Ma, Junhua Liu, Hui Xue, Xiaoxiang Zuo, Xiangnan He, Chao Shen, Xianglong Liu, Minlie Huang, Jing Shao, Xia Hu  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29801v1  

#### Abstract
Modern open-world agents such as OpenClaw exhibit powerful cross-environment execution capabilities yet introduce broad new safety risk sources. Meanwhile, advanced frontier AI models drastically lower attack barriers, rendering current agent alignment frameworks inadequate for real-world deployment...

---

### 26. [Toward AI Systems That Understand Self and Others: A Multi-Phase Inference Framework for Human Cognitive Diversity and World-Model Alignment](https://arxiv.org/abs/2605.29930)

**Authors**: Toru Takahashi  
**Category**: cs.AI  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29930v1  

#### Abstract
Mutual misunderstanding in contemporary society does not arise merely because people hold different opinions or values. Even under the same observations, different subjects may form different inferential targets, state representations, prediction errors, and update priorities. This paper proposes a ...

---

### 27. [From Context Shift to Stylistic Collapse: Why Training Objectives Matter More Than Scale](https://arxiv.org/abs/2605.28826)

**Authors**: Rohan Mahapatra  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.28826v1  

#### Abstract
In modern LLMs, linguistic features function not as stylistic artifacts but as probes of probability mass, allocated under training alignment objectives. Language models trained with contemporary pipelines exhibit severe reshaping of linguistic features, leading to extreme language re-distribution. ...

---

### 28. [Reasoning-preserved Efficient Distillation of Large Language Models via Activation-aware Initialization](https://arxiv.org/abs/2605.29327)

**Authors**: Junlin He, Yihong Tang, Tong Nie, Guilong Li, Binyu Yang, Jinxiao Du, Lijun Sun, Wei Ma  
**Category**: cs.CL  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29327v1  

#### Abstract
Efficient Distillation (EDistill) compresses large language models (LLMs) by structured pruning parameters and tuning lightweight modules with high training efficiency. Although these EDistilled LLMs achieve state-of-the-art (SOTA) performance on general ability benchmarks relative to similarly size...

---

### 29. [PRISM: Processing-In-Memory Sparse MTTKRP for Tensor Decomposition Acceleration](https://arxiv.org/abs/2605.29728)

**Authors**: Daniel Pacheco, Leonel Sousa, Aleksandar Ilic  
**Category**: cs.DC  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29728v1  

#### Abstract
Sparse tensors are the most used representation of sparse multidimensional data. Operations that decompose them, selecting their most important features while reducing their dimension, have become prevalent procedures in machine learning. One of the most used tensor decomposition algorithms is the A...

---

### 30. [Robust Frequency-Calibrated Virtual EEG Channel Generation from Four Frontal Electrodes for Wearable EEG Augmentation](https://arxiv.org/abs/2605.29263)

**Authors**: Minghao Xiao  
**Category**: cs.LG  
**Published**: 2026-05-29  
**Score**: 7.5  
**Type**: new  
**ArXiv ID**: 2605.29263v1  

#### Abstract
Low-channel wearable electroencephalography (EEG) is attractive for long-term monitoring, but four frontal electrodes provide only a sparse and spatially biased view of distributed scalp activity. We present FAVC-Net, a compact frequency-calibrated virtual-channel network that generates 13 unmeasure...

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
