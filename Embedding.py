import numpy as np
import gensim
import os
import GeneralHelperFunctions
import typing
import pandas as pd


class RestartableCurpus():

    def __init__(self) -> None:
        """Corpus has to be a generator"""
    
    def __iter__(self) -> typing.Generator:
        def mini_gen() -> list[str]:
            for i in GeneralHelperFunctions.load_filtered_corpus():
                yield i.split(" ")
        return mini_gen()
        

def Word2Vec(corpus: typing.Generator | None = None) -> gensim.models.Word2Vec:
    W2V = gensim.models.Word2Vec(sentences=corpus, min_count= 20, window=5,vector_size=100, epochs= 5, sg=1, workers= os.cpu_count()*2)
    return W2V


def SaveWord2Vec(W2V: gensim.models.Word2Vec):
    W2V.save("W2V-Full.model")   
    W2VLite = W2V.wv
    W2VLite.save("W2V-Stripped.model")             


def LoadWord2VecStripped() -> gensim.models.KeyedVectors:
    return gensim.models.KeyedVectors.load("W2V-Stripped.model", mmap='r')

def get_pos_list(W2V: gensim.models.keyedvectors) -> list:
    l = []
    f1 = open('positive-words.txt')
    for i in f1:
        i = i.strip()
        if i in W2V.key_to_index.keys():
            l.append(i)
    return l

def get_neg_list(W2V: gensim.models.KeyedVectors) -> list:
    l = []
    f1 = open('negative-words.txt')
    print(W2V.key_to_index.keys())
    for i in f1:
        i = i.strip()
        if i in W2V.key_to_index.keys():
            l.append(i)
    return l

def make_embeding_vector(words: list):
    W2V = LoadWord2VecStripped()
    emb = 0
    for w in words:
        emb += W2V.get_vector(w)
    return emb/len(words)

def CheckProximityUnloaded(w1: list[str], w2: list[str]) -> pd.DataFrame:
    W2V = LoadWord2VecStripped()
    vembed = make_embeding_vector(w2)
    
    arr = np.empty((len(w1)), dtype=float)    
    print(len(w2))
    for i1, First in enumerate(w1):
        distance = np.sqrt(np.sum(np.square(vembed - W2V.get_vector(First))))
        arr[i1] = distance
    return pd.DataFrame(arr, w1 , ['distance'])
        
