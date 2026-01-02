import string
import nltk
from nltk.corpus import stopwords
import re

# Get the list of English stopwords
stopwords = set(stopwords.words('english'))




def preprocessing_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    text = text.split()

   


    clean_text = []
    for i in text:
        if i not in stopwords:
            clean_text.append(i)
    
    return " ".join(clean_text)

