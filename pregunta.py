"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

        # Leer el archivo de texto y almacenar las líneas relevantes en una lista
    with open("clusters_report.txt", 'r') as file:
        lineas = file.readlines()[4:]  # Empieza desde la fila 5

    # Procesar las líneas y unirlas con la última columna
    data = []
    fila_actual = ''
    for linea in lineas:
        linea_strip = linea.strip()
        if not linea_strip:  # Si es una línea en blanco
            if fila_actual:  # Si hay datos en la fila actual, agregarla a la lista de datos
                data.append(fila_actual)
                fila_actual = ''  # Reiniciar la fila actual
        else:
            fila_actual += ' ' + linea_strip  # Unir la línea con la fila actual

    # Si queda alguna fila en fila_actual, añádela a la lista de datos
    if fila_actual:
        data.append(fila_actual)

    # Crear DataFrame
    df = pd.DataFrame(data, columns=['Columna'])

    # Eliminar el espacio antes del signo de porcentaje (%) y agrupar los datos que son texto
    df['Columna'] = df['Columna'].str.replace(r'\s+%', '', regex=True)
    df['Columna'] = df['Columna'].apply(lambda x: x.strip() if x.isnumeric() else x) # Eliminar espacios al inicio y al final de las cadenas
    df = df.replace(r'\s+', ' ', regex=True) # Eliminar espacios en blanco
    df['Columna'] = df['Columna'].str.replace(' ', '', 1)
    df = df['Columna'].str.split(' ', n=3, expand=True)


    # Renombrar las columnas
    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.')
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '')
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['cluster'] = df['cluster'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)
    # Mostrar el DataFrame
    
    #print(df5.iloc[1])

    return df

#df = ingest_data()
#print(df)
