
# coding: utf-8

# In[1]:

import networkx as nx
import matplotlib.pyplot as plt
import json
leer=open('C:\\Users\\David\\Documents\\GitHub\\redes_facebook\\DRO.json').read()
leido=json.loads(leer)
G=nx.Graph()
G.add_node(leido["name"])
for k in leido["friends"]:
    G.add_node(k["name"])    
l=G.nodes()
for k in leido["friends"]:
    for d in k["mutual_friends"]:
        G.add_edge(k["name"],d["name"])
for x in l:
    G.add_edge("DRO",x)
nx.draw(G,with_labels=False)
plt.savefig("red_local_DRO.png",dpi=1000)
plt.show()



# In[7]:

import networkx as nx
import matplotlib.pyplot as plt
import json
def abrir_json(nombrearchivo):
    abrir=open('C:\\Users\\David\\Documents\\GitHub\\redes_facebook\\' + nombrearchivo).read()
    abierto=json.loads(abrir)
    return abierto
a=abrir_json('DCU.json')
b=abrir_json('DRO.json')
c=abrir_json('AAM.json')
d=abrir_json('CGA.json')
e=abrir_json('FASV.json')
f=abrir_json('GLCS.json')
g=abrir_json('IB.json')
h=abrir_json('JHJ.json')
i=abrir_json('JMP.json')
j=abrir_json('JTO.json')
k=abrir_json('MABC.json')
l=abrir_json('MHR.json')
m=abrir_json('MJ.json')
n=abrir_json('MVM.json')
o=abrir_json('NGS.json')
p=abrir_json('PN.json')
q=abrir_json('RC.json')
r=abrir_json('SAMM.json')
s=abrir_json('SMV.json')
t=abrir_json('TBP.json')
u=abrir_json('TGS.json')
v=abrir_json('VF.json')
w=abrir_json('MSB.json')
y=abrir_json('AIVV (3).json')
G1=nx.Graph()
G1.add_node(a["name"])
for z in a["friends"]:
    G1.add_node(z["id"])
    G1.add_edge(a["name"],z["id"])
    for x in z["mutual_friends"]:
        G1.add_edge(z["id"],x["id"])
G2=nx.Graph()
G2.add_node(b["name"])
for z in b["friends"]:
    G2.add_node(z["id"])
    G2.add_edge(b["name"],z["id"])
    for x in z["mutual_friends"]:
        G2.add_edge(z["id"],x["id"])
G3=nx.Graph()
G3.add_node(c["name"])
for z in c["friends"]:
    G3.add_node(z["id"])
    G3.add_edge(c["name"],z["id"])
    for x in z["mutual_friends"]:
        G3.add_edge(z["id"],x["id"])
G4=nx.Graph()
G4.add_node(d["name"])
for z in d["friends"]:
    G4.add_node(z["id"])
    G4.add_edge(d["name"],z["id"])
    for x in z["mutual_friends"]:
        G4.add_edge(z["id"],x["id"])
G5=nx.Graph()
G5.add_node(e["name"])
for z in e["friends"]:
    G5.add_node(z["id"])
    G5.add_edge(e["name"],z["id"])
    for x in z["mutual_friends"]:
        G5.add_edge(z["id"],x["id"])
G6=nx.Graph()
G6.add_node(f["name"])
for z in f["friends"]:
    G6.add_node(z["id"])
    G6.add_edge(f["name"],z["id"])
    for x in z["mutual_friends"]:
        G6.add_edge(z["id"],x["id"])
G7=nx.Graph()
G7.add_node(g["name"])
for z in g["friends"]:
    G7.add_node(z["id"])
    G7.add_edge(g["name"],z["id"])
    for x in z["mutual_friends"]:
        G7.add_edge(z["id"],x["id"])
G8=nx.Graph()
G8.add_node(h["name"])
for z in h["friends"]:
    G8.add_node(z["id"])
    G8.add_edge(h["name"],z["id"])
    for x in z["mutual_friends"]:
        G8.add_edge(z["id"],x["id"])
G9=nx.Graph()
G9.add_node(i["name"])
for z in i["friends"]:
    G9.add_node(z["id"])
    G9.add_edge(i["name"],z["id"])
    for x in z["mutual_friends"]:
        G9.add_edge(z["id"],x["id"])
G10=nx.Graph()
G10.add_node(j["name"])
for z in j["friends"]:
    G10.add_node(z["id"])
    G10.add_edge(j["name"],z["id"])
    for x in z["mutual_friends"]:
        G10.add_edge(z["id"],x["id"])
G11=nx.Graph()
G11.add_node(k["name"])
for z in k["friends"]:
    G11.add_node(z["id"])
    G11.add_edge(k["name"],z["id"])
    for x in z["mutual_friends"]:
        G11.add_edge(z["id"],x["id"])
G12=nx.Graph()
G12.add_node(l["name"])
for z in l["friends"]:
    G12.add_node(z["id"])
    G12.add_edge(l["name"],z["id"])
    for x in z["mutual_friends"]:
        G12.add_edge(z["id"],x["id"])
G13=nx.Graph()
G1.add_node(m["name"])
for z in m["friends"]:
    G13.add_node(z["id"])
    G13.add_edge(m["name"],z["id"])
    for x in z["mutual_friends"]:
        G13.add_edge(z["id"],x["id"])
G14=nx.Graph()
G14.add_node(n["name"])
for z in n["friends"]:
    G14.add_node(z["id"])
    G14.add_edge(n["name"],z["id"])
    for x in z["mutual_friends"]:
        G14.add_edge(z["id"],x["id"])
G15=nx.Graph()
G15.add_node(o["name"])
for z in o["friends"]:
    G15.add_node(z["id"])
    G15.add_edge(o["name"],z["id"])
    for x in z["mutual_friends"]:
        G15.add_edge(z["id"],x["id"])
G16=nx.Graph()
G16.add_node(p["name"])
for z in p["friends"]:
    G16.add_node(z["id"])
    G16.add_edge(p["name"],z["id"])
    for x in z["mutual_friends"]:
        G16.add_edge(z["id"],x["id"])
G17=nx.Graph()
G17.add_node(q["name"])
for z in q["friends"]:
    G17.add_node(z["id"])
    G17.add_edge(q["name"],z["id"])
    for x in z["mutual_friends"]:
        G17.add_edge(z["id"],x["id"])
G18=nx.Graph()
G18.add_node(r["name"])
for z in r["friends"]:
    G18.add_node(z["id"])
    G18.add_edge(r["name"],z["id"])
    for x in z["mutual_friends"]:
        G18.add_edge(z["id"],x["id"])
G19=nx.Graph()
G19.add_node(s["name"])
for z in s["friends"]:
    G19.add_node(z["id"])
    G19.add_edge(s["name"],z["id"])
    for x in z["mutual_friends"]:
        G19.add_edge(z["id"],x["id"])
G20=nx.Graph()
G20.add_node(t["name"])
for z in t["friends"]:
    G20.add_node(z["id"])
    G20.add_edge(t["name"],z["id"])
    for x in z["mutual_friends"]:
        G20.add_edge(z["id"],x["id"])
G21=nx.Graph()
G21.add_node(u["name"])
for z in u["friends"]:
    G21.add_node(z["id"])
    G21.add_edge(u["name"],z["id"])
    for x in z["mutual_friends"]:
        G21.add_edge(z["id"],x["id"])
G22=nx.Graph()
G22.add_node(v["name"])
for z in v["friends"]:
    G22.add_node((z["id"]))
    G22.add_edge(v["name"],z["id"])
    for x in z["mutual_friends"]:
        G22.add_edge(z["id"],x["id"])
G23=nx.Graph()
G23.add_node(w["name"])
for z in w["friends"]:
    G23.add_node((z["id"]))
    G23.add_edge(w["name"],z["id"])
    for x in z["mutual_friends"]:
        G23.add_edge(z["id"],x["id"])
G24=nx.Graph()
G24.add_node(y["name"])
for z in y["friends"]:
    G24.add_node(z["id"])
    G24.add_edge(y["name"],z["id"])
    for x in z["mutual_friends"]:
        G24.add_edge(z["id"],x["id"])
G27=nx.compose_all([G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15,G16,G17,G18,G19,G20,G21,G22,G23,G24])
nx.draw(G27,with_labels=False,node_color="red")
plt.savefig("red_global_DRO.png",dpi=1000)
plt.show()

   


# In[15]:

import matplotlib.pyplot as plt
import numpy as np
ttx=G.degree()
lista=[]
for a in ttx:
    lista.append( ttx[a])
x=lista
plt.hist(x) 
plt.title(u"Gráfico degree red local") 
plt.show()    


# In[8]:

import matplotlib.pyplot as plt
ttz=G27.degree()
lista_grande=[]
for m in ttz:
    lista_grande.append(ttz[m])
y=lista_grande
plt.hist(y)
plt.title(u"Gráfico degree red global")
plt.show()


# In[16]:

import matplotlib.pyplot as plt
ttx1=nx.clustering(G)
lista_clustering=[]
for t in ttx1:
    lista_clustering.append(ttx1[t])
plt.hist(lista_clustering)
plt.title(u"Gráfico clustering coefficient red local")
plt.show()


# In[9]:

import matplotlib.pyplot as plt
ttz1=nx.clustering(G27)
lista_clustering_grande=[]
for k in ttz1:
    lista_grande_clustering.append(ttz1[k])
plt.hist(lista_grande_clustering)
plt.title(u"Gráfico clustering coefficient  red global")
plt.show


# In[17]:

ttx2=nx.betweenness_centrality(G)
lista_bet=[]
for k in ttx2:
    lista_bet.append(ttx2[k])
plt.hist(lista_bet,bins=600)
plt.xlim(0,0.05)
plt.title(u"Gráfico betweenness centrality red local")
plt.show()



# In[12]:

ttz2=nx.betweenness_centrality(G27)
lista_bet2=[]
for k in ttz2:
    lista_bet2.append(ttz2[k])
plt.hist(lista_bet2,bins=600)
plt.title(u"Gráfico betweenness centrality red global")
plt.show()


# In[44]:
#a y b son los json ya abiertos
def amicos_comun(a,b):
    contador=0
    lis=[]
    for z in b["friends"]:
        for x in a["friends"]:
            if z["id"]==x["id"]:
                contador+=1
    lis.append(contador)
    lis.append(b["name"])
    return lis


# In[55]:

ls=[]
ls.append(amicos_comun(b,a))
ls.append(amicos_comun(b,c))
ls.append(amicos_comun(b,d))
ls.append(amicos_comun(b,e))
ls.append(amicos_comun(b,f))
ls.append(amicos_comun(b,g))
ls.append(amicos_comun(b,h))
ls.append(amicos_comun(b,i))
ls.append(amicos_comun(b,j))
ls.append(amicos_comun(b,k))
ls.append(amicos_comun(b,l))
ls.append(amicos_comun(b,m))
ls.append(amicos_comun(b,n))
ls.append(amicos_comun(b,o))
ls.append(amicos_comun(b,p))
ls.append(amicos_comun(b,q))
ls.append(amicos_comun(b,r))
ls.append(amicos_comun(b,s))
ls.append(amicos_comun(b,t))
ls.append(amicos_comun(b,u))
ls.append(amicos_comun(b,v))
ls.append(amicos_comun(b,w))
ls.append(amicos_comun(b,y))
ls.sort()
ls.reverse()
print("Ranking de compañeros")
for k in ls:
    name=k[1]
    nume=k[0]
    
    print(str(name) + ": " + str(nume) + " amigos")

    



# In[ ]:

var=nx.connected_components(G27)
print("componentes conectados= " + str(len(var)))

