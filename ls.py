import os, subprocess
from tkinter import *
def listFiles(pathName):
    mywin = Tk()
    mywin.geometry("400x400")
    proc = subprocess.Popen(["ls", pathName], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err == None:
        fileList = out.decode()
        fileList = fileList.split('\n')
        scrollView = Scrollbar(mywin)
        scrollView.pack(fill="y", side=RIGHT) 
        myList = Listbox(mywin, yscrollcommand=scrollView.set)
        for line in fileList:
            myList.insert(END, line)
        myList.pack()
        scrollView.config(command=myList.yview)
    mywin.mainloop()
def pathEnterDialogBox():
    pathAuthBox = Tk()
    path = StringVar()
    errorMsg = StringVar()
    def mainFunction():
        if path.get():
            parentDir = path.get()
            if os.path.isdir(parentDir):
                listFiles(parentDir)
            else:
                if os.path.isfile(parentDir):
                    errorMsg="Sorry but the path is a file not a directory! try again!"
                else:
                    errorMsg=" Sorry but the path is nither a directory nor a file! try again!"
        else:
            errorMsg="Please provide a path for the action!"
    pathAuthBox.geometry("500x600")
    inputLable = Label(pathAuthBox, text="Enter the path below:").pack(padx=10, pady=[50, 5],side=TOP, anchor="nw")
    pathInput = Entry(pathAuthBox, textvariable=path, font='arial 13 bold').pack(fill=X, padx=10)
    errorMessage = Label(pathAuthBox, textvariable=errorMsg).pack()
    submitButton = Button(pathAuthBox, text="Submit", command=mainFunction).pack()
    pathAuthBox.mainloop()
pathEnterDialogBox()