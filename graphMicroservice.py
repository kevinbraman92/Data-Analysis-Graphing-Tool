import matplotlib.pyplot
import json
import sys


def create_graph(graph_settings):
    graph_type = graph_settings["graph_type"]
    x_label = graph_settings["x_label"]
    y_label = graph_settings["y_label"]
    values = graph_settings["values"]
    title = graph_settings["title"]
    if graph_type.lower() == 'bar':
        x_values = range(len(values))
        matplotlib.pyplot.bar(x_values, values)
    elif graph_type.lower() == 'line':
        x_values = range(len(values))
        matplotlib.pyplot.plot(x_values, values)

    matplotlib.pyplot.xlabel(x_label)
    matplotlib.pyplot.ylabel(y_label)
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    graph_settings = json.loads(sys.argv[1])
    create_graph(graph_settings)
