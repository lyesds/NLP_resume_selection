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
resume_text = extract_text(path+'\\119.pdf')

doc = nlp(resume_text)
matches = phrase_matcher(doc)

for match_id, start, end in matches:
    span = nlp[start:end]
    print(span)

##############################################################################
##############################################################################
##############################################################################

###                 professions
import pandas as pd
import numpy as np
from pdfminer.high_level import extract_text


data_professions = pd.read_csv('utils/jobs_titles.csv', encoding = 'utf-8', header = None)

data_professions[0] = data_professions[0].str.lower()

#Counting the # of words by row
data_professions['number_of_words'] = data_professions[0].apply(lambda x: len(x.split()))
data_professions = data_professions.drop(data_professions[data_professions.number_of_words > 3].index)
data_professions = data_professions.drop(['number_of_words'], axis=1)
data_professions = data_professions.drop_duplicates()


words = data_professions[0].tolist()




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

path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'
resume_text = extract_text(path+'\\0000.pdf')
resume_text = resume_text.lower()

resume_text = "Work Experience Freelance Consultant (Remotely) Spin-Off Brainy Physics / 2019 Physics Department, Michigan Technological University •	Providing expert advices relate to lens manufacture and developing of new lenses models for the start-up creation. •	Helping with the Business model creation. Applications & Technical Manager Lambda-X, Belgium / 2015 – 2019 •	Conducted a data regression analysis of the relationship between company stocks to improve the quality of the products. •	Increased accessibility and usability of customer data by redesigning data visualization techniques to include statistical graphs and information graphics. •	Tracking multiple customer service metrics with customer service analysis, finding tendencies and later creating the correspondent solutions together with the team. •	The increase in the quality of the technical service create more fidelity by part of the customers generating sales from 2M to 3.5M annually. •	New protocols were created for the manufacturing of the devices and testing of the software •	Worked with a team of 5+ to ideate, create, maintain, and update new prototypes as results 6 new software were developed and 3 new devices are now in the market. Project Manager Visiometrics-CD6, Spain / 2010-2015 •	Ensure strict adherence to the ISO req. for each device create. •	Manage project budget of 1M+ and ensure company obtains the best possible pricing; determine and minimize risk. •	Ensure that the project team understand all aspects of the contract relating to their respective responsibilities. Researcher and support engineer Visiometrics-CD6, Spain / 2007-2009 •	Liaised between design, production, and quality teams to ensure highest standard of quality was being met during each stage of development; Created new protocol in the manufacturing process. •	Refined and improved existing documentation system, resulting in reduced labor costs via increased workplace efficiency."
resume_text = resume_text.lower()

doc = nlp(resume_text)


professions = [nlp.make_doc(text) for text in words]

##############################################################################
#
#                   Using    phrase_matcher
#
##############################################################################

phrase_matcher = PhraseMatcher(nlp.vocab)

# phrase_matcher.add("COUNTRIES",None, *skill)
phrase_matcher.add("PROFESS", None, *professions)
# phrase_matcher.add("PROFESS", *professions)

matches = phrase_matcher(doc)
##############################################################################
#
#                   Using    Matcher
#
##############################################################################
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
matcher.add('PROFESS', [professions])
matches = matcher(doc)


job_list = []
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    job_list.append(span.text)    
    # print(match_id, string_id, start, end, span.text)
    # print(span.text)

job_names = pd.DataFrame(job_list)

job_names = job_names.drop_duplicates()







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
