from tkinter import Tk, Label, Button


class RootWindow:

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        root = Tk()  # Création de la fenêtre racine
        root.title ="Chrismas Hazard"
        lbl_title = Label(root, text='Chrismas Hazard')

        btn_manuel = Button(root, text='Saisie Manuelle')
        btn_csv = Button(root, text='Par CSV')

        lbl_title.grid(column=2, row=0, pady="5" )
        btn_csv.grid(column=1, row=2, padx="10")
        btn_manuel.grid(column=3, row=2, padx="10")

        root.mainloop()  # Lancement de la boucle principale
