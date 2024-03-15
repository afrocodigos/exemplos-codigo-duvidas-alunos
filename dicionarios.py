# Criando um dicionário vazio
dicionario = {}

# Adicionando elementos ao dicionário
dicionario['nome'] = 'João'
dicionario['idade'] = 30
dicionario['cidade'] = 'São Paulo'

# Acessando valores no dicionário
print("Nome:", dicionario['nome'])
print("Idade:", dicionario['idade'])
print("Cidade:", dicionario['cidade'])

# Alterando um valor no dicionário
dicionario['idade'] = 35

# Acessando todos os itens no dicionário
print("\nTodos os itens no dicionário:")
for chave, valor in dicionario.items():
    print(chave + ":", valor)

# Removendo um item do dicionário
del dicionario['cidade']

# Verificando se uma chave está no dicionário
if 'cidade' in dicionario:
    print("\nCidade:", dicionario['cidade'])
else:
    print("\nA chave 'cidade' não está presente no dicionário.")

# Verificando o comprimento do dicionário
print("\nTamanho do dicionário:", len(dicionario))