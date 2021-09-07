# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:39:49 2021
@author: HZU
"""

import re
import pandas as pd
import numpy as np
import spacy
from spacy.matcher import Matcher, PhraseMatcher

# load pre-trained model for all the functions.
nlp = spacy.load('en_core_web_sm')

#Load data from different datasets.

# ##  CSV hard skills to list
# data_hard_skills = pd.read_csv('utils/hard_skills.csv', sep=';', encoding = 'utf-8', names= ['words'], header = None)
# data_hard_skills['words'] = data_hard_skills['words'].str.lower()
# data_hard_skills['tags'] = 'skill'
# hard_skills_words = data_hard_skills['words'].tolist()
# hard_skills_tags = data_hard_skills['tags'].tolist()

# ##  CSV job titles to list
# job_titles = pd.read_csv('utils/jobs_titles.csv', encoding = 'utf-8', header = None)
# job_titles[0] = job_titles[0].str.lower()
# job_titles_words = job_titles[0].tolist()

# ## CSV academic institutions to list
# academic_institutions = pd.read_csv('utils/academic_institutions.csv', encoding = 'utf-8', header = None)
# academic_institutions[0] = academic_institutions[0].str.lower()
# academic_institutions_words = academic_institutions[0].tolist()

# ## CSV academic titles to list
# academic_titles = pd.read_csv('utils/academic_titles.csv', encoding = 'utf-8', header = None)
# academic_titles[0] = academic_titles[0].str.lower()
# academic_titles_words = academic_titles[0].tolist()

# ## CSV hobbies to list
# hobbies = pd.read_csv('utils/hobbies.csv', encoding = 'utf-8', header = None)
# hobbies[0] = hobbies[0].str.lower()
# hobbies_words = hobbies[0].tolist()

## CSV CV data
resumes = pd.read_csv('./assets/df_all_files.csv', encoding = 'utf-8')
resumes['name'] = resumes['name'].replace(np.nan, 'NOVALUE')
resumes['email'] = resumes['email'].replace(np.nan, 'NOVALUE')
resumes['phone'] = resumes['phone'].replace(np.nan, 'NOVALUE')
resumes['address'] = resumes['address'].replace(np.nan, 'NOVALUE')
resumes['hobby'] = resumes['hobby'].replace(np.nan, 'NOVALUE')
resumes['experience'] = resumes['experience'].replace(np.nan, 'NOVALUE')
resumes['educ'] = resumes['educ'].replace(np.nan, 'NOVALUE')
resumes['skills'] = resumes['skills'].replace(np.nan, 'NOVALUE')
resumes['lang'] = resumes['lang'].replace(np.nan, 'NOVALUE')
resumes['pdftext'] = resumes['pdftext'].replace(np.nan, 'NOVALUE')
resumes = resumes.sort_values(by=['id'])
resumes = resumes.reset_index(drop=True)


"""#The pdf umber 11 is not getting the correct data
for i in range(len(resumes)):
    while resumes['name'][i] == 'NOVALUE':
        str_text = resumes['pdftext'][i]
        resumes['name'][i] =  str_text[:250]
    while resumes['address'][i] == 'NOVALUE':
        str_text = resumes['pdftext'][i]
        resumes['address'][i] =  str_text[:250]
    else:
        next
"""

resumes['name2'] = np.where(resumes['name'] == 'NOVALUE', resumes['pdftext'].str[:250], resumes['name'])
resumes['address2'] = np.where(resumes['address'] == 'NOVALUE', resumes['pdftext'].str[:250], resumes['address'])

resumes = resumes.astype(str)
resumes['name2'] = resumes['name2'].str.lower()
resumes['address2'] = resumes['address2'].str.lower()
resumes['id'] = resumes['id'].astype(int)

#Function to extrac the names from resumes['name']
def extract_name(col_names):
    # initialize matcher with a vocab
    matcher = Matcher(nlp.vocab)
    all_names = []
    nlp_text = nlp(col_names)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text)
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        l = span.text
        all_names.append(l)
    all_names = [x.lower() for x in all_names]
    for i in range(len(all_names)):
        if 'name' in all_names[i]:
            next
        elif 'mr' in all_names[i]:
            next
        elif 'father' in all_names[i]:
            next
        elif 'mother' in all_names[i]:
            next
        elif 'curriculum' in all_names[i]:
            next
        elif 'vitae' in all_names[i]:
            next
        else:
            return all_names[i]


#use of NER
def name_via_entity(var):
    doc = nlp(var)
    result = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            result.append(ent.text)
        else:
            next
    if len(result) > 0:
        return str(result[0])
    else:
        return 'no name'


#resumes['name_matcher'] = resumes['name2'].apply(lambda x: extract_name(x))
# resumes['name_entity'] = resumes['pdftext'].apply(lambda x: name_via_entity(x))
#names = resumes[['id', 'name', 'name2', 'name_matcher', 'name_entity']]

#print(names.info())
#print(names.head(15).to_markdown())

def get_email_addresses(var):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    res = r.findall(str(var))
    if len(res) > 0:
        return res[0]
    else:
        return 'no email'


resumes['email_regex'] = resumes['email'].apply(lambda x: get_email_addresses(x))
email = resumes[['id', 'email_regex']]
print(email.info())
print(email.head(30).to_markdown())
