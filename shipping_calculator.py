def shipping_cost():
    number_of_items = int(input("Type in the number of items in the order: "))
    first_item_shipping_cost = 10.95
    subsequent_item_shipping_cost = 2.95
    total_shipping_cost = first_item_shipping_cost + (number_of_items - 1) * subsequent_item_shipping_cost
    print("The total shipping cost for", number_of_items, "is $" + "{:.2f}".format(total_shipping_cost))

shipping_cost()