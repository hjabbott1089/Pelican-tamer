"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = int(input('Enter the sales amount: $'))
    while sales >= 0:
        bonus_one = int(sales/10)
        bonus_two = int(sales/100*15)
        if sales in range(1, 1000):
            print(int(bonus_one))
        else:
            print(int(bonus_two))
        sales = int(input('Enter the sales amount: $'))


main()
