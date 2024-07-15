import pandas as pd
import matplotlib.pyplot as plt
titanic_df = pd.read_csv('C:/Users/i/Desktop/python/datasets/test.csv')
plt.figure(figsize=(10, 6))
plt.hist(titanic_df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution on the Titanic')
plt.show()
