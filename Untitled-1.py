import flet as ft

def main(page: ft.Page):
    page.title = "Containers - clickable and not"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("ТЕКСТ"),
                    margin=0, #Положение по вертикали
                    padding=0, #Горизонтали
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                ),]))
ft.app(target=main,)