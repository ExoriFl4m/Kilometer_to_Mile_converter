from tkinter import *


def button_clicked():
    measure = measure_input.get()
    if radio_state.get() == 1:
        kilometers = round(int(measure) * 1.609, 2)
        my_label4.config(text=kilometers)
    if radio_state.get() == 2:
        miles = round(int(measure) / 1.609, 2)
        my_label4.config(text=miles)


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

# Buttons to select Km's or Miles
def radio_used():
    if radio_state.get() == 1:
        my_label3.grid(column=2, row=1)
        my_label2.grid(column=2, row=0)
    if radio_state.get() == 2:
        my_label3.grid(column=2, row=0)
        my_label2.grid(column=2, row=1)


radio_state = IntVar(value=1)    
radiobutton1 = Radiobutton(text="Convert Miles to Kilometers.", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Convert Kilometers to Miles.", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=4)
radiobutton2.grid(column=1, row=5)

# Entry - Input
measure_input = Entry(width=7)
measure_input.grid(column=1, row=0)

window.mainloop()
