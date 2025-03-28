from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from DataBase import ContactoDB

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        
        MDLabel:
            text: "Agregar Contacto"
            halign: "center"
            pos_hint: {"center_y": 0.5}
        
        MDTextField:
            id: nombre
            hint_text: "nombre"
        
        MDTextField:
            id: telefono
            hint_text: "telefono"
            input_filter: "int"
        
        MDTextField:
            id: correo
            hint_text: "correo"
        
        MDRaisedButton:
            text: "guardar"
            pos_hint: {"center_x": 0.5}
            on_release: app.Agregar_contacto(nombre.text, telefono.text, correo.text)

        MDRaisedButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press: app.root.current = "menu"
'''

class AgregarContactoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Builder.load_string(KV))
