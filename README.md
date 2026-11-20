# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-11-20 14:54:26 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [BOS Summary: The First Token Matters](https://arxiv.org/abs/2611.23508v1)

**Authors**: Hui Zhu, Saleh Zare Zade, Rafi Ibn Sultan, Deng Pan, Arun Ross, Dongxiao Zhu  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2611.23508v1  

#### Abstract
Large vision-language models (LVLMs) and language models (LLMs) often exhibit attention sinks, whereby particular positions, such as the beginning-of-sequence (BOS) token, receive a disproportionate share of attention. Under standard causal masking, however, the BOS query attends only to itself, so ...

---

### 2. [TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents](https://arxiv.org/abs/2611.25112v1)

**Authors**: Shashwat Jaiswal, Chloe Alverti, Mengmei Ye, Chen Wang, Hubertus Franke, Fan Lai, Tianyin Xu, Josep Torrellas  
**Category**: cs.DC  
**Published**: 2026-11-20  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2611.25112v1  

#### Abstract
LLM agents alternate between inference and tool execution, repeatedly reusing their growing context across calls. Under high concurrency, their combined key-value (KV) cache working set can reach hundreds of GiB, far exceeding GPU memory capacity. As idle KV cache blocks are evicted to slower storag...

---

### 3. [DS3M: Deep structured state space models for nonlinear system identification on modern hardware](https://arxiv.org/abs/2611.25274v1)

**Authors**: Marco Roschkowski, Hannes Gernandt  
**Category**: cs.LG  
**Published**: 2026-11-20  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2611.25274v1  

#### Abstract
Neural state-space identification learns dynamical models from measured inputs and outputs. SUBNET combines this task with an encoder that estimates initial states from short measurement histories. Its continuous-time version requires many successive neural-network evaluations during numerical integ...

---

### 4. [Global Importance Estimation for KV Cache Eviction](https://arxiv.org/abs/2611.24969v1)

**Authors**: Seojin Kim, Noseong Park  
**Category**: cs.CL  
**Published**: 2026-11-20  
**Score**: 46.5  
**Type**: new  
**ArXiv ID**: 2611.24969v1  

#### Abstract
Memory consumption of the key-value (KV) cache remains a central bottleneck for long-context LLM inference. We introduce PRKV, a training-free KV eviction method that estimates multi-hop global token importance by applying Personalized PageRank over attention-induced transition graphs. This enables ...

---

### 5. [Twindex: Index Cache Offloading with Coarse-to-Fine Selection for Long-Context Sparse-Attention Serving](https://arxiv.org/abs/2611.25078v1)

**Authors**: Yuxuan Xia, Jiakun Fan, Han Meng, Hao Mark Chen, Shenji Wan, Dongsheng Yang  
**Category**: cs.DC  
**Published**: 2026-11-20  
**Score**: 46.0  
**Type**: new  
**ArXiv ID**: 2611.25078v1  

#### Abstract
In long-context decoding, GPU memory (HBM) caps how many requests a GPU decodes at once. Sparse-attention models such as Qwen3.8-Flash-Next, DeepSeek V4.1-Flash and GLM-5.2 add an indexer: at every step it scores all past index entries with its own indexer cache, and attention reads the main KV of o...

---

### 6. [Vector Field Transforms: Structured Hyperdimensional Memory for Spatio-Temporal Reasoning](https://arxiv.org/abs/2611.24962v1)

**Authors**: William Youngwoo Chung, Andrew Ding, Hansen Jin Lillemark, Mohsen Imani  
**Category**: cs.AR  
**Published**: 2026-11-20  
**Score**: 44.0  
**Type**: new  
**ArXiv ID**: 2611.24962v1  

#### Abstract
Vector Symbolic Architectures (VSAs) are attractive for edge intelligence because their fixed-width distributed representations and simple algebraic operations map naturally to low-power vector hardware. However, conventional VSA memory superposes information, such as object, position, and time, int...

---

### 7. [Continual Tool-Space Extension Learning for Multimodal Agents](https://arxiv.org/abs/2611.23810v1)

**Authors**: Jinbae Seo, Jungin Park, Hyunsung Jang, Namkoo Ha, Jiyoung Lee, Kwanghoon Sohn  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2611.23810v1  

#### Abstract
Multimodal agents largely rely on generic tools such as cropping, search, and code execution, leaving specialist vision models outside their tool space. However, bringing such a model into an already trained agent is not straightforward. The challenge is to learn each new tool efficiently while reta...

---

### 8. [From Points to Trajectories: Rethinking Multimodal Alignment for Physical Events](https://arxiv.org/abs/2611.24249v1)

**Authors**: Yiyang Zhu, Guangyuan Liu, Jingdi Lei, Li Wei, Chau Yuen  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2611.24249v1  

#### Abstract
Advancing physical artificial intelligence (Physical AI) requires moving beyond static object recognition to ground how real-world mechanics (e.g., impact, friction, and force transfer) unfold over time. While multimodal aligners seek to capture these interactions by matching multi-sensor streams, p...

---

### 9. [Risk-Controlled Correction for Frozen Multimodal Models under Missing Modalities](https://arxiv.org/abs/2611.23886v1)

**Authors**: Hoang Pham Cong, Long D. Nguyen, Ho Viet Duc Luong, Nguyen Tran Minh Nhat, Binh P. Nguyen, Huynh Thi Thanh Binh  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2611.23886v1  

#### Abstract
A deployed multimodal predictor may face missing modalities after its weights can no longer be changed. This raises a question that training-time repair does not answer: what part of the resulting error is still correctable from the information that remains? We show that this part is characterized b...

---

### 10. [Cross-Question Reliable Reinforcement Learning](https://arxiv.org/abs/2611.25292v1)

**Authors**: Hector G. Rodriguez, Marcus Rohrbach  
**Category**: cs.LG  
**Published**: 2026-11-20  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.25292v1  

#### Abstract
AI systems operating near the limits of their capabilities can maximize utility while minimizing the risk of error by abstaining or deferring questions they are not confident about to a human or a stronger model. Recently, large language models (LLMs) have been post-trained to estimate confidence in...

---

### 11. [GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits](https://arxiv.org/abs/2611.24619v1)

**Authors**: Firas Spanioli, Yaniv David  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 37.5  
**Type**: new  
**ArXiv ID**: 2611.24619v1  

#### Abstract
As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpretability, and computat...

---

### 12. [Vanguard: Knowing When to Trust the Draft in Speculative Vision-Language Agents](https://arxiv.org/abs/2611.23917v1)

**Authors**: Hanqi Mao, Jiajun Fan, Ruihan Guo, Shuaike Shen, Ziwen Wang, Hui Ren, Xianrui Zhong, Ge Liu  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2611.23917v1  

#### Abstract
Vision-language agents that browse websites, operate phones and act in homes reason before every action, so every step waits for a large model, a latency and cost that stand in the way of deployment. Step-level speculation lets a small model draft each step and calls the large model only on rejected...

---

### 13. [Native FPGA Hard-Block Implementation from High-Level Synthesis](https://arxiv.org/abs/2611.25281v1)

**Authors**: Mohamed Bouaziz, Mahmoud A. Elshenawy, Krishnan B. Iyer, Abdurauf Abdurakhmanov, Ammar M. Seliaman, Suhaib A. Fahmy  
**Category**: cs.AR  
**Published**: 2026-11-20  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2611.25281v1  

#### Abstract
High-level synthesis (HLS) maps computations to FPGA hard blocks, yet often leaves their arithmetic modes, internal registers, and cascade links idle and recreates them in the fabric, costing area and timing. We present a C++ template library that reaches native hard-block implementations without mo...

---

### 14. [Modeling LLM Reasoning Dynamics with Structural Representations](https://arxiv.org/abs/2611.23749v1)

**Authors**: Ilia Karpov, Andrey Atamanyuk, Dmitry Ilvovsky, Aleksandr Anokhin, Alex Elizov, Dmitry Zagorulkin, Sergei O. Kuznetsov  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.23749v1  

#### Abstract
Language-model reasoning alternates between sustained activities and local operations. We study how this temporal structure predicts continuation and the computation needed to analyze it. T/E/S combines text, local events, and spans of activity. Across reasoning and information-seeking tasks, events...

---

### 15. [NaviGATE: Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning](https://arxiv.org/abs/2611.24552v1)

**Authors**: Jie Peng, Yongxue Shan, Yongfu Zha, Cui Miao, Xiaodong Wang  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 32.5  
**Type**: new  
**ArXiv ID**: 2611.24552v1  

#### Abstract
Multimodal knowledge graph reasoning (MKGR) aims to infer missing facts by jointly exploiting relational structures, textual descriptions, and visual evidence. Existing embedding-based methods effectively capture graph topology, but their fixed multimodal representations are less effective for query...

---

### 16. [Evidence-Based Credit Assignment for Search-Augmented Language Models](https://arxiv.org/abs/2611.23824v1)

**Authors**: Wen Wang, Jindong Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Junwei He, Wenkui Fan  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2611.23824v1  

#### Abstract
Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. T...

---

### 17. [Temporal Extrapolation of Elastic Seismic Wave Propagation in Layered Media Using Neural Operators](https://arxiv.org/abs/2611.25130v1)

**Authors**: Dibyajyoti Nayak, Yuze Pu, Kami Mohammadi, Somdatta Goswami  
**Category**: cs.LG  
**Published**: 2026-11-20  
**Score**: 31.0  
**Type**: new  
**ArXiv ID**: 2611.25130v1  

#### Abstract
Temporal prediction of seismic velocity fields beyond the time interval represented in training remains challenging for neural operator models. This study develops a coupled neural operator framework for stress-conditioned temporal prediction in layered elastic media. A time-integrator-embedded Deep...

---

### 18. [Berth: SLO-Preserving GPU Sharing Without New Preemption](https://arxiv.org/abs/2611.25091v1)

**Authors**: Mohammadali Khodabandehlou, Mahdi Alizadeh, Lei Gao, Murali Annavaram, Bhaskar Krishnamachari  
**Category**: cs.DC  
**Published**: 2026-11-20  
**Score**: 26.0  
**Type**: new  
**ArXiv ID**: 2611.25091v1  

#### Abstract
Inference services keep GPUs reserved for their worst-case load, and most of that capacity sits idle. Filling it with best-effort work such as training is the obvious remedy, and latency is why it rarely happens: on a shared GPU, a request that must finish within milliseconds finds the best-effort j...

---

### 19. [SpecLook: Speculating Where to Look for Fast and Reliable Agentic MLLMs](https://arxiv.org/abs/2611.23483v1)

**Authors**: Xi Ding, Jiawei Zhang  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 23.5  
**Type**: new  
**ArXiv ID**: 2611.23483v1  

#### Abstract
Agentic multimodal large language models (MLLMs) that think with images interleave reasoning with zoom-in tool calls. However, this sequential loop is slow, and its answers carry no reliability score. Prior speculation of tokens, reasoning steps, or answers keeps the loop, and answer speculation als...

---

### 20. [Beyond Corpus-Driven Imitation: Evolving Musical Mindsets in the Agentic Orchestra via Quantum Reinforcement Learning](https://arxiv.org/abs/2611.24290v1)

**Authors**: Eduardo Reck Miranda, Moein Fahmideh Vatandoost  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 23.0  
**Type**: new  
**ArXiv ID**: 2611.24290v1  

#### Abstract
This paper presents a framework for computer-aided music composition and performance based on quantum reinforcement learning and multi-agent interaction. We introduce the agentic orchestra, where musical agents evolve distinct mindsets through trial-and-error engagement with a musical environment, r...

---

### 21. [KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs](https://arxiv.org/abs/2611.24294v1)

**Authors**: Haoran Luo, Jiapu Wang, Linhao Luo, Luu Anh Tuan  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 22.0  
**Type**: new  
**ArXiv ID**: 2611.24294v1  

#### Abstract
Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agentic KE and multimodal KE. However, a live knowledge base needs omnimodality, a cl...

---

### 22. [Physics of Language Models: Part 4.2, Canon Layers at Scale where Synthetic Pretraining Resonates in Reality](https://arxiv.org/abs/2611.24963v1)

**Authors**: Zeyuan Allen-Zhu  
**Category**: cs.CL  
**Published**: 2026-11-20  
**Score**: 21.5  
**Type**: new  
**ArXiv ID**: 2611.24963v1  

#### Abstract
Do standard benchmarks see the architectural differences that matter? We study it with 64 from-scratch pretraining runs of Transformers and three linear-model families at 1.3-8B parameters on 1-2T Nemotron-CC tokens, at a cost of roughly 100k USD per 8B run.
  In academic-scale pretraining (1.3B par...

---

### 23. [GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance](https://arxiv.org/abs/2611.23476v1)

**Authors**: Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, Chen-Yu Lee  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 21.0  
**Type**: new  
**ArXiv ID**: 2611.23476v1  

#### Abstract
Autonomous AI agents pair a frozen base model with an editable harness of prompts, skills, tool rules, and memory. Recursive self-improvement (RSI) adapts this harness from experience without weight updates, yet self-editing without external graders often backfires: reflection and scalar scores conf...

---

### 24. [Scone: Symmetry-aware Neural Combinatorial Optimization for Graph Coloring](https://arxiv.org/abs/2611.25273v1)

**Authors**: Paolo Pellizzoni, Melanie Weber  
**Category**: cs.LG  
**Published**: 2026-11-20  
**Score**: 16.5  
**Type**: new  
**ArXiv ID**: 2611.25273v1  

#### Abstract
Graph coloring, which entails assigning colors to nodes such that no adjacent nodes have the same color, is a fundamental combinatorial optimization problem. In general, however, finding a node coloring with no monochromatic edges given a fixed palette is NP-hard. This motivates learning-based metho...

---

### 25. [Embodied Graph: A Relational World Model for Long-Horizon Tasks](https://arxiv.org/abs/2611.24115v1)

**Authors**: Zongyuan Wu, Xin Wang, Tongtong Feng, Yuan Meng, Zeyang Zhang, Ling Feng, Wenwu Zhu  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 16.0  
**Type**: new  
**ArXiv ID**: 2611.24115v1  

#### Abstract
Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success. World models tackle this by learning latent dynamics for imagination-based planning. However, existing approaches merely rely on dense pixel-lev...

---

### 26. [TETHER: Training-Free, Elastic, ToC-Anchored Hierarchy Extraction and Recovery in Design-Driven Long Documents](https://arxiv.org/abs/2611.24960v1)

**Authors**: Yu Zou, Yan Chen, Jialei Zeng, Xiaorui Zhou, Aixi Zhong, Qi Zhou, Haoran You, Ke Jiang, Changyu Hu  
**Category**: cs.CL  
**Published**: 2026-11-20  
**Score**: 14.5  
**Type**: new  
**ArXiv ID**: 2611.24960v1  

#### Abstract
Converting complex documents into structured knowledge constitutes the critical infrastructure urgently required for deploying Large Language Models (LLMs) in downstream research. However, blind to the Table of Contents (ToC) as a macro-structure, existing bottom-up paradigms rely on localized visua...

---

### 27. [Why Sub-4-Bit Vision CNNs Collapse and Where Mixed-Precision Recovery Stops](https://arxiv.org/abs/2611.23445v2)

**Authors**: Michael Schroeder  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 14.0  
**Type**: new  
**ArXiv ID**: 2611.23445v2  

#### Abstract
Deep vision models operating in resource-constrained environments depend heavily on low-bit quantization, yet compressing weights below 4 bits frequently induces catastrophic accuracy collapse. While mixed-precision recovery strategies aim to rescue accuracy by selectively retaining high-precision p...

---

### 28. [Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition for LLM Agent](https://arxiv.org/abs/2611.24697v1)

**Authors**: Siyuan Du, Yuxin Liu, Meng Tang, Haoran Li, Yechao Bai, Feiyang Pan, Jia He  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2611.24697v1  

#### Abstract
Reinforcement learning (RL) has become a common approach for training large language model (LLM) agents on long-horizon tasks. However, learning from sparse terminal rewards makes credit assignment and exploration difficult. We approach these challenges through a policy-induced capability region, th...

---

### 29. [HapBO: Harnessed $\\alpha$-$\\pi$ Bayesian Optimization via Expert Natural Language Priors](https://arxiv.org/abs/2611.25100v1)

**Authors**: Jean-S\'ebastien Giroux, Rose Guay Hottin, Marco Bonizzato  
**Category**: cs.LG  
**Published**: 2026-11-20  
**Score**: 13.5  
**Type**: new  
**ArXiv ID**: 2611.25100v1  

#### Abstract
Bayesian Optimization (BO) can be substantially more sample-efficient when informed by prior knowledge about the problem. In practice, however, such knowledge is often available only in natural language, e.g., expert intuitions or documentation, rather than as the explicit probability distribution l...

---

### 30. [BeFit: Shifting Complexity from Weights to Bernstein Activations for Resource-Constrained Sensing](https://arxiv.org/abs/2611.23520v1)

**Authors**: Malak Gamal El-Din, Yasser Shoukry, Salma Elmalaki  
**Category**: cs.AI  
**Published**: 2026-11-20  
**Score**: 13.0  
**Type**: new  
**ArXiv ID**: 2611.23520v1  

#### Abstract
Time-series sensing increasingly relies on neural networks, yet deployment on resource-constrained microcontrollers remains challenging. Aggressive model compression can reduce accuracy, while restricting weights to multiplication-free representations introduces further losses. We present BeFit, an ...

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
