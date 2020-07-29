import csv

with open("cool_csv.csv") as cool_csv_dict:
  cool_csv_dict = csv.DictReader(cool_csv_dict)
  for row in cool_csv_dict:
    print(row["Cool Fact"])