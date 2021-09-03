import os
import re
import tabulate
from tika import parser
import pandas as pd

def extract_text_from_pdf(filenumber: str, path='./pdf/'):
    """
    Function that will put the text from the pdf in a list
    :param filenumber: filename without extension
    :param path: folder in the project where the file is located
    :return: a list of strings that make the text of the pdf file
    """
    res_tika = parser.from_file(path+filenumber+'.pdf')  # dictionary
    res = res_tika['content']
    res = res.replace(' \n', '')
    res = res.split('\n')
    return res


'''file = '1'
print(extract_text_from_pdf(filenumber=file, path='./pdf/'))'''


def sections(filenumber: str, path='./pdf/'):
    name, email, phone, address, hobby, experience, educ, skills, lang = [], [], [], [], [], [], [], [], []
    pdftext=[]
    for i in extract_text_from_pdf(filenumber=filenumber, path=path):

        i = re.sub(' +', ' ', i)
        i = i.strip()
        pdftext.append(i)

        if 'name' in i.lower():
            name.append(i)
        if any(map(i.lower().__contains__, ['email', 'e-mail', '@'])):
            email.append(i)
        if any(map(i.lower().__contains__, ['phone', 'mob', 'num', '+91'])):
            phone.append(i)
        if 'address' in i.lower():
            address.append(i)
        if any(map(i.lower().__contains__, ['hobby', 'hobbies'])):
            hobby.append(i)
        if any(map(i.lower().__contains__, ['employment', 'experience', 'work', 'position', 'role'])):
            experience.append(i)
        if any(map(i.lower().__contains__, ['academic', 'programs', 'courses', 'education', 'training', 'certification'])):
            educ.append(i)
        if any(map(i.lower().__contains__, ['programming', 'tech', 'it', 'skills'])):
            skills.append(i)
        if any(map(i.lower().__contains__, ['lang', 'languages'])):
            lang.append(i)
    return name, email, phone, address, hobby, experience, educ, skills, lang, pdftext

file = '5'
#print(extract_text_from_pdf(filenumber=file, path='./pdf/'))
result = sections(filenumber=file)
print(result[0], len(result[0]))
print(result[1], len(result[1]))
print(result[2], len(result[2]))
print(result[3], len(result[3]))
print(result[4], len(result[4]))
# print(result[-1], len(result[-1]))

'''
# print(extract_text_from_pdf(filenumber=file, path='./pdf/').keys())
print(extract_text_from_pdf(filenumber=file, path='./pdf/')['content'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['metadata'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['status'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['text'])
'''

datapath = './pdf_lite/'
def build_dictionnary():
    df = pd.DataFrame(columns=["id", "name", "email", "phone", "address", "hobby", "experience", "educ", "skills", "lang", "pdftext"])
    ids = []
    datas = []
    for filename in os.listdir(datapath):
        if filename.endswith(".pdf"):
            id = filename[:-4]
            ids.append(id)
            data_ = []
            for i in range(10):
                data = sections(filenumber=id, path=datapath)[i]
                #for s in data:
                #    s = re.sub(' +', ' ', s)
                #    s = s.strip()
                #    data_.append(s)
                data_.append(data)
            datas.append(data_)
            #print(datas[0][0], len(data_))
            dfrow = [id]
            for j in range(10):
                dfrow.append(datas[0][j])
            df.loc[len(df)] = dfrow
    #out = dict(zip(ids, datas))
    return df

df_100files = build_dictionnary()
print(df_100files.head().to_markdown())
