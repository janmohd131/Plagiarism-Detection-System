import nltk

def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

