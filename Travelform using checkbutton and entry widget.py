from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Yatra")


#creating a function getvals to store value assing by user.

def getvals():
    print("submitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")

#heading
Label(root, text="Welcome to Lalit Travels",bg="Orange", font="Aerial 16 bold",pady=50,padx=10).grid(row=0,column=3)

# text for our form
name = Label(root, text ="Name",pady=10,justify= "center",font=("bold",12))
phone = Label(root, text ="Phone",pady=10,font=("bold",12))
gender = Label(root, text ="Gender",pady=10,font=("bold",12))
emergency= Label(root, text ="Emergency Contact",pady=10,font=("bold",12))
paymentmode = Label(root, text ="Payment Mode",pady=10,font=("bold",12))

#pack text for our form
name.grid(row= 1,column=2)
phone.grid(row= 2,column=2)
gender.grid(row= 3,column=2)
emergency.grid(row= 4,column=2)
paymentmode.grid(row=5 ,column=2)

# Tkinter variable for storing entry
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our formndigo")
nameentry= Entry(root, textvariable= namevalue,bg="White", font="Aerial 13 bold")
phoneentry = Entry(root, textvariable= phonevalue,bg="White", font="Aerial 13 bold")
genderentry = Entry(root, textvariable= gendervalue,bg="White", font="Aerial 13 bold")
emergencyentry = Entry(root, textvariable= emergencyvalue,bg="White", font="Aerial 13 bold")
paymentmodeentry = Entry(root, textvariable= paymentmodevalue,bg="white", font="Aerial 13 bold")

# packing form for our entry
nameentry.grid(row= 1, column=3)
phoneentry.grid(row= 2, column=3)
genderentry.grid(row= 3, column=3)
emergencyentry.grid(row= 4, column=3)
paymentmodeentry.grid(row= 5, column=3)


#checkbox and packing it

foodservice= Checkbutton(text="Want to prebook your meal?", variable= foodservicevalue,background="red", font="Aerial 13 bold")
foodservice.grid(row=6, column=3)

# button and Packing it and assinging it a command

Button(text="Submit to Lalit Travels",bg="gold",  font="Aerial 13 bold", command=getvals).grid(row=7,column=3)

root.mainloop()
