"""
Chapter 8 practice project
Program: salaryCalculatorGUI.py
1/25/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the Salary Calculator. User enters Hourly wage and number of hours worked and then outputs the employee's total salary.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

    # Definition of our classes' constructor method 
    def __init__(self):
        # Call to the EasyFrame class constructor
        EasyFrame.__init__(self, title = "Salary Calculator 2.0", width = 400, height = 200, resizable = True, background = "yellow")

        # Variable to store a Font design for multiple labels
        labelFont = Font(family = "Georgia", size = 14)

        # add the widgets to the window
        self.addLabel(text = "Salary Calculator", row = 0, column = 0, sticky = "NEWS", columnspan = 2, background = "yellow", foreground = "blue4", font = Font(family = "Terminal", size = 20, weight = "bold"))
        self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "yellow", foreground = "blue2", font = labelFont)
        self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, background = "yellow", foreground = "blue2", font = labelFont)
        self.wage = self.addFloatField(value = 0.0, row = 1, column = 1)
        self.hoursWorked = self.addIntegerField(value = 0, row = 2, column = 1)

        # Bind the hoursWorked to the press of the enter key event
        self.hoursWorked.bind("<Return>", lambda event: self.compute())

        self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
        self.button["background"] = "palegoldenrod"
        self.button["width"] = 15

        self.addLabel(text = "The Employee's Salary is: ", row = 4, column = 0, background = "yellow", font = labelFont, foreground = "red4")
        self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")

    # Definition of the compute() function which is the event handler
    def compute(self):
        wage = self.wage.getNumber()
        hours = self.hoursWorked.getNumber()
        salary = wage * hours
        self.outputField.setNumber(salary)

    


        
       



# Global definition of the main() method
def main():
    # Instantiate an object from a class into mainloop()
    SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()