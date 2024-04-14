"""DESAFIO 
DESAFIO 1 : ENCONTRE O INDICE DE "O" DENTRO DA VARIAVEL BIBLIOTECA
DESAFIO 2 : USANDO A FRASE "DESENVOLVIMENTO DE APLICAÇÕES" IMPRIMA APENAS 'DE APLICAÇÕES'


"""

Biblioteca = 'Biblioteca'

print(Biblioteca.index('o'))

Frase = 'DESENVOLVIMENTO DE APLICAÇÕES'

indice_d = Frase.rindex('D')
indice_s = Frase.rindex('S')

print(Frase[indice_d:indice_s + 1 ])