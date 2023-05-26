import flair
from flair.datasets import CONLL_03, WNUT_17
from flair.embeddings import TransformerWordEmbeddings
from flair.models import TokenClassifier
from flair.nn.multitask import make_multitask_model_and_corpus
from flair.trainers import ModelTrainer

# transformer and learning rate
# transformer = 'distilbert-base-uncased' -> nur für english
# learning_rate = 5e-5

# for state-of-the-art use instead:
transformer = 'xlm-roberta-large'
learning_rate = 5e-5

flair.device = 'cuda:0'

for seed in [123]:
    flair.set_seed(seed)

    # load corpus 1
    corpus_1 = CONLL_03(in_memory=True,
                        column_format={0: "text", 3: "ner"},
                        )

    # load corpus 2
    corpus_2 = WNUT_17(in_memory=True,
                       )

    # shared embeddings
    shared_embeddings = TransformerWordEmbeddings(transformer, fine_tune=True, use_context=True)

    # 5. initialize bare-bones sequence tagger (no CRF, no RNN, no reprojection)
    conll_tagger = TokenClassifier(embeddings=shared_embeddings,
                                   label_dictionary=corpus_1.make_label_dictionary(label_type='ner'),
                                   label_type='ner',
                                   )

    # 5. initialize bare-bones sequence tagger (no CRF, no RNN, no reprojection)
    wnut_tagger = TokenClassifier(embeddings=shared_embeddings,
                                  label_dictionary=corpus_2.make_label_dictionary(label_type='ner'),
                                  label_type='ner',
                                  )

    # Define mapping (which tagger should train on which model)
    mapping = [
        (conll_tagger, corpus_1),
        (wnut_tagger, corpus_2),
    ]

    # create a multitask model and corpus from this mapping
    multitask_model, multicorpus = make_multitask_model_and_corpus(mapping)

    # train as alwys
    trainer = ModelTrainer(multitask_model, multicorpus)
    trainer.fine_tune(
        f"resources/taggers/multitask_ner/conll+wnut_{seed}",
        learning_rate=learning_rate,
        max_epochs=10,
        save_final_model=True, # can set this to False if you don't want to save the model
        monitor_test=True, # can set this to False to speed up training
    )
