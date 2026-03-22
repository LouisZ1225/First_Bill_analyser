import pandas as pd


def load_data(file_path):
    """读取账单数据"""
    data = pd.read_csv(file_path)
    return data


def total_expense(data):
    """计算总消费"""
    return data["amount"].sum()


def category_summary(data):
    """分类统计"""
    return data.groupby("category")["amount"].sum()


def max_expense(data):
    """最大消费"""
    row = data.loc[data["amount"].idxmax()]
    return row["item"], row["amount"]