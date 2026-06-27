# ==========================================
# PERSONAL EXPENSE TRACKER (FINAL FIXED)
# ==========================================

expenses = [
    {
        "description": "Breakfast",
        "category": "Food",
        "amount": 120.0,
        "date": "01-07-2025"
    }
]
# ==============================
# USER INPUT BUDGET (FIX)
# ==============================
while True:
    try:
        budget = float(input("Enter Monthly Budget (Rs.): "))
        if budget <= 0:
            print("Budget must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input! Enter number only.")


# ==============================
# ADD EXPENSE
# ==============================
def add_expense():
    try:
        desc = input("Enter Description: ")
        cat = input("Enter Category: ").title()
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Amount must be positive")
            return

        date = input("Enter Date (DD-MM-YYYY): ")

        expenses.append({
            "description": desc,
            "category": cat,
            "amount": amount,
            "date": date
        })

        print("Expense Added Successfully!")

    except ValueError:
        print("Invalid amount!")


# ==============================
# VIEW ALL
# ==============================
def view_expenses():
    print("\n===== ALL EXPENSES =====")

    print(f"{'No':<5}{'Desc':<20}{'Category':<15}{'Amount':<10}{'Date'}")
    print("-" * 70)

    for i, e in enumerate(expenses, 1):
        print(f"{i:<5}{e['description']:<20}{e['category']:<15}{e['amount']:<10.2f}{e['date']}")


# ==============================
# CATEGORY SUMMARY
# ==============================
def category_summary():
    summary = {}

    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n===== CATEGORY SUMMARY =====")

    for k, v in summary.items():
        print(k, "-> Rs.", round(v, 2))


# ==============================
# TOP CATEGORY
# ==============================
def top_category():
    summary = {}

    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    top = max(summary, key=summary.get)
    return top, summary[top]


# ==============================
# BUDGET REPORT
# ==============================
def budget_report():
    total = sum(e["amount"] for e in expenses)
    remaining = budget - total
    percent = (total / budget) * 100

    print("\n===== BUDGET REPORT =====")
    print("Total Spent :", total)
    print("Budget      :", budget)
    print("Remaining   :", remaining)
    print("Used %      :", round(percent, 2))

    if percent >= 100:
        print("⚠ Budget Exceeded!")
    elif percent >= 80:
        print("⚠ Warning: 80% Budget Used!")

    t = top_category()
    print("Top Category:", t[0], "(", t[1], ")")


# ==============================
# FILTER CATEGORY
# ==============================
def filter_category():
    cat = input("Enter Category: ").title()

    found = False

    for e in expenses:
        if e["category"] == cat:
            print(e["description"], e["amount"], e["date"])
            found = True

    if not found:
        print("No records found")


# ==============================
# MOST EXPENSIVE
# ==============================
def most_expensive():
    high = max(expenses, key=lambda x: x["amount"])

    print("\nMost Expensive Expense")
    print(high)


# ==============================
# AVERAGE DAILY
# ==============================
def avg_daily():
    dates = set(e["date"] for e in expenses)
    total = sum(e["amount"] for e in expenses)

    print("Average Daily Spending:", round(total / len(dates), 2))


# ==============================
# SAVE FILE
# ==============================
def save_file():
    with open("expenses.txt", "w") as f:
        for i, e in enumerate(expenses, 1):
            f.write(f"{i}. {e['description']} | {e['category']} | {e['amount']} | {e['date']}\n")

    print("Saved to expenses.txt")


# ==============================
# MENU
# ==============================
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("Budget:", budget)

    print("\n1.Add Expense")
    print("2.View All")
    print("3.Category Summary")
    print("4.Budget Report")
    print("5.Filter Category")
    print("6.Most Expensive")
    print("7.Average Daily")
    print("8.Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            category_summary()
        elif choice == 4:
            budget_report()
        elif choice == 5:
            filter_category()
        elif choice == 6:
            most_expensive()
        elif choice == 7:
            avg_daily()
        elif choice == 8:
            save_file()
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Enter valid number")