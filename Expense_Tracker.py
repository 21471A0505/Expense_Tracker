import datetime
import json

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("===== List of Expenses =====")
        for expense in self.expenses:
            print(f"Date: {expense.date.strftime('%Y-%m-%d')}, Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}")
        print("============================")

    def calculate_total_expenses(self, start_date=None, end_date=None):
        total_expenses = sum(expense.amount for expense in self.expenses if self._is_within_time_frame(expense.date, start_date, end_date))
        return total_expenses

    def generate_monthly_report(self, month, year):
        monthly_expenses = {}
        for expense in self.expenses:
            if expense.date.month == month and expense.date.year == year:
                if expense.category in monthly_expenses:
                    monthly_expenses[expense.category] += expense.amount
                else:
                    monthly_expenses[expense.category] = expense.amount
        return monthly_expenses

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            json.dump([expense.__dict__ for expense in self.expenses], file, default=str)

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.expenses = [Expense(datetime.datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S'), 
                                        expense['amount'], expense['category'], expense['description']) for expense in data]
            print("Expenses loaded successfully.")
        except FileNotFoundError:
            print("No expense data found.")

    def _is_within_time_frame(self, date, start_date, end_date):
        if start_date and date < start_date:
            return False
        if end_date and date > end_date:
            return False
        return True

def get_date(prompt):
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt + ": "))
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

def main():
    expense_tracker = ExpenseTracker()

    # Load expenses from a file (if available)
    filename = "expenses.json"
    expense_tracker.load_expenses(filename)

    while True:
        print("\n===== Expense Tracker Application =====")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter Expense Details:")
            date = get_date("Enter Expense Date")
            amount = get_amount("Enter Expense Amount")
            category = input("Enter Expense Category: ")
            description = input("Enter Expense Description: ")
            expense_tracker.add_expense(Expense(date, amount, category, description))
            print("Expense added successfully.")
        elif choice == "2":
            expense_tracker.list_expenses()
        elif choice == "3":
            total_expenses = expense_tracker.calculate_total_expenses()
            print(f"\nTotal Expenses: ${total_expenses:.2f}")
        elif choice == "4":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            monthly_report = expense_tracker.generate_monthly_report(month, year)
            print("\n===== Monthly Expense Report =====")
            for category, amount in monthly_report.items():
                print(f"{category}: ${amount:.2f}")
            print("===================================")
        elif choice == "5":
            expense_tracker.save_expenses(filename)
            print("Expenses saved successfully.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
