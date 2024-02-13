import json
from difflib import get_close_matches
data = json.load(open("data.json.json")) ## loading json data as a python dict

def translate(word):
    """
    returns a word from the data dict
    handles some case sentitivity issues and 
    mistyped words issues 
    """
    # handling case sensitive
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_no = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no\n")
        if yes_no == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == "N":
            return f"The word doesn't exist"
        else:
            return f"We don't understand your entry"
    else:
        return f"The word {word} doesn't exist. Please double check it."

word = input("Enter a word: ")
output = translate(word)
if type(output) == list:    
    for item in output:
        print(item)
else:
    print(output)
    

