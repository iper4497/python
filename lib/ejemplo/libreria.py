# Esta nueva versión del script tiene bastantes cambios
#   - Una nueva clase, baraja española, que hereda funciones y propiedades de la clase mazo. Ilustro así un concepto
#     importante en Programación Orientada a Objetos
#   - Defino la función__resp__ en los objetos para poder imprimir directamente en pantalla. Las funciones PrintName e ImprimeMazo ya no son necesarias
#   - Defino una función en la clase Mazo que me ordena las cartas por palo y valor. Para ello, necesito también una función que me devuelva el valor
#     numérico de la carta en la clase Carta. En esta función hago uso de If...Elif...Else
#   - Uso también una función anónima (lambda) en la función ordenar. Investigaré más adelante el uso de estas funciones http://www.secnetix.de/olli/Python/lambda_functions.hawk
 
 
import random
import itertools
 
class Carta():
 
    def __init__(self,valor,palo):
 
        # El constructor de la clase. Esta función se llama cuando la clase se instancia
 
        self.palo=palo
        self.valor=valor
 
 
    def PrintName(self):
 
        # La siguiente clase imprime en la consola la carta
 
        print(str(self.valor)+' de '+ self.palo)
 
    def ValorNumerico(self): # Esta función me devuelve el valor númerico de las figuras
 
        valornumerico=0
        if isinstance(self.valor, str)==True:
 
           valornumerico=int(self.valor[0:2])
 
        else:
            valornumerico=int(self.valor)
 
        return valornumerico
 
 
 
 
    def __repr__(self): # sobre-escribo la función __resp__ del objeto para poder imprimir directamente algo entendible
 
         return '{}: {} {}'.format(self.__class__.__name__,
                                  self.valor,
                                  self.palo)
 
class Mazo():
 
    def __init__(self):
 
        self.set=[]
 
    def NuevaCarta(self,obj): # Función para añadir cartas al mazo una a una
 
        self.set.append(obj)
 
    def SetdeCartas(self,obj): # Función para añadir una lista de cartas al mazo
 
        self.set=self.set+obj
 
 
    def ImprimeMazo(self): # Imprimir en consola las cartas en el mazo
 
        for card in self.set:
            card.PrintName()
 
    def Barajar(self): # Función que mezcla las cartas
 
        random.shuffle(self.set)
 
 
    def __repr__(self): # sobre-escribo la función __resp__ del objeto para poder imprimir directamente algo entendible
 
         mazostring='___________________\nOBJETO MAZO \nNumero de Cartas: '+str(len(self.set))+'\n___________________\nCARTAS SEGÚN ORDEN ACTUAL:\n'
         mazostring=mazostring+'\n Puntuación Basica (Suma valor cartas en mazo):'+str(self.PuntuacionBasica())+'\n'
         for item in self.set:
             mazostring=mazostring+str(item.valor)+' '+item.palo+'\n'
 
 
         return mazostring
 
    def Ordenar(self):
 
        self.set.sort(key=lambda x: (x.palo,x.ValorNumerico()))
 
    def DarCartas(self,number): # Método para repartir cartas del Mazo.
 
        cartas=[]
        for item in range(0,number):
            cartas.append(self.set[0])
            self.set.pop(0) # la carta escogida se elimina del mazo
 
 
        return cartas
 
    def PuntuacionBasica(self):
 
        puntuacion=0
        for carta in self.set:
            puntuacion=puntuacion+carta.ValorNumerico()
 
        return puntuacion
 
class BarajaEspanola(Mazo):
 
    def __init__(self):
 
        palos=('Oros','Copas','Bastos','Espadas')
        cartas=(1,2,3,4,5,6,7,'10 Sota','11 Caballo','12 Rey')
        self.set=[]
        for item in itertools.product(cartas,palos):
            carta=Carta(item[0],item[1])
            self.set.append(carta)
