#Integrante:Jonathan Elias Gamez Larin
#Hacemos uso del módulo smtplib
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk, Entry, Label, Button, messagebox


#Creamos la ventana con su respectivo tamaño
vent= Tk()
vent.geometry("500x400")
vent.configure(bg='#25A18E')
vent.title('Enviar Un Correo!')



def Send():

    Sender = 'eliaslarin@gmail.com'
    Destinatario = (input1.get())
    User = (input2.get())
 

    # Se Crea El Objeto Del Mensaje
    mensaje = MIMEMultipart()
     
    #Se Crea El Modelo Del Mensaje 
    mensaje_html="""

    <!DOCYPE html>
    <html>
    <body>
    <h1> Hola {}</h1>
    <p>{}</p>
    </body>
    </html>

    """
 
    # Se crean los atributos para el mensaje
    mensaje['From'] = Sender

    mensaje['To'] = Destinatario

    mensaje['Subject'] = 'Mensaje Automatico'
    
    Body = (input3.get())
    mensaje.attach(MIMEText(mensaje_html.format(User,Body), 'html'))
    # Se crea la conexion con el servidor
    sesion_smtp= smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    # Se inicia la sesion con el servidor
    sesion_smtp.login('eliaslarin@gmail.com','bmajyxdlqiorimtm')
    texto= mensaje.as_string()
    sesion_smtp.sendmail(Sender, Destinatario, texto)
 
    # Con esta funcion cerramos la conexion
    sesion_smtp.quit()
    text= "!Se logro enviar el correo!"

    messagebox.showinfo(title="Enviar", message=str(text))

labl1=Label(vent, bg = "#118AB2",text="Enviar a:")
input1=Entry(vent)
labl2=Label(vent,bg = "#06D6A0", text="Usuario:")
input2=Entry(vent)
labl3=Label(vent, bg = "#05F140",text="Cuerpo de su mensaje:")
input3=Entry(vent)
btn1 = Button(vent,text="Enviar",command=Send)


#Aqui podemos ajustar las posiciones
labl1.place(x=80, y=20)
input1.place(x=150, y=20)
labl2.place(x=80, y=60)
input2.place(x=150, y=60)
labl3.place(x=20, y=100)
input3.place(x=150, y=100, relwidth=0.6,relheight=0.4)
btn1.place(x=400, y=280)
vent.mainloop()