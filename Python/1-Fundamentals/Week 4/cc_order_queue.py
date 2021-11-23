class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self,flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self,costumer,flavor,scoops):
        self.costumer = str(costumer)
        self.flavor = str(flavor)
        self.scoops = int(scoops)

        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        if scoops not in range(1,4):
            print("Choose between 1 to 3 scoops")
            return
        print("Order created!")

        order = {"costumer":costumer, "flavor":flavor, "scoops":scoops}
        self.orders.enqueue(order)

    def show_orders(self):
        print("\nAll pending ice cream orders:")
        for i in self.orders.items:
            print("Costumer:",i["costumer"],"-Flavor:",i["flavor"],"-Scoops:",str(i["scoops"]))
 
    def next_order(self):
        print("\nNext order up!")
        a = self.orders.dequeue()
        print("Customer:",a["customer"],"-- Flavor:",a["flavor"],"--Scoops:",str(a["scoops"]))


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)

shop.show_orders()
shop.next_order()
shop.show_orders()


