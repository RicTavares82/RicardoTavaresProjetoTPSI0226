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
        print("\n------ Menu ------")
        print("1 - Pesquisar cliente")
        print("2 - Atualizar cliente")
        print("3 - Criar cliente")
        print("4 - Apagar cliente")
        print("5 - Estatística")
        print("6 - Sair")
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
def pesquisar_cliente():
    flag = True
    while flag:
        flag = False
        procurarNome = input("\nEscreva o Nome ou ID a pesquisar: ").strip()
        encontrou = False
        for cliente in listagem:
            if cliente["nome"].lower() == procurarNome.lower():
                print(cliente)
                encontrou = True
                flag = True
        if not encontrou:
            if procurarNome.isdigit():
                procurarNum = int(procurarNome)
                for cliente in listagem:
                    if cliente["id"] == procurarNum:
                        print(cliente)
                        encontrou = True
                        flag = True
        if not encontrou:
            print("\nEsses dados não existem.")
            flag = True
        else:
            novaPesquisa = input("\nDeseja pesquisar outro cliente? (s/n): ")
            if novaPesquisa.lower() != "s":
                # flag = False
                break


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
        print("6 - Sair")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
            print("\nOpção errada, escolha de novo")
            flag = True
        else:
            match escolha:
                case "1":
                    encontrou = True
                    print("\nPesquisar por Nome")
                    procurarNome = input("\nEscreva o Nome a pesquisar: ")
                    if procurarNome.isdigit():
                        print("\nTem de usar letras para pesquisar por nome.")
                        flag = True
                        # continue
                    for cliente in listagem:
                        if cliente["nome"].lower() == procurarNome.lower():
                            print(cliente)
                            encontrou = True
                            flag = True
                    if not encontrou:
                        print("\nEsses dados não existem.")
                        flag = True
                case "2":
                    encontrou = True
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
                    break
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
                    break
                case "4":
                    encontrou = True
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
                    break
                case "5":
                    encontrou = True
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
                    break
                case "6":
                    print("\nSair")
                    flag = False
                    break
                case _:
                    print("\nOpção inválida, escolha de novo.")


def atualizar_cliente():
    print("pesquise o cliente que deseja atualizar")
    pesquisar_clientes()
    id_atualizar = input(print("Indique o ID a atualizar: "))
    for cliente in listagem:
        if cliente["id"] == int(id_atualizar):
            cliente["nome"] = input("Nome: ")
            cliente["idade"] = int(input("Idade: "))
            cliente["cidade"] = input("Cidade: ")
            cliente["area_profissional"] = input("Área Profissional: ")
            cliente["assunto"] = input("Assunto: ")
            cliente["genero"] = input("Gênero (m/f): ")
            cliente["valor_consulta"] = float(input("Valor da Consulta: "))
            cliente["tipo_consulta"] = input("Tipo de Consulta (presencial/online): ")
            listagem[cliente]["data_consulta"] = input(
                "Data da Consulta (YYYY-MM-DD): "
            )
            listagem[cliente]["casado"] = input("Casado (s/n): ").lower() == "s"
            listagem[cliente]["filhos"] = input("Filhos (s/n): ").lower() == "s"

    print("Cliente atualizado com sucesso!")

    # {'id': 6, 'nome': 'Bruno Costa', 'idade': 41, 'cidade': 'Setúbal', 'area_profissional': 'Logística', 'assunto': 'Conflitos Familiares', 'genero': 'm', 'valor_consulta': 55.0, 'tipo_consulta': 'presencial', 'data_consulta': '2024-05-25', 'casado': True, 'filhos': True}

    pass


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
        print("Estatística")
        escolhas = menu2()
    elif escolhas == "6":
        print("Sair")
        break
    else:
        print("Opção inválida, escolha de novo.")

# Ao sair do programa, os dados são salvos no ficheiro JSON.
with open(filename, "w", encoding="utf-8") as manipfile:
    json.dump(listagem, manipfile, ensure_ascii=True, indent=4)
