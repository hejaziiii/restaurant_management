
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
    return random.choice(["single", "pair"])

def generate_customers():
    customers = []
    for i in range(2000):
        name = random_string(random.randint(5, 12))
        money = random_money()
        customer_type = random_type()
        customers.append(Customer(name, money, customer_type))
    return customers

def simulate(customers, restaurant):
    for i in range(6):
        for customer in customers:
            if random.random() < 0.01 and customer.type == "single":
                restaurant.place_customer(customer)
            elif random.random() < 0.02 and customer.type == "pair":
                restaurant.place_customer(customer)
    return restaurant

def main():
    restaurant = Restaurant(10000)
    customers = generate_customers()
    for i in range(3):
        restaurant = simulate(customers, restaurant)
        print("Month: ", i+1)
        print("Restaurant balance: ", restaurant.balance)
        print("Restaurant seats: ", restaurant.seats)
        print("")
    print("Total balance: ", restaurant.balance)

main()


