# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:54:14 2021

@author: HZU
"""

##############################################################################
##############################################################################
##############################################################################

###             All labels

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



##############################################################################
##############################################################################
##############################################################################

###               Name extraction

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

##############################################################################
##############################################################################
##############################################################################

###                 Email

import re

def extract_email(email):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None


##############################################################################
##############################################################################
##############################################################################

###                 skills

from pdfminer.high_level import extract_text
import pandas as pd

##Creating the list with the skills and also the label
data_skills = pd.read_csv('utils/skills.csv', sep=';', encoding = 'utf-8', names= ['words'], header = None)
data_skills['words'] = data_skills['words'].str.lower()
data_skills['tags'] = 'skill'
words = data_skills['words'].tolist()
tags = data_skills['tags'].tolist()

# ##Loading an empty model
# import spacy
# from spacy.tokens import Doc
# from spacy.training import Example

# nlp_skills = spacy.blank('en')
# texto = nlp_skills(resume_text)
# predict = Doc(nlp_skills.vocab, words = words, tags = tags)
# nlp_text = nlp_skills(resume_text, )


import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
phrase_matcher = PhraseMatcher(nlp.vocab)

skill = [nlp.make_doc(text) for text in words]

# phrase_matcher.add("COUNTRIES",None, *skill)
phrase_matcher.add("SKILL", [skill])

path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'
resume_text = extract_text(path+'\\120.pdf')

doc = nlp(resume_text)
matches = phrase_matcher(doc)

for match_id, start, end in matches:
    span = nlp[start:end]
    print(span)

##############################################################################
##############################################################################
##############################################################################

###                 professions

from pdfminer.high_level import extract_text
import pandas as pd

##Creating the list with the skills and also the label
data_professions = pd.read_csv('utils/professions.csv', sep=';', encoding = 'utf-8', names= ['professions'], header = None)
data_professions['professions'] = data_professions['professions'].str.lower()
words = data_professions['professions'].tolist()

# ##Loading an empty model
# import spacy
# from spacy.tokens import Doc
# from spacy.training import Example

# nlp_skills = spacy.blank('en')
# texto = nlp_skills(resume_text)
# predict = Doc(nlp_skills.vocab, words = words, tags = tags)
# nlp_text = nlp_skills(resume_text, )


import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
phrase_matcher = PhraseMatcher(nlp.vocab)

professions = [nlp.make_doc(text) for text in words]

# phrase_matcher.add("COUNTRIES",None, *skill)
phrase_matcher.add("PROFESS", None, *professions)
phrase_matcher.add("PROFESS", professions)



path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'
resume_text = extract_text(path+'\\1.pdf')

resume_text = "data_professions = pd.read_csv('utils/professions.csv', sep=';', encoding = 'utf-8', names= ['professions'], header = None) data_professions['professions'] = data_professions['professions'].str.lower() words = data_professions['professions'].tolist() Academic Coordinator, Academic Counselor,  Academic Dean, Academic Department Chair, Academic Director"

doc = nlp(resume_text)
matches = phrase_matcher(doc)

for match_id, start, end in matches:
    span = nlp[start:end]
    print(span)










def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]





























































###---------------------------------------------------------------------------

# details
# information
# personal details
# personal data
# personal info
# identifying information
# individual data
# personal contact information
# personal detail
# biographical data
# individual details
# data privacy
# individual information
# biographical details
# contact data
# contact details
# contact info
# contact information
# contact preferences
# data identifying
# identification data


    # objective = (
    #     'career goal',
    #     'objective',
    #     'career objective',
    #     'employment objective',
    #     'professional objective',
    #     'summary',
    #     'career summary',
    #     'professional summary',
    #     'summary of qualifications',
    # )

    # work_and_employment = (
    #     'employment history',
    #     'work history',
    #     'work experience',
    #     'experience',
    #     'professional experience',
    #     'professional background',
    #     'additional experience',
    #     'career related experience',
    #     'related experience',
    #     'programming experience',
    #     'freelance',
    #     'freelance experience',
    #     'army experience',
    #     'military experience',
    #     'military background',
    # )

    # education_and_training = (
    #     'academic background',
    #     'academic experience',
    #     'programs',
    #     'courses',
    #     'related courses',
    #     'education',
    #     'educational background',
    #     'educational qualifications',
    #     'educational training',
    #     'education and training',
    #     'training',
    #     'academic training',
    #     'professional training',
    #     'course project experience',
    #     'related course projects',
    #     'internship experience',
    #     'internships',
    #     'apprenticeships',
    #     'college activities',
    #     'certifications',
    #     'special training',
    # )

    # skills_header = (
    #     'credentials',
    #     'qualifications',
    #     'areas of experience',
    #     'areas of expertise',
    #     'areas of knowledge',
    #     'skills',
    #     "other skills",
    #     "other abilities",
    #     'career related skills',
    #     'professional skills',
    #     'specialized skills',
    #     'technical skills',
    #     'computer skills',
    #     'personal skills',
    #     'computer knowledge',        
    #     'technologies',
    #     'technical experience',
    #     'proficiencies',
    #     'languages',
    #     'language competencies and skills',
    #     'programming languages',
    #     'competencies'
    # )

    # misc = (
    #     'activities and honors',
    #     'activities',
    #     'affiliations',
    #     'professional affiliations',
    #     'associations',
    #     'professional associations',
    #     'memberships',
    #     'professional memberships',
    #     'athletic involvement',
    #     'community involvement',
    #     'refere',
    #     'civic activities',
    #     'extra-Curricular activities',
    #     'professional activities',
    #     'volunteer work',
    #     'volunteer experience',
    #     'additional information',
    #     'interests'
    # )

    # accomplishments = (
    #     'achievement',
    #     'licenses',
    #     'presentations',
    #     'conference presentations',
    #     'conventions',
    #     'dissertations',
    #     'exhibits',
    #     'papers',
    #     'publications',
    #     'professional publications',
    #     'research',
    #     'research grants',
    #     'project',
    #     'research projects',
    #     'personal projects',
    #     'current research interests',
    #     'thesis',
    #     'theses',
    # )