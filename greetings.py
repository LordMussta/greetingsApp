import tkinter as tk
from tkinter import ttk

def EnterName():
    user_result.set("Hello " + user_name.get() + "!")
    print(f"Hello {user_name.get() or 'World'}!")
    if len(user_name.get()) == 0:
        pass
    else:
        namesList.append(user_name.get())
        print("passed else test")
    user_name.set("")
    display = ""
    for name in namesList:
        display += name + "\n"
    display_label.config(text=display)

root = tk.Tk()
root.geometry("400x400")
root.title("Greetings App")


user_name = tk.StringVar()
print(user_name)
user_result = tk.StringVar()
namesList = []

instructions_label = ttk.Label(root, text="Please enter a name to be greeted and added to the list. ", padding=(20))
instructions_label.pack(fill="y")

name_label = ttk.Label(root, text="Enter Name: ", padding=(30,10)).pack()
name_entry = ttk.Entry(root, textvariable=user_name).pack()

nameBtn = ttk.Button(root, text="Submit",  command=EnterName, padding=(30,10,30,10))
nameBtn.pack(fill="y")

quitBtn = ttk.Button(root, text="Quit", command=root.destroy, padding=(30,10))
quitBtn.pack(fill="y")

greeting = ttk.Label(root, textvariable=user_result, padding=(10))
greeting.pack(fill="y")

display_label = ttk.Label(root, text="", padding=(30,10))
display_label.pack(fill="y")

root.mainloop()
