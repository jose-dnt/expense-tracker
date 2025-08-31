import argparse
from datetime import datetime


class Expense:
    all_expenses = []

    def __init__(self, description, amount):

        self.id = self.__generate_id()
        self.date = datetime.today().date()
        self.description = description
        self.amount = amount

        Expense.all_expenses.append(self)

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


print(Expense("a", 2).date)

parser = argparse.ArgumentParser(prog="expense-tracker")
sub_parsers = parser.add_subparsers(dest="command", required=True)

add_parser = sub_parsers.add_parser("add", help="Add an expense")
add_parser.add_argument(
    "--description", required=True, help="Description of the expense"
)
add_parser.add_argument(
    "--amount", type=float, required=True, help="Amount of the expense"
)

list_parser = sub_parsers.add_parser("list", help="List all expenses")

delete_parser = sub_parsers.add_parser("delete", help="Delete an expense")
delete_parser.add_argument(
    "--id", type=int, required=True, help="ID of the expense to delete"
)

summary_parser = sub_parsers.add_parser("summary", help="Show expense summary")
summary_parser.add_argument("--month", type=int, help="Filter summary by month")

args = parser.parse_args()
