
class Dog:
    def __init__(self, name, breed):
        self.name = name    
        self.breed = breed    
        print(f"[Dog] Created Dog: {self.name}, Breed: {self.breed}")

    def bark(self):
      
        print(f"{self.name} says: Woof! Woof!")



def main():
    print("Creating two dogs:") 
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "German Shepherd")

    print("\nMaking the dogs bark:")
    dog1.bark()
    dog2.bark()


if __name__ == "__main__":
    main()
