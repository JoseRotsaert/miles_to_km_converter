import tkinter

USERFONT =("Arial", 16, "normal")

def button_click():
    inputmiles = round(int(input_miles.get())*1.609344,2)
    label_km_result.config(text=inputmiles)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles", font=USERFONT)
label_miles.grid(column=2, row=0)

label_txtisequalto = tkinter.Label(text="is equal to", font=USERFONT)
label_txtisequalto.grid(column=0, row=1)

label_km_result = tkinter.Label(font=USERFONT)
label_km_result.grid(column=1, row=1)

label_txtkm = tkinter.Label(text="Km", font=USERFONT)
label_txtkm.grid(column=2, row=1)

button_calculate = tkinter.Button(text="Calculate", command = button_click)
button_calculate.grid(column=1, row=2)


window.mainloop()
