from tkinter import *


root = Tk()
root.geometry("500x300")
root.title("Adding two numbers")


# labels
l1 = Label(root, text="Please enter the first number:")
l2 = Label(root, text="Please enter the second number:")
l3 = Label(root, text="Results")

# entry
e1 = Entry(root, width=30)
e2 = Entry(root, width=30)
e3 = Entry(root, width=30)


def adding_sum():
    entry1 = e1.get()
    entry2 = e2.get()
    first_entry = float(entry1)
    second_entry = float(entry2)
    sum = int(first_entry + second_entry)
    e3.delete(0,END)

    e3.insert(0, sum)


def clearing_all():
    e3.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)


def terminating():
    import sys
    sys.exit()


# buttons
b1 = Button(root, text="ADD", command=adding_sum)
b2 = Button(root, text="CLEAR", command=clearing_all)
b3 = Button(root, text="EXIT", command=terminating)


# label packs
l1.grid(column=0, row=0, padx=10, pady=10)
l2.grid(column=0, row=1, padx=10, pady=10)
l3.grid(column=0, row=2, padx=10, pady=10)

# entry packs
e1.grid(column=1, row=0, padx=10, pady=10)
e2.grid(column=1, row=1, padx=10, pady=10)
e3.grid(column=1, row=2, padx=10, pady=10)

# button packs
b1.place(x=20, y=200)
b2.place(x=150, y=200)
b3.place(x=300, y=200)
root.mainloop()
