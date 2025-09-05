import os 
import sys 
from src.MLProject.exception import CustomException
from src.MLProject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        logging.info("Connection established successfully", mydb)
        df = pd.read_sql_query("Select * from studentsperformance", mydb)
        print(df.head())

        return df


    except Exception as ex:
        raise CustomException(ex, sys)
