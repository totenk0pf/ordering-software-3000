from tkinter import *
from tkinter import ttk
import trace

root = Tk()
root.geometry("340x550")
root.title("Paradise Pizza")
root.configure(background='skyblue1')

#Order
def save_info():

   cusname_info = cusname.get()
   cusnum_info = cusnum.get()
   cusnum_info = str(cusnum_info)
   address_info = address.get()
   print("Name:", cusname_info,",Number:", cusnum_info,",Address:", address_info)

   file = open("user.txt", "w")
   file.write(cusname_info)
   file.write(cusnum_info)
   file.write(address_info)
   file.close()
   print(" Customer name ", cusname_info, "has been ordered successfully")

   name_info.delete(0, END)
   num_info.delete(0, END)
   DeliveryEntry.delete(0, END)

  
Order = Button(text="Order", command=save_info, bg="orange red")
Order.grid(row=13, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)
Exit = Button(root, text="Exit", command=exit, bg="orchid1")
Exit.grid(row=1, column=3, sticky="ew", pady=5, padx=20, ipadx=15, ipady=3)

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

DPLabel = Label(root, text="Delivery/Pickup")
DPLabel.grid(column=2, row=3, padx=5, pady=5)

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
PizzaNam = Label(text="Choose Your Pizza")
PizzaNam.grid(column=2, row=7)
Pizzamax = Label(text="(5 Max)")
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

def PizzaSet1(root):
   root.pickpizza = ttk.Combobox(root, state="readonly", textvariable=pset1)
   root.pickpizza['values'] = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza")
   root.pickpizza.grid(column=2, row=8, pady=5)

PizzaSet1(root)

Pizza2Lab = Label(text="Pizza 2 :")
Pizza2Lab.grid(column=1, row=9, pady=5)

def PizzaSet2(root):
   root.pickpizza = ttk.Combobox(root, state="readonly", textvariable=pset2)
   root.pickpizza['values'] = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza")
   root.pickpizza.grid(column=2, row=9, pady=5)

PizzaSet2(root)
  
Pizza3Lab = Label(text="Pizza 3 :")
Pizza3Lab.grid(column=1, row=10, pady=5)

def PizzaSet3(root):
   root.pickpizza = ttk.Combobox(root, state="readonly", textvariable=pset3)
   root.pickpizza['values'] = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza")
   root.pickpizza.grid(column=2, row=10, pady=5)

PizzaSet3(root)

Pizza4Lab = Label(text="Pizza 4 :")
Pizza4Lab.grid(column=1, row=11, pady=5)

def PizzaSet4(root):
   root.pickpizza = ttk.Combobox(root, state="readonly", textvariable=pset4)
   root.pickpizza['values'] = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza")
   root.pickpizza.grid(column=2, row=11, pady=5)

PizzaSet4(root)

Pizza5Lab = Label(text="Pizza 5 :")
Pizza5Lab.grid(column=1, row=12, pady=5)

def PizzaSet5(root):
   root.pickpizza = ttk.Combobox(root, state="readonly", textvariable=pset5)
   root.pickpizza['values'] = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza")
   root.pickpizza.grid(column=2, row=12, pady=5)

PizzaSet5(root)

TCost = 0

Totallable = Label(text="Total cost :")
Totallable.grid(column=1, row=14, pady=5)
Costlable = Label(text=TCost)
Costlable.grid(column=2, row=14, pady=5)

def calcTotalCost(self):
    global TCost
    if not pset1.get() == "":
        TCost += 8.5
    if not pset2.get() == "":
        TCost += 8.5
    if not pset3.get() == "":
        TCost += 8.5
    if not pset4.get() == "":
        TCost += 8.5
    if not pset5.get() == "":
        TCost += 8.5
    Costlable.config(text=TCost)
    print(TCost)

root.bind("<Button-1>", calcTotalCost)

root.mainloop()


