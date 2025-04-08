from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from menu_screen import MenuScreen
from mostrar_contactos import ListaContactosScreen
from Agregar_contactos import AgregarContactoScreen
from eliminar_contactos import EliminarContactoScreen
from modificar_contactos import ModificarContactoScreen
from DataBase import ContactoDB

class ContactosApp(MDApp):
    def build(self):
        self.db = ContactoDB()
        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ListaContactosScreen(name="mostrar_contactos"))
        sm.add_widget(AgregarContactoScreen(name="Agregar_contacto"))
        sm.add_widget(EliminarContactoScreen(name="eliminar_contacto"))
        sm.add_widget(ModificarContactoScreen(self.db, name="modificar_contacto"))
        return sm
    
    def Agregar_contacto(self, nombre, telefono, correo):
        if nombre and telefono and correo:
            self.db.agregar(nombre, telefono, correo)
            print("Contacto agregado correctamente")
            self.root.current = "menu"
            pantalla = self.root.get_screen("mostrar_contactos")
            pantalla.actualizar_lista()
        else: 
            print("Todos los campos son obligatorios")
            
    def mostrar_contactos(self):
        pantalla = self.root.get_screen("mostrar_contactos")
        pantalla.actualizar_lista()
        self.root.current = "mostrar_contactos"
            
if __name__ == "__main__":
    ContactosApp().run()


