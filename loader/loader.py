from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd

class DatasetLoader(ABC):
    
    def __init__(self, file_path:str) ->None:
        self.file_path = Path(file_path)
    
    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass