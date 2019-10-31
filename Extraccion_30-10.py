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

########################################
##### Obtencion de tabla Compound  #####
########################################

Componentes, compuesto, concentracion =[],[],[]
Componentes=Medio[' ']
Comp_llave={}
llave=1
for elemento in Componentes:
	if elemento not in Comp_llave:
		Comp_llave[elemento]='Comp_'+str(llave)
		llave=llave+1

Medio.pop(' ')
with open(os.path.join(my_args.outputPath,'COMPOUND.txt'), mode="w") as oFile:
	for key in Medio:
		for i in range(0,len(Medio[key])):
				if Medio[key][i]!=" ":
					compuesto.append(Componentes[i])
					concentracion.append(Medio[key][i])								
		#with open(os.path.join(my_args.outputPath,key + '.txt'), mode="w") as oFile:
		llave=1
		for i in range(0,len(compuesto)):
			oFile.write(compuesto[i])
			oFile.write('\t')
			oFile.write(concentracion[i])
			oFile.write('\t')
			oFile.write(str(key))
			oFile.write('\t')
			oFile.write(str(Comp_llave[compuesto[i]]))
			oFile.write('\t')
			oFile.write('1')
			oFile.write('\n')
			llave=llave+1

		compuesto.clear()
		concentracion.clear()

Bacteria.pop(' ')
bac, diversidad, medios=[],[],[]
bac=list(Bacteria.values())
medios=list(Bacteria.keys())

"""
###########################################################################
###			Obtencion de un .txt por bacteria con sus medios    	    ###
###########################################################################

for i in range(0,len(Bacteria.values())):
	for j in range(0,len(Bacteria.values())):
		if i!=j:
			if bac[i]==bac[j]:
				diversidad.append(medios[j])
	diversidad.append(medios[i])
		with open(os.path.join(my_args.outputPath,bac[i] + '.txt'), mode="a") as oFile:
			for m in diversidad:
				oFile.write(m)
				oFile.write('\n')	
	diversidad.clear()



########################################################
#### Obtencion de la tabla LINK formateable por SQL ####
########################################################


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
		oFile.write('BMDM')
		oFile.write('\t')
		oFile.write('1')
		oFile.write('\n')
"""
########################################################
#### Obtencion de la tabla BACTERIA formateable por SQL ####
########################################################

llave=1
Bac_llave={}
for i in bac:
	if i not in Bac_llave:
		Bac_llave[i]='Bac_'+str(llave)
		llave=llave+1

with open(os.path.join(my_args.outputPath, 'BACTERIA.txt'), mode='w') as oFile:
	for i in Bac_llave:
		oFile.write(str(Bac_llave[i]))
		oFile.write('\t')
		oFile.write(str(i))
		oFile.write('\t')
		oFile.write('NA')
		oFile.write('\t')
		oFile.write('NA')
		oFile.write('\t')
		oFile.write('1')
		oFile.write('\n')

########################################################
#### Obtencion de la tabla MEDIUM formateable por SQL ##
########################################################
llave=1
Medio_llave={}
for i in medios:
	if i not in Medio_llave:
		Medio_llave[i]='M_'+str(llave)
		llave=llave+1
print(medios)
print(len(medios))
with open(os.path.join(my_args.outputPath, 'MEDIUM.txt'), mode='w') as oFile:
	for i in Medio_llave:
		oFile.write(str(Medio_llave[i]))
		oFile.write('\t')
		oFile.write(str(i))
		oFile.write('\t')
		oFile.write('1')
		oFile.write('\n')
		
########################################################
#### Obtencion de la tabla MEDIUM-COMPOUND formateable por SQL ##
########################################################

#with open(os.path.join(my_args.outputPath,''))