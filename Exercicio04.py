"""este projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes."""


_version_ ="0.0.1"
__author__="Danilo Araujo"
__License__="Unlicense"

menu = """ 

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

Saldo = 0;
Limite = 500;
Extrato = 0;
numero_saques=0
LIMITE_SAQUE=3


while True:
  
  opçao = input(menu)

  if opçao == "D": 
    add = (float(input("Informe o valor do deposito : R$ ")))
    Saldo = add + Saldo
  
    if add > 0 :
        Saldo == add;
        Extrato == f"Deposito R$: {add: .2f}"
    
    else:
           print("Operação falhou: você não tem saldo suficiente ")  
  
     
  elif opçao == "S":
      add = float(input("Digite o valor do saque : R$"))
      
      limiteSaldo = add > Saldo;
      
      LIMITE_SAQUE = add > Limite;
      
      ExcedeuSaque = numero_saques >= LIMITE_SAQUE;
      
      if limiteSaldo: 
        print("Operação falhou: Você não tem saldo suficiente .")
        
      elif LIMITE_SAQUE:
            print("Operação falhou! O valor do saque excede o limite.")

      elif ExcedeuSaque:
            print("Operação falhou! Número máximo de saques excedido.")
            
      elif add > 0:
            Saldo -= add
            Extrato += f"Saque: R$ {add:.2f}"
            numero_saques += 1

      else:
            print("Operação falhou! O valor informado é inválido.")
      
  elif opçao == "E" and Saldo == Saldo:
       print("================ EXTRATO ================")
       print("Não foram realizadas movimentações." if not Extrato else Extrato)
       print(f"Saldo: R$ {Saldo:.2f}")
       print("==========================================")
        
  elif opçao == "Q":
    break;
  
  else:
    print("Operação invalida, por favor selecione novamente a operação desejada")   

