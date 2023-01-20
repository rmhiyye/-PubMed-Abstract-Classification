#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import spacy

stop_words = stopwords.words('english') # english stopwords
word_tokenize = spacy.blank("en")
stemmer = PorterStemmer()

def tokenise(document, remove_stop = True):
    '''
    Clean a document and return tokens
    Input: string, document 
    Output: normalised list of tokens from document    
    '''
    #cleaned = re.sub(r'[^\w\s_]+|\d+', '', document).strip().lower() # remove numbers because queries don't contain numbers
    
    tokenised = [str(tok).lower() for tok in word_tokenize(document)] # tokenise document
    
    #if remove_stop == True:
    #   text_clean = [token for token in tokenised if token not in stop_words and token not in string.punctuation]
        
    text_clean = []  
    if remove_stop == True:
        for word in tokenised:
            if (word not in stop_words and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
                stem_word = stemmer.stem(word)  # stemming word
                text_clean.append(stem_word)
    
            
    return text_clean

