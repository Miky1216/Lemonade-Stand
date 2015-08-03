import random
import datetime
import os
import os.path
import webbrowser

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

class GameData:    
    def __init__(self):
        self.UserName = ""
        self.ForecastGenerator = 0
        self.TemperatureGenerator = 0
        self.CostToMakePitcher = 0
        self.CashOnHand = 10.0
        self.Profit = 0
        self.FloatPricePerCup = 0
        self.ProfitGainLoss = 0

class UserInput:
    def GetUserName(self):
        UserName = ""
        while UserName is "":
            UserName = raw_input("Enter your player name: ")
            if UserName == ("Mike"):
				webbrowser.open("https://youtu.be/E-WHW-QNswE?t=25")
            elif UserName == ("Terrill"):
                webbrowser.open("https://youtu.be/E-WHW-QNswE?t=25")
            elif UserName == ("Bravo"):
                webbrowser.open("https://youtu.be/E-WHW-QNswE?t=25")
            elif UserName == ("mike"):
                webbrowser.open("https://youtu.be/E-WHW-QNswE?t=25")
            else: 
                continue
        return UserName
    def HowMuchToChargePerCup(self):
        CheckForValidNumber = 0
        FloatPricePerCup = 0
        while CheckForValidNumber == 0:
            PricePerCup = raw_input("How much do you want to charge per cup of lemonade?") 
            try:
                FloatPricePerCup = float(PricePerCup)
            except:
                print ""
            if FloatPricePerCup >= 0.01 and FloatPricePerCup <= 1.00:
                CheckForValidNumber = 1
            else:
                print "Error! Enter a number between $0.01 and $1.00"                
        return FloatPricePerCup

class InitialCalculations:
    def ChangeInForecast(self):
        ForecastGenerator = random.randint(1,3)
        if ForecastGenerator == 3:
            print "The forecast is sunny"
        if ForecastGenerator == 2:
            print "The forecast is cloudy"
        if ForecastGenerator == 1:
            print "The forecast is rainy"
        return ForecastGenerator
    def ChangeInOutsideTemp(self):
        TemperatureGenerator = random.randint(70,95)
        print "with a temperature of " + str(TemperatureGenerator) + " degrees Fahrenheit"
        return TemperatureGenerator
    def CalculatePitcherCupPrice(self, VariableList):
        PriceOfOneLemon = random.uniform(0.10, 0.50)
        print "One Lemon costs $" + str(round(PriceOfOneLemon,2))
        PriceOfFivePoundBagOfSugar = random.uniform(2.0,3.99)
        print "A five pound bag of sugar costs $" + str(round(PriceOfFivePoundBagOfSugar,2))
        PriceOfOneHundredCups = random.uniform(3.0,4.99)
        print "A bag of 100 cups costs $" + str(round(PriceOfOneHundredCups,2))
        VariableList.CostToMakePitcher = (PriceOfOneLemon * 5) + (PriceOfFivePoundBagOfSugar / 4) + (PriceOfOneHundredCups / 10)
        print "Cost to make one pitcher of lemonade is $" + str(round(VariableList.CostToMakePitcher,2))
        print "Cost to make one cup of lemonade is $" + str(round((VariableList.CostToMakePitcher / 10), 2))
        print "Cash on hand is $" + str(round(VariableList.CashOnHand,2))
        return VariableList

class ProfitCalculations:
    def CalculateProfit(self, VariableList):
        #print "VariableList.ForecastGenerator " + str(VariableList.ForecastGenerator)
        if VariableList.ForecastGenerator == 3:
            VariableList.ForecastGenerator = 21
        VariableList.Profit = (VariableList.TemperatureGenerator / 10) * (VariableList.ForecastGenerator) * (1.10 - VariableList.FloatPricePerCup) * (VariableList.FloatPricePerCup)
        print "$" + str(VariableList.Profit)
    def ShowProfitLoss(self, VariableList):
        VariableList.DailyProfitGainLoss = VariableList.Profit - VariableList.CostToMakePitcher
        print "Your daily gain or loss was $" + str(round(VariableList.DailyProfitGainLoss,2))
        VariableList.CashOnHand = VariableList.CashOnHand + VariableList.DailyProfitGainLoss
    def EndGameBonus(self, VariableList):
        if VariableList.CashOnHand >= 100:
            webbrowser.open("https://youtu.be/GGXzlRoNtHU?t=6")
        elif VariableList.CashOnHand <= 30:
            webbrowser.open("https://youtu.be/S8u3NFEbjAs?t=7")
        else:
            raise SystemExit    
class CheckHighScore:
    def ReadHighScoreFile(self, VariableList):
        PATH='./highscore'
        if not os.path.isfile(PATH) or not os.access(PATH, os.R_OK):
            file = open('highscore', 'w+')
            file.close()
        file = open('highscore', 'r')
        ReadFile = file.read()
        if ReadFile == "":
            file.close()
            file = open('highscore', 'w')
            FileWrite = str(round(VariableList.CashOnHand,2)) + "," + VariableList.UserName + ","
            file.write(FileWrite)
            for line in range(0,4):
                file.write("00.00," + "     " + ",")
            file.close()
        else:
            FileList = ReadFile.split(",")
            print "\nHigh Score    Name"
            for item in range(0,5):
                if VariableList.CashOnHand > float(FileList[item * 2]):
                    HoldCOH = FileList[item * 2]
                    HoldName = FileList[(item * 2) + 1]
                    FileList[item * 2] = VariableList.CashOnHand
                    FileList[(item * 2) + 1] = VariableList.UserName
                    VariableList.CashOnHand = HoldCOH
                    VariableList.UserName = HoldName
                print "  " + str(round(float(FileList[item * 2]),2)) + "       " + FileList[(item * 2) + 1]
            file.close()
            file = open('highscore', 'w')
            for item in range(0,5):
                file.write(str(round(float(FileList[item * 2]),2)) + "," + FileList[(item * 2) + 1] + ",")
            file.close()
        
class GameLoop:
    def RunGame(self):
        PlayerName = UserInput()
        VariableList = GameData()
        VariableList.UserName = PlayerName.GetUserName()
        for DayCounter in range(0,7):
            print "Day: " + str(DayCounter+1)
            TimeCheck = TimeofDay()
            if TimeCheck.CheckTimeOfDay() == 0:
                print "Exiting: Program only accessible during daytime"
                raise SystemExit
            GenerateRandomForecast = InitialCalculations()
            VariableList.ForecastGenerator = GenerateRandomForecast.ChangeInForecast()
            GenerateTemperature = InitialCalculations()
            VariableList.TemperatureGenerator = GenerateTemperature.ChangeInOutsideTemp()
            if  VariableList.TemperatureGenerator >= 90 and VariableList.ForecastGenerator == 1:
                print "Gahh! The humidity is brutal! Daily profit is $0!"
                VariableList.DailyProfitGainLoss = 0
            else:
                PitcherCupPriceGenerator = InitialCalculations()
                PitcherCupPriceGenerator.CalculatePitcherCupPrice(VariableList)
                PlayerChargePerCup = UserInput()
                VariableList.FloatPricePerCup = PlayerChargePerCup.HowMuchToChargePerCup()
                ProfitGainLossCalc = ProfitCalculations()
                ProfitGainLossCalc.CalculateProfit(VariableList)
                ProfitGainLossCalc.ShowProfitLoss(VariableList)
        print "Game Over! Your final score is $" + str(round(VariableList.CashOnHand,2))
        HighScore = CheckHighScore()
        HighScore.ReadHighScoreFile(VariableList)
        ProfitGainLossCalc.EndGameBonus(VariableList)
if __name__ == "__main__":
    StartProgram = GameLoop()
    StartProgram.RunGame()
