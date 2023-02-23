# Módulo para leer el archivo csv
import csv 

# Funcion para abrir archivo
def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    header= next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row) #une los valores de las listas en tuplas
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
      
    
#Correr el archivo desde la terminal
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

'''
Un archivo CSV es un tipo de archivo que se utiliza para almacenar datos en una forma tabular estructurada (fila / columna). Es un archivo de texto plano y, como su nombre lo indica, almacena los valores separados por una coma.
'''