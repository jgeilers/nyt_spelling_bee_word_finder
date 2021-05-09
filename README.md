# nyt_spelling_bee_word_finder
Finds all of the words for the day's NYT Spelling Bee

alpha_words.txt includes a good amount (but not all) of the words in the English dictionary
dictionary.json turns alpha_words.txt into a json file, used for faster searching
alph_dictionary.json is a json file with each letter of the alphabet as the key and each word containing that letter as values


txt_to_json_script.py creates dictionary.json from alpha_words.txt
json_to_alph_json.py creates alph_dictionary.json from dictionary.json

word_finder.py takes the alph_dictionary.json file and the letters of the day as input, in that order. Make sure to include the center/required letter of the spelling bee as the first letter of the input. The result should print the words that include the required letter and the additional 6 letters but no other letters. 

Note: for learning purposes, do not use this program before attempting your best on the NYT Spelling Bee. The purpose of this is to learn the other words you did not catch. Additionally, there are many words not accepted by the NYT Spelling Bee so many of the words returned will not be accepted.

Enjoy!
