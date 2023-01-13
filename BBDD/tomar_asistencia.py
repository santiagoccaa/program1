from tkinter import messagebox
from datetime import datetime
import tkinter as tk
import pymysql

def insertar_asistencia(dato):

	try: 
		conexion = pymysql.connect(
			host='localhost',
			user= 'root',
			passwd='',
			db='call_center')

		cursor=conexion.cursor()
		#------AÑO,MES,DIA-------------
		ymd = datetime.today()
		fecha_entrada = ymd.strftime("%Y-%m-%d")
		#-----HORA
		ahora = datetime.now()
		hora_entrada = ahora.strftime("%H:%M:%S")

		if dato != "":

			cursor.execute("SELECT nombre,cuenta FROM `personal` WHERE cedula={}".format(dato))

			sacar_nom=cursor.fetchone()
			nombre=(sacar_nom[0])
			cuenta=(sacar_nom[1])

			sql="INSERT INTO `asistencia` (nombre,cedula,cuenta,fecha_Ingreso,hora_ingreso) VALUES  (%s,%s,%s,%s,%s)"
			datos=nombre, dato,cuenta, fecha_entrada, hora_entrada

			cursor.execute(sql, datos)

			nom=str(nombre)
			mensaje='Bienvenido '+ str(nom)
			messagebox.showinfo('Aviso',mensaje)

			conexion.close()

		else:
			messagebox.showwarning('Aviso', 'Debes Digitar Correctamente el Numero')	

	except Exception as er:
		print(er)
		messagebox.showwarning('Aviso', 'Debes Digitar Correctamente el Numero')


def insertar_salida(dato):

	try:
		conexion = pymysql.connect(
			host='localhost',
			user= 'root',
			passwd='',
			db='call_center')

		cursor=conexion.cursor()

		despues = datetime.now()
		hora_sal = despues.strftime("%H:%M:%S")

		if dato != "":

			sql="UPDATE asistencia SET hora_salida = %s WHERE cedula=%s"
			data=hora_sal, dato

			cursor.execute(sql, data)

			#----CALCULO DE HORA------------

			sql="SELECT hora_ingreso, nombre FROM asistencia WHERE cedula='{}'".format(dato)
			
			cursor.execute(sql)

			hora_ini=cursor.fetchone()
			valor1=hora_ini[0]
			nombre=hora_ini[1]
			horastr1=str(valor1)

			sql2="SELECT hora_salida FROM asistencia WHERE cedula='{}'".format(dato)

			cursor.execute(sql2)

			hora_end=cursor.fetchone()
			valor2=hora_end[0]
			horastr2=str(valor2)

			formato = "%H:%M:%S"
			h1 = datetime.strptime(horastr1, formato)
			h2 = datetime.strptime(horastr2, formato)
			resultado = h2 - h1

			sql="UPDATE asistencia SET tiempo_laborado = %s WHERE cedula='{}'".format(dato)
			trabajado=resultado

			cursor.execute(sql, trabajado)
			conexion.close()

			nom=str(nombre)
			mensaje='Salida Marcada, '+ str(nom)
			messagebox.showinfo('Aviso',mensaje)

		else:
			messagebox.showwarning('Aviso', 'Debes Digitar Correctamente el Numero')

	except Exception as er:
		messagebox.showwarning('Aviso', 'Debes Digitar Correctamente el Numero')
		print(er)
