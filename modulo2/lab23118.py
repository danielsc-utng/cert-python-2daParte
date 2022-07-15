## Luis daniel Sánchez Cabrera
## Laboratorio 2.3.1.18

def mysplit(strng):
    
    if strng == '' or strng.isspace():
        return [ ]
    lista=[]
    palabra = ''
    dentro = not strng[0].isspace()
    for x in strng:
        if dentro:
            if not x.isspace():
                palabra = palabra + x
            else:
                lista.append(palabra)
                dentro = False
        else:
            if not x.isspace():
                dentro = True
                palabra = x
            else:
                continue
    if dentro:
        lista.append(palabra)
        return lista


print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))