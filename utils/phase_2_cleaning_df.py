# -*- coding: utf-8 -*-
"""
@author: HZU
"""

import pandas as pd
import numpy as np

data = pd.read_csv(r'utils/resumes_cleaned.csv')

def cambiar(x):
    x = x.replace("'",'')
    x = x.replace("[",'')
    x = x.replace("]",'')
    return x

data = data.astype(str)

data['location'] =data['location'].apply(lambda x: cambiar(x))
data['academic_titles'] =data['academic_titles'].apply(lambda x: cambiar(x))
data['academic_institutions'] =data['academic_institutions'].apply(lambda x: cambiar(x))
data['work_experience'] =data['work_experience'].apply(lambda x: cambiar(x))
data['certifications'] =data['certifications'].apply(lambda x: cambiar(x))
data['hobbies'] =data['hobbies'].apply(lambda x: cambiar(x))
data['languages'] =data['languages'].apply(lambda x: cambiar(x))


data['academic_titles'] = data['academic_titles'].str.lower()
data['academic_institutions'] =data['academic_institutions'].str.lower()
data['work_experience'] =data['work_experience'].str.lower()
data['certifications'] =data['certifications'].str.lower()
data['hobbies'] =data['hobbies'].str.lower()
data['languages'] =data['languages'].str.lower()

# data_academic_titles = pd.DataFrame()
# data_academic_titles[0] = data['academic_titles']
# data_academic_titles.drop(data_academic_titles.loc[data_academic_titles[0]=='This person do not have academic titles'].index, inplace=True)
# data_academic_titles.reset_index( drop=True , inplace=True)


####Here I put all the values found in academic titles in a list, to get the unique values.
###THIS WAY YOU CAN GET THE WHOLE NAME OF THE TITLE
# a = []
# for n in range(len(data_academic_titles)):
#     l = data_academic_titles[0][n]
#     m = l.split(", ")
#     for i in range(len(m)):
#         a.append(m[i])
# for i in range(len(a)):
#     a[i] = a[i].replace(',',"")
    
# unique_academic_titles = np.unique(a)

def cambiar_titulo(x):
    x = x.replace('b. e',"bachelor in engineering")
    x = x.replace('b.a',"bachelor")
    x = x.replace('b.a economics',"bacherlor in economics")
    x = x.replace('b.a. economics',"bachelor in economics")
    x = x.replace('b.com',"bacherlor in computer science")
    x = x.replace('b.e',"bachelor in engineering")
    x = x.replace('b.s. electrical engineering',"bachelor in engineering")
    x = x.replace('b.tech',"bacherlor in computer science")
    x = x.replace('bachelor',"bachelor")
    x = x.replace('bachelor in architecture',"bachelor in architecture")
    x = x.replace('bachelor in business administration',"bachelor in business administration")
    x = x.replace('bachelor in commerce',"bachelor in commerce")
    x = x.replace('bachelor in engineering',"bachelor in engineering")
    x = x.replace('bachelor in technology',"bacherlor in computer science")
    x = x.replace('bachelor of architecture',"bachelor of architecture")
    x = x.replace('bachelor of business administration',"bachelor of business administration")
    x = x.replace('bachelor of commerce',"bachelor of commerce")
    x = x.replace('bachelor of computer applications',"bacherlor in computer science")
    x = x.replace('bachelor of economics',"bachelor of economics")
    x = x.replace('bachelor of education',"bachelor of education")
    x = x.replace('bachelor of engineering',"bachelor in engineering")
    x = x.replace('bachelor of laws',"bachelor of laws")
    x = x.replace('bachelor of public administration',"bachelor of public administration")
    x = x.replace('bachelor of science in chemistry',"bachelor of science in chemistry")
    x = x.replace('bachelor of science in civil engineering',"bachelor of science in civil engineering")
    x = x.replace('bachelor of science in computer science',"bacherlor in computer science")
    x = x.replace('bachelor of science in electrical engineering',"bachelor of science in electrical engineering")
    x = x.replace('bachelor of science in environmental science',"bachelor of science in environmental science")
    x = x.replace('bachelor of science in finance',"bachelor of science in finance")
    x = x.replace('bachelor of science in information technology',"bacherlor in computer science")
    x = x.replace('bachelor of science in mathematics',"bachelor of science in mathematics")
    x = x.replace('bachelor of science in mechanical engineering',"bachelor of science in mechanical engineering")
    x = x.replace('bachelor of technology',"bacherlor in computer science")
    x = x.replace('bs in finance',"bacherlor in finance")
    x = x.replace('doctor of medicine',"doctor of medicine")
    x = x.replace('h.s.c.',"higher secondary school certificate")
    x = x.replace('m.com',"master in computation")
    x = x.replace('m.sc',"master in science")
    x = x.replace('master of arts',"master of arts")
    x = x.replace('master of business',"master of business")
    x = x.replace('master of business administration',"master of business administration")
    x = x.replace('master of city planning',"master of architecture")
    x = x.replace('master of commerce',"master of commerce")
    x = x.replace('master of computer applications',"master of computer applications")
    x = x.replace('master of education',"master of education")
    x = x.replace('master of engineering',"master of engineering")
    x = x.replace('master of finance',"master of finance")
    x = x.replace('master of mathematics',"master of mathematics")
    x = x.replace('master of science',"master of science")
    x = x.replace('master of social work',"master of social work")
    x = x.replace('master of statistics',"master of statistics")
    x = x.replace('master of surgery',"master of surgery")
    x = x.replace('master of technology',"master in computation")
    x = x.replace('mba',"master of business administration")
    x = x.replace('msc.',"master of science")
    x = x.replace('post graduate',"post graduate")
    x = x.replace('s.s.l.c',"secondary school leaving certificate")
    x = x.replace('ssc',"secondary school certificate")
    x = x.replace('sslc',"secondary school leaving certificate")
    return x


data['academic_titles'] = data['academic_titles'].apply(lambda x: cambiar_titulo(x))

def delete_duplicates_inside(x):
    # x = x.replace(',',"")
    x = x.split(", ")
    x = list(dict.fromkeys(x))
    x = str(x)
    x = cambiar(x)
    return str(x)
    
data['academic_titles'] = data['academic_titles'].apply(lambda x: delete_duplicates_inside(x))
data['academic_institutions'] =data['academic_institutions'].apply(lambda x: delete_duplicates_inside(x))
data['work_experience'] =data['work_experience'].apply(lambda x: delete_duplicates_inside(x))
data['certifications'] =data['certifications'].apply(lambda x: delete_duplicates_inside(x))
data['hobbies'] =data['hobbies'].apply(lambda x: delete_duplicates_inside(x))
data['languages'] =data['languages'].apply(lambda x: delete_duplicates_inside(x))


#####Here I put all the values found in academic institution in a list, to get the unique values.
####THIS WAY YOU CAN GET THE WHOLE NAME OF THE TITLE
# data_acad_insti = pd.DataFrame()
# data_acad_insti[0] = data['academic_institutions']
# a = []
# for n in range(len(data_acad_insti)):
#     l = data_acad_insti[0][n]
#     m = l.split(", ")
#     for i in range(len(m)):
#         a.append(m[i])
# for i in range(len(a)):
#     a[i] = a[i].replace(',',"")
    
# unique_academic_institutions = np.unique(a)


data_to_show = pd.DataFrame()
data_to_show[0] = data['work_experience']
a = []
for n in range(len(data_to_show)):
    l = data_to_show[0][n]
    m = l.split(", ")
    for i in range(len(m)):
        a.append(m[i])
for i in range(len(a)):
    a[i] = a[i].replace(',',"")
    
unique_values_to_show = np.unique(a)

##############################################################################
######################        45 unique academic title name
##############################################################################
######################        1929 unique work experience name
##############################################################################
######################        335 unique academic institutions name
##############################################################################
######################        35 unique languages name
##############################################################################
######################        134 unique hobbies name
##############################################################################
######################        9217 unique certifications name


pd.DataFrame(unique_values_to_show).to_csv("unique_academic_titles.csv")
pd.DataFrame(unique_values_to_show).to_csv("unique_awork_experience.csv")

data.to_csv(r'super_cleaned_df.csv',sep=',', index=False, mode='w')  







