from loader import DatasetLoader
import pandas as pd

class JSONLoader(DatasetLoader):
    def load(self) -> pd.DataFrame:
        return pd.read_json(self.file_path)
