import sys

import flair
from flair.models import SequenceTagger
from flair.datasets import CONLL_03_GERMAN


def evaluate_model_and_write_to_file(path_to_model, test_file_name):
    corpus = CONLL_03_GERMAN(base_path="CONLL_03_GER")
    roberta_tagger = SequenceTagger.load(path_to_model)
    test_results = roberta_tagger.evaluate(data_points=corpus.test,
                                           gold_label_type="ner",
                                           out_path=test_file_name)
    print(f"Main Score: {test_results.main_score}")
    with open(test_file_name, 'r') as original: data = original.read()
    with open(test_file_name, 'w') as modified: modified.write(f"Main Score: {test_results.main_score}\n" + data)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 model_multi_dataset_evaluation.py <path_to_models> <model_name> <cuda_device>")
        return
    flair.device = f'cuda:{sys.argv[3]}'
    for i in range(1, 4):
        path = f"{sys.argv[1]}/{sys.argv[2].format(run = i)}"
        model_name = f"{sys.argv[2].format(run = i)}_test_ger"
        evaluate_model_and_write_to_file(path, model_name)


if __name__ == '__main__':
    main()
