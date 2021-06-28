# Mauricio Corado 1254732

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))

    def print_item_description(self):
        print('{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
  #  def add_item(self):

  #  def remove_item(self):

  #  def modify_item(self):

    # def get_cost_of_cart(self):

  #  def print_total(self):

   # def print_description(self):



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
