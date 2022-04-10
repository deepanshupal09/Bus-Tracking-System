import tkinter as tk
import csv
from tkinter import ttk
import pandas as pd

def getScript(name):
    print(name)




class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=500, height=900)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=False)
        scrollbar.pack(side="right", fill="y")

def calcTime():
    df = pd.read_csv("Bus_dataset.csv")

    bus_stand_name = bus_name.get()
    user_time_zone = str(hrs.get().zfill(2)) + str(min.get().zfill(2))


    start_time = []
    for i in df.index:
        a = df.loc[i, "Bus Stand Names"]
        if a == bus_stand_name:
            start_time.append(df.iloc[i])

    temp = []
    for i in start_time:
        for j in range(1, len(i)):
            temp.append(i[j])
    start_time = temp

    print("Bus Timings are:- ")
    for i in temp:
        a = i
        if int(a.replace(":", "")) >= int(user_time_zone):
            print(i)


main_win = tk.Tk()
main_win.geometry("1600x900")
main_win.title("Bus")

bus_stop = open("Bus_dataset.csv", "r")
reader = csv.reader(bus_stop)
temp = list(reader)
stand_names = []


for i in range(1,len(temp)):
    stand_names.append(temp[i][0])


btns = []
X,Y = 10,20

# for i in stand_names:
#     tempBtn = ttk.Button(main_win, text=i, command=main_win.destroy, width=30)
#     tempBtn.place(x=X, y=Y)
#     btns.append(tempBtn)
#     if X >= 1100:
#         X = 10
#         Y += 60
#     else:
#         X += 265
#

bus_name = tk.StringVar()

frame = ScrollableFrame(main_win, borderwidth=0)
frame.place(x=10,y=10)

style = ttk.Style()

for i in stand_names:
    bus = ttk.Radiobutton(frame.scrollable_frame, text=i, value=i, variable=bus_name, padding=5, style="TRadiobutton", command=lambda: getScript(i))
    style.configure('TRadiobutton', font=("Segoe UI", 14), foreground='black')
    #bus.place(x=X, y=Y)
    # if X >= 1100:
    #     X = 10
    #     Y += 60
    # else:
    #     X += 160
    bus.pack()

# ENTERING TIME

hrs = ttk.Spinbox(main_win, from_=0, to=23, state='readonly', width=4)
hrs.place(x=160, y=300)
colon = tk.Label(main_win, text=":", font=("Helvetical Bold", 15))
colon.place(x=210,y=294)
min = ttk.Spinbox(main_win, from_=0, to=59, state='readonly', width=4)
min.place(x=230, y=300)



submit = ttk.Button(main_win, text="Submit", command=calcTime)
submit.place(x=1100,y=800)



main_win.mainloop()
