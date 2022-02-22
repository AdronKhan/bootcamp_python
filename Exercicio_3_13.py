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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_13.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa converte temperaturas em ºC para ºF

print("\n\n") #Esta linha é apenas estética para melhor visialização das saidas no prompt

temp_c = float(input("Por favor, digite a temperatura em ºC a ser convertidas em ºF: "))
temp_f = (((9 * temp_c)/5) + 32)

print(f"{temp_c :.2f}º celsius equivalem a {temp_f :.2f}º farenheit.\n\n")
