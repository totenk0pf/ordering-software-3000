#Import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import trace

class mainwindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
    # Window - create window that's non-resizable and titled 'Paradise Pizza' with size of 340 of width and 620 of height
        root.geometry("340x620")
        root.title("Paradise Pizza")
        root.resizable(False, False)
        self.run()

    def run(self, *args):
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
        self.name_cus = Label(root, text="Your Name :")
        self.phone_cus = Label(root, text="Phone Number :")
        #Ask for name
        self.name_info = Entry(root, textvariable=var.cusname, validate="key")
        self.name_info['validatecommand'] = (self.name_info.register(test_nam),'%P','%d')
        #Ask for number
        self.num_info = Entry(root, textvariable=var.cusnum, validate="key")
        self.num_info['validatecommand'] = (self.num_info.register(test_num),'%P','%d')
        self.name_cus.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
        self.phone_cus.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
        self.name_info.grid(row=1, column=2, sticky="ew", pady=5, padx=5)
        self.num_info.grid(row=2, column=2, sticky="ew", pady=5, padx=5)

        #trace the input from save_info
        var.cusname.trace('w', lambda *args:namelimit(self.name_info))
        var.cusnum.trace('w', lambda *args:numlimit(self.num_info))

        #Allow customer to pick-up or get a delivery
        var.dp_check.set(0)
        self.dp_label = Label(root, text="Delivery/Pickup", bg="orange red", width=50)
        self.dp_label.grid(column=0, columnspan=4, row=3, pady=5)

        #Telling customer that it would cost $3 extra to delivery
        self.deprice = Label(text="(+ $3)")
        self.deprice.grid(row=5, column=3)

        #Ask for address if they picked delivery
        self.delivery_address = Label(root, text="Address :")
        self.delivery_address.grid(column=1, row=6, padx=5, pady=5, sticky="ew")
        self.delivery_entry = Entry(root, textvariable=var.address)
        self.delivery_entry.grid(column=2, row=6, padx=5, pady=5, sticky="ew")
        
        #If delivery = ask for address
        def showaddress():
            if var.dp_check.get() == 1:
                self.delivery_address.grid()
                self.delivery_entry.grid()
                self.PickupCheck.deselect()
                calctotalcost()
            elif var.dp_check.get() == 0:
                self.delivery_address.grid_remove()
                self.delivery_entry.grid_remove()
                self.delivery_check.deselect()
                calctotalcost()
                
        #Checkbox for delivery/pick-up - trigger address input if picked delivery
        self.delivery_check = Checkbutton(root, text="Delivery", variable=var.dp_check, onvalue=1, offvalue=0, command=showaddress)
        self.delivery_check.grid(column=2, row=5, pady=5)
        self.PickupCheck = Checkbutton(root, text="Pickup", variable=var.dp_check, onvalue=0, offvalue=1, command=showaddress)
        self.PickupCheck.grid(column=2, row=4, pady=5)
        self.delivery_check.select()

        #Pizza list
        self.pizzanam = Label(text="Choose Your Pizza", bg="orange red", width=50)
        self.pizzanam.grid(column=0, columnspan=4, row=7)
        self.pizzamax = Label(text="(5 Max)", bg="orange red")
        self.pizzamax.grid(column=3, row=7)

        #Pizza1's input in combobox
        self.Pizza1Lab = Label(text="Pizza 1 :")
        self.Pizza1Lab.grid(column=1, row=8, pady=5)
        self.pick_pizza1 = ttk.Combobox(root, state="readonly", textvariable=var.pset1)
        self.pick_pizza1['values'] = var.pizza_list
        self.pick_pizza1.current(0)
        self.pick_pizza1.grid(column=2, row=8, pady=5)

        #Pizza2's input in combobox
        self.Pizza2Lab = Label(text="Pizza 2 :")
        self.Pizza2Lab.grid(column=1, row=9, pady=5)
        self.pick_pizza2 = ttk.Combobox(root, state="readonly", textvariable=var.pset2)
        self.pick_pizza2['values'] = var.pizza_list
        self.pick_pizza2.current(0)
        self.pick_pizza2.grid(column=2, row=9, pady=5)

        #Pizza3's input in combobox
        self.Pizza3Lab = Label(text="Pizza 3 :")
        self.Pizza3Lab.grid(column=1, row=10, pady=5)
        self.pick_pizza3 = ttk.Combobox(root, state="readonly", textvariable=var.pset3)
        self.pick_pizza3['values'] = var.pizza_list
        self.pick_pizza3.current(0)
        self.pick_pizza3.grid(column=2, row=10, pady=5)

        #Pizza4's input in combobox
        self.Pizza4Lab = Label(text="Pizza 4 :")
        self.Pizza4Lab.grid(column=1, row=11, pady=5)
        self.pick_pizza4 = ttk.Combobox(root, state="readonly", textvariable=var.pset4)
        self.pick_pizza4['values'] = var.pizza_list
        self.pick_pizza4.current(0)
        self.pick_pizza4.grid(column=2, row=11, pady=5)

        #Pizza5's input in combobox
        self.Pizza5Lab = Label(text="Pizza 5 :")
        self.Pizza5Lab.grid(column=1, row=12, pady=5)
        self.pick_pizza5 = ttk.Combobox(root, state="readonly", textvariable=var.pset5)
        self.pick_pizza5['values'] = var.pizza_list
        self.pick_pizza5.current(0)
        self.pick_pizza5.grid(column=2, row=12, pady=5)

        #Total cost of the picked pizza
        self.tcost = 0
        self.none = 0
        self.totallabel = Label(text="Total cost :")
        self.totallabel.grid(column=1, row=15, pady=5)
        self.cost_label = Label(text=self.tcost)
        self.cost_label.grid(column=2, row=15, pady=5)

        #Calulate the pizza price
        def calctotalcost():
            self.tcost = 0
            total_list = [(pset1.get()), (pset2.get()), (pset3.get()), (pset4.get()), (pset5.get())]
            for pizza in total_list:
                if pizza == "None":
                    self.tcost += 0
                elif pizza in common_pizza:
                    self.tcost += 8.5
                elif pizza in highclass_pizza:
                    self.tcost += 13.5

        if var.dp_check.get() == 1:
            self.tcost += 3
            self.cost_label.config(text=self.tcost)
            receiptapp.printtcost.config(text=self.tcost)
            self.tcost = 0

        def cal_on_click(self):
            calctotalcost()

        self.pick_pizza1.bind("<<ComboboxSelected>>", cal_on_click)
        self.pick_pizza2.bind("<<ComboboxSelected>>", cal_on_click)
        self.pick_pizza3.bind("<<ComboboxSelected>>", cal_on_click)
        self.pick_pizza4.bind("<<ComboboxSelected>>", cal_on_click)
        self.pick_pizza5.bind("<<ComboboxSelected>>", cal_on_click)

        #Order button for the front page
        self.order = Button(text="Order", command=save_info, bg="orange red")
        self.order.grid(row=13, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)

        #Exit Button for the front page
        self.exit_but = Button(root, text="Exit", command=root.destroy, bg="silver")
        self.exit_but.grid(row=0, rowspan=5, column=3, sticky="ew", pady=5, padx=20, ipadx=15, ipady=3)

        #Cancel Button for the front page
        self.cancel_but = Button(text="Cancel", command=cancel, bg="silver")
        self.cancel_but.grid (row=14, column=2, sticky="ew", ipadx=35, ipady=5, pady=5)

        #Footing for the front page
        self.footing = Label(text="Thank you",font=("Monotype Corsiva",15), bg="orange red", width=35, height=3)
        self.footing.grid(row=16, column=0, columnspan=4)
        self.footing2 = Label(text="...",font=("Monotype Corsiva",15), bg="orange red", width=35, height=10)
        self.footing2.grid(row=17, column=0, columnspan=4, ipady=0)
        self.footing3 = Label(text="Contact us ~0275930535~",font=("Monotype Corsiva",10), bg="orange red")
        self.footing3.grid(rowspan=17, row=8, columnspan=4, column=0)

        #Phone number input's validation
        #Allows only 14 numbers
        def namelimit(name_info):
            if len(var.cusname.get()) >= 14:
                var.cusname.set(var.cusname.get()[:14])
                self.num_info.focus()

        #Allows only 10 alphabets
        def numlimit(num_info):
            if len(var.cusnum.get()) >= 10:
                var.cusnum.set(var.cusnum.get()[:10])
                self.delivery_entry.focus()


        #Confirmbutton on receipt window
        def cancel_rorder():
            receiptapp.destroy()

        #Connect with the self.order button to get all the input    
        def save_info():
            calctotalcost()
            cusself.name_info = var.cusname.get()
            cusself.num_info = str(var.cusnum.get())
            address_info = address.get()
            print("Name: ", cusself.name_info,", Number: ", cusself.num_info,", Address: ", address_info)

            file = open("user.txt", "w")
            file.write(cusself.name_info)
            file.write(cusself.num_info)
            file.write(address_info)
            file.close()
            print(" Customer name ", cusself.name_info, "has been self.ordered successfully")

        #Validate input, make sure all infomation that required are filled
            if (var.cusname.get() == "") or (var.cusnum.get() == "") or (var.dp_check.get() == 1 and address.get() == ""):
                messagebox.showerror("Error","You must input all of the customer's information!")
            else:
            #Confirm that self.order to make sure they agree upon everything
                confirm_ask = messagebox.askyesno("Confirm self.order", "Do you wish to confirm the self.order?")
                if confirm_ask == True:
                    self.display_name["text"] = cusself.name_info
                    self.display_phone["text"] = cusself.num_info
                    if var.dp_check.get() == 1:
                        self.display_address["text"] = address_info
                    elif var.dp_check.get() == 0:
                        #Clear-up everything after they finish the self.order which allow another self.order
                        self.address_label.grid_remove()
                        self.display_address.grid_remove()
                    self.deiconify()
                    self.name_info.delete(0, END)
                    self.num_info.delete(0, END)
                    self.delivery_entry.delete(0, END)
                    self.print_pizza1['values'] = var.pizza_list
                    self.print_pizza1.current(self.pick_pizza1.current())
                    self.print_pizza2['values'] = var.pizza_list
                    self.print_pizza2.current(self.pick_pizza2.current())
                    self.print_pizza3['values'] = var.pizza_list
                    self.print_pizza3.current(self.pick_pizza3.current())
                    self.print_pizza4['values'] = var.pizza_list
                    self.print_pizza4.current(self.pick_pizza4.current())
                    self.print_pizza5['values'] = var.pizza_list
                    self.print_pizza5.current(self.pick_pizza5.current())
                    self.pick_pizza1.current(0)
                    self.pick_pizza2.current(0)
                    self.pick_pizza3.current(0)
                    self.pick_pizza4.current(0)
                    self.pick_pizza5.current(0)
                    self.tcost = 0
                    self.cost_label.config(text=self.tcost)

        #Make function for cancel button on the 'Order' window
        def cancel():
            cancelask = messagebox.askyesno("Cancel order", "Do you wish to cancel the order?")
            if cancelask == True:
                #delete: name's input, number's input, delivery's input and every picked pizza
                self.name_info.delete(0, END)
                self.num_info.delete(0, END)
                self.delivery_entry.delete(0, END)
                self.pick_pizza1.current(0)
                self.pick_pizza2.current(0)
                self.pick_pizza3.current(0)
                self.pick_pizza4.current(0)
                self.pick_pizza5.current(0)
                self.tcost = 0
                self.cost_label.config(text=self.tcost)

root = Tk()

class receiptwindow(Toplevel):
    def __init__(self, master=None):
            Toplevel.__init__(self, master)
            #receipt's window structure
            #self.master.geometry("")
            self.master.resizable(False, False)
            self.master.protocol("WM_DELETE_WINDOW", self.Pass)
            self.master.withdraw()
            self.run()

    #Pass receipt window
    def Pass():
        pass

    def run(self, *args):
            #Print gathered information onto receipt window
            self.infolabel = Label(self, text="Customer's Infomation", bg="orange red", width=36)
            self.infolabel.grid(column=0, columnspan=3, row=0)
            self.namelabel = Label(self, text="Name :")
            self.namelabel.grid(column=1, row=1, pady=2)
            self.display_name = Label(self, text="")
            self.display_name.grid(column=2, row=1, pady=2)
            self.PhoneLabel = Label(self, text="Number :")
            self.PhoneLabel.grid(column=1, row=2, pady=2)
            self.display_phone = Label(self, text="")
            self.display_phone.grid(column=2, row=2, pady=2)
            self.address_label = Label(self, text="Address :")
            self.address_label.grid(column=1, row=3, pady=2)
            self.display_address = Label(self, text="")
            self.display_address.grid(column=2, row=3, pady=2)

            #Print picked pizza on the receipt window
            self.PizzaInLabel = Label(self, text="Customer’s Pizza", bg="orange red", width=36)
            self.PizzaInLabel.grid(column=0, columnspan=3, row=4, pady=3)
            self.print_pizza1 = ttk.Combobox(self, state="disabled")
            self.print_pizza1.grid(column=0, columnspan=3, row=5)
            self.print_pizza1['values'] = var.pizza_list
            self.print_pizza1.current(self.pick_pizza1.current())
            self.print_pizza2 = ttk.Combobox(self, state="disabled")
            self.print_pizza2.grid(column=0, columnspan=3, row=6)
            self.print_pizza2['values'] = var.pizza_list
            self.print_pizza2.current(self.pick_pizza2.current())
            self.print_pizza3 = ttk.Combobox(self, state="disabled")
            self.print_pizza3.grid(column=0, columnspan=3, row=7)
            self.print_pizza3['values'] = var.pizza_list
            self.print_pizza3.current(self.pick_pizza3.current())
            self.print_pizza4 = ttk.Combobox(self, state="disabled")
            self.print_pizza4.grid(column=0, columnspan=3, row=8)
            self.print_pizza4['values'] = var.pizza_list
            self.print_pizza4.current(self.pick_pizza4.current())
            self.print_pizza5 = ttk.Combobox(self, state="disabled")
            self.print_pizza5.grid(column=0, columnspan=3, row=9)
            self.print_pizza5['values'] = var.pizza_list
            self.print_pizza5.current(self.pick_pizza5.current())

            #Print the total cost
            self.print_cost_label = Label(self, text="Total cost:            $")
            self.print_cost_label.grid(column=1, row=10, pady=2)
            self.printtcost = Label(self, text="")
            self.printtcost.grid(column=2, row=10, pady=2)

            #Confirmbutton on receipt window to exit and confirm the self.order
            self.confirmbutton = Button(self, text="Confirm", command=self.withdraw, bg="orange red")
            self.confirmbutton.grid(row=11, column=0, columnspan=3, sticky="ew")
            self.cancelwindow = Button(self, text="Cancel", command=cancel_rorder, bg="silver")
            self.cancelwindow.grid(row=12, column=0, columnspan=3, sticky="ew")

class variables():
    def __init__(self):
        # List of pizza that devide into 2 to seperate the price
        self.pizza_list = ("None", "Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Egg Pizza", "Spicy Pizza", "Sea Pizza", "Hawaiian Pizza", "Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza", "The Ultimate Pizza")
        self.common_pizza = ("Meat Combo Pizza", "Meat Hater Pizza", "Cheesy Pizza", "Egg Pizza", "Spicy Pizza", "Sea Pizza", "Hawaiian Pizza")
        self.highclass_pizza = ("Original Italian Pizza", "Mix BBQ Pizza", "The Epic Pizza", "The Ultimate Pizza")

        # String
        self.cusname = StringVar()
        self.cusnum = StringVar()

        self.dp_check = IntVar()
        self.address = StringVar()

        self.pset1 = StringVar()
        self.pset2 = StringVar()
        self.pset3 = StringVar()
        self.pset4 = StringVar()
        self.pset5 = StringVar()

        self.display_name = StringVar()
        self.display_phone = StringVar()
        self.display_address = StringVar()

var = variables()

mainapp = mainwindow(root)
receiptapp = receiptwindow(root)

root.mainloop()
