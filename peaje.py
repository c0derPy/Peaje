#-*- coding: utf-8 -*-

"""
	Algoritmo que permite obtener el promedio por mes 
	de vehiculos que pasan por un peaje en el año, 
	ademas permite conocer cual fue el mes en el que 
	pasaron mayor cantidad de vehiculos.
			by:<c0der>
	
"""

from collections import defaultdict
from collections import Counter 
from math import floor

# Meses
meses = {'01': 'Enero', '02': 'Febrero', '03':'Marzo',
		 '04': 'Abril', '05': 'Mayo', '06': 'Junio',
		 '07': 'Julio', '08': 'Agosto', '09': 'Septiembre',
		 '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}

# Diccionario que contiene el registro de la informacion
# Se inicializa por defecto para contener una lista(arreglo)
registro = defaultdict(list)

def registrar_vehiculo(placa, anio, mes, dia):
	""" Registrar placa del vehiculo y la fecha """
	if placa != '' and anio != '' and mes != '' and dia != '':
		registro[anio].append((placa, mes))
	else:
		print 'No se pudo realizar el registro'

def get_num_vehiculos_mes(placa_mes):
	""" Obtener el numero de vehiculos que han pasado cada mes"""
	num_meses = []
	for dato in placa_mes:
		num_meses.append(dato[1])
	vehiculos_por_mes = Counter(num_meses)	
	return vehiculos_por_mes

def ver_cantidad_vehiculos_por_mes(anio, num_vehiculos_por_mes):
	""" Muestra el mes con la cantidad de vehiculos 
		que transitaron """

	reporte = ''	
	for mes, cantidad in num_vehiculos_por_mes.items():
		num_mes = mes if len(mes) == 2 else '0'+mes
		reporte += '%d\t %s\t%s\n' % (cantidad, anio, meses[num_mes]) 
	return reporte

def mes_mas_transitado(num_vehiculos_por_mes):
	""" Obtiene el mes mas transitado (Mes donde pasaron
	 mayor cantidad de vehiculos) """
	mes_transitado = num_vehiculos_por_mes.most_common(1)[0]
	mes = mes_transitado[0]
	cantidad = mes_transitado[1]
	return (meses[mes], cantidad)

def promedio_vehiculos_por_mes(num_vehiculos_por_mes):
	""" Obtiene el promedio por mes de vehiculos que 
	    transitaron en el año"""

	num_meses = len(num_vehiculos_por_mes)
	total_vehiculos = sum(num_vehiculos_por_mes.values())
	promedio = float(total_vehiculos) / float(num_meses)
	return floor(promedio) 

def generar_estadistica():
	""" Genera la estadistica """

	titulo = 'ESTADISTICA DE TRANSPORTE'
	estadistica = titulo.center(40, '=') + "\n"
	for anio, placa_mes in registro.items():
		estadistica += 'VEHICULOS\tAÑO\tMES\n'
		num_vehiculos_mes = get_num_vehiculos_mes(placa_mes)
		estadistica += ver_cantidad_vehiculos_por_mes(anio,num_vehiculos_mes)
		estadistica += '\n[+]Mes mas transitado: %s, %d vehiculos.' % mes_mas_transitado(num_vehiculos_mes)
		estadistica += '\n[+]Transitaron un promedio de %d vehiculos por mes en el año %s.\n' % (promedio_vehiculos_por_mes(num_vehiculos_mes), anio)
		estadistica += '-------------------------------\n'

	return estadistica

def eliminar_registro_vehiculos():
	""" Eliminar registros """
	global registro
	registro = defaultdict(list)

if __name__ == '__main__':
	registrar_vehiculo('BVC-123', '2016', '01', '12')
	registrar_vehiculo('BVC-123', '2016', '12', '04')
	registrar_vehiculo('BVC-123', '2016', '03', '05')
	registrar_vehiculo('BVC-125', '2016', '03', '09')
	print generar_estadistica()
