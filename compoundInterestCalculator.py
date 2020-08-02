import tkinter as tk

class interestCalculator():

    def __init__(self, master):
        self.master = master
        master.title = ("Compound Interest Calculator")

        #Configure column size
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=5)
        master.grid_columnconfigure(3, weight=5)

        #Title
        self.titleLabel = tk.Label(text="Compound Interest Calculator", font=("Times",16)).grid(row=0,column=0,sticky='EW',columnspan=3,pady=15)

        #Options
        self.initialAmountLabel = tk.Label(master,text="Initial Amount (£)").grid(sticky='W')
        self.initialAmountEntry = tk.Entry(master, width=8)
        self.initialAmountEntry.grid(sticky='W')

        self.interestRateLabel = tk.Label(text="Yearly Interest Rate (%)").grid(sticky='W')
        self.interestRateEntry = tk.Entry(master, width=3).grid(sticky='W')

        self.calcPeriodLabel = tk.Label(text="Calculation Period").grid(sticky='W')
        self.calcPeriodFrame = tk.Frame(master).grid(sticky='W')
        self.yearsEntry = tk.Entry(self.calcPeriodFrame, width=3)
        self.yearsLabel = tk.Label(self.calcPeriodFrame, text="years")
        self.monthsEntry = tk.Entry(self.calcPeriodFrame, width=3)
        self.monthsLabel = tk.Label(self.calcPeriodFrame, text="months")
        
        self.compoundIntervalLabel = tk.Label(text="Compound Interval").grid(sticky='W')
        self.compoundDefaultVal = tk.StringVar(master)
        self.compoundDefaultVal.set("yearly")
        self.compoundchoice = tk.OptionMenu(master, self.compoundDefaultVal, "monthly", "yearly").grid(sticky='W')

        self.regularAmountLabel = tk.Label(text="Regular deposit/withdrawal (£)").grid(sticky='W')
        self.regularAmountDefaultVal = tk.StringVar(master)
        self.regularAmountDefaultVal.set("no")
        self.regularAmountChoice = tk.OptionMenu(master, self.regularAmountDefaultVal, "yes", "no").grid(sticky='W')
        self.regularAmountEntry = tk.Entry(master, width=8).grid(sticky='W')

        self.increaseDepositsLabel = tk.Label(text="Increase deposits in line with annual inflation?").grid(sticky='W')
        self.increaseDepositsDefaultVal = tk.StringVar(master)
        self.increaseDepositsDefaultVal.set("no")
        self.increaseDepositsChoice = tk.OptionMenu(master, self.increaseDepositsDefaultVal, "yes", "no").grid(sticky='W')
        self.annualInflationLabel = tk.Label(text="Annual inflation rate (%)").grid(sticky='W')
        self.annualInflationEntry = tk.Entry(master, width=3).grid(sticky='W')

        self.calculateButton = tk.Button(text="Calculate", command=self.calculateResult).grid(sticky='W')
        self.resultLabel = tk.Label(master, text="").grid(sticky='W')
        self.calculateAgainButton= tk.Button(text="Calculate Again", command=self.reset)

    def calculateResult(self):
        print("A")

    def calculateRegularDeposit(self):
        print("B")
        
    def calculateIncreasingDeposits(self):
        print("C")

    def reset(self):
        grid()
        print("D")

def main():
    window = tk.Tk()
    window.geometry("300x500")
    #window.configure(bg='#aaabb8')  #window background colour
    generator = interestCalculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
