# Quiz: Leer un número entero de 5 dígitos y determinar si es capicúa.


print("------------------------------")
print("--------Número Capicúa--------")
print("------------------------------")


# input

a = int(input("Digite el primer valor de su número: "))
b = int(input("Digite el segundo valor de su número: "))
c = int(input("Digite el tercer valor de su número: "))
d = int(input("Digite el cuarto valor de su número: "))
e = int(input("Digite el quinto valor de su número: "))


# processing and output

if(a==e and b==d):
    print("El número cumple la condición, es capicúa.")
else:
    print("Por favor revise los valores digitados y vuelva a intentarlo de nuevo.")
