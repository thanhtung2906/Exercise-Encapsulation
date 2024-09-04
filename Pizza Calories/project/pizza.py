from dough import Dough
from toppings import Toppings
class Pizza:
    def __init__(self,name:str,dough:Dough,toppings_capacity:int):
        self.__name = name 
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity
        self.pizza_weight = dough.get_weight()
    def add_topping(self,topping:Toppings):
        if sum(self.__toppings.values()) <= self.__toppings_capacity:
                if topping in self.__toppings:
                    self.pizza_weight += topping.get_weight()
                    
                else:
                    self.pizza_weight += topping.get_weight()
                    self.__toppings[topping] = topping.get_weight()
                    
        else:
            return 'Not enough space for another topping'
    def calculate_total_weight(self):
        return self.pizza_weight
    def __repr__(self) -> str:
        return f'Pizza {self.__name},Dough:{dough},Toppings:{self.__toppings} ,Total Weight:{self.calculate_total_weight()}'
    
dough = Dough("Pastry Flour","Oven",100)
Peparoni = Pizza("Peparoni",dough,5)
meat = Toppings("Meat",1)
sausage = Toppings("Sausage",3)
vegatables = Toppings("Vegatable",1)

Peparoni.add_topping(meat)
Peparoni.add_topping(meat)
Peparoni.add_topping(meat)
Peparoni.add_topping(meat)
Peparoni.add_topping(sausage)
Peparoni.add_topping(vegatables)



print(Peparoni)

    
