'''
Created on 19 Nov 2018

@author: juan
'''


class Player:
    
    def __init__(self,new_name):
        self.__name = new_name
        self.__no_of_games = 0
        self.__total = 0
        self.__record = 0
        
    def get_name(self):
        return self.__name
    
    def get_no_of_games(self):
        return self.__no_of_games
    
    def get_record(self):
        return self.__record
    
    def add_game(self, points):
        if points >= 0:
            self.__no_of_games += 1
            self.__total += points
            if points > self.__record:
                self.__record = points
                
    def average(self):
        if self.__no_of_games > 0:
            ka = self.__total / self.__no_of_games
        else:
            ka = 0.0
        return ka
    
    def is_master(self):
        if self.__no_of_games > 0:
            ka = self.__total / self.__no_of_games
            if self.__total >= 3000 and ka > 2000:
                return True
            else:
                return False
        
    def is_better(self, another_player):
        if self.__record > another_player.get_record():
            return True
        if self.__record == another_player.get_record() and self.average() > another_player.average():
            return True
        else:
            return False
        
    def __str__(self):
        if self.is_master():
            str1 = "{:s}, number of games {:d}, record {:d} points, MASTER.".format(self.__name, self.__no_of_games, self.get_record())
            return str1
        else:
            str2 = "{:s}, number of games {:d}, record {:d} points, has not achieved master title.".format(self.__name, self.__no_of_games, self.get_record())
            return str2
        
            