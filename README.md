# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-09-22 10:19:42 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [Analytical Power-Aware Provisioning for Prefill-Decode Disaggregated AI Inference](https://arxiv.org/abs/2609.24639v1)

**Authors**: Mingyuan Yan, Haiyu Wang, Linxuan Biao, H. Jonathan Chao, Sai Qian Zhang, Wenqi Cui  
**Category**: cs.DC  
**Published**: 2026-09-22  
**Score**: 119.0  
**Type**: new  
**ArXiv ID**: 2609.24639v1  

#### Abstract
Power availability increasingly constrains the operation of AI inference fleets, creating a need for provisioning methods that jointly consider serving capacity and power consumption. Prefill--decode (PD) disaggregation has emerged as a prevalent architecture for large-scale inference serving. Howev...

---

### 2. [SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816v1)

**Authors**: Aditya Anirudh Jonnalagadda, Agasthi Haputhanthri, Pranav Dangi, Rohan Juneja, Wenshuo Yue, Aritra Bagchi, Bin Gao, Tulika Mitra  
**Category**: cs.AR  
**Published**: 2026-09-22  
**Score**: 92.0  
**Type**: new  
**ArXiv ID**: 2609.23816v1  

#### Abstract
The key-value (KV) cache has become the dominant consumer of memory in large language model (LLM) serving systems as context lengths, concurrency, and request lifetimes grow. High-bandwidth memory (HBM) provides the bandwidth attention decode needs but limited capacity, while off-package memory and ...

---

### 3. [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://arxiv.org/abs/2609.24197v1)

**Authors**: Weifan Jiang, Krishna Teja Chitty-Venkata, Megan Flynn, Reed Meyerson, Zhenting Qi, Tianyu Wu, Eldar Kurtic, Minlan Yu, Alexandre Marques  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 86.5  
**Type**: new  
**ArXiv ID**: 2609.24197v1  

#### Abstract
Speculative decoding losslessly accelerates large language model inference by having a lightweight draft model predict future tokens for verification by the target model. Recent block diffusion drafters further reduce drafting latency by predicting multiple tokens in parallel. However, existing bloc...

---

### 4. [GDN Tree-Scan: Served Tree Verification for Recurrent-Hybrid Language Models](https://arxiv.org/abs/2609.23900v1)

**Authors**: Zhiyuan Ma  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 78.0  
**Type**: new  
**ArXiv ID**: 2609.23900v1  

#### Abstract
Tree speculative decoding verifies multiple candidate continuations in one target forward pass. For attention-only transformers, the verifier mainly needs an ancestry mask. Recurrent-hybrid language models break this assumption: a candidate row must also carry the recurrent state that native sequent...

---

### 5. [Seeing Through Conflicts: Improving Instruction Hierarchy Alignment in Vision-Language Models](https://arxiv.org/abs/2609.22234v1)

**Authors**: Nicholas Sansoterra, Zishuo Zheng, Sachin Kumar  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 67.5  
**Type**: new  
**ArXiv ID**: 2609.22234v1  

#### Abstract
Instruction hierarchy (IH) alignment teaches language models to prioritize higher-level instructions when inputs conflict. While studied primarily in text-only settings, vision-language models (VLMs) introduce new challenges for IH: instructions may be embedded in images, split across modalities, vi...

---

### 6. [Cost-Aware Reinforcement Learning with Action Masking and Projection for Battery Energy Storage Dispatch under Suppressed-Spread Market Shifts](https://arxiv.org/abs/2609.23590v1)

**Authors**: Kuanlin Chen, Chen-Wei Kuo, Cheng-En Ou  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 62.0  
**Type**: new  
**ArXiv ID**: 2609.23590v1  

#### Abstract
Battery energy storage system (BESS) dispatch must preserve operational feasibility while declining price spreads reduce the margin available to pay for cycling. We study a proximal policy optimization (PPO) controller whose pre-selection physical action mask and emergency projection are separated f...

---

### 7. [RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models](https://arxiv.org/abs/2609.20971v1)

**Authors**: Chuxu Song, Jiuqi Wei, Zhencan Peng  
**Category**: cs.AI  
**Published**: 2026-09-22  
**Score**: 59.0  
**Type**: new  
**ArXiv ID**: 2609.20971v1  

#### Abstract
Long-context large language model inference is increasingly limited by prefill, where dense self-attention processes the entire prompt before generation begins. Sparse block selection can reduce this cost, but a block centroid may hide a highly relevant token among many irrelevant ones. We call this...

---

### 8. [Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference](https://arxiv.org/abs/2609.24698v1)

**Authors**: Changxu Liu, Zhaogeng Li  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 58.5  
**Type**: new  
**ArXiv ID**: 2609.24698v1  

#### Abstract
Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverag...

---

### 9. [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1)

**Authors**: Fanchao Chen, Ziheng Jiang, Ziyun Wei, Zheng Zhong, Du Li, Chi Zhang, Haibin Lin, Shivaram Venkataraman  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 57.5  
**Type**: new  
**ArXiv ID**: 2609.22870v1  

#### Abstract
Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs). Although FP8 quantization can accelerate RL training, maintaining stability throughout an FP8 RL pipeline remains challenging. While previous works have focused o...

---

### 10. [Balancing Reasoning and Hardware Constraints in RAG Pipelines for Ukrainian Multi-Domain Document Understanding](https://arxiv.org/abs/2609.22124v1)

**Authors**: Illya Havrylov  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 56.0  
**Type**: new  
**ArXiv ID**: 2609.22124v1  

#### Abstract
This paper describes the system submitted to the UNLP 2026 Shared Task on Multi-Domain Document Understanding. The challenge required extracting precise answers, document IDs, and page numbers from a diverse corpus of Ukrainian PDF documents within a strict 9-hour offline Kaggle execution limit. Dur...

---

### 11. [Accurate Simulation of Distributed Training Jobs with Network Contention Modeling](https://arxiv.org/abs/2609.23278v1)

**Authors**: Yeonho Yoo, Hyunho Lee, Hyunmok Choi, Chuck Yoo, Gyeongsik Yang  
**Category**: cs.DC  
**Published**: 2026-09-22  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.23278v1  

#### Abstract
Trace-driven simulation is widely used to evaluate distributed training (DT) jobs in GPU clusters, but existing simulators either ignore network contention or approximate it with a fixed penalty. This misses how scheduling decisions determine which jobs share server network interfaces and inter-serv...

---

### 12. [Acceptance-Aware Draft Model Training for Speculative Decoding](https://arxiv.org/abs/2609.24150v1)

**Authors**: Tianhua Xia, Mugilan Ganesan, Yifei Feng, Haiyu Wang, Maximilian Egger, Sai Qian Zhang  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 55.0  
**Type**: new  
**ArXiv ID**: 2609.24150v1  

#### Abstract
Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that are verified by the target model in a single forward pass. Its speedup is largely determined by the acceptance length, yet existing draft-model training...

---

### 13. [Low resource cross-modal alignment using HGNN to enhance speech representation](https://arxiv.org/abs/2609.23191v1)

**Authors**: Yannick Yomie Nzeuhang, Marie Tahon, Paulin Melatagia Yonta  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.23191v1  

#### Abstract
Speech-text space alignment is a multimodal representation learning method consisting to map different speech and text into a shared representation space, leading to enrichment of the representation of each modality. Proposed architectures, such as SAMU-XLSR, typically follow a student/teacher frame...

---

### 14. [Leveraging Inference-Time Compute for Diffusion Models via Global Scheduling of Denoising Trajectories](https://arxiv.org/abs/2609.22867v1)

**Authors**: Yuan Cao, Yifu Tang, Hangqi Li, Zeyu Zheng  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 53.5  
**Type**: new  
**ArXiv ID**: 2609.22867v1  

#### Abstract
Diffusion models generate a sample by traversing a denoising trajectory, a sequence of stochastic noise-reduction steps that transforms pure noise into a draw from a target distribution. At deployment time, additional computation can improve sample quality without retraining: at each step, the sampl...

---

### 15. [COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.22697v1)

**Authors**: Weizhen Bian, Sitong Cheng, Rongxiu Zhong, Jiahao Pan, Liumeng Xue, Boyi Kang, Shilei Zhang, Jinglei Liu, Yue Wang, Junlan Feng, Bei Liu, Wei Xue  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 53.0  
**Type**: new  
**ArXiv ID**: 2609.22697v1  

#### Abstract
Recently, text-to-speech systems have made significant progress in speech expressiveness and controllability. However, the speaking style of generated speech typically relies on clear user-specified instructions. In natural conversations, speaking style should be naturally inferred from the precedin...

---

### 16. [TARGet: Topology-Aware Fusion-based Radio Frequency Circuit Functional Modeling using Graph Neural Networks](https://arxiv.org/abs/2609.22165v1)

**Authors**: Soroosh Noorzad, Sebastian Bodero, Morteza Fayazi  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2609.22165v1  

#### Abstract
Automatic synthesis of analog and Radio Frequency (RF) circuits is an emerging area that requires an efficient circuit modeling method. In recent years, Machine Learning (ML) solutions have played a promising role in this regard. However, many existing ML approaches require separate training data fo...

---

### 17. [KerColle: Unlocking Fine-Grained GPU Concurrency in Vision-Language-Action Models](https://arxiv.org/abs/2609.22335v1)

**Authors**: Anna Li, Christina Giannoula, Nandita Vijaykumar  
**Category**: cs.AR  
**Published**: 2026-09-22  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2609.22335v1  

#### Abstract
Vision-Language-Action (VLA) models have emerged as foundational models for next-generation robotics. High VLA inference throughput is critical for meeting the control-rate requirements of robots. VLA models comprise two phases, a vision-language model (VLM) and an action head, that can be decoupled...

---

### 18. [Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering](https://arxiv.org/abs/2609.24202v1)

**Authors**: Jingkun Liu, Yue Song  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2609.24202v1  

#### Abstract
Sparse attention reduces the quadratic cost of global self-attention while retaining strong empirical performance, but how its restricted interactions shape the evolution of token representations remains theoretically underexplored. Modeling tokens as particles on the unit sphere, we introduce opini...

---

### 19. [Assessing Adversarial Robustness of Latent Reasoning Models](https://arxiv.org/abs/2609.22228v1)

**Authors**: Shaolong Chen, Ang Li, Mingjie Li, Yisen Wang  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.22228v1  

#### Abstract
Large language models increasingly rely on long chain-of-thought (CoT) trajectories for complex reasoning, but autoregressive generation brings substantial memory and inference costs. Latent reasoning models (LRMs) offer a more efficient alternative by compressing intermediate reasoning into a small...

---

### 20. [StepKV: Step-Aware KV Cache Compression for LLM Agents](https://arxiv.org/abs/2609.22158v1)

**Authors**: Boyu Feng, Jiahong Liu, Yifan Li, Wenhao Yu, Zexuan Qiu, Yuliang Sun, Ming Shen, Xiang Li, Quanyu Dai, Irwin King  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.22158v1  

#### Abstract
Key-value (KV) caching is essential for efficient autoregressive large language model (LLM) inference, but the cache grows linearly with context length, increasing storage and decoding costs. KV cache compression mitigates this cost by retaining only a subset of cached tokens. This challenge is part...

---

### 21. [Comparing Latent Concept Formation in State Space Models and Transformers via Sparse Autoencoders](https://arxiv.org/abs/2609.24440v1)

**Authors**: Rithin Nagaraj, Rupa Laalasa Oruganti, Prerna Subhashchandra Kunder, Ashwini M Joshi  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.24440v1  

#### Abstract
The quadratic scaling of Transformer self-attention has driven the adoption of sub-quadratic Selective State Space Models (SSMs) like Mamba, which compress past context into a fixed-size recurrent hidden state. This strict informational bottleneck raises a foundational question for mechanistic inter...

---

### 22. [TreeSpark: Calibrated, Load-Adaptive Draft Trees for Semi-Autoregressive Speculative Decoding](https://arxiv.org/abs/2609.22098v1)

**Authors**: Huapeng Zhou, Huayu Wang, Xinyu Wang  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 44.5  
**Type**: new  
**ArXiv ID**: 2609.22098v1  

#### Abstract
Speculative decoding accelerates language-model inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Recent block drafters make drafting nearly free: a single backbone pass emits an entire block of draft tokens. Draft trees promise a further gain -- several...

---

### 23. [ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs](https://arxiv.org/abs/2609.23314v1)

**Authors**: Junyoung Park, Jungwook Choi, Mingu Lee  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2609.23314v1  

#### Abstract
Modern LLMs with QK-normalization, gated attention, learned attention sinks, or logit softcapping exhibit weaker persistent attention sinks, on which existing KV cache eviction methods primarily rely. We observe that across these models, weaker sinks co-occur with greater value-vector dispersion rel...

---

### 24. [Summarize, Judge, Refine: Decoupled Content Understanding and Policy Learning for Multimodal Content Moderation](https://arxiv.org/abs/2609.22094v1)

**Authors**: Zeeshan Ahmed, Yang Qin, Hanqing Huang  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.22094v1  

#### Abstract
Content moderation systems traditionally entangle multimodal understanding with policy-specific classification, requiring full pipeline retraining for every policy change and suffering from label scarcity since multimedia cannot be meaningfully augmented. We propose Summarize-Judge-Refine (SJR), a t...

---

### 25. [Offline Multimodal Large Language Models for Decision Support in Air Operations](https://arxiv.org/abs/2609.21390v1)

**Authors**: Joao P. A. Dantas, Jelton A. Cunha, Gabriel Dietzsch  
**Category**: cs.AI  
**Published**: 2026-09-22  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.21390v1  

#### Abstract
Air operations rely on complex rules, established procedures, and time-critical analysis under limited connectivity and strict security constraints. In such environments, analysts must combine written doctrine with images, often without access to external computing resources. This paper studies offl...

---

### 26. [Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache](https://arxiv.org/abs/2609.24635v1)

**Authors**: Lingfeng Wu, Behzad Shomali  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.24635v1  

#### Abstract
When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent st...

---

### 27. [Lifted Bellman Linear Programming for Offline Reinforcement Learning](https://arxiv.org/abs/2609.24489v1)

**Authors**: Hyukjun Yang, Jongchan Park, Narim Jeong, Donghwan Lee  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.24489v1  

#### Abstract
Offline reinforcement learning (RL) typically trains a critic by minimizing a regression loss against bootstrapped value targets stabilized by target networks with exponential moving average (EMA) updates. Multi-step targets incorporate behavior-policy actions and therefore require off-policy correc...

---

### 28. [Driving on Registers, Reasoning on Risk: Risk-Aware Occupancy for Register-Based End-to-End Autonomous Driving](https://arxiv.org/abs/2609.21486v1)

**Authors**: Jiaxing Chen, Hengduo Zou, YuKai Qin, Yiren Zhao, Lidong Yu, Bolin Gao  
**Category**: cs.AI  
**Published**: 2026-09-22  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.21486v1  

#### Abstract
Multimodal trajectory prediction improves behavioral coverage in end-to-end autonomous driving, but existing methods remain limited by sparse scene representations. Incomplete evidence leads to low-quality candidate generation and unreliable ranking among geometrically similar trajectories. On a reg...

---

### 29. [On the Efficiency-Safety Dilemma in Large Reasoning Models](https://arxiv.org/abs/2609.23587v1)

**Authors**: Yifei Yang, Zouying Cao, Xingrui Wang, Xiao Zhou, Yuexian Li, Dongjie Yang, Hai Zhao  
**Category**: cs.CL  
**Published**: 2026-09-22  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.23587v1  

#### Abstract
Large reasoning models (LRMs) incur high inference costs, often mitigated by efficiency techniques like quantization and pruning. However, the impact of these techniques on model adversarial robustness remains largely unexplored. This study provides the first comprehensive analysis of the interplay ...

---

### 30. [A Pinch of SFT, A Dash of RL: When Reinforcement Learning Helps Long-Horizon Advertising Agents](https://arxiv.org/abs/2609.22194v1)

**Authors**: Aakash Kolekar, Sahika Genc, Bunyamin Sisman, Shahriar Shariat, Shree Vandana Kachroo, Avishek Saha, Qianli Wu, Ari Singer, Benoit Dumoulin  
**Category**: cs.LG  
**Published**: 2026-09-22  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.22194v1  

#### Abstract
Enterprise analytics agents solve long-horizon tool-use problems over distributed business data, requiring retrieval, reasoning, API calls, code execution, and adaptation to intermediate observations. Supervised fine-tuning (SFT) calibrates tool syntax and teacher-supported behavior, whereas reinfor...

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
