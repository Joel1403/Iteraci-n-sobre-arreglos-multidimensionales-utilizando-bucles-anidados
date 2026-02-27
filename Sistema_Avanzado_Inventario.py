
import json
import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            print("\nResultados encontrados:")
            for p in encontrados:
                self.mostrar_producto(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_producto(self, producto):
        print(f"ID: {producto.get_id()} | "
              f"Nombre: {producto.get_nombre()} | "
              f"Cantidad: {producto.get_cantidad()} | "
              f"Precio: ${producto.get_precio():.2f}")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nLista de Productos:")
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump(
                    {id_p: p.to_dict() for id_p, p in self.productos.items()},
                    f,
                    indent=4
                )
            print("Inventario guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    data = json.load(f)
                    for id_p, datos in data.items():
                        self.productos[id_p] = Producto.from_dict(datos)
                print("Inventario cargado correctamente.")
            except Exception as e:
                print(f"Error al cargar archivo: {e}")


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo()

        elif opcion == "7":
            inventario.guardar_archivo()
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
