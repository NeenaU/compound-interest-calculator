import tkinter as tk

class interestCalculator():

    def __init__(self, master):
        self.master = master
        master.title = ("Compound Interest Calculator")

        #Title
        self.titleLabel = tk.Label(text="Compound Interest Calculator")

        #Options
        self.initialAmountLabel = tk.Label(text="Initial Amount (£)")
        self.initialAmountEntry = tk.Entry(master, width=8)

        self.calcPeriodLabel = tk.Label(text="Calculation Period")
        self.yearsLabel = tk.Label(text="years")
        self.yearsEntry = tk.Entry(master, width=3)
        self.monthsLabel = tk.Label(text="months")
        self.monthsEntry = tk.Entry(master, width=3)
        
        self.compoundIntervalLabel = tk.Label(text="Compound Interval")
        self.compoundDefaultVal = tk.StringVar(master)
        self.compoundDefaultVal.set("yearly")
        self.compoundchoice = tk.OptionMenu(master, self.compoundDefaultVal, "monthly", "yearly")

        self.regularAmountLabel = tk.Label(text="Regular deposit/withdrawal (£)")
        self.regularAmountDefaultVal = tk.StringVar(master)
        self.regularAmountDefaultVal.set("no")
        self.regularAmountChoice = tk.OptionMenu(master, self.regularAmountDefaultVal, "yes", "no")
        self.regularAmountEntry = tk.Entry(master, width=8)

        self.increaseDepositsLabel = tk.Label(text="Increase deposits in line with annual inflation?")
        self.increaseDepositsDefaultVal = tk.StringVar(master)
        self.increaseDepositsDefaultVal.set("no")
        self.increaseDepositsChoice = tk.OptionMenu(master, self.increaseDepositsDefaultVal, "yes", "no")
        self.annualInflationLabel = tk.Label(text="Annual inflation rate (%)")
        self.annualInflationEntry = tk.Entry(master, width=3)

        self.calculateButton = tk.Button(text="Calculate", command=self.calculateResult)
        self.resultLabel = tk.Label(master)
        self.calculateAgainButton= tk.Button(text="Calculate Again", command=self.reset)

    def calculateResult(self):
        print("A")

    def calculateRegularDeposit(self):
        print("B")
        
    def calculateIncreasingDeposits(self):
        print("C")

    def reset(self):
        print("D")

def main():
    window = tk.Tk()
    window.geometry("400x275")
    #window.configure(bg='#aaabb8')  #window background colour
    generator = interestCalculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
