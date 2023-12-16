import argparse
from pathlib import Path

from model import Connection
import dags.scripts.config as config

# Initialize directory and csv file
# create them if does not exist programatically
def init_csv_file():
    pass

# Initialize schema and table
def init_db():
    # Establish a db connection
    # get db session
    # create a schema named raw
    # create users table in schema raw with appropiate columns
    # commit db
    # close db
    pass


if __name__ == '__main__':
    init_csv_file()
    init_db()
