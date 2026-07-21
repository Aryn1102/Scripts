from csv_loader import CSVLoader
from json_loader import JSONLoader

csv_loader = CSVLoader("train.csv")
csv_df = csv_loader.load()

json_loader = JSONLoader("train.json")
json_df = json_loader.load()