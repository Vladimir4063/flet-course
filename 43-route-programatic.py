import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Ruta Inicial: {page.route}"))

    def route_change(event: ft.RouteChangeEvent):
        # la propiedad event va a mostrar el nombre del cambio de "route"
        page.add(ft.Text(f"Nueva ruta: {event.route}"))

    def go_store(event):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)