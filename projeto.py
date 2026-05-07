# nome primeiro+ultimo - string
# idade - int
# cidade - string
# area profissional - string
# tema/assunto - string
# genero - m/f - char
# valor consulta - double
# local consulta - presencial/online - string
# data consulta - data
# casado/casada - boolean
# filhos - boolean

import os as fsos
import json

filename = "./Dados/data1.txt"
dicionario = {}

if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        dicionario = json.load(manipfile)

    print("Dados carregados com sucesso!")
    print(dicionario)
else:
    print("O ficheiro ainda não existe. Criando um dicionário vazio...")
    dicionario = {}


def menu():
    print("Seja bem-vindo ao sistema de cadastro de clientes!")
    print(
        "Esta app regista os clientes, onde é possível criar, ler, atualizar e apagar clientes."
    )
    print("App criada por: Ricardo Tavares. 2026")


def menu2():
    flag = True
    escolha = 0
    while flag:
        flag = False
        print("\n------ Menu ------")
        print("1 - Pesquisar cliente")
        print("2 - Estatística")
        print("3 - Criar cliente")
        print("4 - Apagar cliente")
        print("5 - Atualizar cliente")
        print("6 - Sair")
        escolha = input("\nEscolha uma opção: ")
        if escolha < "1" or escolha > "6" or len(escolha) != 1:
            print("\nopção errada, escolha de novo")
            flag = True
    return escolha


menu()
escolhas = menu2()
print(escolhas)

while escolhas != "6":
    if escolhas == "1":
        print("Pesquisar cliente")
    elif escolhas == "2":
        print("Estatística")
    elif escolhas == "3":
        print("Criar cliente")
    elif escolhas == "4":
        print("Apagar cliente")
    elif escolhas == "5":
        print("Atualizar cliente")
    else:
        print("Opção inválida, escolha de novo.")
    escolhas = menu2()

# with open(filename, "w", encoding="utf-8") as manipfile:
#     json.dump(dicionario, manipfile, ensure_ascii=True, indent=4)
