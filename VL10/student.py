class Person:
    def __init__(self, name: str):
        print("In constructor Person")
        self.name = name

    def greet(self):
        print(f"Servus, ich bin {self.name}")

class Student(Person):
    def __init__(self, name, matnr):
        print("In constructor Student")
        super().__init__(name)
        self.matnr = matnr


s = Student("John", "1234")
s.greet()