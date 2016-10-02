'''
This time, let's pick our own csv data sets and visualize them!

Download either the Netflix or the Mashable dataset to get started
'''

from matplotlib import pyplot as plt
import csv

'''
What I want you to do is take the data and visualize the data in 
a useful way to show off data and interesting information
'''
class Advanced:
    def __init__(self):
        self.headers, self.rows = self.import_data()

    '''
    You don't have to edit this function unless you want to.
    It takes the file and reads each line to store it into
    two variables which you can then manipulate and read.
    '''
    def import_data(self):
        result = []

        # change this with the location of your data file
        file_dir = '../data/OnlineNewsPopularity/OnlineNewsPopularity.csv'
        with open(file_dir, 'rb') as f:
            reader = csv.reader(f)
            headers = reader.next()
            print headers
            for line in reader:
                # let's store the line data into a python data structure
                result.append(line)

            return headers, result

    '''
    Let's take two variables from the data and graph them. On the x-axis, 
    use `timedelta` which has older links as larger numbers (submitted longer ago),
    and on the y-axis let's graph 

    Edit the following function to accomplish this
    '''
    def graph_data(self):

        # these indices are which column the data is stored in in the csv file

        x_axis_index = 1
        y_axis_index = 10

        plt.xlabel(self.headers[x_axis_index])
        plt.ylabel(self.headers[y_axis_index])


        x_axis_values = []
        y_axis_values = []

        for row in self.rows:
            x_axis_values.append(row[x_axis_index])
            y_axis_values.append(row[y_axis_index])
        plt.plot(x_axis_values, y_axis_values)
        plt.show()

        return

    '''
    Now try to find out the average number of images in a post. This
    information could be interesting because maybe there's a certain
    number of images that statistically has the most amount
    of shares.
    '''
    def get_average_images(self):
        return
