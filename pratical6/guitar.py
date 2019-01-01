def main():
    guitars = []
    print("My guitars!")
    # guitar_name = input("Name: ")
    # while guitar_name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar_to_add = Guitar (name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(guitar_to_add, "added.")
    #     name = input("Name:")
    Gibson = Guitar ("Gibson L-5 CES", 1922, 16035.40)
    Line = Guitar ("Line 6 JTV-59", 2010, 1512.9)
    guitars.append(Gibson)
    guitars.append(Line)
    if guitars:
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar{0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f} {2}".format(i+1, guitar, vintage_string))
    # print(guitars)
main()
