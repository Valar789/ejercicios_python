# Calcular la diferencia en dia de 2 fechas

from datetime import date

hoy  = date(2022, 9 , 16)
otra_fecha = date(24, 9, 16)

diferencia_fecha = hoy - otra_fecha

print(diferencia_fecha.days)