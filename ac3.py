'''Exercício 1'''

def tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    if l2 == l3:
        return "Isósceles"
    if l1 != l2 != l3:
        return "Escaleno"
    return "Triângulo inexistente"

print(tipo_triangulo(5, 5, 5))
print(tipo_triangulo(3, 7, 7))
print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(1, 1, 9))

'''Exercício 2'''

def dia_semana(x):
    if x == 1:
        return "Domingo"
    if x == 2:
        return "Segunda-feira"
    if x == 3:
        return "Terça-feira"
    if x == 4:
        return "Quarta feira"
    if x == 5:
        return "Quinta-feira"
    if x == 6:
        return "Sexta-feira"
    if x == 7:
        return "Sábado"
    return "Incompatível"

print(dia_semana(2))
print(dia_semana(4))
print(dia_semana(1))
print(dia_semana(11))

'''exercício 3'''

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicaçao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    x = input("Operação desejada ")
    if x == "soma":
        resultado = a + b
        print("A resposta da soma é: ", resultado)
    if x == "subtracao":
        resultado = a - b
        print("A resposta da subtração é: ", resultado)
    if x == "multiplicacao":
        resultado = a * b
        print("A resposta da multiplicação é: ", resultado)
    if x == "divisao":
        resultado = a / b
        print("A resposta da divisão é: ", resultado)
    else:
        print("A operação não é valida.")

calculadora()