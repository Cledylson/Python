from tkinter import *
from tkinter import messagebox
from random import randint, choice

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk() 
        self.botao_ran = Button(self.janela_principal, text='Mega Senna Aleatória', command=self.mega_sena_ran)
        self.botao_cho = Button(self.janela_principal, text='Mega Senna escolha', command=self.mega_sena_cho)
        self.botao_duo = Button(self.janela_principal, text='Mega Senna as DUAS', command=self.mega_duo)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit)
        self.botao_ran["width"] = 30
        self.botao_cho["width"] = 30
        self.botao_duo["width"] = 30
        self.botao_sair["width"] = 10
        self.botao_ran.pack()
        self.botao_cho.pack()
        self.botao_duo.pack()
        self.botao_sair.pack()
        mainloop()
    

    def mega_duo(self):
        self.mega_sena_cho()
        self.mega_sena_ran()
          

    def mega_sena_ran(self):
        a = randint(1, 60)
        b = randint(1, 60)
        c = randint(1, 60)
        d = randint(1, 60)
        e = randint(1, 60)
        f = randint(1, 60)
        if a == b or a == c or a == d or a == e or a == f or b == c \
            or b == d or b == e or b == f or c == d or c == e \
                or d == e or d == f or e == f:
                return self.mega_sena_ran()
        else:
            messagebox.showinfo("O resultado é ", \
            f"{a} {b} {c} {d} {e} {f}")


    def mega_sena_cho(self):
        x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
        a = choice(x)
        b = choice(x)
        c = choice(x)
        d = choice(x)
        e = choice(x)
        f = choice(x)
        if a == b or a == c or a == d or a == e or a == f or b == c \
            or b == d or b == e or b == f or c == d or c == e \
                or d == e or d == f or e == f:
                return self.mega_sena_cho()
        else:
            messagebox.showinfo("O resultado é ", \
            f"{a} {b} {c} {d} {e} {f} ")
   

gui = MinhaGUI()
