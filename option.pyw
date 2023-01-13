from tkinter import messagebox
import tkinter as tk
import pymysql

from BBDD.crearBBDD import *
from convert.convertoexcel import crearhoja


class AdministracionDB():

	def __init__(self):

		self.root=tk.Tk()

		self.ancho_ventana = 400
		self.alto_ventana = 480

		self.x_ventana = self.root.winfo_screenwidth() // 2 - self.ancho_ventana // 2
		self.y_ventana = self.root.winfo_screenheight() // 2 - self.alto_ventana // 2

		self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
		self.root.geometry(self.posicion)

		self.root.iconbitmap('img/logoConfig.ico')
		self.root.resizable(0,0)
		self.root.title("Administracion")
		self.root.config(bg="#F0F0F0")

		self.img=tk.PhotoImage(file="img/img.png")
		self.lb_img=tk.Label(self.root, image = self.img).pack()

#-----------BOTONES---------------------
		'''
		self.boton=tk.Button(
			self.root, text='Crear Base de Datos', 
			font=('Poppins 15 bold'),
			bd=4, 
			command=crearDB, bg='#43C5FE', fg='#FFFFFF').pack(pady=5)
		'''
		self.boton=tk.Button(
			self.root, text='Tomar Asistencia',
			font=('Poppins 15 bold'),
			bd=4, 
			command=crearhoja, bg='#43C5FE', fg='#FFFFFF').pack(pady=5)

		self.boton=tk.Button(
			self.root, text=' Crear Tabla de Asistencia ',
			font=('Poppins 15 bold'),
			bd=4, 
			command=creartabla, bg='#43C5FE', fg='#FFFFFF').pack(pady=5)
	
		self.root.mainloop()

main=AdministracionDB()