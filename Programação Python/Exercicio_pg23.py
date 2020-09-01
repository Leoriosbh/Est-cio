'''
Created on 26/08/2020

@author: Leonardo Rios
'''
nome = input("Qual seu nome: ")
ultimoNome = input("Qual seu ultimo nome: ")
idade = input("Qual sua idade: ")
curso = input("Qual seu curso: ")
endereco = input("Qual seu endereco: ")
dicionario = {}
dicionario["nome"] = str(nome)
dicionario["ultimoNome"] = str(ultimoNome)
dicionario["idade"] = str(idade)
dicionario["curso"] = str(curso)
dicionario["endereco"] = str(endereco)
print(dicionario.items())

print()

print(str(nome))
print(str(ultimoNome))
print(str(idade))
print(str(curso))
print(str(endereco))

print()

del dicionario ["curso"]
dicionario["ultimoNome"] = 'Lopes'
print(dicionario.items())

print()

print(str(endereco))

dicTeste = dicionario.copy()

print()

dicTeste["nome"] = 'Leonardo'
dicTeste["idade"] ='60'
print(dicTeste.items())