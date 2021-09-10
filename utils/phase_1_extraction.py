# -*- coding: utf-8 -*-
"""
@author: HZU
"""

import pandas as pd
import numpy as np
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from unidecode import unidecode
import re

# load pre-trained model for all the functions.
nlp = spacy.load('en_core_web_sm')

## CSV academic titles to list
academic_titles = pd.read_csv('utils/academic_titles.csv', encoding = 'utf-8', header = None)
academic_titles[0] = academic_titles[0].str.lower()
academic_titles_words = academic_titles[0].tolist()
academic_titles = [nlp.make_doc(text) for text in academic_titles_words]

## CSV academic titles to list
academic_institutions = pd.read_csv('utils/academic_institutions.csv', encoding = 'utf-8', header = None)
academic_institutions[0] = academic_institutions[0].str.lower()
academic_institutions_words = academic_institutions[0].tolist()    
academic_institutions = [nlp.make_doc(text) for text in academic_institutions_words]

##  CSV job titles to list
job_titles = pd.read_csv('utils/jobs_titles.csv', encoding = 'utf-8', header = None)
job_titles[0] = job_titles[0].str.lower()
job_titles_words = job_titles[0].tolist()
job_titles = [nlp.make_doc(text) for text in job_titles_words]

##  CSV hard skills to list
certifications = pd.read_csv('utils/hard_skills.csv', sep=';', encoding = 'utf-8', header = None)
certifications[0] = certifications[0].str.lower()
certifications_words = certifications[0].tolist()
certifications = [nlp.make_doc(text) for text in certifications_words]

## CSV hobbies to list
hobbies = pd.read_csv('utils/hobbies.csv', encoding = 'utf-8', header = None)
hobbies[0] = hobbies[0].str.lower()
hobbies_words = hobbies[0].tolist()
hobbies = [nlp.make_doc(text) for text in hobbies_words]

## CSV hobbies to list
languages = pd.read_csv('utils/languages.csv', encoding = 'utf-8', header = None)
languages[0] = languages[0].str.lower()
languages_words = languages[0].tolist()
languages = [nlp.make_doc(text) for text in languages_words]

#Function to extract name
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

#Function to extract email
def get_email_addresses(var):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    res = r.findall(str(var))
    if len(res) > 0:
        return res[0]
    else:
        return 'no email'
    
#Function to extract phonenumber
def get_phone(var):
    r = re.compile(r"(\+91)?\s*?(\d{8,10})")
    res = r.findall(str(var))
    if len(res) > 0:
        out = res[0]
        out = '-'.join(out)
    else:
        out = 'no phone'
    return out

#Function to extract the city from address
def extract_location(col_address):
    doc = nlp(col_address)
    result = []
    for ent in doc.ents:
        if ent.label_=='GPE':
            result.append(ent.text)
        else:
            next
    if len(result) > 0:
        return str(result[0])
    else:
        return 'no address'

## Function to extract academic titles
def extract_academic_titles(col_address):
    doc = nlp(col_address)
    phrase_matcher_academic_titles = PhraseMatcher(nlp.vocab)
    phrase_matcher_academic_titles.add("ACA_TITLES", None, *academic_titles)
    matches_academic_titles = phrase_matcher_academic_titles(doc)
    
    academic_list = []
    for match_id, start, end in matches_academic_titles:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        academic_list.append(span.text)
    if len(academic_list) > 0:
        return academic_list
    else:
        return ['This person do not have academic titles']

## Function to extract academic institutions
def extract_academic_institutions(col_address):
    doc = nlp(col_address)
    phrase_matcher_academic_institutions = PhraseMatcher(nlp.vocab)
    phrase_matcher_academic_institutions.add("ACA_INSTI", None, *academic_institutions)
    matches_academic_institutions = phrase_matcher_academic_institutions(doc)
    
    academic_institutions = []
    for match_id, start, end in matches_academic_institutions:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        academic_institutions.append(span.text)
    if len(academic_institutions) > 0:
        return academic_institutions
    else:
        return ['This person do not have listed academic institutions']

## Function to extract work experience
def extract_work_experience(col_address):
    doc = nlp(col_address)
    phrase_matcher_job_titles = PhraseMatcher(nlp.vocab)
    phrase_matcher_job_titles.add("JOB_TITLE", None, *job_titles)
    matches_job_titles = phrase_matcher_job_titles(doc)
    
    job_titles_list = []
    for match_id, start, end in matches_job_titles:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        job_titles_list.append(span.text)
    if len(job_titles_list) > 0:
        return job_titles_list
    else:
        return ['This person do not have listed work experience']

def extract_certifications(col_address):
    doc = nlp(col_address)
    phrase_matcher_certifications = PhraseMatcher(nlp.vocab)
    phrase_matcher_certifications.add("JOB_TITLE", None, *certifications)
    matches_certifications = phrase_matcher_certifications(doc)
    
    certifications_list = []
    for match_id, start, end in matches_certifications:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        certifications_list.append(span.text)
    if len(certifications_list) > 0:
        return certifications_list
    else:
        return ['This person do not have listed certifications']

## Function to extract hobbies
def extract_hobbies(col_address):
    doc = nlp(col_address)
    phrase_matcher_hobbies = PhraseMatcher(nlp.vocab)
    phrase_matcher_hobbies.add("JOB_TITLE", None, *hobbies)
    matches_hobbies = phrase_matcher_hobbies(doc)
    
    hobbies_list = []
    for match_id, start, end in matches_hobbies:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        hobbies_list.append(span.text)
    if len(hobbies_list) > 0:
        return hobbies_list
    else:
        return ['This person do not have listed hobbies']
    
## Function to extract languages
def extract_languages(col_address):
    doc = nlp(col_address)
    phrase_matcher_languages = PhraseMatcher(nlp.vocab)
    phrase_matcher_languages.add("JOB_TITLE", None, *languages)
    matches_languages = phrase_matcher_languages(doc)
    
    languages_list = []
    for match_id, start, end in matches_languages:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        languages_list.append(span.text)
    if len(languages_list) > 0:
        return languages_list
    else:
        return ['English']
