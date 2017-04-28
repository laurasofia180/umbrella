from pymongo import MongoClient

class db ():
  def __init__(self):
        self.client = MongoClient('10.131.137.188')
        self.db = self.client ['Test']
