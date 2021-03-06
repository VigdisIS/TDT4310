import nltk
from nltk.corpus import brown
from collections import defaultdict, Counter


# a)

def mostFreqTag(corpus):
    tags = [tag for (word, tag) in corpus.tagged_words()]
    print(f"Most frequent tag in the brown corpus is: {nltk.FreqDist(tags).max()}")
    return nltk.FreqDist(tags).max()


mostFreqTag(brown)


# b)


def ambiguousWords():
    word_tags = defaultdict(Counter)
    for word, pos in brown.tagged_words():
        word_tags[word][pos] += 1

    ambiguous_words = filter(lambda x: len(word_tags[x]) > 1, word_tags.keys())

    result = 0
    for i in ambiguous_words:
        # print(i, word_tags[i])
        result += 1

    print(f"{result} words are ambiguous.")
    return result


ambiguousWords()


# c)

def percentageAmbiguous():
    return (ambiguousWords() / len(brown.words())) * 100


print(f"The percentage of ambiguous words is: {percentageAmbiguous()} %")


# d)

def highestNrDistTags():
    cfd = nltk.ConditionalFreqDist(brown.tagged_words())
    conditions = cfd.conditions()
    number_of_tags = []

    for condition in conditions:
        number_of_tags.append((condition, len(cfd[condition])))

    number_of_tags = list(reversed(sorted(number_of_tags, key=lambda x: x[1])))
    tenHighestDist = number_of_tags[:10]

    words = [POSPair[0] for POSPair in tenHighestDist]
    # print(words)

    for word in words:
        for sent in brown.sents():
            if word in sent:
                print(' '.join(sent))
                break
            else:
                continue
            break

    # print(number_of_tags[:10])
    # print(len(brown.sents()))


print("Some sentences:")
highestNrDistTags()
