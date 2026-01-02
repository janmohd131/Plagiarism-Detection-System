import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

import preprocess
import sentence_tokenize
import vectorize
import similarity
import semantic_similarity


# ==========================
# Window Setup
# ==========================
root = tk.Tk()
root.title("Plagiarism Detection System")
root.geometry("1100x750")
root.configure(bg="#0f172a")  # dark slate

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_SUB = ("Segoe UI", 11)
FONT_TEXT = ("Segoe UI", 10)

ACCENT = "#38bdf8"
CARD = "#020617"
TEXT_BG = "#020617"
TEXT_FG = "#e5e7eb"


# ==========================
# Header
# ==========================
header = tk.Frame(root, bg="#020617", height=90)
header.pack(fill="x")

tk.Label(
    header,
    text="Plagiarism Detection System",
    font=FONT_TITLE,
    fg="white",
    bg="#020617"
).pack(pady=(18, 2))

tk.Label(
    header,
    text="TF-IDF • Semantic Similarity • NLP",
    font=FONT_SUB,
    fg="#94a3b8",
    bg="#020617"
).pack()


# ==========================
# Input Area
# ==========================
content = tk.Frame(root, bg="#0f172a")
content.pack(fill="both", expand=True, padx=20, pady=15)

left = tk.Frame(content, bg=CARD)
left.grid(row=0, column=0, padx=10, pady=10)

right = tk.Frame(content, bg=CARD)
right.grid(row=0, column=1, padx=10, pady=10)

tk.Label(left, text="Document 1", font=("Segoe UI", 12, "bold"),
         fg="white", bg=CARD).pack(anchor="w", padx=10, pady=5)

text1 = tk.Text(left, width=60, height=14, bg=TEXT_BG,
                fg=TEXT_FG, insertbackground="white", wrap="word")
text1.pack(padx=10, pady=10)

tk.Label(right, text="Document 2", font=("Segoe UI", 12, "bold"),
         fg="white", bg=CARD).pack(anchor="w", padx=10, pady=5)

text2 = tk.Text(right, width=60, height=14, bg=TEXT_BG,
                fg=TEXT_FG, insertbackground="white", wrap="word")
text2.pack(padx=10, pady=10)


# ==========================
# Results Box
# ==========================
result_frame = tk.Frame(root, bg=CARD)
result_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    result_frame,
    text="Results",
    font=("Segoe UI", 14, "bold"),
    fg="white",
    bg=CARD
).pack(anchor="w", padx=10, pady=5)

result_box = tk.Text(
    result_frame,
    height=10,
    bg="#020617",
    fg="#e5e7eb",
    font=("Consolas", 10),
    wrap="word"
)
result_box.pack(fill="x", padx=10, pady=10)




# for highlighting sentences in the ui
text1.tag_config("highlight", background="#5F1CC9")
text2.tag_config("highlight", background="#5F1CC9")

text1.tag_remove("highlight", "1.0", tk.END)
text2.tag_remove("highlight", "1.0", tk.END)

def highlight_sentence(text_widget, sentence):
    start = "1.0"
    while True:
        pos = text_widget.search(sentence, start, stopindex=tk.END)
        if not pos:
            break
        end = f"{pos}+{len(sentence)}c"
        text_widget.tag_add("highlight", pos, end)
        start = end





# ==========================
# Logic
# ==========================
def check_plagiarism():
    doc1 = text1.get("1.0", tk.END).strip()
    doc2 = text2.get("1.0", tk.END).strip()

    if not doc1 or not doc2:
        messagebox.showwarning("Input Required", "Please enter both documents.")
        return

    result_box.delete("1.0", tk.END)

    # ---------- TF-IDF ----------
    cleaned_docs = [
        preprocess.preprocessing_text(doc1),
        preprocess.preprocessing_text(doc2)
    ]

    tfidf_matrix, _ = vectorize.tfidf_vectorize(cleaned_docs)
    tfidf_score = similarity.compute_cosine_similarity(tfidf_matrix)[0][1] * 100

    # ---------- Semantic Document ----------
    semantic_doc_score = semantic_similarity.document_level_semantic_similarity(
        doc1,doc2
    )
    semantic_doc_score = semantic_doc_score * 100

    # ---------- Sentence Level ----------
    sents1 = sentence_tokenize.tokenize_sentences(doc1)
    sents2 = sentence_tokenize.tokenize_sentences(doc2)

    sent_results = semantic_similarity.semantic_similarity(
        sents1, sents2
    )

    # ---------- Display ----------
    result_box.insert(tk.END, f"TF-IDF Similarity: {tfidf_score:.2f}%\n")
    if tfidf_score >= 80:
        result_box.insert(
        tk.END,
        "⚠️ High Text Matching Detected\n"
        "Large portions of the text use the same words or phrases.\n"
        "This indicates possible copy-paste plagiarism.\n\n"
    )

    elif tfidf_score >= 50:
        result_box.insert(
        tk.END,
        "⚠️ Moderate Text Matching\n"
        "Some sentences or phrases are similar in wording.\n"
        "The text may contain partially copied content.\n\n"
    )

    else:
        result_box.insert(
        tk.END,
        "✅ Low Text Matching\n"
        "The wording of both texts is mostly different.\n"
        "No direct copying detected.\n\n"
    )
    
    result_box.insert(tk.END, f"Semantic Similarity: {semantic_doc_score:.2f}%\n\n")

    if semantic_doc_score >= 80:
        result_box.insert(
        tk.END,
        "⚠️ High Meaning-Based Similarity Detected\n"
        "The two texts convey almost the same ideas, even if written differently.\n"
        "This strongly suggests paraphrased plagiarism.\n\n"
    )

    elif semantic_doc_score >= 50:
        result_box.insert(
        tk.END,
        "⚠️ Moderate Meaning-Based Similarity\n"
        "Some parts of the texts share similar ideas or meanings.\n"
        "There may be partial paraphrasing or reused concepts.\n\n"
    )

    else:
        result_box.insert(
        tk.END,
        "✅ Low Meaning-Based Similarity\n"
        "The texts express different ideas and meanings.\n"
        "No significant semantic plagiarism detected.\n\n"
    )

    result_box.insert(
    tk.END,
    "📌 Final Summary:\n"
    "- TF-IDF checks word-level copying\n"
    "- Semantic similarity checks meaning-level copying\n"
    "A high score in either may indicate plagiarism.\n\n"
    )



    result_box.insert(tk.END, "Sentence-level Matches:\n")

    for i, j, score in sent_results:
        result_box.insert(
            tk.END,
            f"- File1 Sentence {i+1} ↔ File2 Sentence {j+1} → {score*100:.2f}%\n"
        )

# highlighting sentences

    for i, j, score in sent_results:
        if score >= 0.75:
            highlight_sentence(text1, sents1[i])
            highlight_sentence(text2, sents2[j])


def export_csv():
    if not result_box.get("1.0", tk.END).strip():
        messagebox.showwarning("No Data", "Run plagiarism check first.")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not path:
        return

    doc1 = text1.get("1.0", tk.END).strip()
    doc2 = text2.get("1.0", tk.END).strip()

    sents1 = sentence_tokenize.tokenize_sentences(doc1)
    sents2 = sentence_tokenize.tokenize_sentences(doc2)

    sent_results = semantic_similarity.semantic_similarity(
        sents1, sents2, threshold=0.75
    )

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Sentence File1",
            "Sentence File2",
            "Semantic Similarity (%)",
            "Warning"
        ])

        for i, j, score in sent_results:
            writer.writerow([
                sents1[i],
                sents2[j],
                f"{score*100:.2f}",
                "Plagiarized"
            ])

    messagebox.showinfo("Exported", "CSV report generated successfully!")


# ==========================
# Buttons
# ==========================
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=15)

ttk.Button(
    btn_frame,
    text="Run Plagiarism Check",
    command=check_plagiarism
).grid(row=0, column=0, padx=15)

ttk.Button(
    btn_frame,
    text="Download CSV Report",
    command=export_csv
).grid(row=0, column=1, padx=15)


# ==========================
root.mainloop()
