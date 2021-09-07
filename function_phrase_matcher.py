# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:39:49 2021

@author: HZU
"""

import pandas as pd
import numpy as np
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

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
resumes = pd.read_csv('df_all_files.csv', encoding = 'utf-8')
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

#The pdf umber 11 is not getting the correct data
for i in range(len(resumes)):
    while resumes['name'][i] == 'NOVALUE':
        str_text = resumes['pdftext'][i]
        resumes['name'][i] =  str_text[:250]
    while resumes['address'][i] == 'NOVALUE':
        str_text = resumes['pdftext'][i]
        resumes['address'][i] =  str_text[:250]        
    else:
        next

resumes = resumes.astype(str)
resumes['name'] = resumes['name'].str.lower()
resumes['address'] = resumes['address'].str.lower()
resumes['id'] = resumes['id'].astype(int)


# load pre-trained model for all the functions.
nlp = spacy.load('en_core_web_sm')



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

resumes['new_name'] = 'NONVALUE'
resumes['new_name'] = resumes['name'].apply(lambda x: extract_name(x))
#reorgineze the order

#Function to extract the city from address
def extract_location(col_address):
    ## CSV with cities and countries names to list
    cities = pd.read_csv('utils/cities.csv', encoding = 'utf-8', header = None)
    cities[0] = cities[0].str.lower()
    cities[0] = cities[0].astype(str)
    cities_words = cities[0].tolist()    
    cities = [nlp.make_doc(text) for text in cities_words]
    countries = pd.read_csv('utils/countries.csv', encoding = 'utf-8', header = None)
    countries[0] = countries[0].str.lower()
    countries[0] = countries[0].astype(str)
    countries_words = countries[0].tolist()    
    countries = [nlp.make_doc(text) for text in countries_words]

    doc = nlp(col_address)
    phrase_matcher_cities = PhraseMatcher(nlp.vocab)
    phrase_matcher_countries = PhraseMatcher(nlp.vocab)
    phrase_matcher_cities.add("CITIES", None, *cities)
    phrase_matcher_countries.add("COUNTRY", None, *countries)
    matches_city = phrase_matcher_cities(doc)
    matches_country = phrase_matcher_countries(doc)
    
    cities_list = []
    country_list = []    
    for match_id, start, end in matches_city:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        cities_list.append(span.text)
    for match_id, start, end in matches_country:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        country_list.append(span.text)
        
    if len(cities_list) > 0 and len(country_list) == 0:
        result = [cities_list[0], 'country_unknown']        
    elif len(cities_list) == 0 and len(country_list) > 0:        
        result = ['little_unknown', country_list[0]]
    elif len(cities_list) > 0 and len(country_list) > 0:        
        result = [cities_list[0], country_list[0]]
    else:
        result = ['little_unknown', 'country_unknown']

    return result

resumes['cities_new'] = 'NONVALUE'
for i in range(202,500):
    text_address = resumes['address'][i]
    text_address = extract_location(text_address)
    resumes['cities_new'][i] = text_address

resumes['cities_new'] = resumes['cities_new'].astype(str)

data = resumes['cities_new'][202:500]

data = resumes['pdftext'][10]

###############################################################################
###############################################################################
import threading                                                                


items = resumes['address']

def process(items, start, end):                                                 
    for item in items[start:end]:                                               
        try:                                                                    
            text_address = extract_location(item)
            resumes['cities_new'][i] = text_address

                                             
        except AttributeError:                                                       
            print('error with item')                                            


def split_processing(items, num_splits=4):                                      
    split_size = len(items) // num_splits                                       
    threads = []                                                                
    for i in range(num_splits):                                                 
        # determine the indices of the list this thread will handle             
        start = i * split_size                                                  
        # special case on the last chunk to account for uneven splits           
        end = None if i+1 == num_splits else (i+1) * split_size                 
        # create the thread                                                     
        threads.append(                                                         
            threading.Thread(target=process, args=(items, start, end)))         
        threads[-1].start() # start the thread we just created                  

    # wait for all threads to finish                                            
    for t in threads:                                                           
        t.join()                                                                

split_processing(items)


items = resumes['address']
for item in items[1:3]:
    print(item)
    print('\n')

###############################################################################
###############################################################################
    
    








