# -*- coding: utf-8 -*-
# @Date    : 2018/11/07
# @Author  : xiaoliang8006

import numpy as np
from sklearn import svm
from sklearn import metrics
from time import time
import json
from scipy import sparse, io
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy import sparse, io
from sklearn.decomposition import PCA
import cPickle as pickle
import sys

#log
class Logger(object):
    def __init__(self,fileN ="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN,"a")
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout = Logger("mylog.txt") #这里我将Log输出到D盘
#下面所有的方法，只要控制台输出，都将写入"mylog.txt"


# Utility function to move the midpoint of a colormap to be around the values of interest.
class MidpointNormalize(Normalize):

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))


class TrainerLinear:
    def __init__(self, training_data, training_target):
        self.training_data = training_data
        self.training_target = training_target
        self.clf = svm.SVC(C=1, class_weight=None, coef0=0.0,
                           decision_function_shape=None, degree=3, gamma='auto',
                           kernel='linear', max_iter=-1, probability=False,
                           random_state=None, shrinking=True, tol=0.001, verbose=False)

 

    def train_classifier(self):
        self.clf.fit(self.training_data, self.training_target)
        joblib.dump(self.clf, 'model/SVM_sklearn.pkl')
        training_result = self.clf.predict(self.training_data)
        print metrics.classification_report(self.training_target, training_result)
        #performance_report(self.training_target, training_result)




class TrainerRbf:
    def __init__(self, training_data, training_target):
        self.training_data = training_data
        self.training_target = training_target
        self.clf = svm.SVC(C=100, class_weight=None, coef0=0.0,
                           decision_function_shape=None, degree=3, gamma=0.01,
                           kernel='rbf', max_iter=-1, probability=False,
                           random_state=None, shrinking=True, tol=0.001, verbose=False)

    def train_classifier(self):
        self.clf.fit(self.training_data, self.training_target)
        joblib.dump(self.clf, 'model/SVM_sklearn.pkl')
        training_result = self.clf.predict(self.training_data)
        print metrics.classification_report(self.training_target, training_result)




def performance_report(target, result):
    confusion = metrics.confusion_matrix(target, result)
    print 'confusion matrix'
    print confusion

    TP = int(confusion[0, 0])
    FN = int(confusion[0, 1])
    FP = int(confusion[1, 0])
    TN = int(confusion[1, 1])

    # 下面是我自己注释掉的，最后要取消掉注释
    # 下面全面的衡量这个分类器的效果
    Accuracys = float(TP + TN) / (TP + FP + TN + FN)
    Precisions = float(TP) / (TP + FP)
    Recalls = float(TP) / (TP + FN)  # recall
    f_value = 2 * Recalls * Precisions / (Recalls + Precisions)

    print("TP:" + str(TP))
    print("TN:" + str(TN))
    print("FP:" + str(FP))
    print("FN:" + str(FN))
	
    print("Recalls: %s" % str(Recalls))
    print("Precisions: %s" % str(Precisions))
    print("Accuracys: %s" % str(Accuracys))
    print("f_value: %s" % str(f_value))



def SVM_train(train_data, train_target):
    clf = svm.SVC(kernel='linear', class_weight='balanced', C =100, gamma = 0.01)
    clf.fit(train_data, train_target)
    expected = train_target
    predicted = clf.predict(train_data)
    # summarize the fit of the model
    print metrics.classification_report(expected, predicted)
    print metrics.confusion_matrix(expected, predicted)


def feature_selection(data, data_target, feature_names):
    clf = svm.SVC(class_weight='balanced', C =2)
    clf.fit(data, data_target)


# how much train data, how much test data
def select_data(x, y, takeup):
    train_x, test_x, train_y, test_y = train_test_split(
        x, y, test_size=takeup, random_state=20) #test data take up takeup, random_seed is 20
    return train_x, test_x, train_y, test_y

######################################################################################
	
if '__main__' == __name__:
      # how much test data take up
    # 0.1 indicates test data take up 10%
    print "********************** trainning start **********************"
    t0 = time()
    takeup = 0.1
    x = io.mmread('Data/X.mtx') 
    with open('Data/y.json', 'r') as f:
        y = json.load(f)
    train_x, test_x, train_y, test_y = select_data(x, y, takeup)
    print 'takeup finished'

    '''
    #train num1
    print '#################### train num1 ##########################'
    start_time1 = time.time() 
    TrainerRbf(train_x, train_y).train_classifier()
    print 'training took %fs!' % (time.time() - start_time1)
    '''
    
    #train num2
    print '###### train SVM model2 #######'
    start_time2 = time() 
    TrainerLinear(train_x, train_y).train_classifier()
    print 'training took %fs!' % (time() - start_time2)
 
    #train num3
    '''
    print '##################### train num3 #######################'
    start_time3 = time.time() 
    SVM_train(train_x, train_y)
    print 'training took %fs!' % (time.time() - start_time3)
    print '$$$$$$$$$$$$$$ trainning finished  $$$$$$$$$$$$$$$$$'
   '''
    modela = joblib.load('model/SVM_sklearn.pkl')
    predict = modela.predict(test_x)
    performance_report(test_y,predict)
    print("*************** Trainning done in %0.3fs ***************\n\n" % ((time() - t0)))

