
# Experiments
## Multi-Data Set Training on Conll_03 Eng/Dutch -> test on Conll_03 German
## Phase 01
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
* F-score (micro) - Average: 93.77  ±  0.07
* F-score (macro) - Average: 92.46  ±  0.16
* Accuracy - Average: 90.62  ±  0.08
#### Multi-Corpus (Eng/Dutch)
* F-score (micro) - Average: 93.75  ±  0.04
* F-score (macro) - Average: 93.45  ±  0.04
* Accuracy - Average: 91.11  ±  0.07
### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng)
* F-score (micro) - Average: 75.86  ±  0.73
#### Multi-Corpus (Eng/Dutch)
* F-score (micro) - Average: 74.93  ±  1.32

## Phase 02
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
* F-score (micro) - Average: 77.39  ±  0.68
* F-score (macro) - Average: 75.74  ±  0.94
* Accuracy - Average: 66.78  ±  0.85
#### Single Corpus (only Conll_03 Eng) full fine-tuning
* F-score (micro) - Average: 93.52  ±  0.12
* F-score (macro) - Average: 92.18  ±  0.06
* Accuracy - Average: 90.27  ±  0.27
#### Multi-Corpus (Eng/Dutch) linear probing
* F-score (micro) - Average: 72.26  ±  0.67
* F-score (macro) - Average: 70.64  ±  0.77
* Accuracy - Average: 60.62  ±  0.86
#### Multi-Corpus (Eng/Dutch) full fine-tuning
* F-score (micro) - Average: 93.83  ±  0.12
* F-score (macro) - Average: 93.54  ±  0.13
* Accuracy - Average: 91.36  ±  0.18
### Test Results on Conll_03 German
#### Single Corpus (only Conll_03 Eng) full fine-tuning
* F-score (micro) - Average: 78.42  ±  0.39
#### Multi-Corpus (Eng/Dutch) full fine-tuning
* F-score (micro) - Average: 77.25  ±  0.39
