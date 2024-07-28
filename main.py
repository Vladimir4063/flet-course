import flet as ft
import time

def main(page: ft.Page):

    # class 18
    # text_home = ft.Text(value="Hola Rey", color="red")
    # page.add(ft.SafeArea(
    #     ft.Text("Hello, Flet!"),
    #     page.controls.append(text_home)
        
    # ))
    # page.update()


    # Se actualiza en tiempo real debido al page.update()
    # lbl_texto = ft.Text()
    # page.add(lbl_texto)
    # for i in range(10):
    #     lbl_texto.value=f"Step: {i}"
    #     page.update()
    #     time.sleep(1)


    # Contenedores que sirven para contener otros controles
    # Generamos y Renderizamos controles mediante un for
    
    lenguajes = ['Python', 'Flet', 'Flutter', 'Hola']
    etiquetas = []

    for i in lenguajes:
        etiquetas.append(ft.Text(i))

    row_datos = ft.Row(controls=etiquetas)


    # forma directa de renderizar controles
    # row_datos = ft.Row(
    #     controls=[
    #         ft.Text('Python'),
    #         ft.Text('Flet'),
    #         ft.Text('Flutter')
    #     ]
    # )

    page.add(row_datos)

ft.app(main)
