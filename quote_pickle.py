# Quote pickler
import pickle

with open('raw_quotes.txt', 'r') as f:
	quotes = f.readlines()
	quotes.insert(0,0)
	pickle.dump(quotes, open('raw_quotes.p', 'wb'))

