# -*- coding: utf-8 -*-
"""Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LamJtBFEMkeEDUdzLBRydCkGCMy_Yhjc
"""

# -*- coding: utf-8 -*-
"""k-means שיעור 6-סאלח.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IUcMFliypRebxgvS1624AwzScB8rGe1P
"""

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
#או from sklearn.preprocessing import MinMaxScaler

data=np.genfromtxt("data.csv",delimiter=',',skip_header=1)
satesfication=data[:,0]
loyality=data[:,1]
plt.scatter(satesfication,loyality)
plt.xlabel("satesfication")
plt.ylabel("loyality")
plt.show()

kmeans_model=KMeans(n_clusters=2)
kmeans_model.fit(data) #תהליך אימון של המודל 

print("the final centers of the clusters is:",kmeans_model.cluster_centers_)#מחזיר את מספר האשכולות במודל 
print("the sum square error is(sse):",kmeans_model.inertia_)
print("the num of iterations is:",kmeans_model.n_iter_)
print("the labels of all point:",kmeans_model.labels_)

labels=kmeans_model.labels_

plt.scatter(satesfication,loyality,c=labels,cmap='rainbow')

data_scaled=scale(data)

[m,n]=np.shape(data)
sse=[]
for k in range(1,m+1):
  model=KMeans(n_clusters=k)
  model.fit(data_scaled)
  sse.append(model.inertia_)
plt.plot(range(1,m+1),sse)
plt.xlabel("number of clusters")
plt.ylabel("sse")
plt.grid()
plt.show()

kmeans_model_new=KMeans(n_clusters=4)
kmeans_model_new.fit(data_scaled)


print("the final centers of the clusters is:",kmeans_model_new.cluster_centers_)#מחזיר את מספר האשכולות במודל 
print("the sum square error is(sse):",kmeans_model_new.inertia_)
print("the num of iteration is:",kmeans_model_new.n_iter_)
print("the labels of all point:",kmeans_model_new.labels_)
new_labels=kmeans_model_new.labels_
plt.scatter(satesfication,loyality,c=new_labels,cmap='rainbow')

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import minmax_scale



DataSet = load_breast_cancer()
data=DataSet.data

data_scaled = minmax_scale(data)

def KMeansClustering(k,centers,data):
  clus_model=KMeans(n_clusters=k,init=centers)
  clus_model.fit(data_scaled)
  print("the finalcenters is:",clus_model.cluster_centers_)
  print("the num of iteration is:",clus_model.n_iter_)
  print("the sum square error is(sse):",clus_model.inertia_)
  print("\n\n")

m,n=np.shape(data)
for i in range(4):
  print("run number",i+1)
  rows=np.random.randint(0,m,2)
  centers=data_scaled[rows]
  KMeansClustering(2,centers,data_scaled)

import numpy as np 
import random 
x = np.random.randint(0,10,20)
y = np.random.randint(0,10,20)
plt.scatter(x, y) # OR plt.plot(x,y,"*")
plt.grid()
plt.show

import numpy as np 
from matplotlib import pyplot as plt 
import random 
x = np.random.randint(0,10,20)
y = np.random.randint(0,10,20)
plt.subplots(1,3,figsize = (8,5))
plt.subplot(1,3,1)
plt.scatter(x, y) # OR plt.plot(x,y,"*")

plt.subplot(1,3,2)
plt.plot(x,y,"Dg")

plt.subplot(1,3,3)
plt.plot(x,y,"*r")

plt.grid()
plt.show

from sklearn.datasets import load_breast_cancer
dataSet = load_breast_cancer()
data = dataSet.data
targets = dataSet.target 
from sklearn.model_selection  import train_test_split 
train_data,test_data,train_target,test_target = train_test_split(data,targets,test_size = 0.2)


from sklearn.neighbors import KNeighborsClassifier 
model = KNeighborsClassifier(3) #k=3
model.fit(train_data,train_target ) #אימוון המודל
knn_target = model.predict(test_data)
# print(knn_target)

from sklearn import metrics  #בדיקה של התוצאות
print("KNN Accuracy :" ,metrics.accuracy_score(test_target, knn_target))
print("KNN Precision : " , metrics.precision_score(test_target, knn_target))
print("KNN Recall : " , metrics.recall_score(test_target, knn_target))
print("KNN Facore : " , metrics.f1_score(test_target, knn_target))
print("\n KNN Calssification report:")
print(metrics.classification_report( test_target, knn_target))


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(train_data ,train_target)
NB_traget = model.predict(test_data)

print("NB Accuracy :" ,metrics.accuracy_score(test_target, NB_traget))
print("NB Precision : " , metrics.precision_score(test_target, NB_traget))
print("NB Recall : " , metrics.recall_score(test_target, NB_traget))
print("NB Fscore : " , metrics.f1_score(test_target, NB_traget))
print("\n NB Calssification report:")
print(metrics.classification_report( test_target, NB_traget))

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(train_data,train_target)
DT_target = model.predict(test_data)

print("DT Accuracy :" ,metrics.accuracy_score(test_target, DT_target))
print("DT Precision : " , metrics.precision_score(test_target, DT_target))
print("DT Recall : " , metrics.recall_score(test_target, DT_target))
print("DT Fscore : " , metrics.f1_score(test_target, DT_target))
print("\n DT Calssification report:")
print(metrics.classification_report( test_target, DT_target))


print("Confusion Matrix: \n")
print(metrics.confusion_matrix(test_target, knn_target))

import numpy as np 
import matplotlib.pyplot as plt 

dataSet = np.loadtxt("/content/dataR2.csv",delimiter = ',',skiprows=1)
from sklearn.preprocessing import MinMaxScaler # סיפריית הנירמול
scaler = MinMaxScaler() #המנרמל 
scaler.fit(dataSet) #נירמול הנתונים 
data = dataSet[:,:-1]
targets = dataSet[:,-1]

from sklearn.model_selection import train_test_split  #חלוקה הדאטא לאימון ובדיקה
train_data,test_data,train_target,test_target = train_test_split(data,targets,test_size = 0.2)
from sklearn.neighbors import KNeighborsClassifier  # להביא את המסווג 
from sklearn import metrics  #בדיקה של התוצאות
k_num = np.arange(1,16,2)
list_k = []

for k in k_num:
  model = KNeighborsClassifier(k) #k=1,3,5,...
  model.fit(train_data,train_target ) #אימוון המודל
  result_knn_target = model.predict(test_data)
  list_k.append(metrics.accuracy_score(test_target, result_knn_target))
plt.subplots(1,1,figsize = (6,5))
plt.plot(k_num,list_k)
plt.xlabel("K")
plt.grid()
plt.show