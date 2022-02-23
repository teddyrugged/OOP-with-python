# The entry point of your application

from data.data import resources, FORMAT


class Printer:
    resources, FORMAT = resources, FORMAT

    def __init__(self):
        self.print_mode = input("Enter A for coloured and B for grayscale: ").lower
        self.num_pages = int(input("Enter number of pages? "))
        self.coloured_price = self.num_pages* FORMAT["coloured"]["price"]
        self.greyscale_price = self.num_pages * FORMAT["greyscale"]["price"]

    def avaliable_resources(self):
        required_ink = FORMAT["coloured"]["materials"]["ink"] * self.num_pages
        if self.print_mode == "B":
            required_ink = FORMAT["greyscale"]["materials"]["ink"] * self.num_pages

        if resources["ink"] < required_ink and resources["paper"] < self.num_pages:
            print(f"Not enough resource to print")
            return False

        if resources["ink"] < required_ink:
            print(f"Not enough ink to print")
            return False

        if resources["paper"] < self.num_pages:
            print(f"Not enough paper to print")
            return False

        return True

    @property
    def cost(self):
        amount = self.coloured_price
        if self.print_mode == "B":
            amount = self.greyscale_price
        print(f"Printing cost is ${amount}.\nEnter Coins:--> ")
        penny = int(input("How many pennies are you paying? ")) * 0.01
        nickel = int(input("How many nickels are you paying? ")) * 0.05
        dime = int(input("How many dimes are you paying? ")) * 0.1
        quarter = int(input("How many quarters are you paying? ")) * 0.25

        total_coin = penny + nickel + dime + quarter

        return total_coin

    
    def validated_amount(self,cost):
        amount = self.coloured_price
        if self.print_mode == "B":
            amount = self.greyscale_price

        if (cost < amount):
            print("Not enough coins")
            print(f"Here is your money ${amount}\nprinting....")
            return round(cost, 2)
        
        if (cost >= amount):
            if (cost > amount):
                print(f"Here is your change ${cost - amount}\nprinting....")
                return amount
            print("Printing...")
            return round(amount)

    @classmethod
    def report(cls,amount,pages):
        ink = FORMAT["coloured"]["materials"]["ink"] * pages
        cls.resources = {
                        'ink': cls.resources["ink"] - ink,
                        'paper': cls.resources["paper"] - pages,
                        'profit': cls.resources["profit"] + amount
                    }
        return cls.resources


    
            





if __name__ == "__main__":
    x = Printer()
    print(x.avaliable_resources())
    cost = x.cost
    pages = x.num_pages
    profit = x.validated_amount(cost)
    #print(x.coloured_price)
    print(x.report(profit,pages)) 
    print("================================================")
    # i = Printer()
    # print(i.avaliable_resources())
    # cost = i.cost
    # profit = i.validated_amount(cost)
