from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from TkTreectrl import *
from PIL import *

import dict

root = Tk()
root.resizable(False, False)

# Dictionary
pizza_list = ["Ramadan Halal Pizza", "Absolutely Haram Pizza", "Pizza that gives you the big gay", "Pineapple only pizza"]
pizza_list_index = 0

firstname = ""
lastname = ""
phonein1 = ""
phonein2 = ""
phonein3 = ""
address = ""

# Defining process
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Admin/Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    # Using try in case user types in unknown file or closes without choosing a file.
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
    about.lift(root)

title = root.title("ultimate ordering software 3000")

# Top menu bar
menubar= Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Manual")
helpmenu.add_command(label="About", command=aboutDisplay)
menubar.add_cascade(label="Help", menu=helpmenu)

# Main GUI
# Customer's details frame
CustomerFrame = LabelFrame(root, text="Customer's details")
CustomerFrame.grid(column=1, row=1, ipadx=10, ipady=10, padx=(20), pady=(10,5))

# Input customer's name
NameLabel = Label(CustomerFrame, text="Customer's name:")
NameLabel.grid(column=1, row=1, padx=(20,10), pady=(15,5))
FirstNameInput = Entry(CustomerFrame, textvariable=firstname)
FirstNameInput.grid(column=2, row=1, padx=(0,10), pady=(15,5), sticky="ew")
LastNameInput = Entry(CustomerFrame, textvariable=lastname)
LastNameInput.grid(column=3, row=1, padx=(0,10), pady=(15,5), sticky="ew")

# Input customer's phone number
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=4)

PhoneLabel = Label(CustomerFrame, text="Phone number:")
PhoneLabel.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
PhoneInput1 = Entry(CustomerFrame, textvariable=phonein1)
PhoneInput1.grid(column=2, row=2, padx=(0,10), pady=5, sticky="ew")
PhoneInput2 = Entry(CustomerFrame, textvariable=phonein2)
PhoneInput2.grid(column=3, row=2, padx=(0,10), pady=5, sticky="ew")
PhoneInput3 = Entry(CustomerFrame, textvariable=phonein3)
PhoneInput3.grid(column=4, row=2, padx=(0,0), pady=5, sticky="ew")

# Delivery/Pickup
dpCheck = IntVar()
dpCheck.set(0)

DPLabel = Label(CustomerFrame, text="Delivery/Pickup:")
DPLabel.grid(column=1, row=3, padx=(20,10), pady=5)

DeliveryAddress = Label(CustomerFrame, text="Customer's address:")
DeliveryAddress.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
DeliveryEntry = Entry(CustomerFrame, textvariable="address")
DeliveryEntry.grid(column=2, columnspan=3, row=4, padx=(0,0), pady=5, sticky="ew")
DeliveryAddress.grid_remove()
DeliveryEntry.grid_remove()

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

def deselect():
    if dpCheck.get() == 1:
        PickupCheck.deselect()
    elif dpCheck.get() == 0:
        DeliveryCheck.deselect()

# Pizza ordering frame
PizzaFrame = LabelFrame(root, text="Order")
PizzaFrame.grid(column=1, row=5, ipadx=10, ipady=10, padx=(20,20), pady=(0,5), sticky="ew")
ButtonFrame = Frame(PizzaFrame)
ButtonFrame.grid(column=3, row=1)

PizzaLabel = Label(text="Pizzas")
PizzaList = Treectrl(PizzaFrame)
PizzaList.column_create()
PizzaList.column_create()
PizzaList.column_create()
PizzaList.grid(column=1, row=1, padx=(20,0), pady=(10,0), ipadx=20, sticky="ew")
PizzaList.height = PizzaList.size()

#for i in pizza_list:
#    pizza_list_index = pizza_list_index + 1
#    PizzaList.insert(pizza_list_index, pizza_list[pizza_list_index])
#    if pizza_list_index = pizza_list:
#        break

RemoveButton = Button(ButtonFrame, text="Remove")
RemoveButton.grid(column=2, row=1, padx=20, pady=(10,0), sticky="ew")
LoadButton = Button(ButtonFrame, text="Load", command=OpenFile)
LoadButton.grid(column=2, row=2, padx=20, pady=(10,0), sticky="ew")

root.config(menu=menubar)
root.mainloop()