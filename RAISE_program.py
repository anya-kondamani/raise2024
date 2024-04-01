#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:07:00 2024

@author: anyakondamani
"""

from collections import Counter
import re
import pandas as pd


data = pd.read_csv("Dataset_10k.csv")
english_data = data[data["language"]=='en']
titles = english_data["title"].astype(str)
all_titles_text = ' '.join(titles)
clean_text = re.sub(r'[^a-zA-Z\s]', '', all_titles_text).lower()
words = clean_text.split()
word_frequencies = Counter(words)
words_df = pd.DataFrame(list(word_frequencies.items()), columns=['Word','Frequency'])
words_df = words_df.sort_values(by='Frequency', ascending=False)
words_to_remove = ['ai','artificial','intelligence','the','and','a','to','of','in','for','is','with','on','it','can','will','as','by','be','are','at','an','how','that','its','what','from']
df = words_df[~words_df['Word'].isin(words_to_remove)]
#print(df.head(20))

titles_sources_df=data[['title','source']]
merged_df=pd.merge(titles_sources_df,df,left_on='title',right_on='Word',how='right')
correlation_matrix=merged_df.groupby(['source','Word']).size().unstack(fill_value=0)
print(correlation_matrix)