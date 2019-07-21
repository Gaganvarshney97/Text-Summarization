
# coding: utf-8

# In[3]:


import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
sentence_data = open('pa.txt').read()
stopwords = set(stopwords.words("english"))
# Removing Square Brackets and Extra Spaces
sentence_data = re.sub(r'\[[0-9]*\]', ' ', sentence_data)  
sentence_data = re.sub(r'\s+', ' ', sentence_data)  
#print(sentence_data)
# Removing special characters and digits
sentence_text = re.sub('[^a-zA-Z]', ' ', sentence_data )  
sentence_text = re.sub(r'\s+', ' ', sentence_text) 
#print(sentence_text)
sent_list = sent_tokenize(sentence_data)
words=word_tokenize(sentence_text)
#print(words)

word_frequencies = {}  
for word in words: 
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
            
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    
sentence_scores = {}  
for sent in sent_list:  
    for word in word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
import heapq  
summary_sentences = heapq.nlargest(1, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary)

