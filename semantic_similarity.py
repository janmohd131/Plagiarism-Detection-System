from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity_main(sentences1, sentences2):
   
    embeddings1 = model.encode(sentences1)
    embeddings2 = model.encode(sentences2)

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(embeddings1, embeddings2)

    return similarity_matrix

def document_level_semantic_similarity_main(documents):
    """
    documents: list of strings (2 documents)
    returns: cosine similarity matrix
    """

    # convert text → embeddings (numbers)
    embeddings = model.encode(documents)

    # cosine similarity on embeddings
    similarity_matrix = cosine_similarity(embeddings)

    return similarity_matrix

# for the Ui
def document_level_semantic_similarity(doc1, doc2):
    """
    Computes semantic similarity between two documents
    """
    embeddings = model.encode([doc1, doc2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    return similarity[0][0]


def semantic_similarity(sentences1, sentences2, threshold=0.75):
    embeddings1 = model.encode(sentences1)
    embeddings2 = model.encode(sentences2)

    sim_matrix = cosine_similarity(embeddings1, embeddings2)

    results = []
    for i in range(len(sentences1)):
        for j in range(len(sentences2)):
            score = sim_matrix[i][j]
            if score >= threshold:
                results.append((i, j, score))

    return results
