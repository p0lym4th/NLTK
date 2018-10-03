#This python script implements the bag-of-words strategy on a text file
#
#Steven Large
#September 27th 2018

import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.snowball import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer


generic_string = "This is a simple string of text. It contains two sentences."
complex_string = "This is a more complicated string, isn\'t it?"

print(sent_tokenize(generic_string))
print(sent_tokenize(generic_string,language="english"))

print("\n\n")

for sentence in sent_tokenize(generic_string,language="english"):
	print(sentence)
print("\n\n")

tbwt = TreebankWordTokenizer()

print(tbwt.tokenize(generic_string))

print("\n\n")

#This example parses the contraction WRONG
print(tbwt.tokenize(complex_string))

print("\n\n")

#The string in what follows is a 'regular expression'
ret = RegexpTokenizer('[a-zA-Z0-9\'\.]+')

#The following should correctly parse the contraction
print(ret.tokenize(complex_string))

print("\n\n")

sw = set(stopwords.words('english'))

simple_Token = tbwt.tokenize(generic_string)
clean_Token = [t for t in simple_Token if t not in sw]

for word in simple_Token:
	print(word.encode('UTF-8'))

print("\n")

for word in clean_Token:
	print(word.encode('UTF-8'))

print("\n\n")

ess = SnowballStemmer('english',ignore_stopwords=True)
print(ess.stem("flies"))

