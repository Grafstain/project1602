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

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == "1":
            attribute = "strength"
        elif choice == "2":
            attribute = "dexterity"
        elif choice == "3":
            attribute = "health"
        elif choice == "4":
            attribute = "wisdom"

        points_to_add = input(f"How many points would you like to add to {attribute}? ")

        try:
            points_to_add = int(points_to_add)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if points_to_add > points_left:
            print(f"You only have {points_left} points left to allocate.")
            continue

        if points_to_add < 0:
            print("You can't allocate negative points.")
            continue

        attributes[attribute] += points_to_add
        points_left -= points_to_add

    print("Allocation complete.")
    print(attributes)


if __name__ == '__main__':
    main()
