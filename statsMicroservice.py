import sys
import pandas
import json


def summary_statistics(data):
    data = pandas.DataFrame(data)
    pandas.options.display.float_format = '{:,.2f}'.format
    return data.describe()


if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    statistics = summary_statistics(data)
    print(statistics)
