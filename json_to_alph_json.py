import sys
import json

## READS JSON FILE
with open(sys.argv[1], "r") as JSON:
	json_dict = json.load(JSON)

alph, alph_dict = "qwertyuiopasdfghjklzxcvbnm", {}
for letter in alph:
	alph_dict[letter] = []

for num, word in enumerate(json_dict.keys()):
	if len(word) >= 4:
		for letter in set(word):
			alph_dict[letter].append(word)
	
with open('alph_dictionary.json', 'w') as json_file:
    json.dump(alph_dict, json_file)
