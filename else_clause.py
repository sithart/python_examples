# INITIAL CODE
from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    # print(app)
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')

apps_data[0].append('free_or_not')
print(apps_data[0])
print(apps_data[1:6])
