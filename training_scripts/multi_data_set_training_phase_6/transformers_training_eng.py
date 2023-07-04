import sys
import flair
from flair.datasets import CONLL_03, CONLL_03_GERMAN
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
import torch
from flair.optim import LinearSchedulerWithWarmup

flair.device = f'cuda:{sys.argv[1]}'
corpus = CONLL_03()
corpus._dev = CONLL_03_GERMAN(base_path="../../model_test_scripts/CONLL_03_GER").test
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type)

mini_batches = [40, 400]
learning_rates = [1.0e-5, 1.0e-4]

for mini_batch in mini_batches:
    for lr in learning_rates:
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

        trainer.train(base_path=f'resources/taggers/conll_eng_ner_roberta_large_mini_batch_{mini_batch}_lr_{lr}_ger_test_as_dev',
                      learning_rate=lr,
                      max_epochs=10,
                      optimizer=torch.optim.AdamW,
                      scheduler=LinearSchedulerWithWarmup,
                      warmup_fraction=0.1,
                      mini_batch_size=mini_batch,
                      embeddings_storage_mode="none",
                      use_final_model_for_eval=True,
                      monitor_test=True,
                      )
        del tagger
        del trainer
        del embeddings
