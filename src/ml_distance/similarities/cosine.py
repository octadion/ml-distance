import math
from typing import List

def cosine(a: List[float], b: List[float]) -> float:
    """
    Returns the cosine similarity between vectors a and b.
    
    :param a: First vector
    :param b: Second vector
    :return: Cosine similarity
    """
    p = 0
    p2 = 0
    q2 = 0
    for i in range(len(a)):
        p += a[i] * b[i]
        p2 += a[i] * a[i]
        q2 += b[i] * b[i]
    return p / (math.sqrt(p2) * math.sqrt(q2))