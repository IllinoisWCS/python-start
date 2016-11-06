'''
This time, let's pick our own csv data sets and visualize them!

Download the Mashable dataset to get started
'''

import matplotlib.pyplot as plt
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
        file_dir = 'data/OnlineNewsPopularity/OnlineNewsPopularity.csv'
        with open(file_dir, 'rb') as f:
            reader = csv.reader(f)
            headers = reader.next()
            print headers
            for line in reader:
                # let's store the line data into a python data structure
                result.append(line)

            return headers, result

    '''
    This function takes two variables from the data and graphs them. We pass in two indices, both indicate columns of the data as stored in the csv file. Refer to OnlineNewsPopularity.names to see what index maps to what column. Remember, the indices start with 0.

    If you were to run this function without passing any parameters in, it won't fail! It will simply produce the default graph because of the default values we've set for each index. We've set the default value on the x-axis to be the index for `timedelta` which has larger numbers for older links (because they were submitted longer ago). We've set the default value on the y-axis to be the index for `num_videos`. Feel free to run this function without any parameters and check out the graph.
    '''

    def graph_data(self, x=1, y=10):

        # these indices are which column the data is stored in in the csv file

        x_axis_index = x
        y_axis_index = y

        plt.xlabel(self.headers[x_axis_index])
        plt.ylabel(self.headers[y_axis_index])


        x_axis_values = []
        y_axis_values = []

        for row in self.rows:
            x_axis_values.append(row[x_axis_index])
            y_axis_values.append(row[y_axis_index])
        plt.plot(x_axis_values, y_axis_values)
        plt.show()

    '''
    Now try to find out the average number of images in a post. This information could be interesting because maybe there's a certain number of images that statistically has the most amount of shares.

    You can use graph_data to accomplish this, or if you want to try out other graph types or styles, feel free to copy graph_data over and see what you can come up with.

    You might want to check out these docs: http://matplotlib.org/api/pyplot_api.html
    '''
    def get_average_images(self):
        return