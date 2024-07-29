import flet as ft



    

def main(page: ft.Page):

    txt_nombre = ft.TextField(label="Digite su nombre")

    lbl_saludo = ft.Text() #genera variable vacia con Text

    def saludar(event):
        # asigno al value de la variable el valor del input (TextField)
        lbl_saludo.value = f"Hola {txt_nombre.value}"
        page.update()

    page.add(
        ft.Row(controls=[
            # ft.TextField(label="Your Name"),
            # ft.TextField(label="Years"),
            txt_nombre,
            ft.ElevatedButton(text="Say my name:", on_click=saludar),
            lbl_saludo

        ])
    )

ft.app(main)