from tkinter import*
import mysql.connector
from tkinter import messagebox

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '815878330000',
        database = 'lunch_restaurante'
    )

except Exception as error:
    messagebox.showwarning('Sem conexão',error)


class Restaurante:

    def __init__(self):

        self.window = Tk()
        self.window.title("Login")
        self.window.resizable(0,0)
        self.window.geometry("900x600+220+80")
        self.window.config(bg='white')
        
        global usuario
        global senha

        usuario = StringVar()
        senha = StringVar()
        
        
        self.cor_frameLeft = '#e9f4f7'
        self.cor_verde = '#568274'
        self.logo = PhotoImage(file='assets/logo1.png')
        self.logo2 = PhotoImage(file='assets/logo2.png')

        self.frame_Left = Frame(self.window, bg = self.cor_frameLeft,width=450, height=450).place(x=50,y= 80)
        
        
        self.label_logo2 = Label(self.window, image=self.logo2,bg='white').place(x=370, y = 0.1, width= 80, height=80)
        self.label_logoPerson = Label(self.window, image=self.logo,bg='white').place(x=400, y = 5)

        self.label_logo3 = Label(self.window, image=self.logo2,bg='white').place(x=500, y = 0.1, width= 80, height=80)
              
        self.label_login = Label(self.frame_Left, text ='L o g i n',font='arial 25 bold',
                                    bg =self.cor_frameLeft,fg=self.cor_verde).place(x=160, y = 140)        
        
        self.label_usuario = Label(self.frame_Left, text = 'Usuário', font ='Modric 10',
                                    bg=self.cor_frameLeft,fg=self.cor_verde).place(x=100, y=220)

        self.entry_usuario = Entry(self.frame_Left, bg=self.cor_frameLeft, bd=0, textvariable=usuario)
        self.entry_usuario.place(x=100, y = 240, width=260, height=20)
        self.frame_usuario = Frame(self.frame_Left, bg = self.cor_verde).place(x=100, y = 260, width =260, height =2)
        
        self.label_senha = Label(self.frame_Left, text ='Senha:', font ='Arial 10 ',
                                bg=self.cor_frameLeft,fg=self.cor_verde).place(x=100, y = 290)

        self.entry_senha = Entry(self.frame_Left, bg=self.cor_frameLeft, bd=0,textvariable=senha, show='*')
        self.entry_senha.place(x=100, y = 310, width=260, height=20)
        self.frame_senha = Frame(self.frame_Left, bg = self.cor_verde).place(x=100, y = 330, width =260, height =2)
        
        
        self.label_top = Label(self.frame_Left, text = 'O r i e n t a l',font='Arial 20 bold',
                                    bg='white',fg='black').place(x=400, y=20)
        
        self.bottao_entrar = Button(self.frame_Left, text ='Entrar', bg='yellow',fg='black',
                                    font='arial 15 bold', command=self.logs)
        self.bottao_entrar.place(x=100, y = 360,width=260,height=60)
        
        self.window.mainloop()


   
    
    def logs(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM lunch_restaurante.login WHERE BINARY usuario='%s'AND BINARY senha='%s'" % (usuario.get(), senha.get())
        mycursor.execute(sql)

        try:

            if mycursor.fetchone():
                msg = messagebox.showinfo('Mysql',' Usuário Autenticado !')               
                
                if usuario.get() =='paulo' and senha.get() =='1234':                   
                    messagebox.showinfo('Mysql','Logado como ADM ! ')
                    self.window.destroy()
                    
                    
                
                elif msg == 'ok':
                    self.window.destroy()                
                                       
            elif usuario.get() == '' or senha.get() == '':
                messagebox.showerror('Mysql','Usuario ou Senha inválidos')        
                        
            else:
                messagebox.showerror('MySql','Usuário ou Senha inválidos !')
        
        
        except Exception as error:
                    messagebox.showwarning('Error', error)





app = Restaurante()