import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data-visualization/sample_data.csv")
sns.histplot(data=df, x="Value", bins=20, kde=True)
plt.figure(figsize=(10,4))
sns.barplot(x="Category", y="Value", data=df)
plt.show()




