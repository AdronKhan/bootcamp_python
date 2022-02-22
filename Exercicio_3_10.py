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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_10.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa calcula o aumento de um salário, dados o valor do salário e percentual de aumento.

print ("\n\n") #este comando serve apenas para melhor visualizar a saida do programa na tela do prompt

salario = float(input("Por favor, digite o salário atual: \n"))
aumento = float(input("Por favor, digite o percentual de aumento - somente números: "))
novo_salário = (salario * (1+aumento/100))

print(f"Um aumento de {aumento}% sobre um salário de R$ {salario:.2f} resulta num novo salário de R$ {novo_salário:.2f}")