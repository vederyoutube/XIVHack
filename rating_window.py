import flet as ft
from flet import *

def main(page):
    page.add(
        ft.IconButton(ft.icons.HOME)
             )
    page.add(
        ft.Text("Оцените комнаду:") 
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("Дизайн:"),
        ft.Slider(min=0, max=5, divisions=5, label="{value}",width=500)
        )
    page.add(
        ft.Text("Юзабилити:"),
        ft.Slider(min=0, max=5, divisions=5, label="{value}",width=500)
        )
    page.add(
        ft.Text("Верстка:"),
        ft.Slider(min=0, max=5, divisions=5, label="{value}",width=500)
        )
    page.add(
        ft.Text("Реализация:"),
        ft.Slider(min=0, max=5, divisions=5, label="{value}",width=500)
        )
    page.add(
        ft.ElevatedButton(text="Отправить")
    )
    

    

ft.app(target=main)