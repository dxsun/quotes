# Tag extractor + jsonizer
import json

def tags_to_dict(file_name):
	"""
	Converts tags for all quotes into one dictionary.

	Input:
		file_name (str): File where each line contains comma-separated keys (line number
					 	 corresponds to quote number)

	Output:
		Dict{str:tuple(int)}: Key is a tag and value is a tuple of quote numbers
							  that correspond to that tag
	"""
	tag_file = open(file_name,'r')
	output = dict()

	for num in range(1,366):
		tags = tag_file.readline().split(',')
		for tag in tags:
			if(tag in output):
				temp = output[tag]
				output[tag] = temp+(num,)
			else:
				output[tag] = num

	return output

tagz = tags_to_dict('raw_tags.txt')
json.dump(tagz,open('raw_tags.json','w'))