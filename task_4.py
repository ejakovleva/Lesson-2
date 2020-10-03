sentence = input("What do you like to do in your free time? ")
y = sentence.split()

for i, j in enumerate(y):
    print(i + 1, j[:10])
