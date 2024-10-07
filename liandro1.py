import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#LIANDRO 1

df = pd.read_csv('laptop_price.csv')

plt.figure(figsize=(10, 6))
df['Company'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Laptops by Company')
plt.xlabel('Company')
plt.ylabel('NUmber of Laptops')
plt.xticks(rotation=45)
plt.show()

#LIANDRO 2

plt.figure(figsize=(10, 6))
df['RAM (GB)'].value_counts().sort_index().plot(kind='barh', color='lightgreen')
plt.title('Count of Laptops by RAM Size')
plt.xlabel('Number of Laptops')
plt.ylabel('RAM (GB)')
plt.show()


