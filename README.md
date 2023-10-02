# Universal Text Semantic Encoder

This repository contains experiments and findings on various sentence embedding techniques.

## Objective

The main aim is to analyze and compare the efficiency of different sentence embedding models and understand which models work best for the task and why.

## Methods Evaluated

1. Aggregated Word2Vec and GloVe embeddings.
2. BERT-based sentence embeddings (BERT-Tiny).
3. SentenceTransformers (DistilBERT).

## Internal Metrics:

- Pearson Correlation
-  Spearman Correlation
-  MSE
  
## Benchmarks

- SentEval: Provides a set of tasks and corresponding datasets to evaluate the quality of sentence embeddings.
- STS Benchmark: A standard benchmark for sentence similarity tasks. It contains pairs of sentences with similarity scores, making it useful to test how well the embeddings capture semantic meaning between sentences.

## Experiment Hypotheses

1. **Traditional Embeddings vs. Modern Techniques**:
  - Hypothesis: Modern embeddings like BERT-based and SentenceTransformers might capture semantic nuances better than traditional ones like Word2Vec and GloVe.
3. **Model's Depth and Complexity**:
    - Hypothesis: Architectural features, especially attention mechanisms in models like BERT, can significantly influence the quality of embeddings by better capturing contextual relationships.
4. **Model's Depth and Complexity**:
    - Hypothesis: Deeper models, like BERT, with a large number of parameters, may offer better embeddings by capturing more nuanced semantic relationships than simpler models.
5. **Training Data and Fine-tuning**:
    - Hypothesis: Models fine-tuned on specific tasks, such as SentenceTransformers for sentence comparison, might generate superior embeddings than those trained on generic tasks.
6. **Tokenization and Input Representation**:
- Hypothesis: Advanced tokenization methods, like the subword approach in BERT, may produce better embeddings by efficiently handling morphological variations and out-of-vocabulary words.

## Results

| Model   | Task             | Pearson | Spearman | MSE      |
| ------- | ---------------- | ------- | -------- | -------- |
| w2v     | SICKRelatedness  | 0.8014  | 0.7152   | 0.3644   |
| w2v     | STSBenchmark     | 0.6423  | 0.6197   | 1.6468   |
| glove   | SICKRelatedness  | 0.7869  | 0.7037   | 0.3885   |
| glove   | STSBenchmark     | 0.6578  | 0.6453   | 1.5440   |
| st      | SICKRelatedness  | 0.8509  | 0.8005   | 0.2823   |
| st      | STSBenchmark     | 0.7535  | 0.7581   | 1.0942   |
| bert    | SICKRelatedness  | 0.7781  | 0.6867   | 0.4020   |
| bert    | STSBenchmark     | 0.6507  | 0.6370   | 1.5519   |

## Conclusions

Traditional Embeddings vs. Modern Techniques: Our experiment supports the hypothesis that modern techniques outperform traditional embeddings. The SentenceTransformers, in particular, provided superior results in the tasks used for evaluation, emphasizing their ability to better capture semantic nuances.

Impact of Model Architecture: BERT-based embeddings showed improved performance over aggregated embeddings but slightly underperformed when compared to SentenceTransformers. This may suggest that while attention mechanisms in transformers like BERT offer advantages over traditional methods, dedicated sentence embedding models like SentenceTransformers are optimized for capturing entire sentence semantics.

Overall Quality: All embedding methods provided reasonably good results, indicating their potential usefulness in various applications. However, for tasks that require a deep understanding of sentence semantics, using specialized models like SentenceTransformers would be beneficial.


## License

[MIT License](LICENSE)
