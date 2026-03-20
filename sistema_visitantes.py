import tkinter as tk
from tkinter import ttk, messagebox

# ============================
# MODELO
# ============================
class Visitante:
    def __init__(self, cedula, nombre, motivo):
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo


# ============================
# SERVICIO
# ============================
class VisitaServicio:
    def __init__(self):
        self._visitantes = []

    def registrar(self, visitante):
        if any(v.cedula == visitante.cedula for v in self._visitantes):
            return False
        self._visitantes.append(visitante)
        return True

    def obtener_todos(self):
        return list(self._visitantes)

    def eliminar(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False

    def actualizar(self, cedula, nombre, motivo):
        for v in self._visitantes:
            if v.cedula == cedula:
                v.nombre = nombre
                v.motivo = motivo
                return True
        return False


# ============================
# UI
# ============================
class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Sistema Profesional de Registro de Visitantes")
        self.root.geometry("750x450")
        self.root.resizable(False, False)

        # ======= FORM =======
        frame_form = tk.LabelFrame(self.root, text="Datos del Visitante", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0, sticky="w")
        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w")
        tk.Label(frame_form, text="Motivo:").grid(row=2, column=0, sticky="w")

        self.cedula_entry = tk.Entry(frame_form, width=30)
        self.nombre_entry = tk.Entry(frame_form, width=30)
        self.motivo_entry = tk.Entry(frame_form, width=30)

        self.cedula_entry.grid(row=0, column=1, padx=5, pady=2)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=2)
        self.motivo_entry.grid(row=2, column=1, padx=5, pady=2)

        # ======= BUTTONS =======
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Registrar", width=15, command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Actualizar", width=15, command=self.actualizar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Eliminar", width=15, command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="Limpiar", width=15, command=self.limpiar).grid(row=0, column=3, padx=5)

        # ======= TABLE =======
        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        columnas = ("cedula", "nombre", "motivo")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")

        self.tree.column("cedula", width=150)
        self.tree.column("nombre", width=200)
        self.tree.column("motivo", width=300)

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos)

    # ===== FUNCTIONS =====
    def registrar(self):
        cedula = self.cedula_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        motivo = self.motivo_entry.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)
        if self.servicio.registrar(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar(self):
        cedula = self.cedula_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        motivo = self.motivo_entry.get().strip()

        if self.servicio.actualizar(cedula, nombre, motivo):
            messagebox.showinfo("Actualizado", "Registro actualizado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "No se pudo actualizar")

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un registro")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar?")
        if not confirm:
            return

        cedula = self.tree.item(seleccionado)["values"][0]
        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Eliminado", "Registro eliminado")
            self.actualizar_tabla()
            self.limpiar()

    def limpiar(self):
        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.motivo_entry.delete(0, tk.END)

    def cargar_datos(self, event):
        seleccionado = self.tree.selection()
        if seleccionado:
            valores = self.tree.item(seleccionado)["values"]
            self.limpiar()
            self.cedula_entry.insert(0, valores[0])
            self.nombre_entry.insert(0, valores[1])
            self.motivo_entry.insert(0, valores[2])

    def actualizar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for v in self.servicio.obtener_todos():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def run(self):
        self.root.mainloop()


# ============================
# MAIN
# ============================
if __name__ == "__main__":
    servicio = VisitaServicio()
    app = AppTkinter(servicio)
    app.run()
