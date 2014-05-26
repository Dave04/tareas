import json
leer=open('out.json').read()
leido=json.loads(leer)
nombre= leido["name"]
foto= leido["picture"]["data"]["url"]
alto=leido["picture"]["data"]["height"]
ancho=leido["picture"]["data"]["width"]
hombres=0
mujeres=0
total=0
lenguas=[]
lenguas2=[]
lugares=[]
lugares2=[]
q=[]
le=[]
lu=[]
relaciones=[]
relaciones2=[]
re=[]
edades=[]
sumatoria=0
final={}
for k in leido["friends"]["data"]:
    total+=1
    if 'gender' in k:
        if k['gender']=='male':
            hombres+=1
        if k['gender']=='female':
            mujeres+=1
    if 'languages' in k:
        for d in k['languages']:
            lenguas.append(d['name'])
            if not  d['name'] in lenguas2:
                lenguas2.append(d['name'])
    if 'hometown' in k:
        for e in k['hometown']:
            lugares.append(k['hometown']['name'])
            if not k['hometown']['name'] in lugares2:
                lugares2.append(k['hometown']['name'])
    if 'relationship_status' in k:
        relaciones.append(k['relationship_status'])
        if not k['relationship_status'] in relaciones2:
                relaciones2.append(k['relationship_status'])
    if 'birthday' in k:
        if len(k['birthday'])==10:
            edad = k['birthday'][6:10]
            edades.append(edad)
            sumatoria+=int(edad)
            edades = sorted(edades)
            viejo=2014-int(edades[0])
            joven=2014-int(edades[-1])
promedio=2014-(sumatoria//len(edades))
solo=0
casado=0
en=0
abierta=0
complicado=0
divorciado=0
comprometidos=0
viudo=0
separado=0               
for k in lenguas2:
    le.append({"language":k , "count": lenguas.count(k)})
for k in lugares2:
    lu.append({"town":k , "count": lugares.count(k)})
for k in relaciones2:
    if k == 'Single':
        solo=relaciones.count(k)
    if k == 'Married':
        casado=relaciones.count(k)
    if k=='In a relationship':
        en=relaciones.count(k)
    if k=='In an open relationship':
        abierta=relaciones.count(k)
    if k=="It's complicated":
        complicado=relaciones.count(k)
    if k== 'Divorced':
        divorciado=relaciones.count(k)
    if k=='Engaged':
        comprometidos=relaciones.count(k)
    if k=='Widowed':
        viudo=relaciones.count(k)
    if k=='Separated':
        separado=relaciones.count(k)
q.append({"name": nombre , "picture":{"url":foto, "width":ancho, "height":alto}, "friends":{"count":total, "gender":{"male":hombres, "female": mujeres},"age":{"average":promedio,"youngest": joven, "oldest": viejo},"languages": le,"hometown": lu,"relationship_status":{"single":solo,"in_a_relationship":en,"engaged":comprometidos,"married":casado,"open_relationship":abierta,"complicated":complicado,"separated":separado,"divorced":divorciado,"widowed":viudo}}})
w=open('DRuz_Fb.json','w')
json.dump(q[0],w,indent=4)
w.close()
