class Parent:
    def __init__(self, gadget, item_collection):
        self.gadget = gadget
        self.item_collection = item_collection
    
    def show_gadget(self):
        print(self.gadget)
        
    def show_collection(self):
        print(self.item_collection)
        
class Child(Parent):
    def show_all(self):
        print(self.gadget)
        print(self.item_collection)
        
c = Child(['phone', 'tabs', 'laptops'], ['iphone', 'lenova'])
c.show_all()
