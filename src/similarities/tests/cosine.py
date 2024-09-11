import numpy as np
from src.similarities import cosine

query_embedding = np.array([1, 2, 3])
doc_embedding = np.array([4, 5, 6])

sim = cosine(query_embedding, doc_embedding)

result = {
    "index": 1,
    "similarity": sim
}

print(result)
