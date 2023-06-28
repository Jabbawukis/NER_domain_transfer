Train
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------------+
|                                       Model                                       | F-score (micro) | F-score (macro) |    Accuracy    |
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------------+
|                                Single Corpus (Eng)                                |  93.88  ±  0.11 |  92.65  ±  0.09 | 90.74  ±  0.08 |
|                              Multi-Corpus (Eng+Dutch)                             |  93.73  ±  0.27 |  93.42  ±  0.26 | 91.09  ±  0.36 |
|                   Single Corpus (Eng) linear probing (lp-lr 0.8)                  |  77.76  ±  0.47 |  76.0  ±  0.52  | 67.4  ±  0.56  |
|                  Single Corpus (Eng) full fine-tuning (lp-lr 0.8)                 |  93.58  ±  0.2  |  92.28  ±  0.21 | 90.4  ±  0.23  |
|                Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.8)                |  72.09  ±  0.22 |  70.4  ±  0.27  | 60.29  ±  0.25 |
|               Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.8)               |  93.95  ±  0.11 |  93.65  ±  0.11 | 91.54  ±  0.18 |
|                   Single Corpus (Eng) linear probing (lp-lr 0.3)                  |  77.99  ±  0.44 |  76.25  ±  0.56 | 67.61  ±  0.45 |
|                  Single Corpus (Eng) full fine-tuning (lp-lr 0.3)                 |  93.62  ±  0.17 |  92.26  ±  0.21 | 90.37  ±  0.26 |
|                Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.3)                |  72.57  ±  1.05 |  70.86  ±  1.04 | 60.88  ±  1.32 |
|               Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3)               |  94.04  ±  0.05 |  93.73  ±  0.06 | 91.6  ±  0.07  |
|                             Single Corpus (Eng) BitFit                            |  89.44  ±  0.21 |  87.59  ±  0.19 | 83.55  ±  0.48 |
|                          Multi-Corpus (Eng+Dutch) BitFit                          |  90.04  ±  0.14 |  89.53  ±  0.16 | 85.54  ±  0.36 |
|               Single Corpus (Eng) linear probing (lp-lr 0.3) BitFit               |  78.58  ±  0.45 |  76.72  ±  0.39 | 68.57  ±  0.58 |
|              Single Corpus (Eng) full fine-tuning (lp-lr 0.3) BitFit              |  92.11  ±  0.81 |  90.33  ±  0.82 | 87.97  ±  1.36 |
|             Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.3) BitFit            |  72.87  ±  0.18 |  71.06  ±  0.19 | 61.18  ±  0.09 |
|            Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3) BitFit           |  91.98  ±  0.25 |  91.5  ±  0.27  | 88.47  ±  0.36 |
|           Single Corpus (Eng + Dev-Split => CoNLL-03 German Test-Split)           |  93.79  ±  0.12 |  92.49  ±  0.15 | 90.72  ±  0.18 |
|         Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)        |  93.82  ±  0.1  |  93.51  ±  0.11 | 91.34  ±  0.11 |
|          Single Corpus (Dutch + Dev-Split => CoNLL-03 German Test-Split)          |  94.68  ±  0.55 |  94.71  ±  0.56 | 92.9  ±  0.94  |
| Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split + max_epochs=5) |  93.49  ±  0.05 |  93.15  ±  0.05 | 90.72  ±  0.07 |
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------------+
Test
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------+
|                                       Model                                       | F-score (micro) | F-score (macro) | Accuracy |
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------+
|                                Single Corpus (Eng)                                |  77.08  ±  0.45 |                 |          |
|                              Multi-Corpus (Eng+Dutch)                             |  76.4  ±  0.46  |                 |          |
|                  Single Corpus (Eng) full fine-tuning (lp-lr 0.8)                 |  78.1  ±  0.95  |                 |          |
|               Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.8)               |  76.75  ±  0.96 |                 |          |
|                  Single Corpus (Eng) full fine-tuning (lp-lr 0.3)                 |  78.28  ±  0.47 |                 |          |
|               Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3)               |  76.55  ±  0.74 |                 |          |
|                             Single Corpus (Eng) BitFit                            |  68.98  ±  1.53 |                 |          |
|                          Multi-Corpus (Eng+Dutch) BitFit                          |  65.99  ±  0.77 |                 |          |
|              Single Corpus (Eng) full fine-tuning (lp-lr 0.3) BitFit              |  74.69  ±  0.62 |                 |          |
|            Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3) BitFit           |  67.96  ±  1.41 |                 |          |
|           Single Corpus (Eng + Dev-Split => CoNLL-03 German Test-Split)           |  77.02  ±  0.1  |                 |          |
|         Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)        |  76.32  ±  0.99 |                 |          |
|          Single Corpus (Dutch + Dev-Split => CoNLL-03 German Test-Split)          |  74.9  ±  0.82  |                 |          |
| Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split + max_epochs=5) |  76.47  ±  0.84 |                 |          |
+-----------------------------------------------------------------------------------+-----------------+-----------------+----------+
