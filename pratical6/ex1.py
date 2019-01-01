from pratical6.car import Car
MENU = """Menu:
d) drive
r) refuel
q) quit"""

def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice != "d" and choice != "r":
            print("Invalid choice")
        elif choice =="d":
            distance = int(input("How many km do you wish to drive? "))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            else:
                if distance > car.fuel:
                    car.drive(distance)
                    print("The car drove", str(car.drive_distance)+"km and ran out of fuel.")
                else:
                    car.drive(distance)
                    print("The car drove", str(car.drive_distance)+"km.")
        elif choice == "r":
            amount = int(input("How many units of fuel do you want to add to the car? "))
            while amount < 0:
                print("Fuel amount must be >=0")
                amount = int(input("How many units of fuel do you want to add to the car? "))
            else:
                car.add_fuel(amount)
                print("Added", str(amount),"units of fuel.")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    else:
        print("Good bye", name+"'s driver.")


main()