# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:14:10 2021

@author: HZU
"""
import pandas as pd


#now we will use the skills dataframe to clean a little more the working experience
data_skills = pd.read_csv('utils/skills.csv', sep=';', encoding = 'utf-8', names= ['words'], header = None)
data_skills['words'] = data_skills['words'].str.lower()



data_professions = pd.read_csv('utils/jobs_titles.csv', encoding = 'utf-8', header = None)
data_professions[0] = data_professions[0].str.lower()
#Counting the # of words by row
data_professions['number_of_words'] = data_professions[0].apply(lambda x: len(x.split()))
data_professions = data_professions.drop(data_professions[data_professions.number_of_words > 3].index)
data_professions = data_professions.drop(['number_of_words'], axis=1)
data_professions = data_professions.drop_duplicates()



data_professions['delete']= data_professions.isin(data_skills)
data_professions['delete'].loc[data_professions['delete'] == False] = 0
data_professions['delete'].loc[data_professions['delete'] == True] = 1
data_professions['delete'].astype(int)


data_skills['delete']= data_skills.isin(data_professions)
data_skills['delete'].loc[data_skills['delete'] == False] = 0
data_skills['delete'].loc[data_skills['delete'] == True] = 1
data_skills['delete'].astype(int)

df = data_professions




# todelete = ['inplant training','private','india','various','associate','additional','marketing','other','various','india','channel','channel sales',
# 'self','player','networking','senior','operations','operations team','pre-sales','presentations',
# 'multiple','master','exploring','personal growth','principle','final year project','maintenance',
# 'summer','communication','tier 1','creative','myself','nothing','everything','human',
# 'server','professional experience:','presentations','test','many','various','other experience',
# 'official','senior','client','collector','active member','tech','channel']

# todelete = ['contracts','major','infrastructure',
# 'construction','information technology','wimax','solutions','deployment','security',
# 'systems integration','cisco','credit','installer','wireless','ph.d.','analyst','academic','collections']

'is engineer'
'runner'
'content'
'candidate'
'employee'
'network'
'channels'
'previous experience'
'banking'
'risk management'
'awards'
'co-op'
'm. tech'



df = data_professions

for i in range(len(todelete)):
    df.drop(df.loc[df[0] == todelete[i]].index, inplace=True)

df.to_csv(r'jobs_titles.csv',sep=',', index=False, mode='w')















