my_list = [7, 5, 3, 3, 2]
num = int(input("What is your rating? "))


for i in my_list:
    if num > i:
        index = my_list.index(i)
        my_list.insert(index, num)
        print(my_list)
        break
    elif num == i:
        how_much = my_list.count(num)
        ind = my_list.index(num, how_much)
        my_list.insert(ind + 1, num)
        print(my_list)
        break
    elif my_list[-1] > num > 0:
        my_list.append(num)
        print(my_list)
        break
    if num < 0:
        print("Enter a positive number!")
        break



