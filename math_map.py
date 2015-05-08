#!/usr/bin/env python

import sys
import string
import math

def mapper():
  counter = 0
  num_sum = 0
  num_prime = 0

  for line in sys.stdin:
    nums = line.strip('\n')
    counter = counter + 1
    num_sum = num_sum + int(nums)
    if check_prime(int(nums)):
      num_prime = num_prime + 1

  print 'Num_Count \t %d' % (counter)
  print 'Num_Sum \t %d' % (num_sum)
  print 'Num_Prime \t %d' % (num_prime)

def check_prime(n):
  for k in range(2, math.sqrt(n) + 1):
    if n % k == 0:
      return False
  return True

mapper()
