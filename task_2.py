products = input("What do you need to buy today in a grocery store? ")
products_list = []
if ", " not in products:
    print("Please separate your list by a comma and a tab!")
elif "and" in products:
    print("Please separate your list by a comma and a tab and don't use 'and'!")
elif "  " in products:
    print("Please separate your list by a comma and 1 tab!")
else:
    products_list = products.split(", ")

    x = products_list[::2]
    y = products_list[1::2]

    z = 1
    for i in x:
        y.insert(z, i)
        z = z + 2
    print(y)
