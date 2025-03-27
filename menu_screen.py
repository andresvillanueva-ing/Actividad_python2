from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

diseño = """

MDScreen:
    MDLabel:
        text: "Gestion de Contactos"
        haling: "center"
        pos_hint: {"center_y": 0.8}
        
    MDRaisedButton:
        text: "Mostrar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_press: app.root.current = "lista_contacto"
    
    MDRaisedButton:
        text: "Agregar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: app.root.current = "agregar_contacto"
        
    MDRaisedButton:
        text: "modificar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_press: app.root.current = "modificar_contacto"
        
    MDRaisedButton:
        text: "eliminar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: app.root.current = "eliminar_contacto"
"""

class MenuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add.widget(Builder.load_string(diseño))