import chardet
import pandas as pd
import numpy as np
suicide_attack = pd.read_csv("PakistanSuicideAttacks Ver 11 (30-November-2017).csv" ,encoding='Windows-1252')
#print(suicide_attack.head(10))
#print(suicide_attack.groupby("Province"))
#print(suicide_attack.describe())
#print(suicide_attack.sort_values(by='No. of Suicide Blasts').head(10))

#print(suicide_attack.shape)
#print(suicide_attack.index)
#print(type(suicide_attack))
#print(suicide_attack[['Date','Islamic Date']])
print(suicide_attack.head(10))
