"""Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado."""




def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo > 20:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Digite o consumo médio mensal: "))
plano_recomendado = recomendar_plano(consumo)
print("Com base no seu consumo, recomenda-se:", plano_recomendado)

  

                     
    
    

    
    