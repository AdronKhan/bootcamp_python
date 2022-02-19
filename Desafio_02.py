


qtd_km = int(input("Digite a quantidade de quilómetros percorridos:"))

qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preço_por_dia = 60
preço_por_km = 0.15

preço_total_km = qtd_km * preço_por_km
preço_total_dia = qtd_dias * preço_por_dia

preço_a_pagar = preço_total_km + preço_total_dia

print (f"total a pagar: R$ {preço_a_pagar : 7.2f}")