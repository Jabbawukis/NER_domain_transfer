import sys
from flair.models import SequenceTagger
from flair.datasets import CONLL_03_GERMAN

corpus = CONLL_03_GERMAN(base_path="CONLL_03_GER")
roberta_tagger = SequenceTagger.load(sys.argv[1])

# roberta_tagger.embeddings.fine_tune = True
# roberta_tagger.embeddings.static_embeddings = False

test_results = roberta_tagger.evaluate(data_points=corpus.test,
                                       gold_label_type="ner",
                                       out_path=sys.argv[2])
print(f"Main Score: {test_results.main_score}")
with open(sys.argv[2], 'r') as original: data = original.read()
with open(sys.argv[2], 'w') as modified: modified.write(f"Main Score: {test_results.main_score}\n" + data)
