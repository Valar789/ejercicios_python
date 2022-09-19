# Obtener la fecha y hora actual del sistema

import datetime

ahora = datetime.datetime.now()
print(ahora)

print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S')) #EJE 15/07/2022 12:45:30