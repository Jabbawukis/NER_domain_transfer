
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

### Train Results
#### train Single Corpus (only Conll_03 Eng)
* F-score (micro) - Average: 93.88  ±  0.11
* F-score (macro) - Average: 92.65  ±  0.09
* Accuracy - Average: 90.74  ±  0.08
#### train Multi-Corpus (Eng/Dutch)
* F-score (micro) - Average: 93.73  ±  0.27
* F-score (macro) - Average: 93.42  ±  0.26
* Accuracy - Average: 91.09  ±  0.36
### Test Results on Conll_03 German
#### test Single Corpus (only Conll_03 Eng)
* F-score (micro) - Average: 77.08  ±  0.45
#### test Multi-Corpus (Eng/Dutch)
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

### Train Results
#### train Single Corpus (only Conll_03 Eng) linear probing (lr 0.8)
* F-score (micro) - Average: 77.76  ±  0.47
* F-score (macro) - Average: 76.0  ±  0.52
* Accuracy - Average: 67.4  ±  0.56
#### train Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.8)
* F-score (micro) - Average: 93.58  ±  0.2
* F-score (macro) - Average: 92.28  ±  0.21
* Accuracy - Average: 90.4  ±  0.23
#### train Multi-Corpus (Eng/Dutch) linear probing (lr 0.8)
* F-score (micro) - Average: 72.09  ±  0.22
* F-score (macro) - Average: 70.4  ±  0.27
* Accuracy - Average: 60.29  ±  0.25
#### train Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.8)
* F-score (micro) - Average: 93.95  ±  0.11
* F-score (macro) - Average: 93.65  ±  0.11
* Accuracy - Average: 91.54  ±  0.18
### Test Results on Conll_03 German
#### test Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.8)
* F-score (micro) - Average: 78.1  ±  0.95
#### test Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.8)
* F-score (micro) - Average: 76.75  ±  0.96

## Phase 02b (linear probing lr 0.3 + full fine-tuning) (lr 0.8)
### Params:
* ...
* learning_rate=0.3 (linear probing)
* ...

### Train Results
#### train Single Corpus (only Conll_03 Eng) linear probing (lr 0.3)
* F-score (micro) - Average: 77.99  ±  0.44
* F-score (macro) - Average: 76.25  ±  0.56
* Accuracy - Average: 67.61  ±  0.45
#### train Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.3)
* F-score (micro) - Average: 93.62  ±  0.17
* F-score (macro) - Average: 92.26  ±  0.21
* Accuracy - Average: 90.37  ±  0.26
#### train Multi-Corpus (Eng/Dutch) linear probing (lr 0.3)
* F-score (micro) - Average: 72.57  ±  1.05
* F-score (macro) - Average: 70.86  ±  1.04
* Accuracy - Average: 60.88  ±  1.32
#### train Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.3)
* F-score (micro) - Average: 94.04  ±  0.05
* F-score (macro) - Average: 93.73  ±  0.06
* Accuracy - Average: 91.6  ±  0.07
### Test Results on Conll_03 German
#### test Single Corpus (only Conll_03 Eng) full fine-tuning (lr 0.3)
* F-score (micro) - Average: 78.28  ±  0.47
#### test Multi-Corpus (Eng/Dutch) full fine-tuning (lr 0.3)
* F-score (micro) - Average: 76.55  ±  0.74

## Phase 03 (full fine-tuning + Bias Only training)
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

### Train Results
#### train Single Corpus (only Conll_03 Eng) BitFit

#### train Multi-Corpus (Eng/Dutch) BitFit

### Test Results on Conll_03 German
#### test Single Corpus (only Conll_03 Eng) BitFit

#### test Multi-Corpus (Eng/Dutch) BitFit

