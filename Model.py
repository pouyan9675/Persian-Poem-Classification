#!/usr/bin/python3
# -*- coding: utf-8 -*-
from hazm import *

class model:

    normalizer = Normalizer()
    stemmer = Stemmer()

    def __init__(self,label):
        self.label = label
        self.bigrams = 0
        self.unigrams = 0
        self.bigram={}
        self.unigram={}

    def unigram_and_bigram(self, text):
        count=0
        text = self.normalizer.normalize(text)
        tokens = word_tokenize(text)

        first_word = self.stemmer.stem(self.normalizer(tokens[0]))
        if first_word in self.unigram:
            self.unigram[first_word] += 1
        else:
            self.unigrams += 1
            self.unigram[first_word] = 1

        for i in range(0, len(tokens)-1):
            w1 = self.stemmer.stem(tokens[i])
            w2 = self.stemmer.stem(tokens[i+1])
            model = (w1, w2)

            if w2 in self.unigram:
                self.unigram[w2] += 1
            else:
                self.unigrams += 1
                self.unigram[w2] = 1

            if model in self.bigram:
                self.bigram[model] += 1
            else:
                self.bigram[model] = 1
                self.bigrams += 1


    def print_all(self):
        print('Bigram : ' + str(self.bigrams) + ' , Unigrams : ' + str(self.unigrams))
        print(self.bigram)
        print(self.unigram)
