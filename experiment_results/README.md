
# Experiments
## Multi-Data Set Training on Conll_03 Eng/Dutch -> test on Conll_03 German
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
#### Single Corpus (only Conll_03 Eng)
* F-score (micro) - Average: 93.88  ±  0.11
* F-score (macro) - Average: 92.65  ±  0.09
* Accuracy - Average: 90.74  ±  0.08
#### Multi-Corpus (Eng/Dutch)
* F-score (micro) - Average: 93.73  ±  0.27
* F-score (macro) - Average: 93.42  ±  0.26
* Accuracy - Average: 91.09  ±  0.36
### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng)
* F-score (micro) - Average: 77.08  ±  0.45
#### Multi-Corpus (Eng/Dutch)
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
#### Single Corpus (only Conll_03 Eng) linear probing

#### Single Corpus (only Conll_03 Eng) full fine-tuning

#### Multi-Corpus (Eng/Dutch) linear probing

#### Multi-Corpus (Eng/Dutch) full fine-tuning

### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng) full fine-tuning

#### Multi-Corpus (Eng/Dutch) full fine-tuning


## Phase 02b (linear probing lr 0.3 + full fine-tuning)
### Params:
* ...
* learning_rate=0.3 (linear probing)
* ...

### Train Results
#### Single Corpus (only Conll_03 Eng) linear probing

#### Single Corpus (only Conll_03 Eng) full fine-tuning

#### Multi-Corpus (Eng/Dutch) linear probing

#### Multi-Corpus (Eng/Dutch) full fine-tuning

### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng) full fine-tuning

#### Multi-Corpus (Eng/Dutch) full fine-tuning


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
#### Single Corpus (only Conll_03 Eng)

#### Multi-Corpus (Eng/Dutch)

### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng)

#### Multi-Corpus (Eng/Dutch)

