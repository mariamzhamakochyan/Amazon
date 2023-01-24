class User:
    def __init__(self, role, username, mail):
        self.role = role
        self.username = username
        self.mail = mail
        self.user_buyer = []
        self.user_saler = []

    def add(self, role, username, mail):
        user_info = {self.username:self.mail}
        if self.role == "B":
            self.user_buyer.append(user_info)
        else:
            self.user_saler.append(user_info)




