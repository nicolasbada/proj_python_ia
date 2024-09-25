lista = [1,6,9]
Tupla = (3,7,8)
dicionario = {
"Professor":"Gustavo",
"Disciplina":"Versionamento",
"Aluno":"Nicolas",
"Ano":2024
}
print(lista[2])
print(Tupla[2])
print(dicionario.keys())
print(type(dicionario))
for x in dicionario.values():
    print("{:>10}{:>16}".format(x.keys("valor",x.values)))