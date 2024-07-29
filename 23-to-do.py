import flet as ft


def main(page: ft.Page):
    def add_clicked_task(e):
        page.add(
            ft.Checkbox(
                label=txt_nueva_tarea.value
            )
        )
    
    txt_nueva_tarea = ft.TextField(
        hint_text="¿Cual tarea desea agregar?", 
        width=300
    )

    btn_agregar_tarea = ft.ElevatedButton("Agregar", icon=ft.icons.ADD ,on_click=add_clicked_task)

    page.add(
        ft.Row([txt_nueva_tarea, btn_agregar_tarea])
    )


ft.app(main)