from main import (
    ninety_nine_bottles, calculate_total_sales,
    calculate_average_sales, filter_to_better_than_average_sales,
)
import pytest

def test_caculate_candy_total_no_data_returns_0():
    sales_totals = {}

    total = calculate_total_sales(sales_totals)

    assert total == 0.0


def test_caculate_candy_total_returns_total_sales():
    sales_totals = {
        "Junior Mints": { "quantity": 100, "price": 2.0 },
        "Red Vines": { "quantity": 50, "price": 2.5 },
        "Candy Corn": { "quantity": 0, "price": 0.5 },
        "Butterfinger": { "quantity": 20, "price": 3.5 },
    }

    total = calculate_total_sales(sales_totals)

    assert total == 395.0


# @pytest.mark.skip("remove this line when working on calculate_average_sales")
def test_caculate_candy_average_no_data_returns_0():
    sales_totals = {}

    average = calculate_average_sales(sales_totals)

    assert average == 0.0


# @pytest.mark.skip("remove this line when working on calculate_average_sales")
def test_caculate_candy_average_returns_average():
    sales_totals = {
        "Junior Mints": { "quantity": 100, "price": 2.0 },
        "Red Vines": { "quantity": 50, "price": 2.5 },
        "Candy Corn": { "quantity": 0, "price": 0.5 },
        "Butterfinger": { "quantity": 20, "price": 3.5 },
    }

    average = calculate_average_sales(sales_totals)

    assert average == 98.75


# @pytest.mark.skip("remove this line when working on filter_to_better_than_average_sales")
def test_filter_to_above_average_sales_no_data_returns_empty_dict():
    sales_totals = {}

    filtered = filter_to_better_than_average_sales(sales_totals)

    assert filtered == {}


# @pytest.mark.skip("remove this line when working on filter_to_better_than_average_sales")
def test_filter_to_above_average_sales_returns_filtered_result():
    sales_totals = {
        "Junior Mints": { "quantity": 100, "price": 2.0 },
        "Red Vines": { "quantity": 50, "price": 2.5 },
        "Candy Corn": { "quantity": 0, "price": 0.5 },
        "Butterfinger": { "quantity": 20, "price": 3.5 },
    }

    filtered = filter_to_better_than_average_sales(sales_totals)

    assert filtered == {
        "Junior Mints": { "quantity": 100, "price": 2.0},
        "Red Vines": { "quantity": 50, "price": 2.5},
    }


# @pytest.mark.skip("remove this line when working on ninety_nine_bottles")
def test_99_bottles_returns_lyrics():
    count = 99
    beverage = "pop"

    lines = ninety_nine_bottles(count, beverage)

    assert len(lines) == 99 * 2

# @pytest.mark.skip("remove this line when working on ninety_nine_bottles")
def test_2_bottles_returns_lyrics():
    count = 2
    beverage = "pop"
    expected_lines = [
        '2 bottles of pop on the wall, 2 bottles of pop',
        'If one of those bottles should happen to fall, 1 bottle of pop on the wall',
        '1 bottle of pop on the wall, 1 bottle of pop',
        'If one of those bottles should happen to fall, 0 bottles of pop on the wall',
    ]

    lines = ninety_nine_bottles(count, beverage)

    assert len(lines) == 4
    assert lines == expected_lines


# @pytest.mark.skip("remove this line when working on ninety_nine_bottles")
def test_1_bottle_returns_lyrics():
    count = 1
    beverage = "pop"
    expected_lines = [
        '1 bottle of pop on the wall, 1 bottle of pop',
        'If one of those bottles should happen to fall, 0 bottles of pop on the wall',
    ]

    lines = ninety_nine_bottles(count, beverage)

    assert len(lines) == 2
    assert lines == expected_lines


# @pytest.mark.skip("remove this line when working on ninety_nine_bottles")
def test_0_bottles_returns_no_lyrics():
    count = 0
    beverage = "pop"

    lines = ninety_nine_bottles(count, beverage)

    assert len(lines) == 0
