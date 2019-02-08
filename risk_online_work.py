import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import warnings; warnings.filterwarnings('ignore')

df = pd.read_csv('online_sex_work.csv' , index_col=None)

#df1 = df.iloc[: 10, 1:5]
#df2 = df.iloc[: 10, 5:8]
#total_row = df.count
#print(total_row)
#print(df)
#checking how many index column is null 

#print(len(df.index[df.index.isnull()]))

#how to check how many column are having null value


#null_columns=df.columns[df.isnull().any()]
#print(null_columns)
#print(df[null_columns].isnull().sum())


#df = df.iloc[28832:1019744]
#df.index=df.index.astype(int)
#df.drop(df.index[[28832,1019742]])1048575
#print(type(df))
#df=df.drop(df.index[28831:])
#print(df)
#print(len(df.index[df.index.isnull()]))

#print(df)

df=df.dropna(axis=0,how='all')
df.index=df.index.astype(int)
df['Number_of_Comments_in_public_forum'] = df['Number_of_Comments_in_public_forum'].str.replace(' ', '').astype(int)

#print(df)

#df1=df.iloc[1:10,0:7]
#print(df1)
#print(df1.groupby("Sexual_orientation"))
#print(df.describe())

#df['Age'].astype(int)
df['Age']=df['Age'].replace('???',np.nan)
print(df[df['Age']=='???'])
df['Age']=df['Age'].str.replace(',', '.')
df['Age']=df['Age'].astype(float)
df['Age'].fillna(df['Age'].mean(), inplace=True)
#print(df['Age'].head())
#plt.figure()
#df.plot(kind = "hist",y ="Age" ,bins = 50,range= (0,250),normed = True)
plt.show()
df['Location'].fillna(df['Location'].mode()[0], inplace=True)
print(df['Location'])

df['Verification'] = df['Verification'] != 'Non_Verfied'

#print(df['Verification'].head(20))
#print(df.head())
dummy=pd.get_dummies(df['Gender'])
#print(dummy.head(20))

dummy1=pd.get_dummies(df['Sexual_orientation'])
#print(dummy1.head(20))




