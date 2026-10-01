# arXiv Papers Bot 🤖

This repository automatically fetches and displays relevant papers from arXiv based on configured criteria.

## RSS Vercel Deployment [![An example of deployed RSS Server using vercel](https://img.shields.io/badge/Deployed-Example-blue)](https://arxiv.tachicoma.top/)

You can click this to deploy yours 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maydomine/arxiv_rss_bot)
## 📊 Statistics

- **Last Updated**: 2026-10-01 12:26:24 UTC
- **Total Papers Found**: 30
- **Categories Monitored**: cs.AI, cs.CL, cs.DC, cs.LG, cs.AR

## 📚 Recent Papers

### 1. [MoRE: Scaling mixture of experts with hardware-aware low-rank routing](https://arxiv.org/abs/2609.36301v1)

**Authors**: Honam Wong, Surbhi Goel, Enric Boix-Adser\`a  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 109.0  
**Type**: new  
**ArXiv ID**: 2609.36301v1  

#### Abstract
Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts. In this regime, the standard linear router becomes a bottleneck: with $M$ experts and hidden dimension $h$, its per-token cost $\Theta(Mh)$ dominates the MoE layer ...

---

### 2. [Preserving Provenance in Shared KV Caches for LLM Serving](https://arxiv.org/abs/2609.38706v1)

**Authors**: Wei Song, Yuxin Cao, Xi Zheng, Leo Zhang, Xiao Cheng  
**Category**: cs.DC  
**Published**: 2026-10-01  
**Score**: 96.0  
**Type**: new  
**ArXiv ID**: 2609.38706v1  

#### Abstract
Production LLM serving stacks combine an inference engine's local prefix cache with a shared KV-cache tier for fleet-wide reuse. The local cache distinguishes requests by adapter, weight configuration and sharing domain, but the shared tier may key entries only by token content and coarse model meta...

---

### 3. [Reinforcing Multimodal Reasoning via Token-Level Perception-Grounded Advantage Estimation](https://arxiv.org/abs/2609.39168v1)

**Authors**: Zhihan Zhang, Lizi Liao  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 94.5  
**Type**: new  
**ArXiv ID**: 2609.39168v1  

#### Abstract
Reinforcement Learning with Verifiable Rewards (RLVR) has improved the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet existing frameworks rely on coarse, sequence-level reward signals that lack the fine-grained supervision over the visually-grounded steps within a multimodal...

---

### 4. [$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient](https://arxiv.org/abs/2609.37976v1)

**Authors**: Hongbo Ma, Sansheng Cao, Jiajun Fan, Bangji Yang, Ge Liu  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 77.5  
**Type**: new  
**ArXiv ID**: 2609.37976v1  

#### Abstract
LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singu...

---

### 5. [Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard](https://arxiv.org/abs/2609.39838v1)

**Authors**: Julian Schulz, Lukas F\"ulle, Rieke Fruengel  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 64.0  
**Type**: new  
**ArXiv ID**: 2609.39838v1  

#### Abstract
Chain-of-thought monitoring as an approach for AI oversight and control is threatened by the possibility of steganographic reasoning, where LLMs conceal their reasoning inside innocuous-looking text. Two neighbouring capabilities, steganographic messaging (passing a concealed message) and encoded re...

---

### 6. [Looped Actor: Depth-Recurrent Reasoning Models for Reinforcement Learning](https://arxiv.org/abs/2609.37432v1)

**Authors**: T. Konstantin Rusch, Tim Seyde, Jared Boyer, Zach J. Patterson, Daniela Rus  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 63.0  
**Type**: new  
**ArXiv ID**: 2609.37432v1  

#### Abstract
Looped reasoning models repeatedly apply a shared set of parameters, enabling more computation without increasing the model size. These models also support input-dependent computation by dynamically deciding when to stop looping. Motivated by the recent success of looped transformers in language mod...

---

### 7. [Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference](https://arxiv.org/abs/2609.38981v1)

**Authors**: Jianxing Qin, Alexander Du, Danfeng Zhang, Matthew Lentz, Danyang Zhuo  
**Category**: cs.DC  
**Published**: 2026-10-01  
**Score**: 60.0  
**Type**: new  
**ArXiv ID**: 2609.38981v1  

#### Abstract
LLM inference systems may vary batch composition, prompt chunking, prefill/decode execution, and KV-cache reuse, eviction, or recomputation. These optimizations should not affect system outputs. Production systems, including vLLM's batch-invariant mode and SGLang's deterministic mode, target this go...

---

### 8. [Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding](https://arxiv.org/abs/2609.36173v1)

**Authors**: Haohui Zhang, Keyu Chen, Haocheng Sun, Weibo Gu, Ruizhi Qiao, Xing Sun, Bo Jiang  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 57.0  
**Type**: new  
**ArXiv ID**: 2609.36173v1  

#### Abstract
Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the f...

---

### 9. [ChronoGraph: Functional 4D Scene Graphs with Vision-Language Models for Interaction Understanding and Grounded Planning](https://arxiv.org/abs/2609.39665v1)

**Authors**: Chenyangguang Zhang, Malgorzata Gwiazda, Guanlong Jiao, Yuanchen Ju, Federico Tombari, Koushil Sreenath, Marc Pollefeys, Sunghwan Hong  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2609.39665v1  

#### Abstract
Embodied agents must determine where to act, anticipate the resulting scene changes, and interpret observed outcomes to guide subsequent actions. This requires connecting 4D interaction understanding, which explains how past actions changed the scene, with spatially grounded planning, which determin...

---

### 10. [Trident: Unifying Guarded Dispatch and Host Execution for PyTorch Triton Workloads](https://arxiv.org/abs/2609.37241v1)

**Authors**: Jinjie Liu, Xiaoyan Liu, Shuhan Zhang, Wenjia Sun, Ruilin Yang, Chunlei Men, Yonghua Lin, Shaohua Li  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 56.5  
**Type**: new  
**ArXiv ID**: 2609.37241v1  

#### Abstract
User-written Triton kernels enable high-performance GPU computation within PyTorch, but their end-to-end latency can remain dominated by host-side orchestration, especially when device execution is short. Although torch.compile can generate native host wrappers for captured graphs, each invocation s...

---

### 11. [WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325v1)

**Authors**: Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu, Tommi Jaakkola, Yang Zhang, Shiyu Chang  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 55.5  
**Type**: new  
**ArXiv ID**: 2609.40325v1  

#### Abstract
As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI ...

---

### 12. [Hierarchical Compression of Vision-Language Model Benchmarks](https://arxiv.org/abs/2609.37515v1)

**Authors**: Hyunjong Ok, Seunggu Kang, Jaeho Lee  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 54.5  
**Type**: new  
**ArXiv ID**: 2609.37515v1  

#### Abstract
Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace. Benchmark compression methods that preserve model rankings at a fraction of the cost are well studied for l...

---

### 13. [ScaGNN: a Graph Neural Network for Multiple Scattering Simulations](https://arxiv.org/abs/2609.37509v1)

**Authors**: R\'emi Marsal, St\'ephanie Chaillat, Alexandre Chapoutot  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 52.5  
**Type**: new  
**ArXiv ID**: 2609.37509v1  

#### Abstract
The boundary element method (BEM) provides an efficient numerical framework for solving multiple scattering problems in unbounded homogeneous domains. By restricting the discretization to the domain boundaries, it substantially reduces computational complexity. The procedure first consists in determ...

---

### 14. [Learning Process Rewards via Reasoning State Propagation](https://arxiv.org/abs/2609.39220v1)

**Authors**: Kai Gan, Zi-Hao Zhou, Bo Ye, Jian Zhao, Min-Ling Zhang, Tong Wei  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2609.39220v1  

#### Abstract
Process reward models (PRMs) have demonstrated notable effectiveness in test-time scaling and reinforcement learning by providing fine-grained signals for evaluating intermediate reasoning states, but their training relies heavily on costly process annotations. A natural way to alleviate this depend...

---

### 15. [Scheduling Recursive Reasoning in Looped Transformers](https://arxiv.org/abs/2609.36653v1)

**Authors**: Boyuan Wang, Chengyao Yu, Jiaxi Ren, Hongxin Wei, Bingyi Jing, Yuxin Tao  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 52.0  
**Type**: new  
**ArXiv ID**: 2609.36653v1  

#### Abstract
Recurrent reasoning models have attracted growing attention for scaling test-time computation, typically by iteratively refining latent states with shared parameters. However, these models apply each learned update with a fixed unit scale, which can be conservative when updates make persistent progr...

---

### 16. [Markovian Nonconvex ADMM for Reinforcement Learning: Bellman-Resolvent Stability Beyond Smooth Blocks](https://arxiv.org/abs/2609.36859v1)

**Authors**: Zhaojun Peng  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 51.5  
**Type**: new  
**ArXiv ID**: 2609.36859v1  

#### Abstract
We identify and study a structural mechanism for Markovian nonconvex ADMM in reinforcement learning. Using finite discounted MDPs as a canonical proving ground, we show that the discounted Bellman resolvent $(I-\gamma P_\pi)^{-1}$ can provide the multiplier stability that classical nonconvex ADMM an...

---

### 17. [ABC: Advantage-Based Control Variates for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2609.36058v1)

**Authors**: Hsiao-Ru Pan, Florent Draye, Bernhard Sch\"olkopf  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 51.0  
**Type**: new  
**ArXiv ID**: 2609.36058v1  

#### Abstract
Recent progress in reinforcement learning with verifiable rewards (RLVR) has highlighted the effectiveness of simple critic-free policy-gradient methods such as Group Relative Policy Optimization (GRPO). In contrast, actor-critic methods rely on learned value functions whose approximation error can ...

---

### 18. [Decode-Latency Feedback Prefill: A Model-Free Controller and Its Generalization Limits](https://arxiv.org/abs/2609.38386v1)

**Authors**: Gaurav Agarwal, Ashish Garg, Isha Singhal  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 48.0  
**Type**: new  
**ArXiv ID**: 2609.38386v1  

#### Abstract
Concurrent autoregressive inference creates a fundamental interference problem: prefilling a newly arrived long prompt can delay tokens for requests that are already decoding. Fixed prefill chunks reduce this interference, but the best chunk size depends on the model, hardware, load, and latency obj...

---

### 19. [AdaKerNet: Neural Kernel Decoding for Task-Adaptive Prediction with Multimodal Large Models](https://arxiv.org/abs/2609.36368v1)

**Authors**: Konstantinos D. Polyzos, Eleni Oikonomou, Tara Javidi  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 48.0  
**Type**: new  
**ArXiv ID**: 2609.36368v1  

#### Abstract
Large foundation models have been introduced with the promise of efficient adaptation to downstream tasks. Yet, under limited supervision, MLLMs, an important class of large foundation models, remain challenging to adapt to various downstream tasks. Adaptation typically relies either on MLLM paramet...

---

### 20. [Scaling Parameter and Context in Attention: Native Sparse Attention from Mixture-of-Head](https://arxiv.org/abs/2609.38832v1)

**Authors**: Zizhuo Fu, Runsheng Wang, Meng Li  
**Category**: cs.CL  
**Published**: 2026-10-01  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.38832v1  

#### Abstract
Scaling attention parameters can improve language model quality, but retaining full token histories makes additional heads costly at long contexts. Furthermore, since attention retrieves and combines contextual information, parameter scaling should also support longer contexts. We therefore ask whet...

---

### 21. [Structure-augmented LLMs for High-Level Synthesis Pragma Optimization](https://arxiv.org/abs/2609.38601v1)

**Authors**: Haocheng Xu, Ye Qiao, Phyo Pyae Moe Aung, Alok Mishra, Pavana Prakash, Rolando Pablo Hong Enriquez, Adam Han Wu, Zhiheng Chen, Dejan Milojicic, Sitao Huang  
**Category**: cs.AR  
**Published**: 2026-10-01  
**Score**: 45.0  
**Type**: new  
**ArXiv ID**: 2609.38601v1  

#### Abstract
Pragma insertion drives the quality of high-level synthesis (HLS) designs. Choosing the right directives demands expert knowledge and reasoning about loop nesting, data dependences, and memory layout. While existing large language models (LLMs) show promise in code generation, they lack explicit pro...

---

### 22. [FluxLite: Inference-Time Proposal Control for Discrete Diffusion Models](https://arxiv.org/abs/2609.35947v1)

**Authors**: Yinuo Ren, Haoxuan Chen, Grant M. Rotskoff, Jiequn Han, Lexing Ying  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.35947v1  

#### Abstract
Many inference-time tasks for pretrained discrete diffusion models and diffusion language models reduce to drawing samples from a tilted version of the pretrained distribution. Feynman-Kac sequential Monte Carlo (SMC) makes this correction exact in principle, but its prescribed weights routinely deg...

---

### 23. [Prompts Live on an Arc: Gaussian Curricula in Fisher--Rao Coordinates for Rollout-Efficient GRPO](https://arxiv.org/abs/2609.38018v1)

**Authors**: Mei Okonkwo, Pixel Nomand, Julian Berg, Elena Voss, Lena Park, Marcus Hale, Adrian Cho, Sofia Reyes  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 43.5  
**Type**: new  
**ArXiv ID**: 2609.38018v1  

#### Abstract
Group relative policy optimization (GRPO) learns only from prompts whose sampled responses disagree: a group that is entirely correct or entirely incorrect has zero reward variance, contributes no gradient, and still consumes its rollouts. Prompt-selection methods reduce this waste by steering sampl...

---

### 24. [Beyond Compression: Diagnosing How Post-Training Changes Mathematical Reasoning](https://arxiv.org/abs/2609.37066v1)

**Authors**: Hongyang Li, Yiming Zhu, Xiao Li, Caesar Wu, Said Mammar, Pascal Bouvry  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 42.5  
**Type**: new  
**ArXiv ID**: 2609.37066v1  

#### Abstract
Post-training is central to mathematical reasoning in modern large language models (LLMs), but endpoint pass@1 alone underidentifies what has changed. Gains may reflect newly reachable solutions, cheaper sampling of latent solutions, surface robustness, or memorisation. We compare three post-trainin...

---

### 25. [Targeted Retrieval, Compact Representations: How CoT Reasoning Improves Long-Context Counting](https://arxiv.org/abs/2609.38958v1)

**Authors**: Liang Twist Shan, Tianyu Hu, Hao Yan, Yiqiao Zhong  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.38958v1  

#### Abstract
Large language models (LLMs) have been rapidly improving in long-context tasks, powered by Chain-of-Thought (CoT) reasoning. However, the internal mechanisms underlying this improvement remain unclear. We investigate these mechanisms through a needle-in-a-haystack (NIAH) counting task, where an LLM ...

---

### 26. [Representable but Unlearned: Encoding Rank and the Interaction-Prediction Floor](https://arxiv.org/abs/2609.36208v1)

**Authors**: Zahra Khodagholi, Niloofar Yousefi  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.36208v1  

#### Abstract
Input encodings can restrict which measured contrasts a predictor can jointly reproduce, even when no single contrast is forced to vanish. We compute the attainable contrast space from an encoder's equivalence classes and a fixed contrast design, without labels, loss, or a fitted model; projecting t...

---

### 27. [SERA: Scale-Equalized Rollout Allocation for Maximum Likelihood Reinforcement Learning](https://arxiv.org/abs/2609.36552v1)

**Authors**: Zihao Chen, Fanxiang Xiong, Hongran Ren, Xuefeng Bai, Zhongxiang Dai, Kehai Chen, Zhiguo Zhang, Zhiyong Wang, Yu Cheng  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.36552v1  

#### Abstract
Maximum Likelihood Reinforcement Learning (MaxRL) targets prompt-wise log-success and has shown strong performance on reasoning tasks. Under finite rollout budgets, however, the estimator used by MaxRL attenuates each prompt's likelihood gradient by a factor that depends on its success probability a...

---

### 28. [Inducing Process Supervision from Outcome-Only Reinforcement Learning](https://arxiv.org/abs/2609.36641v1)

**Authors**: Shengda Fan, Xin Cong, Zhong Zhang, Haotian Chen, Yankai Lin  
**Category**: cs.LG  
**Published**: 2026-10-01  
**Score**: 42.0  
**Type**: new  
**ArXiv ID**: 2609.36641v1  

#### Abstract
Process reward models (PRMs) have become a key component for LLMs, as their step-level feedback supports both post-training and test-time reasoning. However, training strong PRMs remains costly: human step annotation is difficult to scale, while Monte Carlo estimation is computationally expensive an...

---

### 29. [Understanding as No-Arbitrage: Bounded Dutch Books as a Definition and Training Objective for Language Models](https://arxiv.org/abs/2609.39341v1)

**Authors**: Daniel Dragonevskiy  
**Category**: cs.AI  
**Published**: 2026-10-01  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.39341v1  

#### Abstract
Does a language model merely predict tokens, or does it understand what it says? We make this question measurable by defining "understanding" through the lens of no-arbitrage. A model understands a vocabulary to a certain degree if a computationally bounded trader cannot extract guaranteed profit by...

---

### 30. [Spike-driven Vision-Language-Action Model](https://arxiv.org/abs/2609.39514v1)

**Authors**: Shuai Wang, Malu Zhang, Mingquan Liu, Weihui Dai, Dehao Zhang, Jieyuan Zhang, Yimeng Shan, Zijian Zhou, Yang Yang  
**Category**: cs.CL  
**Published**: 2026-10-01  
**Score**: 41.5  
**Type**: new  
**ArXiv ID**: 2609.39514v1  

#### Abstract
Vision-language-action (VLA) models bridge multimodal understanding and robotic control, advancing the dominant paradigm for embodied intelligence. However, most existing models rely on large Transformers, whose latency and energy costs hinder deployment on resource-constrained platforms. Through sp...

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
