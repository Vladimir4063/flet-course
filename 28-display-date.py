import flet as ft
from flet import Page
def main(page:ft.Page):
    page.title="Title page windows"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    num = ft.Text(
        value=0,
        text_align="center",
        width=100
    )

    def minus_click(e):
        num.value = int(num.value) - 1
        page.update()

    def plus_click(e):
        num.value = int(num.value) + 1
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                num,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)
