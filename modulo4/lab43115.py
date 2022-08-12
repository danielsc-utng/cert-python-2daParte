## Luis daniel Sánchez Cabrera
## Laboratorio 4.3.1.15

from os import strerror

counters = {chr(ch):0 for ch in range(ord('a'), ord('z')+1)}
file_name = input("Enter name:")

try:
    f = open(file_name, 'rt')
    for linea in f:
        for letra in linea:
            if letra.isalpha():
                counters[char.lower()] +=1
    f.close()
    for letra in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(letra, '->', cnt)
except IOError as e:
    print("I/O error", strerror(e.errno))
