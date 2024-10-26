from tkinter import *
from tkinter import ttk, filedialog
from parser.parser import Jsparser

class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        def open_file_dialog():
            file_path = filedialog.askopenfilename(title="Open File", filetypes=[("All Files", "*.*")])
            if file_path:
                parser = Jsparser()
                parsed = parser.jsparse(file_path)
                ent1.delete(0,END)
                ent1.insert(0,parsed)

        def clicked():
            btn2.configure(text="OMG! YOU CLICKED ME!!! " + ent1.get())

        def openFile():
            ent1.delete(0,END)
            ent1.insert(0,"Open file?!")
            btn2.configure(text="Open a file you say?")

        # Frame 1 definition
        hierarchyFrame = Frame(parent, padx=10, pady = 10)
        hierarchyFrame.pack(side = LEFT, fill=BOTH)

        workFrame = Frame(parent, padx=10, pady=10, width=250, background="red")
        workFrame.pack(side = LEFT, expand=TRUE, fill=BOTH)

        # Menu
        menu = Menu(parent)
        item = Menu(menu, tearoff=False)
        item.add_command(label='New')
        item.add_command(label='Open', command=open_file_dialog)
        item.add_command(label='Close',command=parent.destroy)
        menu.add_cascade(label='File', menu=item)
        parent.config(menu=menu)

        # Hierarchy frame definition
        hierarchyLabel = Label(hierarchyFrame, text="Object Hierarchy")
        hierarchyLabel.pack()
        hierarchy = ttk.Treeview(hierarchyFrame)
        hierarchy.pack(fill=BOTH)
        btn1 = Button(hierarchyFrame, text="Quit", command=parent.destroy)
        btn1.pack(fill=X)

        #Workspace frame definition -- TODO create specific forms for all possible game object types
        btn2 = Button(workFrame,text="CLICK ME!!!",background="blue", command=clicked)
        btn2.pack(expand=TRUE)
        ent1 = Entry(workFrame)
        ent1.pack(expand = TRUE, fill=BOTH)
        
        # populate treeview test -- TODO replace with file read logic
        hierarchy.insert('','0','item1',text="Root")
        hierarchy.insert('item1','1','item2',text="Child1")
        hierarchy.insert('item1','2','item3',text="Child2")
        hierarchy.insert('item1','end','item4',text="Child3")

if __name__ == "__main__":
    root = Tk()
    # Window properties
    root.title("QuestJS Editor")
    root.geometry("500x500")
    MainApplication(root).pack(side="top", fill=BOTH, expand=True)
    root.mainloop()