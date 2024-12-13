import os


class PathConstants:
    # appdata
    APP_PATH: str = os.path.join(os.getenv('APPDATA', ''), 'rpassword')

    @property
    def DATABASES_PATH(self) -> str:
        """
        Property to get the path to the databases folder.

        :return str: The path to the databases folder.
        """
        path: str = ''

        if os.name == 'nt':
            path = os.path.join(self.APP_PATH, 'databases')
        else:
            path = os.path.join(os.getenv('HOME', ''), '.rpassword', 'databases')

        if not os.path.exists(path):
            os.makedirs(path)

        return path
