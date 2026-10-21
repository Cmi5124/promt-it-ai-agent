# Cross-project Research & Idea Atlas — NOT a feature backlog for any specific project

This optional atlas organizes general engineering research into **questions to ask** and **validation procedures**, not ready-to-implement requirements. Topic-level links and individual benchmark claims are not independently verified by this integration; research claims are **CANDIDATE/NOT_VERIFIED** until reviewed at use time.

| Topic or shared pattern | Generalizable engineering question | Validation path | Relevant reference |
|---|---|---|---|
| Hierarchical Agent Skills / progressive disclosure | How to load only relevant instructions? | Task router, context budget, instruction adherence | 08, 14 |
| ECC / multi-agent prompt stack integration | Which components are genuinely additive vs duplicate? | Gap analysis, measurable verified-task success | 07, 14 |
| Context compaction / Compress–Cache–Retrieve | Does compression preserve answerability and recoverability? | A/B task fidelity, retrieval, token/tool/latency | 08 |
| Agent working memory vs durable memory | Which state survives reset and who can access it? | TTL, provenance, ACL, recovery, stale-conflict tests | 08 |
| Encoding text, dataset or agent state as image | Can visual packing reduce token cost without losing precision? | Round-trip/decode, corruption, patches/tokens, adversarial tests | 12, 08 |
| Layered raw/structured/semantic payload | Can separate data layers reduce duplication and improve retrieval? | Storage and retrieval benchmarks, checksum coverage | 12 |
| Crop/tamper detection for image datasets | Can damaged samples be detected and reconstructed? | Corruption simulations, error correction, recovery rate | 12 |
| AI-driven computer use / Brain–Session–Hands | How to separate planning/state/execution and enforce rights? | Permission containment, rollback, success-after-tools | 14, 05 |
| Reverse-engineering agent via MCP / binary inspection | What can be inferred safely from packaged artifacts? | Authorized static/dynamic lab, provenance, license review | 13 |
| Independent security hunter/verifier | Does separating discovery and verification reduce false findings? | Precision/recall, evidence quality, exploit/no-exploit judgment | 04, 13 |
| Security graph / attack paths | Can graph relations improve issue triage? | Ground truth findings, false positive/coverage | 04, 13 |
| Unicode homograph/domain spoofing | Can visually indistinguishable text bypass human or policy checks? | Unicode normalization, IDNA, browser behavior validation | 04, 07 |
| Controlled security load/chaos lab | How much load/failure can the authorized test system tolerate? | Isolated load, SLO, blast-radius stop, recovery | 04, 11 |
| Online storage platforms at massive scale | Which routing/auth/cache/residency ideas transfer to small systems? | Bottleneck/constraint matching, trade-off, phased adoption | 01, 07 |
| Retrieval relevance vs answerability | Do top-ranked chunks actually contain sufficient evidence? | Answerability labels, citation completeness and abstention | 05 |
| RAG vs GraphRAG vs HybridRAG | Which approach solves the particular query mix? | Consistent corpus/query eval, latency, recall, groundedness | 05 |
| Homemade embeddings/tokenizer | When is from-scratch justified vs pretrained? | Compute/data/license/quality baselines | 06, 05 |
| Training models with constrained compute | Can quality goals be met within GPU/time/budget limits? | Full memory/cost estimates, staged eval | 06, 11 |
| Heterogeneous multiple-GPU inference | Does topology and software support feasible throughput? | TP/PP/kernels/interconnect, load and OOM trials | 11 |
| Quantization / KV caching / speculative decode | Which optimization yields gain without quality regression? | Same prompts/concurrency, TTFT/TPOT/VRAM/error | 11, 05 |
| Native multimodal/spatial perception | Which modality adds measurable capabilities? | Segmentation/depth/temporal/3D correctness and FPS | 12 |
| Dataset lineage, held-out evaluation | Could label leakage or reuse invalidate metrics? | Group/time splits, contamination scans, immutable manifests | 06 |
| Portfolio and future-proof architecture | How to allow new versions without opening endless products? | Versioned core, extension contracts, WIP/priority gates | 01, 09 |
| Terminal-first repeatable workflow | Can scripted operations reduce manual inconsistency? | Idempotency, dry run, audit, permission, rollback | 02, 14 |
| Model × agent harness benchmarking | Is success from model weights or tooling? | Model-only/tool-assisted/full-system isolation | 05 |
| Real-world business automation | Are simple rules more dependable than AI for routine tasks? | Reliability, exception rate, review cost, maintainability | 15 |

**Handling a new share:** first classify `(EXPLAIN | FACT_CHECK | RESEARCH | COMPARE | PLAN | IMPLEMENT_REQUEST)`, then choose depth and mode. Only an explicit approved task may promote an idea from this atlas into implementation. Preserve original links and decision trail in a project-specific backlog if the Owner requests it.
