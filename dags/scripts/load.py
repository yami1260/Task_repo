import csv

from model import Connection, Users
import dags.scripts.config as config

def get_file_path():
    # should return a os file path with correct destination.
    # Do not change file name
    # filename = "random_user.csv"
    # write your code here
    filepath = ''
    return filepath

def main():
    filename = get_file_path()
    data_insert = []

    # read the csv file
    # Create user object
    # insert the user object in the array
    with open(filename, encoding='utf-8') as csvf:
        pass

    # Connect with the db
    # get a sessions
    # First delete all previous users table data from schema raw
    # bulk load data
    # commit db
    # close db
    # write your code here

if __name__ == '__main__':
    main()
