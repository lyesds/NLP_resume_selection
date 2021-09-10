import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-bright')

# resumes = pd.read_csv('./assets/super_cleaned_df.csv', encoding = 'utf-8')
# resumes['work_experience2'] = resumes['work_experience'].str.replace(' ', '')
# print(resumes.columns)
# print(resumes[resumes['id'] == 915].index[0])
# resumes.iloc[2, 8] = 'human/resource, learner'
# print(resumes.iloc[901:910].head().to_markdown())

def tf_idf(resumes, filenumber: int, subsetoption, filteringsection: str, similaritysection: str, scattersection: str):
    resumes['work_experience2'] = resumes['work_experience'].str.replace(' ', '')
    filteringsection_list = resumes[filteringsection][resumes['id'] == filenumber].values
    filteringsection_string = filteringsection_list[0].replace(',', '')
    filteringsection_string = filteringsection_string.replace('in ', '')
    filteringsection_string = filteringsection_string.replace('of ', '')
    filteringsection_list = list(filteringsection_string.split(' '))
    pattern = '|'.join(filteringsection_list)
    #print(pattern)
    subset = resumes[resumes[filteringsection].str.contains(pattern)]
    #print(subset.head().to_markdown())
    #print(subset.shape)

    if subsetoption:
        corpus = subset[similaritysection].values.tolist()
    else:
        corpus = resumes[similaritysection].values.tolist()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)

    pairwise_similarity = X * X.T
    arr = pairwise_similarity.toarray()
    np.fill_diagonal(arr, np.nan)

    input_doc = corpus[resumes[resumes['id'] == filenumber].index[0]]
    input_idx = corpus.index(input_doc)
    #print(input_doc, input_idx)

    input_arr_sorted = np.sort(arr[input_idx])[::-1][1:11]
    result_idx = np.argsort(arr[input_idx])[::-1][1:11]

    closest_cvs_filenumber = []
    for i in range(len(result_idx)):
        closest_cvs_filenumber.append(resumes.iloc[result_idx[i], 0])

    #print(input_arr_sorted)
    #print(resumes.loc[result_idx, ['id', similaritysection]].to_markdown())

    if subsetoption:
        corpus2 = subset[scattersection].values.tolist()
    else:
        corpus2 = resumes[scattersection].values.tolist()
    vectorizer2 = TfidfVectorizer()
    X2 = vectorizer2.fit_transform(corpus2)

    pairwise_similarity2 = X2 * X2.T
    arr2 = pairwise_similarity2.toarray()
    np.fill_diagonal(arr2, np.nan)

    input_doc = corpus[resumes[resumes['id'] == filenumber].index[0]]
    input_idx = corpus.index(input_doc)
    #print(input_doc, input_idx)

    arr2 = arr2[input_idx, result_idx]
    print(arr2)

    sns.set(font_scale=1.2)
    custom_markers = [',', '.', 'o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
    custom_palette = sns.color_palette(n_colors=10)

    fig, axs = plt.subplots(1, 1, figsize=(5, 5))
    fig.suptitle('10 closest CVs to CV '+str(filenumber)+'.pdf')
    sns.scatterplot(ax=axs, x=input_arr_sorted, y=arr2, hue=closest_cvs_filenumber, s=100, legend=False,
                    markers=custom_markers[0:10], palette="deep")
    sns.scatterplot(ax=axs, x=[1], y=[1])
    for i, txt in enumerate(closest_cvs_filenumber):
        axs.annotate(txt, (input_arr_sorted[i], arr2[i]))
    axs.text(x=0.5, y=1.05, s='The more upper right the closer the CV is', fontsize=10, alpha=0.75,
             ha='center', va='bottom', transform=axs.transAxes)
    plt.xlim(0, 1.05)
    plt.ylim(0, 1.05)
    plt.xlabel('Similarity for '+similaritysection)
    plt.ylabel('Similarity for '+scattersection)
    #plt.show()

    return fig, closest_cvs_filenumber  # the functions returns 1) the scatter plot and 2) the list of the 10 closest CVs


def tf_idf_list(resumes, filenumber: int, subsetoption, filteringsection: str, similaritysection: str, scattersection: str):
    resumes['work_experience2'] = resumes['work_experience'].str.replace(' ', '')
    filteringsection_list = resumes[filteringsection][resumes['id'] == filenumber].values
    filteringsection_string = filteringsection_list[0].replace(',', '')
    filteringsection_string = filteringsection_string.replace('in ', '')
    filteringsection_string = filteringsection_string.replace('of ', '')
    filteringsection_list = list(filteringsection_string.split(' '))
    pattern = '|'.join(filteringsection_list)
    #print(pattern)
    subset = resumes[resumes[filteringsection].str.contains(pattern)]
    #print(subset.head().to_markdown())
    #print(subset.shape)

    if subsetoption:
        corpus = subset[similaritysection].values.tolist()
    else:
        corpus = resumes[similaritysection].values.tolist()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)

    pairwise_similarity = X * X.T
    arr = pairwise_similarity.toarray()
    np.fill_diagonal(arr, np.nan)

    input_doc = corpus[resumes[resumes['id'] == filenumber].index[0]]
    input_idx = corpus.index(input_doc)
    #print(input_doc, input_idx)

    input_arr_sorted = np.sort(arr[input_idx])[::-1][1:11]
    result_idx = np.argsort(arr[input_idx])[::-1][1:11]

    closest_cvs_filenumber = []
    for i in range(len(result_idx)):
        closest_cvs_filenumber.append(resumes.iloc[result_idx[i], 0])

    if subsetoption:
        corpus2 = subset[scattersection].values.tolist()
    else:
        corpus2 = resumes[scattersection].values.tolist()
    vectorizer2 = TfidfVectorizer()
    X2 = vectorizer2.fit_transform(corpus2)

    pairwise_similarity2 = X2 * X2.T
    arr2 = pairwise_similarity2.toarray()
    np.fill_diagonal(arr2, np.nan)

    input_doc = corpus[resumes[resumes['id'] == filenumber].index[0]]
    input_idx = corpus.index(input_doc)
    #print(input_doc, input_idx)

    arr2 = arr2[input_idx, result_idx]

    return closest_cvs_filenumber  # the functions returns 1) the scatter plot and 2) the list of the 10 closest CVs



#print(tf_idf(filenumber=915, subsetoption=True, filteringsection='academic_titles', similaritysection='work_experience2', scattersection='hobbies'))
#print(tf_idf(filenumber=915, subsetoption=False, filteringsection='academic_titles', similaritysection='work_experience2', scattersection='hobbies'))
