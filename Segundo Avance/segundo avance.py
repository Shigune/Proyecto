import csv
with open("C:\Copa_Mundial_2023.csv") as copa:
          datos_mundial = csv.reader(copa)
          for fila in datos_mundial:
            print(f"Equipo Local: {fila[0]}")
            print(f"Equipo Visitante: {fila[1]}")
            print(f"Goles del equipo local: {fila[2]}")
            print(f"Goles del equipo visitante: {fila[3]}")
            print(f"Tarjetas del equipo local: {fila[4]}")
            print(f"Tarjetas del equipo visitante: {fila[5]}")
            print()