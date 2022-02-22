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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_4.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa objetiva informar se um contribuinte deve ou não pagar impostos sobre seu salário
#A premissa é que incide imposto para valores de salário superiores a R$ 1,200.00

salario = float(input("\n\nDigite seu salário atual: "))
teto = 1200.00
if salario > teto:
    print ("Perdeu, preibói! Vai paga imposto SIM!\n\n")
if salario <= teto:
    print ("Ufa! Ganhar pouco é ruim mas não paga imposto na fonte! Há!\n\n")