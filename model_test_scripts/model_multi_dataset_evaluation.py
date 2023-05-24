import sys
from flair.nn import Classifier
from flair.datasets import CONLL_03_GERMAN


corpus = CONLL_03_GERMAN(base_path="CONLL_03_GER")
roberta_tagger = Classifier.load(sys.argv[1])
roberta_tagger.evaluate(data_points=corpus.test,
                        gold_label_type="tag_type",
                        out_path=".")
