items_number = int(input("How many items to you want to add? "))
devices_list = []
prices_list = []
quantity_list = []
unit_list = []
for i in range(items_number):
    name = input(f"Enter the name of a device № {i+1}: ")
    price = int(input(f"Enter the price for a device № {i+1}: "))
    quantity = int(input(f"Enter the quantity sold of a device № {i+1} during a month: "))
    unit = input(f"Enter the unit type of an item № {i+1}: ")
    devices_list.append(name)
    prices_list.append(price)
    quantity_list.append(quantity)
    unit_list.append(unit)
devices_dict = dict(name=devices_list, price=prices_list, quantity=quantity_list, unit=unit_list)
# print(devices_dict)

items_list = []
for key in devices_dict.keys():
    for x in range(len(devices_dict[key])):
        y = {key: devices_dict[key][x]}
        items_list.append(y)

new_items_list = []
for i, j in enumerate(items_list):
    y = items_list[::items_number]
    new_items_list.append(y)
    if i == items_number - 1:
        break
    items_list.pop(0)

new_items_list_2 = []
for a in new_items_list:
    z = {}
    for c in a:
        z.update(c)
    new_items_list_2.append(z)

final_devices_list = []
for d, e in enumerate(new_items_list_2):
    tuple_list = d + 1, e
    final_devices_list.append(tuple_list)
print(final_devices_list)










