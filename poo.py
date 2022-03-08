#pruebas
class Coche():
         ruedas=4
         largo=260
         ancho=130
         arrancado=False

         def arrancar(self):
                  self.arrancado=True

         def estado(self):
                  if(self.arrancar):
                           return "El coche esta arrancado"
                  else:
                           return "El coche esta parado"
                  
mazda=Coche() #ejemplar de clase

mazda.arrancar() #arrancamos coche
print (mazda.arrancado) #devuelve true, el coche esta arrancado.
print (mazda.estado())