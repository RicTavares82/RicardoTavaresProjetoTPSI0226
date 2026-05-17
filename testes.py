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


# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

# for key in dictionary:
#     print(key, "->", dictionary)

listagem = [
    {
        "id": 1,
        "nome": "Ana Martins",
        "idade": 34,
        "cidade": "Lisboa",
        "area_profissional": "Marketing Digital",
        "assunto": "Ansiedade Profissional",
        "genero": "f",
        "valor_consulta": 65.5,
        "tipo_consulta": "online",
        "data_consulta": "2024-05-15",
        "casado": True,
        "filhos": True,
    },
    {
        "id": 2,
        "nome": "Ricardo Pereira",
        "idade": 28,
        "cidade": "Porto",
        "area_profissional": "Engenharia de Software",
        "assunto": "Gest\u00e3o de Tempo",
        "genero": "m",
        "valor_consulta": 50.0,
        "tipo_consulta": "presencial",
        "data_consulta": "2024-05-16",
        "casado": False,
        "filhos": False,
    },
    {
        "id": 3,
        "nome": "Catarina Santos",
        "idade": 45,
        "cidade": "Coimbra",
        "area_profissional": "Professora",
        "assunto": "Burnout",
        "genero": "f",
        "valor_consulta": 60.0,
        "tipo_consulta": "presencial",
        "data_consulta": "2024-05-18",
        "casado": True,
        "filhos": True,
    },
    {
        "id": 4,
        "nome": "Jo\u00e3o Silva",
        "idade": 19,
        "cidade": "Braga",
        "area_profissional": "Estudante",
        "assunto": "Orienta\u00e7\u00e3o Vocacional",
        "genero": "m",
        "valor_consulta": 40.0,
        "tipo_consulta": "online",
        "data_consulta": "2024-05-20",
        "casado": False,
        "filhos": False,
    },
    {
        "id": 5,
        "nome": "Marta Oliveira",
        "idade": 52,
        "cidade": "Faro",
        "area_profissional": "Gest\u00e3o Hoteleira",
        "assunto": "Transi\u00e7\u00e3o de Carreira",
        "genero": "f",
        "valor_consulta": 75.0,
        "tipo_consulta": "online",
        "data_consulta": "2024-05-22",
        "casado": True,
        "filhos": False,
    },
    {
        "id": 6,
        "nome": "Bruno Costa",
        "idade": 41,
        "cidade": "Set\u00fabal",
        "area_profissional": "Log\u00edstica",
        "assunto": "Conflitos Familiares",
        "genero": "m",
        "valor_consulta": 55.0,
        "tipo_consulta": "presencial",
        "data_consulta": "2024-05-25",
        "casado": True,
        "filhos": True,
    },
    {
        "id": 7,
        "nome": "Helena Vaz",
        "idade": 37,
        "cidade": "Lisboa",
        "area_profissional": "Arquiteta",
        "assunto": "Autoestima",
        "genero": "f",
        "valor_consulta": 70.0,
        "tipo_consulta": "online",
        "data_consulta": "2024-05-26",
        "casado": False,
        "filhos": True,
    },
    {
        "id": 8,
        "nome": "Tiago Ferreira",
        "idade": 31,
        "cidade": "Leiria",
        "area_profissional": "Enfermeiro",
        "assunto": "Stress P\u00f3s-Traum\u00e1tico",
        "genero": "m",
        "valor_consulta": 45.0,
        "tipo_consulta": "presencial",
        "data_consulta": "2024-05-28",
        "casado": False,
        "filhos": False,
    },
    {
        "id": 9,
        "nome": "Sofia Almeida",
        "idade": 26,
        "cidade": "Viseu",
        "area_profissional": "Advogada",
        "assunto": "Fobia Social",
        "genero": "f",
        "valor_consulta": 80.0,
        "tipo_consulta": "online",
        "data_consulta": "2024-05-30",
        "casado": False,
        "filhos": False,
    },
    {
        "id": 10,
        "nome": "Lu\u00eds Mendes",
        "idade": 60,
        "cidade": "Lisboa",
        "area_profissional": "Contabilista",
        "assunto": "Planeamento de Reforma",
        "genero": "m",
        "valor_consulta": 50.0,
        "tipo_consulta": "presencial",
        "data_consulta": "2024-06-01",
        "casado": True,
        "filhos": True,
    },
]

for cliente in listagem:
    print(cliente["id"])
