from tkinter import *

# actions

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_results_label.config(text=f"{km}")

window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=20, pady=20)

# UI elements
miles_input = Entry(width=7)
miles_label = Label(text='Miles')
is_equal_label = Label(text='is equal to')
kilometer_results_label = Label(text='0')
kilometer_label = Label(text='Km')
calculate_button = Button(text='Calculate', command=miles_to_km)

# UI element placement
miles_input.grid(column=1, row= 0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
kilometer_results_label.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)






































window.mainloop()