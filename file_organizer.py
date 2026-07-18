import os
from pathlib import Path
from collections import Counter
import shutil
import json

def main():
    while True:
        show_menu()
        file=input("Enter folder name to be scanned")
        scan_directory(file)

def show_menu():
    print("1. scan directory")
    print("2. categorize files")
    print("3. create folder")
    print("4. move file")
    print("5. load config")
    print("6. save_log")
    print("7. Exit")
    choice = int(input("Enter the choice"))
    if choice == 1:
        inp
        scan_directory()


def scan_directory(file):
    print(os.listdir())

def categorize_files(folder):
    for file in folder:
        ext=os.path.splitext()
        if ext == ".txt" or ".csv" or ".md":
            return "Plain text"
        elif ext == ".docx" or ".pdf" or ".odt" or ".rtf":
            return "Formatted Text"
        elif ext == ".html" or ".xml" or ".json":
            return "Web"
        elif ext == ".jpg/" or ".jpeg" or ".png" or ".gif" or ".tiff" or ".webp" or ".svg" or ".eps" or ".ai":
            return "Image"
        elif ext == ".mp4" or ".mov" or ".mkv" or ".avi" or ".webm":
            return "video"
        elif ext == ".mp3" or ".wav" or ".flac" or ".aac":
            return "video"
        elif ext == ".zip" or ".rar" or ".7z" or ".tar":
            return "compressed data"
        elif ext == ".xlsx" or ".sqlite" or ".dbf" or ".sql":
            return "spredsheet & databases"
        elif ext == ".exe" or ".msi" or ".app" or ".dmg":
            return "executable or system file"
        elif ext == ".py" or ".js" ".c" or ".cpp" or ".sh":
            return "Scripts/code"

def create_folder():
    input_name=input("name of folder")
    folder=Path(input_name)
    folder.mkdir(exists_ok=True)

def move_file(source, destination):
    path=Path(destination)
    shutil.move(source, path)
    category = categorize_files(source)
    save_log(f"Moved {source} to {category}")

def load_config():
    with open("config.json", "r") as file:
        config=json.load()
    return config

def save_log(message):
    with open("organizer.log", "a") as file:
        file.write(message + "\n")
    

def undo_last_operation():
    pass