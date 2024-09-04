from player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []
    def get_name(self) -> str:
        return self.__name
    def set_name(self, name: str):
        self.__name = name
        return self.__name
    
    def get_rating(self) -> int:
        return self.__rating
    def set_rating(self, rating: int):
        self.__rating = rating
        return self.__rating
    
    def get_players(self) -> list:
        return self.__players
    def set_players(self, players: list):
        self.__players = players
        return self.__players
    def add_player(self, player: Player) -> str:
        for existing_player in self.__players:
            if existing_player.get_name() == player.get_name():
                return f"Player {player.get_name()} has already joined"
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        for player in self.__players:
            if player.get_name() == player_name:
                self.__players.remove(player)
                return f"Player {player_name} removed from the team"

        return f"Player {player_name} not found"


player1 = Player("Ronaldo", 85, 90, 88, 92, 87)
player2 = Player("Messi", 80, 85, 89, 91, 88)

team = Team("MU", 5)
print(team.add_player(player1))  
print(team.add_player(player1))  
print(team.add_player(player2))  

print(team.remove_player("John"))  
print(team.remove_player("Messi"))  

print(player1)
