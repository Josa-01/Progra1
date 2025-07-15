import pandas as pd # usamos la libreria pandas para el manejo de datos

# hay que leer el archivo de excel
archivo = "Examen2.xlsx" 
xls = pd.ExcelFile(archivo)

# para poder leer los dos sheets que tiene el excel
sopa_df = pd.read_excel(xls, sheet_name='Sopa', header=None)
palabras_df = pd.read_excel(xls, sheet_name='Palabras', header=None)

palabras_texto = palabras_df.iloc[0, 0]  
palabras = palabras_texto.strip().split()

for i, row in sopa_df.iterrows():
    if row.notna().sum() > 0:
        inicio = i
        break

# tomar la sopa de letras y convertirla matriz
sopa_df = sopa_df.iloc[inicio:].dropna(how='all', axis=1).reset_index(drop=True)
sopa = sopa_df.fillna('').astype(str).applymap(lambda x: x.lower()).values.tolist()


direcciones = [
    (0, 1),   
    (0, -1),  
    (1, 0),   
    (-1, 0),  
    (1, 1),   
    (-1, 1), 
    (1, -1),  
    (-1, -1)  
]

#  buscar enn la sopa
def buscar_palabra(palabra, sopa):
    palabra = palabra.lower()
    filas = len(sopa)
    columnas = len(sopa[0])
    resultados = []

    for f in range(filas):
        for c in range(columnas):
            for df, dc in direcciones:
                r, col = f, c
                encontrada = True

                for letra in palabra:
                    if 0 <= r < filas and 0 <= col < columnas:
                        if sopa[r][col] != letra:
                            encontrada = False
                            break
                        r += df
                        col += dc
                    else:
                        encontrada = False
                        break

                if encontrada:
                    resultados.append((palabra.upper(), f, c))
    return resultados

print("Resultados :")
for palabra in palabras:
    encontrados = buscar_palabra(palabra, sopa)
    for palabra, fila, columna in encontrados:
        print(f"Palabra: {palabra} - Fila: {fila} - Columna: {columna}")
