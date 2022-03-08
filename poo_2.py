#contructores
#pruebas
#clase coche sin valores
class Coche():
         ruedas=""
         largo=""
         ancho=""
         arrancado=""

         def __init__(self, ruedas, largo, ancho, arrancado): 
             self.ruedas=ruedas
             self.largo=largo
             self.ancho=ancho
             self.arracado=arrancado
             

         def arrancar(self):
                  self.arrancado=True

         def estado(self):
                  if(self.arrancar):
                           return "El coche esta arrancado"
                  else:
                           return "El coche esta parado"
                  

c1=Coche(4,130,50,False)
print(c1.ancho) #muestra valor incialmente con constructor