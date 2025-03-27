from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from menu_screen import MenuScreen
from mostrar_contactos import ListaContactosScreen
from Agregar_contactos import AgregarContactoScreen
from Actividad_python2.eliminar_contactos import EliminarContactoScreen
from modificar_contactos import ModificarContactoScreen

class ContactosApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ListaContactosScreen(name="Lista_conatctos"))
        sm.add_widget(AgregarContactoScreen(name="Agregar_contacto"))
        sm.add_widget(EliminarContactoScreen(name="Eliminar_contacto"))
        sm.add_widget(ModificarContactoScreen(name="Modificar_contacto"))
        return sm
    
ContactosApp().run()


