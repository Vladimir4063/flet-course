import flet as ft
import requests


def main(page: ft.Page):
    page.title = "App Mana del Día"
    page.window.width = 375
    page.window.height = 810
    page.theme_mode = ft.ThemeMode.LIGHT

    nro_parasha = None
    name_parasha = None
    sign_parasha = None
    info_aliya = None
    aliya = None

    def fetch_api_data():
        data = None
        nonlocal nro_parasha, name_parasha, sign_parasha, info_aliya, aliya
        try:
            response = requests.get("https://manadeldia.vercel.app/api/get/aliya")
            if response.status_code == 200:
                print(data)
                data = response.json()
                # Asignar los datos a las variables
                nro_parasha = data['nroParasha']
                name_parasha = data['nameParasha']
                sign_parasha = data['signParasha']
                info_aliya = f"Aliyá 1, {data['section1']}"
                aliya = data['aliya1']
            else:
                print("Error al obtener datos de la API")
        except Exception as e:
            print(f"Excepción al conectar con la API: {e}")

    nro_parasha = 47
    name_parasha = "Reé"
    sign_parasha = "OBSERVA"
    info_aliya = "Aliyá 1, Deuteronomio 11:26 - 12:10"
    aliya = ("""26 Miren, hoy les doy a elegir entre la bendición y la maldición: 27 bendición, si obedecen los mandamientos que yo, el Señor su Dios, hoy les mando obedecer; 28 maldición, si desobedecen los mandamientos del Señor su Dios y se apartan del camino que hoy les mando seguir, y se van tras dioses extraños que jamás han conocido. 29 Cuando el Señor su Dios los haya hecho entrar en la tierra que van a poseer, ustedes bendecirán al monte Guerizín y maldecirán al monte Ebal. 30 Esos montes están al otro lado del Jordán, hacia el oeste, en el territorio de los cananeos que viven en el Arabá, en la vecindad de Guilgal, junto a las encinas de Moré. 31 Ustedes están a punto de cruzar el Jordán y entrar a tomar posesión de la tierra que les da el Señor su Dios. Cuando la hayan tomado y ya estén viviendo allí, 32 cuiden de obedecer todos los estatutos y las leyes que hoy les mando.""" * 4)

    # call api
    # fetch_api_data()


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
            title_txt = ft.Container(
                content=ft.Text("Mana del Día", size=30, weight=ft.FontWeight.W_300),
                # padding=20,
                alignment=ft.alignment.center,
                # bgcolor=ft.colors.RED,
            )

            # IMAGE
            img_moises = ft.Container(
                content=ft.Image(
                    src="https://manadeldia.vercel.app/static/img/moises.png",
                    width=200,
                    height=200,
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center
            )

            parasha_nro_txt = ft.Container(
                content=ft.Text(
                    f"PARASHA {nro_parasha}",
                    theme_style=ft.TextThemeStyle.BODY_SMALL,
                ),
                alignment=ft.alignment.center
            )

            name_parasha_txt = ft.Container(
                content=ft.Text(
                    f"{name_parasha}",
                    size=40,
                    weight=ft.FontWeight.W_600,
                    italic=True
                ),
                alignment=ft.alignment.center
            )

            sig_parasha_txt = ft.Container(
                content=ft.Text(
                    f"{sign_parasha}",
                    size=50,
                    weight=ft.FontWeight.W_700
                ),
                alignment=ft.alignment.center
            )

            info_parasha_txt = ft.Container(
                content=ft.Text(
                    f"{info_aliya}",
                    size=13,
                    italic=True,
                    color=ft.colors.BLACK87
                ),
                alignment=ft.alignment.center
            )

            aliya_txt = ft.Container(
                content=ft.Text(aliya),
                padding=10,
                bgcolor=ft.colors.AMBER_50,
                border_radius=10
            )

            # content.controls.append(title_txt)
            content.controls.append(img_moises)
            content.controls.append(parasha_nro_txt)
            content.controls.append(name_parasha_txt)
            content.controls.append(sig_parasha_txt)
            content.controls.append(info_parasha_txt)
            content.controls.append(aliya_txt)
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
        indicator_color=ft.colors.AMBER_100,
        on_change=lambda e: update_content(
            e.control.selected_index
        ),  # Cambiar el contenido según la selección
        bgcolor=ft.colors.AMBER_200,
    )

    # Start content home view
    update_content(2)
    page.bgcolor=ft.colors.AMBER_100 #color page
    page.add(content)  # Add container
    page.add(nav_bar)  # Add navigation

if __name__ == "__main__":
    ft.app(target=main)
