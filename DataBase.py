import sqlite3

class ContactoDB:
    def __init__(self):
        self.conexion = sqlite3.connect("contactos.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono INTEGER NOT NULL,
                correo TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def mostrar(self):
        self.cursor.execute("SELECT * FROM contactos")
        return self.cursor.fetchall()

    def agregar(self, nombre, telefono, correo):
        self.cursor.execute("INSERT INTO contactos (nombre, telefono, correo) VALUES (?, ?, ?)", 
                            (nombre, telefono, correo))
        self.conexion.commit()

    def eliminar(self, contacto_id):
        self.cursor.execute("DELETE FROM contactos WHERE id = ?", (contacto_id,))
        self.conexion.commit()

    def editar(self, contacto_id, nombre, telefono, correo):
        self.cursor.execute("""
            UPDATE contactos 
            SET nombre = ?, telefono = ?, correo = ? 
            WHERE id = ?
        """, (nombre, telefono, correo, contacto_id))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
