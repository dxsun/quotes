from PyDictionary import PyDictionary as PyD 

dictionary = PyD()

def phrase_to_synonyms(phrase):
	garbage_words = ' '

	synonyms = set()
	phrase_array = phrase.split(' ')
	for word in phrase_array:
		if word not in garbage_words:
			syn = dictionary.synonym(word)
			try:
				synonyms.update(syn)
			except TypeError:
				pass

	return synonyms

