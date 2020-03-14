import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("school-21-student-expulsion-prediction/train.csv")

# print(df)

#Исследования данных
n_samples, n_features = df.shape
print("Количество наблюдений ",n_samples)
print("Количество атрибутов ", n_features)

pd.set_option('display.max_columns',None)
description = df.describe()
description.to_excel('data/description.xlsx')

print("Количество пустых значений")
print(df.isnull().sum())
# df = pd.get_dummies(df)
print("Количество атрибутов {}  и наблюдений {} после замены категориальных на фиктивные".format(df.shape[1],df.shape[0]))
print("Количество пустых значений после замены категориальных на фиктивные")
# print(df.isnull().sum())


description_after_preprocessing = df.describe().to_excel('data/description_after_preprocessing.xlsx')

df['contract_status'].value_counts().plot(kind='bar')
plt.title("Поступили")
print("%f подписали контракт " %(df.contract_status[df.contract_status == 1].count()/df.contract_status.count() * 100))
corr = df.corr()
corr.to_excel("data/correlation.xlsx")