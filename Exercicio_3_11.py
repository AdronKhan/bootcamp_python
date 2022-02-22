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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_11.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa calcula o desconto de um preço dado preço original e percentual de desconto

print ("\n\n") #este comando serve apenas para melhor visualizar a saida do programa na tela do prompt

preco = float(input("Por favor, digite o preço sem desconto: "))
desconto = float(input("Por favor, digite o percentual de desconto - somente números: "))
novo_preco = (preco * (1-desconto/100))

print(f"Um desconto de {desconto}% sobre um preço de R$ {preco:.2f} resulta num novo preco de R$ {novo_preco:.2f}\n\n")