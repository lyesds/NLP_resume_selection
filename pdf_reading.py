# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:42:48 2021

@author: HZU
"""
from pdfminer.high_level import extract_text



path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'
filepdf = path+'\\1.pdf'


resume_text_2 = extract_text(filepdf)



from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open(filepdf, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

from pprint import pprint
pprint(output_string.getvalue())

resume_text = output_string.getvalue()


from pdfminer.high_level import extract_pages
for page_layout in extract_pages(filepdf):
    for element in page_layout:
        print(element)
        
        
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
for page_layout in extract_pages(filepdf):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())
            
l =[]

import pandas as pd
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

path = r'C:\Users\HZU\Documents\AI_Becode\2021-08-30_NLP_resume_selection\files\pdf'
filepdf = path+'\\2.pdf'

font_size = []
bold_lines=[]
max_line = []
for page_layout in extract_pages(filepdf):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                # print(text_line)
                for character in text_line:
                    if isinstance(character, LTChar):
                        # pprint(character.fontname)
                        # pprint(character.size)
                        # l.append(character.fontname)
                        if 'Bold' in character.fontname:
                            bold_lines.append(text_line.get_text())
                        #get all the font sizes
                        font_size.append(character.size)

#drop min and max in list
font_size.remove(max(font_size))
font_size.remove(min(font_size))
#drop duplicates in list
font_size = list(dict.fromkeys(font_size))

for page_layout in extract_pages(filepdf):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                for character in text_line:
                    if isinstance(character, LTChar):
                        if character.size in font_size:
                            max_line.append(text_line.get_text())

df_bold = pd.DataFrame(bold_lines)
df_bold = df_bold.drop_duplicates()
df_bold.reset_index(drop=True, inplace=True)










