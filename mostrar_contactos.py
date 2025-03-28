from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.label import MDLabel
from DataBase import ContactoDB

KV = '''
<ListaContactosScreen>:
    name: "lista_contactos"

    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "Lista de Contactos"
            halign: "center"
            theme_text_color: "Primary"

        MDScrollView:
            MDBoxLayout:
                id: container 
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height

        MDRaisedButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = "menu"
'''

class ListaContactosScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)  # Cargar el KV dentro de la clase

        self.db = ContactoDB()  # Conectar con la base de datos

    def on_kv_post(self, base_widget):  
        """Este método se ejecuta después de cargar el KV para asegurar que los ids existen."""
        self.actualizar_lista()

    def actualizar_lista(self):
        if not hasattr(self, 'ids') or 'container' not in self.ids:
            print("Error: No se encontró el ID 'container'")
            return
        
        container = self.ids.container
        container.clear_widgets()  

        contactos = self.db.mostrar()

        if not contactos:
            mensaje = MDLabel(
                text="No hay contactos registrados",
                halign="center",
                theme_text_color="Secondary"
            )
            container.add_widget(mensaje)
        else:
            for contacto in contactos:
                nombre = contacto[1] 
                item = OneLineListItem(text=nombre)
                container.add_widget(item)
