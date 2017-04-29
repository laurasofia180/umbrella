from pymongo import MongoClient

class db ():
  def __init__(self):
        self.client = MongoClient('10.131.137.188')
        self.db = self.client ['Test']
        self.db = client.test_database
        self.index = self.db["index"]

def insert(self, word, file_paths):
    self.index.insert_one({"_id": word, "file_paths": file_paths})

def search(self, word):
    return self.index.find_one({"_id": word})
