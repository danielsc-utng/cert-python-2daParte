def read_int(prompt, min, max):
    entrada = False
    while not entrada:     
        try:    
            valor = int(input(prompt))
            entrada = True
        except ValueError:
            print("Error: Entrada incorrecta")
        if entrada:
            entrada = valor >= min and valor <= max
        if not entrada:
            print("Error: El valor no está entre el rango permitido")
    return valor
v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)
