from tkinter import *
from tkinter import ttk

# Function to add a digit to the display
def add_digit(digit):
    value = display.get()
    if value == "0":
        value = digit
    else:
        value += digit
    display.delete(0, END)
    display.insert(0, value)

# Function to add an operator to the display
def add_operator(operator):
    global first_num
    first_num = int(display.get())
    global math_operator
    math_operator = operator
    display.delete(0, END)

# Function to calculate the result
def calculate():
    try:
        second_num = int(display.get())
        display.delete(0, END)
        if math_operator == "+":
            result = first_num + second_num
        elif math_operator == "-":
            result = first_num - second_num
        elif math_operator == "*":
            result = first_num * second_num
        elif math_operator == "/":
            if second_num == 0:
                raise ZeroDivisionError("Division by zero!")
            result = first_num / second_num
        else:
            result = first_num  # For cases where operator is not specified
        display.insert(0, result)
    except ValueError:
        display.insert(0, "Error: Invalid input")
    except ZeroDivisionError as e:
        display.insert(0, f"Error: {e}")

# Function to clear the display
def clear():
    display.delete(0, END)
    display.insert(0, "0")

# Button click function
def button_click(text):
    if text.isdigit() or text == ".":
        add_digit(text)
    elif text in ["+", "-", "*", "/"]:
        add_operator(text)
    elif text == "=":
        calculate()
    elif text == "C":
        clear()

# Create the main window
root = Tk()
root.title("Calculator")
root.geometry("275x320")

# Create a frame for the calculator
frame = ttk.Frame(root, borderwidth=2, relief="groove")
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Create the display widget
display = ttk.Entry(frame, font=("Helvetica", 20), justify=RIGHT)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

# Create the buttons
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

for text, row, column in buttons:
    button = ttk.Button(frame, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# Configure row and column weights to make buttons expand
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
