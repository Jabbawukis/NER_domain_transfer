import sys
import flair
from flair.data import MultiCorpus
from flair.datasets import CONLL_03_DUTCH, CONLL_03
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
flair.device = f'cuda:{sys.argv[1]}'
corpus = MultiCorpus([CONLL_03_DUTCH(), CONLL_03()]) # -> removed .downsample(0.1)
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type)
embeddings = TransformerWordEmbeddings(model='xlm-roberta-large',
                                       layers="-1",
                                       subtoken_pooling="first",
                                       fine_tune=True,
                                       use_context=True,
                                       )
for run in range(1, 4):
    tagger = SequenceTagger(hidden_size=256,
                            embeddings=embeddings,
                            tag_dictionary=label_dict,
                            tag_type=label_type,
                            use_crf=False,
                            use_rnn=False,
                            reproject_embeddings=False,
                            )

    trainer = ModelTrainer(tagger, corpus)

    trainer.fine_tune(f'resources/taggers/conll_eng_dutch_ner_roberta_large_run_{run}',
                      learning_rate=5.0e-6,
                      mini_batch_size=4,
                      )
    del tagger
    del trainer