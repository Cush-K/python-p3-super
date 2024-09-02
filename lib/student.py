from user import User

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade
    
    def log_in(self):
        super().log_in()
        self.in_class = True
        
        
james = Student("James", 10)
james.log_in()
print(james.__dict__)