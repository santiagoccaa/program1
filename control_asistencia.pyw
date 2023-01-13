import tkinter as tk
from tkinter import messagebox
import pymysql

import datetime
import time 
from datetime import date

from Styles import styles 
from BBDD.tomar_asistencia import insertar_asistencia ,insertar_salida

class Asistencia():

	def __init__(self):

		self.root=tk.Tk()

		self.ancho_ventana = 1366
		self.alto_ventana = 768

		self.x_ventana = self.root.winfo_screenwidth() // 2 - self.ancho_ventana // 2
		self.y_ventana = self.root.winfo_screenheight() // 2 - self.alto_ventana // 2

		self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
		self.root.geometry(self.posicion)

		self.root.iconbitmap('img/icono.ico')
		self.root.resizable(0,0)
		self.root.title("Asistencia")
		self.root.config(bg="#FFFFFF")

		self.img=tk.PhotoImage(file="img/img.png")
		self.lb_img=tk.Label(self.root, image = self.img, bg='#FFFFFF').place(x=80,y=50)

		self.lado=tk.PhotoImage(file="img/prueba4.png")
		self.lb_img=tk.Label(self.root, image = self.lado, bg='#FFFFFF').place(x=1050,y=170)

#-----------FECHA Y HORA-------------------

		self.hora=tk.Label(text="", **styles.STYLE_LABEL, pady=10, padx=10)
		self.fecha=tk.Label(text="", **styles.STYLE_LABEL, pady=10, padx=10)

		self.hora.configure(font=('Poppins 25 italic'), bg='#FFFFFF', fg='#239CF4')
		self.hora.place(x=130, y=545)
		self.fecha.configure(font=('Poppins 25 italic'), bg='#FFFFFF', fg='#239CF4')
		self.fecha.place(x=80, y=500)
		self.update_clock()
		self.get_date()

		#-----NOMBRE EMPRESA------------

		self.ide=tk.Label(self.root, 
			text='READY TO ANSWER',
			 font=('Poppins 30 italic bold'),
			 bg='#FFFFFF', fg='#149CFA').place(x=690, y=60)

		self.ide=tk.Label(self.root, 
			text='CONTACT CENTER',
			 font=('Poppins 15 italic bold'),
			 bg='#FFFFFF', fg='#767676').place(x=790, y=110)

		#---------TITULO-------------

		self.ide=tk.Label(self.root, 
			text='Ingrese su ID de Empleado',
			 font=('Poppins 27 italic'),
			 bg='#FFFFFF', fg='#202020').place(x=680, y=210)

		self.cedula=tk.StringVar()

		#----------CAJA DE TEXTO-------------------

		self.dig_ID=tk.Entry(
			self.root,
			**styles.STYLE_Entry, 
			justify=tk.CENTER,
			width=27,
			textvar=self.cedula).place(x=650, y=280)

		def entrada(cod):
			try:
				conexion = pymysql.connect(
					host='localhost',
					user= 'root',
					passwd='',
					db='call_center')

				cursor=conexion.cursor()

				owo =date.today()
				d3=owo.strftime("%Y-%m-%d")
				sacada=str(d3)

				sql1="SELECT nacimiento FROM personal WHERE nacimiento='{}'".format(sacada)

				cursor.execute(sql1)
				cumple=cursor.fetchall()

				con=0
				X=260
				Y=620
				for i in cumple:

					tupla=cumple[con]

					valor=tupla[0]

					fech=str(valor)

					sql2="SELECT nombre FROM personal WHERE nacimiento='{}'".format(sacada)

					cursor.execute(sql2)
					nombre=cursor.fetchall()

					nom=nombre[con]
					v_nom=nom[0]

					strr=str(v_nom)
					mensaje="¡¡Ready To Answer Te Desea Un Feliz Cumpleaños " + strr + "¡¡"

					if fech==sacada:
						tk.Label(self.root, 
							text=mensaje,
							font=('Poppins 20 italic bold')
							,bg='#FFFFFF', fg='#ED42F5').place(x=X, y=Y)
					con=con+1
					Y=Y+44
			except Exception as er:
				print(er)

			insertar_asistencia(cod)

			self.cedula.set('')

		def salida():

			insertar_salida(self.cedula.get())

			self.cedula.set('')


#-----------BOTON---------------------

		self.boton=tk.Button(self.root,text='Marcar Entrada',**styles.STYLE_Boton ,bd=1, 
			command=lambda:entrada(self.cedula.get()),width=25).place(x=750, y=400)

		self.boton=tk.Button(self.root,text='Marcar Salida',**styles.STYLE_Boton ,bd=1, 
			command=lambda:salida(),width=25).place(x=750, y=490)

		self.root.mainloop()

	def update_clock(self):
		now=time.strftime("%I:%M:%S %p")
		self.hora.configure(text=now)
		self.root.after(1000, self.update_clock)

	def get_date(self):

		fecha=datetime.datetime.now()
		diaSemana=fecha.strftime("%A")

		dia =date.today()
		d1=dia.strftime("%d-%m-%Y")
		self.fecha.configure(text=d1 +  ' | ' + diaSemana)

if __name__ == '__main__':
	Asistencia()