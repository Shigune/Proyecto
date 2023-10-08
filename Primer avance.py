#Solicitud de datos.
print('--- Ingrese los datos solicitados a continuacion  ---')
equipo_local= (input('Ingrese el nombre del equipo local '))
equipo_visitante= (input('Infrese el nombre del equipo visitante '))
goles_local= int(input('Ingrese la cantidad de goles del equipo local '))
goles_visitante= int(input('Ingrese la cantidad de goles del equipo visitante '))
tarjetas_local= int(input('Ingrese la cantidad de tarjetas del equipo local '))
tarjetas_visitante= int(input('Ingrese la cantidad de tarjetas del equipo visitante '))
#Titulo
print ('----------')
print ('World Cup')
print()
#Informacion del equipo local
print ('Equipo local: ', equipo_local)
print('Goles que realizo el equipo local:', goles_local)
print('Cantidad de tarjetas del equipo local:',tarjetas_local)
print()
#Informacion del equipo visitante.
print ('Equipo visitante: ', equipo_visitante)
print('Goles que realizo el equipo visitante:', goles_visitante)
print('Cantidad de tarjetas del equipo visitante:',tarjetas_visitante)
print()
#Resultados, que equipo ganó y si hubo empate. 
if goles_local>goles_visitante:
    print('El equipo ganador es ', equipo_local)
elif goles_visitante>goles_local:
    print('El equipo ganador es', equipo_visitante)
if goles_visitante!=goles_local:
    print('No hubo empate en este partido')
else:
    print('Si hubo empate en este partido')