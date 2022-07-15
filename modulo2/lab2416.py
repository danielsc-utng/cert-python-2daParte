## Luis daniel Sánchez Cabrera
## Laboratorio 2.4.1.6

digitos = ['1111110', #0
            '0110000', #1
            '1101101', #2
            '1111001', #2
            '0110011', #4
            '1011011', #5
            '1011111', #6
            '1110000', #7
            '1111111', #8
            '1111011', #9
            ]
            
def pantalla(num):
    global digitos
    digito = str(num)
    lineas = ['' for linea in range(5)]
    for x in digito:
        espacio = [[' ',' ',' '] for linea in range(5)]
        patron = digitos[ord(x) - ord('0')]
        if patron[0] == '1':
            espacio[0][0] = espacio[0][1] = espacio[0][2] = '#'
        if patron[1] == '1':
            espacio[0][2] = espacio[1][2] = espacio[2][2] = '#'    
        if patron[2] == '1':
            espacio[2][2] = espacio[3][2] = espacio[4][2] = '#'
        if patron[3] == '1':
            espacio[4][0] = espacio[4][1] = espacio[4][2] = '#'
        if patron[4] == '1':
            espacio[2][0] = espacio[3][0] = espacio[4][0] = '#'
        if patron[5] == '1':
            espacio[0][0] = espacio[1][0] = espacio[2][0] = '#'
        if patron[6] == '1':
            espacio[2][0] = espacio[2][1] = espacio[2][2] = '#'
        for linea in range(5):
            lineas[linea] += ''.join(espacio[linea]) + ' '
    for linea in lineas:
        print(linea)
        
pantalla(int(input("Introduce el número ")))