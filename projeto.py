# nome primeiro+ultimo - string
# idade - int
# cidade - string
# area profissional - string
# assunto - string
# genero - m/f - char
# valor consulta - double
# tipo consulta - presencial/online - string
# data consulta - data
# casado/casada - boolean
# filhos - boolean
# notas - string

from datetime import datetime
import os as fsos
import json

filename = "./Dados/Projeto_consultas.json"
listagem = []  # lista com dicionários, onde cada elemento representa um cliente

# Verificar se o ficheiro existe, caso exista, carregar os dados para a variável listagem e caso contrário, criar uma lista vazio.
if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        listagem = json.load(manipfile)

    # print(listagem)
    print("Dados carregados com sucesso!")
else:
    print("O ficheiro ainda não existe. Criado neste momento um dicionário vazio...")
    listagem = []


# definition - uma função para o "menu de introdução".
def introducao():
    print("\nSeja bem-vindo/a ao sistema de cadastro de clientes!")
    print("Onde é possível criar, ler, atualizar e apagar clientes.")
    print("App criada por: Ricardo Tavares. 2026")


# definition - uma função para o "menu de opções".
def menu2():
    flag = True  # flag para controlar o loop do menu, para garantir que o usuário escolha uma opção válida
    escolha = 0  # variável para armazenar a escolha do usuário
    while flag:
        flag = False  # resetar a flag para evitar loop infinito, a menos que o usuário escolha uma opção inválida
        print("\n------ Menu APP------")
        print("1 - Pesquisar cliente")
        print("2 - Ordenação dados cliente")
        print("3 - Atualizar cliente")
        print("4 - Criar cliente")
        print("5 - Apagar cliente")
        print("6 - Estatísticas")
        print("7 - Sair da APP")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "7" or len(escolha) != 1:
            print("\nOpção errada, escolha de novo")
            flag = True
        if escolha == "7":
            print("A sair da app...")
            flag = False
    return escolha


# definition - uma função para gerar o próximo ID, que é o ID do último cliente + 1, ou 1 se a lista estiver vazia.
def gerar_proximo_id(lista_clientes):
    if not lista_clientes:  # uso a negação para verificar se a lista está vazia, o que é mais eficiente do que verificar o comprimento da lista
        return 1  # Se a lista estiver vazia, o primeiro ID é 1

    # Pega no último dicionário da lista e procura dentro do campo "id" o valor e soma 1
    ultimo_id = lista_clientes[-1]["id"]
    return ultimo_id + 1


# definition - uma função para pesquisar um cliente.
def pesquisar_clientes():
    flag = True
    while flag:
        flag = False
        escolha = ""
        print("\n------ Menu PESQUISA ------")
        print("1 - Pesquisar por Nome")
        print("2 - Pesquisar por ID")
        print("3 - Pesquisar Data Consulta")
        print("4 - Pesquisar por Cidade")
        print("5 - Pesquisar por Idade")
        print("6 - Listar TODOS os clientes")
        print("7 - Sair da pesquisa")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "7" or len(escolha) != 1:
            print("\nOpção errada, escolha de novo")
            flag = True
        else:
            match escolha:
                case "1":
                    encontrou = False
                    print("\nPesquisar por Nome")
                    procurarNome = input("\nEscreva o Nome a pesquisar: ")
                    if procurarNome.isdigit():
                        print("\nTem de usar letras para pesquisar por nome.")
                        flag = True
                        continue
                    for cliente in listagem:
                        if cliente["nome"].lower() == procurarNome.lower():
                            print(cliente)
                            encontrou = True
                            flag = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                        flag = True
                case "2":
                    encontrou = False
                    print("\nPesquisar por ID")
                    procurarNome = input("\nEscreva o ID a pesquisar: ")
                    if not procurarNome.isdigit():
                        print("\nTem de usar números para pesquisar por ID.")
                        flag = True
                        continue
                    for cliente in listagem:
                        if cliente["id"] == int(procurarNome):
                            print(cliente)
                            encontrou = True
                            flag = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                        flag = True

                case "3":
                    encontrou = False
                    print("\nPesquisar por Data da Consulta")
                    procurarNome = input(
                        "\nEscreva a Data da Consulta a pesquisar (AAAA-MM-DD): "
                    )
                    try:
                        # Tenta converter o texto numa data real para não acontecer 2024-02-45.
                        datetime.strptime(procurarNome, "%Y-%m-%d")

                        # Se passou, a data é válida.
                        for cliente in listagem:
                            if cliente["data_consulta"] == procurarNome:
                                print("\n", cliente)
                                encontrou = True
                                flag = True
                    except ValueError:
                        print(
                            "\nErro: Data não encontrada ou formato errado. Use AAAA-MM-DD (ex: 2024-05-18)."
                        )
                case "4":
                    encontrou = False
                    print("\nPesquisar por Cidade")
                    procurarNome = input("\nEscreva o Nome da Cidade a pesquisar: ")
                    if procurarNome.isdigit():
                        print("\nTem de usar letras para pesquisar por nome da cidade.")
                        flag = True
                        continue
                    for cliente in listagem:
                        if cliente["cidade"].lower() == procurarNome.lower():
                            print(cliente)
                            encontrou = True
                            flag = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                        flag = True

                case "5":
                    encontrou = False
                    print("\nPesquisar por Idade")
                    procurarNome = input("\nEscreva a Idade a pesquisar: ")
                    if not procurarNome.isdigit():
                        print("\nTem de usar números para pesquisar por Idade.")
                        flag = True
                        continue
                    for cliente in listagem:
                        if cliente["idade"] == int(procurarNome):
                            print(cliente)
                            encontrou = True
                            flag = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                        flag = True
                case "6":
                    print("\nListar TODOS os clientes")
                    for cliente in listagem:
                        print("\n", cliente)
                    flag = False

                case "7":
                    print("\nSair da pesquisa")
                    flag = False

                case _:
                    print("\nOpção inválida, escolha de novo.")


# definition - uma função para pesquisar um cliente na eliminação e na atualização.
def pesquisar_cliente_opcao():
    while True:
        escolha = ""
        print("\n------ Menu PESQUISA ------")
        print("1 - Pesquisar por Nome")
        print("2 - Pesquisar por ID")
        print("3 - Pesquisar Data Consulta")
        print("4 - Pesquisar por Cidade")
        print("5 - Pesquisar por Idade")
        print("6 - Voltar ao menu principal")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
            print("\nOpção errada, escolha de novo")
        else:
            match escolha:
                case "1":
                    encontrou = False
                    print("\nPesquisar por Nome")
                    procurarNome = input("\nEscreva o Nome a pesquisar: ")
                    if procurarNome.isdigit():
                        print("\nTem de usar texto para pesquisar por nome.")
                        continue
                    for cliente in listagem:
                        if cliente["nome"].lower() == procurarNome.lower():
                            print("\nCliente encontrado:")
                            print(cliente)
                            return
                    if not encontrou:
                        print("\nEsses dados não existem.")
                case "2":
                    encontrou = False
                    print("\nPesquisar por ID")
                    procurarNome = input("\nEscreva o ID a pesquisar: ")
                    if not procurarNome.isdigit():
                        print("\nTem de usar números para pesquisar por ID.")
                        continue
                    for cliente in listagem:
                        if cliente["id"] == int(procurarNome):
                            print("\nCliente encontrado:")
                            print(cliente)
                            return
                    if not encontrou:
                        print("\nEsses dados não existem.")

                case "3":
                    print("\nPesquisar por Data da Consulta")
                    procurarNome = input(
                        "\nEscreva a Data da Consulta a pesquisar (AAAA-MM-DD): "
                    )
                    try:
                        # Tenta converter o texto numa data real para não acontecer 2024-02-45.
                        datetime.strptime(procurarNome, "%Y-%m-%d")

                        # Se passou, a data é válida.
                        for cliente in listagem:
                            if cliente["data_consulta"] == procurarNome:
                                print("\n", cliente)
                                return
                    except ValueError:
                        print(
                            "\nErro: Data não encontrada ou formato errado. Use AAAA-MM-DD (ex: 2024-05-18)."
                        )
                case "4":
                    encontrou = False
                    print("\nPesquisar por Cidade")
                    procurarNome = input("\nEscreva o Nome da Cidade a pesquisar: ")
                    if procurarNome.isdigit():
                        print("\nTem de usar letras para pesquisar por nome da cidade.")
                        continue
                    for cliente in listagem:
                        if cliente["cidade"].lower() == procurarNome.lower():
                            print("\nCliente encontrado:")
                            print(cliente)
                            encontrou = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                case "5":
                    encontrou = False
                    print("\nPesquisar por Idade")
                    procurarNome = input("\nEscreva a Idade a pesquisar: ")
                    if not procurarNome.isdigit():
                        print("\nTem de usar números para pesquisar por Idade.")
                        continue
                    for cliente in listagem:
                        if cliente["idade"] == int(procurarNome):
                            print("\nCliente encontrado:")
                            print(cliente)
                            encontrou = True
                    if not encontrou:
                        print("\nEsses dados não existem.")

                case "6":
                    # print("\nSair da pesquisa")
                    break
                case _:
                    print("\nOpção inválida, escolha de novo.")


# definition - uma função para atualizar um cliente, onde é escolhido qual campo a atualizar.
def atualizar_clientes():
    print("pesquise o cliente que deseja atualizar")
    pesquisar_cliente_opcao()
    id_atualizar = input(
        "\nDigite o numero do id para o confirmar ou carrege no 'n' para sair: "
    )
    if id_atualizar.lower() == "n":
        # print("\nA voltar ao menu principal...")
        return
    for cliente in listagem:
        if cliente["id"] == int(id_atualizar):
            while True:
                escolha = ""
                print("\n------ Menu ATUALIZAR ------")
                print("1 - Alterar Nome")
                print("2 - Alterar Idade")
                print("3 - Alterar Cidade")
                print("4 - Alterar área profissional")
                print("5 - Alterar assunto")
                print("6 - Alterar genero")
                print("7 - Alterar valor consulta")
                print("8 - alterar tipo consulta")
                print("9 - Alterar data consulta")
                print("10 - Alterar casado/casada")
                print("11 - Alterar filhos")
                print("12 - Alterar notas")
                print("13 - Voltar ao menu principal")
                escolha = input("\nEscolha uma opção: ")
                if escolha < "1" or escolha > "13":
                    print("\nOpção errada, escolha de novo")
                else:
                    match escolha:
                        case "1":
                            while True:
                                cliente["nome"] = input("Nome: ")
                                if cliente["nome"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                else:
                                    break
                        case "2":
                            while True:
                                cliente_variavel = input("Idade: ")
                                if cliente_variavel.isdigit():
                                    cliente["idade"] = int(cliente_variavel)
                                    break
                                else:
                                    print("\nTem de usar apenas numeros para a idade.")
                        case "3":
                            while True:
                                cliente["cidade"] = input("Cidade: ")
                                if cliente["cidade"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                else:
                                    break
                        case "4":
                            while True:
                                cliente["area_profissional"] = input(
                                    "Área Profissional: "
                                )
                                if cliente["area_profissional"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                else:
                                    break
                        case "5":
                            while True:
                                cliente["assunto"] = input("Assunto: ")
                                if cliente["assunto"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                else:
                                    break
                        case "6":
                            while True:
                                cliente["genero"] = (input("Gênero (m/f): ")).lower()
                                if cliente["genero"].isdigit():
                                    print(
                                        "\nTem de usar 'm' para masculino ou 'f' para feminino."
                                    )
                                elif cliente["genero"].lower() not in ["m", "f"]:
                                    print(
                                        "\nTem de usar 'm' para masculino ou 'f' para feminino."
                                    )
                                else:
                                    break
                        case "7":
                            while True:
                                cliente_variavel = input("Valor da Consulta: ")
                                if not cliente_variavel.replace(".", "").isdigit():
                                    print(
                                        "\nTem de usar números para o valor da consulta."
                                    )
                                else:
                                    cliente["valor_consulta"] = float(cliente_variavel)
                                    break
                        case "8":
                            while True:
                                cliente["tipo_consulta"] = input(
                                    "Tipo de Consulta (presencial/online): "
                                )
                                if cliente["tipo_consulta"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                elif cliente["tipo_consulta"].lower() not in [
                                    "presencial",
                                    "online",
                                ]:
                                    print("\nTem de usar 'presencial' ou 'online'.")
                                else:
                                    break
                        case "9":
                            while True:
                                cliente["data_consulta"] = input(
                                    "Data da Consulta (YYYY-MM-DD): "
                                )
                                if not cliente["data_consulta"].isdigit():
                                    print(
                                        "\nTem de usar o formato YYYY-MM-DD para a data."
                                    )
                                    print("--- Exemplo: 2024-05-15 -----")
                                else:
                                    break
                        case "10":
                            while True:
                                cliente["casado"] = input("Casado (s/n): ").lower()
                                if cliente["casado"].isdigit():
                                    print("\nTem de usar 's' para sim ou 'n' para não.")
                                else:
                                    if cliente["casado"] == "s":
                                        cliente["casado"] = True
                                        break
                                    elif cliente["casado"] == "n":
                                        cliente["casado"] = False
                                        break
                                    else:
                                        print(
                                            "\nTem de usar 's' para sim ou 'n' para não."
                                        )
                        case "11":
                            while True:
                                cliente_variavel = input("Filhos (s/n): ").lower()
                                if cliente_variavel.isdigit():
                                    print("\nTem de usar 's' para sim ou 'n' para não.")
                                else:
                                    cliente["filhos"] = cliente_variavel == "s"
                                    break
                        case "12":
                            while True:
                                cliente["notas"] = input("Notas: ")
                                if cliente["notas"].isdigit():
                                    print("\nTem de usar apenas texto.")
                                else:
                                    break
                        case "13":
                            return
                        case _:
                            print("\nOpção inválida, escolha de novo.")

    print("\nCliente atualizado com sucesso!")


# definition - uma função para criar um cliente.
def criar_clientes():
    novo_cliente = {}
    novo_cliente["id"] = gerar_proximo_id(listagem)
    while True:
        novos_dados = input("Nome: ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        else:
            novo_cliente["nome"] = novos_dados
            break
    while True:
        novos_dados = input("Idade: ")
        if not novos_dados.isdigit():
            print("\nTem de usar números para colocar a idade.")
        else:
            novo_cliente["idade"] = int(novos_dados)
            break
    while True:
        novos_dados = input("Cidade: ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        else:
            novo_cliente["cidade"] = novos_dados
            break
    while True:
        novos_dados = input("Área Profissional: ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        else:
            novo_cliente["area_profissional"] = novos_dados
            break
    while True:
        novos_dados = input("Assunto consulta: ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        else:
            novo_cliente["assunto"] = novos_dados
            break
    while True:
        novos_dados = input("Gênero (m/f): ").lower()
        if novos_dados.isdigit():
            print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
        elif novos_dados.lower() not in ["m", "f"]:
            print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
        else:
            novo_cliente["genero"] = novos_dados
            break
    while True:
        novos_dados = input("Valor da Consulta: ")
        if not novos_dados.replace(".", "").isdigit():
            print("\nTem de usar números.")
        else:
            novo_cliente["valor_consulta"] = float(novos_dados)
            break
    while True:
        novos_dados = input("Tipo de Consulta (presencial/online): ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        elif novos_dados.lower() not in ["presencial", "online"]:
            print("\nTem de usar 'presencial' ou 'online'.")
        else:
            novo_cliente["tipo_consulta"] = novos_dados
            break
    while True:
        data_input = input("Data (AAAA-MM-DD): ")
        try:
            # Tenta converter o texto numa data real para não acontecer 2024-02-45.
            datetime.strptime(data_input, "%Y-%m-%d")

            # Se passou, a data é válida!e guardamos como string para o JSON aceitar
            novo_cliente["data_consulta"] = data_input
            break
        except ValueError:
            print(
                "\nErro: Data inválida ou formato errado. Use AAAA-MM-DD (ex: 2024-05-18)."
            )
    while True:
        novos_dados = input("Casado (s/n): ").lower()
        if novos_dados.isdigit():
            print("\nTem de usar 's' para sim ou 'n' para não.")
        else:
            if novos_dados == "s":
                novo_cliente["casado"] = True
                break
            elif novos_dados == "n":
                novo_cliente["casado"] = False
                break
            else:
                print("\nTem de usar 's' para sim ou 'n' para não.")
    while True:
        novos_dados = input("Filhos (s/n): ").lower()
        if novos_dados.isdigit():
            print("\nTem de usar 's' para sim ou 'n' para não.")
        else:
            novo_cliente["filhos"] = novos_dados == "s"
            break
    while True:
        novos_dados = input("Notas: ")
        if novos_dados.isdigit():
            print("\nTem de usar apenas texto.")
        else:
            novo_cliente["notas"] = novos_dados
            break
    listagem.append(novo_cliente)
    print("\nCliente criado com sucesso!")


# definition - uma função para apagar um cliente.
def apagar_clientes():
    print("pesquise o cliente que deseja apagar")
    pesquisar_cliente_opcao()
    id_apagar = input(
        "\nDigite o numero do id para o confirmar ou carrege no 'n' para sair: "
    )
    if id_apagar.lower() == "n":
        # print("\nA voltar ao menu principal...")
        return
    for cliente in listagem:
        if cliente["id"] == int(id_apagar):
            listagem.remove(cliente)
            print("\nCliente apagado com sucesso!")
            return
    print("\nCliente não encontrado.")


def ordenar_clientes():
    while True:
        print("\n------ Menu ORDENAR ------")
        print("Ordenar por Nome (Bubble Sort)")
        print("1 - descendente")
        print("2 - ascendente")
        print("Ordenar por ID (Selection Sort)")
        print("3 - descendente")
        print("4 - ascendente")
        print("Ordenar por Data Consulta (Bubble Sort)")
        print("5 - descendente")
        print("6 - ascendente")
        print("7 - Voltar ao menu principal")
        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "1":
                print("\nA ordenar por Nome (Descendente)...")
                n = len(listagem)
                # Ciclo para percorrer toda a lista
                for i in range(n):
                    # O último i elementos já estão no lugar
                    for j in range(0, n - i - 1):
                        # Comparamos o nome atual com o próximo
                        # Para descendente (Z-A), se o atual for MENOR que o próximo, trocamos
                        if (
                            listagem[j]["nome"].lower()
                            < listagem[j + 1]["nome"].lower()
                        ):
                            # Troca de posição (Mecânica clássica de Python)
                            listagem[j], listagem[j + 1] = listagem[j + 1], listagem[j]
                for cliente in listagem:
                    print("\n", cliente)

            case "2":
                print("\nA ordenar por Nome (Ascendente)...")
                n = len(listagem)
                for i in range(n):
                    for j in range(n - 1):
                        if (
                            listagem[j]["nome"].lower()
                            > listagem[j + 1]["nome"].lower()
                        ):
                            listagem[j], listagem[j + 1] = listagem[j + 1], listagem[j]
                for cliente in listagem:
                    print("\n", cliente)

            case "3":
                print("\nA ordenar por ID (Descendente)...")
                n = len(listagem)
                for i in range(n):
                    # Consideramos que o maior está na posição atual para haver uma referencia, e depois procuramos se existe algum maior que ele no resto da lista
                    indice = i
                    for j in range(i + 1, n):
                        # Para descendente, procuramos se existe algum ID MAIOR que o atual
                        if listagem[j]["id"] > listagem[indice]["id"]:
                            indice = j
                    # Troca o atual pelo maior encontrado
                    listagem[i], listagem[indice] = (
                        listagem[indice],
                        listagem[i],
                    )
                for cliente in listagem:
                    print("\n", cliente)
            case "4":
                print("\nA ordenar por ID (Ascendente)...")
                n = len(listagem)
                for i in range(n):
                    for j in range(n - 1):
                        if listagem[j]["id"] > listagem[j + 1]["id"]:
                            listagem[j], listagem[j + 1] = listagem[j + 1], listagem[j]
                for cliente in listagem:
                    print("\n", cliente)
            case "5":
                print("\nA ordenar por Data Consulta (Descendente)...")
                n = len(listagem)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if (
                            listagem[j]["data_consulta"]
                            < listagem[j + 1]["data_consulta"]
                        ):
                            listagem[j], listagem[j + 1] = listagem[j + 1], listagem[j]
                for cliente in listagem:
                    print("\n", cliente)
            case "6":
                print("\nA ordenar por Data Consulta (Ascendente)...")
                n = len(listagem)
                for i in range(n):
                    for j in range(n - 1):
                        if (
                            listagem[j]["data_consulta"]
                            > listagem[j + 1]["data_consulta"]
                        ):
                            listagem[j], listagem[j + 1] = listagem[j + 1], listagem[j]
                for cliente in listagem:
                    print("\n", cliente)
            case "7":
                # print("\nSair da ordenação...")
                break
            case _:
                print("\nOpção inválida, escolha de novo.")


def estatisticas():
    while True:
        print("\n------ Menu ESTATÍSTICAS ------")
        print("1 - Número total de consultas")
        print("2 - Idade média dos clientes")
        print("3 - Cidades dos clientes")
        print("4 - valor médio das consultas")
        print("5 - Valor mais alto de consulta")
        print("6 - Valor mais baixo de consulta")
        print("7 - Consulta mais comum (presencial ou online)")
        print("9 - Filtro para valores")
        print("10 - Filtro para idades")
        print("11 - Filtro para datas")
        print("12 - Voltar ao menu principal")
        escolha = input("\nEscolha uma opção: ")
        match escolha:
            case "1":
                print("\nNúmero total de consultas:", len(listagem))
            case "2":
                if len(listagem) > 0:
                    for cliente in listagem:
                        idade_total = sum(cliente["idade"])
                    idade_media = idade_total / len(listagem)
                    print("\nIdade média dos clientes:", idade_media)
                else:
                    print("\nNenhum cliente registrado para calcular a idade média.")
            case "3":
                compara_cidades = {}
                for cliente in listagem:
                    cidade = cliente["cidade"]
                    if cidade in compara_cidades:
                        compara_cidades[cidade] += 1
                    else:
                        compara_cidades[cidade] = 1
                print("\nCidades com mais consultas:")
                for cidade in compara_cidades:
                    print(f"{cidade}: {compara_cidades[cidade]} vezes")
            case "4":
                pass

        # else:
        #     print("Nenhum cliente registrado para calcular estatísticas.")


# main - "programa principal" onde o menu é mostrado e as escolhas do utilizador são processadas.
introducao()
escolhas = menu2()
while escolhas != "7":
    if escolhas == "1":
        print("Pesquisar cliente")
        pesquisar_clientes()
        escolhas = menu2()
    elif escolhas == "2":
        print("Ordenação dados cliente")
        ordenar_clientes()
        escolhas = menu2()
    elif escolhas == "3":
        print("Atualizar cliente")
        atualizar_clientes()
        escolhas = menu2()
    elif escolhas == "4":
        print("Criar cliente")
        criar_clientes()
        escolhas = menu2()
    elif escolhas == "5":
        print("Apagar cliente")
        apagar_clientes()
        escolhas = menu2()
    elif escolhas == "6":
        print("Estatísticas")
        estatisticas()
        escolhas = menu2()
    elif escolhas == "7":
        print("A sair da app...")
        break
    else:
        print("Opção inválida, escolha de novo.")

# Ao sair do programa, Todos os dados e alterações no momento são salvos no ficheiro JSON.
with open(filename, "w", encoding="utf-8") as manipfile:
    json.dump(listagem, manipfile, ensure_ascii=True, indent=4)
