def get_income():
    income = float(input("Enter your total monthly income: $"))
    return income

def get_expenses():
    print("\nEnter your monthly expenses:")
    rent = float(input("Rent: $"))
    food = float(input("Food: $"))
    transport = float(input("Transport: $"))
    other = float(input("Other: $"))
    total = rent + food + transport + other
    return total

def calculate_balance(income, expenses):
    return income - expenses

def show_summary(income, expenses, balance):
    print("\n=== Budget Summary ===")
    print(f"Income:   ${income:.2f}")
    print(f"Expenses: ${expenses:.2f}")
    print(f"Balance:  ${balance:.2f}")
    if balance < 0:
        print("⚠️ You are over budget!")
    elif balance == 0:
        print("⚠️ You’ve spent your entire budget.")
    else:
        print("✅ You are within your budget!")

def main():
    print("💰 Welcome to Your Budget Tracker 💰")
    income = get_income()
    expenses = get_expenses()
    balance = calculate_balance(income, expenses)
    show_summary(income, expenses, balance)

if __name__ == "__main__":
    main()
