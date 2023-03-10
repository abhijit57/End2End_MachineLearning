import os, sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # Used to create class variables


# Using dataclass, allows us to directly define your class variables; (dataclass decorator comes in handy when only defining variables)
@dataclass   
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")   # data ingestion component's output will be stored in the artifacts folder
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "raw.csv")


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()   # train test raw data paths get saved inside this class variable -> ingestion_config

    def initiate_data_ingestion(self):
        '''
        Helps read data from databases or any data source
        '''
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except:
            pass
        

if __name__ == "__main__":

    di_obj = DataIngestion()
    di_obj.initiate_data_ingestion()


