import flet as ft
from flet import *
from fletcarousel import BasicAnimatedHorizontalCarousel,HintLine,AutoCycle,BasicHorizontalCarousel


def main(page: ft.Page):
    page.add(
    ft.Row(controls=[
        ft.IconButton(ft.icons.HOME),
        ft.IconButton(ft.icons.ACCOUNT_CIRCLE)
    ])
)
    page.add(
    BasicHorizontalCarousel(
    page=page,
    items_count=3,
    # auto_cycle=AutoCycle(duration=1),
    items=[
        Container(
            content=Text(value=str(i), size=20),
            height=200,
            width=300,
            bgcolor='red',
            border_radius=15,
            alignment=alignment.center,
        ) for i in range(10)
    ],
    buttons=[
        FloatingActionButton(
            icon=icons.NAVIGATE_BEFORE,
            bgcolor='#1f2127'
        ),
        FloatingActionButton(
            icon=icons.NAVIGATE_NEXT,
            bgcolor='#1f2127'
        )
    ],
    vertical_alignment=CrossAxisAlignment.CENTER,
    items_alignment=MainAxisAlignment.CENTER
)
)

ft.app(target=main)