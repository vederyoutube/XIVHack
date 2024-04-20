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
    items_count=1,
    padding=50,
    # auto_cycle=AutoCycle(duration=1),
    items=[
        Container(
            content=Text(value=str(), size=30),
            height=400,
            width=600,
            bgcolor='red',
            border_radius=15,
            alignment=alignment.center,
        )
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
    page.add(
        ft.Row(controls=[
        ft.ElevatedButton(text="Оценить команду")
    ]
    )
)

ft.app(target=main)