import json

class JSONReader:
    def __init__(self, file_path):
        with open(file_path) as json_file:
            self.json_data = json.load(json_file)
