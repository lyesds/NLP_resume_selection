# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:39:49 2021

@author: HZU
"""

import pandas as pd
import spacy
from spacy.matcher import Matcher

#Load data from different datasets.

##  CSV hard skills to list
data_hard_skills = pd.read_csv('utils/hard_skills.csv', sep=';', encoding = 'utf-8', names= ['words'], header = None)
data_hard_skills['words'] = data_hard_skills['words'].str.lower()
data_hard_skills['tags'] = 'skill'
hard_skills_words = data_hard_skills['words'].tolist()
hard_skills_tags = data_hard_skills['tags'].tolist()

##  CSV job titles to list
job_titles = pd.read_csv('utils/jobs_titles.csv', encoding = 'utf-8', header = None)
job_titles[0] = job_titles[0].str.lower()
job_titles_words = job_titles[0].tolist()

## CSV academic institutions to list
academic_institutions = pd.read_csv('utils/academic_institutions.csv', encoding = 'utf-8', header = None)
academic_institutions[0] = academic_institutions[0].str.lower()
academic_institutions_words = academic_institutions[0].tolist()

## CSV academic titles to list
academic_titles = pd.read_csv('utils/academic_titles.csv', encoding = 'utf-8', header = None)
academic_titles[0] = academic_titles[0].str.lower()
academic_titles_words = academic_titles[0].tolist()

## CSV hobbies to list
hobbies = pd.read_csv('utils/hobbies.csv', encoding = 'utf-8', header = None)
hobbies[0] = hobbies[0].str.lower()
hobbies_words = hobbies[0].tolist()

## CSV CV data
resumes = pd.read_csv('df_100files.csv', encoding = 'utf-8')

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

nlp_text = nlp(resumes['name'][15])

def extract_name(col_names):
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
        else:
            return all_names[i]


resumes['name'] 
resumes['name'] = resumes['name'].apply(lambda x: extract_name(x))





aaaaaaaaaaaaaaaa = extract_name(resumes['pdftext'][16])














