import csv

with open("C:\ ") as copa:
          reader = csv.reader(copa)
          for fila in reader:
              print(f"Local: {fila[0]} Visita: {fila[1]} Goles local: {fila[2]} Goles visita: {fila[3]} Tarjetas casa: {fila[4]} Tarjetas visita: {fila[5]}")