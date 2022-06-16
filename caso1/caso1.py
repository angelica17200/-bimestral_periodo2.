"""programa para calcular las 5 notas de una materia y la definitiva """

print("---------------------------------")
print("--------NOTAS ESTUDIANTES -------")
print("---------------------------------")

#input
cod = int(input("Digite el código del estudiante: "))
if cod!=0:
    nota1 = float(input("Digite la nota del parcial no. 1:"))
    nota2 = float(input("Digite la nota del parcial no. 2:"))
    nota3 = float(input("Digite la nota del parcial no. 3:"))
else:
    print("Fin de los datos de entrada")

#processing 
reprobados = 0

while cod != 0:
    nota_final = ( nota1 + nota2 + nota3)/3
    print("El estudiante de codigo " + str(cod) + " obtuvo una nota definitiva de " + str(nota_final))
    if nota_final < 3:
        reprobados = reprobados + 1
        #input 
        cod = int(input("Digite el codigo del estudiante: "))
        if cod !=0:
            nota1=("Digite la nota del parcial no. 1:")
            nota2=("Digite la nota del parcial no. 2:")
            nota3=("Digite la nota del parcial no. 3:")
        else:
            print("Fin de los datos de entrada")
#output
print("Cantidad de estudiante que reprobaron la materia: " + str(reprobados))
print("eso era...")




