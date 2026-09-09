# GenPark Gale-Shapley Deferred Acceptance Matching Skill

Gale-Shapley deferred acceptance algorithm ensuring stable, envy-free, and Pareto-efficient bipartite matching.

Learn more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph LR
    P[Proposers: Preference Lists] -->|Deferred Proposals| A[Acceptors: Tentative Holds]
    A -->|Better Offer Received| R[Rejections & Backtracking]
    R --> P
    A --> S[Guaranteed Stable Matching No Blocking Pairs]
    style P fill:#e1f5fe
    style A fill:#fff9c4
    style R fill:#ffcdd2
    style S fill:#c8e6c9
```

## Features
- Classic Gale-Shapley proposing-oriented deferred acceptance algorithm.
- Guaranteed stability with zero blocking pairs.
- Pure Python standard library.
