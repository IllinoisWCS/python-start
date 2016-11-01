import json
import matplotlib.pyplot as plt

'''
    The dataset we are using is a dataset of 200,000+ Jeopardy questions. It is a JSON file that consists of an array of objects.

    JSON stands for JavaScript Object Notation. It represents a dataset as a combinations of JavaScript objects and arrays. In our case, we have an array of Javascript Objects saved in this JSON file. To be more concrete, our file looks something like this:
    [
        {
            "category": "HISTORY",
            "air_date": "2004-12-31",
            "question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'",
            "value": "200",
            "answer": "Copernicus",
            "round": "Jeopardy!",
            "show_number": "4680"
        },
        ... << more questions of this same format
    ]

    Can you see any similarities? A JavaScript array is inherently no different in terms of structure than a Python array. A JavaScript object looks kind of like how we represented Python dictionaries in the previous exercises. In fact, when we read in the file using the Python libraries, it creates exactly what we expect. We create an array of Python dictionaries. Each dictionary in the array has the same set of keys, each key having its own custom value. So each dictionary now represents a Jeopardy question.
'''
class JSONExample:
    def __init__(self):
        self.items = self.import_data()

    '''
    This function, you don't have to edit. This is just to show you how we use the Python json library to read in the JSON file with the jeopardy questions into a Python array of Python dictionaries.
    '''
    def import_data(self):
        items = []
        file_dir = 'data/JeopardyData/jeopardy.json'
        with open(file_dir, 'r') as f:
            items = json.load(f)
        return items

    '''
    This function shows how to graph a histogram.

    We can access each item's individual value given a key. The key we're using here as an example is the value of the question (aka, how much money was awarded if answered correctly). We can then graph the distribution of the question values in a histogram.

    We create an array of all of the values. By specifying the number of bins, we specify how precise each range in the histogram is, from the minimum price to the maximum price.

    Note: Because value can be easily converted from a string to a valid integer, we can do the histogram. In other words, we can only graph histograms of numeric values.

    Some things you can try:
        - You can use this function to do the same histogram graphing for a key like show_number.
        - You can get a more accurate distribution by getting rid of outliers.
        - You can specify a date range and only look at the question value distribution. To determine date ranges, you might want to use these docs - https://docs.python.org/2/library/datetime.html
    '''
    def graph_data_histogram(self):
        attribute_values = []

        for item in self.items:
            value = item['value']
            if value is not None:
                attribute_values.append(int(value))

        plt.hist(attribute_values, bins=100)
        plt.title('Distribution of question values')
        plt.xlabel('value range')
        plt.ylabel('number of questions')
        plt.show()

