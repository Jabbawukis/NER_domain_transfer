import sys
import flair
from flair.datasets import CONLL_03
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

flair.device = f'cuda:{sys.argv[1]}'
corpus = CONLL_03()
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type)
for run in range(1, 4):
    embeddings = TransformerWordEmbeddings(model='xlm-roberta-large',
                                           layers="-1",
                                           subtoken_pooling="first",
                                           fine_tune=False,
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

    trainer.fine_tune(f'resources/taggers/conll_eng_ner_roberta_large_run_{run}_linear_probing',
                      learning_rate=0.8,
                      mini_batch_size=32,
                      )
    del tagger
    del trainer
    del embeddings

    finished_tagger = SequenceTagger.load(f'resources/taggers/conll_eng_ner_roberta_large_run_{run}_linear_probing/final-model.pt')
    finished_tagger.embeddings.fine_tune = True
    finished_tagger.embeddings.static_embeddings = False
    new_trainer = ModelTrainer(finished_tagger, corpus)
    new_trainer.fine_tune(f'resources/taggers/conll_eng_ner_roberta_large_run_{run}_full_fine_tuning',
                          learning_rate=5.0e-6,
                          mini_batch_size=4,
                          )

    del finished_tagger
    del new_trainer
