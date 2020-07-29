
import csv

with open("books.csv") as books_csv:
  isbn_list = []
  books_reader = csv.DictReader(books_csv, delimiter = '@')
  for row in books_reader:
    isbn_list.append(row['ISBN'])
  print(isbn_list)
