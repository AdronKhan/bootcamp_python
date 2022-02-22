##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_12.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa calcula o desconto de um preço dado preço original e percentual de desconto

print ("\n\n") #este comando serve apenas para melhor visualizar a saida do programa na tela do prompt

distancia_km = int(input("Digite a distância a ser percorrida em km: "))
velocidade_kmh = int(input("Digite a velocidade média em Km/h: "))

horas = (distancia_km // velocidade_kmh)
minutos = ((distancia_km)/(velocidade_kmh) - (distancia_km)//(velocidade_kmh))*60


print(f"\n\nO tempo estimado de viagem é de {horas} horas e {minutos:.0f} minutos\n\n")

#Agora calculando como no gabarito, com uso do resto das divisões %

tempo_s = int((distancia_km)/(velocidade_kmh) * 3600)  # convertemos de horas para segundos
horas_b = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos_b = int(tempo_s / 60)
segundos_b = int(tempo_s % 60)
print(f"Resposta alternativa: \n\nO tempo estimado é de {horas_b} horas, {minutos_b} minutos e {segundos_b} segundos.\n\n")
