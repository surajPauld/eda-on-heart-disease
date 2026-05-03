import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart.csv")
df.head()

#inforrmation of dataset
df.info()

#A statistical summary
df.describe()

#Checking or missing values
df.isnull().sum()

df.duplicated().sum()

df['Sex'] = df['Sex'].astype('category')

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
