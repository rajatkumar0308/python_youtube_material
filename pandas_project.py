#Project : capstone project of financial data using python 
#loading -> cleaning -> transformation -> aggregation -> visualization

#Step1: import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step2: Load the data
df = pd.read_csv("C:/Users/rajat/OneDrive/Desktop/packages/Financial_datasets_.csv")
#print(df.head())    # output 5 rows from data
#print(df.info())    # check metadata

# step3 data cleaning
# handle missing value , correct data types, remove duplicates
#print(df.isnull().sum())
df.drop_duplicates(inplace=True)
print(df.info())

# Step4 transformation : 
# feature engineering - new column addion
# categorization - group of numeric data for better analysis.

df['Amount_Category'] = pd.cut(df['amount'], bins=[0, 5000, 10000, 20000], labels=['Low', 'Medium', 'High'])
#print(df.head())

# step5: data aggregation - groupby or pivot using pandas
transcation_summary = df.groupby("type").agg(
    total_amount=("amount","sum"),
    avg_amount=("amount","mean"),
    count_trans=("amount","count")
).reset_index()

print(transcation_summary)

# step6 visuzliation - bar plot , histogram, scatter plot 

plt.figure(figsize=(10,6))
sns.barplot(x="type",y="total_amount",data=transcation_summary)
plt.title("banks data for amount groups")
plt.show()








