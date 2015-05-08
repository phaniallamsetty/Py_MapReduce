#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = None
chunk_count = 0

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if old_word != key:
    if old_word:
      if old_word == "Average_Sentence_Length":
        word_count = word_count/chunk_count
      print '%s\t%s' % ( old_word,word_count)
    word_count = 0
  old_word = key
  if old_word == "Average_Sentence_Length":
    chunk_count = chunk_count + 1
  try:
    word_count = word_count + int(val)
  except:
    continue
if old_word == "Average_Sentence_Length":
  word_count = word_count/chunk_count
print '%s\t%s' % (old_word,word_count)
