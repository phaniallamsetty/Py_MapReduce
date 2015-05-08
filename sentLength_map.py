#!/usr/bin/env python

import sys
import string
import re

lines = ''
sen_count = 0
txt_len = 0
for line in sys.stdin:
  line = line.replace('\n','')
  lines = lines + line
  
txt = re.findall("[A-Z].*?[\.!?]", lines, re.MULTILINE | re.DOTALL )

sen_count = len(txt)

for sen in txt:
  words = sen.split()
  sen_len = 0
  for w in words:
    if w[0].isupper():
      sen_len = 0
    sen_len = sen_len + len(w)
  txt_len = txt_len + sen_len

avg_sen_len = txt_len/sen_count
print 'Sentence_Count\t%d' % (sen_count)
print 'Average_Sentence_Length\t%d' % (avg_sen_len)

    
