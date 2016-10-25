import csv
import sys

class Intermediate:
    '''
    This exercise should get you warmed up on how the data structure `dictionary` can be used

    Dictionaries, or hashmaps, allow for a way to associate a 'key' with a 'value'. Imagine it like an index of a textbook. You know what topic you want to look for (the key), and you want a list of where it can be found (the value).

    For this exercise, I want you to take the idea of a book index and check to find what pages two different topics are both on. For example, if our book index looked like:
        apples: [2, 5, 64, 66, 70]
        oranges: [3, 6, 63, 64, 70]
        grapes: [3, 4, 5, 50, 64]

    and we called the function with 'apples' and 'oranges' as our topics, the function should return
    [64, 70]
    If one of the topics queried is not in the book_index, you should return False for now.


    You may find some help from these docs:
        - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    '''

    def dictionary_exercise(self, book_index, topic1, topic2):
        pages_topic1 = book_index[topic1]
        pages_topic2 = book_index[topic2]
        shared_pages = []
        for elem1 in pages_topic1:
            if elem1 in pages_topic2:
                shared_pages.append(elem1)
        for elem2 in pages_topic2:
            if elem2 in pages_topic1 and elem2 not in shared_pages:
                shared_pages.append(elem2)
        if len(shared_pages) > 0:
            return shared_pages
        return False


    '''
    .CSV exercise
    (CSV files are like raw versions of Excel files, they are tabulated using commas and new lines)

    One awesome part about Python and many other languages is that it can import in files to parse data and return information.

    For example, if we had a file that contained your grades history from high school, you would be able to calculate metrics such as your GPA by just specifying what file to use.

    In this case, I want you to calculate the GPA of files that are in the format
    [ClassName, Grade]

    Our parameter, csvfile, is a string that has the file name. In order to access its contents, you'll have to open the file to expose a file object. Then, you'll have to create a csv reader object and read the file line-by-line.

    Our tests use the following scale. Assume all classes are 1 credit hour.
    - A/A+ - 4.0
    - A- - 3.7
    - B+ - 3.3
    - B - 3.0
    - B- - 2.7
    - C+ - 2.3
    - C - 2.0
    - C- - 1.7
    - D+ - 1.3
    - D - 1.0
    - F - 0.0

    You may find some help from these docs:
        - with open('filename', 'r') as f
        - csv reader objects and their available functions - https://docs.python.org/2/library/csv.html
    '''

    def calculate_GPA_CSV(self, csvfile):
        # This is a default return value for this function. You'll want to change this!
        return 0

    '''
    In data science, we not only want to know the average, the median, the maximum and the minimum of a set of numbers that we're given, but also, how much those numbers vary.

    For this exercise, I'll refer to the array of numbers as our data. Each number in that array is called a data point.

    We use the concept of variance and standard deviation. Variance, intuitively, gives us a sense of how far apart data points are from the average. If variance is small, then we can say that our data is mostly centered around the average and our average actually is very representative of all data points. However, if variance is quite large, then we cannot say that. Our data varies way too much for our average to be representative.

    You can calculate the variance via 3 steps.
    1. Find the mean (or average).
    2. For each data point, calculate its difference from the mean. Square this difference.
    3. Sum all of the differences you find.

    Taking the square root of variance yields a measure called standard deviation. Standard deviation is also a measure of how spread out our data points are. It is more often used by statisticians and data scientists to describe the spread of data points.

    In this case, we give a csvfile that has the following format:
    [Country, GDP]

    You'll need to use similar techniques above to read this file and it's values.

    Using the CSV parsing techniques you've learned above, fill in the functions below that calculate the following statistics about countries and their GDP values
    - Average GDP
    - Max GDP and which country has that GDP
    - Min GDP and which country has that GDP
    - Variance
    - Standard Deviation

    Hints:
        - More reading on standard deviation and variance: http://www.mathsisfun.com/data/standard-deviation.html
        - If you're interested in where this data came from: http://data.worldbank.org/indicator/NY.GDP.MKTP.CD
        - sys.float_info.max (sys is already imported for you)
        - You'll want to store the GDP values you encounter while reading the CSV file into an array to calculate the variance - array.append
    '''

    def calculate_statistics(self, gdpfile):
        # Default values are set for you
        average = 0

        max_gdp = 0
        min_gdp = sys.float_info.max
        country_with_highest_gdp = 'USA'
        country_with_lowest_gdp = 'USA'

        variance = 0
        standard_deviation = 0

        # Insert your code here!

        return average, max_gdp, min_gdp, country_with_highest_gdp, country_with_lowest_gdp, variance, standard_deviation