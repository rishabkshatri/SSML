#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
#importing all the modules
import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))


#starting a function to clean the text iteratively
#by removing all the unnecessary symbols/stop words
#by using regular expressions module of python
def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = BeautifulSoup(text, "lxml").text # HTML decoding
    #using beautiful soup
    text = text.lower() # lowercase text
    #changing the case to lower
    text = REPLACE_BY_SPACE_RE.sub(' ', text) 
    # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) 
    # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) 	   # delete stopwors from text
    return text
    
df['post'] = df['post'].apply(clean_text)
print_plot(10)
#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
