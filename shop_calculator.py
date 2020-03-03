"""
Program to calculate the total amount of items purchased
with a 10% discount if the item total is greater than $100

"""


def main():
    total = 0
    print('Please enter how many items you purchased!!')
    items_purchased = int(input('Number of items:'))
    while items_purchased <= 0:
        print("Invalid number of items!")
        items_purchased = int(input('Number of items:'))
    for item in range(1, items_purchased + 1):
        cost = float(input("Price of item:"))
        total = total + cost
    if total > 100:
        total = total - (total/10)
    print("Total price of", items_purchased, "items is $", '%.2f' % total)


main()
