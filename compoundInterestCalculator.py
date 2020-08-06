import tkinter as tk
from tkinter import messagebox

class interestCalculator():

    def __init__(self, master):
        self.master = master
        master.title = ("Compound Interest Calculator")

        #Title
        self.titleLabel = tk.Label(text="Compound Interest Calculator", font=("Times",16), width=24).grid(row=0,column=0,sticky='EW',pady=15)

        #Options
        self.initialAmountLabel = tk.Label(master, text="Initial Amount").grid(sticky='W')
        self.initialAmountFrame = tk.Frame(master)  #widgets are placed side by side in a frame
        self.initialAmountFrame.grid(row=2,sticky='NW',pady=6)
        self.poundSign1 = tk.Label(self.initialAmountFrame, text="£")
        self.poundSign1.grid(row=0,column=0)
        self.initialAmount =tk.IntVar()
        self.initialAmountEntry = tk.Entry(self.initialAmountFrame, textvariable=self.initialAmount, width=8)
        self.initialAmountEntry.grid(row=0,column=1)
        self.initialAmountEntry.bind("<1>", self.initialAmountEntryClick)

        self.interestRateLabel = tk.Label(text="Yearly Interest Rate").grid(sticky='W')
        self.interestRateFrame = tk.Frame(master)
        self.interestRateFrame.grid(row=4,sticky='NW',pady=6)
        self.interestRate = tk.IntVar()
        self.interestRateEntry = tk.Entry(self.interestRateFrame, textvariable=self.interestRate, width=3)
        self.interestRateEntry.grid(row=0,column=0,padx=4)
        self.interestRateEntry.bind("<1>", self.interestRateEntryClick)
        self.percentSign1 = tk.Label(self.interestRateFrame, text="%")
        self.percentSign1.grid(row=0,column=1)

        self.calcPeriodLabel = tk.Label(text="Calculation Period").grid(sticky='W')
        self.calcPeriodFrame = tk.Frame(master)
        self.calcPeriodFrame.grid(row=6,sticky='NW',pady=6)
        
        self.years = tk.IntVar()
        self.yearsEntry = tk.Entry(self.calcPeriodFrame, textvariable=self.years, width=3)
        self.yearsEntry.bind("<1>", self.yearsEntryClick)
        self.yearsLabel = tk.Label(self.calcPeriodFrame, text="years")
        
        self.months = tk.IntVar()
        self.monthsEntry = tk.Entry(self.calcPeriodFrame, textvariable=self.months, width=3)
        self.monthsEntry.bind("<1>", self.monthsEntryClick)
        self.monthsLabel = tk.Label(self.calcPeriodFrame, text="months")

        self.yearsEntry.grid(row=0,column=0,padx=4)
        self.yearsLabel.grid(row=0,column=1)
        self.monthsEntry.grid(row=0,column=2,padx=4)
        self.monthsLabel.grid(row=0,column=3)

        self.regularAmountLabel = tk.Label(text="Regular deposit/withdrawal").grid(sticky='W')
        self.regularAmountFrame = tk.Frame(master)
        self.regularAmountFrame.grid(row=10,sticky='NW',pady=6)
        self.regularAmountVar = tk.StringVar(master)
        self.regularAmountVar.set("no")
        self.regularAmountChoice = tk.OptionMenu(self.regularAmountFrame, self.regularAmountVar, "yes", "no", command=self.checkRegularAmount)   #command called when an option is selected
        self.regularAmountChoice.grid(row=0,column=0)                                                                                            #if yes is selected, the entry will become visible
        self.amountLabel = tk.Label(self.regularAmountFrame, text="Amount:")
        self.poundSign2 = tk.Label(self.regularAmountFrame, text="£")
        self.regularAmount = tk.IntVar()
        self.regularAmountEntry = tk.Entry(self.regularAmountFrame, textvariable=self.regularAmount, width=8)
        self.regularAmountEntry.bind("<1>", self.regularAmountEntryClick)

        self.increaseDepositsLabel = tk.Label(text="Increase deposits in line with annual inflation?").grid(sticky='W')
        self.increaseDepositsFrame = tk.Frame(master)
        self.increaseDepositsFrame.grid(row=12,sticky='NW',pady=6)
        self.increaseDepositsVar = tk.StringVar(master)
        self.increaseDepositsVar.set("no")
        self.increaseDepositsChoice = tk.OptionMenu(self.increaseDepositsFrame, self.increaseDepositsVar, "yes", "no", command=self.checkIncreaseDeposits)   #command called when an option is selected
        self.increaseDepositsChoice.grid(row=0,column=0)                                                                                                            #if yes is selected, the label, entry and % sign will become visible
        self.annualInflationLabel = tk.Label(self.increaseDepositsFrame, text="Annual inflation rate:")
        self.annualInflation = tk.IntVar()
        self.annualInflationEntry = tk.Entry(self.increaseDepositsFrame, textvariable=self.annualInflation, width=3)
        self.annualInflationEntry.bind("<1>", self.annualInflationEntryClick)
        self.percentSign2 = tk.Label(self.increaseDepositsFrame, text="%")

        self.calculateButton = tk.Button(master, text="Calculate", command=self.verifyValues)
        self.calculateButton.grid(sticky='NW',pady=6)
        self.resultLabel = tk.Label(master, text="").grid(sticky='W')
        self.calculateAgainButton= tk.Button(master, text="Calculate Again", command=self.reset)

    #checkRegularAmount and checkIncreaseDeposits
    #add extra widgets onto the screen if the menuoption variable is yes
    #remove the extra widgets if not
    def checkRegularAmount(self, value):
        if value == "no":
            self.amountLabel.grid_forget()
            self.poundSign2.grid_forget()
            self.regularAmountEntry.grid_forget()
            
        else:
            self.amountLabel.grid(row=0,column=1)
            self.poundSign2.grid(row=0,column=2)
            self.regularAmountEntry.grid(row=0,column=3)

    def checkIncreaseDeposits(self, value):
        if value == "no":
            self.annualInflationLabel.grid_forget()
            self.annualInflationEntry.grid_forget()
            self.percentSign2.grid_forget()
            
        else:
            self.annualInflationLabel.grid(row=0,column=1)
            self.annualInflationEntry.grid(row=0,column=2)
            self.percentSign2.grid(row=0,column=3)

    #Verifies the values of all entry boxes
    #If an error is found, the entry background becomes red
    def verifyValues(self):

        #Verifying that values are ints
        try:
            self.initialAmount.get()
        except:
            messagebox.showerror("Error", "Enter a number for the initial amount")
            self.initialAmount.set(0)
            self.initialAmountEntry.configure(bg='#D54323')
            return
            
        try:
            self.interestRate.get()
        except:
            messagebox.showerror("Error", "Enter a number for the yearly interest rate")
            self.interestRate.set(0)
            self.interestRateEntry.configure(bg='#D54323')
            return
            
        try:
            self.years.get()
        except:
            messagebox.showerror("Error", "Enter a number for the number of years")
            self.years.set(0)
            self.yearsEntry.configure(bg='#D54323')
            return

        try:
            self.months.get()
        except:
            messagebox.showerror("Error", "Enter a number for the number of months")
            self.months.set(0)
            self.monthsEntry.configure(bg='#D54323')
            return

        try:
            self.regularAmount.get()
        except:
            messagebox.showerror("Error", "Enter a number for the regular deposit/withdrawal amount")
            self.regularAmount.set(0)
            self.regularAmountEntry.configure(bg='#D54323')
            return

        try:
            self.annualInflation.get()
        except:
            messagebox.showerror("Error", "Enter a number for the annual inflation")
            self.annualInflation.set(0)
            self.annualInflationEntry.configure(bg='#D54323')
            return

        #Verifying that values are between/higher than a certain number(s) 
        try:
            if self.initialAmount.get() > 0:

                if self.years.get() >= 0:

                    if self.months.get() >= 0 and self.months.get() <=12 :

                        if self.regularAmount.get() >= 0:
                            self.calculateResult()

                        else:
                            messagebox.showerror("Error", "Enter a number greater than 0 for the regular amount")
                            self.regularAmount.set(0)
                            self.regularAmountEntry.configure(bg='#D54323')
                            return

                    else:
                        messagebox.showerror("Error", "Enter a number greater than or equal to 0 and less than 12 for the number of months")
                        self.months.set(0)
                        self.monthsEntry.configure(bg='#D54323')
                        return

                else:
                    messagebox.showerror("Error", "Enter a number greater than or equal to 0 for the number of years")
                    self.years.set(0)
                    self.yearsEntry.configure(bg='#D54323')
                    return
                
            else:
                messagebox.showerror("Error", "Enter a number greater than 0 for the initial amount")
                self.initialAmount.set(0)
                self.initialAmountEntry.configure(bg='#D54323')
                return

        except:
            return

    #These 6 functions change the background of an entry back to white when the user clicks on or types in it
    def initialAmountEntryClick(self, event):
        if self.initialAmountEntry['bg'] == '#D54323':
            self.initialAmountEntry.configure(bg='#FFFFFF')

    def interestRateEntryClick(self, event):
        if self.interestRateEntry['bg'] == '#D54323':
            self.interestRateEntry.configure(bg='#FFFFFF')

    def yearsEntryClick(self, event):
        if self.yearsEntry['bg'] == '#D54323':
            self.yearsEntry.configure(bg='#FFFFFF')

    def monthsEntryClick(self, event):
        if self.monthsEntry['bg'] == '#D54323':
            self.monthsEntry.configure(bg='#FFFFFF')

    def regularAmountEntryClick(self, event):
        if self.regularAmountEntry['bg'] == '#D54323':
            self.regularAmountEntry.configure(bg='#FFFFFF')

    def annualInflationEntryClick(self, event):
        if self.annualInflationEntry['bg'] == '#D54323':
            self.annualInflationEntry.configure(bg='#FFFFFF')

    def calculateResult(self):
        self.calculateButton.grid_forget()
        self.calculateAgainButton.grid(sticky='W')

        self.initialAmountEntry.configure(bg='#FFFFFF')
        self.interestRateEntry.configure(bg='#FFFFFF')
        self.yearsEntry.configure(bg='#FFFFFF')
        self.monthsEntry.configure(bg='#FFFFFF')
        self.regularAmountEntry.configure(bg='#FFFFFF')
        self.annualInflationEntry.configure(bg='#FFFFFF')

        #if self.regularAmountVar == "yes":
        #if self.increaseDepositsVar == "yes":
            

    def calculateRegularDeposit(self):
        print("B")
        
    def calculateIncreasingDeposits(self):
        print("C")

    def reset(self):
        self.calculateButton.grid(row=13,sticky='W')
        self.calculateAgainButton.grid_forget()

def main():
    window = tk.Tk()
    window.geometry("300x500")
    generator = interestCalculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
