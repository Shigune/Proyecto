#Solicitud de datos.
print('--- Ingrese los datos solicitados a continuacion  ---')
equipo_local= (input('Ingrese el nombre del equipo local '))
equipo_visitante= (input('Ingrese el nombre del equipo visitante '))
goles_local= int(input('Ingrese la cantidad de goles del equipo local '))
goles_visitante= int(input('Ingrese la cantidad de goles del equipo visitante '))
tarjetas_local= int(input('Ingrese la cantidad de tarjetas del equipo local '))
tarjetas_visitante= int(input('Ingrese la cantidad de tarjetas del equipo visitante '))

#Declaracion de variables.
empate=goles_local==goles_visitante
puntos=0
puntuacion_equipo_local=puntos
puntuacion_equipo_visitante=puntos
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
if goles_local>goles_visitante: #Si gana el equipo local
    print('El equipo ganador es ', equipo_local)
    print(equipo_local,'Obtiene 3 puntos.')
    print(equipo_visitante,'Obtiene 0 puntos.')
    puntuacion_equipo_local+=3
elif goles_visitante>goles_local: #Si gana el equipo visitante
    print('El equipo ganador es', equipo_visitante)
    print(equipo_visitante,'Obtiene 3 puntos.')
    print(equipo_local,'Obtiene 0 puntos.')
    puntuacion_equipo_visitante+=3
if empate==True: #Si hay empate, puntuacion final.
    print('Si hubo empate en este partido')
    print('Ambos equipos obtienen 1 punto.')
    puntuacion_equipo_local+=1
    puntuacion_equipo_visitante+=1
    if goles_visitante>goles_local:
        puntuacion_equipo_visitante+=3
    if goles_local>goles_visitante:
        puntuacion_equipo_local+=3
    if goles_visitante==goles_local:
        if tarjetas_local>tarjetas_visitante:
            puntuacion_equipo_visitante+=3
        elif tarjetas_visitante>tarjetas_local:
            puntuacion_equipo_local+=3
    print('La puntuacion del equipo local es de',puntuacion_equipo_local)
    print('La puntuacion del equipo visitante es de',puntuacion_equipo_visitante)
else: #Si no hay empate, puntuacion final.
    print('No hubo empate en este partido')
    print()
    print('La puntuacion del equipo local es de',puntuacion_equipo_local)
    print('La puntuacion del equipo visitante es de',puntuacion_equipo_visitante)