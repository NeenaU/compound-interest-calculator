import tkinter as tk

class interestCalculator():

    def __init__(self, master):
        self.master = master
        master.title = ("Compound Interest Calculator")

        #Title
        self.titleLabel = tk.Label(text="Compound Interest Calculator", font=("Times",16), width=24).grid(row=0,column=0,sticky='EW',pady=15)

        #Options
        self.initialAmountLabel = tk.Label(master, text="Initial Amount").grid(sticky='W')
        self.initialAmountFrame = tk.Frame(master)  #widgets can be placed side by side in a frame
        self.initialAmountFrame.grid(row=2,sticky='NW',pady=6)
        self.poundSign1 = tk.Label(self.initialAmountFrame, text="£")
        self.poundSign1.grid(row=0,column=0)
        self.initialAmountEntry = tk.Entry(self.initialAmountFrame, width=8)
        self.initialAmountEntry.grid(row=0,column=1)

        self.interestRateLabel = tk.Label(text="Yearly Interest Rate").grid(sticky='W')
        self.interestRateFrame = tk.Frame(master)
        self.interestRateFrame.grid(row=4,sticky='NW',pady=6)
        self.interestRateEntry = tk.Entry(self.interestRateFrame, width=3)
        self.interestRateEntry.grid(row=0,column=0)
        self.percentSign1 = tk.Label(self.interestRateFrame, text="%")
        self.percentSign1.grid(row=0,column=1)

        self.calcPeriodLabel = tk.Label(text="Calculation Period").grid(sticky='W')
        self.calcPeriodFrame = tk.Frame(master)
        self.calcPeriodFrame.grid(row=6,sticky='NW',pady=6)
        self.yearsEntry = tk.Entry(self.calcPeriodFrame, width=3)
        self.yearsLabel = tk.Label(self.calcPeriodFrame, text="years")
        self.monthsEntry = tk.Entry(self.calcPeriodFrame, width=3)
        self.monthsLabel = tk.Label(self.calcPeriodFrame, text="months")

        self.yearsEntry.grid(row=0,column=0)
        self.yearsLabel.grid(row=0,column=1)
        self.monthsEntry.grid(row=0,column=2)
        self.monthsLabel.grid(row=0,column=3)
        
        self.compoundIntervalLabel = tk.Label(text="Compound Interval").grid(sticky='W')
        self.compoundDefaultVal = tk.StringVar(master)
        self.compoundDefaultVal.set("yearly")
        self.compoundchoice = tk.OptionMenu(master, self.compoundDefaultVal, "monthly", "yearly").grid(sticky='NW',pady=6)

        self.regularAmountLabel = tk.Label(text="Regular deposit/withdrawal").grid(sticky='W')
        self.regularAmountFrame = tk.Frame(master)
        self.regularAmountFrame.grid(row=10,sticky='NW',pady=6)
        self.regularAmountDefaultVal = tk.StringVar(master)
        self.regularAmountDefaultVal.set("no")
        self.regularAmountChoice = tk.OptionMenu(self.regularAmountFrame, self.regularAmountDefaultVal, "yes", "no", command=self.checkRegularAmount)   #command called when an option is selected
        self.regularAmountChoice.grid(row=0,column=0)                                                                                                   #if yes is selected, the entry will become visible
        self.amountLabel = tk.Label(self.regularAmountFrame, text="Amount:")
        self.poundSign2 = tk.Label(self.regularAmountFrame, text="£")
        self.regularAmountEntry = tk.Entry(self.regularAmountFrame, width=8)

        self.increaseDepositsLabel = tk.Label(text="Increase deposits in line with annual inflation?").grid(sticky='W')
        self.increaseDepositsFrame = tk.Frame(master)
        self.increaseDepositsFrame.grid(row=12,sticky='NW',pady=6)
        self.increaseDepositsDefaultVal = tk.StringVar(master)
        self.increaseDepositsDefaultVal.set("no")
        self.increaseDepositsChoice = tk.OptionMenu(self.increaseDepositsFrame, self.increaseDepositsDefaultVal, "yes", "no", command=self.checkIncreaseDeposits)   #command called when an option is selected
        self.increaseDepositsChoice.grid(row=0,column=0)                                                                                                            #if yes is selected, the label, entry and % sign will become visible
        self.annualInflationLabel = tk.Label(self.increaseDepositsFrame, text="Annual inflation rate:")
        self.annualInflationEntry = tk.Entry(self.increaseDepositsFrame, width=3)
        self.percentSign2 = tk.Label(self.increaseDepositsFrame, text="%")

        self.calculateButton = tk.Button(master, text="Calculate", command=self.calculateResult)
        self.calculateButton.grid(sticky='NW',pady=6)
        self.resultLabel = tk.Label(master, text="").grid(sticky='W')
        self.calculateAgainButton= tk.Button(master, text="Calculate Again", command=self.reset)

    def checkRegularAmount(self, value):
        if value == "no":
            self.amountLabel.grid()
            self.poundSign2.grid()
            self.regularAmountEntry.grid()
        else:
            self.amountLabel.grid(row=0,column=1)
            self.poundSign2.grid(row=0,column=2)
            self.regularAmountEntry.grid(row=0,column=3)

    def checkIncreaseDeposits(self, value):
        if value == "no":
            self.annualInflationLabel.grid()
            self.annualInflationEntry.grid()
            self.percentSign2.grid()
            
        else:
            self.annualInflationLabel.grid(row=0,column=1)
            self.annualInflationEntry.grid(row=0,column=2)
            self.percentSign2.grid(row=0,column=3)

    def calculateResult(self):
        self.calculateButton.grid()
        self.calculateAgainButton.grid(sticky='W')
        print("A")

    def calculateRegularDeposit(self):
        print("B")
        
    def calculateIncreasingDeposits(self):
        print("C")

    def reset(self):
        print("D")

def main():
    window = tk.Tk()
    window.geometry("300x500")
    #window.configure(bg='#aaabb8')  #window background colour
    generator = interestCalculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
