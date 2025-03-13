def calculate_total_sales(sales_totals):
    total_sales = 0

    for data in sales_totals.values():
        total_sales += data["quantity"] * data["price"]

    return total_sales

def calculate_average_sales(sales_totals):
    if len(sales_totals) == 0:
        return 0
    
    return calculate_total_sales(sales_totals) / len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    filtered = {}

    if not sales_totals:
        return filtered
    
    average_sales = calculate_average_sales(sales_totals)

    for candy, data in sales_totals.items():
        sales = data["quantity"] * data["price"]
        if sales > average_sales:
            filtered[candy] = data
    
    return filtered
    
def ninety_nine_bottles(count, beverage):
    lines = []

    while count > 0:
        if count == 1:
            lines.append(f'{count} bottle of {beverage} on the wall, {count} bottle of {beverage}')
        else:
            lines.append(f'{count} bottles of {beverage} on the wall, {count} bottles of {beverage}')
        if count - 1 == 1:
            lines.append(f'If one of those bottles should happen to fall, {count - 1} bottle of {beverage} on the wall')
        else:
            lines.append(f'If one of those bottles should happen to fall, {count - 1} bottles of {beverage} on the wall')

        count -= 1

    return lines
