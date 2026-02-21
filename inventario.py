import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("Archivo de inventario creado.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        try:
                            id_producto, nombre, cantidad, precio = linea.split(",")
                            self.productos[id_producto] = Producto(
                                id_producto,
                                nombre,
                                int(cantidad),
                                float(precio)
                            )
                        except ValueError:
                            print("Advertencia: Línea corrupta ignorada:", linea)

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")
        except Exception as e:
            print("Error inesperado al cargar:", e)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print("Error inesperado al guardar:", e)

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: El producto ya existe.")
            return

        self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio

        self.guardar_en_archivo()
        print("Producto actualizado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return

        del self.productos[id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos.values():
            print(
                f"ID: {producto.id_producto} | "
                f"Nombre: {producto.nombre} | "
                f"Cantidad: {producto.cantidad} | "
                f"Precio: ${producto.precio}"
            )


def menu():
    inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id_producto, nombre, cantidad, precio)

            elif opcion == "2":
                id_producto = input("ID del producto a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "3":
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "4":
                inventario.mostrar_inventario()

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
        except Exception as e:
            print("Error inesperado:", e)


if __name__ == "__main__":
    menu()
