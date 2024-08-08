#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def spam_detection(random_state=0, fraction=1.0):
    ham_data = []
    spam_data = []
    with gzip.open("src/ham.txt.gz") as file:
        ham_data = file.readlines()
        ham_data = ham_data[:int(fraction * len(ham_data))]
    
    with gzip.open("src/spam.txt.gz") as file:
        spam_data = file.readlines()
        spam_data = spam_data[:int(fraction * len(spam_data))]

    vec = CountVectorizer()
    feature_matrix = vec.fit_transform(ham_data + spam_data).toarray()

    labels = np.concatenate((np.zeros(len(ham_data)), np.ones(len(spam_data))))

    X_train, X_test, y_train, y_test = train_test_split(
    feature_matrix, labels, train_size=0.75, random_state=random_state)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    score = accuracy_score(y_test, y_pred)

    return score, len(y_test), np.sum(y_test != y_pred)


def main():
    print(spam_detection())

if __name__ == "__main__":
    main()
