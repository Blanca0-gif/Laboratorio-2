import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("songsTaylor.csv", delimiter=";")

#Elimina las filas duplicadas y solamente mantiene la primera que se encuentra
df=df.drop_duplicates(subset="track_name", keep="first")

#Muestre las primeras 5 de formas ascendente segun el numero de streams en spotify
cinco_top = df[["track_name","spotify_streams" ]].sort_values(by="spotify_streams", ascending=True).head(5)
#print(cinco_top)

#Ajusta el tamaño del grafico
plt.figure(figsize=(12, 8)) 
plt.bar(cinco_top["track_name"], cinco_top["spotify_streams"], color="#a27cc9")#crea el grafico tomando como eje x el nombre de las canciones y eje y  el numero de streams
plt.xlabel('Canciones')
plt.ylabel("Reproducciones")
#Hace rotar el nombre de las canciones para que puedan visualizarse completas
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()