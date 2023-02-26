# allocate attributions points fir character
def main():
    attributes = {'strength': 0, 'dexterity': 0, 'health': 0, 'wisdom': 0}
    points_left = 30

    while points_left > 0:
        print(f"You have {points_left} points left to allocate.")
        print("Which attribute would you like to add points to?")
        print("1. Strength")
        print("2. Dexterity")
        print("3. Health")
        print("4. Wisdom")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            attribute = "strength"
        elif choice == "2":
            attribute = "dexterity"
        elif choice == "3":
            attribute = "health"
        elif choice == "4":
            attribute = "wisdom"
        else:
            print("Invalid choice. Please try again.")
            continue

        points_to_add = input("How many points would you like to add to this attribute? ")

        try:
            points_to_add = int(points_to_add)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if points_to_add <= points_left:
            attributes[attribute] += points_to_add
            points_left -= points_to_add
        else:
            print("You don't have enough points left. Please try again.")
main()

