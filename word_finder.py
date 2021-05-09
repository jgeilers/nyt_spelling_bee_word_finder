import sys
import json

## READS JSON FILE
with open(sys.argv[1], "r") as JSON:
	json_dict = json.load(JSON)

letters, alph = sys.argv[2], "qwertyuiopasdfghjklzxcvbnm"
required, additional = letters[0], letters[1:]

## FOR JSON FILE WITH ALPHABET LETTERS AS KEYS AND 
## WORDS CONTAINING THAT LETTER AS VALUES
common = set(json_dict[required])
for letter in additional:
	letter_set = set(json_dict[letter])
	intersection = common.intersection(letter_set)
	only_A = common - letter_set
	common = only_A.union(intersection)

final = set()
not_included = set(alph) - set(letters)
for word in common:
	if len(set(word).intersection(not_included)) == 0:
		final.add(word)

print(final)