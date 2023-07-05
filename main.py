from tkinter import *


def button_clicked():
    miles = miles_input.get()
    kilometers = int(miles) * 1.609
    my_label4.config(text=kilometers)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=450, height=200)
window.config(padx=100, pady=50)

# Label - is equal to
my_label = Label(text="is equal to", font=("Arial", 12))
my_label.grid(column=0, row=1)

# Label - Miles
my_label2 = Label(text="Miles", font=("Arial", 12))
my_label2.grid(column=2, row=0)

# Label - Km
my_label3 = Label(text="Km", font=("Arial", 12))
my_label3.grid(column=2, row=1)

# Label - Km Output
my_label4 = Label(text="0", font=("Arial", 12, "italic"))
my_label4.grid(column=1, row=1)

# Button - Calculate
button = Button(text="Calculate", command=button_clicked,font=("Arial", 12, "bold"))
button.grid(column=1, row=3)

# Entry - Input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

window.mainloop()
