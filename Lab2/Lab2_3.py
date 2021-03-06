import nltk
from nltk.corpus import brown


# (source used: http://www.nltk.org/book/ch05.html)

# a)

def lookupTagger(train_size):
    tagged = brown.tagged_sents()

    size = int(len(tagged) * train_size)
    train_set = tagged[:size]
    test_set = tagged[size:]

    fd = nltk.FreqDist(brown.words())
    cfd = nltk.ConditionalFreqDist(brown.tagged_words())
    most_freq_words = fd.most_common(200)
    likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
    baseline_tagger = nltk.UnigramTagger(model=likely_tags)

    print(f"The accuracy ({train_size}) is: {baseline_tagger.evaluate(test_set)}")


lookupTagger(0.9)
lookupTagger(0.5)


def lookupTaggerCat(train_size, ctgry):
    tagged = brown.tagged_sents(categories=ctgry)

    size = int(len(tagged) * train_size)
    train_set = tagged[:size]
    test_set = tagged[size:]

    fd = nltk.FreqDist(brown.words())
    cfd = nltk.ConditionalFreqDist(brown.tagged_words())
    most_freq_words = fd.most_common(200)
    likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
    baseline_tagger = nltk.UnigramTagger(model=likely_tags)

    print(f"The accuracy ({train_size}) is: {baseline_tagger.evaluate(test_set)}")

print("Using a smaller total set of sentences: ")
lookupTaggerCat(0.9, "humor")
lookupTaggerCat(0.5, "humor")
