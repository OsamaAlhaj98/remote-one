class Store: 
    
    def __init__(self):
        self.vegtables = {}
        self.fruits = {}
        
    def add_vegtable(self,name,price,quantity):
        self.vegtables[name] = {"price":float(price), "quantity":int(quantity)}
        
    def add_fruit(self,name,price,quantity):
        self.fruits[name]= {"price":float(price), "quantity":int(quantity)}
        
    def display_items(self):
        print("vegtables:")
        for name, item in self.vegtables.items():
            print(f"Name: {name}, price: {item['price']},Quantity: {item['quantity']}")
            
    def calc_total(self):
        total = 0
        for item in self.vegtables.values():
            total+=item["price"]*item["quantity"]
        for item in self.fruits.values():
            total+=item["price"]*item["quantity"]
        return total
    
    def check_ava(self,item_name):
        if item_name in self.vegtables:
            return self.vegtables[item_name]["quantity"]>0
        if item_name in self.fruits:
            return self.fruits[item_name]["quantity"]>0
        return False
            

store = Store()

store.add_vegtable("Carrot", 2.5, 10)
store.add_vegtable("Potatoes", 1.75, 6)
store.add_vegtable("Spinach", 3.0, 15)
store.add_vegtable("Tomato", 1.5, 20)

store.add_fruit("Peach", 2.0, 8)
store.add_fruit("Banana", 1.0, 12)
store.add_fruit("Apple", 3.0, 7)
store.add_fruit("Orange", 1.5, 10)

store.display_items()

total_payment = store.calc_total()
print(f"total is = {total_payment}")

print("Carrot:", store.check_ava("Carrot"))
print("Spinach:", store.check_ava("Spinach"))
print("Apple:", store.check_ava("Apple"))
print("Grapes:", store.check_ava("Grapes"))
