class User:
    
    def init(self, id: int, email: str, password: str, is_active: bool = True):
        self.id = id
        self.email = email
        self.password = password
        self.is_active = is_active

    def deactivate(self):
        self.is_active = False 