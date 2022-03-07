#pruebas
class Coche():
         ruedas=4
         largo=260
         ancho=130
         arrancado=False

         def arrancar(self):
                  Coche.arrancado=True

mazda=Coche() #ejemplar de clase

a=mazda.ancho
print (a)
print (mazda.arrancado) #aqui el coche no esta arrancado
mazda.arrancar() #arrancamos coche
print (mazda.arrancado) #devuelve true, el coche esta arrancado.