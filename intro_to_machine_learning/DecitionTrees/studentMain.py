import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

dt_accuracy = clf.score(features_test, labels_test)
print "Decision Tree Accuracy =", dt_accuracy


#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
