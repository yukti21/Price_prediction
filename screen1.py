from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)
f1 = ('Times', 19)
f2 = ('Times', 11)
con = sqlite3.connect('predidb1.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Record(
                    Total_Volume number, 
                    T1 number,
                    T2 number,
                    T3 number,
                    Total_Bags number,
                    Type number, 
                    Year number,
                    Month number,
                    region text
                )
            ''')
con.commit()

ws = Tk()
ws.title('User Input')
ws.geometry('900x900')
ws.config(bg='#097969')

def nextpage():
    ws.destroy()
    import screen2



def insert_record():
    check_counter = 0
    warn = ""
    if register_Total_volume.get() == "":
        warn = "Total Volume  can't be empty"
    else:
        check_counter += 1

    if register_4046.get() == "":
        warn = "4046 can't be empty"
    else:
        check_counter += 1

    if register_4225.get() == "":
        warn = "4225 can't be empty"
    else:
        check_counter += 1

    if register_4770.get() == "":
        warn = "4770 can't be empty"
    else:
        check_counter += 1

    if register_Total_Bags.get() == "":
        warn = "Total_Bags can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Type"
    else:
        check_counter += 1

    if register_Year.get() == "":
        warn = "Year can't be empty"
    else:
        check_counter += 1

    if register_month.get() == "":
        warn = "Select Month"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Select region"
    else:
        check_counter += 1

    if check_counter == 9:
        try:
            con = sqlite3.connect('predidb1.db')
            cur = con.cursor()
            cur.execute(
                "INSERT INTO Record VALUES (:Total_Volume, :T1, :T2 ,:T3, :Total_Bags, :Type, :Year, :Month, :region)",
                {
                    'Total_Volume': register_Total_volume.get(),
                    'T1': register_4046.get(),
                    'T2': register_4225.get(),
                    'T3': register_4770.get(),
                    'Total_Bags': register_Total_Bags.get(),
                    'Type': var.get(),
                    'Year': register_Year.get(),
                    'Month': register_month.get(),
                    'region': variable.get()

                })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


var = StringVar()
var.set(0)

regions = []
variable = StringVar()
world = open('region.txt', 'r')
for region in world:
    region = region.rstrip('\n')
    regions.append(region)
    variable.set(regions[0])

# widgets

# nxtpg_btn = Button(
#   left_frame,
#  width=15,
# text='>>>>>>',
# font=f,
# relief=SOLID,
# cursor='hand2',
# command=login_response
# )

right_frame = Frame(
    ws,
    bd=2,
    bg='#AFE1AF',
    relief=SOLID,
    padx=10,
    pady=10
)
Label(
    right_frame,
    text="Avacado price prediction",
    bg='#AFE1AF',
    font=f1
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Please complete each of the fields below to estimate the price.",
    bg='#AFE1AF',
    font=f2
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Total Volume",
    bg='#AFE1AF',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter 4046",
    bg='#AFE1AF',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="enter 4225",
    bg='#AFE1AF',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter 4770",
    bg='#AFE1AF',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Total Bags",
    bg='#AFE1AF',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Type",
    bg='#AFE1AF',
    font=f
).grid(row=7, column=0, sticky=W, pady=10)


type_frame = LabelFrame(
    right_frame,
    bg='#AFE1AF',
    padx=10,
    pady=10,
)


type1_rb = Radiobutton(
    right_frame,
    text='Organic',
    bg='#AFE1AF',
    variable=var,
    value=0,
    font=('Times', 10),

).grid(row=7, column=1, pady=10, padx=20)

type2_rb = Radiobutton(
    right_frame,
    text='Conventional',
    bg='#AFE1AF',
    variable=var,
    value=1,
    font=('Times', 10)

).grid(row=7, column=2, pady=10, padx=20)

Label(
    right_frame,
    text="Year",
    bg='#AFE1AF',
    font=f
).grid(row=8, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Month",
    bg='#AFE1AF',
    font=f
).grid(row=9, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="region",
    bg='#AFE1AF',
    font=f
).grid(row=10, column=0, sticky=W, pady=10)

register_Total_volume = Entry(
    right_frame,
    font=f
)

register_4046 = Entry(
    right_frame,
    font=f
)

register_4225 = Entry(
    right_frame,
    font=f
)
register_4770 = Entry(
    right_frame,
    font=f
)
register_Total_Bags = Entry(
    right_frame,
    font=f
)

register_Year = Entry(
    right_frame,
    font=f
)
register_month = Entry(
    right_frame,
    font=f
)
register_region = OptionMenu(
    right_frame,
    variable,
    *regions)

register_region.config(
    width=15,
    font=('Times', 12)
)

reg_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

next_btn = Button(
    right_frame,
    width=15,
    text='>>>>>>>',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=nextpage)


register_Total_volume.grid(row=2, column=1, pady=10, padx=20)
register_4046.grid(row=3, column=1, pady=10, padx=20)
register_4225.grid(row=4, column=1, pady=10, padx=20)
register_4770.grid(row=5, column=1, pady=10, padx=20)
register_Total_Bags.grid(row=6, column=1, pady=10, padx=20)
type_frame.grid(row=7, column=1, pady=10, padx=20)
register_Year.grid(row=8, column=1, pady=10, padx=20)
register_month.grid(row=9, column=1, pady=10, padx=20)
register_region.grid(row=10, column=1, pady=10, padx=20)
reg_btn.grid(row=12, column=0, rowspan=2, pady=10, padx=20)
next_btn.grid(row=16, column=0, rowspan=2, pady=10, padx=20)
right_frame.place(x=12, y=50)

# infinite loop
ws.mainloop()