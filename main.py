# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:54:14 2021

@author: HZU
"""

# with open("1.txt") as f:
#     # cv = f.readlines()
#     cv = f.read()

# import spacy
# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
# from pprint import pprint

# nlp = en_core_web_sm.load()

# cv_nlp = nlp(cv)

# pprint([(X.text, X.label_) for X in cv_nlp.ents])

from pdfminer.high_level import extract_text

path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'

resume_text = extract_text(path+'\\120.pdf')




import spacy
from spacy.matcher import Matcher

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
    matcher.add('NAME', [pattern])
    
    matches = matcher(nlp_text)
    
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        print(span)
        return span.text



a = extract_name(resume_text)


import re

def extract_email(email):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None


























1) Personal Information
2) Summary
Work experience
    3) Technical Skills
4) Earlier Projects and Experience
5) Education.











details
information
personal details
personal data
personal info
identifying information
individual data
personal contact information
personal detail
biographical data
individual details
data privacy
individual information
biographical details
contact data
contact details
contact info
contact information
contact preferences
data identifying
identification data




















    objective = (
        'career goal',
        'objective',
        'career objective',
        'employment objective',
        'professional objective',
        'summary',
        'career summary',
        'professional summary',
        'summary of qualifications',
    )

    work_and_employment = (
        'employment history',
        'work history',
        'work experience',
        'experience',
        'professional experience',
        'professional background',
        'additional experience',
        'career related experience',
        'related experience',
        'programming experience',
        'freelance',
        'freelance experience',
        'army experience',
        'military experience',
        'military background',
    )

    education_and_training = (
        'academic background',
        'academic experience',
        'programs',
        'courses',
        'related courses',
        'education',
        'educational background',
        'educational qualifications',
        'educational training',
        'education and training',
        'training',
        'academic training',
        'professional training',
        'course project experience',
        'related course projects',
        'internship experience',
        'internships',
        'apprenticeships',
        'college activities',
        'certifications',
        'special training',
    )

    skills_header = (
        'credentials',
        'qualifications',
        'areas of experience',
        'areas of expertise',
        'areas of knowledge',
        'skills',
        "other skills",
        "other abilities",
        'career related skills',
        'professional skills',
        'specialized skills',
        'technical skills',
        'computer skills',
        'personal skills',
        'computer knowledge',        
        'technologies',
        'technical experience',
        'proficiencies',
        'languages',
        'language competencies and skills',
        'programming languages',
        'competencies'
    )

    misc = (
        'activities and honors',
        'activities',
        'affiliations',
        'professional affiliations',
        'associations',
        'professional associations',
        'memberships',
        'professional memberships',
        'athletic involvement',
        'community involvement',
        'refere',
        'civic activities',
        'extra-Curricular activities',
        'professional activities',
        'volunteer work',
        'volunteer experience',
        'additional information',
        'interests'
    )

    accomplishments = (
        'achievement',
        'licenses',
        'presentations',
        'conference presentations',
        'conventions',
        'dissertations',
        'exhibits',
        'papers',
        'publications',
        'professional publications',
        'research',
        'research grants',
        'project',
        'research projects',
        'personal projects',
        'current research interests',
        'thesis',
        'theses',
    )




















































