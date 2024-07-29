import flet as ft

def main(page: ft.Page):
    txt_first_name = ft.TextField()
    txt_last_name = ft.TextField()

    # #disables individuality
    txt_first_name.disabled = True


    col_controles = ft.Column(
        controls=[
            txt_first_name,
            txt_last_name
        ]
    )

    # se aplica para todos los hijos
    col_controles.disabled=True

    page.add(col_controles)

ft.app(main)