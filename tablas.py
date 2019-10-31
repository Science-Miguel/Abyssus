
import argparse
import os
####################################################################
##### lee argumento: archivo de entrada en linea de comandos    ####
####################################################################
parseoArgs = argparse.ArgumentParser()

parseoArgs.add_argument(
		"-d", "--dic",
			help="Archivo de entrada medio", required=True)


parseoArgs.add_argument(
		"-f", "--file",
			help="Archivo de entrada componente", required=True)
parseoArgs.add_argument("--outputPath", dest="outputPath", help="Output path to place output files", metavar="PATH")

parseoArgs.add_argument("--outputPath", dest="outputPath", help="Output path to place output files", metavar="PATH")

my_args = parseoArgs.parse_args()



Medio_llave={}
with open(my_args.dic, 'r')as dic:
	for line in dic:
		#line.replace('\n',)
		text=line.split('\t')
		Medio_llave[text[0]]=text[1]


tabla=[]
with open(my_args.file, 'r') as file:
	for line in file:
		tabla=tabla+line.split('\t')
print(tabla)
#for i in range(0,len(tabla))

"""
with open(os.path.join(my_args.outputPath, "ejemplo.txt"), mode='w')as oFile:
	for key in Medio_llave:
			oFile.write(str(Medio_llave[key]))"""
