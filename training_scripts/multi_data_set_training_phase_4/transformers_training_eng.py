import sys
import flair
from flair.datasets import CONLL_03
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
import torch
from flair.optim import LinearSchedulerWithWarmup

flair.device = f'cuda:{sys.argv[1]}'
corpus = CONLL_03(base_path="CONLL_03_ENG_GER_combination")
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type)
for run in range(1, 4):
    embeddings = TransformerWordEmbeddings(model='xlm-roberta-large',
                                           layers="-1",
                                           subtoken_pooling="first",
                                           fine_tune=True,
                                           use_context=True,
                                           )
    tagger = SequenceTagger(hidden_size=256,
                            embeddings=embeddings,
                            tag_dictionary=label_dict,
                            tag_type=label_type,
                            use_crf=False,
                            use_rnn=False,
                            reproject_embeddings=False,
                            )

    trainer = ModelTrainer(tagger, corpus)

    trainer.train(base_path=f'resources/taggers/conll_eng_ner_roberta_large_run_{run}_ger_test_as_dev',
                  learning_rate=5.0e-6,
                  max_epochs=10,
                  optimizer=torch.optim.AdamW,
                  scheduler=LinearSchedulerWithWarmup,
                  warmup_fraction=0.1,
                  mini_batch_size=4,
                  embeddings_storage_mode="none",
                  use_final_model_for_eval=True,
                  monitor_test=True,
                  monitor_dev=True,
                  )
    del tagger
    del trainer
    del embeddings
