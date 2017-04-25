#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# Reduce the size of the data set to 1% to speed up
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

svm_classifier = SVC(kernel = 'rbf', C = 10000)

tic = time()
svm_classifier.fit(features_train, labels_train)
toc = time()
print "training time:", round(toc - tic, 3), "s"

tic = time()
predictions = svm_classifier.predict(features_test)
toc = time()
print "testing time:", round(toc - tic, 3), "s"

# print "number of test events classified in Chris class:", np.count_nonzero(predictions)

svm_accuracy = svm_classifier.score(features_test, labels_test)
print "SVM Accuracy =", svm_accuracy

#########################################################


