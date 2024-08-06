import flet as ft

def main(page:ft.Page):
    page.title="GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()

    # Genero un objeto que hereda de GridView con su propiedades
    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=0.5,
        spacing=5,
        run_spacing=5,
    )

    page.add(images)

    # Inserto mediante "append" imagenes dentro de cada objeto de "images" y las renderizo
    for i in range(0,60):
        images.controls.append(
            ft.Container(
                ft.Image(
                    src=f"https://picsum.photos/150/150?{i}",
                    fit=ft.ImageFit.NONE,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                ),
                # marco un color para ver el cambio efectuado en child_aspect_ratio=1.5
                bgcolor=ft.colors.AMBER
            )
        )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
