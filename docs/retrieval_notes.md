### Corpus Construction

A sentence-level retrieval corpus was created from HotpotQA contexts.

Each record contains:

- Question ID
- Document Title
- Sentence Index
- Sentence Text

This structure supports:

- Sentence retrieval
- Evidence attribution
- Faithfulness analysis
- Failure diagnosis
- 
### Embedding Model

Selected Model: all-MiniLM-L6-v2

Reasons:
- Lightweight & CPU-friendly
- Strong retrieval baseline
- Widely used in semantic search

Embedding Dimension: 384