class EstacionDeServicio:
     def __init__(self, cantidad_colas, ):
        self.cantidad_colas = cantidad_colas

class Vehiculo:
    def __init__(self, marca, tipo_bencina):
        self.marca = marca
        self.tipo_bencina = tipo_bencina

class Bencina:
    def __init__(self, tipo):
        self.tipo = tipo

# tipos de vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, tipo_bencina):
        Vehiculo.__init__(self, marca, tipo_bencina)

class Moto(Vehiculo):
    def __init__(self, marca, tipo_bencina):
        Vehiculo.__init__(self, marca, tipo_bencina)

class Camion(Vehiculo):
    def __init__(self, marca, tipo_bencina):
        Vehiculo.__init__(self, marca, tipo_bencina)
        
class Camioneta(Vehiculo):
    def __init__(self, marca, tipo_bencina):
        Vehiculo.__init__(self, marca, tipo_bencina)

# 