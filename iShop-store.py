prices = []
items = []
#بداية للمشروع
print("\n*****  Welcome to iShop calculator *****\n")
number_of_items = int(input("How many items are there in your basket today? "))

#if and else
if number_of_items > 0:
    print("\nLet's get to counting them ....\n")
    for i in range(1, number_of_items):
         name = input(f"Please tell me the name of the item number {i}: ")
         items.append(name)
         price = float(input(f"What is the price of {name}\n"))
         prices.append(price)
    choice = input("Would you like to see your entire basket items? ").lower()
    if choice == "yes" or choice == "y":
        print(items)
        see_price = input("Would you like to see how much it'll cost? ").lower()
        if see_price == "yes" or see_price == "y":
            print("\nBuying these items will cost: ")
            print(sum(prices))
        else:
            input("Press enter to exit")
    else:
        input("Press enter to exit")
else: 
    print("Seems like you aren't in the mood for shopping today.")