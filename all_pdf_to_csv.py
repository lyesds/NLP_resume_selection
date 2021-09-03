# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:18:50 2021

@author: HZU
"""

from tika import parser  
import pandas as pd
import os.path

path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'

df_resumes = pd.DataFrame()

list_resumes_str = []
list_file = []
for i in range(1,3267):
    value=i
    if os.path.isfile(path+f'\\{value}.pdf'):
        parsed_pdf = parser.from_file(path+f'\\{value}.pdf')
        resume_text = parsed_pdf['content'] 
        try:
            resume_text = resume_text.lower()
            list_resumes_str.append(resume_text)
            list_file.append(i)
            print(i)
        except AttributeError:
            next
    else:
        next

data = {'file_name':list_file, 'str':list_resumes_str}
df_resumes = pd.DataFrame(data)    
df_resumes.to_csv(r'resumes_str.csv',sep=',', index=False, mode='w')
