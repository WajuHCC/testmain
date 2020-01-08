import tkinter
from weather import weather_report

root = tkinter.Tk()
label = tkinter.Label(master=root, text="Wpisz lokalizację: ")
label.grid(row=1, column=1)
# label.pack()

pole = tkinter.Entry(master=root)
pole.grid(row=1, column=2)

button = tkinter.Button(master=root, text="Sprawdz", command=weather_report)
button.grid(row=2, column=1)

wynik1 = tkinter.Label(master=root, text="Pogoda dla lokalizacji: ")
wynik1.grid(row=3, column=1)

wynik2 = tkinter.Label(master=root, text=pole)
wynik2.grid(row=3, column=2)





root.mainloop()
