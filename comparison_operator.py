from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
data = []
n_apps_more_9 = 0
n_apps_less_9 = 0
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price > 9:
        n_apps_more_9 = n_apps_more_9 + 1
        data.append(rating)
    if price <= 9:
        n_apps_less_9 = n_apps_less_9 + 1

avg_rating = sum(data)/len(data)
print(len(data))
print(n_apps_more_9)
