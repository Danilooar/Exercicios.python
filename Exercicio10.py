"""Objetivo do projeto: Criar um módulo de login do nosso "APP" deve obter as swguintes informações do funcionário

  ¨¨Funcionalidade do módulo 1 
       1-Obter o nome do usuário
       
       2_Obter a idade do usuário
       
       3-Registrar de forma  automática a data de cadastro do usuário, usando a data do registro como data de registro.
       
       4- Para cada novo Funcinário que é registrado na empresa, ele recebe um dos seguintes cartões que é sorteado de forma aleatório
       
  ¨¨Funcionalidade do módulo  2
       1-Usando os dados obtidos no módulo 1, exiba as seguintes informações :
         * Olá [nome do usuário] seu registro foi concluido com sucesso no dia [data de cadastro no formato dd/mm/aaaa] Parabén, houve um sorteio e você ganhou um cartão de compras no valor de [Valor sorteado]

"""

from datetime import datetime
import random


print('------------- Olá, bem-vindo a nossa empresa ------------- ')
nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

cadastro = datetime.now()

Cartoes = ['R$50,00 ', 'R$200,00', 'R$120,00' ]


Sorteio = (random.choice((Cartoes)))

aniversario = datetime.strptime(
  input('Digite sua data de aniversário no formato dd/mm/aaaa: '),'%d/%m/%Y'
  )

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {cadastro.day}/{cadastro.month}/{cadastro.year}.\nParabéns,houve um sorteio e você ganhou um cartão de compras no valor de {Sorteio}')