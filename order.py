# PIZZA ORDERING SOFTWARE
# -- can I get 12 credits?
# https://github.com/totenk0pf/ordering-software-3000

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

import os

root = Tk()
root.resizable(False, False)

# Defining variables
firstname = ''
lastname = ''
phonein1 = ''
phonein2 = ''
phonein3 = ''
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
    showPyzza.grid(column=1, row=1)
    about.lift(root)

title = root.title("ultimate ordering software 3000")

# Top menu bar
menubar= Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

def openConfig():
        ConfigWindow = Toplevel(root)

optionmenu = Menu(menubar, tearoff=0)
#optionmenu.add_command(Label="Configurations", command=openConfig)
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
phonein2 = StringVar()
phonein3 = StringVar()

PhoneLabel = Label(CustomerFrame, text="Phone number:")
PhoneLabel.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
PhoneInput1 = Entry(CustomerFrame, textvariable=phonein1, validate="key", validatecommand=(ncmd, '%S'))
PhoneInput1.grid(column=2, row=2, padx=(0,10), pady=5, sticky="ew")
PhoneInput2 = Entry(CustomerFrame, textvariable=phonein2, validate="key", validatecommand=(ncmd, '%S'))
PhoneInput2.grid(column=3, row=2, padx=(0,10), pady=5, sticky="ew")
PhoneInput3 = Entry(CustomerFrame, textvariable=phonein3, validate="key", validatecommand=(ncmd, '%S'))
PhoneInput3.grid(column=4, row=2, padx=(0,0), pady=5, sticky="ew")

# PHONEINPUT SWITCH
def phone1Limit(PhoneInput1):
    if len(phonein1.get()) == 3:
        PhoneInput2.focus()
def phone2Limit(PhoneInput2):
    if len(phonein2.get()) == 3:
        PhoneInput3.focus()
def phone3Limit(PhoneInput3):
    if len(phonein3.get()) == 3:
        DeliveryEntry.focus()

phonein1.trace('w', lambda *args:phone1Limit(PhoneInput1))
phonein2.trace('w', lambda *args:phone2Limit(PhoneInput2))
phonein3.trace('w', lambda *args:phone3Limit(PhoneInput3))

# Delivery/Pickup
dpCheck = IntVar()
dpCheck.set(0)

DPLabel = Label(CustomerFrame, text="Delivery/Pickup:")
DPLabel.grid(column=1, row=3, padx=(20,10), pady=5)

address = StringVar()

DeliveryAddress = Label(CustomerFrame, text="Customer's address:")
DeliveryAddress.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
DeliveryEntry = Entry(CustomerFrame, textvariable=address)
DeliveryEntry.grid(column=2, columnspan=3, row=4, padx=(0,0), pady=5, sticky="ew")

def showAddress():
    if dpCheck.get() == 1:
        DeliveryAddress.grid()
        DeliveryEntry.grid()
    elif dpCheck.get() == 0:
        DeliveryAddress.grid_remove()
        DeliveryEntry.grid_remove()

DeliveryCheck = Checkbutton(CustomerFrame, text="Delivery", variable=dpCheck, onvalue=1, offvalue=0, command=showAddress)
DeliveryCheck.grid(column=2, row=3, padx=(0,10), pady=5)
PickupCheck = Checkbutton(CustomerFrame, text="Pickup", variable=dpCheck, onvalue=0, offvalue=1, command=showAddress)
PickupCheck.grid(column=4, row=3, padx=(0,10), pady=5)

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

PizzaList = ttk.Treeview(PizzaFrame, height=14)
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
PizzaList.insert(GourmetPizza, "end", 'PT', text="Cursed Pizza", values=("$13.50"))
PizzaList.insert(GourmetPizza, "end", 'RP', text="Rice Pizza", values=("$13.50"))
PizzaList.grid(column=1, row=1, padx=(20,0), pady=(10,0), sticky="ew")

TotalCost = 0

OrderList = ttk.Treeview(PizzaFrame, height=14)
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

TotalAmount = 0

def getTotalAmount():
    TotalAmount = len(OrderList.get_children(RegularPizza)) + len(OrderList.get_children(GourmetPizza))

TotalRow = OrderList.insert("", 3, "TT", text="Total cost:", values=(TotalCost))

dynamicIID = 0

def addPizza():
        # DEPRECATED - MIGHT USE IN THE NEAR FUTURE
        ''' New window - insert amount
        AddWindow = Toplevel(root)
        AddLabel = Label(AddWindow, text="Please input amount of pizzas:")
        AddLabel.pack(padx=20, pady=10)
        AddEntry = Entry(AddWindow, textvariable=phonein1, validate="key", validatecommand=(ncmd, '%S'))
        AddEntry.pack(padx=20, pady=(0,10))
        AddOK = Button(AddWindow, text="OK")
        AddOK.pack(side=LEFT, padx=(20,0), pady=10, ipadx=20)
        CancelButton = Button(AddWindow, text="Cancel", command=AddWindow.
        CancelButton.pack(side=RIGHT, padx=(0,20), pady=10, ipadx=10)
        AddWindow.resizable(FALSE, FALSE)
        AddWindow.title("Amount")
        AddWindow.lift(root) '''
        # Add the selected pizza
        AddPrompt = simpledialog.askinteger("Amount", "Enter the desired amount:")
        if AddPrompt > 5:
                WarnMsg = messagebox.showwarning("Invalid", "Maximum amount of pizzas allowed is 5.")
        elif AddPrompt <= 5:
                selectedItem = PizzaList.focus()
                returnItem = PizzaList.item(selectedItem)
                getItemName = returnItem.get('text')
                global dynamicIID
                if PizzaList.parent(selectedItem) == RegularPizza:
                       OrderList.insert(RegularPizza, "end", dynamicIID, text=getItemName, values=AddPrompt)
                elif PizzaList.parent(selectedItem) == GourmetPizza:
                       OrderList.insert(GourmetPizza, "end", dynamicIID, text=getItemName, values=AddPrompt)
                dynamicIID += 1
                getTotalAmount()
                TotalCost = 8.5 * TotalAmount
                print(TotalCost)
                print(TotalAmount)

def removePizza():
        selectedOrderItem = OrderList.focus()
        returnOrderItem = OrderList.item(selectedOrderItem)
        getOrderItemName = returnOrderItem.get('text')
        global dynamicIID
        while getOrderItemName not in ["Regular Pizzas", "Gourmet Pizzas"]:
                OrderList.delete(selectedOrderItem)

AddButton = Button(ButtonFrame, text="Add", command=addPizza)
AddButton.grid(column=1, row=1, padx=5, pady=(10,0), sticky="ew")
RemoveButton = Button(ButtonFrame, text="Remove", command=removePizza)
RemoveButton.grid(column=1, row=2, padx=5, pady=(10,0), sticky="ew")
#LoadButton = Button(ButtonFrame, text="Load", command=OpenFile)
#LoadButton.grid(column=1, row=3, padx=5, pady=(10,0), sticky="ew")

def resetEntry():
    ResetPrompt = messagebox.askyesno("Reset", "Are you sure you want to reset the customer's information?")
    if ResetPrompt == True:
        FirstNameInput.delete(0, 'end')
        LastNameInput.delete(0, 'end')
        PhoneInput1.delete(0, 'end')
        PhoneInput2.delete(0, 'end')
        PhoneInput3.delete(0, 'end')
        DeliveryEntry.delete(0, 'end')

def confirmEntry():
    ConfirmPrompt = messagebox.askyesno("Confirm", "Do you wish to confirm the order?")

OptionsFrame = LabelFrame(root, text="Options")
OptionsFrame.grid(column=1, row=6, ipadx=10, ipady=10, padx=(20,20), pady=(0,20), sticky="ew")
ConfirmButton = Button(OptionsFrame, text="Confirm order", command=confirmEntry)
ConfirmButton.grid(column=1, row=1, ipadx=20, ipady=20, padx=20, pady=(10,0), sticky="nesw")
ResetButton = Button(OptionsFrame, text="Reset order", command=resetEntry)
ResetButton.grid(column=2, row=1, ipadx=20, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")

root.attributes("-topmost", True)
root.config(menu=menubar)
root.mainloop()
