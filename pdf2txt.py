# Analizador de pdf
import argparse
import os
import pdftotext

####################################################################
##### lee argumento: archivo de entrada en linea de comandos    ####
####################################################################
parseoArgs = argparse.ArgumentParser()
parseoArgs.add_argument(
		"-f", "--file",
			help="Archivo de entrada en formato texto", required=True)

my_args = parseoArgs.parse_args()

# Load your PDF
with open(my_args.file , "rb") as f:
    pdf = pdftotext.PDF(f)

# Save all text to a txt file.
with open('output.txt', 'w') as s:
    s.write("\n\n".join(pdf))