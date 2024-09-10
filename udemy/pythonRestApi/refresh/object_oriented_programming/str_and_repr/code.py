# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person {self.name}, {self.age} year old."

#     def __repr__(self):
#         return f"<Person({self.name}, {self.age})>" # reconstruir o objeto.


# bob = Person("Bob", 35)
# print(bob.age)
# print(bob)
# print(bob.__repr__())



class Store:
    def __init__(self, name):
        self.name = name    
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        return sum([item["price"] for item in self.items])



store = Store("Alexandre")

print(store.stock_price())