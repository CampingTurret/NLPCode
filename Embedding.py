import numpy as np
import gensim
import os
import GeneralHelperFunctions
import typing
import pandas as pd


class RestartableCurpus():

    def __init__(self, corpus: typing.Generator) -> None:
        """Corpus has to be a generator"""
        GeneralHelperFunctions.safe_filtered_corpus(corpus)
    
    def __iter__(self) -> typing.Generator:
        return GeneralHelperFunctions.load_filtered_corpus()
        

def Word2Vec(corpus: typing.Generator | None = None) -> gensim.models.Word2Vec:
    W2V = gensim.models.Word2Vec(sentences=corpus, min_count= 20, window=8,vector_size=1000, epochs= 10, sg=1, workers= os.cpu_count()*2)
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
        if i in W2V.Vocab():
            l.append(i)
    return l

def get_neg_list(W2V: gensim.models.KeyedVectors) -> list:
    l = []
    f1 = open('negative-words.txt')
    for i in f1:
        if i in W2V.Vocab():
            l.append(i)
    return l


def CheckProximityUnloaded(w1: list[float] | float, w2: list[float] | float) -> pd.DataFrame:
    W2V = LoadWord2VecStripped()
    if isinstance(w1, float):
        w1 = [w1]
    if isinstance(w2, float):
        w2 = [w2]
    arr = np.empty((len(w1), len(w2)), dtype=float)    
    for i1, First in enumerate(w1):
        arr[i1,:] = W2V.distances(First, w2)

    return pd.DataFrame(arr, w2, w1)
        
