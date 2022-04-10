import tkinter as tk
import csv
from tkinter import ttk
import pandas as pd
from tkinter import PhotoImage
from tkinter import messagebox

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=310, height=750)

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
    global df
    df = pd.read_csv("Bus_dataset.csv")

    bus_stand_name = starting_stop.get()
    user_time_zone = str(hrs.get().zfill(2)) + str(min.get().zfill(2))

    global start_time
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

    avail_buses = []
    for i in temp:
        a = i
        if int(a.replace(":", "")) >= int(user_time_zone):
            avail_buses.append(i)
    global bus_select
    bus_select = tk.StringVar()

    frame3 = ScrollableFrame(main_win)
    for i in avail_buses:
        temp = ttk.Radiobutton(frame3.scrollable_frame, text=i, value=i, variable=bus_select, padding=5,style="TRadiobutton")
        style.configure('TRadiobutton', font=("Segoe UI", 14), foreground='black')
        temp.pack()

    frame3.place(x=1100, y=40)

    calc_button = ttk.Button(main_win, text="Calculate Estimated Time", style="TButton", command=calc)
    calc_button.place(x=750, y=500)


def calc():
    try:
        Select_time = bus_select.get()
        Ending_stop = dest_stop.get()

        end_time = []
        for i in df.index:
            a = df.loc[i, "Bus Stand Names"]
            if a == Ending_stop:
                end_time.append(df.iloc[i])

        temp = []
        for i in end_time:
            for j in range(1, len(i)):
                temp.append(i[j])
        end_time = temp

        # In[108]:

        col_val = start_time.index(Select_time)
        start = start_time[col_val].split(":")
        end = end_time[col_val].split(":")
        est_time = []
        for i in range(2):
            est_time.append(int(end[i]) - int(start[i]))
        est_time_label.configure(text=f"Estimated time: {abs(est_time[0])} hour(s) and {abs(est_time[1])} minute(s)")
        print(f"Estimated time is {abs(est_time[0])} hour(s) and {abs(est_time[1])} minutes")
    except:
        messagebox.showerror("Invalid Input", "Invalid Input")




main_win = tk.Tk()
main_win.geometry("1300x800")
main_win.title("Bus")

bg = PhotoImage(file = "bus image.png")
canvas1 = tk.Canvas( main_win, width = 400,height = 400)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")


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

starting_stop = tk.StringVar()
dest_stop = tk.StringVar()

frame = ScrollableFrame(main_win, borderwidth=0)
#frame.place(x=10,y=10)

style = ttk.Style()

for i in stand_names:
    bus = ttk.Radiobutton(frame.scrollable_frame, text=i, value=i, variable=starting_stop, padding=5, style="TRadiobutton")
    style.configure('TRadiobutton', font=("Segoe UI", 14), foreground='black')
    #bus.place(x=X, y=Y)
    # if X >= 1100:
    #     X = 10
    #     Y += 60
    # else:
    #     X += 160
    bus.pack()


frame2 = ScrollableFrame(main_win, borderwidth=0)
#frame2.place(x=400,y=10)

# separator = ttk.Separator(main_win, orient="vertical").grid(row=0,column=2,rowspan=4, ipady=500, sticky='ns')
# separator2 = ttk.Separator(main_win, orient="vertical").grid(row=0,column=10,rowspan=4, ipady=500, sticky='ns')

#separator.pack(fill='y')

for i in stand_names:
    bus2 = ttk.Radiobutton(frame2.scrollable_frame, text=i, value=i, variable=dest_stop, padding=5, style="TRadiobutton")
    style.configure('TRadiobutton', font=("Segoe UI", 14), foreground='black')
    #bus.place(x=X, y=Y)
    # if X >= 1100:
    #     X = 10
    #     Y += 60
    # else:
    #     X += 160
    bus2.pack()


# ENTERING TIME
#style.configure("TSpinbox", arrowsize=200)

starting_label = tk.Label(main_win, text="Starting stop",font=("Helvetical Bold", 25))
dest_label = tk.Label(main_win, text="Destination stop",font=("Helvetical Bold", 25))

time = tk.Label(main_win, text="Select Boarding Time",font=("Helvetical Bold", 25))
time.place(x=700,y=0)

avail_buses = tk.Label(main_win, text="Available Buses",font=("Helvetical Bold", 25))
avail_buses.place(x=1050,y=0)

est_time_label = tk.Label(main_win, text=f"Estimated time: ",
                          font=("Segoe UI", 15))
est_time_label.place(x=700, y=200)

hrs = tk.Spinbox(main_win, from_=0, to=23,  width=4, wrap=True, font=("Segoe UI", 15))
hrs_label = tk.Label(main_win, text="HH               MM", font=("Segoe UI", 15))
hrs_label.place(x=760,y=40)
hrs.place(x=760, y=80)
colon = tk.Label(main_win, text=":", font=("Helvetical Bold", 25))
colon.place(x=830,y=70)
min = tk.Spinbox(main_win, from_=0, to=59, width=4, wrap=True, font=("Segoe UI", 15))
min.place(x=850, y=80)




submit = ttk.Button(main_win, text="Submit", command=calcTime, style="TButton")
submit.place(x=785,y=140)

style.configure("TButton", font=("Segoe UI", 12))

starting_label.grid(row=0, column=0)
frame.grid(row=1, column=0)
canvas1.grid(row=0, column=0, padx=0, pady=0, rowspan=10, columnspan=10, sticky='ew')
frame2.grid(row=1, column=1)
dest_label.grid(row=0, column=1)
#separator.grid(rowspan=5, column=1, sticky='ew')





main_win.mainloop()
