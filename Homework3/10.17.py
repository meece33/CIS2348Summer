# Mauricio Corado 1254732

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))

if __name__ == "__main__":
    obj1 = ItemToPurchase()          # Takes input for the first object to purchase
    print('Item 1')
    obj1.item_name = input('Enter the item name:\n')
    obj1.item_price = int(input('Enter the item price:\n'))
    obj1.item_quantity = int(input('Enter the item quantity:\n'))

    obj2 = ItemToPurchase()    # Takes input for the second object to purchase
    print('\nItem 2')
    obj2.item_name = input('Enter the item name:\n')
    obj2.item_price = int(input('Enter the item price:\n'))
    obj2.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')        # calls the cost method that was initialized earlier
    obj1.print_item_cost()
    obj2.print_item_cost()

    total = ((obj1.item_price * obj1.item_quantity) + (obj2.item_price * obj2.item_quantity))  # calcs for Total

    print('\nTotal: ${}'.format(total))