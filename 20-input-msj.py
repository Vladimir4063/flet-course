import flet as ft


def saludar(event):
    print("Hola")
    

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your Name"),
            ft.TextField(label="Years"),
            ft.ElevatedButton(text="Say my name:", on_click=saludar)

        ])
    )

ft.app(main)