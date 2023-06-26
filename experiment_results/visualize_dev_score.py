import os
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def extract_f1_scores(log_file):
    f1_scores = []
    with open(log_file, 'r') as file:
        log_content = file.read()
        matches = re.findall(r'DEV : loss [0-9.]+ - f1-score \(micro avg\)  ([0-9.]+)', log_content)
        f1_scores = [float(score) for score in matches]
    return f1_scores


def calculate_average_f1_scores(f1_scores, epoch):
    epoch_scores = [scores[epoch - 1] for scores in f1_scores]
    average_score = sum(epoch_scores) / len(epoch_scores)
    return average_score


def plot_average_f1_scores(average_scores, model_names, num_epochs):
    epochs = range(1, num_epochs + 1)
    plt.figure(figsize=(10, 6))  # Adjust the figure size as desired
    for i in range(len(model_names)):
        plt.plot(epochs, average_scores[:, i], marker='o', label=model_names[i])
        # Add text annotations for each data point
        for j, score in enumerate(average_scores[:, i]):
            plt.text(epochs[j], score, str(round(score, 4)), ha='center', va='bottom')
    plt.xlabel('Epoch')
    plt.ylabel('Average Dev F1-score')
    plt.title('Average Dev (German Conll_03) F1-score at Each Epoch')
    plt.xlim(1, num_epochs)  # Set x-axis limits to ensure all epochs are depicted
    plt.xticks(rotation=0)  # Display x-axis tick labels horizontally
    plt.legend()
    plt.tight_layout()  # Adjust the layout to prevent labels from being cut off
    plt.show()


def process_log_files(directory_list):
    model_scores = []
    model_names = []
    for model in directory_list:
        f1_scores = []
        model_names.append(model[0])
        for file_name in os.listdir(model[1]):
            log_file = os.path.join(model[1], file_name)
            epoch_scores = extract_f1_scores(log_file)
            f1_scores.append(epoch_scores)
        model_scores.append(f1_scores)

    num_epochs = len(model_scores[0][0])
    average_scores = []
    for epoch in range(1, num_epochs + 1):
        scores = []
        for model_f1_scores in model_scores:
            scores.append(calculate_average_f1_scores(model_f1_scores, epoch))
        average_scores.append(scores)

    average_scores = np.array(average_scores)
    plot_average_f1_scores(average_scores, model_names, num_epochs)


directories: list[list[str, Path]] = [["Single Corpus (Eng + Dev-Split => CoNLL-03 German Test-Split)",
                                       "multi_data_set_conll_train_results/Phase_04/conll_eng_ner_roberta_large_training_phase_4/only_full_fine_tuning_ger_test_as_dev"],
                                      ["Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)",
                                       "multi_data_set_conll_train_results/Phase_04/conll_eng_dutch_ner_roberta_large_training_phase_4/only_full_fine_tuning_ger_test_as_dev"]]

process_log_files(directories)
