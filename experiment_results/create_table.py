from prettytable import PrettyTable


def extract_results(file_path, search_param, line_start_index):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = {}
    current_model = None

    for line in lines:
        line = line.strip()
        if line.startswith("#### ") and current_model:
            current_model = None
        if line.startswith(search_param):
            current_model = line[line_start_index:]
            results[current_model] = []
        elif current_model and (line.startswith("* A") or line.startswith("* F")):
            index = line.index(":")
            results[current_model].append(line[index + 2:])

    return results


def create_table(results):
    table = PrettyTable()
    table.field_names = ["Model", "F-score (micro)", "F-score (macro)", "Accuracy"]

    for model, entries in results.items():
        if entries:
            if len(entries) == 3:
                table.add_row([model] + entries)
            else:
                # Handle missing entries
                missing_entries = [""] * (3 - len(entries))
                table.add_row([model] + entries + missing_entries)
        else:
            # Handle empty models
            table.add_row([model, "", "", ""])

    return table


def write_table_to_file(tables, output_file):
    with open(output_file, 'w') as file:
        for table in tables:
            file.write(str(table))
            file.write("\n")


file_path = "README.md"

results = extract_results(file_path, "#### train", 11)
train_table = create_table(results)

results = extract_results(file_path, "#### test", 10)
test_table = create_table(results)

output_file = "TABLE.md"
write_table_to_file(["Train", train_table, "Test", test_table], output_file)
