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

with open(my_args.file, 'r') as file:
	for line in file:
		line = re.sub(',',', ', line)
		match = re.findall(r'\,([^\n|\r|\,]+)', line)
		if match:
			Medio[match[0]] = match[4:]
			Bacteria[match[2]]= match[4:]
print(Medio,Bacteria)