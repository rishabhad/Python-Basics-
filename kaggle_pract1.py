import chardet
import pandas as pd
import numpy as np
with open("PakistanSuicideAttacks Ver 11 (30-November-2017).csv" ,'rb') as rawdata:
	result= chardet.detect(rawdata.read(100000))
#print(result)
'''{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}'''

suicide_attack = pd.read_csv("PakistanSuicideAttacks Ver 11 (30-November-2017).csv" ,encoding='Windows-1252')
#print(suicide_attack.head(10))

#print(cities)
suicide_attack['City']=suicide_attack['City'].str.lower()
suicide_attack['City']=suicide_attack['City'].str.strip()
#print(cities)
cities=suicide_attack['City'].unique()
cities.sort()
print(cities)
