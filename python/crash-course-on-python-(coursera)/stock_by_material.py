# Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in
# stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def stock_by_material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class Shirt(Clothing):
    material = "Cotton"


class Pants(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
sweatpants = Pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.stock_by_material("Cotton")
print(current_stock)
