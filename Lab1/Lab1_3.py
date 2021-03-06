import re
from nltk.corpus import words


# a)

def pigLatinConverter(word):
    word = word.lower()
    pattern = r"(^[b-df-hj-np-tv-z]+)"
    result = word

    match = re.match(pattern, word)
    if match:
        result = re.sub(pattern, r"", word)
        result += match.group(0)

    result += 'ay'

    return result

print("Single words translated to Pig Latin:")
print(pigLatinConverter("string"))
print(pigLatinConverter("idle"))


# b)

def textToPigLatin(inputText):
    convertedString = ""
    inputText = inputText.split()
    for string in inputText:
        convertedString += pigLatinConverter(string) + " "

    return convertedString

print("\n")
print("Sentence translated to pig latin:")
print(textToPigLatin("Pig Latin translator but make it a sentence"))
