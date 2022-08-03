#!/bin/python3

from os import environ
from re import compile
from re import match


import re
#
# Write the regular expression in the blank space below
#r'^[a-z]$|^([a-z]).*\1$'
regularExpression =r'^(a|b).*\1$|^[ab]$'
pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()

    if pattern.match(someString):
        result[i] = 'True'

print('\n'.join(result))
# with open(environ['OUTPUT_PATH'], 'w') as fileOut:
#     fileOut.write('\n'.join(result))


