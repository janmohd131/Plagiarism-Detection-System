from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(tfidf_matrix):
    """
    Input: TF-IDF matrix
    Output: cosine similarity matrix
    """
    return cosine_similarity(tfidf_matrix)
