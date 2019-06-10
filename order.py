# PIZZA ORDERING SOFTWARE
# -- can I get 12 credits?
# https://github.com/totenk0pf/ordering-software-3000

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

import os
import json

root = Tk()
root.resizable(False, False)

# Defining variables
firstname = StringVar()
lastname = StringVar()
phonein1 = ''
address = ''

# Defining functions
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Admin/Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

def SaveFile():
    name = asksaveasfilename(initialdir="C:/Users/Admin/Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )

def aboutDisplay():
    about = Toplevel(root)
    about.title('About')
    pyzza = ImageTk.PhotoImage(Image.open("pyzza.png"))
    showPyzza = Label(about, image=pyzza)
    showPyzza.image = pyzza
    showPyzza.grid(column=1, row=1)
    about.lift(root)

title = root.title("Pizza Ordering Software")

# Top menu bar
menubar= Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

def openConfig():
        ConfigWindow = Toplevel(root)
        ConfigWindow.title("Configurations")

        ConfigWindow.attributes("-topmost", True)

optionmenu = Menu(menubar, tearoff=0)
optionmenu.add_command(label="Configurations", command=openConfig)
menubar.add_cascade(label="Options", menu=optionmenu)

def openManual():
    os.system("start \"\" https://github.com/totenk0pf/ordering-software-3000/blob/master/README.md")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Manual", command=openManual)
helpmenu.add_command(label="About", command=aboutDisplay)
menubar.add_cascade(label="Help", menu=helpmenu)

# Validation
def only_characters(char):
        return char.isalpha()

def only_numbers(char):
        return char.isdigit()

# LETTERS ONLY
ccmd = root.register(only_characters)

# NUMBERS ONLY
ncmd = root.register(only_numbers)

# Main GUI
# Customer's details frame
CustomerFrame = LabelFrame(root, text="Customer's details")
CustomerFrame.grid(column=1, row=1, ipadx=10, ipady=10, padx=(20), pady=(10,5), sticky="ew")

firstname = StringVar()
lastname = StringVar()

# Input customer's name
NameLabel = Label(CustomerFrame, text="Customer's name:")
NameLabel.grid(column=1, row=1, padx=(20,10), pady=(15,5))
FirstNameInput = Entry(CustomerFrame, textvariable=firstname, validate="key", validatecommand=(ccmd, '%S'))
FirstNameInput.grid(column=2, row=1, padx=(0,10), pady=(15,5), sticky="ew")
LastNameInput = Entry(CustomerFrame, textvariable=lastname, validate="key", validatecommand=(ccmd, '%S'))
LastNameInput.grid(column=3, row=1, padx=(0,10), pady=(15,5), sticky="ew")

# Input customer's phone number
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=4)

# Defining text variables
phonein1 = StringVar()

PhoneLabel = Label(CustomerFrame, text="Phone number:")
PhoneLabel.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
PhoneInput = Entry(CustomerFrame, textvariable=phonein1, validate="key", validatecommand=(ncmd, '%S'))
PhoneInput.grid(column=2, columnspan=2, row=2, padx=(0,10), pady=5, sticky="ew")

# Phone number input's validation
def fnameLimit(FirstNameInput):
        if len(firstname.get()) >= 10:
                firstname.set(firstname.get()[:10])
                LastNameInput.focus()

def lnameLimit(LastNameInput):
        if len(lastname.get()) >= 10:
                lastname.set(lastname.get()[:10])
                PhoneInput.focus()

def phone1Limit(PhoneInput):
        if len(phonein1.get()) >= 9:
                phonein1.set(phonein1.get()[:9])
                DeliveryEntry.focus()

firstname.trace('w', lambda *args:fnameLimit(FirstNameInput))
lastname.trace('w', lambda *args:lnameLimit(LastNameInput))
phonein1.trace('w', lambda *args:phone1Limit(PhoneInput))

# Delivery/Pickup
dpCheck = IntVar()
dpCheck.set(0)

DPLabel = Label(CustomerFrame, text="Delivery/Pickup:")
DPLabel.grid(column=1, row=3, padx=(20,10), pady=5)

address = StringVar()

DeliveryAddress = Label(CustomerFrame, text="Customer's address:")
DeliveryAddress.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
DeliveryEntry = Entry(CustomerFrame, textvariable=address)
DeliveryEntry.grid(column=2, columnspan=2, row=4, padx=(0,10), pady=5, sticky="ew")

# Displays/hides address entry
def showAddress():
    if dpCheck.get() == 1:
        DeliveryAddress.grid()
        DeliveryEntry.grid()
    elif dpCheck.get() == 0:
        DeliveryAddress.grid_remove()
        DeliveryEntry.grid_remove()

DeliveryCheck = Checkbutton(CustomerFrame, text="Delivery (+$3)", variable=dpCheck, onvalue=1, offvalue=0, command=showAddress)
DeliveryCheck.grid(column=2, row=3, padx=(0,10), pady=5)
PickupCheck = Checkbutton(CustomerFrame, text="Pickup", variable=dpCheck, onvalue=0, offvalue=1, command=showAddress)
PickupCheck.grid(column=3, row=3, padx=(0,10), pady=5)

DeliveryCheck.select()

def deselect():
    if dpCheck.get() == 1:
        PickupCheck.deselect()
    elif dpCheck.get() == 0:
        DeliveryCheck.deselect()

# Pizza ordering frame
PizzaFrame = LabelFrame(root, text="Order")
PizzaFrame.grid(column=1, row=5, ipadx=10, ipady=10, padx=(20,20), pady=(0,5), sticky="ew")
ButtonFrame = Frame(PizzaFrame)
ButtonFrame.grid(column=2, row=1, padx=(20))

PizzaList = ttk.Treeview(PizzaFrame, height=14, selectmode="browse")
PizzaList["columns"]=("one")
PizzaList.column("#0", width=150, minwidth=150, stretch=NO)
PizzaList.column("one", width=50, minwidth=50, stretch=NO)
PizzaList.heading("#0", text="Name", anchor="w")
PizzaList.heading("one", text="Price", anchor="w")

# INSERT LIST OF PIZZA
# REGULAR PIZZAS
RegularPizza = PizzaList.insert("", 1, "RGP", text="Regular Pizzas")
PizzaList.item(RegularPizza, open=True)
PizzaList.insert(RegularPizza, "end", 'HP', text="Hawaiian Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'SBP', text="Steak & Bacon Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'PP', text="Pepperoni Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'CP', text="Cheese Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'BOP', text="Beef & Onion Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'VP', text="Veggie Pizza", values=("$8.50"))
PizzaList.insert(RegularPizza, "end", 'NYP', text="New Yorker Pizza", values=("$8.50"))
# GOURMET PIZZAS
GourmetPizza = PizzaList.insert("", 2, "GP", text="Gourmet Pizzas")
PizzaList.item(GourmetPizza, open=True)
PizzaList.insert(GourmetPizza, "end", 'RHP', text="Ramadan Halal Pizza", values=("$13.50"))
PizzaList.insert(GourmetPizza, "end", 'POP', text="Pineapple Only Pizza", values=("$13.50"))
PizzaList.insert(GourmetPizza, "end", 'COP', text="Crust Only Pizza", values=("$13.50"))
PizzaList.insert(GourmetPizza, "end", 'PT', text="Pizza that's been in a tomb for 1000 years", values=("$13.50"))
PizzaList.insert(GourmetPizza, "end", 'RP', text="Rice Pizza", values=("$13.50"))
PizzaList.grid(column=1, row=1, padx=(20,0), pady=(10,0), sticky="ew")

TotalCost = 0

OrderList = ttk.Treeview(PizzaFrame, height=14, selectmode="browse")
OrderList["columns"]=("one")
OrderList.column("#0", width=150, minwidth=150, stretch=NO)
OrderList.column("one", width=50, minwidth=50, stretch=NO)
OrderList.heading("#0", text="Name", anchor="w")
OrderList.heading("one", text="Amount", anchor="w")
OrderList.grid(column=3, row=1, padx=0, pady=(10,0), sticky="ew")
RegularPizza = OrderList.insert("", 1, "RGP", text="Regular Pizzas")
OrderList.item(RegularPizza, open=True)
GourmetPizza = OrderList.insert("", 2, "GP", text="Gourmet Pizzas")
OrderList.item(GourmetPizza, open=True)
TotalRow = OrderList.insert("", 3, "TT", text="Total cost:", values=TotalCost)

TotalAmount = 0
TotalAmountRegular = 0
TotalAmountGourmet = 0

printListReg = []
printListGour = []
printList = []

dynamicIID = 0

def calcTotalCost():
        global TotalCost
        TotalCost = (TotalAmountRegular * 8.50) + (TotalAmountGourmet * 13.50)

def addPizza():
        # Add the selected pizza
        global TotalAmount
        global TotalCost
        global TotalAmountRegular
        global TotalAmountGourmet
        global dynamicIID
        selectedItem = PizzaList.focus()
        returnItem = PizzaList.item(selectedItem)
        getItemName = returnItem.get('text')
        if TotalAmount <= 4:
                while getItemName not in ["Regular Pizzas","Gourmet Pizzas"]:
                        if PizzaList.parent(selectedItem) == RegularPizza:
                                OrderList.insert(RegularPizza, "end", dynamicIID, text=getItemName, values=1)
                                TotalAmountRegular += 1
                                printListReg.append(getItemName)
                                break
                        elif PizzaList.parent(selectedItem) == GourmetPizza:
                                OrderList.insert(GourmetPizza, "end", dynamicIID, text=getItemName, values=1)
                                TotalAmountGourmet += 1
                                printListGour.append(getItemName)
                                break
                TotalAmount = TotalAmountRegular + TotalAmountGourmet
        dynamicIID += 1
        calcTotalCost()
        OrderList.set(TotalRow, column="one", value=TotalCost)
        if TotalAmount > 4:
            messagebox.showwarning("Invalid", "Maximum amount of pizzas allowed is 5.")
        
RegularList = OrderList.get_children(RegularPizza)
GourmetList = OrderList.get_children(GourmetPizza)

def removePizza():
        selectedOrderItem = OrderList.focus()
        returnOrderItem = OrderList.item(selectedOrderItem)
        getOrderItemName = returnOrderItem.get('text')
        global TotalCost
        global TotalAmount
        global dynamicIID
        global TotalAmountRegular
        global TotalAmountGourmet
        if OrderList.focus() == "":
                messagebox.showwarning("Error", "Please select a pizza to remove!")
        else:
                if getOrderItemName not in ["Regular Pizzas", "Gourmet Pizzas"]:
                        if OrderList.parent(selectedOrderItem) == "RGP":
                                OrderList.delete(selectedOrderItem)
                                printListReg.remove(getOrderItemName)
                                TotalCost -= 8.5
                                TotalAmountRegular -= 1
                        elif OrderList.parent(selectedOrderItem) == "GP":
                                OrderList.delete(selectedOrderItem)
                                printListGour.remove(getOrderItemName)
                                TotalCost -= 13.5
                                TotalAmountGourmet -= 1
                        TotalAmount = TotalAmountRegular + TotalAmountGourmet
                        calcTotalCost()
                        OrderList.set(TotalRow, column="one", value=TotalCost)

AddButton = Button(ButtonFrame, text="Add", command=addPizza)
AddButton.grid(column=1, row=1, padx=5, pady=(10,0), sticky="ew")
RemoveButton = Button(ButtonFrame, text="Remove", command=removePizza)
RemoveButton.grid(column=1, row=2, padx=5, pady=(10,0), sticky="ew")
#LoadButton = Button(ButtonFrame, text="Load", command=OpenFile)
#LoadButton.grid(column=1, row=3, padx=5, pady=(10,0), sticky="ew")

PrintWindow = Toplevel(root)
PrintWindow.title("Your order")
PrintWindow.resizable(False, False)
# Customer's details frame
CustomerFrame = LabelFrame(PrintWindow, text="Customer's details")
CustomerFrame.grid(column=1, row=1, ipadx=10, ipady=10, padx=(20), pady=(10,5), sticky="ew")
# Print the customer's details
custName = StringVar()
phoneNum = StringVar()
printAddress = StringVar()
dpOption = StringVar()

NameLabel = Label(CustomerFrame, text="Customer's name:")
NameLabel.grid(column=1, row=1, padx=(20,10), pady=(15,5))
CustomerName = Label(CustomerFrame, textvariable=custName)
CustomerName.grid(column=2, row=1, padx=(10), pady=(15,5))
PhoneLabel = Label(CustomerFrame, text="Phone number:")
PhoneLabel.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
PhoneNumber = Label(CustomerFrame, textvariable=phoneNum)
PhoneNumber.grid(column=2, row=2, padx=(10), pady=(5))
DPLabel = Label(CustomerFrame, text="Delivery/Pickup:")
DPLabel.grid(column=1, row=3, padx=(20,10), pady=5)
PrintDeliveryAddress = Label(CustomerFrame, text="Customer's address:")
PrintDeliveryAddress.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
Address = Label(CustomerFrame, textvariable=printAddress)
Address.grid(column=2, row=4, padx=(10), pady=5, sticky="ew")
DeliveryOpt = Label(CustomerFrame, textvariable=dpOption)
DeliveryOpt.grid(column=2, row=3, padx=(10), pady=(5))
# Pizza list's frame
PizzaFrame = LabelFrame(PrintWindow, text="Order")
PizzaFrame.grid(column=1, row=4, ipadx=10, ipady=10, padx=(20,20), pady=(0,5), sticky="ew")
PrintList = ttk.Treeview(PizzaFrame, height=14, selectmode="none")
PrintList["columns"]=("one")
PrintList.column("#0", width=150, minwidth=150, stretch=NO)
PrintList.column("one", width=50, minwidth=50, stretch=NO)
PrintList.heading("#0", text="Name", anchor="w")
PrintList.heading("one", text="Amount", anchor="w")
PrintList.grid(column=1, row=5, padx=(20,0), pady=(10,0), sticky="ew")
RegularPrint = PrintList.insert("", 1, "RGP", text="Regular Pizzas")
PrintList.item(RegularPizza, open=True)
GourmetPrint = PrintList.insert("", 2, "GP", text="Gourmet Pizzas")
PrintList.item(GourmetPizza, open=True)
TotalRow = PrintList.insert("", 3, "TT", text="Total cost:", values=TotalCost)
# Parse the items from the order list
selectedItem = OrderList.focus()
returnItem = OrderList.item(selectedItem)
getItemName = returnItem.get('text')

def resetEntry():
        global TotalAmountRegular
        global TotalAmountGourmet
        global TotalAmount
        ResetPrompt = messagebox.askyesno("Reset", "Are you sure you want to reset the customer's information?")
        if ResetPrompt == True:
                FirstNameInput.delete(0, 'end')
                LastNameInput.delete(0, 'end')
                PhoneInput.delete(0, 'end')
                DeliveryEntry.delete(0, 'end')
                for i in OrderList.get_children(RegularPizza):
                        OrderList.delete(i)
                        TotalAmountRegular = 0
                for i in PrintList.get_children(RegularPizza):
                        PrintList.delete(i)
                for i in OrderList.get_children(GourmetPizza):
                        OrderList.delete(i)
                        TotalAmountGourmet = 0
                for i in PrintList.get_children(GourmetPizza):
                        PrintList.delete(i)
                del printListReg[:]
                del printListGour[:]
                TotalAmount = TotalAmountRegular + TotalAmountGourmet
        calcTotalCost()
        OrderList.set(TotalRow, column="one", value=TotalCost)

def confirmEntry():
        global dynamicIID
        global TotalCost
        ConfirmPrompt = messagebox.askyesno("Confirm", "Do you wish to confirm the order?")
        if ConfirmPrompt == True:
                if len(FirstNameInput.get()) == 0 or len(LastNameInput.get()) == 0 or len(PhoneInput.get()) == 0 or (len(address.get()) == 0 and dpCheck.get() == 1):
                        messagebox.showerror("Error", "Please input all of the customer's information.")
                else:
                        PrintWindow.deiconify()
                        PrintWindow.lift(root)
                        custName.set(FirstNameInput.get() + " " + LastNameInput.get())
                        phoneNum.set(PhoneInput.get())
                        printAddress.set(address.get())
                        if dpCheck.get() == 1:
                                dpOption.set("Delivery")
                                TotalCost += 3
                                PrintDeliveryAddress.grid()
                                printAddress.set(address.get())
                        elif dpCheck.get() == 0:
                                dpOption.set("Pickup")
                                PrintDeliveryAddress.grid_remove()
                                calcTotalCost()
                                Address.grid_remove()
                        for item in printListReg:
                                PrintList.insert(RegularPizza, "end", dynamicIID, text=item, values=1)
                                dynamicIID += 1
                        for item in printListGour:
                                PrintList.insert(GourmetPizza, "end", dynamicIID, text=item, values=1)
                                dynamicIID += 1
                        PrintList.set(TotalRow, column="one", value=TotalCost)
                        PrintWindow.grab_set()
                
def confirmOrder():
        global TotalAmountRegular
        global TotalAmountGourmet
        global TotalAmount
        FirstNameInput.delete(0, 'end')
        LastNameInput.delete(0, 'end')
        PhoneInput.delete(0, 'end')
        DeliveryEntry.delete(0, 'end')
        for i in OrderList.get_children(RegularPizza):
                OrderList.delete(i)
                TotalAmountRegular = 0
        for i in PrintList.get_children(RegularPizza):
                PrintList.delete(i)
        for i in OrderList.get_children(GourmetPizza):
                OrderList.delete(i)
                TotalAmountGourmet = 0
        for i in PrintList.get_children(GourmetPizza):
                PrintList.delete(i)
        del printListReg[:]
        del printListGour[:]
        TotalAmount = TotalAmountRegular + TotalAmountGourmet
        calcTotalCost()
        OrderList.set(TotalRow, column="one", value=TotalCost)
        messagebox.showinfo("Confirmed", "Your order has been confirmed.")
        PrintWindow.withdraw()
        PrintWindow.grab_release()

def cancelOrder():
        messagebox.showinfo("Canceled", "Your order has been canceled.")
        PrintWindow.withdraw()
        for i in PrintList.get_children(RegularPizza):
                PrintList.delete(i)
        for i in PrintList.get_children(GourmetPizza):
                PrintList.delete(i)
        PrintWindow.grab_release()

def checkOrderList(): # Scans the order list for update (also used as a debugging function)
        root.after(2000, checkOrderList)  # Loop every 2 seconds
root.after(2000, checkOrderList)

# Buttons' frame
ButtonFrame = Frame(PrintWindow)
ButtonFrame.grid(column=1, row=5, padx=(20), pady=(0,20))
ConfirmButton = Button(ButtonFrame, text="Confirm order", command=confirmOrder)
ConfirmButton.grid(column=1, row=1, ipadx=20, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")
CancelButton = Button(ButtonFrame, text="Cancel order", command=cancelOrder)
CancelButton.grid(column=2, row=1, ipadx=20, ipady=20, padx=(0), pady=(10,0), sticky="nesw")
PrintLabel = Label(PrintWindow)
PrintWindow.withdraw()

OptionsFrame = LabelFrame(root, text="Options")
OptionsFrame.grid(column=1, row=6, ipadx=0, ipady=10, padx=(20,20), pady=(0,20), sticky="ew")
ConfirmButton = Button(OptionsFrame, text="Confirm order", command=confirmEntry)
ConfirmButton.grid(column=1, row=1, ipadx=15, ipady=20, padx=20, pady=(10,0), sticky="nesw")
ResetButton = Button(OptionsFrame, text="Reset order", command=resetEntry)
ResetButton.grid(column=2, row=1, ipadx=20, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")
ConfigButton = Button(OptionsFrame, text="Configurations", command=openConfig)
ConfigButton.grid(column=3, row=1, ipadx=15, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")

ExitButton = Button(OptionsFrame, text="Exit program", command=root.quit)
ExitButton.grid(column=4, row=1, ipadx=15, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")

def Pass():
        pass
PrintWindow.protocol("WM_DELETE_WINDOW", Pass)

root.iconbitmap('favicon.ico')
root.attributes("-topmost", True)
root.config(menu=menubar)
root.mainloop()