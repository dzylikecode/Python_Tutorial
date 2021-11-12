def make_pizza(size, *toppings):
    """describe the process of making a pizza"""

    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
