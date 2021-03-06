import string

import svm as svm
from nltk import word_tokenize, stem
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import regex as re
import csv

# Source used: https://www.pluralsight.com/guides/building-a-twitter-sentiment-analysis-in-python
from sklearn.model_selection import train_test_split

stop_words = set(stopwords.words('english'))


def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    tweet_tokens = word_tokenize(tweet)
    filtered_words = [w for w in tweet_tokens if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(w, pos='a') for w in filtered_words]
    result = " ".join(lemma_words)
    return result


def which_user(label):
    if label == 'RichardDawkins':
        return "was probably tweeted by Richard Dawkins"
    else:
        return "was probably tweeted by xQc"


def predict_tweet(tweet):
    tweet_re = [preprocess_tweet(tweet)]

    tweet_re = vectorizer.transform(tweet_re)

    pred = svm.predict(tweet_re)

    results = svm.predict_proba(tweet_re)

    print(f"The tweet '{tweet.strip()}' {pred[0]} with a probability of {results.max()}\n")


content = []

with open('all_tweets.csv', newline='', encoding="UTF-8") as csvfile:
    tweetsreader = csv.reader(csvfile, delimiter=',')
    for row in tweetsreader:
        content.append(row)

tweets = [row[1] for row in content]
labels = [row[0] for row in content]

tweets = list(map(preprocess_tweet, tweets))
labels = list(map(which_user, labels))

X_train, X_test, y_train, y_test = train_test_split(
    tweets, labels, test_size=0.1, random_state=68)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

svm = SVC(probability=True)

svm.fit(X_train, y_train)


with open('xQc_tests.txt', 'r', encoding='utf-8') as f:
    xQc_tests = f.readlines()
    f.close()

with open('RichardDawkins_tests.txt', 'r', encoding='utf-8') as f:
    RichardDawkins_tests = f.readlines()
    f.close()

print("Testing with tweets from xQc: ")
print("------------------------------")
for tweet in xQc_tests:
    predict_tweet(tweet)

print("\n")
print("Testing with tweets from Richard Dawkins: ")
print("------------------------------")
for tweet in RichardDawkins_tests:
    predict_tweet(tweet)