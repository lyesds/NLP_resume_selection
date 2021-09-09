import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# load pre-trained model for all the functions.

# please run this in the terminal before (770MB download): python -m spacy download en_core_web_lg
'''nlp = spacy.load('en_core_web_lg')


doc1 = nlp("computer")
doc2 = nlp("surgery")
doc3 = nlp("laws")
doc4 = nlp("computation")'''

# Similarity of two documents
#print(doc1, "<->", doc2, doc1.similarity(doc2))
#print(doc1, "<->", doc3, doc1.similarity(doc3))
#print(doc1, "<->", doc4, doc1.similarity(doc4))

# Similarity of tokens and spans
#french_fries = doc1[2:4]
#burgers = doc1[-1]
#print(french_fries, "<->", burgers, french_fries.similarity(burgers))

'''corpus = ['computer', 'surgery', 'laws', 'computation']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.shape)
print(X)
'''

resumes = pd.read_csv('./assets/super_cleaned_df.csv', encoding = 'utf-8')
#print(resumes.info())
#resumes.iloc[2, 8] = 'human/resource, learner'

print(resumes['id'].iloc[901:910].head().to_markdown())

corpus = resumes['work_experience'].values.tolist()
print(corpus[:5], len(corpus))

'''corpus_ = [e.split(', ') for e in corpus]
print(corpus_[:5], len(corpus_))

corpus2 = []
count = 0
for e in corpus:
    L1 = e.split()
    L2 = [i.strip(',') for i in L1]
    count += len(set(L2))
    #corpus2.append(ii)
print(count)
#print(corpus2[:5], len(corpus2))'''

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

features = vectorizer.get_feature_names()
print(len(features))
print(X.shape)
print(X[1:3], X[1:3].size)

pairwise_similarity = X * X.T
arr = pairwise_similarity.toarray()
np.fill_diagonal(arr, np.nan)

input_doc = corpus[905]
input_idx = corpus.index(input_doc)
print(input_doc, input_idx)

# result_idx = np.nanargmax(arr[input_idx])
print(arr[input_idx])
input_arr_sorted = np.sort(arr[input_idx])
print(input_arr_sorted)
#result_idx = np.argpartition(arr[input_idx], -4)[-4:]
result_idx = np.argsort(arr[input_idx])[::-1][1:11]
print(result_idx, len(result_idx))
#print(corpus[result_idx], result_idx)

closest_cvs_filenumber = []
for i in range(len(result_idx)):
    closest_cvs_filenumber.append(resumes.iloc[result_idx[i], 0])
print(closest_cvs_filenumber)

print(resumes.loc[result_idx, ['id', 'work_experience']].to_markdown())



