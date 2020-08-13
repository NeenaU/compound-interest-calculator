import tkinter as tk
from tkinter import messagebox

class interestCalculator():

    def __init__(self, master):
        self.master = master
        master.title = ("Compound Interest Calculator")

        #Title
        self.titleLabel = tk.Label(text="Compound Interest Calculator", font=("Times",16), width=24).grid(row=0,column=0,sticky='EW',pady=15)

        #Option widgets
        self.initialAmountLabel = tk.Label(master, text="Initial Amount").grid(sticky='W')
        self.initialAmountFrame = tk.Frame(master)  #widgets are placed side by side in a frame
        self.initialAmountFrame.grid(row=2,sticky='NW',pady=6)
        self.poundSign1 = tk.Label(self.initialAmountFrame, text="£")
        self.poundSign1.grid(row=0,column=0)
        self.initialAmount = tk.IntVar()
        self.initialAmount.trace("w", self.initialAmountEntryClick)
        self.initialAmountEntry = tk.Entry(self.initialAmountFrame, textvariable=self.initialAmount, width=8)
        self.initialAmountEntry.grid(row=0,column=1)
        self.initialAmountEntry.bind("<1>", self.initialAmountEntryClick)

        self.interestRateLabel = tk.Label(text="Yearly Interest Rate").grid(sticky='W')
        self.interestRateFrame = tk.Frame(master)
        self.interestRateFrame.grid(row=4,sticky='NW',pady=6)
        self.interestRate = tk.IntVar()
        self.interestRate.trace("w", self.interestRateEntryClick)
        self.interestRateEntry = tk.Entry(self.interestRateFrame, textvariable=self.interestRate, width=3)
        self.interestRateEntry.grid(row=0,column=0,padx=4)
        self.interestRateEntry.bind("<1>", self.interestRateEntryClick)
        self.percentSign1 = tk.Label(self.interestRateFrame, text="%")
        self.percentSign1.grid(row=0,column=1)

        self.timePeriodLabel = tk.Label(text="Time Period").grid(sticky='W')
        self.timePeriodFrame = tk.Frame(master)
        self.timePeriodFrame.grid(row=6,sticky='NW',pady=6)
        self.timePeriod = tk.IntVar()
        self.timePeriod.trace("w", self.timePeriodEntryClick)
        self.timePeriodEntry = tk.Entry(self.timePeriodFrame, textvariable=self.timePeriod, width=3)
        self.timePeriodEntry.bind("<1>", self.timePeriodEntryClick)
        self.timePeriodVar = tk.StringVar(master)
        self.timePeriodVar.set("years")
        self.timePeriodChoice = tk.OptionMenu(self.timePeriodFrame, self.timePeriodVar, "years", "months")
        self.timePeriodChoice.grid(row=0,column=0)    
        self.timePeriodEntry.grid(row=0,column=0,padx=4)
        self.timePeriodChoice.grid(row=0,column=1)

        self.compoundIntervalLabel = tk.Label(text="Compound Interval").grid(sticky='W')
        self.compoundIntervalVar = tk.StringVar(master)
        self.compoundIntervalVar.set("yearly")
        self.compoundIntervalChoice = tk.OptionMenu(master, self.compoundIntervalVar, "yearly", "monthly", "weekly", "daily")
        self.compoundIntervalChoice.grid(sticky='W',pady=6)

        self.regularAmountLabel = tk.Label(text="Regular monthly deposit").grid(sticky='W')
        self.regularAmountFrame = tk.Frame(master)
        self.regularAmountFrame.grid(row=10,sticky='NW',pady=6)
        self.regularAmountVar = tk.StringVar(master)
        self.regularAmountVar.set("no")
        self.regularAmountChoice = tk.OptionMenu(self.regularAmountFrame, self.regularAmountVar, "yes", "no", command=self.checkRegularAmount)   #command called when an option is selected
        self.regularAmountChoice.grid(row=0,column=0)                                                                                            #if yes is selected, the entry will become visible
        self.amountLabel = tk.Label(self.regularAmountFrame, text="Amount:")
        self.poundSign2 = tk.Label(self.regularAmountFrame, text="£")
        self.regularAmount = tk.IntVar()
        self.regularAmount.trace("w", self.regularAmountEntryClick)
        self.regularAmountEntry = tk.Entry(self.regularAmountFrame, textvariable=self.regularAmount, width=8)
        self.regularAmountEntry.bind("<1>", self.regularAmountEntryClick)

        self.calculateButton = tk.Button(master, text="Calculate", command=self.verifyValues)
        self.calculateButton.grid(sticky='NW',pady=6)
        self.resultText = tk.Text(master, state='disabled', width=37, height=6)
        self.resultText.grid(sticky='NW',pady=6)
        self.resetButton= tk.Button(master, text="Reset", command=self.reset)

    #checkRegularAmount, checkIncreaseDeposits and checkTimePeriod
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
            self.timePeriod.get()
        except:
            messagebox.showerror("Error", "Enter a number for the time period")
            self.timePeriod.set(0)
            self.timePeriodEntry.configure(bg='#D54323')
            return

        try:
            self.regularAmount.get()
        except:
            messagebox.showerror("Error", "Enter a number for the regular deposit amount")
            self.regularAmount.set(0)
            self.regularAmountEntry.configure(bg='#D54323')
            return

        #Verifying that values are between/higher than a certain number(s) 
        try:
            if self.initialAmount.get() >= 0:

                if (self.timePeriodVar.get() == "years" and self.timePeriod.get() > 0) or (self.timePeriodVar.get() == "months" and self.timePeriod.get() > 0):

                    if self.timePeriodVar.get() == "months" and self.timePeriod.get() > 12:

                        messagebox.showerror("Error", "Enter a number less than 12 for the number of months")
                        self.regularAmount.set(0)
                        self.timePeriodEntry.configure(bg='#D54323')
                        return
                        
                    else:
                        
                        if self.regularAmount.get() >= 0:
                            self.calculateResult()

                        else:
                            messagebox.showerror("Error", "Enter a number greater than 0 for the regular amount")
                            self.regularAmount.set(0)
                            self.regularAmountEntry.configure(bg='#D54323')
                            return

                else:
                    messagebox.showerror("Error", "Enter a number greater than or equal to 0 for the time period")
                    self.timePeriod.set(0)
                    self.timePeriodEntry.configure(bg='#D54323')
                    return
                
            else:
                messagebox.showerror("Error", "Enter a number greater than or equal to 0 for the initial amount")
                self.initialAmount.set(0)
                self.initialAmountEntry.configure(bg='#D54323')
                return

        except:
            return

    #These 6 functions change the background of an entry back to white when the user clicks on or types in it
    def initialAmountEntryClick(self, *args):
        if self.initialAmountEntry['bg'] == '#D54323':
            self.initialAmountEntry.configure(bg='#FFFFFF')

    def interestRateEntryClick(self, *args):
        if self.interestRateEntry['bg'] == '#D54323':
            self.interestRateEntry.configure(bg='#FFFFFF')

    def timePeriodEntryClick(self, *args):
        if self.timePeriodEntry['bg'] == '#D54323':
            self.timePeriodEntry.configure(bg='#FFFFFF')

    def monthsEntryClick(self, *args):
        if self.monthsEntry['bg'] == '#D54323':
            self.monthsEntry.configure(bg='#FFFFFF')

    def regularAmountEntryClick(self, *args):
        if self.regularAmountEntry['bg'] == '#D54323':
            self.regularAmountEntry.configure(bg='#FFFFFF')

    def calculateResult(self):
        self.calculateButton.grid_forget()
        self.resetButton.grid(sticky='NW',row=11,pady=6)

        #Principal balance
        p = self.initialAmount.get()

        #Interest rate
        r = self.interestRate.get() / 100

        #n = number of times interest applied per time period
        if self.compoundIntervalVar.get() == "yearly":
            n = 1
        elif self.compoundIntervalVar.get() == "monthly":
            n = 12
        elif self.compoundIntervalVar.get() == "weekly":
            n = 52
        elif self.compoundIntervalVar.get() == "daily":
            n = 365

        #t = time periods elapsed
        if self.timePeriodVar.get() == "years":
            t = self.timePeriod.get()
        else:
            t = self.timePeriod.get() / 12

        #Calculate compound interest
        result = round(p * (1 + (r/n)) ** (n*t), 2)

        #Include amount made/lost from monthly deposits and calculate interest gained
        interestGained = 0
        if self.regularAmountVar.get() == "yes":
            d = self.regularAmount.get() #regular deposit amount
            interestFromDeposits = round(d * (((1+(r/12))**(12*t)-1)/(r/12)) * (1+r/12),2)
            result += interestFromDeposits

            timeInMonths = 0
            if self.timePeriodVar.get() == "years":
                timeInMonths = t*12
            else:
                timeInMonths = t
            
            earningsFromDeposits = d * timeInMonths
            interestGained = round(result - p - earningsFromDeposits, 2)

        else:
            interestGained = round(result - p, 2)

        
        if self.timePeriodVar.get() == "years":
            textForResultText = "You started with £" + str(p) + "\nYou ended with £" + str(result) + " over " + str(t) + " years\nYou gained £" + str(interestGained) + " in interest"
        else:
            textForResultText = "You started with £" + str(p) + "\nYou ended with £" + str(result) + " over " + str(int(t*12)) + " months\nYou gained £" + str(interestGained) + " in interest"
        

        self.resultText.configure(state='normal')
        self.resultText.insert(tk.INSERT, textForResultText)

        if self.regularAmountVar.get() == "yes":
            depositsText = "\nYou also deposited £" + str(earningsFromDeposits) + " \nYou earned £" + str(interestFromDeposits) + " in interest from \nyour deposits"
            self.resultText.insert(tk.INSERT, depositsText)

        self.resultText.configure(state='disabled')

    def reset(self):
        self.regularAmount.set(0)
        self.interestRate.set(0)
        self.timePeriod.set(0)
        self.initialAmount.set(0)
        
        self.timePeriodVar.set("years")
        self.compoundIntervalVar.set("yearly")
        self.regularAmountVar.set("no")

        self.resetButton.grid_forget()
        self.calculateButton.grid(row=11,sticky='NW',pady=6)
        
        self.resultText.configure(state='normal')
        self.resultText.delete(1.0, tk.END)
        self.resultText.configure(state='disabled')
        
        

def main():
    window = tk.Tk()
    
    w = 300
    h = 500
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    generator = interestCalculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()
