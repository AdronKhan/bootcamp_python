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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_9.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa recebe do usuário informações sobre quantidade de dias, horas, minutos e segundos do usuário e os converte em segundos

print ("\n\n") #este comando serve apenas para melhor visualizar a saida do programa na tela do prompt

dias = int(input ("Por favor, digite o número de dias: "))
horas = int(input ("Por favor, digite o número de horas: "))
minutos = int(input ("Por favor, digite o número de minutos: "))
segundos = int(input("Por favor, digite o número de segundos: "))

conversao_segundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print(f"\n\n{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos equivalem a {conversao_segundos} segundos.\n\n")