import os
import Tkinter                                      # Tkinter wordt gebruikt voor de GUI (Graphical User Interface).
from Tkinter import *
from tkFileDialog import askopenfilename

class MainFrame:

    def __init__(self):
        #De volgende code maakt een venster met een grootte van 250x150. De naam van het venster is DataToGo.
        self.mf = Tk()
        self.mf.geometry("250x150")
        self.mf.title("DataToGo")

        # Met de volgende code wordt er een menu aan het venster toegevoegd. Het menu bevat een knop help, waar de UserGuide kan raadplegen.
        def UserGuide():                                                                # Een test om te zien of er een document wordt geopend. Ja dit gebeurt. Hier komt de gebruikershandleiding te staan.
            os.system('C:\Users\Alyssa\Desktop\IPFIT5_Usability_V1.2_Concept.pdf')

        menu = Menu (self.mf)
        self.mf.config(menu=menu)

        helpmenu = Menu (menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="User Guide", command=UserGuide)

        
        # Vervolgens worden er buttons aangemaakt voor het imagen, mounten, live search en keyword search.
        self.imageButton = Tkinter.Button(self.mf,
                                          text = "Create Image",
                                          width = 12,
                                          command = self.createImage) # Bij een klik op de knop wordt er een commando uitgevoerd. 
        self.imageButton.grid(row=1, column=0)

        self.mountButton = Tkinter.Button(self.mf,
                                          text = "Mount Image",
                                          width = 12,
                                          command = self.mountImage)
        self.mountButton.grid(row=2, column=0)

        self.liveSearchButton = Tkinter.Button(self.mf,
                                          text = "Live Search",
                                          width = 12,
                                          command = self.liveSearch)
        self.liveSearchButton.grid(row=3, column=0)

        self.keywordSearchButton = Tkinter.Button(self.mf,
                                          text = "Keyword Search",
                                          width = 12,
                                          command = self.keywordSearch) 
        self.keywordSearchButton.grid(row=4, column=0)
        
        self.mf.mainloop()

    def callback(self):
        print "called the callback!"

    # Met de commando wordt er een functie (def) uitgevoerd. 
    def createImage(self):

        win = Toplevel()
        win.title("Create Image")
        Label(win, width=50, height=1).pack(side='bottom')
        label1 = Label(win, text='     Please Select the Source Evidence Type').pack(side=TOP)
        checkbutton1 = Checkbutton(win, text="Physical Drive         ")
        checkbutton2 = Checkbutton(win, text="Logical Drive          ")
        
        checkbutton1.pack()
        checkbutton2.pack()
        
        label2 = Label(win, text = '___________________________________________________________________').pack(side='top')

        cancelbutton = Button(win, text='Cancel', width=7, command=win.destroy).pack(side=RIGHT)
        nextbutton = Button(win, text='Next>', width=7).pack(side=RIGHT)
        

    def mountImage(self):

        def load_file():
            fname = askopenfilename(filetypes=(("EWF files", "*.E01"),
                                               ("All files", "*.*") ))
            if fname:
                try:
                    print fname
                   # print("""here it comes: self.settings["template"].set(fname)""")
                except:                     # <- naked except is a bad idea
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                return
            
        win = Toplevel()
        win.title("Mount Image")
        Label(win, width=30, height=1).pack(side='bottom')
    
        label1 = Label(win, text='Add Image             ').pack(side='top')
        text1 = Text(win, width = 20, height = 1, wrap = WORD)                                    
        text1.pack(side='left')

        browseButton = Button(win, text='Browse...', width=8, command=load_file).pack(side='left')
        
        
        label2 = Label(win, text=' ',pady=50).pack()
        button2 = Button(win, text='Mount', width=8).pack(side=RIGHT)
        button3 = Button(win, text='Cancel', width=8, command=win.destroy).pack(side=RIGHT)
       
            
    def liveSearch(self):
        win = Toplevel()
        message = ""
        Label(win, width=100, height=30).pack()
        

    def keywordSearch(self):
        win = Toplevel()
        message = ""
        Label(win, width=100, height=30).pack()
     
        
if __name__ == "__main__":
    app = MainFrame()


self.mf.mainloop()
