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
        UserName = ""
        while UserName is "":
            UserName = raw_input("Enter your player name: ")
    def HowMuchToChargePerCup(self):
        PricePerCup = raw_input("How much do you want to charge per cup of lemonade?")
        return PricePerCup

class InitialCalculations:
    def ChangeInForecast(self):
        ForecastGenerator = random.randint(1,3)
        if ForecastGenerator == 3:
            print "The forecast is sunny"
        if ForecastGenerator == 2:
            print "The forecast is cloudy"
        if ForecastGenerator == 1:
            print "The forecast is rainy"
    def ChangeInOutsideTemp(self):
        TemperatureGenerator = random.randint(60,95)
        print "with a temperature of " + str(TemperatureGenerator) + " degrees Fahrenheit"
    def CalculatePitcherCupPrice(self):
        PriceOfOneLemon = random.uniform(0.10, 0.50)
        print "One Lemon costs $" + str(round(PriceOfOneLemon,2))
        PriceOfFivePoundBagOfSugar = random.randint(2,3)
        print "A five pound bag of sugar costs $" + str(PriceOfFivePoundBagOfSugar)
        PriceOfOneHundredCups = random.randint(3,5)
        print "A bag of 100 cups costs $" + str(PriceOfOneHundredCups)
        #Cost of one pitcher, Pitcher makes 10 cups
        CostToMakePitcher = (PriceOfOneLemon * 5) + (PriceOfFivePoundBagOfSugar / 4) + (PriceOfOneHundredCups / 10)
        print "Cost to make one pitcher of lemonade is $" + str(round(CostToMakePitcher,2))
        print "Cost to make one cup of lemonade is $" + str(round((CostToMakePitcher / 10), 2))
        return CostToMakePitcher

class ProfitCalculations:
    def CalculateProfit(self):
        pass
        GainLossCalc = 
    def ShowProfitLoss(self):
        pass

class CheckHighScore:
    def ReadFile(self):
        file = open('highscore', 'r')
        print file.read()
        file.close()
        file = open('highscore', 'w')
        file.write('test')
        file.close()
        
class GameLoop:
    def RunGame(self):
        PlayerName = UserInput()
        PlayerName.GetUserName()
        for DayCounter in range(0,6):
            print "Day: " + str(DayCounter+1)
            TimeCheck = TimeofDay()
            if TimeCheck.CheckTimeOfDay() == 0:
                print "Exiting: Program only accessible during daytime"
                raise SystemExit
            GenerateRandomForecast = InitialCalculations()
            GenerateRandomForecast.ChangeInForecast()
            GenerateTemperature = InitialCalculations()
            GenerateTemperature.ChangeInOutsideTemp()
            PitcherCupPriceGenerator = InitialCalculations()
            PitcherCupPriceGenerator.CalculatePitcherCupPrice()
            PlayerChargePerCup = UserInput()
            PlayerChargePerCup.HowMuchToChargePerCup()
if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
