
nome = input('Digite seu nome:')
print(nome)
#------------------------

a=3
b=5

resultado = (2*a)*(3*b)
print(resultado)

#------------------------

variaveis=[]
soma=int(0)

for i in range(0,3,1):
    variaveis.append(int(input("Digite uma variavel: ")))

for i in variaveis:
    soma += i

print(soma)