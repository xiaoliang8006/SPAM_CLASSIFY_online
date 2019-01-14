# Introduction  
### 对垃圾短信进行分类 代码分为如下几个模块  


# model
### 该文件夹存放的是训练模型

# Data  
### 该文件夹下存放了程序的所有数据

#### label.txt是带标签数据，用来模型训练和模型测试
#### nolabel.txt是不带标签数据用来检验效果
#### X.mtx和y.json是预处理得到的新闻内容和新闻标记
#### feature.json是预处理得到的新闻特征
#### vec_tfidf是预处理得到的tfidf值


***

# code

运行环境: python2.7 + apache + php

#### DataProcess.py是对数据做预处理
#### SVM_Trainer.py是训练SVM模型
#### Message_Classify.py是对给定的短信预测结果
#### SPAM_CLASSIFY_online文件夹放置在apache的根目录下即可，将index.php拿出也放置在apache的根目录下