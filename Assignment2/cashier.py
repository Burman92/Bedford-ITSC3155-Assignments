class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * .50
        quarters = int(input("how many quarters?: ")) * .25
        nickles = int(input("how many nickles?: ")) * .05

        total = float(large_dollars + half_dollars + quarters + nickles)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins < cost:
            print(f"Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is the ${change} in change")
        return True