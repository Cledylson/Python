import tkinter as tk

class Calculadora:

    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Botões numéricos
        self.btn7 = self.create_button(7, 1, 1)
        self.btn8 = self.create_button(8, 1, 2)
        self.btn9 = self.create_button(9, 1, 3)
        self.btn4 = self.create_button(4, 2, 1)
        self.btn5 = self.create_button(5, 2, 2)
        self.btn6 = self.create_button(6, 2, 3)
        self.btn1 = self.create_button(1, 3, 1)
        self.btn2 = self.create_button(2, 3, 2)
        self.btn3 = self.create_button(3, 3, 3)
        self.btn0 = self.create_button(0, 4, 2)

        # Botões de operações
        self.btn_clear = self.create_button("C", 4, 1)
        self.btn_div = self.create_button("/", 1, 4)
        self.btn_mult = self.create_button("*", 2, 4)
        self.btn_sub = self.create_button("-", 3, 4)
        self.btn_add = self.create_button("+", 4, 4)
        self.btn_equal = self.create_button("=", 4, 3)

        self.equation = ""

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 14),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
        return button

    def button_click(self, text):
        if text == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif text == "=":
            result = str(eval(self.equation))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.equation = result
        else:
            self.equation += str(text)
            self.display.insert(tk.END, text)

root = tk.Tk()
my_calculator = Calculadora(root)
root.mainloop()
