from shop.order import Order

# GENERATOR ZAMÓWIEŃ
number_of_orders = int(input("Enter the number of orders to generate: "))

def run_example():
    orders = []
    for _ in range(number_of_orders):
        orders.append(Order.order_generator())

    orders.sort(key=lambda order: order.total_price)
    for order in orders:
        print(order)


if __name__ == "__main__":
    run_example()
