# -*- coding: utf-8 -*-
# @Date    : 2018/11/07
# @Author  : xiaoliang8006

import jieba
import jieba.posseg as pseg
import sklearn.feature_extraction.text
from sklearn.externals import joblib
import cPickle as pickle
from scipy import sparse, io
import sys,os
from time import time
import  warnings
# generate word vector using tf-idf weight
class TfidfVectorizer(sklearn.feature_extraction.text.TfidfVectorizer):
    def build_analyzer(self):
        def analyzer(doc):
            words = pseg.cut(doc)
            new_doc = ''.join(w.word for w in words if w.flag != 'x')
            words = jieba.cut(new_doc)
            return words
        return analyzer

#获取信息***************************
gpus = sys.argv[1]
text = [gpus];
# 模块二:预测信息
# 读取待预测的短息读取到X1中
X1 = []
X2 = []
#f = open('test.txt')
X1.append(gpus)
# 进行分词，分词后保存在X2中
for i in range(len(X1)):
    words = pseg.cut(X1[i])
    str1 = ""
    for key in words:
        str1 += key.word
        str1 += ' '
    X2.append(str1)  # 短信内容

#*******************************LR********************************
start2 =time()
warnings.filterwarnings("ignore")# 忽略一些版本不兼容等警告
model=joblib.load("SPAM_CLASSIFY_online/model/LR_model.m")
vectorizer = joblib.load("SPAM_CLASSIFY_online/Data/Myvectorizer.m")#实例化
x_demand_prediction = vectorizer.transform(X2)
y_predict = model.predict(x_demand_prediction)
end2 =time()
# 输出
for i in range(len(X1)):
    if int(y_predict[i]) == 0:
        print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size=5 weight=700> LR: </font> <font color=green size=5 weight=700>非垃圾短信 </font> 用时: %0.3fs</br>" % (end2 - start2))
    else:
        print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size=5 weight=700> LR: </font> <font color=red size=5 weight=700>垃圾短信! </font> 用时: %0.3fs</br>" % (end2 - start2))


				
#**************************DT************************
start4 =time()
model=joblib.load("SPAM_CLASSIFY_online/model/dtree_py2_final.m")
vectorizer = joblib.load("SPAM_CLASSIFY_online/Data/tfidf_py2_final.m")#实例化
x_demand_prediction = vectorizer.transform(X2)
y_predict = model.predict(x_demand_prediction)
end4 =time()
# 输出
for i in range(len(X1)):
    if int(y_predict[i]) == 0:
        print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size=5 weight=700> DT: </font> <font color=green size=5 weight=700>非垃圾短信 </font> 用时: %0.3fs</br>" % (end4 - start4))
    else:
        print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size=5 weight=700> DT: </font> <font color=red size=5 weight=700>垃圾短信! </font> 用时: %0.3fs</br>" % (end4 - start4))


#*****************************SVM*********************************************
start =time()
vec_tfidf = joblib.load("SPAM_CLASSIFY_online/Data/vec_tfidf") #note absolute path
data_tfidf = vec_tfidf.transform(text)
#data_tfidf = vec_tfidf.fit_transform(text)
#model = pickle.load(open('model/SVM_sklearn.pkl', 'rb'))
modelb = joblib.load('SPAM_CLASSIFY_online/model/SVM_sklearn.pkl')

predict = modelb.predict(data_tfidf)
end =time()
if predict == "0":
    print("&nbsp;<font size=5 weight=700> SVM: </font> <font color=green size=5 weight=700>非垃圾短信 </font> 用时: %0.3fs</br>" % (end - start))
elif predict == "1":
    print("&nbsp;<font size=5 weight=700> SVM: </font> <font color=red size=5 weight=700>垃圾短信! </font> 用时: %0.3fs</br>" % (end - start))

	
		
#***************GBDT****************************************
start3 =time()
model = joblib.load('SPAM_CLASSIFY_online/model/gbdt_s.pkl')
vectorizer = joblib.load("SPAM_CLASSIFY_online/Data/vec_tfidf_s")#实例化
x_demand_prediction = vectorizer.transform(X2)
y_predict = model.predict(x_demand_prediction)
end3 =time()
# 输出
for i in range(len(X1)):
    if int(y_predict[i]) == 0:
        print("<font size=5 weight=700> GBDT: </font> <font color=green size=5 weight=700>非垃圾短信 </font> 用时: %0.3fs</br>" % (end3 - start3))
    else:
        print("<font size=5 weight=700> GBDT: </font> <font color=red size=5 weight=700>垃圾短信! </font> 用时: %0.3fs</br>" % (end3 - start3))







