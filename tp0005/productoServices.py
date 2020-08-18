from repositorios import Repositorios
from producto import Producto


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def crearProducto(self):
        print("\n----Agregando producto----")
        descripcion = input('Ingrese una descripcion: ')
        precio = int(input('Ingrese un precio: '))
        tipo = input('Ingrese el tipo de producto: ')
        return Producto(descripcion, precio, tipo)

    def add_producto(self, producto=None):
        if producto is None:
            producto.crearProducto()
        lastKey = -1
        for productKey in Repositorios.productosList:
            lastKey = productKey
        lastKey = lastKey + 1
        Repositorios.productosList[lastKey] = producto.__dict__
        return lastKey

    def update_producto(self, key):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando-----")

                descripcion = input('Introduzca la nueva descripcion: ')
                Repositorios.productosList[key]["_descripcion"] = descripcion
                print(Repositorios.productosList)

                precio = int(input('Introduzca el nuevo precio: '))
                Repositorios.productosList[key]["_precio"] = precio
                print(Repositorios.productosList)

                tipo = input('Introduzca el nuevo tipo de producto: ')
                Repositorios.productosList[key]["_tipo"] = tipo
                print(Repositorios.productosList)
            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError("El legajo a eliminar no existe")
        del Repositorios.productosList[key]
