class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

class CarTesting:
    @staticmethod
    def test_drive(car):
        print(f"Testing the {car.make} {car.model}...")
        print("Accelerating...")
        print("Braking...")
        print("Checking handling...")
        print("Testing complete!")

def main():
    # Create some sample cars
    car1 = Car("Toyota", "Camry", 2021, "Red")
    car2 = Car("Honda", "Civic", 2020, "Blue")

    # Display details of the cars
    print("Car 1 Details:")
    car1.display_details()
    print("\nCar 2 Details:")
    car2.display_details()

    # Test drive a car
    print("\nTesting Car 1:")
    CarTesting.test_drive(car1)

if __name__ == "__main__":
    main()
