class User:
    def __init__(self, first_name, last_name, age):#self 可以用任意的名称代替，但是最好使用self
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0 

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()} and the age is {self.age}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User, Privileges):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


    
User1 = Admin("John", "Doe", 30) 
User1.privileges.show_privileges()