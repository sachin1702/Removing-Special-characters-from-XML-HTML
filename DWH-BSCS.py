import os,glob
import re
import paramiko
import cx_Oracle 

folder_path = r'C:\Users\Desktop\Project Python\BSCS-DWH'

for filename in glob.glob(os.path.join(folder_path, '*.xml')):
  #with open(filename, 'r') as f:
    # Open the file and read to generate Information in string format
    
    
    # 0020 — 007F   Basic Latin
    # 00A0 — 00FF   Latin-1 Supplement
    # 0100 — 017F   Latin Extended-A
    # 0180 — 024F   Latin Extended-B
    # \u0621-\u064A0-9 Arabic Characters
   

    result = re.sub(r'[^\u0020-\u007F\u00A0-\u00FF\u0100-\u017F\u0180-\u024F\u0621-\u064A0-9]',r'', inFile)
    print(result)

    # generating an outputfile
    outFile = open(filename, 'w',encoding='utf-8')
    outFile.writelines(result)
    outFile.close()
    text = f.read()
    print (filename)'''

