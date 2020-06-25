#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inFile = open(r'C:\Users\ENQRRUH\Desktop\Project Python\BSCS-DWH\ADDR23583409.889400.xml', 'r',encoding='utf-8').read()

# prints "123" by keeping all characters from the following ranges:
# 0020 — 007F   Basic Latin
# 00A0 — 00FF   Latin-1 Supplement
# 0100 — 017F   Latin Extended-A
# 0180 — 024F   Latin Extended-B
# \u0621-\u064A0-9 Arabic Characters

result = re.sub(r'[^\u0020-\u007F\u0621-\u064A0-9\u00A0-\u00FF\u0100-\u017F\u0180-\u024F]',r'', inFile)
print(result)

# generating an outputfile
outFile = open(r'C:\Users\ENQRRUH\Desktop\Project Python\BSCS-DWH\ADDR23583409.8894001.xml', 'w',encoding='utf-8')
outFile.writelines(result)
outFile.close()

