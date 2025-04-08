from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivy.app import App

class AgregarContactoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))

        
        titulo = MDLabel(
            text="Agregar Contacto",
            halign="center",
            pos_hint={"center_y": 0.5},
            font_style="H5"
        )
        layout.add_widget(titulo)

        # Campo nombre
        self.input_nombre = MDTextField(
            hint_text="Nombre"
        )
        layout.add_widget(self.input_nombre)

        # Campo teléfono
        self.input_telefono = MDTextField(
            hint_text="Teléfono",
            input_filter="int"
        )
        # Limita a 10 dígitos
        self.input_telefono.bind(text=self.validar_longitud_telefono)
        layout.add_widget(self.input_telefono)

        # Campo correo
        self.input_correo = MDTextField(
            hint_text="Correo"
        )
        layout.add_widget(self.input_correo)

        # Botón guardar
        boton_guardar = MDRaisedButton(
            text="Guardar",
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.guardar_contacto()
        )
        layout.add_widget(boton_guardar)

        # Botón volver
        boton_volver = MDRaisedButton(
            text="Volver",
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.volver_menu()
        )
        layout.add_widget(boton_volver)

        self.add_widget(layout)

    def on_pre_enter(self):
        self.input_nombre.text = ""
        self.input_telefono.text = ""
        self.input_correo.text = ""

    def validar_longitud_telefono(self, instance, value):
        if len(value) > 10:
            instance.text = value[:10]  # Solo deja los primeros 10 caracteres

    def guardar_contacto(self):
        nombre = self.input_nombre.text.strip()
        telefono = self.input_telefono.text.strip()
        correo = self.input_correo.text.strip()

        if nombre and telefono and correo:
            app = App.get_running_app()
            app.Agregar_contacto(nombre, telefono, correo)
        else:
            print("Todos los campos son obligatorios.")

    def volver_menu(self):
        App.get_running_app().root.current = "menu"
