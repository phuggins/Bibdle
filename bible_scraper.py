#%%
import nltk
import numpy as np

#%%
# import KJV of the bible
bible = nltk.corpus.gutenberg.words('bible-kjv.txt')

# %%
five_letter_words = []

for word in bible:
    if len(word) == 5:
        five_letter_words.append(word)

# %%
# Remove duplicates
final_list = set(five_letter_words)
final_list = [x.upper() for x in final_list]

# %%
with open('kjv_words.txt', 'w') as f:
    for item in final_list:
        f.write("%s\n" % item)
# %%
