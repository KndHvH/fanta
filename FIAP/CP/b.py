#1

num1=int(input("Digite numero 1: "))
num2=int(input("Digite numero 2: "))

soma=num1+num2

print(soma)

print("_______________________")
#2

metro=float(input("Digite em Metro: "))
mm=float(metro*1000)
print(f"{metro} Metros = {mm} Milimetros")

print("_______________________")
#3
dias=int(input("Digite o numero de dias: "))
horas=int(input("Digite o numero de horas: "))
minutos=int(input("Digite o numero de minutos: "))
segundos=int(input("Digite o numero de segundos: "))

horas += dias * 24
minutos += horas * 60
total_seg = minutos * 60 + segundos

print("Total segundos = ",total_seg)

print("_______________________")
#4

sal=int(input("Digite o seu salario: "))
porc=int(input("Digite a porcentagem do aumento (sem %): "))

x=float(1+porc/100)
novo_sal=sal*x
diff=novo_sal-sal

print("Antigo salario: R$",sal)
print(f"Porcentagem de aumento: {porc}%")
print("Novo salario: R$",nsal)
print("Diferenca em reais: R$",diff)

print("_______________________")
#5
valor=int(input("Digite o valor do produto: "))
porc=int(input("Digite a porcentagem de desconto sem o %: "))
porc=porc*-1
n_valor=valor*(1+porc/100)
print("Valor desconto:",(valor*(porc/100)))
print("Novo valor: ",n_valor)

