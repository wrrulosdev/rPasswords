from typing import Optional


class LoginState:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoginState, cls).__new__(cls, *args, **kwargs)
            
        return cls._instance
    
    def __init__(self):
        self.logged: bool = False
        self.master_password: Optional[str] = None
