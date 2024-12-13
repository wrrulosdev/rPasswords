import flet as ft

from views.login import LoginView
from states.login import LoginState
from states.databases import DatabasesState


def initialize_states() -> None:
    """ Initialize the states of the app. """
    login_state: LoginState = LoginState()
    databases_state: DatabasesState = DatabasesState()
    

def main(page: ft.Page) -> None:
    """
    Main function of the app.

    :param ft.Page page: Flet page object.
    """
    page.title = 'rPasswords'
    page.window.width = 455
    page.window.height = 600
    # dark mode
    page.theme_mode = ft.ThemeMode.LIGHT
    
    if not LoginState().logged:
        LoginView(page)


initialize_states()
ft.app(main)
