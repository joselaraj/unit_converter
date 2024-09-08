#create a conversion application,
#this app will convert lbs to kilograms
#the formula for this is 1 lb = 0.453592 Kg 

#import customtkinter to make it look nice 
import customtkinter
from tkinter import *

def convert():
    lbs  = float(lbs_entry.get())
    kilo =float(0.453592) 
    conversion = (lbs * kilo)

    conversion_rounded = round(conversion,2)
    #the reason for this is to display the conversion in the app 
    conv_label.configure(text=conversion_rounded)


def validation(): 
    pass 
#set the default color theme to dark blue and set the apperance mode to system 
customtkinter.set_appearance_mode('system') 
customtkinter.set_default_color_theme('green')

#create the window for the app and set the geometry to 500x350
root= customtkinter.CTk() 
root.geometry("500x350")
root.title("Conversion app")

#create a frame for the app 
head_frame = customtkinter.CTkFrame(master=root)
head_frame.pack(pady=40,padx=60)

#create a heading label 
head_label = customtkinter.CTkLabel(master=head_frame,text="Pound to Kilogram conversion",
                                    font=("Roboto",25))
head_label.pack()

#create another frame for user input and submission
entry_frame = customtkinter.CTkFrame(master=root)
entry_frame.pack(pady=12,padx=10)

#create a lbs entry 
lbs_entry= customtkinter.CTkEntry(master=entry_frame,placeholder_text="Enter LBS")
lbs_entry.pack(side=LEFT)

#create a button for the conversion 

btn = customtkinter.CTkButton(master=entry_frame,text="Convert",command=convert)
btn.pack(side=RIGHT,padx=5)

#create a bottom frame for to display the conversion, and also include a quit button for the user to quit the program 
bottom_frame = customtkinter.CTkFrame(master=root)
bottom_frame.pack() 

result = customtkinter.CTkLabel(master=bottom_frame,text="Converted to Kilograms:") 
result.pack(side=LEFT)

conv_label= customtkinter.CTkLabel(master=bottom_frame, text="")
conv_label.pack(side=RIGHT,padx=10) 

quit_frame = customtkinter.CTkFrame(master=root) 
quit_frame.pack(pady=12,padx=10) 

quit_button = customtkinter.CTkButton(master=quit_frame,text="Quit",command=root.destroy) 
quit_button.pack(pady=12,padx=10) 

#mainloop the app 
root.mainloop() 
