s=open('bangchucai.txt','r',encoding='utf-8').read().split(' ')
import numpy as np

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


print(cosine(s,s))