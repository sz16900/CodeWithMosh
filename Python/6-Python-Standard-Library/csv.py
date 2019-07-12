import csv

# writing
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id, product_id, price"])
    writer.writerow([1000, 1, 100])
    writer.writerow([1002, 2, 1000])

# reading

with open("data2.csv", "w") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
