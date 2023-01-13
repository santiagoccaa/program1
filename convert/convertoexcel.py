import xlsxwriter
from datetime import datetime
import pymysql
from tkinter import messagebox
import os
import errno

def create_table(personal):

    conexion = pymysql.connect(
            host='localhost',
            user= 'root',
            passwd='',
            db='call_center')

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, cedula, cuenta, fecha_Ingreso, hora_ingreso, hora_salida, tiempo_laborado FROM asistencia")

    header = [row[0] for row in cursor.description]

    lista=[]

    for i in cursor.fetchall():

        conver_list= list(i)
        datos="_".join(map(str, conver_list))
        output=datos.split('_')
        tupla=tuple(output)
        lista.append(tupla)
        convertir=tuple(lista)

    conexion.close()

    return header, convertir

def export(personal):

    conexion = pymysql.connect(
            host='localhost',
            user= 'root',
            passwd='',
            db='call_center')

    cursor = conexion.cursor()

    workbook = xlsxwriter.Workbook(personal + '.xlsx')
    worksheet = workbook.add_worksheet('Asistencia')

    header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': '#07BBF6'})
    normal = workbook.add_format({'border': True})

    tarde= workbook.add_format({'border': True, 'bg_color': '#F62807'})
    temprano= workbook.add_format({'border': True, 'bg_color': '#07F612'})

    header, rows = create_table(personal)

    row_index = 0
    column_index = 0 

    for column_name in header:
        worksheet.write(row_index, column_index, column_name, header_cell_format)
        column_index += 1

#-----------OBETENGO VALORES------------------------------
    
    lista1=[]
    lista2=[]

    cursor.execute("SELECT hora_ingreso FROM personal")
    hora_definida=cursor.fetchall()

    cursor.execute("SELECT hora_ingreso FROM asistencia")
    hora_entrada=cursor.fetchall()

    for i in hora_definida:

        conver_list= list(i)
        datos="".join(map(str, conver_list))
        output=datos.split(' ')
        dato="".join(map(str, output))
        validar=dato
        num1=validar.replace(':','')
        hora_d=int(num1)

        lista1.append(hora_d)

    for j in hora_entrada:

        conver_list= list(j)
        datos="".join(map(str, conver_list))
        output=datos.split(' ')
        dato="".join(map(str, output))
        validar=dato
        num2=validar.replace(':','')
        hora_e=int(num2)
        lista2.append(hora_e)

#---------CREAR FILAS Y COLUM EXCEL------------------- 
    row_index += 1

    contador=0

    for row in rows:
        column_index = 0

        for column in row:
            worksheet.write(row_index, column_index, column, normal)

            if column_index==4 and lista1[contador] < lista2[contador]:

                worksheet.write(row_index, column_index, column, tarde)

            elif column_index==4 and lista1[contador] > lista2[contador]:

                worksheet.write(row_index, column_index, column, temprano)
      
            column_index += 1
        contador=contador+1
        row_index += 1

    print(str(row_index) + ' Filas de Excel creadas con Excito: ' + workbook.filename)

    workbook.close()

def crearhoja():

    try:
        os.mkdir('RegistroAsistencia')

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
      
        archivo='Asistencia_'
        ymd = datetime.today()
        fecha = ymd.strftime("%Y-%m-%d")
        name=archivo+fecha

        export('RegistroAsistencia/'+name)

        messagebox.showinfo('Aviso','Asistencia del dia de hoy Tomada')

    except Exception as er:
        messagebox.showwarning('Error', 'La Hoja de Asistencia ya Existe')
        print(er)


          