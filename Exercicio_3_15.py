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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_15.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa calcula o tempo de vida perdido por um fumante perguntando a ele quanto cigarros fuma por dia e que cada cigarro reduz a vida em 10 minutos

print("\n\n") #Esta linha é apenas estética para melhor visialização das saidas no prompt

cigarros_dia = int(input("Quantos cigarros você fuma em média por dia?\n"))
tempo_fumando = int(input("A quantos anos você fuma?\n"))
tempo_perdido = int((tempo_fumando * 365 * cigarros_dia * 10)/60//24)

print(f"Parabéns! Você vai encontrar o Criador {tempo_perdido} dias mais cedo!\n")