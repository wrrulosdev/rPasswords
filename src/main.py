import flet as ft

from views.login import LoginView


def main(page: ft.Page) -> None:
    """
    Main function of the app.

    :param ft.Page page: Flet page object.
    """
    page.title = 'rPasswords'
    page.window.width = 400
    page.window.height = 600
    # dark mode
    page.theme_mode = ft.ThemeMode.LIGHT
    LoginView(page)


ft.app(main)
