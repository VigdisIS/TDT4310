import nltk
from nltk import FreqDist, NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
all_words = FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:500]
stop_words = set(stopwords.words("english"))


def features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[f'contains({word})'] = (word in document_words)
        for synset in wn.synsets(word):
            for lemma in synset.lemmas():
                features[f'contains({lemma.name().lower()})'] = (
                    lemma.name() in document_words)
    return features


featuresets = [(features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = NaiveBayesClassifier.train(train_set)

print(f'Accuracy: {nltk.classify.accuracy(classifier, test_set)}')
classifier.show_most_informative_features(10)
