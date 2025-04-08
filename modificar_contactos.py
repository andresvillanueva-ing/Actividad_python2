from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from DataBase import ContactoDB


class ModificarContactoScreen(MDScreen):
    def __init__(self, db, **kwargs):
        super().__init__(**kwargs)
        self.db = db
        self.ContactoDB = db
        self.contacto_id = None
        
        #Interfaz de usuario de la pantalla modificar contacto.
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.input_buscar = MDTextField(hint_text="Nombre del contacto a modificar")
        self.btn_buscar = MDRaisedButton(text="Buscar", on_release=self.buscar_contacto)
        
        self.input_nombre = MDTextField(hint_text="Nuevo nombre")
        self.input_telefono = MDTextField(hint_text="Nuevo teléfono")
        self.input_correo = MDTextField(hint_text="Nuevo correo")
        
        self.btn_guardar = MDRaisedButton(text="Guardar cambios", on_release=self.confirmar_guardado)
        self.btn_volver = MDFlatButton(text="Volver", on_release=self.volver_al_menu)
        
        layout.add_widget(self.input_buscar)
        layout.add_widget(self.btn_buscar)
        layout.add_widget(self.input_nombre)
        layout.add_widget(self.input_telefono)
        layout.add_widget(self.input_correo)
        layout.add_widget(self.btn_guardar)
        layout.add_widget(self.btn_volver)
        
        self.add_widget(layout)
        self.dialog = None
    
    #Limpiar campos de texto
    def on_pre_enter(self):
        self.input_nombre.text = ""
        self.input_telefono.text = ""
        self.input_correo.text = ""

    #Buscar contacto por el nombre
    def buscar_contacto(self, instance):
        nombre_buscar = self.input_buscar.text.strip()
        contacto = self.db.buscar_por_nombre(nombre_buscar)
        if contacto:
            self.contacto_id, nombre, telefono, correo = contacto
            self.input_nombre.text = nombre
            self.input_telefono.text = str(telefono)
            self.input_correo.text = correo
        else:
            self.mostrar_dialogo("Error", "No se encontró el contacto")
    
    #Confirmar guardar los datos modificados.
    def confirmar_guardado(self, instance):
        if self.contacto_id:
            self.dialog = MDDialog(
                title="Confirmar cambios",
                text="¿Seguro que deseas modificar este contacto?",
                buttons=[
                    MDFlatButton(text="Cancelar", on_release=lambda x: self.dialog.dismiss()),
                    MDRaisedButton(text="Aceptar", on_release=self.guardar_cambios)
                ]
            )
            self.dialog.open()
        else:
            self.mostrar_dialogo("Error", "Primero busca un contacto")
    
    #Guardar los datos modificados.
    def guardar_cambios(self, instance):
        nombre = self.input_nombre.text.strip()
        telefono = self.input_telefono.text.strip()
        correo = self.input_correo.text.strip()
        
        if nombre and telefono and correo:
            self.db.actualizar(self.contacto_id, nombre, telefono, correo)
            self.mostrar_dialogo("Éxito", "Contacto actualizado correctamente")
            self.dialog.dismiss()
        else:
            self.mostrar_dialogo("Error", "Todos los campos deben estar llenos")

    #Cargar los datos del contacto
    def cargar_datos(self, contacto):
        self.contacto_id = contacto["id"]
        self.input_nombre.text = contacto["nombre"]
        self.input_telefono.text = str(contacto["telefono"])
        self.input_correo.text = contacto["correo"]

    #Modificar los datos del contacto cargado.
    def modificar_contacto(self, contacto_dict):
        self.manager.get_screen("modificar_contacto").cargar_datos(contacto_dict)
        self.manager.current = "modificar_contacto"


    def volver_al_menu(self, instance):
        self.manager.current = "menu"

    def mostrar_dialogo(self, titulo, mensaje):
        dialogo = MDDialog(title=titulo, text=mensaje, buttons=[MDFlatButton(text="Aceptar", on_release=lambda x: dialogo.dismiss())])
        dialogo.open()
