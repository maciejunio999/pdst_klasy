import csv

class Item:
    # class attributes
    number_of_items = 0
    pay_rate = 0.8

    all = []

    # class methods
    @classmethod
    def increase_num_of_items(cls):
        cls.number_of_items += 1
    
    @classmethod
    def get_num_of_items(cls):
        return cls.number_of_items
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            l = len(item.get('name'))
            Item(name=item.get('name')[1:l-1], price=float(item.get('price')), quantity=float(item.get('quantity')))
    
    # static methods
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here even numbers like 5.0 are interpreted as int
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # magic methods
    def __init__(self, name: str, price: float, quantity=0):
        # validate arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero"

        # assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # actions to execute
        Item.all.append(self)
        Item.increase_num_of_items()
    
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.__price}, {self.__quantity})'
    
    # work with name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # work with name
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def apply_discount(self):
        self.__price = round(self.__price * Item.pay_rate, 2)
    
    def apply_increment(self, increment):
        c = round(self.__price * (increment + 1), 2)
        if Item.is_integer(c): self.__price = int(c)
    
    # work with quantity
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity
        self.__quantity = new_quantity
    
    # private methods
    def __show_success(self):
        print('Success!')

    # other
    def total_cost(self):
        self.__show_success()
        return round(self.__price * self.__quantity, 2)