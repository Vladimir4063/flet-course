import flet as ft
from flet import Page,Row


def main(page:Page):
    page.title = "Ejemplo de Drag&Drop"

    def drag_accept(event):
        source = page.get_control(event.src_id)
        source.content.content.value = "0"
        event.control.content.content.value = "1"

        page.update()

    page.add(
        Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    # content_when_dragging: Permite cambiar el elemento de arrastre
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    # content_feedback: Permite estilizar el elemento de arrastre
                    content_feedback=ft.Text("Hola", color=ft.colors.DEEP_PURPLE_400),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)
