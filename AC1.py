#Exercício 1-
import math

a = float(input("Informe o valor de a da equação: "))
b = float(input("Informe o valor de b da equação: "))
c = float(input("Informe o valor de c da equação: "))

d = (b**2 - 4*a*c)
print("Delta vale: ", d)

x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)
print("x1 vale:", x1)
print("x2 vale: ", x2)

#Exercício 2

ano = int(input("Que ano deseja analisar? "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))