import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Oxford.csv")

rating = df["rating"].value_counts()

plt.figure(figsize=(12, 8)) 
plt.plot(rating.index,rating.values, color="#ea1e06")
plt.show()