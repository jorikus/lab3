class Item:
    def __init__(self, item_name, quantity):
        self.__item_name = item_name
        self.quantity = quantity
    
    def get_cost(self):
        print('Parent method')
        return 0
