from tkinter import *


def convert_miles_to_km():
    """Converts miles to kilometers and prints the result in the window."""
    mile_as_km = 1.609344
    user_miles = float(miles_input.get())
    converted_kilometers = mile_as_km * user_miles
    kilometer_result_label.config(text=round(converted_kilometers))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(padx=10, pady=10)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=3, row=1)
kilometer_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
