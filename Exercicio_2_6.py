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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_2_6.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Calcule um aumento de 15% para um salário de R$ 750

salario = 750
aumento = 15
novo_salario = (750*(1+(aumento/100)))

print(f"\nO novo salário, com aumento de {aumento}%, é de R$ {novo_salario:.2f}\n")