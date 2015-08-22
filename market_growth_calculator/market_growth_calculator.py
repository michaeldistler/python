# Market Growth Rate Calculator
# (Change in Market size = (Current MS - Original MS)/
# Original MS) x 100 = Market Growth Rate (%)


def remove_commas(number):
    # Remove commas and convert to an integer
    commas_removed_number = number.replace(",", "")
    return int(commas_removed_number)


def market_growth(current_ms, original_ms):
    return growth_calculator(current_ms, original_ms)


def product_sales_growth(current_sr, original_sr):
    return growth_calculator(current_sr, original_sr)


def growth_calculator(current, original):
    # Remove any commas, returns an integer
    current_int = remove_commas(current)
    original_int = remove_commas(original)
    # Change in market/product size
    change = current_int - original_int
    # Calculate market/product growth
    growth_rate = (change / original_int) * 100
    return growth_rate


x = "1,000"
removed = remove_commas(x)
print removed


x = growth_calculator("1000", "2000")
print x

original_ms = raw_input("Original Market Share: ")
current_ms = raw_input("Current Market Share: ")

original_sr = raw_input("Original Sales Revenue: ")
current_sr = raw_input("Current Sales Revenue: ")

market_growth = "Total Market Growth: " + str(
    int(market_growth(current_ms, original_ms)
        )) + "%"
product_sales_growth = "Total Sales Growth: " + str(
    int(product_sales_growth(current_sr, original_sr)
        )) + "%"

print(market_growth + "\n" + product_sales_growth)
