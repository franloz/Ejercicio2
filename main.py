class Electrodomestico:
    def __init__(self, precioBa=100,color="blanco",consumo='F',peso=5):
        self.color=color
        self.precioBa = precioBa
        self.comprobarConsumoEnergetico(consumo)
        self.peso = peso

    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A", "B", "C", "D", "E", "F"):
            self.consumo = letra
        else:
            self.consumo='F'


    def comprobarColor(self,color):
        if color in ("blanco", "negro","rojo", "azul", "gris"):
            self.color=color
        else:
            self.color = "blanco"

    def precioFinal(self):
        if self.consumo == 'A':
            self.precioBa = self.precioBa + 100
        elif self.consumo == 'B':
            self.precioBa = self.precioBa + 80
        elif self.consumo == 'C':
            self.precioBa = self.precioBa + 60
        elif self.consumo == 'D':
            self.precioBa = self.precioBa + 50
        elif self.consumo == 'E':
            self.precioBa = self.precioBa + 30
        elif self.consumo == 'F':
            self.precioBa = self.precioBa + 10

        if 0 < self.peso < 19:
            self.precioBa = self.precioBa + 10
        elif 20 < self.peso < 49:
            self.precioBa = self.precioBa + 50
        elif 50 < self.peso < 79:
            self.precioBa = self.precioBa + 80
        elif self.peso > 80:
            self.precioBa = self.precioBa + 100


class Lavadora(Electrodomestico):
    def __init__(self, precioBa=100, color="blanco", consumo='F', peso=5, carga=5):
        super().__init__(precioBa=precioBa, color=color, consumo=consumo, peso=peso)
        self.carga=carga

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.carga > 30:
            self.precioBa = self.precioBa + 50

class Television(Electrodomestico):
    def __init__(self, precioBa=100, color="blanco", consumo='F', peso=5, resolucion=20, fourK=False):
        super().__init__(precioBa=precioBa, color=color, consumo=consumo, peso=peso)
        self.resolucion = resolucion
        self.fourK = fourK

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.precioBa = self.precioBa*1.3
        if self.fourK == True:
            self.precioBa = self.precioBa+50



electrodomesticos=[]
electrodomesticos.append(Television(100,"negro",'F',10,6,True))
electrodomesticos.append(Television(300,"rojo",'E',15,20,False))
electrodomesticos.append(Television(300,"azul",'A',25,40,False))
electrodomesticos.append(Television(300,"gris",'B',30,50,False))
electrodomesticos.append(Television(300,"blanco",'C',5,10,False))

electrodomesticos.append(Lavadora(400,"negro",'D',6,8))
electrodomesticos.append(Lavadora(250,"rojo",'F',10,3))
electrodomesticos.append(Lavadora(120,"gris",'F',7,2))

electrodomesticos.append(Electrodomestico(1000,"negro",'D',6))
electrodomesticos.append(Electrodomestico(700,"rojo",'E',8))

tele=0
lava=0
ele=0
for e in electrodomesticos:
    e.precioFinal()
    if isinstance(e, Television):
        tele += e.precioBa
    elif isinstance(e,Lavadora):
        lava += e.precioBa
    else:
        ele += e.precioBa
total=tele+lava+ele
print("Total de televisores: " + repr(tele))
print("Total de lavadoras: " + repr(lava))
print("Total de electrodomésticos: " + repr(ele))
print("Total: " + repr(total))


