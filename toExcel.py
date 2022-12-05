import pandas as pd
#liste contenant les elements a inserer dans la colonne
list1 = ["pomme" , "fraise", "banane", "chocolat"]
list2 = ["apple" , "strawberry", "banana", "chocolate"]

'''
    Titre du colonne 
'''
col1 = "Francais"
col2 = "Anglais"
data = pd.DataFrame({col1 : list1 , col2 : list2})

'''
    appel de la fonction to_excel du dataframe 
     passer en parametre le nom du fichier de sortie et de la feuille '''

data.to_excel('sample_data.xlsx', sheet_name= "sheet1" , index = False)