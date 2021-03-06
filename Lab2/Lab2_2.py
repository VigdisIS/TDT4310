import nltk
from nltk.corpus import brown
from nltk.corpus import nps_chat
from Lab2_1 import mostFreqTag


# (source used: http://www.nltk.org/book/ch05.html)


# a)

def testSplit(corpus, train_size):
    try:
        tagged = corpus.tagged_sents()
    except AttributeError:
        tagged = corpus.tagged_posts()

    size = int(len(tagged) * train_size)
    train_set = tagged[:size]
    test_set = tagged[size:]

    default_tagger = nltk.DefaultTagger(mostFreqTag(corpus))
    default_tagger.tag(train_set)
    accuracy = default_tagger.evaluate(test_set)

    return accuracy


print(f"The accuracy (90/10) for the Brown corpus is: {testSplit(brown, 0.9)}")
print(f"The accuracy (50/50) for the Brown corpus is: {testSplit(brown, 0.5)}")
print(f"The accuracy (90/10) for the NPS Chat corpus is: {testSplit(nps_chat, 0.9)}")
print(f"The accuracy (50/50) for the NPS Chat corpus is: {testSplit(nps_chat, 0.5)}")


# b)

def mixedTaggers(corpus, train_size):
    try:
        tagged = corpus.tagged_sents()
    except AttributeError:
        tagged = corpus.tagged_posts()

    size = int(len(tagged) * train_size)
    train_set = tagged[:size]
    test_set = tagged[size:]

    patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'), (r'.*ould$', 'MD'), (r'.*\'s$', 'NN$'),
                (r'.*s$', 'NNS'), (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), (r'.*', 'NN')]

    def_tagger = nltk.RegexpTagger(patterns)
    bi = nltk.BigramTagger(train_set, backoff=def_tagger)
    uni = nltk.UnigramTagger(train_set, backoff=bi)

    accuracy = uni.evaluate(test_set)

    return accuracy


print(f"The accuracy (90/10) for the Brown corpus is: {mixedTaggers(brown, 0.9)}")
print(f"The accuracy (50/50) for the Brown corpus is: {mixedTaggers(brown, 0.5)}")
print(f"The accuracy (90/10) for the NPS Chat corpus is: {mixedTaggers(nps_chat, 0.9)}")
print(f"The accuracy (50/50) for the NPS Chat corpus is: {mixedTaggers(nps_chat, 0.5)}")
