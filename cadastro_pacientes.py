import tkinter as tk
from tkinter import ttk


dados = 1
class Tela:
    def __init__(self,master):
        self.nossaTela = master
        self.nossaTela.title("Cadastro de Pacientes")
        self.titulo = tk.Label(self.nossaTela, text="Cadastro de PACIENTES")
        self.entrada_nome1 = tk.Label(self.nossaTela, text="Nome: ")
        self.entrada_email1 = tk.Label(self.nossaTela, text="Email: ")
        self.entrada_cpf1 = tk.Label(self.nossaTela, text="CPF: " )
        self.entrada_rg1 = tk.Label(self.nossaTela, text="RG: " )
        self.entrada_tel1 = tk.Label(self.nossaTela, text="Telefone: " )
        self.entrada_data1 = tk.Label(self.nossaTela, text="Data de Nascimento: " )
        self.entrada_nome = tk.Entry(self.nossaTela, background="light gray")
        self.entrada_email = tk.Entry(self.nossaTela, background="light gray")
        self.entrada_cpf = tk.Entry(self.nossaTela, background="light gray" )
        self.entrada_rg = tk.Entry(self.nossaTela, background="light gray" )
        self.entrada_tel = tk.Entry(self.nossaTela, background="light gray" )
        self.entrada_data = tk.Entry(self.nossaTela, background="light gray" )
        self.salvar = tk.Button(self.nossaTela, text="Salvar" , command=self.cadastro)
        self.sair = tk.Button(self.nossaTela, text="Sair", command=janelaRaiz.quit)
        self.salvar["font"] = ("Verdana", 10)
        self.sair["font"] = ("Verdana", 10)
        self.titulo["font"] = ("Verdana", 10)
        self.entrada_cpf["font"] = ("Verdana", 10)
        self.entrada_data["font"] = ("Verdana", 10)
        self.entrada_email["font"] = ("Verdana", 10)
        self.entrada_nome["font"] = ("Verdana", 10)
        self.entrada_rg["font"] = ("Verdana", 10)
        self.entrada_tel["font"] = ("Verdana", 10)
        self.entrada_nome.place(x=120 , y=60)
        self.entrada_email.place(x=120 , y=80)
        self.entrada_cpf.place(x = 120, y= 100)
        self.entrada_rg.place(x = 120 , y=120)
        self.entrada_tel.place(x= 120 , y= 140)
        self.entrada_data.place(x= 120, y=160)
        self.entrada_nome1.place(x=5 , y=60)
        self.entrada_email1.place(x=5 , y=80)
        self.entrada_cpf1.place(x = 5, y= 100)
        self.entrada_rg1.place(x = 5 , y=120)
        self.entrada_tel1.place(x= 5, y= 140)
        self.entrada_data1.place(x= 5, y=160)
        self.titulo.place(x=60, y= 10)
        self.salvar.place(x=110,y=220)
        self.sair.place(x=160, y= 220)
    
    def cadastro(self):
        nome = self.entrada_nome.get()
        email = self.entrada_email.get() 
        cpf = self.entrada_cpf.get() 
        rg = self.entrada_rg.get() 
        tel = self.entrada_tel.get() 
        data =self.entrada_data.get()
        a = data
        a = a[6:10]
        idade = int(a)
        idade = 2023 - idade
        data = idade
        global dados 
        dados = {"Nome" : [nome] , "Email": [email], "CPF" : [cpf], "RG" : [rg] , "Telefone": [tel] , "Idade" : [idade] }
        with open('./clinica_pacientes.txt', 'a') as arquivo_cadastro:
            for key, value in dados.items():
                arquivo_cadastro.write('%s:%s\n' % (key, value))
        
        if idade > 65:
            return Tela.base_date_risk(1)
        else:
            return Tela.base_date(1)  

    def base_date(self):
        janela2 = tk.Toplevel()
        janela = tk.Toplevel() 
        janela.title("Dados Salvos com Sucesso")
        janela2.title("Dados para conferir") 
        texto = tk.Label (janela, text='Esse paciente é considerado fora do grupo de risco' )
        bt = tk.Button(janela, text="OK" , command=Tela(janelaRaiz))
        bt = tk.Button(janela, text="OK" , command=janela.destroy)          
       
        texto.pack()
        bt.pack()
        
        


    def base_date_risk(self):
        janela2 = tk.Toplevel()
        janela = tk.Toplevel()
        janela2.title("Dados para conferir") 
        janela.title("Dados Salvos com Sucesso")
        texto = tk.Label(janela , text='Esse paciente é considerado fora do grupo de risco')
        bt = tk.Button(janela, text="OK" , command=Tela(janelaRaiz))
        bt = tk.Button(janela, text="OK" , command=janela.destroy)    
        texto.pack()
        bt.pack()
        
        
        



janelaRaiz = tk.Tk()
janelaRaiz.geometry("295x320")
Tela(janelaRaiz)

janelaRaiz.mainloop()
