"""Calcule com o datatome quantos dias falta para a da data do seu aniversário"""

from datetime import datetime

aniversario = datetime(2024 , 6, 12);

Dias_para_aniv = aniversario - datetime.now()


print(Dias_para_aniv)


