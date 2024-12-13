from typing import Optional

import flet as ft


class LoginForm(ft.Container):
    def __init__(self, page: Optional[ft.Page] = None) -> None:
        """ Constructor of the LoginForm class. """
        super().__init__()
        self.page = page

    def build(self) -> ft.Container:
        """ 
        Build method of the LoginForm class.
        
        :return: ft.Container
        """
        if self.page is None:
            raise ValueError('Page is required to build the LoginForm.')
        
        file_picker: ft.FilePicker = ft.FilePicker(on_result=LoginForm.on_dialog_result)
        self.page.overlay.append(file_picker)
        self.page.update()
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Iniciar Sesión", size=14),
                    ft.TextField(label="Master Password", password=True),
                    ft.Row(
                        controls=[
                            ft.Dropdown(
                                label='Please select a DB',
                                width=200,
                                options=[
                                    ft.dropdown.Option("Red"),
                                    ft.dropdown.Option("Green"),
                                    ft.dropdown.Option("Blue"),
                                ],
                            ),
                            ft.IconButton(
                                icon=ft.Icons.ADD, 
                                height=50,
                                width=50,
                                tooltip='Add new DB',
                                on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color=ft.Colors.RED_300,
                                height=50,
                                width=50,
                                tooltip='Delete DB',
                                on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text='Login',
                                height=50,
                                width=200,
                                on_click=self.login,
                                icon=ft.Icons.LOGIN_ROUNDED
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=50,
            border_radius=10,
        )
    
    def login(self, e):
        print(self.page)
        print(e.page)
        print("Iniciando sesión...")
        
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print(e)