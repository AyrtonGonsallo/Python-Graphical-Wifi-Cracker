import tkinter as tk
from threading import Thread
from time import sleep
from tkinter import ttk
from GetWifiData import getData
from passwordGenerator import Generate
from WiFiCracker import getHosts, startHack
from Singleton import MyClass

LARGEFONT = ("Verdana", 35)
c = MyClass()


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconbitmap("Files/icone.ico")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.title("Gonsallo Ayrton´s Python Wifi Cracker")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menu_bar = tk.Menu(self)
        menu_file = tk.Menu(menu_bar, tearoff=0)

        def showA():
            self.show_frame(Accueil)

        def showP1():
            self.show_frame(Page1)

        def showP2():
            self.show_frame(Page2)

        def showP3():
            self.show_frame(Page3)

        menu_file.add_command(label="Accueil",
                              command=showA)
        menu_file.add_command(label="Mots de passes des réseaux connus",
                              command=showP1)
        menu_file.add_command(label="Générer des mots de passe", command=showP2)
        menu_file.add_command(label="Craquer des Wifi", command=showP3)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Changer de page", menu=menu_file)
        self.config(menu=menu_bar)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Accueil, Page1, Page2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # Accueil, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Accueil)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame Accueil

class Accueil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Accueil", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

    # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Mots de passes des réseaux connus", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # code ------------------------------------
        # Create the text widget
        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=2, padx=10, pady=10)
        text_widget = tk.Text(frame1, height=10, width=100)
        scroll_bar = tk.Scrollbar(frame1)

        long_text = """ici seront affichés les résultats
        """

        text_widget.pack(side="left", )
        scroll_bar.pack(side="right", fill="y")
        # Insert text into the text widget
        text_widget.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text_widget.yview)
        text_widget.insert(tk.END, long_text)

        def Effacer():
            text_widget.delete("1.0", "end")

        def GetWifiInfos():
            text_widget.delete("1.0", "end")
            text_widget.insert(tk.END, getData())

        button4 = ttk.Button(self, text="Afficher",
                             command=GetWifiInfos)
        button4.grid(row=0, column=3, padx=10, pady=10)
        button5 = ttk.Button(self, text="Effacer",
                             command=Effacer)
        button5.grid(row=1, column=3, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    selection = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Génerér MDP", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        ##code -----------------

        tk.Label(self, text="Longueur du mot de passe").grid(row=1, column=2)
        tk.Label(self, text="maximum de mots de passe").grid(row=2, column=2)
        tk.Label(self, text="type de combinaisons").grid(row=3, column=2)

        def sel():
            self.selection = str(var.get())

        var = tk.IntVar()
        R1 = tk.Radiobutton(self, text="1) Combinaison Alphanumerique", variable=var, value=1, command=sel)
        R2 = tk.Radiobutton(self, text="2) Combinaisons Numériques seules", variable=var, value=2, command=sel)
        R3 = tk.Radiobutton(self, text="3) Combinaisons de Caractère seules", variable=var, value=3, command=sel)
        R4 = tk.Radiobutton(self, text="4) Combinaisons Caractères speciaux seules", variable=var, value=4, command=sel)
        R5 = tk.Radiobutton(self, text="5) Combinaisons Caractère speciaux & nombres seules", variable=var, value=5,
                            command=sel)
        R6 = tk.Radiobutton(self, text="6) Combinaisions Alphanumeriques et Caracters speciaux", variable=var, value=6,
                            command=sel)
        R7 = tk.Radiobutton(self, text="7) Combinaisons speciales", variable=var, value=7, command=sel)
        R1.grid(row=4, column=3)
        R2.grid(row=5, column=3)
        R3.grid(row=6, column=3)
        R4.grid(row=7, column=3)
        R5.grid(row=8, column=3)
        R6.grid(row=9, column=3)
        R7.grid(row=10, column=3)
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e1.grid(row=1, column=3)
        e2.grid(row=2, column=3)
        tk.Label(self, text="Si 7) Entrez la Combinaison").grid(row=11, column=3)
        e3 = tk.Entry(self)
        e3.grid(row=11, column=4)

        def genererMDP():
            if self.selection == "7":
                Generate(self.selection, e1.get(), e2.get(), e3.get())
            else:
                Generate(self.selection, e1.get(), e2.get(), "")

        button4 = ttk.Button(self, text="Générer",
                             command=genererMDP)
        button4.grid(row=12, column=3, padx=10, pady=10)


class Page3(tk.Frame):
    hosts = []
    res = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Craquer des Wifi", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # code ------------------------------------
        # Create the text widget
        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=2, padx=10, pady=10)
        text_widget = tk.Text(frame1, height=10, width=100)
        scroll_bar = tk.Scrollbar(frame1)

        long_text = """ici seront affichés les résultats
                """

        text_widget.pack(side="left", )
        scroll_bar.pack(side="right", fill="y")
        # Insert text into the text widget
        text_widget.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text_widget.yview)
        text_widget.insert(tk.END, long_text)

        def attack():
            startHack(e3.get(), self.hosts)

        def Attaquer():
            text_widget.insert(tk.END, "Attaque en cours...")
            thread1 = Thread(target=attack)
            thread1.start()
            thread2 = Thread(target=display)
            thread2.start()

        def display():
            while not c.getIsOver():
                res2 = c.getResults()
                text_widget.insert(tk.END, res2)
                c.setResults("")
                sleep(2)
            if c.getIsOver():
                res2 = c.getResults()
                text_widget.insert(tk.END, res2)
                c.setResults("")

        def Effacer():
            text_widget.delete("1.0", "end")

        def GetWifiInfos():
            text_widget.delete("1.0", "end")
            res = getHosts()
            self.hosts = res[0]
            self.res = res[1]
            text_widget.insert(tk.END, self.res)

        button4 = ttk.Button(self, text="Voir les réseaux",
                             command=GetWifiInfos)
        button4.grid(row=0, column=3, padx=10, pady=10)
        button5 = ttk.Button(self, text="Effacer",
                             command=Effacer)
        button5.grid(row=1, column=3, padx=10, pady=10)
        tk.Label(self, text="Réseau a attaquer").grid(row=2, column=3)
        e3 = tk.Entry(self)
        e3.grid(row=2, column=4)
        button6 = ttk.Button(self, text="Attaquer",
                             command=Attaquer)
        button6.grid(row=3, column=4, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
