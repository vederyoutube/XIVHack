import flet as ft # type: ignore

def login(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def button_clicked(e):
        page.route = "/register"
        page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [

                ],
            )
        )
        
    a = ft.Text ('Вход в личный кабинет', size=32,)
    с = ft.Text (size=32,)
    login = ft.TextField(label="Логин", width=500)
    password = ft.TextField(label="Пароль", password=True, hint_text='***********',width=500)
    d = ft.Text (size=32,)
    b = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Вход", size=32),
                ],
            ), 
        )
    )
    register = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        value="Регистрация", size=14, color='grey'
                    ),
                ],alignment=ft.MainAxisAlignment.END,
            ),
        ) ,
        on_click=button_clicked)
    
    page.add(a, с, login, password, d, b, register)

ft.app(target=login, view=ft.AppView.WEB_BROWSER)
