import tkinter
import house

# Saisir dans l'entry data/house.csv
# Dans le label bleu self.labelVariable.set(...) afficher la moyenne

class simpleapp_tk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("data/house.csv")

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
        content = self.entryVariable.get()
        try:
            model = house.HouseCsv(content)
            model.load()
            min, max, avg = model.compute_loyers_per_m2()
            self.labelVariable.set( f"Min: {min:.0f}, max: {max:.0f}, avg: {avg:.1f}" )
        except:
            self.labelVariable.set("Erreur")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnPressEnter(self,event):
        content = self.entryVariable.get()
        model = house.HouseCsv(content)
        model.load()
        min, max, avg = model.compute_loyers_per_m2()
        self.labelVariable.set( f"Min: {min:.0f}, max: {max:.0f}, avg: {avg:.1f}" )
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()