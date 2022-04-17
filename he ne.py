import tkinter as tk
import tkinter.font
from tkinter import ttk
from PIL import ImageTk, Image
import random, math, csv
from tkinter import messagebox

# def get_current_value():
#     return '{: .2f}'.format(slider.get())

global s_no
global sinthetan, wavelength, dn, current_order, current_N
s_no = 0
dn=0
sinthetan = 0
wavelength = 0
current_order = "NaN"
current_N = "NaN"

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        f = open("obs.csv", "w",newline='')
        f.close()
        main_win.destroy()
        obs_table.destroy()


def N_changed(event):
    #print(N_combo.get())
    N_label.configure(text=f'N: {N.get()}')

def order_changed(event):
    #print(N_combo.get())
    order_label.configure(text=f'N: {order.get()}')


def slider_changed(event):
    distance_label.configure(text=f"Distance from screen: {D.get()}")

    laser.place(x=600+(D.get() * 1.6), y=(300+(h.get() * 1.6)))

def height_changed(event):
    height_label.configure(text=f"Height: {-1 * h.get()}")
    laser.place(x=(600+(D.get()*1.6)), y=300+(h.get()*1.6))

def start():
    if -5 < h.get() < 5 and N.get() == '100' and order.get() == '1':
        pic3 = Image.open('example.jpg')
        pic2.paste(pic3, (0,0))
    else:
        pic3 = Image.open('example2.jpg')
        pic2.paste(pic3, (0,0))

def refresh(event):
    order_combo.set('1')
    N_label.configure(text=f"N: {N.get()}")
    order_label.configure(text="Order: 1")
    if N.get() == '600':
        order_combo['values'] = ('1')

    elif N.get() == '300':
        order_combo['values'] = ('1', '2')

    else:
        order_combo['values'] = ('1', '2', '3')


def calc():

    global s_no, current_order, current_N, dn, sinthetan, wavelength

    D = 100
    N_600 = [39, 40, 41]
    N_300 = [19.4, 19.5, 19.6, 19.7, 19.8, 19.9]
    N_100 = [6.4, 6.5, 6.6, 6.7, 6.8, 6.9]

    if N.get() == '600':
        dn = random.choice(N_600)
        sinthetan = dn/(math.sqrt(D**2 + dn**2))
        wavelength = 0.00166 * sinthetan * (10 ** 7)
        wavelength = round(wavelength, 2)
        sinthetan = round(sinthetan, 2)

        current_N = 600
        current_order = 1
        print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 1\nWavelength = {wavelength} angstrom')
    elif N.get() == '300':
        dn = random.choice(N_300)
        if order.get() == '1':
            sinthetan = dn / (math.sqrt(D ** 2 + dn ** 2))
            wavelength = 0.0033 * sinthetan * (10**7)
            wavelength = round(wavelength,2)
            sinthetan = round(sinthetan, 2)
            dn = round(dn,2)
            current_N = 300
            current_order = 1
            print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 1\nWavelength = {wavelength} angstrom')
        else:
            dn *= 2
            sinthetan = dn / (math.sqrt(D ** 2 + dn ** 2))
            wavelength = (0.0033 * sinthetan * (10 ** 7))/2
            wavelength = round(wavelength, 2)
            sinthetan = round(sinthetan, 2)
            dn = round(dn, 2)
            current_N = 300
            current_order = 2
            print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 2\nWavelength = {wavelength} angstrom')
    else:
        dn = random.choice(N_100)
        if order.get() == '1':
            sinthetan = dn / (math.sqrt(D ** 2 + dn ** 2))
            wavelength = 0.01 * sinthetan * (10 ** 7)
            wavelength = round(wavelength, 2)
            sinthetan = round(sinthetan, 2)
            dn = round(dn, 2)
            current_N = 100
            current_order = 1
            print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 1\nWavelength = {wavelength} angstrom')
        elif order.get() == '2':
            dn *= 2
            sinthetan = dn / (math.sqrt(D ** 2 + dn ** 2))
            wavelength = (0.01 * sinthetan * (10 ** 7)) / 2
            wavelength = round(wavelength, 2)
            sinthetan = round(sinthetan, 2)
            dn = round(dn, 2)
            current_N = 100
            current_order = 2
            print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 2\nWavelength = {wavelength} angstrom')
        else:
            dn *= 3
            sinthetan = dn / (math.sqrt(D ** 2 + dn ** 2))
            wavelength = (0.01 * sinthetan * (10 ** 7)) / 3
            wavelength = round(wavelength, 2)
            sinthetan = round(sinthetan, 2)
            dn = round(dn, 2)
            current_N = 100
            current_order = 3
            print(f'dn = {dn}\nsinthetan = {sinthetan}\norder = 3\nWavelength = {wavelength} angstrom')


def addTable():
    global s_no, current_order, current_N, dn, sinthetan, wavelength
    if current_N == 'NaN':
        messagebox.showerror(title="Invalid Input", message="Start the Simulation First")
    else:
        f=open("obs.csv", "a", newline='')
        writer = csv.writer(f)
        s_no += 1
        error = abs(wavelength-6328)/6328 * 100
        error = round(error, 2)
        data = [s_no, current_order, current_N, dn, sinthetan, wavelength, f'{error}%']
        writer.writerow(data)
        tree.insert('', tk.END, values=data)
        f.close()



#creating elements

main_win = tk.Tk()
main_win.title("He Ne Laser")
main_win.geometry("1024x768")
main_win.resizable(False, False)
main_win.configure(background='white')

style = ttk.Style()


#btn = ttk.Button(main_win, text="Button", style="TButton")
global pic2
# creating image
laser = tk.Canvas(main_win, height=96, width=177)
laser.configure(borderwidth=0,highlightthickness=0,background='white')
pic = ImageTk.PhotoImage(Image.open('laser.png'))
laser.create_image(0,0, anchor='nw', image=pic)

#laser straight pic



laser_straight = tk.Canvas(main_win, height=21,width=500)
laser_straight.configure(borderwidth=0,highlightthickness=0, bg='white')
laser_straight_pic = ImageTk.PhotoImage(Image.open('laser_straight.png'))
laser_straight.create_image(0,0, anchor='nw', image=laser_straight_pic)


diffraction_pic = tk.Canvas(main_win, height=163, width=378)
diffraction_pic.configure(borderwidth=0,highlightthickness=0,background='white')
pic2 = ImageTk.PhotoImage(Image.open('example.jpg'))
diffraction_pic.create_image(0,0, anchor='nw', image=pic2)

diffraction_grating = tk.Canvas(main_win, height=180, width=180)
diffraction_grating.configure(borderwidth=0,highlightthickness=0,background='white')
diffraction_grating_pic = ImageTk.PhotoImage(Image.open('diffraction grating.png'))
diffraction_grating.create_image(0,0, anchor='nw', image=diffraction_grating_pic)



#creating elements

D = tk.IntVar()
h = tk.IntVar()
N = tk.StringVar()
order = tk.StringVar()

distance = ttk.Scale(main_win, from_=0, to=100, style="Horizontal.TScale", command=slider_changed, variable=D)
distance_label = ttk.Label(main_win, text="Distance from screen: ", style="TLabel")

height = ttk.Scale(main_win, from_=-20, to=20, style="Horizontal.TScale", command=height_changed, variable=h)
height_label = ttk.Label(main_win, text="Height: 0", style="TLabel")

start_btn = ttk.Button(main_win, text="Start", command=calc)
add_to_table = ttk.Button(main_win, text="Add To Table", command=addTable)

# N COMBO BOX

font1 = tkinter.font.Font(family="Segoe UI", size=12)
N_combo = ttk.Combobox(main_win, textvariable=N, state='readonly', height=100, font=font1, width=5)
N_combo['values'] = ('100', '300', '600')
main_win.option_add("*TCombobox*Listbox*Font", font1)
N_label = ttk.Label(main_win, text="N: 600", style="TLabel")
N_combo.set(600)
N_combo.bind('<FocusIn>', lambda event: refresh(event))
N_combo.bind('<<ComboboxSelected>>', N_changed)

# order(n) COMBO BOX

order_combo = ttk.Combobox(main_win, textvariable=order, state='readonly', height=100, font=font1, width=5)
order_combo['values'] = ('1')
main_win.option_add("*TCombobox*Listbox*Font", font1)
order_label = ttk.Label(main_win, text="Order: 1", style="TLabel")
order_combo.set(1)
order_combo.bind('<<ComboboxSelected>>', order_changed)

#configuring elements
style.configure('TButton', font=(None, 12), foreground='black')
style.configure('Horizontal.TScale', background='white')
style.configure('TLabel', background='white', font=("Segoe UI", 10))


#placing elements

#btn.place(x=50,y=50)
laser.place(x=600,y=300)


#distance.place(x=880, y=270)
#distance_label.place(x=870, y=300)

height.place(x=880, y=200)
height_label.place(x=880, y=230)

N_combo.place(x=880, y=270)
N_label.place(x=880, y=320)

order_combo.place(x=880, y=350)
order_label.place(x=880, y=380)

start_btn.place(x=850, y=430)
add_to_table.place(x=850, y = 470)


diffraction_grating.place(x=300, y=270)
laser_straight.place(x=200,y=335)
diffraction_pic.place(x=50,y=50)




obs_table = tk.Tk()
columns = ("S.No", "Order", "N", "dn", "sinthetan", "lambda", "Percentage Error")

obs_table.title('Observation Table')
obs_table.geometry("580x266")
obs_table.configure(background='white')
obs_table.resizable(False, False)

tree = ttk.Treeview(obs_table, columns=columns, show='headings')

obs_heading = tk.Label(obs_table, text="Observation Table", font=('Segoe UI', 20), background='white',
                    foreground='blue', anchor=tk.CENTER)
obs_heading.grid(row=0, column=0)

f = open("obs.csv", "r")
reader = csv.reader(f)
data = list(reader)

if not data:

    tree.heading('S.No', text='S.No')
    tree.column("S.No", minwidth=0, width=35, stretch=tk.NO)

    tree.heading('Order', text='Order')
    tree.column("Order", minwidth=0, width=50, stretch=tk.NO)

    tree.heading('N', text='N')
    tree.column("N", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('dn', text='dn')
    tree.column("dn", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('sinthetan', text='Sinθn')
    tree.column("sinthetan", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('lambda', text='λ')
    tree.column("lambda", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('Percentage Error', text='Percentage Error')
    tree.column("Percentage Error", minwidth=0, width=100, stretch=tk.NO)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(obs_table, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

else:
    tree.heading('S.No', text='S.No')
    tree.column("S.No", minwidth=0, width=35, stretch=tk.NO)

    tree.heading('Order', text='Order')
    tree.column("Order", minwidth=0, width=50, stretch=tk.NO)

    tree.heading('N', text='N')
    tree.column("N", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('dn', text='dn')
    tree.column("dn", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('sinthetan', text='Sin θn')
    tree.column("sinthetan", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('lambda', text='λ')
    tree.column("lambda", minwidth=0, width=100, stretch=tk.NO)

    tree.heading('Percentage Error', text='Percentage Error')
    tree.column("Percentage Error", minwidth=0, width=100, stretch=tk.NO)

    for item in data:
        tree.insert('', tk.END, values=item)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(main_win, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
#
# for contact in contacts:
#     tree.insert('', END, values=contact)


main_win.protocol("WM_DELETE_WINDOW", on_closing)
obs_table.protocol("WM_DELETE_WINDOW", on_closing)



obs_table.mainloop()

main_win.mainloop()
