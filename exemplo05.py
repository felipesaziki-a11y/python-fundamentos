from typing import Dict, List, Tuple


def obter_clientes_com_score_alto(clientes: Dict[str, Dict[str, float]]):
    clientes_selecionados: List[str] = []
    for nome_cliente, dados_cliente in clientes.items():
        score = dados_cliente["score"]
        if score > 650:
            clientes_selecionados.append(nome_cliente)
    return clientes_selecionados


def somar_salarios(clientes: Dict[str, Dict[str, float]]) -> float:
    total = 0
    for dados in clientes.values():
        salario = dados["salario"]
        total = total + salario
    return total


def obter_nome_clientes(clientes: Dict[str, Dict[str, float]]) -> List[str]:
    nomes = []
    for nome_cliente in clientes.keys():
        nomes.append(nome_cliente)
    return nomes


def processar_disponibilidade_emprestimo():
    clientes: Dict[str, Dict[str, float]] = {
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
    clientes_aprovados_para_emprestimo = obter_clientes_com_score_alto(clientes)
    total_salarios = somar_salarios(clientes)
    nome_clientes = obter_nome_clientes(clientes)


def percorrer_lista_vs_vetor_tupla():
    produtos: List[str] = ["Uva", "Morango", "Abacaxi"]
    for produto in produtos:
        print(produto)
    
    jogos: Dict[str] = {"unc": "Uncharted", "rnc": "Ratchet and Clank", "tm": "Twisted Metal"}
