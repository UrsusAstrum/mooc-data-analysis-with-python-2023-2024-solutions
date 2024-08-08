#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    feature_matrix = np.zeros((len(a), 29))
    
    for i in range(len(a)):
        counts = Counter(a[i])
        for j in range(len(list(alphabet))):
            if list(alphabet)[j] in counts.keys():
                feature_matrix[i, j] += counts[list(alphabet)[j]]

    return feature_matrix

def contains_valid_chars(s):
    for letter in list(s):
        if letter not in alphabet_set:
            return False
    return True

def get_features_and_labels():
    finnish = np.array(list(load_finnish()))
    english = np.array(list(load_english()))

    finnish = np.array([i.lower() for i in finnish])
    finnish = finnish[[contains_valid_chars(i) for i in finnish]]

    english = np.array([x for x in english if x[0].islower()])
    english = np.array([i.lower() for i in english])
    english = english[[contains_valid_chars(i) for i in english]]

    finnish_features = get_features(finnish)
    english_features = get_features(english)

    X = np.concatenate((finnish_features, english_features))
    y = np.concatenate((np.zeros(len(finnish)), np.ones(len(english))))

    return X, y


def word_classification():

    X, y = get_features_and_labels()

    model = MultinomialNB()
    model.fit(X, y)
    scores = cross_val_score(model, X, y, cv=5)
    other_scores = cross_val_score(model, X, y, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0))

    return other_scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
