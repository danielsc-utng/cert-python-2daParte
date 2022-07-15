## Luis daniel Sánchez Cabrera
## Laboratorio 2.3.1.18

def mysplit(strng):
    
    if strng == '' or strng.isspace():
        return [ ]
    lista=[]
    palabra = ''
    espacio = not strng[0].isspace()
    for x in strng:
        if espacio:
            if not x.isspace():
                palabra = palabra + x
            else:
                lista.append(palabra)
                espacio = False
        else:
            if not x.isspace():
                espacio = True
                palabra = x
            else:
                continue
    if espacio:
        lista.append(palabra)
        return lista


print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))