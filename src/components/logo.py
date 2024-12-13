import flet as ft


class Logo(ft.Container):
    def __init__(self) -> None:
        """ Constructor of the Logo class. """
        super().__init__()

    def build(self) -> ft.Container:
        """
        Build method of the Logo class.

        :return ft.Container: Logo container with the image.
        """
        return ft.Container(
            content=ft.Image(
                src="src/assets/logo.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            ),
            width=120,
            height=120,
            padding=20,
            border=ft.border.all(1, color=ft.Colors.BLACK87),
            border_radius=100,
        )
