class Cricket:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Player: {self.__player} Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score > 0:
            self.__score = new_score
            print(f"Upadated Score :{self.__score}")
        else:
            ("Score should not be negative")
class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Player: {self.__player} Score: {self.__score}")
    def play(self):
        print(f"{self.__player} scores a goal")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score > 0:
            self.__score = new_score
            print(f"Upadated Score :{self.__score}")
        else:
            ("Score should not be negative")

cricket = Cricket("M.S Dhoni", 85)
football = Football("Maradona" , 10)

for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

cricket.__score = 455
print(f"Score is still {cricket.get_score()}")

newscore = cricket.set_score(100)

    