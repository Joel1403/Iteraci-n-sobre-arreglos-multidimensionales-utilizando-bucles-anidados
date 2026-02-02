class Dashboard:
    def __init__(self):
        self.tareas = []

    def mostrar_menu(self):
        print("\n===== DASHBOARD - PROGRAMACIÓN ORIENTADA A OBJETOS =====")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

    def agregar_tarea(self):
        tarea = input("Ingrese la descripción de la tarea: ")
        self.tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def ver_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            print("\nLista de tareas:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self):
        self.ver_tareas()
        if self.tareas:
            try:
                indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                self.tareas.pop(indice)
                print("Tarea eliminada correctamente.")
            except (ValueError, IndexError):
                print("Opción inválida.")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.ver_tareas()
            elif opcion == "3":
                self.eliminar_tarea()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.ejecutar()
