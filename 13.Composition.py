
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        print(f"[Engine] Engine created with {self.horsepower} HP")

    def start(self):
        print(f"[Engine] Engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  
        print(f"[Car] Car '{self.brand}' created with engine.")

    def start_car(self):
        print(f"[Car] Starting the {self.brand} car...")
        self.engine.start() 



def main():
   
    engine = Engine(150)

    
    car = Car("Toyota", engine)

 
    car.start_car()


if __name__ == "__main__":
    main()
