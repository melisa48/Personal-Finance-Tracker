from datetime import datetime

class Transaction:
    def __init__(self, amount, category, date, description=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"

class FinanceTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []
    
    def add_income(self, amount, category, date, description=""):
        income = Transaction(amount, category, date, description)
        self.incomes.append(income)
    
    def add_expense(self, amount, category, date, description=""):
        expense = Transaction(amount, category, date, description)
        self.expenses.append(expense)
    
    def get_total_income(self):
        return sum(income.amount for income in self.incomes)
    
    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()
    
    def display_transactions(self, transactions):
        for transaction in transactions:
            print(transaction)
    
    def display_summary(self):
        print("Income:")
        self.display_transactions(self.incomes)
        print("\nExpenses:")
        self.display_transactions(self.expenses)
        print(f"\nTotal Income: {self.get_total_income()}")
        print(f"Total Expenses: {self.get_total_expenses()}")
        print(f"Balance: {self.get_balance()}")

def main():
    tracker = FinanceTracker()
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")
            tracker.add_income(amount, category, datetime.strptime(date, '%Y-%m-%d'), description)
        
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, datetime.strptime(date, '%Y-%m-%d'), description)
        
        elif choice == '3':
            tracker.display_summary()
        
        elif choice == '4':
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
