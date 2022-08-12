## Luis daniel Sánchez Cabrera
## Laboratorio 4.5.1.22


from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Dia de la semana: %w"))
print(my_date.strftime("Dia del año: %j"))
print(my_date.strftime("Número de semana en el año: %W"))
