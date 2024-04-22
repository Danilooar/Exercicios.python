"""Desafio
Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto."""


import re

def validar_numero_telefone(numero):

    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"
    
    if re.match(padrao, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

numero_telefone = input("Insira o seu número: ")


resultado = validar_numero_telefone(numero_telefone)
print(resultado)

