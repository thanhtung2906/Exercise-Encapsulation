class Player:
    def __init__(self,name:str,endurance:int,sprint:int,dribble:int,passing:int,shooting:int):
        self.__name =  name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting
    def get_name(self):
        return self.__name 
    def set_name(self,name):
        self.__name = name
        return self.__name 
    
    def get_endurance(self):
        return self.__endurance
    def set_endurance(self,endurance):
        self.__endurance = endurance
        return self.__endurance

    def get_sprint(self):
        return self.__sprint
    def set_sprint(self,sprint):
        self.__sprint = sprint
        return self.__sprint
    
    def get_dribble(self):
        return self.__dribble
    def set_dribble(self,dribble):
        self.__dribble = dribble
        return self.__dribble
    
    def get_passing(self):
        return self.__passing
    def set_passing(self,passing):
        self.__passing = passing 
        return self.__passing 
    
    def get_shooting(self):
        return self.__shooting
    def set_shooting(self,shooting):
        self.__shooting = shooting
        return self.__shooting


    def __str__(self) -> str:
        return (f"Player: {self.__name}\n"
                f"Endurance: {self.__endurance}\n"
                f"Sprint: {self.__sprint}\n"
                f"Dribble: {self.__dribble}\n"
                f"Passing: {self.__passing}\n"
                f"Shooting: {self.__shooting}\n")