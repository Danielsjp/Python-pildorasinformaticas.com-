def sumar(number1, number2):
         
         try:
                  total = (int(number1) + int(number2))
                  return total
         except ValueError:
                  print ("numero introducido incorrecto")
                  return ("NO")
num1 = (input("Introduce un numero: "))
num2 = (input("Introduce otro numero: "))
print(sumar(num1, num2)) 