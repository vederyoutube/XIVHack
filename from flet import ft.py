import flet as ft
def main(page: ft.Page):
    page.add(
    ft.Row(controls=[
        ft.IconButton(ft.icons.HOME),
        ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
    ])
)