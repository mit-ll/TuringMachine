# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:07:00 2015

@author: Jack
"""

from sklearn import svm
from PIL import Image
from numpy import array
import pickle

STANDARD_SIZE = (100, 100)

class Classifier:
    def __init__(self, dataFile = "data/data.dat"):
        self.__dataFile = dataFile
        try: 
            fp = open(dataFile,"r")
            self.__model = pickle.load(fp)
            fp.close()
        except: 
            print "No data found in ", dataFile
            print "Check the correct filename was used or run \"train\" to generate the data"
            self.__model = None
    def train(self):
        """ Writes n of each image to create a trained model"""        
        
        # lines to create training set
        # n = 100
        
        X = list()
        y = list()
        # for i in range(n):
#            hw.print(1)
#            X.append(hw.read())
#            y.append(1)
#            hw.print(0)
#            X.append(hw.read())
#            y.append(0)
        # Init our SVM classifier 
        
        # Testing image recognition
        img = Image.open("data/one.bmp")
        img = img.resize(STANDARD_SIZE)
        img = list(img.getdata())
        img = map(list, img)
        x = array(img)
        X.append(x.flatten().tolist())
        y.append(1)
        
        img = Image.open("data/zero.bmp")
        img = img.resize(STANDARD_SIZE)
        img = list(img.getdata())
        img = map(list, img)
        x = array(img)
        X.append(x.flatten().tolist())
        y.append(0)
        
        
        self.__model = svm.SVC()
        
        # Regress y on X
        self.__model.fit(X,y)
        
        # Save out model 
        fp = open(self.__dataFile, "w")
        pickle.dump(self.__model, fp)
        fp.close()
        
    def classify(self, X):
        print self.__model.predict(X)

#X = [[0,0], [1,1]]
#y = [0,1]
#clf = svm.SVC()
#clf.fit(X, y) 
#
#print clf.predict([[2,2]])

ml = Classifier()
ml.train()
img = Image.open("data/one2.bmp")
img = img.resize(STANDARD_SIZE)
img = list(img.getdata())
img = map(list, img)
x = array(img)
x = x.flatten().tolist()
ml.classify(x)