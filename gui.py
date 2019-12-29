#-*- coding:utf-8 -*-

"""
	Interfaz grafica de la aplicacion, usa Tkinter.
			by: c0der
"""

import sys
from Tkinter import *
import tkMessageBox
from peaje import *


def registro(obj_placa, obj_fecha):
	""" Registrar placa del vehiculo y fecha """
	placa = obj_placa.get()
	fecha = obj_fecha.get()
	if placa != '' and fecha != '':
		try:
			anio, mes, dia = fecha.split('-')
			if int(mes) <= 12 and int(dia) <= 30:
				registrar_vehiculo(placa, anio, mes, dia)
				obj_placa.delete(0, 10)
				obj_fecha.delete(0, 10)
				tkMessageBox.showinfo("Notificacion", "Nuevo vehiculo registrado")
			else:
				tkMessageBox.showwarning("Error", "Fecha no valida (AAAA-MM-DD)")	
		except ValueError:
			tkMessageBox.showwarning("Error", "Ocurrio un error por favor use el formato (AAAA-MM-DD)")
	else:
		tkMessageBox.showwarning("Error", "Campos vacios!")

def estadistica(text):
	""" Mostrar la estadistica en el campo text """
	text.insert(END, generar_estadistica())

def borrar_registros(text):
	""" Borrar registros ingresados por el usuario """
	eliminar_registro_vehiculos()
	text.delete('1.0', 'end')


class Gui(Frame):
	""" Interfaz grafica / Peaje App """

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("SECRETARIA DE TRANSPORTE")
		self.pack(fill=BOTH, expand=True)

		frame1 = Frame(self)
		frame1.pack(fill=X)

		lbl_placa = Label(frame1, text="N° Placa", width=6)
		lbl_placa.pack(side=LEFT, padx=5, pady=5)

		entry_placa = Entry(frame1)
		entry_placa.pack(fill=X, padx=5, expand=True)

		frame2 = Frame(self)
		frame2.pack(fill=X)

		lbl_fecha = Label(frame2, text="Fecha (AAAA-MM-DD)", width=16)
		lbl_fecha.pack(side=LEFT, padx=5, pady=5)

		entry_fecha = Entry(frame2)
		entry_fecha.pack(fill=X, padx=5, expand=True)

		frame3 = Frame(self)
		frame3.pack(fill=X)

		btn_registrar = Button(frame3, text="Registrar", command=lambda:registro(entry_placa,
																				 entry_fecha))
		btn_registrar.pack(side=LEFT, padx=5, pady=5)

		btn_estadistica = Button(frame3, text="Estadistica", command=lambda: estadistica(txt))
		btn_estadistica.pack(side=LEFT, padx=5, pady=5)

		btn_borrar = Button(frame3, text="Borrar datos", command=lambda: borrar_registros(txt))
		btn_borrar.pack(side=LEFT, padx=5, pady=5)
		
		frame4 = Frame(self)
		frame4.pack(fill=BOTH, expand=True)
		txt = Text(frame4)
		txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():
	""" Iniciar programa """
	root = Tk()
	root.geometry("300x300")
	app = Gui(root)
	root.mainloop()

if __name__ == '__main__':
	main()

