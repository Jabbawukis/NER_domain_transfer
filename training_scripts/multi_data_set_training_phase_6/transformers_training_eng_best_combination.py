import sys
import flair
from flair.datasets import CONLL_03, CONLL_03_GERMAN
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

flair.device = f'cuda:{sys.argv[1]}'
corpus = CONLL_03()
corpus._dev = CONLL_03_GERMAN(base_path="../../model_test_scripts/CONLL_03_GER").test
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type)

combi_1 = [400, 6.0e-5]
combi_2 = [100, 8e-05]
for combination in [combi_1, combi_2]:
    for run in range(1, 4):
        mini_batch = combination[0]
        lr = combination[1]

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

        trainer.fine_tune(
            base_path=f'resources/taggers/conll_eng_ner_roberta_large_mini_batch_{mini_batch}_lr_{lr}_run_{run}_ger_test_as_dev',
            learning_rate=lr,
            max_epochs=10,
            mini_batch_size=mini_batch,
            monitor_test=True,
            mini_batch_chunk_size=4,
            )
        del tagger
        del trainer
        del embeddings
