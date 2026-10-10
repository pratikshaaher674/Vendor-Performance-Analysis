import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Set the working directory
os.chdir(r'C:\Users\GOKUL')

# Create logs folder automatically
os.makedirs(r'C:\Users\GOKUL\data\logs', exist_ok=True)

logging.basicConfig(
    filename=r'C:\Users\GOKUL\data\logs\ingestion_db.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine = create_engine(r'sqlite:///C:\Users\GOKUL\data\inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists= 'replace', index = False)
    
def load_raw_data():
    '''this functions will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('--------------Ingestion Complete------------')


    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()
    