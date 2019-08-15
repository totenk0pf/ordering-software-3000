#Import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import trace

# Window - create window that's non-resizable and titled 'Paradise Pizza' with size of 340 of width and 620 of height
root = Tk()
root.geometry("340x620")
root.title("Paradise Pizza")
root.resizable(False, False)

# List of pizza that devide into 2 to seperate the price
common_pizza = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Egg Pizza", "Spicy Pizza", "Sea Pizza", "Hawaiian Pizza")
highclass_pizza = ("Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza", "The Ultimate Pizza")

# String
cusname = StringVar()
cusnum = StringVar()

dp_check = IntVar()
address = StringVar()

pset1 = StringVar()
pset2 = StringVar()
pset3 = StringVar()
pset4 = StringVar()
pset5 = StringVar()

display_name = StringVar()
display_phone = StringVar()
display_address = StringVar()

#Confirmbutton on receipt window
def cancel_rorder():
    receipt_window.destroy()

#Pass receipt window
def Pass():
    pass

#Calulate the pizza price
def calctotalcost():
    tcost = 0
    total_list = [(pset1.get()), (pset2.get()), (pset3.get()), (pset4.get()), (pset5.get())]
    for pizza in total_list:
        if pizza == "None":
            tcost += 0
        elif pizza in common_pizza:
            tcost += 8.5
        elif pizza in highclass_pizza:
            tcost += 13.5
if dp_check.get() == 1:
    tcost += 3
    cost_label.config(text=tcost)
    printcost.config(text=tcost)
    tcost = 0

def cal_on_click(self):
    calctotalcost()

#If delivery = ask for address
def showaddress():
    if dp_check.get() == 1:
        delivery_address.grid()
        delivery_entry.grid()
        PickupCheck.deselect()
        calctotalcost()
    elif dp_check.get() == 0:
        delivery_address.grid_remove()
        delivery_entry.grid_remove()
        delivery_check.deselect()
        calctotalcost()

#Connect with the order button to get all the input    
def save_info():
    calctotalcost()
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

#Validate input, make sure all infomation that required are filled
    if (cusname.get() == "") or (cusnum.get() == "") or (dp_check.get() == 1 and address.get() == ""):
        messagebox.showerror("Error","You must input all of the customer's information!")
    else:
    #Confirm that order to make sure they agree upon everything
        confirm_ask = messagebox.askyesno("Confirm order", "Do you wish to confirm the order?")
        if confirm_ask == True:
            display_name["text"] = cusname_info
            display_phone["text"] = cusnum_info
            if dp_check.get() == 1:
                display_address["text"] = address_info
            elif dp_check.get() == 0:
                #Clear-up everything after they finish the order which allow another order
                address_label.grid_remove()
                display_address.grid_remove()
            receipt_window.deiconify()
            name_info.delete(0, END)
            num_info.delete(0, END)
            delivery_entry.delete(0, END)
            print_pizza1['values'] = pizza_list
            print_pizza1.current(pick_pizza1.current())
            print_pizza2['values'] = pizza_list
            print_pizza2.current(pick_pizza2.current())
            print_pizza3['values'] = pizza_list
            print_pizza3.current(pick_pizza3.current())
            print_pizza4['values'] = pizza_list
            print_pizza4.current(pick_pizza4.current())
            print_pizza5['values'] = pizza_list
            print_pizza5.current(pick_pizza5.current())
            pick_pizza1.current(0)
            pick_pizza2.current(0)
            pick_pizza3.current(0)
            pick_pizza4.current(0)
            pick_pizza5.current(0)
            tcost = 0
            cost_label.config(text=tcost)

#Make function for cancel button on the 'Order' window
def cancel():
    cancelask = messagebox.askyesno("Cancel order", "Do you wish to cancel the order?")
    if cancelask == True:
        #delete: name's input, number's input, delivery's input and every picked pizza
        name_info.delete(0, END)
        num_info.delete(0, END)
        delivery_entry.delete(0, END)
        pick_pizza1.current(0)
        pick_pizza2.current(0)
        pick_pizza3.current(0)
        pick_pizza4.current(0)
        pick_pizza5.current(0)
        tcost = 0
        cost_label.config(text=tcost)

def main(*args):
#Program code       
    #Heading of the page
    heading = Label(text="Welcome to Paradise Pizza",font=("Monotype Corsiva",15), bg="orange red", width=35, height=2)
    heading2 = Label(text="Kia ~ Hello ~ Ni hao ~ Konichiwa",font=("Monotype Corsiva",8), bg="orange red")
    heading.grid(row=0, column=0, columnspan=4)
    heading2.grid(row=0, column=0, columnspan=4, rowspan=2, ipady=0)

    # Number or letter only validation
    # Only alphabet input are allowed
    def test_nam(inStr, acttyp):
        if acttyp == '1':
            if not inStr.isalpha():
                return False
        return True

    # Only number input are allowed
    def test_num(inStr,acttyp):
        if acttyp == '1':
            if not inStr.isdigit():
                return False
        return True

    #Ask for information
    name_cus = Label(root, text="Your Name :")
    phone_cus = Label(root, text="Phone Number :")
    #Ask for name
    name_info = Entry(root, textvariable=cusname, validate="key")
    name_info['validatecommand'] = (name_info.register(test_nam),'%P','%d')
    #Ask for number
    num_info = Entry(root, textvariable=cusnum, validate="key")
    num_info['validatecommand'] = (num_info.register(test_num),'%P','%d')
    name_cus.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
    phone_cus.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
    name_info.grid(row=1, column=2, sticky="ew", pady=5, padx=5)
    num_info.grid(row=2, column=2, sticky="ew", pady=5, padx=5)

    #Phone number input's validation
    #Allows only 14 numbers
    def namelimit(name_info):
        if len(cusname.get()) >= 14:
            cusname.set(cusname.get()[:14])
            num_info.focus()

    #Allows only 10 alphabets
    def numlimit(num_info):
        if len(cusnum.get()) >= 10:
            cusnum.set(cusnum.get()[:10])
            delivery_entry.focus()

    #trace the input from save_info
    cusname.trace('w', lambda *args:namelimit(name_info))
    cusnum.trace('w', lambda *args:numlimit(num_info))
    #Allow customer to pick-up or get a delivery

    dp_check.set(0)
    dp_label = Label(root, text="Delivery/Pickup", bg="orange red", width=50)
    dp_label.grid(column=0, columnspan=4, row=3, pady=5)

    #Telling customer that it would cost $3 extra to delivery
    deprice = Label(text="(+ $3)")
    deprice.grid(row=5, column=3)

    #Ask for address if they picked delivery
    delivery_address = Label(root, text="Address :")
    delivery_address.grid(column=1, row=6, padx=5, pady=5, sticky="ew")
    delivery_entry = Entry(root, textvariable=address)
    delivery_entry.grid(column=2, row=6, padx=5, pady=5, sticky="ew")

    #Checkbox for delivery/pick-up - trigger address input if picked delivery
    delivery_check = Checkbutton(root, text="Delivery", variable=dp_check, onvalue=1, offvalue=0, command=showaddress)
    delivery_check.grid(column=2, row=5, pady=5)
    PickupCheck = Checkbutton(root, text="Pickup", variable=dp_check, onvalue=0, offvalue=1, command=showaddress)
    PickupCheck.grid(column=2, row=4, pady=5)
    delivery_check.select()

    #Pizza list
    pizza_list = ("None", "Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Egg Pizza", "Spicy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza", "The Ultimate Pizza")
    pizzanam = Label(text="Choose Your Pizza", bg="orange red", width=50)
    pizzanam.grid(column=0, columnspan=4, row=7)
    pizzamax = Label(text="(5 Max)", bg="orange red")
    pizzamax.grid(column=3, row=7)

    #Pizza1's input in combobox
    Pizza1Lab = Label(text="Pizza 1 :")
    Pizza1Lab.grid(column=1, row=8, pady=5)
    pick_pizza1 = ttk.Combobox(root, state="readonly", textvariable=pset1)
    pick_pizza1['values'] = pizza_list
    pick_pizza1.current(0)
    pick_pizza1.grid(column=2, row=8, pady=5)

    #Pizza2's input in combobox
    Pizza2Lab = Label(text="Pizza 2 :")
    Pizza2Lab.grid(column=1, row=9, pady=5)
    pick_pizza2 = ttk.Combobox(root, state="readonly", textvariable=pset2)
    pick_pizza2['values'] = pizza_list
    pick_pizza2.current(0)
    pick_pizza2.grid(column=2, row=9, pady=5)

    #Pizza3's input in combobox
    Pizza3Lab = Label(text="Pizza 3 :")
    Pizza3Lab.grid(column=1, row=10, pady=5)
    pick_pizza3 = ttk.Combobox(root, state="readonly", textvariable=pset3)
    pick_pizza3['values'] = pizza_list
    pick_pizza3.current(0)
    pick_pizza3.grid(column=2, row=10, pady=5)

    #Pizza4's input in combobox
    Pizza4Lab = Label(text="Pizza 4 :")
    Pizza4Lab.grid(column=1, row=11, pady=5)
    pick_pizza4 = ttk.Combobox(root, state="readonly", textvariable=pset4)
    pick_pizza4['values'] = pizza_list
    pick_pizza4.current(0)
    pick_pizza4.grid(column=2, row=11, pady=5)

    #Pizza5's input in combobox
    Pizza5Lab = Label(text="Pizza 5 :")
    Pizza5Lab.grid(column=1, row=12, pady=5)
    pick_pizza5 = ttk.Combobox(root, state="readonly", textvariable=pset5)
    pick_pizza5['values'] = pizza_list
    pick_pizza5.current(0)
    pick_pizza5.grid(column=2, row=12, pady=5)

    #Total cost of the picked pizza
    tcost = 0
    none = 0
    totallabel = Label(text="Total cost :")
    totallabel.grid(column=1, row=15, pady=5)
    cost_label = Label(text=tcost)
    cost_label.grid(column=2, row=15, pady=5)

    #Print gathered information onto receipt window
    receipt_window  = Toplevel(root)
    infolabel = Label(receipt_window, text="Customer's Infomation", bg="orange red", width=36)
    infolabel.grid(column=0, columnspan=3, row=0)
    namelabel = Label(receipt_window, text="Name :")
    namelabel.grid(column=1, row=1, pady=2)
    display_name = Label(receipt_window, text="")
    display_name.grid(column=2, row=1, pady=2)
    PhoneLabel = Label(receipt_window, text="Number :")
    PhoneLabel.grid(column=1, row=2, pady=2)
    display_phone = Label(receipt_window, text="")
    display_phone.grid(column=2, row=2, pady=2)
    address_label = Label(receipt_window, text="Address :")
    address_label.grid(column=1, row=3, pady=2)
    display_address = Label(receipt_window, text="")
    display_address.grid(column=2, row=3, pady=2)

    #Print picked pizza on the receipt window
    PizzaInLabel = Label(receipt_window, text="Customer’s Pizza", bg="orange red", width=36)
    PizzaInLabel.grid(column=0, columnspan=3, row=4, pady=3)
    print_pizza1 = ttk.Combobox(receipt_window, state="disabled")
    print_pizza1.grid(column=0, columnspan=3, row=5)
    print_pizza1['values'] = pizza_list
    print_pizza1.current(pick_pizza1.current())
    print_pizza2 = ttk.Combobox(receipt_window, state="disabled")
    print_pizza2.grid(column=0, columnspan=3, row=6)
    print_pizza2['values'] = pizza_list
    print_pizza2.current(pick_pizza2.current())
    print_pizza3 = ttk.Combobox(receipt_window, state="disabled")
    print_pizza3.grid(column=0, columnspan=3, row=7)
    print_pizza3['values'] = pizza_list
    print_pizza3.current(pick_pizza3.current())
    print_pizza4 = ttk.Combobox(receipt_window, state="disabled")
    print_pizza4.grid(column=0, columnspan=3, row=8)
    print_pizza4['values'] = pizza_list
    print_pizza4.current(pick_pizza4.current())
    print_pizza5 = ttk.Combobox(receipt_window, state="disabled")
    print_pizza5.grid(column=0, columnspan=3, row=9)
    print_pizza5['values'] = pizza_list
    print_pizza5.current(pick_pizza5.current())

    #Print the total cost
    print_cost_label = Label(receipt_window, text="Total cost:            $")
    print_cost_label.grid(column=1, row=10, pady=2)
    printcost = Label(receipt_window, text="")
    printcost.grid(column=2, row=10, pady=2)

    #Confirmbutton on receipt window to exit and confirm the order
    confirmbutton = Button(receipt_window, text="Confirm", command=receipt_window.withdraw, bg="orange red")
    confirmbutton.grid(row=11, column=0, columnspan=3, sticky="ew")
    cancelwindow = Button(receipt_window, text="Cancel", command=cancel_rorder, bg="silver")
    cancelwindow.grid(row=12, column=0, columnspan=3, sticky="ew")

    #receipt's window structure
    receipt_window.geometry("")
    receipt_window.resizable(False, False)
    receipt_window.protocol("WM_DELETE_WINDOW", Pass)
    receipt_window.withdraw()

    #Calulation
    tcost=0

    pick_pizza1.bind("<<ComboboxSelected>>", cal_on_click)
    pick_pizza2.bind("<<ComboboxSelected>>", cal_on_click)
    pick_pizza3.bind("<<ComboboxSelected>>", cal_on_click)
    pick_pizza4.bind("<<ComboboxSelected>>", cal_on_click)
    pick_pizza5.bind("<<ComboboxSelected>>", cal_on_click)

    #Order button for the front page
    order = Button(text="Order", command=save_info, bg="orange red")
    order.grid(row=13, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)

    #Exit Button for the front page
    exit_but = Button(root, text="Exit", command=root.destroy, bg="silver")
    exit_but.grid(row=0, rowspan=5, column=3, sticky="ew", pady=5, padx=20, ipadx=15, ipady=3)

    #Cancel Button for the front page
    cancel_but = Button(text="Cancel", command=cancel, bg="silver")
    cancel_but.grid (row=14, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)

    #Footing for the front page
    footing = Label(text="Thank you",font=("Monotype Corsiva",15), bg="orange red", width=35, height=3)
    footing.grid(row=16, column=0, columnspan=4)
    footing2 = Label(text="...",font=("Monotype Corsiva",15), bg="orange red", width=35, height=10)
    footing2.grid(row=17, column=0, columnspan=4, ipady=0)
    footing3 = Label(text="Contact us ~0275930535~",font=("Monotype Corsiva",10), bg="orange red")
    footing3.grid(rowspan=17, row=8, columnspan=4, column=0)

main()

root.mainloop()