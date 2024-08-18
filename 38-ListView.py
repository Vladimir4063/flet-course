import flet as ft

def main(page: ft.Page):
    lv_texts = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv_texts)

    for i in range(5100):
        lv_texts.controls.append(ft.Text(f"Line {i}"))
        if i % 500 == 0:
            page.update()
    page.update()


ft.app(target=main)