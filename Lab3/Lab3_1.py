import nltk
import random
from nltk.corpus import names
from tabulate import tabulate


# Source used: https://www.nltk.org/book/ch06.html


def name_features(word):
    return {'last_letter': word[-1]}


def gender_detection(classifier):
    names_with_labels = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in
                                                                                 names.words('female.txt')])

    random.shuffle(names_with_labels)

    featuresets = [(name_features(n), gender) for (n, gender) in names_with_labels]

    train_set, test_set = featuresets[500:], featuresets[:500]

    try:
        classifier_to_use = classifier.train(train_set, max_iter=50)
    except TypeError:
        classifier_to_use = classifier.train(train_set)

    return nltk.classify.accuracy(classifier_to_use, test_set)


data = [["Naive Bayes", gender_detection(nltk.NaiveBayesClassifier)],
        ["Decision Tree", gender_detection(nltk.DecisionTreeClassifier)],
        ["Maximum Entropy", gender_detection(nltk.MaxentClassifier)]]

print(tabulate(data, headers=["Classifier", "Accuracy"]))



