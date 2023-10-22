import csv

with open("C:\Copa_Mundial_2023.csv") as copa:
          reader = csv.reader(copa)
          for fila in reader:
              print(f"Equipo Local: {fila[0]} / Equipo Visitante: {fila[1]} / Goles equipo local: {fila[2]} / Goles equipo visita: {fila[3]} / Tarjetas del equipo local: {fila[4]} / Tarjetas del equipo local: {fila[5]}")