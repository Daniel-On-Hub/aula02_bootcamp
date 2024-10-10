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

