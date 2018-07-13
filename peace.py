from tkinter import Tk, Label, PhotoImage

raiz= Tk()

photo= PhotoImage(file='peace.gif')

peace_label= Label(master=raiz,image=photo,width=600,height=600)

peace_label.pack()
raiz.mainloop()
