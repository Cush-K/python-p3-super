class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name
    
    def log_in(self):
        print("User.login() called")
        self.logged_in = True