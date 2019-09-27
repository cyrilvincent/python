import tkinter
import media

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.db = media.BookDb("data/books.db3")
        

    def initialize(self):

        self.grid()
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("")

        button = tkinter.Button(self,text="Search",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set("...")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClick(self):
        try:
            price = float(self.entryVariable.get())
            books = list(self.db.getByPrice(price))
            if len(books) == 0:
                self.labelVariable.set("No book")
            else:
                self.labelVariable.set(books[0].title)
            self.entry.focus_set()
            self.entry.selection_range(0, tkinter.END)
        except ValueError:
            self.labelVariable.set("Bad price")


    def OnPressEnter(self,event):
        self.labelVariable.set( "Hello " + self.entryVariable.get() + " (button)" )
        self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()