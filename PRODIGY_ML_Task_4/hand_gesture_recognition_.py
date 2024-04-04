# -*- coding: utf-8 -*-
"""Hand Gesture Recognition .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vWLtglaIq83V6RV-9kTtkAKuUDrE4PE8

# **Hand Gesture Recognition Database**

<h1 style="font-family: 'poppins'; font-weight: bold; color: Green;">👨💻Author: Irfan Ullah Khan</h1>

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/programmarself)
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/programmarself)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/irfan-ullah-khan-4a2871208/)  

[![YouTube](https://img.shields.io/badge/YouTube-Profile-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@irfanullahkhan7748)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email)](mailto:programmarself@gmail.com)
[![Website](https://img.shields.io/badge/Website-Contact%20Me-red?style=for-the-badge&logo=website)](https://datasciencetoyou.odoo.com)

# Objectives

<li>View the data as an image</li><br>
<li>Train different classifiers</li><br>
<li>Compare performance for different classifiers using various metrics</li>

# Dataset

# Dataset description
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# Data Exploration"""

#reading csv file
df=pd.read_csv('/content/sign_mnist_train.csv')

df.head()

#shape of the data
df.shape

df.columns

df.isnull().values.any()#finding null values

#defining corelation using heat map
corr_m = df.corr()
sns.heatmap(corr_m)

#plotting he total number of each type of label in data
sns.countplot(df['label'])
plt.show()

X = df.iloc[:,1:]
Y = df.iloc[:,0]

# print(X)
print(Y)

"""# Forming pictures from pixels"""

first = X.iloc[1,:]
# print(first)
first = np.array(first , dtype='float')
pixel = first.reshape((28,28))
plt.imshow(pixel)
plt.show()

second = X.iloc[2,:]
second = np.array(second , dtype='float')
pixel2 = second.reshape((28,28))
plt.imshow(pixel2)
plt.show()

third = X.iloc[7,:]
third = np.array(third , dtype='float')
pixel3 = third.reshape((28,28))
plt.imshow(pixel3)
plt.show()

fourth = X.iloc[15,:]
fourth = np.array(fourth , dtype='float')
pixel4 = fourth.reshape((28,28))
plt.imshow(pixel4)
plt.show()

plt.figure(figsize=(15,10))
k = 0
for i in range(26):
    if(i==9 or i==25):
        continue
    else:
        plt.subplot(5,5,k+1)
        img=df[df.label==i].iloc[0,1:].values
        img=img.reshape((28,28))
        plt.imshow(img)
        plt.title("Class" + str(i))
        plt.axis('off')
        k=k+1
plt.show()

"""### Splitting the Data"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)

"""## 1.KNN"""

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

from sklearn.neighbors import KNeighborsClassifier
#instantiate
classifier = KNeighborsClassifier()
#fitting the data
classifier.fit(X_train,Y_train)

#predict
Y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test,Y_pred)

sns.heatmap(cm)

from sklearn.metrics import accuracy_score

#accuracy score
ascore=accuracy_score(Y_test , Y_pred , normalize=True)
print(ascore)

from sklearn.metrics import f1_score
#f1_score
score=f1_score(Y_pred,Y_test,average='micro')
print(score)

"""## 2.Logistic Regression"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

ascore1=accuracy_score(Y_test , Y_pred , normalize=True)
print(ascore1)

score1=f1_score(Y_pred,Y_test,average='micro')
print(score1)

"""# 3.SVM"""

from sklearn.svm import SVC
#instantiate
svc = SVC()
#fiting the data
svc.fit(X_train , Y_train)

#predict
sv_pred = svc.predict(X_test)

ascore3=accuracy_score(Y_test , sv_pred, normalize=True)
print(ascore3)

score3=f1_score(Y_pred,sv_pred,average='weighted')
print(score3)

"""# 4.Naive Bayes"""

from sklearn.naive_bayes import GaussianNB

#instantiate
obj = GaussianNB()

#fitting the data
obj.fit(X_train,Y_train)

#predict
Y_pred = obj.predict(X_test)

ascore4=accuracy_score(Y_test,Y_pred, normalize=True)
print(ascore4)

score4=f1_score(Y_pred,Y_test,average='micro')
print(score4)

"""# 5.MultinomialNB"""

from sklearn.naive_bayes import MultinomialNB
#instantiate
ob = MultinomialNB()
#fitting the data
ob.fit(X_train,Y_train)

#predict
Y_pred = ob.predict(X_test)

ascore5=accuracy_score(Y_test,Y_pred, normalize=True)
print(ascore5)

score5=f1_score(Y_pred,Y_test,average='micro')
print(score5)

"""# 6.Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
# instantiate
dtc = DecisionTreeClassifier()

# fitting the data
dtc.fit(X_train, Y_train)

# predict
Y_pred = dtc.predict(X_test)

#accuracy
ascore6=accuracy_score(Y_test,Y_pred)
print(ascore6)

# f1 score
score6 = f1_score(Y_pred, Y_test,average='weighted')
print(score6)

"""
# 7.RandomForest"""

from sklearn.ensemble import RandomForestClassifier

#instantiate
rc = RandomForestClassifier()
#fitting the data
rc.fit(X_train , Y_train)

#predict
rc_pred = rc.predict(X_test)

ascore2=accuracy_score(Y_test , rc_pred)
print(ascore2)

score2=f1_score(Y_pred,Y_test,average='micro')
print(score2)

"""# Conclusion

### By the Implemented of 6 Algorithms ,now we can compare the performance of them.
"""

Accuracy = [ascore,ascore1,ascore2,ascore3,ascore4,ascore5,ascore6]
data1 = {
    'Accuracy':Accuracy,
    'Algorithm': ['KNN','Logistic Regression','Random Forest Classifier','SVM linear',"Naive Baye's","MultinominalNB",'Decision Tree']}

df1 = pd.DataFrame(data1)

F1_score = [score,score1,score2,score3,score4,score5,score6]
data2 = {
    'F1_score':F1_score,
    'Algorithm': ['KNN','Logistic Regrss,ion','Random Forest Classifier','SVM linear',"Naive Baye's","MultinominalNB",'Decision Tree']}

df2 = pd.DataFrame(data2)

sns.barplot(x = df1.Accuracy, y = df1.Algorithm)

sns.barplot(x = df2.F1_score, y = df2.Algorithm)

"""####**Now we can say that the best model in the above 6 models on the basis of accuracy is the logistic regression model**"""