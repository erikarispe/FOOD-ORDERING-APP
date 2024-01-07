#THIS IS CODE FOR A MOCK FOOD ORDERING DELIVERY APP THAT USES PYTHON, TKINTER, AND PILLOW
#functionality of the app allows you to order food from different restaurants, add/remove items from the cart, and check out

#you will need to install tkinter as tk, import *, import message box
#you will need to install pillow which allows the ability to upload images
#from pil import ImageTk, Image

#you will need images in a folder for different restatuarants and food items

#you can only check out on the cart page
#you can view your user account on the home page
#you can remove items on the cart page and on the check out page
#you will only be able to place the order on the check out page

import tkinter as tk
from tk import *
from tkinter import messagebox
from PIL import ImageTk, Image

#function to show frame
def show_frame(frame):
    frame.tkraise()

#code for app
app = tk.Tk()

#declare cart total, and cart items list

cart_total = 0.00

cart_items = []

#FRAMES FOR DIFFERENT PAGES
home_page = tk.Frame(app,highlightbackground='red', highlightthickness=10, width=1000, height=550, bg='white')
taco_bell_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
burger_king_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
mcdonalds_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
delivery_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
check_out_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
user_account_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')
cart_page = tk.Frame(app,highlightbackground='red', highlightthickness=1, width=1000, height=550, bg='white')


#function to switch to home page
def go_to_home():
    show_frame(home_page)

#function to switch to checkout page when ready to place order
def go_to_checkout():
    show_frame(check_out_page)

#function for logo banner which will display on each page
def create_logo_banner(frame):
    logo_pil = Image.open('icons/applogo.png')
    resized_logo_pil = logo_pil.resize((50,50))
    food_order_logo = ImageTk.PhotoImage(resized_logo_pil)
    label = tk.Label(frame, image=food_order_logo, text="Food Order", compound="top", background="black")
    label.image = food_order_logo  # Maintain a reference to avoid garbage collection
    label.pack()


# Function to add item to cart
def add_to_cart(item_name, item_price):
    global cart_total, cart_items
    cart_total += item_price
    cart_items.append((item_name, item_price))
    update_cart_display()
    messagebox.showinfo("Item added to cart", f"{item_name} - ${item_price:.2f} added to cart\nCurrent Total: ${cart_total:.2f}")


#funciton for updating the cart items and totals
def update_cart_display():
    #this section of the function is for the cart page
    cart_total_label.config(text=f"Total: ${cart_total:.2f}")
    # Clear the frame and display updated cart items
    for widget in cart_frame.winfo_children():
        widget.destroy()

    for idx, item in enumerate(cart_items):
        item_label = tk.Label(cart_frame, text=f"{item[0]} - ${item[1]:.2f}")
        item_label.grid(row=idx, column=0)

        remove_button = tk.Button(cart_frame, text="Remove", command=lambda x=item: remove_from_cart(x[0], x[1]))
        remove_button.grid(row=idx, column=1)

    #this section of the function is for the check out page
    # Update check_out page labels
    check_out_cart_total_label.config(text=f"Total: ${cart_total:.2f}")
    # Clear the frame and display updated cart items
    for widget in check_out_cart_frame.winfo_children():
        widget.destroy()

    for idx, item in enumerate(cart_items):
        item_label = tk.Label(check_out_cart_frame, text=f"{item[0]} - ${item[1]:.2f}")
        item_label.grid(row=idx, column=0)

        remove_button = tk.Button(check_out_cart_frame, text="Remove", command=lambda x=item: remove_from_cart(x[0], x[1]))
        remove_button.grid(row=idx, column=1)

    #this section of the function is for the delivery page
    # Update the items on the delivery page 
    delivery_cart_total_label.config(text=f"Total: ${cart_total:.2f}")
    # Clear the frame and display updated cart items
    for widget in delivery_items_frame.winfo_children():
        widget.destroy()

    for idx, item in enumerate(cart_items):
        item_label = tk.Label(delivery_items_frame, text=f"{item[0]} - ${item[1]:.2f}")
        item_label.grid(row=idx, column=0)

# Function to remove item from cart
def remove_from_cart(item_name, item_price):
    global cart_total, cart_items
    for item in cart_items:
        if item[0] == item_name and item[1] == item_price:
            cart_items.remove(item)
            cart_total -= item_price
            break

    update_cart_display()

# function for adding an item to cart
def add_item_to_cart(item_name, item_price):
    add_to_cart(item_name, item_price)

# Function to remove item from cart
def remove_from_cart(item_name, item_price):
    global cart_total, cart_items
    for item in cart_items:
        if item[0] == item_name and item[1] == item_price:
            cart_items.remove(item)
            cart_total -= item_price
            break  # Remove only one item (if duplicates present), then break out of the loop
    update_cart_display()


#Funtion to place order, just takes the user to the delivery page
def place_order():
    show_frame(delivery_page)


#logo banners for each of the frames
create_logo_banner(home_page)
create_logo_banner(taco_bell_page)
create_logo_banner(burger_king_page)
create_logo_banner(mcdonalds_page)
create_logo_banner(delivery_page)
create_logo_banner(check_out_page)
create_logo_banner(user_account_page)
create_logo_banner(cart_page)




#grid for different frame pages
home_page.place(relheight=1, relwidth=1)
taco_bell_page.place(relheight=1, relwidth=1)
burger_king_page.place(relheight=1, relwidth=1)
mcdonalds_page.place(relheight=1, relwidth=1)
delivery_page.place(relheight=1, relwidth=1)
check_out_page.place(relheight=1, relwidth=1)
user_account_page.place(relheight=1, relwidth=1)
cart_page.place(relheight=1, relwidth=1)

###########################################
#Images for the different pages
#user account logo
original_usericon_image = Image.open('icons/usericon.png')
resized_usericon_image = original_usericon_image.resize((50,50))
user_icon_image = ImageTk.PhotoImage(resized_usericon_image)


#taco bell logo
original_taco_bell_logo_image = Image.open('icons/tacobelllogo.png')
resized_taco_bell_logo_image = original_taco_bell_logo_image.resize((50,50))
taco_bell_logo_image = ImageTk.PhotoImage(resized_taco_bell_logo_image)

#burger king logo

original_burger_king_logo_image = Image.open('icons/burgerkinglogo.png')
resized_burger_king_logo_image = original_burger_king_logo_image.resize((50,50))
burger_king_logo_image = ImageTk.PhotoImage(resized_burger_king_logo_image)

#mcdondalds logo
original_mcdonalds_logo_image = Image.open('icons/mcdonaldslogo.png')
resized_mcdonalds_logo_image = original_mcdonalds_logo_image.resize((50,50))
mcdonalds_logo_image = ImageTk.PhotoImage(resized_mcdonalds_logo_image)

#cart image
original_cart_image = Image.open('icons/cart.png')
resized_cart_image = original_cart_image.resize((50,50))
cart_image = ImageTk.PhotoImage(resized_cart_image)

#home image 

original_home_image = Image.open('icons/home_icon.png')
resized_home_image = original_home_image.resize((50,50))
home_image = ImageTk.PhotoImage(resized_home_image)

#burrito image
original_burrito_image = Image.open('icons/burrito.png')
resized_burrito_image = original_burrito_image.resize((50,50))
burrito_image = ImageTk.PhotoImage(resized_burrito_image)

#taco image
original_taco_image = Image.open('icons/taco.png')
resized_taco_image = original_taco_image.resize((50,50))
taco_image = ImageTk.PhotoImage(resized_taco_image)

#burger king fries image
original_fries_image = Image.open('icons/burgerkingfries.png')
resized_fries_image = original_fries_image.resize((50,50))
burger_king_fries_image = ImageTk.PhotoImage(resized_fries_image)

#burgerking burger image
original_burger_king_burger_image = Image.open('icons/burgerkingburger.png')
resized_burger_king_burger_image = original_burger_king_burger_image.resize((50,50))
burger_king_burger_image = ImageTk.PhotoImage(resized_burger_king_burger_image)

#mcdonalds fries image
original_mcdonalds_fries_image = Image.open('icons/mcdonaldsfries.png')
resized_mcdonalds_fries_image = original_mcdonalds_fries_image.resize((50,50))
mcdonalds_fries_image = ImageTk.PhotoImage(resized_mcdonalds_fries_image)

#mcdonalds burger image
original_mcdonalds_burger_image = Image.open('icons/mcdonaldsburger.png')
resized_mcdonalds_burger_image = original_mcdonalds_burger_image.resize((50,50))
mcdonalds_burger_image = ImageTk.PhotoImage(resized_mcdonalds_burger_image)

#order delivery image
original_delivery_image = Image.open('icons/orderdelivery.png')
resized_delivery_image = original_delivery_image.resize((125,125))
order_delivery_image = ImageTk.PhotoImage(resized_delivery_image)

###########################################################
#USER ACCOUNT PAGE CONTENT 

user_account_page_label = tk.Label(user_account_page, text='User Account')
user_account_page_label.pack(pady=20, fill='x')

user_name_label = tk.Label(user_account_page, text="User: Test User")
user_name_label.pack(pady=10)

user_email_label = tk.Label(user_account_page, text="Email: 0bYpD@example.com")
user_email_label.pack(pady=10)

user_address_label = tk.Label(user_account_page, text="Address: 123 Main St")
user_address_label.pack(pady=10)

user_language_label = tk.Label(user_account_page, text="Language: English")
user_language_label.pack(pady=10)

home_page_button_user_account = tk.Button(user_account_page,image=home_image, command=go_to_home)
home_page_button_user_account.pack(pady=20)


#########################################################
#Taco Bell Page Content
taco_bell_page_label = tk.Label(taco_bell_page, text='Taco Bell')
taco_bell_page_label.pack(pady=20, fill='x')

items_label = tk.Label(taco_bell_page, text='Items')
items_label.pack(pady=10)

taco_price = 3.00
taco_button = tk.Button(taco_bell_page, image=taco_image, text="Add Taco to Cart", command=lambda: add_item_to_cart("Taco Bell Taco", taco_price))
taco_button.pack(pady=10)

burrito_price = 3.00
burrito_button = tk.Button(taco_bell_page,image=burrito_image, text="Add Burrito to Cart", command=lambda: add_item_to_cart("Taco Bell Burrito", burrito_price))
burrito_button.pack(pady=10)

cart_taco_bell_page_button = tk.Button(taco_bell_page, image=cart_image, command=lambda : cart_page.tkraise())
cart_taco_bell_page_button.pack()

home_page_button_taco_bell = tk.Button(taco_bell_page,image=home_image, command=go_to_home)
home_page_button_taco_bell.pack()

#########################################################
#BURGER KING PAGE CONTENT

burger_king_page_label = tk.Label(burger_king_page, text='Burger King')
burger_king_page_label.pack(pady=20, fill='x')

items_label = tk.Label(burger_king_page, text='Items')
items_label.pack(pady=10)

burger_king_fries_price = 3.00
burger_king_fries_button = tk.Button(burger_king_page, image=burger_king_fries_image, text="Add Fries to Cart", command=lambda: add_item_to_cart("Burger King Fries", burger_king_fries_price))
burger_king_fries_button.pack(pady=10)

burger_king_burger_price = 3.00
burger_king_burger_button = tk.Button(burger_king_page, image=burger_king_burger_image, text="Add Burger to Cart", command=lambda: add_item_to_cart("Burger King Burger", burger_king_burger_price))
burger_king_burger_button.pack(pady=10)

cart_burger_king_page_button = tk.Button(burger_king_page,image=cart_image, command=lambda : cart_page.tkraise())
cart_burger_king_page_button.pack()

home_page_button_burger_king = tk.Button(burger_king_page, image=home_image, command=go_to_home)
home_page_button_burger_king.pack()

#########################################################
#########################################################
#MCDONALD'S PAGE CONTENT
mcdonalds_page_label = tk.Label(mcdonalds_page, text='McDonalds ')
mcdonalds_page_label.pack(pady=20, fill='x')

items_label = tk.Label(mcdonalds_page, text='Items')
items_label.pack(pady=10)

mcdonalds_burger_price = 3.00
mcdonalds_burger_button = tk.Button(mcdonalds_page, image=mcdonalds_burger_image, text="Add Burger to Cart", command=lambda: add_item_to_cart("Mcdonalds Burger", mcdonalds_burger_price))
mcdonalds_burger_button.pack(pady=10)

mcdonalds_fries_price = 3.00
mcdonalds_fries_button = tk.Button(mcdonalds_page, image=mcdonalds_fries_image, text="Add Fries to Cart", command=lambda: add_item_to_cart("McDonalds Fries", mcdonalds_fries_price))
mcdonalds_fries_button.pack(pady=10)

cart_mcdonalds_page_button = tk.Button(mcdonalds_page, image=cart_image, command=lambda : cart_page.tkraise())
cart_mcdonalds_page_button.pack()

home_page_button_mcdonalds = tk.Button(mcdonalds_page, image=home_image, command=go_to_home)
home_page_button_mcdonalds.pack()

#########################################################
#########################################################
#CART PAGE CONTENT
cart_page_label = tk.Label(cart_page, text='Cart ')
cart_page_label.pack(pady=20, fill='x')

cart_frame = tk.Frame(cart_page)
cart_frame.pack()

cart_total_label = tk.Label(cart_page, text='Total: $0.00')
cart_total_label.pack(pady=10)

check_out_cart_page_button = tk.Button(cart_page, text='Check Out', command=lambda: check_out_page.tkraise())
check_out_cart_page_button.pack(pady=20)

home_page_button_cart_page = tk.Button(cart_page, image=home_image, command=go_to_home)
home_page_button_cart_page.pack()



#########################################################
#########################################################
#########################################################
#CHECK OUT PAGE CONTENT


check_out_page_label = tk.Label(check_out_page, text='Check Out ')
check_out_page_label.pack(pady=20, fill='x')

check_out_cart_frame = tk.Frame(check_out_page)
check_out_cart_frame.pack()

check_out_cart_total_label = tk.Label(check_out_page, text='Total: $0.00')
check_out_cart_total_label.pack(pady=10)

check_out_page_place_order_button = tk.Button(check_out_page, text='Place Order', command=place_order)
check_out_page_place_order_button.pack(pady=10)

cart_check_out_page_button = tk.Button(check_out_page, image=cart_image, command=lambda : cart_page.tkraise())
cart_check_out_page_button.pack(pady=10)

home_page_button_check_out_page = tk.Button(check_out_page, image=home_image, command=go_to_home)
home_page_button_check_out_page.pack(pady=10)


#################################################
#DELIVERY PAGE CONTENT
delivery_page_label = tk.Label(delivery_page, text='Delivery ')
delivery_page_label.pack(pady=20, fill='x')

receipt_label = tk.Label(delivery_page, text='Receipt')
receipt_label.pack(pady=10)

delivery_cart_items_label = tk.Label(delivery_page, text='Items Ordered:')
delivery_cart_items_label.pack()

delivery_items_frame = tk.Frame(delivery_page)
delivery_items_frame.pack()

delivery_cart_total_label = tk.Label(delivery_page, text='Total: $0.00')
delivery_cart_total_label.pack(pady=10)

home_page_button_delivery_page = tk.Button(delivery_page, image=home_image, command=go_to_home)
home_page_button_delivery_page.pack(pady=10)




#################################################
#########################################
#BUTTONS ON THE HOME PAGE 
#takes you to the user account page
user_account_home_button = tk.Button(home_page,image=user_icon_image, width=70, height=70 , command=lambda : user_account_page.tkraise())
user_account_home_button.place(x=40, y=75)
#takes you to the cart page
cart_home_button = tk.Button(home_page, width=70, height=70, image=cart_image,command=lambda : cart_page.tkraise())
cart_home_button. place(x=850, y=75)
#takes you to the taco bell page
taco_bell_home_button = tk.Button(home_page,image=taco_bell_logo_image,width=70, height=70,command=lambda: taco_bell_page.tkraise())
taco_bell_home_button.pack(padx=10, pady=10)
#takes you to the burger king page
burger_king_home_button = tk.Button(home_page,width=70, height=70, image=burger_king_logo_image, command=lambda : burger_king_page.tkraise())
burger_king_home_button.pack(padx=10, pady=10)
# takes you to the MCDONALD'S PAGE
mcdonalds_home_button = tk.Button(home_page, width=70, height= 70, image=mcdonalds_logo_image, command=lambda : mcdonalds_page.tkraise())
mcdonalds_home_button.pack(padx=10, pady=10)



#this will show the home page when you start the app
home_page.tkraise()
#code for app
app.geometry('1000x500')
app.title('Food Order App')
app.resizable(False, False)
#this will be able to run the application
app.mainloop()
