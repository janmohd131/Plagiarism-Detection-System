import preprocess
import vectorize
import similarity
import sentence_tokenize
import semantic_similarity

files = ["data/file1.txt","data/file2.txt"]
document = []

for file in files:
    with open(file,"r") as f:
        data1 = f.read()

        tokenize__sentences = sentence_tokenize.tokenize_sentences(data1) #tokenizing the sentences
        clean_text = preprocess.preprocessing_text(" ".join(tokenize__sentences))
        document.append(clean_text)

tf_idf_matrix, features = vectorize.tfidf_vectorize(document) 


similarity_matrix = similarity.compute_cosine_similarity(tf_idf_matrix)  #this is checking the simililarity using vectorization



similarity_percentage = similarity_matrix[0][1]*100  # Earlier the results were in the form of the matrix so i needed in the form of the % form so to make it happen i multiplied with the 100 using slicing

print(f'The similarity between both file is: {similarity_percentage} %')
if similarity_percentage < 20:
    print("TF-IDF: No significant textual similarity detected.")
elif similarity_percentage < 40:
    print("TF-IDF: Minor word overlap detected.")
elif similarity_percentage < 60:
    print("TF-IDF: Possible copy-based similarity.")
elif similarity_percentage < 80:
    print("TF-IDF: High risk of plagiarism.")
else:
    print("TF-IDF: Strong copy-paste plagiarism detected.")
print()
print()
print()

# document level semantic detection
semantic_matrix = semantic_similarity.document_level_semantic_similarity_main(document)

semantic_percentage = semantic_matrix[0][1] * 100

print(f"Document Level Semantic Similarity: {semantic_percentage} %")
if semantic_percentage < 30:
    print("Low similarity – No plagiarism detected.")
elif semantic_percentage < 50:
    print("Moderate similarity – Possible paraphrasing detected.")
elif semantic_percentage < 70:
    print("High semantic similarity – Likely paraphrased plagiarism.")
else:
    print("Severe plagiarism – Meaning is almost identical.")




# senetence level detection

file_1_sentences = []
file_2_sentences = []

with open(files[0],"r") as f:
    text1 = f.read()
    sentences_1 = sentence_tokenize.tokenize_sentences(text1)

    for s in sentences_1:
        clean_s = preprocess.preprocessing_text(s)
        file_1_sentences.append(clean_s)

with open(files[1], "r") as j:
    text2 = j.read()
    sentences_2 = sentence_tokenize.tokenize_sentences(text2)

    for s in sentences_2:
        clean_s = preprocess.preprocessing_text(s)
        file_2_sentences.append(clean_s)

# Semantic level detection
semantic_matrix = semantic_similarity.semantic_similarity(
    file_1_sentences,
    file_2_sentences
)
print(semantic_matrix)
print("\n" + "="*40)
print("SEMANTIC PLAGIARISM DETECTION")
print("Meaning-Based Similarity Analysis")
print("="*40)


THRESHOLD = 0.75  # 75%

for i in range(len(semantic_matrix)):
    for j in range(len(semantic_matrix[i])):
        score = semantic_matrix[i][j]

        if score >= THRESHOLD:
            print()
            print(f"File1 Sentence {i+1}: {file_1_sentences[i]}")
            print(f"File2 Sentence {j+1}: {file_2_sentences[j]}")
            print(f"Similarity: {score*100:.2f}%")
            print("-"*50)


# Tf_Idf detection similarity
all_sentences = file_1_sentences + file_2_sentences

tf_idf_matrix1 , features1 = vectorize.tfidf_vectorize(all_sentences)

similarity_sentences = similarity.compute_cosine_similarity(tf_idf_matrix1)  # (file1+file2) x (file1+file2)
len1 = len(file_1_sentences)

print("\n" + "-"*40)
print("SENTENCE LEVEL SIMILARITY (TF-IDF)")
print("Exact Word Matching")
print("-"*40)


THRESHOLD_HIGH = 0.7
THRESHOLD_MEDIUM = 0.5

for i in range(len1):
    for j in range(len(file_2_sentences)):
        score = similarity_sentences[i][len1+j]
        if score >= THRESHOLD_HIGH:
            print("HIGH SIMILARITY WARNING")
            print(f"File1 Sentence {i+1}: {file_1_sentences[i]}")
            print(f"File2 Sentence {j+1}: {file_2_sentences[j]}")
            print(f"Similarity: {score*100}%")
            print("-"*50)

        elif score >= THRESHOLD_MEDIUM:
            print("MODERATE SIMILARITY")
            print(f"File1 Sentence {i+1}: {file_1_sentences[i]}")
            print(f"File2 Sentence {j+1}: {file_2_sentences[j]}")
            print(f"Similarity: {score*100}%")
            print("-"*50)
