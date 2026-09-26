### Ex 1 - Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e o seu sucessor.

n = int(input('Digite um número inteiro: '))

nant = n-1

npos = n+1

print(f'O número inserido foi {n}. O antecessor de {n} é {nant}, e o posterior é {npos}')