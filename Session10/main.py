"""
A-Z Small Demo: Understanding Word Embeddings using GloVe 50D
-------------------------------------------------------------
Goal:
- Load pretrained GloVe 50-dimensional embeddings
- Explore word vectors
- Find similar words
- Perform word analogies
- Compare sentence similarity
- Visualize embeddings

Install:
pip install gensim numpy scikit-learn
"""

import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------------------------------------
# A. Load GloVe Model
# -------------------------------------------------------------
print("Loading GloVe 50D model...")
model = api.load("glove-wiki-gigaword-50")
print("Model loaded successfully!")
print("Vocabulary size:", len(model))


# # -------------------------------------------------------------
# # B. Basic Word Vector
# # -------------------------------------------------------------
# word = "book"
# print(f"\nEmbedding for '{word}':")
# print(model[word][:50])  # Show first 50 dimensions


# # -------------------------------------------------------------
# # C. Closest Similar Words
# # -------------------------------------------------------------
# print(f"\nWords similar to '{word}':")
# similar_words = model.most_similar(word, topn=5)

# for similar_word, score in similar_words:
#     print(f"{similar_word}: {score:.4f}")


# # -------------------------------------------------------------
# # D. Word Analogy
# # king - man + woman ≈ queen
# # -------------------------------------------------------------
# print("\nAnalogy: king - man + woman = ?")
# analogy = model.most_similar(
#     positive=["king","woman"],
#     negative=["man"],
#     topn=3
# )

# for result, score in analogy:
#     print(f"{result}: {score:.4f}")


# # -------------------------------------------------------------
# # E. Sentence Embedding Function
# # Average word vectors
# # -------------------------------------------------------------
# def get_sentence_embedding(sentence):
#     words = sentence.lower().split()
#     vectors = [model[word] for word in words if word in model]

#     if not vectors:
#         return np.zeros(50)

#     return np.mean(vectors, axis=0)

# sentence1 = "I love machine learning"
# sentence2 = "Artificial intelligence is amazing"
# sentence3 = "Pizza tastes delicious"

# emb1 = get_sentence_embedding(sentence1)
# emb2 = get_sentence_embedding(sentence2)
# emb3 = get_sentence_embedding(sentence3)

# sim12 = cosine_similarity([emb1], [emb2])[0][0]
# sim13 = cosine_similarity([emb1], [emb3])[0][0]

# print("\nSentence Similarity:")
# print(f"'{sentence1}' <-(with)-> '{sentence2}' = {sim12:.4f}")
# print(f"'{sentence1}' <-(with)-> '{sentence3}' = {sim13:.4f}")



# # -------------------------------------------------------------
# # F. Interactive Search
# # -------------------------------------------------------------

# while True:
#     user_word = input("\nEnter a word to find similar words (or type 'exit'): ").lower()

#     if user_word == "exit":
#         break

#     if user_word in model:
#         print(f"Top similar words for '{user_word}':")
#         for sim_word, score in model.most_similar(user_word, topn=5):
#             print(f"  {sim_word}: {score:.4f}")
#     else:
#         print("Word not found in vocabulary.")
