class Toppings:
    def __init__(self,topping_type:str,weight):
        self.__topping_type = topping_type
        self.__weight = weight
    
    def get_weight(self):
        return self.__weight
    
    def get_topping_type(self):
        return self.__topping_type
    
    def set_weight(self,weight):
        self.__weight = weight
        return self.__weight
    
    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type
        return self.__topping_type
    def __repr__(self) -> str:
        return (f'{self.get_topping_type()}')
        