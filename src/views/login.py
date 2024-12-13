import flet as ft

from components.auth.form import LoginForm
from components.logo import Logo


class LoginView:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = 'rPassowrds - Authentication'
        self.page.add(
            ft.Column(
                controls=[
                    Logo().build(),
                    LoginForm(page=self.page).build(),
                    ft.Text(value='github.com/wrrulosdev/rPasswords', size=12, color=ft.Colors.GREY_500)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
        self.page.update()
