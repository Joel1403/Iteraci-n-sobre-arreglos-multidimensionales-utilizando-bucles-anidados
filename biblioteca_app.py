
# ==========================================
# SISTEMA DE BIBLIOTECA DIGITAL
# Implementación en un solo archivo
# ==========================================

class Libro:
    """Representa un libro dentro del sistema."""

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para título y autor (inmutable)
        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    def obtener_titulo(self):
        return self._info[0]

    def obtener_autor(self):
        return self._info[1]

    def obtener_categoria(self):
        return self._categoria

    def obtener_isbn(self):
        return self._isbn

    def __str__(self):
        return f"Título: {self._info[0]} | Autor: {self._info[1]} | Categoría: {self._categoria} | ISBN: {self._isbn}"


class Usuario:
    """Representa un usuario registrado en la biblioteca."""

    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados = []  # lista

    def obtener_id(self):
        return self._id_usuario

    def obtener_nombre(self):
        return self._nombre

    def obtener_libros(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self._libros_prestados:
            if libro.obtener_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None


class BibliotecaServicio:
    """Contiene la lógica del sistema de biblioteca."""

    def __init__(self):
        self.libros = {}       # diccionario ISBN -> Libro
        self.usuarios = {}     # diccionario ID -> Usuario
        self.ids_usuarios = set()  # conjunto de IDs únicos

    # ------------------
    # Gestión de libros
    # ------------------
    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro agregado correctamente.")

    def eliminar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ------------------
    # Gestión de usuarios
    # ------------------
    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ------------------
    # Préstamos
    # ------------------
    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)

        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros[isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("El usuario no tiene ese libro.")

    # ------------------
    # Búsquedas
    # ------------------
    def buscar_por_titulo(self, titulo):

        encontrados = False

        for libro in self.libros.values():
            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros.")

    def buscar_por_autor(self, autor):

        encontrados = False

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros.")

    def buscar_por_categoria(self, categoria):

        encontrados = False

        for libro in self.libros.values():
            if libro.obtener_categoria().lower() == categoria.lower():
                print(libro)
                encontrados = True

        if not encontrados:
            print("No se encontraron libros.")

    # ------------------
    # Libros de usuario
    # ------------------
    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        libros = usuario.obtener_libros()

        if not libros:
            print("El usuario no tiene libros prestados.")
            return

        for libro in libros:
            print(libro)


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n====== BIBLIOTECA DIGITAL ======")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar por título")
        print("8. Buscar por autor")
        print("9. Buscar por categoría")
        print("10. Listar libros de usuario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID usuario: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":

            titulo = input("Título a buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor a buscar: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "9":

            categoria = input("Categoría a buscar: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "10":

            id_usuario = input("ID usuario: ")
            biblioteca.libros_usuario(id_usuario)

        elif opcion == "0":

            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
