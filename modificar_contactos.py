from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
MDScreen:
    MDLabel:
        text: "Modificar Contacto"
        halign: "center"
        pos_hint: {"center_y": 0.8}

    MDRaisedButton:
        text: "Volver"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        on_press: app.root.current = "menu"
'''

class ModificarContactoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Builder.load_string(KV))
