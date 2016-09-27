import docx2txt

# extract text
path = "/home/input_folder_path/"
oppath = "/home/output_folder_path/"
import os
import re
txtfiles = os.listdir(path)
for docx in txtfiles :
    text = docx2txt.process(path + docx)
    f = open(oppath + docx[:-4] + "txt", 'w')
    f.write(newtext.encode('utf8'))
