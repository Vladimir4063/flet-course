import flet as ft

def main(page:ft.Page):
    lv_textos = ft.ListView(expand=True, spacing=10)
    for i in range(500):
        lv_textos.controls.append(ft.Text(f"Line {i}"))

    page.add(
        lv_textos
    )

ft.app(main)