import flet as ft
import os
import mmsql_lib as sql
mn = None
mn1 = None
count = 0
members = [[],[]]
def register(page: ft.Page):
    page.scroll = 'AUTO'

    def pick_files_result(e: ft.FilePickerResultEvent):
        for file in e.files:
            if os.path.getsize(file.path) > 2 * 1024 * 1024: 
                selected_files.value = 'Файл слишком большой!'
                selected_files.update()
                return
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        page.update()

    def validate_email(email):
        if "@" in email and "." in email:
            return None
        else:
            return "Введите корректный адрес электронной почты"

    def validate_password(password):
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
        page.banner = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text(e),
            actions=[
                ft.TextButton("OK", on_click=close_banner),
            ],)
        page.banner.open = True
        page.update()

    def validate_fields(team_name, email, login, password):
        if not team_name:
            return "Пожалуйста, введите название команды"
        if not email:
            return "Пожалуйста, введите адрес электронной почты"
        if not login:
            return "Пожалуйста, введите логин"
        if not password:
            return "Пожалуйста, введите пароль"
        return None
        
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def add_member(_):
        global count
        count += 1
        member_label = ft.Text(f'Участник №{count}')
        member_name = ft.TextField(label='ФИО Участника', width=500)
        member_photo = ft.Row(
            [
                ft.ElevatedButton(
                    "Загрузить фото участника",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=['pdf', 'png', 'jpeg']
                    ),
                ),
                selected_files,
            ], ft.MainAxisAlignment.CENTER
        )    
        member_info = ft.TextField(label='Краткая информация', width=500, max_length=255)
        member_button = ft.Row(
            [
                ft.ElevatedButton(
                    f'Подтвердить Участника №{count}', on_click=member_check(member_name, member_info)
                )
            ]
        )
        page.add(member_label, member_name, member_photo, member_info, member_button)
        page.update()

    def member_check(name, info):
        name1 = name.value
        info1 = info.value
        print(name, info)

    def on_register_click(_):
        team_name_value = team_name.value
        email_value = email.value
        login_value = login.value
        password_value = password.value

        field_error = validate_fields(team_name_value, email_value, login_value, password_value)
        email_error = validate_email(email_value)
        password_error = validate_password(password_value)

        error_messages = []

        if email_error:
            error_messages.append("Ошибка в адресе электронной почты: " + email_error)
        if password_error:
            error_messages.append("Ошибка в пароле: " + password_error)
        if field_error:
            error_messages.append("Заполните все поля" )

        if error_messages:
            error_text = "\n".join(error_messages)
            show_banner(error_text)
        else: 
            print(email)
            members[0].append(mn)
            members[1].append(mn1)
            print(mn,mn1)
            print(members)
            sql.team_reg(team_name_value, email_value, login_value, password_value, members)
            

    register = ft.Text('Регистрация', size=32)
    void1 = ft.Text(size=42)
    team_name = ft.TextField(label='Название команды', width=500, max_length=20)

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

    email = ft.TextField(label='Электронная почта', width=500, hint_text='example@example.org')
    login = ft.TextField(label="Логин", width=500)
    password = ft.TextField(label="Пароль", password=True, hint_text='***********', width=500,)

    b = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="Регистрация", size=32),
                ],
            ), 
        ),
        on_click=on_register_click  
    ) 

    add_member_button = ft.ElevatedButton("Добавить участника", on_click=add_member)

    page.add(register, void1, team_name, team_banner,  add_member_button, email, login, password, b)
    page.update()

ft.app(target=register,) #view=ft.AppView.WEB_BROWSER)
