
"""Desafio
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos."""

import string


itens = []

print("INSIRA O NOME DO EQUIPAMENTO: ")

for e in range (3):
   item = input("")
   
itens.append(item)


print("Lista de equipamentos")  
for a in itens:
  print("-" + item)

 


