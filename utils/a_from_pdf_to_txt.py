import os
from pdfminer.high_level import extract_text, extract_text_to_fp

# path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'

def extract_text_from_pdf(filenumber: str, path='./pdf/'):
    res = extract_text(path+filenumber+'.pdf') # raw text
    res = res.replace(' \n', '')
    res = res.split('\n\n')
    #return res, len(res)
    return res

# testing other outputs... not working
# tags = extract_text_to_fp(inf=path+filenum+'.pdf', outfp='tags.txt', output_type='tag')

print(extract_text_from_pdf(filenumber='1', path='./pdf/'))


datapath = './pdf_lite/'
def build_dictionnary():
    ids = []
    datas = []
    for filename in os.listdir(datapath):
        if filename.endswith(".pdf"):
            id = filename[:-4]
            ids.append(id)
            data = extract_text_from_pdf(filenumber=id, path=datapath)
            datas.append(data)
            print(id)
    return dict(zip(ids, datas))


# print(build_dictionnary())