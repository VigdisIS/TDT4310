from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import state_union


# a)

def countOccurrence(word):
    occurrences = Counter(word.lower() for word in state_union.words())
    return occurrences[word]


print(f"Occurrences of 'men': {countOccurrence('men')}")
print(f"Occurrences of 'women': {countOccurrence('women')}")
print(f"Occurrences of 'people': {countOccurrence('people')}")


# b)

def usageOverTime(word):
    occurrence_ot = []
    years = []
    for fileid in state_union.fileids():
        years.append(fileid[0:4])
        occurrences = Counter(word.lower() for word in state_union.words(fileid))
        occurrence_ot.append(occurrences[word])

    plt.bar(years, occurrence_ot)
    plt.title(f'Usage of "{word}" in State of the Union speeches over time:')
    plt.xlabel('Year')
    plt.ylabel('Occurrences')
    plt.xticks(rotation=90)
    plt.show()


usageOverTime('men')
usageOverTime('women')
usageOverTime('people')
