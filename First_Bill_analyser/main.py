from analyzer import load_data
from analyzer import total_expense
from analyzer import category_summary
from analyzer import max_expense

import pandas as pd
import os

from report import print_report


def main():

    data = load_data("bill.csv")

    total = total_expense(data)

    category_data = category_summary(data)

    max_item, max_amount = max_expense(data)

    print_report(total, category_data, max_item, max_amount)


def load_data(file_name):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    main()