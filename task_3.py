months = ["January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
seasons = {"January": "Winter", "February": "Winter", "March": "Spring", "April": "Spring", "May": "Spring",
           "June": "Summer", "July": "Summer", "August": "Summer", "September": "Autumn", "October": "Autumn",
           "November": "Autumn", "December": "Winter"}
y = []
for i, j in enumerate(months):
    x = i + 1, j
    y.append(x)
    z = dict(y)

month_asked = int(input("Enter any month number "))
print(seasons[z[month_asked]])



