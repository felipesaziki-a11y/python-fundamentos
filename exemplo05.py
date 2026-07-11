from typing import Dict, List, Tuple


def exe


def obter_clientes_com_score_alto(clientes: Dict[str, Dict[str, float]]):
    clientes_selecionados: List[str] = []
    for nome_cliente, dados_cliente in clientes.items():
        score = dados_cliente["score"]
        if score > 650:
    pass



def processar_disponibilidade():
    clientes = {
        "Bianca": {
            "salário": 2300,
            "id": 99,
            "score": 870
        },
        "Alexandre": {
            "salário": 2450,
            "id": 100,
            "score": 430
        },
        "Janice": {
            "salário": 2900,
            "id": 101,
            "score": 560
        },
        "Caio": {
            "salário": 2100,
            "id": 102,
            "score": 850
        }
    }


def percorrer_lista_vs_vetor_tupla():
    produtos: List[str] = ["Uva", "Morango", "Abacaxi"]
    for produto in produtos:
        print(produto)
    
    jogos: Dict[str] = {"unc": "Uncharted", "rnc": "Ratchet and Clank", "tm": "Twisted Metal"}
