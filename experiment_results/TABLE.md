Train
+-------------------------------------------------------------+-----------------+-----------------+----------------+
|                            Model                            | F-score (micro) | F-score (macro) |    Accuracy    |
+-------------------------------------------------------------+-----------------+-----------------+----------------+
|              Single Corpus (only Conll_03 Eng)              |  93.88  ±  0.11 |  92.65  ±  0.09 | 90.74  ±  0.08 |
|                   Multi-Corpus (Eng/Dutch)                  |  93.73  ±  0.27 |  93.42  ±  0.26 | 91.09  ±  0.36 |
|  Single Corpus (only Conll_03 Eng) linear probing (lr 0.8)  |  77.76  ±  0.47 |  76.0  ±  0.52  | 67.4  ±  0.56  |
| Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.8) |  93.58  ±  0.2  |  92.28  ±  0.21 | 90.4  ±  0.23  |
|       Multi-Corpus (Eng/Dutch) linear probing (lr 0.8)      |  72.09  ±  0.22 |  70.4  ±  0.27  | 60.29  ±  0.25 |
|      Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.8)     |  93.95  ±  0.11 |  93.65  ±  0.11 | 91.54  ±  0.18 |
|  Single Corpus (only Conll_03 Eng) linear probing (lr 0.3)  |  77.99  ±  0.44 |  76.25  ±  0.56 | 67.61  ±  0.45 |
| Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.3) |  93.62  ±  0.17 |  92.26  ±  0.21 | 90.37  ±  0.26 |
|       Multi-Corpus (Eng/Dutch) linear probing (lr 0.3)      |  72.57  ±  1.05 |  70.86  ±  1.04 | 60.88  ±  1.32 |
|      Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.3)     |  94.04  ±  0.05 |  93.73  ±  0.06 | 91.6  ±  0.07  |
|           Single Corpus (only Conll_03 Eng) BitFit          |                 |                 |                |
|               Multi-Corpus (Eng/Dutch) BitFit               |                 |                 |                |
+-------------------------------------------------------------+-----------------+-----------------+----------------+
Test
+-------------------------------------------------------------+-----------------+-----------------+----------+
|                            Model                            | F-score (micro) | F-score (macro) | Accuracy |
+-------------------------------------------------------------+-----------------+-----------------+----------+
|              Single Corpus (only Conll_03 Eng)              |  77.08  ±  0.45 |                 |          |
|                   Multi-Corpus (Eng/Dutch)                  |  76.4  ±  0.46  |                 |          |
| Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.8) |  78.1  ±  0.95  |                 |          |
|      Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.8)     |  76.75  ±  0.96 |                 |          |
| Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.3) |  78.28  ±  0.47 |                 |          |
|      Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.3)     |  76.55  ±  0.74 |                 |          |
|           Single Corpus (only Conll_03 Eng) BitFit          |                 |                 |          |
|               Multi-Corpus (Eng/Dutch) BitFit               |                 |                 |          |
+-------------------------------------------------------------+-----------------+-----------------+----------+
