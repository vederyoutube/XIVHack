import flet as ft # type: ignore


def login(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN

    global member
    member = 0

    def fab_pressed(e):
        page.add(ft.Text('Участник №'), ft.TextField(label='ФИО участника', width=500), ft.Row(
            [
                ft.ElevatedButton(
                    "Загрузить фото участника",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        file_type='IMAGE'
                    ),
                ),
            ], ft.MainAxisAlignment.CENTER
            )
        , ft.TextField(label='Информация об участнике', width=500,))
        member += 1

    page.floating_action_button = ft.FloatingActionButton(
        text='Добавить участника', on_click=fab_pressed, bgcolor=ft.colors.BLUE_ACCENT
    )

    page.add()
ft.app(target=login,)