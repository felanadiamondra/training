import pandas as pd

#lecture du fichier excel avec la fonction  read_excel
df = pd.read_excel("sample_data.xlsx")

#recuperation de la colonne anglais
column = df.columns[1]
fruits = []
print(column)

# parcours du colonne et affichage de la liste des elements
for index, row in df.iterrows():
    fruits.append(row[column])
    print(fruits)