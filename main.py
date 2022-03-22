class Asiento():
    pass
    def __init__(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro= registro
    def cambiarColor(self,color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color

class Auto():
    pass
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio= precio
        self.asientos= list(asientos)
        self.marca= marca
        self.motor= motor
        self.registro= registro
        self.cantidadCreados= cantidadCreados

    def cantidadAsientos(self):
        contadorasientos=0
        if None==self.asientos:
            for i in self.asientos:
                if i != None:
                    contadorasientos+=1

        return contadorasientos
    
    def verificarIntegridad(self):
        mensaje1="Auto original"
        mensaje2="Las piezas no son originales"
        if self.registro == self.asientos[0].registro:
            if self.motor.registro == self.registro:
                print(mensaje1)
            else:
                print(mensaje2)
        else:
            print(mensaje2)

class Motor():
    pass
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo= tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def AsignarTipo(self,tipo):
        if (tipo=="electrico" or tipo=="gasolina"):
            self.tipo=tipo






