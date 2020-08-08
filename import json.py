import json

data = json.load(open("data.json"))

def meaning(word):
	return data.values(word)

word = input("Enter the word you want to find the meaning for")

print(meaning(word))


	
