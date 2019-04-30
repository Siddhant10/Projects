                                                                    #MAJOR PROJECT
                                                                    #Classifier for 8000 sentences (POSTIVE OR NEGATIVE)

#CODE

# IMPORTING PACKAGES

import nltk

# if you don't have a nltk package installed use
# nltk.download()

import os
import random
import pickle
from collections import Counter
from nltk.corpus import movie_reviews  # movie_reviews is dataset which is a part of the nltk.corpus
from nltk.classify.scikitlearn import SklearnClassifier #importing a specific package of nltk.classify.scikitlearn
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize #importing package of tokenizing words


# CREATING A CLASS

class SenetenceClassifier(Classifier):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
        
pos_comment = open("short_reviews/positive.txt","r").read() #opening the file with positive comments
neg_comment= open("short_reviews/negative.txt","r").read()  #opening the file with negative comments 

files = []

#spliting positive comments and appending it in the files
for r in pos_comment.split('\n'):
    files.append( (r, "positive") )

#spliting negative comments and appending it in the files
for r in neg_comment.split('\n'):
    files.append( (r, "negative") )


all_words = []

#Tokenizing the words
positive_words = word_tokenize(pos_comment) 
negative_words = word_tokenize(neg_comment)

for w in positive_words:
    all_words.append(w.lower())

for w in negative_words:
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)#frequency distribution

word_features = list(all_words.keys())[:8000] # selecting the number of words

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents]
#random shuffle for more accurate classifier
random.shuffle(featuresets)

#dividing the featuresets into 2 categories
training_set = featuresets[:4000]
testing_set =  featuresets[4000:]



#Different types of algorithms for checking the accuracy for the classifier

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)




type_classifier = SentenceClassifier(
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)


print("type_classifier accuracy percent:", (nltk.classify.accuracy(type_classifier, testing_set))*100)
