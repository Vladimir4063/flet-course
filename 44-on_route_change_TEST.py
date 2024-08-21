import flet as ft

def main(page: ft.Page):
    page.title = "Test"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet App Home"), bgcolor=ft.colors.BLUE_400),
                    ft.ElevatedButton("Ir a Meditación", on_click=lambda _: page.go("/meditacion"))
                ]
            )
        )
        if page.route == "/meditacion":
            page.views.append(
                ft.View(
                    "/meditacion",
                    [
                        ft.AppBar(title=ft.Text("Meditacion"), bgcolor=ft.colors.AMBER_900),
                        ft.ElevatedButton("Volver", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

ft.app(main)