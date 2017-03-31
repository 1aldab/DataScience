#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from classifyNB import classify

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classify(features_train, labels_train)
output = clf.predict(features_test)
my_score = len([i for i, x in enumerate(output) if x == labels_test[i]]) * 1.0 / len(output)
sk_score = clf.score(features_test, labels_test)
print "NB Gaussian score (sklearn):", sk_score
print "NB Gaussian score (manual): ", my_score

### draw the decision boundary with the text points overlaid
print "Output graph is saved."
prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())




