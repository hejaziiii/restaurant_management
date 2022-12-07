
import random
import string



class Customer:
    def __init__(self, name, money, customer_type):
        self.name = name
        self.money = money
        self.type = customer_type

    def pay(self, restaurant):
        restaurant.balance += self.money


class Restaurant:
    def __init__(self, seats):
        self.seats = seats
        self.balance = 0

    def pay_costs(self, costs):
        self.balance -= costs

    def get_money(self, customer):
        self.balance += customer.money

    def place_customer(self, customer):
        if self.seats > 0:
            self.seats -= 1
            customer.pay(self)
        else:
            print("No seats available")

def random_string(string_length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def random_money():
    return random.randint(50, 100)

def random_type():
    return random.choice(["single", "pair", "family"])


def main():
    restaurant = Restaurant(5000000)
    customers = []
    for i in range(2000):
        customers.append(Customer(random_string(), random_money(), random_type()))

    for i in range(3):
      for d in range(30):
        for j in range(6):
          # store minimum number of busy seats
            min_busy_seats = restaurant.seats
            for k in range(24):
                if random.random() < 0.01 and restaurant.seats > 0:
                    restaurant.place_customer(customers.pop())
                if restaurant.seats < min_busy_seats:
                    min_busy_seats = restaurant.seats
            print("\nDaily statistic:")
            # Print daily statistic: minimum number of busy seats
            print("Minimum number of busy seats:", min_busy_seats)
            # Print daily statistic: account state of the restaurant
            print("Restaurant balance:", restaurant.balance)
            for customer in customers:
                if random.random() < 0.01 and customer.type == "single":
                    restaurant.place_customer(customer)
                elif random.random() < 0.02 and customer.type == "pair":
                    restaurant.place_customer(customer)
                elif random.random() < 0.03 and customer.type == "family":
                    restaurant.place_customer(customer)
      print("\nMonthly statistic:")
      print("Restaurant balance:", restaurant.balance)
      print("Restaurant seats:", restaurant.seats)
      print("")

    # Print total statistic: account state of the restauran
    print("\nTotal statistic:")
    print("Total balance:", restaurant.balance)


main()
