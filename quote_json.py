# Quote pickler
import json

with open('raw_quotes.txt', 'r') as f:
	quotes = f.readlines()
	quotes.insert(0,0)
	json.dump(quotes, open('raw_quotes.json', 'w'))
