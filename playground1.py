### Importando bibliotecas

import math


### Ex 5 - Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e o seu sucessor.
##  n = int(input('Digite um número inteiro: '))
##  
##  nant = n-1
##  npos = n+1
##  
##  print(f'O número inserido foi {n}. O antecessor de {n} é {nant}, e o posterior é {npos}.')


### Ex 6 - Faça um programa que leia um número inteiro e mostre na tela o seu dobro, triplo e raiz quadrada.
##  n = int(input('Digite um número inteiro: '))
##  
##  ndbr = n*2
##  ntrp = n*3
##  nraq = math.sqrt(n)
##  
##  print(f'O número inserido foi {n}. O dobro de {n} é {ndbr}, o triplo é {ntrp} e a raiz quadrada é {nraq}.')


### Ex 7 - Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
## n = float(input('Digite a primeira nota do aluno: '))
## n2 = float(input('Digite a segunda nota do aluno: '))
## 
## m = (n+n2)/2
## 
## print(f'A média do aluno foi {m}.')


### Ex 8 - Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
##  n = float(input('Digite um valor em metros: '))
##  
##  nkm = n/1000
##  nhm = n/100
##  nda = n/10
##  ndm = int(n/0.1)
##  ncm = int(n/0.01)
##  nmm = int(n/0.001)
##  
##  print(f'O valor inserido foi {n}m, que corresponde a:')
##  print(f'{nkm}km (quilômetros).')
##  print(f'{nhm}hm (hectômetros).')
##  print(f'{nda}da (decâmetros).')
##  print(f'{ndm}dm (decímetros).')
##  print(f'{ncm}cm (centímetros).')
##  print(f'{nmm}mm (milímetors).')


### Ex 9 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
##  n = int(input('Digite um número inteiro para ver sua tabuada: '))
##  
##  print('-'*15)
##  print('{} x {:2} = {:2}'.format(n, 1, n*1))
##  print('{} x {:2} = {:2}'.format(n, 2, n*2))
##  print('{} x {:2} = {:2}'.format(n, 3, n*3))
##  print('{} x {:2} = {:2}'.format(n, 4, n*4))
##  print('{} x {:2} = {:2}'.format(n, 5, n*5))
##  print('{} x {:2} = {:2}'.format(n, 6, n*6))
##  print('{} x {:2} = {:2}'.format(n, 7, n*7))
##  print('{} x {:2} = {:2}'.format(n, 8, n*8))
##  print('{} x {:2} = {:2}'.format(n, 9, n*9))
##  print('{} x {:2} = {:2}'.format(n, 10, n*10))
##  print('-'*15)


### Ex 10 - Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
##  n = float(input('Digite o valor do saldo em conta: R$'))
##  
##  ncnv = n/5.19
##  
##  print('Com R${:.2f} você pode comprar U${:.2f}.'.format(n, ncnv))


### Ex 11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
### necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
##  a = float(input('Digite a altura da sua parede em metros: '))
##  l = float(input('Digite a largura da sua parede em metros: '))
##  
##  ar = a*l
##  qt = float(ar/2)
##  
##  print('A área da sua parede de {} x {} é igual a {}m². Você precisará de {}l de tinta.'.format(a, l, ar, qt))


### Ex 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
##  v = float(input('Digite o preço original do produto: R$'))
##  
##  vcd = v*0.95
##  
##  print('O preço original é R${:.2f} e ficará R${:.2f} com o desconto de 5% aplicado'.format(v, vcd))


### Ex 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
##  s = float(input('Digite o salário do funcionário: R$'))
##  
##  sca = s*1.045
##  
##  print('O salário original é R${:.2f} e ficará R${:.2f} após o reajuste.'.format(s, sca))


### Ex 14 - Faça um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
##  c = float(input('Digite uma temperatura em ºC: '))
##  
##  ccf = ((9*c)/5)+32
##  
##  print('A temperatuda de {}ºC equivale a {}ºF'.format(c, ccf))


### Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
### ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
##  d = int(input('Por quantos dias o carro foi alugado? '))
##  km = float(input('Quantos km foram percorridos? '))
##  
##  v = (d*60)+(km*0.15)
##  
##  print('O valor a ser pago é R${:.2f}.'.format(v))