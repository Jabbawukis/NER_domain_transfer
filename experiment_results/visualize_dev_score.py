import os
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def extract_f1_scores(log_file):
    f1_scores = []
    with open(log_file, 'r') as file:
        log_content = file.read()
        matches = re.findall(r'DEV : loss [0-9.]+ - f1-score \(micro avg\)  ([0-9.]+)', log_content)
        f1_scores = [float(score) for score in matches]
    return f1_scores


def calculate_average_f1_scores(f1_scores, epoch):
    epoch_scores = [scores[epoch] for scores in f1_scores]
    average_score = sum(epoch_scores) / len(epoch_scores)
    return average_score


def calculate_std_scores(f1_scores, epoch):
    epoch_scores = [scores[epoch] for scores in f1_scores]
    std_score = np.std(epoch_scores)
    return std_score


def plot_average_f1_scores(average_scores, std_scores, model_names, include_std=False):
    num_models = len(model_names)
    max_epochs = len(average_scores[0])
    epochs = range(1, max_epochs + 1)

    plt.figure(figsize=(12, 6))

    if include_std:
        for i in range(num_models):
            model_scores = average_scores[i]
            model_std = std_scores[i]
            plt.errorbar(
                epochs,
                model_scores,
                yerr=model_std,
                marker='o',
                linestyle='None',
                label=model_names[i],
                capsize=3,
            )
            plt.plot(
                epochs,
                model_scores,
                marker='o',
                linestyle='-',
                color='black',
                alpha=0.6,
            )
            plt.fill_between(
                epochs,
                model_scores - model_std,
                model_scores + model_std,
                color='red',
                alpha=0.2,
            )
            for j in range(max_epochs):
                plt.text(j + 1, model_scores[j], str(round(model_scores[j], 4)), ha='center', va='bottom')
                plt.text(j + 1, model_scores[j] - model_std[j], str(round(model_std[j], 4)), ha='center', va='top')
    else:
        for i in range(num_models):
            model_scores = average_scores[i]
            plt.plot(epochs, model_scores, marker='o', label=model_names[i])
            for j in range(max_epochs):
                plt.text(j + 1, model_scores[j], str(round(model_scores[j], 4)), ha='center', va='bottom')

    plt.xlabel('Epoch')
    plt.ylabel('Average Dev F1-score')
    plt.title('Average Dev (German Conll_03) F1-score at Each Epoch')
    plt.xticks(epochs)
    plt.legend()
    plt.tight_layout()
    plt.show()


def process_log_files(directory_list, include_std=False):
    model_scores = []
    model_names = []
    max_epochs = 0
    for model in directory_list:
        f1_scores = []
        model_names.append(model[0])
        max_model_epochs = 0
        for file_name in os.listdir(model[1]):
            log_file = os.path.join(model[1], file_name)
            epoch_scores = extract_f1_scores(log_file)
            f1_scores.append(epoch_scores)
            max_model_epochs = max(max_model_epochs, len(epoch_scores))
        model_scores.append(f1_scores)
        max_epochs = max(max_epochs, max_model_epochs)

    average_scores = []
    std_scores = []
    for model_f1_scores in model_scores:
        model_average_scores = []
        model_std_scores = []
        for epoch in range(max_epochs):
            try:
                s = calculate_average_f1_scores(model_f1_scores, epoch)
                model_average_scores.append(s)
                std = calculate_std_scores(model_f1_scores, epoch)
                model_std_scores.append(std)
            except IndexError:
                continue
        # Pad the model_average_scores with NaN to make them of equal length
        model_average_scores += [np.nan] * (max_epochs - len(model_average_scores))
        model_std_scores += [np.nan] * (max_epochs - len(model_std_scores))
        average_scores.append(model_average_scores)
        std_scores.append(model_std_scores)

    average_scores = np.array(average_scores)
    std_scores = np.array(std_scores)
    plot_average_f1_scores(average_scores, std_scores, model_names, include_std=include_std)


directories: list[list[str, Path]] = [["Multi-Corpus (Eng+Dutch + Dev-Split => CoNLL-03 German Test-Split)",
                                       "multi_data_set_conll_train_results/Phase_04/conll_eng_dutch_ner_roberta_large_training_phase_4/only_full_fine_tuning_ger_test_as_dev"],

                                      ]

process_log_files(directories, include_std=True)
