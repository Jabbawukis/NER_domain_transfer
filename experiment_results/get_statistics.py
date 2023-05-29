import sys
import os
import re
import numpy as np

def find_values_in_file(file_path, main_score=False):
    with open(file_path, 'r') as file:
        content = file.read()
        if main_score:
            main_score_value = re.findall(r'Main Score: (\d+\.\d+)', content)
            return main_score_value
        fscore_micro = re.findall(r'F-score \(micro\) (\d+\.\d+)', content)
        fscore_macro = re.findall(r'F-score \(macro\) (\d+\.\d+)', content)
        accuracy = re.findall(r'Accuracy (\d+\.\d+)', content)
        return fscore_micro, fscore_macro, accuracy

def find_values_in_directory(directory_path, main_score=False):
    fscore_micro_values = []
    fscore_macro_values = []
    accuracy_values = []
    main_score_values = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if main_score:
                main_score_values.extend(find_values_in_file(file_path, True))
            else:
                fscore_micro, fscore_macro, accuracy = find_values_in_file(file_path)
                fscore_micro_values.extend(fscore_micro)
                fscore_macro_values.extend(fscore_macro)
                accuracy_values.extend(accuracy)

    if main_score:
        return main_score_values
    return fscore_micro_values, fscore_macro_values, accuracy_values

def calculate_statistics(values):
    values = [round(float(value) * 100, 2) for value in values]
    average = round(np.mean(values), 2)
    std_deviation = round(np.std(values), 2)
    return average, std_deviation

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path> [--main]")
        return

    directory_path = sys.argv[1]

    if len(sys.argv) == 3 and sys.argv[2] == "--main":
        main_score_values = find_values_in_directory(directory_path, True)
        if not main_score_values:
            print("No matching lines found in the directory.")
            return
        main_score_avg, main_score_std = calculate_statistics(main_score_values)
        print("* F-score (micro) - Average:", main_score_avg, " ± ", main_score_std)
    else:
        fscore_micro_values, fscore_macro_values, accuracy_values = find_values_in_directory(directory_path)

        if not fscore_micro_values and not fscore_macro_values and not accuracy_values:
            print("No matching lines found in the directory.")
            return

        fscore_micro_avg, fscore_micro_std = calculate_statistics(fscore_micro_values)
        fscore_macro_avg, fscore_macro_std = calculate_statistics(fscore_macro_values)
        accuracy_avg, accuracy_std = calculate_statistics(accuracy_values)

        print("* F-score (micro) - Average:", fscore_micro_avg, " ± ", fscore_micro_std)
        print("* F-score (macro) - Average:", fscore_macro_avg, " ± ", fscore_macro_std)
        print("* Accuracy - Average:", accuracy_avg, " ± ", accuracy_std)


if __name__ == '__main__':
    main()
