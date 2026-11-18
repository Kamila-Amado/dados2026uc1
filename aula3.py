#Crie um algorotimo para dzer se um pessoa é maior de idade ou não 
#Números = int ou flot
# Faça um algoritmo para dizer se o número é par ou impar 

numero = int(input("digite um numero inteiro: "))

if numero % 2 == 0: 
    paridade = 'par'
else: 
    paridade = 'impar'

print(f'{numero} é {paridade}')
