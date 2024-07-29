import flet as ft
from flet import Ref

def main(page: ft.Page):
    page.window.width=350

    # creo el input para capturar el valor
    txt_first_name = Ref[ft.TextField]()
    txt_last_name = Ref[ft.TextField]()

    # genero una columna para renderizar los controles
    col_controles = Ref[ft.Column]()

    # creo la funcion para generar la lista y limpiar los input añadiendo un focus al finalizar
    def saludar_clicked(event):
        col_controles.current.controls.append(
            ft.Text(
                f"Hola, {txt_first_name.current.value} {txt_last_name.current.value}!!"
            )
        )

        txt_first_name.current.value = ""
        txt_last_name.current.value = ""

        page.update()
        txt_first_name.focus() 

    # genero un boton que active la funcion para generar la lista "saluda"
    btn_saludar = ft.ElevatedButton('Saludar', on_click=saludar_clicked)

    # renderizo todos los controles en pantalla
    page.add(
        ft.TextField(ref=txt_first_name,label="Nombre"),
        ft.TextField(ref=txt_last_name,label="Apellido"),
        btn_saludar,
        ft.Column(col_controles)
    )

ft.app(main)
