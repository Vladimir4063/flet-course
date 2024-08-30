import flet as ft


def main(page: ft.Page):
    page.title = "App con Múltiples Vistas"
    page.window.width = 375
    page.window.height = 844

    content = ft.Column()

    def update_content(index):
        content.controls.clear()
        if index == 0:
            content.controls.append(ft.Text("Explore Screen"))
        elif index == 1:
            content.controls.append(ft.Text("Commute Screen"))
        elif index == 2:
            content.controls.append(ft.Text("Bookmark Screen"))
        page.update()  # Actualizar para reflejar cambios

    # Configurar barra de navegación
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(
                icon=ft.icons.COMMUTE,
                label="Commute",
            ),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Bookmark"),
        ],
        selected_index=1,
        on_change=lambda e: update_content(
            e.control.selected_index
        ),  # Cambiar la referencia a e.control.selected_index
    )

    # Inicializar el contenido en la pantalla principal
    update_content(1)
    page.add(nav_bar)  # Agregar barra de navegación
    page.add(content)  # Agregar contenedor de contenido


if __name__ == "__main__":
    ft.app(target=main)
