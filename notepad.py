#!/usr/bin/env python
from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, tk.END+"-1c")


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, tk.END+"-1c")
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    file_ = filedialog.asksaveasfile(mode="w")
    if file_:
        content = TextArea.get("1.0", tk.END+"-1c") # do we need "-1c" ???
        file_.write(content)
        file_.close()

# def saveFile():
#     global file
#     if file == None:
#         file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
#                            filetypes=[("All Files", "*.*"),
#                                      ("Text Documents", "*.txt")])
#         if file =="":
#             file = None
#
#         else:
#             #Save as a new file
#             file = open(file, "w")
#             file.write(TextArea.get(1.0, tk.END+"-1c"))
#             file.close()
#
#             root.title(os.path.basename(file) + " - Notepad")
#             print("File Saved")
#     else:
#         # Save the file
#         file = open(file, "w")
#         file.write(TextArea.get(1.0, tk.END+"-1c"))
#         file.close()
#

def contact():

    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. you can see the sourcecode on my github"
    else:
        msg = "Tell us what went wrong. please report us by mail"
    tmsg.showinfo("Experience", msg)


def quitApp():

    value = tmsg.askquestion("Confirm Exit ?", "Are You sure you want to exit NotePad?")
    if value == "yes":
        root.destroy()
    else:
        pass
        #msg = "Tell us what went wrong. please report us by mail"
    #tmsg.showinfo("Experience", msg)



def cut():
    TextArea.event_generate(("<>"))

def copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("Notepad", "Made by tkinter GUI by Chiranjeev")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="Times 30")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    HelpMenu.add_command(label = "Contact and Support", command=contact)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
