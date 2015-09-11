"""
Minha análise de dados para inflammation.
"""

import numpy as np

global dados
dados = np.loadtxt(fname='inflammation.csv', delimiter=',')

def get_dados():
    return dados

def get_media():
    return dados.mean(axis=0)  # Temperatura média por dia

def get_max():
    return dados.max(axis=1)  # Temperatura máxima
