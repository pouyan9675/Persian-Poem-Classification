#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from hazm import *
import os, resource
import time
import Model

def class_parser(file):
    filename = os.path.basename(file)
    info = filename.split('-')
    return (info[0], info[1])

def count_words(file):
    with open ('dataset/' + os.path.basename(file), "r") as txt:
        content = txt.read()
        norm = normalizer.normalize(content)
        global words
        words += len(norm.split(' '))

def current_time_millis():
    millis = int(round(time.time() * 1000))
    return millis


start = current_time_millis()

path = 'dataset'
files = os.listdir(path)

number = 0
for file in files:
    language_model = []
    with open ('dataset/' + os.path.basename(file), "r") as txt:
        content = txt.read()
        unigram_and_bigram(content)
        number += 1

        # print("Working on " + str(number) + "th file...")
        # if number > 2000:
            # break

for cc in names:
    print(cc)
print('Total bigrams : ' + str(bigrams))
print('Total unigrms : ' + str(unigrams))
print('Used RAM : ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + ' MB')
# print(models)

# print('Total words : ' + str(words))

end = current_time_millis()
print('Calculation finished in ' + str((end - start) / 1000) + ' seconds...')
