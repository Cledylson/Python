import tkinter as tk
import time

# Configuração da janela
window = tk.Tk()
window.title("Relógio")

# Função que atualiza o relógio a cada segundo
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Configuração do rótulo do relógio
clock_label = tk.Label(window, font=('Arial', 80), bg='white', fg='black')
clock_label.pack(pady=20)

# Inicialização do relógio
update_clock()

# Execução da janela
window.mainloop()
