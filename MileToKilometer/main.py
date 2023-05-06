import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=100, height=50)
window.config(pady=20)

# Labels
label1 = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
label1.grid(row=1, column=0)


label_miles = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
label_miles.grid(row=0, column=2)

label_km = tkinter.Label(text="0", font=("Arial", 10, "bold"))
label_km.grid(row=1, column=1)

label2 = tkinter.Label(text="Kilometers", font=("Arial", 10, "bold"))
label2.grid(row=1, column=2)


# Button
def miles_to_km():
    label_km.config(text=float(user_input.get())*1.609344)


button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

# Entry
user_input = tkinter.Entry(width=20, justify='center')
user_input.grid(row=0, column=1)

window.mainloop()
