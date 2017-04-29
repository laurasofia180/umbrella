from mongo import Mongo
from mrjob.job import MRJob
from pymongo import MongoClient
import re
import os
import collections

MONGO_SERVER = os.environ.get('MONGO_SERVER')
MONGO_SERVER_PORT = int(os.environ.get('MONGO_SERVER_PORT'))

class DB():
    def __init__(self):
        self.client = MongoClient (MONGO_SERVER, MONGO_SERVER_PORT)
        self.db = self.client ["Test"]
        self.index = self.db ["index"]

    def insert(self, word, file_paths):
    self.indexes.insert_one({"_id": word, "file_paths": file_paths})

    def search(self, word):
    return self.indexes.find_one({"_id": word})


WORD_RE = re.compile(r"[\w*]+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, doc):
	name = os.environ["map_input_file"]
	allnames = name.split('/')
	name = allnames[len(allnames)-1]
	H = {}
	for word in WORD_RE.findall(doc):
		H[word] = 0
	for word in WORD_RE.findall(doc):
		H[word] = H[word]+1
	for word in H:
		yield(word,(name,H[word]))

    def reducer(self, word, values):
	d = collections.defaultdict(int)
	a = []
	P = []
	for n,w in values:
	    if not n in a: a.append(n)
    	    d[n]+=w
	for f in a:
	    P.append([f,d[f]])
	P.sort(key=lambda x: x[1],reverse=True)

	top10 = []
	index = 0
	for p in P:
	    if index<10:
		top10.append(p)
	    else:
		break
	    index+=1;

        yield (word, top10)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
