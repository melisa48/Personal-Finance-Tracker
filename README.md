# Personal Finance Tracker
- This project is a simple personal finance tracker written in Python. 
- It helps users to track their income, expenses, and budget. 
- The program provides a text-based interface to add income and expenses, and to view a summary of financial transactions.

## Features
- Add income with amount, category, date, and description.
- Add expenses with amount, category, date, and description.
- View a summary of all incomes and expenses.
- Calculate the total income, total expenses, and current balance.

## Project Structure
finance_tracker_project/
├── finance_tracker.py
└── transaction.py

- `transaction.py`: Contains the `Transaction` class which represents a single transaction (income or expense).
- `finance_tracker.py`: Contains the `FinanceTracker` class which manages all transactions, and the main program logic for user interaction.

## Getting Started
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository or download the source code files.
   ```bash
   git clone https://github.com/your-username/finance_tracker_project.git
   
2. Navigate to the project directory.
   cd finance_tracker_project

## Usage
1. Run the finance_tracker.py script.
   python finance_tracker.py
2. Follow the on-screen prompts to add income, add expenses, view summary, or exit the program.

## Example Interaction
Personal Finance Tracker
1. Add Income
2. Add Expense
3. View Summary
4. Exit
Choose an option: 1
Enter income amount: 500
Enter income category: Salary
Enter date (YYYY-MM-DD): 2024-05-27
Enter description (optional): May Salary

Personal Finance Tracker
1. Add Income
2. Add Expense
3. View Summary
4. Exit
Choose an option: 3
Income:
2024-05-27 | Salary | 500.0 | May Salary

Expenses:
Total Income: 500.0
Total Expenses: 0.0
Balance: 500.0

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

