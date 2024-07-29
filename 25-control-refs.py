import flet as ft

def main(page: ft.Page):
    page.window.width=350

    # creo el input para capturar el valor 
    txt_first_name = ft.TextField(label="Nombre", autofocus=True)

    txt_last_name = ft.TextField(label="Apellido")

    # genero una columna para renderizar los controles
    col_controles = ft.Column()

    # creo la funcion para generar la lista y limpiar los input añadiendo un focus al finalizar
    def saludar_clicked(event):
        col_controles.controls.append(ft.Text(f"Hola, {txt_first_name.value} {txt_last_name.value}!!"))
        txt_first_name.value = ""
        txt_last_name.value = ""
        
        page.update()
        txt_first_name.focus() 

    # genero un boton que active la funcion para generar la lista "saluda"
    btn_saludar = ft.ElevatedButton('Saludar', on_click=saludar_clicked)

    # renderizo todos los controles en pantalla
    page.add(
        txt_first_name,
        txt_last_name,
        btn_saludar,
        col_controles
    )

ft.app(main)
