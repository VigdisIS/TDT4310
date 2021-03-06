from __future__ import division

import glob
import itertools
import pathlib

from nltk import *
from nltk.corpus import stopwords

corpusDir = pathlib.Path().absolute()


# code for tokenizing content of files inspired by:
# http://carrefax.com/new-blog/2017/11/30/find-most-common-words-in-a-corpus

def tokenizeAndRStopwords(directory):
    # a)

    stop_words = set(stopwords.words('english'))
    file_list = glob.glob(os.path.join(os.getcwd(), directory, '*.txt'))

    corpus = []

    for file_path in file_list:
        with open(file_path, encoding="UTF-8") as f_input:
            content = f_input.read()
            no_links = re.sub('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)', '', content)  # RegEx
            # pattern from: https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a
            # -url
            no_single = re.sub(r'(?:^| )\w(?:$| )', ' ',
                               no_links).strip()
            corpus.append(no_single)
            f_input.close()

    filteredCorpus = [[word for word in document.lower().split() if word not in stop_words] for document in corpus]


    # b)

    total = list(itertools.chain.from_iterable(filteredCorpus))
    fdist = FreqDist(total)
    print("10 most common words from corpus: ")
    print(fdist.most_common(10))

    # c)

    print("\n")
    print("10 most common words from individual users: ")
    for text in filteredCorpus:
        fdist = FreqDist(text)

        print(fdist.most_common(10))

    # d)

    string = " "
    string = (string.join(total))

    hashtagPtrn = "#\S+"
    filtered = re.findall(hashtagPtrn, string)

    fdist = FreqDist(filtered)
    print("\n")
    print("10 most used hashtags:")
    print(fdist.most_common(10))




tokenizeAndRStopwords(corpusDir)
