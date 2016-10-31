import json
import matplotlib.pyplot as plt

'''
    The dataset we are using is a dataset of 200,000+ Jeopardy questions. It is a JSON file that consists of an array of objects. An object is simply a set of key-value pairs. It can be viewed as a dictionary.

    An example of one entry in the array of Jeopardy questions is:

    {
        "category": "HISTORY",
        "air_date": "2004-12-31",
        "question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'",
        "value": "$200",
        "answer": "Copernicus",
        "round": "Jeopardy!",
        "show_number": "4680"
    }
'''
class JSONExample:
    def __init__(self):
        self.items = self.import_data()

    # TODO: documentation about what data looks like internally - array of dictionaries, each dictionary having the key-value pairs listed above
    def import_data(self):
        items = []
        file_dir = 'data/JeopardyData/jeopardy.json'
        with open(file_dir, 'r') as f:
            items = json.load(f)
        return items

    # TODO: documentation on how to access attributes of an object within the data array
    def graph_data_histogram(self, attribute):
        attribute_values = dict()

        for item in self.items:
            value = item[attribute]
            if value not in attribute_values:
                attribute_values[value] = 0
            attribute_values[value] += 1

        labels = []
        y = []
        for value in attribute_values.keys():
            labels.append(value)
            y.append(attribute_values[value])

        plt.hist(xrange(len(labels)), y, width=1.0, align="center", label=labels)
        plt.show()
