import os

FILE_NAME = "expenses.txt"


def add_expense():
    print("\nAdd New Expense")

    date = input("Date (DD-MM-YYYY): ")
    category = input("Category: ")
    amount = input("Amount: ")
    description = input("Description: ")

    with open(FILE_NAME, "a") as file:
        file.write(date + "," + category + "," + amount + "," + description + "\n")

    print("Expense saved successfully.\n")


def view_expenses():
    print("\nAll Expenses\n")

    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"{date} | {category} | ₹{amount} | {description}")

    print()


def show_total():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded.\n")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            total += float(parts[2])

    print(f"\nTotal Spending: ₹{total}\n")


def menu():
    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.\n")


menu()