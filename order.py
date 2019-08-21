# PIZZA ORDERING SOFTWARE
# -- can I get 12 credits please?
# https://github.com/totenk0pf/ordering-software-3000

# SOURCES:
# http://effbot.org/tkinterbook/ - REFERENCES & DOCUMENTATION
# https://docs.python.org/3/library/tk.html - OFFICIAL DOCUMENTATION
# https://python-textbok.readthedocs.io/en/latest/Introduction_to_GUI_Programming.html - PROGRAM STRUCTURE

# https://www.vecteezy.com/vector-art/553406-pizza-slice-vector-icon - ICON USED IN THE PROGRAM (FREE FOR PERSONAL USE - ORIGINAL BY VECTEEZY)

import os
import json

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.colorchooser import *

class main_window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.grid(column=1, row=1)
                self.master.title("Pizza Ordering Software")
                self.master.resizable(False, False)
                self.master.iconbitmap('favicon.ico')
                self.master.attributes("-topmost", True)
                self.widget()

                self.columnconfigure(2, weight=0)
                self.columnconfigure(3, weight=3)
                self.columnconfigure(4, weight=4)
                
        # Calculate the total cost
        def calc_total_cost(self):
                if val.dp_check.get() == 1:
                        val.total_cost = (val.total_amount_regular * 8.50) + (val.total_amount_gourmet * 13.50) + 3
                elif val.dp_check.get() == 0:
                        val.total_cost = (val.total_amount_regular * 8.50) + (val.total_amount_gourmet * 13.50)

        def widget(self, *args):
                # Main GUI
                # Header
                self.head_label = Label(self, bg="#FFFFFF", relief="sunken", borderwidth=2)
                self.head_label.grid(column=1, row=1, ipadx=0, ipady=50, padx=20, pady=(10,5), sticky="ew")

                # Load "config.json" file at launch by using Python's built-in JSON parsing module
                def load_config():
                        try:
                                with open('config.json') as config:
                                        loaded_config = json.load(config)
                                        self.display_shop_name = loaded_config['shopname'] + "'s" + " " + "Pizza Shop"
                                        self.head_label['text'] = self.display_shop_name
                                        self.head_label['bg'] = loaded_config['headerbg']
                        except:
                                print("Config failed to load!")
                load_config()
                
                # Customer's details frame
                self.customer_frame = LabelFrame(self, text="Customer's details")
                self.customer_frame.grid(column=1, row=2, ipadx=10, ipady=10, padx=(20), pady=(10,5), sticky="ew")

                # Validation
                def only_characters(char): # Return whether the input is a character or not
                        return char.isalpha()
                def only_numbers(char): # Return whether the input is a number or not
                        return char.isdigit()

                # Phone number input's validation
                
                def fnameLimit(first_name_input):
                        if len(val.firstname.get()) >= 10:
                                val.firstname.set(val.firstname.get()[:10])
                                self.last_name_input.focus()
                def lnameLimit(last_name_input):
                        if len(val.lastname.get()) >= 10:
                                val.lastname.set(val.lastname.get()[:10])
                                self.phone_input.focus()
                def phone1Limit(phone_input):
                        if len(val.phonein1.get()) >= 9:
                                val.phonein1.set(val.phonein1.get()[:9])
                                self.delivery_entry.focus()
                
                # Registers commands so they can be called during validation
                ccmd = self.register(only_characters)
                ncmd = self.register(only_numbers)

                # The trace function is applied to input fields to trace the user's input (validation)
                val.firstname.trace('w', lambda *args:fnameLimit(self.first_name_input))
                val.lastname.trace('w', lambda *args:lnameLimit(self.last_name_input))
                val.phonein1.trace('w', lambda *args:phone1Limit(self.phone_input))

                # Input customer's name
                self.name_label = Label(self.customer_frame, text="Customer's name:")
                self.name_label.grid(column=1, row=1, padx=(20,10), pady=(15,5))
                self.first_name_input = Entry(self.customer_frame, textvariable=val.firstname, validate="key", validatecommand=(ccmd, '%S'))
                self.first_name_input.grid(column=2, row=1, padx=(0,10), pady=(15,5), sticky="ew")
                self.last_name_input = Entry(self.customer_frame, textvariable=val.lastname, validate="key", validatecommand=(ccmd, '%S'))
                self.last_name_input.grid(column=3, row=1, padx=(0,10), pady=(15,5), sticky="ew")
                #"key" is the type of validation that triggers the command assigned to "validatecommand", which in turn is called upon when "key" is detected in the input fields. "validatecommand" applies the given command onto "%S" (the text string being inserted/deleted).

                # Input customer's phone number
                self.phone_label = Label(self.customer_frame, text="Phone number:")
                self.phone_label.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
                self.phone_input = Entry(self.customer_frame, textvariable=val.phonein1, validate="key", validatecommand=(ncmd, '%S')) # The same validation method from above is applied
                self.phone_input.grid(column=2, columnspan=2, row=2, padx=(0,10), pady=5, sticky="ew")

                # Delivery/Pickup
                self.dp_label = Label(self.customer_frame, text="Delivery/Pickup:")
                self.dp_label.grid(column=1, row=3, padx=(20,10), pady=5)

                # Displays/hides address entry
                def show_address(): # Function retrieves a value from the var class, to see which checkbox is being ticked.
                        if val.dp_check.get() == 1: 
                                self.delivery_address.grid()
                                self.delivery_entry.grid()
                        elif val.dp_check.get() == 0:
                                self.delivery_address.grid_remove()
                                self.delivery_entry.grid_remove()
                        self.calc_total_cost()
                        self.order_list.set(self.total_row, column="one", value=val.total_cost) # The cost is recalculated and price displays are reset to the new value.

                # Deselects the other checkbox automatically
                def deselect():
                        if val.dp_check.get() == 1:
                                self.pickup_check.deselect()
                        elif val.dp_check.get() == 0:
                                self.delivery_check.deselect()

                self.delivery_check = Checkbutton(self.customer_frame, text="Delivery (+$3)", variable=val.dp_check, onvalue=1, offvalue=0, command=show_address)
                self.delivery_check.grid(column=2, row=3, padx=(0,10), pady=5)
                self.delivery_check.select()
                self.pickup_check = Checkbutton(self.customer_frame, text="Pickup", variable=val.dp_check, onvalue=0, offvalue=1, command=show_address)
                self.pickup_check.grid(column=3, row=3, padx=(0,10), pady=5)

                self.delivery_address = Label(self.customer_frame, text="Customer's address:")
                self.delivery_address.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
                self.delivery_entry = Entry(self.customer_frame, textvariable=val.address)
                self.delivery_entry.grid(column=2, columnspan=2, row=4, padx=(0,10), pady=5, sticky="ew")

                # Pizza ordering frame
                self.pizza_frame = LabelFrame(self, text="Order")
                self.pizza_frame.grid(column=1, row=3, ipadx=10, ipady=10, padx=(20,20), pady=(0,5), sticky="ew")
                self.button_frame = Frame(self.pizza_frame)
                self.button_frame.grid(column=2, row=1, padx=(20))

                self.pizza_list = ttk.Treeview(self.pizza_frame, height=14, selectmode="browse")
                self.pizza_list["columns"]=("one")
                self.pizza_list.column("#0", width=150, minwidth=150, stretch=NO)
                self.pizza_list.column("one", width=50, minwidth=50, stretch=NO)
                self.pizza_list.heading("#0", text="Name", anchor="w")
                self.pizza_list.heading("one", text="Price", anchor="w")

                # Adds the selected pizza
                def add_pizza():
                        selected_item = self.pizza_list.focus()
                        return_item = self.pizza_list.item(selected_item)
                        get_item_name = return_item.get('text')
                        if val.total_amount <= 4: # Checks if the total amount of pizzas ordered is less than 4 or not
                                while get_item_name not in ["Regular Pizzas","Gourmet Pizzas"]: # Checks if the selected pizza is the category and not an actual pizza
                                        if self.pizza_list.parent(selected_item) == self.regular_pizza:
                                                self.order_list.insert(self.regular_pizza, "end", val.dynamic_iid, text=get_item_name, values=1) # Insert a pizza with values retrieved from the selection
                                                val.total_amount_regular += 1 # Increases the amount counter by 1
                                                val.print_list_reg.append(get_item_name) # Adds an item to the receipt/print list with values retrieved from the selection.
                                                break
                                        elif self.pizza_list.parent(selected_item) == self.gourmet_pizza: # Same code from above, but for gourmet pizzas
                                                self.order_list.insert(self.gourmet_pizza, "end", val.dynamic_iid, text=get_item_name, values=1)
                                                val.total_amount_gourmet += 1
                                                val.print_list_gour.append(get_item_name)
                                                break
                                val.total_amount = val.total_amount_regular + val.total_amount_gourmet # Calculates the total amount of pizzas
                        val.dynamic_iid += 1 # Increases the IID counter
                        main_app.calc_total_cost() 
                        self.order_list.set(self.total_row, column="one", value=val.total_cost) # Calculates the total cost and reset the price displays to the new value.
                        if val.total_amount > 4:
                            messagebox.showwarning("Invalid", "Maximum amount of pizzas allowed is 5.") # Shows a warning if the user tries to add more than 5 pizzas.

                # Removes the selected pizza
                def remove_pizza():
                        selected_order_item = self.order_list.focus()
                        return_order_item = self.order_list.item(selected_order_item)
                        get_order_item_name = return_order_item.get('text')
                        
                        if self.order_list.focus() == "":
                                messagebox.showwarning("Error", "Please select a pizza to remove!") # Shows a warning if the user doesn't select a pizza to be removed.
                        else:
                                if get_order_item_name not in ["Regular Pizzas", "Gourmet Pizzas"]: # Checks if the selected pizza is the category and not an actual pizza
                                        if self.order_list.parent(selected_order_item) == "RGP": # Checks what group the selected pizza belongs to
                                                self.order_list.delete(selected_order_item) # Removes item from the order list
                                                val.print_list_reg.remove(get_order_item_name)
                                                val.total_cost -= 8.5 # Deducts a value from the total cost
                                                val.total_amount_regular -= 1 # Deducts the total amount of regular pizzas
                                        elif self.order_list.parent(selected_order_item) == "GP": # Same code from above, but for gourmet pizzas
                                                self.order_list.delete(selected_order_item)
                                                val.print_list_gour.remove(get_order_item_name)
                                                val.total_cost -= 13.5
                                                val.total_amount_gourmet -= 1
                                        val.total_amount = val.total_amount_regular + val.total_amount_gourmet
                                        main_app.calc_total_cost()
                                        self.order_list.set(self.total_row, column="one", value=val.total_cost)
                
                self.add_button = Button(self.button_frame, text="Add", command=add_pizza)
                self.add_button.grid(column=1, row=1, padx=5, pady=(10,0), sticky="ew")
                self.remove_button = Button(self.button_frame, text="Remove", command=remove_pizza)
                self.remove_button.grid(column=1, row=2, padx=5, pady=(10,0), sticky="ew")

                # REGULAR PIZZAS
                self.regular_pizza = self.pizza_list.insert("", 1, "RGP", text="Regular Pizzas") # Adds a regular pizza category to the pizza list
                self.pizza_list.item(self.regular_pizza, open=True) # Expands the category 
                for i in val.init_reg_dict:
                        self.pizza_list.insert(self.regular_pizza, "end", text=i[0], values=i[1]) # Inserts the regular pizzas into the pizza list

                # GOURMET PIZZAS
                self.gourmet_pizza = self.pizza_list.insert("", 2, "GP", text="Gourmet Pizzas" ) # Adds a gourmet pizza category to the pizza list
                self.pizza_list.item(self.gourmet_pizza, open=True) # Expands the category
                for i in val.init_gour_dict:
                        self.pizza_list.insert(self.gourmet_pizza, "end", text=i[0], values=i[1]) # Inserts the gourmet pizzas into the pizza list

                self.pizza_list.grid(column=1, row=1, padx=(20,0), pady=(10,0), sticky="ew")

                self.order_list = ttk.Treeview(self.pizza_frame, height=14, selectmode="browse")
                self.order_list["columns"]=("one")
                self.order_list.column("#0", width=150, minwidth=150, stretch=NO)
                self.order_list.column("one", width=50, minwidth=50, stretch=NO)
                self.order_list.heading("#0", text="Name", anchor="w")
                self.order_list.heading("one", text="Amount", anchor="w")
                self.order_list.grid(column=3, row=1, padx=0, pady=(10,0), sticky="ew")
                self.regular_pizza = self.order_list.insert("", 1, "RGP", text="Regular Pizzas") # Adds a regular pizza category into the order list 
                self.order_list.item(self.regular_pizza, open=True) # Expands the category 
                self.gourmet_pizza = self.order_list.insert("", 2, "GP", text="Gourmet Pizzas") # Adds a gourmet pizza category to the pizza list
                self.order_list.item(self.gourmet_pizza, open=True) # Expands the category 
                self.total_row = self.order_list.insert("", 3, "TT", text="Total cost:", values=val.total_cost) # Sets the total cost to its initial value

                # Save & load functions (in progress)
                def open_file():
                        load_info = askopenfilename(initialdir="C:/Users/Admin/Desktop",
                                                filetypes =(("JSON File", "*.json"),("All Files","*.*")),
                                                title = "Choose a file."
                                                ) # Initializes a prompt asking for a JSON file
                        try:
                                with open(load_info,'r') as custInfo:
                                        loadcustList = json.load(custInfo) # Parses the chosen JSON file, and retrieves the embedded list
                                        val.firstname.set(loadcustList['firstname']) # Sets customer's first name
                                        val.lastname.set(loadcustList['lastname']) # Sets customer's last name
                                        val.phonein1.set(loadcustList['number']) # Sets customer's phone number
                                        self.first_name_input.config(validate="key") # Sets the validation for entry fields
                                        self.last_name_input.config(validate="key") 
                                        self.phone_input.config(validate="key")
                                        del val.print_list_reg[:] # Empties the regular print list 
                                        del val.print_list_gour[:] # Empties the gourmet print list
                                        val.print_list_reg = loadcustList['reglist'] # Replaces the regular print list's elements with those from the parsed JSON file.
                                        val.print_list_gour = loadcustList['gourlist'] # Replaces the gourmet print list's elements with those from the parsed JSON file.
                                        if loadcustList['option'] == 1: # Works the same as the deselect() function
                                                self.delivery_check.select()
                                                self.pickup_check.deselect()
                                                show_address()
                                        else:
                                                self.pickup_check.select()
                                                self.delivery_check.deselect()
                                                show_address()
                                        val.address.set(loadcustList['address']) # Sets customer's address
                                        for i in self.order_list.get_children(self.regular_pizza): # Empties the regular order list 
                                                self.order_list.delete(i)
                                                val.total_amount_regular = 0
                                        for i in self.order_list.get_children(self.gourmet_pizza): # Empties the gourmet order list
                                                self.order_list.delete(i)
                                                val.total_amount_gourmet = 0
                                        for item in val.print_list_reg: # Adds the pizzas in the regular print list 
                                                self.order_list.insert(self.regular_pizza, "end", val.dynamic_iid, text=item, values=1)
                                                val.total_amount_regular += 1
                                                val.dynamic_iid += 1
                                        for item in val.print_list_gour: # Adds the pizzas in the gourmet print list 
                                                self.order_list.insert(self.gourmet_pizza, "end", val.dynamic_iid, text=item, values=1)
                                                val.total_amount_gourmet += 1
                                                val.dynamic_iid += 1
                                        main_app.calc_total_cost() # Calculates the total cost
                                        val.total_amount = val.total_amount_regular + val.total_amount_gourmet # Calculates the total amount
                                        self.order_list.set(self.total_row, column="one", value=val.total_cost) # Sets the total cost display
                        except:
                                print("File failed to load!") # Prints a message should the file fail to load
                        

                def save_file():
                        if len(self.first_name_input.get()) == 0 or len(self.last_name_input.get()) == 0 or len(self.phone_input.get()) == 0 or (len(val.address.get()) == 0 and val.dp_check.get() == 1):
                                        messagebox.showerror("Error", "Please input all of the customer's information.") # Displays an error if an input field is left blank
                        else:
                                        saveInfo = asksaveasfilename(initialdir="C:/Users/Admin/Desktop",
                                                                filetypes =(("JSON File", "*.json"),("All Files","*.*")),
                                                                title = "Save a file."
                                                                ) # # Initializes a prompt asking for a directory to save the JSON file
                                        filename = saveInfo + ".json"
                                        custfirstname = self.first_name_input.get()
                                        custlastname = self.last_name_input.get()
                                        custphone_number = self.phone_input.get()
                                        custaddress = self.delivery_entry.get()
                                        saveDict = {
                                        "firstname": custfirstname,
                                        "lastname": custlastname,
                                        "number": custphone_number,
                                        "option": 1,
                                        "address": custaddress,
                                        "reglist": val.print_list_reg,
                                        "gourlist": val.print_list_gour
                                        }
                                        if val.dp_check.get() == 1:
                                                saveDict['option'] = 1
                                        elif val.dp_check.get() == 0:
                                                saveDict['option'] = 0
                                        with open(filename,'w') as saveCustInfo:
                                                json.dump(saveDict, saveCustInfo)

                # Save & load buttons
                sl_frame = Frame(self.customer_frame)
                sl_frame.grid(column=4, row=1, rowspan=4)
                save_button = Button(sl_frame, text="Save", command=save_file)
                save_button.grid(column=1, row=1, rowspan=2, ipadx=30, ipady=10, padx=(20,0), pady=(10), sticky="nsew")
                load_button = Button(sl_frame, text="Load", command=open_file)
                load_button.grid(column=1, row=3, rowspan=2, ipadx=30, ipady=10, padx=(20,0), pady=(10,0), sticky="nsew")

                # Top menu bar
                menubar= Menu(self)

                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Open", command=open_file)
                filemenu.add_command(label="Save", command=save_file)
                filemenu.add_command(label="Exit", command=self.destroy)
                menubar.add_cascade(label="File", menu=filemenu)

                # Configuration menu
                # Open config menu
                def open_config():
                        config_app.deiconify() # Unhides the configuration window

                optionmenu = Menu(menubar, tearoff=0)
                optionmenu.add_command(label="Configurations", command=open_config)
                menubar.add_cascade(label="Options", menu=optionmenu)

                def open_manual():
                        os.system("start \"\"https://github.com/totenk0pf/ordering-software-3000/tree/treeview-manual") # Opens manual with the default browser

                # About window
                def about_display():
                        self.about = Toplevel(self)
                        self.about.title('About')
                        self.about.resizable(False, False)
                        self.about_title = Label(self.about, text="About")
                        self.about_title.grid(column=1, row=1, padx=(20), pady=(20,5))
                        self.about_text = Message(self.about, text="Written in Python 3 (barely over 600 lines), this program has been created in order to get 12 credits. Visit the GitHub repo for more information.", justify=CENTER)
                        self.about_text.grid(column=1, row=3, padx=(20), pady=(0,20))
                        self.about.lift()
                        
                helpmenu = Menu(menubar, tearoff=0)
                helpmenu.add_command(label="Manual", command=open_manual)
                helpmenu.add_command(label="About", command=about_display)
                menubar.add_cascade(label="Help", menu=helpmenu)

                self.master.config(menu=menubar) # Sets the menubar widget as top menu for the program

                def confirm_entry():
                        confirm_prompt = messagebox.askyesno("Confirm", "Do you wish to confirm the order?") # Displays a confirmation dialogue
                        if confirm_prompt == True:
                                if len(self.first_name_input.get()) == 0 or len(self.last_name_input.get()) == 0 or len(self.phone_input.get()) == 0 or (len(val.address.get()) == 0 and val.dp_check.get() == 1):
                                        messagebox.showerror("Error", "Please input all of the customer's information.") # Shows an error message if one of the input fields are left empty
                                else:
                                        if val.total_amount == 0:
                                                messagebox.showerror("Error", "Please order at least one pizza!") # Shows an error message if no pizzas are ordered
                                        else:
                                                print_app.display_info() # Displays the receipt/print window

                # Options area
                option_frame = LabelFrame(self, text="Options")
                option_frame.grid(column=1, row=4, ipadx=0, ipady=10, padx=(20,20), pady=(0,20), sticky="ew")
                confirm_button = Button(option_frame, text="Confirm order", command=confirm_entry)
                confirm_button.grid(column=1, row=1, ipadx=15, ipady=20, padx=20, pady=(10,0), sticky="nesw")

                # Resets the entry fields and lists
                def reset_entry():
                        reset_prompt = messagebox.askyesno("Reset", "Are you sure you want to reset the customer's information?") # Displays a confirmation dialogue
                        if reset_prompt == True:
                                self.first_name_input.delete(0, 'end') # Empties the first name input field
                                self.last_name_input.delete(0, 'end') # Empties the last name input field
                                self.phone_input.delete(0, 'end') # Empties the phone input field
                                self.delivery_entry.delete(0, 'end') # Empties the address input field
                                for i in self.order_list.get_children(self.regular_pizza):
                                        self.order_list.delete(i) # Removes "i" items from the order list
                                        val.total_amount_regular = 0 # Sets the total amount of regular pizza to 0
                                for i in print_app.print_list.get_children(self.regular_pizza):
                                        print_app.print_list.delete(i)
                                for i in self.order_list.get_children(self.gourmet_pizza):
                                        self.order_list.delete(i) # Removes "i" items from the order list
                                        val.total_amount_gourmet = 0 # Sets the total amount of gourmet pizza to 0
                                for i in print_app.print_list.get_children(self.gourmet_pizza):
                                        print_app.print_list.delete(i) # Removes "i" items form the receipt/print list
                                del val.print_list_reg[:] # Empties the regular print list
                                del val.print_list_gour[:] # Empties the gourmet print list
                                val.total_amount = val.total_amount_regular + val.total_amount_gourmet # Calculates the total amount of pizzas
                        main_app.calc_total_cost() # Calculates the total cost
                        self.order_list.set(self.total_row, column="one", value=val.total_cost) # Sets the total cost display
                
                reset_button = Button(option_frame, text="Reset order", command=reset_entry)
                reset_button.grid(column=2, row=1, ipadx=20, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")
                config_button = Button(option_frame, text="Configurations", command=open_config)
                config_button.grid(column=3, row=1, ipadx=15, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")

                exit_button = Button(option_frame, text="Exit program", command=root.destroy)
                exit_button.grid(column=4, row=1, ipadx=15, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")

                try: # Opens the config.json file at launch
                        with open('config.json') as config:
                                loaded_config = json.load(config)
                                display_shop_name = loaded_config['shopname'] + "'s" + " " + "Pizza Shop"
                                head_label['text'] = display_shop_name
                                head_label['bg'] = loaded_config['headerbg']
                except: # Continue running if the file isn't found/returns an error
                        pass

def Pass(self):
        pass

class print_window(Toplevel):
        def __init__(self, master=None):
                Toplevel.__init__(self, master)
                self.title("Your order")
                self.resizable(False, False)
                self.iconbitmap('favicon.ico')
                self.protocol("WM_DELETE_WINDOW", Pass)
                self.attributes("-topmost", True)
                self.widget()
                self.withdraw()

        def widget(self, *args):
                self.customer_frame_print = LabelFrame(self, text="Customer's details")
                self.customer_frame_print.grid(column=1, row=1, ipadx=10, ipady=10, padx=(20), pady=(10,5), sticky="ew")

                # Print the customer's details
                self.name_label = Label(self.customer_frame_print, text="Customer's name:")
                self.name_label.grid(column=1, row=1, padx=(20,10), pady=(15,5))
                self.customername = Label(self.customer_frame_print, textvariable=val.customer_name)
                self.customername.grid(column=2, row=1, padx=(10), pady=(15,5))
                self.phone_label = Label(self.customer_frame_print, text="Phone number:")
                self.phone_label.grid(column=1, row=2, padx=(20,10), pady=5, sticky="ew")
                self.phone_number_label = Label(self.customer_frame_print, textvariable=val.phone_number)
                self.phone_number_label.grid(column=2, row=2, padx=(10), pady=(5))
                self.dp_label = Label(self.customer_frame_print, text="Delivery/Pickup:")
                self.dp_label.grid(column=1, row=3, padx=(20,10), pady=5)
                self.print_delivery_address = Label(self.customer_frame_print, text="Customer's address:")
                self.print_delivery_address.grid(column=1, row=4, padx=(20,10), pady=5, sticky="ew")
                self.address_label = Label(self.customer_frame_print, textvariable=val.print_address)
                self.address_label.grid(column=2, row=4, padx=(10), pady=5, sticky="ew")
                self.delivery_option = Label(self.customer_frame_print, textvariable=val.dp_option)
                self.delivery_option.grid(column=2, row=3, padx=(10), pady=(5))
                
                # Pizza list's frame
                self.pizza_frame = LabelFrame(self, text="Order")
                self.pizza_frame.grid(column=1, row=4, ipadx=10, ipady=10, padx=(20,20), pady=(0,5), sticky="ew")

                self.print_list = ttk.Treeview(self.pizza_frame, height=14, selectmode="none")
                self.print_list["columns"]=("one")
                self.print_list.column("#0", width=150, minwidth=150, stretch=NO)
                self.print_list.column("one", width=50, minwidth=50, stretch=NO)
                self.print_list.heading("#0", text="Name", anchor="w")
                self.print_list.heading("one", text="Amount", anchor="w")
                self.print_list.grid(column=1, row=5, padx=(20,0), pady=(10,0), sticky="ew")
                self.regular_print = self.print_list.insert("", 1, "RGP", text="Regular Pizzas")
                self.print_list.item(self.regular_print, open=True)
                self.gourmet_print = self.print_list.insert("", 2, "GP", text="Gourmet Pizzas")
                self.print_list.item(self.gourmet_print, open=True)
                self.total_row = self.print_list.insert("", 3, "TT", text="Total cost:", values=val.total_cost)

                # Option buttons
                self.button_frame = Frame(self)
                self.button_frame.grid(column=1, row=5, padx=(20), pady=(0,20))

                self.confirm_button = Button(self.button_frame, text="Confirm order", command=self.confirm_order)
                self.confirm_button.grid(column=1, row=1, ipadx=20, ipady=20, padx=(0,20), pady=(10,0), sticky="nesw")
                self.cancel_button = Button(self.button_frame, text="Cancel order", command=self.cancel_order)
                self.cancel_button.grid(column=2, row=1, ipadx=20, ipady=20, padx=(0), pady=(10,0), sticky="nesw")

        # Displays the customer's information
        def display_info(self):
                print_app.deiconify()
                print_app.grab_set()

                val.customer_name.set(main_app.first_name_input.get() + " " + main_app.last_name_input.get())
                val.phone_number.set(main_app.phone_input.get())
                val.print_address.set(main_app.delivery_entry.get())

                if val.dp_check.get() == 1:
                        val.dp_option.set("Delivery")
                        print_app.print_delivery_address.grid()
                        print_app.address_label.grid()
                elif val.dp_check.get() == 0:
                        val.dp_option.set("Pickup")
                        print_app.print_delivery_address.grid_remove()
                        print_app.address_label.grid_remove()
                for item in val.print_list_reg:
                        print_app.print_list.insert(print_app.regular_print, "end", val.dynamic_iid, text=item, values=1)
                        val.dynamic_iid += 1
                for item in val.print_list_gour:
                        print_app.print_list.insert(print_app.gourmet_print, "end", val.dynamic_iid, text=item, values=1)
                        val.dynamic_iid += 1
                print_app.print_list.set(print_app.total_row, column="one", value=val.total_cost)

        # Finalizes and actually confirms the order.
        def confirm_order(self):
                main_app.first_name_input.delete(0, 'end')
                main_app.last_name_input.delete(0, 'end')
                main_app.phone_input.delete(0, 'end')
                main_app.delivery_entry.delete(0, 'end')
                for i in main_app.order_list.get_children(main_app.regular_pizza):
                        main_app.order_list.delete(i)
                        val.total_amount_regular = 0
                for i in self.print_list.get_children(main_app.regular_pizza):
                        self.print_list.delete(i)
                for i in main_app.order_list.get_children(main_app.gourmet_pizza):
                        main_app.order_list.delete(i)
                        val.total_amount_gourmet = 0
                for i in self.print_list.get_children(main_app.gourmet_pizza):
                        self.print_list.delete(i)
                del val.print_list_reg[:]
                del val.print_list_gour[:]
                val.total_amount = val.total_amount_regular + val.total_amount_gourmet
                main_app.calc_total_cost()
                main_app.order_list.set(self.total_row, column="one", value=val.total_cost)
                messagebox.showinfo("Confirmed", "Your order has been confirmed.")
                self.withdraw()
                self.grab_release()

        # Cancels the order
        def cancel_order(self):
                messagebox.showinfo("Canceled", "Your order has been canceled.")
                print_app.withdraw()
                for i in self.print_list.get_children(main_app.regular_pizza):
                        self.print_list.delete(i)
                for i in self.print_list.get_children(main_app.gourmet_pizza):
                        self.print_list.delete(i)
                print_app.grab_release()

class configuration_window(Toplevel):
        def __init__(self, master=None):
                Toplevel.__init__(self, master)
                self.title("Configurations")
                self.attributes("-topmost", True)
                self.resizable(False, False)
                self.iconbitmap('favicon.ico')
                self.protocol("WM_DELETE_WINDOW", Pass)
                self.widget()
                self.withdraw()

        def widget(self, *args):
                self.shop_name_label = Label(self, text="Shop's name:")
                self.shop_name_label.grid(column=1, row=1, padx=(20), pady=(20,5), sticky="ew")
                self.shop_name_entry = Entry(self)
                self.shop_name_entry.grid(column=2, row=1, padx=(0,20), pady=(20,5), sticky="ew")
                
                def change_color():
                        header_color = askcolor()
                        main_app.head_label['bg'] = header_color[1]

                self.color_button = Button(self, text="Change header color", command=change_color)
                self.color_button.grid(column=1, columnspan=2, row=2, padx=(20), pady=(5,5), sticky="ew")

                self.confirm_config_button = Button(self, text="Save", command=self.init_config)
                self.confirm_config_button.grid(column=1, row=3, ipadx=40, padx=(20,5), pady=(5,20), sticky="ew")
                self.cancel_config_button = Button(self, text="Cancel", command=self.withdraw)
                self.cancel_config_button.grid(column=2, row=3, padx=(5,20), pady=(5,20), sticky="ew")

        def init_config(self):
                shopname = config_app.shop_name_entry.get()
                if not shopname == "":
                        display_shop_name = shopname + "'s" + " " + "Pizza Shop"
                        main_app.head_label['text'] = display_shop_name
                        config_app.withdraw()
                else:
                        messagebox.showerror("Error", "Please input all of the informations.")
                config_dict = {
                "shopname": shopname,
                "headerbg": main_app.head_label['bg']
                }
                with open('config.json', 'w') as writeconfig:
                        json.dump(config_dict, writeconfig)
                print(config_dict)

root = Tk()

# Declaring variables in another class so when the GUI initializes it doesn't throw 3000 errors about "_root" at me
class var():
        def __init__(self):
                self.customer_name = StringVar()
                self.phone_number = StringVar()
                self.print_address = StringVar()
                self.dp_option = StringVar()

                self.dp_check = IntVar()
                self.dp_check.set(0)

                # List of pizzas
                self.init_reg_dict = [("Hawaiian Pizza", 8.50),("Steak & Bacon Pizza", 8.50),("Pepperoni Pizza", 8.50),("Cheese Pizza", 8.50),("Beef & Onion Pizza", 8.50),("Veggie Pizza", 8.50),("New Yorker Pizza", 8.50)]
                self.init_gour_dict = [("Ramadan Halal Pizza", 13.50), ("Pineapple Only Pizza", 13.50), ("Crust Only Pizza", 13.50), ("Pizza that's been in a tomb for 1000 years", 13.50), ("Rice Pizza", 13.50)]

                self.firstname = StringVar()
                self.lastname = StringVar()
                self.phonein1 = StringVar()
                self.address = StringVar()

                self.total_cost = 0

                self.total_amount = 0
                self.total_amount_regular = 0
                self.total_amount_gourmet = 0

                self.print_list_reg = []
                self.print_list_gour = []

                self.dynamic_iid = 0

val = var()

main_app = main_window(root)
print_app = print_window(root)
print_app.lift()

config_app = configuration_window(root)

root.mainloop()
