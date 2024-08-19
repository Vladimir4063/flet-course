import flet as ft


def main(page:ft.Page):
    page.title = "Ejemplo de Rutas"

    print("Ruta Inicial", page.route)

    def route_change(event):
        print("Ruta cambiada:", event.route)
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet App")),
                    ft.ElevatedButton("Go to settings", on_click=open_settings),
                ],
            )
        )
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.AppBar(title=ft.Text("Settings"), bgcolor=ft.colors.RED),
                        ft.Text("Settings!", style="bodyMedium"),
                        ft.ElevatedButton(
                            "Go to mail settings", on_click=open_mail_settings
                        )
                    ]
                )
            )
        if page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings/mail",
                    [
                        ft.AppBar(
                            title=ft.Text("Mail Settings"),
                            bgcolor=ft.colors.BLUE
                        ),
                        ft.Text("Mail settings!")
                    ]
                )
            )
        page.update()
    
    def view_pop(event):
        print("View pop:", event.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(event):
        page.go("/settings/mail")

    def open_settings(event):
        page.go("/settings")

    page.go(page.route)

ft.app(main)