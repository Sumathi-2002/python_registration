from tkinter import *
root = Tk()
root.geometry("500x300")


root.eval('tk::PlaceWindow . center')


def getvals():
    print("Registration Successsfully")
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0,column=3)


name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
mail_id = Label(root, text="Mail Id")


name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
mail_id.grid(row=4, column=2)


namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
mail_idvalue = StringVar
checkvalue = IntVar


nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
mail_identry = Entry(root, textvariable =mail_idvalue)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
mail_identry.grid(row=4, column=3)


checkbtn = Checkbutton(text="Remember Me?", variable = checkvalue)
checkbtn.grid(row=6,column=3)


Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()