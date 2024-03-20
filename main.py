from parent_class import Item

    
class Food(Item):
    def get_cost(self):
        super().get_cost()  
        return self.quantity * 100

class Drink(Item):
    def get_cost(self):
        super().get_cost() 
        return self.quantity * 50



def cost(item):
    return item.get_cost()


def main():
    item1 = Food('Бургер', 10)
    item2 = Drink('Сок',  15)
    print(cost(item1))
    print(cost(item2))
    

if __name__ == '__main__':
    main()

