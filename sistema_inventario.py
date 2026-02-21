from itertools import product


class Producto:
    @staticmethod
    def check_not_zero(numero):
        return numero >= 0

    def __init__(self, nombre, precio, cantidad):
        if self.check_not_zero(len(nombre)):
            self.nombre = nombre
        if self.check_not_zero(precio):
            self.precio = precio
        if self.check_not_zero(cantidad):
            self.cantidad = cantidad

    def __str__(self):
        return f"nombre: {self.nombre} - precio: {self.precio} - cantidad: {self.cantidad}"

    def actualizar_precio(self, nuevo_precio):
        if self.check_not_zero(nuevo_precio):
            self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        if self.check_not_zero(nueva_cantidad):
            self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad


product = Producto('mango', 5, 2)
print(product.calcular_valor_total())
print(product.__str__())
