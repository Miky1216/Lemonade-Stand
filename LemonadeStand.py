import random
import datetime

class TimeofDay:
    def CheckTimeOfDay(self):
        now = datetime.datetime.now().time()
        sunrise_list = [[7, 21], [6, 50], [7, 4], [6, 10], [5, 29], [5, 12], [5, 26], [5, 57], [6, 31], [7, 5], [6, 44], [7, 16]]
        sunset_list = [[16, 42], [17, 23], [18, 58], [19, 34], [20, 8], [20, 33], [20, 29], [19, 55], [19, 2], [18, 9], [16, 28], [16, 18]]
        sunrise = now.replace(hour=sunrise_list[datetime.datetime.now().month - 1][0], minute=sunrise_list[datetime.datetime.now().month - 1][1], second=0, microsecond=0)
        sunset = now.replace(hour=sunset_list[datetime.datetime.now().month - 1][0], minute=sunset_list[datetime.datetime.now().month - 1][1], second=0, microsecond=0)
        if sunrise < datetime.datetime.now().time() and datetime.datetime.now().time() < sunset:
            return 1
        else:
            return 0

class Participants:    
    def __init__(self, Participants):
        self.name
        self.demand

class UserInput:
    def GetUserName(self):
        UserName = raw_input("Enter your game name: ")
        return UserName

class InitialCalculations:
    def ChangeInForecast(self):
        pass
    def ChangeInOutsideTemp(self):
        pass
    def CalculatePitcherCupPrice(self):
        pass

class ProfitCalculations:
    def CalculateProfit(self):
        pass
    def ShowProfitLoss(self):
        pass

class GameLoop:
    def RunGame(self):
        TimeCheck = TimeofDay()
        if TimeCheck.CheckTimeOfDay() == 0:
            print "Exiting: Program only accessible during daytime"
            raise SystemExit
            
if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
