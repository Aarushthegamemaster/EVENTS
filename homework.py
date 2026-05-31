from tkinter import *
from tkinter import messagebox

# Function to convert centimeters to inches
def convert():
    try:
        cm = float(centimeters.get())
        inch_value = cm / 2.54
        result_label.config(text=f"The value in inches is {round(inch_value, 2)}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")


# Main window
window = Tk()
window.title("US and Metric Converter")
window.geometry("300x300")

# Input field
Label(text="Enter value in centimeters").pack(pady=5)

centimeters = Entry()
centimeters.pack(pady=5)

# Button
convert_button = Button(text="Convert", command=convert)
convert_button.pack(pady=10)

# Result label
result_label = Label(text="The value in inches is ")
result_label.pack(pady=10)

window.mainloop()