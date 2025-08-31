import argparse
import calendar
from datetime import datetime


class Expense:
    all_expenses = []

    def __init__(self, description, amount):
        self.id = self.__generate_id()
        self.date = datetime.today().date()
        self.description = description
        self.amount = amount

        Expense.all_expenses.append(self)

    def __getitem__(self, key):
        return getattr(self, key)

    def __generate_id(self):
        id = 1
        id_is_available = False

        while not id_is_available:
            for expense in Expense.all_expenses:
                if expense.id == id:
                    break
            else:
                id_is_available = True
                break
            id += 1

        return id


def get_month_name(month_number):
    if 1 <= month_number <= 12:
        return calendar.month_name[month_number]
    else:
        print("Invalid month!")


def find_expense_by_id(id):
    if not isinstance(id, int) or id < 1:
        print("Invalid ID!")
        return

    for expense in Expense.all_expenses:
        if expense.id == id:
            return expense
    else:
        print("There is no expense with this ID!")
        return None


def filter_expenses_by_month(month):
    filtered_expenses = list(
        filter(
            lambda expense: (
                expense.date.year == datetime.today().year
                and expense.date.month == month
            ),
            Expense.all_expenses,
        )
    )
    return filtered_expenses


def add_expense(description, amount):
    expense = Expense(description, amount)
    print(f"Expense added successfully (ID: {expense.id})")
    return expense


def update_expense(id, description, amount):
    expense = find_expense_by_id(id)
    if not expense:
        return
    expense.description = description if description else expense.description
    expense.amount = amount if amount else expense.amount
    print("Expense updated successfully")
    return expense


def list_expenses():
    if len(Expense.all_expenses) < 1:
        print("There are no expenses!")
        return

    def get_column_size(attribute):
        max_size = 1
        for expense in Expense.all_expenses:
            size = len(str(expense[attribute]))
            if size > max_size:
                max_size = size
        return max_size

    id_column = f"{'ID':<{get_column_size('id')}}"
    date_column = f"{'Date':<{get_column_size('date')}}"
    description_column = f"{'Description':<{get_column_size('description')}}"
    amount_column = f"{'Amount':<{get_column_size('amount')}}"

    print(f"{id_column}  {date_column}  {description_column}  {amount_column}")

    for expense in Expense.all_expenses:
        print(
            f"{expense.id:<{len(id_column)}}  {str(expense.date):<{len(date_column)}}  {expense.description:<{len(description_column)}}  ${expense.amount:<.2f}"
        )


def delete_expense(id):
    expense = find_expense_by_id(id)
    if not expense:
        return
    Expense.all_expenses.remove(expense)
    print("Expense deleted successfully")
    return expense


def show_summary(month):
    if month:
        if month < 1 or month > 12:
            return

        filtered_expenses = filter_expenses_by_month(month)

        total_expenses = 0

        for expense in filtered_expenses:
            total_expenses += expense.amount

        print(f"Total expenses for {get_month_name(month)}: ${total_expenses:.2f}")

    else:
        all_expenses = Expense.all_expenses

        total_expenses = 0

        for expense in all_expenses:
            total_expenses += expense.amount

        print(f"Total expenses: ${total_expenses:.2f}")


def main():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    sub_parsers = parser.add_subparsers(dest="command", required=True)

    add_parser = sub_parsers.add_parser("add", help="Add an expense")
    add_parser.add_argument(
        "--description", required=True, help="Description of the expense"
    )
    add_parser.add_argument(
        "--amount", type=float, required=True, help="Amount of the expense"
    )

    update_parser = sub_parsers.add_parser("update", help="Update an expense")
    update_parser.add_argument(
        "--id", type=int, required=True, help="ID of the expense to update"
    )
    update_parser.add_argument(
        "--description", required=True, help="Description of the expense"
    )
    update_parser.add_argument(
        "--amount", type=float, required=True, help="Amount of the expense"
    )

    sub_parsers.add_parser("list", help="List all expenses")

    delete_parser = sub_parsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument(
        "--id", type=int, required=True, help="ID of the expense to delete"
    )

    summary_parser = sub_parsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=int, help="Filter summary by month")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_expense(args.description, args.amount)
        case "update":
            update_expense(args.id, args.description, args.amount)
        case "list":
            list_expenses()
        case "delete":
            delete_expense(args.id)
        case "summary":
            show_summary(args.month)


if __name__ == "__main__":
    main()
