import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("sample_data.cv")
sns.histplot(data=df, x="Value", bins=20, kde=True)
plt.figure(figsize=(10,4))
sns.barplot(x="Category", y="Value", data=df)
plt.show()




