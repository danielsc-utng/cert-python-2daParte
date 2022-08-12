## Luis daniel Sánchez Cabrera
## Laboratorio 3.4.1.13


class WeekDayError(Exception):
    pass
	

class Weeker:
    __nombres = ['Lun', 'Mar', 'Mie', 'Jue', 'vie', 'Sab', 'Dom']

    def __init__(self, day):
        try:
            self.__actual = Weeker.__nombres.index(day)
        except ValueError:
            raise WeekDayError
            

    def __str__(self):
        return Weeker.__nombres[self.__actual]

    def add_days(self, n):
        self.__actual = (self.__actual + n) % 7

    def subtract_days(self, n):
        self.actual = (self.__actual - n) % 7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
