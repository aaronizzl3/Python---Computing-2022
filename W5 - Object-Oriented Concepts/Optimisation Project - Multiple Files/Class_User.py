class User:
    username = ""
    role = ""
    auth = False

    def __init__(self, username, auth, role="Standard"):
        self.username = username
        self.auth = auth
        self.role = role