import sys
import json

## THIS READS THE TEXT FILE AND SAVES IT AS JSON
words = open(sys.argv[1])
word_list = words.readlines()
json_words = {}
for count in range(len(word_list)):
    json_words[word_list[count].rstrip()] = '1'
with open('dictionary.json', 'w') as json_file:
    json.dump(json_words, json_file)