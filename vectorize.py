from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectorize(cleaned_documents):
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_documents)

    return tfidf_matrix, vectorizer.get_feature_names_out()
