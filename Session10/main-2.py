"""
REAL-WORLD PROJECT:
Semantic FAQ Search Engine using GloVe 50D Embeddings
-----------------------------------------------------
Problem:
A company has many FAQs.
Users ask questions in different wording.
Traditional keyword matching fails.

Solution:
Use GloVe embeddings to find semantically similar FAQs.

Example:
User asks:
"How can I reset my password?"

System should match:
"Forgot password recovery"

-----------------------------------------------------
Install:
pip install gensim numpy scikit-learn
"""

import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------------------------------------
# STEP 1: Load GloVe Model
# -------------------------------------------------------------
print("Loading GloVe model...")
model = api.load("glove-wiki-gigaword-50")
print("Model loaded successfully!")


# -------------------------------------------------------------
# STEP 2: Company FAQ Database
# -------------------------------------------------------------
faq_database = [
    {
        "question": "How do I reset my password?",
        "answer": "Go to settings > account > reset password."
    },
    {
        "question": "How can I track my order?",
        "answer": "Visit the orders page and click track shipment."
    },
    {
        "question": "What is the refund policy?",
        "answer": "Refunds are available within 30 days of purchase."
    },
    {
        "question": "How do I contact customer support?",
        "answer": "Email support@example.com or call customer care."
    },
    {
        "question": "How can I update my profile?",
        "answer": "Go to profile settings and edit your details."
    }
]


# -------------------------------------------------------------
# STEP 3: Sentence Embedding Function
# -------------------------------------------------------------
def sentence_embedding(sentence):
    words = sentence.lower().split()

    vectors = [
        model[word]
        for word in words
        if word in model
    ]

    if not vectors:
        return np.zeros(50)

    return np.mean(vectors, axis=0)


# -------------------------------------------------------------
# STEP 4: Precompute FAQ Embeddings
# -------------------------------------------------------------
for faq in faq_database:
    faq["embedding"] = sentence_embedding(faq["question"])


# -------------------------------------------------------------
# STEP 5: Semantic Search Function
# -------------------------------------------------------------
def search_faq(user_query):
    query_vector = sentence_embedding(user_query)

    best_match = None
    best_score = -1

    for faq in faq_database:
        score = cosine_similarity(
            [query_vector],
            [faq["embedding"]]
        )[0][0]

        if score > best_score:
            best_score = score
            best_match = faq

    return best_match, best_score


# -------------------------------------------------------------
# STEP 6: Interactive User Search
# -------------------------------------------------------------
print("\nSemantic FAQ Search Engine Ready!")
print("Type your question (or 'exit'):\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    result, confidence = search_faq(user_input)

    print("\nBest Match Found:")
    print("Matched FAQ:", result["question"])
    print("Answer:", result["answer"])
    print("Confidence Score:", round(confidence, 4))
    print("-" * 50)


# -------------------------------------------------------------
# SAMPLE TEST QUERIES:
# -------------------------------------------------------------
# "I forgot my login password"
# "Where is my shipment?"
# "Can I get my money back?"
# "Need help from support team"
# "Edit my account details"