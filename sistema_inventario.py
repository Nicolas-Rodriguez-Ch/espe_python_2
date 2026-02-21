class Producto:
    @staticmethod
    def check_non_negative(numero):
        return numero >= 0

    def __init__(self, nombre, precio, cantidad):
        try:
            if not nombre or not isinstance(nombre, str) or not self.check_non_negative(len(nombre)):
                raise ValueError('No es un nombre valido')
            if not precio or not isinstance(precio, (int, float)) or not self.check_non_negative(precio):
                raise ValueError('El precio no puede ser menor que 0')
            if not cantidad or not isinstance(cantidad, int) or not self.check_non_negative(cantidad):
                raise ValueError('La cantidad no puede ser menor que 0')

            self.cantidad = cantidad
            self.precio = precio
            self.nombre = nombre
        except ValueError as e:
            print(f"Error al crear producto: {e}")
            raise

    def __str__(self):
        return f"nombre: {self.nombre} - precio: {self.precio} - cantidad: {self.cantidad}"

    def actualizar_precio(self, nuevo_precio):
        try:
            if not nuevo_precio or not isinstance(nuevo_precio, (int, float)) or not self.check_non_negative(
                    nuevo_precio):
                raise ValueError('El precio no puede ser menor que 0')
            self.precio = nuevo_precio
        except ValueError as e:
            print(f"Error actualizando el precio de {self.nombre}: {e}")
            raise

    def actualizar_cantidad(self, nueva_cantidad):
        try:
            if not nueva_cantidad or not isinstance(nueva_cantidad, int) or not self.check_non_negative(nueva_cantidad):
                raise ValueError('La cantidad no puede ser menor que 0')
            self.cantidad = nueva_cantidad
        except ValueError as e:
            print(f"Error actualizando la cantidad de: {self.nombre}: {e}")
            raise

    def calcular_valor_total(self):
        return self.precio * self.cantidad


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        try:
            for producto in self.productos:
                if producto.nombre.lower() == nombre.lower():
                    return producto
            raise ValueError('Producto no encontrado')
        except ValueError as e:
            print(f"Error al buscar el producto {nombre}: {e}")
            return None

    def calcular_valor_inventario(self):
        counter = 0
        for producto in self.productos:
            counter += producto.calcular_valor_total()
        return counter

    def listar_productos(self):
        for producto in self.productos:
            print(producto.__str__())


mangos = Producto('mango', 1, 4)
limon = Producto('limon', 1, 10)
inventario = Inventario()
inventario.agregar_producto(mangos)
inventario.agregar_producto(limon)
inventario.listar_productos()
inventario.buscar_producto('tomate')
print(inventario.calcular_valor_inventario())
