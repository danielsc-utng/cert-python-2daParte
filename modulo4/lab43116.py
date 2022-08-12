## Luis daniel Sánchez Cabrera
## Laboratorio 4.3.1.16

from os import strerror

counters = {chr(ch):0 for ch in range(ord('a'), ord('z')+1)}
file_name = input("Ingrese el nombre del archivo:")
try:
    f = open(file_name, 'rt')
    for line in f:
        for ch in line:
            if ch.isalpha():
                counters[ch.lower()] +=1
    f.close()
    f = open(file_name+'hist', 'wt')
    for letra in sorted(counters.keys(), key= lambda x: counters[x], reverse=True):
        cnt = counters[letra]
        if cnt > 0:
            f.write(letra + '-->' + str(counters[letra])+ '\n')
    f.close()
except IOError as e:
        print("No se pudo abrir el archivo.", strerror(e.errno))
        exit()
