import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#LIANDRO

df = pd.read_csv('laptop_price.csv')

plt.figure(figsize=(10, 6))
df['RAM (GB)'].value_counts().sort_index().plot(kind='barh', color='lightgreen')
plt.title('Count of Laptops by RAM Size')
plt.xlabel('Number of Laptops')
plt.ylabel('RAM (GB)')
plt.show()

