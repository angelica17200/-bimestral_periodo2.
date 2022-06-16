"""Programa para calcular numeros pares e impares"""

print("--------------------------------")
print("-------- PARES E IMPARES -------")
print("--------------------------------")

#input 

n = int(input("Digite un número entero y positivo: "))

#Procesamiento

par = 0
impar = 0

while n != 0:
    r = n % 2
    if r == 0:
        par = par + 1
    else:
        impar = impar + 1
    n = int(input("Digite un número entero y positivo: "))

#output
print("Se ingresaron " + str(par) + " números pares")
print("Se ingresaron " + str(impar) + " números impares")
print("Eso era...")