# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-11-06 13:24:53 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542v1)

**Authors**: Xuan Wang, Zhuanhao Wu, Tingzhu Fang, Xushi Li, Sicheng Zhang, Zhenyu Yang, Feng Liu, Zhaohui Fan, Qiang Xie, Huayi Zou, Yuncong Liu, Zeyu Song, Ke Zhu, Yanjia Zeng, Jingchun Gao, Yan Shi, Kui Luo, Gezi Li, Liangjun Feng, Cheng Li  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 145.5  
**Type**: new  
**ArXiv ID**: 2611.07542v1  

#### Abstract
In large language model (LLM) serving systems, the key-value (KV) cache grows linearly with sequence length and concurrency, so long-context inference easily hits the high-bandwidth memory (HBM) capacity wall and results in low concurrency. Offloading the KV cache to host dynamic random-access memor...

---

### 2. [NUMA-Torch: Compiler-Driven NUMA-Aware LLM Prefill on Multi-Socket CPUs](https://arxiv.org/abs/2611.07105v1)

**Authors**: Thisara Rathnayaka Weerakoon (Department of Computer Science & Engineering, University of Moratuwa, Sri Lanka), Ishan Dewpura (Department of Computer Science & Engineering, University of Moratuwa, Sri Lanka), Niman Ransindu (Department of Computer Science & Engineering, University of Moratuwa, Sri Lanka), Shavin Anjitha (Department of Computer Science & Engineering, University of Moratuwa, Sri Lanka), Tharindu R. Patabandi (Independent Researcher, San Jose, CA, USA), Sanath Jayasena (Department of Computer Science & Engineering, University of Moratuwa, Sri Lanka)  
**Category**: cs.DC  
**Published**: 2026-11-06  
**Score**: 87.5  
**Type**: new  
**ArXiv ID**: 2611.07105v1  

#### Abstract
For sufficiently large transformer-based Large Language Models (LLMs), whose parameters cannot be retained in on-chip caches, prefill throughput on multi-socket CPUs is often limited by sustainable DRAM bandwidth rather than peak floating-point throughput. In the standard PyTorch compilation (i.e., ...

---

### 3. [FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning](https://arxiv.org/abs/2611.08240v1)

**Authors**: Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, Tailin Wu  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 72.0  
**Type**: new  
**ArXiv ID**: 2611.08240v1  

#### Abstract
Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an av...

---

### 4. [ZYFA: Speed and Accuracy of FP8 FlashAttention on AMD CDNA4](https://arxiv.org/abs/2611.07496v1)

**Authors**: Quentin Anthony, Ganesh Bikshandi, Praneeth Medepalli, Stephen Ebert  
**Category**: cs.DC  
**Published**: 2026-11-06  
**Score**: 69.0  
**Type**: new  
**ArXiv ID**: 2611.07496v1  

#### Abstract
Attention is a core building block of frontier models and often dominates compute-bound prefill at long context. FP8 matrix instructions offer twice the peak throughput of BF16, but they accelerate only matrix multiplication, and the softmax between the two matrix multiplications of attention runs o...

---

### 5. [Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism](https://arxiv.org/abs/2611.06984v1)

**Authors**: Jia Wei, Ziyi Qiu, Yi Xu, Xuehai Qian  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 66.5  
**Type**: new  
**ArXiv ID**: 2611.06984v1  

#### Abstract
Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are still needed by wor...

---

### 6. [StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning](https://arxiv.org/abs/2611.08403v1)

**Authors**: Yang Ouyang, Jung-Eun Kim  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 62.5  
**Type**: new  
**ArXiv ID**: 2611.08403v1  

#### Abstract
Self-consistency (SC) is a widely used decoding strategy for improving chain-of-thought reasoning, but it requires sampling many complete reasoning trajectories with a preset budget. Its efficient variants reduce the cost mainly by stopping full-trajectory sampling early or distributing the number o...

---

### 7. [FastAFD: When Does Attention-FFN Disaggregation Pay on Rack-Scale NVLink?](https://arxiv.org/abs/2611.07149v1)

**Authors**: Yichao Fu, Yuxuan Zhang, Minshen Zhang, Ruitian Wang, Junda Chen, Hao Zhang  
**Category**: cs.DC  
**Published**: 2026-11-06  
**Score**: 59.0  
**Type**: new  
**ArXiv ID**: 2611.07149v1  

#### Abstract
Attention-FFN disaggregation (AFD) separates attention from the experts of a mixture-of-experts (MoE) model and has been reported to raise decode throughput over colocated serving. Whether this advantage holds on rack-scale NVLink systems such as GB200 NVL72 remains unclear: prior results were obtai...

---

### 8. [Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost](https://arxiv.org/abs/2611.07232v1)

**Authors**: Ruitian Wang, Xinyu Yang, Minshen Zhang, Hao Zhang  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2611.07232v1  

#### Abstract
At context lengths of about 1M tokens, dense attention is costly in prefill and decoding, and training typically relies on long documents, which become scarcer as the target length increases. Most sparse attention methods score all preceding blocks or tokens, so their selection cost per query is $O(...

---

### 9. [MambaTG: Candidate-Aware State Space Modeling for Future Link Prediction on Temporal Graphs](https://arxiv.org/abs/2611.07569v1)

**Authors**: Nguyen Hong Quan, Sitao Luan, Yilun Zheng, Lihui Chen  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2611.07569v1  

#### Abstract
Future link prediction on temporal graphs involves both repeated interactions between previously connected node pairs and first-time interactions between pairs with no prior interaction. While repeated-edge prediction can exploit direct pairwise evidence, unseen-edge prediction must generalize beyon...

---

### 10. [Module-Aware Optimization for Graph Neural Networks](https://arxiv.org/abs/2611.08379v1)

**Authors**: Guy Hadad, Haggai Roitman, Moshe Eliasof, Bracha Shapira  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2611.08379v1  

#### Abstract
Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. For Graph Neural Networks (GNNs), however, the effect...

---

### 11. [Should You Split Decode? Disaggregation Across Future Models and Accelerators](https://arxiv.org/abs/2611.08299v1)

**Authors**: Ramyad Hadidi  
**Category**: cs.AR  
**Published**: 2026-11-06  
**Score**: 50.0  
**Type**: new  
**ArXiv ID**: 2611.08299v1  

#### Abstract
For large language model (LLM) inference, prefill/decode disaggregation (P/D) is deployed in production to isolate phases with different resource demands. Attention/feed-forward network disaggregation (AFD) splits decode again, but adds communication, placement constraints, and another provisioned p...

---

### 12. [BlockLock: Reproducible LLM Inference with Fixed Batch Geometry](https://arxiv.org/abs/2611.06977v1)

**Authors**: Xiuyuan Qi, Pedro Reviriego, Javier Conde, Shanshan Liu  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 49.0  
**Type**: new  
**ArXiv ID**: 2611.06977v1  

#### Abstract
Reproducible LLM inference requires that a request produces the same output regardless of the other requests in the batch. Existing solutions pay for this in different ways: batch-invariant kernels constrain every operator, and isolating prefill with fixed-shape decode ({our CoRun-style baseline}) g...

---

### 13. [Not All Loops Cost the Same: Phase-Dependent Depth for Serving Looped Transformers](https://arxiv.org/abs/2611.07211v1)

**Authors**: Zhixu Du, Yuhan Cheng, Hai "Helen" Li, Yiran Chen  
**Category**: cs.DC  
**Published**: 2026-11-06  
**Score**: 47.0  
**Type**: new  
**ArXiv ID**: 2611.07211v1  

#### Abstract
Looped transformers scale inference-time reasoning by repeatedly reusing a shared core, increasing computation without increasing parameter count. Serving prefilling and decoding with a uniform loop budget couples their costs. We present LoopDuet, a phase-dependent depth and training-free serving ap...

---

### 14. [Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction](https://arxiv.org/abs/2611.07998v1)

**Authors**: Makoto Takamoto, Chaitanya Sampara, Viktor Zaverkin, Daniel O\~noro-Rubio, Mathias Niepert  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 43.0  
**Type**: new  
**ArXiv ID**: 2611.07998v1  

#### Abstract
It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains often playing dominant roles. Fragment-based representations have therefore emerged as an effective strategy for incorporating chemically meaningful i...

---

### 15. [HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding](https://arxiv.org/abs/2611.07263v1)

**Authors**: Jongwoo Ko, Pashmina Cameron  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2611.07263v1  

#### Abstract
Parallel block drafting accelerates speculative decoding by predicting multiple future positions in a single backbone pass, but on-device deployment constrains both drafter capacity and context storage. Under tight memory budgets, drafters must model long-range dependencies and fine-grained draft-po...

---

### 16. [Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281v1)

**Authors**: Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2611.08281v1  

#### Abstract
Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 ex...

---

### 17. [MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents](https://arxiv.org/abs/2611.07689v1)

**Authors**: Yizhen Jiang, Haowei Guo, Tianyi Bai, Zengjie Hu, Lu Ma, Zhengyang Zhao, Haoze Sun, Peng Pei, Wentao Zhang  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.07689v1  

#### Abstract
Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rathe...

---

### 18. [Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios](https://arxiv.org/abs/2611.07510v1)

**Authors**: Zhenlong Dai, Zhuoluo Zhao, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.07510v1  

#### Abstract
The rapid development of large language models (LLMs) for code, which closely aligns with the practical needs of real-world software development, has sparked growing attention in repository-level code completion. However, existing Code LLMs present challenges in focusing on suitable contexts from th...

---

### 19. [Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](https://arxiv.org/abs/2611.07122v1)

**Authors**: Korbinian K\"ugler, Carolin Schmidt, Florian Dandl, Filipe Rodrigues  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.07122v1  

#### Abstract
Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit sur...

---

### 20. [Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2611.07561v1)

**Authors**: Weiqin Chen, Xinmeng Huang, Dongsheng Ding, Santiago Paternain  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.07561v1  

#### Abstract
Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to feasible policies but do not prevent constraint violations during training. We study a stronger requirement, safe explor...

---

### 21. [Monotone Viability Learning for Offline Safe Reinforcement Learning](https://arxiv.org/abs/2611.07616v1)

**Authors**: Ziqian Wang, Zhen Zhang  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 41.0  
**Type**: new  
**ArXiv ID**: 2611.07616v1  

#### Abstract
Offline safe reinforcement learning requires reliable long-horizon safety estimates from fixed data. Learning Hamilton-Jacobi (HJ) viability in this setting calls for semantic preservation, convergence, and numerical stability. To address these challenges, we propose Monotone Viability Learning (MoV...

---

### 22. [Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation](https://arxiv.org/abs/2611.07866v1)

**Authors**: Hongyang Su, Beibei Kong, Lei Cheng, Chengxiang Zhuo, Zang Li  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 35.0  
**Type**: new  
**ArXiv ID**: 2611.07866v1  

#### Abstract
LLM-based recommender systems increasingly generate chain-of-thought (CoT) text before each item prediction to activate the LLM's reasoning capacity, costing tens to hundreds of extra tokens per recommendation at inference. We ask whether inference-time reasoning artifacts (textual or latent) can be...

---

### 23. [Graph Neural Networks for Resource Allocation in Integrated Sensing and Communication](https://arxiv.org/abs/2611.07277v1)

**Authors**: Junyu Liao, Lili Chen, Tian Han, Jamie Evans  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2611.07277v1  

#### Abstract
In vehicular integrated sensing and communication (ISAC) networks, each service-provider vehicle uses a limited power budget to serve multiple sensing targets and communication receivers. Maximizing the communication sum-rate subject to sensing signal-to-interference-plus-noise ratio (SINR) constrai...

---

### 24. [OpenRDMA: A GPU-Native Multi-Path Reliable RDMA Transport Architecture](https://arxiv.org/abs/2611.07559v1)

**Authors**: Ziheng Ji, Chunyu Liu, Weihao Peng, Mingheng Mi, Pu Wang, Hai Zhang  
**Category**: cs.AR  
**Published**: 2026-11-06  
**Score**: 34.5  
**Type**: new  
**ArXiv ID**: 2611.07559v1  

#### Abstract
As the computing power density of large-scale AI clusters rises, network communication increasingly limits system performance. GPU-initiated communication requires low-overhead request submission to overlap communication with computation. However, GPUDirect RDMA (GDR) still relies on CPU involvement...

---

### 25. [The Gating Mechanism of KV Cache Eviction](https://arxiv.org/abs/2611.07605v1)

**Authors**: Hao Gu, Xintong Yang, Zhiwei Li, Lei Zhu, Jian Yang, Qiyuan Zhu, Dezhi Li, Jingyuan Zhang, Zhizhuo Kou, Hao Wang, Bei Liu, Jiacheng Liu, Sirui Han  
**Category**: cs.CL  
**Published**: 2026-11-06  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2611.07605v1  

#### Abstract
KV cache eviction must decide which entries carry information that the rest of the cache can no longer supply. A natural way to estimate this is a learnable gate: give each cached entry a gate on its attention weight and train the gate on the model's own objective. The gate belongs inside the normal...

---

### 26. [Rethinking Data Selection: The Importance of Coverage over Difficulty in LLM Fine-Tuning](https://arxiv.org/abs/2611.07323v1)

**Authors**: Lalchand Pandia, Kanishka Misra, Allyson Ettinger  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2611.07323v1  

#### Abstract
Selecting high-quality training data can reduce computation cost for LLM fine-tuning. Prior work on data selection developed a variety of difficulty-based scores, motivated by the intuition that harder examples are more informative. While effective for smaller classification models, we find that suc...

---

### 27. [The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning](https://arxiv.org/abs/2611.07934v1)

**Authors**: Muhammad Ibrahim Khan, Aniket Dixit, Faizan Ahmed, James Brusey  
**Category**: cs.LG  
**Published**: 2026-11-06  
**Score**: 33.5  
**Type**: new  
**ArXiv ID**: 2611.07934v1  

#### Abstract
Reinforcement learning (RL) provides a framework for continuous improvement through interaction with an environment. However, RL agents struggle against tasks that offer exploration challenges and sparse rewards, because learning efficient policies from scratch is slow and sample-inefficient. In con...

---

### 28. [CST-Bench: Benchmarking Counterfactual Spatial Transition Reasoning with Causal Transition On-Policy Self-Distillation](https://arxiv.org/abs/2611.07541v1)

**Authors**: Ying Li, Yongle Cheng, Jing Li, Xingquan Cai, Yawei Luo  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 33.0  
**Type**: new  
**ArXiv ID**: 2611.07541v1  

#### Abstract
Spatial reasoning is a fundamental capability of multimodal large language models (MLLMs), yet existing benchmarks mainly focus on static scene understanding. When objects are moved or swapped, models must infer not only spatial relations but also how interventions change the scene state. To address...

---

### 29. [Characterizing CUDA Locality Domains on Blackwell GPUs](https://arxiv.org/abs/2611.07535v1)

**Authors**: Rocky Wang, Joyce Zhou, Keith Jiang, Jason Zhao  
**Category**: cs.DC  
**Published**: 2026-11-06  
**Score**: 32.0  
**Type**: new  
**ArXiv ID**: 2611.07535v1  

#### Abstract
Low latency is critical to user experience. As NVIDIA Blackwell and Rubin GPUs advance multi-die scaling, data placement and cross-die communication become increasingly important. However, the latency implications and underlying costs of cross-die communication and die-aware execution remain largely...

---

### 30. [Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies](https://arxiv.org/abs/2611.07667v1)

**Authors**: Mete Erdogan, Mirac Suzgun, Aneesh Pappu, Guowei Xu, Batu El, Andrew A. Schoen, Furong Huang, John P. Dickerson, Mert Pilanci, James Zou  
**Category**: cs.AI  
**Published**: 2026-11-06  
**Score**: 31.5  
**Type**: new  
**ArXiv ID**: 2611.07667v1  

#### Abstract
The performance of multi-agent LLM systems depends not only on the capabilities of the underlying models but also on information-sharing policies, which govern what information each agent observes and at what level of detail. But does providing AI agents with more detailed information always improve...

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
