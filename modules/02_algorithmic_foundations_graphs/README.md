# Module 02: Algorithmic Foundations — Graphs

## Purpose

This module introduces graph algorithms that later appear in genome assembly, phylogenetics, network-style biological modelling, and dynamic programming on graph structures.

Graph concepts are central to computational biology. Biological data can be represented using nodes and edges in many contexts, including overlap graphs, de Bruijn graphs, phylogenetic trees, shortest paths, connectivity analysis, and directed acyclic graphs.

## Core Concepts

- Graph representation
- Degree arrays
- Breadth-first search
- Connected components
- Bipartite graphs
- Directed acyclic graphs
- Topological sorting
- Shortest paths
- Strongly connected components
- Constraint modelling
- Graph traversal and connectivity

## Rosalind Problems Covered

| Problem ID | Topic | Treatment |
|---|---|---|
| DEG | Degree array | Worked example |
| DDEG | Double-degree array | Worked example |
| BFS | Breadth-first search | Fully explained |
| CC | Connected components | Fully explained |
| BIP | Bipartite graph | Archive solution |
| DAG | Directed acyclic graph | Fully explained |
| DIJ | Dijkstra shortest path | Fully explained |
| BF | Bellman-Ford shortest path | Archive solution |
| CTE | Shortest cycle through edge | Archive solution |
| TS | Topological sorting | Archive solution |
| HDAG | Hamiltonian path in DAG | Archive solution |
| NWC | Negative weight cycle | Archive solution |
| SCC | Strongly connected components | Fully explained |
| 2SAT | Constraint modelling | Worked example |
| GS | General sink | Archive solution |
| SC | Semi-connected graph | Archive solution |
| SDAG | Shortest paths in DAG | Archive solution |
| SQ | Square in graph | Archive solution |

## Learning Outcomes

After completing this module, a learner should be able to:

- represent graphs using adjacency lists or related structures;
- compute degree-based graph properties;
- perform graph traversal using BFS;
- identify connected components;
- reason about directed graphs and DAGs;
- understand shortest-path and connectivity problems;
- connect graph algorithms to genome assembly and phylogenetics.

## Connection to Later Modules

This module is especially important for:

- Module 08: Graphs and Genome Assembly
- Module 11: Phylogenetics and Evolution
- Module 06: Dynamic Programming and Alignment
- Module 13: ML-ready Bioinformatics Bridge

Genome assembly problems such as overlap graphs, de Bruijn graphs, Eulerian paths, and genome reconstruction build directly on the graph foundations introduced here.
