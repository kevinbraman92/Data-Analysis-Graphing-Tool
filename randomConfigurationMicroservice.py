import subprocess
import json


def call_micro_random(lower, upper):
    result = subprocess.run(['python', 'microRandom.py', str(lower), str(upper)], stdout=subprocess.PIPE, text=True)
    return int(result.stdout.strip())


def generate_random_settings():
    graph_types = ['bar', 'line']
    x_labels = ['Time', 'Category', 'Type']
    y_labels = ['Value', 'Count', 'Percentage']
    graph_type = graph_types[call_micro_random(0, len(graph_types) - 1)]
    x_label = x_labels[call_micro_random(0, len(x_labels) - 1)]
    y_label = y_labels[call_micro_random(0, len(y_labels) - 1)]
    lower_bound = call_micro_random(1, 50)
    upper_bound = call_micro_random(lower_bound + 1, lower_bound + 100)
    num_values = call_micro_random(3, 100)
    values = [call_micro_random(lower_bound, upper_bound) for numbers in range(num_values)]
    graph_settings = {
        "graph_type": graph_type,
        "title": f"Your random {graph_type} graph",
        "x_label": x_label,
        "y_label": y_label,
        "values": values
    }
    return graph_settings


if __name__ == "__main__":
    settings = generate_random_settings()
    print(json.dumps(settings))
