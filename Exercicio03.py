"""Exercicio numero 3
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.
_________________________________
Tabela de imposto
---------------------------
de 0.00 a R$ 2000 ---> Isento 
de 2001 até 3000 ---> 8% sobre 1000
de 3001 até 4500 ---> 18% sobre 1000
acima de R$ 4500 ---> 28% sobre 1000
_________________________________
"""




__version_ ="0.0.1"
__author__="Danilo Araujo"
__License__="Unlicense"

Renda_Mensal = float(input("Digite a sua renda mensal: "))

if Renda_Mensal <= 2000:
    print("Você está isento.")

elif 2001 <= Renda_Mensal <= 3000: 
    imposto = (Renda_Mensal - 2000) * 0.08
    print("""-----Você deve pagar R$ {:.2f} de Imposto de Renda.------
          
 --------Obrigado por utilizar nosso serviço-------
          """.format(imposto))


elif 3001 <= Renda_Mensal <= 4500: 
    imposto = (Renda_Mensal - 3000) * 0.18 
    print(""" -----Você deve pagar R$ {:.2f} de Imposto de Renda.------
          
 --------Obrigado por utilizar nosso serviço-------
          """.format(imposto))
else:
    imposto = (Renda_Mensal - 3500) * 0.28 
    print(""" -----Você deve pagar R$ {:.2f} de Imposto de Renda.------
          
 --------Obrigado por utilizar nosso serviço-------          """.format(imposto))