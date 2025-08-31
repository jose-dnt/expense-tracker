import argparse

parser = argparse.ArgumentParser(prog="expense-tracker")
sub_parsers = parser.add_subparsers(dest="command", required=True)

add_parser = sub_parsers.add_parser("add", help="Add an expense")
add_parser.add_argument("--description", required=True, help="Description of the expense")
add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

list_parser = sub_parsers.add_parser("list", help="List all expenses")

delete_parser = sub_parsers.add_parser("delete", help="Delete an expense")
delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

summary_parser = sub_parsers.add_parser("summary", help="Show expense summary")
summary_parser.add_argument("--month", type=int, help="Filter summary by month")

args = parser.parse_args()
