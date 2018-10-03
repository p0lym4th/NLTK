#This python script shows how to import and read nltk corpus files
#
#Steven Large
#September 27th 2018

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown

print(gutenberg.fileids())

#This splits the corpus into sentences which are separated by a period. Each element of the resulting array contains, as elements, words (encoded with UTF-8)
print(gutenberg.sents('carroll-alice.txt')[0:2])

print(gutenberg.words('carroll-alice.txt')[0:5])
