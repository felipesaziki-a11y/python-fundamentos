from pathlib import Path

# Padrão de nomenclatura:
# nome funções          snake_case
# nome de parâmetros    snake_case
# nome de variáveis     snake_case

def exemplo_01():
    # range é utilizado para ir de um ponto até outro, neste caso ir de 0 até 4
    for i in range(0, 5):
        print("Olá mundo", i)

def exemplo_02():
    # cwd é utilizado para pegar o diretório atual da execução do python
    diretorio_atual = Path.cwd()
    nome_novo_diretorio = "Arquivos"
    caminho_novo_diretorio = diretorio_atual / nome_novo_diretorio

    if caminho_novo_diretorio.exists() == False:
        # mkdir => make directory (Criar uma pasta)
        print("Criando pasta Arquivos")
        caminho_novo_diretorio.mkdir()
    
    texto = "Olá"

    for i in range(2000, 2027):
        nome_pasta_contas = "contas-celesc-" + str(i)
        caminho_contas_celesc = caminho_novo_diretorio / nome_pasta_contas
        caminho_contas_celesc.mkdir()
        
        for j in range(0, 10_000):
            texto = texto + "Mundo\n"
            nome_arquivo = "arquivo" + str(j) + ".txt"
            arquivo_caminho = caminho_contas_celesc / nome_arquivo
            with open(arquivo_caminho, "w") as file:
                file.write(texto)
        print(caminho_contas_celesc)



    print(caminho_novo_diretorio)
    # C:\Users\Francisco Aulas\Desktop\python-fundamentos + "Arquivos"
    # for i in range(0, 10):
    #     with open("arquivo.txt", "w+") as arquivo:
    #         arquivo.write("Abacate")

