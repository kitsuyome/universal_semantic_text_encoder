# Universal Text Semantic Encoder

This repository contains experiments and findings on various sentence embedding techniques.

## Objective

The main aim is to analyze and compare the efficiency of different sentence embedding models and understand which models work best for the task and why.

## Methods Evaluated

1. Aggregated Word2Vec and GloVe embeddings.
2. Aggregated embeddings from transformer models (BERT and T5)
3. SentenceTransformers.
4. Instructor.

## Datasets

Datasets to be used for the evaluations will include:

- Stanford Natural Language Inference (SNLI): A widely recognized dataset for natural language understanding tasks, making it an ideal choice for evaluating the semantic understanding capabilities of embeddings.
- STS Benchmark: A standard benchmark for sentence similarity tasks, making it useful to test how well the embeddings capture semantic meaning between sentences.

## Metrics

### Internal Metrics:

- Cosine Similarity: Measures the cosine of the angle between two vectors, providing a measure of similarity.

### External Metrics (Benchmarks):

- SentEval: A framework for evaluating the quality of sentence embeddings using a variety of tasks.
- BEIR: A benchmark tool for evaluating sentence embeddings in information retrieval tasks.

## Experiment Hypotheses

1. **Traditional Embeddings vs. Advanced Techniques**:
    - Hypothesis: Traditional embeddings (like Word2Vec, GloVe) might underperform when compared to more advanced techniques, such as transformer-based embeddings (like BERT, T5) and sentence-specific embeddings (like SentenceTransformers). The latter methods, due to their architectures and specialized training, are likely to capture complex semantic relationships more effectively.
    
2. **Aggregated Embeddings vs. Sentence-Specific Embeddings**:
    - Hypothesis: Sentence-specific embeddings (like SentenceTransformers) are expected to represent sentences better than aggregated word embeddings because they are designed to capture the entire sentence's semantics.

3. **Domain Specificity**:
    - Hypothesis: Models fine-tuned on domain-specific datasets, including those using the Instructor method, might perform better for tasks within that domain compared to general pre-trained models.
      
## Setup and Execution


## Results and Findings


## License

[MIT License](LICENSE)
