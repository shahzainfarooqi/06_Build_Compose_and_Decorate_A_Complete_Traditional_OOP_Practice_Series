
class Student:
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks     
        print(f"[Student] Student object created for: {self.name}")

    def display(self):
     
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")



def main():
    print("Creating Student...")
    student1 = Student("Shahzain", 85)

    print("\nDisplaying Student Info:")
    student1.display()


if __name__ == "__main__":
    main()
