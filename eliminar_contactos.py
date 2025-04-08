from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.clock import Clock
from DataBase import ContactoDB

class EliminarContactoScreen(MDScreen):         
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = ContactoDB()
        self.dialog = None
        self.create_ui()

    def create_ui(self):
        layout = MDBoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        toolbar = MDTopAppBar(title="Eliminar Contacto")
        layout.add_widget(toolbar)
        
        self.busqueda_field = MDTextField(hint_text="Ingrese el nombre", mode="rectangle")
        btn_buscar = MDRaisedButton(text="Buscar", pos_hint={"center_x": 0.5}, on_release=self.buscar_contacto)
        
        layout.add_widget(self.busqueda_field)
        layout.add_widget(btn_buscar)
        
        self.nombre_label = MDLabel(text="Nombre: ", theme_text_color="Primary")
        self.telefono_label = MDLabel(text="Teléfono: ", theme_text_color="Secondary")
        self.correo_label = MDLabel(text="Correo: ", theme_text_color="Secondary")
        
        layout.add_widget(self.nombre_label)
        layout.add_widget(self.telefono_label)
        layout.add_widget(self.correo_label)
        
        btn_eliminar = MDRaisedButton(
            text="Eliminar", pos_hint={"center_x": 0.5}, on_release=self.confirmar_eliminar
        )
        btn_volver = MDRaisedButton(
            text="Volver", pos_hint={"center_x": 0.5}, on_release=self.volver_menu
        )
        
        layout.add_widget(btn_eliminar)
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)



    def mostrar_mensaje(self, mensaje):
        if not hasattr(self, 'mensaje_dialog') or self.mensaje_dialog is None:
            self.mensaje_dialog = MDDialog(
                title="Aviso",
                text=mensaje,
                buttons=[
                    MDRaisedButton(text="OK", on_release=lambda x: self.mensaje_dialog.dismiss()),
                ],
            )
        else:
            self.mensaje_dialog.text = mensaje
        self.mensaje_dialog.open()

    def buscar_contacto(self, instance):
        nombre_buscar = self.busqueda_field.text.strip()
        contacto = self.db.buscar_por_nombre(nombre_buscar)
    
        if contacto:
            self.contacto_id = contacto[0]
            self.nombre_label.text = f"Nombre: {contacto[1]}"
            self.telefono_label.text = f"Teléfono: {contacto[2]}"
            self.correo_label.text = f"Correo: {contacto[3]}"
        else:
            self.mostrar_mensaje("Contacto no encontrado")

    def confirmar_eliminar(self, instance):
        if hasattr(self, 'contacto_id'):
            self.dialog = MDDialog(
                title="Eliminar Contacto",
                text="¿Está seguro de que desea eliminar este contacto?",
                buttons=[
                    MDRaisedButton(text="Cancelar", on_release=lambda x: self.dialog.dismiss()),
                    MDRaisedButton(text="Eliminar", on_release=lambda x: self.eliminar_contacto())
                ],
            )
            self.dialog.open()
        else:
            self.mostrar_mensaje("Primero busque un contacto")

    def eliminar_contacto(self):
        self.db.eliminar(self.contacto_id)
        self.dialog.dismiss()
        self.mostrar_mensaje("Contacto eliminado correctamente")
        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', "menu"), 1)

    def volver_menu(self, instance):
        self.manager.current = "menu"
