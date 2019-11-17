#Hibrido
import os
import re
import argparse
from time import time

parser=argparse.ArgumentParser()
#parser.add_argument( "--file", dest = "file", help = "Archivo a leer")
parser.add_argument( "--dic", dest = "dic" , help = "Archivo con palabras a buscar")
parser.add_argument("--path", dest= "path", help= "Ruta de escritura")
my_args=parser.parse_args()

#Lectura del diccionario y almacenado en lista

palabras=[]
with open(os.path.join(my_args.dic), mode ='r') as dic:
	for line in dic:
		palabras=line.split(',')
		
#print(palabras,len(palabras))

#Lectura del archivo de busqueda
t0=time()
oraciones=[]
extraccion=[]
filenames=[]
contador,escritura=0,0
for path,dirs,files in os.walk(my_args.path):
	for file in files:
		nombre=str(os.path.basename(file))
		print(nombre)
		filenames.append(nombre)
		renom=nombre.replace('.txt','-ext.txt')
		with open(os.path.join(path,file), mode='r', encoding= "utf-8") as file:
			oraciones=(re.split(r'\. [A-Z]', file.read()))
			for palabra in palabras:
				expr=r'[^.]*'+re.escape(palabra)+r'[^.]*\.'
				for oracion in oraciones:
					match=re.search(expr,oracion)
					if match:
						if oracion not in extraccion:
							extraccion.append([palabra, oracion])
		contador=contador+1
	
#Escritura de cada archivo
		if nombre !='iorio_2017.txt' and extraccion:
			with open(os.path.join(my_args.path,renom), mode = 'w',encoding="utf-8" )as oFile:
				for i in extraccion:
					oFile.write(i[0])
					oFile.write(':-\t')
					oFile.write(i[1])
					oFile.write('.\n\n')
			escritura=escritura+1
#Limpieza de la lista
		extraccion.clear()


#print(filenames,len(filenames))
print("Tiempo de ejecucion:",time()-t0)
print("Archivos leidos: ",contador)
print("Archivos escritos: ",escritura)
