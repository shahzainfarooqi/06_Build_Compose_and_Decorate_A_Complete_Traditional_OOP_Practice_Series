
class Person:
    def __init__(self, name):
        self.name = name
        print(f"[Person] Initialized Person with name: {self.name}")

    def display_info(self):
        print(f"Name: {self.name}")



class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print(f"[Teacher] Initialized Teacher with subject: {self.subject}")

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")



def main():
    print("Creating a Person:")
    person = Person("Alice")
    person.display_info()

    print("\nCreating a Teacher:")
    teacher = Teacher("Bob", "Mathematics")
    teacher.display_info()


if __name__ == "__main__":
    main()
