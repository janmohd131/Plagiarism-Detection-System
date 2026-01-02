# Plagiarism-Detection-System
📄 Plagiarism Detection System using NLP (TF-IDF + Semantic Similarity)
🚀 Project Overview

Welcome to my Plagiarism Detection System built with Python and Natural Language Processing (NLP)! This system is designed to help identify plagiarism at two critical levels:

Lexical Similarity (Exact or near-exact word matching) using TF-IDF

Semantic Similarity (Meaning-based plagiarism) using Sentence Embeddings

Unlike typical plagiarism checkers that just return a percentage, this system goes a step further:

Detects plagiarism at the document level.

Detects plagiarism at the sentence level.

Highlights which sentences are plagiarized.

Generates detailed CSV/PDF reports.

Provides an interactive Tkinter-based user interface.

This project was a learning-by-doing experience, where each challenge taught me practical NLP concepts rather than just theoretical knowledge.

🧠 What is NLP?

Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables computers to understand and analyze human language. In this project, NLP plays a key role in:

Cleaning raw text (e.g., removing punctuation, converting to lowercase).

Breaking text into sentences for comparison.

Converting text into numerical form for analysis.

Comparing similarities between texts and sentences.

Detecting plagiarism based on both exact words and meaning.

🎯 Why This Project?

At first, I thought plagiarism detection was just about comparing two documents. However, I soon realized that it’s about understanding:

Which sentences are copied?

Which sentences are paraphrased?

Do two texts have the same meaning but use different words?

This insight motivated me to build a comprehensive plagiarism detection system that does more than just surface-level comparisons.

⚙️ Features
✅ Document-Level Detection

TF-IDF similarity score (word-based) to detect lexical plagiarism.

Semantic similarity score (meaning-based) to identify paraphrasing.

✅ Sentence-Level Detection

Identify which specific sentence in File 1 matches which sentence in File 2.

Works for both TF-IDF and semantic similarity.

✅ NLP Pipeline

Text cleaning (e.g., converting to lowercase, removing punctuation).

Sentence tokenization.

Vectorization of sentences.

Similarity computation using cosine similarity.

✅ User Interface (Tkinter)

Paste two texts or upload documents.

One-click plagiarism check.

Clear and concise similarity results.

User-friendly warnings for plagiarized content.

✅ Reports

CSV report with:

Sentence pairs.

Similarity scores.

Highlighted plagiarized sentences.

Perfect for academic submissions or project reports.

🛠 Technologies Used

Python – The main programming language used.

NLTK – For sentence tokenization.

Scikit-learn – Used for TF-IDF and cosine similarity.

Sentence-Transformers – For calculating semantic similarity between sentences.

Tkinter – For building the graphical user interface (GUI).

Pandas – For generating CSV reports.

🔍 How the System Works

1️⃣ Text Input
The user enters or uploads two documents for comparison.

2️⃣ Preprocessing
The system converts the text to lowercase, removes unnecessary punctuation, and preserves sentence boundaries for accurate comparison.

3️⃣ Sentence Tokenization
The text is broken down into individual sentences for fine-grained comparison.

4️⃣ TF-IDF Similarity
The system calculates the word-based similarity (exact or near-exact plagiarism).

5️⃣ Semantic Similarity
It computes the meaning-based similarity by comparing sentence embeddings, identifying paraphrased content.

6️⃣ Result Interpretation

The system provides similarity percentages.

Clear warnings for plagiarized content.

Highlighted sentences with potential plagiarism.

⚠️ Similarity Warnings

The system provides user-friendly warnings based on the similarity scores:

TF-IDF (Word Matching):

80%+ → High word-level plagiarism.

50–79% → Moderate similarity.

Below 50% → Low similarity.

Semantic Similarity (Meaning):

80%+ → High meaning-based plagiarism.

50–79% → Some sentences share a similar meaning.

Below 50% → Mostly original content.

📊 Example Use Case

Academic assignments: Checking student work for plagiarism.

Research papers: Verifying originality of scientific or academic content.

Learning NLP concepts: A practical project to apply NLP techniques.

Portfolio project: Showcasing NLP skills for students or developers.

🧩 Challenges Faced & Lessons Learned

Throughout this project, I encountered several challenges, each offering valuable lessons:

Understanding TF-IDF matrices: I learned why TF-IDF can produce large matrices and how to interpret them.

Sentence tokenization issues: I had to ensure the preprocessing step didn't accidentally break sentence boundaries.

Interpreting cosine similarity: Figuring out how to properly interpret the similarity between sentence embeddings was tricky but rewarding.

Performance on local machines: Handling the heavy computations required for semantic models was a learning curve, especially with hardware limitations.

Each error and challenge taught me more about NLP and how systems work in practice, beyond the theoretical concepts.

🚀 Future Improvements

PDF report export: Allow users to generate PDF reports.

Better sentence highlighting: Improve the UI to highlight plagiarized sentences more effectively.

Multi-document comparison: Extend the system to compare more than two documents at once.

Performance optimization: Improve the efficiency of the system, especially for larger documents.

Web-based version: Create a web version using Flask or FastAPI for broader accessibility.

👨‍💻 Author

Jan Muhammad
Software Engineering Student
Passionate about learning NLP, Python, and AI through real-world projects.

⭐ Final Note

This project represents my journey from basic text comparison to building a real-world plagiarism detection system using NLP. It reflects not just the technical skills I developed, but also my problem-solving mindset, persistence, and a deep desire to understand systems at their core.
