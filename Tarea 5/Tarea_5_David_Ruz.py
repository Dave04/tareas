
# coding: utf-8

# In[1]:

import math 
from sklearn import datasets, neighbors, linear_model, metrics
import pylab as pl
import numpy as np
from sklearn.metrics import roc_auc_score, precision_score, f1_score, recall_score


# In[2]:

import string
def leer(string):
    leer=open('C:\\Users\\David\\Desktop\\primer semestre 2014\\computacion\\set de datos\\'+string+'.txt')
    la=[]
    de=[]
    for e in leer:
        n=e.split(" ")
        de.append(n)
    de.pop(0) 
    return de
def Y_dato(de):
    orig=[]
    for s in de:
        for f in s:
            if  "ZE" in f or  "NE" in f:
                orig.append(f[:-1]) 
    return orig
def X_dato(de):
    resultados=[]
    for s in de:
        for f in s:
            if  "ZE" in f or  "NE" in f:
                s.remove(f)
    res=[]
    for s in de:
        for f in s:
            k=float(f)
            resultados.append(k)
        res.append(resultados)
        resultados=[]
    return res


# In[3]:

def X_c1(X_dato):
    obt=[]
    obt2=[]
    for k in X_dato:
        a=k[1]
        b=k[3]
        c=k[4]
        d=k[7]
        obt2.append(a)
        obt2.append(b)
        obt2.append(c)
        obt2.append(d)
        obt.append(obt2)
        obt2=[]
    return obt


# In[4]:

test=leer("test")
y=Y_dato(test)
xbeta=X_dato(test)
x=X_c1(xbeta)
training=leer("training")
y1=Y_dato(training)
x1beta=X_dato(training)
x1=X_c1(x1beta)
logistic=linear_model.LogisticRegression()
print("Resultado de: c1. Eventos y Regiones de usuarios de SL")
numero1=logistic.fit(x1,y1).score(x,y)
print('LogisticRegression score: %f' % logistic.fit(x1,y1).score(x,y))
prediccion1=logistic.fit(x1,y1).predict(x)


# In[5]:

def X_c2(X_dato):
    obt=[]
    obt2=[]
    for k in X_dato:
        a=k[8]
        b=k[9]
        c=k[10]
        obt2.append(a)
        obt2.append(b)
        obt2.append(c)
        obt.append(obt2)
        obt2=[]
    return obt


# In[6]:

def X_c3(X_dato):
    obt=[]
    obt2=[]
    for k in X_dato:
        a=k[15]
        b=k[16]
        c=k[18]
        obt2.append(a)
        obt2.append(b)
        obt2.append(c)
        obt.append(obt2)
        obt2=[]
    return obt


# In[7]:

x2=X_c2(xbeta)
x2a=X_c2(x1beta)
logistic=linear_model.LogisticRegression()
print("Resultado de: c2. Características de los productos")
print('LogisticRegression score: %f' % logistic.fit(x2a,y1).score(x2,y))
numero2=logistic.fit(x2a,y1).score(x2,y)
prediccion2=logistic.fit(x2a,y1).predict(x2)


# In[8]:

x3=X_c3(xbeta)
x3a=X_c3(x1beta)
logistic=linear_model.LogisticRegression()
print("Resultado de: c3. Red Seller - Buyer")
print('LogisticRegression score: %f' % logistic.fit(x3a,y1).score(x3,y))
numero3=logistic.fit(x3a,y1).score(x3,y)
prediccion3=logistic.fit(x3a,y1).predict(x3)


# In[9]:

def X_general(X_dato):
    obt=[]
    obt2=[]
    for k in X_dato:
        a=k[1]
        b=k[3]
        c=k[4]
        d=k[7]
        e=k[8]
        f=k[9]
        g=k[10]
        h=k[15]
        i=k[16]
        j=k[18]
        obt2.append(a)
        obt2.append(b)
        obt2.append(c)
        obt2.append(d)
        obt2.append(e)
        obt2.append(f)
        obt2.append(g)
        obt2.append(h)
        obt2.append(i)
        obt2.append(j)
        obt.append(obt2)
        obt2=[]
    return obt


# In[10]:

x4=X_general(xbeta)
x4a=X_general(x1beta)
logistic=linear_model.LogisticRegression()
print("Resultado de todas las caracteristicas")
print('LogisticRegression score: %f' % logistic.fit(x4a,y1).score(x4,y))
numero4=logistic.fit(x4a,y1).score(x4,y)
prediccion4=logistic.fit(x4a,y1).predict(x4)


# In[11]:

def cambio(lista):
    lis=[]
    for k in lista:
        if "ZE" in k:
            lis.append(0)
        if "ONE" in k:
            lis.append(1)
    lista=lis
    return lista


# In[12]:

predic1=cambio(prediccion1)
y_y=cambio(y)
print("resultado AUC de categoria 1: ")
auc1=roc_auc_score(y_y, predic1)
print(roc_auc_score(y_y, predic1))
print("-------------------------------------------------")
predic2=cambio(prediccion2)
print("resultado AUC de categoria 2: ")
auc2=roc_auc_score(y_y, predic2)
print(roc_auc_score(y_y, predic2))
print("-------------------------------------------------")
predic3=cambio(prediccion3)
print("resultado AUC de categoria 3: ")
auc3=roc_auc_score(y_y, predic3)
print(roc_auc_score(y_y, predic3))
print("-------------------------------------------------")
predic4=cambio(prediccion4)
print("resultado AUC de categoria general: ")
auc4=roc_auc_score(y_y, predic4)
print(roc_auc_score(y_y, predic4))
print("-------------------------------------------------")


# In[13]:

print("resultado Precision de categoria 1: ")
pre1=precision_score(y_y, predic1,pos_label=None)
print(precision_score(y_y, predic1,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria 2: ")
pre2=precision_score(y_y, predic2,pos_label=None)
print(precision_score(y_y, predic2,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria 3: ")
pre3=precision_score(y_y, predic3,pos_label=None)
print(precision_score(y_y, predic3,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria general: ")
pre4=precision_score(y_y, predic4,pos_label=None)
print(precision_score(y_y, predic4,pos_label=None))
print("-------------------------------------------------")


# In[14]:

print("resultado F-1 de categoria 1: ")
f1=f1_score(y_y, predic1,pos_label=None)
print(f1_score(y_y,predic1,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria 2: ")
f2=f1_score(y_y, predic2)
print(f1_score(y_y, predic2,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria 3: ")
f3=f1_score(y_y, predic3,pos_label=None)
print(f1_score(y_y, predic3,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria general: ")
f4=f1_score(y_y, predic4,pos_label=None)
print(f1_score(y_y, predic4,pos_label=None))
print("-------------------------------------------------")


# In[15]:

print("resultado Recall de categoria 1: ")
re1=recall_score(y_y, predic1,pos_label=None)
print(recall_score(y_y, predic1,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria 2: ")
re2=recall_score(y_y, predic2,pos_label=None)
print(recall_score(y_y, predic2,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria 3: ")
re3=recall_score(y_y, predic3,pos_label=None)
print(recall_score(y_y, predic3,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria general: ")
re4=recall_score(y_y, predic4,pos_label=None)
print(recall_score(y_y, predic4,pos_label=None))
print("-------------------------------------------------")


# In[16]:

import math
media1=(auc1+f1+pre1+re1)/4
desviacion1=math.sqrt(((auc1-media1)**2 + (f1-media1)**2 + (pre1-media1)**2 + (re1-media1)**2)/3)
print "la media categoria 1 es: ", media1, "la desviacion es: " , desviacion1
media2=(auc2+f2+pre2+re2)/4
desviacion2=math.sqrt(((auc2-media2)**2 + (f2-media2)**2 + (pre2-media2)**2 + (re2-media2)**2)/3)
print "la media categoria 2 es: ", media2, "la desviacion es: " , desviacion2
media3=(auc3+f3+pre3+re3)/4
desviacion3=math.sqrt(((auc3-media3)**2 + (f3-media3)**2 + (pre3-media3)**2 + (re3-media3)**2)/3)
print "la media categoria 3 es: ", media3, "la desviacion es: " , desviacion3
media4=(auc4+f4+pre4+re4)/4
desviacion4=math.sqrt(((auc4-media4)**2 + (f4-media4)**2 + (pre4-media4)**2 + (re4-media4)**2)/3)
print "la media categoria 4 es: ", media4, "la desviacion es: " , desviacion4


# In[21]:

from sklearn import preprocessing
print("parte de la normalizacion:")
x1nor=preprocessing.normalize(x1)
x2anor=preprocessing.normalize(x2a)
x3anor=preprocessing.normalize(x3a)
x4anor=preprocessing.normalize(x4a)
xnor=preprocessing.normalize(x)
x2nor=preprocessing.normalize(x2)
x3nor=preprocessing.normalize(x3)
x4nor=preprocessing.normalize(x4)
prediccion1a=logistic.fit(x1nor,y1).predict(xnor)
prediccion2a=logistic.fit(x2anor,y1).predict(x2nor)
prediccion3a=logistic.fit(x3anor,y1).predict(x3nor)
prediccion4a=logistic.fit(x4anor,y1).predict(x4nor)
predic1a=cambio(prediccion1a)
predic2a=cambio(prediccion2a)
predic3a=cambio(prediccion3a)
predic4a=cambio(prediccion4a)


# In[24]:

print("resultado F-1 de categoria 1 normalizada: ")
f1a=f1_score(y_y, predic1a,pos_label=None)
print(f1_score(y_y,predic1a,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria 2 normalizada: ")
f2a=f1_score(y_y, predic2a,pos_label=None)
print(f1_score(y_y,predic2a,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria 3 normalizada: ")
f3a=f1_score(y_y, predic3a,pos_label=None)
print(f1_score(y_y,predic3a,pos_label=None))
print("-------------------------------------------------")
print("resultado F-1 de categoria general(c1+c2+c3 combinadas)normalizada: ")
f4a=f1_score(y_y, predic4a,pos_label=None)
print(f1_score(y_y,predic4a,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria 1 normalizada: ")
re1a=recall_score(y_y, predic1a,pos_label=None)
print(recall_score(y_y, predic1a,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria 2 normalizada: ")
re2a=recall_score(y_y, predic2a,pos_label=None)
print(recall_score(y_y, predic2a,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria 3 normalizada: ")
re3a=recall_score(y_y, predic3a,pos_label=None)
print(recall_score(y_y, predic3a,pos_label=None))
print("-------------------------------------------------")
print("resultado Recall de categoria generales normalizada: ")
re4a=recall_score(y_y, predic4a,pos_label=None)
print(recall_score(y_y, predic4a,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria 1 normalizada: ")
pre1a=precision_score(y_y, predic1a,pos_label=None)
print(precision_score(y_y, predic1a,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria 2 normalizada: ")
pre2a=precision_score(y_y, predic2a,pos_label=None)
print(precision_score(y_y, predic2a,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria 3 normalizada: ")
pre3a=precision_score(y_y, predic3a,pos_label=None)
print(precision_score(y_y, predic3a,pos_label=None))
print("-------------------------------------------------")
print("resultado Precision de categoria general(combinadas) normalizada: ")
pre4a=precision_score(y_y, predic4a,pos_label=None)
print(precision_score(y_y, predic4a,pos_label=None))
print("-------------------------------------------------")
print("resultado AUC de categoria 1 normalizada: ")
auc1a=roc_auc_score(y_y, predic1a)
print(roc_auc_score(y_y, predic1a))
print("-------------------------------------------------")
print("resultado AUC de categoria 2 normalizada: ")
auc2a=roc_auc_score(y_y, predic2a)
print(roc_auc_score(y_y, predic2a))
print("-------------------------------------------------")
print("resultado AUC de categoria 3 normalizada: ")
auc3a=roc_auc_score(y_y, predic3a)
print(roc_auc_score(y_y, predic3a))
print("-------------------------------------------------")
print("resultado AUC de categoria general(combinadas) normalizada: ")
auc4a=roc_auc_score(y_y, predic4a)
print(roc_auc_score(y_y, predic4a))
print("-------------------------------------------------")


# In[25]:

media1a=(auc1a+f1a+pre1a+re1a)/4
desviacion1a=math.sqrt(((auc1a-media1a)**2 + (f1a-media1a)**2 + (pre1a-media1a)**2 + (re1a-media1a)**2)/3)
print "la media categoria 1 es: ", media1a, "la desviacion es: " , desviacion1a
media2a=(auc2a+f2a+pre2a+re2a)/4
desviacion2a=math.sqrt(((auc2a-media2a)**2 + (f2a-media2a)**2 + (pre2a-media2a)**2 + (re2a-media2a)**2)/3)
print "la media categoria 2 es: ", media2a, "la desviacion es: " , desviacion2a
media3a=(auc3a+f3a+pre3a+re3a)/4
desviacion3a=math.sqrt(((auc3a-media3a)**2 + (f3a-media3a)**2 + (pre3a-media3a)**2 + (re3a-media3a)**2)/3)
print "la media categoria 3 es: ", media3a, "la desviacion es: " , desviacion3a
media4a=(auc4a+f4a+pre4a+re4a)/4
desviacion4a=math.sqrt(((auc4a-media4a)**2 + (f4a-media4a)**2 + (pre4a-media4a)**2 + (re4a-media4a)**2)/3)
print "la media categoria 4(combinadas) es: ", media4a, "la desviacion es: " , desviacion4a


# In[ ]:



