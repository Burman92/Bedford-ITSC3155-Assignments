import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    """write the rest of the codes"""
    on = True
    while on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower().strip()

        if choice == "off":
            on = False

        elif choice == "report":
            sandwich_maker_instance.report()

        elif choice in recipes:
            ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()