import flet as ft
from flet import Page,Row


def main(page:Page):
    page.title = "Ejemplo de Drag&Drop"

    def drag_accept(event):
        source = page.get_control(event.src_id)
        source.content.content.value = "0"
        event.control.content.content.value = "1"

        page.update()

    def drag_will_accept(event):
        event.control.content.border = ft.border.all(
            3, ft.colors.BLACK45 if event.data == "true" else ft.colors.RED
        )
        event.control.update()

    def drag_leave(event):
        event.control.content.border = None
        event.control.update()

    page.add(
        Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=100,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    # content_when_dragging: Permite cambiar el elemento de arrastre
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_900,
                        border_radius=100,
                    ),
                    # content_feedback: Permite estilizar el elemento de arrastre
                    content_feedback=ft.Text("1", color=ft.colors.DEEP_PURPLE_400),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=100,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave
                ),
            ]
        )
    )

ft.app(target=main)
