import re


# a)

def words_beginning_with_sh(inputlist):
    pattern = "^sh"
    return [element for element in inputlist if re.search(pattern, element)]


print("Words beginning with sh:")
print(words_beginning_with_sh(['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']))


# b)

def longer_than_4_char(inputlist):
    pattern = ".{4,}"
    return [element for element in inputlist if re.search(pattern, element)]


print("\n")
print("Words longer than four characters:")
print(longer_than_4_char(['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']))
