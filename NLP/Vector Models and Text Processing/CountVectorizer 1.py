import pandas as pd
import numpy as np
import wget

from sklearn.feature_extraction.text import CountVectorizer

#MultinomialNB is the classifier for this choice.
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import wordnet

#nltk.download("wordnet")
#nltk.download("punkt")
#nltk.download("averaged_perceptron_tagger")

#download the document - had to download manually

# https://www.kaggle.com/shivamkushwaha/bbc-full-text-document-classification
#wget.download('https://lazyprogrammer.me/course_files/nlp/bbc_text_cls.csv')

# read file

df = pd.read_csv(r"C:\Users\Asus\Desktop\All Code\NLP\Vector Models and Text Processing\bbc_text_cls.csv")

#print(df.head())

inputs = df['text']
labels = df['labels']

labels.hist(figsize=(10,5))





