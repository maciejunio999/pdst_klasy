from item import Item

#item1 = Item("Phone", 500, 5)
#item2 = Item("Laptop", 1000, 3)
#item3 = Item("Cable", 10, 10)
#item4 = Item("Mouse", 25, 5)
#item5 = Item("Keyboard", 40, 5)

#print(Item.all)

for i in Item.all:
    print(i.get_name())

Item.instantiate_from_csv()
print(Item.all)