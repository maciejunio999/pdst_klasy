from item import Item

item1 = Item("Iron", 34.99, 20)
item1.pay_rate = 0.9
item1.apply_discount()
print(item1.get_price())


item2 = Item("Sink", 79.99, 10)
item2.apply_discount()
print(item2.get_price())


print(Item.get_num_of_items())