from tkinter import *
import tkinter

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)




#Label 'is equal to'
my_label = Label(text="is equal to", font=("Courier", 12, "normal"))
#my_label.config(text="New Text ")
my_label.grid(column=0, row=2)

#Entry
input = Entry(window, width=10, justify='center')
input.grid(column=1, row=1)
print(input.get())

def button_clicked():
    text = input.get()
    print(text)
    result_label.config(text=f"{float(text) * 1.60934}")



#Button 'calculate'
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

#Label 'Miles'
my_label = Label(text="Miles", font=("Courier", 12, "normal"))
#my_label.config(text="New Text ")
my_label.grid(column=2, row=1)

#Label 'km'
my_label = Label(text="Km", font=("Courier", 12, "normal"))
#my_label.config(text="New Text ")
my_label.grid(column=2, row=2)

#Label for displaying result
result_label = Label(text="0", font=("Courier", 12, "normal"))
result_label.grid(column=1, row=2)
result_label.config(padx=25, pady=25)









window.mainloop()

