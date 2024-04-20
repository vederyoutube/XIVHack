import flet as ft
import os
import re

def register(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        for file in e.files:
            if os.path.getsize(file.path) > 2 * 1024 * 1024:  # Проверяем размер файла
                selected_files.value = 'Файл слишком большой!'
                selected_files.update()
                return
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
    
    def validate_email(email):
        # Проверка корректности ввода адреса электронной почты
        if "@" in email and "." in email:
            return None
        else:
            return "Введите корректный адрес электронной почты"

    def validate_password(password):
        # Проверка пароля на соответствие требованиям
        if len(password) < 8:
            return "Пароль должен содержать не менее 8 символов"
        if not any(char.isupper() for char in password):
            return "Пароль должен содержать хотя бы одну заглавную букву"
        if not any(char.islower() for char in password):
            return "Пароль должен содержать хотя бы одну строчную букву"
        if not any(char.isdigit() for char in password):
            return "Пароль должен содержать хотя бы одну цифру"
        if not any(char in "!@#$%^&*()-_+=<>?/:;.,~" for char in password):
            return "Пароль должен содержать хотя бы один специальный символ"
        return None
    
    def close_banner(e):
        page.banner.open = False
        page.update()



    def show_banner(e):
        page.banner.open = True
        page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_register_click(_):
        # Обработчик нажатия кнопки "Регистрация"
        email_value = email.value
        password_value = password.value

        # Проверка данных
        email_error = validate_email(email_value)
        password_error = validate_password(password_value)

        # Список для хранения сообщений об ошибках
        error_messages = []

        if email_error:
            # Если есть ошибка в адресе электронной почты, добавляем сообщение об ошибке в список
            error_messages.append("Ошибка в адресе электронной почты: " + email_error)
        if password_error:
            # Если есть ошибка в пароле, добавляем сообщение об ошибке в список
            error_messages.append("Ошибка в пароле: " + password_error)

        if error_messages:
            # Если есть хотя бы одна ошибка, объединяем все сообщения об ошибках в одно
            error_message = "\n".join(error_messages)
            # Выводим объединенное сообщение об ошибках в консоль
            page.banner = ft.Banner(
                bgcolor=ft.colors.AMBER_100,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    error_message
                ),
                actions=[
                    ft.TextButton("OK", on_click=close_banner),
        \
                ],
            )

    register = ft.Text('Регистрация', size=32)
    void1 = ft.Text(size=42)
    team_name = ft.TextField(label='Название команды', width=500)
    
    # Поле для загрузки баннера команды
    team_banner = ft.Row(
            [
                ft.ElevatedButton(
                    "Загрузить баннер команды",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=['pdf', 'png', 'jpeg']
                    ),
                ),
                selected_files,
            ], ft.MainAxisAlignment.CENTER
        )
    
    email = ft.TextField(label='Электронная почта', width=500, hint_text='example@ex.com')
    login = ft.TextField(label="Логин", width=500)
    password = ft.TextField(label="Пароль", password=True, hint_text='***********', width=500)

    # Кнопка "Регистрация"
    b = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Регистрация", size=32),
                ],
            ), 
        ),
        on_click=on_register_click  # Устанавливаем обработчик нажатия кнопки
    )

    page.add(register, void1, team_name, team_banner, email, login, password, b)

ft.app(target=register)
