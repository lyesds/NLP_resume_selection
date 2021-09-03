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
    res = res.strip()
    res = res.split('\n')
    res_=[]
    for i in res:
        i = re.sub(' +', ' ', i)
        i = i.strip()
        res_.append(i)
    return res_


'''file = '2'
print(extract_text_from_pdf(filenumber=file, path='./pdf/'))'''

'''
# print(extract_text_from_pdf(filenumber=file, path='./pdf/').keys())
print(extract_text_from_pdf(filenumber=file, path='./pdf/')['content'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['metadata'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['status'])
# print(extract_text_from_pdf(filenumber=file, path='./pdf/')['text'])
'''

def sections(filenumber: str, path='./pdf/'):
    name, email, phone, address, hobby, experience, educ, skills, lang = [], [], [], [], [], [], [], [], []
    pdftext=[]

    extracted = extract_text_from_pdf(filenumber=filenumber, path=path)
    for i in extracted:
        #i = re.sub(' +', ' ', i)
        #i = i.strip()
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
        if any(map(i.lower().__contains__, ['employment', 'experience', 'work', 'position', 'role',
                                            'history',
                                            'professional',
                                            'background',
                                            'career',
                                            'freelance',
                                            'army',
                                            'military'])):
            experience.append(i)
            experience.append(extracted[extracted.index(i)+1:extracted.index(i)+6])
        if any(map(i.lower().__contains__, ['academic', 'programs', 'courses', 'education', 'training', 'certification',
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
                                            ])):
            educ.append(i)
            educ.append(extracted[extracted.index(i)+1:extracted.index(i)+6])
        if any(map(i.lower().__contains__, ['programming', 'tech', 'it', 'skills',
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
                                            ])):
            skills.append(i)
            skills.append(extracted[extracted.index(i)+1:extracted.index(i)+6])
        if any(map(i.lower().__contains__, ['lang', 'languages'])):
            lang.append(i)
    return name, email, phone, address, hobby, experience, educ, skills, lang, pdftext

file = '1'
#print(extract_text_from_pdf(filenumber=file, path='./pdf/'))
result = sections(filenumber=file)
print(result[0], len(result[0]))
print(result[1], len(result[1]))
print(result[2], len(result[2]))
print(result[3], len(result[3]))
print(result[5], len(result[5]))
print(result[-1], len(result[-1]))


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
                data_.append(data)
            #datas.append(data_)
            #print(data_)
            #print(datas[0][0], len(data_))
            dfrow = [id]
            for j in range(10):
                #if len(data_[j]) < 2 :
                if not any(isinstance(e, list) for e in data_[j]):
                #if not res:
                    dfrow.append(' '.join(data_[j]))
                else:
                    dfrow.append(data_[j])
        df.loc[len(df)] = dfrow
    return df

df_100files = build_dictionnary()
print(df_100files.tail().to_markdown())
df_100files.to_csv('./assets/df_100files.csv',sep=',', index=False, mode='w')