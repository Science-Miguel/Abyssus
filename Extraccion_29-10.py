import re
import argparse
import os
####################################################################
##### lee argumento: archivo de entrada en linea de comandos    ####
####################################################################
parseoArgs = argparse.ArgumentParser()
parseoArgs.add_argument(
		"-u", "--usage",
			help = "Usage  template_readFile_with_v1.0.py [-f] InFile.txt",
			action="store_true")

parseoArgs.add_argument(
		"-f", "--file",
			help="Archivo de entrada en formato texto", required=True)

parseoArgs.add_argument("--outputPath", dest="outputPath", help="Output path to place output files", metavar="PATH")

my_args = parseoArgs.parse_args()


###################################################################
##### Apertura y lectura de archivos, con with                 ####
####################################################################

Medio, Bacteria = {},{}
pubid=[]
with open(my_args.file, 'r') as file:
	for line in file:
		line = re.sub(',',', ', line)
		match = re.findall(r'\,([^\n|\r|\,]+)', line)
		if match:
			Medio[match[0]] = match[4:]
			Bacteria[match[0]] = match[2]
			pubid.append(match[1])

######################################################################################################
##### Obtencion de un .txt con nombre del Medio que contenga los compuestos en su concentracion  #####
######################################################################################################

Componentes, compuesto, concentracion =[],[],[]
Componentes=Medio[' ']
Medio.pop(' ')
#for key in Medio:
#	for i in range(0,len(Medio[key])):
#			if Medio[key][i]!=" ":
#					compuesto.append(Componentes[i])
#					concentracion.append(Medio[key][i])								
#	with open(os.path.join(my_args.outputPath,key + '.txt'), mode="a") as oFile:
#			for i in range(0,len(compuesto)):
#					oFile.write(compuesto[i])
#					oFile.write('\t')
#					oFile.write(concentracion[i])
#					oFile.write('\n')
#	compuesto.clear()
#	concentracion.clear()


###########################################################################
###			Obtenicion de un .txt por bacteria con sus medios    	    ###
###########################################################################

#bac, diversidad, medios=[],[],[]
#bac=list(Bacteria.values())
#medios=list(Bacteria.keys())
#for i in range(0,len(Bacteria.values())):
#	for j in range(0,len(Bacteria.values())):
#		if i!=j:
#			if bac[i]==bac[j]:
#				diversidad.append(medios[j])
	#diversidad.append(medios[i])
	#	with open(os.path.join(my_args.outputPath,bac[i] + '.txt'), mode="a") as oFile:
	#		for m in diversidad:
	#			oFile.write(m)
	#			oFile.write('\n')	
	#diversidad.clear()



########################################################
#### Obtencion de la tabla LINK formateable por SQL ####
########################################################

Bacteria.pop(' ')
casa, inquilino=[],[]
for m in Bacteria:
	casa.append(Bacteria[m])
	inquilino.append(m)
llave=1
with open(os.path.join(my_args.outputPath, 'BACTERIA_MEDIUM_DOCS_LINK.txt'), mode='w') as oFile:
	oFile.write("MEDIO\tBACTERIA\tPUBID\tLLAVE\tESTADO\n")
	for i in range(0,len(casa)):
		oFile.write(casa[i])
		oFile.write('\t')
		oFile.write(inquilino[i])
		oFile.write('\t')
		oFile.write(pubid[i])
		oFile.write('\t')
		oFile.write('BMDM'+str(llave))
		oFile.write('\t')
		oFile.write('1')
		oFile.write('\n')
		llave=llave+1


with open(os.path.join(my_args.outputPath, 'Bacterias.csv'), mode='a') as oFile:
	for i in bac:
		oFile.write(str(i)+',')