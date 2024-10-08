import pandas as pd
import matplotlib.pyplot as plt
# Cargar el archivo CSV
df = pd.read_csv("SabrinaSongs.csv", delimiter=";")
#Cuenta las veces que aparece cada genero musical
canGenero = df["track_musical_genre"].value_counts() 

#Le asigna el tamaño al grafico
plt.figure(figsize=(12, 8)) 
#Se crea el grafico de pastel pasandole los valores  y etiquetas
plt.pie(canGenero.values,labels=canGenero.index,autopct="%1.1f%%")
plt.show()
