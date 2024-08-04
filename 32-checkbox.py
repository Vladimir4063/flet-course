import flet as ft

def main(page):
    def checkbox_changed(e):
        output_text.value=(
            f"Tu hicis click en :{todo_check.value}"
        )
        page.update()

    
    output_text = ft.Text()
    todo_check=ft.Checkbox(label="ToDo: Aprendi a usar el checkbox", value=True, on_change=checkbox_changed)
    page.add(
        todo_check,
        output_text
    )
ft.app(main)