import flet as ft


def main(page: ft.Page):
    page.title = "Mana Del Dia"
    page.window.width = 375
    page.window.height = 844

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Mana Del Dia"), bgcolor=ft.colors.RED),
                    ft.ElevatedButton(
                        "Meditacion", on_click=lambda _: page.go("/meditacion")
                    ),
                    ft.ElevatedButton(
                        "Haftará", on_click=lambda _: page.go("/haftara")
                    ),
                ],
            )
        )
        if page.route == "/meditacion":
            page.views.append(
                ft.View(
                    "/meditacion",
                    [
                        ft.AppBar(title=ft.Text("Meditacion de Aliya"), bgcolor=ft.colors.RED),
                        ft.ElevatedButton(
                            "Volver", on_click=lambda _: page.go("/")
                        ),
                    ],
                )
            )
        if page.route == "/haftara":
            page.views.append(
                ft.View(
                    "/haftara",
                    [
                        ft.AppBar(
                            title=ft.Text("Haftará"), bgcolor=ft.colors.RED
                        ),
                        ft.ElevatedButton("Volver", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
