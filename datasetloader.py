from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd

class DatasetLoader(ABC):

    def __init__(self, file_path:str):
        self.file_path = Path(file_path)

    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass

class CSVLoader(DatasetLoader):
    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

class JSONLoader(DatasetLoader):

    def load(self) -> pd.DataFrame:
        return pd.read_json(self.file_path)