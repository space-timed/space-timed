
<div align="center">

# Hi, I'm David John 👋

**Lead Software Engineer** · **13+ years** · **Distributed Systems & Backend Engineering**

Building reliable backend systems across **Payments, Finance, Retail, and Martech**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-David_John-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dappdavid)
[![X](https://img.shields.io/badge/X-@spacetimed__-111111?style=for-the-badge&logo=x&logoColor=white)](https://x.com/spacetimed_)

</div>

---

### 🛠️ Tech Stack

`Java` · `Spring Boot` · `Microservices` · `Kafka` · `PostgreSQL` · `MongoDB` · `Redis` · `AWS` · `Docker` · `Kubernetes`

### ⚙️ I work on

- 🏗️ Distributed backend systems
- ⚡ Event-driven architectures
- 📐 System design & scalability
- 🔐 Secure APIs & authentication
- 🤖 AI-assisted / agentic software development

### 🧠 Currently exploring

`AI/ML Infrastructure` · `LLM Systems` · `Inference Engineering`

---

### 🚀 Highlighted Projects

#### [⚡ llm-inference-gateway](https://github.com/space-timed/llm-inference-gateway)
High-performance, non-blocking OpenAI-compatible LLM Inference Gateway in Java 21, Spring WebFlux, Project Reactor, and Netty.
- **Dynamic Token-Aware EWMA Scheduling:** Achieves **24.3% lower p95 tail latency** under bimodal prompt distributions.
- **Strictly Reactive Pipeline:** Reactor Netty event loops with zero thread pool blocking and zero concurrency permit leaks.
- **Resilience & Observability:** Three-state circuit breakers, pre-stream failovers, and low-cardinality TTFT / TPOT telemetry.
- `Java 21` · `Spring WebFlux` · `Project Reactor` · `Netty` · `Prometheus` · `Grafana`

#### [💳 payment-engine](https://github.com/space-timed/payment-engine)
Distributed Payment Engine (LedgerFlow) in Java & Spring Boot — Double-Entry Ledger, Pessimistic Concurrency Safety, Transactional Outbox, Kafka, Signed Webhooks, and Reconciliation.
- **Immutable Double-Entry Ledger:** Enforces $\sum \text{Debits} == \sum \text{Credits}$ with integer minor unit (`BIGINT`) precision.
- **Pessimistic Concurrency Safety:** Customer wallet deductions execute under `SELECT ... FOR UPDATE` row locks, mathematically preventing double-spending.
- **Event-Driven Resilience:** Transactional outbox draining to Apache Kafka (KRaft), timestamped HMAC-SHA256 signed webhooks, and automated reconciliation auditor.
- `Java 21` · `Spring Boot` · `PostgreSQL 16` · `Apache Kafka` · `Redis`

#### [🛒 pulsecart](https://github.com/space-timed/pulsecart)
Distributed Microservices e-commerce platform implementing 18 applied distributed systems patterns across 15 independently deployable Java microservices.
- **Enterprise Pattern Implementation:** Database-per-service isolation, orchestrator-based Saga coordination with compensating rollbacks, transactional outbox, and CQRS.
- **High-Contention Concurrency Safety:** Atomic conditional updates benchmarked to **0.00% overselling** under 1,000 concurrent threads.
- **Interactive Architecture Studio:** End-to-end request tracing, live Kafka partition inspection, and 8 bounded chaos experiments.
- `Java 21` · `Spring Boot` · `Apache Kafka` · `PostgreSQL` · `Redis` · `Docker` · `Kubernetes`

---


### 📈 GitHub Contributions

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=space-timed&show_icons=true&theme=github_dark&hide_border=true&rank_icon=github&include_all_commits=true&count_private=true&cache_seconds=1800" alt="David's GitHub statistics" height="165" />
<img src="https://streak-stats.demolab.com?user=space-timed&theme=github-dark-blue&hide_border=true" alt="David's GitHub contribution streak" height="165" />

</div>


---
