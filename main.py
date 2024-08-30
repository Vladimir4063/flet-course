import flet as ft


def main(page: ft.Page):
    page.title = "App con Vistas Complejas"
    page.window.width = 375
    page.window.height = 844

    # aliya_view = ft.ListView(expand=True, spacing=10)
    aliya = """26 Miren, hoy les doy a elegir entre la bendición y la maldición: 27 bendición, si obedecen los mandamientos que yo, el Señor su Dios, hoy les mando obedecer; 28 maldición, si desobedecen los mandamientos del Señor su Dios y se apartan del camino que hoy les mando seguir, y se van tras dioses extraños que jamás han conocido. 29 Cuando el Señor su Dios los haya hecho entrar en la tierra que van a poseer, ustedes bendecirán al monte Guerizín y maldecirán al monte Ebal. 30 Esos montes están al otro lado del Jordán, hacia el oeste, en el territorio de los cananeos que viven en el Arabá, en la vecindad de Guilgal, junto a las encinas de Moré. 31 Ustedes están a punto de cruzar el Jordán y entrar a tomar posesión de la tierra que les da el Señor su Dios. Cuando la hayan tomado y ya estén viviendo allí, 32 cuiden de obedecer todos los estatutos y las leyes que hoy les mando."""

    content = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def update_content(index):
        content.controls.clear()
        if index == 0:
            content.controls.append(
                ft.Container(
                    content=ft.Text("Explore Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.RED
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
            img_moises = ft.Image(
                src=f"assets/moises.png",
                width=250,
                height=250,
                fit=ft.ImageFit.CONTAIN,
            )

            saludo_img = ft.Container(
                content=ft.Image(
                    src=f"assets/moises.png",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center
            )

            saludo_txt = ft.Container(
                content=ft.Text(aliya),
                padding=10
            )

            content.controls.append(
                ft.Container(
                    content=ft.Text("Bookmark Screen", size=30),
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.RED
                )
            )
            content.controls.append(img_moises)
            content.controls.append(saludo_img)
            content.controls.append(saludo_txt)
            
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
