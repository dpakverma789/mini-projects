import os
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt


class GenerateInvestmentPlan():
    def __init__(self,age,income):
        self.age = age
        self.income = income

    def InvestmentCalculation(self):
        
        if self.age >= 15 and self.age <= 20:
            investment_percentage = 70; need_percentage = 20; want_percentage = 10
            
        elif self.age >= 21 and self.age <= 25:
            investment_percentage = 50; need_percentage = 35; want_percentage = 15
            
        elif self.age >= 26 and self.age <= 40:
            investment_percentage = 40; need_percentage = 40; want_percentage = 20
            
        else:
            investment_percentage = 20; need_percentage = 70; want_percentage = 10
                
        total_percentage = [investment_percentage, need_percentage, want_percentage ]
        values = self.percentageCalculator(total_percentage)
        investment = values[0]
        need = values[1]
        want = values[2]
        return investment, need, want

    def percentageCalculator(self, total_percentage):
        values = []
        for i in total_percentage:
            values.append(str(round((self.income * i)/100)))
        return values    
            
    
if __name__ == "__main__":

    while True:
        try:
            age = int(input('\n\nEnter Your Age: '))
            if age >= 15:
                income = int(input('\nEnter Your in Hand Income/PocketMoney \u20B9 : '))
                if income:
                    investment = GenerateInvestmentPlan(age, income)
                    investment,need,want = investment.InvestmentCalculation()
                    print('\n\nAs per Our Suggestion YOu should Manage YOur Income like: ')
                    print('\nYOu Should Invest:', investment+'\u20B9',
                          "Amount like in Study/Course, MutualFund, Stocks, Gold, Bank, FDs!")
                    print('\nYOu Should Keep:', need+'\u20B9', 'Amount for YOur Need! like Rent, Food, Fees, Bills')
                    print('\nYOu Should Keep:', want+'\u20B9', 'Amount For Your Wants! like Shopping, Travel, Parties')
                    print('=======================')
                    slice = [int(investment), int(need), int(want)]
                    activities=["INVESTMENT", 'NEED', 'WANTS']
                    cols = ['c', 'm', 'r', 'b']
                    plt.pie(slice,labels=activities, colors=cols, startangle=90, shadow=True, explode=[0, 0, 0.1],
                            autopct='%.0f%%')
                    plt.legend(loc='lower right')
                    plt.title("MONEY MANAGMENT")
                    plt.show()
                else:
                    print('\n\t"Income can not be zero or negative!!"')
                    print('=======================')
                    
            else:
                print('\n\t"You Should Invest in YOur Studies and Skills First!!"')
                print('=======================')
        except:
            print('\n\t"Age OR Income could not be Blank and \n\tIt should be in Numerical Value but not Zero"')
            print('=======================')
    



    

