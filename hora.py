
import datetime
from time import ctime
import os
import ntplib


servidor_de_tiempo = "pool.ntp.org"

print("\nObteniendo la hora del servidor NTP:")
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
print(respuesta.tx_time)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")

print("Respuesta de " + servidor_de_tiempo +  ": " + str(hora_actual) + "\n")


separador = " "
sep = str(hora_actual).split(separador)

fecha = sep[0]
hora = sep[1]

fechass = fecha.split("-")
anio = fechass[0]
mes = fechass[1]
dia = fechass[2]

horasrr = hora.split(":")

fhora = horasrr[0]
fmin = horasrr[1]

hola = 'date -u ' + mes + dia + fhora + fmin + anio

print(hola)
os.system(hola)