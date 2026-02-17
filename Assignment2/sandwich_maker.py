class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Not enough resources for {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']}")
        print(f"Ham: {self.machine_resources['ham']}")
        print(f"Cheese: {self.machine_resources['cheese']}")
