def print_report(total, category_data, max_item, max_amount):

    print("\n====== 消费报告 ======")

    print(f"\n总消费: {total} 元")

    print("\n分类消费:")

    for category, amount in category_data.items():
        print(f"{category}: {amount}")

    print("\n最大消费:")
    print(max_item, max_amount)