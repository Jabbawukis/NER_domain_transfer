
# Experiments
## Multi-Data Set Training on Conll_03 Eng/Dutch -> on Conll_03 German
## Phase 01 (full fine-tuning)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=5.0e-6
* mini_batch_size=4
* max_epochs=10

### Train Results
#### train Single Corpus (Eng)
* F-score (micro) - Average: 93.88  ±  0.11
* F-score (macro) - Average: 92.65  ±  0.09
* Accuracy - Average: 90.74  ±  0.08
#### train Multi-Corpus (Eng+Dutch)
* F-score (micro) - Average: 93.73  ±  0.27
* F-score (macro) - Average: 93.42  ±  0.26
* Accuracy - Average: 91.09  ±  0.36
### Test Results on Conll_03 German
#### test Single Corpus (Eng)
* F-score (micro) - Average: 77.08  ±  0.45
#### test Multi-Corpus (Eng+Dutch)
* F-score (micro) - Average: 76.4  ±  0.46

## Phase 02a (linear probing lr 0.8 + full fine-tuning)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=0.8 (linear probing)
* mini_batch_size=32 (linear probing)
* learning_rate=5.0e-6 (full fine-tuning)
* mini_batch_size=4 (full fine-tuning)
* max_epochs=10

### Train Results
#### train Single Corpus (Eng) linear probing (lp-lr 0.8)
* F-score (micro) - Average: 77.76  ±  0.47
* F-score (macro) - Average: 76.0  ±  0.52
* Accuracy - Average: 67.4  ±  0.56
#### train Single Corpus (Eng) full fine-tuning (lp-lr 0.8)
* F-score (micro) - Average: 93.58  ±  0.2
* F-score (macro) - Average: 92.28  ±  0.21
* Accuracy - Average: 90.4  ±  0.23
#### train Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.8)
* F-score (micro) - Average: 72.09  ±  0.22
* F-score (macro) - Average: 70.4  ±  0.27
* Accuracy - Average: 60.29  ±  0.25
#### train Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.8)
* F-score (micro) - Average: 93.95  ±  0.11
* F-score (macro) - Average: 93.65  ±  0.11
* Accuracy - Average: 91.54  ±  0.18
### Test Results on Conll_03 German
#### test Single Corpus (Eng) full fine-tuning (lp-lr 0.8)
* F-score (micro) - Average: 78.1  ±  0.95
#### test Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.8)
* F-score (micro) - Average: 76.75  ±  0.96

## Phase 02b (linear probing lr 0.3 + full fine-tuning) (lp-lr 0.8)
### Params:
* ...
* learning_rate=0.3 (linear probing)
* ...

### Train Results
#### train Single Corpus (Eng) linear probing (lp-lr 0.3)
* F-score (micro) - Average: 77.99  ±  0.44
* F-score (macro) - Average: 76.25  ±  0.56
* Accuracy - Average: 67.61  ±  0.45
#### train Single Corpus (Eng) full fine-tuning (lp-lr 0.3)
* F-score (micro) - Average: 93.62  ±  0.17
* F-score (macro) - Average: 92.26  ±  0.21
* Accuracy - Average: 90.37  ±  0.26
#### train Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.3)
* F-score (micro) - Average: 72.57  ±  1.05
* F-score (macro) - Average: 70.86  ±  1.04
* Accuracy - Average: 60.88  ±  1.32
#### train Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3)
* F-score (micro) - Average: 94.04  ±  0.05
* F-score (macro) - Average: 93.73  ±  0.06
* Accuracy - Average: 91.6  ±  0.07
### Test Results on Conll_03 German
#### test Single Corpus (Eng) full fine-tuning (lp-lr 0.3)
* F-score (micro) - Average: 78.28  ±  0.47
#### test Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3)
* F-score (micro) - Average: 76.55  ±  0.74

## Phase 03a (only full fine-tuning + Transformer Bias Only training)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=5.0e-6
* mini_batch_size=4
* max_epochs=10

### Train Results
#### train Single Corpus (Eng) BitFit
* F-score (micro) - Average: 89.44  ±  0.21
* F-score (macro) - Average: 87.59  ±  0.19
* Accuracy - Average: 83.55  ±  0.48
#### train Multi-Corpus (Eng+Dutch) BitFit
* F-score (micro) - Average: 90.04  ±  0.14
* F-score (macro) - Average: 89.53  ±  0.16
* Accuracy - Average: 85.54  ±  0.36
### Test Results on Conll_03 German
#### test Single Corpus (Eng) BitFit
* F-score (micro) - Average: 68.98  ±  1.53
#### test Multi-Corpus (Eng+Dutch) BitFit
* F-score (micro) - Average: 65.99  ±  0.77

## Phase 03b (linear probing lr 0.3 + full fine-tuning + Transformer Bias Only training)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=0.3 (linear probing)
* mini_batch_size=32 (linear probing)
* learning_rate=5.0e-6 (full fine-tuning)
* mini_batch_size=4 (full fine-tuning)
* max_epochs=10

### Train Results
#### train Single Corpus (Eng) linear probing (lp-lr 0.3) BitFit
* F-score (micro) - Average: 78.58  ±  0.45
* F-score (macro) - Average: 76.72  ±  0.39
* Accuracy - Average: 68.57  ±  0.58
#### train Single Corpus (Eng) full fine-tuning (lp-lr 0.3) BitFit
* F-score (micro) - Average: 92.11  ±  0.81
* F-score (macro) - Average: 90.33  ±  0.82
* Accuracy - Average: 87.97  ±  1.36
#### train Multi-Corpus (Eng+Dutch) linear probing (lp-lr 0.3) BitFit
* F-score (micro) - Average: 72.87  ±  0.18
* F-score (macro) - Average: 71.06  ±  0.19
* Accuracy - Average: 61.18  ±  0.09
#### train Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3) BitFit
* F-score (micro) - Average: 91.98  ±  0.25
* F-score (macro) - Average: 91.5  ±  0.27
* Accuracy - Average: 88.47  ±  0.36
### Test Results on Conll_03 German
#### test Single Corpus (Eng) full fine-tuning (lp-lr 0.3) BitFit
* F-score (micro) - Average: 74.69  ±  0.62
#### test Multi-Corpus (Eng+Dutch) full fine-tuning (lp-lr 0.3) BitFit
* F-score (micro) - Average: 67.96  ±  1.41

## Phase 04 (full fine-tuning + CoNLL-03 German Test-Split as Dev-Split)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=5.0e-6
* mini_batch_size=4
* max_epochs=10

### Train Results
#### train Single Corpus (Eng + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 93.79  ±  0.12
* F-score (macro) - Average: 92.49  ±  0.15
* Accuracy - Average: 90.72  ±  0.18
#### train Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 93.82  ±  0.1
* F-score (macro) - Average: 93.51  ±  0.11
* Accuracy - Average: 91.34  ±  0.11
### Test Results on Conll_03 German
#### test Single Corpus (Eng + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 77.02  ±  0.1
#### test Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 76.32  ±  0.99

## Phase 05 (full fine-tuning + CoNLL-03 German Test-Split as Dev-Split)
### Params:
* model='xlm-roberta-large'
* layers="-1"
* subtoken_pooling="first"
* fine_tune=True
* use_context=True
* hidden_size=256
* use_crf=False,
* use_rnn=False,
* reproject_embeddings=False
* learning_rate=5.0e-6
* mini_batch_size=4
* max_epochs=10

### Train Results
#### train Single Corpus (Dutch + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 94.68  ±  0.55
* F-score (macro) - Average: 94.71  ±  0.56
* Accuracy - Average: 92.9  ±  0.94
#### train Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split + max_epochs=5)
* F-score (micro) - Average: 93.49  ±  0.05
* F-score (macro) - Average: 93.15  ±  0.05
* Accuracy - Average: 90.72  ±  0.07
### Test Results on Conll_03 German
#### test Single Corpus (Dutch + Dev-Split => CoNLL-03 German Test-Split)
* F-score (micro) - Average: 74.9  ±  0.82
#### test Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split + max_epochs=5)
* F-score (micro) - Average: 76.47  ±  0.84
