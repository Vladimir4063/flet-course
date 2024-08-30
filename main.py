import flet as ft


def main(page: ft.Page):
    page.title = "App con Vistas Complejas"
    page.window.width = 375
    page.window.height = 844

    content = ft.Column()

    def update_content(index):
        content.controls.clear()
        if index == 0:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Explore Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                )
            )
            content.controls.append(
                ft.Row(
                    controls=[ft.Text("Content 1"), ft.Text("Content 2")],
                    alignment="center",
                )
            )
        elif index == 1:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Commute Screen", size=30, color=ft.colors.BLACK),
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    height=200
                )
            )
            content.controls.append(
                ft.Row(
                    controls=[
                        ft.Text("Commute Content 1"),
                        ft.Text("Commute Content 2"),
                    ],
                    alignment="center",
                )
            )
        elif index == 2:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Bookmark Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                )
            )
            content.controls.append(
                ft.Row(
                    controls=[
                        ft.Text("Bookmark Content 1"),
                        ft.Text("Bookmark Content 2"),
                    ],
                    alignment="center",
                )
            )
        elif index == 3:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Bookmark Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                )
            )
            content.controls.append(
                ft.Row(
                    controls=[
                        ft.Text("Bookmark Content 1"),
                        ft.Text("Bookmark Content 2"),
                    ],
                    alignment="center",
                )
            )
        elif index == 4:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Bookmark Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                )
            )
            content.controls.append(
                ft.Row(
                    controls=[
                        ft.Text("Bookmark Content 1"),
                        ft.Text("Bookmark Content 2"),
                    ],
                    alignment="center",
                )
            )
        page.update()  # Actualizar para reflejar cambios

    # Configurar la barra de navegación
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.AUTO_STORIES, label="Haftará"),
            ft.NavigationBarDestination(icon=ft.icons.BOOK, label="Evangelio"),
            ft.NavigationBarDestination(
                icon=ft.icons.LOCAL_FIRE_DEPARTMENT, label="Aliyá"
            ),
            ft.NavigationBarDestination(icon=ft.icons.CALENDAR_MONTH, label="Fiestas"),
            ft.NavigationBarDestination(icon=ft.icons.MENU, label="Más"),
        ],
        selected_index=2,
        on_change=lambda e: update_content(
            e.control.selected_index
        ),  # Cambiar el contenido según la selección
    )

    # Inicializar el contenido de la pantalla principal
    update_content(2)
    page.add(content)  # Agregar contenedor de contenido
    page.add(nav_bar)  # Agregar barra de navegación


if __name__ == "__main__":
    ft.app(target=main)
