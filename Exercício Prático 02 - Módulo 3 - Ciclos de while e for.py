# Ciclos: While e For

import time, os

os.system("cls")

menu = '''
.............................................................
:                           Menu                            :
:...........................................................:
: -- NÍVEL BÁSICO --                                        :
: Exercício B1 - Contagem Simples (while)                   :
: Exercício B2 - Contagem Decrescente (while)               :
: Exercício B3 - Contagem com for                           :
: Exercício B4 - Números Pares                              :
: -- INTERMÉDIO --                                          :
: Exercício I1 - Soma de 1 a 100                            :
: Exercício I2 - Tabuada                                    :
: Exercício I3 - Contador de Pares                          :
: -- NÍVEL AVANÇADO --                                      :
: Exercício A1 - Soma Personalizada                         :
: Exercício A2 - Menu Repetitivo                            :
: Exercício A3 - Fatorial                                   :
:...........................................................: 
'''
print(menu)
time.sleep(3)

# Exercício B1 - Contagem Simples (while) 
# Criar um programa que:
# Mostre números de 1 a 10 usando while.

print("Exercício B1 - Contagem Simples (while)")

b1_i = 1
while b1_i <= 10:
    print(b1_i)
    b1_i += 1

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício B2 - Contagem Decrescente (while)
# Criar um programa que:
# Mostre números de 10 até 1.

print("Exercício B2 - Contagem Decrescente (while)")

b2_i = 10
while b2_i >= 1:
    print(b2_i)
    b2_i -= 1

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício B3 - Contagem com for
# Criar um programa que:
# Mostre números de 1 a 20 usando for.

print("Exercício B3 - Contagem com for")

for b3_i in range(1, 21):
    print(b3_i)

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício B4 - Números Pares
# Criar um programa que:
# Mostre apenas números pares entre 1 e 20.

print("Exercício B4 - Números Pares")

for b4_i in range(2, 21, 2):
    print(b4_i)

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício I1 - Soma de 1 a 100
# Criar programa que:
# Calcule a soma dos números de 1 a 100.

print("Exercício I1 - Soma de 1 a 100")

i1_soma = 0
for i1_i in range(1, 101):
    i1_soma += i1_i
print(f"A soma de 1 a 100 é: {i1_soma}")

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício I2 - Tabuada
# Criar programa que:
# Peça um número
# Continue a pedir enquanto o número for positivo
# Só termina quando o número for negativo

print("Exercício I2 - Tabuada")

while True:
    i2_num = int(input("Insere um número (negativo para sair): "))
    if i2_num < 0:
        print("Número negativo inserido. Programa terminado.")
        break
    print(f"Tabuada do {i2_num}:")
    for i2_i in range(1, 11):
        print(f"{i2_num} x {i2_i} = {i2_num * i2_i}")
    print()

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício I3 - Contador de Pares
# Criar programa que:
# Conte quantos números pares existem entre 1 e 50.

print("Exercício I3 - Contador de Pares")

i3_contador = 0
for i3_i in range(1, 51):
    if i3_i % 2 == 0:
        i3_contador += 1
print(f"Existem {i3_contador} números pares entre 1 e 50.")

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício A1 - Soma Personalizada
# Criar programa que:
# Pergunte quantos números o utilizador quer inserir
# Peça esses números
# Mostre a soma total

print("Exercício A1 - Soma Personalizada")

a1_quantidade = int(input("Quantos números quer inserir? "))
a1_soma = 0

for a1_i in range(1, a1_quantidade + 1):
    a1_num = float(input(f"Digite o número {a1_i}: "))
    a1_soma += a1_num
print(f"A soma total dos {a1_quantidade} números é: {a1_soma}")
print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício A2 - Menu Repetitivo
# Criar programa com menu:
# 1 – Mostrar números de 1 a 10
# 2 – Mostrar números pares até 20
# 0 – Sair

# O menu deve repetir até o utilizador escolher 0.

print("Exercício A2 - Menu Repetitivo")

while True:
    print("\n=== MENU ===")
    print("1 – Mostrar números de 1 a 10")
    print("2 – Mostrar números pares até 20")
    print("0 – Sair")

    a2_opcao = input("\nEscolha uma opção: ")

    if a2_opcao == "1":
        print("\nNúmeros de 1 a 10:")
        for a2_i in range(1, 11):
            print(a2_i, end=" ")
        print()
    elif a2_opcao == "2":
        print("\nNúmeros pares até 20:")
        for a2_i in range(2, 21, 2):
            print(a2_i, end=" ")
        print()
    elif a2_opcao == "0":
        print("\nAdeus!")
        break
    else:
        print("\nOpção inválida! Tente novamente.")

print("---")

# Divisão entre os exercícios
input("Pressione Enter para passar para o próximo exercício: ")
print("---")

# Exercício A3 - Fatorial
# Criar programa que:
# Peça um número
# Calcule o fatorial desse número

# Exemplo:
# 5! = 5 × 4 × 3 × 2 × 1

print("Exercício A3 - Fatorial")

a3_num = int(input("Insere um número inteiro não negativo: "))

if a3_num < 0:
    print("Não existe fatorial de número negativo.")
else:
    a3_fatorial = 1
    for a3_i in range(1, a3_num + 1):
        a3_fatorial *= a3_i
    print(f"{a3_num}! = {a3_fatorial}")