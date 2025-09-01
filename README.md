Simple CLI Expense Tracker
================================

A simple, Python-based command-line tool for tracking personal expenses. This project is an implementation of the Task Tracker project from [roadmap.sh](https://roadmap.sh/projects/expense-tracker).


Features
--------
- Add expenses with a description and amount
- Update an expense's description and/or amount
- Delete expenses by ID
- List all expenses in a table view
- Show total spending (all time) or for a specific month
- Persistent storage in a JSON file (expenses.json)


Requirements
------------
- Python 3.10 or higher (for match-case syntax)


Usage
-----
Run the script via Python:

    python expenses.py <command> [options]

(If installed as a CLI, you can also call it as:)

    expense-tracker <command> [options]


Available Commands
------------------

Add an Expense

    Command:
        expense-tracker add --description "<text>" --amount <number>

    Example:
        expense-tracker add --description "Lunch" --amount 12.50

    Output:
        Expense added successfully (ID: 1)


Update an Expense

    Command:
        expense-tracker update --id <id> --description "<text>" --amount <number>

    Examples:
        expense-tracker update --id 1 --description "Lunch with tip"
        expense-tracker update --id 1 --amount 14.25
        expense-tracker update --id 1 --description "Lunch w/ tip" --amount 14.25

    Output (if anything changed):
        Expense updated successfully
    Output (if nothing changed):
        Nothing was updated


Delete an Expense

    Command:
        expense-tracker delete --id <id>

    Example:
        expense-tracker delete --id 2

    Output:
        Expense deleted successfully


List All Expenses

    Command:
        expense-tracker list

    Example:
        expense-tracker list

    Example output:
        ID  Date        Description   Amount
        1   2024-08-06  Lunch         $12.50
        3   2024-08-06  Dinner        $10.00


Show Summary (Totals)

    Command (all-time total):
        expense-tracker summary

    Command (by month, current year):
        expense-tracker summary --month <1-12>

    Examples:
        expense-tracker summary
        expense-tracker summary --month 8

    Example outputs:
        Total expenses: $22.50
        Total expenses for August: $22.50


Notes
-----
- Data is saved to 'expenses.json' automatically.
- Dates are recorded as YYYY-MM-DD using your current system date.
- Months are specified as numbers (1 = January, 12 = December).
- Monthly summaries consider expenses only in the current year.

## License

MIT License. Free to use and modify!
