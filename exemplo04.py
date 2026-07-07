from rich.console import Console
from rich.table import Table
import requests
import os


url_base = "https://api.franciscosensaulas.com"

def menu():
    opcoes_menu = {
        "Consultar categorias",
        "Cadastrar categoria",
        "Editar categoria",
        "Apagar categoria",
        "Sair"
    }

    menu_escolhido = ""