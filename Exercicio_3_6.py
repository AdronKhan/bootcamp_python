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
# Arquivo: C:\Users\adriano.paes\Desktop\Bootcamp Python\Programas\Exercicio_3_6.py
#
# Aluno: Adriano César Paes de Almeida
##############################################################################

#Retorna se o aluno foi aprovado ou não, sendo obrigatório ter média maior igual a 7 nas 3 matérias

materia1 = float(input("\n\nEntre a nota da M1: "))
materia2 = float(input("\nEntre a nota da M2: "))
materia3 = float(input("\nEntre a nota da M3: "))

if (materia1>=7 and materia2>=7 and materia3>=7):
    print("APROVADO, PARABÉNS!\n\n")
if (materia1<7 or materia2<7 or materia3<7):
    print("REPROVADO, tente outra vez... \n\n")