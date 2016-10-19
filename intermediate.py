import csv

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


    You may find some help from these docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    '''

    def dictionary_exercise(self, book_index, topic1, topic2):
        return False


    '''
    .CSV exercise
    (CSV files are like raw versions of Excel files, they are tabulated using commas and new lines)

    One awesome part about Python and many other languages is that it can import in files to parse data and return information.

    For example, if we had a file that contained your grades history from high school, you would be able to calculate metrics such as your GPA by just specifying what file to use.

    In this case, I want you to calculate the GPA of files that are in the format
    [ClassName, Grade]

    Our parameter, csvfile, is a string that has the file name. In order to access its contents, you'll have to open the file to expose a file object. Then, you'll have to create a csv reader object and read the file line-by-line.

    You may find some help from these docs:
        - with open('filename', 'r') as f
        - csv reader objects and their available functions - https://docs.python.org/2/library/csv.html
    '''

    def calculate_GPA_CSV(self, csvfile):
        return False

    '''
    In data science, we not only want to know the average, the median, the maximum and the minimum of a set of numbers that we're given, but also, how much that data varies.

    We use the concept of variance and standard deviation. Variance is a numeric measure of the average difference between elements of the list of numbers. [TODO: Add in more detail] Taking the square root of variance yields a measure called standard deviation.

    With the mean and standard deviation, we can then designate a z-score for a certain element. [TODO: Add in more detail] [TODO: Add in more detail about percentile]

    In this case, we give a csvfile that has the following format: [TODO: Obtain this file]
    [Country, GDP]

    Using the CSV parsing techniques you've learned above, fill in the functions below that calculate the following statistics about countries and their GDP values
    - Average GDP
    - Median GDP
    - Max GDP and which country has that GDP
    - Min GDP and which country has that GDP
    - Variance
    - Standard Deviation
    - Which Percentile the following countries fall under with their GDP
        - USA
        - Ecuador
        - Luxembourg
        - Nigeria
        - Thailand
        - Any country of your choosing

    Hints:
        - [TODO: insert links about variance, standard deviation, etc.]
    '''

    def calculate_statistics(self, gdpfile):
        # Default values are set for now. You'll want to change these!
        average = 0
        median = 0

        max_gdp = 0
        min_gdp = 0
        country_with_highest_gdp = "USA"
        country_with_lowest_gdp = "USA"

        variance = 0
        standard_deviation = 0

        # We'll create a dictionary to hold the percentiles mapped to their respective countries
        countries_to_examine_percentiles = { "USA": 0, "Ecuador": 0, "Luxembourg": 0, "Nigeria": 0, "Thailand": 0 }

        return average, median, max_gdp, min_gdp, country_with_highest_gdp, country_with_lowest_gdp, variance, standard_deviation, countries_to_examine_percentiles