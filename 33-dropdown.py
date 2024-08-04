import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        txt_output.value = f"Selecionaste el color: {color_dropdown.value}"
        page.update()

    txt_output = ft.Text()
    btn_submit = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(value="Red",
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue")
        ]
    )

    page.add(
        color_dropdown,
        btn_submit,
        txt_output
    )

ft.app(main)