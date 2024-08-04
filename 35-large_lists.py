import flet as ft

def main(page:ft.Page):

    page.window.height=600
    page.window.width=340
    
    for i in range(500):
        page.controls.append(ft.Text(f"Line {i}"))
        page.scroll="always"
        page.update()

ft.app(main)