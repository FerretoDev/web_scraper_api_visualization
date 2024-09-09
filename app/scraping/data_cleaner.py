import pandas as pd


def clean_data(raw_data):
    # Convertir datos crudos en un DataFrame de Pandas
    df = pd.DataFrame(
        raw_data, columns=["Columna1", "Columna2", "Columna3"]
    )  # Ajusta los nombres de las columnas
    # Realiza cualquier limpieza adicional aquí, como eliminar duplicados o tratar valores nulos
    df = df.drop_duplicates()
    return df
