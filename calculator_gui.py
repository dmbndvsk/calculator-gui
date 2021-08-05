from tkinter import *


class Calculator:

    def __init__(self, master):

        """
        DOCSTRING: Define what to do on initialization
        """

        # Reference to the main window of the application
        self.master = master

        # Name of application
        master.title("Calculator")

        # Line where we display the equation
        self.equation = Entry(master, width=36, borderwidth=5)

        # Position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Execute the .create_button() method
        self.create_button()

    def create_button(self):

        """
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        """

        # Buttons using add_button() method
        b0 = self.add_button(0)
        b1 = self.add_button(1)
        b2 = self.add_button(2)
        b3 = self.add_button(3)
        b4 = self.add_button(4)
        b5 = self.add_button(5)
        b6 = self.add_button(6)
        b7 = self.add_button(7)
        b8 = self.add_button(8)
        b9 = self.add_button(9)
        b_add = self.add_button('+')
        b_sub = self.add_button('-')
        b_multi = self.add_button('*')
        b_div = self.add_button('/')
        b_clear = self.add_button('c')
        b_equal = self.add_button('=')

        # Arrange the buttons into lists which represent calculator rows
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_multi]
        row4 = [b_clear, b0, b_equal, b_div]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for button in row:
                button.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def add_button(self, value):

        """
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        """
        return Button(self.master, text=value, height=3, width=9, command=lambda: self.click_button(str(value)))

    def click_button(self, value):

        """
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        """

        # Get the equation that's entered by the user
        current_equation = str(self.equation.get())

        # If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, END)

        # If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        # If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation + value)


# Execution
if __name__ == '__main__':
    # Create the main window of an application
    root = Tk()

    # Tell our calculator class to use this window
    my_gui = Calculator(root)

    # Executable loop on the application, waits for user input
    root.mainloop()
