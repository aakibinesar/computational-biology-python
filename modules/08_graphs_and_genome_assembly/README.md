# Module 08: Graphs and Genome Assembly

## Purpose

This module connects graph algorithms to genome assembly.

Genome assembly can be understood as a graph problem. Reads, k-mers, overlaps, and sequence fragments can be represented using nodes and edges. This module shows how concepts such as overlap graphs, de Bruijn graphs, Eulerian paths, and graph traversal support sequence reconstruction.

## Core Concepts

- Overlap graphs
- Tree completion
- k-mer generation
- de Bruijn graphs
- Eulerian paths and cycles
- Genome reconstruction
- Perfect coverage
- Assembly graph alternatives
- Assembly quality metrics
- Graph-based interpretation of sequence data

## Rosalind Problems Covered

| Problem ID | Topic | Treatment |
|---|---|---|
| GRPH | Overlap graph | Fully explained |
| TREE | Completing a tree | Worked example |
| LONG | Genome reconstruction from overlaps | Worked example |
| DBRU | de Bruijn graph | Fully explained |
| PCOV | Perfect coverage | Worked example |
| GASM | Genome assembly | Fully explained |
| GREP | Alternative assembly paths | Worked example |
| ASMQ | Assembly quality metrics | Worked example |
| DEG / DDEG | Graph degree foundations | Cross-module reference |
| BFS / CC / SCC | Graph traversal and connectivity | Cross-module reference |
| BA3A–BA3M | Textbook genome assembly problems | Cross-module reference |

## Learning Outcomes

After completing this module, a learner should be able to:

- explain why genome assembly can be modelled as a graph problem;
- construct overlap graphs from sequence reads;
- construct de Bruijn graphs from strings and k-mers;
- understand the role of Eulerian paths and cycles in genome reconstruction;
- connect graph traversal ideas to assembly workflows;
- interpret basic assembly quality metrics;
- relate classical graph algorithms to biological sequence reconstruction.

## Connection to Later Modules

This module connects algorithmic graph theory with applied computational biology.

It supports:

- Module 07: String Matching and Genome Indexing
- Module 11: Phylogenetics and Evolution
- Module 13: ML-ready Bioinformatics Bridge

The graph-based thinking introduced here is useful for sequence assembly, biological networks, phylogenetic reasoning, and graph-based biological data representation.
