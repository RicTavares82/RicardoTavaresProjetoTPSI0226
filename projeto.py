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

import os as fsos
import json

filename = "./Dados/Projeto_consultas.json"
listagem = []  # lista com dicionários, onde cada elemento representa um cliente

# Verificar se o ficheiro existe, caso exista, carregar os dados para a variável listagem e caso contrário, criar uma lista vazio.
if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        listagem = json.load(manipfile)

    print(listagem)
    print("Dados carregados com sucesso!")
else:
    print("O ficheiro ainda não existe. Criando um dicionário vazio...")
    listagem = []


# definition - uma função para o "menu de introdução".
def menu():
    print("Seja bem-vindo/a ao sistema de cadastro de clientes!")
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
        print("2 - Atualizar cliente")
        print("3 - Criar cliente")
        print("4 - Apagar cliente")
        print("5 - Estatísticas")
        print("6 - Sair da APP")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
            print("\nOpção errada, escolha de novo")
            flag = True
    return escolha


# definition - uma função para gerar o próximo ID, que é o ID do último cliente + 1, ou 1 se a lista estiver vazia.
def gerar_proximo_id(lista_clientes):
    if not lista_clientes:  # uso a negação para verificar se a lista está vazia, o que é mais eficiente do que verificar o comprimento da lista
        return 1  # Se a lista estiver vazia, o primeiro ID é 1

    # Pega no último dicionário da lista e procura dentro do campo "id" o valor e soma 1
    ultimo_id = lista_clientes[-1]["id"]
    return ultimo_id + 1


# definition - uma função para pesquisar um cliente.
# def pesquisar_cliente():
#     flag = True
#     while flag:
#         flag = False
#         procurarNome = input("\nEscreva o Nome ou ID a pesquisar: ").strip()
#         encontrou = False
#         for cliente in listagem:
#             if cliente["nome"].lower() == procurarNome.lower():
#                 print(cliente)
#                 encontrou = True
#                 flag = True
#         if not encontrou:
#             if procurarNome.isdigit():
#                 procurarNum = int(procurarNome)
#                 for cliente in listagem:
#                     if cliente["id"] == procurarNum:
#                         print(cliente)
#                         encontrou = True
#                         flag = True
#         if not encontrou:
#             print("\nEsses dados não existem.")
#             flag = True
#         else:
#             novaPesquisa = input("\nDeseja pesquisar outro cliente? (s/n): ")
#             if novaPesquisa.lower() != "s":
#                 # flag = False
#                 break


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
        print("6 - Sair da pesquisa")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
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
                    # encontrou = True
                    # print("\nPesquisar por Data da Consulta")
                    # procurarNome = input("\nEscreva a Data da Consulta a pesquisar: ")
                    # if not procurarNome.isdigit():
                    #     print("\nTem de usar números para pesquisar por Data da Consulta.")
                    #     flag = True
                    #     continue
                    # for cliente in listagem:
                    #     if cliente["id"] == int(procurarNome):
                    #         print(cliente)
                    #         encontrou = True
                    #         flag = True
                    # if not encontrou:
                    #     print("\nEsses dados não existem.")
                    #     flag = True
                    pass

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
                    print("\nSair da pesquisa")
                    flag = False

                case _:
                    print("\nOpção inválida, escolha de novo.")


# definition - uma função para pesquisar um cliente na eliminação e na atualização.
def pesquisar_cliente_opcao():
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
        print("6 - Voltar ao menu principal")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
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
                            flag = False
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
                    # encontrou = True
                    # print("\nPesquisar por Data da Consulta")
                    # procurarNome = input("\nEscreva a Data da Consulta a pesquisar: ")
                    # if not procurarNome.isdigit():
                    #     print("\nTem de usar números para pesquisar por Data da Consulta.")
                    #     flag = True
                    #     continue
                    # for cliente in listagem:
                    #     if cliente["id"] == int(procurarNome):
                    #         print(cliente)
                    #         encontrou = True
                    #         flag = True
                    # if not encontrou:
                    #     print("\nEsses dados não existem.")
                    #     flag = True
                    pass

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
                    # print("\nSair da pesquisa")
                    flag = False

                case _:
                    print("\nOpção inválida, escolha de novo.")


def atualizar_cliente():
    print("pesquise o cliente que deseja atualizar")
    pesquisar_cliente_opcao()
    id_atualizar = input("Confirme o numero do ID ou carrege no 'n' para sair: ")
    if id_atualizar.lower() == "n":
        # print("\nA voltar ao menu principal...")
        return
    for cliente in listagem:
        if cliente["id"] == int(id_atualizar):
            while True:
                cliente["nome"] = input("Nome: ")
                if cliente["nome"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente_variavel = input("Idade: ")
                if cliente_variavel.isdigit():
                    cliente["idade"] = int(cliente_variavel)
                    break
                else:
                    print("\nTem de usar apenas numeros para a idade.")

            while True:
                cliente["cidade"] = input("Cidade: ")
                if cliente["cidade"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["area_profissional"] = input("Área Profissional: ")
                if cliente["area_profissional"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["assunto"] = input("Assunto: ")
                if cliente["assunto"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["genero"] = (input("Gênero (m/f): ")).lower()
                if cliente["genero"].isdigit():
                    print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
                elif cliente["genero"].lower() not in ["m", "f"]:
                    print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
                else:
                    break

            while True:
                cliente["valor_consulta"] = input("Valor da Consulta: ")
                if not cliente["valor_consulta"].isdigit():
                    print("\nTem de usar apenas números para o valor da consulta.")
                else:
                    break

            # cliente["valor_consulta"] = float(input("Valor da Consulta: "))

            while True:
                cliente["tipo_consulta"] = input(
                    "Tipo de Consulta (presencial/online): "
                )
                if cliente["tipo_consulta"].isdigit():
                    print("\nTem de usar apenas texto.")
                elif cliente["tipo_consulta"].lower() not in ["presencial", "online"]:
                    print(
                        "\nTem de usar 'presencial' ou 'online' para o tipo de consulta."
                    )
                else:
                    break

            while True:
                cliente["data_consulta"] = input("Data da Consulta (YYYY-MM-DD): ")
                if not cliente["data_consulta"].isdigit():
                    print("\nTem de usar o formato YYYY-MM-DD para a data da consulta.")
                    print("--- Exemplo: 2024-05-15 -----")
                else:
                    break

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
                        print("\nTem de usar 's' para sim ou 'n' para não.")

            # # uma forma mais eficiente e limpa de validar a input ao transformar logo em true ou false.
            # while True:
            #     cliente["casado"] = input("Casado (s/n): ").lower() == "s"
            #     if not isinstance(cliente["casado"], bool):
            #         print("\nTem de usar 's' para sim ou 'n' para não.")
            #     else:
            #         break

            while True:
                cliente["filhos"] = input("Filhos (s/n): ").lower() == "s"
                if not isinstance(cliente["filhos"], bool):
                    print("\nTem de usar 's' para sim ou 'n' para não.")
                else:
                    break

            break

    print("\nCliente atualizado com sucesso!")


def atualizar_clientes():
    print("pesquise o cliente que deseja atualizar")
    pesquisar_cliente_opcao()
    id_atualizar = input("Confirme o numero do ID ou carrege no 'n' para sair: ")
    if id_atualizar.lower() == "n":
        # print("\nA voltar ao menu principal...")
        return
    for cliente in listagem:
        while True:
            escolha = ""
            print("1 - Alterar Nome")
            print("2 - Alterar Idade")
            print("3 - Alterar Cidade")
            print("4 - Alterar Idade")
            print("5 - Alterar assunto")
            print("6 - Alterar genero")
            print("7 - Alterar valor consulta")
            print("8 - alterar tipo consulta")
            print("9 - Alterar data consulta")
            print("10 - Alterar casado/casada")
            print("11 - Alterar filhos")
            print("12 - Alterar notas")
            escolha = input("\nEscolha uma opção: ")
            if escolha < "1" or escolha > "12" or len(escolha) != 1:
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
                                flag = False
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
                        # encontrou = True
                        # print("\nPesquisar por Data da Consulta")
                        # procurarNome = input("\nEscreva a Data da Consulta a pesquisar: ")
                        # if not procurarNome.isdigit():
                        #     print("\nTem de usar números para pesquisar por Data da Consulta.")
                        #     flag = True
                        #     continue
                        # for cliente in listagem:
                        #     if cliente["id"] == int(procurarNome):
                        #         print(cliente)
                        #         encontrou = True
                        #         flag = True
                        # if not encontrou:
                        #     print("\nEsses dados não existem.")
                        #     flag = True
                        pass

                    case "4":
                        encontrou = False
                        print("\nPesquisar por Cidade")
                        procurarNome = input("\nEscreva o Nome da Cidade a pesquisar: ")
                        if procurarNome.isdigit():
                            print(
                                "\nTem de usar letras para pesquisar por nome da cidade."
                            )
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
                        # print("\nSair da pesquisa")
                        flag = False

                    case _:
                        print("\nOpção inválida, escolha de novo.")

        if cliente["id"] == int(id_atualizar):
            while True:
                cliente["nome"] = input("Nome: ")
                if cliente["nome"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente_variavel = input("Idade: ")
                if cliente_variavel.isdigit():
                    cliente["idade"] = int(cliente_variavel)
                    break
                else:
                    print("\nTem de usar apenas numeros para a idade.")

            while True:
                cliente["cidade"] = input("Cidade: ")
                if cliente["cidade"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["area_profissional"] = input("Área Profissional: ")
                if cliente["area_profissional"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["assunto"] = input("Assunto: ")
                if cliente["assunto"].isdigit():
                    print("\nTem de usar apenas texto.")
                else:
                    break

            while True:
                cliente["genero"] = (input("Gênero (m/f): ")).lower()
                if cliente["genero"].isdigit():
                    print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
                elif cliente["genero"].lower() not in ["m", "f"]:
                    print("\nTem de usar 'm' para masculino ou 'f' para feminino.")
                else:
                    break

            while True:
                cliente["valor_consulta"] = input("Valor da Consulta: ")
                if not cliente["valor_consulta"].isdigit():
                    print("\nTem de usar apenas números para o valor da consulta.")
                else:
                    break

            # cliente["valor_consulta"] = float(input("Valor da Consulta: "))

            while True:
                cliente["tipo_consulta"] = input(
                    "Tipo de Consulta (presencial/online): "
                )
                if cliente["tipo_consulta"].isdigit():
                    print("\nTem de usar apenas texto.")
                elif cliente["tipo_consulta"].lower() not in ["presencial", "online"]:
                    print(
                        "\nTem de usar 'presencial' ou 'online' para o tipo de consulta."
                    )
                else:
                    break

            while True:
                cliente["data_consulta"] = input("Data da Consulta (YYYY-MM-DD): ")
                if not cliente["data_consulta"].isdigit():
                    print("\nTem de usar o formato YYYY-MM-DD para a data da consulta.")
                    print("--- Exemplo: 2024-05-15 -----")
                else:
                    break

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
                        print("\nTem de usar 's' para sim ou 'n' para não.")

            # # uma forma mais eficiente e limpa de validar a input ao transformar logo em true ou false.
            # while True:
            #     cliente["casado"] = input("Casado (s/n): ").lower() == "s"
            #     if not isinstance(cliente["casado"], bool):
            #         print("\nTem de usar 's' para sim ou 'n' para não.")
            #     else:
            #         break

            while True:
                cliente["filhos"] = input("Filhos (s/n): ").lower() == "s"
                if not isinstance(cliente["filhos"], bool):
                    print("\nTem de usar 's' para sim ou 'n' para não.")
                else:
                    break

            break

    print("\nCliente atualizado com sucesso!")

    # {'id': 6, 'nome': 'Bruno Costa', 'idade': 41, 'cidade': 'Setúbal', 'area_profissional': 'Logística', 'assunto': 'Conflitos Familiares', 'genero': 'm', 'valor_consulta': 55.0, 'tipo_consulta': 'presencial', 'data_consulta': '2024-05-25', 'casado': True, 'filhos': True}


# main - o programa principal, onde o menu é mostrado e as escolhas do usuário são processadas.
menu()
escolhas = menu2()

while escolhas != "6":
    if escolhas == "1":
        print("Pesquisar cliente")
        pesquisar_clientes()
        escolhas = menu2()
    elif escolhas == "2":
        print("Atualizar cliente")
        atualizar_cliente()
        escolhas = menu2()
    elif escolhas == "3":
        print("Criar cliente")
        escolhas = menu2()
    elif escolhas == "4":
        print("Apagar cliente")
        escolhas = menu2()
    elif escolhas == "5":
        print("Estatísticas")
        escolhas = menu2()
    elif escolhas == "6":
        print("Sair")
        break
    else:
        print("Opção inválida, escolha de novo.")

# Ao sair do programa, os dados são salvos no ficheiro JSON.
with open(filename, "w", encoding="utf-8") as manipfile:
    json.dump(listagem, manipfile, ensure_ascii=True, indent=4)
