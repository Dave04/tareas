
# coding: utf-8

# In[43]:

import gzip
import time
def funcion1(pagina):
    f=gzip.open('C:\\Users\\Karem\\Desktop\\primer semestre 2014\\computacion\\tarea 2\\pld-index.gz','rb')
    hola=f.readline()
    while hola!="":
        d=hola.split('\t')
        if pagina==d[0]:
            valorpagina=d[1]
            break
        hola=f.readline()
    print("valor indice de " + pagina + ": " + valorpagina)
    f.close()
    return valorpagina
    


# In[44]:

def funcion1b(pagina,valorpagina):
    contadorap=0
    h=gzip.open('C:\\Users\\Karem\\Desktop\\primer semestre 2014\\computacion\\tarea 2\\pld-arc.gz','rb')
    chao=h.readline()
    while chao!="":
        r=chao.split('\t')
        if valorpagina[:-1]==r[0]:
            contadorap+=1
        if int(r[0])>int(valorpagina[:-1]):
            break
        chao=h.readline()
    print("numero de outdegree: " + str(contadorap))
    h.close()


# In[45]:

def funcion2(valorpagina):
    contadorw=0
    j=gzip.open('C:\\Users\\Karem\\Desktop\\primer semestre 2014\\computacion\\tarea 2\\pld-arc.gz','rb')
    hi=j.readline()
    try:
        while hi != "":
            s=hi.split('\t')
            if valorpagina==s[1]:
                contadorw+=1
            hi=j.readline()
    except:
        print("numero de indegree: " + str(contadorw))
    j.close()


# In[46]:

def funcion3(blog):
    w=gzip.open('C:\\Users\\Diego\\SkyDrive\\Universidad\\Tercer Semestre\\Computacion\\Tareas\\2\\Archivos\\sd1-index.gz')
    contadorblog=0
    leer=w.readline()
    try:
        while leer!="":
            separar=leer.split('\t')
            if blog in separar[0]:
                contadorblog+=1
            leer=w.readline()
    except:
        print("cantidad total de subdominios de blogspot: " + str(contadorblog))
    w.close()


# In[ ]:

tiempo1i=time.time()
valorpagina=funcion1("apple.com")
tiempo1m=time.time()
funcion1b("apple.com",valorpagina)
tiempo1f=time.time()
tiempoindice=(tiempo1m-tiempo1i)/60
tiempoout=(tiempo1f-tiempo1m)/60
tiempo1t=tiempoindice+tiempoout
print("tiempo en buscar indice: " + str(tiempoindice) + " minutos")
print("tiempo en buscar outdegree: " + str(tiempoout) + " minutos")
print("tiempo total en generar todo: " + str(tiempo1t))


# In[ ]:

tiempoi=time.time()
valorpagina=funcion1("wikipedia.com")
tiempom=time.time()
funcion2(valorpagina)
tiempof=time.time()
tiempo1=(tiempom-tiempoi)/60
tiempo2=(tiempof-tiempom)/60
print("tiempo en buscar indice: " + str(tiempo1) + " minutos")
print("tiempo en buscar indegree: " + str(tiempo2) + " minutos")
print("tiempo total en generar todo: " + str(tiempo1 + tiempo2) + " minutos")


# In[ ]:

tiempo3i=time.time()
funcion3(".blogspot,com")
tiempo3f=time.time()
tiempo3t=(tiempo3f-tiempo3i)/60
print("tiempo total de busqueda de subdominios de blogspot: " + str(tiempo3t) + " minutos")


# In[ ]:

def funcion4(pagina):
    tiempoinicial=time.time()
    valorpagina=funcion1(pagina)
    tiempomedio=time.time()
    funcion1b(pagina,valorpagina)
    tiempofinal=time.time()
    funcion2(valorpagina)
    tiempofinal2=time.time()
    tiempobuscar=(tiempomedio-tiempoinicial)/60
    tiempolinks=(tiempofinal-tiempomedio)/60
    tiempollamado=(tiempofinal2-tiempofinal)/60
    tiempototal=tiempobuscar+tiempolinks+tiempollamado
    print("tiempo en buscar indice: " + str(tiempobuscar) + " minutos")
    print("tiempo en buscar outdegree: " + str(tiempolinks) + " minutos")
    print("tiempo en buscar indegree: " + str(tiempollamado) + " minutos")
    print("tiempo total: " + str(tiempototal) + " minutos")


# In[ ]:


funcion4("yahoo.com")
#----------------------
funcion4("beautybar.com")
#-----------------------
funcion4("over-blog.com")


# In[ ]:



