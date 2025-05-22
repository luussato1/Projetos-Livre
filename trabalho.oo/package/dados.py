import pickle
import os

def salvar_dados(caminho, biblioteca):
    with open(caminho, "wb") as f:
        pickle.dump(biblioteca, f)

def carregar_dados(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            return pickle.load(f)
    return None
