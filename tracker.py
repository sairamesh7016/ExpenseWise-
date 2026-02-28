import os

FILE_NAME = "expenses.txt"
BUDGET_FILE = "budget.txt"


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


def category_summary():
    summary = {}

    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded.\n")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")

            amount = float(amount)

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\nSpending by Category:\n")

    for category, total in summary.items():
        print(f"{category}: ₹{total}")

    print()


# -------- NEW FEATURE --------

def set_budget():
    print("\nSet Monthly Budget")

    budget = input("Enter your monthly budget: ")

    try:
        budget = float(budget)
    except ValueError:
        print("Invalid number.\n")
        return

    with open(BUDGET_FILE, "w") as file:
        file.write(str(budget))

    print("Budget saved successfully.\n")


def check_budget():
    if not os.path.exists(BUDGET_FILE):
        print("\nNo budget set. Please set a budget first.\n")
        return

    with open(BUDGET_FILE, "r") as file:
        budget = float(file.read())

    total = 0

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                total += float(parts[2])

    remaining = budget - total

    print("\n====== Budget Status ======")
    print(f"Budget: ₹{budget}")
    print(f"Spent: ₹{total}")
    print(f"Remaining: ₹{remaining}")

    percent = (total / budget) * 100 if budget > 0 else 0

    if percent >= 100:
        print(f"❌ Budget exceeded by ₹{abs(remaining)}")

    elif percent >= 80:
        print(f"⚠ Warning: {percent:.0f}% of budget used")

    print()


# -------- MENU --------

def menu():
    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Category Summary")
        print("5. Set Monthly Budget")
        print("6. Check Budget Status")
        print("7. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            set_budget()

        elif choice == "6":
            check_budget()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.\n")


menu()
