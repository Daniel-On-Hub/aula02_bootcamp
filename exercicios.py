import math

# Faça um programa que peça dois números inteiros e imprima  divisão inteira do primeiro pelo segundo.

numero_inteiro01 = int(input("Inserir um numero inteiro : "))
numero_inteiro02 = int(input("Inserir outro numero inteiro : "))
resultado = numero_inteiro01 // numero_inteiro02
print(resultado)


# Escreva um programa que calcule o raio a área de um círculo, recebendo o raio como entrada.

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")

# Faça um programa que peça o usuário para digitar uma data em formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano.

data_do_usuario = input("Insira uma data no formato dd/mm/aaaa")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")




