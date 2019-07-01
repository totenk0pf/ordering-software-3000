from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import trace

root = Tk()
root.geometry("340x600")
root.title("Paradise Pizza")
root.resizable(False,False)

#heading
heading = Label(text="Welcome to Paradise Pizza",font=("Monotype Corsiva",15), bg="orange red", width=35, height=3)
heading2 = Label(text="Kia ~ Hello ~ Ni hao ~ Konichiwa",font=("Monotype Corsiva",11), bg="orange red")
heading.grid(row=0, column=0, columnspan=4)
heading2.grid(row=0, column=0, columnspan=4, rowspan=2)

#Ask for Name and Number
#Num and Letter Validation
cusname=StringVar()
cusnum=StringVar()
def testVal(inStr,acttyp):
    if acttyp == '1':
        if not inStr.isalpha():
            return False
    return True

name_cus = Label(root, text="Your Name :")
phone_cus = Label(root, text="Phone Number :")
name_info = Entry(root, textvariable=cusname, validate="key")
name_info['validatecommand'] = (name_info.register(testVal),'%P','%d')

def testVal(inStr,acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True
              
num_info = Entry(root, textvariable=cusnum, validate="key")
num_info['validatecommand'] = (num_info.register(testVal),'%P','%d')

name_cus.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
phone_cus.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

name_info.grid(row=1, column=2, sticky="ew", pady=5, padx=5)
num_info.grid(row=2, column=2, sticky="ew", pady=5, padx=5)

# Phone number input's validation
def nameLimit(name_info):
    if len(cusname.get()) >= 14:
            cusname.set(cusname.get()[:14])
            num_info.focus()

def numLimit(num_info):
    if len(cusnum.get()) >= 10:
            cusnum.set(cusnum.get()[:10])
            DeliveryEntry.focus()

cusname.trace('w', lambda *args:nameLimit(name_info))
cusnum.trace('w', lambda *args:numLimit(num_info))

# Check for delivery or pick-up
dpCheck = IntVar()
dpCheck.set(0)

DPLabel = Label(root, text="Delivery/Pickup", bg="orange red", width=50)
DPLabel.grid(column=0, columnspan=4, row=3, pady=5)

address = StringVar()

DeliveryAddress = Label(root, text="Address :")
DeliveryAddress.grid(column=1, row=6, padx=5, pady=5, sticky="ew")
DeliveryEntry = Entry(root, textvariable=address)
DeliveryEntry.grid(column=2, row=6, padx=5, pady=5, sticky="ew")

def showAddress():
    if dpCheck.get() == 1:
        DeliveryAddress.grid()
        DeliveryEntry.grid()
    elif dpCheck.get() == 0:
        DeliveryAddress.grid_remove()
        DeliveryEntry.grid_remove()

DeliveryCheck = Checkbutton(root, text="Delivery", variable=dpCheck, onvalue=1, offvalue=0, command=showAddress)
DeliveryCheck.grid(column=2, row=5, pady=5)
PickupCheck = Checkbutton(root, text="Pickup", variable=dpCheck, onvalue=0, offvalue=1, command=showAddress)
PickupCheck.grid(column=2, row=4, pady=5)

DeliveryCheck.select()

def deselect():
    if dpCheck.get() == 1:
        PickupCheck.deselect()
    elif dpCheck.get() == 0:
        DeliveryCheck.deselect()

#PizzaOrder
PizzaList = ("None", "Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Egg Pizza", "Spicy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza", "The Ultimate Pizza")
   
PizzaNam = Label(text="Choose Your Pizza", bg="orange red", width=50)
PizzaNam.grid(column=0, columnspan=4, row=7)
Pizzamax = Label(text="(5 Max)", bg="orange red")
Pizzamax.grid(column=3, row=7)

pset1 = StringVar()
pset2 = StringVar()
pset3 = StringVar()
pset4 = StringVar()
pset5 = StringVar()

#PizzaBox = ttk.Combobox(root, state="readonly", values=["Meat_Lover Meat Hater Pizza Cheesy Pizza")
#PizzaBox.grid(column=2, row=8, pady=5)
Pizza1Lab = Label(text="Pizza 1 :")
Pizza1Lab.grid(column=1, row=8, pady=5)

PickPizza1 = ttk.Combobox(root, state="readonly", textvariable=pset1)
PickPizza1['values'] = PizzaList
PickPizza1.current(0)
PickPizza1.grid(column=2, row=8, pady=5)

Pizza2Lab = Label(text="Pizza 2 :")
Pizza2Lab.grid(column=1, row=9, pady=5)

PickPizza2 = ttk.Combobox(root, state="readonly", textvariable=pset2)
PickPizza2['values'] = PizzaList
PickPizza2.current(0)
PickPizza2.grid(column=2, row=9, pady=5)
Pizza3Lab = Label(text="Pizza 3 :")
Pizza3Lab.grid(column=1, row=10, pady=5)

PickPizza3 = ttk.Combobox(root, state="readonly", textvariable=pset3)
PickPizza3['values'] = PizzaList
PickPizza3.current(0)
PickPizza3.grid(column=2, row=10, pady=5)

Pizza4Lab = Label(text="Pizza 4 :")
Pizza4Lab.grid(column=1, row=11, pady=5)

PickPizza4 = ttk.Combobox(root, state="readonly", textvariable=pset4)
PickPizza4['values'] = PizzaList
PickPizza4.current(0)
PickPizza4.grid(column=2, row=11, pady=5)

Pizza5Lab = Label(text="Pizza 5 :")
Pizza5Lab.grid(column=1, row=12, pady=5)

PickPizza5 = ttk.Combobox(root, state="readonly", textvariable=pset5)
PickPizza5['values'] = PizzaList
PickPizza5.current(0)
PickPizza5.grid(column=2, row=12, pady=5)

TCost = 0
none = 0

Totallable = Label(text="Total cost :")
Totallable.grid(column=1, row=15, pady=5)
Costlable = Label(text=TCost)
Costlable.grid(column=2, row=15, pady=5)

displayname = StringVar()
displayphone = StringVar()
displayaddress = StringVar()

ReceiptWindow  = Toplevel(root)
NameLabel = Label(ReceiptWindow, text="Customer's name:")
NameLabel.grid(column=1, row=1)
DisplayName = Label(ReceiptWindow, text="")
DisplayName.grid(column=2, row=1)
PhoneLabel = Label(ReceiptWindow, text="Customer's phone number:")
PhoneLabel.grid(column=1, row=2)
DisplayPhone = Label(ReceiptWindow, text="")
DisplayPhone.grid(column=2, row=2)
AddressLabel = Label(ReceiptWindow, text="Customer's address:")
AddressLabel.grid(column=1, row=3)
DisplayAddress = Label(ReceiptWindow, text="")
DisplayAddress.grid(column=2, row=3)

PrintPizza1 = ttk.Combobox(ReceiptWindow, state="disabled")
PrintPizza1.grid(column=1, row=4)
PrintPizza1['values'] = PizzaList
PrintPizza1.current(PickPizza1.current())
PrintPizza2 = ttk.Combobox(ReceiptWindow, state="disabled")
PrintPizza2.grid(column=1, row=5)
PrintPizza2['values'] = PizzaList
PrintPizza2.current(PickPizza2.current())
PrintPizza3 = ttk.Combobox(ReceiptWindow, state="disabled")
PrintPizza3.grid(column=1, row=6)
PrintPizza3['values'] = PizzaList
PrintPizza3.current(PickPizza3.current())
PrintPizza4 = ttk.Combobox(ReceiptWindow, state="disabled")
PrintPizza4.grid(column=1, row=7)
PrintPizza4['values'] = PizzaList
PrintPizza4.current(PickPizza4.current())
PrintPizza5 = ttk.Combobox(ReceiptWindow, state="disabled")
PrintPizza5.grid(column=1, row=8)
PrintPizza5['values'] = PizzaList
PrintPizza5.current(PickPizza5.current())

PrintCostLabel = Label(ReceiptWindow, text="Total cost:")
PrintCostLabel.grid(column=1, row=9)
PrintCost = Label(ReceiptWindow, text="")
PrintCost.grid(column=2, row=9)

ConfirmButton = Button(ReceiptWindow, text="Confirm", command=ReceiptWindow.withdraw, bg="orange red")
ConfirmButton.grid(row=10, column=1, columnspan=2, sticky="ew", ipadx=35, ipady=5, pady=5)

def Pass():
   pass

ReceiptWindow.geometry("")
ReceiptWindow.resizable(False, False)
ReceiptWindow.protocol("WM_DELETE_WINDOW", Pass)
ReceiptWindow.withdraw()

#Order
def calcTotalCost():
    global TCost
    global none
    TCost = 0
    none = 5
    TotalList = [(pset1.get()), (pset2.get()), (pset3.get()), (pset4.get()), (pset5.get())]
    for pizza in TotalList:
        if not pizza == "None":
            none -= 1
    TCost = (8.5 * len(TotalList)) - (8.5 * none)
    Costlable.config(text=TCost)
    PrintCost.config(text=TCost)

def calcOnClick(self):
    calcTotalCost()

PickPizza1.bind("<<ComboboxSelected>>", calcOnClick)
PickPizza2.bind("<<ComboboxSelected>>", calcOnClick)
PickPizza3.bind("<<ComboboxSelected>>", calcOnClick)
PickPizza4.bind("<<ComboboxSelected>>", calcOnClick)
PickPizza5.bind("<<ComboboxSelected>>", calcOnClick)

def save_info():
    calcTotalCost()

    cusname_info = cusname.get() 
    cusnum_info = str(cusnum.get())
    address_info = address.get()
    print("Name: ", cusname_info,", Number: ", cusnum_info,", Address: ", address_info)



    file = open("user.txt", "w")
    file.write(cusname_info)
    file.write(cusnum_info)
    file.write(address_info)
    file.close()

    print(" Customer name ", cusname_info, "has been ordered successfully")

    if (cusname.get() == "") or (cusnum.get() == "") or (address.get() == ""):
        messagebox.showerror("Error","You must input all of the customer's information!")
    else:
        confirmask = messagebox.askyesno("Confirm order", "Do you wish to confirm the order?")
        if confirmask == True:
            DisplayName["text"] = cusname_info
            DisplayPhone["text"] = cusnum_info
            DisplayAddress["text"] = address_info
            ReceiptWindow.deiconify()
            name_info.delete(0, END)
            num_info.delete(0, END)
            DeliveryEntry.delete(0, END)
            PrintPizza1['values'] = PizzaList
            PrintPizza1.current(PickPizza1.current())
            PrintPizza2['values'] = PizzaList
            PrintPizza2.current(PickPizza2.current())
            PrintPizza3['values'] = PizzaList
            PrintPizza3.current(PickPizza3.current())
            PrintPizza4['values'] = PizzaList
            PrintPizza4.current(PickPizza4.current())
            PrintPizza5['values'] = PizzaList
            PrintPizza5.current(PickPizza5.current())
            PickPizza1.current(0)
            PickPizza2.current(0)
            PickPizza3.current(0)
            PickPizza4.current(0)
            PickPizza5.current(0)
            TCost = 0
            Costlable.config(text=TCost)

Order = Button(text="Order", command=save_info, bg="orange red")
Order.grid(row=13, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)
Exit = Button(root, text="Exit", command=root.destroy, bg="silver")
Exit.grid(row=1, column=3, sticky="ew", pady=5, padx=20, ipadx=15, ipady=3)

def cancel():
    cancelask = messagebox.askyesno("Cancel order", "Do you wish to cancel the order?")
    if cancelask == True:
        name_info.delete(0, END)
        num_info.delete(0, END)
        DeliveryEntry.delete(0, END)
        PickPizza1.current(0)
        PickPizza2.current(0)
        PickPizza3.current(0)
        PickPizza4.current(0)
        PickPizza5.current(0)
        TCost = 0
        Costlable.config(text=TCost)

CancelBut = Button(text="Cancel", command=cancel, bg="silver")
CancelBut.grid (row=14, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)

root.mainloop()
