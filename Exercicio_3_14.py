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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_14.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Este programa calcula o preço a pagar pelo aluguel de um carro com input de dias e km rodado (R$60 por dia e R$0,15 por km)

print("\n\n") #Esta linha é apenas estética para melhor visialização das saidas no prompt

km_rodados = int(input("Por favor, digite a quantidade de quilometros rodados: "))
dias_aluguel = int(input("Por favor, informe quantos dias ficou com o veículo: "))

preco = (km_rodados * 0.15) + (dias_aluguel * 60)

print(f"O preço da locação é de R$ {preco:.2f}\n\n")