d = {'Nome: ': ['Ana', 'Bruno'], 'Idade:': ['18', '19']}

d2 = [
    {
        "Nome": "Ana",
        "Idade": 18,
        "Senha": "A1n8"
    },
    {
        "Nome": "Bruno",
        "Idade": 19,
        "Senha": "B1r9"
    }
]


while True:
    nome = input()
    if (nome == "Saida"):
        break

    idade = int(input())

    idadeString = str(idade)

    senha = ""
    for i in range(2):
        senha += nome[i] + idadeString[i]

    print("Senha: " + senha)

    d2.append(
        {
            "Nome": nome,
            "Idade": idade,
            "Senha": senha
        }
    )

for pessoa in d2:
    print()
    print(pessoa["Nome"])
    print(pessoa["Idade"])
    print(pessoa["Senha"])