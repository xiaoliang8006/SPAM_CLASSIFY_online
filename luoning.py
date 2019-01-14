# coding=utf-8
import jieba.posseg as pseg
import  warnings
from sklearn.externals import joblib#用来保存当前的模型
import sys
from time import time

#reload(sys)
#sys.setdefaultencoding('utf8')
warnings.filterwarnings("ignore")# 忽略一些版本不兼容等警告

start =time()
model=joblib.load("SPAM_CLASSIFY_online/model/dtree_py2_final.m")
# 模块二:预测信息

# 读取待预测的短息读取到X1中
X1 = []
X2 = []
#f = open('test.txt')
gpus = sys.argv[1]
X1.append(gpus)
# 进行分词，分词后保存在X2中
for i in range(len(X1)):
    words = pseg.cut(X1[i])
    str1 = ""
    for key in words:
        str1 += key.word
        str1 += ' '
    X2.append(str1)  # 短信内容

# 计算待预测信息的TF-IDF权重
vectorizer = joblib.load("SPAM_CLASSIFY_online/Data/tfidf_py2_final.m")#实例化
'''
这个矢量化器（也就是计算tfidf的方法实例不要创建新的，而是要使用训练模型中的那一个（因为记下了数据
归一化使用的方差和均值），所以也要把这一个存下来）
'''
x_demand_prediction = vectorizer.transform(X2)

# 预测
#classifier = LogisticRegression()
#classifier.fit(x_train, y_train)
y_predict = model.predict(x_demand_prediction)
end =time()
# 输出
for i in range(len(X1)):
    if int(y_predict[i]) == 0:
        print("yes")
    else:
        print("no")


