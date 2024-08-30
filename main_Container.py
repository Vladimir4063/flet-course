import flet as ft

def main(page: ft.Page):
    page.title = "App Example"
    page.window.width = 375
    page.window.height = 844
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def min_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    page.update()
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Hola"),
                    bgcolor=ft.colors.CYAN_ACCENT_700,
                    # margin=10,
                    padding=10,
                    border_radius=10,
                    width=80,
                    height=80,
                    alignment=ft.alignment.center,
                    # on_click=min_click
                ),
                # txt_number,
                ft.Container(
                    content=ft.Text(
                        "Click +"),
                    bgcolor=ft.colors.GREEN,
                    padding=10,
                    # margin=10,
                    border_radius=10,
                    width=80,
                    height=80,
                    alignment=ft.alignment.center,
                    on_click=plus_click
                ),
                ft.Container(
                    content=ft.Text("Click efect"),
                    # margin=10,
                    padding=10,
                    bgcolor=ft.colors.BROWN,
                    border_radius=10,
                    width=80,
                    height=80,
                    alignment=ft.alignment.center,
                    ink=True,
                    on_click=lambda e: print("Hola")
                ),
                ft.Container(
                    content=ft.Text("Click transparence"),
                    # bgcolor=ft.colors.RED,
                    # margin=10,
                    padding=10,
                    border_radius=10,
                    width=80,
                    height=80,
                    alignment=ft.alignment.center,
                    ink=True,
                    on_click= lambda e: print("Transparence")
                )

            ]
        )
    )
ft.app(main)
