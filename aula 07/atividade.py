Produto={
    "ID":2024001,
    "Produto":"Maçã",
    "Preço":3.50,
    "Validade":"25/09/2024"
}
chave = [x for x in Produto.keys()]
Valor = [x for x in Produto.values()]
x = 0
while(x<len(chave)):
    print("{:<10}{:<10}".format(chave[x],Valor[x]))
    x += 1