import flet as ft

def main(page:ft.Page):
    page.add(ft.Text(f"Ruta incial: {page.route}"))

    def route_change(event: ft.RouteChangeEvent):
        page.add(ft.Text(f"Nueva ruta: {event.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(main, view=ft.WEB_BROWSER)