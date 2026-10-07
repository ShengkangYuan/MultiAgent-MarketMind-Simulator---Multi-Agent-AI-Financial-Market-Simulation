# MultiAgent MarketMind Simulator

An interactive multi-agent financial-market simulation studio that explores how individual investor behavior can produce market-wide phenomena such as mispricing, bubbles, and crashes.

## Research Question
Financial markets are emergent systems: macro-level outcomes arise from interactions among heterogeneous decision-makers whose private reasoning is difficult to observe in real markets.

MarketMind Sim creates a controlled computational environment in which investors with different behavioral traits can repeatedly observe market conditions, make decisions, communicate, and trade. Every round, order, message, and decision rationale is recorded, allowing micro-level behavior to be connected with macro-level market outcomes.

## My Contribution
The project is built on the open-source MASIM framework (Apache-2.0), which provides the Ray-based simulation engine and scenario infrastructure. My contribution focused on transforming the code-first research framework into a usable, reproducible browser-based research studio.

I developed:

- A unified Streamlit interface with simulation, analysis, replay, and reasoning views
- 12 curated scenarios covering behavioral biases, market mechanisms, and financial crises
- Agent-by-agent reasoning timelines and round-by-round replay
- Interactive D3.js communication-topology visualization
- A no-code project builder for configuring agents and market settings
- Cross-platform and offline support, including bundled experimental data

## AI & Multi-Agent Architecture
Four interchangeable decision engines share a common architecture:

- Rule-based agents
- LLM-based agents
- Rule + LLM hybrid agents
- Retrieval-augmented agents

This allows controlled comparisons between formula-based behavioral models and LLM-driven decision-making within the same simulated market.

The LLM is used as a computational representation of investor reasoning rather than as a market-price predictor. Its decisions are recorded together with structured orders and reasoning, making individual behavior observable and comparable across agents.

## Experiment & Finding
In the Anchoring Effect experiment, individually plausible anchoring behavior produced slow price discovery and persistent mispricing, while momentum and noise traders amplified price movements and fundamental traders exerted corrective pressure.

The experiment is intentionally a stylized computational model rather than a calibrated predictor of real markets. Future work includes empirical calibration against historical crises, repeated-run statistical evaluation, and larger datasets.

## Engineering
The system uses Ray for concurrent agent execution and Streamlit for the interactive studio, with NumPy, pandas, SciPy, Pydantic, NetworkX, and D3.js supporting computation and visualization.

Rule-based experiments and the complete studio can run offline without an API key, while LLM scenarios use optional external model interfaces with retry and fallback mechanisms.

## Tech Stack
Python · Ray · Streamlit · NumPy · pandas · SciPy · Pydantic · NetworkX · D3.js · LLM APIs